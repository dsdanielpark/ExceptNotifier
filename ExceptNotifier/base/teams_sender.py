import json
import requests


def send_teams_msg(URL, msg):
    """Send message to chat room through microsoft teams app's webhook url.

    :param URL: URL from teams app
    :type URL: str
    :param msg: Message text
    :type msg: str
    :return: Response according to REST API request
    :rtype: dict
    """
    
    payload = {
        "text": msg
    }
    headers = {
        'Content-Type': 'application/json'
    }
    resp = requests.post(URL, headers=headers, data=json.dumps(payload))

    return resp