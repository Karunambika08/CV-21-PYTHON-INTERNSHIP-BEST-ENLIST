#Day 10
#Create a real time scenario for inheritance example Banking concept¶
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
    def display(self):
        print("\n Net Available Balance=",self.balance)

class Deposit(Bank_Account):  #inheritance
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)

class Withdraw(Bank_Account):  #mutiple inheritance
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", self.balance)
        else:
            print("\n Insufficient balance  ")

s = Bank_Account()
p=Deposit()
p.deposit()
q=Withdraw()
q.withdraw()
s.display()
