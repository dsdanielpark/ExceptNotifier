# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo


def send_discord_msg(_DISCORD_WEBHOOK_URL: str, msg: str) -> dict:
    """Send message to chat room through discord app's webhook url.

    :param _DISCORD_WEBHOOK_URL: Webhook url from discord app
    :type _DISCORD_WEBHOOK_URL: str
    :param msg: Message text
    :type msg: str
    :return: Response according to REST API request
    :rtype: dict
    """
    try:
        from discord import Webhook, RequestsWebhookAdapter

        webhook = Webhook.from_url(
            _DISCORD_WEBHOOK_URL, adapter=RequestsWebhookAdapter()
        )
        resp = webhook.send(msg)
    except:
        from discord import SyncWebhook

        webhook = SyncWebhook.from_url(_DISCORD_WEBHOOK_URL)  # Initializing webhook
        resp = webhook.send(content=msg[:1900])
    return resp


# if __name__ == "__main__":
#     _DISCORD_WEBHOOK_URL = "xxxxx"
#     msg = "Sending Test"
#     send_discord_msg(_DISCORD_WEBHOOK_URL, msg)
