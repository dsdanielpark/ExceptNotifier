# Python: ExceptNotifier
With Python's try-except statement, experience a significantly more flexible way to receive notifications. You can receive alerts through various messaging platforms such as email, Slack, and Discord. This package offers an extensive range of notification options to suit your needs.

Python package [`ExceptNotifier`](https://github.com/dsdanielpark/ExceptNotifier) can give a single line alarm with an error message, whereas [`knockknock`](https://github.com/huggingface/knockknock) gives a process ending alarm with decorator and cli.

<br>

# Quick Start
ExceptNotifier installation
```
pip insall ExceptNotifier
```


<br>

# Features
### `Mail`
In the except statement, an email is sent along with the error message. Additionally, you can send emails from any desired line. <br><br>
a. Log in with the sender's email ID. <br>
b. Obtain an app password for sending Google Mail at the following [link](https://myaccount.google.com/u/3/apppasswords?utm_source=google-account&utm_medium=myaccountsecurity&utm_campaign=tsv-settings&rapt=AEjHL4N2bMRWO46VaMp_jP06zQK14BWNPv66l2o59iJ99CkO8BjYnmoRUe9dtSchkkbubHZMUhevkAnwVJRHb9ygO3afispNlw). 

```python
from ExceptNotifier import ExceptMail, SuccessMail, SendMail
sys.excepthook = ExceptMail.__call__

try:
    main() # Your Code Here
    SuccessMail().__call__()    # No Exception -> Send Success mail.
except ExceptMail:           # Exception -> Send Fail mail.
    pass

SendMail().__call__()           # When Process Ended -> Any Line mail.
```

<details>
<summary> See Example...</summary>

```python
import sys
from ExceptNotifier import ExceptMail, SuccessMail

# 01. Set variable.
global gmail_receiver, gmail_sender, gmail_app_password_of_sender, SendMail
gmail_receiver = 'parkminwoo1991@gmail.com'
gmail_sender = 'heydudenotice@gmail.com'
gmail_app_password_of_sender = 'xxxxxxxxxxx'
sys.excepthook = ExceptMail.__call__

try:
    # 02. Locate your code.
    print(1/0)             
    SuccessMail().__call__() # Success Mail

# Exception Mail
except ExceptMail as e:                    
    sys.exit()
    print(e)

SendMail().__call__()     # Put Any Line: Sending mail



```
</details>