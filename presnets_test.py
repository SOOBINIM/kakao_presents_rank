import urllib.request as req
import json
import requests
import re
from datetime import datetime
import pandas as pd
import csv


def rank():
    # 해당 날짜로 확인하기
    # today = "7/5"
    # reg = '\d{1,2}\/\d{1,2}'

    # "라이프테마" 정규표현식
    life_thema_name_reg = '(?<=_).*(?=_)' # 추천 
    life_thema_date_reg = '\d{1,2}\/\d{1,2}'

    # '라이프테마 중 생일' 정규표현식
    life_thema_name = '라이프테마'
    life_thema_birth_day_name = '생일'

    # "추천" 정규표현식
    recommend_thema_name_reg_ = '10시오픈추천탭'
    recommend_thema_date_reg_ = '.*(?= 10시오픈추천탭)'
    
    # 브랜드명 검색
    brandName = "고려인삼"    

    # 카테고리 명으로 확인하기
    
    searchList = []

    for i in range(6400, 6600):

        url = 'https://gift.kakao.com/a/v1/pages/'+str(i)
        data = requests.get(url)
        resp = data.json()

        try:
            if (resp['name']):
                thema = resp['name']
                print("테마명 : {0}".format(thema))

                life_thema = re.search(life_thema_name, thema) # 라이프테마
                # life_thema_name = re.search(life_thema_name_reg, thema)  # 가벼운선물     
                recommend_thema_name = re.search(recommend_thema_name_reg_, thema) # 추천
                productCollectionIds = resp['components'][1]['property']['collections'][0]['searchCondition']['productCollectionIds'][0]
                print("########## life_thema : {0}".format(life_thema))
                # print("$$$$$$$$$$ life_thema_name : {0}".format(life_thema_name))
                print("########## recommend_thema_name : {0}".format(recommend_thema_name))


                if life_thema.group() == '라이프테마':                    
                    life_thema_name = re.search(life_thema_name_reg, thema)
                    print("# 테마 : {0} ({1})" .format(thema, life_thema_name.group()))
                    print("$$$$$$$$$$ life_thema_name : {0}".format(life_thema_name))
                    if life_thema_name.group() == '생일':
                        for i in range(productCollectionIds, productCollectionIds + 4):
                            url_target = 'https://gift.kakao.com/a/v1/pages/productGroups/collections?page=1&size=100&productCollectionIds=' + str(i) +'&filteringSoldOut=true&sortProperty=PRIORITY&sortDir=DESC'
                            data = requests.get(url_target)
                            response = data.json()
                            items = response['items']
                            if items:
                                for idx, item in enumerate(items):                                
                                    temp = []
                                    name = item['displayName']
                                    brand_name = item['brandName']
                                    if brand_name == brandName:
                                        temp.append(thema)
                                        temp.append(idx+1)
                                        temp.append(name)
                                        searchList.append(temp)
                                        print('순위 = {0}  상품명 :{1}' .format(idx+1, name))
                                    else:
                                        continue
                            else:
                                continue                        
                    else:
                        url_target = 'https://gift.kakao.com/a/v1/pages/productGroups/collections?page=1&size=100&productCollectionIds=' + str(productCollectionIds) +'&filteringSoldOut=true&sortProperty=PRIORITY&sortDir=DESC'
                        data = requests.get(url_target)
                        response = data.json()
                        items = response['items']
                        if items:
                            for idx, item in enumerate(items):                                
                                temp = []
                                name = item['displayName']
                                brand_name = item['brandName']
                                if brand_name == brandName:
                                    temp.append(thema)
                                    temp.append(idx+1)
                                    temp.append(name)
                                    searchList.append(temp)
                                    print('순위 = {0}  상품명 :{1}' .format(idx+1, name))
                                else:
                                    continue
                        else:
                            continue                       
                elif recommend_thema_name.group() == '추천':
                    for i in range(productCollectionIds, productCollectionIds + 4):
                        url_target = 'https://gift.kakao.com/a/v1/pages/productGroups/collections?page=1&size=100&productCollectionIds=' + str(i) +'&filteringSoldOut=true&sortProperty=PRIORITY&sortDir=DESC'
                        data = requests.get(url_target)
                        response = data.json()
                        items = response['items']
                        if items:
                            for idx, item in enumerate(items):                                
                                temp = []
                                name = item['displayName']
                                brand_name = item['brandName']
                                if brand_name == brandName:
                                    temp.append(thema)
                                    temp.append(idx+1)
                                    temp.append(name)
                                    searchList.append(temp)
                                    print('순위 = {0}  상품명 :{1}' .format(idx+1, name))
                                else:
                                    continue
                        else:
                            continue                    

                else: 
                    print("라이프테마, 추천 텝이 아닙니다.")
        except:
            print("{0}번째에는 프로모션이 없습니다. ".format(i))
            pass

    f = open(f'{life_thema_name}.csv', 'w', encoding='cp949', newline='')  # 파일오픈
    csvWriter = csv.writer(f)  # 열어둔 파일
    for i in searchList:
        csvWriter.writerow(i)
    f.close()


if __name__ == "__main__":
    rank()




                # 테마명 : 추천, 생일 인 경우에는 4바퀴를 돈다.
                
                # 추천 : 8/3 10시오픈추천탭
                # 추천_테마명 : 10시오픈추천탭
                # 추천_날짜 : .*(?= 10시오픈추천탭)

                # 생일 : 라이프테마_생일_8/9 주차
                # 생일_테마명 : (?<=_).*(?=_)
                # 생일_날짜 : \d{1,2}\/\d{1,2}


                # 
                # 아닌 경우에는 그냥 돈다 .  




                



