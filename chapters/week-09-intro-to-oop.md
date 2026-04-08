# Week 9 — Introduction to OOP: Classes & Objects

[Back to Learning Plan](../python_learning_plan.md)

---

## Topics

- What is Object-Oriented Programming and why does it matter?
- Classes vs. objects (blueprints vs. instances)
- The `__init__` method (constructor)
- Instance attributes and `self`
- Defining methods on a class

## Concept Guide

Object-Oriented Programming, or OOP, is a way of organizing code around **objects**. If it feels more abstract than the earlier chapters, that is normal at first.

An object combines:

- data, such as `description` or `amount`
- behavior, such as `display()` or `is_expense()`

This helps related code stay together.

## Classes vs. Objects

A **class** is a blueprint.

An **object** is one real thing created from that blueprint.

```python
class Dog:
    pass

my_dog = Dog()
```

`Dog` is the class. `my_dog` is an object created from that class.

## The Role of `__init__`

`__init__` runs when a new object is created. It is commonly used to give that object its starting data.

```python
class Dog:
    def __init__(self, name):
        self.name = name
```

`self` refers to the specific object being created or used.

## Good Class and Method Names

- Class names should usually be **PascalCase nouns**: `BudgetTracker`, `Transaction`, `BankAccount`
- Method names should usually be **lowercase_with_underscores** and describe an action: `add_income()`, `show_summary()`, `is_expense()`

Good names reduce confusion:

```python
class Transaction:
    pass

def display(self):
    pass
```

Those names are clearer than vague alternatives like `DataThing` or `doStuff()`.

## Examples

```python
# A class is a blueprint for creating objects
class Dog:
    def __init__(self, name, breed, age):
        self.name = name      # Instance attribute
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof!")

    def describe(self):
        print(f"{self.name} is a {self.age}-year-old {self.breed}.")

# Creating objects (instances) from the class
my_dog = Dog("Buddy", "Golden Retriever", 3)
your_dog = Dog("Luna", "Husky", 5)

my_dog.bark()        # Buddy says: Woof!
your_dog.describe()  # Luna is a 5-year-old Husky.
```

```python
# Each object gets its own data
dog_one = Dog("Buddy", "Golden Retriever", 3)
dog_two = Dog("Luna", "Husky", 5)

print(dog_one.name)
print(dog_two.name)
```

## Project Step

Keep your Week 8 functions, but replace raw transaction tuples with `Transaction` objects so each transaction can manage its own data and behavior:

```python
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

def add_income(transactions):
    desc = input("Description: ")
    amount = float(input("Amount: $"))
    transactions.append(Transaction(desc, amount, "Income"))

def add_expense(transactions):
    desc = input("Description: ")
    amount = float(input("Amount: $"))
    category = input("Category: ").title() or "Uncategorized"
    transactions.append(Transaction(desc, -amount, category))

def get_balance(transactions):
    return sum(t.amount for t in transactions)

def show_history(transactions):
    for i, transaction in enumerate(transactions, start=1):
        transaction.display(i)

# Usage
transactions = []
add_income(transactions)
add_expense(transactions)
show_history(transactions)
```

## Try It Yourself

1. Add a method that returns `True` when a transaction is income.
2. Add a method that returns a dictionary version of the transaction.
3. Create a second class, such as `Goal` or `Account`, and give it two attributes and one method.

## What to Notice

- A `Transaction` object keeps related data together.
- Methods such as `is_expense()` make your code easier to read later.
- OOP becomes useful when your data starts getting more complex than a simple tuple.
- The class name `Transaction` describes *what the thing is*.

## Common Mistakes

- Thinking a class and an object are the same thing.
- Forgetting to use `self` inside methods.
- Using weak class names that do not describe the object clearly.
- Creating a class when a simpler structure would still work.

## Recap Questions

1. What is the difference between a class and an object?
2. What does `__init__` do?
3. What does `self` refer to?
4. Why is `Transaction` a better class name than something vague?

## Ready to Move On?

- I can define a simple class with attributes and methods.
- I understand the difference between a class and an object.
- I can use `self` correctly inside a method.
- I can explain why objects can be clearer than raw tuples for structured data.

---

**Previous:** [Week 8 — Functions](week-08-functions.md)
**Next:** [Week 10 — OOP Continued](week-10-encapsulation.md)
