Development Status :: 3 - Alpha <br>
*Copyright (c) 2023 MinWoo Park*
<br>
# Python: ExceptNotifier
![Corpus-Show](https://img.shields.io/badge/pypi-ExceptNotifier-orange)
![Pypi Version](https://img.shields.io/pypi/v/ExceptNotifier.svg)
[![Python Version](https://img.shields.io/badge/python-3.6%2C3.7%2C3.8-black.svg)](code_of_conduct.md)
![Code convention](https://img.shields.io/badge/code%20convention-pep8-black)

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

# Features
## `Mail Notifier`
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
