#!/usr/bin/env python3
"""Generate the Call-of-Duty "Operator Dossier" SVG banner set for the README.

Self-contained SVGs (no external fonts/scripts) so GitHub renders them
reliably. Tactical military-HUD aesthetic: night-vision green + tactical
orange on near-black, corner reticle brackets, scanlines, classified stamp.
"""

from pathlib import Path

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

# --- Tactical palette -------------------------------------------------------
BG = "#0a0f0a"       # near-black field
PANEL = "#0c120c"    # section panel
BORDER = "#1f3d24"   # dark mil-green edge
GRID = "#12301a"     # faint grid/scanline
TEXT = "#b7c9b0"     # body
DIM = "#5f7a5a"      # muted labels
HEAD = "#e9fbe4"     # bright headings
ORANGE = "#ff8c1a"   # tactical orange
NV = "#7CFC00"       # night-vision green
RED = "#ff3b30"      # REC / alert
MONO = "ui-monospace, 'SF Mono', SFMono-Regular, Menlo, Consolas, monospace"


def defs() -> str:
    return f"""
  <linearGradient id="accent" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{ORANGE}"/>
    <stop offset="1" stop-color="{NV}"/>
  </linearGradient>
  <linearGradient id="ghead" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{NV}"/>
    <stop offset="1" stop-color="{ORANGE}"/>
  </linearGradient>
  <pattern id="scan" width="3" height="3" patternUnits="userSpaceOnUse">
    <rect width="3" height="1" fill="{GRID}" opacity="0.35"/>
  </pattern>
  <radialGradient id="vig" cx="0.2" cy="0" r="1.1">
    <stop offset="0" stop-color="{NV}" stop-opacity="0.10"/>
    <stop offset="0.6" stop-color="{ORANGE}" stop-opacity="0.03"/>
    <stop offset="1" stop-color="{BG}" stop-opacity="0"/>
  </radialGradient>"""


def corners(w: int, h: int, inset: int = 14, ln: int = 20, col: str = ORANGE) -> str:
    """Four L-shaped HUD reticle brackets."""
    x0, y0, x1, y1 = inset, inset, w - inset, h - inset
    p = (
        f'M{x0} {y0+ln} L{x0} {y0} L{x0+ln} {y0} '
        f'M{x1-ln} {y0} L{x1} {y0} L{x1} {y0+ln} '
        f'M{x1} {y1-ln} L{x1} {y1} L{x1-ln} {y1} '
        f'M{x0+ln} {y1} L{x0} {y1} L{x0} {y1-ln}'
    )
    return f'<path d="{p}" fill="none" stroke="{col}" stroke-width="2"/>'


def reticle(cx: int, cy: int, r: int = 26) -> str:
    return (
        f'<g stroke="{NV}" stroke-width="1.5" fill="none" opacity="0.85">'
        f'<circle cx="{cx}" cy="{cy}" r="{r}"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r-9}" opacity="0.5"/>'
        f'<line x1="{cx-r-6}" y1="{cy}" x2="{cx-r+8}" y2="{cy}"/>'
        f'<line x1="{cx+r-8}" y1="{cy}" x2="{cx+r+6}" y2="{cy}"/>'
        f'<line x1="{cx}" y1="{cy-r-6}" x2="{cx}" y2="{cy-r+8}"/>'
        f'<line x1="{cx}" y1="{cy+r-8}" x2="{cx}" y2="{cy+r+6}"/>'
        f'</g><circle cx="{cx}" cy="{cy}" r="2" fill="{ORANGE}"/>'
    )


def prestige(x: int, y: int, filled: int = 8, total: int = 10, seg_w: int = 26) -> str:
    out = []
    for i in range(total):
        col = ORANGE if i < filled else "#20301e"
        out.append(
            f'<rect x="{x + i*(seg_w+4)}" y="{y}" width="{seg_w}" height="9" '
            f'rx="1" fill="{col}"/>'
        )
    return "".join(out)


