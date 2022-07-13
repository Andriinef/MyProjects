""" Искусственное возбуждение исключения
"""
lst = ['a', 'b', 'c', 'd', 'e', 'f']
letter = input()

# Если буква есть в списке,
if letter in lst:
    # вывести 1.
    print(1)
# Иначе,
else:
    # возбудить исключение ValueError.
    raise ValueError("No such letter")
# s
# Traceback (most recent call last):
#   File "raise.py", line 7, in <module>
#     raise ValueError("No such letter")
# ValueError: No such letter
