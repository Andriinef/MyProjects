""" Посчитать четные и нечетные цифры числа
    Вводится натуральное число.
    Программа должна определять,
    сколько в этом числе четных цифр, а сколько нечетных.
"""

a = input()
a = int(a)

# количество четных цифр
even = 0

# количество нечетных
odd = 0

# Пока число больше нуля,
while a > 0:

    # если оно четное, значит
    # его последняя цифра четная,
    if a % 2 == 0:
        # увеличиваем счетчик
        # четных цифр,
        even += 1

    # в иных случаях (число не делится
    # нацело на 2) число нечетное,
    else:
        # увеличиваем счетчик
        # нечетных цифр,
        odd += 1

    # избавляемся от последнего
    # разряда числа с помощью деления
    # нацело на 10.
    a = a // 10

print("Even: %d" % even)
print("Odd: %d" % odd)
