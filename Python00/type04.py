# tuple : ()
# 수정 불가능한 list

# 생성자
a = tuple()
print(a)

#튜플은 어펜드라는 속성 자체가 없다.
#a.append(1)
#print(a)

b = tuple([1, 2, '3'])
print(b)

# () 사용
# 튜플은 추가와 수정 불가 
c = (1, 2, 3, 4, 5)
print(c)
#c[1] = 'two'
#print(c)

d = tuple(range(3, 6))
print(d)
print(c + d)

# tuple 을 list로 바꾸기
e = list(d)
print(e)
e.append(6)
print(e)

#list를 tuple로 바꾸기
f = tuple(e)
print(f)
# f.append(6)
# print(f)

# unpacking
g, h, i, j = f
print(g)
print(h)
print(i)
print(j)
























