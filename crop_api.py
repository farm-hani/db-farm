import requests
import xmltodict
import sqlite3

# 위치와 농작물 연결하기
def matchCropAndLocation(userlocation):

    key = "B85LN0baWQzjPRGR9PmWmfTOewb9SF%2BCPxZMU5cVs0xRlqXDm0fPYvg4EORTf%2F3mhqMzahK8sxvvxZ4uVI5MYA%3D%3D"
    area_id = "999999999"  # 전체 지역
    crop_spe_id = "PA999999"  # 전체 작물

    endpoint = 'http://apis.data.go.kr/1360000/FmlandWthrInfoService/getMmStatistics'
    url = f"{endpoint}?serviceKey={key}&pageNo=1&numOfRows=200&ST_YM=202311&ED_YM=202311&AREA_ID={area_id}&PA_CROP_SPE_ID={crop_spe_id}"
    res = requests.get(url)

    recommendCrops = []

    if res.status_code == 200:
        xml_data = res.text
        json_data = xmltodict.parse(xml_data)

        # JSON 데이터에서 필요한 정보 추출 및 SQLite에 저장
        items = json_data.get('response', {}).get('body', {}).get('items', {}).get('item', [])
        if not isinstance(items, list):
            items = [items]  # 단일 객체일 경우 리스트로 변환

        for item in items:
            crop_name = item.get('paCropName', 'N/A')
            cropLocation = item.get('areaName', 'N/A')

            if(cropLocation == userlocation):
                recommendCrops.append((crop_name, cropLocation))
                #print(f"위치 : {item.get('areaName', 'N/A')}   작물 명 : {crop_name}")


        if len(recommendCrops) == 0:
            print("일치하는 농작물이 없습니다.")
            return 0
        else:
            return recommendCrops

    else:
        print(f'에러 코드 : {res.status_code}')
