import traceback
import re
import datetime
from email.message import EmailMessage
import sys
import urllib3
import json

http = urllib3.PoolManager()
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

class ExceptChime(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __call__(etype, value, tb):
        """Override excepthook to send error message to AWS Chime.

        :param etype: Error Type
        :type etype: _type_
        :param value: Error Value
        :type value: _type_
        :param tb: Traceback Information
        :type tb: _type_
        """
        excType = re.sub('(<(type|class \')|\'exceptions.|\'>|__main__.)', '', str(etype)).strip()
        start_time = datetime.datetime.now()
        
        exceptNotifier = {'SUBJECT':'[Except Notifier] :warning: Error! Python Code Exception Detected', 'BODY':f'\n\nIMPORTANT WARNING \nPython Exception Detected in Your Code. \n\nHi there, \nThis is an exception catch notifier. \n\n - :x: Code Status: Fail. \n - :x: Detail: Python Code Ran Exceptions. \n - :clock2: Time: {start_time.strftime(DATE_FORMAT)} \n\n :no_entry: {excType}: %{etype.__doc__}\n\n {value} \n\n'}
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

        message = {"Content": data['text']}
        encoded_msg = json.dumps(message).encode("utf-8")
        resp = http.request("POST", URL, body=encoded_msg)



    @staticmethod
    def send_chime_msg(URL: str, msg: str) -> dict:
        """Send message to chat room through chime app's webhook url.

        :param URL: Webhook url from chime app
        :type URL: str
        :param msg: Message text
        :type msg: str
        :return: Response according to REST API request
        :rtype: dict
        """

        url = URL
        message = {"Content": msg}
        encoded_msg = json.dumps(message).encode("utf-8")
        resp = http.request("POST", url, body=encoded_msg)

        return resp



class SuccessChime:
    def __init__(self) -> None:
        pass
        
    def __call__(self, *args, **kwds) -> None:
        exceptNotifier = EmailMessage()
        start_time = datetime.datetime.now()
        f'Time Stamp: {start_time.strftime(DATE_FORMAT)}'
        exceptNotifier = {"SUBJECT":"[Success Notifier] :tada: Success! Python Code Executed Successfully"}
        exceptNotifier["BODY"]=f"\n\nHi there, \nThis is a success notifier.\n\n - :white_check_mark: Code Status: Success. \n - :white_check_mark: Detail: Python Code Ran Without Exceptions. \n - :clock2: Time: {start_time.strftime(DATE_FORMAT)} \n\nI just wanted to let you know that your Python code has run successfully without any exceptions. \n\nAll the best, \nExcept Notifier https://github.com/dsdanielpark/ExceptNotifier"
        
        data = {'text':exceptNotifier['SUBJECT']+exceptNotifier["BODY"]}
        message = {"Content": data['text']}
        encoded_msg = json.dumps(message).encode("utf-8")
        resp = http.request("POST", URL, body=encoded_msg)



class SendChime:
    def __init__(self) -> None:
        pass
        
    def __call__(self, *args, **kwds) -> None:
        exceptNotifier = EmailMessage()
        start_time = datetime.datetime.now()
        f'Time Stamp: {start_time.strftime(DATE_FORMAT)}'
        exceptNotifier = {"SUBJECT":"[Codeline Notifier] :clap: Notice! Code Execution Reached Specified Line"}
        exceptNotifier["BODY"] = f"\n\nHi there, \nThis is a customized notifier.\n\n- :white_check_mark: Code Status: Done. \n- :white_check_mark: Detail: Code Execution Reached Specified Line.  \n- :clock2: Time: {start_time.strftime(DATE_FORMAT)} \n\nThe code has reached the line where you requested an email to be sent. As per your instruction, we are sending this email. \n\nAll the best, \nExcept Notifier https://github.com/dsdanielpark/ExceptNotifier"
        
        data = {'text':exceptNotifier['SUBJECT']+exceptNotifier["BODY"]}
        
        message = {"Content": data['text']}
        encoded_msg = json.dumps(message).encode("utf-8")
        resp = http.request("POST", URL, body=encoded_msg)













if __name__ == "__main__":
    
    # Get your slcak bot and enter URL
    """Get your Webhook URL from your chatroom. 
    https://docs.aws.amazon.com/chime/latest/ag/webhooks.html"""

    global URL 
    URL = "https://hooks.chime.aws/incomingwebhooks/72970d5c-7ed1-4e05-bf39-305b860e7e13?token=VWxFRm1IOVh8MXxzQ2VWZVBjQ3EzNE1Oa29Wa0doeDRBWFNEZWJYdkZnSHdjbnlkRDV0TW40"
    
    sys.excepthook = ExceptChime.__call__

    try:
        print(1/20)  
        SuccessChime().__call__() #1 success sender          

    except ExceptChime as e:      #2 except sender            
        sys.exit()

    SendChime().__call__()        #3 customized sender          