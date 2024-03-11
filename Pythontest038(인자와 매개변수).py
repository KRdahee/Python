def solve(a,b):
    c = a* b
    return c

#    return a*b

var1 = solve(3,4)

var2 = solve(3, ["Cham"])

print(var1,var2)


"""
매개변수(parameter) : 함수를 정의할 때(만들 때) 넘겨받은 값을 관리하는 변수
인자(argument) : 함수를 호출할 때(사용할 때) 함수로 넘겨주는 자료

함수 이름이나 원소의 대소문자 구분에 주의하세요!

"""
def plusDouble(a, b): #이때 a, b는 매개변수!
    return 2*(a+b)

print(plusDouble(3, 4)) #이때 3, 4는 인자!
# 함수 호출시
# a = 3
# b = 4
# 로 간주