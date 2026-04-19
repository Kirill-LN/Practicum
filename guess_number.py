from random import randint

span_number = randint(1, 100)

your_winner = False

while not your_winner :

    user_number = int(input('Write your number :'))

    if user_number == span_number: 
        your_winner = True
        break

    elif user_number > span_number:
        print('Ваше число больше того, что загадано')

    elif user_number < span_number:
        print('Ваше число меньше того, что загадано')

print('Отличная интуиция! Вы угадали число :)')
