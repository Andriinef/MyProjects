""" "Изменение" у даты года, месяца или дня
"""
from datetime import date

d1 = date(2019, 10, 16)
# Объекты типа date являются неизменяемыми.
# С помощью метода replace() от исходного
# объекта создаётся новый date-экземпляр.
# При этом можно поменять значение
# того или иного свойства.
d2 = d1.replace(year=2020, month=12, day=15)
d3 = d1.replace(month=11)

print(d1)
print(d2)
print(d3)
# 2019-10-16
# 2020-12-15
# 2019-11-16
