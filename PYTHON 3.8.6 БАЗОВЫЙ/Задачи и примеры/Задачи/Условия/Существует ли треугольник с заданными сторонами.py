""" Существует ли треугольник с заданными сторонами?
    Вводятся длины трех отрезков.
    Определить, может ли существовать треугольник с такими сторонами.
"""

print("Длины сторон:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# Треугольник существует только тогда,
# когда сумма любых двух его сторон
# больше третьей стороны.
# В заголовке if сразу проверяются
# три стороны. Каждая из них должна
# быть меньше суммы других.Поэтому
# используется логический оператор AND.
if a+b > c and a+c > b and b+c > a:
    print("Треугольник есть")

# Если хотя бы одна сторона оказывается
# больше суммы других, то треугольник
# из заданных отрезков построить нельзя.
else:
    print("Треугольника нет")

# Примечание. Существует понятие
# вырожденного треугольника. В этом случае
# третья сторона может равняться
# сумме двух других.
# Тогда в условии вместо знака ">"
# следует использовать ">=".
