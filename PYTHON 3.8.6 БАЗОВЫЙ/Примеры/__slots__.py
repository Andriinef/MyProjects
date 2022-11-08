class Point:
    __slots__ = ("x", "y", "length")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = x + y


class Point2D(Point):
    pass


p = Point(10, 20)
p2 = Point2D(100, 200)
p2.z = 30
""" - ограничение создаваемых локальных ствойств
    - уменьшение занимаемой памяти
    - ускорение работы локальными свойствами
"""
