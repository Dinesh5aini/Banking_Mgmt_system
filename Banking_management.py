from Admin_signup_login import login_signup
from Admin_dashboard import Admin_dashboard

class Banking_mnmt:
    def main(self):
        obj = login_signup()
        logged_in = obj.admin_login()
        if logged_in:
            while True:
                admin_dashboard_obj = Admin_dashboard()
                admin_dashboard_obj.admin_dashboard()
                choice = input("Do you want to go back to the Admin Dashboard? (y/n): ").lower()
                if choice != "y":
                    break
        else:
            print("Login failed. Exiting the program.")

if __name__ == "__main__":
    banking_mnmt_obj = Banking_mnmt()
    banking_mnmt_obj.main()