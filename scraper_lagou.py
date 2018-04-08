import urllib.request
from bs4 import BeautifulSoup
import re

def getPage(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

def main():
    web_address = 'http://www.lagou.com'
    getPage(web_address)

if __name__ == "__main__":
    main()