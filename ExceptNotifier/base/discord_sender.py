
from discord import Webhook, RequestsWebhookAdapter


def send_discord_msg(URL, msg):
    webhook = Webhook.from_url(URL, adapter=RequestsWebhookAdapter())
    resp = webhook.send(msg)
    return resp



if __name__ =="__main__":
    URL = "https://discordapp.com/api/webhooks/1096733073741193336/AX32bjqL1EYIEfLulwU6jaX4eBR1HZYzxq5UM9ADsCpUeePcF0YlFQnEGLD5geF65kyl"
    msg = "Sending Test"

    send_discord_msg(URL, msg)
