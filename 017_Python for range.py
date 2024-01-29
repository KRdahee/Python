"""
Range 연속되는 숫자를 만들어주는 시퀸스 자료형이다.

"""

range(a, b) #a, a+1, a+2 ... -b까지만
range(0, 9) #0, 1, 2 ... 8까지만
range(5)    #range(0,5) == 0, 1, 2, 3, 4

#range(a) a번 반복한다라는 의미를 가졌다.

#for range_1 = 구간으로 반복하는 방법. a이상 b미만의 수를 변수에 넣어가면서 명령을 수행한다.

a = [1]
for i in range(2, 4):
    a.append(i)
print(a) #[1, 2, 3]

#for range_2 횟수로 반복하는 방법. a번 만큼 명령을 수행한다.

count =  0 
for i in range(10):
    count = count + 1
print(count) #10

#연습문제

for i in range(1, 11):
    print(i)

#range(a, b) : a 이상 b 미만의 연속된 정수가 담긴 시퀀스를 만들어주는 함수이기 떄문에 100까지만 출력된다.

for i in range(5):
    print("I Love Python!")

#range(a) : a번 반복
