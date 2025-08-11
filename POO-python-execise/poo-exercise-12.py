from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("The car is moving")


class Bicycle(Vehicle):
    def move(self):
        print("Bicycle is moving")


car01 = Car()
car01.move()

bicycle01 = Bicycle()
bicycle01.move()
