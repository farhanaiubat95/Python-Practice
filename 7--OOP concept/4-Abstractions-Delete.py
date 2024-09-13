#Abstraction
#Hiding the implementation details of a class and only showing the essentional features to the user.
class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
        print("Account Number : ",self.account_no)
        print("Present Balance : ",self.balance)
    
    def debit(self,amount):
        self.balance-=amount
        print("\nTk",amount,"was debited..")
        print("Total Balance = ",self.get_balance())

    def cradit(self,amount):
        self.balance+=amount
        print("\nTk",amount,"was credited..")
        print("Total Balance = ",self.get_balance())

    def get_balance(self):
        return self.balance

a1=Account(20000,1230)
a1.debit(1000)
a1.cradit(600)



#==Delete
print()
class Car:
    def __init__(self,price):
        self.price=price
        print("Car Price : ",self.price)

c1=Car(100)
print(c1.price)
del c1.price
print(c1)
print(c1.price)


    