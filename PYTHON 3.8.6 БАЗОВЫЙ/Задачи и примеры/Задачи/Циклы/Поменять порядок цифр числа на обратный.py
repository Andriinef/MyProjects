""" Поменять порядок цифр числа на обратный
    Используя арифметические действия,
    поменять порядок цифр числа на обратный.
"""

n1 = int(input("An integer: "))

# новое число
n2 = 0

while n1 > 0:

    # находим остаток,
    # т. е. последнюю цифру числа
    digit = n1 % 10

    # делим нацело, т. е
    # удаляем последнюю цифру числа
    n1 = n1 // 10

    # увеличиваем разрядность
    # второго числа
    n2 = n2 * 10

    # добавляем очередную цифру
    n2 = n2 + digit

print("Inverse number:", n2)
# An integer: 1023
# Inverse number: 3201
