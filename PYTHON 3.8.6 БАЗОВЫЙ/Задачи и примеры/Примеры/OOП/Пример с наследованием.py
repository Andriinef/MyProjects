""" Пример с наследованием
"""


# родительский класс
class Block:
    def __init__(self, width, length, height):
        self.w = width
        self.ln = length
        self.h = height

    def volume(self):
        return self.w * self.ln * self.h


# дочерний класс от Block
class ColorBlock(Block):

    def __init__(self, width, length, height, color):
        # Вызывается конструктор родительского класса.
        # Там будут созданы три поля объекта.
        Block.__init__(self, width, length, height)

        # четвёртое поле создаётся в дочернем классе
        self.c = color


# дочерний класс от Block
class BorderBlock(Block):
    border = 1

    # переопределяется метод родительского класса
    def volume(self):
        w = self.w + BorderBlock.border
        ln = self.ln + BorderBlock.border
        h = self.h + BorderBlock.border
        return w * ln * h


# будет вызван конструктор дочернего класса
block1 = ColorBlock(3, 2, 0.5, "red")

# будет вызван конструктор родительского класса
block2 = BorderBlock(1, 1, 1)

# будет вызван метод родительского класса
print(block1.volume())

# будет вызван метод дочернего класса
print(block2.volume())
# 3.0
# 8
