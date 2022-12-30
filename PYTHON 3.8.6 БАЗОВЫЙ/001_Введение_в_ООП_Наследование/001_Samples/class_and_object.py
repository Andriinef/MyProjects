from dataclasses import dataclass


@dataclass
class Human:
    age: int
    name: str
    gender: str

    def get_name(self):
        return self.name

    def get_age_and_name(self):
        return self.age, self.get_name(), self.gender


if __name__ == "__main__":
    human_1 = Human(age=25, name="John", gender="male")
    print(human_1.get_age_and_name())
