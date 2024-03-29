import requests
import yaml

with open("config.yaml", encoding="UTF-8") as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)

STOCK_PLUS_BASE_URL = _cfg["STOCK_PLUS_BASE_URL"]
WOWTV_BASE_URL = _cfg["WOWTV_BASE_URL"]


class Crawlings:
    def crawling_stock_plus():
        url = STOCK_PLUS_BASE_URL
        response = requests.get(url)
        # print(response)
        return response.text

    def crawling_wow_tv():
        url = WOWTV_BASE_URL
        response = requests.get(url)
        # print(response)
        return response.text
