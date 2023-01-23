import json
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

class Holdings:
    def __init__(self, token):
        self.token = token
    
    def getDomesticStocksBalance(self, token):
        """ 국내 주식 잔고조회 """
        url = KOREA_INVESTMENT_BASE_URL + "/uapi/domestic-stock/v1/trading/inquire-balance"
        params = {
            "CANO": CANO,
            "ACNT_PRDT_CD": ACNT_PRDT_CD,
            "AFHR_FLPR_YN": "N",
            "OFL_YN": "",
            "INQR_DVSN": "02",
            "UNPR_DVSN": "01",
            "FUND_STTL_ICLD_YN": "Y",
            "FNCG_AMT_AUTO_RDPT_YN": "N",
            "PRCS_DVSN": "00",
            "CTX_AREA_FK100": "",
            "CTX_AREA_NK100": ""
        }
        response = requests.get(url, headers = Headers.createKoreaInvestmentHeaders(self, token, "VTTC8434R"), params = params)
        logger.debug(response.json())
        #cash = response.json()['output']['ord_psbl_cash']
        return response.json()
    
    def getOverseasStocksBalance(self, token):
        """ 해외 주식 잔고조회 """
        """※ PSBL_YN(주야간 원장 구분) 값으로 tr_id 구분해서 API 호출
            - 해외주식주문 > 해외주식 주야간원장구분조회 API문서 참조
            - url : /uapi/overseas-stock/v1/trading/dayornight

            [실전투자]
            JTTT3012R : PSBL_YN(주야간 원장 구분) = 'Y' (야간용)
            TTTS3012R : PSBL_YN(주야간 원장 구분) = 'N' (주간용)

            [모의투자]
            VTTT3012R : PSBL_YN(주야간 원장 구분) = 'Y' (야간용)
            VTTS3012R : PSBL_YN(주야간 원장 구분) = 'N' (주간용)"""
        url = KOREA_INVESTMENT_BASE_URL + "/uapi/overseas-stock/v1/trading/inquire-balance"
        params = {
            "CANO": CANO,
            "ACNT_PRDT_CD": ACNT_PRDT_CD,
            "OVRS_EXCG_CD": "NASD", # 미국 전체
            "TR_CRCY_CD": "USD",
            "CTX_AREA_FK200	": "",
            "CTX_AREA_NK200": ""
        }
        response = requests.get(url, headers = Headers.createKoreaInvestmentHeaders(self, token, "VTTT3012R"), params = params)
        logger.debug(response.json())
        #cash = response.json()['output']['ord_psbl_cash']
        return response.json()