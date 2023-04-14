from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from korea_investment_api.domestic_monitoring import DomesticMonitoring
from korea_investment_api.overseas_monitoring import OverseasMonitoring
from korea_investment_api.symbols_creator import SymbolsCreator
from korea_investment_api.learning_model import LearningModel


class Views:
    @api_view(["GET"])
    def monitoring_kospi_stocks(self):
        response = DomesticMonitoring.monitoring_kospi_stocks(
            self, SymbolsCreator.create_kospi_symbols()
        )
        return Response(response)

    @api_view(["GET"])
    def monitoring_kosdaq_stocks(self):
        response = DomesticMonitoring.monitoring_kosdaq_stocks(
            self, SymbolsCreator.create_kosdaq_symbols()
        )
        return Response(response)

    @api_view(["GET"])
    def monitoring_nasdaq_stocks(self):
        response = OverseasMonitoring.monitoring_nasdaq_stocks(
            self, SymbolsCreator.create_nasdaq_symbols()
        )
        return Response(response)

    @api_view(["GET"])
    def monitoring_new_york_stocks(self):
        response = OverseasMonitoring.monitoring_new_york_stocks(
            self, SymbolsCreator.create_new_york_symbols()
        )
        return Response(response)

    @api_view(["GET"])
    def monitoring_amex_stocks(self):
        response = OverseasMonitoring.monitoring_amex_stocks(
            self, SymbolsCreator.create_amex_symbols()
        )
        return Response(response)

    @api_view(["GET"])
    def learning_model(self):
        response = LearningModel.learning_model(self)
        return Response(response)
