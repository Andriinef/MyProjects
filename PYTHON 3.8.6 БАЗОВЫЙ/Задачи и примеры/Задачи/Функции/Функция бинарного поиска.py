""" Функция бинарного поиска
    Напишите функцию,
    которая принимает отсортированный список
    и искомый в нем элемент,
    с помощью метода бинарного поиска
    ищет этот элемент в списке.
    Функция должна возвращать индекс искомого элемента,
    если он найден в списке,
    или None в случае отсутствия элемента.
"""

from random import randint


# Функция в качестве аргументов принимает
# список и элемент, который надо найти в списке.
# Функция возвращает None,
# если элемент не был найден,
# или индекс местонахождения элемента.
def search(lst, item):
    # середина списка
    mid = len(lst) // 2
    # индекс первого элемента
    low = 0
    # индекс последнего элемента
    high = len(lst) - 1
    # Цикл выполняется до тех пор,
    # пока искомый элемент не найден
    # или нижняя граница не превышает верхнюю.
    while lst[mid] != item and low <= high:
        # Если искомый элемент больше
        # элемента в середине среза, то
        # нижняя граница сдвигается за середину.
        if item > lst[mid]:
            low = mid + 1
        # Если искомый элемент меньше элемента
        # в середине среза, то верхняя граница
        # устанавливается перед серединой.
        else:
            high = mid - 1
        # вычисляется середина нового среза
        mid = (low + high) // 2
    # Нижняя граница может быть больше верхней
    # только в случае, когда элемент не был найден.
    if low > high:
        return None
    # Иначе искомый элемент
    # находится в текущей середине.
    else:
        return mid


# заполнение и сортировка списка
a = []
for i in range(10):
    a.append(randint(1, 20))
a.sort()
print(a)

# элемент для поиска
value = int(input())

# Вызов функции,
# вывод полученного результата на экран.
print(search(a, value))
# [3, 6, 7, 7, 8, 9, 13, 13, 15, 18]
# 10
# None
# [1, 8, 8, 10, 12, 13, 15, 18, 19, 19]
# 18
# 7
