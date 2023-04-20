import requests
import traceback
import re
import datetime
from email.message import EmailMessage
import os
import sys
from ExceptNotifier import ExceptTelegram, SuccessTelegram, SendTelegram


if __name__ == "__main__":

    """Get your bot from botfather. 
    https://core.telegram.org/bots/tutorial"""

    
    os.environ['_TELEGRAM_TOKEN'] = "6190978954:AAFtaudWW02ORmqkrQVr7ja-bkQfga9LrXY"
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
