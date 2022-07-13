""" index(x), count(x) - индекс элемента x,
    общее количество x
"""
#    0  1  2  3  4  5  6  7  8
a = [3, 0, 1, 3, 0, 2, 3, 4, 1]

# index(x) ищет первое вхождение
# элемента в список,
# возвращает его индекс
print(a.index(3))  # 0
# index(x, i) ищет первое вхождение,
# начиная с индекса i
print(a.index(3, 5))  # 6
# index(x, i, j) ищет первое вхождение
# на отрезке от i до j
print(a.index(3, 2, 4))  # 3

# Если элемента с заданным значением
# нет в списке или его отрезке,
# то метод index() возбуждает
# исключение ValueError
try:
    print(a.index(5))
except ValueError:
    print("5 is not in list")

# Метод count() возвращает
# количество элементов в списке
# с заданным значением.
print(a.count(1))  # 2
# Если значения нет в списке,
# возвращается 0.
print(a.count(10))  # 0
# 0
# 6
# 3
# 5 is not in list
# 2
# 0
