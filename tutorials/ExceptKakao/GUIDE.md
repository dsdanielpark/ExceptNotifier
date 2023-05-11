# ExceptKakao

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1E5Q-lnWStG1MqtnGCr5pzInlfWt2uc2S?usp=sharing)

## Ready

## *Kakaotalk*
- a. Sign up at the following site: [https://developers.kakao.com/](https://developers.kakao.com/)
- b. Click `My Application` on the top bar.
- c. Click `Add an application`, set a name, and create it.
- d. Click `Kakao Login` in the left menu, then change the State of `Kakao Login Activation` to ON on the resulting page.
- e. In `My Application > Product Settings > Kakao Login`, be sure to set `Redirect URI` as follows: [https://example.com/oauth](https://example.com/oauth)
- f. In the left Consent Items menu, set `Send message in KakaoTalk` to optional agreement.
- g. Copy the `REST API Key` in `My Application > App Settings > Summary`.
- h. If you have successfully completed all of the above steps, go to the following document and follow the instructions:
https://github.com/dsdanielpark/ExceptNotifier/blob/main/tutorials/ExceptKakao/kakao_token_generator.ipynb <Br>

<br>

*API TEST*
```python
from ExceptNotifier import send_kakao_msg

_KAKAO_TOKEN_PATH = 'xxx/xx/xxx.json'

send_kakao_msg(_KAKAO_TOKEN_PATH, msg)
```

## In Python

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

## In Ipython

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1E5Q-lnWStG1MqtnGCr5pzInlfWt2uc2S?usp=sharing)