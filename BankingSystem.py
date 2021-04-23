import BankAccounts
import BankServices

class Customers():
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def get_full_name(self):
        return "{first} {last}".format(first=self.first_name, last=self.last_name)

    def add_account(self):
        self.account_type = input("Account type (\"savings\" or \"checking\"): ")
        self.balance = float(input("Balance Amount: "))
        if self.account_type == "savings":
            self.interest_rate = float(input("Interest rate: "))
            self.account = BankAccounts.SavingsAccount(self.balance, self.interest_rate)
        elif self.account_type == "checking":
            self.account = BankAccounts.CheckingAccount(self.balance)

    def add_service(self):
        self.service_type = input("Account type (\"loan\" or \"credit card\"): ")
        self.interest = float(input("Interest rate: "))
        if self.service_type == "loan":
            self.balance = float(input("Amount borrowed: "))
            self.period = int(input("Length of loan (in months): "))
            self.account = BankServices.Loan(self.balance, self.interest, self.period)
        elif self.service_type == "credit card":
            self.credit_limit = int(input("Credit limit: "))
            self.account = BankServices.CreditCard(self.interest, self.credit_limit)

class Employees:
    def __init__(self, first_name, last_name, start_date, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.start_date = start_date
        self.end_date = ''
        self.salary = salary

    def get_full_name(self):
        return "{first} {last}".format(first=self.first_name, last=self.last_name)
        
    def set_end_date(self, date):
        if type(date) != str:
            print("Please enter string value for end date.")
            raise TypeError
        else:
            self.end_date = date
        return self.end_date
    
    def get_employment_status(self):
        if not self.end_date:
            return "Active employee since {start}".format(start = self.start_date)
        else:
            return "Terminated since {end}".format(end = self.end_date) 