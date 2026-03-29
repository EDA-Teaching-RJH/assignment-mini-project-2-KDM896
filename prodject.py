class Transactions: 
    def __init__(self, date, amount, category):
        self.date = date # defining the variables for the transactions that will come in and the information required for them to be logged correctly.
        self.category = category
        self.amount = amount # my first class being used as the main class where i will continue on using inheritance to create a clear structure for the sub classes.
    def get_summary(self):
        return f"{self.date} | {self.category} | £{self.amount}"# this will return a string representation of the transaction, which will be used when viewing the summary of transactions.

class Income(Transactions):
    def __init__(self, date, amount, category, source):
        super().__init__(date, amount, category)
        self.source = source
        self.transaction_type = "Income"# added to both the income and expense class to allow for differentiation between income and expenses when viewing the summary of transactions.

class Expenses(Transactions):
    def __init__(self, date, amount, category, source): # using inheritance with 'super' in these two classes to avoid repeating code over and over.
        super().__init__(date, amount, category)
        self.source = source
        self.transaction_type = "Expense"

import re

import csv

def save_transactions(transactions):
    with open("finances.csv", "w", newline="") as file:
        fieldnames = ["Date", "Amount", "Category", "Source"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for transaction in transactions:
            writer.writerow({
                "Date": transaction.date,
                "Amount": transaction.amount,
                "Category": transaction.category,
                "Source": transaction.source,
            })# the function here is to save the transactions to a csv file, it also provides the previouse transactions that were saved in the file to the transactions list.

def load_transactions():
    transactions = []#
    try:
        with open("finances.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                date = row["Date"]
                amount = float(row["Amount"])# this is reading the transactions from the csv file and creating instances of the Income or Expenses class based on the category of the transaction, then adding them to the transactions list. 
                category = row["Category"]
                source = row["Source"]
                if "Income" in category:
                    transactions.append(Income(date, amount, category, source))# this function is to load the transactions from the csv file, it reads the file and creates instances of the Income or Expenses class based on the category of the transaction, then adds them to the transactions list.
                else:
                    transactions.append(Expenses(date, amount, category, source))
    except FileNotFoundError:
        pass
    return transactions

def calculate_balance(start_balance, transaction_list):
    balance = start_balance
    for t in transaction_list:
        if t.transaction_type == "Income":
            balance += t.amount
        else:
            balance -= t.amount
    return balance# this function is to calculate the current balance based on the starting balance and the transactions that have been made, it will loop through the transactions and add or subtract the amount based on whether it is a income or expense.

def security_check():#Defining the security log in function to make it so only the original user can login validating the answers against the given correct answers.
    correct_Name = "Kenzie Minott"
    correct_date_of_birth = "14-01-2006"
    correct_passcode = "7890"
    name = input("Enter your name:")
    while True:
        date_of_birth = input("Enter your date of birth (DD-MM-YYYY):")
        if validate_date(date_of_birth):        
            break
        else:
            print("Invalid date format. Please enter the date in DD-MM-YYYY format.")
    passcode = input("Enter your passcode:")
    if name == correct_Name and date_of_birth == correct_date_of_birth and passcode == correct_passcode:#this is to check that the correct credentyials are being added , then allowing access to the menmu if they are correct.
        print("Access granted. Welcome to your financial tracker.")
        return True
    else:
        print("Access denied. Incorrect login details.")
        return False
    
def check_credentials(name, date_of_birth, passcode):
        correct_Name = "Kenzie Minott"
        correct_date_of_birth = "14-01-2006"
        correct_passcode = "7890"
        return name == correct_Name and date_of_birth == correct_date_of_birth and passcode == correct_passcode# defines a function to check the credentials, this is used in the test file to test the security check function.
def validate_date(date):
    pattern = r"^\d{2}-\d{2}-\d{4}$"
    return re.match(pattern, date) is not None

def main():
    if not security_check():
        return
    
    transactions = load_transactions()# this loads the transactions from the csv file and calculating the initial balance based on the starting balance of 5500 and the transactions that have been loaded. this allows for the user to continue using the program without losing their previous data.
    initial_balance = calculate_balance(5500, transactions)
    
    while True:
        print("1- Add Income")
        print("2- Add Expense")
        print("3- View Summary")
        print("4- Exit")
        choice = input("Choose an option:")# looping the main menu to allow for user to continue using the program for multiple inputs.
        
        if choice == "1":# assigns the users input for a desired outcome.
            while True:
                date = input("Enter date (DD-MM-YYYY):")
                if validate_date(date):
                    break
                else:
                    print("Invalid date format. Please enter the date in DD-MM-YYYY format.")
            amount = float(input("Enter amount:"))# getting user input for the date and amount of the transaction, then creating an instance of the Income class and adding it to the transactions list. also updating the initial balance by adding the income amount.
            category = input("Enter category:")
            source = input("Enter source:")
            income = Income(date, amount, category, source)
            transactions.append(income)
            initial_balance += amount
            print("funds added to record.")
        
        elif choice == "2":
            while True:
                date = input("Enter date (DD-MM-YYYY):")
                if validate_date(date):
                    break# this is to get the user input for the date and validate it using the validate_date function, if the date is not in the correct format it will keep asking for a valid date until it gets it.
                else:
                    print("Invalid date format. Please enter the date in DD-MM-YYYY format.")
            
            amount = float(input("Enter amount:"))
            category = input("Enter category:")
            source = input("Enter source:")
            expense = Expenses(date, amount, category, source)
            transactions.append(expense)
            initial_balance -= amount# getting user input for the date and amount of the transaction then updating the initial balance by subtracting the expense amount.
            print("funds removed from record.")
        elif choice == "3":
            for transaction in transactions:
                print(transaction.get_summary())
            print(f"Current balance: £{initial_balance}")# this is to print out the summary of transactions and the current balance, it will loop through the transactions and call the get_summary method for each transaction to print out the details, then it will print out the current balance.
        elif choice == "4":
            save_transactions(transactions)# this is to save the transactions to a csv file when the user chooses to exit the program, it will call the save_transactions function and pass in the transactions list, which will write the transactions to the csv file.
            print("data saved. exiting program.")
            break






if __name__ == "__main__":
            main()