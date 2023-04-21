# Copyright 2023 parkminwoo
from ExceptNotifier import ExceptSMS, SuccessSMS, SendSMS
import os, sys

# QA 23-04-22
if __name__ == "__main__":

    """https://www.twilio.com/en-us"""

    os.environ["_TWILIO_SID"] = "xxxxx"
    os.environ["_TWILIO_TOKEN"] = "xxxxxx"
    os.environ["_RECIPIENT_PHONE_NUMBER"] = "+xxxxxx"
    os.environ["_SENDER_PHONE_NUMBER"] = "+xxxxx"
    # _OPEN_AI_MODEL = "gpt-3.5-turbo"
    # _OPEN_AI_API = "sk-xxxxxxxxx"

    sys.excepthook = ExceptSMS.__call__

    try:
        print(1 / 20)
        SuccessSMS().__call__()  # 1 success sender

    except ExceptSMS as e:  # 2 except sender
        pass

    SendSMS().__call__()  # 3 customized sender


from ExceptNotifier import ExceptLine, SuccessLine, SendLine
