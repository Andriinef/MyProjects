""" split, splitlines, partition, rpartition
- разделение строки
"""
a = "  1 2 \n  4 5 "
# Метод split() без аргументов
# разделяет строку по пробельным символам
# и возвращает список подстрок.
print(a.split())
# Можно указать максимальное
# количество разделений
print(a.split(maxsplit=2))

b = "1 <> 22 <> ab"
# Можно передать
# подстроку-разделитель.
print(b.split(" <> "))

print("----------")

c = "1\n22\n345"
# splitlines() разделяет по
# символам перехода на новую строку.
print(c.splitlines())
print(c.split())
d = "1\n \n \n"
print(d.splitlines())
print(d.split())

print("----------")

a = "one two three"
# partition() разделяет строку
# по первому вхождению аргумента-сепаратора,
# возвращает кортеж из трех элементов -
# подстрока до сепаратора, сепаратор,
# подстрока после него.
print(a.partition("two"))
print(a.partition("four"))

b = "one two three two four"
# rpartition() разделяет строку
# по последнему вхождению сепаратора.
print(b.rpartition("two"))
print(b.rpartition("five"))
# ['1', '2', '4', '5']
# ['1', '2', '4 5 ']
# ['1', '22', 'ab']
# ----------
# ['1', '22', '345']
# ['1', '22', '345']
# ['1', ' ', ' ']
# ['1']
# ----------
# ('one ', 'two', ' three')
# ('one two three', '', '')
# ('one two three ', 'two', ' four')
# ('', '', 'one two three two four')
