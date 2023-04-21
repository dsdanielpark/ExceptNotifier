# Copyright 2023 parkminwoo
import sys, os
from ExceptNotifier import ExceptTelegram, SuccessTelegram, SendTelegram


# QA 23-04-22
if __name__ == "__main__":

    """Get your bot from botfather. 
    https://core.telegram.org/bots/tutorial"""

    os.environ["_TELEGRAM_TOKEN"] = "xxxxxxxxxx"
    # _OPEN_AI_MODEL = "gpt-3.5-turbo"
    # _OPEN_AI_API = "sk-xxxxxxxxx"
    sys.excepthook = ExceptTelegram.__call__

    try:
        print(1 / 0)
        SuccessTelegram().__call__()  # 1 success sender

    except ExceptTelegram as e:  # 2 except sender
        sys.exit()

    SendTelegram().__call__()  # 3 customized sender

    send = SendTelegram()  # You can use it like this, too.
    send()
