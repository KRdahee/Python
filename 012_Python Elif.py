#elif 키워드 는 "이전 조건이 true가 아니면 이 조건을 시도하십시오"라고 말하는 Python의 방식입니다.

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

#if문에서 조건을 만족하지 못했을 때...
#만약 점수가 90이상이라면 A를 출력해라, 아닌 경우에 75이상이라면 B를 출력해라.
#75 < ___ < 90
#else if -> elif

#if-elif문
# 조건 1이 True면 If문, 조건 1이 False이면서 조건 2가 True면 elif문 실행

x = int(input())
if x % 2 == 0:
    print("2의 배수입니다.")
elif x % 3 == 0:
    print("3의 배수입니다")

#정리 : if-elif-else문

"""
if 조건 1:                      
    do A
elif 조건 2:
    do B
elif 조건 3:
    do C
...

else:
    do X

"""

#연습문제

# 변수 answer에 수 1~50 중 하나를 넣어봅시다.
answer = 22
# input을 통해 숫자형으로 입력을 받아서 변수 submit에 저장해봅시다.

submit = int(input())

# if-elif-else문으로 Up-Down Game을 구현해봅시다.
# 만약 answer보다 submit이 더 크면 "정답보다 더 큰 수를 입력했습니다."
# 만약 answer보다 submit이 더 작으면 "정답보다 더 작은 수를 입력했습니다."
# 만약 answer와 submit이 같으면 "정답!" 를 출력합니다.

if answer < submit :
    print("정답보다 더 큰 수를 입력했습니다.")
elif answer > submit :
    print("정답보다 더 작은 수를 입력했습니다.")
else:
    print("정답!")














