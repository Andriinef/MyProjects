""" Ошибка деления на ноль
"""

a = b = ""

# Цикл завершится только тогда,
# когда обе переменные будут содержать
# целые числа.
while type(a) != int or type(b) != int:
    a = input()
    b = input()
    try:
        a = int(a)
        b = int(b)
    # Перехватывается исключение, которое
    # генерируется, когда значение a или b
    # нельзя преобразовать к целому числу.
    except ValueError:
        print("Input integers.")

# пытаемся выполнить деление
try:
    # Если b = 0, будет сгенерировано
    # исключение ZeroDivisionError.
    c = a / b
except ZeroDivisionError:
    print("Cannot be divided by zero.")
# Ветка 'else' сработает,
# если не сработает 'except'.
else:
    print(c)
# hello
# 10
# Input integers.
# 178
# 0
# Cannot be divided by zero.
