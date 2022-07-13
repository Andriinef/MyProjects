""" Метаклассы – (type) это классы,
    экземпляры которых являются классами.
"""


# def create_class_point(name, base, attrs):
#     attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
#     return type(name, base, attrs)
class Meta(type):
    def __new__(mcs, name, base, attrs):
        attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
        return type.__new__(mcs, name, base, attrs)

    # def __init__(cls, name, base, attrs):
    #     super().__init__(name, base, attrs)
    #     cls.MAX_COORD = 100
    #     cls.MIX_COORD = 0


class Point(metaclass=Meta):
    @staticmethod
    def get_coord():
        return 0, 0


pt = Point()
# print(pt.MAX_COORD)
print(pt.get_coord())
