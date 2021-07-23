"""Поменять местами значения x и y"""
x = 1
y = 2
z = y
y = x
x = z
print(y)
print(x)

# или в одну строчку (только для питона)
x, y = y, x
print(y)
print(x)
