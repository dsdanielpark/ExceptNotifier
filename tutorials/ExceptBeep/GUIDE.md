## ExceptBeep
No setup is required. Use as follows. <br>

```python
from ExceptNotifier import beep

beep()
```

```python
from ExceptNotifier import ExceptBeep, SendBeep, SuccessBeep

os.environ['BEEP_TIME'] = 3

try:
    print(1/0)
    SuccessBeep().__call__() #sending success beep
except ExceptBeep: #sending except beep
    pass

SendBeep().__call__() #sending beep
```