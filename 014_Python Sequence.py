"""
시퀀스 자료형

순서가 있는 자료형! 

문자열과 리스트를 묶어서 시퀀스 자료형이라 부른다.

"""

a = "Once"          #문자열
b = [t,w,f,h,u,x,a] #리스트
c = (1,4,7,2,5,78)  #튜플


#시퀀스 특징

#1-1. 원소간의 순서가 존재한다. 인덱싱/슬라이싱이 가능하다.
#1-2.인덱싱/ 슬라이싱 할 때 음수를 넣거나, 자리를 비우는것도 가능하다.

a = "Once"
b = ['t', 'w', 'i', 'c', 'e']
print(a[1])
print(b[2:4])  

a = "Once"
b = ['t', 'w', 'i', 'c', 'e']
print(a[-1]) #e 뒤에서 1번째 원소
print(b[:3]) # ['t', 'w', 'i'] 처음 ~3번째 슬라이싱

#2.맴버 조회 in 연산자로 시퀸스안에 "원소"가 있는지 확인 가능

a = "Once"
b = ['t', 'w', 'i', 'c', 'e']
print('o' in a) #True
print('b' in b) #False


#3.길이 확인 len연산자로 시퀸스 안에 원소가 몇 개 인지 확인 가능.

a = "Once"
b = ['t', 'w', 'i', 'c', 'e']
print(len(a))   #4
print(len(b))   #5

#4.연결연산 + 연산자로 같은 시퀸스 두개를 이어 붙일 수 있다.

c = ['t', 'w', 'i'] + ['c', 'e']
print(c) #['t', 'w', 'i', 'c', 'e']

#5.반복연산 *연산자로 시퀸스를 반복 가능하다.

d = "shy" * 3
print(d) #shyshyshy





