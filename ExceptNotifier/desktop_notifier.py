import requests
import traceback
import re
import datetime
from email.message import EmailMessage
import sys
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

import time
from plyer import notification
 
 



class ExceptDesktop(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __call__(etype, value, tb):
        """Override excepthook to send error message to Line.

        :param etype: Error Type
        :type etype: _type_
        :param value: Error Value
        :type value: _type_
        :param tb: Traceback Information
        :type tb: _type_
        """
        excType = re.sub('(<(type|class \')|\'exceptions.|\'>|__main__.)', '', str(etype)).strip()
        start_time = datetime.datetime.now()
        
        exceptNotifier = {'SUBJECT':'[Except Notifier] ⚠️ Error! Python Code Exception Detected', 'BODY':f'\n\nIMPORTANT WARNING \nPython Exception Detected in Your Code. \n\nHi there, \nThis is an exception catch notifier. \n\n - ☑️ Code Status: Fail.🛠 \n - ☑️ Detail: Python Code Ran Exceptions. \n - 🕐 Time: {start_time.strftime(DATE_FORMAT)} \n\n ⛔️ {excType}: %{etype.__doc__}\n\n {value} \n\n'}
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
        
        exceptNotifier['BODY'] += '\nLocal by frame, innermost last::::'
        for frame in stack:
            exceptNotifier['BODY'] += '\nFrame %s in %s at line %s' % (frame.f_code.co_name, frame.f_code.co_filename, frame.f_lineno)
            for key, val in frame.f_locals.items():
                exceptNotifier['BODY'] += '\n\t%20s = ' % key
                try:
                    exceptNotifier['BODY'] += str(val)
                except:
                    exceptNotifier['BODY'] += '<ERROR WHILE PRINTING VALUE>'
                    
        
        data = {'text':exceptNotifier['SUBJECT']+exceptNotifier['BODY']}


        notification.notify(
            title = exceptNotifier['SUBJECT'][:20],
            message=exceptNotifier['BODY'][:200])
        


    @staticmethod
    def send_line_msg(_LINE_NOTIFY_API_TOKEN: str, msg: str) -> dict:
        """Send message to chat room through Line app's REST API.

        :param _LINE_NOTIFY_API_TOKEN: Line notify API token
        :type _LINE_NOTIFY_API_TOKEN: str
        :param msg: Message text
        :type msg: str
        :return: Response according to REST API request
        :rtype: dict
        """

        api_url = "https://notify-api.line.me/api/notify"
        headers = {'Authorization':'Bearer '+ _LINE_NOTIFY_API_TOKEN}
        message = {
            "message" : msg
        }
        resp = requests.post(api_url, headers= headers , data = message)
        return resp




class SuccessDesktop:
    def __init__(self) -> None:
        pass
        
    def __call__(self, *args, **kwds) -> None:
        exceptNotifier = EmailMessage()
        start_time = datetime.datetime.now()
        f'Time Stamp: {start_time.strftime(DATE_FORMAT)}'
        exceptNotifier = {"SUBJECT":"[Success Notifier] 🎉 Success! Python Code Executed Successfully"}
        exceptNotifier["BODY"]=f"\n\nHi there, \nThis is a success notifier.\n\n - ✅ Code Status: Success. \n - ✅ Detail: Python Code Ran Without Exceptions. \n - 🕐 Time: {start_time.strftime(DATE_FORMAT)} \n\nI just wanted to let you know that your Python code has run successfully without any exceptions. \n\nAll the best, \nExcept Notifier https://github.com/dsdanielpark/ExceptNotifier"
        
        data = {'text':exceptNotifier['SUBJECT']+exceptNotifier["BODY"]}

        notification.notify(
            title = exceptNotifier['SUBJECT'][:20],
            message=exceptNotifier['BODY'][:200])


class SendDesktop:
    def __init__(self) -> None:
        pass
        
    def __call__(self, *args, **kwds) -> None:
        exceptNotifier = EmailMessage()
        start_time = datetime.datetime.now()
        f'Time Stamp: {start_time.strftime(DATE_FORMAT)}'
        exceptNotifier = {"SUBJECT":"[Codeline Notifier] 👏 Notice! Code Execution Reached Specified Line"}
        exceptNotifier["BODY"] = f"\n\nHi there, \nThis is a customized notifier.\n\n- ✅ Code Status: Done. \n- ✅ Detail: Code Execution Reached Specified Line.  \n- 🕐 Time: {start_time.strftime(DATE_FORMAT)} \n\nThe code has reached the line where you requested an email to be sent. As per your instruction, we are sending this email. \n\nAll the best, \nExcept Notifier https://github.com/dsdanielpark/ExceptNotifier"
        
        data = {'text':exceptNotifier['SUBJECT']+exceptNotifier["BODY"]}

        notification.notify(
            title = exceptNotifier['SUBJECT'][:20],
            message=exceptNotifier['BODY'][:200])




if __name__ == "__main__":
    
    sys.excepthook = ExceptDesktop.__call__

    try:
        print(1/0)  
        SuccessDesktop().__call__() #1 success sender          

    except ExceptDesktop as e:      #2 except sender            
        sys.exit()

    SendDesktop().__call__()        #3 customized sender          