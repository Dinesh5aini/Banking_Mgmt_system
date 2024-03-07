import csv

class Balance_Enq:
    def balance_enquiry(self):
        print("Welcome to the balance enquiry page")
        account_no = int(input("Enter your account number: "))
        filename = "customer.csv"
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    if account_no == int(row[0]):
                        print(f"Your balance is {row[2]}")
                        return
            print("Account not found")
        file.close()
        return