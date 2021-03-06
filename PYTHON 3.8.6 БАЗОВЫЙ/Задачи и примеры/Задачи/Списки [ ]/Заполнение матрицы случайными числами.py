""" Заполнение матрицы случайными числами
    Заполните матрицу случайными целыми числами
    и выведите ее на экран в табличной форме.
"""

from random import randint

# количество строк
N = int(input('Количество строк: '))

# Количество столбцов или
# количество элементов в каждой строке.
M = int(input('Количество столбцов: '))

# пустой список
a = []

# За одну итерацию внешнего цикла
# создаётся одна строка матрицы.
for i in range(N):

    # список для элементов строки матрицы
    b = []

    # Строка заполняется элементами
    for j in range(M):
        b.append(randint(1, 99))

    # и добавляется в матрицу.
    a.append(b)

# Вывод матрицы на экран.
# На каждой итерации внешнего цикла
# переменной i присваивается
# целая строка матрицы.
for i in a:

    # Во внутреннем цикле извлекается
    # каждый отдельный элемент строки
    for j in i:
        # и выводится на экран.
        print("%3d" % j, end='')

    # переход на новую линию
    print()
# 26 11 22 89 16  9  5 65 83  9
# 60  2 59 82 35 88 13 90 88 15
#  9 61 33 73 67 65 24 53 86 72
# 41 71 74 27 98 70 36 69 78 94
# 74  8  7 60 16 28 24 19 19 59
