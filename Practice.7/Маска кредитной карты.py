""" Usually when you buy something, you're asked whether your credit card number,
    phone number or answer to your most secret question is still correct.
    However, since someone could look over your shoulder,
    you don't want that shown on your screen.
    Instead, we mask it.
"""


# return masked string
from codewars_test import assert_equals


def maskify(cc):
    result = ""
    if len(cc) > 4:
        result += "#" * (len(cc) - 4)
    result += cc[-4:]
    return result

    # return "#"*(len(cc)-4) + cc[-4:]
    # return len(cc[:-4]) * "#" + cc[-4:]


test = assert_equals(maskify(""), "")
test1 = assert_equals(maskify("123"), "123")
test2 = assert_equals(maskify("SF$SDfgsd2eA"), "########d2eA")
