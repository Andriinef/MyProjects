""" replace - замена подстроки в строке
"""
origin = "fox, box, chair, lamp, desk, box"

# Метод replace возвращает копию строки,
# в которой все вхождения старой подстроки
# заменены на новую.
replaced_all = origin.replace('box', 'cube')

# Если указан третий аргумент, произойдет
# только заданное число замен с начала строки.
replaced_1 = origin.replace('box', 'cube', 1)

print(origin)
print(replaced_all)
print(replaced_1)
# fox, box, chair, lamp, desk, box
# fox, cube, chair, lamp, desk, cube
# fox, cube, chair, lamp, desk, box
