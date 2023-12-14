import requests
import xmltodict
import json
import sqlite3
from user_DB import *
from getPrice import getPrice
from getGraph import getGraph
from recommend_crops_list import recommend_crops_list
import sys

def add_crops(user_id):

    crops_name = input("재배 중인 작물을 입력하세요: ")
    isExist = find_crops(crops_name)

    if isExist:

        save_crops(crops_name, "3월")
        crops_id = get_crops_id(crops_name)

        print(user_id, crops_id)
        save_user_crops(crops_id, user_id)
    else:
        print("존재하지 않는 농산물입니다.")

def default_function(user_id):
    return "This is the default case"

def switch_case(case, user_id):
        
    switch_dict = {
        'case1': print_my_crops,
        'case2': add_crops,
        'case3': recommend_crops_list,        
        #'case4': sys.exit("다음에 또 이용해 주세요."),
    }
    
    # 해당 case에 대한 함수 호출
    return switch_dict.get(case, default_function)(user_id)

def print_my_crops(user_id):
    res = get_crops_list(user_id)

    if res is None:
        print("No crops found for this user.")
    else:
        myCrops = []
        for element in res:

            # 농산물
            # print(element)

            # 가격, 단위
            price, unit, productNo = getPrice(element)

            # 농산물 + 가격 튜플
            myCrops.append((element, unit, price + '원', productNo))

            getGraph(element, unit, price, productNo)

        print(myCrops)

# main
def main():

    # 테이블 생성
    create_table()
    user_name = input("사용자의 이름을 입력하세요: ")
    user_id = get_user_id(user_name)
    print("user id: ", user_id)

    if user_id:
        print(f"어서오세요 {user_name}님!\n")
        
        while True:
            print("[1: 채소 가격 확인하기, 2: 채소 추가하기, 3: 채소 추천받기 4: 종료하기]")
            num = input(f"사용하실 서비스를 입력하세요: ")
            switch_case("case" + num, user_id)
            print("\n")
        
    else:
        print(f"{user_name}님의 정보를 찾을 수 없습니다.")
        print(f"존재하지 않는 사용자입니다. 회원가입을 진행해주세요.")

        print(f"----[회원가입]----")
        user_name = input(f"이름: ")
        save_user(user_name, input(f"거주지: "))

        

    return

if __name__ == "__main__":
    main()
