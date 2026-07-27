"""Month 2 diagrams: weeks 5-8 (loops, lists/tuples, dicts/sets, functions)."""

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
    wrap,
)


# ---------------------------------------------------------------------------
# Week 5 — loops
# ---------------------------------------------------------------------------


def week05_for_loop_anatomy() -> tuple[str, str]:
    d = Diagram(
        1300,
        900,
        eyebrow="Week 05 · Loops",
        title="Anatomy of a for Loop",
        subtitle="Five parts on the header line, one indented body — then the same body runs once per item",
    )

    # ---- Part 1: the header line, dissected --------------------------------
    header_y = 232
    d.add(section(58, 142, 1184, 214, "01", "the structure of the loop"))
    d.add(rect(96, header_y - 40, 1108, 76, rx=11, fill="#080e1c", stroke="#1e2b45", width=1.2))

    tokens = [
        ("for", "pink", "keyword\nstarts the loop"),
        ("number", "amber", "loop variable\nrebound every pass"),
        ("in", "pink", "keyword\nreads 'take each of'"),
        ("range(1, 4)", "cyan", "the iterable\nhands out 1, 2, 3"),
        (":", "purple", "colon\nopens the block"),
    ]
    cursor = 156
    spots: list[tuple[float, float]] = []
    for value, hue, _ in tokens:
        c = color(hue)
        w = len(value) * 15 + 28
        d.add(rect(cursor, header_y - 24, w, 44, rx=8, fill=c["fill"], stroke=c["stroke"], width=1.7))
        d.add(text(cursor + w / 2, header_y + 7, value, size=22, fill=c["text"], anchor="middle", mono=True, weight="700"))
        spots.append((cursor + w / 2, w))
        cursor += w + 14

    callouts = [
        ("for", "keyword that starts the loop", "pink", 0),
        ("number", "rebound on every pass", "amber", 1),
        ("in", "reads as 'take each item of'", "pink", 0),
        ("range(1, 4)", "the iterable, yields 1 2 3", "cyan", 1),
        (":", "colon opens the indented block", "purple", 0),
    ]
    for index, (label, body, hue, row) in enumerate(callouts):
        c = color(hue)
        cx = spots[index][0]
        label_y = 284 + row * 46
        d.add(line(cx, header_y + 22, cx, label_y - 16, stroke=c["stroke"], width=1.2, dash="3 4"))
        d.add(text(cx, label_y, label, size=12.5, fill=TITLE, weight="700", anchor="middle", mono=True))
        for j, chunk in enumerate(wrap(body, 176, 10.5)):
            d.add(text(cx, label_y + 17 + j * 13, chunk, size=10.5, fill=c["dim"], anchor="middle"))

    # ---- Part 2: the body --------------------------------------------------
    d.add(section(58, 400, 560, 190, "02", "the body · indentation is the block"))
    d.add(
        code_block(
            84,
            436,
            508,
            [
                [("for", CODE["kw"]), (" number ", CODE["var"]), ("in", CODE["kw"]), (" range", CODE["fn"]), ("(", CODE["op"]), ("1", CODE["num"]), (", ", CODE["op"]), ("4", CODE["num"]), ("):", CODE["op"])],
                [("    print", CODE["fn"]), ("(number)", CODE["op"]), ("      # in the loop", CODE["com"])],
                [("    total ", CODE["var"]), ("+= number", CODE["op"]), ("     # in the loop", CODE["com"])],
                [("print", CODE["fn"]), ("(", CODE["op"]), ('"done"', CODE["str"]), (")", CODE["op"]), ("          # after the loop", CODE["com"])],
            ],
            size=12,
            leading=22,
            pad=16,
        )
    )
    d.add(rect(92, 456, 5, 46, rx=2.5, fill=color("green")["stroke"]))
    d.add(text(112, 566, "4 spaces = 'this line belongs to the loop'", size=11, fill=color("green")["dim"], mono=True))

    d.add(
        note(
            646,
            400,
            596,
            "amber",
            "range(1, 4) stops before 4",
            "range is start-inclusive and stop-exclusive. range(1, 4) gives 1, 2, 3 — and range(5) gives 0, 1, 2, 3, 4.",
        )
    )
    d.add(
        note(
            646,
            500,
            596,
            "cyan",
            "you rarely need range at all",
            "for letter in \"Python\", for score in scores, for key, value in prices.items() — a for loop walks any sequence directly.",
        )
    )

    # ---- Part 3: the iteration trace ---------------------------------------
    d.add(section(58, 640, 1184, 176, "03", "one pass per item · the loop variable is reassigned each time"))

    passes = [
        ("PASS 1", "number = 1", "prints 1", "total -> 1", "green"),
        ("PASS 2", "number = 2", "prints 2", "total -> 3", "green"),
        ("PASS 3", "number = 3", "prints 3", "total -> 6", "green"),
        ("EXHAUSTED", "no items left", "body skipped", "loop ends", "slate"),
    ]
    box_w = 258
    gap = 34
    start_x = 92
    for index, (label, binding, action, effect, hue) in enumerate(passes):
        c = color(hue)
        bx = start_x + index * (box_w + gap)
        d.add(rect(bx, 676, box_w, 104, rx=11, fill=c["fill"], stroke=c["stroke"], width=1.8))
        d.add(text(bx + 16, 698, label, size=10, fill=c["dim"], mono=True, weight="700", spacing=1.6))
        d.add(text(bx + box_w / 2, 726, binding, size=15, fill=TITLE, anchor="middle", mono=True, weight="700"))
        d.add(text(bx + box_w / 2, 748, action, size=11, fill=c["text"], anchor="middle", mono=True))
        d.add(text(bx + box_w / 2, 768, effect, size=11, fill=c["dim"], anchor="middle", mono=True))
        if index < 3:
            d.add(arrow(bx + box_w + 4, 728, bx + box_w + gap - 8, 728, width=2.2))

    d.add(
        elbow(
            [(start_x + box_w / 2, 780), (start_x + box_w / 2, 800), (start_x + 2 * box_w + 2 * gap + box_w / 2, 800)],
            stroke=FLOW_SOFT,
            width=1.5,
            marker=None,
            dash="5 5",
        )
    )
    d.add(text(670, 816, "same body, new value for number", size=10.5, fill=MUTED, anchor="middle", mono=True))

    items = [("pink", "keyword"), ("amber", "loop variable"), ("cyan", "iterable"), ("purple", "block opener"), ("green", "body runs")]
    d.add(legend(d.center - legend_width(items) / 2, 840, items))
    return "week-05-for-loop-anatomy.svg", d.render()


