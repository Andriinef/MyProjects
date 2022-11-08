from codewars_test import assert_equals


def parts_sums(ls):
    if not ls:
        return [0]
    return [sum(ls), *parts_sums(ls[1:])]  # рекурсия


# def parts_sums(ls):
#     sums = [sum(ls)]
#     for i in ls:
#         sums.append(sums[-1]-i)
#     return sums


test = assert_equals(parts_sums([]), [0])
test1 = assert_equals(parts_sums([0, 1, 3, 6, 10]), [20, 20, 19, 16, 10, 0])
test2 = assert_equals(parts_sums([1, 2, 3, 4, 5, 6]), [21, 20, 18, 15, 11, 6, 0])
test3 = assert_equals(
    parts_sums([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]),
    [
        10037855,
        9293730,
        9292795,
        9292388,
        9291934,
        9291504,
        9291414,
        9291270,
        2581057,
        2580168,
        2579358,
        0,
    ],
)
