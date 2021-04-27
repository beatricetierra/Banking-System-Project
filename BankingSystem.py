import logging 
from datetime import datetime

import BankAccounts
import BankServices
from SaveData import CustomersData
from SaveData import EmployeesData

today = datetime.now().date().strftime("%Y%m%d") 
log_filename = 'BankingSystemLog_{date}.log'.format(date=today)
logging.basicConfig(filename=log_filename, level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

class Customers():
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

        self.record = CustomersData(self.first_name, self.last_name, self.address)
        logging.info('New customer: {last}, {first}'.format(last=self.last_name, first=self.first_name))

    def add_account(self):
        self.account_type = input("Account type (\"savings\" or \"checking\"): ")
        self.balance = float(input("Balance Amount: "))
        if self.account_type == "savings":
            self.add_savings_account()
        elif self.account_type == "checking":
            self.add_checking_account()
    
    def add_savings_account(self):
        self.interest_rate = float(input("Interest rate: "))
        self.account = BankAccounts.SavingsAccount(self.record, self.balance, self.interest_rate)
        self.record.update_account_records(self.account_type, self.balance, self.interest_rate)
        logging.info('New savings acount under {last}, {first}: balance = {balance}, interest = {interest}'.format(
                    last=self.last_name, first=self.first_name, balance=self.balance, interest=self.interest_rate))
    
    def add_checking_account(self):
        self.account = BankAccounts.CheckingAccount(self.record, self.balance)
        self.record.update_account_records(self.account_type, self.balance, None)
        logging.info('New checking acount under {last}, {first}: balance = {balance}'.format(
                    last=self.last_name, first=self.first_name, balance=self.balance))

    def add_service(self):
        self.service_type = input("Account type (\"loan\" or \"credit card\"): ")
        self.interest = float(input("Interest rate: "))
        if self.service_type == "loan":
            self.add_loan_service()
        elif self.service_type == "credit card":
            self.add_creditcard_service()
    
    def add_loan_service(self):
        self.balance = float(input("Amount borrowed: "))
        self.period = int(input("Length of loan (in months): "))
        self.service = BankServices.Loan(self.record, self.balance, self.interest, self.period)
        self.record.update_service_records(self.service_type, self.balance, self.interest, self.period, None)
        logging.info('New loan to {last}, {first}: balance = {balance}, interest = {interest}, duration = {period} months'.format(
                    last=self.last_name, first=self.first_name, balance=self.balance, interest=self.interest, period=self.period))
    
    def add_creditcard_service(self):
        self.credit_limit = int(input("Credit limit: "))
        self.service = BankServices.CreditCard(self.record, self.interest, self.credit_limit)
        self.record.update_service_records(self.service_type, 0, self.interest, None, self.credit_limit)
        logging.info('New credit card to {last}, {first}: credit limit = {limit}, interest = {interest}'.format(
                    last=self.last_name, first=self.first_name, limit=self.credit_limit, interest=self.interest))
    
class Employees:
    def __init__(self, first_name, last_name, start_date, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.start_date = start_date
        self.end_date = ''
        self.salary = salary
        
        self.record = EmployeesData(self.first_name, self.last_name, self.start_date, self.salary)
        logging.info('New employee: {last}, {first}: started = {start}, salary = {salary}'.format(
                                                            last=self.last_name, first=self.first_name,
                                                            start=self.start_date, salary=self.salary))

    def set_end_date(self, date):
        if type(date) != str:
            print("Please enter string value for end date.")
            raise TypeError
        else:
            self.end_date = date
            self.record.update_enddate(date)
        return self.end_date
    
    def get_employment_status(self):
        if not self.end_date:
            return "Active employee since {start}".format(start = self.start_date)
        else:
            return "Terminated since {end}".format(end = self.end_date) 