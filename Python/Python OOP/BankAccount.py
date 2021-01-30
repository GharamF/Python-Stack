class BankAccount:    

    def __init__(self, int_rate, balance):
        self.int_rate=0
        self.balance =0
    
    def make_deposits(self, amount):
        self.balance=self.balance+amount
        return self

    def make_withdrawal(self, amount):
        if(self.balance>amount):
            self.balance=self.balance-amount
        elif (self.balance<amount):
            print("Insufficient funds: Charging a $5 fee")
            self.int_rate=+5
        return self
 
    def display_account_info(self):
        print ("Balance: $", self.balance)
        return self
    
    def yield_interest(self):
        if (self.balance>0):
            self.balance=self.balance*self.int_rate
        return self


Account1 = BankAccount(0 , 0)
Account2 = BankAccount(0 , 0)

Account1.make_deposits(200).make_deposits(20).make_deposits(20).make_withdrawal(250).yield_interest().display_account_info()
Account2.make_deposits(400).make_deposits(20).make_withdrawal(200).make_withdrawal(100).make_withdrawal(100).make_withdrawal(10).display_account_info()