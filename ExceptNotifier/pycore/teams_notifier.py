# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import re
import json
import datetime
import requests
import traceback
from os import environ
from email.message import EmailMessage
from ExceptNotifier.base.teams_sender import send_teams_msg
from ExceptNotifier.base.openai_receiver import receive_openai_advice
from ExceptNotifier.base.bard_receiver import receive_bard_advice

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class ExceptTeams(BaseException):
    """Override excepthook to send error message to Microsoft Teams.

    :param etype: Error Type
    :type etype: _type_
    :param value: Error Value
    :type value: _type_
    :param tb: Traceback Information
    :type tb: _type_
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __call__(etype, value, tb):
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

        exceptNotifier["BODY"] += "\nLocal by frame, innermost last::::"
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

        send_teams_msg(environ["_TEAMS_WEBHOOK_URL"], data["text"])
        if environ.get("_OPEN_AI_API") is not None:
            try:
                error_message = f"error_type=={excType} error_type_document=={etype.__doc__} error_value=={value} stack infomation=={stack} code name=={frame.f_code.co_name}file name=={frame.f_code.co_filename} file_number=={frame.f_lineno}"
                advice_msg = '\tFile: "%s"\n\t\t%s %s: %s\n' % (
                    line[0],
                    line[2],
                    line[1],
                    line[3],
                )
                advice_msg += receive_openai_advice(
                    environ["_OPEN_AI_MODEL"], environ["_OPEN_AI_API"], error_message
                )  # NO-QA
                send_teams_msg(environ["_TEAMS_WEBHOOK_URL"], advice_msg)
            except Exception as e:
                pass

        if environ.get("_BARD_API_KEY") is not None:
            try:
                error_message = f"error_type=={excType} error_type_document=={etype.__doc__} error_value=={value} stack infomation=={stack} code name=={frame.f_code.co_name}file name=={frame.f_code.co_filename} file_number=={frame.f_lineno}"
                advice_msg = '\tFile: "%s"\n\t\t%s %s: %s\n' % (
                    line[0],
                    line[2],
                    line[1],
                    line[3],
                )
                advice_msg += receive_bard_advice(
                    environ["_BARD_API_KEY"], error_message
                )  # NO-QA
                send_teams_msg(environ["_TEAMS_WEBHOOK_URL"], advice_msg)
            except Exception as e:
                pass

    @staticmethod
    def send_teams_msg(_TEAMS_WEBHOOK_URL, msg):
        """Send message to chat room through microsoft teams app's webhook url.

        :param _TEAMS_WEBHOOK_URL: _TEAMS_WEBHOOK_URL from teams app
        :type _TEAMS_WEBHOOK_URL: str
        :param msg: Message text
        :type msg: str
        :return: Response according to REST API request
        :rtype: dict
        """

        payload = {"text": msg}
        headers = {"Content-Type": "application/json"}
        resp = requests.post(
            _TEAMS_WEBHOOK_URL, headers=headers, data=json.dumps(payload)
        )

        return resp


class SuccessTeams:
    """Sending success message to microsoft teams
    """

    def __init__(self) -> None:
        pass

    def __call__(self) -> None:
        exceptNotifier = EmailMessage()
        start_time = datetime.datetime.now()
        f"Time Stamp: {start_time.strftime(DATE_FORMAT)}"
        exceptNotifier = {
            "SUBJECT": "[Success Notifier] 🎉 Success! Python Code Executed Successfully"
        }
        exceptNotifier[
            "BODY"
        ] = f"\n\nHi there, \nThis is a success notifier.\n\n - ✅ Code Status: Success. \n - ✅ Detail: Python Code Ran Without Exceptions. \n - 🕐 Time: {start_time.strftime(DATE_FORMAT)} \n\nI just wanted to let you know that your Python code has run successfully without any exceptions. \n\nAll the best, \nExcept Notifier github.com/dsdanielpark/ExceptNotifier"

        data = {"text": exceptNotifier["SUBJECT"] + exceptNotifier["BODY"]}

        send_teams_msg(environ["_TEAMS_WEBHOOK_URL"], data["text"])


class SendTeams:
    """Sending message to microsoft teams
    """

    def __init__(self) -> None:
        pass

    def __call__(self) -> None:
        exceptNotifier = EmailMessage()
        start_time = datetime.datetime.now()
        f"Time Stamp: {start_time.strftime(DATE_FORMAT)}"
        exceptNotifier = {
            "SUBJECT": "[Codeline Notifier] 👏 Notice! Code Execution Reached Specified Line"
        }
        exceptNotifier[
            "BODY"
        ] = f"\n\nHi there, \nThis is a customized notifier.\n\n- ✅ Code Status: Done. \n- ✅ Detail: Code Execution Reached Specified Line.  \n- 🕐 Time: {start_time.strftime(DATE_FORMAT)} \n\nThe code has reached the line where you requested an email to be sent. As per your instruction, we are sending this email. \n\nAll the best, \nExcept Notifier github.com/dsdanielpark/ExceptNotifier"

        data = {"text": exceptNotifier["SUBJECT"] + exceptNotifier["BODY"]}

        send_teams_msg(environ["_TEAMS_WEBHOOK_URL"], data["text"])


# if __name__ == "__main__":
#     """Follow next page"""
#     environ['_TEAMS_WEBHOOK_URL'] = "microsoft webhook _TEAMS_WEBHOOK_URL"
# #     environ['_OPEN_AI_API'] = "xxxxxxxxxxxxx"  #optional
# #     environ['_OPEN_AI_MODEL'] = "gpt-3.5-turbo" #optional
#     sys.excepthook = ExceptTeams.__call__
#     try:
#         print(1 / 20)
#         SuccessTeams().__call__()  # 1 success sender
#     except ExceptTeams as e:  # 2 except sender
#         sys.exit()
#     SendTeams().__call__()  # 3 customized sender
