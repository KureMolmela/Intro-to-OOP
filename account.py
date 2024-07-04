class Account:
    def __init__(self):
        self.balance = 10000
        self.__interest_rate = 5
        self.__id_number = 'DG57895'
#        print("Starting balance: ", self.balance)

    def set_id_number(self, new_id_number):
        self.__id_number = new_id_number

    def get_interest_rate(self):
        return self.__interest_rate

    def deposit(self, amount):
        self.balance = amount + self.balance
        print("New balance: ", self.balance)

    def withdrawal(self, amount):
        self.balance = self.balance - amount
        print("Withdrawal balance is: ", self.balance)
