# Week 11 — File I/O: Saving & Loading Data

[Back to Learning Plan](../python_learning_plan.md)

---

## Topics

- Reading from and writing to text files
- The `with` statement (context managers)
- Working with CSV files using the `csv` module
- The `json` module: saving and loading structured data
- Error handling with `try`/`except`

## Concept Guide

Programs become much more useful when they can save data and load it later. This is what turns your tracker from a temporary exercise into something a person could actually use more than once.

Without file I/O, your budget tracker forgets everything as soon as the program ends.

## Why `with open(...)` Is Used

```python
with open("notes.txt", "w") as f:
    f.write("Hello")
```

The `with` statement opens the file and makes sure it is properly closed when you are done.

That is safer than opening a file and forgetting to close it yourself.

## Text vs. Structured Data

- Plain text files are good for simple lines of text.
- JSON files are good for structured data such as dictionaries and lists.

For a budget app, JSON is a better fit because transactions have multiple pieces of data.

## Error Handling in Plain English

Sometimes code fails for normal reasons.

- the file does not exist
- the user types invalid input
- data is not in the format you expected

`try` / `except` lets your program handle those problems without crashing immediately.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That was not a valid whole number.")
```

## Examples

```python
# Writing to a file
with open("notes.txt", "w") as f:
    f.write("Line 1: Hello!\n")
    f.write("Line 2: Learning Python.\n")

# Reading from a file
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

# Working with JSON — great for saving structured data
import json

data = {"name": "Alex", "scores": [95, 88, 72]}

# Save to JSON file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Load from JSON file
with open("data.json", "r") as f:
    loaded = json.load(f)
    print(loaded["name"])  # "Alex"

# Error handling
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"Result: {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
```

```python
# You can save a list of dictionaries as JSON
transactions = [
    {"description": "Paycheck", "amount": 1200},
    {"description": "Groceries", "amount": -45}
]

with open("transactions.json", "w") as f:
    json.dump(transactions, f, indent=2)
```

## Project Step

Build directly on your Week 10 classes by teaching both `Transaction` and `BudgetTracker` how to save and load data cleanly:

```python
import json

class Transaction:
    def __init__(self, description, amount, category="Income"):
        self.description = description
        self.amount = amount
        self.category = category

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
    # ... (keep the methods from Week 10) ...

    def save(self, filename="budget_data.json"):
        """Save all transactions to a JSON file."""
        data = [t.to_dict() for t in self.transactions]
        with open(filename, "w") as f:
            json.dump({"owner": self.owner, "transactions": data}, f, indent=2)
        print(f"Data saved to {filename}!")

    def load(self, filename="budget_data.json"):
        """Load transactions from a JSON file."""
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            self.owner = data["owner"]
            self.transactions = [
                Transaction.from_dict(item)
                for item in data["transactions"]
            ]
            print(f"Loaded {len(self.transactions)} transactions.")
        except FileNotFoundError:
            print("No saved data found. Starting fresh!")
```

## Try It Yourself

1. Add the date to each saved transaction and load it back in.
2. Add an `except json.JSONDecodeError` block with a friendly message.
3. Change the default filename and test saving twice.

## What to Notice

- Saving and loading are now part of the class behavior.
- JSON matches your data model better than plain text.
- `try` / `except` turns common failures into manageable situations.
- Good programs do not just work in perfect conditions; they handle mistakes gracefully.

## Common Mistakes

- Forgetting to open the file in the correct mode, such as `"r"` or `"w"`.
- Assuming a file will always exist.
- Catching errors without understanding what might have caused them.
- Saving data in a format that does not match how the program needs to use it later.

## Recap Questions

1. Why is `with open(...)` safer than opening a file manually?
2. Why is JSON a good fit for the budget tracker?
3. What problem does `try` / `except` solve?
4. What happens if you try to load a file that is missing?

## Ready to Move On?

- I can read from and write to files using `with`.
- I understand why JSON fits structured program data.
- I can save and load tracker data without changing its meaning.
- I can handle common file errors without crashing the program.

---

**Previous:** [Week 10 — OOP Continued](week-10-encapsulation.md)
**Next:** [Week 12 — Inheritance & Final Assembly](week-12-inheritance-and-final-project.md)
