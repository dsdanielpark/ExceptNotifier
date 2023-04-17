import requests
import traceback
import re
import datetime
from email.message import EmailMessage
import sys
import pickle
from twilio.rest import Client

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class ExceptSMS(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __call__(etype, value, tb):
        excType = re.sub('(<(type|class \')|\'exceptions.|\'>|__main__.)', '', str(etype)).strip()
        start_time = datetime.datetime.now()
        
        exceptNotifier = {'SUBJECT':'[Except Notifier] ** Error! ** Python Code Exception Detected', 'BODY':f'\n\nIMPORTANT WARNING \nPython Exception Detected in Your Code. \n\nHi there, \nThis is an exception catch notifier. \n\n - Code Status: Fail. \n - Detail: Python Code Ran Exceptions. \n - Time: {start_time.strftime(DATE_FORMAT)} \n\n :no_entry: {excType}: %{etype.__doc__}\n\n {value} \n\n'}
        for line in traceback.extract_tb(tb):
            exceptNotifier['BODY'] += '\tFile: "%s"\n\t\t%s %s: %s\n' % (line[0], line[2], line[1], line[3])
        while 1:
            if not tb.tb_next: break
            tb = tb.tb_next
        stack = []
        f = tb.tb_frame
        while f:
            stack.append(f)
            f = f.f_back
        stack.reverse()
        
        
        exceptNotifier['BODY'] += '\nLocals by frame, innermost last::::'
        for frame in stack:
            exceptNotifier['BODY'] += '\nFrame %s in %s at line %s' % (frame.f_code.co_name, frame.f_code.co_filename, frame.f_lineno)
            for key, val in frame.f_locals.items():
                exceptNotifier['BODY'] += '\n\t%20s = ' % key
                try:
                    exceptNotifier['BODY'] += str(val)
                except:
                    exceptNotifier['BODY'] += '<ERROR WHILE PRINTING VALUE>'
                    
        
        data = {'text':exceptNotifier['SUBJECT']+exceptNotifier['BODY']}

        client = Client(SID, TOKEN)
        client.messages.create(
                                to=TO,
                                from_=FROM,  
                                body=data['text'][:1500]
                                )


    @staticmethod
    def send_sms_msg(SID, TOKEN, FROM, TO, msg):
        client = Client(SID, TOKEN)
        client.messages.create(
            to=TO,
            from_=FROM,  
        body=msg
    )



class SuccessSMS:
    def __init__(self) -> None:
        pass
        
    def __call__(self, *args, **kwds) -> None:
        exceptNotifier = EmailMessage()
        start_time = datetime.datetime.now()
        f'Time Stamp: {start_time.strftime(DATE_FORMAT)}'
        exceptNotifier = {"SUBJECT":"[Success Notifier] ** Success! ** Python Code Executed Successfully"}
        exceptNotifier["BODY"]=f"\n\nHi there, \nThis is a success notifier.\n\n - Code Status: Success. \n - Detail: Python Code Ran Without Exceptions. \n - Time: {start_time.strftime(DATE_FORMAT)} \n\nI just wanted to let you know that your Python code has run successfully without any exceptions. \n\nAll the best, \nExcept Notifier https://github.com/dsdanielpark/ExceptNotifier"
        
        data = {'text':exceptNotifier['SUBJECT']+exceptNotifier["BODY"]}
        
        client = Client(SID, TOKEN)
        client.messages.create(
                                to=TO,
                                from_=FROM,  
                                body=data['text'][:1500]
                                )

class SendSMS:
    def __init__(self) -> None:
        pass
        
    def __call__(self, *args, **kwds) -> None:
        exceptNotifier = EmailMessage()
        start_time = datetime.datetime.now()
        f'Time Stamp: {start_time.strftime(DATE_FORMAT)}'
        exceptNotifier = {"SUBJECT":"[Codeline Notifier] ** Notice! ** Code Execution Reached Specified Line"}
        exceptNotifier["BODY"] = f"\n\nHi there, \nThis is a customized notifier.\n\n- Code Status: Done. \n- Detail: Code Execution Reached Specified Line.  \n- Time: {start_time.strftime(DATE_FORMAT)} \n\nThe code has reached the line where you requested an email to be sent. As per your instruction, we are sending this email. \n\nAll the best, \nExcept Notifier https://github.com/dsdanielpark/ExceptNotifier"
        
        data = {'text':exceptNotifier['SUBJECT']+exceptNotifier["BODY"]}
        
        client = Client(SID, TOKEN)
        client.messages.create(
                                to=TO,
                                from_=FROM,  
                                body=data['text'][:1500]
                                )

if __name__ == "__main__":
    
    """https://www.twilio.com/en-us"""

    global SID, TWILIO_AUTH_TOKEN, FROM, TO
    SID = 'xxxx'
    TOKEN = 'yyyy'
    client = Client(SID, TOKEN)

    TO="+zzzz",
    FROM="+aaaa",  
    
    sys.excepthook = ExceptSMS.__call__

    try:
        print(1/10)  
        SuccessSMS().__call__() #1 success sender          

    except ExceptSMS as e:      #2 except sender    
        with open("exceptError.pickle", "wb") as f:
            pickle.dump(e, f)
        raise pickle.load(f)
        sys.exit()
    
    SendSMS().__call__()        #3 customized sender          