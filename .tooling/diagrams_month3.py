"""Month 3 diagrams: weeks 9-12, the bonus chapter, and the course roadmap."""

from __future__ import annotations

from diagram_kit import (
    ACCENT_TAG,
    CODE,
    FLOW,
    FLOW_SOFT,
    MUTED,
    SUBTITLE,
    TITLE,
    Diagram,
    arrow,
    card,
    circle,
    code_block,
    color,
    divider,
    elbow,
    legend,
    legend_width,
    line,
    note,
    path,
    rect,
    section,
    text,
)


def _marker(hue: str) -> str:
    return {
        "blue": "flowBlue",
        "green": "flowGreen",
        "purple": "flowPurple",
        "amber": "flowAmber",
        "cyan": "flowCyan",
        "red": "flowRed",
        "slate": "flowSoft",
        "pink": "flow",
    }[hue]


# ---------------------------------------------------------------------------
# Week 9
# ---------------------------------------------------------------------------


def week09_blueprint_to_objects() -> tuple[str, str]:
    d = Diagram(
        1240,
        760,
        eyebrow="Week 09 · Intro to OOP",
        title="One Blueprint, Many Objects",
        subtitle="The class is written once. Every instance gets its own attribute values but shares the same methods",
    )

    d.add(section(58, 150, 480, 424, "01", "the class · a blueprint"))
    d.add(
        code_block(
            84,
            190,
            428,
            [
                [("class", CODE["kw"]), (" Dog", CODE["cls"]), (":", CODE["op"])],
                [("    def", CODE["kw"]), (" __init__", CODE["fn"]), ("(", CODE["op"]), ("self", CODE["var"]), (", name, breed, age):", CODE["op"])],
                [("        self.name  ", CODE["var"]), ("= name", CODE["op"])],
                [("        self.breed ", CODE["var"]), ("= breed", CODE["op"])],
                [("        self.age   ", CODE["var"]), ("= age", CODE["op"])],
                [("", CODE["op"])],
                [("    def", CODE["kw"]), (" bark", CODE["fn"]), ("(", CODE["op"]), ("self", CODE["var"]), ("):", CODE["op"])],
                [("        print", CODE["fn"]), ("(", CODE["op"]), ('f"{self.name} says: Woof!"', CODE["str"]), (")", CODE["op"])],
            ],
            size=11.5,
            leading=21,
        )
    )
    d.add(
        card(
            84,
            418,
            428,
            72,
            "purple",
            title="Stored once, on the class",
            subtitle="__init__  ·  bark  ·  describe",
            title_size=14,
        )
    )
    d.add(text(298, 528, "No dog exists yet. This is only the plan.", size=11.5, fill=SUBTITLE, anchor="middle"))

    d.add(section(710, 150, 472, 424, "02", "the objects · real instances"))
    dogs = [
        ("my_dog", "Buddy", "Golden Retriever", "3", "green"),
        ("your_dog", "Luna", "Husky", "5", "cyan"),
    ]
    for index, (variable, name, breed, age, hue) in enumerate(dogs):
        c = color(hue)
        y = 194 + index * 178
        d.add(rect(736, y, 420, 152, rx=11, fill=c["fill"], stroke=c["stroke"], width=1.9))
        d.add(text(756, y + 28, variable, size=14, fill=TITLE, mono=True, weight="700"))
        d.add(text(1136, y + 28, "Dog instance", size=10, fill=c["dim"], anchor="end", mono=True, weight="700"))
        d.add(line(752, y + 42, 1140, y + 42, stroke=c["stroke"], width=1, opacity=0.35))
        for j, (key, value) in enumerate([("self.name", f'"{name}"'), ("self.breed", f'"{breed}"'), ("self.age", age)]):
            d.add(text(760, y + 70 + j * 26, key, size=12, fill=c["dim"], mono=True))
            d.add(text(1132, y + 70 + j * 26, value, size=12.5, fill=TITLE, anchor="end", mono=True, weight="700"))
        d.add(arrow(692, y + 76, 730, y + 76, stroke=c["stroke"], marker=_marker(hue), width=2.2))

    d.add(text(946, 556, "Two objects, two sets of values, one shared set of methods.", size=11.5, fill=SUBTITLE, anchor="middle"))

    d.add(
        note(
            58,
            602,
            546,
            "amber",
            "class vs object",
            "Dog is the class. my_dog is an object (also called an instance). Dog(\"Buddy\", ...) is the moment one is built.",
        )
    )
    d.add(
        note(
            636,
            602,
            546,
            "blue",
            "naming convention",
            "Classes use PascalCase nouns: Transaction, BudgetTracker. Methods use snake_case verbs: add_income(), is_expense().",
        )
    )
    return "week-09-class-blueprint-to-objects.svg", d.render()