def week05_while_loop_cycle() -> tuple[str, str]:
    d = Diagram(
        1220,
        720,
        eyebrow="Week 05 · Loops",
        title="The while Loop Cycle",
        subtitle="Check the condition, run the body, change something — or you will never get out",
    )

    cx = 400
    cy = 400
    d.add(section(58, 142, 700, 434, "01", "the three-beat cycle"))

    d.add(
        card(
            cx - 150,
            196,
            300,
            72,
            "cyan",
            title="count = 1",
            subtitle="set up before the loop",
            title_size=17,
        )
    )
    d.add(arrow(cx, 272, cx, 300, width=2.2))

    d.add(
        path(
            f"M{cx},304 L{cx + 130},364 L{cx},424 L{cx - 130},364 Z",
            fill=color("amber")["fill"],
            stroke=color("amber")["stroke"],
            width=2,
        )
    )
    d.add(text(cx, 358, "count <= 3", size=15, fill=TITLE, anchor="middle", mono=True, weight="700"))
    d.add(text(cx, 378, "still true?", size=11, fill=color("amber")["dim"], anchor="middle"))

    d.add(
        card(
            cx - 150,
            464,
            300,
            84,
            "green",
            title="run the body",
            subtitle="print(count)  ·  count += 1",
            title_size=15,
        )
    )
    d.add(arrow(cx, 428, cx, 460, width=2.2, stroke=color("green")["stroke"], marker="flowGreen"))
    d.add(text(cx + 14, 448, "True", size=11, fill=color("green")["dim"], mono=True, weight="700"))

    d.add(
        elbow(
            [(cx - 150, 506), (200, 506), (200, 364), (cx - 134, 364)],
            stroke=color("green")["stroke"],
            marker="flowGreen",
            width=2.2,
        )
    )
    d.add(text(200, 344, "back to the check", size=10.5, fill=color("green")["dim"], anchor="middle", mono=True))

    d.add(arrow(cx + 134, 364, 618, 364, stroke=color("slate")["stroke"], marker="flowSoft", width=2.2))
    d.add(text(560, 352, "False", size=11, fill=color("slate")["dim"], anchor="middle", mono=True, weight="700"))
    d.add(
        card(
            622,
            330,
            116,
            68,
            "slate",
            title="exit",
            subtitle="continue after the loop",
            title_size=15,
        )
    )

    # right column
    d.add(section(796, 142, 366, 210, "02", "it terminates"))
    d.add(
        code_block(
            820,
            178,
            318,
            [
                [("count ", CODE["var"]), ("= ", CODE["op"]), ("1", CODE["num"])],
                [("while", CODE["kw"]), (" count ", CODE["var"]), ("<= ", CODE["op"]), ("3", CODE["num"]), (":", CODE["op"])],
                [("    print", CODE["fn"]), ("(count)", CODE["op"])],
                [("    count ", CODE["var"]), ("+= ", CODE["op"]), ("1", CODE["num"]), ("   # the exit ticket", CODE["com"])],
            ],
            size=11.5,
            leading=20,
            stroke="#1f4030",
        )
    )
    d.add(text(979, 330, "1  2  3  then stops", size=12, fill=color("green")["dim"], anchor="middle", mono=True))

    d.add(section(796, 396, 366, 180, "03", "it never terminates"))
    d.add(
        code_block(
            820,
            432,
            318,
            [
                [("count ", CODE["var"]), ("= ", CODE["op"]), ("1", CODE["num"])],
                [("while", CODE["kw"]), (" count ", CODE["var"]), ("<= ", CODE["op"]), ("3", CODE["num"]), (":", CODE["op"])],
                [("    print", CODE["fn"]), ("(count)", CODE["op"]), ("   # count never changes", CODE["com"])],
            ],
            size=11.5,
            leading=20,
            stroke="#5b1b1b",
        )
    )
    d.add(text(979, 552, "1 1 1 1 1 ...  press Ctrl+C", size=12, fill=color("red")["dim"], anchor="middle", mono=True))

    d.add(
        note(
            58,
            608,
            546,
            "purple",
            "while True is fine — with a break",
            "A menu loop uses while True: on purpose. The exit condition moves from the header into a break inside the body.",
        )
    )
    d.add(
        note(
            632,
            608,
            530,
            "amber",
            "for or while?",
            "Known number of items -> for. Unknown, driven by user input or a condition -> while.",
        )
    )
    return "week-05-while-loop-cycle.svg", d.render()


