import requests
import xmltodict
from datetime import datetime, timedelta
from user_DB import get_user_location, save_user, create_table

# [ 1 ] 5년 간 해당 날짜의 정보 가져오기
def getArgiWeather(location, key, target_date):
    endpoint = 'http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/GnrlWeather/getWeatherTimeList'
    
    # 중복을 제거하기 위한 날짜와 위치 집합
    unique_info = set()

    # 현재 날짜부터 5년 전까지의 데이터를 가져오기 위한 반복문
    for i in range(5):
        # 현재 날짜에서 i년 전의 날짜로 변경
        current_date = target_date - timedelta(days=i * 365)
        current_date_str = current_date.strftime('%Y-%m-%d')

        url = f"{endpoint}?serviceKey={key}&page_No=1&page_Size=1&obsr_Spot_Nm={location}&date_Time={current_date_str}"
        res = requests.get(url)
        
        if res.status_code == 200:
            xml_data = res.text
            json_data = xmltodict.parse(xml_data)

            # JSON 데이터에서 필요한 정보 추출 및 출력
            items = json_data.get('response', {}).get('body', {}).get('items', {}).get('item', [])
            if not isinstance(items, list):
                items = [items]  # 단일 객체일 경우 리스트로 변환

            for item in items:
                date = item.get('date', 'N/A')
                info = (date, item.get('stn_Name', 'N/A'))

                # 날짜와 위치가 중복되지 않으면 출력하고 중복을 추가
                if info not in unique_info:
                    print(f"날짜 : {date}   위치 : {item.get('stn_Name', 'N/A')}   기온 : {item.get('temp', 'N/A')}   최고기온 : {item.get('max_Temp', 'N/A')}   최저기온 : {item.get('min_Temp', 'N/A')}   습도 : {item.get('hum', 'N/A')}   강수량 : {item.get('rain', 'N/A')}   토양 수분: {item.get('soil_Wt', 'N/A')}")
                    unique_info.add(info)
        else:
            print(f'에러 코드 : {res.status_code}')


# [ 2 ] 사용자의 이름을 입력받아서 위치 정보를 불러오기
def get_user_location_and_weather():
    create_table()  # 테이블이 없을 경우 생성

    user_name = input("사용자의 이름을 입력하세요: ")
    user_location = get_user_location(user_name)

    if user_location:
        print(f"{user_name}님의 위치는 {user_location}입니다.")
        
        # [ 1 ] 날씨 정보 가져오기
        key = "B85LN0baWQzjPRGR9PmWmfTOewb9SF%2BCPxZMU5cVs0xRlqXDm0fPYvg4EORTf%2F3mhqMzahK8sxvvxZ4uVI5MYA%3D%3D"
        target_date = datetime.now()
        getArgiWeather(user_location, key, target_date)
    else:
        print(f"{user_name}님의 정보를 찾을 수 없습니다.")
        save_user(user_name, input(f"{user_name}님의 위치를 입력하세요: "))
        user_location = get_user_location(user_name)
        print(f"{user_name}님의 위치는 {user_location}입니다.")
        key = "B85LN0baWQzjPRGR9PmWmfTOewb9SF%2BCPxZMU5cVs0xRlqXDm0fPYvg4EORTf%2F3mhqMzahK8sxvvxZ4uVI5MYA%3D%3D"
        target_date = datetime.now()
        getArgiWeather(user_location, key, target_date)

if __name__ == '__main__':
    get_user_location_and_weather()