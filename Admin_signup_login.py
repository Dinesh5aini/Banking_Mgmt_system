import csv

class login_signup:
    #Admin signup function
    def admin_signup(self):
        print("Welcome to the admin signup page")
        filename = "admin.csv"
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        print("Admin already exists")
                        return self.admin_login()
            file.close()
        except FileNotFoundError:
            pass

        with open(filename, "a", newline='') as file:
            writer = csv.writer(file)
            admin = input("Enter your username: ")
            password = input("Enter your password: ")
            writer.writerow([admin, password])
            print("Admin created successfully")
        file.close()
        return self.admin_login()

    #Admin login function
    def admin_login(self, max_attempts=5):
        if max_attempts == 0:
            print("You have exceeded the maximum number of attempts")
            return
        print("Welcome to the Admin Login Page")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        try:
            filename = "admin.csv"
            with open(filename, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and username == row[0] and password == row[1]:
                        print("Login successful")
                        file.close()
                        return True
            print("Invalid username or password")
            return self.admin_login(max_attempts - 1)
        except FileNotFoundError:
            print("No admin account found")
            self.admin_signup()
        except PermissionError:
            print("Permission denied: Unable to read the file")
            return False