"""Month 1 diagrams: weeks 1-4 (running code, variables, conditionals, match)."""

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
    code_height,
    color,
    divider,
    elbow,
    legend,
    legend_width,
    line,
    note,
    note_height,
    path,
    rect,
    section,
    text,
)


# ---------------------------------------------------------------------------
# Week 1
# ---------------------------------------------------------------------------


def week01_how_python_runs() -> tuple[str, str]:
    d = Diagram(
        1240,
        690,
        eyebrow="Week 01 · Getting Started",
        title="How Python Runs Your Code",
        subtitle="One file, one statement at a time, always top to bottom — the interpreter never skips ahead",
    )

    top = 148
    height = 300
    width = 348
    xs = [58, 446, 834]

    d.add(section(xs[0], top, width, height, "01", "your file on disk"))
    d.add(
        code_block(
            xs[0] + 20,
            top + 34,
            width - 40,
            [
                [("# budget_tracker.py", CODE["com"])],
                [("print", CODE["fn"]), ("(", CODE["op"]), ('"Budget Tracker"', CODE["str"]), (")", CODE["op"])],
                [("print", CODE["fn"]), ("(", CODE["op"]), ('"=" ', CODE["str"]), ("* ", CODE["op"]), ("40", CODE["num"]), (")", CODE["op"])],
                [("# a note for humans", CODE["com"])],
                [("print", CODE["fn"]), ("(", CODE["op"]), ('"Ready."', CODE["str"]), (")", CODE["op"])],
            ],
            title="SOURCE · PLAIN TEXT",
            size=12.5,
            leading=22,
        )
    )
    d.add(
        text(
            xs[0] + width / 2,
            top + height - 46,
            "A script is just text. Nothing happens until you run it.",
            size=11,
            fill=SUBTITLE,
            anchor="middle",
        )
    )
    d.add(
        text(
            xs[0] + width / 2,
            top + height - 26,
            "python budget_tracker.py",
            size=11.5,
            fill=ACCENT_TAG,
            anchor="middle",
            mono=True,
        )
    )

    d.add(section(xs[1], top, width, height, "02", "the python 3.13 interpreter"))
    steps = [
        ("01", "Read the next line", "pink"),
        ("02", "Check the syntax", "amber"),
        ("03", "Execute the statement", "green"),
    ]
    step_y = top + 42
    for index, (badge, label, hue) in enumerate(steps):
        y = step_y + index * 66
        c = color(hue)
        d.add(rect(xs[1] + 26, y, width - 82, 50, rx=10, fill=c["fill"], stroke=c["stroke"], width=1.6))
        d.add(circle(xs[1] + 50, y + 25, 13, fill="#0b1220", stroke=c["stroke"], width=1.5))
        d.add(text(xs[1] + 50, y + 29, badge, size=10, fill=c["dim"], weight="700", anchor="middle", mono=True))
        d.add(text(xs[1] + 74, y + 30, label, size=13, fill=TITLE, weight="600"))
        if index < 2:
            d.add(arrow(xs[1] + 90, y + 50, xs[1] + 90, y + 64, width=2))

    loop_x = xs[1] + width - 38
    d.add(
        elbow(
            [
                (xs[1] + width - 56, step_y + 157),
                (loop_x, step_y + 157),
                (loop_x, step_y + 25),
                (xs[1] + width - 56, step_y + 25),
            ],
            stroke=FLOW_SOFT,
            width=1.6,
            marker="flowSoft",
            dash="5 5",
        )
    )
    for offset, chunk in enumerate(["repeat", "until", "EOF"]):
        d.add(
            text(
                loop_x + 16,
                step_y + 78 + offset * 13,
                chunk,
                size=9.5,
                fill=MUTED,
                mono=True,
                anchor="middle",
            )
        )
    d.add(
        text(
            xs[1] + width / 2,
            top + height - 30,
            "Comments are read, recognised, and skipped.",
            size=11,
            fill=SUBTITLE,
            anchor="middle",
        )
    )

    d.add(section(xs[2], top, width, height, "03", "your terminal"))
    d.add(
        code_block(
            xs[2] + 20,
            top + 34,
            width - 40,
            [
                [("$ python budget_tracker.py", CODE["dim"])],
                [("Budget Tracker", CODE["out"])],
                [("========================================", CODE["out"])],
                [("Ready.", CODE["out"])],
                [("$ _", CODE["dim"])],
            ],
            title="STDOUT",
            size=11,
            leading=22,
        )
    )
    d.add(
        text(
            xs[2] + width / 2,
            top + height - 46,
            "3 lines of output from 5 lines of file.",
            size=11,
            fill=SUBTITLE,
            anchor="middle",
        )
    )
    d.add(
        text(
            xs[2] + width / 2,
            top + height - 26,
            "the 2 comments produced nothing",
            size=11,
            fill=ACCENT_TAG,
            anchor="middle",
            mono=True,
        )
    )

    mid = top + height / 2
    d.add(arrow(xs[0] + width + 8, mid, xs[1] - 10, mid, label="you run it", label_dy=-14))
    d.add(arrow(xs[1] + width + 8, mid, xs[2] - 10, mid, label="it prints", label_dy=-14))

    notes_y = top + height + 46
    note_w = 348
    d.add(
        note(
            xs[0],
            notes_y,
            note_w,
            "amber",
            "syntax error",
            "If any line cannot be understood, Python reports the file and line number and stops before running anything.",
        )
    )
    d.add(
        note(
            xs[1],
            notes_y,
            note_w,
            "green",
            "print() is a tool",
            "print() is your first debugger. Use it to see what your program is actually doing, not just what you hoped.",
        )
    )
    d.add(
        note(
            xs[2],
            notes_y,
            note_w,
            "blue",
            "order matters",
            "Line 2 cannot use something created on line 4. Execution order is the whole game in Week 1.",
        )
    )

    items = [("pink", "read"), ("amber", "check"), ("green", "execute"), ("slate", "skipped / comment")]
    d.add(legend(d.center - legend_width(items) / 2, 622, items))
    return "week-01-how-python-runs-your-code.svg", d.render()


