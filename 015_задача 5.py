N = input('Введите целое число больше или равно 2: ')
while int(N) < 2:
    N = input('Число меньше двух. Введите целое число больше или равно 2: ')
S = []
n = 0
while n != int(N):
    s = int(input('Введите целое число: '))
    S.append(s)
    n += 1
print(S)
S.sort()
print(S)
print(S[0])
