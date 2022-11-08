""" enumerate(iterable, start=0) создаёт итератор
    со счётчиком"""

a = ["two", "tree", "four", "five"]

# Функция enumerate() принимает
# итерируемый объект или итератор,
# возвращает итератор, генерирующий кортежи.
# Первый элемент кортежа - номер элемента,
# второй - очередной элемент
# переданного в enumerate() объекта.
e = enumerate(a)
for i in e:
    print(i)

print("-----")

# По умолчанию счётчик элементов начинается с нуля.
# Однако стартовое значение можно задать вручную.
e = enumerate(a, 2)
for i in e:
    print(i)
# (0, 'two')
# (1, 'tree')
# (2, 'four')
# (3, 'five')
# -----
# (2, 'two')
# (3, 'tree')
# (4, 'four')
# (5, 'five')
