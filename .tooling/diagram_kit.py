"""Design-system helpers for the course diagrams.

This module is tooling, not course material. It exists so every diagram in
``diagrams/`` shares one dark "neon topology" theme and can be regenerated
after an edit instead of being hand-tweaked in an SVG editor.

Run ``python .tooling/generate_diagrams.py`` from the repository root to rebuild
every diagram.
"""

from __future__ import annotations

from xml.sax.saxutils import escape

# ---------------------------------------------------------------------------
# Theme
# ---------------------------------------------------------------------------

SANS = "ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
# Deliberately ligature-free: a course must render >= and -> exactly as they are typed.
MONO = "ui-monospace, Consolas, 'SF Mono', Menlo, 'DejaVu Sans Mono', 'Courier New', monospace"

PAGE_BG = "#070b14"
FRAME_STROKE = "#1e293b"
PANEL_BG = "#0d1526"
PANEL_STROKE = "#1b2942"

TITLE = "#f8fafc"
SUBTITLE = "#94a3b8"
EYEBROW = "#5b7192"
LABEL = "#8aa2c0"
LABEL_INDEX = "#33507c"
MUTED = "#64748b"
FLOW = "#f43f5e"
FLOW_SOFT = "#475569"
ACCENT_TAG = "#fbbf24"

COLORS = {
    "pink": {"stroke": "#ec4899", "fill": "#2b0f21", "text": "#fbcfe8", "dim": "#f0a8cd"},
    "amber": {"stroke": "#f59e0b", "fill": "#2b1c05", "text": "#fde68a", "dim": "#fcd34d"},
    "blue": {"stroke": "#3b82f6", "fill": "#0a1e3c", "text": "#bfdbfe", "dim": "#93c5fd"},
    "purple": {"stroke": "#a855f7", "fill": "#1d0f33", "text": "#e9d5ff", "dim": "#d8b4fe"},
    "green": {"stroke": "#22c55e", "fill": "#07301c", "text": "#bbf7d0", "dim": "#86efac"},
    "cyan": {"stroke": "#22d3ee", "fill": "#05262f", "text": "#a5f3fc", "dim": "#67e8f9"},
    "red": {"stroke": "#ef4444", "fill": "#2e0e0e", "text": "#fecaca", "dim": "#fca5a5"},
    "slate": {"stroke": "#64748b", "fill": "#101827", "text": "#e2e8f0", "dim": "#94a3b8"},
}

# Token colours for the terminal-style code blocks.
CODE = {
    "kw": "#f472b6",
    "fn": "#60a5fa",
    "cls": "#c4b5fd",
    "str": "#86efac",
    "num": "#fbbf24",
    "com": "#5b6b86",
    "op": "#8fa3bf",
    "var": "#e2e8f0",
    "dim": "#94a3b8",
    "out": "#7dd3fc",
    "err": "#fca5a5",
    "ok": "#86efac",
}

# Rough advance-width ratios used for text wrapping and centring math.
MONO_RATIO = 0.60
SANS_RATIO = 0.54


def color(name: str) -> dict:
    return COLORS[name]


# ---------------------------------------------------------------------------
# Text utilities
# ---------------------------------------------------------------------------


def text_width(value: str, size: float, mono: bool = False) -> float:
    return len(value) * size * (MONO_RATIO if mono else SANS_RATIO)


def wrap(value: str, width: float, size: float, mono: bool = False) -> list[str]:
    """Greedy word wrap for a fixed pixel width."""
    ratio = MONO_RATIO if mono else SANS_RATIO
    max_chars = max(8, int(width / (size * ratio)))
    words = value.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if len(candidate) <= max_chars:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [""]


def _n(value: float) -> str:
    if isinstance(value, int):
        return str(value)
    rounded = round(float(value), 2)
    if rounded == int(rounded):
        return str(int(rounded))
    return str(rounded)


NBSP = "\u00a0"


def hard_spaces(value: str) -> str:
    """Make leading and repeated spaces survive XML whitespace collapsing.

    ``xml:space="preserve"`` is also emitted, but some Markdown hosts sanitise
    it away. Non-breaking spaces have the same advance width in a monospace
    font, so indentation and column alignment survive either way.
    """
    if "  " not in value and not value.startswith(" ") and not value.endswith(" "):
        return value
    out = []
    for index, char in enumerate(value):
        if char != " ":
            out.append(char)
        elif index == 0 or index == len(value) - 1 or value[index - 1] == " " or value[index + 1] == " ":
            out.append(NBSP)
        else:
            out.append(char)
    return "".join(out)


