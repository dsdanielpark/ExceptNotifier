# Copyright 2023 parkminwoo
from ExceptNotifier import ExceptDiscord, SuccessDiscord, SendDiscord
import os, sys

if __name__ == "__main__":

    # Get your slack bot and enter _DISCORD_WEBHOOK_URL
    """Get your _DISCORD_WEBHOOK_URL from HERE. 
    https://discord.com/developers/docs/resources/webhook"""

    os.environ["_DISCORD_WEBHOOK_URL"] = "xxxxxxx"
    # _OPEN_AI_MODEL = "gpt-3.5-turbo"
    # _OPEN_AI_API = "sk-xxxxxxxxx"

    sys.excepthook = ExceptDiscord.__call__

    try:
        print(1 / 0)
        SuccessDiscord().__call__()  # 1 success sender

    except ExceptDiscord as e:  # 2 except sender
        sys.exit()

    SendDiscord().__call__()  # 3 customized sender
