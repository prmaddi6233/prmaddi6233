#!/usr/bin/env python3
"""Generate the "Living Architecture" animated-SVG banner set for the README.

Self-contained SVGs with SMIL animation (no JS, no external services) so they
animate reliably when GitHub embeds them as images. The hero renders Pradeep as
the control plane at the center of a topology of the systems he runs, with data
packets flowing the wires, pulsing nodes, and a radar ping from the core.
"""

import math
from pathlib import Path

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

# --- Palette (deep-space cloud topology) -----------------------------------
BG = "#0a0e1a"
PANEL = "#0e1426"
EDGE = "#20304f"
NODE = "#101a30"
NODE_BD = "#2b4a78"
TEXT = "#aeb9d4"
DIM = "#5f6f92"
HEAD = "#f2f6ff"
CYAN = "#22d3ee"
VIOLET = "#a78bfa"
TEAL = "#2dd4bf"
PKT = "#7dd3fc"
MONO = "ui-monospace, 'SF Mono', SFMono-Regular, Menlo, Consolas, monospace"


def common_defs() -> str:
    return f"""
    <linearGradient id="core" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{CYAN}"/>
      <stop offset="0.5" stop-color="{VIOLET}"/>
      <stop offset="1" stop-color="{TEAL}"/>
    </linearGradient>
    <linearGradient id="wire" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{CYAN}"/>
      <stop offset="1" stop-color="{VIOLET}"/>
    </linearGradient>
    <radialGradient id="halo" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="{VIOLET}" stop-opacity="0.22"/>
      <stop offset="1" stop-color="{BG}" stop-opacity="0"/>
    </radialGradient>
    <filter id="glow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="2.4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M30 0 L0 0 0 30" fill="none" stroke="#111a30" stroke-width="1"/>
    </pattern>"""


def node(cx: float, cy: float, title: str, sub: str, delay: float, accent: str) -> str:
    w, h = 168, 50
    x, y = cx - w / 2, cy - h / 2
    return f"""
  <g>
    <rect x="{x:.0f}" y="{y:.0f}" width="{w}" height="{h}" rx="10" fill="{NODE}" stroke="{NODE_BD}"/>
    <circle cx="{x+16:.0f}" cy="{cy:.0f}" r="4" fill="{accent}" filter="url(#glow)">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="2.6s" begin="{delay}s" repeatCount="indefinite"/>
    </circle>
    <text x="{x+30:.0f}" y="{cy-3:.0f}" font-family="{MONO}" font-size="13" font-weight="700" fill="{HEAD}">{title}</text>
    <text x="{x+30:.0f}" y="{cy+13:.0f}" font-family="{MONO}" font-size="10.5" fill="{DIM}">{sub}</text>
  </g>"""


def wire(x1: float, y1: float, x2: float, y2: float, delay: float) -> str:
    # trim the endpoint back toward centre so packets die at the node edge
    ang = math.atan2(y2 - y1, x2 - x1)
    ex, ey = x2 - 86 * math.cos(ang), y2 - 26 * math.sin(ang)
    path = f"M{x1:.0f} {y1:.0f} L{ex:.0f} {ey:.0f}"
    return f"""
  <path d="{path}" fill="none" stroke="{EDGE}" stroke-width="1.4"
        stroke-dasharray="3 7">
    <animate attributeName="stroke-dashoffset" from="0" to="-40" dur="1.6s" repeatCount="indefinite"/>
  </path>
  <circle r="3.2" fill="{PKT}" filter="url(#glow)">
    <animateMotion dur="2.4s" begin="{delay}s" repeatCount="indefinite" path="{path}"/>
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.1;0.85;1" dur="2.4s" begin="{delay}s" repeatCount="indefinite"/>
  </circle>"""


