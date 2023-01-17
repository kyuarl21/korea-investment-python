from django.urls import path
from koreaInvestmentApi.Views import Views

urlpatterns = [
    path("v1/trading/domestic/auto-trading/", Views.autoTradingDomesticStocks, name="koreaInvestmentApi"),
    path("v1/trading/overseas/auto-trading/", Views.autoTradingOverseasStocks, name="koreaInvestmentApi")
]