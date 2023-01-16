from django.urls import path
from koreaInvestmentApi.views import views

urlpatterns = [
    # path("v1/quotes/domestic-stocks/", views.getDomesticStocksPrice, name="koreaInvestmentApi"),
    path("v1/trading/domestic-stocks/", views.domesticStocksTrading, name="koreaInvestmentApi"),
    path("v1/trading/overseas-stocks/", views.overseasStocksTrading, name="koreaInvestmentApi"),
]