def text(
    x: float,
    y: float,
    value: str,
    *,
    size: float = 12,
    fill: str = TITLE,
    weight: str = "400",
    anchor: str = "start",
    mono: bool = False,
    spacing: float | None = None,
    opacity: float | None = None,
    style: str = "",
) -> str:
    attrs = [
        f'x="{_n(x)}"',
        f'y="{_n(y)}"',
        f'fill="{fill}"',
        f'font-size="{_n(size)}"',
        f'font-family="{MONO if mono else SANS}"',
    ]
    if weight != "400":
        attrs.append(f'font-weight="{weight}"')
    if anchor != "start":
        attrs.append(f'text-anchor="{anchor}"')
    if spacing is not None:
        attrs.append(f'letter-spacing="{_n(spacing)}"')
    if opacity is not None:
        attrs.append(f'opacity="{_n(opacity)}"')
    if style:
        attrs.append(f'font-style="{style}"')
    return f'<text {" ".join(attrs)} xml:space="preserve">{escape(hard_spaces(value))}</text>'


# ---------------------------------------------------------------------------
# Primitives
# ---------------------------------------------------------------------------


def rect(
    x: float,
    y: float,
    w: float,
    h: float,
    *,
    rx: float = 10,
    fill: str = "none",
    stroke: str = "none",
    width: float = 1,
    dash: str | None = None,
    opacity: float | None = None,
    filter_id: str | None = None,
) -> str:
    attrs = [
        f'x="{_n(x)}"',
        f'y="{_n(y)}"',
        f'width="{_n(w)}"',
        f'height="{_n(h)}"',
        f'rx="{_n(rx)}"',
        f'fill="{fill}"',
    ]
    if stroke != "none":
        attrs.append(f'stroke="{stroke}"')
        attrs.append(f'stroke-width="{_n(width)}"')
    if dash:
        attrs.append(f'stroke-dasharray="{dash}"')
    if opacity is not None:
        attrs.append(f'opacity="{_n(opacity)}"')
    if filter_id:
        attrs.append(f'filter="url(#{filter_id})"')
    return f"<rect {' '.join(attrs)}/>"


def line(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    *,
    stroke: str = FLOW_SOFT,
    width: float = 1.4,
    dash: str | None = None,
    marker: str | None = None,
    opacity: float | None = None,
) -> str:
    attrs = [
        f'x1="{_n(x1)}"',
        f'y1="{_n(y1)}"',
        f'x2="{_n(x2)}"',
        f'y2="{_n(y2)}"',
        f'stroke="{stroke}"',
        f'stroke-width="{_n(width)}"',
        'stroke-linecap="round"',
    ]
    if dash:
        attrs.append(f'stroke-dasharray="{dash}"')
    if marker:
        attrs.append(f'marker-end="url(#{marker})"')
    if opacity is not None:
        attrs.append(f'opacity="{_n(opacity)}"')
    return f"<line {' '.join(attrs)}/>"


def path(
    d: str,
    *,
    stroke: str = FLOW_SOFT,
    width: float = 1.6,
    fill: str = "none",
    dash: str | None = None,
    marker: str | None = None,
    opacity: float | None = None,
) -> str:
    attrs = [
        f'd="{d}"',
        f'fill="{fill}"',
        f'stroke="{stroke}"',
        f'stroke-width="{_n(width)}"',
        'stroke-linecap="round"',
        'stroke-linejoin="round"',
    ]
    if dash:
        attrs.append(f'stroke-dasharray="{dash}"')
    if marker:
        attrs.append(f'marker-end="url(#{marker})"')
    if opacity is not None:
        attrs.append(f'opacity="{_n(opacity)}"')
    return f"<path {' '.join(attrs)}/>"


def circle(
    cx: float,
    cy: float,
    r: float,
    *,
    fill: str = "none",
    stroke: str = "none",
    width: float = 1.4,
    opacity: float | None = None,
) -> str:
    attrs = [f'cx="{_n(cx)}"', f'cy="{_n(cy)}"', f'r="{_n(r)}"', f'fill="{fill}"']
    if stroke != "none":
        attrs.append(f'stroke="{stroke}"')
        attrs.append(f'stroke-width="{_n(width)}"')
    if opacity is not None:
        attrs.append(f'opacity="{_n(opacity)}"')
    return f"<circle {' '.join(attrs)}/>"


