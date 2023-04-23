# Copyright 2023 parkminwoo
from IPython.core.ultratb import AutoFormattedTB
from ExceptNotifier import send_chime_msg, receive_openai_advice
import os
import datetime

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def ExceptChimeIpython(shell, etype, evalue, tb, tb_offset=1):
    """ExceptNotifier function for overriding custom execute in ipython

    :param shell: Excecuted shell 
    :type shell: _type_
    :param etype: Error type
    :type etype: _type_
    :param evalue: Error value
    :type evalue: _type_
    :param tb: TraceBack
    :type tb: _type_
    :param tb_offset: Offset of traceback, defaults to 1
    :type tb_offset: int, optional
    """
    itb = AutoFormattedTB(mode="Plain", tb_offset=1)
    shell.showtraceback((etype, evalue, tb), tb_offset=tb_offset)
    stb = itb.structured_traceback(etype, evalue, tb)
    sstb = itb.stb2text(stb)
    start_time = datetime.datetime.now()
    data = {
        "text": f"[Except Notifier] :warning: Error! Python Code Exception Detected \n\nIMPORTANT WARNING \nPython Exception Detected in Your Code. \n\nHi there, \nThis is an exception catch notifier. \n\n - :x: Code Status: Fail. \n - :x: Detail: Python Code Ran Exceptions. \n - :clock2: Time: {start_time.strftime(DATE_FORMAT)} \n\n :no_entry:  {sstb}"
    }

    send_chime_msg(os.environ["_CHIME_WEBHOOK_URL"], data["text"])

    try:
        error_message = f"error sheel=={shell}, error_type_document=={etype.__doc__}, error_value=={evalue}, error message in ipython cell=={sstb}"
        advice_msg = receive_openai_advice(
            os.environ["_OPEN_AI_MODEL"], os.environ["_OPEN_AI_API"], error_message
        )
        send_chime_msg(os.environ["_CHIME_WEBHOOK_URL"], advice_msg)

    except Exception as e:
        print(e)
        pass
