"""Tests for the three reference implementations.

Two jobs:

1. Check that the logic is correct — balances, category totals, the save/load
   round trip, and the input validation.
2. Check that the code listings printed in `chapters/` still behave exactly like
   the reference files next to them. This is the test that stops the guide and
   the code drifting apart, which is the failure mode this repository is most
   prone to.

Nothing here needs installing. Run it with:

    python -m unittest discover tests -v

or, from the repository root, simply:

    python -m unittest
"""

import ast
import importlib.util
import io
import json
import re
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def load_reference(module_name):
    """Import one of the reference implementations by file name."""
    spec = importlib.util.spec_from_file_location(module_name, REPO_ROOT / f"{module_name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def chapter_code_blocks(chapter_filename):
    """Return every ```python block in a chapter, in order."""
    text = (REPO_ROOT / "chapters" / chapter_filename).read_text(encoding="utf-8")
    return re.findall(r"```python\n(.*?)```", text, re.DOTALL)


def definitions_only(source):
    """Parse `source` and keep only imports, classes, and functions.

    The chapter listings end with an interactive `while True:` loop. Stripping the
    top-level statements lets the tests execute the definitions without the menu
    trying to read from stdin.
    """
    tree = ast.parse(source)
    tree.body = [
        node for node in tree.body
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.ClassDef, ast.FunctionDef))
    ]
    return tree


def build_from_chapter(chapter_filename, required_names, prerequisite_sources=()):
    """Execute the chapter block that defines `required_names` and return its namespace."""
    namespace = {}
    for source in prerequisite_sources:
        exec(compile(definitions_only(source), "<chapter>", "exec"), namespace)

    for block in chapter_code_blocks(chapter_filename):
        try:
            tree = definitions_only(block)
        except SyntaxError:
            continue
        defined = {n.name for n in tree.body if isinstance(n, (ast.ClassDef, ast.FunctionDef))}
        if required_names <= defined:
            exec(compile(tree, "<chapter>", "exec"), namespace)
            return namespace

    raise AssertionError(f"{chapter_filename} has no code block defining {sorted(required_names)}")


def output_of(callable_object, *args, **kwargs):
    """Run something and return whatever it printed."""
    with redirect_stdout(io.StringIO()) as captured:
        callable_object(*args, **kwargs)
    return captured.getvalue()


def feed_input(module_namespace, answers):
    """Replace `input` in a namespace with one that returns `answers` in order."""
    supply = iter(answers)
    module_namespace["input"] = lambda _prompt: next(supply)


week8 = load_reference("budget_tracker_week8")
week10 = load_reference("budget_tracker_week10")
final = load_reference("budget_tracker_final")

SAMPLE_TUPLES = [
    ("Paycheck", 1500.00, "Income"),
    ("Groceries", -52.30, "Food"),
    ("Bus pass", -40.00, "Transport"),
]


def seeded(tracker):
    """Add the same three transactions to any tracker, quietly."""
    with redirect_stdout(io.StringIO()):
        tracker.add_income("Paycheck", 1500)
        tracker.add_expense("Groceries", 52.30, "Food")
        tracker.add_expense("Bus pass", 40.00, "Transport")
    return tracker


# --------------------------------------------------------------------------- #
# Week 8 — plain functions over tuples
# --------------------------------------------------------------------------- #

class TestWeek8(unittest.TestCase):

    def test_balance_is_the_sum_of_signed_amounts(self):
        self.assertAlmostEqual(week8.get_balance(SAMPLE_TUPLES), 1407.70, places=2)

    def test_balance_of_nothing_is_zero(self):
        self.assertEqual(week8.get_balance([]), 0)

    def test_expenses_print_with_the_minus_outside_the_dollar_sign(self):
        printed = output_of(week8.show_history, SAMPLE_TUPLES)
        self.assertIn("-$52.30", printed)
        self.assertNotIn("$-52.30", printed)

    def test_income_prints_with_a_plus(self):
        self.assertIn("+$1500.00", output_of(week8.show_history, SAMPLE_TUPLES))

    def test_empty_history_says_so(self):
        self.assertIn("No transactions yet.", output_of(week8.show_history, []))

    def test_category_totals_are_sorted(self):
        printed = output_of(week8.show_category_totals, {"Transport": 40.0, "Food": 52.30})
        self.assertLess(printed.index("Food"), printed.index("Transport"))


