# -- coding:utf-8 --

from bs4 import BeautifulSoup
import urllib.request

resp = urllib.request.urlopen("https://www.iei.or.kr/intro/teacher.kh")

soup = BeautifulSoup(resp, 'html.parser')

teachers = soup.find('div', {'class': 'intro_list'})

li = teachers.select('li')
#print(li[0])

#names = soup.find_all('p', {'class' : 'intro_name'})
#images = soup.find('div', {'class' : 'intro_thum'})
#print(names[0])
#print(image)

lst = list()

for chd in li:
    name = chd.find('p', {'class' :'intro_name'}).text
    image = chd.find('img')['src']
    print('{}[{}]'.format(name, image))