"""Игра "21".
Компьютер выдает по одной карте, юзер говорит "хватит" или "еще".
После каждого решения пользователя, компьютер показывает, сколько очков стало.
Игра заканчивается, когда пользователь ввел слово "хватит", или когда набрал >=21 очка.

Колода 36 карт, номиналы (по 4 штуки в колоде): 2-4, 6-11.
Выдаем 2 карты. Далее даем юзеру подумать хватит или нет.(если 21 - выиграл или 22 - проиграл).
Если хватит, выводим результат (число на руках), если нет, даем добрать "выдать 1 карту" пока не "хватит"."""

import random  # код из модуля рандом стандартной библиотеки

deck = [2, 3, 4, 6, 7, 8, 9, 10, 11] * 4  # список


def init_game():
    global deck
    f_hand1 = random.choice(deck)
    f_hand2 = random.choice(deck)
    f_hand_result = f_hand1 + f_hand2
    print("Первая карта:", f_hand1, "Вторая карта:", f_hand2)

    return f_hand_result


f_hand_result = init_game()


print("Сумма карт на руках =", f_hand_result)
if f_hand_result == 22:
    print("Вы проиграли")
    exit(0)  # выход из программы
if f_hand_result == 21:
    print("Вы выиграли")
    exit(0)
cycle = False
while cycle is False:
    choice = input('Хотите взять еще карту? Ответьте "Да" или "Нет":')
    if choice == "Да":
        f_hand_result += random.choice(deck)
        print("Сумма карт на руках =", f_hand_result)
        if f_hand_result > 21:
            print("Вы проиграли")
            exit(0)  # выход из программы
        if f_hand_result == 21:
            print("Вы выиграли")
            exit(0)
    if choice == "Нет":
        cycle = True
        print("Сумма карт на руках =", f_hand_result)
