import sys
import traceback
import re
import smtplib
from email.message import EmailMessage


class ExceptMail(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __call__(etype, value, tb):
        excType = re.sub('(<(type|class \')|\'exceptions.|\'>|__main__.)', '', str(etype)).strip()
        heydudenoticer = {'TO':gmail_receiver, 'FROM':gmail_sender, 'SUBJECT':'Oops! Python Exception Detected', 'BODY':f'Important: Python Exception Detected in Your Code. \n\n hi there, \nThis is an exception catch notifier.\n\n{excType}: %{etype.__doc__}\n\n {value} \n\n'}
        SMTP_SERVER = 'smtp.gmail.com'
        for line in traceback.extract_tb(tb):
            heydudenoticer['BODY'] += '\tFile: "%s"\n\t\t%s %s: %s\n' % (line[0], line[2], line[1], line[3])
        while 1:
            if not tb.tb_next: break
            tb = tb.tb_next
        stack = []
        f = tb.tb_frame
        while f:
            stack.append(f)
            f = f.f_back
        stack.reverse()
        heydudenoticer['BODY'] += '\nLocals by frame, innermost last:'
        for frame in stack:
            heydudenoticer['BODY'] += '\nFrame %s in %s at line %s' % (frame.f_code.co_name, frame.f_code.co_filename, frame.f_lineno)
            for key, val in frame.f_locals.items():
                heydudenoticer['BODY'] += '\n\t%20s = ' % key
                try:
                    heydudenoticer['BODY'] += str(val)
                except:
                    heydudenoticer['BODY'] += '<ERROR WHILE PRINTING VALUE>'
        heydudenoticer['ALL'] = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (heydudenoticer['FROM'], heydudenoticer['TO'], heydudenoticer['SUBJECT'], heydudenoticer['BODY'])
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, 465)
        smtp.login(gmail_sender, gmail_app_password_of_sender)
        smtp.sendmail(heydudenoticer['FROM'], heydudenoticer['TO'], heydudenoticer['ALL'])
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
        message.set_content("Hi there, \nThis is a success notifier. \n\nI just wanted to let you know that your Python code has run successfully without any exceptions. \n\n - Python Code Status: Done. \n - Detail: Python Code Ran Without Exceptions. \n\nAll the best, \nCatchException https://github.com/dsdanielpark/CatchException")
        message["Subject"] = "Success! Python Code Executed Successfully"
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
        message.set_content("Hi there, \nThis is a customized notifier.\n\nThe code has reached the line where you requested an email to be sent. As per your instruction, we are sending this email. \n\nAll the best, \nCatchException https://github.com/dsdanielpark/CatchException")
        message["Subject"] = "Notice! Code Execution Reached Specified Line"
        message["From"] = gmail_sender
        message["To"] = gmail_receiver
        smtp.send_message(message)
        smtp.quit()




















if __name__ == '__main__':

    # 01. Set variable.
    global gmail_receiver, gmail_sender, gmail_app_password_of_sender
    gmail_receiver = 'parkminwoo1991@gmail.com'
    gmail_sender = 'heydudenotice@gmail.com'
    gmail_app_password_of_sender = 'xxxxxxxxxxx'
    sys.excepthook = ExceptMail.__call__

    try:
        # 02. Locate your code.
        print(1/0)      
        SuccessMail().__call__()          


    # 03-a. Mail Sent: When strike exception
    except ExceptMail as e:                    
        sys.exit()

    # 03-b. Mail Sent:  When code exit without exception
    SuccessMail().__call__()                     
    

