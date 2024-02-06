total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is: " + str(average))

"""
암시적 변환과 명시적 변환
영상 앞부분에서 본 것처럼 일부 데이터 유형은 암시적 변환으로 인해 혼합 및 일치될 수 있습니다. 
암시적 변환은 인터프리터가 우리를 도와 명시적으로 지시하지 않고도 자동으로 한 데이터 유형을 다른 데이터 유형으로 변환하는 것입니다.

대조적으로, 명시적 변환은 변환하려는 데이터 유형에 대한 관련 함수를 호출하여 한 데이터 유형에서 다른 데이터 유형으로 수동으로 변환하는 것입니다. 
일부 텍스트와 함께 숫자를 인쇄하려고 할 때 비디오 예제에서 이것을 사용했습니다. 그렇게 하기 전에 str() 함수를 호출하여 숫자를 문자열로 변환해야 했습니다. 
숫자가 명시적으로 문자열로 변환되면 나머지 텍스트 문자열과 결합하여 결과를 인쇄할 수 있습니다.



expression - 평가 시 결과를 생성하는 숫자, 기호 또는 기타 값의 조합

데이터 유형 data types - 데이터 유형 인스턴스(변수)의 속성 및 동작을 포함하는 데이터 클래스(예: 문자열, int, 부동 소수점, 부울 등)

변수 variable - 코드 내에서 고유한 이름으로 표시되며 특정 데이터 유형의 변경 가능한 값을 저장하는 데이터 유형 클래스의 인스턴스입니다.

암시적 변환 implicit conversion - Python 인터프리터가 자동으로 한 데이터 유형을 다른 데이터 유형으로 변환하는 경우

명시적 변환 explicit conversion - 데이터 유형 변환 함수를 사용하여 한 데이터 유형을 다른 데이터 유형으로 수동으로 변환하는 코드가 작성된 경우:

str() - 값(종종 숫자)을 문자열 데이터 유형 으로 변환합니다.

int() - 값(일반적으로 부동 소수점)을 정수 데이터 유형 으로 변환합니다.

float() - 값(보통 정수)을 float 데이터 유형 으로 변환합니다.


"""
#Variables Annotated by Type

import typing
# Define a variable of type str
z: str = "Hello, world!"
# Define a variable of type int
x: int = 10
# Define a variable of type float
y: float = 1.23
# Define a variable of type list
list_of_numbers: typing.List[int] = [1, 2, 3]
# Define a variable of type tuple
tuple_of_numbers: typing.Tuple[int, int, int] = (1, 2, 3)
# Define a variable of type dict
dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}
# Define a variable of type set
set_of_numbers: typing.Set[int] = {1, 2, 3}

# The following lines assign the variable to the left of the = 
# assignment operator with the values and arithmetic expressions 
# on the right side of the = assignment operator.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests


"""
Use variables to store values

Use basic arithmetic operators with variables to create expressions

Use explicit conversion to change a data type from float to string

"""

# This line outputs the result of the final calculation stored
# in the variable "share_per_person"
print("Each person needs to pay: " + str(share_per_person)) # change a data type

"""
Output multiple string variables on a single line to form a sentence

Use the plus (+) connector or a comma to connect strings in a print() function

Create spaces between variables in  a print() function

"""
# The following 5 lines assign strings to a list of variables.
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."

print(salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix) 
# The comma as a string ", " adds the conventional use of a comma plus a 
# space to separate the last name from the suffix.

# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name,",", suffix)
# However, you will find that this produces a space before a comma within a string.

"""
Resolve TypeError caused by a data type mismatch issue

Use an explicit conversion function

"""

# The following code causes a type error between a string 
# and an integer:

print("5 * 3 = " + (5*3)) 


# Resolution: 
# print("5 * 3 = " + str(5*3))
#
# To avoid a type error between the string and the integer within the
# print() function, you can make an explicit data type conversion by
# using the str() function to convert the integer to a string.  

numerator = 7
denominator = 0   # Possible resolution: Change the denominator value 
result = numerator / denominator
print(result)


# One possible assumption for a number divided by zero error might
# include the issue of a null value as a denominator (could happen when
# using a loop to iterate over values in a database). In such cases, the
# desired outcome may be to leave the numerator value intact. The
# numerator value can be preserved by reassigning the denominator with 
# the integer value of 1. The result would then equal the numerator.