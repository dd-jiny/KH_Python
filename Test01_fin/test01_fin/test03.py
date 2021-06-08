# -- coding:utf-8 --
import json
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
    #print('{}[{}]'.format(name, image))

    tmp = {}
    tmp['name'] = name
    tmp['image'] = image
    lst.append(tmp)

result = {}
result['teachers'] = lst

res_json = json.dumps(result, ensure_ascii=False)
#print(res_json)

with open('teachers.json','w',encoding ='UTF-8')as f:
    f.write(res_json)