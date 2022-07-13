""" Write a generic function chainer that takes a starting value,
    and an array of functions to execute on it
"""
from codewars_test import assert_equals


def chain(init_val, functions):
    if functions:
        function = functions[0]
        return chain(function(init_val), functions[1:])  # рекусия
    return init_val


    # return chain(functions[0](init_val),functions[1:]) if functions else init_val


def add10(x): return x + 10
def mul30(x): return x * 30


test0 = assert_equals(chain(42, []), 42)
test1 = assert_equals(chain(50, [mul30]), 1500)
test2 = assert_equals(chain(50, [mul30, add10]), 1510)
test3 = assert_equals(chain(50, [add10, mul30]), 1800)
