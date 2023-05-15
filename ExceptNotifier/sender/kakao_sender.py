# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import requests
import json


def send_kakao_msg(_KAKAO_TOKEN_PATH: str, msg: str) -> dict:
    """Send message to chat room through kakaotalk app's REST API.

    :param _KAKAO_TOKEN_PATH: Kakaotalk token path
    :type _KAKAO_TOKEN_PATH: str
    :param msg: Message text
    :type msg: str
    :return: Response according to REST API request
    :rtype: dict
    """

    with open(_KAKAO_TOKEN_PATH, "r") as kakao:
        tokens = json.load(kakao)

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {"Authorization": "Bearer " + tokens["access_token"]}
    data = {
        "object_type": "text",
        "text": msg,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com",
        },
    }

    data = {"template_object": json.dumps(data)}
    resp = requests.post(url, headers=headers, data=data)

    return resp


# if __name__ == "__main__":
#     global _KAKAO_TOKEN_PATH
#     _KAKAO_TOKEN_PATH = (
#         r"C:\Users\parkm\Desktop\git\ExceptionNotifier\tutorials\token.json"
#     )
#     msg = "Sending Message Test"
#     resp_status = send_kakao_msg(_KAKAO_TOKEN_PATH, msg)
#     print(resp_status)
