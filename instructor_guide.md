# Python Programming & OOP — Instructor Guide

[Back to Learning Plan](python_learning_plan.md)

---

## How to Use This Guide

This guide is meant to support teaching, discussion, and review. The suggested answers below are not the only acceptable answers, especially for the mini-exercises. Use them as a reference point rather than a script.

Each week has three parts:

- **Suggested Answers: Recap Questions** — what a solid answer contains.
- **Suggested Answers: Try It Yourself** — what a working attempt looks like.
- **What Students Usually Get Wrong** — the specific errors to watch for, and the
  question that unsticks them fastest. This is the part worth reading before class.

## The Reference Implementations

Three runnable files carry the project through the course. Each one is heavily
commented and tied to the chapters it came from.

| File | Milestone | Chapters |
|---|---|---|
| [budget_tracker_week8.py](budget_tracker_week8.py) | Functions, tuples, dictionaries | Weeks 6-8 |
| [budget_tracker_week10.py](budget_tracker_week10.py) | Classes and encapsulation | Weeks 9-10 |
| [budget_tracker_final.py](budget_tracker_final.py) | The finished app with save/load | Weeks 11-12 |

The comments use a small fixed set of symbols, so learners can skim for one kind of
information: 📌 what a block is · 🧠 the idea worth understanding · ⚠️ the trap
beginners hit · 🔁 loop mechanics · 🧮 signs and arithmetic · 🧱 OOP mechanics ·
💾 saving and loading.

### Chapter Listings vs. Reference Files

Students notice when two versions of "the same" program differ, and they are right
to ask. The differences are deliberate and small:

