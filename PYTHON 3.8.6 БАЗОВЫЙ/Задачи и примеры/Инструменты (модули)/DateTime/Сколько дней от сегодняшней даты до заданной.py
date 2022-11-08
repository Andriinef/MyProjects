""" Сколько дней от сегодняшней даты до заданной?
"""
import datetime

# Классовый метод today() класса date
# возвращает экземпляр date,
# содержащий текущую локальную дату.
today = datetime.date.today()
# Создаём два других объекта типа date.
past = datetime.date(2022, 2, 24)  # прошлое
future = datetime.date(2022, 9, 1)  # будущее

print(today)
print(past)
# Количество дней от сегодняшней
# даты до даты в прошлом.
print(today - past)
print(future)
# Количество дней от сегодняшней
# даты до даты в будущем.
print(future - today)
# 2020-07-19
# 2012-05-13
# 2989 days, 0:00:00
# 2021-01-04
# 169 days, 0:00:00
