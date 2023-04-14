import sys
import traceback
import re
import smtplib
import datetime
from email.message import EmailMessage
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"



class ExceptMail(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __call__(etype, value, tb):
        excType = re.sub('(<(type|class \')|\'exceptions.|\'>|__main__.)', '', str(etype)).strip()
        exceptNotifier = {'TO':gmail_receiver, 'FROM':gmail_sender, 'SUBJECT':'[Except Notifier] Error! Python Code Exception Detected', 'BODY':f'IMPORTANT WARNING: \nPython Exception Detected in Your Code. \n\nHi there, \nThis is an exception catch notifier.\n\n{excType}: %{etype.__doc__}\n\n {value} \n\n'}
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
        exceptNotifier['BODY'] += '\nLocals by frame, innermost last:'
        for frame in stack:
            exceptNotifier['BODY'] += '\nFrame %s in %s at line %s' % (frame.f_code.co_name, frame.f_code.co_filename, frame.f_lineno)
            for key, val in frame.f_locals.items():
                exceptNotifier['BODY'] += '\n\t%20s = ' % key
                try:
                    exceptNotifier['BODY'] += str(val)
                except:
                    exceptNotifier['BODY'] += '<ERROR WHILE PRINTING VALUE>'
                    
        exceptNotifier['ALL'] = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (exceptNotifier['FROM'], exceptNotifier['TO'], exceptNotifier['SUBJECT'], exceptNotifier['BODY'])
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, 465)
        smtp.login(gmail_sender, gmail_app_password_of_sender)
        smtp.sendmail(exceptNotifier['FROM'], exceptNotifier['TO'], exceptNotifier['ALL'])
        smtp.quit()


class SuccessMail:
    def __init__(self) -> None:
        pass
        
    def __call__(self, *args, **kwds) -> None:
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 465
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        smtp.login(gmail_sender, gmail_app_password_of_sender)
        message = EmailMessage()
        start_time = datetime.datetime.now()
        
        f'Time Stamp: {start_time.strftime(DATE_FORMAT)}'
        message.set_content(f"Hi there, \nThis is a success notifier.\n\n - Time: {start_time.strftime(DATE_FORMAT)} \n - Code Status: Done. \n - Detail: Python Code Ran Without Exceptions. \n\nI just wanted to let you know that your Python code has run successfully without any exceptions. \n\nAll the best, \nExcept Notifier https://github.com/dsdanielpark/ExceptNotifier")
        message["Subject"] = "[Success Notifier] Success! Python Code Executed Successfully"
        message["From"] = gmail_sender
        message["To"] = gmail_receiver
        
        smtp.send_message(message)
        smtp.quit()


class SendMail:
    def __init__(self) -> None:
        pass
        
    def __call__(self, *args, **kwds) -> None:
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 465
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        smtp.login(gmail_sender, gmail_app_password_of_sender)
        message = EmailMessage()
        start_time = datetime.datetime.now()
        
        f'Time Stamp: {start_time.strftime(DATE_FORMAT)}'
        message.set_content(f"Hi there, \nThis is a customized notifier.\n\n - Time: {start_time.strftime(DATE_FORMAT)}\n - Code Status: Done. \n - Detail: Code Execution Reached Specified Line. \n\nThe code has reached the line where you requested an email to be sent. As per your instruction, we are sending this email. \n\nAll the best, \nExcept Notifier https://github.com/dsdanielpark/ExceptNotifier")
        message["Subject"] = "[Codeline Notifier] Notice! Code Execution Reached Specified Line"
        message["From"] = gmail_sender
        message["To"] = gmail_receiver
        smtp.send_message(message)
        smtp.quit()




















if __name__ == '__main__':

    # Set global variables
    global gmail_receiver, gmail_sender, gmail_app_password_of_sender
    gmail_receiver = 'parkminwoo1991@gmail.com'
    gmail_sender = 'heydudenotice@gmail.com'
    gmail_app_password_of_sender = 'xxxxxxxxxxx'
    sys.excepthook = ExceptMail.__call__

    try:
        print(1/0)      
        SuccessMail().__call__() #1 success sender


    except ExceptMail as e:      #2 except sender            
        sys.exit()


    SendMail().__call__()        #3 Any line sender