def week01_anatomy_of_a_statement() -> tuple[str, str]:
    d = Diagram(
        1180,
        640,
        eyebrow="Week 01 · Getting Started",
        title="Anatomy of Your First Statement",
        subtitle="Every part of print(\"Hello, World!\") has a name and a job",
    )

    base_y = 268
    x0 = 200
    char = 26
    tokens = [
        ("print", "blue", "function name\nthe action you want"),
        ("(", "slate", "opening paren\nstarts the arguments"),
        ('"Hello, World!"', "green", "string literal\nthe text to show"),
        (")", "slate", "closing paren\nends the call"),
    ]

    d.add(rect(96, base_y - 46, 988, 92, rx=12, fill="#080e1c", stroke="#1e2b45", width=1.2))
    d.add(text(112, base_y - 26, "ONE STATEMENT", size=10, fill=MUTED, mono=True, spacing=1.8, weight="700"))

    cursor = x0
    positions = []
    for value, hue, _ in tokens:
        c = color(hue)
        w = len(value) * char * 0.62 + 24
        d.add(rect(cursor, base_y - 22, w, 46, rx=8, fill=c["fill"], stroke=c["stroke"], width=1.6))
        d.add(text(cursor + w / 2, base_y + 10, value, size=25, fill=c["text"], anchor="middle", mono=True, weight="700"))
        positions.append((cursor + w / 2, w, hue))
        cursor += w + 6

    callouts = [
        (positions[0][0], 152, "function name", "the action you want to run", "blue", "up"),
        (positions[1][0], 364, "opening paren", "arguments start here", "slate", "down"),
        (positions[2][0], 152, "string literal", "text lives inside quotes", "green", "up"),
        (positions[3][0], 364, "closing paren", "the call is complete", "slate", "down"),
    ]
    for cx, cy, label, body, hue, direction in callouts:
        c = color(hue)
        w = 236
        bx = min(max(cx - w / 2, 100), 1080 - w)
        d.add(rect(bx, cy, w, 58, rx=9, fill=c["fill"], stroke=c["stroke"], width=1.4))
        d.add(text(bx + w / 2, cy + 24, label, size=12.5, fill=TITLE, weight="700", anchor="middle"))
        d.add(text(bx + w / 2, cy + 43, body, size=11, fill=c["text"], anchor="middle"))
        if direction == "up":
            d.add(line(cx, cy + 58, cx, base_y - 24, stroke=c["stroke"], width=1.3, dash="4 4"))
        else:
            d.add(line(cx, base_y + 26, cx, cy, stroke=c["stroke"], width=1.3, dash="4 4"))

    d.add(divider(96, 1084, 466, label="code vs. comment"))

    d.add(
        card(
            96,
            492,
            478,
            108,
            "green",
            title="This runs",
            subtitle="Python executes it and something happens",
            lines=['print("Budget Tracker")'],
            line_size=13,
            lines_top=566,
        )
    )
    d.add(
        card(
            606,
            492,
            478,
            108,
            "slate",
            title="This never runs",
            subtitle="Everything after # is ignored by Python",
            lines=["# print(\"Budget Tracker\")"],
            line_size=13,
            lines_top=566,
        )
    )
    return "week-01-anatomy-of-a-statement.svg", d.render()


