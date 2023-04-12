import yaml
from korea_investment_api.crawlings import Crawlings
from korea_investment_api.logging_handler import LoggingHandler
from korea_investment_api.quotes import Quotes
from korea_investment_api.token_management import TokenManagement
from korea_investment_api.trading import Trading

logger = LoggingHandler.set_logger()

with open("config.yaml", encoding="UTF-8") as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)

KOREA_INVESTMENT_BASE_URL = _cfg["KOREA_INVESTMENT_BASE_URL"]
KOREA_INVESTMENT_APP_KEY = _cfg["KOREA_INVESTMENT_APP_KEY"]
KOREA_INVESTMENT_APP_SECRET = _cfg["KOREA_INVESTMENT_APP_SECRET"]
CANO = _cfg["CANO"]
ACNT_PRDT_CD = _cfg["ACNT_PRDT_CD"]
ACCESS_TOKEN = ""


class AutoTrading:
    def __init__(self):
        self = self

    def auto_trading_domestic_stocks(self):
        ACCESS_TOKEN = TokenManagement.issue_korea_investment_token()
        response_array = []
        kospiSymbols = ["005930", "035420", "035720"]
        for symbol in kospiSymbols:
            # present_response = Quotes.get_domestic_stock_price(self, ACCESS_TOKEN, symbol)
            # time.sleep(1)
            daily_response = Quotes.get_domestic_stock_daily_prices(
                self, ACCESS_TOKEN, symbol
            )
            # time.sleep(1)

            up_sum = 0
            down_sum = 0
            up_index = 0
            down_index = 0
            for values in daily_response["output"]:
                if float(values["prdy_ctrt"]) > float(0):
                    up_sum += int(values["prdy_vrss"])
                    up_index += int(1)
                elif float(values["prdy_ctrt"]) < float(0):
                    down_sum += int(values["prdy_vrss"])
                    down_index += int(1)

            up_average = up_sum / up_index
            down_average = abs(down_sum) / down_index
            target = up_average / (up_average + down_average) * 100
            # target2 = (up_average / down_average) / ((up_average / down_average) + 1) * 100
            print(target)

            available_response = Trading.get_domestic_available_balance(
                self, ACCESS_TOKEN, symbol
            )
            # print(available_response)
            available_cash = available_response["output"]["ord_psbl_cash"]
            # print(available_cash)

            order_response = ""
            quantity = 100
            if float(target) <= float(30):
                order_response = Trading.order_domestic_stock(
                    self, ACCESS_TOKEN, "VTTC0802U", symbol, quantity
                )
            elif float(target) >= float(70):
                order_response = Trading.order_domestic_stock(
                    self, ACCESS_TOKEN, "VTTC0801U", symbol, quantity
                )

            response_array.append(order_response)

        logger.debug(response_array)
        return response_array

    def auto_trading_overseas_stocks(self):
        ACCESS_TOKEN = TokenManagement.issue_korea_investment_token()
        response_array = []
        excd = "NAS"
        excg = "NASD"
        nasdaqSymbols = [
            "AAPL",
            "MSFT",
            "GOOGL",
            "AMZN",
            "NVDA",
            "TSLA",
            "PEP",
            "AVGO",
            "AZN",
            "COST",
            "CSCO",
            "TMUS",
            "CMCSA",
            "TXN",
            "ADBE",
            "AMGN",
            "HON",
            "NFLX",
            "QCOM",
            "SNY",
            "PDD",
            "INTC",
            "INTU",
            "AMD",
            "GILD",
            "JD",
            "ADP",
            "ISRG",
            "MDLZ",
            "AMAT",
            "PYPL",
            "REGN",
        ]
        for symbol in nasdaqSymbols:
            present_response = Quotes.get_overseas_stock_price(
                self, ACCESS_TOKEN, excd, symbol
            )
            # time.sleep(1)
            daily_response = Quotes.get_overseas_stock_daily_prices(
                self, ACCESS_TOKEN, excd, symbol
            )
            # print(daily_response)
            if daily_response["output1"]["nrec"] == "":
                continue
            # time.sleep(1)
            up_sum = 0
            down_sum = 0
            up_index = 0
            down_index = 0
            for values in daily_response["output2"]:
                if float(values["rate"]) > float(0):
                    if up_index == 14:
                        continue
                    up_sum += float(values["diff"])
                    up_index += int(1)
                elif float(values["rate"]) < float(0):
                    if down_index == 14:
                        continue
                    down_sum += float(values["diff"])
                    down_index += int(1)
                if up_index == 14 and down_index == 14:
                    break

            up_average = up_sum / up_index
            down_average = down_sum / down_index
            target = up_average / (up_average + down_average) * 100
            # target2 = (up_average / down_average) / ((up_average / down_average) + 1) * 100
            print(target)

            order_response = ""
            quantity = 100
            if float(target) <= float(30):
                order_response = Trading.order_overseas_stock(
                    self, ACCESS_TOKEN, "VTTT1002U", excg, symbol, quantity
                )
            elif float(target) >= float(70):
                order_response = Trading.order_overseas_stock(
                    self, ACCESS_TOKEN, "VTTT1001U", excg, symbol, quantity
                )

            response_array.append(order_response)

        logger.debug(response_array)
        return response_array
