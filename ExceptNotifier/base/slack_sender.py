# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo

import requests


def send_slack_msg(slack_webhook_url: str, msg: str) -> dict:
    """Send message to chat room through slack app's api.

    :param slack_webhook_url: slack_webhook_url from slack app
    :type slack_webhook_url: str
    :param msg: Message text
    :type msg: str
    :return: Response according to REST API request
    :rtype: dict
    """

    data = {"text": msg}
    resp = requests.post(url=slack_webhook_url, json=data)

    return resp


# if __name__ == "__main__":
#     slack_webhook_url = "xxxxx"
#     msg = "Test Message"
#     send_slack_msg(slack_webhook_url, msg)
