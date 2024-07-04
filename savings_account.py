from account import Account

class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)

    def withdrawal(self, amount):
        if amount < 2000:
            super().withdrawal(amount)
        else:
            print("Amount exceeds withdrawal limit", self.__interest_rate)

# savings = SavingsAccount()
# savings.withdrawal(1000)