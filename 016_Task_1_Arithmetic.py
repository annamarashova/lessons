def arithmetic(a, b, c):
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        print("%.2f" % (a / b))# функция round(a/b, 2)
    else: print ('Неизвестная операция')

while True:
    a = int(input('Введите число:'))
    b = int(input('Введите второе число: '))
    c = input('Введите действие (+, - , *, /): ')

    arithmetic(a,b,c)