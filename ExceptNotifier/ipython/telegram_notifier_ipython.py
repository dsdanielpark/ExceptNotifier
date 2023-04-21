from IPython.core.ultratb import AutoFormattedTB
from IPython.core.magic import register_cell_magic
from ExceptNotifier import send_telegram_msg, receive_openai_advice
import os
import datetime
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def ExceptTelegramIpython(shell, etype, evalue, tb, tb_offset=1):
    itb = AutoFormattedTB(mode = 'Plain', tb_offset = 1)
    shell.showtraceback((etype, evalue, tb), tb_offset=tb_offset)
    stb = itb.structured_traceback(etype, evalue, tb)
    sstb = itb.stb2text(stb)
    start_time = datetime.datetime.now()
    data = {'text' : f"[Except Notifier] ⚠️ Error! Python Code Exception Detected \n \n\nIMPORTANT WARNING \nPython Exception Detected in Your Code. \n\nHi there, \nThis is an exception catch notifier. \n\n - ☑️ Code Status: Fail.🛠 \n - ☑️ Detail: Python Code Ran Exceptions. \n - 🕐 Time: {start_time.strftime(DATE_FORMAT)} \n\n ⛔️ {sstb}" }
    
    send_telegram_msg(os.environ['_TELEGRAM_TOKEN'], data['text'])

    try:
        error_message = f"error sheel=={shell}, error_type_document=={etype.__doc__}, error_value=={evalue}, error message in ipython cell=={sstb}"
        advice_msg = receive_openai_advice(os.environ["_OPEN_AI_MODEL"], os.environ["_OPEN_AI_API"], error_message)
        send_telegram_msg(os.environ["_TELEGRAM_TOKEN"], advice_msg)

    except Exception as e:
        print(e)
        pass