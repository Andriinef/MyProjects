""" Your task is to convert strings to how they would be written by Jaden Smith.
    The strings are actual quotes from Jaden Smith,
    but they are not capitalized in the same way he originally typed them.
"""
from codewars_test import assert_equals


def to_jaden_case(string):
    return ' '.join(text.capitalize() for text in string.split())


test = assert_equals(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")
