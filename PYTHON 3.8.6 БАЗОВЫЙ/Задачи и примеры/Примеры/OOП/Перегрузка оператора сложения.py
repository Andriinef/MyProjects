""" Перегрузка оператора сложения
"""


class Animal:
    def __init__(self, species):
        self.species = species

    def __add__(self, another):
        # Из полей "родителей" создаётся имя гибрида
        # и присваивается переменной hybrid.
        hybrid = Animal.__hybrid_name(
            self.species, another.species)
        # Создаётся экземпляр Animal.
        # Метод возвращает этот экземпляр.
        return Animal(hybrid)

    # Имеет смысл объявить метод статичным,
    # т. к. в нем не используется self.
    @staticmethod
    # Двойное подчеркивание говорит, что
    # метод предназначен для использования
    # внутри класса. Метод
    # не следует вызывать за пределами класса.
    def __hybrid_name(first, second):
        ln = len(first)
        # берем начало первой строки
        s1 = first[:(ln // 2 + 1)]
        ln = len(second)
        # берем конец второй строки
        s2 = second[(ln // 2):]
        # соединяем
        return s1 + s2


a1 = Animal("cat")
a2 = Animal("dog")

# Для объекта a1 (self)
# вызывается метод __add__().
# Объект a2 передаётся в __add__() в качестве
# второго аргумента (another).
# В данном случае метод __add__() возвращает
# объект того же класса (Animal).
# Этот объект присваивается
# переменной a3.
a3 = a1 + a2
print(a3.species)

b1 = Animal("lion")
b2 = Animal("monkey")
b3 = b1 + b2
print(b3.species)

ab = a3 + b3
print(ab.species)

ba = b3 + a3
print(ba.species)
# caog
# liokey
# caokey
# liokog
