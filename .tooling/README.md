# `.tooling/` — repository maintenance

**This folder is not course material.** Nothing here is part of the 12-week plan, and learners never
need to open it. It is deliberately dot-prefixed so it stays out of the way of the chapters.

It contains the generator that produces every SVG in [`../diagrams`](../diagrams/README.md).

## Rebuilding the diagrams

From the repository root:

```bash
python .tooling/generate_diagrams.py
```

That rewrites all 30 files in `diagrams/`. **Do not hand-edit the SVGs** — edit the builder function
and rerun the script, or your change disappears on the next build.

## Layout

| File | Purpose |
|---|---|
| `diagram_kit.py` | The design system: palette, glow filters, cards, panels, arrows, code blocks, callouts, legends, and the `Diagram` canvas |
| `diagrams_month1.py` | Weeks 1-4 |
| `diagrams_month2.py` | Weeks 5-8 |
| `diagrams_month3.py` | Weeks 9-12, the bonus chapter, and the course roadmap |
| `generate_diagrams.py` | Runner — imports the three month modules and writes every file |

Each diagram is one function returning `(filename, svg_string)`, registered in that module's
`DIAGRAMS` list.

## Two constraints that are easy to break

1. **The monospace stack is deliberately ligature-free.** Fonts like Cascadia Code render `>=` as a
   single `≥` glyph and `->` as `→`. That is unacceptable in a course where learners must type the
   characters exactly. Do not add a ligature font to `MONO` in `diagram_kit.py`.

2. **Whitespace is hardened with non-breaking spaces.** Some Markdown hosts strip
   `xml:space="preserve"`, which would collapse the indentation inside every code block. The
   `hard_spaces()` helper converts leading and repeated spaces to U+00A0, which has the same advance
   width in a monospace font. Route any new text through `text()` or `code_block()` so it gets this
   treatment automatically.

## Adding a diagram

1. Write a builder function in the relevant `diagrams_month*.py`.
2. Add it to that module's `DIAGRAMS` list.
3. Run the generator.
4. Embed it in the chapter with descriptive alt text and a one-line italic caption.
5. Add a row to `diagrams/README.md`.
