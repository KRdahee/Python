#패키지 : 모듈을 폴더(Directory)로 구분하여 관리하는 것

# WHY 필요함? 모듈을 편리하게 관리하기 위해서!

"""
방법 1

import를 이용해서 폴더를 불러온 후, 함수 실행

import user.cal

print(cal.plus(3,4)) #7



방법 2

from - import 사용

함수/변수 사용시 .를 써주지 않아도 된다.

from user.cal import plus

print(plus(3,4))
#cal.plus()라고 적지 않아도 ok


"""