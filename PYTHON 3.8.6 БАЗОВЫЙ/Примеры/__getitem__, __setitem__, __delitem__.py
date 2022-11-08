class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Index...")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Index int and >0")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Index int and >0")
        del self.marks[key]


s1 = Student("Andrii", [5, 5, 3, 2, 5, 2])
del s1[5]
print(s1.marks)
s1[5] = 4
print(s1.marks)
