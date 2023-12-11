from getRecentPrices import *
import requests
import xmltodict
import json
import sqlite3
from user_DB import *

def getGraph(crops_name):

    p_cert_key = "8b73d53c-3f47-48bb-a8fb-5541b85d3ace"
    p_cert_id = "jhe93"
    response_format = "xml"
    p_productno = 429
    
    base_url = "http://www.kamis.or.kr/service/price/xml.do"

    
    # API 호출에 필요한 매개변수 설정
    params = {
        'action': 'dailySalesList',
        'p_cert_key' : p_cert_key,
        'p_cert_id'  : p_cert_id,
        'p_returntype' : response_format
    }
    
    # API 호출
    url = f"{base_url}?action=recentlyPriceTrendList&p_productno={p_productno}&p_cert_key={p_cert_key}&p_cert_id={p_cert_id}&p_returntype={response_format}"
    res = requests.get(url)
    
    if res.status_code == 200:
        xml_data = res.text
        json_data = xmltodict.parse(xml_data)

        print(json_data)

        # JSON 데이터에서 필요한 정보 추출 및 출력
        items = json_data.get('document', {}).get('price', {}).get('item', [])
        if not isinstance(items, list):
            items = [items]  # 단일 객체일 경우 리스트로 변환

        for item in items:
            d40 = item.get('d40', 'N/A')
            d30 = item.get('d30', 'N/A')
            d20 = item.get('d20', 'N/A')
            d10 = item.get('d10', 'N/A')
            d0 = item.get('d0', 'N/A')

            # item_name = item_name.split("/")[0]
            # 날짜와 위치가 중복되지 않으면 출력하고 중복을 추가
            # print(f"품목 : {item_name}   오늘의 도매가 : {todayPrice}")
        thisYear = items[0]
            
        print("d40: ", thisYear['d40'])    
        print("d30: ", thisYear['d30'])    
        print("d20: ", thisYear['d20'])    
        print("d10: ", thisYear['d10'])    
        print("d0: ", thisYear['d0'])    

        # res = getRecentPrices(429)
        # print(res)
            
    else:
        print(f'에러 코드 : {res.status_code}')


getGraph(429)