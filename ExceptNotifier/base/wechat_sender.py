# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import requests


def send_wechat_msg(_WECHAT_WEBHOOK_URL: str, msg: str) -> None:
    """Send message to wechat.

    :param _WECHAT_WEBHOOK_URL: Wechat Webhook URL https://work.weixin.qq.com/api/doc/90000/90136/91770
    :type _WECHAT_WEBHOOK_URL: str
    :param msg: Message to send
    :type msg: str
    """
    msg_template = {"msgtype": "text", "text": {"content": ""}}
    msg_template["text"]["content"] = "\n".join(msg)
    resp = requests.post(_WECHAT_WEBHOOK_URL, json=msg_template)
    return resp
