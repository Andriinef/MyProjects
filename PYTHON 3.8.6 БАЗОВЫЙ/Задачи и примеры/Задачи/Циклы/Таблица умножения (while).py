""" Таблица умножения (while)
    Используя цикл "while", выведите таблицу умножения на экран.
"""

# Счётчик внешнего цикла,
# а также первый множитель.
i = 1

while i < 10:

    # Счётчик внутреннего цикла,
    # а также второй множитель.
    j = 1

    # На каждой итерации внешнего цикла,
    # тело внутреннего цикла
    # выполняется девять раз.
    # При этом переменная i не меняется.
    while j < 10:

        # Вычисляется очередной элемент (i*j)
        #  строки i таблицы умножения.
        # Элемент выводится на экран.
        print("%4d" % (i * j), end="")

        j += 1

    # переход на новую строку
    print()

    i += 1