def week09_init_and_self() -> tuple[str, str]:
    d = Diagram(
        1280,
        720,
        eyebrow="Week 09 · Intro to OOP",
        title="What self Actually Is",
        subtitle="Dog(\"Buddy\", \"Golden Retriever\", 3) is four steps — and self is just the object being built",
    )

    top = 156
    height = 268
    col_w = 276
    gap = 22
    xs = [50 + index * (col_w + gap) for index in range(4)]

    steps = [
        ("01", "you call the class", "Dog(\"Buddy\", ...)", "cyan", ["Python sees a class,", "not a plain function."]),
        ("02", "an empty object is made", "<Dog object>", "blue", ["No attributes yet.", "Just an empty instance."]),
        ("03", "__init__ runs", "__init__(self, ...)", "amber", ["The new object is passed", "in as the first argument."]),
        ("04", "the object is handed back", "my_dog = <Dog>", "green", ["self.name is now \"Buddy\".", "The name my_dog is bound."]),
    ]
    for index, (num, label, code, hue, body) in enumerate(steps):
        c = color(hue)
        x = xs[index]
        d.add(section(x, top, col_w, height, num, label))
        d.add(rect(x + 20, top + 40, col_w - 40, 56, rx=10, fill=c["fill"], stroke=c["stroke"], width=1.8))
        d.add(text(x + col_w / 2, top + 74, code, size=13.5, fill=TITLE, anchor="middle", mono=True, weight="700"))
        for j, chunk in enumerate(body):
            d.add(text(x + col_w / 2, top + 128 + j * 19, chunk, size=11.5, fill=SUBTITLE, anchor="middle"))
        if index < 3:
            d.add(arrow(x + col_w + 2, top + height / 2, xs[index + 1] - 6, top + height / 2, width=2.3))

    d.add(rect(xs[2] + 20, top + 176, col_w - 40, 70, rx=9, fill="#080e1c", stroke=color("amber")["stroke"], width=1.3))
    d.add(text(xs[2] + 34, top + 200, "self.name  = name", size=11, fill=color("amber")["dim"], mono=True))
    d.add(text(xs[2] + 34, top + 220, "self.breed = breed", size=11, fill=color("amber")["dim"], mono=True))
    d.add(text(xs[2] + 34, top + 240, "self.age   = age", size=11, fill=color("amber")["dim"], mono=True))

    d.add(divider(50, 1230, 468, label="calling a method is the same trick"))

    d.add(
        code_block(
            50,
            496,
            568,
            [
                [("my_dog.", CODE["var"]), ("bark", CODE["fn"]), ("()", CODE["op"]), ("          # what you write", CODE["com"])],
                [("Dog.", CODE["cls"]), ("bark", CODE["fn"]), ("(my_dog)", CODE["op"]), ("       # what Python does", CODE["com"])],
                [("", CODE["op"])],
                [("Buddy says: Woof!", CODE["out"])],
            ],
            size=12.5,
            leading=22,
        )
    )
    d.add(
        note(
            650,
            496,
            580,
            "purple",
            "so why write self at all?",
            "Because the object has to arrive somewhere. Python passes it as the first argument to every method; self is just the conventional name for that slot.",
        )
    )
    d.add(
        note(
            650,
            600,
            580,
            "red",
            "the classic beginner error",
            "Leaving self out of a method signature gives 'takes 0 positional arguments but 1 was given' — the object was still passed in.",
        )
    )
    return "week-09-init-and-self.svg", d.render()


# ---------------------------------------------------------------------------
# Week 10
# ---------------------------------------------------------------------------


def week10_encapsulation_boundary() -> tuple[str, str]:
    d = Diagram(
        1240,
        760,
        eyebrow="Week 10 · Encapsulation",
        title="The Class Is a Boundary",
        subtitle="Outside code asks the object to do something — it does not reach in and rearrange the furniture",
    )

    bx, by, bw, bh = 380, 150, 468, 442
    d.add(rect(bx - 8, by - 8, bw + 16, bh + 16, rx=18, fill="none", stroke=color("purple")["stroke"], width=2, opacity=0.4, filter_id="neon"))
    d.add(rect(bx, by, bw, bh, rx=16, fill="#120a24", stroke=color("purple")["stroke"], width=2))
    d.add(text(bx + bw / 2, by + 34, "BudgetTracker", size=19, fill=TITLE, anchor="middle", weight="700"))
    d.add(text(bx + bw / 2, by + 54, "one object that owns its own data", size=11, fill=color("purple")["dim"], anchor="middle"))

    d.add(text(bx + 28, by + 92, "STATE", size=10, fill=MUTED, mono=True, weight="700", spacing=1.8))
    for index, (attr, value) in enumerate([("self.owner", '"Alex"'), ("self.transactions", "[ 3 Transaction ]")]):
        y = by + 108 + index * 44
        c = color("cyan")
        d.add(rect(bx + 28, y, bw - 56, 36, rx=8, fill=c["fill"], stroke=c["stroke"], width=1.4))
        d.add(text(bx + 44, y + 24, attr, size=12, fill=c["text"], mono=True))
        d.add(text(bx + bw - 44, y + 24, value, size=11, fill=c["dim"], anchor="end", mono=True))

    d.add(text(bx + 28, by + 218, "BEHAVIOUR · THE ONLY WAY IN", size=10, fill=MUTED, mono=True, weight="700", spacing=1.8))
    methods = [
        ("add_income(desc, amount)", "green"),
        ("add_expense(desc, amount, cat)", "green"),
        ("get_balance()", "blue"),
        ("show_summary()", "blue"),
        ("__str__()", "amber"),
    ]
    for index, (name, hue) in enumerate(methods):
        c = color(hue)
        y = by + 234 + index * 38
        d.add(rect(bx + 28, y, bw - 56, 30, rx=7, fill=c["fill"], stroke=c["stroke"], width=1.3))
        d.add(text(bx + 44, y + 20, name, size=12, fill=c["text"], mono=True))

    d.add(
        card(
            48,
            210,
            250,
            118,
            "green",
            title="Allowed",
            subtitle="tracker.add_expense(\"Coffee\", 4.5, \"Food\")",
        )
    )
    d.add(arrow(304, 262, bx - 6, 262, stroke=color("green")["stroke"], marker="flowGreen", width=2.4))
    d.add(text(339, 244, "goes through", size=9.5, fill=color("green")["dim"], anchor="middle", mono=True))
    d.add(text(339, 233, "a method", size=9.5, fill=color("green")["dim"], anchor="middle", mono=True))

    d.add(
        card(
            48,
            392,
            250,
            118,
            "red",
            title="Avoid",
            subtitle="tracker.transactions.append(\"oops\")",
        )
    )
    d.add(line(304, 444, bx - 6, 444, stroke=color("red")["stroke"], width=2.4, dash="6 5"))
    d.add(circle(339, 444, 13, fill="#2e0e0e", stroke=color("red")["stroke"], width=2))
    d.add(line(334, 439, 344, 449, stroke=color("red")["text"], width=2))
    d.add(line(344, 439, 334, 449, stroke=color("red")["text"], width=2))
    d.add(text(173, 534, "no validation, no invariants,", size=10, fill=color("red")["dim"], anchor="middle"))
    d.add(text(173, 550, "no summary update", size=10, fill=color("red")["dim"], anchor="middle"))

    d.add(
        card(
            930,
            210,
            252,
            118,
            "blue",
            title="Reads are cheap",
            subtitle="tracker.get_balance() recomputes from the list every time",
        )
    )
    d.add(arrow(bx + bw + 6, 262, 924, 262, stroke=color("blue")["stroke"], marker="flowBlue", width=2.4))

    d.add(
        card(
            930,
            392,
            252,
            118,
            "amber",
            title="__str__",
            subtitle="print(tracker) shows something a human can read",
        )
    )
    d.add(arrow(bx + bw + 6, 444, 924, 444, stroke=color("amber")["stroke"], marker="flowAmber", width=2.4))

    d.add(
        note(
            58,
            626,
            546,
            "purple",
            "what encapsulation buys you",
            "Validation lives in one place, the class can change its internals without breaking callers, and the main loop shrinks to menu handling.",
        )
    )
    d.add(
        note(
            636,
            626,
            546,
            "slate",
            "python's convention, not a lock",
            "A leading underscore (_balance) signals 'internal, please do not touch'. Python trusts you rather than enforcing it.",
        )
    )
    return "week-10-encapsulation-boundary.svg", d.render()


