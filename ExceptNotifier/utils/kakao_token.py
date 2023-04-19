import requests
import json


def get_authorize_code(rest_api_key: str) -> None:
    """Get authorize code link by using KAKAO REST API KEY

    :param rest_api_key: REST API KEY
    :type rest_api_key: str
    """
    redirect_uri = "https://example.com/oauth"
    print()
    print(
        f"\n\nhttps://kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )


def save_token(rest_api_key: str, authorize_code: str, token_path: str) -> dict:
    """Receive authorized token and save it in json format.

    :param rest_api_key: REST API KEY
    :type rest_api_key: str
    :param authorize_code: The code that comes out when you click the link that comes as the return value of the get_authorize_code function.
    :type authorize_code: str
    :param token_path: Path to store token
    :type token_path: str
    :return: Generated tokens
    :rtype: dict
    """

    redirect_uri = "https://example.com/oauth"
    url_token = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": rest_api_key,
        "redirect_uri": redirect_uri,
        "code": authorize_code,
    }
    response = requests.post(url_token, data=data)
    tokens = response.json()
    with open(token_path, "w") as f:
        json.dump(tokens, f)

    return tokens
