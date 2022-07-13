""" get(key) возвращает значение по ключу
"""
d = {'a': 1, 'b': 4, 'c': 2}

# Ключ 'b' есть в словаре.
# Возвращается его значение.
print(d.get('b'))  # 4
# Ключа 'e' нет в словаре.
# Возвращется None
print(d.get('e'))  # None
# None можно заменить на любое
# другое значение по умолчанию.
print(d.get('e', 0))  # 0
# Ключ 'c' есть в словаре.
# Поэтому значение по умолчанию
# не используется.
print(d.get('c', 0))  # 2
# 4
# None
# 0
# 2
