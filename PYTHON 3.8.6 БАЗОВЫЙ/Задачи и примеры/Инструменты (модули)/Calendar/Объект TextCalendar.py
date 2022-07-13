""" Объект TextCalendar """

from calendar import TextCalendar

c = TextCalendar()

# Методы экземпляров класса TextCalendar()
# возвращают строку, содержащую
# название месяцев, аббревиатуры дней недели,
# переходы на новую стоку и числа дней месяца.
a = c.formatmonth(2020, 8)
b = c.formatmonth(2020, 8, 4)

print(a)
print(b)
# Функция repr() возвращает печатное
# представление данного объекта.
print(repr(a))
#     August 2020
# Mo Tu We Th Fr Sa Su
#                 1  2
#  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30
# 31
#
#           September 2020
# Mon  Tue  Wed  Thu  Fri  Sat  Sun
#        1    2    3    4    5    6
#   7    8    9   10   11   12   13
#  14   15   16   17   18   19   20
#  21   22   23   24   25   26   27
#  28   29   30
#
# '    August 2020\nMo Tu We Th Fr Sa Su\n                1  2\n 3  4  5  6  7  8  9\n10 11 12 13 14 15 16\n17 18 19
# 20 21 22 23\n24 25 26 27 28 29 30\n31\n'
