def func():  # функция без параметров
    x = int(input("Введите число: "))
    print('До: '+ str(x))
    x = x ** 2
    print('После:', str(x))

while True:  # бесконечный цикл
    func()
