"""

리스트를 쪼개고, 붙이기!
리스트를 문자열로 바꾸고, 문자열을 리스트로 바꾸는 방법은 다음과 같습니다.

문자열 → 리스트 : 쪼갤 문자열.split(기준 문자열)
리스트 → 문자열 : 연결할 문자열.join(리스트)
이 때,

연결할 문자열 : 리스트의 원소와 원소 사이에 들어가는 문자열
쪼갤 문자열 : 쪼개서 리스트로 만들 문자열
기준 문자열 : 쪼갤 때 기준이 되는 문자열(쪼개진 후에는 기준 문자열은 삭제됨)

"""

#  문자열 "beetea"가 담긴 변수 my_str를 선언해봅시다.
my_str = "beetea"

#  문자열 'e'를 기준으로 my_str를 리스트로 만든 다음, 이를 변수 var1에 담아봅시다.

var1 = my_str.split("e")

# 리스트 ["Seeing", "is", "Believing"]이 담긴 변수 my_list를 선언해봅시다.

my_list = ["Seeing", "is", "Believing"]

# 공백(` `) 1개을 기준으로 my_list를 문자열로 만들어보고, 이를 변수 var2에 담아봅시다.

var2 = " ".join(my_list)

print(var1, var2)

