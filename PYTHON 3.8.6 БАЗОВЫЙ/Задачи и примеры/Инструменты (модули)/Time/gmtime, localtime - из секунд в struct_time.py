""" gmtime, localtime - из секунд в struct_time """

import time

# из секунд с начала "эпохи"
# в объект типа 'struct_time'

# GMT - Greenwich Mean Time (UTC - Coordinated Universal Time)
# - всемирное координированное время
gmt_from_sec = time.gmtime(1347871999)
# по местному времени
loc_from_sec = time.localtime(1347871999)
print(gmt_from_sec)
print(loc_from_sec)

# "Эпоха" - точка начала отсчета времени,
# она зависит от платформы.
# Чтобы узнать ее для данной платформы,
# используется аргумент 0.
era_start_gmt = time.gmtime(0)
era_start_loc = time.localtime(0)
print(era_start_gmt)
print(era_start_loc)

# Аргумент по умолчанию - текущее время.
gmt_now = time.gmtime()
loc_now = time.localtime()
print(gmt_now)
print(loc_now)
# time.struct_time(tm_year=2012, tm_mon=9, tm_mday=17, tm_hour=8, tm_min=53, tm_sec=19, tm_wday=0, tm_yday=261,
# tm_isdst=0) time.struct_time(tm_year=2012, tm_mon=9, tm_mday=17, tm_hour=12, tm_min=53, tm_sec=19, tm_wday=0,
# tm_yday=261, tm_isdst=0) time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0,
# tm_wday=3, tm_yday=1, tm_isdst=0) time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=3, tm_min=0,
# tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0) time.struct_time(tm_year=2020, tm_mon=7, tm_mday=22, tm_hour=9,
# tm_min=20, tm_sec=18, tm_wday=2, tm_yday=204, tm_isdst=0) time.struct_time(tm_year=2020, tm_mon=7, tm_mday=22,
# tm_hour=12, tm_min=20, tm_sec=18, tm_wday=2, tm_yday=204, tm_isdst=0)
