# 리스트 nums를 넣었을 때, 최댓값을 반환(return)하는 함수 our_max를 작성해봅시다.
def our_max(nums_list):
    maxNum = -9999

    for num in nums_list : 
        if maxNum < num:
            maxNum = num

    return maxNum

# 
print(our_max([1, 2, 10, 9, 3, 7, 0, 99, 27, 85]))


"""
max()를 사용하지 않고, 어떤 리스트를 인자로 넘겨주면 그 리스트의 최댓값을 반환(return) 하는 함수 our_max()를 만들어봅시다.

our_max()함수를 만들기 위해서는 이전에 배웠던 정렬을 활용

"""