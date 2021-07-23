# Проверка года рождения на целое и диапазон (от 14 до 90 лет)
print("Отбор на pornhub")
is_digit = False  # переменная будет равна False до тех пор, пока юзер не введет число
while is_digit is False:
    age = input("Введите год рождения: ")
    if age.isdigit() is True:   # это проверка, что строка является целым числом
        is_digit = True
        age = int(age)
        if 1931 < age < 2007:
            print("Ваш возраст = " + str(2021 - age))
        else:
            print("Вы не подходите, pornhub таких не любит")
    else:
        print("Год рождения должен быть числом. Нужно ввести одно число.")
