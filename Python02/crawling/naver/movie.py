# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn#')
#print(resp)

soup = BeautifulSoup(resp, 'html.parser')
#print(soup) beautifulsoup 객체로 반환~ -> 내가 원하는거 가져오기 위해 

movies = soup.find_all('dl', class_='lst_dsc')
print(movies[0])

for movies in movies:
    # 영화제목 [평점]
    # ex)스파이럴 [9.83]
    title = movies.find('a').text 
    #print(title) 일단 제목만 나온다 
    star = movies.find('span', class_= 'num').text
    print('{} [{}]'.format(title, star))