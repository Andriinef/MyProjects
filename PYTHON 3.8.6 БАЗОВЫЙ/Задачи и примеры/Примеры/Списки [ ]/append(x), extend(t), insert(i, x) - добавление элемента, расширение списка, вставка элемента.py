""" append(x), extend(t), insert(i, x)
    - добавление элемента, расширение списка,
    вставка элемента
"""

a = [3, 4]
print(a)
# Метод append(x) добавляет элемент
# x в конец списка.
a.append(20)
print(a)

b = [30, 40]
# Если с помощью append(x)
# добавить другой список, то он
# добавится как один элемент.
a.append(b)
print(a)  # [3, 4, 20, [30, 40]]
# Для объединения элементов двух
# списков используется метод extend(x)
a.extend(b)
print(a)  # [3, 4, 20, [30, 40], 30, 40]
# Вместо extend() можно использовать
# оператор +, то есть
# складывать списки: a + b
a += b
print(a)

print('-----------')

a = [1, 2, 3]
print(a)
# Метод insert(i, x) позволяет
# вставлять значение
# в любое место списка.
# Первый аргумент - индекс,
# второй - вставляемое значение.
a.insert(0, -1)
print(a)  # [-1, 1, 2, 3]
a.insert(3, 8)
print(a)  # [-1, 1, 2, 8, 3]
# [3, 4]
# [3, 4, 20]
# [3, 4, 20, [30, 40]]
# [3, 4, 20, [30, 40], 30, 40]
# [3, 4, 20, [30, 40], 30, 40, 30, 40]
# -----------
# [1, 2, 3]
# [-1, 1, 2, 3]
# [-1, 1, 2, 8, 3]
