# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import requests


def send_whatsapp_msg(
    msg: str,
    sender_phone_number_id: str,
    TOKEN: str,
    receiver_number: str,
    recipient_type: str = "individual",
) -> dict:
    """Send me a message via whatsapp.
    However, from v16 api, it seems to have been changed so that templates that have passed deliberation can be sent.
    Therefore, it is *NOT used* by ExceptNotifier.

    :param msg: Message content (Cannot be used as it is not a template)
    :type msg: str
    :param sender_phone_number_id: Sender phone number
    :type sender_phone_number_id: str
    :param TOKEN: Whatsapp personal token
    :type TOKEN: str
    :param receiver_number: Recipient phone number
    :type receiver_number: str
    :param recipient_type: Type of recipient, defaults to "individual"
    :type recipient_type: str, optional
    :return: _description_
    :rtype: dict
    """

    url = f"https://graph.facebook.com/v16.0/{sender_phone_number_id}/messages"

    data = {
        "messaging_product": "whatsapp",
        "to": receiver_number,
        "type": "template",
        "template": {"name": "hello_world", "language": {"code": "en_US"}},
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(TOKEN),
    }
    resp = requests.post(f"{url}", headers=headers, json=data)
    return resp
