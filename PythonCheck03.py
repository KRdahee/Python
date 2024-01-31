# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
odd_list = []
even_list = []

# 지시사항을 참고하여 코드를 작성하세요.
user = input()
nums_list = set([int(x) for x in '_'.join(user).split('_')])

odd_list = [x for x in nums_list if x%2!=0]
even_list = [x for x in nums_list if x%2 == 0]

odd_list.sort()
even_list.sort(reverse = True)

while True:
    if len(odd_list) != len(even_list):
        if len(odd_list)> len(even_list):
            del(odd_list[-1])
        elif len(odd_list) <len(even_list):
            del(even_list[-1])
    else: break

result = []
for i in range(len(odd_list)):
    result.append(odd_list[i])
    result.append(even_list[i])
    

# 아래 코드는 채점을 위한 코드입니다. 수정하지 마세요!
print(odd_list)
print(even_list)