import queue


def check_braces_closed(string):
    """Проверить, все ли скобки в строке закрыты, вывести результат на экран.

    Пример:
        (5+10)*2 - Все скобки закрыты
        (100-((40 + 4)*12+33-44*5)) - Все скобки закрыты
        1+((5+3)*2 - Скобка с индексом 2 не закрыта
        1+(5+3))*2 - Скобка с индексом 7 лишняя

    Реализация:
        0. Создаем пустой стэк.
        1. Проходим строку посимвольно
        2. Если встретили символ открывающей скобки "(" -- добавляем в стэк позицию этого символа в строке.
        3. Если встретили символ закрывающей скобки ")" -- достаем элемент с верхушки стэка.
        4. Если на шаге 3 в стэке не оказалось элемента -- значит, закрывающая скобка лишняя.
        5. Если после прохождения всей строки в стэке остались элементы -- значит, есть незакрытая скобка.
        6. Если после прохождения всей строки в стэке не осталось элементов -- значит, все скобки закрыты.
    """
    stack = queue.LifoQueue()
    for index, char in enumerate(string):
        if char == "(":
            stack.put(index)
        elif char == ")":
            try:
                stack.get(block=False)
            except queue.Empty:
                print(f"Скобка с индексом {index} лишняя")
                return

    if stack.empty():
        print(f"Все скобки закрыты!")
    else:
        print(f"Скобка с индексом {stack.get()} не закрыта")


if __name__ == '__main__':
    check_braces_closed("(100-((40 + 4)))*12+33-44*5)")
