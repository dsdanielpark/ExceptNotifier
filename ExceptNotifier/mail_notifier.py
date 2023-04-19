#-*- coding: utf-8 -*- 
# Copyright 2023 parkminwoo
import sys
import traceback
import re
import smtplib
import datetime
from email.message import EmailMessage
from ExceptNotifier import send_gmail_msg, receive_openai_advice
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"



class ExceptMail(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __call__(etype, value, tb):
        """Override excepthook to send error message to Gmail.

        :param etype: Error Type
        :type etype: _type_
        :param value: Error Value
        :type value: _type_
        :param tb: Traceback Information
        :type tb: _type_
        """
        excType = re.sub('(<(type|class \')|\'exceptions.|\'>|__main__.)', '', str(etype)).strip()
        exceptNotifier = {'TO':_GAMIL_RECIPIENT_ADDR, 'FROM':_GMAIL_SENDER_ADDR, 'SUBJECT':'[Except Notifier] Error! Python Code Exception Detected', 'BODY':f'IMPORTANT WARNING: \nPython Exception Detected in Your Code. \n\nHi there, \nThis is an exception catch notifier.\n\n{excType}: %{etype.__doc__}\n\n {value} \n\n'}
        SMTP_SERVER = 'smtp.gmail.com'
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
        start_time = datetime.datetime.now()
        
        exceptNotifier['BODY'] += f'\nTime Stamp: {start_time.strftime(DATE_FORMAT)}'
        exceptNotifier['BODY'] += '\nLocals by frame, innermost last::::'
        for frame in stack:
            exceptNotifier['BODY'] += '\nFrame %s in %s at line %s' % (frame.f_code.co_name, frame.f_code.co_filename, frame.f_lineno)
            for key, val in frame.f_locals.items():
                exceptNotifier['BODY'] += '\n\t%20s = ' % key
                try:
                    exceptNotifier['BODY'] += str(val)
                except:
                    exceptNotifier['BODY'] += '<ERROR WHILE PRINTING VALUE>'
        
        print(exceptNotifier['BODY'])            
        exceptNotifier['ALL'] = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (exceptNotifier['FROM'], exceptNotifier['TO'], exceptNotifier['SUBJECT'], exceptNotifier['BODY'])
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, 465)
        smtp.login(_GMAIL_SENDER_ADDR, _GMAIL_APP_PASSWORD_OF_SENDER)
        smtp.sendmail(exceptNotifier['FROM'], exceptNotifier['TO'], exceptNotifier['ALL'])

        try:
            error_message = f'error_type=={excType} error_type_document=={etype.__doc__} error_value=={value} stack infomation=={stack} code name=={frame.f_code.co_name}file name=={frame.f_code.co_filename} file_number=={frame.f_lineno}'
            advice_msg = '\tFile: "%s"\n\t\t%s %s: %s\n' % (line[0], line[2], line[1], line[3])
            advice_msg += receive_openai_advice(_OPEN_AI_MODEL, _OPEN_AI_API, error_message[:150])
            exceptNotifier = {'TO':_GAMIL_RECIPIENT_ADDR, 'FROM':_GMAIL_SENDER_ADDR, 'SUBJECT':'[Except AI Debugging] Error! chatGPT Debugging guide.', 'BODY':f'IMPORTANT WARNING: \nPython Exception Detected in Your Code. \n\nHi there, \nThis is advice from OpenAI ChatGPT \n\n {advice_msg}'}
            smtp.sendmail(exceptNotifier['FROM'], exceptNotifier['TO'], exceptNotifier['ALL'])
        except Exception as e:
            pass
        
        smtp.quit()

    @staticmethod
    def send_gmail_msg(from_email_addr: str, to_email_addr: str, from_email_app_password: str, subject_msg: str, body_msg: str) -> dict:
        """Send mail through gmail smtp server

        :param from_email_addr: Gmail address who send message
        :type from_email_addr: str
        :param to_email_addr: Gmail address who receive message
        :type to_email_addr: str
        :param from_email_app_password: Google app password
        :type from_email_app_password: str
        :param subject_msg: Mail title
        :type subject_msg: str
        :param body_msg: Mail body
        :type body_msg: str
        :return: Response according to sending request
        :rtype: dict
        """
        
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 465
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        EMAIL_ADDR = from_email_addr
        EMAIL_PASSWORD = from_email_app_password
        smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)
        message = EmailMessage()
        message.set_content(body_msg)
        message["Subject"] = subject_msg
        message["From"] = EMAIL_ADDR
        message["To"] = to_email_addr
        resp = smtp.send_message(message)
        smtp.quit()

        return resp



class SuccessMail:
    def __init__(self) -> None:
        pass
        
    def __call__(self, *args, **kwds) -> None:
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 465
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        smtp.login(_GMAIL_SENDER_ADDR, _GMAIL_APP_PASSWORD_OF_SENDER)
        message = EmailMessage()
        start_time = datetime.datetime.now()
        
        f'Time Stamp: {start_time.strftime(DATE_FORMAT)}'
        message.set_content(f"Hi there, \nThis is a success notifier.\n\n - Time: {start_time.strftime(DATE_FORMAT)} \n - Code Status: Done. \n - Detail: Python Code Ran Without Exceptions. \n\nI just wanted to let you know that your Python code has run successfully without any exceptions. \n\nAll the best, \nExcept Notifier https://github.com/dsdanielpark/ExceptNotifier")
        message["Subject"] = "[Success Notifier] Success! Python Code Executed Successfully"
        message["From"] = _GMAIL_SENDER_ADDR
        message["To"] = _GAMIL_RECIPIENT_ADDR
        
        smtp.send_message(message)
        smtp.quit()


class SendMail:
    def __init__(self) -> None:
        pass
        
    def __call__(self, *args, **kwds) -> None:
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 465
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        smtp.login(_GMAIL_SENDER_ADDR, _GMAIL_APP_PASSWORD_OF_SENDER)
        message = EmailMessage()
        start_time = datetime.datetime.now()
        
        f'Time Stamp: {start_time.strftime(DATE_FORMAT)}'
        message.set_content(f"Hi there, \nThis is a customized notifier.\n\n - Time: {start_time.strftime(DATE_FORMAT)}\n - Code Status: Done. \n - Detail: Code Execution Reached Specified Line. \n\nThe code has reached the line where you requested an email to be sent. As per your instruction, we are sending this email. \n\nAll the best, \nExcept Notifier https://github.com/dsdanielpark/ExceptNotifier")
        message["Subject"] = "[Codeline Notifier] Notice! Code Execution Reached Specified Line"
        message["From"] = _GMAIL_SENDER_ADDR
        message["To"] = _GAMIL_RECIPIENT_ADDR
        smtp.send_message(message)
        smtp.quit()





















if __name__ == '__main__':

    # Set global variables
    global _GAMIL_RECIPIENT_ADDR, _GMAIL_SENDER_ADDR, _GMAIL_APP_PASSWORD_OF_SENDER
    _GAMIL_RECIPIENT_ADDR = 'parkminwoo1991@gmail.com'
    _GMAIL_SENDER_ADDR = 'heydudenotice@gmail.com'
    _GMAIL_APP_PASSWORD_OF_SENDER = 'xxxxxxxxxxx'
    sys.excepthook = ExceptMail.__call__

    try:
        print(1/0)      
        SuccessMail().__call__() #1 success sender


    except ExceptMail as e:      #2 except sender            
        sys.exit()


    SendMail().__call__()        #3 Any line sender

