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
    if os.environ["_BARD_ADVICE_LANG"]=='korean':
        input_text = f"다음 error를 어떻게 고칠 수 있을까? 다음 에러에 대해서 설명해주고, 어떤 위치에서 어떤 코드가 잘못 되었는지 말해줘. 그리고 이 코드를 고칠 수 있는 예시 코드를 보여줘 error=={error_message}"
    else:
        input_text = f"How can I fix this error? Give me short infomation about next error. Let me know which code line and which code is incorrect. and try to make it fix or fix example. error=={error_message}"
    
    response = bardapi.core.Bard().get_answer(input_text)
    advice_msg = response["content"]

    return advice_msg


# if __name__ == "__main__":
#     _BARD_API_KEY = "xxxxxxxxxxxxxx."
#     error_message = " Cell 3 in ()----> 1 1/0 ZeroDivisionError: division by zero"
#     advice_msg = receive_bard_advice(_BARD_API_KEY, error_message)

#     print(advice_msg)
