import requests   

def send_line_msg(TOKEN: str, msg: str) -> dict:
    """Send message to chat room through Line app's REST API.

    :param TOKEN: Line notify API token
    :type TOKEN: str
    :param msg: Message text
    :type msg: str
    :return: Response according to REST API request
    :rtype: dict
    """

    api_url = "https://notify-api.line.me/api/notify"
    headers = {'Authorization':'Bearer '+ TOKEN}
    message = {
        "message" : msg
    }
    resp = requests.post(api_url, headers= headers , data = message)
    return resp



if __name__ == "__main__": 
    global TOKEN
    TOKEN = "XXXXXXXXX"
    msg = "Test Message"
    send_line_msg(TOKEN, msg)