# --------------------------------------------------------------------------- #
# Week 9 / 10 — Transaction and BudgetTracker
# --------------------------------------------------------------------------- #

class TestTransaction(unittest.TestCase):

    def test_negative_amounts_are_expenses(self):
        for module in (week10, final):
            with self.subTest(module=module.__name__):
                self.assertTrue(module.Transaction("Rent", -900, "Bills").is_expense())
                self.assertFalse(module.Transaction("Pay", 900, "Income").is_expense())

    def test_display_accepts_an_index_or_none(self):
        for module in (week10, final):
            with self.subTest(module=module.__name__):
                transaction = module.Transaction("Groceries", -52.30, "Food")
                self.assertIn("2. ", output_of(transaction.display, 2))
                self.assertNotIn(". ", output_of(transaction.display).split("]")[0])

    def test_display_handles_index_zero(self):
        # `if index:` would silently drop position 0; `if index is not None:` does not.
        for module in (week10, final):
            with self.subTest(module=module.__name__):
                self.assertIn("0. ", output_of(module.Transaction("X", 1, "Y").display, 0))

    def test_str_returns_text_rather_than_printing_it(self):
        for module in (week10, final):
            with self.subTest(module=module.__name__):
                rendered = str(module.Transaction("Rent", -900, "Bills"))
                self.assertEqual(rendered, "[Bills] Rent: -$900.00")
                self.assertEqual(output_of(print, module.Transaction("Rent", -900, "Bills")).strip(), rendered)


class TestBudgetTracker(unittest.TestCase):

    def test_balance_matches_the_signed_total(self):
        for module in (week10, final):
            with self.subTest(module=module.__name__):
                self.assertAlmostEqual(seeded(module.BudgetTracker("Alex")).get_balance(), 1407.70, places=2)

    def test_each_tracker_gets_its_own_transaction_list(self):
        for module in (week10, final):
            with self.subTest(module=module.__name__):
                first = seeded(module.BudgetTracker("Alex"))
                second = module.BudgetTracker("Sam")
                self.assertEqual(len(second.transactions), 0)
                self.assertEqual(len(first.transactions), 3)

    def test_category_totals_are_positive_and_exclude_income(self):
        for module in (week10, final):
            with self.subTest(module=module.__name__):
                printed = output_of(seeded(module.BudgetTracker("Alex")).spending_by_category)
                self.assertIn("Food: $52.30", printed)
                self.assertIn("Transport: $40.00", printed)
                self.assertNotIn("Income", printed)

    def test_summary_totals(self):
        for module in (week10, final):
            with self.subTest(module=module.__name__):
                printed = output_of(seeded(module.BudgetTracker("Alex")).show_summary)
                self.assertIn("+$1500.00", printed)
                self.assertIn("-$92.30", printed)

    def test_str_is_a_short_label(self):
        for module in (week10, final):
            with self.subTest(module=module.__name__):
                self.assertEqual(str(module.BudgetTracker("Alex")), "BudgetTracker(Alex, 0 transactions)")


# --------------------------------------------------------------------------- #
# Week 8 / 12 — input validation
# --------------------------------------------------------------------------- #

