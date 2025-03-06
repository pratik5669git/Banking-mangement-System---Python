class BankAccount:
    def __init__(self, account_number, balance=0):  
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        self.log_account_info("Deposit", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.log_account_info("Withdraw", amount)
            return True
        else:
            print("Insufficient funds")
            return False

    def get_balance(self):
        return self.balance

    def log_account_info(self, action, amount):
        with open("account_info.txt", "a") as file:
            file.write(f"Account Number: {self.account_number}, Action: {action}, Amount: {amount}, New Balance: {self.balance}\n")


def signup(username, password):
    with open("usersID.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("Signup successful!")


def login(username, password):
    with open("usersID.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if stored_username == username and stored_password == password:
                return True
    return False


def main():
    accounts = {}
    logged_in_user = None
    print("\n\n")
    print("\tWELCOME TO BANKING MANAGEMENT SYSTEM\n\n")
    while True:
        if logged_in_user is None:
            print("1. Signup")
            print("2. Login")
            print("3. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                username = input("Enter username: ")
                password = input("Enter password: ")
                signup(username, password)
            elif choice == 2:
                username = input("Enter username: ")
                password = input("Enter password: ")
                if login(username, password):
                    logged_in_user = username
                    print("Login successful!")
                else:
                    print("Invalid username or password")
            elif choice == 3:
                print("Exiting...")
                break
            else:
                print("Invalid choice")
        else:
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Logout")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                account_number = input("Enter account number: ")
                accounts[account_number] = BankAccount(account_number)
                print("Account created successfully!")
            elif choice == 2:
                account_number = input("Enter account number: ")
                if account_number in accounts:
                    amount = float(input("Enter amount to deposit: "))
                    accounts[account_number].deposit(amount)
                    print("Deposit successful!")
                else:
                    print("Account not found")
            elif choice == 3:
                account_number = input("Enter account number: ")
                if account_number in accounts:
                    amount = float(input("Enter amount to withdraw: "))
                    if accounts[account_number].withdraw(amount):
                        print("Withdrawal successful!")
                else:
                    print("Account not found")
            elif choice == 4:
                account_number = input("Enter account number: ")
                if account_number in accounts:
                    balance = accounts[account_number].get_balance()
                    print("Balance:", balance)
                else:
                    print("Account not found")
            elif choice == 5:
                logged_in_user = None
                print("Logged out successfully!")
            else:
                print("Invalid choice")


if __name__ == "__main__":  
    main()