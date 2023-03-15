class Account:

# key features
# display account details, account number and branch
# starting balance £100
# check balance
# withdraw
# deposit

    def __init__(self, account_number, branch):
        self._account_number = account_number
        self._branch = branch
        self.balance = 100

    def account_details(self):
        print("Account number: "+ self._account_number + ", Branch: " + self._branch + ".")

    def check_balance(self):
        print("Balance: £" + str(format(self.balance, ".2f")))

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
            self.balance = self.balance - amount
            return self.balance


    def apply_interest(self, rate):
        self.balance = self.balance*(1 + rate)
        return self.balance

