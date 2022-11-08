""" isfile, isdir - находится ли по указанному
    адресу обычный файл или директория?
"""
import os.path

a = "desc.txt"
b = "../../calendar"

# isfile(path) возвращает True,
# если путь - существующий обычный файл.
print(os.path.isfile(a))
print(os.path.isfile(b))
# isdir(path) возвращает True,
# если путь - существующая директория.
print(os.path.isdir(a))
print(os.path.isdir(b))

# Если путь не существует,
# isdir() и isfile() возвращают False.
print(os.path.isfile("f"))
# True
# False
# False
# True
# False
