# class StripChars:
#     def __init__(self, chars):
#         self.__counter = 0
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise TypeError("Error...")
#         return args[0].strip(self.__chars)
#
#
# s1 = StripChars("?:.,:; ")
# s2 = StripChars(" ")
# a = input("Input: ")
# res = s1(a)
# res2 = s2(a)
# print(res, res2, sep="\n")
import math


class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


def df_sin(x):
    return math.sin(x)


df_sin = Derivate(df_sin)
print(df_sin(math.pi / 3))
