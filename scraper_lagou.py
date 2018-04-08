import requests

def getPage(city):
    fromdata = {
        'first': 'true',
        'pn': 1,
        'kd': '测试'
    }
    url_position = 'https://www.lagou.com/jobs/positionAjax.json?city={0}needAddtionalResult=false'.format(city)
    r = requests.post(url_position, data=fromdata)
    print(r.text)

def main():
    city = input('选择城市：')
    getPage(city)

if __name__ == "__main__":
    main()