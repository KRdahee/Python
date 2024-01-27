"""

remove를 잘 쓰려면 우선 있는지부터 확인!
리스트에서 .remove()는 원소를 삭제하는 데에 쓰이지만, 만약 그 원소가 리스트 내부에 없을 경우, 오류가 발생합니다.

따라서 우리는 지우려는 원소가 리스트에 있는지 확인한 다음, 원소를 지우거나 다른 조치를 취해야 합니다.

아래의 절차를 따라서 리스트 안의 원소의 값을 오류 없이 제거해봅시다.


이렇게 해봐요!
다음 과정을 통해 "Durian"과 "Pineapple"을 지워봅시다.

원소가 있다면 : 해당 원소를 리스트에서 지웁니다.
원소가 없다면 : 해당 원소가 리스트 안에 없다는 문장을 출력합니다. (“원소은(는) 리스트 안에 없습니다!”)

"""

# 과일들이 담긴 리스트 fruits입니다.
fruits = ['Apple', 'Banana', 'Chamwae', 'Durian']

# 지시사항에 맞추어 "Durian"을 fruits에서 지워봅시다.

fruits.remove("Durian")

# 지시사항에 맞추어 "Pineapple"을 fruits에서 지워봅시다.

if "Pineapple" in fruits:
    print(fruits)
else:
    print("Pineapple은 리스트 안에 없습니다!")


#Pineapple은 리스트 안에 없습니다!