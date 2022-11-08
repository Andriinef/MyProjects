""" Рассчитать массу, плотность или объём
    Если даны плотность и объём, вычислить массу.
    Если даны масса и плотность, вычислить объём.
    Если же даны масса и объём, вычислить плотность.
"""

result = None

# Пользователь выбирает, что он хочет вычислить:
# массу (m), плотность (d) или объём (v)
flag = input("What to calculate? (m, d, v): ")

# Если выбрана масса, то надо запросить плотность
# и объём. Вычислить массу по формуле m = dv.
if flag == "m":
    # функция float() преобразует строку в
    # вещественное число
    d = float(input("Density: "))
    v = float(input("Volume: "))
    result = d * v  # mass
# Если выбрана плотность, то запрашиваются масса
# и объём. Используется формула d = m/v
elif flag == "d":
    m = float(input("Mass: "))
    v = float(input("Volume: "))
    result = m / v  # density
# Если выбран объём, то считываются масса
# и плотность. Объем находится как v = m/d
elif flag == "v":
    m = float(input("Mass: "))
    d = float(input("Density: "))
    result = m / d  # volume

# Вне зависимости от ветки вычисления
# результат записывается в одну и ту же
# переменную result. Форматированный вывод
# с двумя знаками после запятой
print("%.2f" % result)
