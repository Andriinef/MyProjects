"""reversed(seq) - возвращает итератор, обратный seq
"""

a = [1, 2, 3, 4]
# Функция reversed() возвращает
# объект-итератор, генерирующий элементы
# переданной последовательности
# в обратном порядке.
b = reversed(a)
print(b)
print(list(b))

a = "hello"
b = reversed(a)
print(b)
# Помещаем элементы в список,
# затем объединяем их в строку.
print("".join(list(b)))

a = range(5)
b = reversed(a)
print(b)
print(list(b))
# <list_reverseiterator object at 0x7fb003f8d0f0>
# [4, 3, 2, 1]
# <reversed object at 0x7fb003edc7f0>
# olleh
# <range_iterator object at 0x7fb002821b10>
# [4, 3, 2, 1, 0]
