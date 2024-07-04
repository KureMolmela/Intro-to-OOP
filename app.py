from account import Account
from savings_account import SavingsAccount
from current_account import CurrentAccount

# iterate between options
print("Select a number to proceed")
print("1: Current")
print("2: Savings")
one = int(input("Enter: "))
if one == 1:
    current = CurrentAccount()
    print("Select a number to proceed")
    print("1: Withdraw")
    print("2: Deposit")
    curr = int(input("Enter: "))
    if curr == 1:
        amount = int(input("Enter Amount: "))
        current.withdrawal(amount)
    elif curr == 2:
        amount = int(input("Enter Amount: "))
        current.deposit(amount)
    else:
        print("Invalid option")
elif one == 2:
    savings = SavingsAccount()
    print("Select a number to proceed")
    print("1: Withdraw")
    print("2: Deposit")
    curr = int(input("Enter: "))
    if curr == 1:
        amount = int(input("Enter Amount: "))
        savings.withdrawal(amount)
    elif curr == 2:
        amount = int(input("Enter Amount: "))
        savings.deposit(amount)
    else:
        print("Invalid option")