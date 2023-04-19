import requests

def send_wechat_msg(_WECHAT_WEBHOOK_URL, msg):
    msg_template = {
        "msgtype": "text", 
        "text": {
            "content": ""
        }
    }
    msg_template['text']['content'] = '\n'.join(msg)
    requests.post(_WECHAT_WEBHOOK_URL, json=msg_template)