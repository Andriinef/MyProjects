""" issubclass() - является ли класс подклассом другого
"""


class A:
    pass


class B(A):
    pass


class D(B):
    pass


class C:
    pass


# issubclass проверяет, является ли
# один класс подклассом другого
print(issubclass(B, A))  # True
print(issubclass(D, A))  # True
print(issubclass(C, A))  # False

# Класс считается подклассом самого себя
print(issubclass(C, C))  # True

# Второй аргумент может быть
# кортежем классов.
# Чтобы функция вернула истину,
# достаточно одного соответствия
print(issubclass(B, (A, C)))  # True

# Также можно проверять наследование
# встроенных классов
print(issubclass(list, object))  # True
# True
# True
# False
# True
# True
# True
