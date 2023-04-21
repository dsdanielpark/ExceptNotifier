# Copyright 2023 parkminwoo
from ExceptNotifier import ExceptChime, SuccessChime, SendChime
import os, sys

if __name__ == "__main__":

    # Get your slack bot and enter _CHIME_WEBHOOK_URL
    """Get your Webhook _CHIME_WEBHOOK_URL from your chatroom. 
    https://docs.aws.amazon.com/chime/latest/ag/webhooks.html"""

    os.environ["_CHIME_WEBHOOK_URL"] = "xxxx"
    # os.environ['_OPEN_AI_API'] = "sk-xxxxx"
    # os.environ['_OPEN_AI_MODEL'] = "gpt-3.5-turbo"
    sys.excepthook = ExceptChime.__call__

    try:
        print(1 / 20)
        SuccessChime().__call__()  # 1 success sender

    except ExceptChime as e:  # 2 except sender
        sys.exit()

    SendChime().__call__()  # 3 customized sender
