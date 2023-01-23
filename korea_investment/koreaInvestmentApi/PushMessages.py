import datetime
import json
import requests
import time
import yaml

with open('config.yaml', encoding='UTF-8') as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)
    
KAKAO_BASE_URI = _cfg['KAKAO_BASE_URI']

class PushMessages:
    def __init__(self, token, text):
        self.token = token
        self.text = text
    
    def kakao_push_messages(token, text):
        """ Push kakao messages """
        url = KAKAO_BASE_URI + "/v2/api/talk/memo/default/send"
        headers = {
            "Authorization": "Bearer " + token
        }
        body = {
            "template_object" : json.dumps({
                "object_type" : "text",
                "text" : text,
                "link": {
                    #"web_url": "https://developers.kakao.com",
                    #"mobile_web_url": "https://developers.kakao.com"
                }
                #"button_title": "바로 확인"
            })
        }
        response = requests.post(url, headers = headers, data = body)
        if response.json().get('result_code') == 0:
            print('메시지를 성공적으로 보냈습니다.')
        else:
            print('메시지를 성공적으로 보내지 못했습니다. 오류메시지: ' + str(response.json()))
        
        return response.json()