class TestValidation(unittest.TestCase):

    def _amount_after(self, module, answers):
        feed_input(module.__dict__, answers)
        try:
            with redirect_stdout(io.StringIO()) as captured:
                value = module.get_valid_amount("Amount: $")
            return value, captured.getvalue()
        finally:
            module.__dict__.pop("input", None)

    def test_rejects_words(self):
        for module in (week8, week10, final):
            with self.subTest(module=module.__name__):
                value, printed = self._amount_after(module, ["abc", "12.50"])
                self.assertEqual(value, 12.50)
                self.assertIn("Please enter a number", printed)

    def test_rejects_zero_and_negatives(self):
        for module in (week8, week10, final):
            with self.subTest(module=module.__name__):
                value, printed = self._amount_after(module, ["0", "-5", "12.50"])
                self.assertEqual(value, 12.50)
                self.assertIn("positive number", printed)

    def test_rejects_nan(self):
        # `nan <= 0` is False, so a naive guard would let this through and every
        # total afterwards would be nan.
        for module in (week8, week10, final):
            with self.subTest(module=module.__name__):
                value, printed = self._amount_after(module, ["nan", "12.50"])
                self.assertEqual(value, 12.50)
                self.assertIn("positive number", printed)

    def test_rejects_infinity(self):
        for module in (week8, week10, final):
            with self.subTest(module=module.__name__):
                value, printed = self._amount_after(module, ["inf", "12.50"])
                self.assertEqual(value, 12.50)
                self.assertIn("realistic amount", printed)

    def test_non_empty_text_keeps_asking_without_a_default(self):
        feed_input(final.__dict__, ["", "  ", "Rent"])
        try:
            with redirect_stdout(io.StringIO()):
                self.assertEqual(final.get_non_empty_text("Description: "), "Rent")
        finally:
            final.__dict__.pop("input", None)

    def test_non_empty_text_uses_the_default_when_given_one(self):
        feed_input(final.__dict__, [""])
        try:
            self.assertEqual(final.get_non_empty_text("Category: ", "Uncategorized"), "Uncategorized")
        finally:
            final.__dict__.pop("input", None)


# --------------------------------------------------------------------------- #
# Week 11 — saving and loading
# --------------------------------------------------------------------------- #

class TestSaveAndLoad(unittest.TestCase):

    def setUp(self):
        self._temp = tempfile.TemporaryDirectory()
        self.folder = Path(self._temp.name)

    def tearDown(self):
        self._temp.cleanup()

    def test_round_trip_preserves_everything(self):
        original = seeded(final.BudgetTracker("Alex"))
        path = str(self.folder / "data.json")
        output_of(original.save, path)

        restored = final.BudgetTracker("Nobody")
        output_of(restored.load, path)

        self.assertEqual(restored.owner, "Alex")
        self.assertEqual(len(restored.transactions), 3)
        self.assertAlmostEqual(restored.get_balance(), original.get_balance(), places=2)
        self.assertEqual(restored.transactions[1].category, "Food")

    def test_missing_file_starts_fresh_without_crashing(self):
        tracker = final.BudgetTracker("Alex")
        printed = output_of(tracker.load, str(self.folder / "nothing-here.json"))
        self.assertIn("No saved data found", printed)
        self.assertEqual(tracker.transactions, [])

    def test_invalid_json_starts_fresh_without_crashing(self):
        path = self.folder / "broken.json"
        path.write_text("{ this is not json")
        tracker = final.BudgetTracker("Alex")
        self.assertIn("not valid JSON", output_of(tracker.load, str(path)))

    def test_json_of_the_wrong_shape_starts_fresh_without_crashing(self):
        path = self.folder / "list.json"
        path.write_text("[1, 2, 3]")
        tracker = final.BudgetTracker("Alex")
        self.assertIn("missing expected fields", output_of(tracker.load, str(path)))

    def test_a_malformed_file_leaves_the_tracker_untouched(self):
        # load() builds local variables first and only commits them to self once
        # nothing can fail, so a file that goes bad halfway through must not leave
        # a half-loaded tracker behind.
        path = self.folder / "half-bad.json"
        path.write_text(json.dumps({
            "owner": "Mallory",
            "transactions": [
                {"description": "fine", "amount": 10, "category": "Income"},
                {"description": "no amount key"},
            ],
        }))

        tracker = seeded(final.BudgetTracker("Alex"))
        output_of(tracker.load, str(path))

        self.assertEqual(tracker.owner, "Alex")
        self.assertEqual(len(tracker.transactions), 3)

    def test_a_file_without_categories_still_loads(self):
        path = self.folder / "old-version.json"
        path.write_text(json.dumps({
            "owner": "Alex",
            "transactions": [{"description": "Legacy", "amount": -3}],
        }))
        tracker = final.BudgetTracker("Alex")
        output_of(tracker.load, str(path))
        self.assertEqual(tracker.transactions[0].category, "Uncategorized")


