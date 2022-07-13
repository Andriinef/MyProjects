""" Арифметические операции с промежутками времени
"""
from datetime import timedelta

first_delta = timedelta(weeks=3, days=2, hours=12)
print(first_delta)  # 23 days, 12:00:00

second_delta = timedelta(hours=4, minutes=15, seconds=30)
print(second_delta)  # 4:15:30

# Экземпляры timedelta можно складывать,
# находить разность, умножать на целое
# и вещественное число и др.

# Третий промежуток времени равен
# длительности двух предыдущих.
third_delta = first_delta + second_delta
print(third_delta)  # 23 days, 16:15:30

# Половина первого промежутка времени
half_first_delta = first_delta / 2
print(half_first_delta)  # 11 days, 18:00:00
# 23 days, 12:00:00
# 4:15:30
# 23 days, 16:15:30
# 11 days, 18:00:00
