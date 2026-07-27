import json


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

    def to_dict(self):
        return {
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["description"],
            data["amount"],
            data.get("category", "Uncategorized"),
        )


class BudgetTracker:
    def __init__(self, owner):
        self.owner = owner
        self.transactions = []

    def add_income(self, description, amount):
        self.transactions.append(Transaction(description, amount, "Income"))
        print(f"  Income added: +${amount:.2f}")

    def add_expense(self, description, amount, category):
        self.transactions.append(Transaction(description, -amount, category))
        print(f"  Expense added: -${amount:.2f} [{category}]")

    def get_balance(self):
        return sum(transaction.amount for transaction in self.transactions)

    def show_history(self):
        if not self.transactions:
            print("  No transactions yet.")
            return

        for index, transaction in enumerate(self.transactions, start=1):
            transaction.display(index)

        print(f"\n  Current Balance: ${self.get_balance():.2f}")

    def show_summary(self):
        income_total = sum(transaction.amount for transaction in self.transactions if transaction.amount > 0)
        expense_total = sum(transaction.amount for transaction in self.transactions if transaction.amount < 0)
        balance = self.get_balance()

        print(f"\n  --- Summary for {self.owner} ---")
        print(f"  Total Income:    +${income_total:.2f}")
        print(f"  Total Expenses:  -${abs(expense_total):.2f}")
        print(f"  Net Balance:      ${balance:.2f}")

        if balance < 0:
            print("  Warning: You are over budget.")

    def spending_by_category(self):
        category_totals = {}

        for transaction in self.transactions:
            if transaction.is_expense():
                category_totals[transaction.category] = category_totals.get(transaction.category, 0) + abs(transaction.amount)

        if not category_totals:
            print("  No expenses recorded yet.")
            return

        print("\n  --- Spending by Category ---")
        for category, total in sorted(category_totals.items()):
            print(f"  {category}: ${total:.2f}")

    def save(self, filename="budget_data.json"):
        data = {
            "owner": self.owner,
            "transactions": [transaction.to_dict() for transaction in self.transactions],
        }

        with open(filename, "w") as file_handle:
            json.dump(data, file_handle, indent=2)

        print(f"  Data saved to {filename}.")

    def load(self, filename="budget_data.json"):
        try:
            with open(filename, "r") as file_handle:
                data = json.load(file_handle)

            self.owner = data["owner"]
            self.transactions = [
                Transaction.from_dict(item)
                for item in data["transactions"]
            ]
            print(f"  Welcome back, {self.owner}! Loaded {len(self.transactions)} transactions.")
        except FileNotFoundError:
            print("  No saved data found. Starting fresh!")
        except json.JSONDecodeError:
            print(f"  {filename} is not valid JSON. Starting fresh!")
        except (KeyError, TypeError):
            print(f"  {filename} is missing expected fields. Starting fresh!")


def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("  Please enter a positive number.")
                continue
            return amount
        except ValueError:
            print("  Invalid input. Please enter a number.")


def get_non_empty_text(prompt, default_value=None):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        if default_value is not None:
            return default_value
        print("  Input cannot be empty.")


def main():
    print("=" * 44)
    print("   Personal Budget Tracker v1.0")
    print("   Built with Python 3.13")
    print("=" * 44)

    name = get_non_empty_text("\nEnter your name: ", "User")
    tracker = BudgetTracker(name)
    tracker.load()

    while True:
        print(f"\n--- Menu (Balance: ${tracker.get_balance():.2f}) ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transaction History")
        print("4. View Summary")
        print("5. View Spending by Category")
        print("6. Save Data")
        print("7. Quit")

        choice = input("\nSelect an option (1-7): ").strip()

        match choice:
            case "1":
                description = get_non_empty_text("  Description: ")
                amount = get_valid_amount("  Amount: $")
                tracker.add_income(description, amount)

            case "2":
                description = get_non_empty_text("  Description: ")
                amount = get_valid_amount("  Amount: $")
                category = get_non_empty_text("  Category (e.g., Food, Transport, Bills): ", "Uncategorized").title()
                tracker.add_expense(description, amount, category)

            case "3":
                tracker.show_history()

            case "4":
                tracker.show_summary()

            case "5":
                tracker.spending_by_category()

            case "6":
                tracker.save()

            case "7":
                save_first = input("  Save before quitting? (y/n): ").strip().lower()
                if save_first == "y":
                    tracker.save()
                print(f"\n  Goodbye, {tracker.owner}! Happy budgeting!")
                break

            case _:
                print("  Invalid option. Please choose 1-7.")


if __name__ == "__main__":
    main()