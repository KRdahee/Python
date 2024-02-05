"""
def 문으로 함수 만들기

함수를 정의하는 기본 명령어는 def문입니다.

def문은 함수를 정의하는 명령어입니다.

def 함수 이름(매개변수):
    수행할 문장1
    수행할 문장2
    ...

(15, 9, 36, 4.0)
<class 'tuple'>

"""
def add(a, b):
    return a + b

print(add(233, 43))

def calculator(a, b):
    return a + b, a - b, a * b, a / b

print(calculator(12, 3))

print(type(calculator(12, 3)))
