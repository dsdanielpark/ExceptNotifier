import urllib3
import json

http = urllib3.PoolManager()

def send_chime_msg(URL: str, msg: str) -> dict:
    """Send message to chat room through chime app's webhook url.

    :param URL: Webhook url from chime app
    :type URL: str
    :param msg: Message text
    :type msg: str
    :return: Response according to REST API request
    :rtype: dict
    """

    url = URL
    message = {"Content": msg}
    encoded_msg = json.dumps(message).encode("utf-8")
    resp = http.request("POST", url, body=encoded_msg)

    return resp


if __name__ == "__main__":
    URL = "https://hooks.chime.aws/incomingwebhooks/72970d5c-7ed1-4e05-bf39-305b860e7e13?token=VWxFRm1IOVh8MXxzQ2VWZVBjQ3EzNE1Oa29Wa0doeDRBWFNEZWJYdkZnSHdjbnlkRDV0TW40"
    
    send_chime_msg(URL, "Test")