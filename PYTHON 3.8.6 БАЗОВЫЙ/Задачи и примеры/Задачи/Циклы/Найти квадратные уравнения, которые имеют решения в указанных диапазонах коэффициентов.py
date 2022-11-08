""" Найти квадратные уравнения,
    которые имеют решения в указанных диапазонах коэффициентов
    Вводятся целочисленные диапазоны
    для коэффициентов "a", "b" и "c"
    квадратного уравнения.
    Перебрать все возможные сочетания
    коэффициентов и определить,
    при каких из них квадратное уравнение имеет корни,
    а при каких - нет.
    Если уравнение имеет корни, вычислить их.
"""
from math import sqrt

# диапазоны коэффициентов a, b, c
a1 = int(input("a1: "))
a2 = int(input("a2: "))
b1 = int(input("b1: "))
b2 = int(input("b2: "))
c1 = int(input("c1: "))
c2 = int(input("c2: "))

# Создаются объекты-диапазоны.
# +1 позволяет включить верхнюю границу
a = range(a1, a2 + 1)
b = range(b1, b2 + 1)
c = range(c1, c2 + 1)

# перебираются все сочетания коэффициентов
# i - текущий элемент из диапазона a
# j - текущий элемент из диапазона b
# k - текущий элемент из диапазона c
for i in a:

    if i == 0:
        # Если i равен 0, то уравнение
        # не квадратное, а линейное
        # поэтому решать его не надо.
        # Переходим к следующей итерации цикла.
        continue

    for j in b:
        for k in c:
            # Выводятся текущие значения
            # коэффициентов a, b, c.
            print(i, j, k, end=" ")

            # вычисляется дискриминант
            D = j * j - 4 * i * k

            # Если дискриминант не меньше нуля,
            if D >= 0:
                # вычисляются корни уравнения
                x1 = (-j - sqrt(D)) / (2 * i)
                x2 = (-j + sqrt(D)) / (2 * i)

                x1 = round(x1, 2)
                x2 = round(x2, 2)
                print("Yes", x1, x2)

            # Если дискриминант меньше нуля,
            else:
                # корней нет.
                print("No")

# a1: 1
# a2: 3
# b1: -1
# b2: 1
# c1: -1
# c2: 1
# 1 -1 -1 Yes -0.62 1.62
# 1 -1 0 Yes 0.0 1.0
# 1 -1 1 No
# 1 0 -1 Yes -1.0 1.0
# 1 0 0 Yes 0.0 0.0
# 1 0 1 No
# 1 1 -1 Yes -1.62 0.62
# 1 1 0 Yes -1.0 0.0
# 1 1 1 No
# 2 -1 -1 Yes -0.5 1.0
# 2 -1 0 Yes 0.0 0.5
# 2 -1 1 No
# 2 0 -1 Yes -0.71 0.71
# 2 0 0 Yes 0.0 0.0
# 2 0 1 No
# 2 1 -1 Yes -1.0 0.5
# 2 1 0 Yes -0.5 0.0
# 2 1 1 No
# 3 -1 -1 Yes -0.43 0.77
# 3 -1 0 Yes 0.0 0.33
# 3 -1 1 No
# 3 0 -1 Yes -0.58 0.58
# 3 0 0 Yes 0.0 0.0
# 3 0 1 No
# 3 1 -1 Yes -0.77 0.43
# 3 1 0 Yes -0.33 0.0
# 3 1 1 No
