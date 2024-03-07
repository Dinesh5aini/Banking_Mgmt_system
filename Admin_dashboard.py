from Account_creation import AccountCreation
from Deposite import Deposit
from Withdraw import Withdrawal
from Balance_enquiry import Balance_Enq

class Admin_dashboard:
    def admin_dashboard(self):
        print("Welcome to the Admin Dashboard")
        print("1. Account creation")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Balance Enquiry")

        choice = input("Enter your choice: ").lower()
        if choice == "1" or choice == "account creation":
            account_creation_obj = AccountCreation()
            account_creation_obj.account_creation()
        elif choice == "2" or choice == "deposit":
            deposit_obj = Deposit()
            deposit_obj.deposit()
        elif choice == "3" or choice == "withdrawal":
            withdrawal_obj = Withdrawal()
            withdrawal_obj.withdrawal()
        elif choice == "4" or choice == "balance enquiry":
            balance_enq_obj = Balance_Enq()
            balance_enq_obj.balance_enquiry()
        else:
            print("Invalid choice")