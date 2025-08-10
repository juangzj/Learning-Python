# Author: juangzj


class Person:
    def greet(self):
        print("Good Morning")


class Student(Person):
    def study(self):
        print("Studying")


student01 = Student()
student01.greet()
student01.study()
