import datetime
import schedule
import time
from apscheduler.schedulers.background import BlockingScheduler
from django.http import HttpResponse
from koreaInvestmentApi.AutoTrading import AutoTrading

class Views:
    def __init__(self):
        self = self
        
    def autoTradingDomesticStocks(self):
        result = AutoTrading.autoTradingDomesticStocks(self)
        return HttpResponse(result)
    
    def autoTradingOverseasStocks(self):
        result = AutoTrading.autoTradingOverseasStocks(self)
        return HttpResponse(result)