""" - в момент выполнения
    - при компиляции (до иполнения кода)
"""

try:
    x, y = map(int, input().split())
    # f = open("myfile2.txt")
    res = x / y
except FileNotFoundError as z:
    print(z)
except ZeroDivisionError as d:
    print(d)
except ValueError as z:
    print(z)
except ArithmeticError as z:
    print(z)
except Exception as z:
    print(z)

