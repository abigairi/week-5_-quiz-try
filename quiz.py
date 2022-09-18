class BankAccount:
    def __init__(self,account_number,balance,name,type):
        self.no = account_number
        self.balance = balance
        self.name = name
        self.type = type

def __repr__(self):
    return f"account_number: {self.no} \n balance: {self.balance} \n name: {self.name} \ \n type : {self.type }"
bank_account=BankAccount("43526772872",400000,"Abby a/c","Tembo account")
print(f"My bankaccount is {bank_account.no}\n balance is {bank_account.balance}\n account name is {bank_account.name}\n account type is {bank_account.type}")

    

 
class Bank:
    def __init__(self,name,account):
        self.bname=name
        self.account=account

def __init__(self):
    return f"name: {self.bname} \n account: {self.account}"
bank=Bank("NBC", "3243536742879")
print(f"Bank name is {bank.bname}\n account name:{bank.account}")


class Customer:
    def __init__(self, name,account):
        self.name=name
        self.account=account 

def __repr__(self):
    return f" <{self.name} {self.account}>"
customer=Customer("Abby a/c", 34262627777777774)
print(f"Enter customer name {customer.name}\n a/name is {customer.account}")


class Transaction: 
    def __init__(self,account, amount, type):
        self.account=account
        self.amount=amount
        self.type=type
        self.deposit = self.create_deposit()

        def __repr__(self):
         return f"account: {self.account} \n amount: {self.amount} \n type: {self.type} "
    
    
    def create_deposit(self, amount):
            self.amount += amount
            self.balance= self.balance + self.amount
    def withdraw(self, amount):
            self.balance -= amount
            print("Current amount balance",self.balance)
            
    def check_balance(self):
            print("Available balance",self.balance)
















            
            
    
           

            
            
            



