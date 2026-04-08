# Week 12 — Inheritance, Polish & Final Project Assembly

[Back to Learning Plan](../python_learning_plan.md)

---

## Topics

- Inheritance: creating specialized classes from a base class
- The `super()` function
- Method overriding
- Putting it all together: clean code, final features, testing your app

## Concept Guide

Inheritance lets one class build on another. It is a useful idea to understand, even though not every project needs much of it.

You start with a more general class, then create specialized versions of it.

```python
class Animal:
    pass

class Dog(Animal):
    pass
```

`Dog` inherits from `Animal`, which means it can reuse behavior from the parent class.

## Why `super()` Matters

`super()` lets a child class call behavior from the parent class.

```python
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")
```

This avoids repeating the parent setup code.

## Method Overriding

Sometimes a child class needs to replace or customize behavior from the parent class.

```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")
```

That is called **overriding**.

## When to Use Inheritance Carefully

Inheritance is useful when one class is truly a specialized version of another.

It is not always necessary. In your budget tracker, most of the design strength comes from clear classes, methods, and composition. Inheritance is introduced here so you understand it, not because every project needs a deep class hierarchy.

## Examples

```python
# Inheritance — a child class gets everything from the parent
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")  # Call parent's __init__

    def purr(self):
        print(f"{self.name} purrs softly...")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

    def fetch(self, item):
        print(f"{self.name} fetches the {item}!")

kitty = Cat("Whiskers")
kitty.speak()   # Whiskers says Meow!
kitty.purr()    # Whiskers purrs softly...

doggo = Dog("Rex")
doggo.speak()   # Rex says Woof!
doggo.fetch("ball")  # Rex fetches the ball!
```

```python
# Overriding changes inherited behavior
class LoudDog(Dog):
    def speak(self):
        print(f"{self.name} says WOOF!!!")
```

## Project Step — Final Assembly

Start with your Week 11 version and finish the same budget tracker by adding validation, a polished main loop, and a few final quality improvements:

```python
import json


class Transaction:
    def __init__(self, description, amount, category="Income"):
        self.description = description
        self.amount = amount
        self.category = category

    def is_expense(self):
        return self.amount < 0

    def display(self, index):
        sign = "+" if self.amount >= 0 else ""
        print(f"  {index}. [{self.category}] {self.description}: {sign}${self.amount:.2f}")

    def to_dict(self):
        return {
            "description": self.description,
            "amount": self.amount,
            "category": self.category
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["description"], data["amount"], data["category"])


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
        return sum(t.amount for t in self.transactions)

    def show_history(self):
        if not self.transactions:
            print("  No transactions yet.")
            return
        for i, t in enumerate(self.transactions, 1):
            t.display(i)
        print(f"\n  Current Balance: ${self.get_balance():.2f}")

    def show_summary(self):
        income = sum(t.amount for t in self.transactions if t.amount > 0)
        expenses = sum(t.amount for t in self.transactions if t.amount < 0)
        balance = self.get_balance()
        print(f"\n  --- Summary for {self.owner} ---")
        print(f"  Total Income:    +${income:.2f}")
        print(f"  Total Expenses:  -${abs(expenses):.2f}")
        print(f"  Net Balance:      ${balance:.2f}")
        if balance < 0:
            print("  ** Warning: You are over budget! **")

    def spending_by_category(self):
        categories = {}
        for t in self.transactions:
            if t.is_expense():
                categories[t.category] = categories.get(t.category, 0) + abs(t.amount)
        if not categories:
            print("  No expenses recorded yet.")
            return
        print("\n  --- Spending by Category ---")
        for cat, total in sorted(categories.items()):
            print(f"  {cat}: ${total:.2f}")

    def save(self, filename="budget_data.json"):
        data = {
            "owner": self.owner,
            "transactions": [t.to_dict() for t in self.transactions]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"  Data saved to {filename}.")

    def load(self, filename="budget_data.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            self.owner = data["owner"]
            self.transactions = [
                Transaction.from_dict(t)
                for t in data["transactions"]
            ]
            print(f"  Welcome back, {self.owner}! Loaded {len(self.transactions)} transactions.")
        except FileNotFoundError:
            print("  No saved data found. Starting fresh!")


def get_valid_amount(prompt):
    """Keep asking until the user provides a valid positive number."""
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("  Please enter a positive number.")
                continue
            return amount
        except ValueError:
            print("  Invalid input. Please enter a number.")


def main():
    print("=" * 44)
    print("   Personal Budget Tracker v1.0")
    print("   Built with Python 3.13")
    print("=" * 44)

    name = input("\nEnter your name: ").strip() or "User"
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
                desc = input("  Description: ").strip()
                amount = get_valid_amount("  Amount: $")
                tracker.add_income(desc, amount)

            case "2":
                desc = input("  Description: ").strip()
                amount = get_valid_amount("  Amount: $")
                category = input("  Category (e.g., Food, Transport, Bills): ").strip().title()
                tracker.add_expense(desc, amount, category or "Uncategorized")

            case "3":
                tracker.show_history()

            case "4":
                tracker.show_summary()

            case "5":
                tracker.spending_by_category()

            case "6":
                tracker.save()

            case "7":
                save_first = input("  Save before quitting? (y/n): ").lower()
                if save_first == "y":
                    tracker.save()
                print(f"\n  Goodbye, {tracker.owner}! Happy budgeting!")
                break

            case _:
                print("  Invalid option. Please choose 1-7.")


if __name__ == "__main__":
    main()
```

## Try It Yourself

1. Add a budget limit and warn the user when a category total goes over it.
2. Add a search option that finds transactions by keyword.
3. Create a small subclass or helper class that adds one focused feature without changing the rest of the design too much.

## Final Build Checklist

- Your variable names should be clear and specific.
- Your function names should describe actions.
- Your class names should describe things or entities.
- Input should be validated before it is trusted.
- Repeated logic should be moved into functions or methods.
- Saved data should load without breaking the program.
- The menu should keep working until the user chooses to quit.

## What to Notice

- The final program combines variables, conditionals, loops, functions, classes, and file handling.
- Real programs are built from many small ideas working together.
- Clean naming and clear structure matter just as much as syntax.
- You now have a foundation strong enough to build more than one project.

## Common Mistakes

- Using inheritance where a simple helper class or method would be enough.
- Repeating code in a child class instead of using `super()` when appropriate.
- Skipping validation because the final program feels "done".
- Treating the final project like an endpoint instead of a base to improve.

## Recap Questions

1. What does inheritance allow a child class to do?
2. What is `super()` used for?
3. What does it mean to override a method?
4. Which earlier concepts show up in the final budget tracker?

## Ready to Move On?

- I can explain inheritance and recognize when it is useful.
- I can trace how the final project uses ideas from earlier weeks.
- I can run, test, save, and load the final budget tracker.
- I can identify at least one feature I could add next on my own.

---

**Previous:** [Week 11 — File I/O](week-11-file-io.md)
**Next:** [Bonus Challenges & Tips](bonus-challenges-and-tips.md)
