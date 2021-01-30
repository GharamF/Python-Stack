class user:
    def __init__(self, name, email_address ,account_balance):
        self.name = name		
        self.email = email_address		
        self.account_balance = account_balance

    def make_withdrawal(self, amount):
        self.account_balance=self.account_balance-amount
        return self

    def make_deposits(self, amount):
        self.account_balance=self.account_balance+amount
        return self
        

    def display_user_balance(self):
        print ("user ", self.name , "Balance: $", self.account_balance)
        return self





user1 = user("John", "John@gmail.com" , 800)
user2 = user("tony", "tony12@gmail.com" ,3000 )
user3 = user("sara", "sara22@gmail.com" ,1000 )

#Chaining Methods

user1.make_deposits(300).make_deposits(100).make_deposits(50).make_withdrawal(400)
user1.display_user_balance()

#output = user  John Balance: $ 850


user2.make_deposits(200).make_deposits(1000).make_withdrawal(1000).make_withdrawal(100)
user2.display_user_balance()
#user  tony Balance: $ 3100


user3.make_deposits(1000).make_withdrawal(1500).make_withdrawal(500)
user3.display_user_balance()
#user  sara Balance: $ 0
