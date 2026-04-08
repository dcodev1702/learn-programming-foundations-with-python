# Week 3 — Making Decisions with `if` / `elif` / `else`

[Back to Learning Plan](../python_learning_plan.md)

---

## Topics

- Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
- `if`, `elif`, and `else` statements
- Logical operators: `and`, `or`, `not`
- Nested conditionals
- Truthy and falsy values

## Concept Guide

Programs become useful when they can make decisions. This is the point where your code starts reacting instead of just printing fixed output.

An `if` statement tells Python: *only run this block if a condition is true*.

```python
age = 18

if age >= 18:
    print("You are an adult.")
```

The condition `age >= 18` evaluates to either `True` or `False`.

- `if` checks the first condition.
- `elif` means "otherwise, if this other condition is true".
- `else` means "if none of the earlier conditions matched".

Only one branch runs in a single `if` / `elif` / `else` chain.

## How to Read Conditions

```python
if amount > 0:
    print("Income")
```

Read that as: "If `amount` is greater than `0`, then print `Income`."

Comparison operators:

- `==`: equal to
- `!=`: not equal to
- `>`: greater than
- `<`: less than
- `>=`: greater than or equal to
- `<=`: less than or equal to

## Logical Operators

- `and`: both conditions must be true
- `or`: at least one condition must be true
- `not`: flips true to false, or false to true

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed in")
```

## Truthy and Falsy Values

Some values behave like `False` in a condition:

- `0`
- `0.0`
- `""` (empty string)
- `[]` (empty list)
- `None`

Everything else is usually treated as true.

## Examples

```python
# Simple if/else
temperature = 72

if temperature > 85:
    print("It's hot outside! Stay hydrated.")
elif temperature > 65:
    print("Nice weather today!")
else:
    print("It's a bit chilly. Grab a jacket.")

# Combining conditions with and/or
age = 20
has_id = True

if age >= 18 and has_id:
    print("You may enter.")
else:
    print("Sorry, entry denied.")

# Checking user input
answer = input("Do you like Python? (yes/no): ").lower()

if answer == "yes":
    print("Great, you'll love this course!")
elif answer == "no":
    print("Give it a chance — it grows on you!")
else:
    print("I'll take that as a maybe.")
```

```python
# A condition can check for missing data
name = input("Enter your name: ").strip()

if name:
    print(f"Hello, {name}!")
else:
    print("You didn't type a name.")
```

```python
# Be careful with indentation
score = 82

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Keep practicing.")
```

## Project Step

Classify transactions as income or expense and validate input:

```python
balance = 0.0

description = input("Enter a transaction description: ")
amount = float(input("Enter the amount: "))
trans_type = input("Is this (i)ncome or (e)xpense? ").lower()

if trans_type == "i":
    balance += amount
    print(f"Income added: +${amount:.2f}")
elif trans_type == "e":
    balance -= amount
    print(f"Expense recorded: -${amount:.2f}")
else:
    print("Invalid type! Please enter 'i' or 'e'.")

if balance < 0:
    print(f"Warning: You're in the red! Balance: ${balance:.2f}")
else:
    print(f"Current balance: ${balance:.2f}")
```

## Try It Yourself

1. Add a warning message when an expense is larger than `$100`.
2. Add another condition that prints a message when the balance becomes exactly `0`.
3. Ask the user for a score and print `Pass` or `Fail` based on a rule you choose.

## What to Notice

- The program asks a question, then responds differently depending on the answer.
- Conditions make your program interactive and safer.
- The `else` branch catches unexpected cases.
- A second `if` statement can run after the first one if you need an additional check.

## Common Mistakes

- Using `=` instead of `==` when checking equality.
- Forgetting the colon `:` at the end of an `if`, `elif`, or `else` line.
- Misaligning indentation so the wrong block runs.
- Writing several separate `if` statements when one `if` / `elif` / `else` chain would be clearer.

## Recap Questions

1. What is a condition?
2. When would you use `elif` instead of a new `if`?
3. What is the difference between `=` and `==`?
4. What kinds of values count as falsy in Python?

## Ready to Move On?

- I can write `if`, `elif`, and `else` blocks with correct indentation.
- I can compare values using operators like `==`, `>`, and `<=`.
- I can explain the difference between assignment and comparison.
- I can use conditions to make a program respond differently to user input.

---

**Previous:** [Week 2 — Variables & Data Types](week-02-variables-and-data-types.md)
**Next:** [Week 4 — Pattern Matching](week-04-match-case.md)
