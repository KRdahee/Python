# 모듈 불러오기 
#import(불러오다) 키워드를 이용해서 모듈 사용

import random
#random 모듈 불러오기


#모듈 사용법 확인하기

#모듈 속 사용하려는 함수/변수의 사용법 확인

#random.randrange(start, stop, [,step])
#    return a randomly selected element from range(start, stop, step)

random.randrange(start, stop)
#range(start, stop)중의 한 원소를 가지고 옵니다.

#.(dot)을 쓴 후에 모듈 속 함수/ 볌수 사용

import random
print(random.randrange(0,2))
#0이상 2미만 수 중 임의로 출력

#모듈 만들기 : 우리가 원하는 내용이 담긴 모듈 제작 가능. 
#.py(파이썬 파일)로 만들 수 있다.

import my_module

"""
1) py파일 생성 후, 함수와 변수를 만든다.

#cal.py

def plus(a,b):
    c= a + b
    return c

2) 다른 파일에서 만들어 둔 py파일을 불러온다.

#main.py
import cal
print(cal.plus(3,4))

#7
"""