# ---------------------------------------------------------------------------
# Week 2
# ---------------------------------------------------------------------------


def week02_how_variables_are_stored() -> tuple[str, str]:
    d = Diagram(
        1260,
        760,
        eyebrow="Week 02 · Variables & Data Types",
        title="How Python Actually Stores a Variable",
        subtitle="A variable is not a box holding a value — it is a name tag tied to an object in memory",
    )

    top = 156
    height = 396

    d.add(section(58, top, 320, height, "01", "the code you write"))
    d.add(
        code_block(
            80,
            top + 36,
            276,
            [
                [("balance", CODE["var"]), (" = ", CODE["op"]), ("1500.75", CODE["num"])],
                [("name", CODE["var"]), ("    = ", CODE["op"]), ('"Alex"', CODE["str"])],
                [("count", CODE["var"]), ("   = ", CODE["op"]), ("3", CODE["num"])],
                [("", CODE["op"])],
                [("# one line, two halves:", CODE["com"])],
                [("#   left  = the name", CODE["com"])],
                [("#   right = the object", CODE["com"])],
            ],
            title="ASSIGNMENT",
            size=12.5,
            leading=21,
        )
    )
    d.add(
        note(
            80,
            top + 232,
            276,
            "amber",
            "read it right to left",
            "Python builds the object on the right first, then attaches the name on the left to it.",
        )
    )

    d.add(section(432, top, 268, height, "02", "namespace · the names"))
    d.add(section(752, top, 450, height, "03", "object memory · the values"))

    rows = [
        ("balance", "float", "1500.75", "blue", "8 bytes of IEEE-754 double"),
        ("name", "str", '"Alex"', "green", "4 characters, immutable"),
        ("count", "int", "3", "purple", "arbitrary precision integer"),
    ]

    for index, (var, type_name, value, hue, detail) in enumerate(rows):
        c = color(hue)
        y = top + 60 + index * 104

        d.add(rect(456, y, 220, 58, rx=9, fill=c["fill"], stroke=c["stroke"], width=1.8))
        d.add(text(566, y + 24, var, size=15, fill=TITLE, weight="700", anchor="middle", mono=True))
        d.add(text(566, y + 43, "name in the namespace", size=10, fill=c["dim"], anchor="middle"))

        d.add(rect(786, y - 6, 384, 74, rx=10, fill=c["fill"], stroke=c["stroke"], width=1.8))
        d.add(rect(786, y - 6, 6, 74, rx=3, fill=c["stroke"]))
        d.add(text(806, y + 16, type_name, size=11, fill=c["dim"], mono=True, weight="700", spacing=1.2))
        d.add(text(806, y + 42, value, size=20, fill=TITLE, weight="700", mono=True))
        d.add(text(1154, y + 60, detail, size=10, fill=c["dim"], anchor="end"))

        d.add(arrow(686, y + 29, 778, y + 29, stroke=c["stroke"], marker=_marker(hue), width=2.2))
        d.add(text(732, y + 20, "points to", size=9.5, fill=c["dim"], anchor="middle", mono=True))

    footer_y = top + height + 34
    d.add(
        note(
            58,
            footer_y,
            560,
            "green",
            "what this buys you",
            "Two names can point at the same object, and a name can be re-pointed at a different object at any time. The name and the value are independent.",
        )
    )
    d.add(
        note(
            642,
            footer_y,
            560,
            "red",
            "the mental model to avoid",
            "Do not picture a labelled box that the value is poured into. Picture a luggage tag tied to a suitcase that already exists.",
        )
    )

    items = [("blue", "float"), ("green", "str"), ("purple", "int"), ("slate", "name binding")]
    d.add(legend(d.center - legend_width(items) / 2, 700, items))
    return "week-02-how-variables-are-stored.svg", d.render()


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


