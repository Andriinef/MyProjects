""" all(iter), any(iter) - все элементы True,
    любой элемент True?
"""

a = [2, 3, 0, 8]
b = [5, 8]
c = []

# all(a) возвращает False потому что
# один элемент (0) a не True,
# any(a) возвращает True потому что
# есть хотя бы один True-элемент.
print(all(a), any(a))  # False True

# all(b) возвращает True потому что
# все элементы объекта True.
print(all(b), any(b))  # True True

# Если итерируемый объект пуст,
# all() возвращает True
# (нет False-элементов),
# any() возвращает False
# (нет True-элементов).
print(all(c), any(c))  # True False
# False True
# True True
# True False
