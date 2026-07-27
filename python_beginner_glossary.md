# Python Beginner Glossary

[Back to Learning Plan](python_learning_plan.md)

---

## Variable

A named place to store a value so your program can use it later.

## Data Type

The kind of value something is, such as text, a whole number, or a decimal number.

## Identifier

A valid name you give to something in Python, such as a variable, function, or class.

## Keyword

A reserved word that Python already uses as part of the language, such as `if`, `class`, `def`, or `return`.

## String

Text data, written inside quotes.

## Integer

A whole number, such as `3`, `25`, or `-10`.

## Float

A number with a decimal point, such as `2.5` or `19.99`.

## Boolean

A value that is either `True` or `False`.

## Condition

An expression that evaluates to `True` or `False`.

## Conditional

Code that makes decisions, usually with `if`, `elif`, and `else`.

## Loop

Code that repeats.

## Iteration

One single pass through a loop.

## List

An ordered, changeable collection of values.

## Tuple

An ordered collection of values that cannot be changed after it is created.

## Dictionary

A collection of key-value pairs.

## Set

A collection of unique values.

## Mutable

Able to be changed after creation.

## Immutable

Not able to be changed after creation.

## Function

A reusable block of code that can take input, do work, and optionally return a result.

## Parameter

A variable listed in a function definition.

## Argument

A real value passed into a function when it is called.

## Return Value

The result a function sends back with `return`.

## Scope

The part of a program where a variable can be used.

## Class

A blueprint for creating objects.

## Object

A specific instance created from a class.

## Attribute

Data stored on an object.

## Method

A function that belongs to a class.

## Instance

Another word for an object created from a class.

## Encapsulation

Keeping related data and behavior together inside one class.

## Inheritance

Creating a new class based on an existing class.

## JSON

A common text format for storing structured data such as lists and dictionaries.

## File I/O

Reading data from files and writing data to files.

## Exception

An error that happens while a program is running.

## `try` / `except`

Python tools for handling exceptions without crashing immediately.

## `match` / `case`

Python syntax for choosing between several fixed options based on one value.

## `self`

The name used inside a class method to refer to the current object.

## `__name__` / `if __name__ == "__main__":`

`__name__` is a variable Python sets for every file. It holds `"__main__"` when that file is the one you ran, and the module's name when the file was imported by something else. The `if` guard therefore means "only run this when I am the program, not when I am being imported".

## Module

A single Python file that can be imported and reused by another file.

## Docstring

The string on the first line inside a function, class, or module. It describes what the thing does and shows up in `help()` and in editor tooltips.

## f-string

A string prefixed with `f` that can contain expressions inside braces, such as `f"Total: ${amount:.2f}"`.

## Indentation

The leading spaces that tell Python which lines belong to a block. Four spaces per level is the convention.

## Block

A group of lines that belong together because they share the same indentation, such as the body of an `if`, a loop, or a function.

## Namespace

The mapping of names to objects that Python searches when you use a name. Each function call gets its own.

## Frame

The temporary workspace Python creates for a single function call. It holds that call's local names and is thrown away when the function returns.

## Traceback

The report Python prints when an error is not handled. Read it from the bottom: the last line is the error type and message, and the line above it points at your code.

## REPL

The interactive Python prompt you get by typing `python` with no filename. Useful for trying one line at a time.

## Context Manager

An object used with the `with` statement that guarantees cleanup, such as the file object returned by `open()`.

## CSV

A plain-text table format with one record per line and commas between fields. Spreadsheets open it directly, but every value read back is a string.

## `None`

Python's "no value" object. It is falsy, and it is what a function returns when it has no `return` statement.

---

Use this glossary whenever a chapter introduces a word that feels unfamiliar.