def week10_list_of_objects() -> tuple[str, str]:
    d = Diagram(
        1260,
        720,
        eyebrow="Week 10 · Encapsulation",
        title="A List of Objects Is Where It All Comes Together",
        subtitle="Week 6 gave you the list, Week 9 gave you the object — the summary is one comprehension over both",
    )

    d.add(section(58, 150, 604, 396, "01", "self.transactions"))
    rows = [
        ("Paycheck", "+1500.00", "Income", "green"),
        ("Groceries", "-52.30", "Food", "amber"),
        ("Bus pass", "-38.00", "Transport", "cyan"),
    ]
    for index, (desc, amount, category, hue) in enumerate(rows):
        c = color(hue)
        y = 196 + index * 104
        d.add(rect(84, y, 552, 86, rx=11, fill=c["fill"], stroke=c["stroke"], width=1.8))
        d.add(text(104, y + 26, f"[{index}]", size=11, fill=c["dim"], mono=True, weight="700"))
        d.add(text(150, y + 26, "Transaction object", size=11, fill=c["dim"], mono=True))
        d.add(line(100, y + 38, 620, y + 38, stroke=c["stroke"], width=1, opacity=0.3))
        columns = [
            (104, ".description", f'"{desc}"'),
            (296, ".amount", amount),
            (472, ".category", f'"{category}"'),
        ]
        for cx, label, value in columns:
            d.add(text(cx, y + 58, label, size=10.5, fill=c["dim"], mono=True))
            d.add(text(cx, y + 76, value, size=12.5, fill=TITLE, mono=True, weight="700"))

    d.add(section(714, 150, 468, 396, "02", "one line summarises all of them"))
    d.add(
        code_block(
            738,
            190,
            420,
            [
                [("sum", CODE["fn"]), ("(", CODE["op"]), ("t.amount ", CODE["var"]), ("for", CODE["kw"]), (" t ", CODE["var"]), ("in", CODE["kw"])],
                [("    self.transactions)", CODE["var"])],
            ],
            size=12,
            leading=20,
        )
    )
    d.add(arrow(668, 300, 730, 300, width=2.4))

    outputs = [
        ("Total income", "+1500.00", "green"),
        ("Total expenses", "-90.30", "red"),
        ("Net balance", "1409.70", "blue"),
    ]
    for index, (label, value, hue) in enumerate(outputs):
        c = color(hue)
        y = 288 + index * 74
        d.add(rect(738, y, 420, 58, rx=10, fill=c["fill"], stroke=c["stroke"], width=1.7))
        d.add(text(758, y + 36, label, size=13, fill=c["text"]))
        d.add(text(1138, y + 37, value, size=17, fill=TITLE, anchor="end", mono=True, weight="700"))

    d.add(divider(58, 1182, 578, label="__str__ turns the object into readable text"))

    d.add(
        code_block(
            58,
            606,
            546,
            [
                [("def", CODE["kw"]), (" __str__", CODE["fn"]), ("(", CODE["op"]), ("self", CODE["var"]), ("):", CODE["op"])],
                [("    return", CODE["kw"]), (' f"BudgetTracker({self.owner}, ..."', CODE["str"])],
            ],
            size=11.5,
            leading=20,
        )
    )
    d.add(
        code_block(
            636,
            606,
            546,
            [
                [("print", CODE["fn"]), ("(tracker)", CODE["op"])],
                [("BudgetTracker(Alex, 3 transactions)", CODE["out"])],
            ],
            size=11.5,
            leading=20,
        )
    )
    return "week-10-objects-in-a-list.svg", d.render()


