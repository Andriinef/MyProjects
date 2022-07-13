""" Високосный год """

import calendar

# Возвращает True если год является
# високосным, иначе - False.
print(calendar.isleap(2020))
print(calendar.isleap(2019))

# Возвращает количество високосных лет
# в диапазоне от первого года
# до второго (не включая его)
print(calendar.leapdays(2000, 2020))
print(calendar.leapdays(2000, 2021))
# True
# False
# 5
# 6
