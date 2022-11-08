""" Метод hash()возвращает хеш-значение объекта,
    если оно есть. Хэш-значения — это просто целые числа,
    которые используются для быстрого сравнения ключей словаря
    во время просмотра словаря.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.row and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


p1 = Point(1, 2)
p2 = Point(1, 2)
# print(hash(p1), hash(p2), sep="\n")
