# ExceptLine
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1PDrJqxDq4NE6BRUrRkFvDBiMHQz0WbZh?usp=sharing) 

## Ready
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1PDrJqxDq4NE6BRUrRkFvDBiMHQz0WbZh?usp=sharing) 

- a. Register [https://notify-bot.line.me/](https://notify-bot.line.me/)
- b. Go to mypage [https://notify-bot.line.me/my/](https://notify-bot.line.me/my/)
- c. Click `Generate Token`, enter Service Name and click `1-on-1 chat with LINE` (anything you like)
- d. Copy Token. <Br><br>


*API TEST*
```python
from ExceptNotifier import send_line_msg

send_line_msg(_LINE_NOTIFY_API_TOKEN:, "Any Test Message")
```

*Notifier*
```python
import sys
from ExceptNotifier import ExceptLine, SuccessLine, SendLine
sys.excepthook = ExceptLine.__call__

# Define the next two variables optionally when using OpenAI's API.
# os.environ['_OPEN_AI_MODEL']="gpt-3.5-turbo"    
# os.environ['_OPEN_AI_API']="sk-xxxxxx"
os.environ['_LINE_NOTIFY_API_TOKEN'] = 'xxxxxxxxxxx'

try:
    print(1/20)  
    SuccessLine().__call__() #1 success sender          
except ExceptLine as e:      #2 except sender            
    sys.exit()

SendLine().__call__()        #3 customized sender          
```


# Python

```python
# Copyright 2023 parkminwoo
from ExceptNotifier import ExceptLine, SuccessLine, SendLine 
import os, sys


# QA 23-04-22
if __name__ == "__main__":

    """Get your URL from HERE. 
    https://notify-bot.line.me/my/"""

    
    os.environ['_LINE_NOTIFY_API_TOKEN'] =  "xxxxxx"
    # _OPEN_AI_MODEL = "gpt-3.5-turbo"
    # _OPEN_AI_API = "sk-xxxxxxxxx"
    
    sys.excepthook = ExceptLine.__call__

    try:
        print(1 / 0)
        SuccessLine().__call__()  # 1 success sender

    except ExceptLine as e:  # 2 except sender
        sys.exit()

    SendLine().__call__()  # 3 customized sender
```

<br>

# Ipython
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1PDrJqxDq4NE6BRUrRkFvDBiMHQz0WbZh?usp=sharing) 
