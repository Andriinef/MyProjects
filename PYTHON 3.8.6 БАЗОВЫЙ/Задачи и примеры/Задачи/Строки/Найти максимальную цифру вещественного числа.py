""" Найти максимальную цифру вещественного числа
    Генерируется случайное вещественное число.
    Найти в нем максимальную цифру.
"""

# Функция random() из модуля random
# генерирует вещественные
# случайные числа от 0 до 1.
from random import random

# Генерируется случайное число
# от 0 до 1000 и округляется
# до 3-х знаков после запятой
num = round(random() * 1000, 3)
print(num)

# число преобразуется в строку
str_num = str(num)

# Переменная, которая будет
# содержать максимальную цифру.
# Присваивается значение меньшее,
# чем любая допустимая цифра.
max_digit = -1

# Количество итераций цикла
# равно длине строки.
# Переменная i принимает значения
# от 0 до len-1 включительно.
for i in range(len(str_num)):

    # Извлекается символ под индексом i.
    # Если он является точкой,
    if str_num[i] == ".":
        # то итерация цикла прерывается.
        # Происходит переход к следующей итерации.
        continue

    # Иначе символ преобразовывается
    # к целому числу и сравнивается
    # со значением maxDigit.
    # Если maxDigit меньше,
    elif max_digit < int(str_num[i]):
        # то этой переменной присваивается
        # числовое представление символа.
        max_digit = int(str_num[i])

print(max_digit)
