# 0 1 1 2 3 5 8 13 21 34 55 ....

n = input('level : ')
a, b = 0, 1
i = 0
while i < int(n):
    print(a, end=' ')
    a, b = b, a+b
    #a = b
    #b = a+b 가 안되는 이유 위에서 a의 값이 바뀌었기 때문 
    i += 1 






