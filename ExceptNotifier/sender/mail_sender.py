# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import smtplib
from email.message import EmailMessage


def send_gmail_msg(
    _GMAIL_SENDER_ADDR: str,
    _GAMIL_RECIPIENT_ADDR: str,
    _GMAIL_APP_PASSWORD_OF_SENDER: str,
    subject_msg: str,
    body_msg: str,
) -> dict:
    """Send mail through gmail smtp server

    :param _GMAIL_SENDER_ADDR: Gmail address who send message
    :type _GMAIL_SENDER_ADDR: str
    :param _GAMIL_RECIPIENT_ADDR: Gmail address who receive message
    :type _GAMIL_RECIPIENT_ADDR: str
    :param _GMAIL_APP_PASSWORD_OF_SENDER: Google app password
    :type _GMAIL_APP_PASSWORD_OF_SENDER: str
    :param subject_msg: Mail title
    :type subject_msg: str
    :param body_msg: Mail body
    :type body_msg: str
    :return: Response according to sending request
    :rtype: dict
    """

    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 465
    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    EMAIL_ADDR = _GMAIL_SENDER_ADDR
    EMAIL_PASSWORD = _GMAIL_APP_PASSWORD_OF_SENDER
    smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)
    message = EmailMessage()
    message.set_content(body_msg)
    message["Subject"] = subject_msg
    message["From"] = EMAIL_ADDR
    message["To"] = _GAMIL_RECIPIENT_ADDR
    resp = smtp.send_message(message)
    smtp.quit()

    return resp


# if __name__ == "__main__":  # No-QA
#     _GMAIL_SENDER_ADDR = "xxxxx@gmail.com"
#     _GMAIL_APP_PASSWORD_OF_SENDER = "yyyyy"
#     _GAMIL_RECIPIENT_ADDR = "zzzzz@gmail.com"
#     subject_msg = "Python Code Alarm: Process End."
#     body_msg = "Python Code Notice: \nA notification has arrived from your code."
#     send_gmail_msg(
#         _GMAIL_SENDER_ADDR,
#         _GAMIL_RECIPIENT_ADDR,
#         _GMAIL_APP_PASSWORD_OF_SENDER,
#         subject_msg,
#         body_msg,
#     )
