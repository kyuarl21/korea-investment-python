from apscheduler.schedulers.background import BlockingScheduler
from django.conf import settings
from django_apscheduler.jobstores import register_events
from koreaInvestmentApi.DomesticMonitoring import DomesticMonitoring
from koreaInvestmentApi.OverseasMonitoring import OverseasMonitoring
from koreaInvestmentApi.SymbolsCreator import SymbolsCreator

class Operator:
    
    def start(self):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        register_events(scheduler)
        
        @scheduler.scheduled_job('cron', hour=9, name = 'monitoringKospiStocks')
        def monitoringKospiStocks():
            DomesticMonitoring.monitoringKospiStocks(self, SymbolsCreator.createKospiSymbols())
            
        @scheduler.scheduled_job('cron', hour=10, name = 'monitoringKosdaqStocks')
        def monitoringKosdaqStocks():
            DomesticMonitoring.monitoringKosdaqStocks(self, SymbolsCreator.createKosdaqSymbols())
            
        @scheduler.scheduled_job('cron', hour=0, name = 'monitoringNasdaqStocks')
        def monitoringNasdaqStocks():
            OverseasMonitoring.monitoringNasdaqStocks(self, SymbolsCreator.createNasdaqSymbols())
            
        @scheduler.scheduled_job('cron', hour=1, name = 'monitoringNewYorkStocks')
        def monitoringNewYorkStocks():
            OverseasMonitoring.monitoringNewYorkStocks(self, SymbolsCreator.createNewYorkSymbols())
            
        @scheduler.scheduled_job('cron', hour=2, name = 'monitoringAmexStocks')
        def monitoringAmexStocks():
            OverseasMonitoring.monitoringAmexStocks(self, SymbolsCreator.createAmexSymbols())
            
        scheduler.start()