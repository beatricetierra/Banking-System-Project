# Banking-System-Project
This project is a simple version of a banking system.
Program adds customers and employees, tracking updates in generated JSON and log files.

## Installation
Following packages were installed and imported to run program.
* os.path
* json
* logging
* datetime

## Usage
Program adds customers and employees. Each update to either class is tracked in the "BankingSystemLog" file (new one generated and labeled with every new date program is used). 

Each initialized employee's first name, last name, start date, and salary are stored and tracked in the Employees.json file. The employee's end date can also be set, automatically turning the emloyee's status to "Terminated". 

Each initialized customer's first name, last name, and address are stored and tracked in the Cusomters.json file. Each customer is able to add a bank account or service.
* **Bank Account**

  Either a savings account or checking account. Both are enabled to deposit and withraw to the account balance. 
  Initizliazation and changes are tracked in the Accounts.json file.
  
    1. **Savings Account**: Added interest rate to the balance of the bank account.
    2. **Checking Account**: Addition fee to withdraw money from bank account.
* **Bank Service**

  Either a loan or credit card service. Both include a balance and interest rate, and enable to pay off balance. 
  Initizliazation and changes are tracked in the Services.json file.
  
    1. **Loan** : Added calculated monthly payment (fixed rate).
    2. **Credit Card**: Added feature to charge card within the max credit limit. 


