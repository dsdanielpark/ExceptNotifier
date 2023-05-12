## Google Bard
Example code in telegram app.

### Notifier with Google Bard API
- Just set `_BARD_API_KEY`. If you would like to receive guidance in Korean, you can optionally set the following. Set `_BARD_ADVICE_LANG` as `ko` or `jp`.
*Notifier*
```python
from ExceptNotifier import ExceptTelegram, SuccessTelegram, SendTelegram
import sys, os
sys.excepthook = ExceptTelegram.__call__
os.environ['_TELEGRAM_TOKEN'] = "xxxxxxxxx"
os.environ['_BARD_API_KEY']="xxxxxxxxx"
# os.environ['_BARD_ADVICE_LANG']="ko"

try:
    print(1/0)  
    SuccessTelegram().__call__() #1. success sender          
except ExceptTelegram as e:      #2. except sender            
    sys.exit()

SendTelegram().__call__()        #3. customized sender     
```


### Remark
- Python package [BardAPI](https://github.com/dsdanielpark/BARD_API)
- https://github.com/dsdanielpark/BARD_API/blob/main/scripts/google_api.ipynb