# ---------------------------------------------------------------------------
# Composite blocks
# ---------------------------------------------------------------------------


def section(x: float, y: float, w: float, h: float, index: str, label: str) -> str:
    """A numbered container panel with a small header above it."""
    return "\n".join(
        [
            text(x + 4, y - 10, index, size=11, fill=LABEL_INDEX, weight="700", mono=True, spacing=1.5),
            text(x + 34, y - 10, label.upper(), size=11, fill=LABEL, weight="700", mono=True, spacing=2.2),
            rect(x, y, w, h, rx=12, fill=PANEL_BG, stroke=PANEL_STROKE, width=1.2),
        ]
    )


def card(
    x: float,
    y: float,
    w: float,
    h: float,
    hue: str,
    *,
    title: str = "",
    subtitle: str = "",
    lines: list[str] | None = None,
    badge: str | None = None,
    tag: str | None = None,
    footer: str | None = None,
    title_size: float = 15,
    line_size: float = 11,
    glow: bool = True,
    lines_mono: bool = True,
    lines_anchor: str = "middle",
    lines_top: float | None = None,
) -> str:
    """The signature card: tinted fill, neon 2px border, optional badge/tag/footer."""
    c = color(hue)
    cx = x + w / 2
    out: list[str] = []
    if glow:
        out.append(rect(x, y, w, h, rx=12, fill="none", stroke=c["stroke"], width=2, opacity=0.5, filter_id="neon"))
    out.append(rect(x, y, w, h, rx=12, fill=c["fill"], stroke=c["stroke"], width=2))

    if badge:
        out.append(circle(x + 22, y + 22, 12, fill="#0b1220", stroke=c["stroke"], width=1.6))
        out.append(text(x + 22, y + 26, badge, size=10, fill=c["dim"], weight="700", anchor="middle", mono=True))
    if tag:
        out.append(text(x + w - 14, y + 26, tag, size=10, fill=c["dim"], anchor="end", mono=True, spacing=0.4))

    cursor = y + (48 if (badge or tag) else 30)
    if title:
        out.append(text(cx, cursor, title, size=title_size, fill=TITLE, weight="700", anchor="middle"))
        cursor += 18
    if subtitle:
        for chunk in wrap(subtitle, w - 26, 11.5):
            out.append(text(cx, cursor, chunk, size=11.5, fill=c["text"], anchor="middle"))
            cursor += 15
        cursor += 3

    if lines:
        cursor = lines_top if lines_top is not None else cursor + 4
        anchor_x = cx if lines_anchor == "middle" else x + 16
        for item in lines:
            out.append(
                text(anchor_x, cursor, item, size=line_size, fill=c["dim"], anchor=lines_anchor, mono=lines_mono)
            )
            cursor += line_size + 4.5

    if footer:
        out.append(line(x + 12, y + h - 30, x + w - 12, y + h - 30, stroke=c["stroke"], width=1, opacity=0.35))
        out.append(text(cx, y + h - 13, footer, size=10.5, fill=ACCENT_TAG, anchor="middle", mono=True, spacing=0.3))
    return "\n".join(out)


def code_block(
    x: float,
    y: float,
    w: float,
    rows: list,
    *,
    size: float = 12,
    leading: float = 18,
    pad: float = 14,
    title: str | None = None,
    stroke: str = "#1e2b45",
    fill: str = "#080e1c",
) -> str:
    """A terminal-style block.

    Each row is either a ``(text, colour)`` tuple or a list of such tuples when
    a single line needs token-level colouring. Tokens are emitted as ``tspan``
    children of one ``text`` element so the renderer — not this module — is
    responsible for advance widths.
    """
    head = 24 if title else 0
    h = pad * 2 + head + leading * len(rows)
    out = [rect(x, y, w, h, rx=10, fill=fill, stroke=stroke, width=1.2)]
    if title:
        out.append(text(x + pad, y + pad + 6, title, size=10, fill=MUTED, mono=True, spacing=1.6, weight="700"))
    top = y + pad + head + size
    for index, row in enumerate(rows):
        segments = [row] if isinstance(row, tuple) else list(row)
        spans = "".join(
            f'<tspan fill="{colour}">{escape(hard_spaces(value))}</tspan>'
            for value, colour in segments
            if value
        )
        if not spans:
            continue
        out.append(
            f'<text x="{_n(x + pad)}" y="{_n(top + index * leading)}" font-size="{_n(size)}" '
            f'font-family="{MONO}" xml:space="preserve">{spans}</text>'
        )
    return "\n".join(out)


