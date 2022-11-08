class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"Geom {self.__class__}")
        self.x = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print("Geom2")


class Line(Geom):
    name = "Line"

    def draw(self):
        print("Line")


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        Geom.__init__(self, x1, y1, x2, y2)  # super()
        print("Rect")
        self.fill = fill


x = Line(1, 1, 2, 2)
r = Rect(1, 1, 2, 2)
# print(x.__dict__)
# print(r.__dict__)
# print(x.name)
# print(r.name)
# x.draw()
# r.draw()
# print(issubclass(int, object))
