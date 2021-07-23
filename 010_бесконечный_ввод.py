def func():  # функция без параметров
    x = int(input("Введите число: "))
    x = x ** 10
    print(x)


x = 10
while True:  # бесконечный цикл
    print("До")
    func()
    print(x)
    print("После")
