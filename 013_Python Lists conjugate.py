"""
1. 리스트에서 원소를 삽입, 제거, 정렬 할 수 있다.
2. 순서가 있는 자료형을 활용 할 수 있다.
3. 조건에 따라 반복하는 방법을 이해한다.
4. 원소, 횟수로 반복하는 방법을 이해한다.

"""
list.append(d)

#자료 d를 리스트 마지막 원소 뒤에 추가, 오직 한 개의 자료만 넣을 수 있다.

a = []
b = ['a','b','c']
a.append(10)
b.append('d')
print(a,b)

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

['apple', 'banana', 'cherry', 'orange']






list.insert(i,d)

#인덱스 i에 자료 d를 추가. 오직 한 개의 자료만 넣을 수 있다.

c = [1, 2, 4, 5]
c.insert(2,3)   #2는 위치 3은 값

print(c) #[1,2,3,4,5]

fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

['apple', 'orange', 'banana', 'cherry']






list.remove(d)

#처음 나오는 자료 d를 제거

d = [3, 1, 2, 3]
d.remove(3)

print(d) #[1,2,3]

fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")

['apple', 'cherry']






list.sort()

#리스트를 정렬. 숫자형은 오름차순, 문자열은 사전순

e = [6, 2, 4, 1]
f = ['carrot', 'apple', 'banana']

e.sort()
f.sort()
print(e,f)

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

['BMW', 'Ford', 'Volvo']






