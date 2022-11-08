""" Given an array of ones and zeroes, convert the equivalent binary value to an integer.
    Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
"""
from codewars_test import assert_equals


def binary_array_to_number(arr):
    return int("".join(map(str, arr)), base=2)


test0 = assert_equals(binary_array_to_number([0, 0, 0, 1]), 1)
test1 = assert_equals(binary_array_to_number([0, 0, 1, 0]), 2)
test2 = assert_equals(binary_array_to_number([1, 1, 1, 1]), 15)
test3 = assert_equals(binary_array_to_number([0, 1, 1, 0]), 6)
