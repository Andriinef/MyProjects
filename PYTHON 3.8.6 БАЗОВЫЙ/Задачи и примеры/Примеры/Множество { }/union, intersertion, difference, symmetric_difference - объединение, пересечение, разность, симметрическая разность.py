""" union, intersertion, difference, symmetric_difference
    - объединение, пересечение, разность,
    симметрическая разность
"""
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a, '- a')
print(b, '- b')

# Результат содержит элементы
# всех множеств.
print(a.union(b))
# Вместо метода может использоваться
# специальный оператор.
print(a | b, 'union')

# В результат попадают элементы,
# которые есть в обоих множествах.
print(a.intersection(b))
print(a & b, 'intersection')

print(a.difference(b))
# Те, которые есть в 'a',
# но которых нет в 'b'.
print(a - b, 'difference: a - b')
# Те, которые есть в 'b', но не в 'a'.
print(b - a, 'difference: b - a')

# Исключаются совпадающие элементы.
print(a.symmetric_difference(b))
print(a ^ b, 'symmetric difference')
# {1, 2, 3, 4} - a
# {3, 4, 5, 6} - b
# {1, 2, 3, 4, 5, 6}
# {1, 2, 3, 4, 5, 6} union
# {3, 4}
# {3, 4} intersection
# {1, 2}
# {1, 2} difference: a - b
# {5, 6} difference: b - a
# {1, 2, 5, 6}
# {1, 2, 5, 6} symmetric difference
