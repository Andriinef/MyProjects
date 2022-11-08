""" eists - действительно ли существует объект
    по данному адресу
"""
from os.path import exists

# exists(path) возвращает True если
# path ссылается на существующий путь
# или дескриптор открытого файла

a = "desc.txt"
print(exists(a))

a = "test.txt"
print(exists(a))

a = "/boot/grub/"
print(exists(a))

a = "/home/user/"
print(exists(a))
# True
# False
# True
# False
