"""
출력 결과가

19 * 1 = 19
19 * 2 = 38
...
19 * 18 = 342
19 * 19 = 361

이렇게 나와야한다!

#for-range()를 이용해서 19단을 전부 출력해봅시다!

"""
for i in range(1, 10):
    for number in range(1,20):
        print("%d * %d = %d" %(number, i, i*number), end=",")
    print("\n")

#연습문제
    

for i in range(1, 370):
    if i % 19 == 0:
        print(i)

#1차 시도 실패 
        
for i in range(1, 20):
    print("19 *", i, "=", i*19)

#2차 시도 답안..