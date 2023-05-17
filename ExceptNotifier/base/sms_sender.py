# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo

from twilio.rest import Client


def send_sms_msg(
    twilio_sid: str,
    twilio_token: str,
    sender_phone_number: str,
    recipient_phone_number: str,
    msg: str,
) -> dict:
    """Send SMS through twilio platform.
    https://www.twilio.com/en-us

    :param twilio_sid: Twilio personal twilio_sid
    :type twilio_sid: str
    :param twilio_token: Twilio personal twilio_token
    :type twilio_token: str
    :param sender_phone_number: Sender phone number
    :type sender_phone_number: str
    :param recipient_phone_number: Recipient phone number
    :type recipient_phone_number: str
    :param msg: SMS content
    :type msg: str
    :return: Response dict
    :rtype: dict
    """

    client = Client(twilio_sid, twilio_token)
    resp = client.messages.create(
        to=recipient_phone_number, from_=sender_phone_number, body=msg[:1500]
    )
    return resp


# if __name__ == "__main__":
#     """https://www.twilio.com/en-us"""

#     twilio_sid = "xxxxx"
#     twilio_token = "yyyyy"
#     client = Client(twilio_sid, twilio_token)
#     sender_phone_number = "+aaaaa"
#     recipient_phone_number = "+bbbbb"
#     msg = "ExceptNotifier Test"
#     send_sms_msg(
#         twilio_sid, twilio_token, sender_phone_number, recipient_phone_number, msg
#     )
