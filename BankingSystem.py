import BankAccounts

class Customers():
    def __init__(self, first_name, last_name, address, account_type):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.account = self.account_setup(account_type)
    
    def account_setup(self, account_type):
        if account_type == 'savings':
            account = BankAccounts.SavingsAccount()
        elif account_type == 'checking':
            account = BankAccounts.CheckingAccount()
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