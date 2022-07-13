""" delattr() удаляет атрибут объекта
"""


class A:
    p0 = 0

    def __init__(self):
        self.p1 = 44
        self.p2 = 'Yellow'


a = A()
# Просмотр атрибутов экземпляра,
# в том числе унаследованных от класса
# Функция dir() возвращает все свойства 
# и методы указанного объекта без значений
print([i for i in dir(a) if i[0] != '_'])  # ['p0', 'p1', 'p2']
# Если использовать a.__dict__,
# p0 мы не увидим

delattr(a, 'p2')
# Это эквивалентно del a.p2

print([i for i in dir(a) if i[0] != '_'])  # ['p0', 'p1']

# Нельзя удалить атрибут,
# который наследуется от класса
# delattr(a, 'p0') - AttributeError!
# Однако можно удалить атрибут класса
delattr(A, 'p0')
print([i for i in dir(a) if i[0] != '_'])  # ['p1']
# ['p0', 'p1', 'p2']
# ['p0', 'p1']
# ['p1']
