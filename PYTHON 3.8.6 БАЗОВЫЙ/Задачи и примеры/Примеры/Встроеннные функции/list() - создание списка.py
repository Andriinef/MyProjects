""" list() - создание списка
"""
# Создаётся пустой список
a = list()

tuple_iterable = (1, 2, 3)
# Кортеж преобразовывается в список
b = list(tuple_iterable)

range_iterable = range(3, 8)
# Объект range преобразовывается в список
c = list(range_iterable)

str_iterable = "hello"
# Строка преобразуется в список символов
d = list(str_iterable)

another_iter = filter(lambda x: x % 6 == 0, range(55))
# С помощью list() можно получить список генерируемых итератором элементов
e = list(another_iter)

print(a)
print(b)
print(c)
print(d)
print(e)
# []
# [1, 2, 3]
# [3, 4, 5, 6, 7]
# ['h', 'e', 'ln', 'ln', 'o']
# [0, 6, 12, 18, 24, 30, 36, 42, 48, 54]
