class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    


    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self 
    def make_withdrawal(self, amount):# takes an argument that is the amount of the deposit
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)
        return self
    def transfer_money(self,toWhom,amount):
        self.make_withdrawal(amount)
        toWhom.make_deposit(amount)
        return self
        

#Create 3 instances of the User class
User1=User("User1","user1.gmail.com")
User2=User("User2","user2.gmail.com")
User3=User("User3","user3.gmail.com")
#User1 makes 3 deposits and 1 withdrawal
User1.make_deposit(500).make_deposit(500).make_deposit(500).make_withdrawal(300).display_user_balance()
#User2 makes 2 deposits and 2 withdrawals
User2.make_deposit(500).make_deposit(500).make_withdrawal(500).make_withdrawal(300).display_user_balance()
#User3 makes 1 deposits and 3 withdrawals
User3.make_deposit(2000).make_withdrawal(500).make_withdrawal(500).make_withdrawal(300).display_user_balance()
#Transfer Money from User1 to User 3
User1.transfer_money(User3,200).display_user_balance()
User3.display_user_balance()










            
        




    


