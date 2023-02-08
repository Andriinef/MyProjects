from dataclasses import dataclass


@dataclass
class Base:
    a: int

    def print_a(self, multiplier=None, square=False):
        if square and not multiplier:
            print(self.a**2)
        elif not square and multiplier:
            print(self.a * multiplier)
        elif square and multiplier:
            print((self.a**2) * multiplier)
        else:
            print(self.a)


if __name__ == "__main__":
    base = Base(4)
    base.print_a(square=True)
