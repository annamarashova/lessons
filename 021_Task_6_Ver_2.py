def is_prime(number):
    dividers = list(range(2,int((number/2)+1)))
    print(dividers)
    prime = True
    for d in dividers:
        if number % d == 0:
            prime = False
    return prime

number = int(input('Введите число от 1 до 1000: '))
print(is_prime(number))