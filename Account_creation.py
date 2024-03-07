import csv
import numpy as np

class AccountCreation:
    # Account creation function
    def account_creation(self):
        print("Welcome to the account creation page")
        filename = "customer.csv"
        with open(filename, "a", newline='') as file:
            writer = csv.writer(file)
            account_no = ''.join([str(np.random.randint(0, 9)) for _ in range(10)])
            account_name = input("Enter your name: ")
            account_balance = int(input("Enter your initial deposit: "))
            account_status = "Active"
            account_digital_sign = input("Enter your digital signature: ")
            writer.writerow([account_no, account_name, account_balance, account_status, account_digital_sign])
            print("Account created successfully")
            print(f"Your account number is {account_no}")
        file.close()
        return