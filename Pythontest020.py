"""

평균 구하기!

평균을 쉽게 구할 수 있도록 평균을 구하는 프로그램을 작성

평균은 (자료의 합) / (자료의 크기) 입니다.

"""

sky = []

while True :
    num = int(input())
    if not num == 0:
        sky.append(num)
    else:
        break
average = sum(sky)/len(sky)
print(average)