def week05_break_vs_continue() -> tuple[str, str]:
    d = Diagram(
        1220,
        760,
        eyebrow="Week 05 · Loops",
        title="break Leaves · continue Skips",
        subtitle="Same loop over 1..5, one keyword different, completely different output",
    )

    def sequence(x: float, hue_of, stop_at: int, mode: str) -> None:
        for index in range(5):
            value = index + 1
            hue = hue_of(value)
            c = color(hue)
            bx = x + index * 106
            faded = mode == "break" and value > stop_at
            d.add(rect(bx, 316, 88, 74, rx=10, fill=c["fill"], stroke=c["stroke"], width=1.7, opacity=0.28 if faded else 1))
            d.add(
                text(
                    bx + 44,
                    350,
                    str(value),
                    size=22,
                    fill=TITLE,
                    anchor="middle",
                    mono=True,
                    weight="700",
                    opacity=0.4 if faded else None,
                )
            )
            label = {"green": "printed", "amber": "skipped", "red": "stop", "slate": "not run"}[hue]
            d.add(text(bx + 44, 376, label, size=10, fill=c["dim"], anchor="middle", mono=True))
            if index < 4:
                d.add(
                    line(
                        bx + 90,
                        353,
                        bx + 102,
                        353,
                        stroke="#334155" if faded else FLOW_SOFT,
                        width=1.6,
                        dash="3 3" if faded else None,
                    )
                )

    d.add(section(58, 148, 1104, 118, "01", "the two loops"))
    d.add(
        code_block(
            84,
            176,
            520,
            [
                [("for", CODE["kw"]), (" n ", CODE["var"]), ("in", CODE["kw"]), (" range", CODE["fn"]), ("(", CODE["op"]), ("1", CODE["num"]), (", ", CODE["op"]), ("6", CODE["num"]), ("):", CODE["op"])],
                [("    if", CODE["kw"]), (" n == ", CODE["var"]), ("3", CODE["num"]), (": ", CODE["op"]), ("break", CODE["kw"])],
                [("    print", CODE["fn"]), ("(n)", CODE["op"])],
            ],
            size=11.5,
            leading=18,
            stroke="#5b1b1b",
        )
    )
    d.add(
        code_block(
            616,
            176,
            520,
            [
                [("for", CODE["kw"]), (" n ", CODE["var"]), ("in", CODE["kw"]), (" range", CODE["fn"]), ("(", CODE["op"]), ("1", CODE["num"]), (", ", CODE["op"]), ("6", CODE["num"]), ("):", CODE["op"])],
                [("    if", CODE["kw"]), (" n == ", CODE["var"]), ("3", CODE["num"]), (": ", CODE["op"]), ("continue", CODE["kw"])],
                [("    print", CODE["fn"]), ("(n)", CODE["op"])],
            ],
            size=11.5,
            leading=18,
            stroke="#4a3608",
        )
    )

    d.add(text(84, 300, "BREAK", size=11, fill=color("red")["dim"], mono=True, weight="700", spacing=2))
    sequence(84, lambda v: "green" if v < 3 else ("red" if v == 3 else "slate"), 2, "break")
    d.add(arrow(300, 418, 300, 396, stroke=color("red")["stroke"], marker="flowRed", width=2.2))
    d.add(text(300, 438, "break leaves the loop entirely", size=11, fill=color("red")["dim"], anchor="middle", mono=True))
    d.add(text(320, 470, "output:  1  2", size=14, fill=color("green")["dim"], anchor="middle", mono=True, weight="700"))

    d.add(text(616, 300, "CONTINUE", size=11, fill=color("amber")["dim"], mono=True, weight="700", spacing=2))
    sequence(616, lambda v: "amber" if v == 3 else "green", 5, "continue")
    d.add(arrow(832, 418, 832, 396, stroke=color("amber")["stroke"], marker="flowAmber", width=2.2))
    d.add(text(832, 438, "continue jumps to the next item", size=11, fill=color("amber")["dim"], anchor="middle", mono=True))
    d.add(text(852, 470, "output:  1  2  4  5", size=14, fill=color("green")["dim"], anchor="middle", mono=True, weight="700"))

    d.add(divider(58, 1162, 508, label="where each one is actually used"))

    d.add(
        card(
            58,
            538,
            546,
            160,
            "red",
            title="break",
            subtitle="stop early — the answer is found, or the user quit",
            lines=[
                "while True:",
                "    if choice == \"7\":",
                "        break            # menu exit",
            ],
            line_size=12,
            lines_top=628,
            lines_anchor="start",
        )
    )
    d.add(
        card(
            616,
            538,
            546,
            160,
            "amber",
            title="continue",
            subtitle="skip this one item — everything else still runs",
            lines=[
                "for t in transactions:",
                "    if not t.is_expense():",
                "        continue         # income only",
            ],
            line_size=12,
            lines_top=628,
            lines_anchor="start",
        )
    )
    return "week-05-break-vs-continue.svg", d.render()


# ---------------------------------------------------------------------------
# Week 6 — lists & tuples
# ---------------------------------------------------------------------------


def week06_index_and_slicing() -> tuple[str, str]:
    d = Diagram(
        1240,
        700,
        eyebrow="Week 06 · Lists & Tuples",
        title="Indexes Count From Zero, Slices Cut Between Items",
        subtitle="numbers = [0, 1, 2, 3, 4, 5] — the index is a position, the slice boundary is a gap",
    )

    values = ["10", "20", "30", "40", "50", "60"]
    box = 132
    gap = 16
    start = 128
    row_y = 236

    d.add(section(58, 152, 1124, 260, "01", "one list · two ways to point at it"))

    for index, value in enumerate(values):
        hue = "blue"
        c = color(hue)
        bx = start + index * (box + gap)
        d.add(rect(bx, row_y, box, 78, rx=10, fill=c["fill"], stroke=c["stroke"], width=1.8))
        d.add(text(bx + box / 2, row_y + 50, value, size=26, fill=TITLE, anchor="middle", mono=True, weight="700"))
        d.add(text(bx + box / 2, row_y - 14, str(index), size=15, fill=color("green")["dim"], anchor="middle", mono=True, weight="700"))
        d.add(text(bx + box / 2, row_y + 106, str(index - 6), size=15, fill=color("amber")["dim"], anchor="middle", mono=True, weight="700"))

    d.add(text(114, row_y - 14, "index", size=11, fill=color("green")["dim"], mono=True, anchor="end", weight="700"))
    d.add(text(114, row_y + 106, "negative", size=10, fill=color("amber")["dim"], mono=True, anchor="end", weight="700"))
    d.add(text(114, row_y + 50, "value", size=11, fill=SUBTITLE, mono=True, anchor="end", weight="700"))

    d.add(text(640, 390, "numbers[0] -> 10        numbers[-1] -> 60        numbers[2] -> 30", size=12.5, fill=SUBTITLE, anchor="middle", mono=True))

    # ---- slicing -----------------------------------------------------------
    d.add(section(58, 452, 1124, 208, "02", "slicing · numbers[1:4] takes everything between boundary 1 and boundary 4"))

    slice_y = 528
    for index, value in enumerate(values):
        inside = 1 <= index < 4
        hue = "purple" if inside else "slate"
        c = color(hue)
        bx = start + index * (box + gap)
        d.add(rect(bx, slice_y, box, 62, rx=10, fill=c["fill"], stroke=c["stroke"], width=1.8, opacity=1 if inside else 0.45))
        d.add(
            text(
                bx + box / 2,
                slice_y + 40,
                value,
                size=22,
                fill=TITLE,
                anchor="middle",
                mono=True,
                weight="700",
                opacity=None if inside else 0.5,
            )
        )

    for boundary in range(7):
        bx = start + boundary * (box + gap) - gap / 2
        highlight = boundary in (1, 4)
        stroke = color("purple")["stroke"] if highlight else "#2c3d61"
        d.add(line(bx, slice_y - 20, bx, slice_y + 74, stroke=stroke, width=2.4 if highlight else 1, dash=None if highlight else "3 4"))
        d.add(
            text(
                bx,
                slice_y - 28,
                str(boundary),
                size=12,
                fill=color("purple")["dim"] if highlight else "#64748b",
                anchor="middle",
                mono=True,
                weight="700",
            )
        )

    d.add(text(640, 628, "numbers[1:4] -> [20, 30, 40]     ·     the item at boundary 4 is NOT included", size=12.5, fill=color("purple")["dim"], anchor="middle", mono=True))
    return "week-06-index-and-slicing.svg", d.render()


