import requests
import xmltodict
import json
import sqlite3
from user_DB import *


def getPrice(p_cert_key, p_cert_id, response_format):
    
    base_url = "http://www.kamis.or.kr/service/price/xml.do"

    
    # API 호출에 필요한 매개변수 설정
    params = {
        'action': 'dailySalesList',
        'p_cert_key' : p_cert_key,
        'p_cert_id'  : p_cert_id,
        'p_returntype' : response_format
    }
    
    # API 호출
    url = f"{base_url}?action=dailySalesList&p_cert_key={p_cert_key}&p_cert_id{p_cert_id}&p_returntype={response_format}"
    res = requests.get(base_url, params=params)

    
    if res.status_code == 200:
        xml_data = res.text
        json_data = xmltodict.parse(xml_data)

        # print(json_data)

        
        # JSON 데이터에서 필요한 정보 추출 및 출력
        items = json_data.get('document', {}).get('price', {}).get('item', [])
        if not isinstance(items, list):
            items = [items]  # 단일 객체일 경우 리스트로 변환

        for item in items:
            item_name = item.get('item_name', 'N/A')
            todayPrice = item.get('dpr1', 'N/A')

            # 날짜와 위치가 중복되지 않으면 출력하고 중복을 추가
            print(f"품목 : {item_name}   오늘의 도매가 : {todayPrice}")
            
    else:
        print(f'에러 코드 : {res.status_code}')

if __name__ == '__main__':
    p_cert_key = "8b73d53c-3f47-48bb-a8fb-5541b85d3ace"
    p_cert_id = "jhe93"

    create_table()
    user_name = input("사용자의 이름을 입력하세요: ")
    user_location = get_user_location(user_name)

    if user_location:
        print(f"{user_name}님의 위치는 {user_location}입니다.")
        
    else:
        print(f"{user_name}님의 정보를 찾을 수 없습니다.")
        save_user(user_name, input(f"{user_name}님의 위치를 입력하세요: "))
        user_location = get_user_location(user_name)
        print(f"{user_name}님의 위치는 {user_location}입니다.")

    crops_name = input("재배 중인 작물을 입력하세요: ")
    save_crops(crops_name, "3월")
    user_id = get_user_id(user_name)
    crops_id = get_crops_id(crops_name)

    print(user_id, crops_id)
    save_user_crops(crops_id, user_id)

    getPrice(p_cert_key, p_cert_id, "xml")