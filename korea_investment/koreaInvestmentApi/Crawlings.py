import datetime
import json
import requests
import time
import yaml

with open('config.yaml', encoding='UTF-8') as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)
    
STOCK_PLUS_BASE_URL = _cfg['STOCK_PLUS_BASE_URL']
WOWTV_BASE_URL = _cfg['WOWTV_BASE_URL']

class Crawlings:
#    def __init__(self):
#        self = self
        
    def crawlingStockPlus():
        url = STOCK_PLUS_BASE_URL
        response = requests.get(url)
        #print(response)
        return response.text

    def crawlingWowTV():
        url = WOWTV_BASE_URL
        response = requests.get(url)
        #print(response)
        return response.text