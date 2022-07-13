""" Класс с одним свойством и одним методом
"""


# создаётся класс под именем A
class A:
    # поле, или свойство, класса
    class_field = 10

    # метод класса
    # self - объект, к которому применяется метод
    def __init__(self, value):
        # создаётся свойство объекта
        self.obj_field = A.class_field + value
        # self.field - свойство объекта
        # CLASS.field - свойство класса

    def method(self):
        return self.obj_field


# создаются два объекта
# В первом случае аргументу value
# присваивается значение 3, во втором - 100.
a1 = A(3)
a2 = A(100)

# Для каждого объекта вызывается метод.
a1.method()
a2.method()

# значения полей объектов
print(a1.obj_field)
print(a2.obj_field)

# значение поля класса
print(A.class_field)
# 13
# 110
# 10