def week02_input_and_conversion() -> tuple[str, str]:
    d = Diagram(
        1240,
        700,
        eyebrow="Week 02 · Variables & Data Types",
        title="input() Always Hands You a String",
        subtitle="The user types 25 — Python receives \"25\" — you must convert before you can do maths",
    )

    top = 150
    d.add(section(58, top, 300, 250, "01", "what the user types"))
    d.add(
        card(
            84,
            top + 36,
            248,
            88,
            "cyan",
            title="25",
            subtitle="typed at the keyboard",
            title_size=30,
        )
    )
    d.add(
        code_block(
            84,
            top + 142,
            248,
            [
                [("age", CODE["var"]), (" = ", CODE["op"]), ("input", CODE["fn"]), ("(", CODE["op"]), ('"Age? "', CODE["str"]), (")", CODE["op"])],
            ],
            size=12,
            leading=18,
        )
    )
    d.add(text(208, top + 218, "keystrokes, not numbers", size=10.5, fill=MUTED, anchor="middle", mono=True))

    d.add(section(412, top, 300, 250, "02", "what python returns"))
    d.add(
        card(
            438,
            top + 36,
            248,
            88,
            "amber",
            title='"25"',
            subtitle="type: str — every single time",
            title_size=30,
        )
    )
    d.add(
        code_block(
            438,
            top + 142,
            248,
            [
                [("type", CODE["fn"]), ("(", CODE["op"]), ("age", CODE["var"]), (")", CODE["op"])],
                [("<class 'str'>", CODE["out"])],
            ],
            size=12,
            leading=18,
        )
    )
    d.add(text(562, top + 218, 'even when it looks numeric', size=10.5, fill=MUTED, anchor="middle", mono=True))

    d.add(section(766, top, 436, 250, "03", "convert, then calculate"))
    conv = [
        ("int(age)", "25", "whole numbers", "purple"),
        ("float(age)", "25.0", "decimals / money", "blue"),
        ("str(25)", '"25"', "back to text", "green"),
    ]
    for index, (call, result, why, hue) in enumerate(conv):
        c = color(hue)
        y = top + 36 + index * 68
        d.add(rect(792, y, 384, 54, rx=9, fill=c["fill"], stroke=c["stroke"], width=1.6))
        d.add(text(812, y + 24, call, size=14, fill=TITLE, weight="700", mono=True))
        d.add(text(812, y + 42, why, size=10.5, fill=c["dim"]))
        d.add(text(1156, y + 33, result, size=16, fill=c["text"], anchor="end", mono=True, weight="700"))

    mid = top + 80
    d.add(arrow(366, mid, 404, mid))
    d.add(arrow(720, mid, 758, mid))

    d.add(divider(58, 1202, 452, label="the two failure modes beginners hit"))

    d.add(
        card(
            58,
            478,
            560,
            132,
            "red",
            title="Forgetting to convert",
            subtitle="String concatenation instead of addition",
            lines=[
                'age = input("Age? ")   # "25"',
                "print(age + 1)",
                "TypeError: can only concatenate str",
            ],
            line_size=12,
            lines_top=548,
            lines_anchor="start",
        )
    )
    d.add(
        card(
            642,
            478,
            560,
            132,
            "amber",
            title="Converting text that is not a number",
            subtitle="int() raises instead of guessing",
            lines=[
                'int("twenty five")',
                "ValueError: invalid literal for int()",
                "-> wrap it in try / except (Week 11)",
            ],
            line_size=12,
            lines_top=548,
            lines_anchor="start",
        )
    )

    items = [("cyan", "raw keystrokes"), ("amber", "str"), ("purple", "int"), ("blue", "float"), ("green", "str()")]
    d.add(legend(d.center - legend_width(items) / 2, 634, items))
    return "week-02-input-and-type-conversion.svg", d.render()


