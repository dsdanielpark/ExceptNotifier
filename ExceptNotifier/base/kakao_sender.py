import requests
import json


def send_kakao_msg(token_path, msg):
    with open(token_path,"r") as kakao:
        tokens = json.load(kakao)

    url="https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers={
        "Authorization" : "Bearer " + tokens["access_token"]
    }
    data = {
        'object_type': 'text',
        'text': msg,
        'link': {
            'web_url': 'https://developers.kakao.com',
            'mobile_web_url': 'https://developers.kakao.com'
        }
    }
    
    data = {'template_object': json.dumps(data)}
    resp = requests.post(url, headers=headers, data=data)
    resp_status = resp.status_code

    return resp_status


if __name__ == "__main__":
    global token_path
    token_path = r'C:\Users\parkm\Desktop\git\ExceptionNotifier\tutorials\token.json'
    
    msg = "Sending Message Test"
    resp_status = send_kakao_msg(token_path, msg)
    print(resp_status)