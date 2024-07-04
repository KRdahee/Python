import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'숫자 맞춰봐라 호롤롤ㄹ랄랄 1이랑 {x} 사이: '))
        if guess < random_number :
            print("너무 낮음 수고")
        elif guess > random_number :
            print('너무 높음 수고염')
        print(f'오 맞췄음 님 똑똑스키 {random_number}맞음')

guess(10)