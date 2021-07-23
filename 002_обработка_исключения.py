# Ввод веса с проверкой данных
p = input("Сколько ты весишь? Ответ: ")
try:
    p = float(p)
except Exception:
    print("Нужно ввести только число.")
else:
    print("Ты весишь", str(round(p, 1)))
