class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MAX_COORD <= x <= self.MIN_COORD:
            self.x = x + 1
            self.y = y + 2

    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("Error...")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "z":
            raise AttributeError("Error2...")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False
        # print("__getattr__" + item)

    def __delattr__(self, item):
        print("__delattr__" + item)
        object.__delattr__(self, item)


pt1 = Point(1, 2)
pt2 = Point(200, 20)
# a = pt1.x
a = pt1.y
# pt1.z = 5
del pt1.x
print(a)
print(pt1.yy)
print(pt1.__dict__)
