"""Personal Budget Tracker — Week 8 milestone (Functions).

📌 WHAT THIS FILE IS
    The course project as it stands at the end of Week 8. All of the data is still
    plain built-in types: a list of tuples for the transactions, a dictionary for
    the category totals. Nothing here is object-oriented yet — that starts in Week 9.

🆕 WHAT CHANGED SINCE WEEK 7
    Week 7's version was one long `while` loop with every step written inline.
    This version says exactly the same thing, but every step now has a name:
    `add_income()`, `get_balance()`, `show_history()`. Read `main()` at the bottom
    first — it now reads like a table of contents for the whole program.

🧠 THE BIG IDEA OF WEEK 8
    A function is a name you give to a job. Once a job has a name you can read the
    program without reading the details, and when the job is wrong you fix it in
    one place instead of three.

▶️  HOW TO RUN IT
    macOS / Linux:  python3 budget_tracker_week8.py
    Windows:        python budget_tracker_week8.py   (or  py -3 budget_tracker_week8.py)

📖 THE CHAPTERS THIS FILE COMES FROM
    Primary:  chapters/week-08-functions.md  ("Project Step")
    Built on: chapters/week-06-lists-and-tuples.md   (the transaction list)
              chapters/week-07-dictionaries-and-sets.md (the category totals)
    Leads to: chapters/week-09-intro-to-oop.md — where each tuple below becomes a
              `Transaction` object, and then budget_tracker_week10.py.

📌 HOW THIS FILE DIFFERS FROM THE CHAPTER LISTING
    The chapter listing is deliberately shorter so it fits on a page. This file
    adds `get_valid_amount()` (the chapter's "Try It Yourself" #3), the
    `.strip() or "Income"` fallbacks on the description prompts, a `main()`
    function, and the `if __name__ == "__main__":` guard. Every function name,
    parameter, and line of output matches the chapter exactly.

🗺️  THE COMMENT SYMBOLS USED BELOW
    📌 what this block is        🧠 the idea worth understanding
    ⚠️  the trap beginners hit    🔁 how the looping works
    🧮 how the numbers and signs work
"""


def display_menu():
    """Show the main menu options.

    📌 A function with no parameters and no `return`. Its whole job is the side
       effect of putting text on the screen.
    🧠 Notice what it does *not* do: it never reads input and never decides what
       happens next. One function, one responsibility. That is exactly why
       `main()` stays short enough to take in at a glance.
    """
    print("\n--- Budget Tracker Menu ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transaction History")
    print("5. View Spending by Category")
    print("6. Quit")


def get_valid_amount(prompt):
    """Ask for a positive dollar amount, re-asking until the user gives a real one.

    📌 `prompt` is a parameter — the text to display. Whatever the caller passes
       in ("Amount: $") is the argument that fills that slot.
    🧠 This is the `return` half of Week 8. The function neither prints the amount
       nor stores it; it hands the value back so the *caller* decides what to do
       with it. That is precisely what lets both income and expenses reuse it.
    🔁 The loop is deliberate: a validation helper should not give up after one
       bad answer, and it certainly should not crash on one.
    """
    while True:
        try:
            # ⚠️ float() raises ValueError on anything that is not a number —
            #    "abc", "", "12.3.4". Without this try/except one typo would take
            #    the whole program down.
            amount = float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  # 🔁 straight back to the top and ask again

        # 🧠 Written as `not amount > 0` rather than the more obvious
        #    `amount <= 0`, on purpose. Python has a special float called "nan"
        #    (not a number) and a user really can type `nan` at this prompt.
        #    Every comparison against nan is False — including `nan <= 0` — so
        #    `amount <= 0` would wave it through and quietly poison the balance
        #    forever. `nan > 0` is False too, so `not amount > 0` rejects it.
        if not amount > 0:
            print("Please enter a positive number.")
            continue

        # ⚠️ `inf` (infinity) is the other float a user can literally type. It is
        #    genuinely greater than 0, so the check above lets it through, and it
        #    would make every total infinite from then on. A budget has no use
        #    for it, so it gets its own check and its own message.
        if amount == float("inf"):
            print("Please enter a realistic amount.")
            continue

        return amount  # ✅ only reachable once the value is genuinely valid


def add_income(transactions, categories=None):
    """Prompt the user for an income transaction and record it.

    ⚠️ THE WEEK 8 GOTCHA — this function returns nothing, yet it still changes
       the caller's data. That is not magic. `transactions` is a *list*, lists are
       mutable, and `.append()` changes the very same object the caller holds.
       Contrast that with `get_valid_amount()`, which can only reach the caller by
       returning a value. Rebinding a name changes nothing outside the function;
       mutating an object changes it for everyone holding a reference to it.
    📌 `categories` is accepted and ignored so that `add_income()` and
       `add_expense()` can be called identically from `main()`. Only expenses
       count toward category spending.
    """
    # 🧠 `or "Income"` supplies a fallback. An empty string is falsy (Week 3), so
    #    pressing Enter without typing still leaves a sensible description.
    description = input("Description: ").strip() or "Income"
    amount = get_valid_amount("Amount: $")

    # 🧮 THE SIGN CONVENTION — the single most important decision in this program.
    #    Income is stored POSITIVE and expenses are stored NEGATIVE. Because of
    #    that one choice, the balance is simply the sum of everything: there is no
    #    separate running total to keep in step and nothing that can disagree.
    transactions.append((description, amount, "Income"))
    print(f"Added income: +${amount:.2f}")


