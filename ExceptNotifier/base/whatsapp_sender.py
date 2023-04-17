import logging
import requests


def send_whatsapp_msg(
    msg, sender_phone_number_id, TOKEN, receiver_number, recipient_type="individual"
):
    url =  f"https://graph.facebook.com/v16.0/{sender_phone_number_id}/messages"
    

    data = { "messaging_product": "whatsapp", 
            "to": receiver_number, 
            "type": "template", 
            "template": 
                        { "name": "hello_world", 
                          "language": 
                                    { "code": "en_US" }
                        } 
            }
    headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(TOKEN),
        }
    resp = requests.post(f"{url}", headers=headers, json=data)
    return resp