# ---------------------------------------------------------------------------
# Week 11
# ---------------------------------------------------------------------------


def week11_with_open() -> tuple[str, str]:
    d = Diagram(
        1220,
        700,
        eyebrow="Week 11 · File I/O",
        title="What with open(...) Guarantees",
        subtitle="The file is closed when the block ends — including when the block blows up halfway through",
    )

    d.add(section(58, 150, 546, 402, "01", "with · the context manager"))
    d.add(
        code_block(
            84,
            190,
            494,
            [
                [("with", CODE["kw"]), (" open", CODE["fn"]), ("(", CODE["op"]), ('"notes.txt"', CODE["str"]), (", ", CODE["op"]), ('"w"', CODE["str"]), (") ", CODE["op"]), ("as", CODE["kw"]), (" f:", CODE["var"])],
                [("    f.", CODE["var"]), ("write", CODE["fn"]), ("(", CODE["op"]), ('"Hello\\n"', CODE["str"]), (")", CODE["op"])],
                [("# file is already closed here", CODE["com"])],
            ],
            size=12,
            leading=21,
            stroke="#1f4030",
        )
    )
    steps = [
        ("open the file", "OS hands back a file object", "cyan"),
        ("run the block", "read or write through f", "green"),
        ("close it — always", "even if an exception is raised", "purple"),
    ]
    for index, (label, body, hue) in enumerate(steps):
        c = color(hue)
        y = 300 + index * 76
        d.add(rect(84, y, 494, 62, rx=10, fill=c["fill"], stroke=c["stroke"], width=1.7))
        d.add(circle(112, y + 31, 13, fill="#0b1220", stroke=c["stroke"], width=1.5))
        d.add(text(112, y + 35, str(index + 1), size=11, fill=c["dim"], anchor="middle", mono=True, weight="700"))
        d.add(text(138, y + 27, label, size=13.5, fill=TITLE, weight="700"))
        d.add(text(138, y + 47, body, size=11, fill=c["dim"]))
        if index < 2:
            d.add(arrow(112, y + 62, 112, y + 74, width=2))

    d.add(section(636, 150, 546, 402, "02", "manual open · one missing line away from a leak"))
    d.add(
        code_block(
            662,
            190,
            494,
            [
                [("f ", CODE["var"]), ("= ", CODE["op"]), ("open", CODE["fn"]), ("(", CODE["op"]), ('"notes.txt"', CODE["str"]), (", ", CODE["op"]), ('"w"', CODE["str"]), (")", CODE["op"])],
                [("f.", CODE["var"]), ("write", CODE["fn"]), ("(", CODE["op"]), ("data)", CODE["op"]), ("        # raises here?", CODE["com"])],
                [("f.", CODE["var"]), ("close", CODE["fn"]), ("()", CODE["op"]), ("             # never reached", CODE["com"])],
            ],
            size=12,
            leading=21,
            stroke="#5b1b1b",
        )
    )
    d.add(
        card(
            662,
            300,
            494,
            110,
            "red",
            title="Handle stays open",
            subtitle="Buffered bytes may never reach disk, and the OS keeps the lock until the process exits.",
        )
    )
    d.add(
        note(
            662,
            426,
            494,
            "amber",
            "the modes you will use",
            '"r" read (default) · "w" write, truncates the file first · "a" append to the end.',
        )
    )

    d.add(
        note(
            58,
            586,
            1124,
            "cyan",
            "same idea, different resources",
            "with also works for network sockets, database connections, and locks. Any object that needs deterministic cleanup can be a context manager.",
        )
    )
    return "week-11-with-open-lifecycle.svg", d.render()


