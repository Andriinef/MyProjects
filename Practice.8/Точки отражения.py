""" Given two points P and Q, output the symmetric point of point P about Q.
    Each argument is a two-element array of integers representing the point's X and Y coordinates.
    Output should be in the same format, giving the X and Y coordinates of point P1.
    You do not have to validate the input.
"""

from pydoc import describe

from codewars_test import assert_equals


def symmetric_point(p, q):
    # x = 2*q[0] - p[0]
    # y = 2*q[1] - p[1]
    # return [x, y]
    return [2 * q[0] - p[0], 2 * q[1] - p[1]]


test = describe("Example Tests")
test1 = assert_equals(symmetric_point([0, 0], [1, 1]), [2, 2])
test2 = assert_equals(symmetric_point([2, 6], [-2, -6]), [-6, -18])
test3 = assert_equals(symmetric_point([10, -10], [-10, 10]), [-30, 30])
test4 = assert_equals(symmetric_point([1, -35], [-12, 1]), [-25, 37])
test5 = assert_equals(symmetric_point([1000, 15], [-7, -214]), [-1014, -443])
test6 = assert_equals(symmetric_point([0, 0], [0, 0]), [0, 0])