def week02_reassignment() -> tuple[str, str]:
    d = Diagram(
        1240,
        640,
        eyebrow="Week 02 · Variables & Data Types",
        title="What Reassignment Really Does",
        subtitle="score = score + 5 does not edit the number 10 — it builds a new object and re-points the name",
    )

    top = 158
    height = 300
    width = 360
    xs = [58, 442, 826]
    labels = [
        ("01", "before", "score = 10"),
        ("02", "evaluate the right side", "score + 5  ->  15"),
        ("03", "rebind the name", "score = 15"),
    ]

    for index, (num, label, code) in enumerate(labels):
        d.add(section(xs[index], top, width, height, num, label))
        d.add(
            text(
                xs[index] + width / 2,
                top + 34,
                code,
                size=13,
                fill=ACCENT_TAG,
                anchor="middle",
                mono=True,
                weight="700",
            )
        )

    def name_tag(x: float, y: float, hue: str, faded: bool = False) -> None:
        c = color(hue)
        d.add(rect(x, y, 132, 48, rx=9, fill=c["fill"], stroke=c["stroke"], width=1.7, opacity=0.35 if faded else 1))
        d.add(
            text(
                x + 66,
                y + 30,
                "score",
                size=16,
                fill=TITLE if not faded else c["dim"],
                anchor="middle",
                mono=True,
                weight="700",
                opacity=0.45 if faded else None,
            )
        )

    def value_box(x: float, y: float, value: str, hue: str, note_text: str, faded: bool = False) -> None:
        c = color(hue)
        d.add(rect(x, y, 150, 60, rx=10, fill=c["fill"], stroke=c["stroke"], width=1.8, opacity=0.3 if faded else 1))
        d.add(
            text(
                x + 75,
                y + 30,
                value,
                size=24,
                fill=TITLE if not faded else c["dim"],
                anchor="middle",
                mono=True,
                weight="700",
                opacity=0.45 if faded else None,
            )
        )
        d.add(text(x + 75, y + 50, "int object", size=9.5, fill=c["dim"], anchor="middle", mono=True))
        d.add(text(x + 75, y + 80, note_text, size=10.5, fill=c["dim"], anchor="middle"))

    # Step 1
    name_tag(xs[0] + 30, top + 100, "blue")
    value_box(xs[0] + 186, top + 94, "10", "blue", "lives in memory")
    d.add(arrow(xs[0] + 162, top + 124, xs[0] + 180, top + 124, stroke=color("blue")["stroke"], marker="flowBlue", width=2.2))

    # Step 2
    name_tag(xs[1] + 30, top + 100, "blue")
    value_box(xs[1] + 186, top + 94, "10", "blue", "unchanged")
    d.add(arrow(xs[1] + 162, top + 124, xs[1] + 180, top + 124, stroke=color("blue")["stroke"], marker="flowBlue", width=2.2))
    d.add(rect(xs[1] + 60, top + 208, 246, 62, rx=10, fill=color("amber")["fill"], stroke=color("amber")["stroke"], width=1.7))
    d.add(text(xs[1] + 183, top + 232, "15", size=22, fill=TITLE, anchor="middle", mono=True, weight="700"))
    d.add(text(xs[1] + 183, top + 254, "brand new int object", size=10, fill=color("amber")["dim"], anchor="middle", mono=True))
    d.add(
        arrow(
            xs[1] + 330,
            top + 158,
            xs[1] + 290,
            top + 202,
            stroke=color("amber")["stroke"],
            marker="flowAmber",
            width=2,
        )
    )

    # Step 3
    name_tag(xs[2] + 30, top + 100, "green")
    value_box(xs[2] + 186, top + 94, "10", "slate", "no name points here", faded=True)
    d.add(
        line(
            xs[2] + 162,
            top + 124,
            xs[2] + 180,
            top + 124,
            stroke="#334155",
            width=2,
            dash="4 4",
        )
    )
    d.add(text(xs[2] + 261, top + 200, "unreachable -> garbage collected", size=9.5, fill=MUTED, anchor="middle", mono=True))
    d.add(rect(xs[2] + 186, top + 214, 150, 60, rx=10, fill=color("green")["fill"], stroke=color("green")["stroke"], width=1.8))
    d.add(text(xs[2] + 261, top + 244, "15", size=24, fill=TITLE, anchor="middle", mono=True, weight="700"))
    d.add(text(xs[2] + 261, top + 264, "int object", size=9.5, fill=color("green")["dim"], anchor="middle", mono=True))
    d.add(
        elbow(
            [(xs[2] + 96, top + 148), (xs[2] + 96, top + 244), (xs[2] + 180, top + 244)],
            stroke=color("green")["stroke"],
            marker="flowGreen",
            width=2.2,
        )
    )

    d.add(arrow(xs[0] + width + 6, top + height / 2, xs[1] - 8, top + height / 2))
    d.add(arrow(xs[1] + width + 6, top + height / 2, xs[2] - 8, top + height / 2))

    d.add(
        note(
            58,
            top + height + 40,
            560,
            "purple",
            "why this matters later",
            "In Week 8 you will pass a variable into a function. Rebinding inside the function does exactly this — and it never touches the caller's name.",
        )
    )
    d.add(
        note(
            642,
            top + height + 40,
            560,
            "cyan",
            "counter idiom",
            "score += 5 is shorthand for the same three steps. For lists, += mutates in place instead, which is why Week 6 makes a point of mutability.",
        )
    )
    return "week-02-reassignment-and-memory.svg", d.render()


# ---------------------------------------------------------------------------
# Week 3
# ---------------------------------------------------------------------------


