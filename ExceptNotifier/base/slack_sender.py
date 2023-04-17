import requests


def send_slack_msg(URL: str, msg: str) -> dict:
    """Send message to chat room through slack app's api.

    :param URL: URL from slack app
    :type URL: str
    :param msg: Message text
    :type msg: str
    :return: Response according to REST API request
    :rtype: dict
    """
    
    data = {'text':msg}
    resp = requests.post(url=URL, json=data)
    return resp


if __name__ == "__main__": 
    URL = "xxxxx"
    msg = "Test Message"
    send_slack_msg(URL, msg)
