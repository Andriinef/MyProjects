""" asctime() преобразует кортеж
    или struct_time в строку-дату
"""
import time

tuple_time = (2020, 7, 21, 7, 44, 20, 1, 203, 0)
# передача в asctime() кортежа из 9 элементов
print(time.asctime(tuple_time))

print("-------")

# Создается объект struct_time.
gm = time.gmtime()
print(gm)
# Передаем его в asctime()
print(time.asctime(gm))

print("--------")

# Аргументом по умолчанию является экземпляр
# struct_time, который возвращает
# функция localtime() без аргументов.
# В результате asctime() возвращает строку
# с текущим местным временем.
print(time.asctime())

print("--------")

# Секунды конвертируются в struct_time,
# который преобразуется в строку с датой.
print(time.asctime(time.gmtime(10002038476)))
# Tue Jul 21 07:44:20 2020 ------- time.struct_time(tm_year=2020, tm_mon=7, tm_mday=21, tm_hour=4, tm_min=40,
# tm_sec=8, tm_wday=1, tm_yday=203, tm_isdst=0) Tue Jul 21 04:40:08 2020 -------- Tue Jul 21 07:40:08 2020 --------
# Tue Dec 14 08:01:16 2286
