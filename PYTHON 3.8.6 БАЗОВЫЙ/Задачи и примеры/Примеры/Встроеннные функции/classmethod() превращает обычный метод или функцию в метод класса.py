""" classmethod() превращает обычный метод
    или функцию в метод класса
"""


# Класс с обычными методами, которые в
# качестве первого аргумента
# получают объект-экземпляр.
# Метод класса объявляется с декоратором
# @classmethod и в качестве первого аргумента
# получает объект-класс.
# В данном классе методов класса нет.
class A:
    w = "Class Word"

    def __init__(self, word):
        self.w = word

    def print_word(self):
        print(self.w)


# Создаём объект-экземпляр
a = A("Instance Word")
# Вызываем метод, куда в качестве
# первого аргумента передаётся экземпляр
a.print_word()  # Instance Word

# Нельзя обычный метод вызывать через имя класса.
# В этом случае в функцию первым аргументом
# не передаётся объект-класс.
# A.print_word() - ERROR

# Даже если класс не содержит методов класса,
# мы можем их создать с помощью функции classmethod()
A.static_print_word = classmethod(A.print_word)
A.static_print_word()  # Class Word


# Если бы был создан одноимённый метод,
# он заменил бы обычный метод.
# При его вызове через экземпляр a.print_word()
# первым аргументом передавался бы
# не объект-экземпляр, а объект-класс.


def just_func(cls):
    print(cls)
    if hasattr(cls, 'w'):
        print(cls.w)


# В методы класса можно превращать
# обычные функции
A.just_func = classmethod(just_func)
A.just_func()  # <class '__main__.A'>
# Class Word

just_func("Test")  # Test
# Instance Word
# Class Word
# <class '__main__.A'>
# Class Word
# Test
