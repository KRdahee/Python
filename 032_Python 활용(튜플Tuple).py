"""

여러 자료를 담는 자료형이 필요하다면?

대부분 리스트를 이용 그러나 값이 바뀔 위험이 있다!

"""

my_list = ['l','i','s','t']

my_list[1] = 'a'

print(my_list) 

# ['l','a', 's', 't']

#Tuple의 필요성 : 값을 바꿀 수 없으면서도 여러 자료를 담을 수 있다.
# 소괄호로 묶어서 표현한다()

tuple_zero = ()

tuple_one = (1,)

tuple_ = (1,2,3,4,5)

tuple_ = 1,2,3,4,5



#Tuple의 특징 1 : 시퀸스 자료형으로 index를 이용한 인덱싱, 슬라이싱이 가능하다.

my_tuple = ('t','w','i','c','e')

print(my_tuple[1]) #'w'

print(my_tuple[2:4]) #('i', 'c')



#Tuple의 특징 2 : in 연산자로 Tuple안에 원소 확인 / len() 함수로 Tuple 길이를 확인한다.

my_tuple = ('t','w','i','c','e')

print('t' in my_tuple) #True

print(len(my_tuple)) #5



#Tuple의 특징 3 : +연산자로 Tuple과 Tuple을 연결 *연산자로 Tuple을 반복

my_tuple = ('i', 'c', 'e')

print(('e','i')+ my_tuple) # ('e','l','i','c','e')

print(my_tuple * 2) # ('i', 'c', 'e','i', 'c', 'e')



#Tuple의 특징 4 : 자료추가, 삭제, 변경이 불가능하다. 한번 만들어지면 고정!!

my_tuple = ('t','w','i','c','e')

print(my_tuple.append('!')) #error
print(my_tuple.remove('w')) #error

my_tuple[1] = 's' #error
