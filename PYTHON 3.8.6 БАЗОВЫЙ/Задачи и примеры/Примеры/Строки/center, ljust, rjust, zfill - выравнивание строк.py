""" center, ljust, rjust, zfill - выравнивание строк
"""
a = "hello"
# Исходная строка выравнивается по центру
# в строке длинной width (первый параметр).
print(a.center(10))
print(a.center(10, '*'))
# Строка выравнивается по левому краю
# в строке длинной width.
print(a.ljust(10), 'world')
print(a.ljust(10, '-'))
# Выравнивание по правому краю.
print(a.rjust(10))
print(a.rjust(10, '-'))

# Возвращает копию строки
# слева заполненную символом '0'
# так, чтобы длина строки стала width.
print(a.zfill(9))
print('21'.zfill(5))
print('-21'.zfill(5))
#   hello
# **hello***
# hello      world
# hello-----
#      hello
# -----hello
# 0000hello
# 00021
# -0021
