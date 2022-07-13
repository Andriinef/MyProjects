""" Simple, given a string of words, return the length of the shortest word(s).
    String will never be empty and you do not need to account for different data types.
"""
from codewars_test import assert_equals


def find_short(s):
    return sorted(len(word) for word in s.split())[0]   # Метод split()разбивает строку на список.
    # return min(len(word) for word in s.split())


test = assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
test1 = assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
test2 = assert_equals(find_short("lets talk about javascript the best language"), 3)
test3 = assert_equals(find_short("i want to travel the world writing code one day"), 1)
test4 = assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)
test5 = assert_equals(find_short("Let's travel abroad shall we"), 2)