def week11_save_load_roundtrip() -> tuple[str, str]:
    d = Diagram(
        1320,
        740,
        eyebrow="Week 11 · File I/O",
        title="The Save / Load Round Trip",
        subtitle="Objects cannot be written to disk directly — convert to plain dicts on the way out, rebuild objects on the way in",
    )

    top = 172
    box_w = 268
    gap = 30
    xs = [40 + index * (box_w + gap) for index in range(4)]

    save = [
        ("Transaction objects", "green", ["Transaction(\"Paycheck\",", "  1500.0, \"Income\")"], "in memory"),
        ("to_dict()", "cyan", ["{\"description\": ...,", " \"amount\": ...}"], "objects -> plain dicts"),
        ("json.dump()", "purple", ["json.dump(data, f,", "          indent=2)"], "dicts -> text"),
        ("budget_data.json", "amber", ["{", "  \"owner\": \"Alex\", ...", "}"], "on disk"),
    ]
    d.add(section(40, top, 1240, 168, "01", "saving"))
    for index, (title, hue, body, caption) in enumerate(save):
        c = color(hue)
        x = xs[index]
        d.add(rect(x, top + 34, box_w, 112, rx=11, fill=c["fill"], stroke=c["stroke"], width=1.8))
        d.add(text(x + box_w / 2, top + 60, title, size=14, fill=TITLE, anchor="middle", weight="700"))
        for j, chunk in enumerate(body):
            d.add(text(x + box_w / 2, top + 84 + j * 17, chunk, size=10.5, fill=c["dim"], anchor="middle", mono=True))
        d.add(text(x + box_w / 2, top + 138, caption, size=10, fill=c["text"], anchor="middle", mono=True))
        if index < 3:
            d.add(arrow(x + box_w + 4, top + 90, x + box_w + gap - 8, top + 90, width=2.3))

    load_top = 396
    load = [
        ("budget_data.json", "amber", ["text on disk"], "read with open()"),
        ("json.load()", "purple", ["data = json.load(f)"], "text -> dicts"),
        ("from_dict()", "cyan", ["Transaction.from_dict(", "  item)"], "dicts -> objects"),
        ("Transaction objects", "green", ["tracker.transactions"], "back in memory"),
    ]
    d.add(section(40, load_top, 1240, 168, "02", "loading"))
    for index, (title, hue, body, caption) in enumerate(load):
        c = color(hue)
        x = xs[index]
        d.add(rect(x, load_top + 34, box_w, 112, rx=11, fill=c["fill"], stroke=c["stroke"], width=1.8))
        d.add(text(x + box_w / 2, load_top + 62, title, size=14, fill=TITLE, anchor="middle", weight="700"))
        for j, chunk in enumerate(body):
            d.add(text(x + box_w / 2, load_top + 88 + j * 17, chunk, size=10.5, fill=c["dim"], anchor="middle", mono=True))
        d.add(text(x + box_w / 2, load_top + 138, caption, size=10, fill=c["text"], anchor="middle", mono=True))
        if index < 3:
            d.add(arrow(x + box_w + 4, load_top + 90, x + box_w + gap - 8, load_top + 90, width=2.3))

    d.add(
        elbow(
            [(xs[3] + box_w / 2, top + 150), (xs[3] + box_w / 2, 356), (xs[0] + box_w / 2, 356), (xs[0] + box_w / 2, load_top + 30)],
            stroke=color("amber")["stroke"],
            marker="flowAmber",
            width=2.2,
            dash="6 5",
        )
    )
    d.add(text(660, 348, "the same file, next time the program starts", size=11, fill=color("amber")["dim"], anchor="middle", mono=True))

    d.add(
        note(
            40,
            600,
            620,
            "green",
            "why to_dict / from_dict exist",
            "json only understands dict, list, str, int, float, bool and None. A Transaction is none of those, so you translate at the boundary.",
        )
    )
    d.add(
        note(
            692,
            600,
            588,
            "red",
            "handle the first run",
            "The very first load() has no file. Catch FileNotFoundError and start empty — do not let a missing file crash the app.",
        )
    )
    return "week-11-save-load-roundtrip.svg", d.render()


def week11_try_except() -> tuple[str, str]:
    d = Diagram(
        1220,
        720,
        eyebrow="Week 11 · File I/O",
        title="How try / except Changes the Path",
        subtitle="An exception stops the try block instantly and looks for the first except that matches its type",
    )

    d.add(
        code_block(
            58,
            150,
            460,
            [
                [("try", CODE["kw"]), (":", CODE["op"])],
                [("    number ", CODE["var"]), ("= ", CODE["op"]), ("int", CODE["fn"]), ("(", CODE["op"]), ("input", CODE["fn"]), ("())", CODE["op"])],
                [("    result ", CODE["var"]), ("= ", CODE["op"]), ("100", CODE["num"]), (" / number", CODE["op"])],
                [("    print", CODE["fn"]), ("(result)", CODE["op"])],
                [("except", CODE["kw"]), (" ValueError", CODE["cls"]), (":", CODE["op"])],
                [("    print", CODE["fn"]), ("(", CODE["op"]), ('"Not a number!"', CODE["str"]), (")", CODE["op"])],
                [("except", CODE["kw"]), (" ZeroDivisionError", CODE["cls"]), (":", CODE["op"])],
                [("    print", CODE["fn"]), ("(", CODE["op"]), ('"Cannot divide by zero!"', CODE["str"]), (")", CODE["op"])],
            ],
            title="THE CODE",
            size=12,
            leading=22,
        )
    )
    d.add(
        note(
            58,
            420,
            460,
            "amber",
            "order matters here too",
            "Excepts are checked top to bottom, just like elif. Put the specific errors first and the broad ones last.",
        )
    )
    d.add(
        note(
            58,
            530,
            460,
            "red",
            "do not swallow everything",
            "A bare except: hides typos and logic bugs as well as the failure you meant to handle. Name the exception you expect.",
        )
    )

    x = 570
    d.add(section(x, 150, 592, 486, "01", "three inputs, three paths"))

    paths = [
        ("25", "green", "no exception", ["int(\"25\") -> 25", "100 / 25 -> 4.0", "prints 4.0"], "the try block finishes"),
        ("abc", "amber", "ValueError raised", ["int(\"abc\") boom", "line 3 never runs", "prints Not a number!"], "first except matches"),
        ("0", "purple", "ZeroDivisionError raised", ["int(\"0\") -> 0", "100 / 0 boom", "prints Cannot divide by zero!"], "second except matches"),
    ]
    for index, (typed, hue, headline, body, footer) in enumerate(paths):
        c = color(hue)
        y = 190 + index * 148
        d.add(rect(x + 24, y, 544, 124, rx=11, fill=c["fill"], stroke=c["stroke"], width=1.8))
        d.add(text(x + 86, y + 16, "user types", size=9, fill=c["dim"], anchor="middle", mono=True, weight="700"))
        d.add(rect(x + 44, y + 24, 84, 38, rx=8, fill="#0b1220", stroke=c["stroke"], width=1.5))
        d.add(text(x + 86, y + 50, typed, size=17, fill=TITLE, anchor="middle", mono=True, weight="700"))
        d.add(text(x + 146, y + 38, headline, size=13, fill=TITLE, weight="700"))
        d.add(text(x + 146, y + 58, footer, size=10.5, fill=c["dim"], mono=True))
        for j, chunk in enumerate(body):
            d.add(text(x + 44, y + 86 + j * 17, chunk, size=10.5, fill=c["dim"], mono=True))

    d.add(
        text(
            d.center,
            676,
            "Whatever happens, the program keeps running — that is the entire point.",
            size=12,
            fill=SUBTITLE,
            anchor="middle",
        )
    )
    return "week-11-try-except-flow.svg", d.render()


