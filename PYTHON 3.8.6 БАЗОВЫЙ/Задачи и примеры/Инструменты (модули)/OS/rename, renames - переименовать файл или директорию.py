""" rename, renames - переименовать файл или директорию
"""
import os

print(os.listdir())
# rename() переименовывает один файл или
# одну директорию по указанному адресу.
# Первый аргумент - исходное имя,
# второй - новое.
os.rename('test.txt', 'hello.txt')
print(os.listdir())

os.makedirs('pics/land')
print(os.listdir())
print(os.listdir('pics'))
# Если требуется переименовать путь,
# используется функция renames().
os.renames('pics/land', 'imgs/grass')
print(os.listdir())
print(os.listdir('imgs'))
# ['test.txt']
# ['hello.txt']
# ['hello.txt', 'pics']
# ['land']
# ['hello.txt', 'imgs']
# ['grass']
