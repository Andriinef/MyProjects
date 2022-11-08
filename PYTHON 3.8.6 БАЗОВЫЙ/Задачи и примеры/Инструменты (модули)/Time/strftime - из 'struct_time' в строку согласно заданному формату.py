""" strftime - из 'struct_time' в строку
    согласно заданному формату
"""
import time

# strftime() похожа на asctime(), но здесь вы можете
# сами задать форму строки-даты.
# Строка с шаблоном даты передается первым аргументом,
# вторым - кортеж или struct_time.
# Строка содержит директивы,
# что и как выводить (см. документацию).

# Если второго аргумента нет,
# выводится текущее локальное время.
now = time.strftime("%A %B %d %H:%M %Z")
print(now)

tuple_time = (2020, 7, 21, 7, 44, 20, 1, 203, 0)
# Вместо struct_time можно передавать кортеж.
yesterday = time.strftime("%c - %j day of the year", tuple_time)
print(yesterday)

# Получаем объект struct_time,
era_start = time.gmtime(0)
print(era_start)
# передаем его в strrftime().
print(time.strftime("%c", era_start))
# Thursday July 23 11:32 MSK
# Tue Jul 21 07:44:20 2020 - 203 day of the year
# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
# Thu Jan  1 00:00:00 1970
