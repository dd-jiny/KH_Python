# lambda 파라미터 : 리턴될 값
from pickle import NONE

hap01 = lambda a, b: a + b
print(hap01(10, 20))

gob = lambda a, b : a * b
print(gob(10, 20))

hap02 = lambda a, b, c: a + b + c
print(hap02(10, 20, 30))

a = [(1, 'one', 9), (2, 'two', 8), (3, 'three', 7), (4, 'four', 6)]
a.sort(key=lambda a:a[1]) # a를 1번지 기준으로 정렬 현재는 four, one, three, two 알파벳 순서
# a.sort(key=lambda a:a[2]) 2번지를 기준으로 했을때 6, 7, 8, 9 
print(a)


                      #x 조건이 참일때 거짓일 때 
#min01 = lambda x, y: x if x < y else y 
#print(min01(11, 22))
min01 = (lambda x, y: x if x < y else y)(11, 22) #만약 x가 y보다 작다면 x 크다면 y
print(min01)

max01 = (lambda x, y: x if x > y else y)(33, 44)
print(max01)


b = lambda x: (lambda newx: x + newx)
print(b(100)(90))
#b에 100이 들어가 x에 100이 들어감 다음에 newx에 90이 들어감

# c = lambda newx : 100 + newx
c = b(100) #->b에다가 100을 넣어 실행 newx가 없으니 <function <lambda>.<locals>.<lambda> at 0x00000160E06B9C10> 이거 뜬다
print(c)
# d = 100 + 90
d = c(90)
print(d)


#1 ~ 100 사이에서의 5의 배수 출력 
e = lambda x: bool(x % 5)
#print(e(9)) #지금 상황에서 결과값이 0이아니면 다 참이다 0만 false
five = [i for i in range(1, 100) if not e(i)]
print(five)

# None == Null 비슷해~
f = lambda x: x if (x % 5 != 0) else None
res = [i for i in range(1,100) if not f(i)]
print(res)

#위에거 한출로 합쳐보장~
result = [i for i in range(1, 100) if not (lambda x: x if (x % 5 != 0) else None)(i)]
print(result)
































