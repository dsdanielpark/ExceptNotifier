# ExceptDesktop
No setup is required. Use as follows. <br>

*Test*
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