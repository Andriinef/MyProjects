""" Сильное число — это число, сумма факториала его цифр равна самому числу
"""
import math

from codewars_test import assert_equals


def strong_num(number):
    # res_sum = 0
    # for item in [int(j) for j in str(number)]:
    #     res_sum += math.factorial(item)

    if sum(math.factorial(item) for item in [int(j) for j in str(number)]) == number:
        return "STRONG!!!!"
    return "Not Strong !!"


test0 = assert_equals(strong_num(1), "STRONG!!!!")
test1 = assert_equals(strong_num(2), "STRONG!!!!")
test2 = assert_equals(strong_num(145), "STRONG!!!!")
test3 = assert_equals(strong_num(7), "Not Strong !!")
test4 = assert_equals(strong_num(93), "Not Strong !!")
test5 = assert_equals(strong_num(185), "Not Strong !!")
