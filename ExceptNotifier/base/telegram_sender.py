# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import requests


def send_telegram_msg(_TELEGRAM_TOKEN: str, msg: str) -> dict:
    """Send message via telegram bot.

    :param _TELEGRAM_TOKEN: Telegram secure bot Token
    :type _TELEGRAM_TOKEN: str
    :param msg: Message content
    :type msg: str
    :return: Response dict
    :rtype: dict
    """
    url = f"https://api.telegram.org/bot{_TELEGRAM_TOKEN}/getUpdates"
    req_dict = requests.get(url).json()
    print(req_dict)
    bot_id = dict(dict(dict(list(dict(req_dict).values())[1][0])["message"])["from"])[
        "id"
    ]
    bot_url = f"https://api.telegram.org/bot{_TELEGRAM_TOKEN}/sendMessage?chat_id={bot_id}&text={msg}"
    resp = requests.get(bot_url).json()

    return resp


# if __name__ == "__main__":
#     _TELEGRAM_TOKEN = "xxxxxxxxxx"
#     msg = "Test Message"
#     send_telegram_msg(_TELEGRAM_TOKEN, msg)
