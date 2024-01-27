"""
[Logical Operators 논리 자료형의 연산]

True, False밖에 없는 논리 자료형에서 새로운 연산이 필요할 때 사용한다.

Python Logical Operators

and Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

"""
#And(모두 True?) 각 논리가 모두 True여야 True이다.

print(3==3 and 4<=5 and 6>2)

#세 항이 모두 True이므로, True!


#OR(True가 있나?) 논리들 중 True가 존재 한다면 True!

print(3==3 or 4<=5 or 6<2)

#4<=5가 True이므로, True가 존재하기에 True!


#NOT(기존 논리와 반대로!) 논리값을 뒤집는다!

print(not 3==4) 

#False에 not을 붙였으므로 True!

#연습문제

# 괄호 안에 적절한 명제를 채워 stat1이 True가 되게 해봅시다.
stat1 = 3==3 and 2<4 and 6==6

# 괄호 안에 적절한 명제를 채워 stat2이 False가 되게 해봅시다.
stat2 = 4>=6 or "apple"=="Apple" or 6>198 

# 괄호 안에 적절한 명제를 채워 stat3이 True가 되게 해봅시다.
stat3 = not (3==4)

# 위의 세 변수를 한 문장으로 출력해서 True, False 여부를 확인해봅시다.

print(stat1, stat2, stat3)









