# ExceptTelegram
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1jwWGs7eCUJQvj_g7SEMqm3a4Kdrp9ZQP?usp=sharing) 

![](https://github.com/dsdanielpark/ExceptNotifier/tree/main/assets/imgs/telegram.gif)

## Ready
Go through the following process to prepare the `_TELEGRAM_TOKEN` variable.

- a. Open your telegram app and search for BotFather. (A built-in Telegram bot that helps users create custom Telegram bots)
- b. Type /newbot to create a new bot
- c. Give your bot a name & a username
- d. Copy your new Telegram bot’s token
- e. You have to click Start_bot and must enter anything to your bot. <br>

Before use Notifier, Please use this to check if you follow guide. The Telegram bot may have a slight delay and it responded within 2-3 minutes. API TEST

## Test Sender
Go through the following steps to make sure you are communicating properly with the application.
*API TEST*
```python
from ExceptNotifier import send_telegram_msg

_TELEGRAM_TOKEN = "xxxxx:xxxxx-xxxx"
send_telegram_msg(_TELEGRAM_TOKEN, 'test message')
```

# Python

```python
import os
import sys
from ExceptNotifier import ExceptTelegram, SuccessTelegram, SendTelegram


# QA 23-04-22
if __name__ == "__main__":

    """Get your bot from botfather. 
    https://core.telegram.org/bots/tutorial"""

    
    os.environ['_TELEGRAM_TOKEN'] = "xxxxxxxxxx"
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

```

# Ipython
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1jwWGs7eCUJQvj_g7SEMqm3a4Kdrp9ZQP?usp=sharing) 