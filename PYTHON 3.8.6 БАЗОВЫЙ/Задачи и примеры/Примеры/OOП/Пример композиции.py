""" Пример композиции
"""


class Planet:
    def __init__(self, name):
        self.name = name


class Star:
    def __init__(self, name, star_type):
        self.name = name
        self.type = star_type


# Объекты, созданные на базе этого класса,
# будут содержать объекты других классов,
# т. е. будут являться составными,
# представлять собой агрегаторы.
class System:
    def __init__(self, star_name, star_type):
        # Создаётся экземпляр класса Star и
        # присваивается полю star экземпляра класса System.
        self.star = Star(star_name, star_type)
        self.planets = []

    def add_planet(self, *name):
        # Создаются экземпляры класса Planet и
        # помещаются в поле planets экземпляра System.
        for i in name:
            self.planets.append(Planet(i))

    # Метод __str__() вызывается,
    # когда объект передаётся в функцию print().
    def __str__(self):
        # формируется строка с данными
        s = self.star.name + ": " + self.star.type
        for i in self.planets:
            s += "\n" + i.name
        # метод должен возвращать строку
        return s


solar_system = System("Sun", "yellow")

# Несколько строк-аргументов в методе
# присваиваются одной переменной name.
solar_system.add_planet("Mercury", "Venus", "Earth")

solar_system.add_planet("Mars", "Jupiter")

print(solar_system)
# Sun: yellow
# Mercury
# Venus
# Earth
# Mars
# Jupiter
