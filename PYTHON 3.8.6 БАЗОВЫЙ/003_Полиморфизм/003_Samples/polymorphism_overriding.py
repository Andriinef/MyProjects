from dataclasses import dataclass


@dataclass
class Multiplier:
    a: int

    def print_a(self, x):
        print(self.a * x)


class Exponent(Multiplier):
    def print_a(self, x):
        print(self.a**x)


if __name__ == "__main__":
    Multiplier(5).print_a(2)
    Exponent(5).print_a(2)
