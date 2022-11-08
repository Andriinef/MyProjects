""" join, split, splitext - объединение составных
    частей адреса и разделение его на части
"""
import os.path

# os.path является вложенным модулем в модуль os,
# и реализует некоторые полезные функции для работы с путями

# Объединяет один или более компонентов пути
# с помощью разделителя директорий, который добавляется
# к каждой не пустой части пути, кроме последней.
print(os.path.join("/home", "user", "file.txt"))
print(os.path.join("user", "file.txt"))

# Разделяет адрес на пару (head, tail),
# где tail - последний компонент пути,
# а head - все, что находится до него.
print(os.path.split("/home/user/file.txt"))
# Разделяет адрес на пару,
# где хвост - расширение файла.
print(os.path.splitext("/home/user/file.txt"))
# /home/user/file.txt
# user/file.txt
# ('/home/user', 'file.txt')
# ('/home/user/file', '.txt')
