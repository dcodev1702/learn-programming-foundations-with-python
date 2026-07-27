class Transaction:
    def __init__(self, description, amount, category="Income"):
        self.description = description
        self.amount = amount
        self.category = category

    def is_expense(self):
        return self.amount < 0

    def display(self, index=None):
        sign = "+" if self.amount >= 0 else ""
        prefix = f"{index}. " if index is not None else ""
        print(f"  {prefix}[{self.category}] {self.description}: {sign}${self.amount:.2f}")


class BudgetTracker:
    def __init__(self, owner):
        self.owner = owner
        self.transactions = []

    def add_income(self, description, amount):
        self.transactions.append(Transaction(description, amount, "Income"))
        print(f"Income added: +${amount:.2f}")

    def add_expense(self, description, amount, category):
        self.transactions.append(Transaction(description, -amount, category))
        print(f"Expense added: -${amount:.2f} [{category}]")

    def get_balance(self):
        return sum(transaction.amount for transaction in self.transactions)

    def show_history(self):
        if not self.transactions:
            print("No transactions yet.")
            return

        print(f"\n--- History For {self.owner} ---")
        for index, transaction in enumerate(self.transactions, start=1):
            transaction.display(index)

    def show_summary(self):
        income_total = sum(transaction.amount for transaction in self.transactions if transaction.amount > 0)
        expense_total = sum(transaction.amount for transaction in self.transactions if transaction.amount < 0)

        print(f"\n--- Summary For {self.owner} ---")
        print(f"  Total Income:   +${income_total:.2f}")
        print(f"  Total Expenses: -${abs(expense_total):.2f}")
        print(f"  Balance:         ${self.get_balance():.2f}")

    def spending_by_category(self):
        category_totals = {}

        for transaction in self.transactions:
            if transaction.is_expense():
                category_totals[transaction.category] = category_totals.get(transaction.category, 0) + abs(transaction.amount)

        if not category_totals:
            print("No expense categories yet.")
            return

        print("\n--- Spending By Category ---")
        for category, total in sorted(category_totals.items()):
            print(f"  {category}: ${total:.2f}")


def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Please enter a positive number.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("=" * 44)
    print("   Personal Budget Tracker - Week 10")
    print("=" * 44)

    owner = input("Enter your name: ").strip() or "User"
    tracker = BudgetTracker(owner)

    while True:
        print(f"\n--- Menu (Balance: ${tracker.get_balance():.2f}) ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transaction History")
        print("4. View Summary")
        print("5. View Spending by Category")
        print("6. Quit")

        choice = input("\nSelect an option (1-6): ").strip()

        match choice:
            case "1":
                description = input("Description: ").strip() or "Income"
                amount = get_valid_amount("Amount: $")
                tracker.add_income(description, amount)
            case "2":
                description = input("Description: ").strip() or "Expense"
                amount = get_valid_amount("Amount: $")
                category = input("Category: ").strip().title() or "Uncategorized"
                tracker.add_expense(description, amount, category)
            case "3":
                tracker.show_history()
            case "4":
                tracker.show_summary()
            case "5":
                tracker.spending_by_category()
            case "6":
                print("Goodbye!")
                break
            case _:
                print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()