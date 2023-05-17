# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import requests


def send_line_msg(line_token: str, msg: str) -> dict:
    """Send message to chat room through Line app's REST API.

    :param line_token: Line notify API token
    :type line_token: str
    :param msg: Message text
    :type msg: str
    :return: Response according to REST API request
    :rtype: dict
    """

    api_url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer " + line_token}
    message = {"message": msg}
    resp = requests.post(api_url, headers=headers, data=message)
    return resp


# if __name__ == "__main__":
#     global line_token
#     line_token = "XXXXXXXXX"
#     msg = "Test Message"
#     send_line_msg(line_token, msg)
