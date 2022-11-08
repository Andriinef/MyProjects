""" dirname, basename - получить имена директории
    и файла из пути
"""
import os.path

# Возвращает адрес директории.
# Это первый элемент пары, которую возвращает функция split().
print(os.path.dirname("/home/user/test.html"))
# Возвращает "базовое" имя пути.
# Это второй элемент пары, которую возвращает функция split().
print(os.path.basename("/home/user/test.html"))

# Функции не проверяют, действительно
# ли существует такой путь, что в нем
# является каталогом, а что файлом.
print(os.path.dirname("/home/user/"))
print(os.path.dirname("/home/user"))
# /home/user
# test.html
# /home/user
# /home
