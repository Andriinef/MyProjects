""" zip(*iter) - агрегация элементов из
    нескольких итерируемых объектов
"""

a = [1, 2, 3, 4, 5]
b = [11, 12, 13, 14]
c = [21, 22, 23, 24]

# Создаётся объект-итератор, генерирующий кортежи.
# Каждый кортеж содержит i-ый элемент из a, b, c.
# Количество кортежей равно количеству элементов
# самого короткого списка.
z = zip(a, b, c)
# извлекается первый элемент итератора
print(z.__next__())  # (1, 11, 21)
# оставшиеся преобразуются в список
# [(2, 12, 22), (3, 13, 23), (4, 14, 24)]
print(list(z))

print('--------')

new_list1 = []
new_list2 = []
# zip() используется для обработки разных
# итерируемых объектов в одном цикле
for i, j in zip(a, b):
    new_list1.append(i+1)
    new_list2.append(j-1)

print(new_list1)
print(new_list2)
# (1, 11, 21)
# [(2, 12, 22), (3, 13, 23), (4, 14, 24)]
# --------
# [2, 3, 4, 5]
# [10, 11, 12, 13]
