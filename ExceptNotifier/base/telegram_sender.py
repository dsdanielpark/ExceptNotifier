import requests


def send_telegram_msg(TOKEN: str, msg: str) -> dict:
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    req_dict = requests.get(url).json()
    bot_id = dict(dict(dict(list(dict(req_dict).values())[1][0])['message'])['from'])['id']
    bot_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={bot_id}&text={msg}"
    resp = requests.get(bot_url).json()

    return resp


if __name__ == "__main__": #No-QA

    TOKEN = "xxxxx"
    msg = "Test Message"
    send_telegram_msg(TOKEN, msg)
