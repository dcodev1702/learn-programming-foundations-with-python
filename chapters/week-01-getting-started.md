# Week 1 — Getting Started & Your First Program

[Back to Learning Plan](../python_learning_plan.md)

---

## Topics

- What is programming? How does Python work?
- Installing Python 3.13 and setting up VS Code (or your preferred editor)
- Running your first script
- The `print()` function and string basics
- Comments

## Concept Guide

Programming is the process of giving a computer a clear set of instructions. If that sounds abstract right now, that is normal. A Python program is just a text file containing those instructions.

When you run a Python file, the Python interpreter reads your code from top to bottom and executes it step by step.

- A **script** is a Python file such as `budget_tracker.py`.
- A **statement** is one instruction, such as `print("Hello")`.
- A **syntax error** means Python could not understand your code.
- A **comment** is a note for humans. Python ignores it.

Comments are useful when they explain *why* something exists, not when they repeat what the code already says.

## Why `print()` Matters

`print()` is your first debugging tool. It lets you see what your program is doing.

- Use it to display messages to the user.
- Use it to check whether a variable contains what you expect.
- Use it to understand the order in which your code runs.

## Examples

```python
# Your very first Python program
print("Hello, World!")

# Printing multiple things
print("My name is Alex.")
print("I am learning Python!")

# Comments explain your code — Python ignores them
# This line won't run, but it helps humans understand your code
```

```python
# Python runs from top to bottom
print("Step 1")
print("Step 2")
print("Step 3")
```

```python
# Comments should add useful context
print("Budget Tracker")

# Good comment: explains intent
print("=" * 40)
```

## Project Step

Create `budget_tracker.py` and print a welcome banner:

```python
# budget_tracker.py — Your Personal Budget Tracker
print("=" * 40)
print("   Welcome to My Budget Tracker!")
print("=" * 40)
print("Track your income and expenses easily.")
```

## Try It Yourself

1. Change the banner text so it uses your own name.
2. Add a line that prints today's goal, such as `Add your first transaction`.
3. Add one comment explaining why the banner is helpful for the user.

## What to Notice

- Each `print()` call does one small job.
- Strings are wrapped in quotes.
- Your program is already becoming an interface for the user.
- Small programs are easier to understand than one big block of code.

## Common Mistakes

- Forgetting quotes around text, which causes Python to treat the text like a variable name.
- Changing indentation randomly. Even simple programs should be kept neat.
- Expecting comments to run. Comments are ignored by Python.
- Feeling like the program is too small to matter. These first steps are the base for everything that follows.

## Recap Questions

1. What does `print()` do?
2. What is the difference between code and a comment?
3. What does it mean that Python runs code from top to bottom?

## Ready to Move On?

- I can create and run a simple Python file.
- I can use `print()` to show output.
- I understand that comments are for humans, not Python.
- I can explain the order in which Python reads simple code.

---

**Next:** [Week 2 — Variables & Data Types](week-02-variables-and-data-types.md)
