"""Personal Budget Tracker — the finished application (Week 12).

📌 WHAT THIS FILE IS
    The end of the road: every idea from the twelve weeks, wired together into one
    program that a person could genuinely use. Nothing in this file is new. It is
    the Week 10 classes, plus Week 11's saving and loading, plus a polished menu.

🆕 WHAT CHANGED SINCE WEEK 10
    Week 11 gave `Transaction` a `to_dict()` / `from_dict()` pair and gave
    `BudgetTracker` a `save()` / `load()` pair, so the data outlives the program.
    Week 12 added the last of the validation, the save-on-quit prompt, and the
    over-budget warning.

🧠 THE BIG IDEA OF THE FINAL BUILD
    Every layer has exactly one job. `Transaction` knows about one money movement.
    `BudgetTracker` knows about a collection of them. `main()` knows about talking
    to a human, and nothing else. You can change any one layer without disturbing
    the other two.

📖 WHERE EVERY PIECE OF THIS FILE COMES FROM
    chapters/week-02-variables-and-data-types.md  f-strings, `${value:.2f}`
    chapters/week-03-if-elif-else.md              the over-budget warning
    chapters/week-04-match-case.md                the menu dispatch
    chapters/week-05-loops.md                     `while True:` plus `break`
    chapters/week-06-lists-and-tuples.md          the transaction list, the money format
    chapters/week-07-dictionaries-and-sets.md     `.get()` in spending_by_category()
    chapters/week-08-functions.md                 get_valid_amount(), get_non_empty_text()
    chapters/week-09-intro-to-oop.md              the `Transaction` class
    chapters/week-10-encapsulation.md             the `BudgetTracker` class
    chapters/week-11-file-io.md                   to_dict/from_dict, save/load, try/except
    chapters/week-12-inheritance-and-final-project.md   final assembly and `__main__`

📌 HOW THIS FILE RELATES TO THE WEEK 12 CHAPTER LISTING
    It is the same program, line for line. The chapter shows the code; this file
    adds the commentary, the `__str__` methods from Week 10, and nothing else.
    If you spot a real difference, that is a bug — please report it.

▶️  HOW TO RUN IT
    macOS / Linux:  python3 budget_tracker_final.py
    Windows:        python budget_tracker_final.py   (or  py -3 budget_tracker_final.py)
    Your data lands in budget_data.json, next to wherever you ran the command.

🗺️  THE COMMENT SYMBOLS USED BELOW
    📌 what this block is        🧠 the idea worth understanding
    ⚠️  the trap beginners hit    🔁 how the looping works
    🧮 how the numbers and signs work   🧱 object-oriented mechanics
    💾 saving and loading
"""

# 💾 The only import in the whole course. `json` is part of Python's standard
#    library, so there is nothing to install — `import json` is all it takes.
import json


