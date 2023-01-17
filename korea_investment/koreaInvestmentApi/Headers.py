import yaml

with open('config.yaml', encoding='UTF-8') as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)
    
KOREA_INVESTMENT_BASE_URL = _cfg['KOREA_INVESTMENT_BASE_URL']
KOREA_INVESTMENT_APP_KEY = _cfg['KOREA_INVESTMENT_APP_KEY']
KOREA_INVESTMENT_APP_SECRET = _cfg['KOREA_INVESTMENT_APP_SECRET']

class Headers:
    def __init__(self, token, trId):
        self.token = token
        self.trId = trId

    def createKoreaInvestmentHeaders(self, token, trId):
        headers = {"content-type": "application/json; charset=utf-8",
            "authorization": "Bearer " + token,
            "appKey": KOREA_INVESTMENT_APP_KEY,
            "appSecret": KOREA_INVESTMENT_APP_SECRET,
            "tr_id": trId,
            "custtype": "P"
        }
        return headers