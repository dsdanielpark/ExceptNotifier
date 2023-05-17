# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import requests


def send_wechat_msg(wechat_webhook_url: str, msg: str) -> None:
    """Send message to wechat.

    :param wechat_webhook_url: Wechat Webhook URL https://work.weixin.qq.com/api/doc/90000/90136/91770
    :type wechat_webhook_url: str
    :param msg: Message to send
    :type msg: str
    """
    msg_template = {"msgtype": "text", "text": {"content": ""}}
    msg_template["text"]["content"] = "\n".join(msg)
    resp = requests.post(wechat_webhook_url, json=msg_template)
    return resp
