from account import Account

# key features
# interest rate 4%
# charge of 5.5% for withdrawing

class Savings(Account):

    def __init__(self, account_number, branch):
        super().__init__(account_number, branch)

    def apply_interest(self):
        super().apply_interest(0.04)

#polymorphism
    def withdraw(self, amount):
        self.balance = self.balance - amount*1.055
        return round(self.balance, 2)
