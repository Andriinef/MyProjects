""" choice, choices - возвращают случайный элемент
    или элементы из последовательности
"""
import random

a = [3, 8, 9, 0]
print("a -", a)

for i in range(6):
    # choice(seq) возвращает один случайный элемент
    # из непустой последовательности 'seq'.
    print(random.choice(a), end=" ")

print()

for i in range(6):
    # choices(seq) возвращает k-размерный
    # список элементов, выбранных из 'seq'.
    # По умолчанию k=1.
    print(random.choices(a), end=" ")

print()

for i in range(2):
    print(random.choices(a, k=3), end=" ")

print()

b = [10, 5, 1, 1]
for i in range(2):
    # Если указана последовательность weights,
    # выбор делается в соответствии с весами элементом.
    # Здесь 3 имеет вес 10 и будет выбираться чаще,
    # чем число 9, которое имеет вес 1.
    print(random.choices(a, k=4, weights=b), end=" ")

print("\na -", a)
# a - [3, 8, 9, 0]
# 3 9 8 3 3 0
# [3] [0] [0] [0] [9] [3]
# [8, 0, 3] [0, 9, 3]
# [0, 3, 8, 8] [8, 3, 3, 3]
# a - [3, 8, 9, 0]
