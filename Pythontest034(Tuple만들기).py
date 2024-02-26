"""
리스트처럼 여러 자료형을 담을 수 있지만 변할 수 없는 자료형을 우리는 Tuple(튜플)이라고 부릅니다.

튜플을 다음과 같은 방법으로 만들 수 있습니다.

"""
tuple_zero = ()
tuple_one = ('a',)
tuple_many = ('a', 'b', 'c', 'd', 'e')
tuple_no_gwalho = 'a', 'b', 'c', 'd', 'e'


"""

숫자 1, 2, 3, 4, 5이 담긴 튜플 my_tuple을 하나 선언해봅시다.

my_tuple의 세번째의 원소를 변수 var1에 넣어봅시다.

my_tuple의 두번째부터 네번째까지의 원소를 슬라이싱하여 변수 var2에 넣어봅시다.

my_tuple의 길이를 변수 var3에 넣어봅시다.

"""

my_tuple =(1,2,3,4,5)

var1 = my_tuple[2]

var2 = my_tuple[1:4]

var3 = len(my_tuple)

print(var1, var2, var3)

