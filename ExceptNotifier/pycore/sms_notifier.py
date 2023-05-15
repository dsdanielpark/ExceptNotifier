# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo

import re
import datetime
import traceback
from os import environ
from twilio.rest import Client
from email.message import EmailMessage
from ExceptNotifier.base.sms_sender import send_sms_msg
from ExceptNotifier.base.openai_receiver import receive_openai_advice
from ExceptNotifier.base.bard_receiver import receive_bard_advice

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class ExceptSMS(BaseException):
    """Override excepthook to send error message to SMS.

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
            "SUBJECT": "[Except Notifier] ** Error! ** Python Code Exception Detected",
            "BODY": f"\n\nIMPORTANT WARNING \nPython Exception Detected in Your Code. \n\nHi there, \nThis is an exception catch notifier. \n\n - Code Status: Fail. \n - Detail: Python Code Ran Exceptions. \n - Time: {start_time.strftime(DATE_FORMAT)} \n\n :no_entry: {excType}: %{etype.__doc__}\n\n {value} \n\n",
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

        send_sms_msg(
            environ["_TWILIO_SID"],
            environ["_TWILIO_TOKEN"],
            environ["_SENDER_PHONE_NUMBER"],
            environ["_RECIPIENT_PHONE_NUMBER"],
            data["text"],
        )

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
                send_sms_msg(
                    environ["_TWILIO_SID"],
                    environ["_TWILIO_TOKEN"],
                    environ["_SENDER_PHONE_NUMBER"],
                    environ["_RECIPIENT_PHONE_NUMBER"],
                    advice_msg,
                )
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
                send_sms_msg(
                    environ["_TWILIO_SID"],
                    environ["_TWILIO_TOKEN"],
                    environ["_SENDER_PHONE_NUMBER"],
                    environ["_RECIPIENT_PHONE_NUMBER"],
                    advice_msg,
                )
            except Exception as e:
                pass

    @staticmethod
    def send_sms_msg(
        _TWILIO_SID: str,
        _TWILIO_TOKEN: str,
        _SENDER_PHONE_NUMBER: str,
        _RECIPIENT_PHONE_NUMBER: str,
        msg: str,
    ) -> dict:
        """Send SMS through twilio platform.
        https://www.twilio.com/en-us

        :param _TWILIO_SID: Twilio personal _TWILIO_SID
        :type _TWILIO_SID: str
        :param _TWILIO_TOKEN: Twilio personal _TWILIO_TOKEN
        :type _TWILIO_TOKEN: str
        :param _SENDER_PHONE_NUMBER: Sender phone number
        :type _SENDER_PHONE_NUMBER: str
        :param _RECIPIENT_PHONE_NUMBER: Recipient phone number
        :type _RECIPIENT_PHONE_NUMBER: str
        :param msg: SMS content
        :type msg: str
        :return: Response dict
        :rtype: dict
        """

        client = Client(_TWILIO_SID, _TWILIO_TOKEN)
        resp = client.messages.create(
            to=_RECIPIENT_PHONE_NUMBER, from_=_SENDER_PHONE_NUMBER, body=msg[:1500]
        )
        return resp


class SuccessSMS:
    """Sending success message to SMS
    """

    def __init__(self) -> None:
        pass

    def __call__(self) -> None:
        exceptNotifier = EmailMessage()
        start_time = datetime.datetime.now()
        f"Time Stamp: {start_time.strftime(DATE_FORMAT)}"
        exceptNotifier = {
            "SUBJECT": "[Success Notifier] ** Success! ** Python Code Executed Successfully"
        }
        exceptNotifier[
            "BODY"
        ] = f"\n\nHi there, \nThis is a success notifier.\n\n - Code Status: Success. \n - Detail: Python Code Ran Without Exceptions. \n - Time: {start_time.strftime(DATE_FORMAT)} \n\nI just wanted to let you know that your Python code has run successfully without any exceptions. \n\nAll the best, \nExcept Notifier github.com/dsdanielpark/ExceptNotifier"

        data = {"text": exceptNotifier["SUBJECT"] + exceptNotifier["BODY"]}

        send_sms_msg(
            environ["_TWILIO_SID"],
            environ["_TWILIO_TOKEN"],
            environ["_SENDER_PHONE_NUMBER"],
            environ["_RECIPIENT_PHONE_NUMBER"],
            data["text"],
        )


class SendSMS:
    """Sending message to SMS
    """

    def __init__(self) -> None:
        pass

    def __call__(self) -> None:
        exceptNotifier = EmailMessage()
        start_time = datetime.datetime.now()
        f"Time Stamp: {start_time.strftime(DATE_FORMAT)}"
        exceptNotifier = {
            "SUBJECT": "[Codeline Notifier] ** Notice! ** Code Execution Reached Specified Line"
        }
        exceptNotifier[
            "BODY"
        ] = f"\n\nHi there, \nThis is a customized notifier.\n\n- Code Status: Done. \n- Detail: Code Execution Reached Specified Line.  \n- Time: {start_time.strftime(DATE_FORMAT)} \n\nThe code has reached the line where you requested an email to be sent. As per your instruction, we are sending this email. \n\nAll the best, \nExcept Notifier github.com/dsdanielpark/ExceptNotifier"

        data = {"text": exceptNotifier["SUBJECT"] + exceptNotifier["BODY"]}

        send_sms_msg(
            environ["_TWILIO_SID"],
            environ["_TWILIO_TOKEN"],
            environ["_SENDER_PHONE_NUMBER"],
            environ["_RECIPIENT_PHONE_NUMBER"],
            data["text"],
        )


# if __name__ == "__main__":
#     """https://www.twilio.com/en-us"""
#     environ['_TWILIO_SID'] = "xxxx"
#     environ['_TWILIO_TOKEN'] = "yyyyyy"
#     environ['_RECIPIENT_PHONE_NUMBER'] = ("+aaaaaa",)
#     environ['_SENDER_PHONE_NUMBER'] = ("+bbbbbb",)
#     sys.excepthook = ExceptSMS.__call__
# #     environ['_OPEN_AI_API'] = "xxxxxxxxxxxxx"  #optional
# #     environ['_OPEN_AI_MODEL'] = "gpt-3.5-turbo" #optional
#     try:
#         print(1 / 10)
#         SuccessSMS().__call__()  # 1 success sender
#     except ExceptSMS as e:  # 2 except sender
#         with open("exceptError.pickle", "wb") as f:
#             pickle.dump(e, f)
#         raise pickle.load(f)
#         sys.exit()
#     SendSMS().__call__()  # 3 customized sender
