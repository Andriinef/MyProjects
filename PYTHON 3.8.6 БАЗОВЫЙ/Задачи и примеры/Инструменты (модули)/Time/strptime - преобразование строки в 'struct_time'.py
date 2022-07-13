""" strptime - преобразование строки в 'struct_time'
"""
import time

s = '25.03.2010, 15:30'  # строка
f = '%d.%m.%Y, %H:%M'    # шаблон
# Функция strptime() позволяет "извлечь"
# из произвольной строки данные даты и времени.
# Первый аргумент - строка, содержащая дату,
# второй - строка-шаблон с директивами,
# которые соответствуют "извлекаемым" данным из первой строки.
st = time.strptime(s, f)
print(st)
print(st.tm_yday)

print(time.ctime())
# По умолчанию шаблон соответствует строке,
# которую возвращает ctime():
# "%a %b %d %H:%M:%S %Y"
print(time.strptime(time.ctime()))
# time.struct_time(tm_year=2010, tm_mon=3, tm_mday=25, tm_hour=15, tm_min=30, tm_sec=0, tm_wday=3, tm_yday=84,
# tm_isdst=-1) 84 Thu Jul 23 12:46:55 2020 time.struct_time(tm_year=2020, tm_mon=7, tm_mday=23, tm_hour=12,
# tm_min=37, tm_sec=25, tm_wday=3, tm_yday=205, tm_isdst=-1)
