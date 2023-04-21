# Copyright 2023 parkminwoo
from IPython.core.ultratb import AutoFormattedTB
from ExceptNotifier import send_sms_msg, receive_openai_advice
import os
import datetime
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def ExceptSMSIpython(shell, etype, evalue, tb):
    """ExceptNotifier function for overriding custom execute in ipython

    :param shell: Excecuted shell 
    :type shell: _type_
    :param etype: Error type
    :type etype: _type_
    :param evalue: Error value
    :type evalue: _type_
    :param tb: TraceBack
    :type tb: _type_

    """
    itb = AutoFormattedTB(mode = 'Plain')
    shell.showtraceback(etype, evalue, tb)
    stb = itb.structured_traceback(etype, evalue, tb)
    sstb = itb.stb2text(stb)
    start_time = datetime.datetime.now()
    data = {'text' : f"[Except Notifier] ** Error ** Python Code Exception Detected \n \n\nIMPORTANT WARNING \nPython Exception Detected in Your Code. \n\nHi there, \nThis is an exception catch notifier. \n\n * Code Status: Fail.🛠 \n * Detail: Python Code Ran Exceptions. \n * Time: {start_time.strftime(DATE_FORMAT)} \n\n ** {sstb}" }
    
    send_sms_msg(
            os.environ["_TWILIO_SID"],
            os.environ["_TWILIO_TOKEN"],
            os.environ["_SENDER_PHONE_NUMBER"],
            os.environ["_RECIPIENT_PHONE_NUMBER"],
            data["text"],
        )
    try:
        error_message = f"error sheel=={shell}, error_type_document=={etype.__doc__}, error_value=={evalue}, error message in ipython cell=={sstb}"
        advice_msg = receive_openai_advice(os.environ["_OPEN_AI_MODEL"], os.environ["_OPEN_AI_API"], error_message)
        send_sms_msg(
            os.environ["_TWILIO_SID"],
            os.environ["_TWILIO_TOKEN"],
            os.environ["_SENDER_PHONE_NUMBER"],
            os.environ["_RECIPIENT_PHONE_NUMBER"],
            advice_msg,
        )
    except Exception as e:
        print(e)
        pass