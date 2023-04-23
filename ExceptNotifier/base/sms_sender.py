# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo

from twilio.rest import Client


def send_sms_msg(
    _TWILIO_SID: str,
    _TWILIO_TOKEN: str,
    _SENDER_PHONE_NUMBER: str,
    _RECIPIENT_PHONE_NUMBER: str,
    msg: str,
) -> dict:
    """Send SMS through twilio platform.
    https://www.twilio.com/en-us

    :param _TWILIO_SID: Twilio personal _TWILIO_SID
    :type _TWILIO_SID: str
    :param _TWILIO_TOKEN: Twilio personal _TWILIO_TOKEN
    :type _TWILIO_TOKEN: str
    :param _SENDER_PHONE_NUMBER: Sender phone number
    :type _SENDER_PHONE_NUMBER: str
    :param _RECIPIENT_PHONE_NUMBER: Recipient phone number
    :type _RECIPIENT_PHONE_NUMBER: str
    :param msg: SMS content
    :type msg: str
    :return: Response dict
    :rtype: dict
    """

    client = Client(_TWILIO_SID, _TWILIO_TOKEN)
    resp = client.messages.create(
        to=_RECIPIENT_PHONE_NUMBER, from_=_SENDER_PHONE_NUMBER, body=msg[:1500]
    )
    return resp


# if __name__ == "__main__":
#     """https://www.twilio.com/en-us"""

#     _TWILIO_SID = "xxxxx"
#     _TWILIO_TOKEN = "yyyyy"
#     client = Client(_TWILIO_SID, _TWILIO_TOKEN)
#     _SENDER_PHONE_NUMBER = "+aaaaa"
#     _RECIPIENT_PHONE_NUMBER = "+bbbbb"
#     msg = "ExceptNotifier Test"
#     send_sms_msg(
#         _TWILIO_SID, _TWILIO_TOKEN, _SENDER_PHONE_NUMBER, _RECIPIENT_PHONE_NUMBER, msg
#     )
