# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import openai
from os import environ


def receive_openai_advice(
    openai_model: str, open_ai_api: str, error_message: str
) -> str:
    """Receive debugging information about your code from models in open ai.

    :param openai_model: model name of open ai
    :type openai_model: str
    :param open_ai_api: API KEY value of open ai
    :type open_ai_api: str
    :param error_message: Error message
    :type error_message: str
    :return: Returns a description and example of the code, the location of the error, and a debugging code example.
    :rtype: str
    """

    openai.api_key = open_ai_api
    model_engine = openai_model

    if environ.get("_PROMPT_COMMAND") is None:
        input_text = f"How can I fix this error? Give me short infomation about next error. Let me know which code line and which code is incorrect. and try to make it fix or fix example. error== {error_message}"
    else:
        input_text = f"{environ['_PROMPT_COMMAND']} error=={error_message}"
    resp = openai.ChatCompletion.create(
        model=model_engine, messages=[{"role": "user", "content": input_text}]
    )
    advice_msg = resp["choices"][0]["message"]["content"]
    return advice_msg


def get_resp_openai_advice(
    openai_model: str, open_ai_api: str, error_message: str
) -> dict:
    """Check response of Open AI API status

    :param openai_model: model name of open ai
    :type openai_model: str
    :param open_ai_api: API KEY value of open ai
    :type open_ai_api: str
    :param error_message: Error message
    :type error_message: str
    :return: Returns response dict to openai
    :rtype: dict
    """
    openai.api_key = open_ai_api
    model_engine = openai_model


def receive_openai_advice(
    openai_model: str, open_ai_api: str, error_message: str
) -> str:
    """Receive debugging information about your code from models in open ai.

    :param openai_model: model name of open ai
    :type openai_model: str
    :param open_ai_api: API KEY value of open ai
    :type open_ai_api: str
    :param error_message: Error message
    :type error_message: str
    :return: Returns a description and example of the code, the location of the error, and a debugging code example.
    :rtype: str
    """

    openai.api_key = open_ai_api
    model_engine = openai_model
    if environ.get("_PROMPT_COMMAND") is None:
        input_text = f"How can I fix this error? Give me short infomation about next error. Let me know which code line and which code is incorrect. and try to make it fix or fix example. error== {error_message}"
    else:
        input_text = f"{environ['_PROMPT_COMMAND']} error== {error_message}"
    resp = openai.ChatCompletion.create(
        model=model_engine, messages=[{"role": "user", "content": input_text}]
    )
    advice_msg = resp["choices"][0]["message"]["content"]
    return advice_msg
    resp = openai.ChatCompletion.create(
        model=model_engine, messages=[{"role": "user", "content": input_text}]
    )
    return resp


# if __name__ == "__main__":
#     open_ai_api = "sk-xxxxx"
#     openai_model = "gpt-3.5-turbo"
#     error_message = " Cell 3 in ()----> 1 1/0 ZeroDivisionError: division by zero"
#     advice_msg = receive_openai_advice(openai_model, open_ai_api, error_message)
#     print(advice_msg)
