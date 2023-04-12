import requests
import yaml
from korea_investment_api.common_headers import CommonHeaders
from korea_investment_api.logging_handler import LoggingHandler

logger = LoggingHandler.set_logger()

with open("config.yaml", encoding="UTF-8") as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)

KOREA_INVESTMENT_BASE_URL = _cfg["KOREA_INVESTMENT_BASE_URL"]
KOREA_INVESTMENT_APP_KEY = _cfg["KOREA_INVESTMENT_APP_KEY"]
KOREA_INVESTMENT_APP_SECRET = _cfg["KOREA_INVESTMENT_APP_SECRET"]
CANO = _cfg["CANO"]
ACNT_PRDT_CD = _cfg["ACNT_PRDT_CD"]
ACCESS_TOKEN = ""


class Quotes:
    def __init__(self, token, symbol):
        self.token = token
        self.symbol = symbol

    def get_domestic_stock_price(self, token, symbol):
        """국내주식 현재가 조회"""
        url = (
            KOREA_INVESTMENT_BASE_URL
            + "/uapi/domestic-stock/v1/quotations/inquire-price"
        )
        params = {"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": symbol}
        response = requests.get(
            url,
            headers=CommonHeaders.create_korea_investment_headers(
                self, token, "FHKST01010100"
            ),
            params=params,
        )
        logger.debug(response.json())
        # return int(response.json()['output']['stck_prpr'])
        return response.json()

    def get_domestic_stock_daily_prices(self, token, symbol):
        """국내주식 일자별 시세 조회"""
        url = (
            KOREA_INVESTMENT_BASE_URL
            + "/uapi/domestic-stock/v1/quotations/inquire-daily-price"
        )
        params = {
            "FID_COND_MRKT_DIV_CODE": "J",
            "FID_INPUT_ISCD": symbol,
            "FID_PERIOD_DIV_CODE": "D",
            "FID_ORG_ADJ_PRC": "0",
        }
        response = requests.get(
            url,
            headers=CommonHeaders.create_korea_investment_headers(
                self, token, "FHKST01010400"
            ),
            params=params,
        )
        logger.debug(response.json())
        return response.json()

    def get_domestic_stock_daily_prices_by_industry(self, token):
        """국내주식 업종별 시세 조회"""
        url = (
            KOREA_INVESTMENT_BASE_URL
            + "/uapi/domestic-stock/v1/quotations/inquire-daily-indexchartprice"
        )
        params = {
            "FID_COND_MRKT_DIV_CODE": "U",
            "FID_INPUT_ISCD": "0002",
            "FID_INPUT_DATE_1": "20230101",
            "FID_INPUT_DATE_2": "20230116",
            "FID_PERIOD_DIV_CODE": "D",
        }
        response = requests.get(
            url,
            headers=CommonHeaders.create_korea_investment_headers(
                self, token, "HHDFS76240000"
            ),
            params=params,
        )
        logger.debug(response.json())
        return response.json()

    def get_overseas_stock_price(self, token, excd, symb):
        """해외주식 현재가 조회"""
        url = KOREA_INVESTMENT_BASE_URL + "/uapi/overseas-price/v1/quotations/price"
        params = {"AUTH": "", "EXCD": excd, "SYMB": symb}
        response = requests.get(
            url,
            headers=CommonHeaders.create_korea_investment_headers(
                self, token, "HHDFS00000300"
            ),
            params=params,
        )
        logger.debug(response.json())
        return response.json()

    def get_overseas_stock_daily_prices(self, token, excd, symb):
        """해외주식 일자별 시세 조회"""
        url = (
            KOREA_INVESTMENT_BASE_URL + "/uapi/overseas-price/v1/quotations/dailyprice"
        )
        params = {
            "AUTH": "",
            "EXCD": excd,
            "SYMB": symb,
            "GUBN": "0",
            "BYMD": "",
            "MODP": "1",
            "KEYB": "",
        }
        response = requests.get(
            url,
            headers=CommonHeaders.create_korea_investment_headers(
                self, token, "HHDFS76240000"
            ),
            params=params,
        )
        logger.debug(response.json())
        return response.json()
