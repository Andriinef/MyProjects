class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2, x3, y3):
        print(f"Geom {self.__class__}")
        self.__x = x1  # private
        self.__y1 = y1
        self._x2 = x2  # protected
        self._y2 = y2
        self.x3 = x3  # public
        self.y3 = y3
        self.__verify_coord(x1)

    def __verify_coord(self, coord):
        self.coord = coord
        return 0 <= coord < 100


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, x3, y3, fill=None):
        super().__init__(x1, y1, x2, y2, x3, y3)
        self.__fill = fill
