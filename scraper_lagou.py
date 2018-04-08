import requests

def getPage(city):
    fromdata = {
        'first': 'true',
        'pn': 1,
        'kd': '测试'
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Referer': 'https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput='
    }
    payload = {
        'city': city,
        'needAddtionalResult': 'false'
    }
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    r = requests.post(url, params=payload, data=fromdata, headers=headers)
    result = r.json()['content']['positionResult']['result']
    print(result)

def main():
    city = input('选择城市：')
    getPage(city)

if __name__ == "__main__":
    main()