a = [1, 2, 3, 4, 2, 5, 4]
a.append(6)  # добавление значений
a.remove(4)  # удаление значений - первого встретившегося
# удаление всех двоек
s = []
for b in a:
    if b == 2:
        continue
    s.append(b)
print(s)
print(list(reversed(s)))

# обход и изменение списка с помощью цикла while
n = 0
while n != len(a):
    a[n] = a[n] ** 2
    n += 1
print(a)
# обход исходного списка с сохранением измененных данных в новый
# table = []
# for b in a:
#     b = b ** 3
#     table.append(b)
# print(table)
# обход списка
b = [element ** 2 for element in a if element > 10]
print(b)
