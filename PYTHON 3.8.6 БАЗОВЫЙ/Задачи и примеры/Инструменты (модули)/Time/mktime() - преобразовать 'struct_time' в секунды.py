""" mktime() - преобразовать 'struct_time' в секунды """

import time

# Функция mktime() принимает объект типа struct_time
# или кортеж из 9-ти чисел,
# возвращает количество секунд, прошедших
# с начала "эпохи" до переданного в качестве аргумента времени.
tuple_time = (2020, 7, 21, 7, 44, 20, 1, 203, 0)
print(time.mktime(tuple_time))

print("-------")

# Получаем struct_time текущего времени по гринвичу.
gm = time.gmtime()
print(gm)
# Преобразуем struct_time в секунды.
print(time.mktime(gm))

print("-------")

# Получаем struct_time локального времени
# в момент начала "эпохи",
local = time.localtime(0)
print(local)
# переводим в секунды.
print(time.mktime(local))
# 1595306660.0
# -------
# time.struct_time(tm_year=2020, tm_mon=7, tm_mday=22, tm_hour=12, tm_min=6, tm_sec=11, tm_wday=2, tm_yday=204, tm_isdst=0)
# 1595408771.0
# -------
# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=3, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
# 0.0
