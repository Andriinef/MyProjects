""" set(), frozenset() - создание изменяемого
    и неизменяемого множеств
"""
# set() создаёт изменяемое множество
a = set(range(5))
# frozenset() создаёт
# неизменяемое множество
b = frozenset(range(3, 7))
print(a)
print(b)

# Добавлять элементы можно
# только во множество типа set
a.add(10)
print(a)

# пример создания множества из строки
a = set('abc4')
print(a)

# Изменяемое множество можно создать
# не только вызовом set(),
a = set([2, 2, 1, 1, 3])
# также путём использования
# фигурных скобок.
aa = {2, 2, 1, 1, 3}
# Во множестве не может
# быть одинаковых элементов.
print(a)  # {1, 2, 3}
print(aa)

# Неизменяемое множество можно
# создать только вызовом frozenset()
b = frozenset([2, 2, 1])
print(b)
# {0, 1, 2, 3, 4}
# frozenset({3, 4, 5, 6})
# {0, 1, 2, 3, 4, 10}
# {'a', '4', 'b', 'c'}
# {1, 2, 3}
# {1, 2, 3}
# frozenset({1, 2})
