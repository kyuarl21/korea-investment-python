import datetime
import json
import requests
import time
import yaml
from koreaInvestmentApi.quotes import quotes
from koreaInvestmentApi.tokenManagement import tokenManagement

with open('config.yaml', encoding='UTF-8') as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)
    
KOREA_INVESTMENT_BASE_URL = _cfg['KOREA_INVESTMENT_BASE_URL']
KOREA_INVESTMENT_APP_KEY = _cfg['KOREA_INVESTMENT_APP_KEY']
KOREA_INVESTMENT_APP_SECRET = _cfg['KOREA_INVESTMENT_APP_SECRET']
CANO = _cfg['CANO']
ACNT_PRDT_CD = _cfg['ACNT_PRDT_CD']
ACCESS_TOKEN = ""

class trading:
    def __init__(self):
        self = self
        
    def domesticStocksTrading(self):
        ACCESS_TOKEN = tokenManagement.issueKoreaInvestmentToken()
        symbol_list = ["005930", "035420", "035720"]
        for symbol in symbol_list:
            present_price = quotes.getDomesticStocksPrice(self, ACCESS_TOKEN, symbol)
        
        return "Helo"
    
    def overseasStocksTrading(self):
        ACCESS_TOKEN = tokenManagement.issueKoreaInvestmentToken()
        excd = "NAS"
        symbol_list = ["AAPL", "MSFT", "GOOGL"]
        for symbol in symbol_list:
            present_price = quotes.getOverseasStocksPrice(self, ACCESS_TOKEN, excd, symbol)
            
        return "Helo"