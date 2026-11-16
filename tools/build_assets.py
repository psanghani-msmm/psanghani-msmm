#!/usr/bin/env python3
"""Build the SVG artwork for the profile README.

Run from the repository root:  python3 tools/build_assets.py
Writes assets/avatar.svg, assets/hero.svg and assets/pipeline.svg.
The cartoon character is defined once (CHARACTER) and reused by the avatar
and the animated hero banner, so a tweak to the face lands in both.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

FONT = "ui-sans-serif,-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"

# Palette for the character
SKIN = "#e8b088"
SKIN_SHADOW = "#c98b64"
HAIR = "#1f1a1a"
HOODIE = "#c40b0b"        # MSMM red, a shade darker for the fabric
HOODIE_LIGHT = "#e10d0d"  # MSMM primary red
INK = "#1a1a1a"

# MSMM Engineering brand (from msmmeng.com: --primary, --secondary and friends)
RED = "#e10d0d"
RED_DARK = "#b80a0a"
RED_LIGHT = "#ff3333"
NAVY = "#1e3a5f"
NAVY_DARK = "#142a45"
NAVY_DEEP = "#0d1b2e"
NAVY_LIGHT = "#2a5080"
MIST = "#c9d6e8"


def character(animated: bool) -> str:
    """Head-and-shoulders cartoon in a 512x512 box (no background).

    animated=True adds a blink and a waving arm (SMIL, works in <img>).
    """
    blink_white = blink_pupil = blink_spark = ""
    if animated:
        blink_white = ('<animate attributeName="ry" values="18;18;1;18" '
                       'keyTimes="0;0.92;0.95;1" dur="4.2s" repeatCount="indefinite"/>')
        blink_pupil = ('<animate attributeName="ry" values="8;8;0.5;8" '
                       'keyTimes="0;0.92;0.95;1" dur="4.2s" repeatCount="indefinite"/>')
        blink_spark = ('<animate attributeName="ry" values="3;3;0.2;3" '
                       'keyTimes="0;0.92;0.95;1" dur="4.2s" repeatCount="indefinite"/>')

    def eye(cx: int) -> str:
        return (
            f'<ellipse cx="{cx}" cy="232" rx="16" ry="18" fill="#fff">{blink_white}</ellipse>'
            f'<ellipse cx="{cx + 2}" cy="234" rx="8" ry="8" fill="{INK}">{blink_pupil}</ellipse>'
            f'<ellipse cx="{cx + 6}" cy="229" rx="3" ry="3" fill="#fff">{blink_spark}</ellipse>'
        )

    arm = ""
    if animated:
        arm = f'''
  <!-- waving arm, pivot at the shoulder -->
  <g transform="translate(392 446)">
    <g>
      <animateTransform attributeName="transform" type="rotate" values="-22;14;-22"
        dur="1.3s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1"/>
      <path d="M0 0 L48 -96" stroke="{HOODIE}" stroke-width="44" stroke-linecap="round" fill="none"/>
      <path d="M36 -72 L62 -124" stroke="{SKIN}" stroke-width="32" stroke-linecap="round" fill="none"/>
      <circle cx="70" cy="-142" r="30" fill="{SKIN}"/>
      <path d="M48 -156 q-16 -14 -6 -30" stroke="{SKIN}" stroke-width="16" stroke-linecap="round" fill="none"/>
      <path d="M60 -170 v-26 M74 -172 v-30 M88 -166 v-26" stroke="{SKIN}" stroke-width="14" stroke-linecap="round"/>
    </g>
  </g>'''

    return f'''
  <!-- hood ring -->
  <ellipse cx="256" cy="398" rx="78" ry="26" fill="{HOODIE_LIGHT}"/>
  <!-- neck -->
  <rect x="226" y="316" width="60" height="78" rx="22" fill="{SKIN_SHADOW}"/>
  <!-- body -->
  <path d="M92 512 C92 424 160 384 256 384 C352 384 420 424 420 512 Z" fill="{HOODIE}"/>
  <path d="M212 388 L256 446 L300 388" fill="{HOODIE_LIGHT}"/>
  <path d="M240 444 v44 M272 444 v44" stroke="#ffd6d6" stroke-width="5" stroke-linecap="round"/>
  {arm}
  <!-- ears -->
  <circle cx="162" cy="242" r="18" fill="{SKIN}"/>
  <circle cx="350" cy="242" r="18" fill="{SKIN}"/>
  <!-- head -->
  <ellipse cx="256" cy="232" rx="96" ry="104" fill="{SKIN}"/>
  <!-- hair -->
  <path d="M160 236 C154 136 200 100 256 100 C312 100 358 136 352 236 C342 194 322 170 298 168 C272 166 252 178 236 178 C210 178 182 194 160 236 Z" fill="{HAIR}"/>
  <path d="M226 110 C236 84 266 78 286 90 C268 92 250 100 242 114 Z" fill="{HAIR}"/>
  <!-- brows -->
  <path d="M194 198 q24 -14 48 -2" stroke="{HAIR}" stroke-width="7" fill="none" stroke-linecap="round"/>
  <path d="M270 196 q24 -12 48 2" stroke="{HAIR}" stroke-width="7" fill="none" stroke-linecap="round"/>
  <!-- eyes -->
  {eye(220)}
  {eye(292)}
  <!-- glasses -->
  <g fill="#fff" fill-opacity="0.06" stroke="{INK}" stroke-width="5">
    <circle cx="220" cy="232" r="27"/>
    <circle cx="292" cy="232" r="27"/>
  </g>
  <path d="M247 230 h18 M193 228 h-26 M319 228 h26" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
  <!-- nose and mouth -->
  <path d="M256 242 q-9 18 4 24" stroke="{SKIN_SHADOW}" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M226 284 q30 28 60 0" stroke="#9a3b2e" stroke-width="6" fill="none" stroke-linecap="round"/>
  <path d="M236 288 q20 14 40 0 z" fill="#fff"/>
  <!-- cheeks -->
  <circle cx="186" cy="266" r="12" fill="#f5a3a3" opacity="0.55"/>
  <circle cx="326" cy="266" r="12" fill="#f5a3a3" opacity="0.55"/>
'''


def avatar() -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{NAVY_LIGHT}"/>
    <stop offset="0.55" stop-color="{NAVY}"/>
    <stop offset="1" stop-color="{NAVY_DARK}"/>
  </linearGradient>
  <clipPath id="frame"><rect width="512" height="512" rx="112"/></clipPath>
</defs>
<g clip-path="url(#frame)">
  <rect width="512" height="512" fill="url(#bg)"/>
  <circle cx="96" cy="90" r="120" fill="#fff" opacity="0.07"/>
  <circle cx="440" cy="420" r="170" fill="{RED}" opacity="0.22"/>
  <ellipse cx="256" cy="256" rx="300" ry="78" transform="rotate(-24 256 256)" fill="none" stroke="#fff" stroke-opacity="0.12" stroke-width="10"/>
  {character(animated=False)}
</g>
</svg>
'''


def msmm_mark(size: float) -> str:
    """The MSMM globe-and-skyline mark, drawn as vectors (after the site's favicon)."""
    bars = [(13, 45), (16.8, 39), (20.6, 43), (24.4, 33), (28.2, 40), (32, 24),
            (35.8, 29), (39.6, 35), (43.4, 40), (47.2, 43)]
    rects = "".join(f'<rect x="{x}" y="{y}" width="3" height="{61 - y}" fill="#fff"/>' for x, y in bars)
    k = size / 64
    return f'''<g transform="scale({k})">
      <ellipse cx="32" cy="32" rx="30" ry="8" transform="rotate(28 32 32)" fill="none" stroke="#fff" stroke-width="3.5"/>
      <circle cx="32" cy="32" r="24" fill="{RED}" stroke="#fff" stroke-width="2.5"/>
      <g clip-path="url(#markclip)">{rects}</g>
      <path d="M 9 25.4 A 30 8 28 0 1 50.4 47.4" fill="none" stroke="#fff" stroke-width="3.5"/>
    </g>'''


def hero() -> str:
    # Skyline bars along the bottom right, rising one after another (echoes the logo)
    bars = []
    heights = [60, 110, 80, 150, 100, 190, 160, 120, 90, 140, 70, 110, 50]
    x = 700
    for i, h in enumerate(heights):
        bars.append(f'''
    <rect x="{x}" y="400" width="26" height="{h}" fill="#fff" fill-opacity="0.07">
      <animate attributeName="y" values="400;{400 - h}" dur="1.2s" begin="{0.08 * i:.2f}s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
    </rect>''')
        x += 38

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="1200" height="400" font-family="{FONT}">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{NAVY_DEEP}"/>
    <stop offset="0.55" stop-color="{NAVY_DARK}"/>
    <stop offset="1" stop-color="{NAVY}"/>
  </linearGradient>
  <radialGradient id="glow">
    <stop offset="0" stop-color="{RED}" stop-opacity="0.45"/>
    <stop offset="1" stop-color="{RED}" stop-opacity="0"/>
  </radialGradient>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0H0V40" fill="none" stroke="#fff" stroke-opacity="0.05"/>
  </pattern>
  <clipPath id="frame"><rect width="1200" height="400" rx="28"/></clipPath>
  <clipPath id="markclip"><circle cx="32" cy="32" r="22.5"/></clipPath>
</defs>
<g clip-path="url(#frame)">
  <rect width="1200" height="400" fill="url(#bg)"/>
  <rect width="1200" height="400" fill="url(#grid)"/>
  <circle cx="1040" cy="40" r="300" fill="url(#glow)">
    <animateTransform attributeName="transform" type="translate" values="0 0;-40 30;0 0" dur="10s" repeatCount="indefinite"/>
  </circle>
  <!-- orbit ring, like the logo's -->
  <ellipse cx="600" cy="420" rx="760" ry="150" fill="none" stroke="#fff" stroke-opacity="0.08" stroke-width="3" transform="rotate(-8 600 420)"/>
  {"".join(bars)}

  <!-- character -->
  <g transform="translate(62 83) scale(0.62)">
    <g>
      <animateTransform attributeName="transform" type="translate" values="0 0;0 -6;0 0" dur="3.4s" repeatCount="indefinite"/>
      {character(animated=True)}
    </g>
  </g>

  <!-- copy -->
  <text x="430" y="172" font-size="60" font-weight="800" fill="#ffffff">Parixit Sanghani</text>
  <rect x="432" y="190" height="6" rx="3" width="0" fill="{RED}">
    <animate attributeName="width" values="0;120" dur="1.2s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
  </rect>
  <text x="432" y="244" font-size="32" font-weight="600" fill="{MIST}" letter-spacing="2" opacity="0">AI Developer
    <animate attributeName="opacity" values="0;1" begin="0.5s" dur="0.9s" fill="freeze"/>
  </text>

  <!-- company mark -->
  <g transform="translate(1004 300)">{msmm_mark(56)}</g>
  <text x="1072" y="324" font-size="17" font-weight="700" fill="#fff">MSMM</text>
  <text x="1072" y="344" font-size="13" fill="{MIST}">Engineering, LLC</text>
</g>
</svg>
'''


def pipeline() -> str:
    nodes = [
        ("Ingest", ["Crawl, hash, dedupe", "S3, SharePoint, folders"]),
        ("Parse", ["OCR for clean text", "vision model for drawings"]),
        ("Index", ["Postgres + Qdrant", "OpenSearch + Neo4j"]),
        ("Reason", ["Search, check, search again", "LangGraph agent, any model"]),
        ("Deliver", ["Cited answer, or an action", "a person approves first"]),
    ]
    w, h, gap, x0, y0 = 196, 124, 44, 20, 86
    parts = []
    for i, (title, lines) in enumerate(nodes):
        x = x0 + i * (w + gap)
        parts.append(f'''
  <g transform="translate({x} {y0})">
    <rect width="{w}" height="{h}" rx="18" fill="#fff" fill-opacity="0.06" stroke="url(#accent)" stroke-opacity="0.8" stroke-width="1.5"/>
    <circle cx="26" cy="28" r="9" fill="url(#accent)">
      <animate attributeName="r" values="9;11;9" dur="2.4s" begin="{i * 0.3:.1f}s" repeatCount="indefinite"/>
    </circle>
    <text x="44" y="34" font-size="20" font-weight="800" fill="#fff">{title}</text>
    <text x="20" y="72" font-size="13.5" fill="{MIST}">{lines[0]}</text>
    <text x="20" y="94" font-size="13.5" fill="{MIST}">{lines[1]}</text>
  </g>''')
        if i < len(nodes) - 1:
            x1, x2, yc = x + w, x + w + gap, y0 + h / 2
            parts.append(f'''
  <path d="M{x1} {yc} H{x2}" stroke="#fff" stroke-opacity="0.25" stroke-width="2" stroke-dasharray="4 6"/>
  <circle r="4.5" fill="{RED_LIGHT}">
    <animateMotion dur="1.6s" begin="{i * 0.4:.1f}s" repeatCount="indefinite" path="M{x1} {yc} H{x2}"/>
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.15;0.85;1" dur="1.6s" begin="{i * 0.4:.1f}s" repeatCount="indefinite"/>
  </circle>''')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 250" width="1200" height="250" font-family="{FONT}">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{NAVY_DEEP}"/>
    <stop offset="1" stop-color="{NAVY}"/>
  </linearGradient>
  <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{RED_LIGHT}"/>
    <stop offset="1" stop-color="{RED}"/>
  </linearGradient>
  <clipPath id="frame"><rect width="1200" height="250" rx="24"/></clipPath>
</defs>
<g clip-path="url(#frame)">
  <rect width="1200" height="250" fill="url(#bg)"/>
  <text x="600" y="48" text-anchor="middle" font-size="22" font-weight="700" fill="#ffffff">From a folder of PDFs and drawings to an answer you can trust</text>
  {"".join(parts)}
  <text x="600" y="238" text-anchor="middle" font-size="13" fill="#8fa6c4">Every step is idempotent, traced with OpenTelemetry, and runs inside the customer's own cloud account.</text>
</g>
</svg>
'''


if __name__ == "__main__":
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "avatar.svg").write_text(avatar())
    (ASSETS / "hero.svg").write_text(hero())
    (ASSETS / "pipeline.svg").write_text(pipeline())
    print("wrote", *[p.name for p in sorted(ASSETS.glob("*.svg"))])
