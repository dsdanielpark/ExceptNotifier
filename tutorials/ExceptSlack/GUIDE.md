# ExceptSlack
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-dAaKl_gwX481FxH424aCVFqsq-thGXK?usp=sharing) 

## Ready
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-dAaKl_gwX481FxH424aCVFqsq-thGXK?usp=sharing) 
- a. visit https://api.slack.com/
- b. `Create an app` - `From scratch` - `Create App`
- c. Add webhook: Click `Incoming Webhooks` - Activate Incomming `On` - Add New Webhook to Workspace
- d. Copy `Webhook URL` <Br><br>

*API TEST*
```python
from ExceptNotifier import send_slack_msg

send_slack_msg(_SLACK_WEBHOOK_URL, "Any Test Message")
```
*Notifier*
```python
import sys
from ExceptNotifier import ExceptSlack, SuccessSlack, SendSlack
sys.excepthook = ExceptSlack.__call__

# Define the next two variables optionally when using OpenAI's API.
# os.environ['_OPEN_AI_MODEL']="gpt-3.5-turbo"    
# os.environ['_OPEN_AI_API']="sk-xxxxxx"
os.environ['_SLACK_WEBHOOK_URL'] = 'https://hooks.slack.com/services/xxxxxxxxxxxxxxxxxxx'

try:
    print(1/0)  
    SuccessSlack().__call__() #1 success sender          
except ExceptSlack as e:      #2 except sender            
    sys.exit()

SendSlack().__call__()        #3 customized sender     
```

# Python

```python
# Copyright 2023 parkminwoo
from ExceptNotifier import SendSlack, SuccessSlack, ExceptSlack
import os, sys

# QA 23-04-22
if __name__ == "__main__":

    # Get your slack bot and enter _SLACK_WEBHOOK_URL
    """Get your _SLACK_WEBHOOK_URL from HERE. 
    https://api.slack.com/messaging/webhooks#create_a_webhook"""

    
    os.environ['_SLACK_WEBHOOK_URL'] ='xxxxx'
    # _OPEN_AI_MODEL = "gpt-3.5-turbo"
    # _OPEN_AI_API = "sk-xxxxxxxxx"

    sys.excepthook = ExceptSlack.__call__

    try:
        print(1 / 0)
        SuccessSlack().__call__()  # 1 success sender

    except ExceptSlack as e:  # 2 except sender
        sys.exit()

    SendSlack().__call__()  # 3 customized sender


```

# Ipython
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-dAaKl_gwX481FxH424aCVFqsq-thGXK?usp=sharing) 