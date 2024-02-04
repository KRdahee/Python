"""
평균 나이 구하기 | p.40

평균은 주어진 수를 다 합쳐서 개수만큼 나눠서 얻을 수 있습니다.

이번 실습에서는 6명의 팀원의 나이가 주어졌을 때 평균을 구하는 실습을 하겠습니다.

이 실습을 통해 연산자 사용에 있어서 주의사항과 파이썬으로 실수(real number)를 표현하는 방법 등을 배울 수 있습니다.

(6+6)/2를 작성해보겠습니다.

print(6 + 6 / 2)
#출력값은 아래와 같습니다.
#9
#/가 +보다 우선순위가 높아 /부터 계산합니다.
print((6 + 6) / 2)
#출력값은 아래와 같습니다.
#6




1. 50 + 45 + 33 + 39 + 29 + 30 / 6을 출력하세요.

파이썬은 연산자 우선순위가 높은 나눗셈을 먼저 계산해 30/6인 5를 구한뒤 나머지 덧셈을 계산합니다. 이를 방지하기 위해서는 앞의 덧셈을 괄호로 묶어줘야 합니다.

2. 50 + 45 + 33 + 39 + 29 + 30을 괄호로 묶고 6으로 나누어 출력하세요.

3. 50 + 45 + 33 + 39 + 29 + 30을 괄호로 묶고 //연산자를 사용해 6으로 나눈 몫을 출력하세요.

4. round를 사용하여 평균 값을 소수점 첫째 자리까지 출력하세요.

실행결과

201.0
37.666666666666664
37
37.7

"""

#Round함수

#Round함수는 실수의 소수점을 원하는 자리까지만 저장 할 수 있다.

#round(숫자, 표시할 소수점 자릿수)

#1번을 해보세요!
print(50 + 45 + 33 + 39 + 29 + 30) / 6
#2번을 해보세요!
print(50 + 45 + 33 + 39 + 29 + 30) / 6
#3번을 해보세요!
print(50 + 45 + 33 + 39 + 29 + 30) // 6
#4번을 해보세요!
round((50 + 45 + 33 + 39 + 29 + 30)/ 6, 1)
