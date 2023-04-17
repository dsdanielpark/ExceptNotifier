
from twilio.rest import Client

def send_sms_msg(SID: str, TOKEN: str, FROM: str, TO: str, msg: str)->dict:
    """Send SMS through twilio platform.
    https://www.twilio.com/en-us

    :param SID: Twilio personal SID
    :type SID: str
    :param TOKEN: Twilio personal TOKEN
    :type TOKEN: str
    :param FROM: Sender phone number
    :type FROM: str
    :param TO: Recipient phone number
    :type TO: str
    :param msg: SMS content
    :type msg: str
    :return: Response dict
    :rtype: dict
    """
    
    client = Client(SID, TOKEN)
    resp = client.messages.create(
        to=TO,
        from_=FROM,  
        body=msg
    )
    return resp


if __name__ == "__main__":
    """https://www.twilio.com/en-us"""

    SID = 'xxxxx'
    TOKEN = 'yyyyy'
    client = Client(SID, TOKEN)
    FROM = "+zzzzz"
    TO = "+aaaaa"
    msg="ExceptNotifier Test"

    send_sms_msg(SID, TOKEN, FROM, TO, msg)
