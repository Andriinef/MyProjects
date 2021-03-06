""" Вывести элементы, которые больше
    среднего арифметического элементов массива
    Заполнить список случайными целыми числами.
    Найти среднее арифметическое от
    значений элементов этого списка.
    Вывести на экран элементы списка,
    значения которых больше среднего арифметического.
"""

from random import randint

N = 10
a = []

# Переменная для хранения суммы элементов.
# Необходима для вычисления среднего значения.
suma = 0

for i in range(N):
    a.append(randint(0, 9))
    print(a[i], end=' ')

    # Добавляем значение
    # элемента к общей сумме.
    suma = suma + a[i]

print()

# Среднее значение находится при делении
# суммы значений элементов на их количество.
average = suma / N
print("The average: %.2f" % average)

# обход элементов списка
for i in a:
    # Если текущий элемент больше среднего,
    # то выводим элемент на экран.
    if i > average:
        print(i, end=' ')
print()
