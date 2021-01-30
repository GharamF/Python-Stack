class BankAccount:    
    def __init__(self, int_rate, balance):
        self.int_rate=0
        self.balance =0
    
    
class user: 
    def __init__(self, name, email_address ):
        self.name = name		
        self.email = email_address
        self.bankaccount = BankAccount(int_rate= 0, balance=0)

    def make_withdrawal(self, amount):
        if(self.bankaccount.balance>amount):
            self.bankaccount.balance=self.bankaccount.balance-amount
        elif (self.bankaccount.balance<amount):
            print("Insufficient funds: Charging a $5 fee")
            self.bankaccount.int_rate=+5
        return self 

    def make_deposits(self, amount):
        self.bankaccount.balance=self.bankaccount.balance+amount
        return self
        

    def display_user_balance(self):
        print ("user ", self.name , "Balance: $", self.bankaccount.balance)
        return self





user1 = user("John", "John@gmail.com" )
user2 = user("tony", "tony12@gmail.com" )
user3 = user("sara", "sara22@gmail.com" )
user1.make_deposits(30)
user1.make_withdrawal(20)
user1.display_user_balance()