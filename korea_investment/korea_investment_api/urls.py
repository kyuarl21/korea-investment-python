from django.urls import path
from korea_investment_api.views import Views

urlpatterns = [
    path(
        "v1/monitoring/domestic/kospi",
        Views.monitoring_kospi_stocks,
        name="korea_investment_api",
    ),
    path(
        "v1/monitoring/domestic/kosdaq",
        Views.monitoring_kosdaq_stocks,
        name="korea_investment_api",
    ),
    path(
        "v1/monitoring/overseas/nasdaq",
        Views.monitoring_nasdaq_stocks,
        name="korea_investment_api",
    ),
    path(
        "v1/monitoring/overseas/nyse",
        Views.monitoring_new_york_stocks,
        name="korea_investment_api",
    ),
    path(
        "v1/monitoring/overseas/amex",
        Views.monitoring_amex_stocks,
        name="korea_investment_api",
    ),
    path(
        "v1/learning-model",
        Views.learning_model,
        name="korea_investment_api",
    ),
]
