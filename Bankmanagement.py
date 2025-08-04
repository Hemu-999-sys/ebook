#BankManagement Project

class Account:
    def __init__(self,username,password,balance=0):
        self.username = username
        self.password = password 
        self.balance  = balance

def deposit(self,amount):
    self.balance += amount
    print(f"Deposited {amount}, New balance:  {self.balance}")

def withdraw(self,amount):
    if amount <= self.balance:
        self.balance -= amount
        print(f"Withdrawn  {amount}, New balance:  {self.balance}")
    else:
        print("Insufficient funds!") 

def check_balance(self):
    print(f"Your current balance is:  {self.balance}")

def mini_statement(self):
    print("Mini Statement:")
    print(f"Username:  {self.username}")
    print(f"Balance:  {self.balance}")

#BankManagement class to manage all accounts and user interactions

class BankManagement:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        username= input("Enter username:")    
        password= input("Enter password:")

        if username in self.accounts:
            print("Username already exists!")
        else:
            self.accounts[username] = Account(username,password,0)
            print("Account created successfully!")

    def login(self):
        username = input("Enter your username:")   
        password = input("Enter your password:") 

        if username in self.accounts:
            user_account = self.accounts[username]
            if user_account.password == password:
                print(f"Login successfull Welcome, {username}") 
                return user_account
            else:
                print("Incorrect password!")
        else:
            print("Username not found!")
        return None

    def deposit(self, user_account):
        amount = float(input("Enter deposit amount:"))
        if amount > 0:
            user_account.deposit(amount)
        else:
            print("Invalid amount!")  

    def withdraw(self, user_account):
        amount = float(input("Enter withdrawl amount:"))
        if amount > 0:
            user_account.withdraw(amount)
        else:
            print("Invalid amount!")  

    def check_balance(self, user_account):
        user_account.check_balance()

    def mini_statement(self, user_account):
        user_account.mini_statement()

    def exit(self):
        print("Thank you for using our ATM:")
        exit()

# Main part of the program starts here
bank=BankManagement()

while True:
    print("*** Welcome to Bank of Baroda ***")
    print("1. Create Account:")
    print("2. Login:")
    print("3. Exit:")
    choice= input("Enter an option:")

    if choice == "1":
        bank.create_account()
    elif choice == "2":
        user_account = bank.login()
        if user_account:
            
            while True:
                print("\n*** Welcome to Bank of Baroda ATM:")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Mini Statement")
                print("5. Logout")
                sub_choice = input("Enter your choice:")

                if sub_choice == "1":
                    bank.deposit(user_account)
                elif sub_choice == "2": 
                    bank.withdraw(user_account)
                elif sub_choice == "3":
                    bank.check_balance(user_account)
                elif sub_choice == "4": 
                    bank.mini_statement(user_account)
                elif sub_choice == "5": 
                    print("Logged out successfully.")
                    break
                else:
                    print("Invalid choice, please try again.")
    elif choice == "3":
        bank.exit()

    else:
        print("Invalid choice, please try again.")                             

