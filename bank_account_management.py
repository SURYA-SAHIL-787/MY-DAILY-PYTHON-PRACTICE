class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount

    def display_details(self):
        print(
            f"Account Number: {self.account_number}, "
            f"Holder: {self.holder_name}, "
            f"Balance: {self.balance:.2f}"
        )


def find_highest_balance_account(accounts):
    if not accounts:
        return None

    highest_account = accounts[0]

    for account in accounts[1:]:
        if account.balance > highest_account.balance:
            highest_account = account

    return highest_account


n = int(input("Enter the number of bank accounts: "))
accounts = []

for i in range(n):
    print(f"\nEnter details of account {i + 1}:")

    account_number = input("Enter account number: ")
    holder_name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))

    account = BankAccount(account_number, holder_name, balance)
    accounts.append(account)


result = find_highest_balance_account(accounts)

if result is None:
    print("No bank accounts available.")
else:
    print("\nAccount with the highest balance:")
    result.display_details()
