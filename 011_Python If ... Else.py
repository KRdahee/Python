"""
[Python If ... Else 조건문]

Python 조건 및 If 문

Python은 수학의 일반적인 논리적 조건을 지원합니다.

같음: a == b
같지 않음: a != b
미만: a < b
작거나 같음: a <= b
보다 큼: a > b
이상: a >= b

"""


#파이썬의 조건문 -if문

#만약 i==1이면, i를 출력하라!
#     (조건)     (명령)



#가장 일반적으로 "if 문" 및 루프에서 사용될 수 있습니다. "if 문"은 if 키워드를 사용하여 작성됩니다.

a = 33
b = 200
if b > a:
    print("b is greater than a")


#If문   조건이 True일 때, 명령 실행!!

if string[0] == "a":
    count = count + 1
    print(string)


#If문에 들어갈 명령들은 같은 들여쓰기로 구분한다!!
    
if string[0]== "a":
    count = count + 1
    print(string)

#if문에서 조건을 만족하지 못한다면?

"""
만약 i ==1 하면 i를 출력하라!
아니면 i+1을 출력하라!
else(i !=1)

"""

#if-else문

#조건이 True면 If문 False면 else문 실행

x = input()
if x in ['a','e','i', 'o', 'u']:
    print("모음입니다.")
else:
    print("자음입니다.")


#연습문제

## input()을 이용해서 숫자(정수) 입력을 받고, 변수 num에 이를 넣어봅시다.

num = int(input())

# if-else문을 이용해서 만약 입력받은 수가 홀수면 "(입력받은 수) 홀수입니다."
# 짝수면 "(입력받은 수) 짝수입니다."를 출력해봅시다.
# 괄호는 출력하지 않습니다.

#if num을 2로 나눴을 때 나머지가 1일 경우를 컴퓨터 언어로 작성하면?
#if num % 2 == 1

if num % 2 == 1 :
    print(num, "홀수입니다.")
else:
    print(num, "짝수입니다.")



