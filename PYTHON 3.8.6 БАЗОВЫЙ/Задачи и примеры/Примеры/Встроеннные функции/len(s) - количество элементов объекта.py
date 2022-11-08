""" len(s) - количество элементов объекта
"""

a = [1, 2, 3, 4]
b = ("a", "b", "c")
c = {1: "a", 2: "b"}
d = range(8)
e = "hello"

# len() возвращает количество
# элементов объекта.
# Аргумент может быть последовательностью
# или коллекцией.
print(a, " -", len(a))
print(b, " -", len(b))
print(c, " -", len(c))
print(d, " -", len(d))
print(e, " -", len(e))
# [1, 2, 3, 4]  - 4
# ('a', 'b', 'c')  - 3
# {1: 'a', 2: 'b'}  - 2
# range(0, 8)  - 8
# hello  - 5
