"""

원소의 개수 세기 / 꺼내기
리스트에 원소의 개수를 세고, 인덱스로 원소를 꺼내는 방법은 다음과 같습니다.

원소의 개수세기 : 시퀀스이름.count(자료)
인덱스로 원소 꺼내기 : 리스트이름.pop(인덱스)
단, 존재하지 않는 인덱스를 pop할 경우 Python은 오류를 발생시킵니다.

"""

# 숫자 1, 2, 2, 3, 3, 3이 담긴 리스트 my_list를 하나 선언해봅시다.

my_list = [1, 2, 2, 3, 3, 3]

# my_list 안의 숫자 3의 개수를 변수 var1에 넣어봅시다.

var1 = my_list.count(3)

# 일부 원소를 제거하여 my_list가 [1, 2, 3]이 되도록 해봅시다.

my_list.pop(1) # -> [1,2,3,3,3]
my_list.pop(2)
my_list.pop(3)

print(my_list)
