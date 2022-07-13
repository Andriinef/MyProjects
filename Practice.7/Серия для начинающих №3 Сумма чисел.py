""" Given two integers a and b, which can be positive or negative,
    find the sum of all the integers between and including them and return it.
    If the two numbers are equal return a or b.
"""
from codewars_test import assert_equals


def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


test0 = assert_equals(get_sum(0, 1), 1)
test1 = assert_equals(get_sum(0, -1), -1)
