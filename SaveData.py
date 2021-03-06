import os.path
import json
import logging
from datetime import datetime

today = datetime.now().date().strftime("%Y%m%d") 
log_filename = 'BankingSystemLog_{date}.log'.format(date=today)
logging.basicConfig(filename=log_filename, level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

class RecordInfo:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.name = "{last}, {first}".format(last=self.last, first=self.first)

    def check_file_exists(self, file):
        return os.path.exists(file)

    def load_json(self, file):
        with open(file) as f:
            data = json.load(f)
        return data
    
    def write_json(self, file, data):
        with open(file, 'w') as f:
            json.dump(data, f, indent=4)

    def get_record(self, file):
        if not self.check_file_exists(file):
            open(file, "w")
        try:
            records = self.load_json(file)
        except:
            print("Created new file.")
            records = {}
        return records

class CustomersData(RecordInfo):
    def __init__(self, first, last, address):
        RecordInfo.__init__(self, first, last)
        self.address = address
        self.update_customer_records()

    def update_customer_records(self):
        f = "Customers.json"
        record = self.get_record(f)
        record[self.name] = {'first': self.first, 
                        'last': self.last, 
                        'address': self.address}
        self.write_json(f, record)
        return "Updated {file}".format(file=f)

    def update_account_records(self, account_type, balance, interest_rate):
        f = "Accounts.json"
        record = self.get_record(f)
        record[self.name] = {'account_type': account_type, 
                         'balance': balance, 
                         'interest_rate': interest_rate}
        self.write_json(f, record)
        return "Updated {file}".format(file=f)

    def update_service_records(self, service_type, balance, interest, period, credit_limit):
        f = "Services.json"
        record = self.get_record(f)
        record[self.name] = {'account_type': service_type, 
                       'balance': balance, 
                       'interest_rate': interest,
                       'period': period,
                       'credit_limit': credit_limit}
        self.write_json(f, record)
        return "Updated {file}".format(file=f)

    def update_balance(self, file, value):
        record = self.get_record(file)
        record[self.name]['balance'] = value
        self.write_json(file, record)
        logging.info("Updated balance of {name} to ${balance}".format(name=self.name, balance=value))
        return "Updated {file}".format(file=file)

class EmployeesData(RecordInfo):
    def __init__(self, first, last, start_date, salary):
        RecordInfo.__init__(self, first, last)
        self.start_date = start_date
        self.salary = salary
        self.update_employee_records()
    
    def update_employee_records(self):
        f = "Employees.json"
        record = self.get_record(f)
        record[self.name] = {'salary': self.salary, 
                         'start date': self.start_date, 
                         'end date': None}
        self.write_json(f, record)
        return "Updated {file}".format(file=f)

    def update_enddate(self, end_date):
        f = 'Employees.json'
        record = self.get_record(f)
        record[self.name]['end date'] = end_date
        self.write_json(f, record)
        logging.info("Updated termindation date of {name} to {date}".format(name=self.name, date=end_date))
        return "Termination date added to {file}".format(file=f)
    