# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo

import requests


def send_slack_msg(_SLACK_WEBHOOK_URL: str, msg: str) -> dict:
    """Send message to chat room through slack app's api.

    :param _SLACK_WEBHOOK_URL: _SLACK_WEBHOOK_URL from slack app
    :type _SLACK_WEBHOOK_URL: str
    :param msg: Message text
    :type msg: str
    :return: Response according to REST API request
    :rtype: dict
    """

    data = {"text": msg}
    resp = requests.post(url=_SLACK_WEBHOOK_URL, json=data)

    return resp


# if __name__ == "__main__":
#     _SLACK_WEBHOOK_URL = "xxxxx"
#     msg = "Test Message"
#     send_slack_msg(_SLACK_WEBHOOK_URL, msg)
