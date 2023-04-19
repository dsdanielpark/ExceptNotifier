Development Status :: 3 - Alpha <br>
*Copyright (c) 2023 MinWoo Park, South Korea*
<br>

# Python Package: ExceptNotifier
![Except-Notifier](https://img.shields.io/badge/pypi-ExceptNotifier-orange)
![Pypi Version](https://img.shields.io/pypi/v/ExceptNotifier.svg)
[![Python Version](https://img.shields.io/badge/python-3.6%20to%203.7-black)](code_of_conduct.md)
![Code convention](https://img.shields.io/badge/code%20convention-pep8-black)
##### Provides a notification from the application shown in the following screen,

![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/main2.png)
 The `ExceptNotifier` Python package offers a flexible approach to receiving notifications by enhancing Python's try-except statement. This package enables you to receive alerts through various messaging applications or emails.
<Br><br>
With `ExceptNotifier`, you can obtain detailed compilation errors, including debug information, sent directly to your preferred messaging platform or email. By integrating OpenAI's ChatGPT, you can receive additional error code information as long as you provide the required API model name and key. This feature ensures that error handling and notifications are more informative and accessible, streamlining your debugging process.

<br><br>

### Supporting Applications

- [Telegram](https://telegram.org/)
- [Discord](https://discord.com/)
- [Slack](https://slack.com/)
- [Google Mail](https://mail.google.com/)
- SMS Sending using [Twilio](https://www.twilio.com/en-us)
- Desktop Notification using [Plyer](https://github.com/kivy/plyer)
- [Line](https://line.me/en/)
- [AWS Chime](https://aws.amazon.com/ko/chime/download-chime/)
- [Microsoft Teams](https://www.microsoft.com/en/microsoft-teams/download-app)
- [Kakao Talk](https://www.kakaocorp.com/page/service/service/KakaoTalk?lang=en)
- Beep Sound from [system](https://docs.python.org/3/library/winsound.html)

<Br>

### AI Debugging
If you have OpenAI API Key and model name, you can get information and code examples for debugging in any application.
- [OPEN AI API](https://platform.openai.com/docs/introduction)


<br><br>

# Quick Start
```bash
pip install ExceptNotifier
pip install exceptnotifier

conda install ExceptNotifier
conda install exceptnotifier
```

<br>


# App Setup Overview

- The variables in the following table must not be contaminated.
- Depending on the situation, consider designating them as global variables for use.
- If you are using Telegram, an example is attached as an image.
- As you already know, API Keys or security tokens must be secured. Note that the key values which exposured in github will be expired after insecured.

| App | Required Variables | Free or Paid | Ease of Setup | Time Required for Setup|Guide Tutorial Link|
|:--:|:--|:--:|:--:|:--:|:---:|
|Beep|N/A|Free|N/A|0 min|[ExceptBeep](https://github.com/dsdanielpark/ExceptNotifier/blob/main/documents/ExceptBeep/GUIDE.md)|
|Desktop|N/A|Free|N/A|0 min|[ExceptDesktop](https://github.com/dsdanielpark/ExceptNotifier/blob/main/documents/ExceptDesktop/GUIDE.md)|
|Telegram|`_TELEGRAM_TOKEN`|Freemium|Easy|2min|[ExceptTelegram](https://github.com/dsdanielpark/ExceptNotifier/blob/main/documents/ExceptTelegram/GUIDE.md)|
|Discord|`_DISCORD_WEBHOOK_URL`|Freemium|Easy|1min|[ExceptDiscord](https://github.com/dsdanielpark/ExceptNotifier/blob/main/documents/ExceptTelegram/GUIDE.md)|
|AWS Chime|`_CHIME_WEBHOOK_URL`|Freemium|Easy|1min|[ExceptChime](https://github.com/dsdanielpark/ExceptNotifier/blob/main/documents/ExceptChime/GUIDE.md)|
|Slack|`_SLACK_WEBHOOK_URL`|Freemium|Easy|3min|[ExceptSlack](https://github.com/dsdanielpark/ExceptNotifier/blob/main/documents/ExceptSlack/GUIDE.md)|
|G-Mail|`_GAMIL_RECIPIENT_ADDR`, `_GMAIL_SENDER_ADDR`, `_GMAIL_APP_PASSWORD_OF_SENDER` |Restricted free|Medium|3min|[ExceptMail](https://github.com/dsdanielpark/ExceptNotifier/blob/main/documents/ExceptMail/GUIDE.md)|
|Line|`_LINE_NOTIFY_API_TOKEN`|Freemium|Medium|4min|[ExceptLine](https://github.com/dsdanielpark/ExceptNotifier/blob/main/documents/ExceptLine/GUIDE.md)|
|SMS|`_TWILIO_SID`, `_TWILIO_TOKEN`, `_RECIPIENT_PHONE_NUMBER`, `_SENDER_PHONE_NUMBER`|Not free|Medium|5min|[ExceptSMS](https://github.com/dsdanielpark/ExceptNotifier/blob/main/documents/ExceptSMS/GUIDE.md)|
|Microsoft Teams|`_TEAMS_WEBHOOK_URL`|Not Free|Medium|5min|[ExceptTeams](https://github.com/dsdanielpark/ExceptNotifier/blob/main/documents/ExceptTeams/GUIDE.md)|
|KakaoTalk|`_KAKAO_TOKEN_PATH`|Freemium|Hell|>=10min(Token refreshes daily.)|[ExceptKakao](https://github.com/dsdanielpark/ExceptNotifier/blob/main/documents/ExceptKakao/GUIDE.md)|


If you add the following two variables to the required variables for each application in the table above, you can receive error location and explanation, as well as examples, from OpenAI's model

| API | Required Variables | Free or Paid | Ease of Setup | Time Required for Setup|Guide Tutorial Link|
|:--:|:--|:--:|:--:|:--:|:---:|
| OpenAI API |`Required variables for each application`+ `_OPEN_AI_MODEL`,`_OPEN_AI_API`|Not free|Easy|2min|[APIOpenAI](https://github.com/dsdanielpark/ExceptNotifier/blob/main/documents/APIOpenAI/GUIDE.md)|


<br><br>

# 1. Key Features
To use the desired application, you must define the necessary variables. Ensure that the variable names remain unchanged, and you can use either local or global variables. If you are using `Telegram`, an example is attached as an image.

## 1-1. Except`[appName]`
If you use Python's try except statement as it is, but change except as follows, you can receive notifications through your application.
```
ExceptChime, ExceptTelegram, ExceptDiscord, ExceptSMS, ExceptMail, ExceptKakao, ExceptLine, ExceptSlack, ExceptTeams, ExceptDesktope, ExceptBeep
```

*Example*
```python
from ExceptNotifier import ExceptTelgeram
_TELEGRAM_TOKEN = "xxxx"

try:
    print(1/0)
except ExceptTelegram:    # sending except message to telegram
    sys.exit()
```
![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/ex1.png)

<br>

## 1-2. AI Debbugging Infomation Notification
You can receive debugging information from ChatGPT via OpenAI's API when using the Except statement. The syntax remains the same, but you'll need to configure these two variables:
`_OPEN_AI_MODEL`,`_OPEN_AI_API`

*Example*
```python
from ExceptNotifier import ExceptTelgeram
_TELEGRAM_TOKEN = "xxxx"
_OPEN_AI_MODEL="gpt-3.5-turbo"
_OPEN_AI_API="sk-xxxxxx"

try:
    print(1/0)
except ExceptTelegram: # sending msg WITH AI DEBUGGING to telegram
    sys.exit()
```

![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/ex2.png)

<br>

## 1-3. Success`[appName]`
By placing the try except in python at the end of the try statement, applications can be notified that the try statement worked normally.
```
SuccessChime, SuccessTelegram, SuccessDiscord, SuccessSMS, SuccessMail, SuccessKakao, SuccessLine, SuccessSlack, SuccessTeams, SuccessDesktope, SuccessBeep
```
*Example*

```python
from ExceptNotifier import SuccessTelgeram
_TELEGRAM_TOKEN = "xxxx"

try:
    print(1/20)
    SuccessTelgeram().__call__()  # sending success message to telegram
except:
    sys.exit()
```

![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/ex3.png)

<Br>

## 1-4. Send`[appName]`
Place it anywhere on the line of code you want, and you'll be notified when that line of code is reached.
```
SendChime, SendTelegram, SendDiscord, SendSMS, SendMail, SendKakao, SendLine, SendSlack, SendTeams, SendDesktope, SendBeep
```
*Example*

```python
from ExceptNotifier import SendTelgeram
_TELEGRAM_TOKEN = "xxxx"

SendTelegram().__call__() # sending message to telegram

noti = SendTelegram()
noti()                    # sending message to telegram
```

![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/ex4.png)


<br><br>

# 2. Features
You can receive debugging information from ChatGPT via OpenAI's API when using the Except statement. The syntax remains the same, but you'll need to configure these two variables:
`_OPEN_AI_MODEL`,`_OPEN_AI_API`



## 2-1. *Telegram Notifier*

- a. Open your telegram app and search for BotFather. (A built-in Telegram bot that helps users create custom Telegram bots) <br>
- b. Type /newbot to create a new bot <br>
- c. Give your bot a name & a username <br>
- d. Copy your new Telegram bot’s token <br>

For more infomation, visit [Telegram Bot Father API](https://core.telegram.org/bots/api)
<br><br>
 
### a. Without OpenAI API

```python
from ExceptNotifier import ExceptTelegram, SuccessTelegram, SendTelegram
import sys
sys.excepthook = ExceptTelegram.__call__

_TELEGRAM_TOKEN = "xxxx"

try:
    print(1/0)  
    SuccessTelegram().__call__() #1. success sender          

except ExceptTelegram as e:      #2. except sender            
    sys.exit()

SendTelegram().__call__()        #3. customized sender     
```


![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/fig44.png)


### b. With OpenAI API
```python
from ExceptNotifier import ExceptTelegram, SuccessTelegram, SendTelegram
import sys
sys.excepthook = ExceptTelegram.__call__

_TELEGRAM_TOKEN = "xxxx"
_OPEN_AI_MODEL="gpt-3.5-turbo"
_OPEN_AI_API="sk-xxxxxx"

try:
    print(1/0)  
    SuccessTelegram().__call__() #1. success sender          

except ExceptTelegram as e:      #2. except sender            
    sys.exit()

SendTelegram().__call__()        #3. customized sender     

```


## 2-2. *Mail Notifier*
In the except statement, an email is sent along with the error message. Additionally, you can send emails from any desired line. <br>
- a. Log in with the sender's email ID. <br>
- b. Obtain an app password for sending Google Mail at the following [link](https://myaccount.google.com/u/3/apppasswords?utm_source=google-account&utm_medium=myaccountsecurity&utm_campaign=tsv-settings&rapt=AEjHL4N2bMRWO46VaMp_jP06zQK14BWNPv66l2o59iJ99CkO8BjYnmoRUe9dtSchkkbubHZMUhevkAnwVJRHb9ygO3afispNlw) or [google document](https://support.google.com/accounts/answer/185833?hl=en). 

```python
from ExceptNotifier import ExceptMail, SuccessMail, SendMail
sys.excepthook = ExceptMail.__call__

try:
    main() # Your Code Here
    SuccessMail().__call__()    # No Exception -> Send Success mail.
except ExceptMail:              # Exception -> Send Fail mail.
    pass

SendMail().__call__()           # When Process Ended -> Any Line mail.
```

<details>
<summary> See Example...</summary>

```python
import sys
from ExceptNotifier import ExceptMail, SuccessMail, SendMail

# 01. Set variable
_gmail_receiver = 'xxxxx@gmail.com'
_gmail_sender = 'xxxxx@gmail.com'
_gmail_app_password_of_sender = 'xxxxx'

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
import sys
from ExceptNotifier import ExceptMail, SuccessMail, SendMail
sys.excepthook = ExceptMail.__call__

_GAMIL_RECIPIENT_ADDR = 'xxxxxxx@gmail.com'
_GMAIL_SENDER_ADDR = 'yyyyyy@gmail.com'
_GMAIL_APP_PASSWORD_OF_SENDER = 'zzzzzz'

try:
    'your code'
    SuccessMail().__call__()
except ExceptMail:
    pass

SendMail().__call__() 
```
</details>

<br>

## 2-3. *Discord Notifier*
- a. Select the channel to receive notifications.
- b. Click "Edit Channel" in the upper right corner of the chat window.
- c. Click Integrations - Webhook - New Webhook.
- d. Then click Copy Webhook.

```python
import sys
from ExceptNotifier import ExceptDiscord, SuccessDiscord, SendDiscord
global _DISCORD_WEBHOOK_URL 
_DISCORD_WEBHOOK_URL = "xxxxxxxxxxxxxxxxx"
sys.excepthook = ExceptDiscord.__call__

try:
    print(1/20)  
    SuccessDiscord().__call__() #1 success sender          
except ExceptDiscord as e:      #2 except sender            
    sys.exit()

SendDiscord().__call__()        #3 customized sender       
```

<br>

## 2-4. *Chime Notifier*
- a. Select the Chat room to receive notifications.
- b. Click "Room Setting" in the upper right corner.
- c. Click "Manage Webhook and bot."
- d. Create Add Webhook, set it up, then click Copy Webhook.
```python
import sys
from ExceptNotifier import SuccessChime, ExceptChime, SendChime
_CHIME_WEBHOOK_URL = "xxxxxxxxxxxxxxxxxx"
_OPEN_AI_API = "xxxxxxxxxxxxx"
_OPEN_AI_MODEL = "gpt-3.5-turbo"
sys.excepthook = ExceptChime.__call__

try:
    print(1/0)  
    SuccessChime().__call__() #1 success sender          
except ExceptChime as e:      #2 except sender            
    sys.exit()

SendChime().__call__()        #3 customized sender       
```
<br>

## 2-5. *Slack Notifier*
- a. visit https://api.slack.com/
- b. `Create an app` - `From scratch` - `Create App`
- c. Add webhook: Click `Incoming Webhooks` - Activate Incomming `On` - Add New Webhook to Workspace
- d. Copy `Webhook URL`

```python
import sys
from ExceptNotifier import ExceptSlack, SuccessSlcak, SendSlack
sys.excepthook = ExceptSlack.__call__

_SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/xxxxxxxxxxxxxxxxxxx'

try:
    print(1/0)  
    SuccessSlcak().__call__() #1 success sender          
except ExceptSlack as e:      #2 except sender            
    sys.exit()

SendSlack().__call__()        #3 customized sender     
```
<Br>

## 2-6. *Line Notifier*
- a. Register [https://notify-bot.line.me/](https://notify-bot.line.me/).
- b. Go to mypage [https://notify-bot.line.me/my/](https://notify-bot.line.me/my/).
- c. Click `Generate Token`, enter Service Name and click `1-on-1 chat with LINE` (anything you like).
- d. Copy Token.

```python
import sys
from ExceptNotifier import ExceptLine, SuccessLine, SendLine
sys.excepthook = ExceptLine.__call__

_LINE_NOTIFY_API_TOKEN = 'xxxxxxxxxxx'

try:
    print(1/20)  
    SuccessLine().__call__() #1 success sender          
except ExceptLine as e:      #2 except sender            
    sys.exit()

SendLine().__call__()        #3 customized sender          
```

<Br>

## 2-7. *SMS Notifier*
- a. Sign up for Twilio. [https://www.twilio.com/en-us](https://www.twilio.com/en-us).
- b. Click Console in the upper right corner.
- c. Copy the variables provided in the console.

```python
import sys
from ExceptNotifier import ExceptSMS, SuccessSMS, SendSMS
sys.excepthook = ExceptSMS.__call__

_TWILIO_SID = 'xxxx'
_TWILIO_TOKEN = 'yyyyyy'
_RECIPIENT_PHONE_NUMBER="+aaaaaa",
_SENDER_PHONE_NUMBER="+bbbbbb",  

try:
    print(1/10)  
    SuccessSMS().__call__() #1 success sender          
except ExceptSMS as e:      #2 except "wb") as f:
    sys.exit()

SendSMS().__call__()        #3 customized sender        
```
<Br>

## 2-8. *Teams Notifier*
- a. Create the channel that you want to notify.
- b. App - Search: webhook - Incoming Webhook [https://teams.microsoft.com/l/app/203a1e2c-26cc-47ca-83ae-be98f960b6b2?source=app-details-dialog](https://teams.microsoft.com/l/app/203a1e2c-26cc-47ca-83ae-be98f960b6b2?source=app-details-dialog).
- c. Click `Request Approval` <br>
After you can use webhook incomming. Proceed to next steps.
Microsoft Teams allows limited application access per organization, so it can only be used if the webhook incoming application is available.
- c. Go to the team channel to receive notifications, and click `Connectors` in Settings.
- d. `Connectors` After configuring webhook incoming in Connector, copy the webhook URL.

```python
import sys
from ExceptNotifier import ExceptTeams, SuccessTeams, SendTeams
sys.excepthook = ExceptTeams.__call__

_TEAMS_WEBHOOK_URL = 'microsoft webhook _TEAMS_WEBHOOK_URL'

try:
    print(1/20)  
    SuccessTeams().__call__() #1 success sender          
except ExceptTeams as e:      #2 except sender            
    sys.exit()

SendTeams().__call__()        #3 customized sender        
```

<Br>

<Br>

## 2-9. *Kakaotalk Notifier*
- a. Sign up at the following site: [https://developers.kakao.com/](https://developers.kakao.com/).
- b. Click "My Application" on the top bar.
- c. Click "Add an application," set a name, and create it.
- d. Click "Kakao Login" in the left menu, then change the State of "Kakao Login Activation" to ON on the resulting page.
- e. In My Application > Product Settings > Kakao Login, be sure to set Redirect URI as follows: [https://example.com/oauth](https://example.com/oauth).
- f. In the left Consent Items menu, set "Send message in KakaoTalk" to selective agreement.
- g. Copy the REST API Key in My Application > App Settings > Summary, and go to the following document.

**In this example, some API keys were exposed by creating and removing a test application, but for security reasons, your API key should not be exposed to the outside world.**

- h. If you have successfully completed all of the above steps, go to the following document and follow the instructions:
 https://github.com/dsdanielpark/ExceptNotifier/blob/main/tutorials/kakao_token_generator.ipynb
<Br>

```python
import sys
from ExceptNotifier import ExceptKakao, SuccessKakao, SendKakao
sys.excepthook = ExceptKakao.__call__

_KAKAO_TOKEN_PATH = 'xxxx/xxx/xxx.json''

try:
    print(1/0)  
    SuccessKakao().__call__() #1 success sender          
except ExceptKakao as e:      #2 except sender            
    sys.exit()

SendKakao().__call__()        #3 customized sender         
```


## 2-10. *Beep Notifier*
No setup is required. Use as follows.

```python
from Exceptnotifier import ExceptBeep, SuccessBeep, SendBeep(), beep()
BEEP_TIME = 1
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


## 2-11. *Desktop Notifier*
No setup is required. Use as follows.

```python
from ExceptNotifier import ExceptDesktop, SuccessDesktop, SendDesktop
sys.excepthook = ExceptDesktop.__call__

try:
    print(1/0)  
    SuccessDesktop().__call__() #1 success sender          

except ExceptDesktop as e:      #2 except sender            
    sys.exit()

SendDesktop().__call__()        #3 customized sender         
```

<Br><br><br>

### Inspiring
- Thanks to [Myunghak Lee](https://github.com/myeonghak) for providing great ideas on providing debugging information through open ai API.

<br>

### Contacts
- Maintainer [Daniel Park, South Korea](https://github.com/DSDanielPark) <br>
- Email parkminwoo1991@gmail.com

  
#### Could you kindly add this badge to your repository?
  ```
![Except-Notifier](https://img.shields.io/badge/pypi-ExceptNotifier-orange)
  ```

##### The package is currently in the development and QA stages, and the development stage will be updated at the top of this page. If it is determined that the product is stable through feature improvement, addition, and issue resolution, the development stage will reach stage 5. If no new updates or issues arise, it will be adjusted upward to stage 6 or higher.
