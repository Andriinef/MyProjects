"""format(...) выполняет операцию форматирования строки
"""
a = "{} {}!"
# Возвращает копию строки,
# в которой каждое поле для замены
# замещено соответствующей
# строкой-аргументом метода.
print(a.format("hello", "world"))
print(a.format("hi", "Ben"))

# Поля для замены содержат
# числовой индекс аргументов.
a = "apple{1}, orange{0}"
print(a.format(333, 888))

# Поля для замены содержат
# имена ключевых аргументов.
a = "a{apple}, o{orange}"
print(a.format(apple=4, orange=1))
print(a.format(orange=1, apple=4))

# Пример вывода вещественного числа
a = "fraction {:.3}"
print(a.format(12 / 7))

# Метод format() имеет множество
# других инструментов форматирования.
a = "{0:b}"
print(a.format(34))
# hello world!
# hi Ben!
# apple888, orange333
# a4, o1
# a4, o1
# fraction 1.71
# 100010