def hero() -> str:
    W, H = 900, 430
    cx, cy = 450, 210
    rx, ry = 300, 150
    nodes = [
        (90,  "PLATFORM @ SCALE", "150+ AWS accounts",     CYAN),
        (150, "GOVERNANCE",       "Control Tower · AFT",   VIOLET),
        (210, "IaC / AUTOMATION", "Terraform · Spacelift", TEAL),
        (330, "SECURITY POSTURE", "detect · enforce · audit", CYAN),
        (270, "COST GOVERNANCE",  "FinOps · FOCUS 1.2",    VIOLET),
        (30,  "K8s PLATFORM",     "multi-tenant EKS",      TEAL),
    ]
    pts = [(a, cx + rx * math.cos(math.radians(a)), cy - ry * math.sin(math.radians(a)),
            t, s, c) for a, t, s, c in nodes]

    wires = "".join(wire(cx, cy, x, y, i * 0.35) for i, (_, x, y, *_ ) in enumerate(pts))
    boxes = "".join(node(x, y, t, s, i * 0.4, c) for i, (_, x, y, t, s, c) in enumerate(pts))

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Pradeep Maddi — the control plane at the centre of a cloud platform topology">
  <defs>{common_defs()}</defs>
  <rect width="{W}" height="{H}" rx="16" fill="{BG}"/>
  <rect width="{W}" height="{H}" rx="16" fill="url(#grid)"/>
  <rect x="{cx-260}" y="{cy-160}" width="520" height="320" fill="url(#halo)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="15.5" fill="none" stroke="{EDGE}"/>

  {wires}

  <!-- radar ping from the core (starts wider than the card so it never crosses the text) -->
  <circle cx="{cx}" cy="{cy}" r="70" fill="none" stroke="{CYAN}" stroke-width="1.5">
    <animate attributeName="r" values="70;158" dur="3.4s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.5;0" dur="3.4s" repeatCount="indefinite"/>
  </circle>

  {boxes}

  <!-- control-plane core -->
  <g>
    <rect x="{cx-168}" y="{cy-46}" width="336" height="92" rx="16" fill="{PANEL}" stroke="url(#core)" stroke-width="2"/>
    <circle cx="{cx-140}" cy="{cy-22}" r="3.5" fill="{CYAN}"/>
    <text x="{cx}" y="{cy-8}" text-anchor="middle" font-family="{MONO}" font-size="27" font-weight="700" fill="{HEAD}">PRADEEP MADDI</text>
    <text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="{MONO}" font-size="12.5" letter-spacing="1.2" fill="url(#core)">CLOUD PLATFORM ENGINEER · FINOPS</text>
  </g>

  <text x="30" y="{H-22}" font-family="{MONO}" font-size="12" fill="{DIM}">// control plane · 150+ account AWS Organization</text>
  <text x="{W-30}" y="{H-22}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{DIM}">fail-closed by design</text>
</svg>"""


def section(num: str, title: str, sub: str) -> str:
    esc = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    num, title, sub = esc(num), esc(title), esc(sub)
    W, H = 900, 56
    line_y = H // 2
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{num} {title}">
  <defs>{common_defs()}</defs>
  <rect width="{W}" height="{H}" rx="10" fill="{PANEL}"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="9.5" fill="none" stroke="{EDGE}"/>
  <circle cx="26" cy="{line_y}" r="5" fill="{CYAN}" filter="url(#glow)">
    <animate attributeName="opacity" values="0.4;1;0.4" dur="2.4s" repeatCount="indefinite"/>
  </circle>
  <text x="46" y="{line_y+6}" font-family="{MONO}" font-size="18" font-weight="700" fill="url(#wire)">{num}</text>
  <text x="86" y="{line_y+6}" font-family="{MONO}" font-size="18" font-weight="700" letter-spacing="1" fill="{HEAD}">{title}</text>
  <path d="M{300} {line_y} L{W-150} {line_y}" stroke="{EDGE}" stroke-width="1.2" stroke-dasharray="3 7">
    <animate attributeName="stroke-dashoffset" from="0" to="-40" dur="1.6s" repeatCount="indefinite"/>
  </path>
  <circle r="2.6" fill="{PKT}" filter="url(#glow)">
    <animateMotion dur="2.6s" repeatCount="indefinite" path="M300 {line_y} L{W-150} {line_y}"/>
  </circle>
  <text x="{W-26}" y="{line_y+5}" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="{DIM}">{sub}</text>
</svg>"""


def manifest() -> str:
    """The operator.manifest card — replaces the plain YAML code block."""
    W, H = 900, 292
    kx, vx = 34, 150
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Operator manifest — role: Cloud Platform Engineer and FinOps; org: 150+ account AWS Organization; building cloud-finops-agent">
  <defs>{common_defs()}</defs>
  <rect width="{W}" height="{H}" rx="12" fill="{PANEL}"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="11.5" fill="none" stroke="{EDGE}"/>
  <!-- title bar -->
  <circle cx="26" cy="26" r="4.5" fill="{CYAN}"/>
  <circle cx="42" cy="26" r="4.5" fill="{VIOLET}"/>
  <circle cx="58" cy="26" r="4.5" fill="{TEAL}"/>
  <text x="80" y="30" font-family="{MONO}" font-size="12.5" letter-spacing="1" fill="{DIM}">operator.manifest &#183; control-plane spec</text>
  <line x1="0" y1="48" x2="{W}" y2="48" stroke="{EDGE}"/>

  <g font-family="{MONO}" font-size="15">
    <text x="{kx}" y="90"  fill="{CYAN}" font-weight="700">role</text>
    <text x="{vx}" y="90"  fill="{HEAD}">Cloud Platform Engineer &#183; FinOps</text>

    <text x="{kx}" y="120" fill="{CYAN}" font-weight="700">org</text>
    <text x="{vx}" y="120" fill="{HEAD}">150+ account AWS Organization</text>

    <text x="{kx}" y="150" fill="{CYAN}" font-weight="700">domains</text>
    <text x="{vx}" y="150" fill="{VIOLET}">[ <tspan fill="{TEXT}">platform engineering, FinOps, Kubernetes at scale, governance</tspan> ]</text>

    <text x="{kx}" y="180" fill="{CYAN}" font-weight="700">building</text>
    <text x="{vx}" y="180" fill="{TEAL}">cloud-finops-agent</text>
    <text x="{vx+186}" y="180" fill="{DIM}"># tiered, fail-closed cost validation</text>

    <text x="{kx}" y="216" fill="{CYAN}" font-weight="700">thesis</text>
    <text x="{vx}" y="216" fill="{VIOLET}">&#8250;</text>
    <text x="{vx+18}" y="216" fill="{TEXT}">Cost and security recommendations rot in backlogs because</text>
    <text x="{vx+18}" y="242" fill="{TEXT}">nobody proves they are safe to apply. I build the evidence</text>
    <text x="{vx+18}" y="268" fill="{TEXT}">layer that does.</text>
  </g>

  <circle r="2.6" fill="{PKT}" filter="url(#glow)">
    <animateMotion dur="3.2s" repeatCount="indefinite" path="M{W-30} 26 L30 26"/>
  </circle>
