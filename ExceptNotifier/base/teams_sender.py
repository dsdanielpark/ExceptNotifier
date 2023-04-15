import json
import requests


def send_teams_msg(URL, msg):
    
    payload = {
        "text": msg
    }
    headers = {
        'Content-Type': 'application/json'
    }
    resp = requests.post(URL, headers=headers, data=json.dumps(payload))

    return resp