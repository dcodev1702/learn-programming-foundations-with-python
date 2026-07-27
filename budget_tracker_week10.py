"""Personal Budget Tracker — Week 10 milestone (Classes and Encapsulation).

📌 WHAT THIS FILE IS
    The course project as it stands at the end of Week 10. The tuples and the
    loose functions from Week 8 are gone. In their place are two classes, each one
    owning its own data and the behaviour that belongs with it.

🆕 WHAT CHANGED SINCE WEEK 8
    Week 8:   a transaction was a tuple `("Rent", -900, "Bills")` and the
              functions that worked on it lived somewhere else entirely.
    Week 9:   that tuple became a `Transaction` object, so it could carry its own
              `is_expense()` and `display()` methods.
    Week 10:  the program-level jobs — holding the list, totalling it, reporting
              on it — moved into a `BudgetTracker` class. Week 8 also kept a
              separate `categories` dictionary in step by hand; this version has
              deleted it and derives the same totals from the transactions.

🧠 THE BIG IDEA OF WEEK 10 (ENCAPSULATION)
    Data and the code that operates on that data belong together. `BudgetTracker`
    owns `self.transactions`, so nothing outside the class has to know how the
    list is stored — callers just ask for `get_balance()`. Change the storage
    later and every caller keeps working.

📖 THE CHAPTERS THIS FILE COMES FROM
    Primary:  chapters/week-10-encapsulation.md  ("Project Step")
    Built on: chapters/week-09-intro-to-oop.md   (the `Transaction` class)
              chapters/week-08-functions.md      (the menu loop and validation)
    Leads to: chapters/week-11-file-io.md — which adds `save()` and `load()`, and
              then budget_tracker_final.py.

📌 HOW THIS FILE DIFFERS FROM THE CHAPTER LISTING
    The chapter listing stops after the class definitions and a few sample calls.
    This file adds `get_valid_amount()` and a full interactive `main()` so the
    milestone is actually runnable. The classes themselves match the chapter.

▶️  HOW TO RUN IT
    macOS / Linux:  python3 budget_tracker_week10.py
    Windows:        python budget_tracker_week10.py   (or  py -3 budget_tracker_week10.py)

🗺️  THE COMMENT SYMBOLS USED BELOW
    📌 what this block is        🧠 the idea worth understanding
    ⚠️  the trap beginners hit    🔁 how the looping works
    🧮 how the numbers and signs work   🧱 object-oriented mechanics
"""


class Transaction:
    """One single money movement: what it was, how much, and which category.

    🧱 A class is a blueprint, not a thing. This block creates no transactions at
       all — it describes what every transaction will look like. The objects get
       built later, by calls such as `Transaction("Rent", -900, "Bills")`.
    🧠 WHY BOTHER, when Week 8's tuple worked? Because a tuple can only hold
       values. An object holds values *and* the behaviour that goes with them, so
       `is_expense()` lives next to the amount it is asking about instead of in
       some distant function.
    """

    def __init__(self, description, amount, category="Income"):
        """Set up a brand-new transaction.

        🧱 `__init__` is not the thing that creates the object — Python has
           already made a blank one and handed it to us as `self`. `__init__`'s
           only job is to fill in that blank object's starting values.
        🧱 `self` is "the particular object this call is about". Two transactions
           each get their own `self.amount`; that is what keeps them independent.
        📌 `category="Income"` is a default parameter (Week 8). Leave it out and
           the transaction is treated as income.
        """
        self.description = description
        self.amount = amount
        self.category = category

    def is_expense(self):
        """Return True when this transaction takes money out.

        🧮 The whole test rests on the sign convention carried over from Week 8:
           income is stored POSITIVE, expenses are stored NEGATIVE.
        🧠 The method returns the comparison directly. Writing
           `if self.amount < 0: return True else: return False` says the same
           thing three times as slowly — `self.amount < 0` is *already* True/False.
        """
        return self.amount < 0

    def display(self, index=None):
        """Print this transaction as one readable line.

        📌 `index=None` makes the number optional, so the same method serves both
           a numbered history list and a one-off print.
        ⚠️ Test with `is not None`, never with a bare `if index:`. Index 0 is a
           perfectly real position, but it is also falsy, so `if index:` would
           silently drop it. This is one of the most common beginner bugs.
        """
        # 🧮 Build the sign by hand and print the absolute value, so money reads
        #    "-$52.30" rather than "$-52.30" with the minus stranded inside the
        #    number. Same format as Week 6 — one money format for the whole course.
        sign = "+" if self.amount >= 0 else "-"
        prefix = f"{index}. " if index is not None else ""
        print(f"  {prefix}[{self.category}] {self.description}: {sign}${abs(self.amount):.2f}")

    def __str__(self):
        """Return the human-readable form used by `print(transaction)`.

        🧱 A "dunder" (double-underscore) method hooks into built-in syntax rather
           than being called by name. Define `__str__` and `print(obj)` and
           `str(obj)` and f-strings all start producing this text instead of the
           default `<__main__.Transaction object at 0x000001C...>`.
        📌 Not shown in the Week 10 chapter listing, which stops at `get_balance()`
           and friends. It is here because the Week 12 chapter's final program uses
           it, and because it is the cleanest illustration of print-vs-return.
        🧠 `display()` PRINTS and returns nothing; `__str__` RETURNS text and
           prints nothing. That is the Week 8 print-vs-return distinction again,
           and it is why `__str__` is the more flexible of the two — the caller
           chooses what to do with the string.
        """
        sign = "+" if self.amount >= 0 else "-"
        return f"[{self.category}] {self.description}: {sign}${abs(self.amount):.2f}"