def week06_list_vs_tuple() -> tuple[str, str]:
    d = Diagram(
        1220,
        680,
        eyebrow="Week 06 · Lists & Tuples",
        title="Mutable List, Immutable Tuple",
        subtitle="append() changes the object you already have — a tuple refuses and raises instead",
    )

    d.add(section(58, 150, 546, 400, "01", "list · mutable"))
    d.add(
        code_block(
            84,
            186,
            494,
            [
                [("items ", CODE["var"]), ("= [", CODE["op"]), ("1", CODE["num"]), (", ", CODE["op"]), ("2", CODE["num"]), (", ", CODE["op"]), ("3", CODE["num"]), ("]", CODE["op"])],
                [("items.", CODE["var"]), ("append", CODE["fn"]), ("(", CODE["op"]), ("4", CODE["num"]), (")", CODE["op"])],
                [("print", CODE["fn"]), ("(items)", CODE["op"]), ("   # [1, 2, 3, 4]", CODE["com"])],
            ],
            size=12,
            leading=20,
            stroke="#1f4030",
        )
    )

    for index, (label, values, hue) in enumerate(
        [("before", ["1", "2", "3"], "green"), ("after", ["1", "2", "3", "4"], "green")]
    ):
        y = 300 + index * 106
        c = color(hue)
        d.add(text(96, y + 8, label.upper(), size=10, fill=MUTED, mono=True, weight="700", spacing=1.6))
        for j, value in enumerate(values):
            bx = 96 + j * 66
            fresh = index == 1 and j == 3
            d.add(
                rect(
                    bx,
                    y + 22,
                    56,
                    50,
                    rx=8,
                    fill=color("amber")["fill"] if fresh else c["fill"],
                    stroke=color("amber")["stroke"] if fresh else c["stroke"],
                    width=1.7,
                )
            )
            d.add(text(bx + 28, y + 54, value, size=18, fill=TITLE, anchor="middle", mono=True, weight="700"))
        d.add(text(430, y + 54, "id: 0x7f2a...c40", size=10.5, fill=c["dim"], anchor="middle", mono=True))
    d.add(text(330, 512, "same object, new contents — the id never changed", size=11.5, fill=color("green")["dim"], anchor="middle"))

    d.add(section(658, 150, 504, 400, "02", "tuple · immutable"))
    d.add(
        code_block(
            684,
            186,
            452,
            [
                [("point ", CODE["var"]), ("= (", CODE["op"]), ("40.7", CODE["num"]), (", ", CODE["op"]), ("-74.0", CODE["num"]), (")", CODE["op"])],
                [("point[", CODE["var"]), ("0", CODE["num"]), ("] = ", CODE["op"]), ("41.0", CODE["num"])],
                [("TypeError: 'tuple' object does", CODE["err"])],
                [("not support item assignment", CODE["err"])],
            ],
            size=12,
            leading=20,
            stroke="#5b1b1b",
        )
    )
    d.add(
        card(
            684,
            326,
            452,
            96,
            "purple",
            title="( 40.7 , -74.0 )",
            subtitle="fixed shape, fixed contents, locked at creation",
            title_size=22,
        )
    )
    d.add(
        note(
            684,
            442,
            452,
            "cyan",
            "why the course uses tuples",
            "Each transaction is (description, amount, category) — always three fields in the same order. A tuple documents that shape.",
        )
    )

    d.add(
        note(
            58,
            580,
            1104,
            "amber",
            "the payoff comes in week 8",
            "Because a list is mutable, passing it into a function lets that function change your original data. Because a tuple is not, it cannot be changed by accident.",
        )
    )
    return "week-06-list-vs-tuple-mutability.svg", d.render()


# ---------------------------------------------------------------------------
# Week 7 — dictionaries & sets
# ---------------------------------------------------------------------------


