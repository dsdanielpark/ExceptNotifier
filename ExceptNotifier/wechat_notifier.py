# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import requests
import traceback
import re
import datetime
from email.message import EmailMessage
import sys
from ExceptNotifier import send_wechat_msg, receive_openai_advice

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class ExceptWechat(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __call__(etype, value, tb):
        """Override excepthook to send error message to Telegram.

        :param etype: Error Type
        :type etype: _type_
        :param value: Error Value
        :type value: _type_
        :param tb: Traceback Information
        :type tb: _type_
        """
        excType = re.sub(
            "(<(type|class ')|'exceptions.|'>|__main__.)", "", str(etype)
        ).strip()
        start_time = datetime.datetime.now()

        exceptNotifier = {
            "SUBJECT": "[Except Notifier] ⚠️ Error! Python Code Exception Detected",
            "BODY": f"\n\nIMPORTANT WARNING \nPython Exception Detected in Your Code. \n\nHi there, \nThis is an exception catch notifier. \n\n - ☑️ Code Status: Fail.🛠 \n - ☑️ Detail: Python Code Ran Exceptions. \n - 🕐 Time: {start_time.strftime(DATE_FORMAT)} \n\n ⛔️ {excType}: %{etype.__doc__}\n\n {value} \n\n",
        }
        for line in traceback.extract_tb(tb):
            exceptNotifier["BODY"] += '\tFile: "%s"\n\t\t%s %s: %s\n' % (
                line[0],
                line[2],
                line[1],
                line[3],
            )
        while 1:
            if not tb.tb_next:
                break
            tb = tb.tb_next
        stack = []
        f = tb.tb_frame
        while f:
            stack.append(f)
            f = f.f_back
        stack.reverse()
        exceptNotifier["BODY"] += "\nLocals by frame, innermost last::::"
        for frame in stack:
            exceptNotifier["BODY"] += "\nFrame %s in %s at line %s" % (
                frame.f_code.co_name,
                frame.f_code.co_filename,
                frame.f_lineno,
            )
            for key, val in frame.f_locals.items():
                exceptNotifier["BODY"] += "\n\t%20s = " % key
                try:
                    exceptNotifier["BODY"] += str(val)
                except:
                    exceptNotifier["BODY"] += "<ERROR WHILE PRINTING VALUE>"

        data = {"text": exceptNotifier["SUBJECT"] + exceptNotifier["BODY"]}
        send_wechat_msg(_WECHAT_WEBHOOK_URL, data["text"])

        try:
            error_message = f"error_type=={excType} error_type_document=={etype.__doc__} error_value=={value} stack infomation=={stack} code name=={frame.f_code.co_name}file name=={frame.f_code.co_filename} file_number=={frame.f_lineno}"
            advice_msg = '\tFile: "%s"\n\t\t%s %s: %s\n' % (
                line[0],
                line[2],
                line[1],
                line[3],
            )
            advice_msg += receive_openai_advice(
                _OPEN_AI_MODEL, _OPEN_AI_API, error_message
            )  # NO-QA
            send_wechat_msg(_WECHAT_WEBHOOK_URL, advice_msg)
        except Exception as e:
            print(e)
            pass

    @staticmethod
    def send_wechat_msg(_WECHAT_WEBHOOK_URL: str, msg: str) -> None:
        """Send message to wechat.

        :param _WECHAT_WEBHOOK_URL: Wechat Webhook URL https://work.weixin.qq.com/api/doc/90000/90136/91770
        :type _WECHAT_WEBHOOK_URL: str
        :param msg: Message to send
        :type msg: str
        """
        msg_template = {"msgtype": "text", "text": {"content": ""}}
        msg_template["text"]["content"] = "\n".join(msg)
        requests.post(_WECHAT_WEBHOOK_URL, json=msg_template)


class SuccessWechat:
    def __init__(self) -> None:
        pass

    def __call__(self, *args, **kwds) -> None:
        exceptNotifier = EmailMessage()
        start_time = datetime.datetime.now()
        f"Time Stamp: {start_time.strftime(DATE_FORMAT)}"
        exceptNotifier = {
            "SUBJECT": "[Success Notifier] 🎉 Success! Python Code Executed Successfully"
        }
        exceptNotifier[
            "BODY"
        ] = f"\n\nHi there, \nThis is a success notifier.\n\n - ✅ Code Status: Success. \n - ✅ Detail: Python Code Ran Without Exceptions. \n - 🕐 Time: {start_time.strftime(DATE_FORMAT)} \n\nI just wanted to let you know that your Python code has run successfully without any exceptions. \n\nAll the best, \nExcept Notifier https://github.com/dsdanielpark/ExceptNotifier"

        data = {"text": exceptNotifier["SUBJECT"] + exceptNotifier["BODY"]}

        send_wechat_msg(_WECHAT_WEBHOOK_URL, data["text"])


class SendWechat:
    def __init__(self) -> None:
        pass

    def __call__(self, *args, **kwds) -> None:
        exceptNotifier = EmailMessage()
        start_time = datetime.datetime.now()
        f"Time Stamp: {start_time.strftime(DATE_FORMAT)}"
        exceptNotifier = {
            "SUBJECT": "[Codeline Notifier] 👏 Notice! Code Execution Reached Specified Line"
        }
        exceptNotifier[
            "BODY"
        ] = f"\n\nHi there, \nThis is a customized notifier.\n\n- ✅ Code Status: Done. \n- ✅ Detail: Code Execution Reached Specified Line.  \n- 🕐 Time: {start_time.strftime(DATE_FORMAT)} \n\nThe code has reached the line where you requested an email to be sent. As per your instruction, we are sending this email. \n\nAll the best, \nExcept Notifier https://github.com/dsdanielpark/ExceptNotifier"

        data = {"text": exceptNotifier["SUBJECT"] + exceptNotifier["BODY"]}

        send_wechat_msg(_WECHAT_WEBHOOK_URL, data["text"])


if __name__ == "__main__":

    """Get your wechat webhook URL. 
    https://work.weixin.qq.com/api/doc/90000/90136/91770"""

    global _WECHAT_WEBHOOK_URL
    _WECHAT_WEBHOOK_URL = "xxxxxxxxxxx"
    _OPEN_AI_MODEL = "gpt-3.5-turbo"
    _OPEN_AI_API = "sk-xxxxxxxxx"
    sys.excepthook = ExceptWechat.__call__

    try:
        print(1 / 0)
        SuccessWechat().__call__()  # 1 success sender

    except ExceptWechat as e:  # 2 except sender
        sys.exit()

    SendWechat().__call__()  # 3 customized sender

    send = SendWechat()  # You can use it like this, too.
    send()
