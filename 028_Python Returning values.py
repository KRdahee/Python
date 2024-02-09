def area_triangle(base, height):
    return base*height/2

#No Output

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)

#Error on line 1:
#    area_a = area_triangle(5,4)
#NameError: name 'area_triangle' is not defined

sum = area_a + area_b

#NameError: name 'area_a' is not defined

print("The sum of both areas is: " + str(sum))

#The sum of both areas is: <built-in function sum>

def area_triangle(base, height):
    return base*height/2
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))

#The sum of both areas is: 20.5

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

#No Output

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

"""
Error on line 1:
    hours, minutes, seconds = convert_seconds(5000)
NameError: name 'convert_seconds' is not defined
"""

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

#1 23 20

def greeting(name):
    print("Welcome, " + name)
result = greeting("Christine")
print(result)

#Welcome, Christine
#None