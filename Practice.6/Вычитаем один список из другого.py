""" Ваша цель в этом ката — реализовать функцию разности,
    которая вычитает один список из другого
    и возвращает результат
"""
from codewars_test import assert_equals


def array_diff(a, b):
    # for i in range(len(b)):
    #     while b[i] in a:
    #         a.remove(b[i])
    # return a

    # return [item for item in a if item not in b]
    result = list()
    for item in a:
        if item not in b:
            result.append(item)
    return result


test0 = assert_equals(
    array_diff([1, 2], [1]), [2], "a was [1,2], b was [1], expected [2]"
)
test1 = assert_equals(
    array_diff([1, 2, 2], [1]), [2, 2], "a was [1,2,2], b was [1], expected [2,2]"
)
test2 = assert_equals(
    array_diff([1, 2, 2], [2]), [1], "a was [1,2,2], b was [2], expected [1]"
)
test3 = assert_equals(
    array_diff([1, 2, 2], []), [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]"
)
test4 = assert_equals(array_diff([], [1, 2]), [], "a was [], b was [1,2], expected []")
test5 = assert_equals(
    array_diff([1, 2, 3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]"
)
