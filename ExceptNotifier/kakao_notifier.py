import requests
import traceback
import re
import datetime
from email.message import EmailMessage
import sys
import json
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class ExceptKakao(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __call__(etype, value, tb):
        excType = re.sub('(<(type|class \')|\'exceptions.|\'>|__main__.)', '', str(etype)).strip()
        start_time = datetime.datetime.now()
        
        exceptNotifier = {'SUBJECT':'[Except Notifier] ** Error! ** Python Code Exception Detected', 'BODY':f'\n\nIMPORTANT WARNING \nPython Exception Detected in Your Code. \n\nHi there, \nThis is an exception catch notifier. \n\n - * Code Status: Fail. \n - * Detail: Python Code Ran Exceptions. \n - * Time: {start_time.strftime(DATE_FORMAT)} \n\n :no_entry: {excType}: %{etype.__doc__}\n\n {value} \n\n'}
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
        
        with open(token_path,"r") as kakao:
            tokens = json.load(kakao)

        url="https://kapi.kakao.com/v2/api/talk/memo/default/send"
        headers={
            "Authorization" : "Bearer " + tokens["access_token"]
        }
        data = {
            'object_type': 'text',
            'text': data['text'],
            'link': {
                'web_url': 'https://developers.kakao.com',
                'mobile_web_url': 'https://developers.kakao.com'
            }
        }
        
        data = {'template_object': json.dumps(data)}
        response = requests.post(url, headers=headers, data=data)
        response.status_code


    @staticmethod
    def send_slack_message(URL, msg):
        data = {'text':msg}
        resp = requests.post(url=URL, json=data)
        return resp



class SuccessKakao:
    def __init__(self) -> None:
        pass
        
    def __call__(self, *args, **kwds) -> None:
        exceptNotifier = EmailMessage()
        start_time = datetime.datetime.now()
        f'Time Stamp: {start_time.strftime(DATE_FORMAT)}'
        exceptNotifier = {"SUBJECT":"[Success Notifier] ** Success! ** Python Code Executed Successfully"}
        exceptNotifier["BODY"]=f"\n\nHi there, \nThis is a success notifier.\n\n - * Code Status: Success. \n - * Detail: Python Code Ran Without Exceptions. \n - :clock2: Time: {start_time.strftime(DATE_FORMAT)} \n\nI just wanted to let you know that your Python code has run successfully without any exceptions. \n\nAll the best, \nExcept Notifier https://github.com/dsdanielpark/ExceptNotifier"
        
        data = {'text':exceptNotifier['SUBJECT']+exceptNotifier["BODY"]}
        
        with open(token_path,"r") as kakao:
            tokens = json.load(kakao)

        url="https://kapi.kakao.com/v2/api/talk/memo/default/send"
        headers={
            "Authorization" : "Bearer " + tokens["access_token"]
        }
        data = {
            'object_type': 'text',
            'text': data['text'],
            'link': {
                'web_url': 'https://developers.kakao.com',
                'mobile_web_url': 'https://developers.kakao.com'
            }
        }
        
        data = {'template_object': json.dumps(data)}
        response = requests.post(url, headers=headers, data=data)
        response.status_code


class SendKakao:
    def __init__(self) -> None:
        pass
        
    def __call__(self, *args, **kwds) -> None:
        exceptNotifier = EmailMessage()
        start_time = datetime.datetime.now()
        f'Time Stamp: {start_time.strftime(DATE_FORMAT)}'
        exceptNotifier = {"SUBJECT":"[Codeline Notifier] ** Notice! ** Code Execution Reached Specified Line"}
        exceptNotifier["BODY"] = f"\n\nHi there, \nThis is a customized notifier.\n\n- * Code Status: Done. \n- * Detail: Code Execution Reached Specified Line.  \n- :clock2: Time: {start_time.strftime(DATE_FORMAT)} \n\nThe code has reached the line where you requested an email to be sent. As per your instruction, we are sending this email. \n\nAll the best, \nExcept Notifier https://github.com/dsdanielpark/ExceptNotifier"
        
        data = {'text':exceptNotifier['SUBJECT']+exceptNotifier["BODY"]}
        
        with open(token_path,"r") as kakao:
            tokens = json.load(kakao)

        url="https://kapi.kakao.com/v2/api/talk/memo/default/send"
        headers={
            "Authorization" : "Bearer " + tokens["access_token"]
        }
        data = {
            'object_type': 'text',
            'text': data['text'],
            'link': {
                'web_url': 'https://developers.kakao.com',
                'mobile_web_url': 'https://developers.kakao.com'
            }
        }
        
        data = {'template_object': json.dumps(data)}
        response = requests.post(url, headers=headers, data=data)
        response.status_code








if __name__ == "__main__":
    
    """Follow next notebooks"""

    global token_path 
    token_path = r'C:\Users\parkm\Desktop\git\ExceptionNotifier\notebooks\kakao\token.json'
    
    sys.excepthook = ExceptKakao.__call__

    try:
        print(1/0)  
        SuccessKakao().__call__() #1 success sender          

    except ExceptKakao as e:      #2 except sender            
        sys.exit()

    SendKakao().__call__()        #3 customized sender          