# --------------------------------------------------------------------------- #
# The chapters and the reference files must agree
# --------------------------------------------------------------------------- #

class TestChaptersMatchReferences(unittest.TestCase):
    """Execute the chapter listings and compare them against the reference files.

    If one of these fails, a chapter and its reference implementation have drifted
    apart. Fix whichever one is wrong — do not relax the test.
    """

    @classmethod
    def setUpClass(cls):
        cls.week8_chapter = build_from_chapter(
            "week-08-functions.md",
            {"display_menu", "get_balance", "show_history", "show_category_totals"},
        )

        week9_transaction = next(
            block for block in chapter_code_blocks("week-09-intro-to-oop.md")
            if "class Transaction" in block and "is_expense" in block
        )
        cls.week10_chapter = build_from_chapter(
            "week-10-encapsulation.md", {"BudgetTracker"},
            prerequisite_sources=[week9_transaction],
        )
        cls.week11_chapter = build_from_chapter("week-11-file-io.md", {"Transaction"})
        cls.week12_chapter = build_from_chapter(
            "week-12-inheritance-and-final-project.md",
            {"Transaction", "BudgetTracker", "get_valid_amount", "get_non_empty_text", "main"},
        )

    def test_week8_functions_agree(self):
        self.assertEqual(self.week8_chapter["get_balance"](SAMPLE_TUPLES), week8.get_balance(SAMPLE_TUPLES))
        for name, argument in (
            ("display_menu", None),
            ("show_history", SAMPLE_TUPLES),
            ("show_history", []),
            ("show_category_totals", {"Food": 52.30, "Transport": 40.0}),
            ("show_category_totals", {}),
        ):
            with self.subTest(function=name, argument=argument):
                args = () if argument is None else (argument,)
                self.assertEqual(
                    output_of(self.week8_chapter[name], *args),
                    output_of(getattr(week8, name), *args),
                )

    def test_week9_transaction_agrees(self):
        chapter = self.week10_chapter["Transaction"]("Groceries", -52.30, "Food")
        reference = week10.Transaction("Groceries", -52.30, "Food")
        self.assertEqual(output_of(chapter.display, 2), output_of(reference.display, 2))
        self.assertEqual(chapter.is_expense(), reference.is_expense())

    def test_week10_tracker_agrees(self):
        chapter = seeded(self.week10_chapter["BudgetTracker"]("Alex"))
        reference = seeded(week10.BudgetTracker("Alex"))
        self.assertEqual(chapter.get_balance(), reference.get_balance())
        self.assertEqual(str(chapter), str(reference))
        for method in ("show_history", "show_summary", "spending_by_category"):
            with self.subTest(method=method):
                self.assertEqual(output_of(getattr(chapter, method)), output_of(getattr(reference, method)))

    def test_week10_empty_tracker_agrees(self):
        chapter = self.week10_chapter["BudgetTracker"]("Alex")
        reference = week10.BudgetTracker("Alex")
        for method in ("show_history", "spending_by_category"):
            with self.subTest(method=method):
                self.assertEqual(output_of(getattr(chapter, method)), output_of(getattr(reference, method)))

    def test_week11_serialisation_agrees(self):
        chapter_class = self.week11_chapter["Transaction"]
        self.assertEqual(
            chapter_class("Groceries", -52.3, "Food").to_dict(),
            final.Transaction("Groceries", -52.3, "Food").to_dict(),
        )
        without_category = {"description": "Legacy", "amount": -3}
        self.assertEqual(
            chapter_class.from_dict(without_category).category,
            final.Transaction.from_dict(without_category).category,
        )

    def test_week12_reports_agree(self):
        chapter = seeded(self.week12_chapter["BudgetTracker"]("Alex"))
        reference = seeded(final.BudgetTracker("Alex"))
        self.assertEqual(chapter.get_balance(), reference.get_balance())
        for method in ("show_history", "show_summary", "spending_by_category"):
            with self.subTest(method=method):
                self.assertEqual(output_of(getattr(chapter, method)), output_of(getattr(reference, method)))

    def test_week12_over_budget_warning_agrees(self):
        chapter = self.week12_chapter["BudgetTracker"]("Alex")
        reference = final.BudgetTracker("Alex")
        with redirect_stdout(io.StringIO()):
            chapter.add_expense("Rent", 900, "Bills")
            reference.add_expense("Rent", 900, "Bills")
        self.assertEqual(output_of(chapter.show_summary), output_of(reference.show_summary))

    def test_week12_validation_agrees(self):
        for answers, expected in (
            (["abc", "7"], 7.0),
            (["0", "1"], 1.0),
            (["nan", "12.5"], 12.5),
            (["inf", "3"], 3.0),
        ):
            with self.subTest(answers=answers):
                feed_input(self.week12_chapter, answers)
                with redirect_stdout(io.StringIO()) as chapter_output:
                    chapter_value = self.week12_chapter["get_valid_amount"]("Amount: $")

                feed_input(final.__dict__, answers)
                try:
                    with redirect_stdout(io.StringIO()) as reference_output:
                        reference_value = final.get_valid_amount("Amount: $")
                finally:
                    final.__dict__.pop("input", None)

                self.assertEqual(chapter_value, expected)
                self.assertEqual(chapter_value, reference_value)
                self.assertEqual(chapter_output.getvalue(), reference_output.getvalue())

    def test_week12_files_are_interchangeable(self):
        """A file written by the chapter's code must load in the reference, and back."""
        with tempfile.TemporaryDirectory() as folder:
            chapter = seeded(self.week12_chapter["BudgetTracker"]("Alex"))
            path = str(Path(folder) / "from-chapter.json")
            output_of(chapter.save, path)

            reference = final.BudgetTracker("Nobody")
            output_of(reference.load, path)
            self.assertEqual(reference.owner, "Alex")
            self.assertAlmostEqual(reference.get_balance(), chapter.get_balance(), places=2)

            other_path = str(Path(folder) / "from-reference.json")
            output_of(seeded(final.BudgetTracker("Sam")).save, other_path)

            back = self.week12_chapter["BudgetTracker"]("Nobody")
            output_of(back.load, other_path)
            self.assertEqual(back.owner, "Sam")
            self.assertAlmostEqual(back.get_balance(), 1407.70, places=2)


