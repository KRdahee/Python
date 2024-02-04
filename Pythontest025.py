"""
for문으로 곱셈표 출력하기
"""

print(2*1)
print(2*2)
print(2*3)
print(2*4)
print(2*5)
print(2*6)
print(2*7)
print(2*8)
print(2*9)
print(2*10)

#for문과 리스트로 2단 출력하기

#for 변수 in 리스트(또는 튜플이나 문자열):
#    수행할 문장

number = [1,2,3,4,5,6,7,8,9]
for item in number:         #number의 각 원소를 하나씩 item에 입력한다.
    print(2 * item)         #2*item의결괏값을 출력한다.