class Transaction:
    """One single money movement: what it was, how much, and which category.

    🧱 A blueprint, not a thing. This block creates no transactions; it describes
       what every transaction will look like when one is built.
    """

    def __init__(self, description, amount, category="Income"):
        """Set up a brand-new transaction.

        🧱 Python has already made a blank object and passed it in as `self`.
           `__init__`'s only job is to fill in that object's starting values.
        📌 `category="Income"` is a default parameter (Week 8): leave it out and
           the transaction counts as income.
        """
        self.description = description
        self.amount = amount
        self.category = category

    def is_expense(self):
        """Return True when this transaction takes money out.

        🧮 Rests entirely on the sign convention: income is stored POSITIVE,
           expenses are stored NEGATIVE.
        """
        return self.amount < 0

    def display(self, index=None):
        """Print this transaction as one readable line.

        📌 `index=None` makes the number optional, so one method serves both the
           numbered history list and a one-off print.
        ⚠️ Test with `is not None`, never a bare `if index:`. Index 0 is a real
           position but it is also falsy, so `if index:` would silently drop it.
        """
        # 🧮 Build the sign by hand and print the absolute value, so money reads
        #    "-$52.30" and not "$-52.30" with the minus stranded inside the
        #    number. Same format Week 6 introduced — one money format throughout.
        sign = "+" if self.amount >= 0 else "-"
        prefix = f"{index}. " if index is not None else ""
        print(f"  {prefix}[{self.category}] {self.description}: {sign}${abs(self.amount):.2f}")

    def __str__(self):
        """Return the human-readable form used by `print(transaction)`.

        🧠 `display()` PRINTS and returns nothing; `__str__` RETURNS text and
           prints nothing. Week 8's print-vs-return distinction, one more time.
        """
        sign = "+" if self.amount >= 0 else "-"
        return f"[{self.category}] {self.description}: {sign}${abs(self.amount):.2f}"

    def to_dict(self):
        """Convert this object into a plain dictionary that `json` can write.

        💾 WHY THIS METHOD HAS TO EXIST. `json` understands exactly six things:
           dicts, lists, strings, numbers, booleans and None. A `Transaction` is
           none of them, so `json.dump()` would raise TypeError on one directly.
           This method translates at the boundary, on the way out.
        """
        return {
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
        }

    @classmethod
    def from_dict(cls, data):
        """Rebuild a Transaction from the dictionary that `to_dict()` produced.

        💾 The other half of the round trip: object -> dict -> JSON text on disk
           -> dict -> object.
        🧱 `@classmethod` means this is called on the CLASS, not on an instance:
           `Transaction.from_dict(...)`. That is the point — there is no object
           yet, which is precisely what this method is for. `cls` is the class
           itself, so `cls(...)` is the same as writing `Transaction(...)`.
        ⚠️ `data.get("category", "Uncategorized")` rather than `data["category"]`.
           A file saved by an older version of the program may have no category
           at all, and `[]` would raise KeyError on it. `.get()` supplies a
           default and the old file still loads. This is what "be forgiving about
           what you read" means in practice.
        """
        return cls(
            data["description"],
            data["amount"],
            data.get("category", "Uncategorized"),
        )


