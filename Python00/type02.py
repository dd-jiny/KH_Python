#문자
# single quotation 과 double quotation은 차이 없음

# single quotation * 1
a = 'python\'s hello, world!'
print(a)

# single quotation * 3
b = '''python's
hello, world!
                hello, python!!
'''
print(b)

# double quotation * 1
c = "Hello, \"World!\""
print(c)


# double quotation * 3
d = """
abc
def
"ghi"
"""
print(d)

#혼합
e = 'abc"def"ghi\npython\'s string'
print(e)
f = "abc'def'ghi\ttest"
print(f)
# r : raw string (\(역슬래쉬)를 문자로 인식)
g=r"C:\Workspace_Python\Python00"
h = "C:\test"
print(g)
print(h)

#문자열 더하기, 곱하기
str01 = 'hello,'
str02 = 'python!'
print(str01 + str02)
print(str01 * 3 + str02)





















