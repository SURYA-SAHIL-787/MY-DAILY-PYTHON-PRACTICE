class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, name, amount):
        self.expenses.append({"name": name, "amount": amount})

    def show_expenses(self):
        print("\nAll Expenses:")
        for expense in self.expenses:
            print(f"{expense['name']} - ₹{expense['amount']}")

    def total_expense(self):
        total = sum(expense["amount"] for expense in self.expenses)
        print(f"\nTotal Expense: ₹{total}")


tracker = ExpenseTracker()

tracker.add_expense("Food", 120)
tracker.add_expense("Travel", 50)
tracker.add_expense("Notebook", 80)

tracker.show_expenses()
tracker.total_expense()
