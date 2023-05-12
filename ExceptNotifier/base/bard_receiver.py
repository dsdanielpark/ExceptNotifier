# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import bardapi
import os


def receive_bard_advice(_BARD_API_KEY: str, error_message: str) -> str:
    """Receive debugging information about your code from google bard.
    :param _OPEN_AI_API:__Secure-1PSID value of google bard
    :type _OPEN_AI_API: str
    :param error_message: Error message
    :type error_message: str
    :return: Returns a description and example of the code, the location of the error, and a debugging code example.
    :rtype: str
    """
    os.environ["_BARD_API_KEY"] = _BARD_API_KEY
    input_text = f"How can I fix this error? Give me short infomation about next error. Let me know which code line and which code is incorrect. and try to make it fix or fix exampel. error== {error_message}"
    response = bardapi.core.Bard().get_answer(input_text)
    advice_msg = response["content"]

    return advice_msg


# if __name__ == "__main__":
#     _BARD_API_KEY = "xxxxxxxxxxxxxx."
#     error_message = " Cell 3 in ()----> 1 1/0 ZeroDivisionError: division by zero"
#     advice_msg = receive_bard_advice(_BARD_API_KEY, error_message)

#     print(advice_msg)
