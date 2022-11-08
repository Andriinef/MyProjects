""" randint, randrange - возвращают случайное целое
"""
import random

for i in range(6):
    # случайное число может быть
    # 10, 11, 12 или 13
    print(random.randint(10, 13), end=" ")

print("\n-----------")

for i in range(6):
    # 10, 11 или 12 (13 исключено)
    print(random.randrange(10, 13), end=" ")

print("\n-----------")

for i in range(6):
    # Первый аргумент по умолчанию = 0.
    # Может быть 0, 1 или 2.
    print(random.randrange(3), end=" ")

print("\n-----------")

for i in range(6):
    # Третий аргумент - шаг.
    # 10, 15, 20 или 25
    print(random.randrange(10, 30, 5), end=" ")
# 12 10 11 10 13 12
# -----------
# 12 10 12 11 10 12
# -----------
# 0 1 2 2 0 2
# -----------
# 20 10 15 25 10 20
