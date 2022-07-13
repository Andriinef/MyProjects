""" Write a function, persistence, that takes in a positive parameter num
    and returns its multiplicative persistence,
    which is the number of times you must multiply
    the digits in num until you reach a single digit.
"""
from codewars_test import assert_equals


def persistence(n):
    counter = 0
    str_n = str(n)
    while len(str_n) is not 1:
        result = 1
        for i in str_n:
            result *= int(i)
        str_n = str(result)
        counter += 1
    return counter


test0 = assert_equals(persistence(39), 3)
test1 = assert_equals(persistence(4), 0)
test2 = assert_equals(persistence(25), 2)
test3 = assert_equals(persistence(999), 4)
