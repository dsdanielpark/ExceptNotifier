import requests


def send_slack_msg(URL, msg):
    data = {'text':msg}
    resp = requests.post(url=URL, json=data)
    return resp


if __name__ == "__main__": 
    URL = "xxxxx"
    msg = "Test Message"
    send_slack_msg(URL, msg)
