"""Premium artwork generators: silk, velvet, curtains, wax seals, detailed mandala,
perahera frieze, watercolor florals. All original, procedurally drawn."""
import random
from math import cos, sin, pi, radians
from orn import f, petal_d, svg_uri, ring


# ------------------------------------------------------------------ fabrics
def silk(cid, tint="#efe6d8", hi="#fffaf2", seed=7, freq="0.0028 0.009", rot=-24, scale=28, cls="silk"):
    """Satin drape: turbulence lit with diffuse + specular light, tinted."""
    return f'''<svg class="{cls}" viewBox="0 0 400 860" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
<defs><filter id="{cid}" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
<feTurbulence type="fractalNoise" baseFrequency="{freq}" numOctaves="2" seed="{seed}" result="n"/>
<feGaussianBlur in="n" stdDeviation="3" result="nb"/>
<feDiffuseLighting in="nb" surfaceScale="{scale}" diffuseConstant="1" lighting-color="{tint}" result="d"><feDistantLight azimuth="225" elevation="42"/></feDiffuseLighting>
<feSpecularLighting in="nb" surfaceScale="{scale}" specularConstant=".55" specularExponent="22" lighting-color="{hi}" result="s"><feDistantLight azimuth="225" elevation="50"/></feSpecularLighting>
<feComposite in="s" in2="d" operator="arithmetic" k2="1" k3="1"/></filter></defs>
<g transform="rotate({rot} 200 430) scale(1.9) translate(-105 -226)"><rect width="400" height="860" filter="url(#{cid})"/></g></svg>'''


def noise_uri(opacity=.18, freq=.9, size=160):
    return svg_uri(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency="{freq}" numOctaves="3" stitchTiles="stitch"/>'
        f'<feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 {opacity} 0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>')


def curtain_bg(base, dark, light, seed=3, total=620):
    """Irregular vertical folds as a CSS background value."""
    rnd = random.Random(seed)
    stops, x = [], 0
    while x < total:
        w = rnd.uniform(26, 58)
        stops += [f"{dark} {f(x)}px", f"{base} {f(x + w*.28)}px", f"{light} {f(x + w*.5)}px", f"{base} {f(x + w*.72)}px"]
        x += w
    stops.append(f"{dark} {f(x)}px")
    return f"repeating-linear-gradient(90deg,{','.join(stops)})"


# ------------------------------------------------------------------ seals
def wax_seal(cid, c1, c2, c3, text="", emblem="", ink="#00000055", seed=5, cls="wax"):
    rnd = random.Random(seed)
    pts = []
    n = 22
    for i in range(n):
        a = i / n * 2 * pi
        r = 46 + rnd.uniform(-2.5, 3.5) + (5 if rnd.random() < .18 else 0)
        pts.append((50 + r * cos(a), 50 + r * sin(a)))
    d = f"M{f((pts[-1][0]+pts[0][0])/2)} {f((pts[-1][1]+pts[0][1])/2)}"
    for i, p in enumerate(pts):
        q = pts[(i + 1) % n]
        d += f"Q{f(p[0])} {f(p[1])} {f((p[0]+q[0])/2)} {f((p[1]+q[1])/2)}"
    d += "Z"
    txt = ""
    if text:
        txt = (f'<text x="50" y="57" text-anchor="middle" font-size="21" font-family="Pinyon Script,Great Vibes,cursive" fill="#ffffff55" transform="translate(.7 .9)">{text}</text>'
               f'<text x="50" y="57" text-anchor="middle" font-size="21" font-family="Pinyon Script,Great Vibes,cursive" fill="{ink}">{text}</text>')
    return f'''<svg class="{cls}" viewBox="0 0 100 100" aria-hidden="true"><defs>
<radialGradient id="{cid}a" cx=".38" cy=".32" r=".75"><stop offset="0" stop-color="{c1}"/><stop offset=".55" stop-color="{c2}"/><stop offset="1" stop-color="{c3}"/></radialGradient>
<radialGradient id="{cid}b" cx=".62" cy=".7" r=".6"><stop offset="0" stop-color="{c1}" stop-opacity=".0"/><stop offset="1" stop-color="{c3}" stop-opacity=".55"/></radialGradient>
<filter id="{cid}s"><feDropShadow dx="0" dy="2.5" stdDeviation="2.2" flood-opacity=".45"/></filter></defs>
<path d="{d}" fill="url(#{cid}a)" filter="url(#{cid}s)"/>
<circle cx="50" cy="50" r="33" fill="url(#{cid}b)"/>
<circle cx="50" cy="50" r="33" fill="none" stroke="{c3}" stroke-width="2.2" opacity=".7"/>
<circle cx="50" cy="50" r="31.6" fill="none" stroke="{c1}" stroke-width=".9" opacity=".8"/>
<circle cx="50" cy="50" r="28" fill="none" stroke="{c3}" stroke-width=".6" stroke-dasharray="1 2" opacity=".6"/>
{emblem}{txt}
<ellipse cx="36" cy="30" rx="12" ry="6" fill="#fff" opacity=".22" transform="rotate(-30 36 30)"/></svg>'''


