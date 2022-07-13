""" bool() - преобразование к булевому типу
"""

# Все числа - True, кроме нуля
print(bool(15))  # True
print(bool(0))  # False

# Пустая строка - False
print(bool("hello"))  # True
print(bool(""))  # False

# Пустая последовательность - False
print(bool([1, 2, 3]))  # True
print(bool([]))  # False
