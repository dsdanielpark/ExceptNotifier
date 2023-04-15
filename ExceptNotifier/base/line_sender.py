import requests   

def send_line_msg(TOKEN, msg):
    api_url = "https://notify-api.line.me/api/notify"
    headers = {'Authorization':'Bearer '+ TOKEN}
    message = {
        "message" : msg
    }
    resp = requests.post(api_url, headers= headers , data = message)
    return resp



if __name__ == "__main__": 
    TOKEN = "XXXXXXXXX"
    msg = "Test Message"
    send_line_msg(TOKEN, msg)
