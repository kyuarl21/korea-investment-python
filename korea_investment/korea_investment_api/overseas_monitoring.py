import yaml
from korea_investment_api.crawlings import Crawlings
from korea_investment_api.holdings import Holdings
from korea_investment_api.logging_handler import LoggingHandler
from korea_investment_api.quotes import Quotes
from korea_investment_api.token_management import TokenManagement
from korea_investment_api.trading import Trading

logger = LoggingHandler.set_logger()

with open('config.yaml', encoding='UTF-8') as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)
    
KOREA_INVESTMENT_BASE_URL = _cfg['KOREA_INVESTMENT_BASE_URL']
KOREA_INVESTMENT_APP_KEY = _cfg['KOREA_INVESTMENT_APP_KEY']
KOREA_INVESTMENT_APP_SECRET = _cfg['KOREA_INVESTMENT_APP_SECRET']
CANO = _cfg['CANO']
ACNT_PRDT_CD = _cfg['ACNT_PRDT_CD']
ACCESS_TOKEN = ""

class OverseasMonitoring:
    
    def monitoring_nasdaq_stocks(self, nasdaqSymbols):
        ACCESS_TOKEN = TokenManagement.issue_korea_investment_token()
        stocks_balance = Holdings.get_overseas_stocks_balance(self, ACCESS_TOKEN)
        print(stocks_balance)
        response_array = []
        excd = "NAS"
        excg = "NASD"
        #test_symbols = ["AAPL", "MSFT", "AMZN"]
        for symbol in nasdaqSymbols:
            present_response = Quotes.get_overseas_stock_price(self, ACCESS_TOKEN, excd, symbol)
            #time.sleep(1)
            daily_response = Quotes.get_overseas_stock_daily_prices(self, ACCESS_TOKEN, excd, symbol)
            #print(daily_response)
            if (daily_response['output1']['nrec'] == ""):
                continue
            #time.sleep(1)
            up_sum = 0; down_sum = 0
            up_index = 0; down_index = 0
            for values in daily_response['output2']:
                if (float(values['rate']) > float(0)):
                    if (up_index == 14):
                        continue
                    up_sum += float(values['diff'])
                    up_index += int(1)
                elif (float(values['rate']) < float(0)):
                    if (down_index == 14):
                        continue
                    down_sum += float(values['diff'])
                    down_index += int(1)
                if (up_index == 14 and down_index == 14):
                    break

            up_average = up_sum / up_index
            down_average = down_sum / down_index
            target = up_average / (up_average + down_average) * 100
            #target2 = (up_average / down_average) / ((up_average / down_average) + 1) * 100
            print("symbol: " + str(symbol) + "  target: " + str(target))
            
            order_response = ""
            quantity = 100
            if (float(target) <= float(30)):
                order_response = Trading.order_overseas_stock(self, ACCESS_TOKEN, "VTTT1002U", excg, symbol, quantity)
                order_response['output']['symbol'] = symbol
            # elif (float(target) >= float(70)):
            #     for holdings in stocks_balance['output1']:
            #         if (str(holdings['ovrs_pdno']) == str(symbol)):
            #             order_response = Trading.order_overseas_stock(self, ACCESS_TOKEN, "VTTT1001U", holdings['ovrs_excg_cd'], holdings['ovrs_pdno'], holdings['ord_psbl_qty'])
            #             order_response['output']['symbol'] = symbol
                
            response_array.append(order_response)
        
        logger.debug(response_array)
        return response_array
    
    def monitoring_new_york_stocks(self, newYorkSymbols):
        ACCESS_TOKEN = TokenManagement.issue_korea_investment_token()
        stocks_balance = Holdings.get_overseas_stocks_balance(self, ACCESS_TOKEN)
        print(stocks_balance)
        response_array = []
        excd = "NYS"
        excg = "NYSE"
        for symbol in newYorkSymbols:
            present_response = Quotes.get_overseas_stock_price(self, ACCESS_TOKEN, excd, symbol)
            #time.sleep(1)
            daily_response = Quotes.get_overseas_stock_daily_prices(self, ACCESS_TOKEN, excd, symbol)
            #print(daily_response)
            if (daily_response['output1']['nrec'] == ""):
                continue
            #time.sleep(1)
            up_sum = 0; down_sum = 0
            up_index = 0; down_index = 0
            for values in daily_response['output2']:
                if (float(values['rate']) > float(0)):
                    if (up_index == 14):
                        continue
                    up_sum += float(values['diff'])
                    up_index += int(1)
                elif (float(values['rate']) < float(0)):
                    if (down_index == 14):
                        continue
                    down_sum += float(values['diff'])
                    down_index += int(1)
                if (up_index == 14 and down_index == 14):
                    break

            up_average = up_sum / up_index
            down_average = down_sum / down_index
            target = up_average / (up_average + down_average) * 100
            #target2 = (up_average / down_average) / ((up_average / down_average) + 1) * 100
            print("symbol: " + str(symbol) + "  target: " + str(target))
            
            order_response = ""
            quantity = 100
            if (float(target) <= float(30)):
                order_response = Trading.order_overseas_stock(self, ACCESS_TOKEN, "VTTT1002U", excg, symbol, quantity)
                order_response['output']['symbol'] = symbol
            # elif (float(target) >= float(70)):
            #     for holdings in stocks_balance['output1']:
            #         if (str(holdings['ovrs_pdno']) == str(symbol)):
            #             order_response = Trading.order_overseas_stock(self, ACCESS_TOKEN, "VTTT1001U", holdings['ovrs_excg_cd'], holdings['ovrs_pdno'], holdings['ord_psbl_qty'])
            #             order_response['output']['symbol'] = symbol
                
            response_array.append(order_response)
        
        logger.debug(response_array)
        return response_array
    
    def monitoring_amex_stocks(self, amexSymbols):
        ACCESS_TOKEN = TokenManagement.issue_korea_investment_token()
        stocks_balance = Holdings.get_overseas_stocks_balance(self, ACCESS_TOKEN)
        print(stocks_balance)
        response_array = []
        excd = "AMS"
        excg = "AMEX"
        for symbol in amexSymbols:
            present_response = Quotes.get_overseas_stock_price(self, ACCESS_TOKEN, excd, symbol)
            #time.sleep(1)
            daily_response = Quotes.get_overseas_stock_daily_prices(self, ACCESS_TOKEN, excd, symbol)
            #print(daily_response)
            if (daily_response['output1']['nrec'] == ""):
                continue
            #time.sleep(1)
            up_sum = 0; down_sum = 0
            up_index = 0; down_index = 0
            for values in daily_response['output2']:
                if (float(values['rate']) > float(0)):
                    if (up_index == 14):
                        continue
                    up_sum += float(values['diff'])
                    up_index += int(1)
                elif (float(values['rate']) < float(0)):
                    if (down_index == 14):
                        continue
                    down_sum += float(values['diff'])
                    down_index += int(1)
                if (up_index == 14 and down_index == 14):
                    break

            up_average = up_sum / up_index
            down_average = down_sum / down_index
            target = up_average / (up_average + down_average) * 100
            #target2 = (up_average / down_average) / ((up_average / down_average) + 1) * 100
            print("symbol: " + str(symbol) + "  target: " + str(target))
            
            order_response = ""
            quantity = 100
            if (float(target) <= float(30)):
                order_response = Trading.order_overseas_stock(self, ACCESS_TOKEN, "VTTT1002U", excg, symbol, quantity)
                order_response['output']['symbol'] = symbol
            # elif (float(target) >= float(70)):
            #     for holdings in stocks_balance['output1']:
            #         if (str(holdings['ovrs_pdno']) == str(symbol)):
            #             order_response = Trading.order_overseas_stock(self, ACCESS_TOKEN, "VTTT1001U", holdings['ovrs_excg_cd'], holdings['ovrs_pdno'], holdings['ord_psbl_qty'])
            #             order_response['output']['symbol'] = symbol
                
            response_array.append(order_response)
        
        logger.debug(response_array)
        return response_array