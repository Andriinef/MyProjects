from dataclasses import dataclass


@dataclass
class Student:
    __schoolName = "QWE School"  # атрибут приватного класу

    __name: str  # атрибут приватного екземпляра
    __age: int  # атрибут приватного екземпляра

    def __display(self):  # приватний метод
        return self.__schoolName, self.__name, self.__age


if __name__ == "__main__":
    std = Student("Bill", 18)
    """
    Python выполняет изменение имен частных переменных.
    Каждый элемент с двойным подчеркиванием будет изменен на _object._class__variable.
    Таким образом, к нему все еще можно получить доступ извне класса,
    но от этой практики следует воздержаться.
    """
    print(std._Student__schoolName)
    print(std._Student__name)
    print(std._Student__age)
    print(std._Student__display())