def week07_dict_lookup() -> tuple[str, str]:
    d = Diagram(
        1240,
        720,
        eyebrow="Week 07 · Dictionaries & Sets",
        title="Look Up by Meaning, Not by Position",
        subtitle="A list makes you remember that Food is at index 0 — a dictionary lets you just ask for \"Food\"",
    )

    d.add(section(58, 150, 528, 268, "01", "list · addressed by position"))
    d.add(
        code_block(
            84,
            186,
            476,
            [
                [("totals ", CODE["var"]), ("= [", CODE["op"]), ("120.5", CODE["num"]), (", ", CODE["op"]), ("42.0", CODE["num"]), (", ", CODE["op"]), ("88.0", CODE["num"]), ("]", CODE["op"])],
                [("totals[", CODE["var"]), ("0", CODE["num"]), ("]", CODE["op"]), ("   # 120.5 ... of what?", CODE["com"])],
            ],
            size=12,
            leading=20,
        )
    )
    for index, value in enumerate(["120.5", "42.0", "88.0"]):
        bx = 96 + index * 156
        c = color("slate")
        d.add(rect(bx, 286, 138, 62, rx=9, fill=c["fill"], stroke=c["stroke"], width=1.6))
        d.add(text(bx + 69, 324, value, size=19, fill=TITLE, anchor="middle", mono=True, weight="700"))
        d.add(text(bx + 69, 272, f"[{index}]", size=11.5, fill=c["dim"], anchor="middle", mono=True, weight="700"))
    d.add(text(322, 384, "the meaning lives in your head, not in the data", size=11.5, fill=color("red")["dim"], anchor="middle"))

    d.add(section(640, 150, 542, 268, "02", "dict · addressed by key"))
    d.add(
        code_block(
            666,
            186,
            490,
            [
                [("categories ", CODE["var"]), ("= {", CODE["op"]), ('"Food"', CODE["str"]), (": ", CODE["op"]), ("120.5", CODE["num"]), (", ...}", CODE["op"])],
                [("categories[", CODE["var"]), ('"Food"', CODE["str"]), ("]", CODE["op"]), ("   # 120.5", CODE["com"])],
            ],
            size=12,
            leading=20,
        )
    )
    pairs = [("Food", "120.50", "green"), ("Transport", "42.00", "cyan"), ("Bills", "88.00", "purple")]
    for index, (key, value, hue) in enumerate(pairs):
        c = color(hue)
        y = 268 + index * 46
        d.add(rect(666, y, 200, 36, rx=8, fill=c["fill"], stroke=c["stroke"], width=1.6))
        d.add(text(766, y + 24, f'"{key}"', size=13, fill=c["text"], anchor="middle", mono=True, weight="700"))
        d.add(arrow(872, y + 18, 916, y + 18, stroke=c["stroke"], marker=_marker(hue), width=2))
        d.add(rect(922, y, 232, 36, rx=8, fill="#0c1424", stroke=c["stroke"], width=1.4))
        d.add(text(1038, y + 24, value, size=14, fill=TITLE, anchor="middle", mono=True, weight="700"))
    d.add(text(660, 264, "key", size=10, fill=MUTED, mono=True, anchor="end", weight="700"))

    d.add(divider(58, 1182, 458, label="reading a key that might not exist"))

    d.add(
        card(
            58,
            486,
            360,
            170,
            "red",
            title="Direct indexing",
            subtitle="crashes when the key is missing",
            lines=[
                'categories["Pets"]',
                "KeyError: 'Pets'",
            ],
            line_size=12,
            lines_top=580,
            lines_anchor="start",
        )
    )
    d.add(
        card(
            440,
            486,
            360,
            170,
            "green",
            title=".get() with a default",
            subtitle="returns a fallback instead of raising",
            lines=[
                'categories.get("Pets", 0)',
                "0",
            ],
            line_size=12,
            lines_top=580,
            lines_anchor="start",
        )
    )
    d.add(
        card(
            822,
            486,
            360,
            170,
            "amber",
            title="The running-total idiom",
            subtitle="first time and every time after",
            lines=[
                "categories[cat] = (",
                "  categories.get(cat, 0) + amount",
                ")",
            ],
            line_size=11.5,
            lines_top=576,
            lines_anchor="start",
        )
    )
    return "week-07-dict-lookup-vs-list-index.svg", d.render()


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


def week07_set_uniqueness() -> tuple[str, str]:
    d = Diagram(
        1200,
        640,
        eyebrow="Week 07 · Dictionaries & Sets",
        title="A Set Keeps Each Value Once",
        subtitle="Duplicates collapse on the way in — order is not promised on the way out",
    )

    d.add(section(58, 150, 400, 300, "01", "what you add"))
    inputs = ["Food", "Bills", "Food", "Transport", "Food"]
    for index, value in enumerate(inputs):
        dup = index in (2, 4)
        hue = "amber" if dup else "cyan"
        c = color(hue)
        y = 190 + index * 50
        d.add(rect(84, y, 348, 40, rx=8, fill=c["fill"], stroke=c["stroke"], width=1.5, opacity=0.9))
        d.add(text(104, y + 26, f'add("{value}")', size=13, fill=c["text"], mono=True))
        if dup:
            d.add(text(412, y + 26, "duplicate", size=10.5, fill=c["dim"], anchor="end", mono=True))

    d.add(section(742, 150, 400, 300, "02", "what you get back"))
    outputs = [("Food", "green"), ("Bills", "green"), ("Transport", "green")]
    for index, (value, hue) in enumerate(outputs):
        c = color(hue)
        y = 216 + index * 60
        d.add(rect(768, y, 348, 46, rx=8, fill=c["fill"], stroke=c["stroke"], width=1.6))
        d.add(text(942, y + 30, f'"{value}"', size=15, fill=TITLE, anchor="middle", mono=True, weight="700"))
    d.add(text(942, 420, "3 unique values, no ordering promise", size=11, fill=color("green")["dim"], anchor="middle"))

    d.add(
        card(
            488,
            234,
            224,
            132,
            "purple",
            title="set()",
            subtitle="hashes each value and drops repeats",
            title_size=22,
        )
    )
    d.add(arrow(438, 300, 482, 300, width=2.4))
    d.add(arrow(716, 300, 762, 300, width=2.4))

    d.add(
        note(
            58,
            486,
            546,
            "cyan",
            "use a set when",
            "You only care whether something is present, or you need to strip duplicates: unique categories, tags, seen IDs.",
        )
    )
    d.add(
        note(
            636,
            486,
            506,
            "amber",
            "use a dict when",
            "You need a value attached to each key: a running total per category, a price per item.",
        )
    )
    return "week-07-set-uniqueness.svg", d.render()


# ---------------------------------------------------------------------------
# Week 8 — functions
# ---------------------------------------------------------------------------


