""" update, ... - изменение множества с помощью другого
"""
b = {3, 4, 5, 6, 7}

# Данные методы меняют исходное множество,
# а не возвращают новое.

a = {1, 2, 3, 4}
# Добавляет элементы из 'b', которых нет в 'a'
a.update(b)
print(a, "after update")

a = {1, 2, 3, 4}
# В 'a' остаются только те элементы,
# которые есть и в 'a', и в 'b'
a.intersection_update(b)
print(a, "after intersection update")

a = {1, 2, 3, 4}
# В 'a' остаются только те элементы, которых нет в 'b'
a.difference_update(b)
print(a, "after difference update")

a = {1, 2, 3, 4}
# Из 'a' исключаются те элементы, которые есть и в 'b'.
# Остальные элементы 'b' добавляются в 'a'.
a.symmetric_difference_update(b)
print(a, "after symmetric difference update")
# {1, 2, 3, 4, 5, 6, 7} after update
# {3, 4} after intersection update
# {1, 2} after difference update
# {1, 2, 5, 6, 7} after symmetric difference update
