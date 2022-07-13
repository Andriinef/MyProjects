"""join(iterable) - соединение строк из итерируемого объекта
"""
a = ['1', '2', '3']
# Метод join() возвращает строку,
# представляющую собой соединение
# строк из итерируемого объекта.
# Разделителем между элементами
# является строка, к которой
# применяется метод.
print(' '.join(a))

b = ('one', 'two', 'three')
print(' < '.join(b))

c = [1, 2, 3]
# Если в итерируемом объекте есть
# нестроковые значения, будет
# возбуждено исключение TypeError.
print(' '.join(c))
# 1 2 3
# one < two < three
# Traceback (most recent call last):
#   File "code.py", line 8, in <module>
#     print(' '.join(c))
# TypeError: sequence item 0: expected str instance, int found
