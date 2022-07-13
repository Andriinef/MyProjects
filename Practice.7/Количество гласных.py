""" Return the number (count) of vowels in the given string.
    We will consider a, e, i, o, u as vowels for this Kata (but not y).
    The input string will only consist of lower case letters and/or spaces.
"""
from codewars_test import assert_equals


def get_count(sentence):
    # counter = 0
    # for i in sentence:
    #     if i in ('a', 'e', 'i', 'o', 'u'):
    #         counter += 1
    # return counter
    return sum(1 for i in sentence if i in ('a', 'e', 'i', 'o', 'u'))
    # return len([x for x in inputStr if x in 'aeoiu'])


test0 = assert_equals(get_count("aeiou"), 5, f"Incorrect answer for \"aeiou\"")
test1 = assert_equals(get_count("y"), 0, f"Incorrect answer for \"y\"")
test2 = assert_equals(get_count("bcdfghjklmnpqrstvwxz y"), 0, f"Incorrect answer for \"bcdfghjklmnpqrstvwxz y\"")
test3 = assert_equals(get_count(""), 0, f"Incorrect answer for empty string")
test4 = assert_equals(get_count("abracadabra"), 5, f"Incorrect answer for \"abracadabra\"")
