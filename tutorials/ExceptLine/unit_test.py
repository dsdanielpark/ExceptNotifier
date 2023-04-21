# Copyright 2023 parkminwoo
from ExceptNotifier import ExceptLine, SuccessLine, SendLine
import os, sys


# QA 23-04-22
if __name__ == "__main__":

    """Get your URL from HERE. 
    https://notify-bot.line.me/my/"""

    os.environ["_LINE_NOTIFY_API_TOKEN"] = "xxxxxx"
    # _OPEN_AI_MODEL = "gpt-3.5-turbo"
    # _OPEN_AI_API = "sk-xxxxxxxxx"

    sys.excepthook = ExceptLine.__call__

    try:
        print(1 / 0)
        SuccessLine().__call__()  # 1 success sender

    except ExceptLine as e:  # 2 except sender
        sys.exit()

    SendLine().__call__()  # 3 customized sender
