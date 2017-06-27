""" bank account thing """
class BankAccount():
    """ this is the bank account class """
    def __init__(self, kind):
        self.kind = kind
        self.balance = 0
        self.overdraft_fees = 0

    def deposit(self, amount):
        """ this is a method """
        self.balance += amount

    def withdraw(self, amount):
        """ this is a method """
        self.balance -= amount
        if self.balance < 0:
            self.overdraft_fees += 20
        return self.balance

SAVINGS = BankAccount(100)
CHECKING = BankAccount(25)

SAVINGS.deposit(5000)
CHECKING.deposit(2000)

SAVINGS.withdraw(1500)

print(SAVINGS.balance, " dollars left in Savings")
print(CHECKING.balance, " is your current balance in your checking account")
