class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.__balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append(("Deposit", amount))
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            self.transactions.append(("Withdrawal", amount))
            print(f"₹{amount} withdrawn successfully.")

    def get_balance(self):
        return self.__balance

    def display_transactions(self):
        print("Transaction history:")

        for transaction_type, amount in self.transactions:
            print(f"{transaction_type}: ₹{amount}")


account = BankAccount("Sahil", 5000)

account.deposit(2000)
account.withdraw(1500)
account.withdraw(7000)

print("Current balance:", account.get_balance())
account.display_transactions()
