""" Заполнение случайными числами
"""
from random import randint

low = int(input("Enter min: "))
high = int(input("Enter max: "))

# Здесь i играет роль только счётчика цикла.
# Генерируются десять случайных чисел,
# они формируют список.
a = [randint(low, high) for i in range(10)]

# равносильно следующему:
# a = []
# for i in range(10):
#     a.append(randint(low, high))

print(a)
# Enter min: -5
# Enter max: 7
# [-4, 5, 5, 0, 7, 6, 4, -1, 1, 3]
