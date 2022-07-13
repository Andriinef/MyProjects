""" startswith(prefix), endswith(suffix) - начинается ли
    строка с prefix и заканчивается ли на suffix
"""
a = 'onetwothree'
# Метод startswith() проверяет,
# начинается ли строка с указанного
# в качестве аргумента префикса.
print(a.startswith('one'))
print(a.startswith('two'))
# Кроме того проверять можно подстроку.
print(a.startswith('two', 3))

print('--------')

a = '[1, 2, 3]'
# Можно указать кортеж
# возможных префиксов.
print(a.startswith(('[', '(')))

print('--------')

a = 'onetwothree'
# Метод endswith() проверяет,
# заканчивается ли строка
# на указанный суффикс.
print(a.endswith('three'))
# Проверять можно срез.
print(a.endswith('two', 0, 6))
# True
# False
# True
# --------
# True
# --------
# True
# True
