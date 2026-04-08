# Week 4 — Pattern Matching with `match` (Python's Switch)

[Back to Learning Plan](../python_learning_plan.md)

---

## Topics

- The `match`/`case` statement (introduced in Python 3.10)
- Matching literal values
- The wildcard `_` pattern (default case)
- When to use `match` vs. `if/elif`

## Concept Guide

`match` is useful when one value can lead to many clear choices. If `if` statements started feeling repetitive last week, this feature solves that problem in some situations.

It works especially well for menus, commands, and fixed option lists.

```python
choice = "2"

match choice:
    case "1":
        print("Add income")
    case "2":
        print("Add expense")
    case _:
        print("Invalid choice")
```

Python checks each `case` from top to bottom until it finds a match.

The `_` case is the fallback. It is similar to `else` in an `if` statement.

## When to Use `match` vs. `if`

Use `match` when:

- you are comparing the same value many times
- the options are fixed and easy to list
- you want a menu to read cleanly

Use `if` when:

- conditions involve ranges like `score >= 90`
- conditions combine logic with `and` or `or`
- each branch checks something different

## Examples

```python
# match/case works great for menu-style choices
command = input("Enter a command (start/stop/status/quit): ").lower()

match command:
    case "start":
        print("Starting the system...")
    case "stop":
        print("Stopping the system...")
    case "status":
        print("System is running normally.")
    case "quit":
        print("Goodbye!")
    case _:
        print(f"Unknown command: '{command}'")

# Matching with multiple values using |
day = input("Enter a day of the week: ").lower()

match day:
    case "saturday" | "sunday":
        print("It's the weekend!")
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("It's a weekday.")
    case _:
        print("That's not a valid day.")
```

```python
# match keeps menu code easier to scan
menu_choice = input("Choose A, B, or C: ").upper()

match menu_choice:
    case "A":
        print("You picked option A")
    case "B":
        print("You picked option B")
    case "C":
        print("You picked option C")
    case _:
        print("That option does not exist")
```

## Project Step

Start with your Week 3 tracker and replace the menu decision logic with `match` so the options are easier to read:

```python
balance = 0.0

print("\n--- Budget Tracker Menu ---")
print("1. Add Income")
print("2. Add Expense")
print("3. View Balance")
print("4. Quit")

choice = input("\nSelect an option (1-4): ")

match choice:
    case "1":
        amount = float(input("Income amount: $"))
        balance += amount
        print(f"Added ${amount:.2f} income.")
    case "2":
        amount = float(input("Expense amount: $"))
        balance -= amount
        print(f"Recorded ${amount:.2f} expense.")
    case "3":
        print(f"Current balance: ${balance:.2f}")
    case "4":
        print("Goodbye!")
    case _:
        print("Invalid option. Please choose 1-4.")
```

## Try It Yourself

1. Add a fifth option that prints a short help message.
2. Create a separate `match` example that responds to days of the week or letter grades.
3. Change the menu so the user can type words like `income` and `expense` instead of numbers.

## What to Notice

- `choice` is checked once, then compared against several fixed values.
- Each `case` handles one user option.
- The wildcard `_` prevents the program from silently ignoring bad input.
- `match` makes menu code easier to read than a long chain of `elif` statements.

## Common Mistakes

- Using `match` for range checks like `score > 90`, where `if` is usually a better tool.
- Forgetting the wildcard `_` case, which leaves invalid input unhandled.
- Expecting `match` to be better for every situation. It is best for fixed choices.
- Forgetting that `case` values must match the type of the value being checked.

## Recap Questions

1. When is `match` a better fit than `if` / `elif`?
2. What does the `_` case do?
3. Why is `match` useful for menus?

## Ready to Move On?

- I can use `match` to handle fixed menu choices.
- I know when `if` is a better fit than `match`.
- I remember to include a fallback case for invalid input.
- I can trace which `case` block will run for a given value.

---

**Previous:** [Week 3 — Making Decisions](week-03-if-elif-else.md)
**Next:** [Week 5 — Loops](week-05-loops.md)
