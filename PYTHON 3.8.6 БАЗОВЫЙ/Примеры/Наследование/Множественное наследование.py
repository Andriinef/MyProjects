class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: sold")


class MixinLog2:
    def __init__(self):
        super().__init__()
        print("init MixinLog2")


class NoteBoor(Goods, MixinLog, MixinLog2):
    pass


n = NoteBoor("Acer", 1.5, 3000)
n.print_info()
n.save_sell_log()
print(NoteBoor.__mro__)       # Наследование
