"""Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
которому этот месяц принадлежит (зима, весна, лето или осень)."""


def season(month):
    if month in (1, 2, 12):
        print('Зима')
    elif 3 <= month <= 5:
        print('Весна')
    elif 6 <= month <= 8:
        print('Лето')
    elif 9 <= month <= 11:
        print('Осень')

while True:
    month = int(input('Введите номер месяца от 1 до 12: '))
    season(month)