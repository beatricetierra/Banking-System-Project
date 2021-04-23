class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('Not enough funds. Balance is {balance}'.format(balance = self.balance))
            raise ValueError
        self.balance -= amount
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, balance = 0, interest_rate = 0.0007):
        BankAccount.__init__(self, balance)
        self.interest_rate = interest_rate

    def compute_interest(self, n_periods = 1):
        return self.balance * ((1 + self.interest_rate) ** n_periods - 1)

class CheckingAccount(BankAccount):
    def __init__(self, balance = 0):
        BankAccount.__init__(self, balance)

    def withdraw(self, amount, fee):
        BankAccount.withdraw(self, amount+fee)
        return self.balance

class Customers():
    def __init__(self, first_name, last_name, address, account_type):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.account = self.account_setup(account_type)
    
    def account_setup(self, account_type):
        if account_type == 'savings':
            account = SavingsAccount()
        elif account_type == 'checking':
            account = CheckingAccount()
        return account
    
    def get_full_name(self):
        return "{first} {last}".format(first=self.first_name, last=self.last_name)

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

class BankService():
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest
    
    def pay(self, amount):
        self.balance -= amount
        return self.balance

class Loan(BankService):
    def __init__(self, balance, interest, period):
        BankService.__init__(self, balance, interest)
        self.principal = balance
        self.period = period
        self.monthly_payment = self.monthly_payment()
    
    def monthly_payment(self):
        p = self.principal
        r = self.interest/12 #monthly interest rate
        n = self.period
        numerator = r*(1+r)**n
        denominator = ((1+r)**n) - 1
        return p*numerator/denominator

class CreditCard(BankService):
    def __init__(self, balance, interest, max_credit):
        BankService.__init__(self, balance, interest)
        self.max_credit = max_credit
    
    def charge(self, amount):
        if self.balance + amount > self.max_credit:
            print('Exceed credit limit')
            raise ValueError
        self.balance += amount
        return self.balance 