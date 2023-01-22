import datetime
import json
import requests
import time
import yaml
from koreaInvestmentApi.Crawlings import Crawlings
from koreaInvestmentApi.Holdings import Holdings
from koreaInvestmentApi.Quotes import Quotes
from koreaInvestmentApi.TokenManagement import TokenManagement
from koreaInvestmentApi.Trading import Trading
from koreaInvestmentApi.LoggingHandler import LoggingHandler
logger = LoggingHandler.setLogger()

with open('config.yaml', encoding='UTF-8') as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)
    
KOREA_INVESTMENT_BASE_URL = _cfg['KOREA_INVESTMENT_BASE_URL']
KOREA_INVESTMENT_APP_KEY = _cfg['KOREA_INVESTMENT_APP_KEY']
KOREA_INVESTMENT_APP_SECRET = _cfg['KOREA_INVESTMENT_APP_SECRET']
CANO = _cfg['CANO']
ACNT_PRDT_CD = _cfg['ACNT_PRDT_CD']
ACCESS_TOKEN = ""

class DomesticMonitoring:
    def __init__(self):
        self = self
        
    def monitoringKospiStocks(self, kospiSymbols):
        ACCESS_TOKEN = TokenManagement.issueKoreaInvestmentToken()
        stocks_balance = Holdings.getDomesticStocksBalance(self, ACCESS_TOKEN)
        response_array = []
        for symbol in kospiSymbols:
            #present_response = Quotes.getDomesticStockPrice(self, ACCESS_TOKEN, symbol)
            #time.sleep(1)
            daily_response = Quotes.getDomesticStockDailyPrices(self, ACCESS_TOKEN, symbol)
            #time.sleep(1)
        
            up_sum = 0; down_sum = 0
            up_index = 0; down_index = 0
            for values in daily_response['output']:
                if (float(values['prdy_ctrt']) > float(0)):
                    up_sum += int(values['prdy_vrss'])
                    up_index += int(1)
                elif (float(values['prdy_ctrt']) < float(0)):
                    down_sum += int(values['prdy_vrss'])
                    down_index += int(1)

            up_average = up_sum / up_index
            down_average = abs(down_sum) / down_index
            target = up_average / (up_average + down_average) * 100
            #target2 = (up_average / down_average) / ((up_average / down_average) + 1) * 100
            print("symbol: " + str(symbol) + "  target: " + str(target))
            
            available_response = Trading.getDomesticAvailableBalance(self, ACCESS_TOKEN, symbol)
            #print(available_response)
            available_cash = available_response['output']['ord_psbl_cash']
            #print(available_cash)
            
            order_response = ""
            quantity = 100
            if (float(target) <= float(30)):
                order_response = Trading.orderDomesticStock(self, ACCESS_TOKEN, "VTTC0802U", symbol, quantity)
                order_response['output']['symbol'] = symbol
            elif (float(target) >= float(70)):
                for holdings in stocks_balance['output1']:
                    if (str(holdings['pdno']) == str(symbol)):
                        order_response = Trading.orderDomesticStock(self, ACCESS_TOKEN, "VTTC0801U", holdings['pdno'], holdings['ord_psbl_qty'])
                        order_response['output']['symbol'] = symbol
            
            response_array.append(order_response)
        
        logger.debug(response_array)
        return response_array
    
    def monitoringKosdaqStocks(self, kosdaqSymbols):
        ACCESS_TOKEN = TokenManagement.issueKoreaInvestmentToken()
        stocks_balance = Holdings.getDomesticStocksBalance(self, ACCESS_TOKEN)
        response_array = []
        for symbol in kosdaqSymbols:
            #present_response = Quotes.getDomesticStockPrice(self, ACCESS_TOKEN, symbol)
            #time.sleep(1)
            daily_response = Quotes.getDomesticStockDailyPrices(self, ACCESS_TOKEN, symbol)
            #time.sleep(1)
        
            up_sum = 0; down_sum = 0
            up_index = 0; down_index = 0
            for values in daily_response['output']:
                if (float(values['prdy_ctrt']) > float(0)):
                    up_sum += int(values['prdy_vrss'])
                    up_index += int(1)
                elif (float(values['prdy_ctrt']) < float(0)):
                    down_sum += int(values['prdy_vrss'])
                    down_index += int(1)

            up_average = up_sum / up_index
            down_average = abs(down_sum) / down_index
            target = up_average / (up_average + down_average) * 100
            #target2 = (up_average / down_average) / ((up_average / down_average) + 1) * 100
            print("symbol: " + str(symbol) + "  target: " + str(target))
            
            available_response = Trading.getDomesticAvailableBalance(self, ACCESS_TOKEN, symbol)
            #print(available_response)
            available_cash = available_response['output']['ord_psbl_cash']
            #print(available_cash)
            
            order_response = ""
            quantity = 100
            if (float(target) <= float(30)):
                order_response = Trading.orderDomesticStock(self, ACCESS_TOKEN, "VTTC0802U", symbol, quantity)
                order_response['output']['symbol'] = symbol
            elif (float(target) >= float(70)):
                for holdings in stocks_balance['output1']:
                    if (str(holdings['pdno']) == str(symbol)):
                        order_response = Trading.orderDomesticStock(self, ACCESS_TOKEN, "VTTC0801U", holdings['pdno'], holdings['ord_psbl_qty'])
                        order_response['output']['symbol'] = symbol
            
            response_array.append(order_response)
        
        logger.debug(response_array)
        return response_array