- **Week 8.** The reference adds `get_valid_amount()` (which is Try It Yourself #3),
  `.strip() or "Income"` fallbacks on the description prompts, a `main()` function,
  and the `if __name__ == "__main__":` guard. The chapter leaves these out so the
  listing stays focused on what a function *is*.
- **Week 10.** The reference adds `get_valid_amount()`, a `main()` with the
  interactive menu, and a `__str__` on `Transaction` as well as on `BudgetTracker`.
  The two classes themselves match the chapter line for line.
- **Week 12.** No behavioural differences at all. The reference is the chapter
  listing plus commentary.

Everything else is identical, including every printed message. If a student finds a
real difference in output, that is a bug worth reporting.

### One Money Format, All Twelve Weeks

From Week 6 onward, every transaction line is printed the same way:

```python
sign = "+" if amount >= 0 else "-"
print(f"  {index}. [{category}] {description}: {sign}${abs(amount):.2f}")
```

The sign is built by hand and the value is printed with `abs()`, so an expense reads
`-$52.30` rather than `$-52.30` with the minus stranded inside the number. If a
student's output has the minus in the wrong place, this is the line to look at.

### The Sign Convention

Income is stored **positive**, expenses are stored **negative**, from Week 3 to the
end. Almost every confusing bug in student code traces back to breaking this rule —
usually by storing an expense positive and then subtracting it somewhere else too.
The payoff is that `get_balance()` is nothing more than `sum(...)`.

## Week 1 — Getting Started

### Suggested Answers: Recap Questions

1. `print()` displays output to the screen.
2. Code gives Python instructions; comments are notes for humans and are ignored by Python.
3. Python executes statements from top to bottom unless control flow changes that order.

### Suggested Answers: Try It Yourself

1. Any custom banner text is fine if it still uses valid strings and `print()`.
2. The extra line should use `print()` and display a clear goal.
3. The comment should explain purpose, not repeat obvious code.

### What Students Usually Get Wrong

- Typing `Print()` instead of `print()`. Python is case-sensitive, and the resulting
  `NameError` does not say so. Point at the capital letter rather than explaining.
- Smart quotes pasted from a document or chat window. `“hello”` is not `"hello"`, and
  the `SyntaxError` is baffling until you know to look for it.
- Running the file from the wrong folder and getting "can't open file". Have them
  check the folder before they change the code.
- Believing comments make code run differently. Ask: "what does Python do with this
  line?" until the answer is "nothing".

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

### What Students Usually Get Wrong

- **The single biggest one:** forgetting that `input()` always returns a string, so
  `"10" + "5"` becomes `"105"`. Have them `print(type(value))` rather than telling them.
- Expecting `total = price * 2` to update itself when `price` changes later. The
  right-hand side is evaluated once, at that moment. The Week 2 reassignment diagram
  is the fastest way to fix this idea.
- Wrapping the conversion around the wrong thing: `int(input("Amount: "))` is right,
  `input(int("Amount: "))` is not.
- Treating `=` as "is equal to". It is "put this value in this name". Reading it out
  loud as "gets" helps.

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

### What Students Usually Get Wrong

- Using a chain of separate `if` statements where `elif` is meant, so two branches
  both run. Ask: "should more than one of these be able to happen?"
- Writing `if balance = 0:` and hitting a `SyntaxError` they cannot parse.
- Writing `if x == True:` instead of `if x:`. Harmless, but worth correcting early —
  the comparison is already a boolean.
- Comparing a string to a number: `if choice == 1:` when `choice` came from `input()`.
  This one silently does nothing, which makes it much harder to spot than a crash.
- Over-trusting truthiness. `if index:` looks reasonable until `index` is `0`.

## Week 4 — Pattern Matching

### Suggested Answers: Recap Questions

1. `match` is useful when one value maps to many fixed choices.
2. The `_` case is the fallback when nothing else matches.
3. It makes menu logic easier to scan and organize.

### Suggested Answers: Try It Yourself

1. The new option should appear in the menu and in a `case` branch.
2. A separate day-or-grade example should compare one value against several fixed cases.
3. Word-based commands should still be normalized with `.lower()` or `.strip()`.

### What Students Usually Get Wrong

- `case 1:` instead of `case "1":`. `input()` returns a string, so the numeric case
  never matches and every choice falls through to `_`. This is the single most common
  Week 4 bug, and it appears again in every later menu.
- Forgetting the `case _:` fallback, so a typo does nothing at all and the program
  looks frozen.
- Assuming a `case` needs a `break` the way other languages do. Python does not fall
  through; a `break` there would try to exit the surrounding loop instead.
- Adding a menu line without adding the matching `case`, or the reverse. Have them
  change both in the same edit, every time.

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

### What Students Usually Get Wrong

- Infinite loops caused by never updating the condition variable — or by putting the
  update after a `continue`, so it is skipped exactly when it matters most.
- Off-by-one with `range()`. `range(1, 5)` stops at 4. `range(1, 6)` is the one that
  counts to five.
- Reaching for a manual counter (`i = 0` ... `i += 1`) when `enumerate()` already does
  it. Correct the result, not the instinct — the manual version is not wrong, just noisier.
- Modifying a list while looping over it, which quietly skips elements. If they need
  to filter, build a new list.
- Not knowing that Ctrl-C escapes a runaway loop. Show them once, early.

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

### What Students Usually Get Wrong

- `IndexError` from `transactions[len(transactions)]`. The last item is at
  `len(...) - 1`, or just `[-1]`.
- Expecting `my_list.append(x)` to return the new list. It returns `None`, so
  `items = items.append(x)` silently destroys the list. A very common one.
- Trying to change a tuple and meeting `TypeError`. That is the tuple doing its job.
- Unpacking the wrong number of values: `for desc, amt in transactions` against
  three-item tuples.
- Not realising `list_b = list_a` makes a second name for one list, not a copy. The
  Week 6 mutability diagram settles this argument quickly.

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

### What Students Usually Get Wrong

- `KeyError` from `categories[cat] = categories[cat] + amount` on a brand-new
  category. The `.get(cat, 0)` idiom exists precisely for this, and it is worth
  writing on the board.
- Treating `"Food"`, `"food"`, and `"FOOD"` as one category. `.strip().title()` at
  the point of input is the fix — and note it must come *before* the `or` fallback.
- Expecting dictionaries to be sorted. They keep insertion order; `sorted()` is what
  gives an alphabetical report.
- Using a list where a set is meant, then writing an `if x not in list` guard by hand.
- Trying to use a list as a dictionary key. Keys must be immutable.

## Week 8 — Functions

### Suggested Answers: Recap Questions

1. A parameter appears in the function definition; an argument is the value passed in.
2. `print()` displays output; `return` sends a value back to the caller.
3. Lists can change outside the function because they are mutable objects.
4. A good function name clearly describes an action.

### Suggested Answers: Try It Yourself

1. The expense-count function should loop or use `sum()` to count negative transactions.
2. The category filter should take a category as a parameter.
3. The positive-number function should use a loop and input validation. Compare with
   `get_valid_amount()` in [budget_tracker_week8.py](budget_tracker_week8.py), which
   also explains why the guard is written `not amount > 0` rather than `amount <= 0`.

### What Students Usually Get Wrong

- **The defining confusion of this week:** printing where a `return` is needed. The
  function looks like it works, then `total = show_total()` sets `total` to `None`.
  Ask "who needs this value?" — if the answer is anything but the screen, it should
  return.
- Defining a function and never calling it, then wondering why nothing happened.
- Assuming a function changes its arguments. It depends entirely on mutability:
  rebinding a name inside the function is invisible outside; mutating the object is
  not. The Week 8 call-stack diagram is the one to project here.
- Reaching for globals rather than parameters, which works until two callers need
  different data.
- Writing a "validation" helper that calls itself instead of looping. It works, right
  up until somebody leans on the Enter key and hits `RecursionError`. The docstring in
  `get_non_empty_text()` in the final reference tells that story.

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

### What Students Usually Get Wrong

- Leaving `self` out of a method definition, then meeting
  "takes 0 positional arguments but 1 was given". Explain that Python passes the
  object in automatically; the definition has to have somewhere to put it.
- Writing `amount` instead of `self.amount` inside a method, which either raises
  `NameError` or, worse, silently reads a local variable of the same name.
- Believing `__init__` creates the object. Python has already made a blank one and
  handed it over as `self`; `__init__` only fills in the starting values.
- Printing an object and getting `<__main__.Transaction object at 0x...>`. That is the
  motivation for `__str__` in Week 10 — let them hit it before you fix it.
- Declaring `transactions = []` at class level instead of inside `__init__`, so every
  object shares one list. Rare, but deeply confusing when it happens.

## Week 10 — Encapsulation

### Suggested Answers: Recap Questions

1. Encapsulation means keeping related data and behavior together.
2. It helps the class manage its own rules and reduces scattered logic.
3. `__str__` controls how an object is shown as text. Note the contrast with
   `display()`: `display()` prints and returns nothing, while `__str__` returns text
   and prints nothing, so the caller chooses what to do with it. Both appear in
   [budget_tracker_week10.py](budget_tracker_week10.py).
4. A list of objects keeps structured data and behavior together.

### Suggested Answers: Try It Yourself

1. The expense-count method should live on `BudgetTracker`.
2. The category filter method should search inside the tracker's transactions.
3. The `main()` function should create a tracker and call methods in a readable order.

### What Students Usually Get Wrong

- Storing `self.balance` as an attribute and updating it in every method. It works
  until one method forgets, and then the number is quietly wrong forever. Week 10's
  real lesson is that `get_balance()` derives the value and therefore cannot drift.
  The same argument applies to Week 8's hand-maintained `categories` dictionary,
  which this milestone deliberately deletes.
- Reaching into `tracker.transactions` from outside the class instead of adding a
  method. Ask "what is the tracker being asked to do?" and name that.
- Having `__str__` print instead of return. The symptom is `print(obj)` showing the
  text followed by `None`.
- Confusing a class attribute with an instance attribute.
- Putting `main()` inside the class. It is a program-level job, not a tracker job.

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

### What Students Usually Get Wrong

- Trying to `json.dump()` a list of `Transaction` objects directly and hitting
  `TypeError: Object of type Transaction is not JSON serializable`. This is exactly
  why `to_dict()` and `from_dict()` exist — translate at the boundary.
- Opening with `"w"` when they meant `"r"`, which truncates the file they were trying
  to read. Recoverable only if they had a backup, so mention it before it happens.
- Writing a bare `except:`. It hides the bug and swallows Ctrl-C. Always name the
  exception.
- Catching only `FileNotFoundError` and then meeting a hand-edited or truncated file.
  The reference catches `json.JSONDecodeError` and `(KeyError, TypeError)` separately
  so the message can say what actually went wrong.
- Assigning straight onto `self` while parsing. If the file goes bad halfway through,
  the tracker is left half-loaded — new owner, old transactions. Both the chapter and
  the reference build local variables first and commit them only once nothing can
  fail. Worth a full minute of discussion; it is a real-world habit.
- Using `data["category"]` in `from_dict()`, which breaks on files written by an
  earlier version. `.get("category", "Uncategorized")` keeps old saves loadable.

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

### What Students Usually Get Wrong

- Forgetting `super().__init__(...)` in a child class, so the parent's attributes are
  never set and the first method call raises `AttributeError`.
- Reaching for inheritance where a method or a helper class would do. The chapter says
  this outright, and it is worth repeating: the tracker itself needs no inheritance at
  all. Inheritance is taught here to be understood, not to be used everywhere.
- Copying the parent's code into the child instead of calling `super()`.
- Writing `_name_` instead of `__name__`. Two underscores on each side.
- Dropping the `if __name__ == "__main__":` guard, so importing the file for a test
  launches the whole interactive menu.
- Declaring the project "done" without ever running it from a clean folder. Have them
  delete `budget_data.json` and start it once more — the first-run path is the one
  path they will never have tested.

## Bonus Chapter — Challenges & Tips

### Suggested Answers: Try It Yourself

1. Redoing a chapter's project step from memory is the real assessment for this
   course. What matters is whether the learner can explain each choice, not whether
   the code matches the listing character for character.
2. Any small feature is fine. Push for one that touches an existing class rather than
   a brand-new script — integrating is the harder and more useful skill.
3. Reading code aloud reliably exposes vague names. If a sentence needs "the thing
   that", the name is wrong.

### Suggested Answers: Reflection Questions

1. There is no wrong answer, but "all of it" usually means the learner has not yet
   separated *syntax* from *design*. Ask which one they mean, and if they cannot
   choose, ask them to write a loop and then a class and see which stalls first.
2. A good answer defines each idea by its job, not its syntax: a variable names a
   value; a conditional chooses between paths; a loop repeats work; a function names a
   job; a class binds data to the behavior that belongs with it. If they can only
   recite syntax, go back to the diagrams rather than the code.
3. The honest answer is often "no". Names such as `data`, `temp`, `x`, `list2`, and
   `do_it()` are the ones to hunt for. Ask them to rename three things and re-read.
4. Steer them toward the smallest feature that touches existing code — a search
   option or a per-category budget limit — rather than a rewrite or a GUI. Finishing
   a small feature teaches more than abandoning a large one.

### Bonus Challenges — What to Expect

| # | Challenge | What to watch for |
|---|---|---|
| 1 | Monthly budgets | Where the limits are stored. A dictionary on `BudgetTracker` is the natural home; a second parallel dictionary is not. |
| 2 | Date tracking | `datetime` objects are not JSON-serializable. They will need `.isoformat()` on save and `date.fromisoformat()` on load — the same to_dict/from_dict lesson as Week 11. |
| 3 | Search & filter | Case-insensitive matching (`keyword.lower() in description.lower()`) and a sensible "no results" message. |
| 4 | Data visualization | Requires `pip install matplotlib`, which the course has not covered. Expect to help with `python -m venv .venv`, activation, and the install before any plotting happens. |
| 5 | Multiple accounts | The one genuinely appropriate use of inheritance in this project. Check they call `super().__init__(...)`. |
| 6 | Export to CSV | `csv.DictWriter` with a header row. Watch for the missing `newline=""` argument to `open()`, which produces blank lines between rows on Windows. |

## Teaching Notes

- Encourage learners to explain code out loud before editing it.
- Prefer small corrections over rewriting a student's whole program.
- If a learner is stuck, narrow the problem to one value, one condition, or one loop at a time.
- Ask learners to justify names. Good naming is part of understanding.
- Let them hit the error before you explain the fix. Most of the entries in the
  "What Students Usually Get Wrong" sections above are far more memorable as a
  three-minute mystery than as a warning given in advance.
- When a student's program misbehaves and nothing looks wrong, check the sign
  convention and check whether a value is a string that should be a number. Between
  them, those two account for most of it.

---

This guide is meant to support judgment, not replace it.