class BudgetTracker:
    """Owns the transactions, every report drawn from them, and the save file.

    🧠 Encapsulation, from Week 10: the data and the code that works on it live
       together. Nothing outside this class touches `self.transactions` directly.
    """

    def __init__(self, owner):
        """Start an empty tracker for one named person."""
        self.owner = owner

        # ⚠️ The list is created here, inside `__init__`, so every tracker gets a
        #    fresh one. A class-level `transactions = []` would be shared by all
        #    trackers — a classic and very confusing bug.
        self.transactions = []

    def add_income(self, description, amount):
        """Record money coming in (stored POSITIVE)."""
        self.transactions.append(Transaction(description, amount, "Income"))
        print(f"  Income added: +${amount:.2f}")

    def add_expense(self, description, amount, category):
        """Record money going out.

        🧮 The caller passes a positive number and this method stores the
           negative. Flipping the sign in exactly one place means no caller can
           forget to do it.
        """
        self.transactions.append(Transaction(description, -amount, category))
        print(f"  Expense added: -${amount:.2f} [{category}]")

    def get_balance(self):
        """Return income minus expenses.

        🧠 CALCULATED, never stored. A `self.balance` attribute would be a second
           copy of the truth that every method would have to remember to update,
           and one missed update makes the number quietly wrong. Derived values
           cannot drift.
        """
        return sum(transaction.amount for transaction in self.transactions)

    def show_history(self):
        """Print every transaction, numbered from 1, then the running balance."""
        if not self.transactions:
            print("  No transactions yet.")
            return

        # 🔁 The tracker never formats a transaction itself — it asks each object
        #    to display itself. Add a field to `Transaction` later and this loop
        #    needs no changes at all.
        for index, transaction in enumerate(self.transactions, start=1):
            transaction.display(index)

        print(f"\n  Current Balance: ${self.get_balance():.2f}")

    def show_summary(self):
        """Print income, expense and balance totals, warning if overdrawn."""
        # 🧠 Two generator expressions, each filtering by sign. Read the first as
        #    "the amount of every transaction, but only the positive ones".
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
        balance = self.get_balance()

        print(f"\n  --- Summary for {self.owner} ---")
        print(f"  Total Income:    +${income_total:.2f}")

        # 🧮 `expense_total` is already negative, so `abs()` strips the minus and
        #    the "-" printed before the "$" puts it back in the readable place.
        print(f"  Total Expenses:  -${abs(expense_total):.2f}")
        print(f"  Net Balance:      ${balance:.2f}")

        # 📌 Week 3's conditional, still earning its place in the final build.
        if balance < 0:
            print("  ** Warning: You are over budget! **")

    def spending_by_category(self):
        """Print how much has been spent in each category.

        🧠 The dictionary is rebuilt from `self.transactions` on every call, so it
           cannot go stale. Week 8 kept a running `categories` dictionary that
           had to be updated by hand — two places holding the same fact, which is
           two places to get it wrong.
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
            print("  No expenses recorded yet.")
            return

        print("\n  --- Spending by Category ---")

        # 🔁 `sorted()` keeps the order stable between runs.
        for category, total in sorted(category_totals.items()):
            print(f"  {category}: ${total:.2f}")

    def save(self, filename="budget_data.json"):
        """Write the owner and every transaction to a JSON file.

        💾 `"w"` means write, and it REPLACES the file's entire contents. That is
           what we want here — the file is a complete snapshot, not a log.
        """
        data = {
            "owner": self.owner,
            # 🧠 A list comprehension: "call to_dict() on every transaction and
            #    collect the results". Each object becomes a plain dictionary.
            "transactions": [transaction.to_dict() for transaction in self.transactions],
        }

        # 💾 `with open(...)` is Week 11's context manager. It closes the file
        #    when the block ends — including when the block raises halfway
        #    through, which is exactly when you would forget to close it by hand.
        with open(filename, "w") as file_handle:
            # 📌 `indent=2` pretty-prints the JSON. Open budget_data.json in any
            #    editor after saving; being able to read your own data file is
            #    worth far more than the few extra bytes.
            json.dump(data, file_handle, indent=2)

        print(f"  Data saved to {filename}.")

    def load(self, filename="budget_data.json"):
        """Restore a previous session from disk, or start fresh if that fails.

        💾 THE THREE WAYS READING A FILE GOES WRONG, each caught separately so
           the message can actually tell the user what happened:
             • FileNotFoundError  — first run, nothing saved yet. Not an error.
             • JSONDecodeError    — the file exists but is not valid JSON
                                    (hand-edited, truncated, disk filled up).
             • KeyError/TypeError — valid JSON, wrong shape: a key we need is
                                    missing, or the top level is a list, not a dict.
        ⚠️ Never write a bare `except:`. It swallows everything — including the
           Ctrl-C you are pressing to escape — and hides the bug you need to see.
        """
        try:
            with open(filename, "r") as file_handle:
                data = json.load(file_handle)

            # ⚠️ Build LOCAL variables first, and only commit them to `self`
            #    afterwards. If a transaction halfway down the file is malformed,
            #    the exception fires here — before anything on the object has been
            #    touched — so the tracker is left cleanly empty rather than half
            #    loaded with a new owner and somebody else's transactions.
            owner = data["owner"]
            loaded = [Transaction.from_dict(item) for item in data["transactions"]]

            # ✅ Past every possible failure: now it is safe to swap them in.
            self.owner = owner
            self.transactions = loaded
            print(f"  Welcome back, {self.owner}! Loaded {len(self.transactions)} transactions.")
        except FileNotFoundError:
            print("  No saved data found. Starting fresh!")
        except json.JSONDecodeError:
            print(f"  {filename} is not valid JSON. Starting fresh!")
        except (KeyError, TypeError):
            print(f"  {filename} is missing expected fields. Starting fresh!")

    def __str__(self):
        """Return a short label for the tracker itself.

        🧱 What `print(tracker)` shows. Keep it short — `__str__` is a label, not
           a report. The report is `show_summary()`.
        """
        return f"BudgetTracker({self.owner}, {len(self.transactions)} transactions)"


def get_valid_amount(prompt):
    """Ask for a positive dollar amount, re-asking until the user gives a real one.

    🔁 A validation helper should never give up after one bad answer, and should
       never crash on one either.
    """
    while True:
        try:
            # ⚠️ float() raises ValueError on "abc", "" or "12.3.4".
            amount = float(input(prompt))
        except ValueError:
            print("  Invalid input. Please enter a number.")
            continue

        # 🧠 `not amount > 0` rather than `amount <= 0`, on purpose. A user can
        #    type `nan` at this prompt, and every comparison against nan is False
        #    — including `nan <= 0` — so `amount <= 0` would let it through and
        #    quietly turn the balance into nan forever. `nan > 0` is False too,
        #    so `not amount > 0` correctly rejects it.
        if not amount > 0:
            print("  Please enter a positive number.")
            continue

        # ⚠️ `inf` (infinity) is the other float a user can literally type. It is
        #    genuinely greater than 0, so the check above lets it through, and it
        #    would make every total infinite from then on.
        if amount == float("inf"):
            print("  Please enter a realistic amount.")
            continue

        return amount


def get_non_empty_text(prompt, default_value=None):
    """Ask for some text, either re-asking until it is non-empty or falling back.

    📌 Not in the Week 12 chapter listing — this is the reference version's extra
       polish, and a good model for the chapter's "Try It Yourself".
    🧠 `default_value=None` distinguishes two different jobs in one function:
         • no default given  -> keep asking until the user actually types something
         • default given     -> pressing Enter accepts the default
    ⚠️ This used to call ITSELF instead of looping. That works right up until
       somebody leans on the Enter key, at which point Python runs out of stack
       and raises RecursionError. "Repeat until valid" is a loop's job, not
       recursion's.
    """
    while True:
        text = input(prompt).strip()

        if text:
            return text

        if default_value is not None:
            return default_value

        print("  Input cannot be empty.")


def main():
    """Run the finished application: load, serve the menu, offer to save on exit."""
    print("=" * 44)
    print("   Personal Budget Tracker v1.0")
    print("   Built with Python 3.13")
    print("=" * 44)

    name = get_non_empty_text("\nEnter your name: ", "User")

    # 🧱 The blueprint becomes a real object on this line.
    tracker = BudgetTracker(name)

    # 💾 Load immediately, before the menu appears. If a save file exists it
    #    replaces the name just entered with the saved owner — which is why the
    #    greeting says "Welcome back".
    tracker.load()

    # 🔁 The forever-loop, safe because option 7 `break`s out of it.
    while True:
        # 🧠 Recalculated every pass, so the header can never be stale.
        print(f"\n--- Menu (Balance: ${tracker.get_balance():.2f}) ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transaction History")
        print("4. View Summary")
        print("5. View Spending by Category")
        print("6. Save Data")
        print("7. Quit")

        choice = input("\nSelect an option (1-7): ").strip()

        # ⚠️ The cases are strings, because `input()` always returns a string.
        match choice:
            case "1":
                # 📌 Every branch follows the same three beats: gather validated
                #    input, hand it to the tracker, let the tracker report back.
                description = get_non_empty_text("  Description: ")
                amount = get_valid_amount("  Amount: $")
                tracker.add_income(description, amount)

            case "2":
                description = get_non_empty_text("  Description: ")
                amount = get_valid_amount("  Amount: $")
                # 🧠 `.title()` normalises the category, so "food", "Food" and
                #    "FOOD" all land in one bucket instead of three.
                category = get_non_empty_text(
                    "  Category (e.g., Food, Transport, Bills): ", "Uncategorized"
                ).title()
                tracker.add_expense(description, amount, category)

            case "3":
                tracker.show_history()

            case "4":
                tracker.show_summary()

            case "5":
                tracker.spending_by_category()

            case "6":
                tracker.save()

            case "7":
                # ⚠️ Saving is explicit, never automatic. Silently writing to a
                #    user's file on the way out is the kind of "helpful" that
                #    loses somebody's data.
                save_first = input("  Save before quitting? (y/n): ").strip().lower()
                if save_first == "y":
                    tracker.save()
                print(f"\n  Goodbye, {tracker.owner}! Happy budgeting!")
                break  # 🔁 the one and only exit

            case _:
                print("  Invalid option. Please choose 1-7.")


# 🧠 THE LAST TWO LINES, EXPLAINED. Python sets a variable called `__name__` in
#    every file it loads. In the file you actually ran, it is set to "__main__";
#    in a file that was merely imported, it is set to that file's module name.
#    So this guard means "start the menu only if I am the program being run".
#    Without it, `import budget_tracker_final` in a test would launch the whole
#    interactive app instead of just loading the classes.
if __name__ == "__main__":
    main()
