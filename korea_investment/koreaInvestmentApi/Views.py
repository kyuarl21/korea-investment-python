import datetime
import json
import schedule
import time
from apscheduler.schedulers.background import BlockingScheduler
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from koreaInvestmentApi.AutoTrading import AutoTrading

class Views:
    def __init__(self):
        self = self
    
    @api_view(['GET'])
    def autoTradingDomesticStocks(self):
        response = AutoTrading.autoTradingDomesticStocks(self)
        return Response(response)
    
    @api_view(['GET'])
    def autoTradingOverseasStocks(self):
        response = AutoTrading.autoTradingOverseasStocks(self)
        return Response(response)