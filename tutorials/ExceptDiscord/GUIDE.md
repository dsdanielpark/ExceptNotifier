# ExceptDiscord
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1lwsIBpql_1zgEdIWRw6O_jBOZKJdHqBh?usp=sharing) 
![](https://github.com/dsdanielpark/ExceptNotifier/tree/main/assets/imgs/discord.gif)

## Ready
Go through the following process to prepare the `_TELEGRAM_TOKEN` variable.

- a. Select the channel to receive notifications.
- b. Click Edit Channel in the upper right corner of the chat window.
- c. Click Integrations - Webhook - New Webhook.
- d. Then click Copy Webhook. API TEST <Br>


# Python

```python
# QA 23-04-22
# Copyright 2023 parkminwoo
from ExceptNotifier import ExceptDiscord, SuccessDiscord, SendDiscord
import os, sys

if __name__ == "__main__":

    # Get your slack bot and enter _DISCORD_WEBHOOK_URL
    """Get your _DISCORD_WEBHOOK_URL from HERE. 
    https://discord.com/developers/docs/resources/webhook"""

  
    os.environ['_DISCORD_WEBHOOK_URL'] = 'xxxxxxx'
    # _OPEN_AI_MODEL = "gpt-3.5-turbo"
    # _OPEN_AI_API = "sk-xxxxxxxxx"

    sys.excepthook = ExceptDiscord.__call__

    try:
        print(1 / 0)
        SuccessDiscord().__call__()  # 1 success sender

    except ExceptDiscord as e:  # 2 except sender
        sys.exit()

    SendDiscord().__call__()  # 3 customized sender
```

# Ipython
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1lwsIBpql_1zgEdIWRw6O_jBOZKJdHqBh?usp=sharing) 