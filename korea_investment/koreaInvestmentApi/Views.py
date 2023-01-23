from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from koreaInvestmentApi.DomesticMonitoring import DomesticMonitoring
from koreaInvestmentApi.OverseasMonitoring import OverseasMonitoring
from koreaInvestmentApi.SymbolsCreator import SymbolsCreator

class Views:
    
    @api_view(['GET'])
    def monitoringKospiStocks(self):
        response = DomesticMonitoring.monitoringKospiStocks(self, SymbolsCreator.createKospiSymbols())
        return Response(response)
    
    @api_view(['GET'])
    def monitoringKosdaqStocks(self):
        response = DomesticMonitoring.monitoringKosdaqStocks(self, SymbolsCreator.createKosdaqSymbols())
        return Response(response)
    
    @api_view(['GET'])
    def monitoringNasdaqStocks(self):
        response = OverseasMonitoring.monitoringNasdaqStocks(self, SymbolsCreator.createNasdaqSymbols())
        return Response(response)
    
    @api_view(['GET'])
    def monitoringNewYorkStocks(self):
        response = OverseasMonitoring.monitoringNewYorkStocks(self, SymbolsCreator.createNewYorkSymbols())
        return Response(response)
    
    @api_view(['GET'])
    def monitoringAmexStocks(self):
        response = OverseasMonitoring.monitoringAmexStocks(self, SymbolsCreator.createAmexSymbols())
        return Response(response)