# Ahutor: juangzj
class User:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password

    def is_password_correct(self, name_entered, password_entered):
        if name_entered == self.__name:
            if password_entered == self.__password:
                print("The password is correct")
            else:
                print("Wrong password ")
        else:
            print("name does'nt exist ")


user01 = User("juan", "goyes")

user01.is_password_correct("jose", "zambrano")

user01.is_password_correct("juan", "zambrano")

user01.is_password_correct("juan", "goyes")
