import json
import requests
import yaml

with open("config.yaml", encoding="UTF-8") as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)

KOREA_INVESTMENT_BASE_URL = _cfg["KOREA_INVESTMENT_BASE_URL"]
KOREA_INVESTMENT_APP_KEY = _cfg["KOREA_INVESTMENT_APP_KEY"]
KOREA_INVESTMENT_APP_SECRET = _cfg["KOREA_INVESTMENT_APP_SECRET"]


class TokenManagement:
    def issue_korea_investment_token():
        """한국투자증권 토큰 발급"""
        url = KOREA_INVESTMENT_BASE_URL + "/oauth2/tokenP"
        headers = {"content-type": "application/json"}
        body = {
            "grant_type": "client_credentials",
            "appkey": KOREA_INVESTMENT_APP_KEY,
            "appsecret": KOREA_INVESTMENT_APP_SECRET,
        }
        response = requests.post(url, headers=headers, data=json.dumps(body))
        # print(response.json())
        return response.json()["access_token"]
