s = ['ты', 'он', 'оно', 'она', 'ты', 'оно', 'ты', 'мы', 'ты', 'они']
# удаление второго элемента ты с конца
b = list(reversed(s))
table = []
N = 0
for m in b:
    if m == 'ты':
        N += 1
    if N == 2 and m == 'ты':
        continue # она пропускает весь оставшийся код цикла после себя
    table.append(m)
print(N)
print('table = ',table)
b = list(reversed(table)) #reversed возращает не список
print('b = ', b)