# ---------------------------------------------------------------------------
# Week 12
# ---------------------------------------------------------------------------


def week12_inheritance() -> tuple[str, str]:
    d = Diagram(
        1240,
        790,
        eyebrow="Week 12 · Inheritance",
        title="Inheritance, super(), and Attribute Lookup",
        subtitle="A child gets everything the parent has, then adds to it or replaces part of it",
    )

    d.add(
        card(
            d.center - 230,
            146,
            460,
            118,
            "purple",
            title="Animal",
            subtitle="the base class",
            lines=["__init__(self, name, sound)", "speak()"],
            line_size=12,
            lines_top=216,
        )
    )

    children = [
        (
            96,
            "Cat(Animal)",
            "cyan",
            ["__init__()      overrides", "  -> super().__init__(name, \"Meow\")", "speak()         inherited", "purr()          new"],
        ),
        (
            466,
            "Dog(Animal)",
            "green",
            ["__init__()      overrides", "  -> super().__init__(name, \"Woof\")", "speak()         inherited", "fetch(item)     new"],
        ),
        (
            836,
            "LoudDog(Dog)",
            "amber",
            ["__init__()      inherited", "speak()         OVERRIDES Dog", "fetch(item)     inherited", "", ""],
        ),
    ]
    for x, title, hue, lines in children:
        d.add(
            card(
                x,
                336,
                308,
                160,
                hue,
                title=title,
                lines=lines,
                line_size=10.5,
                lines_top=396,
                lines_anchor="start",
            )
        )

    d.add(elbow([(250, 264), (250, 306), (250, 330)], stroke=color("cyan")["stroke"], marker="flowCyan", width=2.2))
    d.add(elbow([(620, 264), (620, 330)], stroke=color("green")["stroke"], marker="flowGreen", width=2.2))
    d.add(elbow([(774, 416), (830, 416)], stroke=color("amber")["stroke"], marker="flowAmber", width=2.2))
    d.add(text(560, 300, "inherits from", size=10.5, fill=MUTED, anchor="middle", mono=True))

    d.add(divider(58, 1182, 542, label="what happens when you call kitty.speak()"))

    lookup = [
        ("1", "Look on the Cat class", "not found", "slate"),
        ("2", "Follow the MRO up to Animal", "found", "green"),
        ("3", "Run Animal.speak(kitty)", "Whiskers says Meow!", "green"),
    ]
    for index, (num, label, result, hue) in enumerate(lookup):
        c = color(hue)
        x = 58 + index * 378
        d.add(rect(x, 572, 356, 76, rx=10, fill=c["fill"], stroke=c["stroke"], width=1.7))
        d.add(circle(x + 26, 598, 12, fill="#0b1220", stroke=c["stroke"], width=1.5))
        d.add(text(x + 26, 602, num, size=10.5, fill=c["dim"], anchor="middle", mono=True, weight="700"))
        d.add(text(x + 48, 602, label, size=12.5, fill=TITLE, weight="600"))
        d.add(text(x + 48, 628, result, size=11, fill=c["dim"], mono=True))
        if index < 2:
            d.add(arrow(x + 358, 610, x + 372, 610, width=2))

    d.add(
        note(
            58,
            676,
            546,
            "amber",
            "super() is not magic",
            "super().__init__(name, \"Meow\") simply runs the parent's setup so the child does not have to copy those assignments.",
        )
    )
    d.add(
        note(
            636,
            676,
            546,
            "red",
            "use it sparingly",
            "The budget tracker gets its strength from composition — a tracker HAS transactions. Reach for inheritance only when the child truly IS a kind of the parent.",
        )
    )
    return "week-12-inheritance-and-super.svg", d.render()


