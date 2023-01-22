from django.urls import path
from koreaInvestmentApi.Views import Views

urlpatterns = [
    path("v1/monitoring/domestic/kospi/", Views.monitoringKospiStocks, name="koreaInvestmentApi"),
    path("v1/monitoring/domestic/kosdaq/", Views.monitoringKosdaqStocks, name="koreaInvestmentApi"),
    path("v1/monitoring/overseas/nasdaq/", Views.monitoringNasdaqStocks, name="koreaInvestmentApi"),
    path("v1/monitoring/overseas/nyse/", Views.monitoringNewYorkStocks, name="koreaInvestmentApi"),
    path("v1/monitoring/overseas/amex/", Views.monitoringAmexStocks, name="koreaInvestmentApi"),
]