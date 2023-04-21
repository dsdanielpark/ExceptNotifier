Development Status :: 2 - Pre-Alpha <br>
*Copyright (c) 2023 MinWoo Park, South Korea*<br>
Before QA<br> 

![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/logo2.png)

<h5 align="center">Integrates AI-assisted debugging notifications into Python try-except statements for various messaging applications. </h5>

<p align="center">
<a href="(https://img.shields.io/badge/pypi-ExceptNotifier-orange"></a>
<a href="https://pypi.org/project/exceptnotifier/"><img alt="PyPI" src="https://img.shields.io/pypi/v/exceptnotifier"></a>
<a href="https://pepy.tech/project/exceptnotifier"><img alt="Downloads" src="https://pepy.tech/badge/exceptnotifier"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/main3.png)
##### Provides a notification from the application shown in the captured screen.

# Python Package: ExceptNotifier
 The `ExceptNotifier` Python package offers a flexible approach to receiving notifications by enhancing Python's try-except statement. This package enables you to receive alerts through various messaging applications or emails.
<Br><br>
With `ExceptNotifier`, you can obtain detailed compilation errors, including debug information, sent directly to your preferred messaging platform or email. By integrating OpenAI's ChatGPT, you can receive additional error code information as long as you provide the required API model name and key. This feature ensures that error handling and notifications are more informative and accessible, streamlining your debugging process.

<Br>


