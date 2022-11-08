class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Seconds Error")
        self.seconds = seconds % self.__DAY

    def __verify_data(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Error... int, Clock")
        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):  # __ne__
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):  # __gt__ self.seconds > sc
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __le__(self, other):  # __ge__ self.seconds => sc
        sc = self.__verify_data(other)
        return self.seconds <= sc


c1 = Clock(1000)
c2 = Clock(1000)
print(c1 == c2)
print(c1 < c2)
