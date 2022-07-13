""" add, remove, discard, pop, clear
    - добавление и удаление элементов
"""
a = {4, 2, 1, 3}

# Добавляет элемент, если его нет во множестве.
a.add(5)
print(a, 'after add')

# Удаляет элемент из множества.
# Если такого элемента нет,
# будет выброшено исключение KeyError.
a.remove(2)
print(a, 'after remove')

# Удаляет элемент, если он есть во множестве.
a.discard(8)
print(a, 'after discard')

# Удаляет и возвращает случайный элемент.
# Если множество пустое,
# будет возбуждено KeyError.
b = a.pop()
print(b, 'extracted item')
print(a, 'after pop')

# Удаляет из множества все элементы.
a.clear()
print(a, 'after clear')
# {1, 2, 3, 4, 5} after add
# {1, 3, 4, 5} after remove
# {1, 3, 4, 5} after discard
# 1 extracted item
# {3, 4, 5} after pop
# set() after clear
