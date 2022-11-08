""" It's pretty straightforward.
    Your goal is to create a function that removes the first and last characters of a string.
    You're given one parameter, the original string.
    You don't have to worry with strings with less than two characters.
"""
from codewars_test import assert_equals


def remove_char(s):
    # length = len(s)
    # result_string = s[1:length - 1]
    # return result_string
    return s[1:-1]


test = assert_equals(remove_char("eloquent"), "loquen")
test1 = assert_equals(remove_char("country"), "ountr")
test2 = assert_equals(remove_char("person"), "erso")
test3 = assert_equals(remove_char("place"), "lac")
test4 = assert_equals(remove_char("ok"), "")
test5 = assert_equals(remove_char("ooopsss"), "oopss")
