
# 라이브러리 import
import requests
import pprint
import json
import xmltodict
from datetime import datetime, timedelta

def getArgiWeather(location, key, target_date):
    endpoint = 'http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherMonDayList'
    
    # 5년 동안의 데이터를 가져오기 위한 반복문
    for i in range(target_date.year, target_date.year - 5, -1):
        url = f"{endpoint}?serviceKey={key}&page_No=1&obsr_Spot_Nm={location}&search_Year={i}&search_Month={target_date.month}"
        res = requests.get(url)
        
        if res.status_code == 200:
            xml_data = res.text
            json_data = xmltodict.parse(xml_data)

            # JSON 데이터에서 필요한 정보 추출 및 출력
            items = json_data['response']['body'].get('items', {}).get('item', [])
            for item in items:
                print(f"날짜 : {item.get('date', 'N/A')} \t 위치 : {item.get('stn_Name', 'N/A')} \t 기온 : {item.get('temp', 'N/A')} \t 최고기온 : {item.get('max_Temp', 'N/A')} \t 최저기온 : {item.get('min_Temp', 'N/A')} \t 습도 : {item.get('hum', 'N/A')} \t  강수량 : {item.get('rain', 'N/A')} \t 토양 수분: {item.get('soil_Wt', 'N/A')}")
        else:
            print(f'Error code : {res.status_code}')

if __name__ == '__main__':
    location = "청라"
    key = "B85LN0baWQzjPRGR9PmWmfTOewb9SF%2BCPxZMU5cVs0xRlqXDm0fPYvg4EORTf%2F3mhqMzahK8sxvvxZ4uVI5MYA%3D%3D"

    # 현재 날짜에서 11월 10일로 설정
    target_date = datetime(datetime.now().year, 11, 10)

    getArgiWeather(location, key, target_date)
'''
# 라이브러리 import
import requests
import pprint
import json
import xmltodict
from datetime import datetime

def getArgiWeather(location, key, now_year,now_month):
    
    endpoint = 'http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherMonDayList'
    url = f"{endpoint}?serviceKey={key}&page_No=1&Page_Size=31&obsr_Spot_Nm={location}&search_Year={now_year}&search_Month={now_month}"
    res = requests.get(url)
    return res

if __name__ == '__main__':
    location = "완주군 이서면"
    key = "B85LN0baWQzjPRGR9PmWmfTOewb9SF%2BCPxZMU5cVs0xRlqXDm0fPYvg4EORTf%2F3mhqMzahK8sxvvxZ4uVI5MYA%3D%3D"
    now = datetime.now()
    now_year = now.year
    now_month = now.month
    response = getArgiWeather(location, key, now_year, now_month)
    
    
    if(response.status_code ==200):
        xml_data = response.text
        json_data = xmltodict.parse(xml_data)
        
        # JSON 데이터에서 필요한 정보 추출 및 출력
        items = json_data['response']['body'].get('items', {}).get('item', [])
        for item in items:
            print(f"날짜 : {item.get('date', 'N/A')} \t 위치 : {item.get('stn_Name', 'N/A')} \t 기온 : {item.get('temp', 'N/A')} \t 최고기온 : {item.get('max_Temp', 'N/A')} \t 최저기온 : {item.get('min_Temp', 'N/A')} \t 습도 : {item.get('hum', 'N/A')} \t  강수량 : {item.get('rain', 'N/A')} \t 토양 수분: {item.get('soil_Wt', 'N/A')}")
    else:
        print(f'Error code : {response}')
        
        
'''
'''
# url 입력
# url = 'https://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherTenMinList?serviceKey=B85LN0baWQzjPRGR9PmWmfTOewb9SF%2BCPxZMU5cVs0xRlqXDm0fPYvg4EORTf%2F3mhqMzahK8sxvvxZ4uVI5MYA%3D%3D&Page_No=1&Page_Size=20&date=2018-01-01&time=1300&obsr_Spot_Nm=%EA%B0%80%ED%8F%89%EA%B5%B0%20%EA%B0%80%ED%8F%89%EC%9D%8D&obsr_Spot_Code=477802A001&type=json'
# url = 'https://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherTenMinList?serviceKey=B85LN0baWQzjPRGR9PmWmfTOewb9SF+CPxZMU5cVs0xRlqXDm0fPYvg4EORTf/3mhqMzahK8sxvvxZ4uVI5MYA==&Page_No=1&Page_Size=20&date=2023-11-22&time=1300&obsr_Spot_Nm=%EA%B0%80%ED%8F%89%EA%B5%B0%20%EA%B0%80%ED%8F%89%EC%9D%8D&obsr_Spot_Code=477802A001&type=json'


# url = 'https://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherTenMinList'
# my_api_key = 'B85LN0baWQzjPRGR9PmWmfTOewb9SF%2BCPxZMU5cVs0xRlqXDm0fPYvg4EORTf%2F3mhqMzahK8sxvvxZ4uVI5MYA%3D%3D'

# params ={'serviceKey' : 'B85LN0baWQzjPRGR9PmWmfTOewb9SF+CPxZMU5cVs0xRlqXDm0fPYvg4EORTf/3mhqMzahK8sxvvxZ4uVI5MYA==', 'Page_No' : '1', 'Page_Size' : '20', 'date' : '2023-11-22', 'obsr_Spot_Nm' : '가평군 가평읍', 'obsr_Spot_Code' : '477802A001', }

# url 불러오기
response = requests.get(url)

#데이터 값 출력해보기
contents = response.text
print(contents)

import requests

def getAirQualityByCity(city, key):
    endpoint = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
    url = f"{endpoint}?sidoName={city}&pageNo=1&returnType=json&numOfRows=100&serviceKey={key}&ver=1.0"
    res = requests.post(url)

    return res
'''
# if __name__ == '__main__':
#     city = "인천"
#     key = "B85LN0baWQzjPRGR9PmWmfTOewb9SF%2BCPxZMU5cVs0xRlqXDm0fPYvg4EORTf%2F3mhqMzahK8sxvvxZ4uVI5MYA%3D%3Dy"
#     #key = "B85LN0baWQzjPRGR9PmWmfTOewb9SF+CPxZMU5cVs0xRlqXDm0fPYvg4EORTf/3mhqMzahK8sxvvxZ4uVI5MYA=="


#     response = getAirQualityByCity(city, key)
   
#     if (response.status_code == 200):
#         response_json = response.json()

#         response_body = response_json['response']['body']
#         print("잘나와?")
#         for item in response_body['items']:
#             print(f"{item['stationName']}\tPM10: {item['pm10Value']}ug/m3")
#     else:
#         print(f'Error code : {response}')

# # 데이터 결과값 예쁘게 출력해주는 코드
# pp = pprint.PrettyPrinter(indent=4)
# print(pp.pprint(contents))

# #문자열을 json으로 변경
# json_ob = json.loads(contents)
# print(json_ob)
# print(type(json_ob)) #json타입 확인
