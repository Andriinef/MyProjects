""" getatime, getmtime, getctime - время последнего доступа,
    изменения, изменения метаданных (или время создания)
"""
import os.path
import time

f = '/home/p/flag.png'
# getatime(path) возвращает время
# (количество секунд с начала "эпохи")
# последнего доступа к path
af = os.path.getatime(f)
# getmtime(path) возвращает время
# последней модификации
mf = os.path.getmtime(f)
# getctime(path) возвращает системное ctime,
# которое в некоторых системах (как Unix) -
# время последнего изменения метаданных,
# а на других (как Windows) - время создания path.
cf = os.path.getctime(f)
print(af)
print(mf)
print(cf)

print(time.ctime(af))
print(time.ctime(mf))
print(time.ctime(cf))
# 1594808423.4133074
# 1560647773.754593
# 1576949805.7576323
# Wed Jul 15 13:20:23 2020
# Sun Jun 16 04:16:13 2019
# Sat Dec 21 20:36:45 2019
