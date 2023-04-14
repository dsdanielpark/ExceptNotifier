import smtplib
from email.message import EmailMessage

def send_gmail(FROM_EMAIL_ADDR, TO_EMAIL_ADDR, FROM_EMAIL_PASSWORD, subject_msg, body_msg):
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 465
    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    EMAIL_ADDR = FROM_EMAIL_ADDR
    EMAIL_PASSWORD = FROM_EMAIL_PASSWORD
    smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)
    message = EmailMessage()
    message.set_content(body_msg)
    message["Subject"] = subject_msg
    message["From"] = EMAIL_ADDR
    message["To"] = TO_EMAIL_ADDR
    resp = smtp.send_message(message)
    smtp.quit()

    return resp


if __name__ == "__main__": #No-QA
    FROM_EMAIL_ADDR = 'xxxxxxxxxxxxxxxx@gmail.com'
    FROM_EMAIL_PASSWORD = 'yyyyyyyyyy'
    body_msg = "Python Code Notice: \nA notification has arrived from your code."
    subject_msg = "Python Code Alarm: Process End."
    TO_EMAIL_ADDR = 'zzzzzzzzzzz@gmail.com'
    
    send_gmail(FROM_EMAIL_ADDR, TO_EMAIL_ADDR, FROM_EMAIL_PASSWORD, subject_msg, body_msg)