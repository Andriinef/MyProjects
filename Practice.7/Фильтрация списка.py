"""In this kata you will create a function that takes a list
    of non-negative integers and strings and returns a new list
    with the strings filtered out.
"""
from codewars_test import assert_equals

# def filter_list(n):
# return [list_numbers for list_numbers in n if isinstance(list_numbers, int)]


""" isinstance( объект , информация о классе ) 
    Возврат True, если аргумент объекта является экземпляром аргумента классa
    или его (прямого, косвенного или виртуального ) подкласса. 
    Если объект не является объектом данного типа, функция всегда возвращает False. 
    Если classinfo является кортежем объектов типов (или, рекурсивно, других таких кортежей), 
    вернуть, True если объект является экземпляром любого из типов. 
    Если classinfo не является типом или кортежем типов и таких кортежей, 
    возникает TypeError исключение.
"""


def filter_list(n):
    return [x for x in n if type(x) is int]


# def filter_list(l):
#     new_list =[]
#     for x in l:
#         if type(x) != str:
#             new_list.append(x)
#     return new_list


test0 = assert_equals(
    filter_list([1, 2, "a", "b"]), [1, 2], 'For input [1, 2, "a", "b"]'
)
test1 = assert_equals(
    filter_list([1, "a", "b", 0, 15]), [1, 0, 15], 'Fot input [1, "a", "b", 0, 15]'
)
test3 = assert_equals(
    filter_list([1, 2, "aasf", "1", "123", 123]),
    [1, 2, 123],
    'For input [1, 2, "aasf", "1", "123", 123]',
)
