""" getsize - размер файла в байтах
"""
from os.path import getsize

a = "/home/pl/test.html"
b = "/home/pl/flag.png"

# возвращает размер (целое число)
# файла в байтах
sa = getsize(a)
sb = getsize(b)

print(sa, "bytes")
print(sb, "bytes")
print(round(sb / 1024), "kilobytes")

print(sa > sb)
# 1798 bytes
# 11039 bytes
# 11 kilobytes
# False
