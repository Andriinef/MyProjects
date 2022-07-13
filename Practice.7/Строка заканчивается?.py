""" Complete the solution so that it returns true if
    the first argument(string) passed in ends with
    the 2nd argument (also a string).
"""
from codewars_test import assert_equals


def solution(string, ending):
    return string[-len(ending):] == ending or '' == ending
    # return ending in string[-len(ending):]
    # return string.endswith(ending)


test0 = assert_equals(solution('abcde', 'cde'), True)
test1 = assert_equals(solution('abcde', 'abc'), False)
test2 = assert_equals(solution('abcde', ''), True)
