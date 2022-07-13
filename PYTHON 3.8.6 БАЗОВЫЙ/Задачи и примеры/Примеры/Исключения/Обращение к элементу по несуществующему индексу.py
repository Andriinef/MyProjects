""" Обращение к элементу по несуществующему индексу
"""
a = [1.2, 1.8, 3.2, 2.5, 1.7, 2.6, 0.5]

print("s - stop")

while True:
    # запрашиваем индекс элемента
    ind_x = input("ID: ")
    if ind_x == 's':
        break

    try:
        # Если было введено не число,
        # будет сгенерировано исключение
        # ValueError.
        # Поток выполнения сразу перейдет
        # к ветке 'except ValueError'.
        ind_x = int(ind_x)
        # Если был введен индекс,
        # которого нет в списке,
        # будет сгенерировано исключение
        # IndexError.
        print(a[ind_x])

    # Перехват и обработка исключений позволяет
    # программе не завершиться,
    # а перейти к следующей итерации цикла.
    except ValueError:
        print("Must be an integer!")
    except IndexError:
        print("No item with ID =", ind_x)
# s - stop
# ID: 4
# 1.7
# ID: 3
# 2.5
# ID: 8
# No item with ID = 8
# ID: 0
# 1.2
# ID: s
