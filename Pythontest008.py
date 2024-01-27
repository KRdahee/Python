"""

리스트 내부의 원소 삭제하기
리스트에 원소를 삭제하는 방법은 다음과 같습니다.

원소 삽입 : 리스트이름.remove(삭제할 자료)
my_list = ['a', 'b', 'c', 'f']
my_list.remove('f')
print(my_list) #['a', 'b', 'c']

my_list.remove('d') #오류!
Copy
단, 리스트 안에 존재하지 않는 원소를 지우려고 하면 오류가 발생해요!

"""

my_list = [5, 2, 4, 3, 2, 1]

my_list.remove(2)


#or

my_list = []

my_list.append(5)
my_list.append(4)
my_list.append(3)
my_list.append(2)
my_list.append(1)

my_list.remove(3)

print(my_list)