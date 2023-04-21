# Copyright 2023 parkminwoo
from ExceptNotifier import SendSlack, SuccessSlack, ExceptSlack
import os, sys

# QA 23-04-22
if __name__ == "__main__":

    # Get your slack bot and enter _SLACK_WEBHOOK_URL
    """Get your _SLACK_WEBHOOK_URL from HERE. 
    https://api.slack.com/messaging/webhooks#create_a_webhook"""

    os.environ["_SLACK_WEBHOOK_URL"] = "xxxxx"
    # _OPEN_AI_MODEL = "gpt-3.5-turbo"
    # _OPEN_AI_API = "sk-xxxxxxxxx"

    sys.excepthook = ExceptSlack.__call__

    try:
        print(1 / 0)
        SuccessSlack().__call__()  # 1 success sender

    except ExceptSlack as e:  # 2 except sender
        sys.exit()

    SendSlack().__call__()  # 3 customized sender
