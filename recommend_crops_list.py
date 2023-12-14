import requests
import xmltodict
import json
import sqlite3
from user_DB import *
from crop_api import matchCropAndLocation


def recommend_crops_list(user_id):

    location = get_location(user_id)
    print( "<"+ location +"에서 재배하기 좋은 농작물 추천>")

    crops = matchCropAndLocation(location)

    if(crops == 0):
        print("추천할 농작물이 없습니다.")
        return

    unique_crops = list(set(crops))

    print(unique_crops)
    
    