class TestChapterLinks(unittest.TestCase):
    """Every chapter from Week 6 on should point at the file that implements it."""

    EXPECTED = {
        "week-06-lists-and-tuples.md": "budget_tracker_week8.py",
        "week-07-dictionaries-and-sets.md": "budget_tracker_week8.py",
        "week-08-functions.md": "budget_tracker_week8.py",
        "week-09-intro-to-oop.md": "budget_tracker_week10.py",
        "week-10-encapsulation.md": "budget_tracker_week10.py",
        "week-11-file-io.md": "budget_tracker_final.py",
        "week-12-inheritance-and-final-project.md": "budget_tracker_final.py",
    }

    def test_each_chapter_links_to_its_reference(self):
        for chapter, reference in self.EXPECTED.items():
            with self.subTest(chapter=chapter):
                text = (REPO_ROOT / "chapters" / chapter).read_text(encoding="utf-8")
                self.assertIn("Reference implementation:", text)
                self.assertIn(f"(../{reference})", text)

    def test_every_reference_documents_its_chapters(self):
        for module_name in ("budget_tracker_week8", "budget_tracker_week10", "budget_tracker_final"):
            with self.subTest(module=module_name):
                docstring = load_reference(module_name).__doc__
                self.assertIsNotNone(docstring, f"{module_name} has no module docstring")
                self.assertIn("chapters/", docstring)
                self.assertIn("HOW TO RUN IT", docstring)

    def test_every_function_and_method_is_documented(self):
        for module_name in ("budget_tracker_week8", "budget_tracker_week10", "budget_tracker_final"):
            source = (REPO_ROOT / f"{module_name}.py").read_text(encoding="utf-8")
            for node in ast.walk(ast.parse(source)):
                if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                    with self.subTest(module=module_name, name=node.name):
                        self.assertIsNotNone(
                            ast.get_docstring(node),
                            f"{module_name}.{node.name} has no docstring",
                        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
