""" Сортировка пузырьком
    Заполните список случайными числами
    и выведите его на экран.
    Выполните сортировку списка по возрастанию,
    используя метод пузырька.
    Выведите на экран отсортированный список.
"""

from random import randint

N = 7
a = []

# Заполнение списка
# случайными числами.
for i in range(N):
    a.append(randint(1, 20))
print(a)

# За одну итерацию внешнего цикла
# на "дно" (в конец списка)
# опускается один элемент
# (самый большой).
for i in range(N - 1):

    # Количество итераций внутреннего
    # цикла зависит от i.
    # Когда i = 0, то количество
    # итераций равно 6.
    # Самый большой элемент окажется
    # в самом конце списка.
    # Когда i = 1, количество
    # итераций равно 5.
    # Самый большой из оставшихся окажется
    # на предпоследнем месте списка.
    # ...
    # Когда i = 5, количество
    # итераций равно 1.
    # Сравниваются первый и второй
    # элементы списка.
    for j in range(N - i - 1):
        # Обмен значений элементов, если
        # впереди стоящий больше следующего.
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)
# [7, 17, 3, 17, 4, 16, 1]
# [1, 3, 4, 7, 16, 17, 17]
