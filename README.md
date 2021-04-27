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
Program adds customers and employees.
Each customer is able to add a bank account or service.
* Bank Account
  Either a savings account or checking account. Both are enabled to deposit and withraw to the account balance.
    1. Savings Account
       Added interest rate to the balance of the bank account.
    3. Checking Account
       Addition fee to withdraw money from bank account.
* Bank Service
  Either a loan or credit card service. Both include a balance and interest rate, and enable to pay off balance.
    1. Loan
       Added calculated monthly payment (fixed rate).
    3. Credit Card
       Added feature to charge card within the max credit limit. 