def week08_call_stack() -> tuple[str, str]:
    d = Diagram(
        1360,
        880,
        eyebrow="Week 08 · Functions",
        title="What Happens to a Value You Pass Into a Function",
        subtitle="A fresh frame is built for the call, the parameter is bound to the argument's object — then the whole frame is thrown away",
    )

    col_w = 296
    gap = 22
    xs = [40 + index * (col_w + gap) for index in range(4)]
    top = 150
    height = 434

    headers = [
        ("01", "before the call", "score = 10"),
        ("02", "the call is made", "add_one(score)"),
        ("03", "inside the function", "number = number + 1"),
        ("04", "after return", "print(score)"),
    ]
    for index, (num, label, code) in enumerate(headers):
        d.add(section(xs[index], top, col_w, height, num, label))
        d.add(
            text(
                xs[index] + col_w / 2,
                top + 32,
                code,
                size=12.5,
                fill=ACCENT_TAG,
                anchor="middle",
                mono=True,
                weight="700",
            )
        )

    def frame(x: float, y: float, w: float, h: float, label: str, hue: str, ghost: bool = False) -> None:
        c = color(hue)
        d.add(
            rect(
                x,
                y,
                w,
                h,
                rx=10,
                fill="#0a1120" if not ghost else "#0a0f1c",
                stroke=c["stroke"],
                width=1.6,
                dash="5 5" if ghost else None,
                opacity=0.45 if ghost else 1,
            )
        )
        d.add(text(x + 12, y + 20, label.upper(), size=9.5, fill=c["dim"], mono=True, weight="700", spacing=1.4, opacity=0.55 if ghost else None))

    def binding(x: float, y: float, name: str, hue: str, ghost: bool = False) -> None:
        c = color(hue)
        d.add(rect(x, y, 104, 40, rx=8, fill=c["fill"], stroke=c["stroke"], width=1.6, opacity=0.35 if ghost else 1))
        d.add(
            text(
                x + 52,
                y + 26,
                name,
                size=14,
                fill=TITLE,
                anchor="middle",
                mono=True,
                weight="700",
                opacity=0.4 if ghost else None,
            )
        )

    def obj(x: float, y: float, value: str, hue: str, caption: str, ghost: bool = False) -> None:
        c = color(hue)
        d.add(rect(x, y, 108, 46, rx=9, fill=c["fill"], stroke=c["stroke"], width=1.8, opacity=0.3 if ghost else 1))
        d.add(
            text(
                x + 54,
                y + 31,
                value,
                size=20,
                fill=TITLE,
                anchor="middle",
                mono=True,
                weight="700",
                opacity=0.4 if ghost else None,
            )
        )
        d.add(text(x + 54, y + 62, caption, size=9.5, fill=c["dim"], anchor="middle", mono=True))

    # ---- column 1 ----------------------------------------------------------
    x = xs[0]
    frame(x + 22, top + 56, col_w - 44, 124, "global frame", "blue")
    binding(x + 40, top + 96, "score", "blue")
    obj(x + 168, top + 93, "10", "blue", "int object")
    d.add(arrow(x + 146, top + 116, x + 162, top + 116, stroke=color("blue")["stroke"], marker="flowBlue", width=2))
    d.add(text(x + col_w / 2, top + 250, "Only the module level exists.", size=11, fill=SUBTITLE, anchor="middle"))
    d.add(text(x + col_w / 2, top + 268, "There is no function frame yet.", size=11, fill=SUBTITLE, anchor="middle"))

    # ---- column 2 ----------------------------------------------------------
    x = xs[1]
    frame(x + 22, top + 56, col_w - 44, 124, "global frame", "blue")
    binding(x + 40, top + 96, "score", "blue")
    obj(x + 168, top + 93, "10", "blue", "int object")
    d.add(arrow(x + 146, top + 116, x + 162, top + 116, stroke=color("blue")["stroke"], marker="flowBlue", width=2))

    frame(x + 22, top + 208, col_w - 44, 112, "add_one frame · new", "green")
    binding(x + 40, top + 248, "number", "green")
    d.add(
        elbow(
            [(x + 222, top + 139), (x + 256, top + 139), (x + 256, top + 268), (x + 150, top + 268)],
            stroke=color("green")["stroke"],
            marker="flowGreen",
            width=2.2,
        )
    )
    d.add(text(x + col_w / 2, top + 350, "The parameter is bound to the", size=11, fill=SUBTITLE, anchor="middle"))
    d.add(text(x + col_w / 2, top + 368, "same object — not a copy of it.", size=11, fill=SUBTITLE, anchor="middle"))

    # ---- column 3 ----------------------------------------------------------
    x = xs[2]
    frame(x + 22, top + 56, col_w - 44, 124, "global frame", "blue")
    binding(x + 40, top + 96, "score", "blue")
    obj(x + 168, top + 93, "10", "blue", "unchanged")
    d.add(arrow(x + 146, top + 116, x + 162, top + 116, stroke=color("blue")["stroke"], marker="flowBlue", width=2))

    frame(x + 22, top + 208, col_w - 44, 124, "add_one frame", "amber")
    binding(x + 40, top + 248, "number", "amber")
    obj(x + 168, top + 245, "11", "amber", "NEW int object")
    d.add(arrow(x + 146, top + 268, x + 162, top + 268, stroke=color("amber")["stroke"], marker="flowAmber", width=2))
    d.add(text(x + col_w / 2, top + 350, "number = number + 1 builds a new", size=11, fill=SUBTITLE, anchor="middle"))
    d.add(text(x + col_w / 2, top + 368, "object and re-points the LOCAL name.", size=11, fill=SUBTITLE, anchor="middle"))
    d.add(text(x + col_w / 2, top + 396, "Inside function: 11", size=12, fill=color("amber")["dim"], anchor="middle", mono=True, weight="700"))

    # ---- column 4 ----------------------------------------------------------
    x = xs[3]
    frame(x + 22, top + 56, col_w - 44, 124, "global frame", "blue")
    binding(x + 40, top + 96, "score", "blue")
    obj(x + 168, top + 93, "10", "blue", "still 10")
    d.add(arrow(x + 146, top + 116, x + 162, top + 116, stroke=color("blue")["stroke"], marker="flowBlue", width=2))

    frame(x + 22, top + 208, col_w - 44, 124, "add_one frame · discarded", "slate", ghost=True)
    binding(x + 40, top + 248, "number", "slate", ghost=True)
    obj(x + 168, top + 245, "11", "slate", "", ghost=True)
    d.add(line(x + 34, top + 218, x + col_w - 34, top + 322, stroke="#7f1d1d", width=2))
    d.add(line(x + col_w - 34, top + 218, x + 34, top + 322, stroke="#7f1d1d", width=2))
    d.add(text(x + col_w / 2, top + 350, "The frame, the parameter, and every", size=11, fill=SUBTITLE, anchor="middle"))
    d.add(text(x + col_w / 2, top + 368, "local name vanish when the call ends.", size=11, fill=SUBTITLE, anchor="middle"))
    d.add(text(x + col_w / 2, top + 396, "Outside function: 10", size=12, fill=color("green")["dim"], anchor="middle", mono=True, weight="700"))

    for index in range(3):
        d.add(arrow(xs[index] + col_w + 2, top + 180, xs[index + 1] - 6, top + 180, width=2.4))

    d.add(
        code_block(
            40,
            626,
            640,
            [
                [("def", CODE["kw"]), (" add_one", CODE["fn"]), ("(", CODE["op"]), ("number", CODE["var"]), ("):", CODE["op"])],
                [("    number ", CODE["var"]), ("= number + ", CODE["op"]), ("1", CODE["num"])],
                [("    print", CODE["fn"]), ("(", CODE["op"]), ('f"Inside function: {number}"', CODE["str"]), (")", CODE["op"])],
                [("", CODE["op"])],
                [("score ", CODE["var"]), ("= ", CODE["op"]), ("10", CODE["num"])],
                [("add_one", CODE["fn"]), ("(score)", CODE["op"])],
                [("print", CODE["fn"]), ("(", CODE["op"]), ('f"Outside function: {score}"', CODE["str"]), (")", CODE["op"])],
            ],
            title="THE CODE BEING TRACED",
            size=12,
            leading=20,
        )
    )

    d.add(
        note(
            706,
            626,
            614,
            "purple",
            "the precise wording",
            "Python is call by object reference (also called call by assignment). For immutable values — int, float, str, bool, tuple — the result LOOKS exactly like pass by value, because rebinding a name can never reach back into the caller.",
        )
    )
    d.add(
        note(
            706,
            734,
            614,
            "amber",
            "the exception to watch for",
            "If you MUTATE a list or dict instead of rebinding it, the caller does see the change. That is the next diagram.",
        )
    )

    items = [("blue", "caller / global frame"), ("green", "new frame"), ("amber", "rebound local"), ("slate", "destroyed")]
    d.add(legend(d.center - legend_width(items) / 2, 824, items))
    return "week-08-call-stack-and-frames.svg", d.render()


