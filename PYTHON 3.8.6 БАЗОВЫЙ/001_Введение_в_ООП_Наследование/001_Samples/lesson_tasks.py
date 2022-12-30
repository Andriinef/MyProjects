from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    color: str
    volume: float

    def drive_forward(self):
        print("Drive forward")

    def drive_backward(self):
        print("Drive backward")


class Car2(Car):
    def turn_left(self):
        print("Turn left")

    def turn_right(self):
        print("Turn right")


@dataclass
class Airplane:
    model: str

    def get_up(self):
        print("Going up")

    def get_land(self):
        print("Landing")


@dataclass
class FlyingCar(Car2, Airplane):
    pass


if __name__ == "__main__":
    # car = Car2('Audi', 'white', 3.5)
    # fc = FlyingCar(brand="Tesla", color="Black", volume=10, model="F")
    # car.turn_left()
    # car.drive_backward()
    # car.turn_right()
    # car.drive_forward()
    # fc.get_up()
    # fc.drive_forward()
    # fc.turn_left()
    # fc.drive_backward()
    # fc.get_land()
    Car2("Audi", "white", 3.5).drive_forward()
    Car2("Audi", "white", 3.5).drive_backward()
    Car2("Audi", "white", 3.5).turn_left()
    Car2("Audi", "white", 3.5).turn_right()
    FlyingCar(brand="Tesla", color="Black", volume=10, model="F").drive_forward()
    FlyingCar(brand="Tesla", color="Black", volume=10, model="F").drive_backward()
    FlyingCar(brand="Tesla", color="Black", volume=10, model="F").turn_left()
    FlyingCar(brand="Tesla", color="Black", volume=10, model="F").turn_right()
    FlyingCar(brand="Tesla", color="Black", volume=10, model="F").get_up()
    FlyingCar(brand="Tesla", color="Black", volume=10, model="F").get_land()
    FlyingCar("Tesla", "Black", 10, "F").drive_forward()
