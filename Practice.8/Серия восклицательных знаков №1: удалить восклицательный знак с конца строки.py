""" Remove an exclamation mark from the end of a string.
    For a beginner kata, you can assume that the input data is always a string,
    no need to verify it.
"""


def remove(s):
    return s[:-1] if s.endswith('!') else s


tests = [
    ["Hi!", "Hi"],
    ["Hi!!!", "Hi!!"],
    ["!Hi", "!Hi"],
    ["!Hi!", "!Hi"],
    ["Hi! Hi!", "Hi! Hi"],
    ["Hi", "Hi"]
]
