import csv

class Withdrawal:
    #withdrawal function
    def withdrawal(self):
        print("Welcome to the withdrawal page")
        account_no = int(input("Enter your account number: "))
        filename = "customer.csv"
        with open(filename, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            for row in rows:
                if row:
                    if account_no == int(row[0]):
                        withdrawal_amount = int(input("Enter the amount to withdraw: "))
                        if withdrawal_amount > int(row[2]):
                            print("Insufficient funds")
                            return
                        row[2] = int(row[2]) - withdrawal_amount
                        print(f"Your new balance is {row[2]}")
                        with open(filename, "w", newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(rows)
                        file.close()
                        return
            print("Account not found")
        file.close()
        return