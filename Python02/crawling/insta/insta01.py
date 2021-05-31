# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

tag = input('search tags : ')
url = 'https://www.instagram.com/explore/tags/' + tag 

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

#print(soup)

print(soup.find('div', {'class', '_9AhH0'}))
#여기까지 none이 되는 이유 -> 응답된 이후의 데이터 이기 때문이럴 때 필요한 것 동적 크롤링 셀레니움~