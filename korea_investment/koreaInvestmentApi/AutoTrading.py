import datetime
import json
import requests
import time
import yaml
from koreaInvestmentApi.Crawlings import Crawlings
from koreaInvestmentApi.Quotes import Quotes
from koreaInvestmentApi.TokenManagement import TokenManagement

with open('config.yaml', encoding='UTF-8') as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)
    
KOREA_INVESTMENT_BASE_URL = _cfg['KOREA_INVESTMENT_BASE_URL']
KOREA_INVESTMENT_APP_KEY = _cfg['KOREA_INVESTMENT_APP_KEY']
KOREA_INVESTMENT_APP_SECRET = _cfg['KOREA_INVESTMENT_APP_SECRET']
CANO = _cfg['CANO']
ACNT_PRDT_CD = _cfg['ACNT_PRDT_CD']
ACCESS_TOKEN = ""

class AutoTrading:
    def __init__(self):
        self = self
        
    def autoTradingDomesticStocks(self):
        ACCESS_TOKEN = TokenManagement.issueKoreaInvestmentToken()
        response_array = []
        symbol_list = ["005930", "035420", "035720"]
        #for symbol in symbol_list:
        #    price_response = Quotes.getDomesticStockPrice(self, ACCESS_TOKEN, symbol)
        #    time.sleep(1)
        #    daily_price = Quotes.getDomesticStockDailyPrices(self, ACCESS_TOKEN, symbol)
        
        response = Quotes.getDomesticStockPrice(self, ACCESS_TOKEN, "005930")
        time.sleep(1)
        daily_response = Quotes.getDomesticStockDailyPrices(self, ACCESS_TOKEN, "005930")
        
        return daily_response
    
    def autoTradingOverseasStocks(self):
        ACCESS_TOKEN = TokenManagement.issueKoreaInvestmentToken()
        excd = "NAS"
        symbol_list = ["AAPL", "MSFT", "GOOGL"]
        for symbol in symbol_list:
            present_price = Quotes.getOverseasStockPrice(self, ACCESS_TOKEN, excd, symbol)
            
        return present_price