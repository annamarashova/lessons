#дескриптор файла - содержит целое число без знака, с помощью которого процесс обращается к открытому файлу.
file = open('README.md')
print(file.read())
file.close()

#менеджер контекста(оператор with)
with open('README.md') as file:
    lines = file.readlines()#вернет текст файла разбитый по строкам
    print(lines)

#менеджер контекста(оператор with)
with open('README.md') as file:
    for line in file:
        print(line)
