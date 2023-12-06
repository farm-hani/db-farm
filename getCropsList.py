import requests
import xmltodict
import json
import sqlite3
from user_DB import *


def getCropsList(start_idx, end_idx):

    api_key = "d3a4f4b11aa74ba09c4b9a1dc13aa0eb289176ff9f1e9bdf9390138b5fb1ffac"
    
    base_url = "http://211.237.50.150:7080/openapi/"
    api_url = "Grid_20171128000000000572_1"

    url = f"{base_url}{api_key}/json/{api_url}/{start_idx}/{end_idx}?"  # Change 'xml' to 'json'
    
    # API 호출
    res = requests.get(url)
    
    if res.status_code == 200:

        json_data = res.json()
        # print(json_data)

        # JSON 데이터에서 필요한 정보 추출 및 출력
        items = json_data.get('Grid_20171128000000000572_1', {}).get('row', [])
        if not isinstance(items, list):
            items = [items]  # 단일 객체일 경우 리스트로 변환

        for item in items:
            item_name = item.get('PRDLST_NM', 'N/A')
            season = item.get('M_DISTCTNS', 'N/A')

            # 날짜와 위치가 중복되지 않으면 출력하고 중복을 추가
            #print(f"품목 : {item_name}   계절 : {season}")
            #create_table()  # 테이블이 없을 경우 생성
            save_crops(item_name, season)
            print(f"품목 : {item_name}")


            
    else:
        print(f'에러 코드 : {res.status_code}')

if __name__ == '__main__':

    create_table()

    getCropsList(1, 300)