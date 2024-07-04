import random

print('비밀번호를 생성합시다!')

chars = ',!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'

number = input('비밀번호의 양을 입력해주세요.')
number = int(number)

length = input('비밀번호의 길이를 입력해주세요.')
length = int(length)

print('\n 여기 완성된 비밀번호 입니다:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)