from django.apps import AppConfig


class KoreaInvestmentApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "korea_investment_api"

    # def ready(self):
    #     from korea_investment_api.operator import Operator
    #     Operator.start(self)
