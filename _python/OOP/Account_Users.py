class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account= BankAccount(int_rate=2, balance=0)
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount)	# the specific user's account increases by the amount of the value received
        return self 
    def make_withdrawal(self, amount):# takes an argument that is the amount of the deposit
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self


class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount

        return self
		# your code here
    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(self.balance)
        return self
		# your code here
    def yield_interest(self):
        print(self.int_rate)
        if(self.balance>0):
            self.balance+=(self.int_rate/100)*self.balance
        return self


User1=User("User1","user1.gmail.com")
User1.make_deposit(100).make_withdrawal(200).display_user_balance()