def week08_function_anatomy() -> tuple[str, str]:
    d = Diagram(
        1260,
        802,
        eyebrow="Week 08 · Functions",
        title="Anatomy of a Function — Definition and Call",
        subtitle="Parameters are the slots in the definition; arguments are the values you drop into them at the call site",
    )

    d.add(section(58, 146, 690, 330, "01", "the definition"))
    d.add(
        code_block(
            84,
            186,
            638,
            [
                [("def", CODE["kw"]), (" calculate_tip", CODE["fn"]), ("(", CODE["op"]), ("bill", CODE["var"]), (", ", CODE["op"]), ("tip_percent", CODE["var"]), ("=", CODE["op"]), ("18", CODE["num"]), ("):", CODE["op"])],
                [('    """Calculate the tip amount for a bill."""', CODE["str"])],
                [("    tip ", CODE["var"]), ("= bill * (tip_percent / ", CODE["op"]), ("100", CODE["num"]), (")", CODE["op"])],
                [("    return", CODE["kw"]), (" tip", CODE["var"])],
            ],
            size=12.5,
            leading=24,
        )
    )

    labels = [
        (108, "def", "starts a definition", "pink"),
        (216, "calculate_tip", "the name you will call", "blue"),
        (400, "bill", "required parameter", "green"),
        (560, "tip_percent=18", "optional, has a default", "amber"),
        (140, "docstring", "what it does, in one line", "cyan"),
        (140, "return", "hands a value back to the caller", "purple"),
    ]
    for index, (x, label, body, hue) in enumerate(labels[:4]):
        c = color(hue)
        y = 340 + (index % 2) * 62
        d.add(rect(84 + index * 162, y, 152, 52, rx=8, fill=c["fill"], stroke=c["stroke"], width=1.4))
        d.add(text(84 + index * 162 + 76, y + 22, label, size=11.5, fill=TITLE, anchor="middle", mono=True, weight="700"))
        d.add(text(84 + index * 162 + 76, y + 40, body, size=10, fill=c["dim"], anchor="middle"))

    d.add(section(786, 146, 416, 330, "02", "the two special lines"))
    d.add(
        card(
            810,
            190,
            368,
            120,
            "cyan",
            title="The docstring",
            subtitle="First line inside the function. Shows up in help() and in your editor's tooltip.",
        )
    )
    d.add(
        card(
            810,
            330,
            368,
            128,
            "purple",
            title="return vs print",
            subtitle="return hands a value back so the caller can use it. print only draws characters on screen.",
        )
    )

    d.add(divider(58, 1202, 512, label="the call site"))

    d.add(
        code_block(
            58,
            542,
            560,
            [
                [("big_tip ", CODE["var"]), ("= calculate_tip", CODE["fn"]), ("(", CODE["op"]), ("50", CODE["num"]), (", ", CODE["op"]), ("25", CODE["num"]), (")", CODE["op"])],
                [("print", CODE["fn"]), ("(", CODE["op"]), ('f"Tip: ${big_tip:.2f}"', CODE["str"]), (")", CODE["op"])],
                [("Tip: $12.50", CODE["out"])],
            ],
            size=12.5,
            leading=22,
        )
    )

    mapping = [
        ("50", "bill", "green"),
        ("25", "tip_percent", "amber"),
    ]
    for index, (argument, parameter, hue) in enumerate(mapping):
        c = color(hue)
        y = 566 + index * 68
        d.add(rect(660, y, 108, 46, rx=9, fill=c["fill"], stroke=c["stroke"], width=1.7))
        d.add(text(714, y + 31, argument, size=19, fill=TITLE, anchor="middle", mono=True, weight="700"))
        d.add(text(714, y - 6, "argument", size=9.5, fill=c["dim"], anchor="middle", mono=True, weight="700"))
        d.add(arrow(774, y + 23, 838, y + 23, stroke=c["stroke"], marker=_marker(hue), width=2.2))
        d.add(rect(844, y, 168, 46, rx=9, fill="#0c1424", stroke=c["stroke"], width=1.5))
        d.add(text(928, y + 30, parameter, size=15, fill=c["text"], anchor="middle", mono=True, weight="700"))
        d.add(text(928, y - 6, "parameter", size=9.5, fill=c["dim"], anchor="middle", mono=True, weight="700"))

    d.add(
        rect(844, 698, 168, 42, rx=9, fill=color("purple")["fill"], stroke=color("purple")["stroke"], width=1.7)
    )
    d.add(text(928, 692, "return value", size=9.5, fill=color("purple")["dim"], anchor="middle", mono=True, weight="700"))
    d.add(text(928, 726, "12.50", size=17, fill=TITLE, anchor="middle", mono=True, weight="700"))
    d.add(
        elbow(
            [(838, 719), (646, 719), (646, 600), (624, 600)],
            stroke=color("purple")["stroke"],
            marker="flowPurple",
            width=2.2,
        )
    )
    d.add(text(742, 710, "flows back into big_tip", size=10.5, fill=color("purple")["dim"], anchor="middle", mono=True))
    d.add(
        text(
            d.center,
            772,
            "Positional arguments are matched left to right. Anything you leave out falls back to its default.",
            size=11.5,
            fill=SUBTITLE,
            anchor="middle",
        )
    )
    return "week-08-function-anatomy.svg", d.render()


