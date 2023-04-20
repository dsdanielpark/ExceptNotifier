# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import requests


def send_line_msg(_LINE_NOTIFY_API_TOKEN: str, msg: str) -> dict:
    """Send message to chat room through Line app's REST API.

    :param _LINE_NOTIFY_API_TOKEN: Line notify API token
    :type _LINE_NOTIFY_API_TOKEN: str
    :param msg: Message text
    :type msg: str
    :return: Response according to REST API request
    :rtype: dict
    """

    api_url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer " + _LINE_NOTIFY_API_TOKEN}
    message = {"message": msg}
    resp = requests.post(api_url, headers=headers, data=message)
    return resp


# if __name__ == "__main__":
#     global _LINE_NOTIFY_API_TOKEN
#     _LINE_NOTIFY_API_TOKEN = "XXXXXXXXX"
#     msg = "Test Message"
#     send_line_msg(_LINE_NOTIFY_API_TOKEN, msg)
