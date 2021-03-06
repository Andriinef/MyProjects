""" Как удалить случайный элемент словаря?
    Дан словарь.
    Написать код, который удаляет один из элементов словаря.
    Выбор удаляемого элемента должен быть случайным
    (псевдослучайным).
"""


import random

d = {"A": 4, "O": 6, "P": 10,
     "M": 7, "B": 3}
print(d)

# Метод keys() создаёт объект,
# содержащий ключи словаря.
# Этот объект преобразуется в
# список ключей с помощью функции list().
keys = list(d.keys())

# Функция choice() выбирает
# случайный элемент из последовательности.
# В переменную 'what_del'
# записывается случайный ключ.
what_del = random.choice(keys)

# Удаляем из словаря элемент
# по его ключу.
del d[what_del]

print(d)
# {'A': 4, 'O': 6, 'P': 10, 'M': 7, 'B': 3}
# {'A': 4, 'O': 6, 'M': 7, 'B': 3}
