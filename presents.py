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

    # 카테고리 명으로 확인하기
    reg = '라이프테마'
    value = "라이프테마"
    brandName = "고려인삼"
    searchList = []

    for i in range(6500, 6600):

        url = 'https://gift.kakao.com/a/v1/pages/'+str(i)
        data = requests.get(url)
        resp = data.json()

        try:
            if (resp['name']):
                thema = resp['name']
                category = re.search(reg, thema)

                if category:
                    if (category.group() == value):
                        print("# 테마 : {0} ({1})" .format(thema, category.group()))
                        print(i)
                        productCollectionIds = resp['components'][1]['property'][
                            'collections'][0]['searchCondition']['productCollectionIds'][0]
                        for y in range(productCollectionIds, productCollectionIds+4):

                            url_target = 'https://gift.kakao.com/a/v1/pages/productGroups/collections?page=1&size=100&productCollectionIds=' + \
                                str(y) + \
                                '&filteringSoldOut=true&sortProperty=PRIORITY&sortDir=DESC'
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
                                        # print(searchList)
                                        print(productCollectionIds)
                                        print("# 테마 : {0} ({1})" .format(
                                            thema, category.group()))
                                        print('순위 = {0}  상품명 :{1}' .format(
                                            idx+1, name))
                                    else:
                                        continue
                            else:
                                continue
                else:
                    print("날짜가 일치 하지 않습니다. {0}" .format(thema))
                    print("라이프 테마가 아닙니다. {0}" .format(thema))
                    print("brand_name :  {0}" .format(items['brandName']))
                    continue

        except:
            # print("{0}번째에는 프로모션이 없습니다. ".format(i))
            pass

    f = open(f'{value}.csv', 'w', encoding='cp949', newline='')  # 파일오픈
    csvWriter = csv.writer(f)  # 열어둔 파일
    for i in searchList:
        csvWriter.writerow(i)
    f.close()


if __name__ == "__main__":
    rank()
