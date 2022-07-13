""" is...? - isdigit, isalpha, isidentifier,
    islower, isupper, istitle, isprintable, isspace
"""
print('__ isdigit:')
# Все ли символы являются цифрами
print('567', '567'.isdigit())
print('5da', '5da'.isdigit())

print('__ isalpha:')
# Все ли символы являются буквами
print('dabc', 'dabc'.isalpha())
print('da bc', 'da bc'.isalpha())
print('5da', '5da'.isalpha())

print('__ isidentifier:')
# Может ли строка быть идентификатором
print('apple5', 'apple5'.isidentifier())
print('a 56', 'a 56'.isidentifier())

print('__ islower:')
# Буквы в строке строчные?
print('hello', 'hello'.islower())
print('hello!', 'hello!'.islower())
print('Hello', 'Hello'.islower())

print('__ isupper:')
# Буквы в строке прописные?
print('HI!', 'HI!'.isupper())
print('Hi!', 'Hi!'.isupper())

print('__ istitle:')
# Каждое слово начинается с прописной буквы?
print('Hi World', 'Hi World'.istitle())
print('Hi world', 'Hi world'.istitle())

print('__ isprintable:')
# В строке нет непечатаемых символов?
print('a   b', 'a   b'.isprintable())
print('a\tb', 'a\tb'.isprintable())

print('__ isspace:')
# Строка содержит только пробельные символы?
print(' \t ', ' \t '.isspace())
print('a b', 'a b'.isspace())
# __ isdigit:
# 567 True
# 5da False
# __ isalpha:
# dabc True
# da bc False
# 5da False
# __ isidentifier:
# apple5 True
# a 56 False
# __ islower:
# hello True
# hello! True
# Hello False
# __ isupper:
# HI! True
# Hi! False
# __ istitle:
# Hi World True
# Hi world False
# __ isprintable:
# a   b True
# a	b False
# __ isspace:
# True
# a b False
