# ExceptSMS
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/13NuBhAxhwo67oc4jn3y8zpJiJrR-LHrP?usp=sharing)

## Ready
- a. Sign up for Twilio. [https://www.twilio.com/en-us](https://www.twilio.com/en-us)
- b. Click Console in the upper right corner.
- c. Copy the variables provided in the console. <br><br>


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
# Python

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

# Ipython
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/13NuBhAxhwo67oc4jn3y8zpJiJrR-LHrP?usp=sharing)