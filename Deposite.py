import csv

class Deposit:
    # deposit function
    def deposit(self):
        print("Welcome to the deposit page")
        account_no = int(input("Enter your account number: "))
        filename = "customer.csv"
        with open(filename, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            for row in rows:
                if row:
                    if account_no == int(row[0]):
                        deposit_amount = int(input("Enter the amount to deposit: "))
                        row[2] = int(row[2]) + deposit_amount
                        print(f"Your new balance is {row[2]}")
                        with open(filename, "w", newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(rows)
                        file.close()
                        return
            print("Account not found")
        file.close()
        return