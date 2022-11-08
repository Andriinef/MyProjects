""" remove, rmdir, removedirs - удаление файлов и каталогов
"""
import os

print(os.listdir())
print(os.listdir("folder"))
print(os.listdir("imgs"))

try:
    # Функция rmdir() удаляет пустой каталог,
    # иначе выбрасывает исключение OSError.
    os.rmdir("folder")
except OSError:
    print("Directory not empty")
    # С помощью функции remove()
    # можно удалить файл.
    os.remove("folder/text.txt")
    os.rmdir("folder")

# removedirs() удаляет дерево каталогов,
# начиная с вложенного каталога.
# В примере сначала удаляется 'lands',
# если пуст, затем 'imgs',
# если пуст. Иначе OSError.
os.removedirs("imgs/lands")

print(os.listdir())
# ['imgs', 'folder']
# ['text.txt']
# ['lands']
# Directory not empty
# []
