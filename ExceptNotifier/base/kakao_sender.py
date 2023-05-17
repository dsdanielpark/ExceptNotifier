# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import requests
import json


def send_kakao_msg(kakao_token_path: str, msg: str) -> dict:
    """Send message to chat room through kakaotalk app's REST API.

    :param kakao_token_path: Kakaotalk token path
    :type kakao_token_path: str
    :param msg: Message text
    :type msg: str
    :return: Response according to REST API request
    :rtype: dict
    """

    with open(kakao_token_path, "r") as kakao:
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

