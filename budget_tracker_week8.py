def display_menu():
    print("\n--- Budget Tracker Menu ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transaction History")
    print("5. View Spending by Category")
    print("6. Quit")


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


def add_income(transactions):
    description = input("Description: ").strip() or "Income"
    amount = get_valid_amount("Amount: $")
    transactions.append((description, amount, "Income"))
    print(f"Added income: +${amount:.2f}")


def add_expense(transactions, categories):
    description = input("Description: ").strip() or "Expense"
    amount = get_valid_amount("Amount: $")
    category = input("Category: ").strip().title() or "Uncategorized"
    transactions.append((description, -amount, category))
    categories[category] = categories.get(category, 0) + amount
    print(f"Recorded expense: -${amount:.2f} [{category}]")


def get_balance(transactions):
    return sum(amount for _, amount, _ in transactions)


def show_history(transactions):
    if not transactions:
        print("No transactions yet.")
        return

    print("\n--- Transaction History ---")
    for index, (description, amount, category) in enumerate(transactions, start=1):
        sign = "+" if amount > 0 else ""
        print(f"  {index}. [{category}] {description}: {sign}${amount:.2f}")


def show_category_totals(categories):
    if not categories:
        print("No spending categories yet.")
        return

    print("\n--- Spending By Category ---")
    for category, total in sorted(categories.items()):
        print(f"  {category}: ${total:.2f}")


def main():
    transactions = []
    categories = {}

    print("=" * 44)
    print("   Personal Budget Tracker - Week 8")
    print("=" * 44)

    while True:
        display_menu()
        choice = input("\nChoose an option: ").strip()

        match choice:
            case "1":
                add_income(transactions)
            case "2":
                add_expense(transactions, categories)
            case "3":
                print(f"Current balance: ${get_balance(transactions):.2f}")
            case "4":
                show_history(transactions)
            case "5":
                show_category_totals(categories)
            case "6":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please choose 1-6.")


if __name__ == "__main__":
    main()