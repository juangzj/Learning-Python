# Ahutor: juangzj
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def increase_salary(self, percent):
        if percent > 5:
            self.__salary += self.__salary * (percent / 100)
        else:
            print("Won't increase (less than or equal to 5%)")

    def get_salary(self):
        return self.__salary


emp = Employee(1000)
print(emp.get_salary())  # 1000

emp.increase_salary(4)
print(emp.get_salary())

emp.increase_salary(10)
print(emp.get_salary())
