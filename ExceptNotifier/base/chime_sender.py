# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import urllib3
import json

http = urllib3.PoolManager()


def send_chime_msg(chime_webhook_url: str, msg: str) -> dict:
    """Send message to chat room through chime app's webhook url.

    :param chime_webhook_url: Webhook url from chime app
    :type chime_webhook_url: str
    :param msg: Message text
    :type msg: str
    :return: Response according to REST API request
    :rtype: dict
    """

    url = chime_webhook_url
    message = {"Content": msg}
    encoded_msg = json.dumps(message).encode("utf-8")
    resp = http.request("POST", url, body=encoded_msg)

    return resp

