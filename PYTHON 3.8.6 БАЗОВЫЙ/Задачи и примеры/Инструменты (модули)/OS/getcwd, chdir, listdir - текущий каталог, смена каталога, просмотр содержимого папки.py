"""getcwd, chdir, listdir - текущий каталог,
    смена каталога, просмотр содержимого папки
"""
import os

# Модуль os предоставляет множество функций
# для работы с операционной системой,
# причём их поведение, как правило,
# не зависит от ОС, поэтому программы остаются переносимыми

# getcwd() возвращает строку, представляющую
# текущую рабочую директорию.
print(os.getcwd())
# listdir(path) возвращает список,
# содержащий имена элементов в директории,
# заданной через path.
# Значение по умолчанию path -
# текущий каталог.
print(os.listdir())

# chdir(path) изменяет
# текущий рабочий каталог на path.
os.chdir("/home/pl")

print(os.getcwd())
print(os.listdir())

print(os.listdir("/boot/grub"))
# /home/p/EXERCISES/modules/os/dir
# ['getcwd_chdir_listdir.py', 'desc.txt']
# /home/p/test
# ['flag.png', 'WebViewPlusAnother', 'test.html']
# ['fonts', 'grubenv', 'x86_64-efi', 'locale', 'grub.cfg', 'unicode.pf2']
