# -*- coding:utf-8 -*-

with open('test01.txt', 'r') as file: #변수의 close를 자동으로 해줄게 ~ 
    a = file.read()
    print(a)