def hero() -> str:
    W, H = 900, 330
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Operator Dossier — Pradeep Maddi, Cloud Platform Engineer and FinOps">
  <defs>{defs()}</defs>
  <rect width="{W}" height="{H}" rx="14" fill="{BG}"/>
  <rect width="{W}" height="{H}" rx="14" fill="url(#vig)"/>
  <rect width="{W}" height="{H}" rx="14" fill="url(#scan)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="13.5" fill="none" stroke="{BORDER}"/>
  {corners(W, H)}
  {reticle(812, 150, 30)}

  <!-- REC + timecode -->
  <circle cx="42" cy="40" r="5" fill="{RED}"/>
  <text x="56" y="45" font-family="{MONO}" font-size="13" font-weight="700" fill="{RED}">REC</text>
  <text x="94" y="45" font-family="{MONO}" font-size="12.5" fill="{DIM}">00:00:07:12   ·   FEED 04</text>

  <!-- CLASSIFIED stamp -->
  <g transform="translate(690 24)">
    <rect x="0" y="0" width="168" height="30" rx="3" fill="none" stroke="{ORANGE}" stroke-width="1.5"/>
    <text x="84" y="20" text-anchor="middle" font-family="{MONO}" font-size="12.5" font-weight="700" letter-spacing="2" fill="{ORANGE}">TS // SCI  CLASSIFIED</text>
  </g>

  <!-- accent bar + identity -->
  <rect x="40" y="86" width="6" height="176" rx="3" fill="url(#accent)"/>
  <text x="70" y="106" font-family="{MONO}" font-size="13" letter-spacing="3" fill="{NV}">OPERATOR DOSSIER  //  OPSEC LEVEL 5</text>
  <text x="68" y="164" font-family="{MONO}" font-size="52" font-weight="700" fill="{HEAD}">PRADEEP MADDI</text>
  <text x="70" y="198" font-family="{MONO}" font-size="19" font-weight="700" fill="{ORANGE}">PLATFORM ENGINEER  //  FINOPS OPERATOR</text>

  <!-- data readout -->
  <text x="70" y="234" font-family="{MONO}" font-size="13.5" fill="{TEXT}"><tspan fill="{DIM}">CALLSIGN &#8250; </tspan>CLOUDOPS<tspan fill="{DIM}">    THEATER &#8250; </tspan>150+ ACCOUNT AWS ORG</text>
  <text x="70" y="256" font-family="{MONO}" font-size="13.5" fill="{TEXT}"><tspan fill="{DIM}">STATUS &#8250; </tspan>DEPLOYED · FAIL-CLOSED<tspan fill="{DIM}">    CLEARANCE &#8250; </tspan>ADMIN</text>

  <!-- prestige + grid -->
  <text x="70" y="298" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{DIM}">PRESTIGE</text>
  {prestige(150, 289)}
  <text x="{W-30}" y="298" text-anchor="end" font-family="{MONO}" font-size="12" fill="{DIM}">GRID 51.04&#176;N 114.07&#176;W · YYC</text>
</svg>"""


def section(num: str, title: str, sub: str) -> str:
    esc = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    num, title, sub = esc(num), esc(title), esc(sub)
    W, H = 900, 64
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{num} {title}">
  <defs>{defs()}</defs>
  <rect width="{W}" height="{H}" rx="10" fill="{PANEL}"/>
  <rect width="{W}" height="{H}" rx="10" fill="url(#scan)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="9.5" fill="none" stroke="{BORDER}"/>
  {corners(W, H, inset=10, ln=13, col=NV)}
  <path d="M24 20 L36 32 L24 44" fill="none" stroke="{ORANGE}" stroke-width="2.5"/>
  <text x="52" y="40" font-family="{MONO}" font-size="20" font-weight="700" fill="{NV}">{num}</text>
  <text x="98" y="40" font-family="{MONO}" font-size="12" fill="{DIM}">//</text>
  <text x="122" y="40" font-family="{MONO}" font-size="21" font-weight="700" letter-spacing="1" fill="{HEAD}">{title}</text>
  <text x="{W-26}" y="39" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="{ORANGE}">[ {sub} ]</text>
</svg>"""


def footer() -> str:
    W, H = 900, 92
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Signal out — open to Principal and Senior Cloud Platform Engineering roles">
  <defs>{defs()}</defs>
  <rect width="{W}" height="{H}" rx="10" fill="{BG}"/>
  <rect width="{W}" height="{H}" rx="10" fill="url(#scan)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="9.5" fill="none" stroke="{BORDER}"/>
  {corners(W, H, inset=10, ln=15, col=ORANGE)}
  {reticle(W//2, 40, 15)}
  <text x="{W//2}" y="74" text-anchor="middle" font-family="{MONO}" font-size="13" letter-spacing="1.5" fill="{DIM}"><tspan fill="{NV}">// SIGNAL OUT &#183; </tspan>OPEN TO PRINCIPAL / SENIOR CLOUD PLATFORM &#183; AWS &#183; FINOPS</text>
</svg>"""


assets = {
    "hero.svg": hero(),
    "h-about.svg": section("01", "MISSION BRIEFING", "whoami"),
    "h-impact.svg": section("02", "THEATER OF OPS", "scope & impact"),
    "h-projects.svg": section("03", "OPERATIONS LOG", "selected work"),
    "h-stack.svg": section("04", "LOADOUT", "tech stack"),
    "h-certs.svg": section("05", "DOG TAGS", "credentials"),
    "h-writing.svg": section("06", "INTEL", "field notes"),
    "h-contact.svg": section("07", "EXFIL", "contact"),
    "footer.svg": footer(),
}

for name, svg in assets.items():
    (OUT / name).write_text(svg)
    print(f"wrote assets/{name}")
