""" Return an array, where the first element is the count of positives numbers
    and the second element is sum of negative numbers.
    0 is neither positive nor negative.
    If the input is an empty array or is null, return an empty array.
"""
from codewars_test import assert_equals


def count_positives_sum_negatives(arr):
    count_positives = 0
    sum_negatives = 0
    if not arr:
        return []
    for i in arr:
        if i > 0:
            count_positives += 1
        elif i < 0:
            sum_negatives += i
    return [count_positives, sum_negatives]


test = assert_equals(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]), [10, -65])
test1 = assert_equals(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]), [8, -50])
test2 = assert_equals(count_positives_sum_negatives([1]), [1, 0])
test3 = assert_equals(count_positives_sum_negatives([-1]), [0, -1])
test4 = assert_equals(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0])
test5 = assert_equals(count_positives_sum_negatives([]), [])
