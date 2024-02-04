#문자열 포매팅으로 print() 함수 더 편하게 사용하기

#1번을 해보세요!
print("나는 사과 %d개를 먹었습니다.")
#2번을 해보세요!
print("나는 사과 %d개와 배 %d개를 먹었습니다.")
#3번을 해보세요!
for item in range(2,20):
    for each in range(2, 20):
        print('%d X %d = %d' %(item, each, item * each))
