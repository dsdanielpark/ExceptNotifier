import requests
import json

def get_authorize_code(rest_api_key):
    rest_api_key = '44bae6e1a82b322885e2e8f614677c75'
    redirect_uri = 'https://example.com/oauth'
    print()
    print(f'\n\nhttps://kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={redirect_uri}&response_type=code')
    

def save_token(rest_api_key, authorize_code, token_path):
    redirect_uri = 'https://example.com/oauth'
    url_token = 'https://kauth.kakao.com/oauth/token'
    data = {
        'grant_type':'authorization_code',
        'client_id':rest_api_key,
        'redirect_uri':redirect_uri,
        'code': authorize_code,
    }
    response = requests.post(url_token, data=data)
    tokens = response.json()
    with open(token_path,"w") as f:
        json.dump(tokens, f)
    
    return tokens

