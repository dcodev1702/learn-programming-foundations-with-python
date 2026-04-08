# Week 8 — Functions

[Back to Learning Plan](../python_learning_plan.md)

---

## Topics

- Defining functions with `def`
- Parameters and arguments
- Return values
- Default parameter values
- Scope: local vs. global variables
- Docstrings

## Concept Guide

Functions let you group reusable code under a name. Once you start using them well, your programs become much easier to read and extend.

Instead of rewriting the same logic many times, you define it once and call it when needed.

```python
def greet(name):
    print(f"Hello, {name}!")
```

In that example:

- `greet` is the function name
- `name` is a parameter
- `greet("Alex")` is a function call
- `"Alex"` is an argument

## Good Function Names

Function names should usually describe an action.

Good names:

```python
calculate_total()
show_menu()
save_data()
```

Less helpful names:

```python
do_it()
thing()
stuff()
```

Choose names that tell the reader what the function does.

## Parameters vs. Return Values

Parameters are inputs to the function.

Return values are outputs from the function.

```python
def square(number):
    return number * number
```

This function takes in one value and returns one value.

## Scope: Local vs. Global

Variables created inside a function are usually local to that function.

```python
def example():
    message = "inside"
    print(message)
```

`message` exists only inside `example()`.

Keeping data local helps prevent accidental bugs.

## How Arguments Behave in Python

Beginners often hear the phrase "pass by value". Python works a little differently.

Python passes references to objects into functions.

For practical beginner use, remember this:

- Reassigning a number or string inside a function does **not** change the original variable outside.
- Modifying a list or dictionary inside a function **can** change the original object outside.

Example with an immutable value:

```python
def add_one(number):
    number = number + 1
    print(f"Inside function: {number}")

score = 10
add_one(score)
print(f"Outside function: {score}")
```

Output:

- inside the function, `number` becomes `11`
- outside the function, `score` is still `10`

Example with a mutable value:

```python
def add_item(items):
    items.append("new")

shopping = ["milk", "bread"]
add_item(shopping)
print(shopping)
```

After the function call, `shopping` has changed.

This is why mutability matters.

## Examples

```python
# A simple function
def greet(name):
    """Greet someone by name."""
    print(f"Hello, {name}! Welcome aboard.")

greet("Alex")
greet("Sam")

# Function with a return value
def calculate_tip(bill, tip_percent=18):
    """Calculate the tip amount for a bill."""
    tip = bill * (tip_percent / 100)
    return tip

my_tip = calculate_tip(50)        # Uses default 18%
print(f"Tip: ${my_tip:.2f}")      # Tip: $9.00

big_tip = calculate_tip(50, 25)   # Override with 25%
print(f"Tip: ${big_tip:.2f}")     # Tip: $12.50

# Functions can return multiple values
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([4, 8, 1, 9, 3])
print(f"Min: {low}, Max: {high}")
```

```python
# A function can do one clear job and return a result
def format_currency(amount):
    return f"${amount:.2f}"

print(format_currency(12.5))
```

```python
# Default parameters make some inputs optional
def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_user("Alex")
greet_user("Sam", "Welcome")
```

## Project Step

Take your Week 7 tracker and move the repeated logic into functions so the main loop becomes easier to follow:

```python
def display_menu():
    """Show the main menu options."""
    print("\n--- Budget Tracker Menu ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transaction History")
    print("5. View Spending by Category")
    print("6. Quit")

def add_income(transactions):
    """Prompt the user for an income transaction."""
    desc = input("Description: ")
    amount = float(input("Amount: $"))
    transactions.append((desc, amount, "Income"))

def add_expense(transactions, categories):
    """Prompt the user for an expense transaction."""
    desc = input("Description: ")
    amount = float(input("Amount: $"))
    category = input("Category: ").title() or "Uncategorized"
    transactions.append((desc, -amount, category))
    categories[category] = categories.get(category, 0) + amount

def get_balance(transactions):
    """Calculate the current balance from all transactions."""
    return sum(amount for _, amount, _ in transactions)

def show_history(transactions):
    """Display all transactions."""
    if not transactions:
        print("No transactions yet.")
        return
    for i, (desc, amt, cat) in enumerate(transactions, 1):
        sign = "+" if amt > 0 else ""
        print(f"  {i}. [{cat}] {desc}: {sign}${amt:.2f}")

def show_category_totals(categories):
    """Display category totals."""
    if not categories:
        print("No category data yet.")
        return
    for category, total in sorted(categories.items()):
        print(f"  {category}: ${total:.2f}")

transactions = []
categories = {}

while True:
    display_menu()
    choice = input("\nChoose an option: ")

    match choice:
        case "1":
            add_income(transactions)
        case "2":
            add_expense(transactions, categories)
        case "3":
            print(f"Balance: ${get_balance(transactions):.2f}")
        case "4":
            show_history(transactions)
        case "5":
            show_category_totals(categories)
        case "6":
            break
        case _:
            print("Invalid choice.")
```

## Try It Yourself

1. Write a function that counts how many expense transactions exist.
2. Add a function that prints only transactions from one category.
3. Write a small function that safely asks for a positive number and keeps asking until the user enters one.

## What to Notice

- Each function handles one responsibility.
- Smaller functions are easier to test and debug.
- Functions make the later OOP chapters easier, because methods are functions attached to classes.
- Naming matters here too: `display_menu()` is much clearer than a vague name like `menu1()`.

## Common Mistakes

- Printing inside a function when you really need to `return` a value.
- Using unclear function names that do not describe the action.
- Relying too much on global variables instead of passing data in as parameters.
- Assuming lists behave the same way as numbers when passed into functions.

## Recap Questions

1. What is the difference between a parameter and an argument?
2. What is the difference between `print()` and `return` inside a function?
3. Why can a list change outside a function when it is modified inside one?
4. What makes a function name good?

## Ready to Move On?

- I can define and call functions with parameters.
- I know when a function should `return` a value.
- I can explain the difference between local variables and outside data.
- I can break repeated program logic into smaller, clearly named functions.

---

**Previous:** [Week 7 — Dictionaries & Sets](week-07-dictionaries-and-sets.md)
**Next:** [Week 9 — Introduction to OOP](week-09-intro-to-oop.md)