def add_expense(transactions, categories):
    """Prompt the user for an expense transaction and record it.

    📌 Two parameters, because this function touches two pieces of data. Passing
       them in rather than reaching for global variables is what Week 8 means by
       "keep data local" — and it is what makes the function reusable.
    """
    description = input("Description: ").strip() or "Expense"
    amount = get_valid_amount("Amount: $")

    # 🧠 `.strip().title()` runs first and `or` picks the fallback afterwards, so
    #    "  food  " becomes "Food". That means "food", "Food" and "FOOD" all land
    #    in one category instead of three.
    category = input("Category: ").strip().title() or "Uncategorized"

    # 🧮 Note the minus sign. The user typed a positive number; we store the
    #    negative. Every total in this file depends on that.
    transactions.append((description, -amount, category))

    # 🧠 Week 7's `.get(key, default)` in a single line: "the total so far, or 0
    #    if this category is brand new, plus this expense".
    # ⚠️ Category totals are kept POSITIVE even though the transaction is
    #    negative, because "Food: $56.55" reads better than "Food: $-56.55".
    #    Also notice the hazard: `transactions` and `categories` now hold
    #    overlapping information and must be updated together. Week 10 drops this
    #    dictionary and derives the same totals from `transactions` on demand —
    #    one source of truth is always safer than two that have to agree.
    categories[category] = categories.get(category, 0) + amount

    print(f"Recorded expense: -${amount:.2f} [{category}]")


def get_balance(transactions):
    """Calculate the current balance from all transactions.

    🧮 This is the payoff for the sign convention. Because expenses are already
       negative, "income minus expenses" collapses into "add everything up".
    🧠 `for _, amount, _ in transactions` unpacks each 3-item tuple and discards
       the parts we do not need. `_` is the conventional name for "I have to name
       this, but I am not going to use it".
    """
    return sum(amount for _, amount, _ in transactions)


def show_history(transactions):
    """Display all transactions, numbered from 1."""
    # ⚠️ A guard clause: handle the empty case first and leave early, so the rest
    #    of the function can assume there is something to show. A bare `return`
    #    just means "this function is finished".
    if not transactions:
        print("No transactions yet.")
        return

    print("\n--- Transaction History ---")

    # 🔁 `enumerate(..., start=1)` hands back a counter *and* the item on every
    #    pass. Humans count from 1, Python counts from 0, and `start=1` bridges
    #    the two without any manual counter variable.
    for index, (description, amount, category) in enumerate(transactions, start=1):
        # 🧮 Build the sign ourselves and print the absolute value, so money reads
        #    as "-$52.30" instead of "$-52.30" with the minus stranded inside the
        #    number. This is the same format Week 6 introduced — one money format
        #    for the whole course.
        sign = "+" if amount >= 0 else "-"
        print(f"  {index}. [{category}] {description}: {sign}${abs(amount):.2f}")


def show_category_totals(categories):
    """Display the total spent in each category."""
    if not categories:
        print("No spending categories yet.")
        return

    print("\n--- Spending by Category ---")

    # 🔁 `.items()` yields key/value pairs and `sorted()` puts them in a stable,
    #    predictable order, so the report never shuffles between runs.
    for category, total in sorted(categories.items()):
        print(f"  {category}: ${total:.2f}")


def main():
    """Run the interactive tracker until the user chooses to quit.

    📌 THIS IS THE POINT OF WEEK 8. Read the `match` block below: every branch is
       a single line naming what happens. The details live in the functions above.
       Compare it with the Week 7 version, where all of that detail was crammed
       into the loop itself.
    """
    # 🧠 Both containers are created here, in one place, and then passed into the
    #    functions that need them. Nothing in this file uses a global variable.
    transactions = []  # list of (description, amount, category) tuples
    categories = {}    # {"Food": 56.55, ...} — expense totals, kept positive

    print("=" * 44)
    print("   Personal Budget Tracker - Week 8")
    print("=" * 44)

    # 🔁 `while True:` is an intentional forever-loop. It is safe here because
    #    there is exactly one clearly marked way out: the `break` on option 6.
    while True:
        display_menu()
        choice = input("\nChoose an option: ").strip()

        # 🧠 Week 4's `match` compares `choice` against each `case` in order.
        # ⚠️ The cases are strings ("1"), not numbers (1), because `input()`
        #    always returns a string. `case 1:` would never match anything.
        match choice:
            case "1":
                add_income(transactions)
            case "2":
                add_expense(transactions, categories)
            case "3":
                # 🧠 `get_balance()` returns a value, so it can be dropped
                #    straight into an f-string. That is the difference between a
                #    function that returns and one that prints.
                print(f"Current balance: ${get_balance(transactions):.2f}")
            case "4":
                show_history(transactions)
            case "5":
                show_category_totals(categories)
            case "6":
                print("Goodbye!")
                break  # 🔁 the one and only exit from the loop
            case _:
                # ⚠️ `_` is the wildcard: it matches anything the cases above
                #    missed. Without it, a typo would be silently ignored.
                print("Invalid choice. Please choose 1-6.")


# 🧠 This guard means "only run main() when this file is executed directly".
#    If another file ever does `import budget_tracker_week8`, Python sets
#    __name__ to the module name instead of "__main__", so the menu does not
#    hijack that program. Week 12 explains it in full.
if __name__ == "__main__":
    main()
