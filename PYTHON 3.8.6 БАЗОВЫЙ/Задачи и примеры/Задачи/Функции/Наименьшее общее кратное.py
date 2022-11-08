""" Наименьшее общее кратное
    Напишите функцию,
    которая возвращает наименьшее общее
    кратное двух переданных в нее чисел.
"""


# Наименьшее общее кратное двух чисел -
# это наименьшее число,
# которое делится нацело на оба заданных числа.


def lcm(a, b):
    # Произведение всегда кратно
    # любому из своих множителей.
    m = a * b
    # Однако оно может быть
    # не наименьшим общим кратным.

    # поиск наибольшего общего делителя
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    # Наименьшее общее кратное вычисляется
    # с помощью деления произведения чисел
    # на их наибольший общий делитель.
    # Здесь используется целочисленное деление
    # только потому, что Python
    # при обычном делении (/)
    # всегда возвращает тип float.
    return m // (a + b)


x = int(input("a="))
y = int(input("b="))
print("LCM:", lcm(x, y))
# a=14
# b=6
# LCM: 42
