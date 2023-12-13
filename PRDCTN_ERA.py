import requests
from datetime import datetime, timedelta
import json
import re  # 정규 표현식 라이브러리 추가
import sqlite3
from user_DB import *


def getLaterSeasonalProduce():

    # 예시 API 키
    api_key = "d3a4f4b11aa74ba09c4b9a1dc13aa0eb289176ff9f1e9bdf9390138b5fb1ffac"

    base_url = "http://211.237.50.150:7080/openapi/"
    api_url = "Grid_20171128000000000572_1"

    url = f"{base_url}{api_key}/json/{api_url}/1/1000?"  # Change 'xml' to 'json'

    # API 호출
    res = requests.get(url)

    if res.status_code == 200:
        json_data = res.json()

        # JSON 데이터에서 필요한 정보 추출 및 출력
        items = json_data.get('Grid_20171128000000000572_1', {}).get('row', [])
        if not isinstance(items, list):
            items = [items]  # 단일 객체일 경우 리스트로 변환

        later_seasonal_produce = []

        for item in items:
            produce_name = item.get('PRDLST_NM', 'N/A')
            season = item.get('M_DISTCTNS', 'N/A')
            season_range = item.get('PRDCTN__ERA', 'N/A')
            produce_cl = item.get('PRDLST_CL', 'N/A')

            later_seasonal_produce.append((produce_name, season, season_range))


            # 현재 달보다 1~2달 후에 시작하는 농산물 추출
            current_month = datetime.now().month +5
            # 정규 표현식을 사용하여 숫자 부분만 추출
            start_month = int(re.search(r'\d+', season_range).group()) if re.search(r'\d+', season_range) else None
            if start_month and start_month in [(current_month + 1) % 12, (current_month + 2) % 12]:
                later_seasonal_produce.append((produce_name, season, season_range))
        
        print(later_seasonal_produce)
        save_crops(produce_name, season)
        return later_seasonal_produce

    else:
        print(f'에러 코드 : {res.status_code}')
        return None

