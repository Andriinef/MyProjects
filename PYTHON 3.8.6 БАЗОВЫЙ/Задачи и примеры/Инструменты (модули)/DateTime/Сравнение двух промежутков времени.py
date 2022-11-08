""" Сравнение двух промежутков времени
"""
import datetime

# Объекты типа date
day1 = datetime.date(2020, 4, 20)
day2 = datetime.date(2020, 5, 5)
day3 = datetime.date(2020, 5, 21)
print(day1)
print(day2)
print(day3)

# При нахождении разности между двумя датами
# получается объект типа timedelta
# - промежуток времени
delta12 = abs(day1 - day2)
delta32 = abs(day3 - day2)
print(delta12)
print(delta32)

# Промежутки времени можно сравнивать между собой
print("delta12 > delta32?", delta12 > delta32)
# 2020-04-20
# 2020-05-05
# 2020-05-21
# 15 days, 0:00:00
# 16 days, 0:00:00
# delta12 > delta32? False
