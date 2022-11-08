""" Объект Calendar """

# Модуль calendar содержит
# класс Calendar,
from calendar import Calendar

# от которого создаются
# экземпляры типа Calendar.
c = Calendar()

# С помощью различных методов получают
# не отформатированные календарные данные
month = c.itermonthdays(2020, 7)

# и используют их по своему усмотрению.
i = 1
for day in month:
    print("%3d" % day, end="")
    if i % 7 == 0:
        print()
    i += 1

#  0  0  1  2  3  4  5
#  6  7  8  9 10 11 12
# 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# 27 28 29 30 31  0  0
