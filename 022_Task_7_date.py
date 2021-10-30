"""Написать функцию date, принимающую 3 аргумента — день, месяц и год.
Вернуть True, если такая дата есть в нашем календаре, и False иначе."""

def date(year, month, day):
    if year < 0 or month < 1 or month > 12 or day > 31 or day < 1:
        return False
    if month == 2 or year%4 == 0:
        if 1 <= day <= 29:
            return True
        else:
            return False
    if month == 2 or year%4 != 0:
        if 1 <= day <= 28:
            return True
        else:
            return False
    long_months = (1,3,5,7,8,10,12) #кортеж
    if month in long_months:
        if 1 <= day <= 31:
            return True
        else:
            return False
    else:
        if 1 <= day <= 30:
            return True
        else:
            return False

while True:
    year = int(input('Введите год: '))
    month = int(input('Введите месяц: '))
    day = int (input('Введите день: '))
    result = date(year, month, day)
    if result == True:
        print(f'Дата существует: {day}.{month}.{year}')
    else:
        print (f'Такой даты не сущетсвует: {day}.{month}.{year}')
