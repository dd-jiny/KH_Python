# set (집합)

#생성자
#순서x 실행할때마다 순서 바뀜 
a = set(['1', '2', '3', '4', '4'])
print(a)

# 생성자에 iterable한 객체를 넣으면 set의 값으로 변환
#iterable
b = set('hello')
print(b)

#{} 사용
c = {'a', 'b', 'c', 'hello', '1', '2', '3'}
print(c)

#값추가
c.add('world')
print(c)

# 합집합, 교집합
print(a.union(b))
print(a | b)

print(a.intersection(c))
print(a & c)

