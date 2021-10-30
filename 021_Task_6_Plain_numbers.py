"""Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True,
если оно простое, и False - иначе."""

def is_prime(number):
    dividers = list(range(2,number))
    for d in dividers:
        if number % d == 0:
            print('False')
            break
    else:
        print('True')

number = int(input('Введите число от 1 до 1000: '))
is_prime(number)