class BudgetTracker:
    """Owns the list of transactions and every report drawn from it.

    🧠 THIS CLASS IS THE POINT OF WEEK 10. In Week 8 the transaction list was a
       bare variable in `main()` that every function had to be handed. Here the
       list belongs to the tracker, and the methods that use it live alongside it.
       Nothing outside this class ever touches `self.transactions` directly.
    """

    def __init__(self, owner):
        """Start an empty tracker for one named person."""
        self.owner = owner

        # ⚠️ The list is created HERE, inside `__init__`, so every tracker gets a
        #    fresh one. Written as a class-level `transactions = []` instead, all
        #    trackers would silently share a single list.
        self.transactions = []

    def add_income(self, description, amount):
        """Record money coming in.

        🧮 Stored POSITIVE, exactly as in Week 8. Nothing about the sign
           convention changed when the tuples became objects.
        """
        self.transactions.append(Transaction(description, amount, "Income"))
        print(f"Income added: +${amount:.2f}")

    def add_expense(self, description, amount, category):
        """Record money going out.

        🧮 Note the minus: the caller passes a positive number and this method
           stores the negative. Doing the flip in one place means no caller can
           forget it.
        """
        self.transactions.append(Transaction(description, -amount, category))
        print(f"Expense added: -${amount:.2f} [{category}]")

    def get_balance(self):
        """Return income minus expenses.

        🧮 Because expenses are already negative, "income minus expenses" is just
           "add everything up".
        🧠 The balance is CALCULATED on demand, never stored. A stored
           `self.balance` would be a second copy of the truth that every method
           would have to remember to update — and one forgotten update makes the
           number silently wrong. Deriving it means it cannot drift.
        """
        return sum(transaction.amount for transaction in self.transactions)

    def show_history(self):
        """Print every transaction, numbered from 1."""
        # ⚠️ Guard clause: deal with the empty case and leave, so the rest of the
        #    method can assume there is something to show.
        if not self.transactions:
            print("No transactions yet.")
            return

        print(f"\n--- History for {self.owner} ---")

        # 🔁 The tracker does not know how to format a transaction, and it should
        #    not: it asks each object to display itself. Add a field to
        #    `Transaction` later and this loop needs no changes at all.
        for index, transaction in enumerate(self.transactions, start=1):
            transaction.display(index)

    def show_summary(self):
        """Print totals for income, expenses, and the resulting balance."""
        # 🧠 Two generator expressions, each filtering by sign. Read the first as
        #    "the amount of every transaction, but only the positive ones".
        # 📌 The chapter listing calls the loop variable `t`. It is spelled out
        #    here because Week 8's own advice — names should say what they mean —
        #    applies to one-line loops too.
        income_total = sum(
            transaction.amount
            for transaction in self.transactions
            if transaction.amount > 0
        )
        expense_total = sum(
            transaction.amount
            for transaction in self.transactions
            if transaction.amount < 0
        )

        print(f"\n--- Summary for {self.owner} ---")
        print(f"  Total Income:   +${income_total:.2f}")

        # 🧮 `expense_total` is negative, so `abs()` strips the minus and the "-"
        #    printed just before the "$" puts it back in the right place.
        print(f"  Total Expenses: -${abs(expense_total):.2f}")
        print(f"  Balance:         ${self.get_balance():.2f}")

    def spending_by_category(self):
        """Print how much has been spent in each category.

        🆕 THIS IS THE WEEK 10 UPGRADE WORTH STUDYING. Week 8 kept a running
           `categories` dictionary that `add_expense()` had to update by hand —
           two places holding overlapping facts that could drift apart. Here the
           dictionary is rebuilt from `self.transactions` every time it is
           needed. It cannot go stale, because it does not outlive the call.
        """
        category_totals = {}

        for transaction in self.transactions:
            if transaction.is_expense():
                # 🧠 Week 7's `.get(key, default)`: "whatever is there already, or
                #    0 if this category is new, plus this expense".
                # 🧮 `abs()` keeps the report positive — "Food: $52.30" reads
                #    better than "Food: $-52.30".
                category_totals[transaction.category] = (
                    category_totals.get(transaction.category, 0) + abs(transaction.amount)
                )

        if not category_totals:
            print("No expense categories yet.")
            return

        print("\n--- Spending by Category ---")

        # 🔁 `sorted()` keeps the order stable between runs.
        for category, total in sorted(category_totals.items()):
            print(f"  {category}: ${total:.2f}")

    def __str__(self):
        """Return a short description of the tracker itself.

        🧱 This is what `print(tracker)` shows. Keep it short: `__str__` is a
           label for the object, not a report. The report is `show_summary()`.
        """
        return f"BudgetTracker({self.owner}, {len(self.transactions)} transactions)"


