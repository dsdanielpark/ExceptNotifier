# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo

import json
import requests


def send_teams_msg(teams_webhook_url, msg):
    """Send message to chat room through microsoft teams app's webhook url.

    :param teams_webhook_url: teams_webhook_url from teams app
    :type teams_webhook_url: str
    :param msg: Message text
    :type msg: str
    :return: Response according to REST API request
    :rtype: dict
    """

    payload = {"text": msg}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(teams_webhook_url, headers=headers, data=json.dumps(payload))

    return resp
