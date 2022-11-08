""" Given an array describing the color of each glove,
    return the number of pairs you can constitute,
    assuming that only gloves of the same color can form pairs.
"""
from codewars_test import assert_equals


def number_of_pairs(gloves):
    counter = 0
    gloves.sort()
    while True:
        if len(gloves) <= 1:
            return counter
        elif gloves[0] != gloves[1]:
            gloves.pop(0)
        elif gloves[0] == gloves[1]:
            counter += 1
            gloves.pop(0)
            gloves.pop(0)

    # color_count = {}
    # counter = 0
    # for i in gloves:
    #     color_count[i] = gloves.count(i)
    # for i in color_count.values():
    #     while i > 1:
    #         i //= 2
    #         counter += 1
    # return counter

    # return sum(gloves.count(color)//2 for color in set(gloves))


test1 = assert_equals(number_of_pairs(["red", "red"]), 1)
test2 = assert_equals(number_of_pairs(["red", "green", "blue"]), 0)
test3 = assert_equals(
    number_of_pairs(["gray", "black", "purple", "purple", "gray", "black"]), 3
)
test4 = assert_equals(number_of_pairs([]), 0)
test5 = assert_equals(
    number_of_pairs(
        ["red", "green", "blue", "blue", "red", "green", "red", "red", "red"]
    ),
    4,
)