def get_valid_amount(prompt):
    """Ask for a positive dollar amount, re-asking until the user gives a real one.

    📌 Still a plain function, not a method, and deliberately so: it knows nothing
       about budgets. Turning it into a method would tie a general-purpose helper
       to one specific class for no benefit.
    """
    while True:
        try:
            # ⚠️ float() raises ValueError on "abc", "" or "12.3.4". Without this
            #    try/except a single typo would crash the program.
            amount = float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # 🧠 `not amount > 0` rather than `amount <= 0`, on purpose. A user can
        #    type `nan` at this prompt, and every comparison against nan is False
        #    — including `nan <= 0` — so `amount <= 0` would let it through and
        #    quietly poison the balance. `nan > 0` is False too, so this rejects it.
        if not amount > 0:
            print("Please enter a positive number.")
            continue

        # ⚠️ `inf` (infinity) is the other float a user can literally type. It is
        #    genuinely greater than 0, so the check above lets it through, and it
        #    would make every total infinite from then on.
        if amount == float("inf"):
            print("Please enter a realistic amount.")
            continue

        return amount


def main():
    """Run the interactive tracker until the user chooses to quit.

    📌 COMPARE THIS WITH WEEK 8. The menu is the same and the loop is the same,
       but every branch is now a message sent to one object. `main()` no longer
       passes data structures around; it just asks the tracker to do things.
    """
    print("=" * 44)
    print("   Personal Budget Tracker - Week 10")
    print("=" * 44)

    owner = input("Enter your name: ").strip() or "User"

    # 🧱 THE MOMENT AN OBJECT IS BORN. `BudgetTracker` was only a blueprint until
    #    this line ran; `tracker` is one real instance built from it.
    tracker = BudgetTracker(owner)

    # 🔁 An intentional forever-loop, safe because option 6 `break`s out of it.
    while True:
        # 🧠 The balance is recalculated on every pass, so the header cannot go
        #    stale. That is only cheap and safe because it is derived, not stored.
        print(f"\n--- Menu (Balance: ${tracker.get_balance():.2f}) ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transaction History")
        print("4. View Summary")
        print("5. View Spending by Category")
        print("6. Quit")

        choice = input("\nSelect an option (1-6): ").strip()

        # ⚠️ The cases are strings ("1"), not numbers (1), because `input()`
        #    always hands back a string. `case 1:` would never match.
        match choice:
            case "1":
                description = input("Description: ").strip() or "Income"
                amount = get_valid_amount("Amount: $")
                tracker.add_income(description, amount)
            case "2":
                description = input("Description: ").strip() or "Expense"
                amount = get_valid_amount("Amount: $")
                # 🧠 `.title()` first, `or` second: "  food  " becomes "Food", so
                #    "food", "Food" and "FOOD" all land in one category.
                category = input("Category: ").strip().title() or "Uncategorized"
                tracker.add_expense(description, amount, category)
            case "3":
                tracker.show_history()
            case "4":
                tracker.show_summary()
            case "5":
                tracker.spending_by_category()
            case "6":
                print("Goodbye!")
                break  # 🔁 the one and only exit
            case _:
                # ⚠️ The wildcard catches anything the cases above missed.
                print("Invalid option. Please choose 1-6.")


# 🧠 "Only run main() when this file is executed directly." If another file ever
#    imports this one, Python sets __name__ to the module name instead of
#    "__main__", so the menu will not hijack that program. Week 12 explains it
#    in full.
if __name__ == "__main__":
    main()
