""" Вывод даты в различных форматах
"""
from datetime import date

a = date.today()

# Строковое представление экземпляра date по умолчанию
print(a)
# Метод strftime() объектов date,
# time и datetime позволяет задать
# формат вывода даты и времени
print(a.strftime("%d/%m/%y"))
print(a.strftime("%d/%m/%Y"))
print(a.strftime("%A, %d, %B, %Y"))
# 2020-07-18
# 18/07/20
# 18/07/2020
# Saturday, 18, July, 2020
