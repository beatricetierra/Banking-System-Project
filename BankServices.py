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
        self.monthly_payment = self.calculate_monthly_payment()

    def calculate_monthly_payment(self):
        p = self.principal
        r = self.interest/12 #monthly interest rate
        n = self.period
        numerator = r*(1+r)**n
        denominator = ((1+r)**n) - 1
        return p*numerator/denominator

class CreditCard(BankService):
    def __init__(self, interest, max_credit):
        balance = 0
        BankService.__init__(self, balance, interest)
        self.max_credit = max_credit
    
    def charge(self, amount):
        if self.balance + amount > self.max_credit:
            print('Exceed credit limit')
            raise ValueError
        self.balance += amount
        return self.balance 