# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo

import json
import requests


def send_teams_msg(_TEAMS_WEBHOOK_URL, msg):
    """Send message to chat room through microsoft teams app's webhook url.

    :param _TEAMS_WEBHOOK_URL: _TEAMS_WEBHOOK_URL from teams app
    :type _TEAMS_WEBHOOK_URL: str
    :param msg: Message text
    :type msg: str
    :return: Response according to REST API request
    :rtype: dict
    """

    payload = {"text": msg}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(_TEAMS_WEBHOOK_URL, headers=headers, data=json.dumps(payload))

    return resp
