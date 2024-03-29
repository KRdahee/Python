"""
BMI(체질량지수) 계산하기
BMI(체질량지수)는 우리 몸의 신장과 몸무게를 통해 계산되는 수치로, 비만도를 판단하는데 사용됩니다.

BMI 수치를 계산하는 방법은 다음과 같습니다.
BMI = 체중(kg) / (신장(m)의 제곱)

마지막으로 BMI의 수치에 따라 4가지 등급으로 나누어집니다.

주어진 조건에 맞는 비밀번호를 만들어주는 함수 BMI()를 만들어봅시다.

인자 : 딕셔너리 body_data
“신장” : 신장 수치(단위 cm)
“체중” : 체중 수치(단위 kg)
매개변수 : 딕셔너리 body_info
반환값 : BMI 수치

"""
#예시
body_data = {
    "신장" : 175,
    "몸무게" : 74
}

BMI(body_data)

#힌트
#BMI를 계산할 때, 사용하는 신장의 단위는 m(미터) 입니다. 
#인자에는 cm(센티미터)단위로 들어가므로 단위 변환을 꼭 생각해봅시다.

#1m = 100cm
#1cm = 0.01m

#BMI를 계산할 때, 신장의 제곱을 해야합니다. 제곱은 math 모듈의 pow()를 사용하면 됩니다.

import math

test1 = math.pow(2, 4)
print (test1)  #2의 4승 >>  16

test2 = math.pow(5, 3)
print(test2)  # 5의 3승 >> 125

#파이썬에서는 반올림하는 함수 round()가 있습니다. 숫자와 표시할 소수점자리를 입력하면 반올림하여 계산해줍니다.
BMI = 24.1631456789

# BMI의 소수점 2번째 자리까지 확인하겠다, 
BMI = round(BMI, 2)
# 24.16

#정답------------------------------------------------
# BMI를 계산하는 함수 BMI()를 만들어봅시다.
# BMI를 계산할 때, 사용하는 신장의 단위는 m(미터) 입니다
def BMI(body_info) :
    import math

    # 신장(cm)을 m로 변환
    height = body_info["신장"] / 100
    
    # BMI 계산
    bmi = body_info["몸무게"] / math.pow(height, 2)
    
    # 소수점 2번째 자리까지 반올림
    bmi = round(bmi, 2)
    
    return bmi

# 저장된 데이터의 신장의 단위는 cm, 몸무게의 단위는 kg입니다.
body_data = {
    "신장" : 175,
    "몸무게" : 74
}

print("BMI : ", BMI(body_data))