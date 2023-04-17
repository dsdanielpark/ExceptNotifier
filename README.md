Development Status :: 3 - Alpha <br>
*Copyright (c) 2023 MinWoo Park*
<br>

# Python Package: ExceptNotifier
![Except-Notifier](https://img.shields.io/badge/pypi-ExceptNotifier-orange)
![Pypi Version](https://img.shields.io/pypi/v/ExceptNotifier.svg)
[![Python Version](https://img.shields.io/badge/python-3.6%2C3.7%2C3.8-black.svg)](code_of_conduct.md)
![Code convention](https://img.shields.io/badge/code%20convention-pep8-black)



![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/readme4.png)



Python package `ExceptNotifier` can provides a more flexible way to receive notifications by overriding Python's try-except statement. You can receive alerts through various messaging platforms like email, Slack,Telegram, and Discord. This package offers an extensive range of notification options to suit your needs. 
<br>
Regardless of whether an exception occurs or not, with `ExceptNotifier`, you can send the entire detailed compile error to a messenger or email at a desired specific location. 



<br>

# Quick Start
ExceptNotifier installation
```
pip install ExceptNotifier
```


<br>

# Package Structure

```
📦ExceptNotifier
                               # Notifiers
 ┣ 📜chime_notifier.py
 ┣ 📜discord_notifier.py
 ┣ 📜kakao_notifier.py
 ┣ 📜line_notifier.py
 ┣ 📜mail_notifier.py
 ┣ 📜slack_notifier.py
 ┣ 📜sms_notifier.py
 ┣ 📜teams_notifier.py
 ┣ 📜telegram_notifier.py
 ┣ 📜__init__.py
 ┣ 📜__main__.py
                               # Sending message methods
 ┣ 📂base
 ┃ ┣ 📜chime_sender.py
 ┃ ┣ 📜discord_sender.py
 ┃ ┣ 📜kakao_sender.py
 ┃ ┣ 📜line_sender.py
 ┃ ┣ 📜mail_sender.py
 ┃ ┣ 📜slack_sender.py
 ┃ ┣ 📜sms_sender.py
 ┃ ┣ 📜teams_sender.py
 ┃ ┣ 📜telegram_sender.py
 ┃ ┗ 📜whatsapp_sender.py
                               # Utilities for setting
 ┣ 📂utils
 ┗ ┗  📜kakao_token.py
```

# Features
### Telegram Notifier

a. Open your telegram app and search for BotFather. (A built-in Telegram bot that helps users create custom Telegram bots) <br>
b. Type /newbot to create a new bot <br>
c. Give your bot a name & a username <br>
d. Copy your new Telegram bot’s token <br>
For more infomation, visit [Telegram Bot Father API](https://core.telegram.org/bots/api)
<br><br>

 
```python
from ExceptNotifier import ExceptTelegram, SuccessTelegram, SendTelegram
import sys
sys.excepthook = ExceptTelegram.__call__

TELEGRAM_TOKEN = "xxxx"

try:
    print(1/0)  
    SuccessTelegram().__call__() #1. success sender          

except ExceptTelegram as e:      #2. except sender            
    sys.exit()

SendTelegram().__call__()        #3. customized sender     
```
![](https://github.com/dsdanielpark/ExceptNotifier/blob/main/assets/imgs/fig9.png)

### Mail Notifier
In the except statement, an email is sent along with the error message. Additionally, you can send emails from any desired line. <br><br>
a. Log in with the sender's email ID. <br>
b. Obtain an app password for sending Google Mail at the following [link](https://myaccount.google.com/u/3/apppasswords?utm_source=google-account&utm_medium=myaccountsecurity&utm_campaign=tsv-settings&rapt=AEjHL4N2bMRWO46VaMp_jP06zQK14BWNPv66l2o59iJ99CkO8BjYnmoRUe9dtSchkkbubHZMUhevkAnwVJRHb9ygO3afispNlw) or [google document](https://support.google.com/accounts/answer/185833?hl=en). 

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
global gmail_receiver, gmail_sender, gmail_app_password_of_sender
gmail_receiver = 'xxxxxx@gmail.com'
gmail_sender = 'yyyyyy@gmail.com'
gmail_app_password_of_sender = 'zzzzzzzzzz'
sys.excepthook = ExceptMail.__call__

try:
    print(1/0) # 02.Locate your code      
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

global gmail_receiver, gmail_sender, gmail_app_password_of_sender
gmail_receiver = 'xxxxxxx@gmail.com'
gmail_sender = 'yyyyyy@gmail.com'
gmail_app_password_of_sender = 'zzzzzz'
sys.excepthook = ExceptMail.__call__


try:
    'your code'
    SuccessMail().__call__()
except ExceptMail:
    pass

SendMail().__call__() 
```
</details>



<br><br><br>
### Contacts
Maintainer: [Daniel Park, South Korea](https://github.com/DSDanielPark) <br>
E-mail parkminwoo1991@gmail.com
<br>
  
#### Could you kindly add this badge to your repository?
  ```
![Except-Notifier](https://img.shields.io/badge/pypi-ExceptNotifier-orange)
  ```
