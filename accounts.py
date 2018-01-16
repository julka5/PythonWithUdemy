import datetime
import pytz


class Account:
    """ Simple account class with balance"""
    @staticmethod
    def _current_time():  # static method
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = []
        print("Account created for " + self._name)
        if balance > 0:
            self._transaction_list.append((Account._current_time(), balance))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))  # tuple

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))  # tuple
        else:
            print("You don't have that much money")
        self.show_balance()

    def show_balance(self):
        print("balance is {}".format(self.__balance))

    def show_transactions(self):

        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":

    julia = Account("Julia", 0)
    julia.show_balance()

    julia.deposit(100)

    julia.withdraw(50)

    julia.show_transactions()

    john = Account("John", 500)
    john.withdraw(300)
    john.deposit(150)
    john.show_transactions()
    john.show_balance()
    john.__balance = 1000  # python mangles the name with two underscores
    # using class name( see below), that's why the balance is not changed
    # have to use kicia._Account__balance = 10000
    # works for names with two underscores at the beginning and less than two on the end
    print(john.__dict__)

