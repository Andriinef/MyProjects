from codewars_test import assert_equals


def find_smallest_int(arr):
    return sorted(arr)[0]
    # return min(arr)


test0 = assert_equals(find_smallest_int([78, 56, 232, 12, 11, 43]), 11)
test1 = assert_equals(find_smallest_int([78, 56, -2, 12, 8, -33]), -33)
test2 = assert_equals(find_smallest_int([0, 1 - 2**64, 2**64]), 1 - 2**64)
