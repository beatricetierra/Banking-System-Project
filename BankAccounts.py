class BankAccount:
    def __init__(self, record, balance = 0):
        self.record = record
        self.balance = balance        

    def deposit(self, amount):
        self.balance += amount
        self.record.update_balance('Accounts.json', self.balance)
        return self.balance

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('Not enough funds. Balance is {balance}'.format(balance = self.balance))
            raise ValueError
        self.balance -= amount
        self.record.update_balance('Accounts.json', self.balance)
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, record, balance = 0, interest_rate = 0.0007):
        BankAccount.__init__(self, record, balance)
        self.interest_rate = interest_rate

    def compute_interest(self, n_periods = 1):
        return self.balance * ((1 + self.interest_rate) ** n_periods - 1)

class CheckingAccount(BankAccount):
    def __init__(self, record, balance = 0):
        BankAccount.__init__(self, record, balance)

    def withdraw(self, amount, fee):
        BankAccount.withdraw(self, amount+fee)
        return self.balance