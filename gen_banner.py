#!/usr/bin/env python3
# Generates dark.svg and light.svg GitHub profile hero banners (pure SMIL, no JS)
import html
import os

_here = os.path.dirname(os.path.abspath(__file__))
ASCII_ART = open(os.path.join(_here, "ascii.txt"), encoding="utf-8").read().rstrip("\n").splitlines()

ROLES = ["Computer Engineering Student", "Systems & Low-Level Enthusiast", "Algorithms & Data Structures", "Cryptography Enthusiast", "Open Source Learner"]
INFO = [
    ("~/location", "Eindhoven, Netherlands"),
    ("~/focus", "Embedded systems - low-level programming - algorithms"),
    ("~/github", "github.com/mrbera88"),
    ("~/email", "berauzun173@gmail.com"),
]
SKILLS = ["Python", "Java", "C++", "C#", "SQL", "ARM Assembly", "Git", "Linux", "Data Structures & Algorithms", "RTL Design", "Cryptography"]

PAL = {
  "dark": dict(bg="#030712", panel="#0F172A", panel2="#0B1222", border="rgba(255,255,255,.08)",
               text="#F8FAFC", muted="#94A3B8", g1="#7C3AED", g2="#22D3EE", g3="#10B981",
               glow1="#22D3EE", glow2="#7C3AED", scan="rgba(34,211,238,.06)", pillfill="rgba(124,58,237,.10)"),
  "light": dict(bg="#FFFFFF", panel="#F8FAFC", panel2="#EEF2F7", border="rgba(15,23,42,.08)",
               text="#0F172A", muted="#475569", g1="#2563EB", g2="#06B6D4", g3="#10B981",
               glow1="#06B6D4", glow2="#2563EB", scan="rgba(37,99,235,.05)", pillfill="rgba(37,99,235,.07)"),
}