def week12_final_architecture() -> tuple[str, str]:
    d = Diagram(
        1360,
        920,
        eyebrow="Week 12 · Final Project Assembly",
        title="Personal Budget Tracker · Full Application Topology",
        subtitle="Every concept from the 12 weeks, wired together into one running program",
    )

    d.add(section(48, 150, 380, 214, "01", "entry point"))
    d.add(
        card(
            72,
            186,
            332,
            152,
            "pink",
            title="main()",
            subtitle="banner · ask for name · load saved data",
            lines=["if __name__ == \"__main__\":", "    main()"],
            line_size=11,
            lines_top=284,
            footer="week 1 · week 8",
        )
    )

    d.add(section(468, 150, 380, 214, "02", "the loop"))
    d.add(
        card(
            492,
            186,
            332,
            152,
            "cyan",
            title="while True:",
            subtitle="show the menu, read one choice, repeat",
            lines=["choice = input(...).strip()"],
            line_size=11,
            lines_top=296,
            footer="week 5",
        )
    )

    d.add(section(888, 150, 424, 214, "03", "the dispatcher"))
    d.add(
        card(
            912,
            186,
            376,
            152,
            "amber",
            title="match choice:",
            subtitle="seven cases plus a wildcard fallback",
            lines=["case \"1\" ... case \"7\" ... case _"],
            line_size=11,
            lines_top=296,
            footer="week 3 · week 4",
        )
    )

    d.add(arrow(408, 262, 462, 262, width=2.4))
    d.add(arrow(828, 262, 882, 262, width=2.4))

    d.add(section(48, 418, 1264, 250, "04", "the domain model"))

    d.add(
        card(
            76,
            458,
            560,
            192,
            "purple",
            title="BudgetTracker",
            subtitle="owns the data and every rule that touches it",
            lines=[
                "owner                 transactions[]",
                "add_income()          add_expense()",
                "get_balance()         show_summary()",
                "spending_by_category()",
                "save()                load()",
            ],
            line_size=11.5,
            lines_top=530,
            lines_anchor="start",
            footer="week 9 · week 10 · week 11",
        )
    )
    d.add(
        card(
            690,
            458,
            300,
            192,
            "green",
            title="Transaction",
            subtitle="one record, one responsibility",
            lines=[
                "description",
                "amount",
                "category",
                "is_expense()  display()",
                "to_dict()     from_dict()",
            ],
            line_size=11.5,
            lines_top=530,
            lines_anchor="start",
            footer="week 9 · week 11",
        )
    )
    d.add(
        card(
            1032,
            458,
            256,
            192,
            "blue",
            title="Input helpers",
            subtitle="never trust raw input()",
            lines=[
                "get_valid_amount()",
                "get_non_empty_text()",
                "",
                "float() + try/except",
                "loop until valid",
            ],
            line_size=11.5,
            lines_top=530,
            lines_anchor="start",
            footer="week 2 · week 11",
        )
    )

    d.add(arrow(642, 554, 684, 554, stroke=color("green")["stroke"], marker="flowGreen", width=2.2))
    d.add(text(663, 540, "has many", size=9.5, fill=color("green")["dim"], anchor="middle", mono=True))
    d.add(arrow(996, 554, 1026, 554, stroke=color("blue")["stroke"], marker="flowBlue", width=2.2))

    d.add(elbow([(1100, 344), (1100, 386), (356, 386), (356, 452)], stroke=FLOW, marker="flow", width=2.4))
    d.add(text(700, 378, "each case calls one tracker method", size=10.5, fill=ACCENT_TAG, anchor="middle", mono=True))

    d.add(section(48, 718, 1264, 130, "05", "persistence"))
    d.add(
        card(
            76,
            752,
            420,
            80,
            "amber",
            title="budget_data.json",
            subtitle="owner + list of transaction dicts",
            title_size=15,
        )
    )
    d.add(arrow(196, 660, 196, 746, stroke=color("amber")["stroke"], marker="flowAmber", width=2.4))
    d.add(text(208, 706, "save()", size=11, fill=color("amber")["dim"], mono=True, weight="700"))
    d.add(arrow(392, 746, 392, 660, stroke=color("amber")["stroke"], marker="flowAmber", width=2.4, dash="6 5"))
    d.add(text(404, 706, "load() on startup", size=11, fill=color("amber")["dim"], mono=True))

    d.add(
        card(
            760,
            744,
            528,
            94,
            "slate",
            title="Data that never leaves memory",
            subtitle="Anything not written to the file is gone the moment the process exits — that is why Week 11 exists.",
        )
    )

    items = [
        ("pink", "entry point"),
        ("cyan", "loop"),
        ("amber", "dispatch / storage"),
        ("purple", "tracker class"),
        ("green", "record class"),
        ("blue", "validation"),
    ]
    d.add(legend(d.center - legend_width(items) / 2, 866, items))
    return "week-12-final-app-architecture.svg", d.render()


# ---------------------------------------------------------------------------
# Bonus + roadmap
# ---------------------------------------------------------------------------


