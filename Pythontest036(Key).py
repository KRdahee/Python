# 변수 my_dict1을 만들고 빈 딕셔너리(Dictionary)를 만들어봅시다.
my_dict = {}

# my_dict1에 대응관계를 넣어봅시다 (1 → "Integer",  'a'  → "String")
my_dict1 = {1 : "Integer", 'a':"String"}
print(my_dict1)

# 키 후보(key_candidate)인 변수 두 개가 있습니다.
key_candidate1 = [1, 2, 3]
key_candidate2 = (1, 2, 3)

# 위의 키 변수 두 개 중에 옳은 것 하나를 None 자리에 넣어봅시다. (None은 지워주세요)
my_dict2 = {key_candidate2 : "I am Value!"}

print(my_dict2)