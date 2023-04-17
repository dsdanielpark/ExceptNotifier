
from twilio.rest import Client

def send_sms_msg(SID, TOKEN, FROM, TO, msg):
    client = Client(SID, TOKEN)
    client.messages.create(
        to=TO,
        from_=FROM,  
        body=msg
    )


if __name__ == "__main__":
    """https://www.twilio.com/en-us"""
    
    SID = 'xxxxx'
    TOKEN = 'yyyyy'
    client = Client(SID, TOKEN)
    FROM = "+zzzzz"
    TO = "+aaaaa"
    msg="ExceptNotifier Test"

    send_sms_msg(SID, TOKEN, FROM, TO, msg)
