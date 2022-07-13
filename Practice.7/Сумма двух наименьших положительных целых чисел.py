""" Create a function that returns the sum of the two lowest
    positive numbers given an array of minimum 4 positive integers.
    No floats or non-positive integers will be passed.
"""

from codewars_test import assert_equals


def sum_two_smallest_numbers(numbers):
    # numbers.sort()
    # return sum(numbers[:2])

    return sum(sorted(numbers)[:2])

    # numbers.sort()
    # return numbers[0] + numbers[1]


test = assert_equals(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
test1 = assert_equals(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
test2 = assert_equals(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)
