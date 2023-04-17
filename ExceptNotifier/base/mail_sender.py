import smtplib
from email.message import EmailMessage

def send_gmail(from_email_addr: str, to_email_addr: str, from_email_app_password: str, subject_msg: str, body_msg: str) -> dict:
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


if __name__ == "__main__": #No-QA
    from_email_addr = 'xxxxxxxxxxxxxxxx@gmail.com'
    from_email_app_password = 'yyyyyyyyyy'
    body_msg = "Python Code Notice: \nA notification has arrived from your code."
    subject_msg = "Python Code Alarm: Process End."
    to_email_addr = 'zzzzzzzzzzz@gmail.com'
    
    send_gmail(from_email_addr, to_email_addr, from_email_app_password, subject_msg, body_msg)