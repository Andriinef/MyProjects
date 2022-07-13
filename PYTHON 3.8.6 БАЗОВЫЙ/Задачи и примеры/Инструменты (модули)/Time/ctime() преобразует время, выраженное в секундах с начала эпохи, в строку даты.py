""" ctime() преобразует время,
    выраженное в секундах с начала эпохи,
    в строку даты
"""
import time

# без аргумента возвращает
# текущее время (местное)
print('now:')
print(time.ctime())

# дата начала эпохи
print('\nstart (local):')
print(time.ctime(0))

# преобразование секунд в строку-дату
print('\nany:')
print(time.ctime(1023231233))
# now:
# Wed Jul 22 16:06:58 2020
#
# start (local):
# Thu Jan  1 03:00:00 1970
# 
# any:
# Wed Jun  5 02:53:53 2002
