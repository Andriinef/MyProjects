""" "Добавление" к дате промежутка времени
"""
import datetime

# Первая дата -
# экземпляр типа date
today = datetime.date.today()
print(today)  # 2020-07-18

# Промежуток времени -
# экземпляр типа timedelta
delta = datetime.timedelta(24.01)
print(delta)  # 24 days, 0:00:00

# При сложении даты с промежутком
# времени получаем новую дату
that_day = today + delta
print(that_day)  # 2020-08-11
# 2020-07-18
# 24 days, 0:00:00
# 2020-08-11
