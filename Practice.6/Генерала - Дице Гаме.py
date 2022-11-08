""" Generala — игра в кости, популярная в Южной Америке.
    Это очень похоже на Yahtzee,
    но с другим подходом к подсчету очков.
    В нее играют 5 кубиками, и возможные результаты
"""
from codewars_test import assert_equals


# set() используется для преобразования любого
# итерируемого объекта в последовательность итерируемых
# элементов с отдельными элементами, обычно называемыми Set {множество}.
# .count() возвращает количество раз, когда указанное значение встречается в строке
def points(dice):
    if len(set(dice)) == 1:
        return 50
    if len(set(dice)) == 2 and (dice.count(dice[0]) == 4 or dice.count(dice[0]) == 1):
        return 40
    if len(set(dice)) == 2:
        return 30
    if len(set(dice)) == 5 and "3" in dice and "4" in dice and "5" in dice:
        return 20
    return 0


# def points(dice):
#     def repeated_times(_dice, character):
#         return 5 - len(_dice.replace(character, ""))
#     _set = set(dice)
#     if len(_set) == 1:
#         return 50
#     elif len(_set) == 2:
#         item_left, item_right = _set
#         if repeated_times(dice, item_left) == 4  \
#            or repeated_times(dice, item_right) == 4:
#             return 40
#         elif repeated_times(dice, item_left) == 3  \
#                 and repeated_times(dice, item_right) == 2  \
#                 or repeated_times(dice, item_left) == 2  \
#                 and repeated_times(dice, item_right) == 3:
#             return 30
#     elif len(_set) == 5:
#         if "6" not in _set:
#             return 20
#         elif "6" in _set and "5" in _set and '4' in _set and '3' in _set:
#             return 20
#     return 0


test0 = assert_equals(points("55555"), 50)
test1 = assert_equals(points("66666"), 50)
test2 = assert_equals(points("11111"), 50)
test3 = assert_equals(points("22222"), 50)
test4 = assert_equals(points("33333"), 50)
test5 = assert_equals(points("44444"), 50)
test6 = assert_equals(points("44441"), 40)
test7 = assert_equals(points("33233"), 40)
test8 = assert_equals(points("22262"), 40)
test9 = assert_equals(points("12121"), 30)
test10 = assert_equals(points("44455"), 30)
test11 = assert_equals(points("66116"), 30)
test12 = assert_equals(points("12345"), 20)
test13 = assert_equals(points("23456"), 20)
test14 = assert_equals(points("34561"), 20)
test15 = assert_equals(points("13564"), 20)
test16 = assert_equals(points("62534"), 20)
test17 = assert_equals(points("44421"), 0)
test18 = assert_equals(points("61623"), 0)
test19 = assert_equals(points("12346"), 0)
