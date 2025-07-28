class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

    def display_info(self):
        print(
            f"The car is: {self.color}, the model is: {self.model}, and it was made in {self.year}"
        )


car_1 = Car("black", "Ford Mustang", 2025)

car_1.display_info()
