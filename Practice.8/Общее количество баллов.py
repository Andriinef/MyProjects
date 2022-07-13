""" Write a function that takes such collection and counts the points of our team in the championship.
    Rules for counting points for each match:
"""
from codewars_test import assert_equals


def points(games):
    counter = 0
    for i in games:
        scores_str = i.split(':')
        first_score = int(scores_str[0])
        second_score = int(scores_str[1])

        if first_score > second_score:
            counter += 3
        elif first_score == second_score:
            counter += 1
    return counter


# def points(games):
#     count = 0
#     for score in games:
#         res = score.split(':')
#         if res[0]>res[1]:
#             count += 3
#         elif res[0] == res[1]:
#             count += 1
#     return count


test = assert_equals(points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']), 30)
test1 = assert_equals(points(['1:1', '2:2', '3:3', '4:4', '2:2', '3:3', '4:4', '3:3', '4:4', '4:4']), 10)
test2 = assert_equals(points(['0:1', '0:2', '0:3', '0:4', '1:2', '1:3', '1:4', '2:3', '2:4', '3:4']), 0)
test3 = assert_equals(points(['1:0', '2:0', '3:0', '4:0', '2:1', '1:3', '1:4', '2:3', '2:4', '3:4']), 15)
test4 = assert_equals(points(['1:0', '2:0', '3:0', '4:4', '2:2', '3:3', '1:4', '2:3', '2:4', '3:4']), 12)
