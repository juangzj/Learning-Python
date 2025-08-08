# Author: juangzj
class Vehicle:
    def star(self):
        print("The car is on")

    def off(self):
        print("The car is off")


class Car(Vehicle):
    def honk(self):
        print("The car is honking")


car01 = Car()

car01.star()
car01.honk()
car01.off()