def week03_decision_flow() -> tuple[str, str]:
    d = Diagram(
        1220,
        780,
        eyebrow="Week 03 · Conditionals",
        title="One Chain, Exactly One Branch",
        subtitle="if / elif / else is tested top to bottom and stops at the first True — traced with temperature = 72",
    )

    d.add(
        code_block(
            58,
            146,
            402,
            [
                [("temperature", CODE["var"]), (" = ", CODE["op"]), ("72", CODE["num"])],
                [("", CODE["op"])],
                [("if", CODE["kw"]), (" temperature ", CODE["var"]), ("> ", CODE["op"]), ("85", CODE["num"]), (":", CODE["op"])],
                [("    print", CODE["fn"]), ("(", CODE["op"]), ('"It\'s hot outside!"', CODE["str"]), (")", CODE["op"])],
                [("elif", CODE["kw"]), (" temperature ", CODE["var"]), ("> ", CODE["op"]), ("65", CODE["num"]), (":", CODE["op"])],
                [("    print", CODE["fn"]), ("(", CODE["op"]), ('"Nice weather today!"', CODE["str"]), (")", CODE["op"])],
                [("else", CODE["kw"]), (":", CODE["op"])],
                [("    print", CODE["fn"]), ("(", CODE["op"]), ('"Grab a jacket."', CODE["str"]), (")", CODE["op"])],
            ],
            title="THE CODE",
            size=12.5,
            leading=22,
        )
    )

    d.add(
        note(
            58,
            412,
            402,
            "amber",
            "the colon and the indent",
            "The colon opens the block. The four-space indent is what actually belongs to the branch — Python uses whitespace, not braces.",
        )
    )
    d.add(
        note(
            58,
            412 + note_height("The colon opens the block. The four-space indent is what actually belongs to the branch — Python uses whitespace, not braces.", 402) + 16,
            402,
            "red",
            "= vs ==",
            "= assigns a value. == asks a question. if temperature = 85 is a SyntaxError, not a comparison.",
        )
    )

    x = 520
    w = 640
    rows = [
        ("01", "if", "temperature > 85", "72 > 85", "False", "red", "skipped", 'print("It\'s hot outside!")'),
        ("02", "elif", "temperature > 65", "72 > 65", "True", "green", "runs", 'print("Nice weather today!")'),
        ("03", "else", "everything else", "never reached", "—", "slate", "skipped", 'print("Grab a jacket.")'),
    ]

    d.add(section(x, 146, w, 396, "01", "evaluation order"))
    for index, (num, kw, condition, evaluated, result, hue, verdict, body) in enumerate(rows):
        c = color(hue)
        y = 182 + index * 122
        d.add(rect(x + 24, y, w - 48, 100, rx=11, fill=c["fill"], stroke=c["stroke"], width=1.7))
        d.add(circle(x + 50, y + 26, 12, fill="#0b1220", stroke=c["stroke"], width=1.5))
        d.add(text(x + 50, y + 30, num, size=10, fill=c["dim"], weight="700", anchor="middle", mono=True))
        d.add(text(x + 74, y + 31, kw, size=15, fill=TITLE, weight="700", mono=True))
        d.add(text(x + 128, y + 31, condition, size=13, fill=c["text"], mono=True))
        d.add(text(x + w - 72, y + 31, result, size=14, fill=c["text"], anchor="end", mono=True, weight="700"))
        d.add(text(x + w - 72, y + 50, evaluated, size=10, fill=c["dim"], anchor="end", mono=True))
        d.add(line(x + 40, y + 62, x + w - 64, y + 62, stroke=c["stroke"], width=1, opacity=0.3))
        d.add(text(x + 74, y + 84, body, size=12, fill=c["dim"] if hue != "green" else TITLE, mono=True))
        badge_hue = "green" if verdict == "runs" else "slate"
        bc = color(badge_hue)
        d.add(rect(x + w - 128, y + 70, 64, 22, rx=11, fill=bc["fill"], stroke=bc["stroke"], width=1.2))
        d.add(text(x + w - 96, y + 85, verdict, size=10, fill=bc["dim"], anchor="middle", mono=True, weight="700"))
        if index < 2:
            d.add(
                text(
                    x + 50,
                    y + 116,
                    "|",
                    size=12,
                    fill=MUTED,
                    anchor="middle",
                    mono=True,
                )
            )

    d.add(
        elbow(
            [(x + w - 34, 304), (x + w + 14, 304), (x + w + 14, 596), (x + 300, 596)],
            stroke=color("green")["stroke"],
            marker="flowGreen",
            width=2.4,
        )
    )
    d.add(
        card(
            x - 44,
            566,
            340,
            60,
            "green",
            title="Nice weather today!",
            title_size=15,
            subtitle="the only line that printed",
        )
    )
    d.add(
        text(
            x + 320,
            640,
            "Once a branch runs, the rest of the chain is never even evaluated.",
            size=11.5,
            fill=SUBTITLE,
            anchor="middle",
        )
    )

    items = [("green", "condition True · branch runs"), ("red", "condition False"), ("slate", "never evaluated")]
    d.add(legend(d.center - legend_width(items) / 2, 700, items))
    return "week-03-if-elif-else-flow.svg", d.render()


