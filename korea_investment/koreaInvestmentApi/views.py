import datetime
import schedule
import time
from apscheduler.schedulers.background import BlockingScheduler
from django.http import HttpResponse
from koreaInvestmentApi.quotes import quotes
from koreaInvestmentApi.trading import trading

class views:
    def __init__(self):
        self = self
        
#    def getDomesticStocksPrice(self):
#        result = quotes.getDomesticStocksPrice(self)
#        return HttpResponse(result)
    
    def domesticStocksTrading(self):
        #result = schedule.every(5).second.do(trading.domesticStocksTrading(self))
        result = trading.domesticStocksTrading(self)
        return HttpResponse(result)
    
    def overseasStocksTrading(self):
        #result = schedule.every(1).hour.do(trading.overseasStocksTrading(self))
        result = trading.overseasStocksTrading(self)
        return HttpResponse(result)
    