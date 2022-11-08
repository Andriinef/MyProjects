""" walk - обход дерева каталогов
"""
import os

# Создается объект-генератор, генерирующий кортежи.
# Каждый кортеж соответствует
# одному каталогу дерева и содержит три элемента:
# адрес, список вложенных каталогов, список вложенных файлов.
a = os.walk("/home/pl/folder")
print(a)

for i in a:
    print(i)

# ('/home/pl/folder', ['HTML', 'imgs'], ['flag.png'])
# 'folder' - каталог верхнего уровня данного дерева.
# Он содержит два вложенных каталога и один файл.
# ('/home/pl/folder/HTML', [], ['test.html', 'test1.html'])
# Каталог HTML не содержит подкаталогов, содержит два файла.
# ('/home/pl/folder/imgs', [], [])
# Каталог imgs пуст.
# <generator object walk at 0x7f97c159a360>
# ('/home/pl/folder', ['HTML', 'imgs'], ['flag.png'])
# ('/home/pl/folder/HTML', [], ['test.html', 'test1.html'])
# ('/home/pl/folder/imgs', [], [])