def week08_mutable_arguments() -> tuple[str, str]:
    d = Diagram(
        1240,
        740,
        eyebrow="Week 08 · Functions",
        title="Rebinding vs Mutating an Argument",
        subtitle="The rule that decides whether the caller sees your change — and it is not about the function, it is about the object",
    )

    d.add(section(58, 150, 546, 420, "01", "immutable · caller is untouched"))
    d.add(
        code_block(
            84,
            190,
            494,
            [
                [("def", CODE["kw"]), (" add_one", CODE["fn"]), ("(", CODE["op"]), ("number", CODE["var"]), ("):", CODE["op"])],
                [("    number ", CODE["var"]), ("= number + ", CODE["op"]), ("1", CODE["num"]), ("   # REBIND", CODE["com"])],
                [("", CODE["op"])],
                [("score ", CODE["var"]), ("= ", CODE["op"]), ("10", CODE["num"])],
                [("add_one", CODE["fn"]), ("(score)", CODE["op"])],
                [("print", CODE["fn"]), ("(score)", CODE["op"]), ("   # 10", CODE["com"])],
            ],
            size=12,
            leading=21,
            stroke="#1e3555",
        )
    )
    d.add(
        card(
            84,
            360,
            494,
            94,
            "blue",
            title="score is still 10",
            subtitle="A new int was created inside the function. The caller's name never moved.",
        )
    )
    d.add(
        note(
            84,
            472,
            494,
            "slate",
            "immutable types",
            "int · float · str · bool · tuple · frozenset — none of them can be edited in place, so a function can only ever rebind its own local name.",
        )
    )

    d.add(section(636, 150, 546, 420, "02", "mutable · caller sees the change"))
    d.add(
        code_block(
            662,
            190,
            494,
            [
                [("def", CODE["kw"]), (" add_item", CODE["fn"]), ("(", CODE["op"]), ("items", CODE["var"]), ("):", CODE["op"])],
                [("    items.", CODE["var"]), ("append", CODE["fn"]), ("(", CODE["op"]), ('"new"', CODE["str"]), (")", CODE["op"]), ("  # MUTATE", CODE["com"])],
                [("", CODE["op"])],
                [("shopping ", CODE["var"]), ("= [", CODE["op"]), ('"milk"', CODE["str"]), ("]", CODE["op"])],
                [("add_item", CODE["fn"]), ("(shopping)", CODE["op"])],
                [("print", CODE["fn"]), ("(shopping)", CODE["op"]), ("  # ['milk', 'new']", CODE["com"])],
            ],
            size=12,
            leading=21,
            stroke="#4a3608",
        )
    )
    d.add(
        card(
            662,
            360,
            494,
            94,
            "amber",
            title="shopping now has 2 items",
            subtitle="Both names point at one list. Editing it in place is visible everywhere.",
        )
    )
    d.add(
        note(
            662,
            472,
            494,
            "green",
            "mutable types",
            "list · dict · set · your own class instances — .append(), [key] = value, and attribute assignment all change the shared object.",
        )
    )

    d.add(
        note(
            58,
            608,
            1124,
            "purple",
            "the one-sentence rule",
            "Assigning to a bare name inside a function (name = ...) only ever affects that function. Calling a method that changes the object, or assigning into it (obj.attr = ..., d[key] = ..., lst.append(...)), affects everyone who holds a reference to it.",
        )
    )
    return "week-08-mutable-vs-immutable-arguments.svg", d.render()


DIAGRAMS = [
    week05_for_loop_anatomy,
    week05_while_loop_cycle,
    week05_break_vs_continue,
    week06_index_and_slicing,
    week06_list_vs_tuple,
    week07_dict_lookup,
    week07_set_uniqueness,
    week08_call_stack,
    week08_function_anatomy,
    week08_mutable_arguments,
]
