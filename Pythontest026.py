#range() 함수로 숫자열 쉽게 가져오기

number = [i for i in range(1,10)]
print(number)
#결과값은 [1, 2, 3, 4, 5, 6, 7, 8, 9] 입니다.

#range(시작할 정수, 끝나는 정수 + 1)

#1번을 해보세요!
for i in range(10):
    print(i) 
    
#2번을 해보세요!

for item in range(2,20):
    print(item)



#for 문을 두 번 사용해 19단 곱셈표 출력하기

for item in range(2, 20):
    for each in range(2, 20):
        print(item * each)
        


#19단 곱셈표 완성하기

for item in range(2,20):
    for each in range(2,20):
        print(item, ' x ', each, ' = ', item * each)