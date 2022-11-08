""" lower, upper, swapcase, capitalize,
    title - изменение регистра букв
"""
a = "HELLO world"
print(a, "- origin")
# буквы приводятся к нижнему регистру
print(a.lower(), "- lower")
# к верхнему регистру
print(a.upper(), "- upper")
# регистр букв меняется на обратный
print(a.swapcase(), "- swap.")
# Первая буква приводится к верхнему регистру,
# остальные - к нижнему
print(a.capitalize(), "- cap.")
# Первая буква каждого слова
# приводится к верхнему регистру
print(a.title(), "- title")
# HELLO world - origin
# hello world - lower
# HELLO WORLD - upper
# hello WORLD - swap.
# Hello world - cap.
# Hello World - title
