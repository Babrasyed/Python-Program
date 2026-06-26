class BankAccountDetail:
    def __init__(self,name,balance):
        self.__name=name
        self.__balance=balance
   
    def Deposite(self,add_amount):
        if add_amount <=0:
            print("invalid amount")
        else:
            self.__balance = self.__balance + add_amount
    def Withdraw(self,reduce_amount):
        self.balance = self.balance-reduce_amount
    def Check_balance(self):
        print(self.balance)
    
        
# reduce_amount=int(input("enter withdrawn amount:"))
# add_amount = int(input("enter amount added amount:"))

# add_amount = int(input("enter amount added amount:"))
client= BankAccountDetail("CEO Babra", 1000)
# client.Deposite(60)
# client.Withdraw(30)
# client.Check_balance()
client.__name="biya"
print(client.__name)
print(client.__balance)







#property

class BankAccountDetail:
    def __init__(self,name,balance):
        self.__name=name
        self.__balance=balance
   
    def Deposite(self,add_amount):
        if add_amount <=0:
            print("invalid amount")
        else:
            self.__balance = self.__balance + add_amount
    def Withdraw(self,reduce_amount):
        self.balance = self.balance-reduce_amount
    def Check_balance(self):
        print(self.balance)
    
        
# reduce_amount=int(input("enter withdrawn amount:"))
# add_amount = int(input("enter amount added amount:"))

# add_amount = int(input("enter amount added amount:"))
client= BankAccountDetail("CEO Babra", 1000)
client.__name="biya"

# client.Deposite(60)
# client.Withdraw(30)
# client.Check_balance()
print(client.__balance) #Accessmodifier .__
print(client.__name)











    