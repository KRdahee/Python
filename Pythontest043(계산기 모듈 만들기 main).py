"""
cal.py 모듈은 계산기 기능이 담긴 모듈입니다. 
이 안에는 plus() 와 minus() 함수가 있고, 모델명이 담긴 변수 modelName이 있습니다. 
오른쪽 실습에서 직접 이 cal.py를 만들어보고, main.py에서 이를 불러보기.


cal.py 파일을 열고, a,b를 인자로 갖는 함수 plus, minus를 정의해봅니다.
plus : a+b를 반환하는 함수
minus : a-b를 반환하는 함수
cal.py 파일에서 변수 modelName을 만들고 ‘ELI-C2’를 대입해봅시다.

main.py 파일을 열고, import cal을 이용해 저장된 모듈 cal을 불러와봅시다.

변수 var1에 모듈 cal의 모델이름(modelName)을 넣어봅시다.

변수 var2에 모듈 cal의 plus 함수를 이용해서 3+4의 값을 넣어봅시다.

변수 var3에 모듈 cal의 minus 함수를 이용해서 7-2의 값을 넣어봅시다.

var1, var2, var3의 값을 출력하여 확인해봅시다.


"""
import cal

var1 = cal.modelName

var2 = cal.plus(3, 4)

var3 = cal.minus(7, 2)


## 변수의 값을 확인하는 출력문입니다.
print(var1, var2, var3)