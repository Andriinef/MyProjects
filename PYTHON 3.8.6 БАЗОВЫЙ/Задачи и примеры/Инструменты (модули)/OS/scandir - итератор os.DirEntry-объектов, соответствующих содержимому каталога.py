""" scandir - итератор os.DirEntry-объектов,
    соответствующих содержимому каталога
"""
import os

# Создается объект-итератор,
# генерирующий экземпляры класса DirEntry.
# Каждый DirEntry соответствует
# вложенному в указанный каталог элементу.
snap = os.scandir('/home/pl/snap')
print(snap)

# Экземпляры DirEntry имеют свойства и методы,
# позволяющие получить системные
# сведения о файле или каталоге.
for i in snap:
    print(i.name, i.path, i.is_dir())
# <posix.ScandirIterator object at 0x7fef2e2a4cf0>
# inkscape /home/pl/snap/inkscape True
# gimp /home/pl/snap/gimp True
# atom /home/pl/snap/atom True
