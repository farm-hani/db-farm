# import requests

# def getGeoCode(address, client_id,client_secret):

#     header = {
#         "X-NCP-APIGW-API-KEY-ID":"yckqlorpai",
#         "X-NPC-APIGW-API-KEY":"0b8YgLUO7I2pJoBQQRWfR98FhHEGTIpxFSu6C4E8",
#     }

#     endpoint = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
#     url = f"{endpoint}?query={address}"

#     res = requests.get(url,headers=header)

#     return res

import requests

def getAirQualityByCity(city, key):
    endpoint = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
    url = f"{endpoint}?sidoName={city}&pageNo=1&returnType=json&numOfRows=100&serviceKey={key}&ver=1.0"
    res = requests.post(url)

    return res

if __name__ == '__main__':
    city = "인천"
    key = "B85LN0baWQzjPRGR9PmWmfTOewb9SF%2BCPxZMU5cVs0xRlqXDm0fPYvg4EORTf%2F3mhqMzahK8sxvvxZ4uVI5MYA%3D%3Dy"
    #key = "B85LN0baWQzjPRGR9PmWmfTOewb9SF+CPxZMU5cVs0xRlqXDm0fPYvg4EORTf/3mhqMzahK8sxvvxZ4uVI5MYA=="


    response = getAirQualityByCity(city, key)
   
    if (response.status_code == 200):
        response_json = response.json()

        response_body = response_json['response']['body']
        print("잘나와?")
        for item in response_body['items']:
            print(f"{item['stationName']}\tPM10: {item['pm10Value']}ug/m3")
    else:
        print(f'Error code : {response}')
        
        
        
