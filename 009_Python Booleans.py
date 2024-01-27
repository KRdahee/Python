""" 

[논리 자료형 Booleans]

참(True)혹은 거짓(False)을 나타내는 자료형을 논리 자료형이라고 합니다. 

비교 연산자

숫자나 문자의 값을 비교하는 연산자.

주어진 진술이 참이면 True 거짓이면 False를 반환한다.

+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y

"""

"""
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3
"""

print(3 < 5)    #True
print(7 == 5)   #False  
print(2 >= 10)  #False
print(5 != 10)  #True
print(2 == 2)   #True

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


#값과 변수 평가

#이 bool()함수를 사용하면 모든 값을 평가하고 True와 False를 반환받는다.

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

"""
True를 반환할 때

1.거의 모든 값은 일종의 콘텐츠가 있는지 평가됩니다.

2. 빈 문자열을 제외한 모든 문자열은 True입니다

3. 0을 제외한 모든 숫자는 True 입니다

4. 빈 목록을 제외한 모든 목록, 튜플, 집합 및 사전은 True 입니다

"""

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


#False를 반환할 때 (empty values, such as (), [], {}, "", the number 0, and the value None)

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#a class with a __len__ function that returns 0 or False

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

#Functions can Return a Boolean 함수는 Boolean을 반환 가능하다.

def myFunction() :
    return True

print(myFunction())

def myFunction() :
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

# Python에는 또한 객체가 특정 데이터 유형인지 확인하는 데 사용할 수 있는 isinstance()함수 와 같이 부울 값을 반환하는 많은 내장 함수가 있습니다

#객체가 정수인지 아닌지 확인하세요.

x = 200
print(isinstance(x, int))

# Q1. == 혹은 != 연산자을 이용해서 True인 명제를 ans1에 넣어봅시다.
ans1 = (15 == 15)

# Q2. > 혹은 < 연산자를 이용해서 False인 명제를 ans2에 넣어봅시다.

ans2 = (2 >= 10)

# Q3. >= 혹은 <= 연산자를 이용해서 True인 명제를 ans3에 넣어봅시다.
ans3 = (3 < 5)

# 위의 세 변수를 출력해서 True, False 여부를 확인해봅시다.
print(ans1, ans2, ans3)



