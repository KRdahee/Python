"""
리스트 원소 삽입
리스트에 원소를 삽입하는 방법은 다음과 같습니다.

원소 삽입 : 리스트이름.insert(인덱스, 자료)
my_list = ['a', 'c']
my_list.insert(1, 'b')

print(my_list) #['a', 'b', 'c']

"""

my_list = []

my_list.append(5)
my_list.append(4)
my_list.append(2)
my_list.append(1)

my_list.insert(2,3)

print(my_list)