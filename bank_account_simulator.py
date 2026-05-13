class BankAccount:
    def __init__(self, holder_name):
        self.holder_name = holder_name
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.balance += amount
        self.transactions.append(f"Deposited: {amount:.2f}")
        print(f"Deposited {amount:.2f} successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be greater than zero.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount
        self.transactions.append(f"Withdrawn: {amount:.2f}")
        print(f"Withdrawn {amount:.2f} successfully.")

    def show_balance(self):
        print(f"\nAccount Holder: {self.holder_name}")
        print(f"Current Balance: {self.balance:.2f}")

    def show_transactions(self):
        if not self.transactions:
            print("\nNo transactions found.")
            return

        print("\nTransaction History:")

        for index, transaction in enumerate(self.transactions, start=1):
            print(f"{index}. {transaction}")


def get_amount():
    try:
        amount = float(input("Enter amount: "))
        return amount
    except ValueError:
        print("Enter a valid amount.")
        return None


def create_account():
    name = input("Enter account holder name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return None

    print(f"Account created for {name}.")
    return BankAccount(name)


def menu():
    account = None

    while True:
        print("\n===== BANK ACCOUNT SIMULATOR =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Balance")
        print("5. View Transactions")
        print("6. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            account = create_account()

        elif choice == "2":
            if account is None:
                print("Create an account first.")
                continue

            amount = get_amount()

            if amount is not None:
                account.deposit(amount)

        elif choice == "3":
            if account is None:
                print("Create an account first.")
                continue

            amount = get_amount()

            if amount is not None:
                account.withdraw(amount)

        elif choice == "4":
            if account is None:
                print("Create an account first.")
                continue

            account.show_balance()

        elif choice == "5":
            if account is None:
                print("Create an account first.")
                continue

            account.show_transactions()

        elif choice == "6":
            print("Exiting Bank Account Simulator.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()
