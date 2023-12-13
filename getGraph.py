from getRecentPrices import *
import requests
import xmltodict
import json
import sqlite3
import sys
from user_DB import *
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정 (예시: 나눔고딕)
font_path = "C:/Windows/Fonts/NanumGothic.ttf"  # 나눔고딕 폰트 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

def getGraph(element, unit, price, productNo):

    days = ["40", "30", "20", "10", "today"]
    #prices = []

    if(productNo == '-'):
        return
    

    p_cert_key = "8b73d53c-3f47-48bb-a8fb-5541b85d3ace"
    p_cert_id = "jhe93"
    response_format = "xml"
    p_productno = productNo
    
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

        #print(json_data)

        # JSON 데이터에서 필요한 정보 추출 및 출력
        items = json_data.get('document', {}).get('price', {}).get('item', [])
        if not isinstance(items, list):
            items = [items]  # 단일 객체일 경우 리스트로 변환

        for item in items:
            d40 = int(item.get('d40', '0') or '0')  # 0으로 기본값 설정
            d30 = int(item.get('d30', '0') or '0')
            d20 = int(item.get('d20', '0') or '0')
            d10 = int(item.get('d10', '0') or '0')
            d0 = int(item.get('d0', '0') or '0')

            # item_name = item_name.split("/")[0]
            # 날짜와 위치가 중복되지 않으면 출력하고 중복을 추가
            # print(f"품목 : {item_name}   오늘의 도매가 : {todayPrice}")
        thisYear = items[0]
        prices = [int(thisYear.get('d40', '0') or '0'),
                int(thisYear.get('d30', '0') or '0'),
                int(thisYear.get('d20', '0') or '0'),
                int(thisYear.get('d10', '0') or '0'),
                int(thisYear.get('d0', '0') or '0')]
            
        print("d40: ", thisYear['d40'])    
        print("d30: ", thisYear['d30'])    
        print("d20: ", thisYear['d20'])    
        print("d10: ", thisYear['d10'])    
        print("d0: ", thisYear['d0'])    

        # res = getRecentPrices(429)
        #print(prices)

        valid_data = [(day, price) for day, price in zip(days, prices) if day is not None and price is not None]

        if not valid_data:
            print("No valid data to plot.")
            return

        # 데이터가 있는 경우 그래프 그리기
        days, prices = zip(*valid_data)  # 다시 언패킹
        plt.plot(days, prices, marker='o', linestyle='-')

        # 그래프에 제목과 축 레이블 추가
        #print(element)
        plt.title(str(element) + ' 가격의 경향성')
        plt.xlabel('Days')
        plt.ylabel('Prices')

        # y축 범위 수동으로 지정
        plt.ylim(min(prices) - 1000, max(prices) + 1000)

        # 그래프 보여주기
        plt.show()
            
    else:
        print(f'에러 코드 : {res.status_code}')