</svg>"""


def metrics() -> str:
    """Animated stat strip — big crisp numbers under the SCOPE header."""
    W, H = 900, 120
    cells = [
        ("150+",   "AWS accounts",     CYAN),
        ("$500K+", "identified / yr",  VIOLET),
        ("150",    "accounts guarded", TEAL),
        ("100%",   "IaC-managed",      CYAN),
    ]
    cw = W / len(cells)
    parts = []
    for i, (num, label, accent) in enumerate(cells):
        cx = cw * i + cw / 2
        if i:
            parts.append(f'<line x1="{cw*i:.0f}" y1="26" x2="{cw*i:.0f}" y2="{H-26}" stroke="{EDGE}"/>')
        parts.append(f"""
    <g>
      <circle cx="{cx:.0f}" cy="34" r="3.5" fill="{accent}" filter="url(#glow)">
        <animate attributeName="opacity" values="0.4;1;0.4" dur="2.6s" begin="{i*0.3:.2f}s" repeatCount="indefinite"/>
      </circle>
      <text x="{cx:.0f}" y="72" text-anchor="middle" font-family="{MONO}" font-size="38" font-weight="700" fill="url(#core)">{num}</text>
      <text x="{cx:.0f}" y="98" text-anchor="middle" font-family="{MONO}" font-size="12.5" letter-spacing="1" fill="{DIM}">{label}</text>
      <rect x="{cx-26:.0f}" y="108" width="52" height="2.5" rx="1" fill="{accent}" opacity="0.85">
        <animate attributeName="width" values="0;52" keyTimes="0;1" dur="0.9s" begin="{i*0.2+0.2:.2f}s" repeatCount="1" fill="freeze"/>
      </rect>
    </g>""")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Scope: 150+ AWS accounts · $500K+/yr identified savings · 150 accounts guarded · 100% IaC-managed">
  <defs>{common_defs()}</defs>
  <rect width="{W}" height="{H}" rx="12" fill="{PANEL}"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="11.5" fill="none" stroke="{EDGE}"/>
  {''.join(parts)}
</svg>"""


def footer() -> str:
    W, H = 900, 84
    cx = W // 2
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Open to Principal and Senior Cloud Platform Engineering roles">
  <defs>{common_defs()}</defs>
  <rect width="{W}" height="{H}" rx="10" fill="{BG}"/>
  <rect width="{W}" height="{H}" rx="10" fill="url(#grid)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="9.5" fill="none" stroke="{EDGE}"/>
  <circle cx="{cx}" cy="30" r="8" fill="none" stroke="{CYAN}" stroke-width="1.5">
    <animate attributeName="r" values="7;16" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.7;0" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="{cx}" cy="30" r="3" fill="url(#core)"/>
  <text x="{cx}" y="66" text-anchor="middle" font-family="{MONO}" font-size="13" letter-spacing="1.5" fill="{DIM}"><tspan fill="{CYAN}">// online · </tspan>OPEN TO PRINCIPAL / SENIOR CLOUD PLATFORM · AWS · FINOPS</text>
</svg>"""


assets = {
    "hero.svg": hero(),
    "metrics.svg": metrics(),
    "h-about.svg": section("01", "WHOAMI", "about"),
    "h-impact.svg": section("02", "SCOPE & IMPACT", "what I run"),
    "h-projects.svg": section("03", "SELECTED WORK", "open source"),
    "h-stack.svg": section("04", "TECH STACK", "toolchain"),
    "h-certs.svg": section("05", "CREDENTIALS", "verified"),
    "h-writing.svg": section("06", "FIELD NOTES", "writing"),
    "h-contact.svg": section("07", "ESTABLISH LINK", "contact"),
    "footer.svg": footer(),
}

for name, svg in assets.items():
    (OUT / name).write_text(svg)
    print(f"wrote assets/{name}")
