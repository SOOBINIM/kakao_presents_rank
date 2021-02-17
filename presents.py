import urllib.request as req
import json
import requests


# productCollectionIds = 49274

# url_target = 'https://gift.kakao.com/a/v1/pages/productGroups/collections?page=2&size=100&productCollectionIds=' + \
#     str(productCollectionIds)+'&filteringSoldOut=true&sortProperty=PRIORITY'
# data = requests.get(url_target)
# resp = data.json()

# print(resp)

def change():

    for i in range(3842, 3854):

        url = 'https://gift.kakao.com/a/v1/pages/'+str(i)
        data = requests.get(url)
        resp = data.json()

        try:
            # print(url)
            try:
                if resp['name']:
                    thema = resp['name']

                else:
                    thema = '테마 없음'
                thema_split = thema.split('_')
                print("# 테마 : ", thema_split[1])

                productCollectionIds = resp['components'][1]['property'][
                    'collections'][0]['searchCondition']['productCollectionIds'][0]

                url_target = 'https://gift.kakao.com/a/v1/pages/productGroups/collections?page=1&size=100&productCollectionIds=' + \
                    str(productCollectionIds) + \
                    '&filteringSoldOut=true&sortProperty=PRIORITY'
                data = requests.get(url_target)
                resp = data.json()
                # print(productCollectionIds)
                if resp['items']:
                    items = resp['items']

                    for idx, item in enumerate(items):
                        name = item['displayName']
                        brand_name = item['brandName']

                        if brand_name == '':
                            print('순위 = {0}  상품명 :{1}' .format(idx+1, name))
                        else:
                            continue
                else:
                    print("???")
            except:
                1
        except:
            1

    # except:
    #     1


if __name__ == "__main__":
    change()
