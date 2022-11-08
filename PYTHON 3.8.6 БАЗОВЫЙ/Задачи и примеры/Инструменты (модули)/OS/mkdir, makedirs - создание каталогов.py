""" mkdir, makedirs - создание каталогов
"""
import os

print(os.listdir())

# Функция mkdir() создает каталог
# по указанному адресу.
os.mkdir("test")
# Чтобы создать каталог 'lang',
# папка 'test' уже должна существовать.
os.mkdir("test/lang")

try:
    # С помощью mkdir() нельзя создать
    # дерево каталогов.
    os.mkdir("test1/folder")
except FileNotFoundError:
    print("mkdir() creates one directory at a time")

print(os.listdir())
print(os.listdir("test"))

# Для создания дерева каталогов
# используется функция makedirs().
os.makedirs("test1/folder/pics")

print(os.listdir())
print(os.listdir("test1"))
print(os.listdir("test1/folder"))
# ['mkdir_makedirs.py', 'desc.txt']
# mkdir() creates one directory at a time
# ['mkdir_makedirs.py', 'test', 'desc.txt']
# ['lang']
# ['mkdir_makedirs.py', 'test1', 'test', 'desc.txt']
# ['folder']
# ['pics']
