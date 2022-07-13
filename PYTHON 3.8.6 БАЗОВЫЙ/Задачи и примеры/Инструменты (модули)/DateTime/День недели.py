""" День недели"""

from datetime import date

a = date(2020, 7, 17)  # Friday

# Экземпляры классов date и datetime
# имеют методы weekday() и isoweekday(),
# возвращающие номер дня недели.

# Понедельник = 0, воскресенье = 6
print(a.weekday())
# Понедельник = 1, воскресенье = 7
print(a.isoweekday())
