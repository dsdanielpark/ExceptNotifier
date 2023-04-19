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
If you have Openai's model name and API key in any application, you can get information and *examples* for debugging OpenAI ChatGPT.
- [OPEN AI API](https://platform.openai.com/docs/introduction)


<br><br>

# Quick Start
```
pip install ExceptNotifier
```
or
```
pip install exceptnotifier
```

<br>


# 1 Key Features
To use the desired application, you must define the necessary variables. Ensure that the variable names remain unchanged, and you can use either local or global variables.

## 1-1. Except`[Application Name]`
If you use Python's try except statement as it is, but change except as follows, you can receive notifications through your application.
```
ExceptChime, ExceptTelegram, ExceptDiscord, ExceptSMS, ExceptMail, ExceptKakao, ExceptLine, ExceptSlack, ExceptTeams, ExceptDesktope, ExceptBeep
```

*Example*
```python
from ExceptNotifier import ExceptTelgeram

try:
    print(1/0)
except ExceptTelegram:
    # sending except message to telegram
    sys.exit()
```

<br>

## 1-2. AI Debbugging Infomation Notification
You can receive debugging information from ChatGPT via OpenAI's API when using the Except statement. The syntax remains the same, but you'll need to configure these two variables:
`_OPEN_AI_MODEL`,`_OPEN_AI_API`

*Example*
```python
from ExceptNotifier import ExceptTelgeram
_OPEN_AI_MODEL="gpt-3.5-turbo"
_OPEN_AI_API="sk-xxxxxx"

try:
    print(1/0)
except ExceptTelegram: 
    # sending except message WITH AI DEBUGGING INFO to telegram
    sys.exit()
```
<br>

## 1-3. Success`[Application Name]`
By placing the try except in python at the end of the try statement, applications can be notified that the try statement worked normally.
```
SuccessChime, SuccessTelegram, SuccessDiscord, SuccessSMS, SuccessMail, SuccessKakao, SuccessLine, SuccessSlack, SuccessTeams, SuccessDesktope, SuccessBeep
```
*Example*

```python
from ExceptNotifier import SuccessTelgeram

try:
    print(1/20)
    SuccessTelgeram().__call__()  # sending success message to telegram
except:
    sys.exit()
```

<Br>

## 1-4. Send`[Application Name]`
Place it anywhere on the line of code you want, and you'll be notified when that line of code is reached.
```
SendChime, SendTelegram, SendDiscord, SendSMS, SendMail, SendKakao, SendLine, SendSlack, SendTeams, SendDesktope, SendBeep
```
*Example*

```python
from ExceptNotifier import SendTelgeram

SendTelegram().__call__() # sending message to telegram

noti = SendTelegram()

noti()                    # sending message to telegram

```


<br><br>

# 2. Features
## 2-1. *Telegram Notifier*

- a. Open your telegram app and search for BotFather. (A built-in Telegram bot that helps users create custom Telegram bots) <br>
- b. Type /newbot to create a new bot <br>
- c. Give your bot a name & a username <br>
- d. Copy your new Telegram bot’s token <br>

For more infomation, visit [Telegram Bot Father API](https://core.telegram.org/bots/api)
<br><br>
 
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
<summary> See *Example*...</summary>

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

global _gmail_receiver, _gmail_sender, _gmail_app_password_of_sender
_gmail_receiver = 'xxxxxxx@gmail.com'
_gmail_sender = 'yyyyyy@gmail.com'
_gmail_app_password_of_sender = 'zzzzzz'
sys.excepthook = ExceptMail.__call__

try:
    'your code'
    SuccessMail().__call__()
except ExceptMail:
    pass

SendMail().__call__() 
```
</details>



<br><br>


<br>


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

