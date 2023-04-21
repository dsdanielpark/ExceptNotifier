# -*- coding: utf-8 -*-
# Copyright 2023 parkminwoo
import openai


def receive_openai_advice(_OPEN_AI_MODEL, _OPEN_AI_API, error_message):
    openai.api_key = _OPEN_AI_API
    model_engine = _OPEN_AI_MODEL

    input_text = f"How can I fix this error? Give me short infomation about next error. Let me know which code line and which code is incorrect. and try to make it fix or fix exampel. error== {error_message}"
    resp = openai.ChatCompletion.create(
        model=model_engine, messages=[{"role": "user", "content": input_text}]
    )
    advice_msg = resp["choices"][0]["message"]["content"]
    return advice_msg


def get_resp_openai_advice(_OPEN_AI_MODEL, _OPEN_AI_API, error_message):
    openai.api_key = _OPEN_AI_API
    model_engine = _OPEN_AI_MODEL

    input_text = f"How can I fix this error? Give me short infomation about next error. Let me know which code line and which code is incorrect. and try to make it fix or fix exampel. error== {error_message}"
    resp = openai.ChatCompletion.create(
        model=model_engine, messages=[{"role": "user", "content": input_text}]
    )
    return resp


# if __name__ == "__main__":
#     _OPEN_AI_API = "sk-xxxxx"
#     _OPEN_AI_MODEL = "gpt-3.5-turbo"
#     error_message = " Cell 3 in ()----> 1 1/0 ZeroDivisionError: division by zero"
#     advice_msg = receive_openai_advice(_OPEN_AI_MODEL, _OPEN_AI_API, error_message)
#     print(advice_msg)
