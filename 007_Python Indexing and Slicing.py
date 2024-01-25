"""

[Indexing and Slicing 인덱싱&슬라이싱]

문자열/리스트 접근하는 방법

"rescue","secure"는 다른 문자열이다.

[1,2,3],[3,2,1]은 다른 리스트이다.

WHY? = 원소의 배치 순서가 다르기 때문이다!

"""

#Index 
#문자열과 리스트 자료형은 여러 원소로 이루어져 있고 각각 위치를 0부터 순서대로 매긴다.'

#Indexing
#index를 통해서 리스트나 문자열의 특정 위치의 원소를 가져오는 방법 string/list[index]

#alpha에서 인덱스 1인 원소 'e'를 출력

alpha =  'ready'
print(alpha[1]) #e

#Slicing
#index를 이용해서 리스트나 문자열의 일부분을 잘라서 가져오는 방법 string/list[a시작인덱스:b종료인덱스]

#beta에서 2번째 원소 이상, 5번째 원소 미만을 가져온다.

beta = [2, 4, 6, 8, 10, 12, 14]
print(beta[2:5])    #[6, 8, 10]

#연습문제

# 3월 서울의 날씨는 다음과 같습니다.
seoul = ['8_맑음', '9_맑음', '10_흐리고 비', '11_맑음', '12_맑음', '13_맑음', '14_맑음', '15_맑음']

# 10일의 날씨 정보만 추출하여 아래 변수에 넣어봅시다!
seoul_rain = (seoul[2])

# 제주 날씨는 다음과 같습니다. 
jeju = ['8_맑음', '9_맑음', '10_맑음', '11_맑음', '12_흐리고 비', '13_흐리고 비', '14_흐리고 비', '15_맑음', '16_맑음', '17_맑음']

# 12일부터 14일까지의 날씨 정보들을 추출하여 아래 변수에 넣어봅시다!
jeju_rain = (jeju[4:7])

# 여러분이 추출한 날씨 정보를 print()를 이용해서 한번 확인해보세요!
print('서울에서 비가 오는 날씨는 ', seoul_rain)
print('제주에서 비가 오는 날씨는 ', jeju_rain)

"""

Point I
인덱스 : 문자열과 리스트의 특정 원소의 위치, 0부터 시작!

"Hello"에서 H = Index 0, e = index 1, ...
Point II
인덱싱 : 문자열과 리스트의 특정 위치(인덱스)의 원소를 가져오는 것

greet = "Hello!"  
print(greet[1])  

## 출력결과 ##
e
Point III
슬라이싱 : 문자열과 리스트의 특정 부분을 가져오는 것

greet = "Hello!"  
print(greet[0:5])  
Hello


Indexing and Slicing

>>> a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
>>> a
['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']

>>> a[0]
'spam'
>>> a[2]
'bacon'
>>> a[5]
'lobster'
>>> a[len(a)-1]
'lobster'
>>> a[6]

>>> a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
>>> a[2:5]
['bacon', 'tomato', 'ham']
>>> a[-5:-2]
['egg', 'bacon', 'tomato']
>>> a[1:4]
['egg', 'bacon', 'tomato']
>>> a[-5:-2] == a[1:4]
True

>>> a
['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
>>> a[:4]
['spam', 'egg', 'bacon', 'tomato']
>>> a[0:4]
['spam', 'egg', 'bacon', 'tomato']
>>> a[2:]
['bacon', 'tomato', 'ham', 'lobster']
>>> a[2:len(a)]
['bacon', 'tomato', 'ham', 'lobster']

>>> a
['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
>>> a[:]
['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
>>> a == a[:]
True
>>> a is a[:]
False

>>> s = 'mybacon'
>>> s[:]
'mybacon'
>>> s == s[:]
True
>>> s is s[:]
True

>>> a
['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
>>> a[0:6:2]
['spam', 'bacon', 'ham']
>>> a[1:6:2]
['egg', 'tomato', 'lobster']
>>> a[6:0:-2]
['lobster', 'tomato', 'egg']
>>> a
['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
>>> a[::-1]
['lobster', 'ham', 'tomato', 'bacon', 'egg', 'spam']
"""
