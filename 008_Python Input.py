"""

[입력 Input()]

Print를 이용해 컴퓨터로부터 정보를 전달 받았다면, 이제는 정보를 컴퓨터에게 전달해주자!

Input --> Print

이때, 컴퓨터는 사용자가 전달한 값을 어딘가에 보관해야 한다. --> 변수를 사용한다!.

"""

input()

변수 = input() # 대입의 의미를 가졌다.

var + input()  # 터미널에 값을 "입력" 해줍니다.

#연습문제

# input()을 이용해서 입력을 넣고, 이를 변수 var에 담아봅시다.
# input의 괄호 안에 내용을 넣으면 채점이 정상적으로 동작하지 않습니다. 
# ex. input("입력하세요") → 채점 동작 안 됨
var = input()

# 앵무새가 말을 따라합니다!
print("앵무새 :", var)

# 입력한 값이 어떤 자료형인지 확인해봅시다.
print(type(var))

"""

input()의 중요한 특징

무엇을 입력하든 "문자열"로 입력을 받는다.

만약 숫자를 입력해야 한다면 어떻게 해야할까?

입력받은 후 가공해줘야한다.

가공 방법은? 

자료형 사이의 변환 --> 형 변환을 해줘야 한다.

"""

#형 변환 바꿀_자료형(바뀔 자료형)

int     #숫자(정수)
float   #숫자(실수)
str     #문자열
list    #리스트

a = '345'
b = int('345')
print(a,b)
print(type(a)) #<class 'str'> | 문자열
print(type(b)) #<class 'int'> | 숫자

#연습문제

#변수 money에 input을 이용해서 입력을 받아봅시다.
money = input()
# money를 int형으로 변환해서, 다시 money에 넣어줍시다.

money = int(money)

# money를 2배 불려서 print로 출력해봅시다.
money = money*2

print(money)

