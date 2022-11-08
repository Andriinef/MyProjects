""" Разворачивание строки подобной "a-z"
    Даются две буквы английского алфавита.
    Вывести на экран строку,
    включающую по порядку все буквы алфавита
    от заданных первой буквы до последней включительно.
"""

# первый символ
first = input("The first: ")

# последний символ
last = input("The last: ")

# Символы можно сравнивать, так как
# в таблице символов они идут по порядку.
# Символ, стоящий впереди, меньше
# символа, который находится за ним.
# Цикл выполняется до тех пор,
# пока первый символ не больше последнего.
while first <= last:

    # выводим на экран символ
    print(first, end="")

    # Получаем его числовой код
    # из таблицы символов.
    code = ord(first)

    # Переходим к коду
    # следующего символа.
    code = code + 1

    # Получаем следующий символ
    # по его коду.
    first = chr(code)
    # Этот символ будет выводиться
    # в следующей итерации цикла.

print()
