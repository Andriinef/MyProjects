""" Your task is to sort a given string.
    Each word in the string will contain a single number.
    This number is the position the word should have in the result.
    Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
    If the input string is empty, return an empty string.
    The words in the input String will only contain valid consecutive numbers.
"""
from codewars_test import assert_equals


def order(sentence):
    # разбивает строку на список
    words = sentence.split()
    numbers = range(1, 10)
    result = []
    for number in numbers:
        str_number = str(number)
        for word in words:
            if str_number in word:  # поиск str_number в word
                result.append(word)
    return ' '.join(result)


test0 = assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
test1 = assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
test2 = assert_equals(order(""), "")
