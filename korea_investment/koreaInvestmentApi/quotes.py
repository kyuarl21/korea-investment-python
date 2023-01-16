import datetime
import json
import requests
import time
import yaml
from koreaInvestmentApi.tokenManagement import tokenManagement

with open('config.yaml', encoding='UTF-8') as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)
    
KOREA_INVESTMENT_BASE_URL = _cfg['KOREA_INVESTMENT_BASE_URL']
KOREA_INVESTMENT_APP_KEY = _cfg['KOREA_INVESTMENT_APP_KEY']
KOREA_INVESTMENT_APP_SECRET = _cfg['KOREA_INVESTMENT_APP_SECRET']
CANO = _cfg['CANO']
ACNT_PRDT_CD = _cfg['ACNT_PRDT_CD']
ACCESS_TOKEN = ""

class quotes:
    def __init__(self, token, symbol):
        self.token = token
        self.symbol = symbol
            
    def getDomesticStocksPrice(self, token, symbol):
        """ 국내주식 현재가 조회 """
        url = KOREA_INVESTMENT_BASE_URL + "/uapi/domestic-stock/v1/quotations/inquire-price"
        headers = {"content-type": "application/json",
            "authorization": "Bearer " + token,
            "appKey": KOREA_INVESTMENT_APP_KEY,
            "appSecret": KOREA_INVESTMENT_APP_SECRET,
            "tr_id": "FHKST01010100"}
        params = {
            "fid_cond_mrkt_div_code": "J",
            "fid_input_iscd": symbol
        }
        response = requests.get(url, headers = headers, params = params)
        #print(response.json())
        return int(response.json()['output']['stck_prpr'])
    
    def getOverseasStocksPrice(self, token, excd, symb):
        """ 해외주식 현재가 조회 """
        url = KOREA_INVESTMENT_BASE_URL + "/uapi/overseas-price/v1/quotations/price"
        headers = {"content-type": "application/json",
            "authorization": "Bearer " + token,
            "appKey": KOREA_INVESTMENT_APP_KEY,
            "appSecret": KOREA_INVESTMENT_APP_SECRET,
            "tr_id": "HHDFS00000300"}
        params = {
            "AUTH": "",
            "EXCD": excd,
            "SYMB": symb
        }
        response = requests.get(url, headers = headers, params = params)
        #print(response.json())
        return response.json()['output']['last']
    