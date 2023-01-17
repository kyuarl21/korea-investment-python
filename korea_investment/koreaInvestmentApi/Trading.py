import json
import requests
import yaml
from koreaInvestmentApi.Headers import Headers

with open('config.yaml', encoding='UTF-8') as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)
    
KOREA_INVESTMENT_BASE_URL = _cfg['KOREA_INVESTMENT_BASE_URL']
KOREA_INVESTMENT_APP_KEY = _cfg['KOREA_INVESTMENT_APP_KEY']
KOREA_INVESTMENT_APP_SECRET = _cfg['KOREA_INVESTMENT_APP_SECRET']
CANO = _cfg['CANO']
ACNT_PRDT_CD = _cfg['ACNT_PRDT_CD']

class Trading:
    def __init__(self, token, symbol, quantity):
        self.token = token
        self.symbol = symbol
        self.quantity = quantity
        
    def orderDomesticStock(self, token, symbol, quantity):
        """ 국내주식 주문 """
        url = KOREA_INVESTMENT_BASE_URL + "/uapi/domestic-stock/v1/trading/order-cash"
        body = {
            "CANO": CANO,
            "ACNT_PRDT_CD": ACNT_PRDT_CD,
            "PDNO": symbol,
            "ORD_DVSN": "01",
            "ORD_QTY": str(quantity),
            "ORD_UNPR": "0"
        }
        response = requests.post(url, headers = Headers.createKoreaInvestmentHeaders(self, token, "VTTC0802U"), data=json.dumps(body))
        #print(response.json())
        if response.json()['rt_cd'] == '0':
            (f"[매수 성공]{str(response.json())}")
        else:
            (f"[매수 실패]{str(response.json())}")
        
    def getDomesticAvailableBalance(self, token, symbol):
        """ 국내주식 매수가능 조회 """
        url = KOREA_INVESTMENT_BASE_URL + "/uapi/domestic-stock/v1/trading/inquire-psbl-order"
        params = {
            "CANO": CANO,
            "ACNT_PRDT_CD": ACNT_PRDT_CD,
            "PDNO": symbol,
            "ORD_UNPR": "0",
            "ORD_DVSN": "01",
            "CMA_EVLU_AMT_ICLD_YN": "Y",
            "OVRS_ICLD_YN": "Y"
        }
        response = requests.get(url, headers = Headers.createKoreaInvestmentHeaders(self, token, "VTTC8908R"), params = params)
        #print(response.json())
        cash = response.json()['output']['ord_psbl_cash']
        return cash
    
    def orderDomesticStock(self, token, trId, excg, pdno, quantity):
        """ 해외주식 주문 """
        """[실전투자]
            JTTT1002U : 미국 매수 주문
            JTTT1006U : 미국 매도 주문
            TTTS0308U : 일본 매수 주문
            TTTS0307U : 일본 매도 주문
            TTTS0202U : 상해 매수 주문
            TTTS1005U : 상해 매도 주문
            TTTS1002U : 홍콩 매수 주문
            TTTS1001U : 홍콩 매도 주문
            TTTS0305U : 심천 매수 주문
            TTTS0304U : 심천 매도 주문
            TTTS0311U : 베트남 매수 주문
            TTTS0310U : 베트남 매도 주문

            [모의투자]
            VTTT1002U : 미국 매수 주문
            VTTT1001U : 미국 매도 주문
            VTTS0308U : 일본 매수 주문
            VTTS0307U : 일본 매도 주문
            VTTS0202U : 상해 매수 주문
            VTTS1005U : 상해 매도 주문
            VTTS1002U : 홍콩 매수 주문
            VTTS1001U : 홍콩 매도 주문
            VTTS0305U : 심천 매수 주문
            VTTS0304U : 심천 매도 주문
            VTTS0311U : 베트남 매수 주문
            VTTS0310U : 베트남 매도 주문
            
            NASD : 나스닥
            NYSE : 뉴욕
            AMEX : 아멕스
            SEHK : 홍콩
            SHAA : 중국상해
            SZAA : 중국심천
            TKSE : 일본
            HASE : 베트남 하노이
            VNSE : 베트남 호치민"""
        url = KOREA_INVESTMENT_BASE_URL + "/uapi/overseas-stock/v1/trading/order"
        body = {
            "CANO": CANO,
            "ACNT_PRDT_CD": ACNT_PRDT_CD,
            "OVRS_EXCG_CD": excg,
            "PDNO": pdno,
            "ORD_QTY": str(quantity),
            "OVRS_ORD_UNPR": "0",
            "SLL_TYPE": "", # 제거 : 매수, 00 : 매도
            "ORD_SVR_DVSN_CD": "0",
            "ORD_DVSN": ""
        }
        response = requests.post(url, headers = Headers.createKoreaInvestmentHeaders(self, token, trId), data=json.dumps(body))
        #print(response.json())
        if response.json()['rt_cd'] == '0':
            (f"[매수 성공]{str(response.json())}")
        else:
            (f"[매수 실패]{str(response.json())}")
    
    def orderDomesticStock(self, token, trId, excg, unpr, item):
        """ 해외주식 매수가능 조회 모의투자 미지원 """
        """※ PSBL_YN(주야간 원장 구분) 값으로 tr_id 구분해서 API 호출
            - 해외주식주문 > 해외주식 주야간원장구분조회 API문서 참조
            - url : /uapi/overseas-stock/v1/trading/dayornight

            [실전투자]
            JTTT3007R : PSBL_YN(주야간 원장 구분) = 'Y' (야간용)
            TTTS3007R : PSBL_YN(주야간 원장 구분) = 'N' (주간용)"""
        url = KOREA_INVESTMENT_BASE_URL + "/uapi/overseas-stock/v1/trading/inquire-psamount"
        body = {
            "CANO": CANO,
            "ACNT_PRDT_CD": ACNT_PRDT_CD,
            "OVRS_EXCG_CD": excg,
            "OVRS_ORD_UNPR": unpr,
            "ITEM_CD": item
        }
        response = requests.post(url, headers = Headers.createKoreaInvestmentHeaders(self, token, trId), data=json.dumps(body))
        print(response.json())
        return response.json()