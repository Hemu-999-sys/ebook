#Railway Ticket Management System
import random  
class Train:
    def __init__(self, train_num, source, destination, seats):
        self.train_num = train_num        
        self.source = source             
        self.destination = destination    
        self.seats = seats               

    def display_info(self):
        print(f"Train Number: {self.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Available Seats: {self.seats}")
        print()

    def book_tickets(self, num_tickets, existing_pnrs):
        
        if num_tickets > self.seats:
            return None  
        else:
            pnr_list = []  
            for i in range(num_tickets):
                pnr = self.generate_unique_pnr(existing_pnrs)  
                existing_pnrs.add(pnr)  
                pnr_list.append(pnr)
            self.seats -= num_tickets  
            return pnr_list

    def generate_unique_pnr(self, existing_pnrs):
        while True:
            pnr = random.randint(5000, 10000)
            if pnr not in existing_pnrs:
                return pnr

class Passenger:
    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Phone: {self.phone}")

class Ticket:
    def __init__(self, train, source, destination, passengers, pnr):
        self.train = train
        self.source = source
        self.destination = destination
        self.passengers = passengers 
        self.pnr = pnr

    def display_info(self):
        print(f"Train Number: {self.train.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"PNR: {self.pnr}")
        for passenger in self.passengers:
            passenger.display_info()
        print()

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password

accounts = [
    Account("user1", "password1"),
    Account("user2", "password2")
    
]

logged_in_account = None  

while True:
    print("\n1. Create an Account")
    print("2. Login")
    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Enter username: ")
        if any(account.username == username for account in accounts):
            print("Username already exists. Please choose a different username.")
        else:
            password = input("Enter password: ")
            accounts.append(Account(username, password))
            print("Account created successfully!")
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        for account in accounts:
            if account.username == username and account.check_password(password):
                logged_in_account = account
                break
        if logged_in_account is None:
            print("Invalid username or password.")
        else:
            print(f"\nLogged in as {logged_in_account.username}")
            break  
        print("Invalid choice. Please enter 1 or 2.")
trains = [
    Train("24357", "Adilabad", "Thirupathi", 30),
    Train("35689", "Secunderabad", "Bangalore", 60),
]

existing_pnrs = set()

def book_ticket_flow():
    print("\n--- Available Train Details ---\n")
    for train in trains:
        train.display_info()
    while True:
        try:
            train_num = input("Enter Train Number: ")
            num_tickets = int(input("Enter Number of Tickets: "))
            if num_tickets <= 0:
                raise ValueError("Number of tickets should be greater than 0")
            selected_train = None
            for t in trains:
                if t.train_num == train_num:
                    selected_train = t
                    break
            if selected_train is None:
                raise ValueError("Invalid Train Number")
            if num_tickets > selected_train.seats:
                raise ValueError("Selected more tickets than available seats")
            break
        except ValueError as e:
            print(f"Invalid Input: {e}")

    passengers = []
    for i in range(num_tickets):
        print(f"\nEnter Details for Passenger {i + 1}:")
        while True:
            try:
                name = input("Name: ").strip()
                if not name:
                    raise ValueError("Name cannot be empty")
                age = int(input("Age: "))
                if age <= 0 or age > 100:
                    raise ValueError("Invalid Age")
                gender = input("Gender: ").strip()
                phone = input("Phone Number: ").strip()
                if not phone.isdigit() or len(phone) != 10:
                    raise ValueError("Invalid Phone Number")
                passenger = Passenger(name, age, gender, phone)
                passengers.append(passenger)
                break
            except ValueError as e:
                print(f"Invalid Input: {e}")

    pnr_list = selected_train.book_tickets(num_tickets, existing_pnrs)
    if pnr_list is None:
        print("Tickets not available.")
    else:
        print("\n------ Booking Successful ------\nYour Ticket Details:\n")
        for i in range(num_tickets):
            ticket = Ticket(
                selected_train,
                selected_train.source,
                selected_train.destination,
                [passengers[i]],  
                pnr_list[i]
            )
            ticket.display_info()  
        print("----- Thank you for booking! -----\n")

while True:
    print("1. Book Tickets")
    print("2. Logout and Exit")
    menu_choice = input("Enter your choice: ")

    if menu_choice == "1":
        book_ticket_flow()  
    elif menu_choice == "2":
        print("Logged out successfully. Goodbye!")
        break 
    else:
        print("Invalid choice. Please select 1 or 2.")





