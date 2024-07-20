# Hiding implementation details of class and show essential things to user

class Car:
    def __init__(self):
        self.start()
    
    def start(self):
        print("Car Started !")
 
car1 = Car() # you just created object, how it got started you don't know
print()

# Encapsulation --> wrapping data and functions into a single unit(object)

""" Q: Create a class Account with 2 attributes, balance and account no.
Create methods for debit, credit and printing balance """

class Account:
    def __init__(self, accountNo, balance):
        self.accountNo = accountNo
        self.balance = balance
        print("Account Created")
    def debit(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(amount, "Debited Successfuly")
        else:
            print("Insufficient Balance to debit !")
    def credit(self, amount):
        self.balance += amount
        print(amount, "Credited Successfuly")
        
    def getBalance(self):
        return self.balance
        
account = Account(6969, 500)
print("Current Balance:", account.getBalance())
account.debit(100)
account.credit(200)
print("Updated Balance:", account.getBalance())