def course_roadmap() -> tuple[str, str]:
    d = Diagram(
        1360,
        760,
        eyebrow="Learn Programming Foundations With Python",
        title="The 12-Week Build Path",
        subtitle="One project, twelve weeks — every week the budget tracker gains exactly one new capability",
    )

    months = [
        (
            "01",
            "month 1 · foundations",
            "pink",
            [
                ("W1", "Getting Started", "print() · comments · running a script"),
                ("W2", "Variables & Types", "str int float bool · input() · f-strings"),
                ("W3", "Conditionals", "comparisons · and/or/not · truthiness"),
                ("W4", "match / case", "menu dispatch · wildcard fallback"),
            ],
        ),
        (
            "02",
            "month 2 · building blocks",
            "cyan",
            [
                ("W5", "Loops", "while · for · range() · break · continue"),
                ("W6", "Lists & Tuples", "indexing · slicing · mutability"),
                ("W7", "Dicts & Sets", "key lookup · .items() · uniqueness"),
                ("W8", "Functions", "def · parameters · return · scope"),
            ],
        ),
        (
            "03",
            "month 3 · oop & shipping",
            "purple",
            [
                ("W9", "Classes & Objects", "class · __init__ · self · methods"),
                ("W10", "Encapsulation", "__str__ · state · lists of objects"),
                ("W11", "File I/O", "with open · json · try/except"),
                ("W12", "Inheritance & Final", "super() · overriding · full assembly"),
            ],
        ),
    ]

    col_w = 404
    gap = 28
    xs = [46 + index * (col_w + gap) for index in range(3)]
    top = 152

    for index, (num, label, hue, weeks) in enumerate(months):
        x = xs[index]
        d.add(section(x, top, col_w, 420, num, label))
        c = color(hue)
        for j, (week, title, blurb) in enumerate(weeks):
            y = top + 34 + j * 94
            d.add(rect(x + 22, y, col_w - 44, 80, rx=10, fill=c["fill"], stroke=c["stroke"], width=1.6))
            d.add(circle(x + 52, y + 28, 15, fill="#0b1220", stroke=c["stroke"], width=1.5))
            d.add(text(x + 52, y + 33, week, size=11, fill=c["dim"], anchor="middle", mono=True, weight="700"))
            d.add(text(x + 78, y + 33, title, size=14, fill=TITLE, weight="700"))
            d.add(text(x + 40, y + 62, blurb, size=10.5, fill=c["dim"], mono=True))
        if index < 2:
            d.add(arrow(x + col_w + 4, top + 210, x + col_w + gap - 8, top + 210, width=2.4))

    d.add(
        card(
            46,
            614,
            1268,
            96,
            "green",
            title="Personal Budget Tracker",
            subtitle="add income and expenses · categorise them · summarise spending · save and reload — built by you, one week at a time",
            title_size=19,
        )
    )
    for index in range(3):
        d.add(arrow(xs[index] + col_w / 2, 578, xs[index] + col_w / 2, 608, stroke=color("green")["stroke"], marker="flowGreen", width=2.2))

    d.add(text(d.center, 730, "Reference implementations exist for weeks 8, 10, and 12 — open them only after you have tried the work yourself.", size=11.5, fill=SUBTITLE, anchor="middle"))
    return "course-roadmap.svg", d.render()


def bonus_what_next() -> tuple[str, str]:
    d = Diagram(
        1300,
        720,
        eyebrow="After Week 12 · Bonus Challenges",
        title="Where to Take It Next",
        subtitle="Six upgrades to the same app, ordered by how much new ground each one covers",
    )

    tiers = [
        (
            "01",
            "sharpen what you know",
            "green",
            [
                ("Search & filter", "loop + condition + string matching", "week 5 · week 3"),
                ("Monthly budgets", "dict of limits, compare against totals", "week 7"),
                ("Expense counter", "one small, well-named method", "week 10"),
            ],
        ),
        (
            "02",
            "one new idea each",
            "cyan",
            [
                ("Dates on transactions", "the datetime module", "new stdlib"),
                ("Export to CSV", "the csv module and DictWriter", "new stdlib"),
                ("Multiple accounts", "a second tracker, or inheritance", "week 12"),
            ],
        ),
        (
            "03",
            "beyond this course",
            "purple",
            [
                ("Charts", "matplotlib — your first pip install", "third party"),
                ("Automated tests", "pytest — prove it still works", "new discipline"),
                ("A second project", "quiz game · to-do list · calculator", "transfer the skills"),
            ],
        ),
    ]

    col_w = 388
    gap = 30
    xs = [48 + index * (col_w + gap) for index in range(3)]
    top = 154

    for index, (num, label, hue, rows) in enumerate(tiers):
        x = xs[index]
        c = color(hue)
        d.add(section(x, top, col_w, 350, num, label))
        for j, (title, blurb, tag) in enumerate(rows):
            y = top + 36 + j * 102
            d.add(rect(x + 22, y, col_w - 44, 88, rx=10, fill=c["fill"], stroke=c["stroke"], width=1.6))
            d.add(text(x + 42, y + 30, title, size=14.5, fill=TITLE, weight="700"))
            d.add(text(x + 42, y + 52, blurb, size=11, fill=c["text"]))
            d.add(text(x + col_w - 44, y + 74, tag, size=10, fill=c["dim"], anchor="end", mono=True))
        if index < 2:
            d.add(arrow(x + col_w + 2, top + 176, x + col_w + gap - 8, top + 176, width=2.3))

    d.add(
        note(
            48,
            548,
            620,
            "amber",
            "the habit that matters most",
            "Twenty minutes every day beats one long session a week. Break your own code on purpose and read the traceback before you fix it.",
        )
    )
    d.add(
        note(
            698,
            548,
            554,
            "blue",
            "explain it out loud",
            "If you can describe variables, loops, functions, and classes to someone else in your own words, you actually own the concept.",
        )
    )
    return "bonus-where-to-go-next.svg", d.render()


DIAGRAMS = [
    week09_blueprint_to_objects,
    week09_init_and_self,
    week10_encapsulation_boundary,
    week10_list_of_objects,
    week11_with_open,
    week11_save_load_roundtrip,
    week11_try_except,
    week12_inheritance,
    week12_final_architecture,
    course_roadmap,
    bonus_what_next,
]
