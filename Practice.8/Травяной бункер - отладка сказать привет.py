from codewars_test import assert_equals


def say_hello(name):
    # return "Hello, {}".format(name)
    return f"Hello, {name}"
    # return "Hello, " + name


test = assert_equals(say_hello('Mr. Spock'), 'Hello, Mr. Spock')