def week03_truthy_falsy() -> tuple[str, str]:
    d = Diagram(
        1220,
        700,
        eyebrow="Week 03 · Conditionals",
        title="Truthy, Falsy, and the Logical Operators",
        subtitle="Python asks 'is this value truthy?' — not just 'is this value True?'",
    )

    d.add(section(58, 150, 560, 262, "01", "falsy · behaves like False"))
    falsy = ["0", "0.0", '""', "[]", "{}", "set()", "None", "False"]
    for index, value in enumerate(falsy):
        c = color("red")
        col = index % 4
        row = index // 4
        bx = 84 + col * 130
        by = 190 + row * 74
        d.add(rect(bx, by, 112, 56, rx=9, fill=c["fill"], stroke=c["stroke"], width=1.5))
        d.add(text(bx + 56, by + 35, value, size=17, fill=c["text"], anchor="middle", mono=True, weight="700"))
    d.add(
        text(
            338,
            364,
            "empty, zero, or nothing  ->  the if block is skipped",
            size=11,
            fill=SUBTITLE,
            anchor="middle",
        )
    )

    d.add(section(662, 150, 500, 262, "02", "truthy · behaves like True"))
    truthy = ['"Alex"', "1", "-7", "3.14", '[0]', '{"a": 1}']
    for index, value in enumerate(truthy):
        c = color("green")
        col = index % 3
        row = index // 3
        bx = 688 + col * 152
        by = 190 + row * 74
        d.add(rect(bx, by, 134, 56, rx=9, fill=c["fill"], stroke=c["stroke"], width=1.5))
        d.add(text(bx + 67, by + 35, value, size=16, fill=c["text"], anchor="middle", mono=True, weight="700"))
    d.add(
        text(
            912,
            364,
            "anything with content  ->  the if block runs",
            size=11,
            fill=SUBTITLE,
            anchor="middle",
        )
    )

    d.add(divider(58, 1162, 448, label="combining conditions"))

    ops = [
        ("and", "blue", "BOTH sides must be true", ["True  and True   -> True", "True  and False  -> False", "False and True   -> False"]),
        ("or", "purple", "AT LEAST ONE side must be true", ["True  or False  -> True", "False or True   -> True", "False or False  -> False"]),
        ("not", "amber", "flips the answer", ["not True   -> False", "not False  -> True", "not \"\"     -> True"]),
    ]
    for index, (op, hue, blurb, table) in enumerate(ops):
        bx = 58 + index * 370
        d.add(
            card(
                bx,
                476,
                346,
                160,
                hue,
                title=op,
                subtitle=blurb,
                lines=table,
                line_size=12,
                lines_top=576,
                lines_anchor="start",
            )
        )

    d.add(
        text(
            d.center,
            668,
            'if name:  is the idiomatic way to ask "did the user actually type something?"',
            size=11.5,
            fill=ACCENT_TAG,
            anchor="middle",
            mono=True,
        )
    )
    return "week-03-truthy-falsy-and-operators.svg", d.render()


# ---------------------------------------------------------------------------
# Week 4
# ---------------------------------------------------------------------------


def week04_match_dispatch() -> tuple[str, str]:
    d = Diagram(
        1220,
        740,
        eyebrow="Week 04 · Pattern Matching",
        title="How match / case Dispatches One Value",
        subtitle="The subject is evaluated once, then compared against each case top to bottom — first match wins",
    )

    d.add(
        card(
            d.center - 190,
            140,
            380,
            88,
            "cyan",
            title='choice = "2"',
            subtitle="the subject — evaluated exactly once",
            title_size=20,
        )
    )
    d.add(arrow(d.center, 232, d.center, 268, width=2.4))
    d.add(text(d.center + 12, 256, "match choice:", size=11, fill=ACCENT_TAG, mono=True))

    x = 190
    w = 840
    cases = [
        ('case "1":', "Add income", "no match", "slate", False),
        ('case "2":', "Add expense", "MATCH", "green", True),
        ('case "3":', "View balance", "never tested", "slate", False),
        ("case _:", "Invalid choice", "never tested", "slate", False),
    ]
    for index, (label, body, verdict, hue, hit) in enumerate(cases):
        c = color(hue)
        y = 286 + index * 84
        d.add(rect(x, y, w, 66, rx=10, fill=c["fill"], stroke=c["stroke"], width=2 if hit else 1.4, opacity=1 if hit else 0.75))
        d.add(text(x + 22, y + 40, label, size=15, fill=TITLE if hit else c["dim"], mono=True, weight="700"))
        d.add(text(x + 172, y + 40, body, size=13, fill=c["text"] if hit else c["dim"]))
        d.add(text(x + w - 22, y + 40, verdict, size=11.5, fill=c["dim"], anchor="end", mono=True, weight="700"))
        if index < len(cases) - 1 and index < 1:
            d.add(arrow(x + 40, y + 66, x + 40, y + 82, width=2))
        elif index < len(cases) - 1:
            d.add(line(x + 40, y + 66, x + 40, y + 82, stroke="#334155", width=1.6, dash="4 4"))

    d.add(
        elbow(
            [(x + w + 8, 352), (x + w + 46, 352), (x + w + 46, 646), (x + 620, 646)],
            stroke=color("green")["stroke"],
            marker="flowGreen",
            width=2.4,
        )
    )
    d.add(
        card(
            x + 60,
            618,
            556,
            58,
            "green",
            title="Add expense  ->  amount prompt runs",
            title_size=14,
        )
    )

    d.add(
        note(
            58,
            286,
            116,
            "slate",
            "order",
            "Cases run top to bottom.",
            size=10.5,
        )
    )
    d.add(
        note(
            1046,
            286,
            116,
            "amber",
            "fallback",
            "case _ catches anything unmatched.",
            size=10.5,
        )
    )
    d.add(
        text(
            d.center,
            700,
            "Forget case _ and a typo silently does nothing — the program just falls through the whole block.",
            size=11.5,
            fill=SUBTITLE,
            anchor="middle",
        )
    )
    return "week-04-match-case-dispatch.svg", d.render()


