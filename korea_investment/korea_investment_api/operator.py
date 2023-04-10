from apscheduler.schedulers.background import BlockingScheduler
from django.conf import settings
from django_apscheduler.jobstores import register_events
from korea_investment_api.domestic_monitoring import DomesticMonitoring
from korea_investment_api.overseas_monitoring import OverseasMonitoring
from korea_investment_api.symbols_creator import SymbolsCreator

class Operator:
    
    def start(self):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        register_events(scheduler)
        
        @scheduler.scheduled_job('cron', hour=9, name = 'monitoring_kospi_stocks')
        def monitoring_kospi_stocks():
            DomesticMonitoring.monitoring_kospi_stocks(self, SymbolsCreator.create_kospi_symbols())
            
        @scheduler.scheduled_job('cron', hour=10, name = 'monitoring_kosdaq_stocks')
        def monitoring_kosdaq_stocks():
            DomesticMonitoring.monitoring_kosdaq_stocks(self, SymbolsCreator.create_kosdaq_symbols())
            
        @scheduler.scheduled_job('cron', hour=0, name = 'monitoring_nasdaq_stocks')
        def monitoring_nasdaq_stocks():
            OverseasMonitoring.monitoring_nasdaq_stocks(self, SymbolsCreator.create_nasdaq_symbols())
            
        @scheduler.scheduled_job('cron', hour=1, name = 'monitoring_new_york_stocks')
        def monitoring_new_york_stocks():
            OverseasMonitoring.monitoring_new_york_stocks(self, SymbolsCreator.create_new_york_symbols())
            
        @scheduler.scheduled_job('cron', hour=2, name = 'monitoring_amex_stocks')
        def monitoring_amex_stocks():
            OverseasMonitoring.monitoring_amex_stocks(self, SymbolsCreator.create_amex_symbols())
            
        scheduler.start()