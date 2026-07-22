#!/usr/bin/env python3
"""Generate the SVG banner set for the profile README.

Self-contained SVGs (no external fonts/scripts, so GitHub renders them
reliably). Monospace type for the terminal-designed look; gradient accents
match the portfolio site (prmaddi6233.github.io).
"""

from pathlib import Path

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

# Palette (matches the portfolio site)
BG = "#0b1120"
PANEL = "#0f172a"
BORDER = "#24304d"
TEXT = "#cbd5e1"
DIM = "#8595b3"
HEAD = "#f1f5f9"
A1, A2, A3 = "#38bdf8", "#818cf8", "#2dd4bf"
MONO = "ui-monospace, 'SF Mono', SFMono-Regular, Menlo, Consolas, monospace"

GRAD = f"""
  <linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{A1}"/>
    <stop offset="0.55" stop-color="{A2}"/>
    <stop offset="1" stop-color="{A3}"/>
  </linearGradient>
  <linearGradient id="gv" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{A1}"/>
    <stop offset="1" stop-color="{A3}"/>
  </linearGradient>"""


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def hero() -> str:
    W, H = 900, 300
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Pradeep Maddi — Cloud Platform Engineer and FinOps">
  <defs>
    {GRAD}
    <radialGradient id="glow" cx="0.18" cy="0.0" r="0.9">
      <stop offset="0" stop-color="{A1}" stop-opacity="0.16"/>
      <stop offset="0.5" stop-color="{A2}" stop-opacity="0.06"/>
      <stop offset="1" stop-color="{BG}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow2" cx="0.95" cy="0.05" r="0.8">
      <stop offset="0" stop-color="{A3}" stop-opacity="0.12"/>
      <stop offset="1" stop-color="{BG}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="{W}" height="{H}" rx="18" fill="{BG}"/>
  <rect width="{W}" height="{H}" rx="18" fill="url(#glow)"/>
  <rect width="{W}" height="{H}" rx="18" fill="url(#glow2)"/>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="17.5" fill="none" stroke="{BORDER}"/>
  <rect x="40" y="52" width="6" height="196" rx="3" fill="url(#gv)"/>
  <text x="70" y="80" font-family="{MONO}" font-size="14" letter-spacing="3" fill="{A3}">CLOUD PLATFORM ENGINEER // FINOPS</text>
  <text x="68" y="150" font-family="{MONO}" font-size="58" font-weight="700" fill="{HEAD}">Pradeep Maddi</text>
  <text x="70" y="196" font-family="{MONO}" font-size="26" font-weight="700" fill="url(#g)">evidence-based cloud platforms</text>
  <text x="70" y="238" font-family="{MONO}" font-size="15" fill="{DIM}">150+ account AWS Organization  ·  Kubernetes at scale  ·  fail-closed by design</text>
  <circle cx="836" cy="58" r="4" fill="{A1}"/>
  <circle cx="852" cy="58" r="4" fill="{A2}"/>
  <circle cx="868" cy="58" r="4" fill="{A3}"/>
</svg>"""


def section(num: str, title: str, sub: str) -> str:
    W, H = 900, 66
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(num)} {esc(title)}">
  <defs>{GRAD}</defs>
  <rect width="{W}" height="{H}" rx="12" fill="{PANEL}"/>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="11.5" fill="none" stroke="{BORDER}"/>
  <rect x="0" y="0" width="5" height="{H}" rx="2" fill="url(#gv)"/>
  <text x="28" y="41" font-family="{MONO}" font-size="22" font-weight="700" fill="url(#g)">{esc(num)}</text>
  <text x="74" y="41" font-family="{MONO}" font-size="21" font-weight="700" fill="{HEAD}">{esc(title)}</text>
  <text x="{W - 28}" y="40" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="{DIM}">{esc(sub)}</text>
</svg>"""


def footer() -> str:
    W, H = 900, 90
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="footer">
  <defs>{GRAD}
    <radialGradient id="fg" cx="0.5" cy="1.2" r="0.9">
      <stop offset="0" stop-color="{A2}" stop-opacity="0.14"/>
      <stop offset="1" stop-color="{BG}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="{W}" height="{H}" rx="12" fill="{BG}"/>
  <rect width="{W}" height="{H}" rx="12" fill="url(#fg)"/>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="11.5" fill="none" stroke="{BORDER}"/>
  <rect x="{W / 2 - 60}" y="30" width="120" height="3" rx="1.5" fill="url(#g)"/>
  <text x="{W / 2}" y="58" text-anchor="middle" font-family="{MONO}" font-size="14" fill="{DIM}">Open to Senior / Principal Cloud Platform Engineering  ·  AWS  ·  FinOps</text>
</svg>"""


assets = {
    "hero.svg": hero(),
    "h-about.svg": section("01", "WHOAMI", "about"),
    "h-experience.svg": section("02", "CAREER LOG", "2017 → present"),
    "h-projects.svg": section("03", "SELECTED WORK", "open source"),
    "h-stack.svg": section("04", "TECH STACK", "tools of the trade"),
    "h-certs.svg": section("05", "CREDENTIALS", "verified"),
    "h-contact.svg": section("06", "ESTABLISH UPLINK", "get in touch"),
    "footer.svg": footer(),
}

for name, svg in assets.items():
    (OUT / name).write_text(svg)
    print(f"wrote assets/{name}")
