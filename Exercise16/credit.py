from account import Account

# key features
# interest rate 0.1%
# will allow overdraft up to £500

class Credit(Account):

    def __init__(self, account_number, branch):
        super().__init__(account_number, branch)

    def apply_interest(self):
        super().apply_interest(0.001)

    def withdraw(self, amount):
        if self.balance - amount >= -500:
            super().withdraw(amount)
        else:
            print("You have received your overdraft limit.")

