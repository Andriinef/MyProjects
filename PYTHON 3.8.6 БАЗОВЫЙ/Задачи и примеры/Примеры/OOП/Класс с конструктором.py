""" Класс с конструктором
"""


class Person:
    # В Python __init__ - это имя конструктора класса.
    # Конструктор - метод, который автоматически вызывается
    # в момент создания экземпляра класса.
    def __init__(self, person_name, person_surname):
        self.name = person_name
        self.surname = person_surname

    def about(self):
        return self.name + ' ' + self.surname


# Список, в котором будут храниться
# несколько экземпляров класса.
men = []

for i in range(5):
    one = input("Enter person: ")
    one = one.split()

    # Создаётся объект. В конструктор передаются две строки.
    human = Person(one[0], one[1])

    # экземпляр добавляется в список объектов
    men.append(human)

# перебираются объекты списка
for i in men:
    # для каждого объекта вызывается метод его класса
    print(i.about())
# Enter person: Alan Key
# Enter person: Sam Tree
# Enter person: Tom House
# Enter person: Ben Jam
# Enter person: Bob Cloud
# Alan Key
# Sam Tree
# Tom House
# Ben Jam
# Bob Cloud