def code_height(rows: int, *, leading: float = 18, pad: float = 14, title: bool = False) -> float:
    return pad * 2 + (24 if title else 0) + leading * rows


def note(
    x: float,
    y: float,
    w: float,
    hue: str,
    label: str,
    body: str,
    *,
    size: float = 11.5,
    leading: float = 16,
) -> str:
    """A left-bar callout used for 'remember this' asides."""
    c = color(hue)
    body_lines = wrap(body, w - 34, size)
    h = 30 + leading * len(body_lines) + 8
    out = [
        rect(x, y, w, h, rx=8, fill=c["fill"], stroke=c["stroke"], width=1, opacity=0.85),
        rect(x, y, 4, h, rx=2, fill=c["stroke"]),
        text(x + 16, y + 20, label.upper(), size=10, fill=c["dim"], weight="700", mono=True, spacing=1.6),
    ]
    for index, chunk in enumerate(body_lines):
        out.append(text(x + 16, y + 38 + index * leading, chunk, size=size, fill=c["text"]))
    return "\n".join(out)


def note_height(body: str, w: float, *, size: float = 11.5, leading: float = 16) -> float:
    return 30 + leading * len(wrap(body, w - 34, size)) + 8


def pill(x: float, y: float, hue: str, label: str, *, size: float = 11) -> tuple[str, float]:
    """A legend pill. Returns (svg, width)."""
    c = color(hue)
    w = 30 + text_width(label, size) + 14
    out = [
        rect(x, y, w, 26, rx=13, fill="#0c1424", stroke=c["stroke"], width=1.2, opacity=0.95),
        circle(x + 16, y + 13, 4.5, fill=c["stroke"]),
        text(x + 27, y + 17, label, size=size, fill="#cbd5e1"),
    ]
    return "\n".join(out), w


def legend_width(items: list[tuple[str, str]], *, gap: float = 10, size: float = 11) -> float:
    total = 0.0
    for _, label in items:
        total += 30 + text_width(label, size) + 14 + gap
    return max(0.0, total - gap)


def legend(x: float, y: float, items: list[tuple[str, str]], *, gap: float = 10) -> str:
    out = []
    cursor = x
    for hue, label in items:
        svg, w = pill(cursor, y, hue, label)
        out.append(svg)
        cursor += w + gap
    return "\n".join(out)


def flow_label(x: float, y: float, value: str, *, fill: str = ACCENT_TAG, anchor: str = "middle") -> str:
    return text(x, y, value, size=10.5, fill=fill, anchor=anchor, mono=True, spacing=0.5)


def arrow(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    *,
    stroke: str = FLOW,
    width: float = 2.6,
    marker: str = "flow",
    dash: str | None = None,
    label: str | None = None,
    label_dy: float = -10,
    label_fill: str = ACCENT_TAG,
) -> str:
    out = [line(x1, y1, x2, y2, stroke=stroke, width=width, marker=marker, dash=dash)]
    if label:
        out.append(flow_label((x1 + x2) / 2, (y1 + y2) / 2 + label_dy, label, fill=label_fill))
    return "\n".join(out)


def _unit(dx: float, dy: float) -> tuple[float, float]:
    length = (dx**2 + dy**2) ** 0.5 or 1
    return dx / length, dy / length


