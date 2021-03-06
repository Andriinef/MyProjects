""" Пересечение списков.
    Найти совпадающие элементы двух списков
    Даны два списка.
    Сформировать третий список из элементов,
    которые встречаются и в первом списке,
    и во втором.
"""

# исходные списки
a = [5, [1, 2], 2, 'r', 4, 'ee']
b = [4, 'we', 'ee', 3, [1, 2]]

# Элементы, которые встречаются
# в обоих списках.
c = []

# Берем каждый элемент первого списка,
for i in a:
    # если такого элемента еще нет в третьем списке,
    if i in c:
        continue
    # то, перебирая все элементы второго списка,
    # будем сравнивать текущий элемент
    # первого списка со всеми элементами второго.
    for j in b:
        # Если совпадение найдено,
        if i == j:
            # то добавляем элемент в третий список.
            c.append(i)
            # Прерываем внутренний цикл, т. к.
            # дальнейшее сравнение не имеет смысла.
            break

print(c)

# Примечание. Задача может быть решена проще:
# с помощью пересечения множеств.
# Однако такое решение не подходит,
# если списки содержат вложенные списки.
# a = [5, 2, 'r', 4, 'ee']
# b = [4, 1, 'we', 'ee', 2, 'r']
# c = list(set(a) & set(b))
# print(c)
