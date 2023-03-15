from account import Account

account1 = Account("123", "Wakefield")
account1.check_balance()
print(account1.deposit(40))
account1.check_balance()

account1.withdraw(90)
account1.check_balance()
account1.withdraw(10)

account1.apply_interest(0.03)
account1.check_balance()

from current import Current

current1 = Current("345", "Leeds")
current1.check_balance()
current1.apply_interest()
current1.check_balance()
current1.withdraw(40)
current1.check_balance()
current1.withdraw(65)

from credit import Credit
credit1 = Credit("987", "Huddersfield")
credit1.check_balance()
credit1.withdraw(170)
credit1.check_balance()
credit1.deposit(120)
credit1.check_balance()
credit1.apply_interest()
credit1.check_balance()
credit1.withdraw(400)
credit1.check_balance()
credit1.withdraw(160)
credit1.account_details()

from savings import Savings
savings1 = Savings("567", "Pontefract")
savings1.apply_interest()
savings1.check_balance()
savings1.withdraw(40)
savings1.check_balance()

