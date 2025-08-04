# Author: juangzj


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Not enought balacne")

    def get_balance(self):
        return self.__balance


# Bank acount
account = BankAccount(100)

# deposit
account.deposit(50)

# get balance
balance01 = account.get_balance()

print(f"Balance is: {balance01} $")


# withdraw 01
account.withdraw(150)

# balance 02
balance02 = account.get_balance()

print(f" now, you have {balance02} $")

# withdraw 02
account.withdraw(100)

# balance 03
balance03 = account.get_balance()
