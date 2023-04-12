import yaml
from korea_investment_api.crawlings import Crawlings
from korea_investment_api.holdings import Holdings
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


class DomesticMonitoring:
    def monitoring_kospi_stocks(self, kospiSymbols):
        ACCESS_TOKEN = TokenManagement.issue_korea_investment_token()
        stocks_balance = Holdings.get_domestic_stocks_balance(self, ACCESS_TOKEN)
        response_array = []
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
            print("symbol: " + str(symbol) + "  target: " + str(target))

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
                order_response["output"]["symbol"] = symbol
            elif float(target) >= float(70):
                for holdings in stocks_balance["output1"]:
                    if str(holdings["pdno"]) == str(symbol):
                        order_response = Trading.order_domestic_stock(
                            self,
                            ACCESS_TOKEN,
                            "VTTC0801U",
                            holdings["pdno"],
                            holdings["ord_psbl_qty"],
                        )
                        order_response["output"]["symbol"] = symbol

            response_array.append(order_response)

        logger.debug(response_array)
        return response_array

    def monitoring_kosdaq_stocks(self, kosdaqSymbols):
        ACCESS_TOKEN = TokenManagement.issue_korea_investment_token()
        stocks_balance = Holdings.get_domestic_stocks_balance(self, ACCESS_TOKEN)
        response_array = []
        for symbol in kosdaqSymbols:
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
            print("symbol: " + str(symbol) + "  target: " + str(target))

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
                order_response["output"]["symbol"] = symbol
            elif float(target) >= float(70):
                for holdings in stocks_balance["output1"]:
                    if str(holdings["pdno"]) == str(symbol):
                        order_response = Trading.order_domestic_stock(
                            self,
                            ACCESS_TOKEN,
                            "VTTC0801U",
                            holdings["pdno"],
                            holdings["ord_psbl_qty"],
                        )
                        order_response["output"]["symbol"] = symbol

            response_array.append(order_response)

        logger.debug(response_array)
        return response_array
