a = [1, 2, 3, 4, 5]
a.append(6)  # добавление значений
a.remove(4)  # удаление значений
n = 0
while n != 5:
    a[n] = a[n] ** 2
    n += 1
print(a)
a = [element ** 2 for element in a if element > 10]
print(a)
