class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

class SavingsAccount(BankAccount):
    def withdrawl(self, amount):
        if self.balance - amount < 0:
            raise ValueError
        self.balance -= amount
        return self.balance

class CheckingAccount(BankAccount):
    def __init__(self):
        BankAccount.__init__(self)
        self.max_credit = 0
    
    def set_max_credit(self, max_credit):
        self.max_credit = max_credit

    def get_max_credit(self):
        return self.max_credit

    def withdraw(self, amount):
        if self.balance < 0 - self.max_credit:
            raise ValueError
        self.balance -= amount
        return self.balance

class Customers:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.address = ''
    
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_address(self, address):
        self.address = address

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_address(self):
        return self.address

class Employees:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.start_date = ''
        self.end_date = ''
        self.salary = 0
    
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date
    
    def set_salary(self, salary):
        self.salary = salary

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

    def get_start_date(self):
        return self.start_date
    
    def get_end_date(self):
        return self.end_date

    def get_salary(self):
        return self.salary

""" class Service:
    class Loans:
    class CreditCard: """

        