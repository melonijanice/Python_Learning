class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        return self
		# your code here
    def withdraw(self, amount):
        self.balance-=amount
        if(self.balance<0):
            print("Insufficient Funds:Charging fee of 5$")
            self.balance-=5
        return self
		# your code here
    def display_account_info(self):
        print(self.balance)
        return self
		# your code here
    def yield_interest(self):
        print(self.int_rate)
        if(self.balance>0):
            self.balance+=(self.int_rate/100)*self.balance
        return self
		# your code here

user1=BankAccount(10,100)
user1.deposit(5000).deposit(10000).deposit(5000).withdraw(10000).display_account_info().yield_interest().display_account_info()
user2=BankAccount(6,1000)
user2.deposit(5000).deposit(1000).withdraw(5000).withdraw(10000).display_account_info().yield_interest().display_account_info()


