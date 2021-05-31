# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver 

url = 'https://www.instagram.com/explore/tags/' + input('search tags : ' )

driver = webdriver.Chrome('C:\drivers/chromedriver.exe')

driver.implicitly_wait(3)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
#driver.page_source 는 f12 개발자 도구에서 가져온 코드를 드라이버가 읽어서 뭐 어쩌구 저쩌구
#https://glow153.tistory.com/13 참고 
print(soup.find('div', {'class', 'eLAPa'}))

driver.quit()

