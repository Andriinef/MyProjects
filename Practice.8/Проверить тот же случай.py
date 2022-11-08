""" Write a function that will check if two given characters are the same case.
    If either of the characters is not a letter, return -1
    If both characters are the same case, return 1
    If both characters are letters, but not the same case, return 0
"""

import codewars_test as test


# def same_case(a, b):
#     if not a.isalpha() or not b.isalpha():      # Возвращает значение True, если все символы являются буквами алфавита (az)
#         return -1
#     if a.isupper() == b.isupper():      # Проверяет, все ли символы в строке находятся в верхнем регистре.
#         return 1
#     else:
#         return 0
def same_case(a, b):
    return a.isupper() == b.isupper() if a.isalpha() and b.isalpha() else -1


@test.describe("Basic Tests")
def test_group():
    @test.it("basic test case")
    def test_case():
        test.assert_equals(same_case("C", "B"), 1)
        test.assert_equals(same_case("b", "a"), 1)
        test.assert_equals(same_case("d", "d"), 1)
        test.assert_equals(same_case("A", "s"), 0)
        test.assert_equals(same_case("c", "B"), 0)
        test.assert_equals(same_case("b", "Z"), 0)
        test.assert_equals(same_case("\t", "Z"), -1)
        test.assert_equals(same_case("H", ":"), -1)
