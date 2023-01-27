import requests
import yaml
from koreaInvestmentApi.Headers import Headers
from koreaInvestmentApi.LoggingHandler import LoggingHandler

logger = LoggingHandler.setLogger()

with open('config.yaml', encoding='UTF-8') as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)
    
KOREA_INVESTMENT_BASE_URL = _cfg['KOREA_INVESTMENT_BASE_URL']
KOREA_INVESTMENT_APP_KEY = _cfg['KOREA_INVESTMENT_APP_KEY']
KOREA_INVESTMENT_APP_SECRET = _cfg['KOREA_INVESTMENT_APP_SECRET']
CANO = _cfg['CANO']
ACNT_PRDT_CD = _cfg['ACNT_PRDT_CD']
ACCESS_TOKEN = ""

class Quotes:
    def __init__(self, token, symbol):
        self.token = token
        self.symbol = symbol
            
    def getDomesticStockPrice(self, token, symbol):
        """ 국내주식 현재가 조회 """
        url = KOREA_INVESTMENT_BASE_URL + "/uapi/domestic-stock/v1/quotations/inquire-price"
        params = {
            "FID_COND_MRKT_DIV_CODE": "J",
            "FID_INPUT_ISCD": symbol
        }
        response = requests.get(url, headers = Headers.createKoreaInvestmentHeaders(self, token, "FHKST01010100"), params = params)
        logger.debug(response.json())
        #return int(response.json()['output']['stck_prpr'])
        return response.json()
    
    def getDomesticStockDailyPrices(self, token, symbol):
        """ 국내주식 일자별 시세 조회 """
        url = KOREA_INVESTMENT_BASE_URL + "/uapi/domestic-stock/v1/quotations/inquire-daily-price"
        params = {
            "FID_COND_MRKT_DIV_CODE": "J",
            "FID_INPUT_ISCD": symbol,
            "FID_PERIOD_DIV_CODE": "D",
            "FID_ORG_ADJ_PRC": "0"
        }
        response = requests.get(url, headers = Headers.createKoreaInvestmentHeaders(self, token, "FHKST01010400"), params = params)
        logger.debug(response.json())
        return response.json()
    
    def getDomesticStockDailyPricesByIndustry(self, token):
        """ 국내주식 업종별 시세 조회 """
        url = KOREA_INVESTMENT_BASE_URL + "/uapi/domestic-stock/v1/quotations/inquire-daily-indexchartprice"
        params = {
            "FID_COND_MRKT_DIV_CODE": "U",
            "FID_INPUT_ISCD": "0002",
            "FID_INPUT_DATE_1": "20230101",
            "FID_INPUT_DATE_2": "20230116",
            "FID_PERIOD_DIV_CODE": "D"
        }
        response = requests.get(url, headers = Headers.createKoreaInvestmentHeaders(self, token, "HHDFS76240000"), params = params)
        logger.debug(response.json())
        return response.json()
    
    def getOverseasStockPrice(self, token, excd, symb):
        """ 해외주식 현재가 조회 """
        url = KOREA_INVESTMENT_BASE_URL + "/uapi/overseas-price/v1/quotations/price"
        params = {
            "AUTH": "",
            "EXCD": excd,
            "SYMB": symb
        }
        response = requests.get(url, headers = Headers.createKoreaInvestmentHeaders(self, token, "HHDFS00000300"), params = params)
        logger.debug(response.json())
        return response.json()
    
    def getOverseasStockDailyPrices(self, token, excd, symb):
        """ 해외주식 일자별 시세 조회 """
        url = KOREA_INVESTMENT_BASE_URL + "/uapi/overseas-price/v1/quotations/dailyprice"
        params = {
            "AUTH": "",
            "EXCD": excd,
            "SYMB": symb,
            "GUBN": "0",
            "BYMD": "",
            "MODP": "1",
            "KEYB": ""
        }
        response = requests.get(url, headers = Headers.createKoreaInvestmentHeaders(self, token, "HHDFS76240000"), params = params)
        logger.debug(response.json())
        return response.json()