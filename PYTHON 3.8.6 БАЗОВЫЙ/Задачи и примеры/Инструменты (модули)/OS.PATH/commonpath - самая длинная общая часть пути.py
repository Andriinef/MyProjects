""" commonpath - самая длинная общая часть пути
"""
import os.path

a = []
a.append("/home/user/f1.png")
a.append("/home/user/pic/land.gif")
a.append("/home/user/books")

# Возвращает самую длинную общую часть
# пути всех адресов последовательности.
c = os.path.commonpath(a)
print(c)

a.append("/folder/f2.txt")
c = os.path.commonpath(a)
print(c)

# Возбуждает ValueError, если содержатся как абсолютные,
# так и относительные адреса, также в случае
# разных дисков, или если последовательность пуста.
a.append("user/db.sql")
try:
    c = os.path.commonpath(a)
    print(c)
except ValueError:
    print("Can't mix absolute and relative paths")
# /home/user
# /
# Can't mix absolute and relative paths
