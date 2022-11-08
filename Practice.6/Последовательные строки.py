""" You are given an array(list) strarr of strings and an integer k.
    Your task is to return the first longest string consisting of k
    consecutive strings taken in the array.
"""
from codewars_test import assert_equals


def longest_consec(strarr, k):
    if k > len(strarr) or k <= 0:
        return ""
    return max(
        ["".join(strarr[i : i + k]) for i in range(len(strarr) - k + 1)], key=len
    )


testing0 = assert_equals(
    longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2),
    "abigailtheta",
)
testing1 = assert_equals(
    longest_consec(
        [
            "ejjjjmmtthh",
            "zxxuueeg",
            "aanlljrrrxx",
            "dqqqaaabbb",
            "oocccffuucccjjjkkkjyyyeehh",
        ],
        1,
    ),
    "oocccffuucccjjjkkkjyyyeehh",
)
testing2 = assert_equals(longest_consec([], 3), "")
testing3 = assert_equals(
    longest_consec(
        [
            "itvayloxrp",
            "wkppqsztdkmvcuwvereiupccauycnjutlv",
            "vweqilsfytihvrzlaodfixoyxvyuyvgpck",
        ],
        2,
    ),
    "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck",
)
testing4 = assert_equals(
    longest_consec(["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2),
    "wlwsasphmxxowiaxujylentrklctozmymu",
)
testing5 = assert_equals(
    longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), ""
)
testing6 = assert_equals(
    longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3),
    "ixoyx3452zzzzzzzzzzzz",
)
testing7 = assert_equals(
    longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15), ""
)
testing8 = assert_equals(
    longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0), ""
)