def _dist(x1: float, y1: float, x2: float, y2: float) -> float:
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def elbow(
    points: list[tuple[float, float]],
    *,
    stroke: str = FLOW,
    width: float = 2.6,
    marker: str = "flow",
    dash: str | None = None,
    radius: float = 12,
) -> str:
    """Orthogonal poly-line with rounded corners."""
    if len(points) < 2:
        return ""
    d = [f"M{_n(points[0][0])},{_n(points[0][1])}"]
    for index in range(1, len(points) - 1):
        px, py = points[index - 1]
        cx, cy = points[index]
        nx, ny = points[index + 1]
        in_dx, in_dy = _unit(cx - px, cy - py)
        out_dx, out_dy = _unit(nx - cx, ny - cy)
        r = min(radius, _dist(px, py, cx, cy) / 2, _dist(cx, cy, nx, ny) / 2)
        d.append(f"L{_n(cx - in_dx * r)},{_n(cy - in_dy * r)}")
        d.append(f"Q{_n(cx)},{_n(cy)} {_n(cx + out_dx * r)},{_n(cy + out_dy * r)}")
    d.append(f"L{_n(points[-1][0])},{_n(points[-1][1])}")
    return path(" ".join(d), stroke=stroke, width=width, marker=marker, dash=dash)


def divider(x1: float, x2: float, y: float, *, label: str | None = None) -> str:
    out = [line(x1, y, x2, y, stroke="#1b2942", width=1, dash="4 6")]
    if label:
        out.append(text(x1, y - 8, label.upper(), size=10, fill=MUTED, mono=True, spacing=1.8, weight="700"))
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Canvas
# ---------------------------------------------------------------------------

_DEFS = """  <defs>
    <marker id="flow" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
      <path d="M0,0.6 L10,5 L0,9.4 z" fill="#f43f5e"/>
    </marker>
    <marker id="flowSoft" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0.6 L10,5 L0,9.4 z" fill="#64748b"/>
    </marker>
    <marker id="flowGreen" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
      <path d="M0,0.6 L10,5 L0,9.4 z" fill="#22c55e"/>
    </marker>
    <marker id="flowAmber" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
      <path d="M0,0.6 L10,5 L0,9.4 z" fill="#f59e0b"/>
    </marker>
    <marker id="flowCyan" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
      <path d="M0,0.6 L10,5 L0,9.4 z" fill="#22d3ee"/>
    </marker>
    <marker id="flowPurple" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
      <path d="M0,0.6 L10,5 L0,9.4 z" fill="#a855f7"/>
    </marker>
    <marker id="flowBlue" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
      <path d="M0,0.6 L10,5 L0,9.4 z" fill="#3b82f6"/>
    </marker>
    <marker id="flowRed" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
      <path d="M0,0.6 L10,5 L0,9.4 z" fill="#ef4444"/>
    </marker>
    <filter id="neon" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="blur"/>
      </feMerge>
    </filter>
    <linearGradient id="pageWash" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#0e1728"/>
      <stop offset="100%" stop-color="#070b14"/>
    </linearGradient>
  </defs>"""


class Diagram:
    """Collects SVG fragments and renders the framed, titled page."""

    def __init__(
        self,
        width: float,
        height: float,
        *,
        eyebrow: str,
        title: str,
        subtitle: str = "",
        margin: float = 22,
    ) -> None:
        self.width = width
        self.height = height
        self.eyebrow = eyebrow
        self.title = title
        self.subtitle = subtitle
        self.margin = margin
        self.body: list[str] = []
        self.content_left = margin + 26
        self.content_right = width - margin - 26
        self.content_width = self.content_right - self.content_left
        self.center = width / 2

    def add(self, *fragments: str) -> "Diagram":
        for fragment in fragments:
            if fragment:
                self.body.append(fragment)
        return self

    def render(self) -> str:
        m = self.margin
        head = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {_n(self.width)} {_n(self.height)}" '
            f'width="{_n(self.width)}" height="{_n(self.height)}" role="img" '
            f'aria-label="{escape(self.title)}">',
            _DEFS,
            rect(0, 0, self.width, self.height, rx=0, fill=PAGE_BG),
            rect(
                m,
                m,
                self.width - m * 2,
                self.height - m * 2,
                rx=16,
                fill="url(#pageWash)",
                stroke=FRAME_STROKE,
                width=1.4,
            ),
            text(
                self.center,
                m + 30,
                self.eyebrow.upper(),
                size=11,
                fill=EYEBROW,
                weight="700",
                anchor="middle",
                mono=True,
                spacing=3.2,
            ),
            text(self.center, m + 62, self.title, size=25, fill=TITLE, weight="700", anchor="middle"),
        ]
        if self.subtitle:
            head.append(text(self.center, m + 86, self.subtitle, size=12.5, fill=SUBTITLE, anchor="middle"))
        return "\n".join(head + self.body + ["</svg>", ""])
