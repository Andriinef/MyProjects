""" Получить случайное целое и случайное вещественное число
    в заданных диапазонах
    Вводятся границы диапазонов (целочисленного и вещественного).
    Выдать случайные числа в указанных пределах.
"""

# Из модуля random импортируем функцию
# random(), которая генерирует случайное
# вещественное число, и функцию randint(),
# которая генерирует случайное целое.
from random import randint, random

# Запрашиваем нижнюю и верхнюю границы
# диапазона, в пределах которого будет
# генерироваться случайное целое число.
print("Range of integers: ")
i_min = int(input())
i_max = int(input())

# Функция randint() генерирует случайное
# число n, которое не меньше i_min и не
# больше i_max.
n = randint(i_min, i_max)

print(n)

# Запрашиваем нижнюю и верхнюю границы
# диапазона, в пределах которого будет
# генерироваться случайное вещественное число.
print("Range of floats: ")
f_min = float(input())
f_max = float(input())

# Функция random() генерирует вещественное
# число от нуля до единицы. Единица не входит
# в диапазон.
n = random()

# Умножаем полученное число на длину
# диапазона. Например, если f_max = 5.6,
# f_min = 3.2, то получим случайное число
# от нуля до 2.4.
n = n * (f_max - f_min)

# Сдвигаем нижнюю границу числа на величину
# f_min. Таким образом случайное число будет
# лежать в пределах от 3.2 до 5.6.
n = n + f_min

print("%.3f" % n)
