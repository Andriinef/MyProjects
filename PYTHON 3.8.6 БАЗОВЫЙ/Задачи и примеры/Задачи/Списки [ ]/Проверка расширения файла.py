""" Проверка расширения файла
    Пользователь вводит имя файла.
    Проверить, находится ли расширение
    файла в списке допустимых.
"""

# список допустимых расширений
extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']

f_name = input()

# Введённая строка преобразуется в список.
# Разделение происходит по точке.
f_name = f_name.split('.')

# Если длина списка равна двум (или больше),
# то расширение было указано.
if len(f_name) >= 2:

    # Оно последнее в списке. Извлекаем его
    # и преобразуем к нижнему регистру.
    f_name_ext = f_name[-1].lower()

    # Если расширение содержится в списке
    # допустимых, то выводится "Yes".
    if f_name_ext in extensions:
        print("Yes")

    # Когда расширения нет в списке.
    else:
        print("No")

# Длина списка f_name меньше двух.
# Значит, у файла нет расширения.
else:
    print("The f_name has no extension")

# tree.jpg
# Yes
# phones.txt
# No
# run_prog
# The file has no extension
