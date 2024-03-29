""" Заполнение списка натуральными числами
"""
n = int(input())

# Перед 'for' находится то, что надо
# сделать с элементом перед
# его добавлением в список.
# В данном случае надо к i прибавить 1.
# На каждой итерации цикла
# 'for i in range(n)' переменной i
# присваивается число от 0 до n.
lst = [(i + 1) for i in range(n)]

# равносильно следующему:
# lst = []
# for i in range(n):
#     lst.append(i+1)

print(lst)
# 12
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
