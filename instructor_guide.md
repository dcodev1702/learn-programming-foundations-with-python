# Python Programming & OOP — Instructor Guide

[Back to Learning Plan](python_learning_plan.md)

---

## How to Use This Guide

This guide is meant to support teaching, discussion, and review. The suggested answers below are not the only acceptable answers, especially for the mini-exercises. Use them as a reference point rather than a script.

## Week 1 — Getting Started

### Suggested Answers: Recap Questions

1. `print()` displays output to the screen.
2. Code gives Python instructions; comments are notes for humans and are ignored by Python.
3. Python executes statements from top to bottom unless control flow changes that order.

### Suggested Answers: Try It Yourself

1. Any custom banner text is fine if it still uses valid strings and `print()`.
2. The extra line should use `print()` and display a clear goal.
3. The comment should explain purpose, not repeat obvious code.

## Week 2 — Variables & Data Types

### Suggested Answers: Recap Questions

1. A variable stores a value under a name.
2. `input()` returns a string, so numbers must often be converted before math.
3. A valid variable name uses letters, numbers, or underscores, does not start with a number, and is not a keyword.
4. A good variable name is clear and descriptive, not just technically valid.

### Suggested Answers: Try It Yourself

1. Good examples: `category`, `monthly_budget`, `expense_total`.
2. Invalid examples: `2amount`, `class`, `total cost`.
3. The sum example should collect input, convert values, and print a formatted result.

## Week 3 — Conditionals

### Suggested Answers: Recap Questions

1. A condition is an expression that becomes `True` or `False`.
2. `elif` is used when choices are connected and only one branch should run.
3. `=` assigns a value; `==` compares values.
4. Examples of falsy values include `0`, `0.0`, `""`, `[]`, and `None`.

### Suggested Answers: Try It Yourself

1. A large-expense warning should be another `if` check after the amount is known.
2. The zero-balance message should check `balance == 0`.
3. Any clear pass/fail rule is fine if the condition is correct.

## Week 4 — Pattern Matching

### Suggested Answers: Recap Questions

1. `match` is useful when one value maps to many fixed choices.
2. The `_` case is the fallback when nothing else matches.
3. It makes menu logic easier to scan and organize.

### Suggested Answers: Try It Yourself

1. The new option should appear in the menu and in a `case` branch.
2. A separate day-or-grade example should compare one value against several fixed cases.
3. Word-based commands should still be normalized with `.lower()` or `.strip()`.

## Week 5 — Loops

### Suggested Answers: Recap Questions

1. A `while` loop repeats while a condition stays true; a `for` loop iterates over a sequence.
2. `break` exits the loop immediately.
3. `continue` skips the rest of the current iteration and moves to the next one.
4. `while True:` is safe when there is a clear `break` path.

### Suggested Answers: Try It Yourself

1. The action counter should increase once per completed menu action.
2. The number loop should show correct use of `range()` and an even-number check.
3. The password loop should stop only when the correct value is entered.

## Week 6 — Lists & Tuples

### Suggested Answers: Recap Questions

1. Lists are mutable; tuples are immutable.
2. Python indexes from `0`, so the first item is at position `0`.
3. A list is better when you need to store many values of the same kind or grow over time.
4. `enumerate()` provides both an index and a value during iteration.

### Suggested Answers: Try It Yourself

1. The expense-only option should loop through transactions and filter negative amounts.
2. Adding a note or date is fine if the tuple structure stays consistent.
3. The sample loop should show `enumerate()` and unpacking correctly.

## Week 7 — Dictionaries & Sets

### Suggested Answers: Recap Questions

1. A dictionary is better when values are looked up by label rather than position.
2. A key-value pair connects a name to a value.
3. A set is useful when only unique items should be kept.
4. `.get()` avoids errors when a key might not exist.

### Suggested Answers: Try It Yourself

1. The highest-total option can use `max(categories, key=categories.get)` or a loop.
2. The set example should collect category names without duplicates.
3. The default category should be used when the user enters blank input.

## Week 8 — Functions

### Suggested Answers: Recap Questions

1. A parameter appears in the function definition; an argument is the value passed in.
2. `print()` displays output; `return` sends a value back to the caller.
3. Lists can change outside the function because they are mutable objects.
4. A good function name clearly describes an action.

### Suggested Answers: Try It Yourself

1. The expense-count function should loop or use `sum()` to count negative transactions.
2. The category filter should take a category as a parameter.
3. The positive-number function should use a loop and input validation.

## Week 9 — Intro to OOP

### Suggested Answers: Recap Questions

1. A class is a blueprint; an object is an instance created from it.
2. `__init__` sets starting values when an object is created.
3. `self` refers to the current object.
4. `Transaction` is clearer because it describes what the object represents.

### Suggested Answers: Try It Yourself

1. An `is_income()` method can return `self.amount >= 0`.
2. A dictionary method should return the object's fields in key-value form.
3. A second class is acceptable if it has a clear purpose and meaningful names.

## Week 10 — Encapsulation

### Suggested Answers: Recap Questions

1. Encapsulation means keeping related data and behavior together.
2. It helps the class manage its own rules and reduces scattered logic.
3. `__str__` controls how an object is shown as text.
4. A list of objects keeps structured data and behavior together.

### Suggested Answers: Try It Yourself

1. The expense-count method should live on `BudgetTracker`.
2. The category filter method should search inside the tracker's transactions.
3. The `main()` function should create a tracker and call methods in a readable order.

## Week 11 — File I/O

### Suggested Answers: Recap Questions

1. `with open(...)` closes files automatically and safely.
2. JSON works well because the tracker stores structured data.
3. `try` / `except` handles runtime errors gracefully.
4. Missing files should be handled without crashing, often by starting fresh.

### Suggested Answers: Try It Yourself

1. The date can be added as another transaction field and included in save/load methods.
2. `json.JSONDecodeError` should show a friendly recovery message.
3. Changing the filename should still preserve the same save/load logic.

## Week 12 — Final Project

### Suggested Answers: Recap Questions

1. Inheritance lets a child class reuse or extend a parent class.
2. `super()` calls behavior from the parent class.
3. Overriding replaces inherited behavior with a specialized version.
4. The final tracker uses variables, conditionals, loops, functions, classes, file I/O, and naming conventions from earlier weeks.

### Suggested Answers: Try It Yourself

1. A budget-limit feature should compare category totals against a stored limit.
2. The search feature should check each transaction description for a keyword.
3. A subclass or helper class is fine if it adds one focused feature without making the design harder to follow.

## Teaching Notes

- Encourage learners to explain code out loud before editing it.
- Prefer small corrections over rewriting a student's whole program.
- If a learner is stuck, narrow the problem to one value, one condition, or one loop at a time.
- Ask learners to justify names. Good naming is part of understanding.

---

This guide is meant to support judgment, not replace it.