def week04_match_vs_if() -> tuple[str, str]:
    d = Diagram(
        1200,
        640,
        eyebrow="Week 04 · Pattern Matching",
        title="Choosing Between match and if / elif",
        subtitle="Same value, many fixed options → match. Ranges and combined logic → if",
    )

    d.add(
        card(
            58,
            150,
            540,
            230,
            "green",
            title="Reach for match",
            subtitle="one subject compared against fixed, known values",
            lines=[
                "menu choices        \"1\" \"2\" \"3\" \"4\"",
                "command words       start / stop / status",
                "day names           \"saturday\" | \"sunday\"",
                "status codes        200 / 404 / 500",
            ],
            line_size=12,
            lines_top=268,
            lines_anchor="start",
            footer="the subject is evaluated once",
        )
    )
    d.add(
        card(
            622,
            150,
            540,
            230,
            "blue",
            title="Reach for if / elif",
            subtitle="each branch asks a different question",
            lines=[
                "ranges              score >= 90",
                "combined logic      age >= 18 and has_id",
                "membership          if name in blocked",
                "truthiness          if not transactions",
            ],
            line_size=12,
            lines_top=268,
            lines_anchor="start",
            footer="every branch re-evaluates something",
        )
    )

    d.add(divider(58, 1162, 416, label="the same menu, both ways"))

    d.add(
        code_block(
            58,
            444,
            540,
            [
                [("match", CODE["kw"]), (" choice:", CODE["var"])],
                [("    case", CODE["kw"]), (' "1"', CODE["str"]), (":", CODE["op"]), ("  add_income()", CODE["dim"])],
                [("    case", CODE["kw"]), (' "2"', CODE["str"]), (":", CODE["op"]), ("  add_expense()", CODE["dim"])],
                [("    case", CODE["kw"]), (" _", CODE["op"]), (":", CODE["op"]), ("    print(\"Invalid\")", CODE["dim"])],
            ],
            title="FLAT AND SCANNABLE",
            size=12.5,
            leading=21,
            stroke="#1f4030",
        )
    )
    d.add(
        code_block(
            622,
            444,
            540,
            [
                [("if", CODE["kw"]), (" choice == ", CODE["var"]), ('"1"', CODE["str"]), (":", CODE["op"])],
                [("    add_income()", CODE["dim"])],
                [("elif", CODE["kw"]), (" choice == ", CODE["var"]), ('"2"', CODE["str"]), (":", CODE["op"])],
                [("    add_expense()", CODE["dim"]), ("   # repeats 'choice ==' each time", CODE["com"])],
            ],
            title="WORKS, BUT REPETITIVE",
            size=12.5,
            leading=21,
            stroke="#1e3555",
        )
    )

    d.add(
        text(
            d.center,
            602,
            "match needs Python 3.10 or newer — this course targets 3.13, so you are safe.",
            size=11.5,
            fill=ACCENT_TAG,
            anchor="middle",
            mono=True,
        )
    )
    return "week-04-match-vs-if.svg", d.render()


DIAGRAMS = [
    week01_how_python_runs,
    week01_anatomy_of_a_statement,
    week02_how_variables_are_stored,
    week02_input_and_conversion,
    week02_reassignment,
    week03_decision_flow,
    week03_truthy_falsy,
    week04_match_dispatch,
    week04_match_vs_if,
]