def tree_emblem(c):
    br = "".join(f'<path d="M50 60Q{50+s*6} {48-k*4} {50+s*(10+k*2)} {42-k*6}" stroke="{c}" stroke-width="1.3" fill="none"/>'
                 f'<circle cx="{50+s*(10+k*2)}" cy="{42-k*6}" r="2.4" fill="{c}"/>' for k in range(3) for s in (-1, 1))
    return f'<g opacity=".75">{br}<path d="M50 70V36" stroke="{c}" stroke-width="1.6"/><circle cx="50" cy="33" r="2.6" fill="{c}"/></g>'


# ------------------------------------------------------------------ mandala
def mandala_rich(c, cls="mandala-rich", sw=.55):
    """Detailed line-art mandala (viewBox -200..200)."""
    o = []
    add = o.append

    def circle(r, w=sw, dash=None):
        add(f'<circle r="{r}" fill="none" stroke="{c}" stroke-width="{w}"' + (f' stroke-dasharray="{dash}"' if dash else "") + "/>")

    def petals(n, w, h, r0, rot=0, fill="none", inner=False):
        for i in range(n):
            a = rot + i * 360 / n
            add(f'<path d="{petal_d(w, h)}" transform="rotate({f(a)}) translate(0 {f(-r0)})" fill="{fill}" stroke="{c}" stroke-width="{sw}"/>')
            if inner:
                add(f'<path d="{petal_d(w*.55, h*.7)}" transform="rotate({f(a)}) translate(0 {f(-r0-h*.1)})" fill="none" stroke="{c}" stroke-width="{sw*.8}"/>')

    def dots(n, r, s=1.2, rot=0):
        for i in range(n):
            a = radians(rot + i * 360 / n)
            add(f'<circle cx="{f(r*cos(a))}" cy="{f(r*sin(a))}" r="{s}" fill="{c}"/>')

    def scallops(n, r, depth, rot=0):
        d = ""
        for i in range(n):
            a0 = radians(rot + i * 360 / n)
            a1 = radians(rot + (i + 1) * 360 / n)
            am = (a0 + a1) / 2
            p0 = (r * cos(a0), r * sin(a0))
            p1 = (r * cos(a1), r * sin(a1))
            pm = ((r + depth) * cos(am), (r + depth) * sin(am))
            d += f"M{f(p0[0])} {f(p0[1])}Q{f(pm[0])} {f(pm[1])} {f(p1[0])} {f(p1[1])}"
        add(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{sw}"/>')

    def loops(n, r, s, rot=0):
        for i in range(n):
            a = radians(rot + i * 360 / n)
            add(f'<circle cx="{f(r*cos(a))}" cy="{f(r*sin(a))}" r="{s}" fill="none" stroke="{c}" stroke-width="{sw}"/>')

    def spokes(n, r0, r1, rot=0):
        d = "".join(f"M{f(r0*cos(radians(rot+i*360/n)))} {f(r0*sin(radians(rot+i*360/n)))}L{f(r1*cos(radians(rot+i*360/n)))} {f(r1*sin(radians(rot+i*360/n)))}" for i in range(n))
        add(f'<path d="{d}" stroke="{c}" stroke-width="{sw*.7}"/>')

    petals(8, 6, 16, 0, inner=True); circle(18); dots(16, 22, .9)
    petals(12, 7, 20, 24, 15, inner=True); circle(46); circle(49, dash="1 2")
    loops(36, 54, 3.2); circle(58)
    petals(16, 8, 26, 58, 11.25, inner=True); petals(16, 5, 18, 60, 0)
    circle(86); scallops(32, 86, 7); dots(32, 97, 1.1, 5.6)
    circle(100); spokes(72, 100, 110); circle(110)
    petals(24, 9, 32, 110, 7.5, inner=True); petals(24, 5, 20, 112, 0)
    circle(144); loops(48, 149, 3); circle(154)
    scallops(40, 154, 12, 4.5); scallops(40, 154, 7, 4.5); dots(40, 172, 1.3, 4.5)
    petals(40, 5, 18, 176, 0, inner=False); circle(196, dash="2 3")
    return f'<svg class="{cls}" viewBox="-200 -200 400 400" aria-hidden="true">{"".join(o)}</svg>'


# ------------------------------------------------------------------ perahera frieze
def elephant(gold, cloth, trim):
    """Decorated elephant facing right, in a 110x92 box, feet at y=90."""
    g = gold
    return f'''<g>
<path d="M18 50C16 30 34 20 56 21C72 21 84 26 88 38C92 30 104 30 106 42C108 52 102 58 100 70C99 78 102 84 98 86C94 88 92 82 94 74C95 66 94 60 92 58L88 64V90H78L76 70H44L42 90H32L30 70C24 66 19 60 18 50Z" fill="{g}"/>
<path d="M18 52C14 56 13 62 16 66" stroke="{g}" stroke-width="2" fill="none"/>
<path d="M78 34C74 44 76 56 84 60C90 54 90 40 84 34Z" fill="{g}" stroke="#00000033" stroke-width=".8"/>
<path d="M28 24C40 18 64 18 76 24L78 54Q72 60 66 54Q60 60 54 54Q48 60 42 54Q36 60 30 54L26 54Z" fill="{cloth}"/>
<path d="M28 24C40 18 64 18 76 24L78 54Q72 60 66 54Q60 60 54 54Q48 60 42 54Q36 60 30 54L26 54Z" fill="none" stroke="{trim}" stroke-width="1.4"/>
<path d="M30 30H74M31 48H75" stroke="{trim}" stroke-width="1" stroke-dasharray="2 2"/>
<circle cx="52" cy="39" r="5" fill="none" stroke="{trim}" stroke-width="1.2"/><circle cx="52" cy="39" r="1.6" fill="{trim}"/>
<path d="M90 28L104 32L100 50L96 56L92 46Z" fill="{cloth}" stroke="{trim}" stroke-width="1"/>
<path d="M92 34L102 36M93 40L100 42M94 46L99 47" stroke="{trim}" stroke-width=".8"/>
<circle cx="96" cy="39" r="1.3" fill="#2a1a0a"/>
<path d="M98 50C104 54 106 50 104 46" stroke="#fffdf2" stroke-width="2" fill="none" stroke-linecap="round"/>
<path d="M40 20V10H62V20" fill="{cloth}" stroke="{trim}" stroke-width="1"/>
<path d="M36 10Q51 -4 66 10Z" fill="{trim}"/><path d="M51 0V-6" stroke="{trim}" stroke-width="1.2"/><circle cx="51" cy="-7" r="1.6" fill="{trim}"/>
</g>'''


def bearer(gold, cloth, kind, trim):
    head = f'<circle cx="10" cy="20" r="4.2" fill="{gold}"/>'
    body = f'<path d="M4 50L6 28Q10 24 14 28L16 50Z" fill="{cloth}" stroke="{trim}" stroke-width=".7"/><path d="M6 50L5 70H8L10 54L12 70H15L14 50Z" fill="{gold}"/>'
    if kind == "parasol":
        extra = (f'<path d="M14 30L22 -2" stroke="{gold}" stroke-width="1.3"/><path d="M8 0Q22 -16 36 0Z" fill="{cloth}" stroke="{trim}" stroke-width="1"/>'
                 + "".join(f'<path d="M{9+i*3.4} 0v4" stroke="{trim}" stroke-width=".9"/>' for i in range(8)))
    elif kind == "drum":
        extra = f'<rect x="1" y="34" width="18" height="12" rx="5" fill="{gold}" stroke="{trim}" stroke-width=".8"/><path d="M4 34V46M16 34V46" stroke="{cloth}" stroke-width="1"/>'
        head += f'<path d="M5 17L10 10L15 17" fill="{trim}"/>'
    elif kind == "flag":
        extra = f'<path d="M3 30L0 -6" stroke="{gold}" stroke-width="1.3"/><path d="M0 -6L-14 -2L0 4Z" fill="{cloth}" stroke="{trim}" stroke-width=".8"/>'
    else:  # torch
        extra = (f'<path d="M15 30L18 6" stroke="{gold}" stroke-width="1.6"/><path class="flame" d="M18 -6C21 0 22 3 18 7C14 3 15 0 18 -6Z" fill="#ffb627"/>')
        head += f'<path d="M4 20Q10 6 16 20" fill="none" stroke="{trim}" stroke-width="1.2"/>'
    return f'<g>{extra}{body}{head}</g>'


def perahera(gold="#c8a25a", cloth="#7a1f22", trim="#e8cf8f", ground="#c8a25a", cls="perahera"):
    """Seamless procession frieze; returns an SVG 480x100 intended to tile horizontally."""
    items = [
        f'<g transform="translate(6 10) scale(.92)">{elephant(gold, cloth, trim)}</g>',
        f'<g transform="translate(122 24) scale(.95)">{bearer(gold, cloth, "torch", trim)}</g>',
        f'<g transform="translate(150 24) scale(.95)">{bearer(gold, cloth, "drum", trim)}</g>',
        f'<g transform="translate(184 24) scale(.95)">{bearer(gold, cloth, "parasol", trim)}</g>',
        f'<g transform="translate(226 10) scale(.92)">{elephant(gold, cloth, trim)}</g>',
        f'<g transform="translate(344 24) scale(.95)">{bearer(gold, cloth, "flag", trim)}</g>',
        f'<g transform="translate(372 24) scale(.95)">{bearer(gold, cloth, "drum", trim)}</g>',
        f'<g transform="translate(404 24) scale(.95)">{bearer(gold, cloth, "torch", trim)}</g>',
        f'<g transform="translate(436 24) scale(.95)">{bearer(gold, cloth, "parasol", trim)}</g>',
    ]
    base = f'<rect x="0" y="92" width="480" height="8" fill="{ground}"/><path d="M0 91H480" stroke="{trim}" stroke-width="1"/>'
    return f'<svg class="{cls}" viewBox="0 -4 480 104" aria-hidden="true">{"".join(items)}{base}</svg>'


# ------------------------------------------------------------------ watercolor florals
def wc_filter(fid, scale=6, freq=.03, blur=.6):
    return (f'<filter id="{fid}" x="-15%" y="-15%" width="130%" height="130%">'
            f'<feTurbulence type="fractalNoise" baseFrequency="{freq}" numOctaves="3" seed="3" result="t"/>'
            f'<feDisplacementMap in="SourceGraphic" in2="t" scale="{scale}" xChannelSelector="R" yChannelSelector="G" result="d"/>'
            f'<feGaussianBlur in="d" stdDeviation="{blur}"/></filter>')


def rose(cx, cy, s, pal, fid, rot=0):
    """Watercolor rose. pal = (light, mid, dark, deep)."""
    L, M, D, X = pal
    rnd = random.Random(int(cx * 7 + cy))
    o = [f'<g transform="translate({f(cx)} {f(cy)}) rotate({rot}) scale({s})" filter="url(#{fid})">']
    for i in range(8):
        a = i * 45 + rnd.uniform(-10, 10)
        rx, ry = 20 + rnd.uniform(-2, 4), 19 + rnd.uniform(-2, 3)
        o.append(f'<ellipse cx="0" cy="-27" rx="{f(rx)}" ry="{f(ry)}" transform="rotate({f(a)})" fill="{L}" stroke="{M}" stroke-width="1.2" opacity=".9"/>')
        o.append(f'<ellipse cx="0" cy="-20" rx="{f(rx*.6)}" ry="{f(ry*.55)}" transform="rotate({f(a)})" fill="{M}" opacity=".35"/>')
    o.append(f'<circle r="29" fill="{M}" opacity=".75"/>')
    for k in range(10):
        r = 27 - k * 2.5
        a = k * 71 + 20
        o.append(f'<path d="M{f(-r)} 0A{f(r)} {f(r*.82)} 0 0 1 {f(r)} 0Q0 {f(r*.4)} {f(-r)} 0Z" transform="rotate({a}) translate(0 {f(-r*.1)})" fill="{L if k % 2 else M}"/>')
        o.append(f'<path d="M{f(-r*.95)} {f(-r*.1)}A{f(r)} {f(r*.82)} 0 0 1 {f(r*.95)} {f(-r*.1)}" transform="rotate({a}) translate(0 {f(-r*.1)})" stroke="{D}" stroke-width="1.4" fill="none" opacity=".75"/>')
    o.append(f'<circle r="3.5" fill="{X}"/></g>')
    return "".join(o)


def anemone(cx, cy, s, fid, rot=0):
    o = [f'<g transform="translate({f(cx)} {f(cy)}) rotate({rot}) scale({s})" filter="url(#{fid})">']
    for i in range(6):
        o.append(f'<ellipse cx="0" cy="-22" rx="17" ry="22" transform="rotate({i*60+10})" fill="#fbfaf7"/>')
        o.append(f'<ellipse cx="0" cy="-14" rx="9" ry="12" transform="rotate({i*60+10})" fill="#dcdde3" opacity=".55"/>')
    o.append('<circle r="10" fill="#2b2d3c"/>')
    o += [f'<circle cx="{f(14*cos(radians(a)))}" cy="{f(14*sin(radians(a)))}" r="1.8" fill="#2b2d3c"/>' for a in range(0, 360, 24)]
    o.append('</g>')
    return "".join(o)


def blossom(cx, cy, s, fid, pal=("#fbd3da", "#f3a3b3", "#d9677e"), rot=0):
    L, M, D = pal
    o = [f'<g transform="translate({f(cx)} {f(cy)}) rotate({rot}) scale({s})" filter="url(#{fid})">']
    for i in range(5):
        o.append(f'<path d="M0 0C-12 -6 -14 -24 -5 -30L0 -26L5 -30C14 -24 12 -6 0 0Z" transform="rotate({i*72})" fill="{L}"/>')
        o.append(f'<path d="M0 0C-5 -6 -5 -14 0 -18C5 -14 5 -6 0 0Z" transform="rotate({i*72})" fill="{M}" opacity=".7"/>')
    o += [f'<path d="M0 0L{f(9*cos(radians(a)))} {f(9*sin(radians(a)))}" stroke="{D}" stroke-width=".9"/><circle cx="{f(9*cos(radians(a)))}" cy="{f(9*sin(radians(a)))}" r="1.3" fill="#d69a3a"/>' for a in range(0, 360, 30)]
    o.append(f'<circle r="3" fill="{D}"/></g>')
    return "".join(o)


def hydrangea(cx, cy, s, fid, pal=("#c9d7ef", "#9fb5dc", "#6f89bd")):
    rnd = random.Random(int(cx + cy * 3))
    L, M, D = pal
    o = [f'<g transform="translate({f(cx)} {f(cy)}) scale({s})" filter="url(#{fid})">', f'<circle r="30" fill="{M}" opacity=".22"/>']
    for _ in range(34):
        a, r = rnd.uniform(0, 2 * pi), 30 * rnd.random() ** .6
        x, y = r * cos(a), r * sin(a)
        rr = rnd.uniform(0, 45)
        o.append(f'<g transform="translate({f(x)} {f(y)}) rotate({f(rr)})">' + "".join(
            f'<path d="M0 0C-5 -3 -6 -10 0 -12C6 -10 5 -3 0 0Z" transform="rotate({k*90})" fill="{rnd.choice([L, L, M])}"/>' for k in range(4))
            + f'<circle r="1.3" fill="{D}"/></g>')
    o.append("</g>")
    return "".join(o)


def leaf(x, y, s, rot, col, fid, vein="#ffffff55"):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({s})" filter="url(#{fid})">'
            f'<path d="{petal_d(13, 46)}" fill="{col}"/><path d="M0 0V-44" stroke="{vein}" stroke-width="1.2"/></g>')


def eucalyptus(x, y, s, rot, col, fid):
    o = [f'<g transform="translate({f(x)} {f(y)}) rotate({f(rot)}) scale({s})" filter="url(#{fid})"><path d="M0 0Q6 -40 0 -90" stroke="#7d8f69" stroke-width="1.6" fill="none"/>']
    for k in range(6):
        yy = -10 - k * 14
        o.append(f'<ellipse cx="{-9 if k%2 else 9}" cy="{yy}" rx="9" ry="7" fill="{col}" opacity=".85"/>')
    o.append("</g>")
    return "".join(o)


def branch(x0, y0, x1, y1, bend, col="#8a6a55", w=3):
    mx, my = (x0 + x1) / 2 + bend, (y0 + y1) / 2 - bend
    return f'<path d="M{f(x0)} {f(y0)}Q{f(mx)} {f(my)} {f(x1)} {f(y1)}" stroke="{col}" stroke-width="{w}" fill="none" stroke-linecap="round"/>'


def gold_floral_tile(c, size=180):
    """Line-art floral pattern tile for velvet backgrounds."""
    o = []
    for (cx, cy, s) in ((45, 50, 1), (135, 140, 1), (135, 40, .6), (40, 140, .6)):
        o.append(f'<g transform="translate({cx} {cy}) scale({s})">' + ring(8, 7, 26, 4, "none", c, .8) + ring(8, 4, 14, 3, "none", c, .6, rot=22.5) + f'<circle r="4" fill="none" stroke="{c}" stroke-width=".8"/></g>')
    o.append(f'<path d="M45 76Q60 110 110 128M70 40Q100 20 124 30M100 150Q80 170 58 160M160 110Q176 80 150 64" fill="none" stroke="{c}" stroke-width=".8"/>')
    for (x, y, r) in ((78, 104, 30), (96, 27, -70), (78, 160, 120), (166, 86, -20), (20, 90, 200), (150, 180, 60)):
        o.append(f'<path d="{petal_d(6, 20)}" transform="translate({x} {y}) rotate({r})" fill="none" stroke="{c}" stroke-width=".7"/>')
    return svg_uri(f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 180 180">{"".join(o)}</svg>')
