import requests
import json
def getQueryStringParameters():
    FromData = {
        'type': 'uid',
        'value':1889941567,
        'containerid':1076031889941567,
        'page': 2
        }
    return FromData

response = requests.get('https://m.weibo.cn/api/container/getIndex?type=uid&value=1889941567&containerid=1076031889941567&page=2')

json = response.json()
data = json['data']
print(data)

