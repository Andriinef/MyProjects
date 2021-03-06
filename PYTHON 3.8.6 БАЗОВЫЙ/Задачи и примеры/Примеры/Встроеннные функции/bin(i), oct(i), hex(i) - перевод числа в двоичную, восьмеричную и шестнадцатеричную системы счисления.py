""" bin(i), oct(i), hex(i) - перевод числа в двоичную,
    восьмеричную и шестнадцатеричную системы счисления
"""
# Десятичное число переводится
# в двоичную систему счисления
print(bin(30))
# в восьмеричную
print(oct(30))
# в шестнадцатеричную
print(hex(30))

# Один из способов избавиться от префиксов
print(format(30, 'b'))
print(format(30, 'o'))
print(format(30, 'x'))
print(format(30, 'X'))
# Один из способов перевода в bin,
# удаление префикса, добавдение нулей
# и перевода в int([object], [основание системы счисления])
a = bin(a)
a = b.lstrip('0b')
a = a.zfill(6)
a = int(a, 2)


# 0b11110
# 0o36
# 0x1e
# 11110
# 36
# 1e
# 1E
