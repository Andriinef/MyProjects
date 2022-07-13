""" Create a method sayHello/say_hello/SayHello that takes as input a name,
    city, and state to welcome a person. Note that name will be an array
    consisting of one or more values that should be joined together
    with one space between each, and the length of the
    name array in test cases will vary.
"""
from codewars_test import assert_equals


def say_hello(name, city, state):
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"


test0 = assert_equals(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'),
                      'Hello, John Smith! Welcome to Phoenix, Arizona!',
                      'Hello, John Smith! Welcome to Phoenix, Arizona!')
test1 = assert_equals(say_hello(['Franklin', 'Delano', 'Roosevelt'], 'Chicago', 'Illinois'),
                      'Hello, Franklin Delano Roosevelt! Welcome to Chicago, Illinois!', )
test2 = assert_equals(say_hello(['Wallace', 'Russel', 'Osbourne'], 'Albany', 'New York'),
                      'Hello, Wallace Russel Osbourne! Welcome to Albany, New York!')
test3 = assert_equals(say_hello(['Lupin', 'the', 'Third'], 'Los Angeles', 'California'),
                      'Hello, Lupin the Third! Welcome to Los Angeles, California!')
test4 = assert_equals(say_hello(['Marlo', 'Stanfield'], 'Baltimore', 'Maryland'),
                      'Hello, Marlo Stanfield! Welcome to Baltimore, Maryland!')
