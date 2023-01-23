from django.apps import AppConfig

class KoreaInvestmentApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "koreaInvestmentApi"
    
    def ready(self):
        from koreaInvestmentApi.Operator import Operator
        Operator.start(self)