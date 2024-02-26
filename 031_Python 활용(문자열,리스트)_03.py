list.pop(i)

#인덱스 I의 원소를 제거 후 그 원소를 반환 (괄호를 비울 시 마지막 원소)

my_list = [1, 2, 3, 4, 5]
print(my_list.pop(0)) #1
print(my_list.pop())  #5



seq.count(d)

#시퀀스 내부의 자료 d의 개수를 반환한다.

my_seq = [2, 2, 2, 4, 4]

print(my_seq.count(2)) #3 왜냐하면 2가 3개가 있기때문



str.split(c)

#c를 기준으로 문자열을 쪼개서 리스트를 반환(괄호를 비울 시 공백)

my_str = "1 2 3 4 5"

print(my_str.split()) #['1','2','3','4','5'] 이건 공백을 기준으로

element = "Na, Mg, Al, Si"

print(element.split(',')) #['Na','Mg','Al','Si'] 이건 콤마를 기준으로



str.join(list)

#str을 기준으로 리스트를 합쳐서 문자열을 반환(괄호를 비울시 공백)

my_list = ['a','p','p','l','e']
print(''.join(my_list)) #apple

friend = ['Pat', 'Mat']
print('&'.join(friend)) #Pat&Mat