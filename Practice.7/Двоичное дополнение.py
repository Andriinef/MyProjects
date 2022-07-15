""" Implement a function that adds two numbers together and returns their sum in binary.
    The conversion can be done before, or after the addition.
"""
from codewars_test import assert_equals


def add_binary(a, b):
    return bin(a + b).replace('0b', '')  # метод string.replace(old value, new value, count)
    # заменяет указанную фразу другой указанной фразой

    # return bin(a+b)[2:]


test0 = assert_equals(add_binary(1, 1), "10")
test1 = assert_equals(add_binary(0, 1), "1")
test2 = assert_equals(add_binary(1, 0), "1")
test3 = assert_equals(add_binary(2, 2), "100")
test4 = assert_equals(add_binary(51, 12), "111111")
