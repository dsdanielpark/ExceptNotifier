# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import smtplib
from email.message import EmailMessage


def send_gmail_msg(
    gmail_sender_address: str,
    gmail_recipient_address: str,
    gamil_app_pw_of_sender: str,
    subject_msg: str,
    body_msg: str,
) -> dict:
    """Send mail through gmail smtp server

    :param gmail_sender_address: Gmail address who send message
    :type gmail_sender_address: str
    :param gmail_recipient_address: Gmail address who receive message
    :type gmail_recipient_address: str
    :param gamil_app_pw_of_sender: Google app password
    :type gamil_app_pw_of_sender: str
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
    EMAIL_ADDR = gmail_sender_address
    EMAIL_PASSWORD = gamil_app_pw_of_sender
    smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)
    message = EmailMessage()
    message.set_content(body_msg)
    message["Subject"] = subject_msg
    message["From"] = EMAIL_ADDR
    message["To"] = gmail_recipient_address
    resp = smtp.send_message(message)
    smtp.quit()

    return resp

