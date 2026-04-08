# Week 6 — Lists & Tuples

[Back to Learning Plan](../python_learning_plan.md)

---

## Topics

- Creating and accessing lists
- List methods: `append()`, `remove()`, `pop()`, `sort()`, `insert()`
- Looping through lists
- List slicing
- Tuples: immutable sequences
- `len()`, `sum()`, `min()`, `max()`

## Concept Guide

A list stores multiple values in one variable. This is where your programs start handling groups of data instead of just one value at a time.

```python
fruits = ["apple", "banana", "cherry"]
```

Lists are **ordered** and **mutable**.

- **Ordered** means items keep their position.
- **Mutable** means you can change the list after creating it.

This is different from a tuple.

```python
coordinates = (40.7128, -74.0060)
```

Tuples are ordered too, but they are **immutable**, which means they cannot be changed after creation.

## Index Positions

List positions start at `0`, not `1`.

```python
colors = ["red", "green", "blue"]
print(colors[0])   # red
print(colors[1])   # green
print(colors[2])   # blue
```

Negative indexes count from the end.

```python
print(colors[-1])  # blue
```

## Mutability Matters

Because lists are mutable, methods like `append()` and `remove()` change the original list.

```python
items = [1, 2, 3]
items.append(4)
print(items)   # [1, 2, 3, 4]
```

This becomes important later when you pass lists to functions.

## Examples

```python
# Lists — ordered, mutable collections
fruits = ["apple", "banana", "cherry"]
print(fruits[0])    # "apple"
print(fruits[-1])   # "cherry" (last item)

fruits.append("mango")
fruits.remove("banana")
print(fruits)  # ["apple", "cherry", "mango"]

# Looping through a list
scores = [85, 92, 78, 95, 88]
for score in scores:
    print(f"Score: {score}")

print(f"Average: {sum(scores) / len(scores):.1f}")

# List slicing
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])   # [1, 2, 3]
print(numbers[:3])    # [0, 1, 2]
print(numbers[3:])    # [3, 4, 5]

# Tuples — like lists but immutable (can't be changed)
coordinates = (40.7128, -74.0060)
print(f"Lat: {coordinates[0]}, Lon: {coordinates[1]}")
```

```python
# A list can hold mixed types, but keeping similar data together is usually clearer
record = ["Groceries", -52.30, "Food"]
print(record[0])
print(record[1])
print(record[2])
```

```python
# Slicing creates a new list with part of the original
letters = ["a", "b", "c", "d", "e"]
print(letters[1:4])   # ['b', 'c', 'd']
```

## Project Step

Take your Week 5 tracker and start storing each transaction in a list so users can review past activity:

```python
balance = 0.0
transactions = []  # Each item will be a tuple: (description, amount, category)

while True:
    print("\n--- Menu ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transaction History")
    print("5. Quit")

    choice = input("\nSelect an option: ")

    match choice:
        case "1":
            desc = input("Description: ")
            amount = float(input("Amount: $"))
            balance += amount
            transactions.append((desc, amount, "Income"))
        case "2":
            desc = input("Description: ")
            amount = float(input("Amount: $"))
            category = input("Category: ").title()
            balance -= amount
            transactions.append((desc, -amount, category))
        case "3":
            print(f"Current balance: ${balance:.2f}")
        case "4":
            if not transactions:
                print("No transactions yet.")
            else:
                print("\n--- Transaction History ---")
                for i, (desc, amt, category) in enumerate(transactions, start=1):
                    sign = "+" if amt > 0 else "-"
                    print(f"  {i}. [{category}] {desc}: {sign}${abs(amt):.2f}")
        case "5":
            break
        case _:
            print("Invalid choice. Try again.")
```

## Try It Yourself

1. Add a menu option that prints only expense transactions.
2. Add another tuple field, such as a short note or date string.
3. Create a small list of three sample transactions and loop through it with `enumerate()`.

## What to Notice

- `transactions` is a list because the number of transactions can grow.
- Each transaction is stored as a tuple because each record has a fixed structure.
- `enumerate()` gives both the position and the value during a loop.
- Lists are often the main container for program data.

## Common Mistakes

- Forgetting that indexing starts at `0`.
- Trying to change a tuple after it has been created.
- Mixing too many unrelated kinds of data in one list without a clear structure.
- Forgetting that list methods such as `append()` change the original list.

## Recap Questions

1. What is the difference between a list and a tuple?
2. Why does Python use index `0` for the first item?
3. When is a list a better choice than a single variable?
4. What does `enumerate()` add to a loop?

## Ready to Move On?

- I can create, read, and update a list.
- I know that tuples are fixed after creation.
- I can loop through a list and use `enumerate()` when needed.
- I can explain why a growing transaction history belongs in a list.

---

**Previous:** [Week 5 — Loops](week-05-loops.md)
**Next:** [Week 7 — Dictionaries & Sets](week-07-dictionaries-and-sets.md)
