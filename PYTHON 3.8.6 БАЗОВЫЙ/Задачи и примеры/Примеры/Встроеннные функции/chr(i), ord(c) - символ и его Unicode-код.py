""" chr(i), ord(c) - символ и его Unicode-код
"""

# chr(i) принимает
# числовой код символа в Unicode,
# возвращает символ
print(chr(97))  # a
print(chr(20049))  # 乑

# ord(c) принимает символ,
# возвращает его номер в Unicode
print(ord('Z'))  # 90
print(ord('乑'))  # 20049
