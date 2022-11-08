""" Complete the solution so that it reverses the string passed into it.
"""

import codewars_test as test


def solution(string):
    # result_string = ''
    # for i in string:
    #     result_string = i + result_string
    # return result_string
    return string[::-1]


@test.describe("Fixed Tests")
def basic_tests():
    @test.it("Basic A_Draft Cases")
    def basic_test_cases():
        test.assert_equals(solution("world"), "dlrow")
        test.assert_equals(solution("hello"), "olleh")
        test.assert_equals(solution(""), "")
        test.assert_equals(solution("h"), "h")
        test.assert_equals(solution("1, 2, 3"), "3, 2, 1")
