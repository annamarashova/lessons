"""Написать функцию is_year_leap, принимающую 1 аргумент — год,
и возвращающую True, если год високосный, и False иначе.

Рассматриваем года нашей эры:
- 0 год высокосный, следующий +4
"""
def is_year_leap(year):
    if year % 4 == 0:
        print('True')
    else:
        print('False')

while True:
    year = int(input('Введите год:'))
    is_year_leap(year)