"""

[Operators 연산자]

자료형의 연산

+, -, *, /

더하기, 뺴기, 곱하기, 나누기

Python Arithmetic Operators

+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y

Python Assignment Operators

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

Python Comparison Operators

==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y

P
ython Logical Operators

and 	Returns True if both statements are true	x < 5 and  x < 10	
or	    Returns True if one of the statements is true	x < 5 or x < 4	
not	    Reverse the result, returns False if the result is true	not(x < 5 and x < 10)


Python Identity Operators

is 	    Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y

Python Membership Operators

in 	    Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y


Python Bitwise Operators

& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
"""


#The precedence order is described in the table below, starting with the highest precedence at the top:


"""

()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR

"""

#숫자형 자료의 사칙연산!!!

print(3+5) #8

print(3-5) #-2

print(3*5) #15

print(3/5) #0.6


#연습문제

#'num1'이라는 변수를 하나 선언하고, 숫자 23571를 넣어줍시다.
num1 = 23571

#'num2'이라는 변수를 하나 선언하고, 'num1'에 1024를 곱한 값을 넣어줍시다.
num2 = num1*1024

#'num3'이라는 변수를 하나 선언하고, 'num2'에 243을 나눈 값을 넣어줍시다.
num3 = num2/243

#'num4'이라는 변수를 하나 선언하고, 'num3'에 4927819을 더한 값을 넣어줍시다.
num4 = num3+4927819

#'answer'이라는 변수를 하나 선언하고, num4'에 829176을 뺀 값을 넣어줍시다.
answer = num4-829176

#엘리스 토끼에게 외쳐봅시다. '네가 생각한 답은 answer원이야!'
print("네가 생각한 답은", answer, "원이야!")


#숫자형 자료의 특수연산

"""

// 몫 연산자

% 나머지 연산자

** 제곱 연산자

"""

print(13//15) #2    13%5=2...3

print(13%5)   #3    

print(2**4)   #16 거듭제곱


#연습문제

# //을 이용해서 변수 intdiv에 4를 넣는 수식을 작성해봅시다.
intdiv = 16//4

# %을 이용해서 변수 modular에 1을 넣는 수식을 작성해봅시다.
modular = 5%2

# **을 이용해서 변수 expo에 16을 넣는 수식을 작성해봅시다.
expo =  16

#위의 세 변수를 출력해서 확인해봅시다.
print(intdiv, modular, expo)


#문자형 자료의 연산!!!

"""

+ 이어 붙이기 with 문자열

* 반복하기 with 숫자

"""

print("안녕"+"하세요") #안녕하새요
print("안녕"*3)       #안녕안녕안녕


#연습문제

# 변수 connect_str를 선언하고, +(연결 연산자)를 이용해서 '덩덕쿵덕'를 넣어봅시다.
connect_str = "덩덕쿵덕"

# 변수 iterate_str를 선언하고 *(반복 연산자)를 이용해서 '쿵덕쿵덕'을 넣어봅시다.
iterate_str = "쿵덕쿵덕"

# 위 두 변수를 이용해서 '덩덕쿵덕쿵덕쿵덕덩덕쿵덕쿵덕쿵덕'을 변수 jajinmori에 넣어봅시다
jajinmori = (connect_str + iterate_str)*2

print(connect_str, iterate_str, jajinmori)