def gen(mode):
    p = PAL[mode]
    W, H = 1180, 610
    s = []
    A = s.append
    A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Bera Uzun - developer profile banner" font-family="\'JetBrains Mono\',\'Fira Code\',Consolas,monospace">')
    # defs
    A('<defs>')
    A(f'<linearGradient id="acc" x1="0%" y1="0%" x2="100%" y2="0%">'
      f'<stop offset="0%" stop-color="{p["g1"]}"/><stop offset="50%" stop-color="{p["g2"]}"/><stop offset="100%" stop-color="{p["g3"]}"/>'
      f'<animate attributeName="x1" values="0%;-60%;0%" dur="9s" repeatCount="indefinite"/>'
      f'<animate attributeName="x2" values="100%;160%;100%" dur="9s" repeatCount="indefinite"/></linearGradient>')
    A(f'<linearGradient id="ascg" x1="0%" y1="0%" x2="100%" y2="100%">'
      f'<stop offset="0%" stop-color="{p["g2"]}"><animate attributeName="stop-color" values="{p["g2"]};{p["g1"]};{p["g3"]};{p["g2"]}" dur="12s" repeatCount="indefinite"/></stop>'
      f'<stop offset="100%" stop-color="{p["g1"]}"><animate attributeName="stop-color" values="{p["g1"]};{p["g3"]};{p["g2"]};{p["g1"]}" dur="12s" repeatCount="indefinite"/></stop></linearGradient>')
    A(f'<linearGradient id="shimmer" x1="0%" y1="0%" x2="100%" y2="0%">'
      f'<stop offset="0%" stop-color="{p["g1"]}" stop-opacity="0"/><stop offset="50%" stop-color="{p["g2"]}" stop-opacity=".9"/><stop offset="100%" stop-color="{p["g3"]}" stop-opacity="0"/>'
      f'<animate attributeName="x1" values="-100%;100%" dur="4s" repeatCount="indefinite"/>'
      f'<animate attributeName="x2" values="0%;200%" dur="4s" repeatCount="indefinite"/></linearGradient>')
    A(f'<radialGradient id="glowA" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="{p["glow1"]}" stop-opacity=".{ "14" if mode=="dark" else "08"}"/><stop offset="100%" stop-color="{p["glow1"]}" stop-opacity="0"/></radialGradient>')
    A(f'<radialGradient id="glowB" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="{p["glow2"]}" stop-opacity=".{ "12" if mode=="dark" else "07"}"/><stop offset="100%" stop-color="{p["glow2"]}" stop-opacity="0"/></radialGradient>')
    A(f'<radialGradient id="glowC" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="{p["g3"]}" stop-opacity=".10"/><stop offset="100%" stop-color="{p["g3"]}" stop-opacity="0"/></radialGradient>')
    A('<filter id="soft" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="6"/></filter>')
    A('<filter id="tiny" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="1.2"/></filter>')
    A(f'<linearGradient id="glass" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fff" stop-opacity="{".05" if mode=="dark" else ".55"}"/><stop offset="18%" stop-color="#fff" stop-opacity="0"/></linearGradient>')
    # typing clips for roles
    role_w = [len(r)*8.6 for r in ROLES]
    cyc = 4 * len(ROLES)
    for i, w in enumerate(role_w):
        b = i*4
        A(f'<clipPath id="role{i}"><rect x="512" y="188" height="26" width="0">'
          f'<animate attributeName="width" dur="{cyc}s" repeatCount="indefinite" calcMode="linear" '
          f'keyTimes="0;{b/cyc:.4f};{(b+1.4)/cyc:.4f};{(b+3.1)/cyc:.4f};{(b+3.7)/cyc:.4f};1" '
          f'values="0;0;{w:.0f};{w:.0f};0;0"/></rect></clipPath>')
    A('</defs>')

    # background
    A(f'<rect width="{W}" height="{H}" rx="24" fill="{p["bg"]}"/>')
    A(f'<circle cx="200" cy="120" r="300" fill="url(#glowB)"><animateTransform attributeName="transform" type="translate" values="0 0;30 20;0 0" dur="14s" repeatCount="indefinite"/></circle>')
    A(f'<circle cx="980" cy="500" r="320" fill="url(#glowA)"><animateTransform attributeName="transform" type="translate" values="0 0;-25 -18;0 0" dur="17s" repeatCount="indefinite"/></circle>')
    A(f'<circle cx="620" cy="80" r="220" fill="url(#glowC)"><animateTransform attributeName="transform" type="translate" values="0 0;15 25;0 0" dur="12s" repeatCount="indefinite"/></circle>')
    # particles
    for (cx, cy, r, dur, dy) in [(140,520,2,9,-70),(330,90,1.6,12,60),(700,540,2.2,11,-80),(900,120,1.5,10,70),(1080,300,1.8,13,-60),(60,300,1.4,8,50)]:
        A(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{p["g2"]}" opacity=".35"><animateTransform attributeName="transform" type="translate" values="0 0;0 {dy};0 0" dur="{dur}s" repeatCount="indefinite"/><animate attributeName="opacity" values=".1;.5;.1" dur="{dur}s" repeatCount="indefinite"/></circle>')
    # outer border + shimmer
    A(f'<rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="23" fill="none" stroke="{p["border"]}" stroke-width="1.5"/>')
    A(f'<rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="23" fill="none" stroke="url(#shimmer)" stroke-width="1.5" opacity=".8"/>')

    # ===== LEFT PANEL (ASCII) =====
    A(f'<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -6;0 0" dur="7s" repeatCount="indefinite"/>')
    A(f'<rect x="32" y="32" width="404" height="546" rx="18" fill="{p["panel"]}" stroke="{p["border"]}"/>')
    A(f'<rect x="32" y="32" width="404" height="546" rx="18" fill="url(#glass)"/>')
    # window dots
    for i, c in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]):
        A(f'<circle cx="{56+i*22}" cy="56" r="6" fill="{c}" opacity=".9"/>')
    A(f'<text x="234" y="61" text-anchor="middle" font-size="12" fill="{p["muted"]}">bera@dev: ~/portrait</text>')
    # ascii lines
    y0 = 92
    lh = 13.9
    for i, line in enumerate(ASCII_ART):
        t = html.escape(line).replace(" ", "&#160;")
        A(f'<text x="46" y="{y0+i*lh:.0f}" font-size="10.2" xml:space="preserve" fill="url(#ascg)" filter="url(#tiny)" opacity="0">'
          f'<animate attributeName="opacity" values="0;1" dur=".18s" begin="{0.35+i*0.10:.2f}s" fill="freeze"/>{t}</text>')
    # scanline over portrait
    A(f'<rect x="34" y="34" width="400" height="26" fill="{p["scan"]}"><animateTransform attributeName="transform" type="translate" values="0 0;0 512;0 0" dur="6.5s" repeatCount="indefinite"/></rect>')
    # cursor under portrait
    A(f'<rect x="52" y="556" width="9" height="15" fill="{p["g2"]}"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>')
    A('</g>')

    # ===== RIGHT PANEL (terminal) =====
    A(f'<rect x="460" y="32" width="688" height="546" rx="18" fill="{p["panel"]}" stroke="{p["border"]}"/>')
    A(f'<rect x="460" y="32" width="688" height="546" rx="18" fill="url(#glass)"/>')
    for i, c in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]):
        A(f'<circle cx="{486+i*22}" cy="56" r="6" fill="{c}" opacity=".9"/>')
    A(f'<text x="804" y="61" text-anchor="middle" font-size="12" fill="{p["muted"]}">mrbera88 &#8212; zsh &#8212; 120x34</text>')

    def reveal(el, t):
        return el.replace("<text ", f'<text opacity="0" ', 1).replace("</text>",
            f'<animate attributeName="opacity" values="0;1" dur=".5s" begin="{t}s" fill="freeze"/></text>')

    A(reveal(f'<text x="492" y="112" font-size="15" fill="{p["muted"]}">$ whoami</text>', 0.4))
    A(reveal(f'<text x="492" y="152" font-size="34" font-weight="700" fill="{p["text"]}">Hi &#128075; I&#8217;m <tspan fill="url(#acc)">Bera Uzun</tspan></text>', 0.8))
    # typing roles
    A(f'<text x="492" y="207" font-size="17" fill="{p["muted"]}">&gt;</text>')
    for i, r in enumerate(ROLES):
        w = role_w[i]
        A(f'<g clip-path="url(#role{i})"><text x="512" y="208" font-size="17" fill="url(#acc)" font-weight="600" '
          f'textLength="{w:.0f}" lengthAdjust="spacingAndGlyphs">{html.escape(r)}</text></g>')
    kt_list, vals_list = [], []
    for i, w in enumerate(role_w):
        b = i * 4
        kt_list += [b/cyc, (b+1.4)/cyc, (b+3.1)/cyc, (b+3.7)/cyc]
        vals_list += ["0 0", f"{w:.0f} 0", f"{w:.0f} 0", "0 0"]
    kt_list.append(1.0)
    vals_list.append("0 0")
    kt = ";".join("0" if t == 0 else ("1" if t == 1 else f"{t:.4f}") for t in kt_list)
    vals = ";".join(vals_list)
    A(f'<rect x="512" y="193" width="9" height="19" fill="{p["g2"]}"><animate attributeName="opacity" values="1;0;1" dur=".9s" repeatCount="indefinite"/>'
      f'<animateTransform attributeName="transform" type="translate" dur="{cyc}s" repeatCount="indefinite" calcMode="linear" keyTimes="{kt}" values="{vals}"/></rect>')
    # info lines
    y = 258
    for i, (k, v) in enumerate(INFO):
        A(reveal(f'<text x="492" y="{y}" font-size="14.5"><tspan fill="{p["g2"]}">{k}</tspan><tspan fill="{p["muted"]}" dx="10">&#8594;</tspan><tspan fill="{p["text"]}" dx="10">{html.escape(v)}</tspan></text>', 1.4+i*0.35))
        y += 30
    # skills
    A(reveal(f'<text x="492" y="{y+18}" font-size="13" fill="{p["muted"]}" letter-spacing="2">SKILLS</text>', 3.0))
    px, py = 492, y+36
    t0 = 3.2
    for i, sk in enumerate(SKILLS):
        w = len(sk)*7.6 + 26
        if px + w > 1128:
            px = 492; py += 42
        A(f'<g opacity="0"><animate attributeName="opacity" values="0;1" dur=".4s" begin="{t0+i*0.12:.2f}s" fill="freeze"/>'
          f'<rect x="{px:.0f}" y="{py}" width="{w:.0f}" height="30" rx="15" fill="{p["pillfill"]}" stroke="url(#acc)" stroke-width="1">'
          f'<animate attributeName="stroke-width" values="1;1.6;1" dur="3s" begin="{i*0.4:.1f}s" repeatCount="indefinite"/></rect>'
          f'<text x="{px+w/2:.0f}" y="{py+20}" text-anchor="middle" font-size="13.5" fill="{p["text"]}">{html.escape(sk)}</text></g>')
        px += w + 12
    # socials
    sy = 552
    A(reveal(f'<text x="492" y="{sy}" font-size="14"><tspan fill="{p["muted"]}">$ connect --with</tspan>'
             f'<tspan dx="14" fill="url(#acc)" font-weight="600">GitHub</tspan><tspan dx="16" fill="{p["muted"]}">&#183;</tspan>'
             f'<tspan dx="16" fill="url(#acc)" font-weight="600">LinkedIn</tspan><tspan dx="16" fill="{p["muted"]}">&#183;</tspan>'
             f'<tspan dx="16" fill="url(#acc)" font-weight="600">X</tspan><tspan dx="16" fill="{p["muted"]}">&#183;</tspan>'
             f'<tspan dx="16" fill="url(#acc)" font-weight="600">Portfolio</tspan></text>', 5.0))
    A(f'<rect x="1116" y="{sy-13}" width="9" height="15" fill="{p["g2"]}"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>')
    A(f'<rect x="462" y="34" width="684" height="20" fill="{p["scan"]}"><animateTransform attributeName="transform" type="translate" values="0 0;0 520;0 0" dur="9s" repeatCount="indefinite"/></rect>')
    A('</svg>')
    return "".join(s)

for mode in ("dark", "light"):
    with open(os.path.join(_here, f"{mode}.svg"), "w", encoding="utf-8") as f:
        f.write(gen(mode))
    print(mode, "ok", len(ASCII_ART), "ascii lines")
