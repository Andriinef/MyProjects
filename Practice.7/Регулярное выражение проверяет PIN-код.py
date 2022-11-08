""" ATM machines allow 4 or 6 digit PIN codes and
    PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
    If the function is passed a valid PIN string, return true, else return false.
"""

from codewars_test import assert_equals


def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
    # return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()


test0 = assert_equals(validate_pin("1"), False, "Wrong output for '1'")
test1 = assert_equals(validate_pin("12"), False, "Wrong output for '12'")
test2 = assert_equals(validate_pin("123"), False, "Wrong output for '123'")
test3 = assert_equals(validate_pin("12345"), False, "Wrong output for '12345'")
test4 = assert_equals(validate_pin("1234567"), False, "Wrong output for '1234567'")
test5 = assert_equals(validate_pin("-1234"), False, "Wrong output for '-1234'")
test6 = assert_equals(validate_pin("-12345"), False, "Wrong output for '-12345'")
test7 = assert_equals(validate_pin("1.234"), False, "Wrong output for '1.234'")
test8 = assert_equals(validate_pin("00000000"), False, "Wrong output for '00000000'")
test9 = assert_equals(validate_pin("a234"), False, "Wrong output for 'a234'")
test10 = assert_equals(validate_pin(".234"), False, "Wrong output for '.234'")
test11 = assert_equals(validate_pin("1234"), True, "Wrong output for '1234'")
test12 = assert_equals(validate_pin("0000"), True, "Wrong output for '0000'")
test13 = assert_equals(validate_pin("1111"), True, "Wrong output for '1111'")
test14 = assert_equals(validate_pin("123456"), True, "Wrong output for '123456'")
test15 = assert_equals(validate_pin("098765"), True, "Wrong output for '098765'")
test16 = assert_equals(validate_pin("000000"), True, "Wrong output for '000000'")
test17 = assert_equals(validate_pin("123456"), True, "Wrong output for '123456'")
test18 = assert_equals(validate_pin("090909"), True, "Wrong output for '090909'")
