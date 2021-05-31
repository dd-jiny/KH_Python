import re
#re라는 모듈을 사용하겠다.

'''
Regular Expression
.  : 문자 1개
^  : 문자열의 시작
$  : 문자열의 마지막
[] : 문자 집합
|  : or
() : 괄호 안의 정규식 그룹

* : 0 or more
+ : 1 or more
? : 0or 1
{n} : n번 반복
{n, m} : n번 부터 m번
{ㅜ, } ; n번 부터 무한대
'''


"""
r 문자열 표기법(re 모듈 확장 문법)
\w : [a-zA-Z0-9_] -> a~Z, 0~9, _포함하는 모든 문자
\W : [^a-zA-Z0-9_} -> 위의 문자 제외한 나머지 문자
\d : [0-9] -> 숫자를 제외한 나머지 문자
\s : [\t\n\r\f\v] -> 공백을 제외한 모든 문자
\b : 단어의 시작과 끝의 빈 공백
\B : 단어의 시작과 끝이 아닌 빈 공백
\\ : \
\[숫자] : wlwjdehls tntwkakszma dlfclgksms answkduf
\A : 문자열의 시작
\Z : 문자열의 끝
"""

str01 = '나의 이메일은 kh.123@kh.com123 입니다.'
match = re.search(r'[\w]*@[a-zA-Z.]*', str01)
print(match.group())


















































