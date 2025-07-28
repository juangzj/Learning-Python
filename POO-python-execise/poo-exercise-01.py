class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is: {self.name} and I am {self.age} years old")


# creatre an object
person_1 = Person("Juan", "21")

# Call the introduce method
person_1.introduce()
