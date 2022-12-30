from dataclasses import dataclass


@dataclass
class Human:
    age: int

    def say_hello(self):
        print("Hello, I am {}".format(self.age))


@dataclass
class HumanExtended(Human):
    name: str


    def say_hello(self):
        print(f"Hello, I am {self.name} and I am {self.age}")


if __name__ == "__main__":
    # human = Human(age=35)
    # human.say_hello()
    Human(35).say_hello()
    # human2 = HumanExtended(age=56, name="John")
    # human2.say_hello()
    HumanExtended(56, "John").say_hello()


@dataclass
class A:
    a = 10


@dataclass
class B:
    b = 5


@dataclass
class C(A, B):
    pass


if __name__ == "__main__":
    print(C.a)
    print(C.b)
