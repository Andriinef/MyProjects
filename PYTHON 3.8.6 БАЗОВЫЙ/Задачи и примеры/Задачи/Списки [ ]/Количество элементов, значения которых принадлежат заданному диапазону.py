""" Количество элементов,
    значения которых принадлежат заданному диапазону
    Пользователь вводит минимальную и
    максимальную границы диапазона.
    Программа должна выводить на экран
    количество элементов матрицы,
    значения которых принадлежат заданному диапазону.
"""

import random

# Заполнение и вывод списка на экран
arr = []
for i in range(30):
    x = int(random.random() * 100)
    arr.append(x)
    print("%3d" % x, end="")
    # Переход на новую строку
    # после каждого пятого элемента.
    if (i + 1) % 5 == 0:
        print()

# Нижняя и верхняя границы диапазона
minimum = int(input("Min: "))
maximum = int(input("Max: "))

# Количество элементов, попавших в диапазон
counter = 0

# Перебор элементов списка
for i in arr:
    # Если значение принадлежит диапазону,
    if minimum <= i <= maximum:
        # то увеличить счётчики количества
        # таких элементов.
        counter += 1

print(counter)
