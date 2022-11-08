""" Несуществующая переменная
"""
a = 10
b = 105
c = 3.4

# Пользователь должен ввести имя переменной.
var = input("The variable: ")

try:
    # Функция exec() преобразует
    # переданную ей строку в программный код.
    # Например, если var = 'a',
    # то получится print(a).
    exec("print(" + var + ")")

# Если в программе не существует переменной,
# то генерируется исключение NameError.
except NameError:
    print("No such variable")
# The variable: b
# 105
# The variable: table
# No such variable
