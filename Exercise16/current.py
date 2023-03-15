from account import Account

# key features
# interest rate of 1%
# does not allow overdraft

class Current(Account):

    def __init__(self, account_number, branch):
        super().__init__(account_number, branch)
        
    def apply_interest(self):
        super().apply_interest(0.01)

    def withdraw(self, amount):
        if self.balance > amount:
            super().withdraw(amount)
        else:
            print("Insufficient funds.")
