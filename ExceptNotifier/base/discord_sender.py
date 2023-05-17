# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo


def send_discord_msg(discord_webhook_url: str, msg: str) -> dict:
    """Send message to chat room through discord app's webhook url.

    :param discord_webhook_url: Webhook url from discord app
    :type discord_webhook_url: str
    :param msg: Message text
    :type msg: str
    :return: Response according to REST API request
    :rtype: dict
    """
    try:
        from discord import Webhook, RequestsWebhookAdapter

        webhook = Webhook.from_url(
            discord_webhook_url, adapter=RequestsWebhookAdapter()
        )
        resp = webhook.send(msg)
    except:
        from discord import SyncWebhook

        webhook = SyncWebhook.from_url(discord_webhook_url)  # Initializing webhook
        resp = webhook.send(content=msg[:1900])
    return resp
