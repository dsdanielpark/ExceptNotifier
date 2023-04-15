import json
import urllib3
import json

http = urllib3.PoolManager()


def send_chime_msg(URL, msg):
    url = URL
    message = {"Content": msg}
    encoded_msg = json.dumps(message).encode("utf-8")
    resp = http.request("POST", url, body=encoded_msg)
    print(
        {
            "message": msg,
            "status_code": resp.status,
            "response": resp.data,
        }
    )
    return resp