# Supporting Applications
Applicable to both [IPython](https://ipython.org/) and [Python](https://www.python.org/), but needs to be ported differently only in `ExceptNotifier`. Please refer to the detailed example. (`SuccessNotifier` and `SendNotifier` have the same syntax.)
- [Telegram](https://telegram.org/)
- [Discord](https://discord.com/)
- [Slack](https://slack.com/)
- [Google Mail](https://mail.google.com/)
- [Line](https://line.me/en/)
- [AWS Chime](https://aws.amazon.com/ko/chime/download-chime/)
- [Microsoft Teams](https://www.microsoft.com/en/microsoft-teams/download-app)
- [Kakao Talk](https://www.kakaocorp.com/page/service/service/KakaoTalk?lang=en)
- [Wecaht](https://www.wechat.com/)
- SMS Sending using [Twilio](https://www.twilio.com/en-us)
- Desktop Notification using [Plyer](https://github.com/kivy/plyer)
- Beep Sound from [system](https://docs.python.org/3/library/winsound.html)
- [Opea AI API](https://openai.com/blog/openai-api)
        - If you have OpenAI API Key and model name, you can get information and code examples for debugging in any application.


<br>

# Quick Start
```bash
$ pip install ExceptNotifier
```
```bash
$ pip install exceptnotifier
```

<br><br><br>

# Contents

- [App Setup Overview](#app-setup-overview)
- [Tutorial](#tutorial)
- [Python Core](#python-core)
  * [Except`Notifier`](#exceptnotifier)
    + [AI Debbugging Infomation Notification](#ai-debbugging-infomation-notification)
  * [Success`Notifier`](#successnotifier)
  * [Send`Notifier`](#sendnotifier)
  * [Sender](#sender)
- [IPython Core](#ipython-core)
  * [Except`Notifier` in Ipython](#exceptnotifier-in-ipython)
  * [Success`Notifier` in Ipython](#successnotifier-in-ipython)
  * [Send`Notifier` in Ipython](#sendnotifier-in-ipython)
  * [Sender in Ipython](#sender-in-ipython)
- [Applied in each application](#applied-in-each-application)
  * [*Telegram*](#telegram)
    + [a. Notifier without OpenAI API](#a-notifier-without-openai-api)
    + [b. Notifier with OpenAI API](#b-notifier-with-openai-api)
  * [*Mail*](#mail)
  * [*Discord*](#discord)
  * [*Chime*](#chime)
  * [*Slack*](#slack)
  * [*Line*](#line)
  * [*SMS*](#sms)
  * [*Teams*](#teams)
  * [*Kakaotalk*](#kakaotalk)
  * [*Wechat*](#wechat)
  * [*Beep*](#beep)
  * [*Desktop*](#desktop)
- [Contributing Guide](#contributing-guide)
- [License](#license)
- [Code of Conduct](#code-of-conduct)
- [Contacts](#contacts)

<br><br><br>


<br>

# App Setup Overview

- The variables in the following table must not be contaminated.
- Depending on the situation, consider designating them as global variables for use.
- As you already know, API Keys or security tokens must be secured. Note that the key values which exposured in github will be expired after insecured.
- We are trying to maintain the current architecture as much as possible by considering various methods such as inheriting decorators and Excepthook. We set it as an environment variable as follows, and we are refactoring and testing for a better method.

| App | Required Enviroment Variables | Free or Paid | Ease of Setup | Time Required for Setup|Guide Tutorial Link|
|:--:|:--|:--:|:--:|:--:|:---:|
|Beep|N/A|Free|N/A|0min|[ExceptBeep](https://github.com/dsdanielpark/ExceptNotifier/blob/main/tutorials/ExceptBeep/GUIDE.md)|
|Desktop|N/A|Free|N/A|0min|[ExceptDesktop](https://github.com/dsdanielpark/ExceptNotifier/blob/main/tutorials/ExceptDesktop/GUIDE.md)|
|Telegram|`_TELEGRAM_TOKEN`|Freemium|Easy|2min|[ExceptTelegram](https://github.com/dsdanielpark/ExceptNotifier/blob/main/tutorials/ExceptTelegram/GUIDE.md) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1jwWGs7eCUJQvj_g7SEMqm3a4Kdrp9ZQP?usp=sharing) |
|Discord|`_DISCORD_WEBHOOK_URL`|Freemium|Easy|1min|[ExceptDiscord](https://github.com/dsdanielpark/ExceptNotifier/blob/main/tutorials/ExceptTelegram/GUIDE.md) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1lwsIBpql_1zgEdIWRw6O_jBOZKJdHqBh?usp=sharing) |
|AWS Chime|`_CHIME_WEBHOOK_URL`|Freemium|Easy|1min|[ExceptChime](https://github.com/dsdanielpark/ExceptNotifier/blob/main/tutorials/ExceptChime/GUIDE.md) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1hUMMQ6He9M4MlspZ88J9kO8juxvC5b3a?usp=sharing)|
|Slack|`_SLACK_WEBHOOK_URL`|Freemium|Easy|3min|[ExceptSlack](https://github.com/dsdanielpark/ExceptNotifier/blob/main/tutorials/ExceptSlack/GUIDE.md) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-dAaKl_gwX481FxH424aCVFqsq-thGXK?usp=sharing) |
|G-Mail|`_GAMIL_RECIPIENT_ADDR`, `_GMAIL_SENDER_ADDR`, `_GMAIL_APP_PASSWORD_OF_SENDER` |Restricted free|Medium|3min|[ExceptMail](https://github.com/dsdanielpark/ExceptNotifier/blob/main/tutorials/ExceptMail/GUIDE.md)|
|Line|`_LINE_NOTIFY_API_TOKEN`|Freemium|Medium|4min|[ExceptLine](https://github.com/dsdanielpark/ExceptNotifier/blob/main/tutorials/ExceptLine/GUIDE.md) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1PDrJqxDq4NE6BRUrRkFvDBiMHQz0WbZh?usp=sharing) |
|SMS|`_TWILIO_SID`, `_TWILIO_TOKEN`, `_RECIPIENT_PHONE_NUMBER`, `_SENDER_PHONE_NUMBER`|Not free|Medium|5min|[ExceptSMS](https://github.com/dsdanielpark/ExceptNotifier/blob/main/tutorials/ExceptSMS/GUIDE.md)|
|Microsoft Teams|`_TEAMS_WEBHOOK_URL`|Not Free|Medium|5min|[ExceptTeams](https://github.com/dsdanielpark/ExceptNotifier/blob/main/tutorials/ExceptTeams/GUIDE.md)|
|KakaoTalk|`_KAKAO_TOKEN_PATH`|Freemium|Hell|>=10min(Token refreshes daily)|[ExceptKakao](https://github.com/dsdanielpark/ExceptNotifier/blob/main/tutorials/ExceptKakao/GUIDE.md)|


If you add the following two variables to the required variables for each application in the table above, you can receive error location and explanation, as well as examples, from OpenAI's model

| API | Required Variables | Free or Paid | Ease of Setup | Time Required for Setup|Guide Tutorial Link|
|:--:|:--|:--:|:--:|:--:|:---:|
| OpenAI API |`Required variables for each application`+ `_OPEN_AI_MODEL`,`_OPEN_AI_API`|Not free|Easy|2min|[APIOpenAI](https://github.com/dsdanielpark/ExceptNotifier/blob/main/documents/APIOpenAI/GUIDE.md)|

<br>

# Tutorial
I will update tutorial ASAP. `README.md` is sufficient, but read the application's official documentation if necessary. However, we are preparing a more detailed and friendly tutorial.

1. Main-tutorials: [Notebook](https://github.com/DSDanielPark/ExceptNotifier/blob/main/tutorial/ExceptNotifier.ipynb)
2. Sub-tutorial-folder: Tutorials for each function can be found in this [folder](https://github.com/DSDanielPark/ExceptNotifier/tree/main/tutorial). The tutorial is synchronized with the Python file name provided by ExceptNotifier.

 **In this example, some API keys were exposed by creating and removing a test application, but for security reasons, your API key should not be exposed to the outside world.**

<Br>

# Python Core
To use the desired application, you must define the necessary variables. Ensure that the variable names remain unchanged, and you can use either local or global variables. If you are using `Telegram`, an example is attached as an image.


## Except`Notifier`
![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/ex1.png)
If you use Python's try except statement as it is, but change except as follows, you can receive notifications through your application.
- Format: Except`[appName]` <Br>
- Type: class
*ExampleClass*
```
ExceptChime, ExceptTelegram, ExceptDiscord, ExceptSMS, ExceptMail, ExceptKakao, ExceptLine, ExceptSlack, ExceptTeams, ExceptDesktope, ExceptBeep
```

*Example*
```python
import sys, os
from ExceptNotifier import ExceptTelegram
sys.excepthook = ExceptTelegram.__call__

os.environ['_TELEGRAM_TOKEN'] = "xxxx"

try:
    print(1/0)
except ExceptTelegram:    # sending except message to telegram
    sys.exit()
```


### AI Debbugging Infomation Notification
![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/ex2.png)

You can receive debugging information from ChatGPT via OpenAI's API when using the Except statement. The syntax remains the same, but you'll need to configure these two variables:
`_OPEN_AI_MODEL`,`_OPEN_AI_API`

*Example*
```python
import sys, os
from ExceptNotifier import ExceptTelegram
sys.excepthook = ExceptTelegram.__call__

os.envirion['_TELEGRAM_TOKEN'] = "xxxx"
os.envirion['_OPEN_AI_MODEL']="gpt-3.5-turbo"
os.envirion['_OPEN_AI_API']="sk-xxxxxx"

try:
    print(1/0)
except ExceptTelegram: # sending msg WITH AI DEBUGGING to telegram
    sys.exit()
```


## Success`Notifier`
![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/ex3.png)

- Format: Success`[appName]`
- Type: Class <br>
*ExampleClass* <br>
By placing the try except in python at the end of the try statement, applications can be notified that the try statement worked normally.
```
SuccessChime, SuccessTelegram, SuccessDiscord, SuccessSMS, SuccessMail, SuccessKakao, SuccessLine, SuccessSlack, SuccessTeams, SuccessDesktope, SuccessBeep
```
*Example*

```python
import sys, os
from ExceptNotifier import SuccessTelgeram
sys.excepthook = ExceptTelegram.__call__
os.environ['_TELEGRAM_TOKEN'] = "xxxx"

try:
    print(1/20)
    SuccessTelgeram().__call__()  # sending success message to telegram
except:
    sys.exit()
```

## Send`Notifier`
![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/ex4.png)
- Format: Send`[appName]` 
- Type: class <br>
*ExampleClass* <br>
Place it anywhere on the line of code you want, and you'll be notified when that line of code is reached.
```
SendChime, SendTelegram, SendDiscord, SendSMS, SendMail, SendKakao, SendLine, SendSlack, SendTeams, SendDesktope, SendBeep
```
*Example*

```python
import sys, os
from ExceptNotifier import SendTelegram
sys.excepthook = ExceptTelegram.__call__
os.environ['_TELEGRAM_TOKEN'] = "xxxx"

SendTelegram().__call__() # sending message to telegram

noti = SendTelegram()
noti()                    # sending message to telegram
```


## Sender
![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/ex5.png)
It is recommended to conduct a simple message sending test through the `sender`. Assuming that you can communicate with REST API or WEBHOOK normally, `ExceptNotifier` can work normally.
- Every application's ExceptNotifier uses the sender method.
- Format: send_`[appName]`_msg 
- Type: Function <br>
*Example* <br>
```
send_chime_msg, send_telegram_msg, send_discord_msg, send_sms_msg, send_gmail_msg, send_kakao_msg, send_line_msg, send_slack_msg, send_teams_msg, send_desktop_msg, beep
```
*Example*
```python
from ExceptNotifier import send_telegram_msg

send_telegram_msg(_TELEGRAM_TOKEN, "Any Test Message")
```

<br><br>


# IPython Core
You can use all the same except for the python code and `ExceptNotifier` mentioned above. In other words, the `SuccesNotifier`, `SendNotifier`, and `Sender` functions can all be used same in IPython without any special processing. Only `ExceptNotifier` is need to be defined.
- Example in Telegram [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1jwWGs7eCUJQvj_g7SEMqm3a4Kdrp9ZQP?usp=sharing) 

## Except`Notifier` in Ipython
You have to use `raise` in Ipython ExceptNotifier.
- Format: Except[appName]
- Type: function <br>

*Example code without Open AI API*

![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/ipyex1.png)

```python
from ExceptNotifier import ExceptTelegramIpython
import os
os.environ['_TELEGRAM_TOKEN'] = "xxxxx"
get_ipython().set_custom_exc((Exception,), ExceptTelegramIpython)

try:
  print(1/0)
except:
  raise
```

*Example code With Open AI API*

![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/ipyex2.png)

```python
from ExceptNotifier import ExceptTelegramIpython
import os
get_ipython().set_custom_exc((Exception,), ExceptTelegramIpython)

os.environ['_OPEN_AI_MODEL'] = "gpt-3.5-turbo"    
os.environ['_OPEN_AI_API'] = "sk-xxxxx"
os.environ['_TELEGRAM_TOKEN'] = "xxxxx"

try:
  print(1/0)
except:
  raise
```

## Success`Notifier` in Ipython
![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/ipyex3.png)
- Same syntax in Python. See Python Core above.
```python
import sys
import os
from ExceptNotifier import SuccessTelegram
os.environ['_TELEGRAM_TOKEN'] = "xxxxx"

try:
  print(1/20) # Your Code Here
  SuccessTelegram().__call__()    # Sending Success message
except:
  raise
```


## Send`Notifier` in Ipython

![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/ipyex4.png)

- Same syntax in Python. See Python Core above.
```python
import sys
import os
from ExceptNotifier import SendTelegram 
os.environ['_TELEGRAM_TOKEN'] = "xxxxx"

SendTelegram().__call__()         # Sending telegram message
```

## Sender in Ipython

![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/ipyex5.png)

- Same syntax in Python. See Python Core above.
```python
from ExceptNotifier import send_telegram_msg

_TELEGRAM_TOKEN =  "xxxxx"

send_telegram_msg(_TELEGRAM_TOKEN, "This is test message")
```

<br>

# Applied in each application
You can receive debugging information from ChatGPT via OpenAI's API when using the Except statement. The syntax remains the same, but you'll need to configure these two variables:
`_OPEN_AI_MODEL`,`_OPEN_AI_API`


<br>

## *Telegram*
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1jwWGs7eCUJQvj_g7SEMqm3a4Kdrp9ZQP?usp=sharing) 
As all classes function the same, the example will only use one image, like in Telegram.
![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/fig44.png)
- a. Open your telegram app and search for BotFather. (A built-in Telegram bot that helps users create custom Telegram bots) <br>
- b. Type /newbot to create a new bot <br>
- c. Give your bot a name & a username <br>
- d. Copy your new Telegram bot’s token <br>
- e. You have to click `Start_bot` and must enter anything to your bot.
   - Before use Notifier, Please use this to check if you follow guide. The Telegram bot may have a slight delay and it responded within 2-3 minutes.
*API TEST*
```python
from ExceptNotifier import send_telegram_msg

_TELEGRAM_TOKEN = "xxxxx:xxxxx-xxxx"
send_telegram_msg(_TELEGRAM_TOKEN, 'msg')
```

For more infomation, visit [Telegram Bot Father API](https://core.telegram.org/bots/api)
<br><br>
 
### a. Notifier without OpenAI API
*Notifier*
```python
from ExceptNotifier import ExceptTelegram, SuccessTelegram, SendTelegram
import sys, os
sys.excepthook = ExceptTelegram.__call__
os.environ['_TELEGRAM_TOKEN'] = "xxxx"

try:
    print(1/0)  
    SuccessTelegram().__call__() #1. success sender          

except ExceptTelegram as e:      #2. except sender            
    sys.exit()

SendTelegram().__call__()        #3. customized sender     
```


### b. Notifier with OpenAI API
- If you just set `_OPEN_AI_API` and `_OPEN_AI_MODEL` environment variables in all application use case, AI MODEL will automatically send debugging information as a message. Currently, it is mainly based on the `GPT-3.5-TURBO` model, but we plan to update it so that other models can be used later.
*Notifier*
```python
from ExceptNotifier import ExceptTelegram, SuccessTelegram, SendTelegram
import sys, os
sys.excepthook = ExceptTelegram.__call__
os.environ['_TELEGRAM_TOKEN'] = "xxxx"
os.envirion['_OPEN_AI_MODEL']="gpt-3.5-turbo"
os.envirion['_OPEN_AI_API']="sk-xxxxxx"

try:
    print(1/0)  
    SuccessTelegram().__call__() #1. success sender          

except ExceptTelegram as e:      #2. except sender            
    sys.exit()

SendTelegram().__call__()        #3. customized sender     

```
<br>

## *Mail*
In the except statement, an email is sent along with the error message. Additionally, you can send emails from any desired line. <br>
- a. Log in with the sender's email ID. <br>
- b. Obtain an app password for sending Google Mail at the following [link](https://myaccount.google.com/u/3/apppasswords?utm_source=google-account&utm_medium=myaccountsecurity&utm_campaign=tsv-settings&rapt=AEjHL4N2bMRWO46VaMp_jP06zQK14BWNPv66l2o59iJ99CkO8BjYnmoRUe9dtSchkkbubHZMUhevkAnwVJRHb9ygO3afispNlw) or [google document](https://support.google.com/accounts/answer/185833?hl=en). 

*API TEST*
```python
from ExceptNotifier import send_gmail_msg

_GMAIL_SENDER_ADDR = 'xxxx@gmail.com'
_GAMIL_RECIPIENT_ADDR = 'xxxx@gmail.com'
_GMAIL_APP_PASSWORD_OF_SENDER = 'xxxx'
subject_msg = "Test Title"
body_msg = "Test Body" 

send_gmail_msg(
    _GMAIL_SENDER_ADDR,
    _GAMIL_RECIPIENT_ADDR,
    _GMAIL_APP_PASSWORD_OF_SENDER,
    subject_msg,
    body_msg)
```
*Notifier*
```python
import sys, os
from ExceptNotifier import ExceptMail, SuccessMail, SendMail
sys.excepthook = ExceptMail.__call__

# Define the next two variables optionally when using OpenAI's API.
# os.environ['_OPEN_AI_MODEL']="gpt-3.5-turbo"    
# os.environ['_OPEN_AI_API']="sk-xxxxxx"
os.environ['_GAMIL_RECIPIENT_ADDR'] = 'xxxxxxx@gmail.com'
os.environ['_GMAIL_SENDER_ADDR'] = 'yyyyyy@gmail.com'
os.environ['_GMAIL_APP_PASSWORD_OF_SENDER'] = 'zzzzzz'

try:
    main()                      # Your Code Here
    SuccessMail().__call__()    # No Exception -> Send Success mail.
except ExceptMail:              # Exception -> Send Fail mail.
    pass

SendMail().__call__()           # When Process Ended -> Any Line mail.
```

<details>
<summary> See Example...</summary>

```python
import sys, os
from ExceptNotifier import ExceptMail, SuccessMail, SendMail

# Define the next two variables optionally when using OpenAI's API.
# os.environ['_OPEN_AI_MODEL']="gpt-3.5-turbo"    
# os.environ['_OPEN_AI_API']="sk-xxxxxx"
os.environ['_GAMIL_RECIPIENT_ADDR'] = 'xxxxxxx@gmail.com'
os.environ['_GMAIL_SENDER_ADDR'] = 'yyyyyy@gmail.com'
os.environ['_GMAIL_APP_PASSWORD_OF_SENDER'] = 'zzzzzz'

sys.excepthook = ExceptMail.__call__

try:
    # 02.Locate your code
    print(1/0)   
    SuccessMail().__call__()   # Success Mail

except ExceptMail as e:        # Exception Mail       
    sys.exit()
    print(e)

SendMail().__call__()          # Put Any Line: Sending mail
```
</details>

<details>
<summary> Snippet for Python developers...</summary>

```python
import sys, os
from ExceptNotifier import ExceptMail, SuccessMail, SendMail
sys.excepthook = ExceptMail.__call__

# Define the next two variables optionally when using OpenAI's API.
# os.environ['_OPEN_AI_MODEL']="gpt-3.5-turbo"    
# os.environ['_OPEN_AI_API']="sk-xxxxxx"
os.environ['_GAMIL_RECIPIENT_ADDR'] = 'xxxxxxx@gmail.com'
os.environ['_GMAIL_SENDER_ADDR'] = 'yyyyyy@gmail.com'
os.environ['_GMAIL_APP_PASSWORD_OF_SENDER'] = 'zzzzzz'

try:
    'your code'
    SuccessMail().__call__()
except ExceptMail:
    pass

SendMail().__call__() 
```
</details>

<br>

## *Discord*
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1lwsIBpql_1zgEdIWRw6O_jBOZKJdHqBh?usp=sharing) 
- a. Select the channel to receive notifications.
- b. Click `Edit Channel` in the upper right corner of the chat window.
- c. Click `Integrations` - `Webhook` - `New Webhook`.
- d. Then click `Copy Webhook`.
*API TEST*
```python
from ExceptNotifier import send_discord_msg

send_discord_msg(_DISCORD_WEBHOOK_URL, "Any Test Message") 
```
*Notifier*
```python
import sys, os
from ExceptNotifier import ExceptDiscord, SuccessDiscord, SendDiscord
sys.excepthook = ExceptDiscord.__call__

# Define the next two variables optionally when using OpenAI's API.
# os.environ['_OPEN_AI_MODEL']="gpt-3.5-turbo"    
# os.environ['_OPEN_AI_API']="sk-xxxxxx"
os.environ['_DISCORD_WEBHOOK_URL'] = "xxxxxxxxxxxxxxxxx"


try:
    print(1/20)  
    SuccessDiscord().__call__() #1 success sender          
except ExceptDiscord as e:      #2 except sender            
    sys.exit()

SendDiscord().__call__()        #3 customized sender       
```

<br>

## *Chime*
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1hUMMQ6He9M4MlspZ88J9kO8juxvC5b3a?usp=sharing)

- a. Select the Chat room to receive notifications.
- b. Click `Room Setting` in the upper right corner.
- c. Click `Manage Webhook and bot`
- d. Create Add Webhook, set it up, then click `Copy Webhook`.
*API TEST*
```python
from ExceptNotifier import send_chime_msg

send_chime_msg(_CHIME_WEBHOOK_URL, "Any Test Message")

```
*Notifier*
```python
import sys, os
from ExceptNotifier import SuccessChime, ExceptChime, SendChime
sys.excepthook = ExceptChime.__call__

# Define the next two variables optionally when using OpenAI's API.
# os.environ['_OPEN_AI_MODEL']="gpt-3.5-turbo"    
# os.environ['_OPEN_AI_API']="sk-xxxxxx"
os.environ['_CHIME_WEBHOOK_URL'] = "xxxxxxxxxxxxxxxxxx"


try:
    print(1/0)  
    SuccessChime().__call__() #1 success sender          
except ExceptChime as e:      #2 except sender            
    sys.exit()

SendChime().__call__()        #3 customized sender       
```
<br>

## *Slack*
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-dAaKl_gwX481FxH424aCVFqsq-thGXK?usp=sharing) 
- a. visit https://api.slack.com/
- b. `Create an app` - `From scratch` - `Create App`
- c. Add webhook: Click `Incoming Webhooks` - Activate Incomming `On` - Add New Webhook to Workspace
- d. Copy `Webhook URL`
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
<Br>

## *Line*
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1PDrJqxDq4NE6BRUrRkFvDBiMHQz0WbZh?usp=sharing) 
- a. Register [https://notify-bot.line.me/](https://notify-bot.line.me/)
- b. Go to mypage [https://notify-bot.line.me/my/](https://notify-bot.line.me/my/)
- c. Click `Generate Token`, enter Service Name and click `1-on-1 chat with LINE` (anything you like)
- d. Copy Token.

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

<Br>

## *SMS*
- a. Sign up for Twilio. [https://www.twilio.com/en-us](https://www.twilio.com/en-us)
- b. Click Console in the upper right corner.
- c. Copy the variables provided in the console.


*API TEST*
```python
from ExceptNotifier import send_sms_msg

_TWILIO_SID = 'xxxx'
_TWILIO_TOKEN = "xxxx"
_SENDER_PHONE_NUMBER = "xxxx"
_RECIPIENT_PHONE_NUMBER = "xxxx"

send_sms_msg(
    _TWILIO_SID,
    _TWILIO_TOKEN,
    _SENDER_PHONE_NUMBER,
    _RECIPIENT_PHONE_NUMBER,
    "Any Test Message")
```

*Notifier*
```python
import sys
from ExceptNotifier import ExceptSMS, SuccessSMS, SendSMS
sys.excepthook = ExceptSMS.__call__

# Define the next two variables optionally when using OpenAI's API.
# os.environ['_OPEN_AI_MODEL']="gpt-3.5-turbo"    
# os.environ['_OPEN_AI_API']="sk-xxxxxx"
os.environ['_TWILIO_SID'] = 'xxxx'
os.environ['_TWILIO_TOKEN'] = 'yyyyyy'
os.environ['_RECIPIENT_PHONE_NUMBER']="+aaaaaa",
os.environ['_SENDER_PHONE_NUMBER']="+bbbbbb",  

try:
    print(1/10)  
    SuccessSMS().__call__() #1 success sender          
except ExceptSMS as e:      #2 except sender
    sys.exit()

SendSMS().__call__()        #3 customized sender        
```
<Br>

## *Teams*
- a. Create the channel that you want to notify.
- b. `App` - `Search: webhook` - `Incoming Webhook` [https://teams.microsoft.com/l/app/203a1e2c-26cc-47ca-83ae-be98f960b6b2?source=app-details-dialog](https://teams.microsoft.com/l/app/203a1e2c-26cc-47ca-83ae-be98f960b6b2?source=app-details-dialog)
- c. Click `Request Approval` <br>
After you can use webhook incomming. Proceed to next steps.
Microsoft Teams allows limited application access per organization, so it can only be used if the webhook incoming application is available.
- c. Go to the team channel to receive notifications, and click `Connectors` in Settings.
- d. `Connectors` After configuring webhook incoming in Connector, copy the webhook URL.


*API TEST*
```python
from ExceptNotifier import send_teams_msg

_TEAMS_WEBHOOK_URL = 'xxxx'

send_teams_msg(_TEAMS_WEBHOOK_URL, "Any Test Message")
```

*Notifier*
```python
import sys
from ExceptNotifier import ExceptTeams, SuccessTeams, SendTeams
sys.excepthook = ExceptTeams.__call__

# Define the next two variables optionally when using OpenAI's API.
# os.environ['_OPEN_AI_MODEL']="gpt-3.5-turbo"    
# os.environ['_OPEN_AI_API']="sk-xxxxxx"
os.environ['_TEAMS_WEBHOOK_URL'] = 'microsoft webhook _TEAMS_WEBHOOK_URL'

try:
    print(1/20)  
    SuccessTeams().__call__() #1 success sender          
except ExceptTeams as e:      #2 except sender            
    sys.exit()

SendTeams().__call__()        #3 customized sender        
```

<Br>

## *Kakaotalk*
- a. Sign up at the following site: [https://developers.kakao.com/](https://developers.kakao.com/)
- b. Click `My Application` on the top bar.
- c. Click `Add an application`, set a name, and create it.
- d. Click `Kakao Login` in the left menu, then change the State of `Kakao Login Activation` to ON on the resulting page.
- e. In `My Application > Product Settings > Kakao Login`, be sure to set `Redirect URI` as follows: [https://example.com/oauth](https://example.com/oauth)
- f. In the left Consent Items menu, set `Send message in KakaoTalk` to optional agreement.
- g. Copy the `REST API Key` in `My Application > App Settings > Summary`.
- h. If you have successfully completed all of the above steps, go to the following document and follow the instructions:
 https://github.com/dsdanielpark/ExceptNotifier/blob/main/tutorials/kakao_token_generator.ipynb

*API TEST*
```python
from ExceptNotifier import send_kakao_msg

_KAKAO_TOKEN_PATH = 'xxx/xx/xxx.json'

send_kakao_msg(_KAKAO_TOKEN_PATH, msg)
```
*Notifier*
```python
import sys
from ExceptNotifier import ExceptKakao, SuccessKakao, SendKakao
sys.excepthook = ExceptKakao.__call__

# Define the next two variables optionally when using OpenAI's API.
# os.environ['_OPEN_AI_MODEL']="gpt-3.5-turbo"    
# os.environ['_OPEN_AI_API']="sk-xxxxxx"
os.environ['_KAKAO_TOKEN_PATH'] = 'xxxx/xxx/xxx.json''

try:
    print(1/0)  
    SuccessKakao().__call__() #1 success sender          
except ExceptKakao as e:      #2 except sender            
    sys.exit()

SendKakao().__call__()        #3 customized sender         
```


## *Wechat*
a. Get Webhook URL by visiting [here](https://work.weixin.qq.com/api/doc/90000/90136/91770)
*API TEST*
```python
from ExceptNotifier import send_wechat_msg

send_wechat_msg(_WECHAT_WEBHOOK_URL, msg)
```
*Notifier*
```python
import sys
from ExceptNotifier import ExceptWechat, SuccessWechat, SendWechat

# Define the next two variables optionally when using OpenAI's API.
# os.environ['_OPEN_AI_MODEL']="gpt-3.5-turbo"    
# os.environ['_OPEN_AI_API']="sk-xxxxxx"
os.environ['_WECHAT_WEBHOOK_URL'] = "xxxxxxxxxxx"
sys.excepthook = ExceptWechat.__call__

try:
    print(1/0)  
    SuccessWechat().__call__() #1 success sender          
except ExceptWechat as e:      #2 except sender            
    sys.exit()

SendWechat().__call__()        #3 customized sender       
```

<Br>

## *Beep*
No setup is required. Use as follows.
*TEST*
```python
from ExceptNotifier import beep

beep(sec=1, freq=1000) 
```
*Notifier*
```python
from Exceptnotifier import ExceptBeep, SuccessBeep, SendBeep(), beep()
os.environ['BEEP_TIME'] = 1
sys.excepthook = ExceptBeep.__call__

try:
    print(1/20)  
    SuccessBeep().__call__() #1 success beep-beep          

except ExceptBeep as e:      #2 except beep-beep                
    sys.exit()

SendBeep().__call__()        #3 customized beep-beep      

beep()

```

<Br>


## *Desktop*
No setup is required. Use as follows.
*TEST*
```python
from ExceptNotifier import send_desktop_msg

title_msg = "Test Title"
body_msg = "Test Body"
DISP_TIME = 5

send_desktop_msg(title_msg, body_msg, DISP_TIME)
```
*Notifier*
```python
from ExceptNotifier import ExceptDesktop, SuccessDesktop, SendDesktop
sys.excepthook = ExceptDesktop.__call__
# Define the next two variables optionally when using OpenAI's API.
# os.environ['_OPEN_AI_MODEL']="gpt-3.5-turbo"    
# os.environ['_OPEN_AI_API']="sk-xxxxxx"

try:
    print(1/0)  
    SuccessDesktop().__call__() #1 success sender          

except ExceptDesktop as e:      #2 except sender            
    sys.exit()

SendDesktop().__call__()        #3 customized sender         
```

<br>


<Br><br><br>


# Contributing Guide
I will announce contributing rules when the code development status changes to beta soon. Until then, please create an issue for feature requests and bug reports. I would greatly appreciate it if you use it a lot and give your opinions generously. Thank you sincerely.

# License
MIT

# Code of Conduct
Everyone participating in the `ExceptNotifier` project, and in particular in the issue tracker, pull requests, and social media activity, is expected to treat other people with respect and more generally to follow the guidelines articulated in [the Python Community Code of Conduct](https://www.python.org/psf/conduct/).

# Contacts
Core maintainers: [Daniel Park, South Korea](https://github.com/DSDanielPark) <br>
Email parkminwoo1991@gmail.com <br>
- Developer note: [Link](https://github.com/dsdanielpark/ExceptNotifier/blob/main/documents/DEV_NOTE.md)

#### Could you kindly add this badge to your repository?
```
![Except-Notifier](https://img.shields.io/badge/pypi-ExceptNotifier-orange)
```

I would appreciate it if you could share the document widely by specifying that the source is the ExceptNotifier official github.

##### The package is currently in the development and QA stages, and the development stage will be updated at the top of this page. If it is determined that the product is stable through feature improvement, addition, and issue resolution, the development stage will reach stage 5. If no new updates or issues arise, it will be adjusted upward to stage 6 or higher.

