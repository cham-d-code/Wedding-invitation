"""SVG ornament library for the invitation templates (all original, generated)."""
from math import cos, sin, pi, radians
from urllib.parse import quote


def f(n):
    return f"{n:.1f}".rstrip("0").rstrip(".")


def petal_d(w, h):
    """Pointed petal, base at 0,0 pointing up (-y)."""
    return (f"M0 0C{f(w)} {f(-h*.3)} {f(w*.9)} {f(-h*.8)} 0 {f(-h)}"
            f"C{f(-w*.9)} {f(-h*.8)} {f(-w)} {f(-h*.3)} 0 0Z")


def ring(n, w, h, r0, fill, stroke="none", sw=0, rot=0, op=1):
    return "".join(
        f'<path d="{petal_d(w, h)}" transform="rotate({f(rot + i*360/n)}) translate(0 {f(-r0)})" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"/>'
        for i in range(n))


def svg_uri(svg):
    return 'url("data:image/svg+xml,' + quote(svg, safe=" =:/,;-_.#()'") + '")'


def mandala(c, c2, cls="mandala", fill2="none"):
    """Generic rotating mandala / kolam-like rosette. c = stroke colour."""
    parts = [
        f'<circle r="96" fill="none" stroke="{c}" stroke-width=".6" stroke-dasharray="2 4"/>',
        ring(24, 7, 22, 70, "none", c, .8),
        ring(16, 10, 34, 38, fill2, c, .8, rot=11.25),
        f'<circle r="38" fill="none" stroke="{c}" stroke-width=".8"/>',
        ring(8, 12, 34, 0, "none", c2, 1),
        ring(8, 7, 20, 0, "none", c, .8, rot=22.5),
        f'<circle r="6" fill="{c2}"/>',
        "".join(f'<circle cx="{f(86*cos(radians(a)))}" cy="{f(86*sin(radians(a)))}" r="1.8" fill="{c}"/>'
                for a in range(0, 360, 15)),
    ]
    return f'<svg class="{cls}" viewBox="-100 -100 200 200" aria-hidden="true">{"".join(parts)}</svg>'


def lotus(c1, c2, stroke, cls="lotus"):
    back = "".join(f'<path d="{petal_d(15, 62)}" transform="translate(100 112) rotate({a})" fill="{c2}" stroke="{stroke}" stroke-width="1"/>' for a in (-72, -48, 48, 72))
    mid = "".join(f'<path d="{petal_d(18, 72)}" transform="translate(100 112) rotate({a})" fill="{c1}" stroke="{stroke}" stroke-width="1"/>' for a in (-24, 24))
    front = f'<path d="{petal_d(20, 84)}" transform="translate(100 112)" fill="{c1}" stroke="{stroke}" stroke-width="1"/>'
    base = f'<path d="M46 114Q100 132 154 114" fill="none" stroke="{stroke}" stroke-width="1.5"/>'
    return f'<svg class="{cls}" viewBox="0 0 200 134" aria-hidden="true">{back}{mid}{front}{base}</svg>'


def lamp(gold, gid, flames=1, cls="lamp"):
    xs = [40] if flames == 1 else [18, 40, 62]
    fl = "".join(
        f'<path class="flame" style="animation-delay:{i*.3}s" d="M{x} 8C{x+7} 22 {x+9} 32 {x} 42C{x-9} 32 {x-7} 22 {x} 8Z" fill="url(#{gid})"/>'
        for i, x in enumerate(xs))
    glow = f'<ellipse class="glow" cx="40" cy="28" rx="{24 if flames == 1 else 40}" ry="24" fill="url(#{gid})" opacity=".5"/>'
    top = (f'<path d="M4 44Q40 70 76 44Z" fill="{gold}"/><path d="M2 44H78" stroke="{gold}" stroke-width="3" stroke-linecap="round"/>'
           if flames > 1 else
           f'<path d="M12 44Q40 70 68 44Z" fill="{gold}"/><path d="M8 44H72" stroke="{gold}" stroke-width="3" stroke-linecap="round"/>')
    return (f'<svg class="{cls}" viewBox="0 0 80 150" aria-hidden="true"><defs><radialGradient id="{gid}" cx=".5" cy=".65" r=".6">'
            f'<stop offset="0" stop-color="#fffbe0"/><stop offset=".45" stop-color="#ffc53d"/><stop offset="1" stop-color="#ff6a00" stop-opacity="0"/>'
            f'</radialGradient></defs>{glow}{fl}{top}'
            f'<path d="M37 58H43L46 118H34Z" fill="{gold}"/><circle cx="40" cy="76" r="6.5" fill="{gold}"/><circle cx="40" cy="98" r="5" fill="{gold}"/>'
            f'<path d="M16 138Q40 110 64 138Z" fill="{gold}"/><rect x="12" y="136" width="56" height="7" rx="3.5" fill="{gold}"/></svg>')


def spiral(cx, cy, r0, turns, d=1, start=0.0):
    pts = []
    n = 48
    for i in range(n + 1):
        t = i / n
        th = start + d * t * turns * 2 * pi
        r = r0 * (1 - t * .82)
        pts.append((cx + r * cos(th), cy + r * sin(th)))
    return "M" + " L".join(f"{f(x)} {f(y)}" for x, y in pts)


def liyawel(c, cls="divider", accent=None):
    """Horizontal Sinhala 'liyawel' style scroll divider, 320x50."""
    a = accent or c
    half = (
        f'<path d="M34 25H128" stroke="{c}" stroke-width="1.2" fill="none"/>'
        f'<path d="{spiral(34, 15, 10, 1.1, -1, pi/2)}" stroke="{c}" stroke-width="1.2" fill="none"/>'
        f'<path d="{spiral(78, 33, 7, .9, 1, -pi/2)}" stroke="{c}" stroke-width="1" fill="none"/>'
        f'<path d="{spiral(104, 17, 6, .9, -1, pi/2)}" stroke="{c}" stroke-width="1" fill="none"/>'
        + "".join(f'<path d="{petal_d(4, 12)}" transform="translate({x} 25) rotate({r})" fill="{a}"/>'
                  for x, r in ((56, -55), (64, 125), (92, 55), (118, -125)))
    )
    center = (f'<path d="M140 25L150 17L160 25L150 33Z" fill="none" stroke="{c}" stroke-width="1"/>'
              f'<g transform="translate(160 25)">{ring(8, 4, 11, 2, a, "none", 0)}<circle r="3" fill="{c}"/></g>'
              f'<path d="M160 25L170 17L180 25L170 33Z" fill="none" stroke="{c}" stroke-width="1"/>')
    return (f'<svg class="{cls}" viewBox="0 0 320 50" aria-hidden="true"><g>{half}</g>'
            f'<g transform="translate(320 0) scale(-1 1)">{half}</g>{center}</svg>')


def corner(c, cls="corner"):
    """Corner scroll ornament, 120x120, anchored top-left."""
    return (f'<svg class="{cls}" viewBox="0 0 120 120" aria-hidden="true">'
            f'<path d="M8 8H96M8 8V96M16 16H70M16 16V70" stroke="{c}" stroke-width="1.2" fill="none"/>'
            f'<path d="{spiral(96, 18, 10, 1.1, 1, -pi/2)}" stroke="{c}" stroke-width="1.2" fill="none"/>'
            f'<path d="{spiral(18, 96, 10, 1.1, -1, pi)}" stroke="{c}" stroke-width="1.2" fill="none"/>'
            f'<path d="{petal_d(7, 26)}" transform="translate(16 16) rotate(135)" fill="{c}"/>'
            f'<path d="{petal_d(5, 18)}" transform="translate(30 30) rotate(135)" fill="none" stroke="{c}" stroke-width="1"/>'
            f'<circle cx="8" cy="8" r="3" fill="{c}"/></svg>')


def punkalasa(c, cls="punkalasa"):
    spray = ""
    for i, a in enumerate(range(-75, 80, 15)):
        L = 52 if i % 2 else 58
        ex, ey = 60 + sin(radians(a)) * L, 62 - cos(radians(a)) * L
        mx, my = 60 + sin(radians(a)) * L * .5, 62 - cos(radians(a)) * L * .6
        spray += f'<path d="M60 62Q{f(mx)} {f(my)} {f(ex)} {f(ey)}" stroke="{c}" stroke-width="1.1" fill="none"/><circle cx="{f(ex)}" cy="{f(ey)}" r="2.6" fill="{c}"/>'
    leaves = "".join(f'<path d="{petal_d(10, 50)}" transform="translate(60 70) rotate({a})" fill="none" stroke="{c}" stroke-width="1.2"/>' for a in (-62, 62))
    pot = (f'<path d="M48 62H72V74H48Z" fill="{c}"/><ellipse cx="60" cy="62" rx="16" ry="4" fill="{c}"/>'
           f'<circle cx="60" cy="106" r="32" fill="{c}"/>'
           f'<path d="M30 100Q60 114 90 100" stroke="#0003" stroke-width="2" fill="none"/>'
           f'<path d="M31 112Q60 124 89 112" stroke="#0003" stroke-width="1.2" fill="none" stroke-dasharray="3 3"/>'
           f'<ellipse cx="60" cy="140" rx="20" ry="5" fill="{c}"/>')
    return f'<svg class="{cls}" viewBox="0 0 120 150" aria-hidden="true">{spray}{leaves}{pot}</svg>'


def kolam_tile(c):
    return svg_uri(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="44" height="44" viewBox="0 0 44 44">'
        f'<g fill="none" stroke="{c}" stroke-width="1"><rect x="14" y="14" width="16" height="16" rx="5" transform="rotate(45 22 22)"/>'
        f'<circle cx="0" cy="0" r="9"/><circle cx="44" cy="0" r="9"/><circle cx="0" cy="44" r="9"/><circle cx="44" cy="44" r="9"/></g>'
        f'<circle cx="22" cy="22" r="1.6" fill="{c}"/><circle cx="0" cy="22" r="1.2" fill="{c}"/><circle cx="44" cy="22" r="1.2" fill="{c}"/>'
        f'<circle cx="22" cy="0" r="1.2" fill="{c}"/><circle cx="22" cy="44" r="1.2" fill="{c}"/></svg>')


def star8_tile(c, size=60):
    s = size
    h = s / 2
    q = s / 4
    return svg_uri(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 {s} {s}"><g fill="none" stroke="{c}" stroke-width="1">'
        f'<rect x="{h-q*.72}" y="{h-q*.72}" width="{q*1.44}" height="{q*1.44}"/>'
        f'<rect x="{h-q*.72}" y="{h-q*.72}" width="{q*1.44}" height="{q*1.44}" transform="rotate(45 {h} {h})"/>'
        f'<path d="M{h} 0V{h-q*1.02}M{h} {s}V{h+q*1.02}M0 {h}H{h-q*1.02}M{s} {h}H{h+q*1.02}"/>'
        f'<path d="M0 {q*.7}L{q*.7} 0M{s-q*.7} 0L{s} {q*.7}M0 {s-q*.7}L{q*.7} {s}M{s-q*.7} {s}L{s} {s-q*.7}"/>'
        f'</g></svg>')


def flower_tile(c):
    return svg_uri(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="56" height="56" viewBox="-28 -28 56 56">'
        f'{ring(4, 4, 11, 2, "none", c, .8, rot=45)}<circle r="1.6" fill="{c}"/>'
        f'<g transform="translate(-28 -28)">{ring(4, 2.5, 7, 1, c, "none", 0)}</g>'
        f'<g transform="translate(28 28)">{ring(4, 2.5, 7, 1, c, "none", 0)}</g>'
        f'<g transform="translate(28 -28)">{ring(4, 2.5, 7, 1, c, "none", 0)}</g>'
        f'<g transform="translate(-28 28)">{ring(4, 2.5, 7, 1, c, "none", 0)}</g></svg>')


def star8(c, cls="star8", fill="none"):
    return (f'<svg class="{cls}" viewBox="-50 -50 100 100" aria-hidden="true"><g fill="{fill}" stroke="{c}" stroke-width="2">'
            f'<rect x="-30" y="-30" width="60" height="60"/><rect x="-30" y="-30" width="60" height="60" transform="rotate(45)"/></g>'
            f'<circle r="12" fill="none" stroke="{c}" stroke-width="2"/></svg>')


def crescent(c, cls="crescent"):
    return (f'<svg class="{cls}" viewBox="0 0 100 100" aria-hidden="true"><mask id="cm"><rect width="100" height="100" fill="#fff"/>'
            f'<circle cx="60" cy="42" r="34" fill="#000"/></mask><circle cx="46" cy="50" r="38" fill="{c}" mask="url(#cm)"/>'
            f'<path d="M78 20l3 8 8 1-6 5 2 8-7-4-7 4 2-8-6-5 8-1z" fill="{c}"/></svg>')


def arch(c, cls="arch-frame", pointed=True):
    if pointed:
        o = "M18 470V180C18 104 84 70 150 14C216 70 282 104 282 180V470"
        i = "M32 470V184C32 116 92 84 150 34C208 84 268 116 268 184V470"
    else:
        o = "M18 470V160A132 132 0 0 1 282 160V470"
        i = "M32 470V162A118 118 0 0 1 268 162V470"
    return (f'<svg class="{cls}" viewBox="0 0 300 480" preserveAspectRatio="none" aria-hidden="true">'
            f'<path d="{o}" fill="none" stroke="{c}" stroke-width="2.2" vector-effect="non-scaling-stroke"/>'
            f'<path d="{i}" fill="none" stroke="{c}" stroke-width="1" vector-effect="non-scaling-stroke"/></svg>')


def gopuram(c, cls="gopuram"):
    out = []
    w, y, h = 250, 300, 30
    for i in range(7):
        x = (300 - w) / 2
        out.append(f'<path d="M{f(x)} {y}H{f(x+w)}L{f(x+w-10)} {y-h}H{f(x+10)}Z" fill="none" stroke="{c}" stroke-width="1.3"/>')
        n = max(2, int((w - 30) / 22))
        for k in range(n):
            nx = x + 16 + k * (w - 32) / (n - 1)
            out.append(f'<path d="M{f(nx-5)} {y-4}V{y-h+13}A5 5 0 0 1 {f(nx+5)} {y-h+13}V{y-4}" fill="none" stroke="{c}" stroke-width=".9"/>')
        y -= h
        w -= 30
    x = (300 - w) / 2
    out.append(f'<path d="M{f(x)} {y}Q150 {y-60} {f(x+w)} {y}Z" fill="none" stroke="{c}" stroke-width="1.4"/>')
    for k in range(5):
        kx = x + w * (k + .5) / 5
        out.append(f'<path d="M{f(kx)} {y-18 if k in (1, 3) else y-6}v-{12 if k == 2 else 6}" stroke="{c}" stroke-width="1.4"/>')
    out.append(f'<circle cx="150" cy="{y-48}" r="4" fill="{c}"/><path d="M150 {y-52}v-12" stroke="{c}" stroke-width="1.4"/>')
    out.append(f'<path d="M130 300V262A20 20 0 0 1 170 262V300" fill="none" stroke="{c}" stroke-width="1.5"/>')
    out.append(f'<path d="M10 300H290" stroke="{c}" stroke-width="2"/>')
    return f'<svg class="{cls}" viewBox="0 0 300 310" aria-hidden="true">{"".join(out)}</svg>'


def marigold(cx, cy, r, c1, c2):
    return (f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{r}" fill="{c1}" stroke="{c2}" stroke-width="{r*.45:.1f}" stroke-dasharray="1.6 1.2"/>'
            f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{r*.35:.1f}" fill="{c2}"/>')


def thoranam(cls="thoranam"):
    """Marigold + mango-leaf garland across the top, 400x120."""
    out = []
    cols = [("#f7a21b", "#d8650b"), ("#ffd23f", "#e89b0c")]
    swags = [(0, 133), (133, 267), (267, 400)]
    for s, (x0, x1) in enumerate(swags):
        for k in range(15):
            t = k / 14
            x = x0 + (x1 - x0) * t
            y = 8 + 36 * 4 * t * (1 - t)
            c1, c2 = cols[k % 2]
            out.append(marigold(x, y, 6.2, c1, c2))
    for i, x in enumerate((0, 133, 267, 400)):
        g = [f'<g class="strand" style="animation-delay:{i*.4}s;transform-origin:{x}px 8px">']
        for k in range(4):
            c1, c2 = cols[(k + i) % 2]
            g.append(marigold(x, 14 + k * 12, 5.6, c1, c2))
        g.append(f'<path d="{petal_d(6, 26)}" transform="translate({x} 60) rotate(180)" fill="#2f7d32" stroke="#1d5a20" stroke-width=".8"/>')
        g.append('</g>')
        out.append("".join(g))
    for x in (66, 200, 334):
        out.append(f'<path d="{petal_d(7, 30)}" transform="translate({x} 42) rotate(180)" fill="#3a8f3d" stroke="#1d5a20" stroke-width=".8"/>')
        out.append(f'<path d="{petal_d(6, 24)}" transform="translate({x} 42) rotate(155)" fill="#2f7d32" stroke="#1d5a20" stroke-width=".8"/>')
        out.append(f'<path d="{petal_d(6, 24)}" transform="translate({x} 42) rotate(205)" fill="#2f7d32" stroke="#1d5a20" stroke-width=".8"/>')
    return f'<svg class="{cls}" viewBox="-8 0 416 100" preserveAspectRatio="xMidYMin meet" aria-hidden="true">{"".join(out)}</svg>'


def frangipani(cx, cy, s, rot=0, gid="fg"):
    petals = "".join(
        f'<ellipse cx="0" cy="{-s*.5:.1f}" rx="{s*.3:.1f}" ry="{s*.52:.1f}" transform="rotate({i*72+rot+12}) " fill="url(#{gid})" stroke="#e8dcc0" stroke-width=".6"/>'
        for i in range(5))
    return f'<g transform="translate({cx} {cy}) rotate({rot})">{petals}<circle r="{s*.14:.1f}" fill="#f2b705"/></g>'


def frangi_cluster(cls="frangi", gid="fg"):
    leaves = "".join(f'<path d="{petal_d(14, 80)}" transform="translate(70 70) rotate({a})" fill="{c}" />'
                     for a, c in ((200, "#4f7a4f"), (245, "#3f6a44"), (160, "#5f8c5a")))
    veins = "".join(f'<path d="M0 0V-76" transform="translate(70 70) rotate({a})" stroke="#ffffff55" stroke-width="1"/>' for a in (200, 245, 160))
    fl = frangipani(70, 70, 34, 0, gid) + frangipani(112, 52, 26, 30, gid) + frangipani(48, 112, 24, -20, gid)
    return (f'<svg class="{cls}" viewBox="0 0 170 170" aria-hidden="true"><defs><radialGradient id="{gid}" cx=".5" cy="1" r="1">'
            f'<stop offset="0" stop-color="#f7c948"/><stop offset=".35" stop-color="#fff4d0"/><stop offset="1" stop-color="#ffffff"/></radialGradient></defs>'
            f'{leaves}{veins}{fl}</svg>')


def lantern(gold, glow_id, cls="lantern"):
    return (f'<svg class="{cls}" viewBox="0 0 60 150" aria-hidden="true"><defs><radialGradient id="{glow_id}" cx=".5" cy=".5" r=".5">'
            f'<stop offset="0" stop-color="#fff3c4"/><stop offset=".6" stop-color="#ffb84d"/><stop offset="1" stop-color="#ff8a00" stop-opacity=".2"/></radialGradient></defs>'
            f'<path d="M30 0V30" stroke="{gold}" stroke-width="1.2"/><circle cx="30" cy="33" r="3.5" fill="none" stroke="{gold}" stroke-width="1.5"/>'
            f'<path d="M20 44H40L35 36H25Z" fill="{gold}"/>'
            f'<circle class="lglow" cx="30" cy="74" r="28" fill="url(#{glow_id})" opacity=".35"/>'
            f'<path d="M18 46H42L50 74L42 102H18L10 74Z" fill="url(#{glow_id})" stroke="{gold}" stroke-width="2"/>'
            f'<path d="M30 46V102M10 74H50M18 46L30 74L18 102M42 46L30 74L42 102" stroke="{gold}" stroke-width=".9" fill="none"/>'
            f'<path d="M18 102H42L36 110H24Z" fill="{gold}"/><path d="M30 110V122" stroke="{gold}" stroke-width="1.4"/>'
            f'<path d="M26 122H34L32 136H28Z" fill="{gold}"/></svg>')


def slice_path(r1, r2, a0, a1):
    a0r, a1r = radians(a0), radians(a1)
    p = lambda r, a: f"{f(r*cos(a))} {f(r*sin(a))}"
    return f"M{p(r1, a0r)}L{p(r2, a0r)}A{r2} {r2} 0 0 1 {p(r2, a1r)}L{p(r1, a1r)}A{r1} {r1} 0 0 0 {p(r1, a0r)}Z"


def rose_window(cls="rose"):
    cols = ["#b3123a", "#1d4fa8", "#e0a526", "#127a5a", "#6b2fa0", "#1d4fa8"]
    lead = "#0d1020"
    out = [f'<circle r="98" fill="{lead}"/>']
    for i in range(24):
        out.append(f'<path d="{slice_path(72, 94, i*15+1, i*15+14)}" fill="{cols[i % 3]}" opacity=".92"/>')
    for i in range(12):
        out.append(f'<path d="{petal_d(11, 30)}" transform="rotate({i*30+15}) translate(0 -40)" fill="{cols[(i % 2)*3+1]}" stroke="{lead}" stroke-width="2"/>')
        out.append(f'<circle cx="{f(58*cos(radians(i*30)))}" cy="{f(58*sin(radians(i*30)))}" r="8" fill="{cols[i % 2 * 2]}" stroke="{lead}" stroke-width="2"/>')
    for i in range(8):
        out.append(f'<path d="{petal_d(9, 26)}" transform="rotate({i*45})" fill="{cols[2] if i % 2 else cols[0]}" stroke="{lead}" stroke-width="2"/>')
    out.append(f'<circle r="9" fill="#f6e7b0" stroke="{lead}" stroke-width="2"/>')
    out.append(f'<circle r="98" fill="none" stroke="#c9a14a" stroke-width="3"/><circle r="72" fill="none" stroke="#c9a14a" stroke-width="1.2"/>')
    return f'<svg class="{cls}" viewBox="-100 -100 200 200" aria-hidden="true">{"".join(out)}</svg>'


def cross(c, cls="cross", rays=True):
    r = ""
    if rays:
        r = "".join(f'<path d="M0 0L{f(46*cos(radians(a)))} {f(46*sin(radians(a)))}" stroke="{c}" stroke-width=".6" opacity=".6"/>' for a in range(0, 360, 15))
    return (f'<svg class="{cls}" viewBox="-50 -50 100 100" aria-hidden="true">{r}'
            f'<path d="M-4 -34H4V-14H18V-6H4V34H-4V-6H-18V-14H-4Z" fill="{c}"/></svg>')


def dove(c, cls="dove"):
    return (f'<svg class="{cls}" viewBox="0 0 80 50" aria-hidden="true"><g fill="{c}">'
            f'<path class="wing" d="M34 26C28 12 16 4 2 2C12 10 18 20 22 28Z"/>'
            f'<path d="M20 30C30 24 46 22 58 26C64 22 70 22 74 25C70 26 68 28 66 30C60 38 44 40 32 38L20 44L24 36C20 34 18 32 20 30Z"/>'
            f'<path class="wing2" d="M40 26C44 12 56 4 72 0C64 10 56 20 50 28Z" opacity=".85"/></g></svg>')


def deco_corner(c, cls="deco-corner"):
    return (f'<svg class="{cls}" viewBox="0 0 100 100" aria-hidden="true"><g fill="none" stroke="{c}" stroke-width="1.3">'
            f'<path d="M4 96V4H96"/><path d="M12 96V12H96"/><path d="M20 60V20H60"/><path d="M28 44V28H44"/>'
            f'<path d="M20 20L4 4"/></g><rect x="30" y="30" width="6" height="6" transform="rotate(45 33 33)" fill="{c}"/></svg>')


def sunburst(c, cls="sunburst"):
    rays = "".join(f'<path d="M150 150L{f(150+140*cos(radians(a)))} {f(150-140*sin(radians(a)))}" stroke="{c}" stroke-width="{1.2 if i % 2 else .6}"/>'
                   for i, a in enumerate(range(10, 171, 8)))
    arcs = "".join(f'<path d="M{150-r} 150A{r} {r} 0 0 1 {150+r} 150" fill="none" stroke="{c}" stroke-width="1"/>' for r in (40, 46, 90))
    return f'<svg class="{cls}" viewBox="0 0 300 152" aria-hidden="true">{rays}{arcs}<circle cx="150" cy="150" r="22" fill="{c}"/></svg>'


def waves(cls="waves"):
    def wave(y, amp, per, col, klass):
        d = f"M0 {y}"
        x = 0
        while x < 2880:
            d += f" q{per/4} {-amp} {per/2} 0 t{per/2} 0"
            x += per
        d += " V200 H0Z"
        return f'<svg class="wv {klass}" viewBox="0 0 2880 200" preserveAspectRatio="none" aria-hidden="true"><path d="{d}" fill="{col}"/></svg>'
    return (f'<div class="{cls}">' + wave(90, 26, 480, "#8cc9c7", "w1") + wave(110, 22, 360, "#3d9ea3", "w2")
            + wave(130, 18, 600, "#1f6f78", "w3") + wave(160, 10, 300, "#f1e6d2", "w4") + '</div>')


def palm(c, cls="palm"):
    fr = "".join(f'<path d="M70 40Q{f(70+60*cos(radians(a)))} {f(40-40*sin(radians(a)))} {f(70+95*cos(radians(a)))} {f(40-25*sin(radians(a))+30)}" stroke="{c}" stroke-width="7" stroke-linecap="round" fill="none"/>'
                 for a in (20, 55, 90, 125, 160, 200, -20))
    return (f'<svg class="{cls}" viewBox="0 0 160 260" aria-hidden="true"><path d="M70 40Q88 150 60 258" stroke="{c}" stroke-width="9" fill="none" stroke-linecap="round"/>'
            f'{fr}<circle cx="66" cy="46" r="6" fill="{c}"/><circle cx="76" cy="48" r="5" fill="{c}"/></svg>')


def hills(cls="hills"):
    layers = [("#c9d4bf", 60, "h1"), ("#9fb38e", 90, "h2"), ("#6f8a5e", 118, "h3"), ("#4a6340", 150, "h4")]
    out = []
    for i, (col, y, k) in enumerate(layers):
        d = f"M0 {y}"
        for j in range(9):
            x = j * 200 + 100
            d += f" Q{x} {y - 40 + (j*37 % 50)} {x+100} {y + (j*13 % 18)}"
        d += " V260 H0Z"
        rows = ""
        if i >= 2:
            rows = "".join(f'<path d="M0 {y+22+r*14} Q450 {y+8+r*14} 900 {y+24+r*14} T1800 {y+22+r*14}" stroke="#ffffff22" stroke-width="3" fill="none" stroke-dasharray="4 7"/>' for r in range(4))
        out.append(f'<svg class="hl {k}" viewBox="0 0 1800 260" preserveAspectRatio="none" aria-hidden="true"><path d="{d}" fill="{col}"/>{rows}</svg>')
    return f'<div class="{cls}">{"".join(out)}</div>'


def sprig(c, cls="sprig", n=6, c2=None):
    c2 = c2 or c
    out = [f'<path d="M20 200Q60 110 20 10" stroke="{c}" stroke-width="1.6" fill="none"/>']
    for k in range(n):
        t = (k + .6) / (n + .4)
        y = 200 - 190 * t
        x = 20 + 40 * 4 * t * (1 - t) * .75
        side = 1 if k % 2 else -1
        out.append(f'<path d="{petal_d(7, 30 - k*1.5)}" transform="translate({f(x)} {f(y)}) rotate({f(side*55 - 10)})" fill="{c2 if k % 2 else c}"/>')
    out.append(f'<path d="{petal_d(6, 24)}" transform="translate(21 12) rotate(-12)" fill="{c}"/>')
    return f'<svg class="{cls}" viewBox="0 0 90 210" aria-hidden="true">{"".join(out)}</svg>'


def small_lotus(c, cls="st-orn"):
    return (f'<svg class="{cls}" viewBox="0 0 60 30" aria-hidden="true"><g transform="translate(30 26)">'
            + "".join(f'<path d="{petal_d(5, 20 if a == 0 else 16)}" transform="rotate({a})" fill="{c}"/>' for a in (-60, -30, 0, 30, 60))
            + f'</g><path d="M2 27H58" stroke="{c}" stroke-width=".8"/></svg>')


def diamond_orn(c, cls="st-orn"):
    return (f'<svg class="{cls}" viewBox="0 0 120 20" aria-hidden="true"><path d="M0 10H48M72 10H120" stroke="{c}" stroke-width=".8"/>'
            f'<path d="M60 2L68 10L60 18L52 10Z" fill="none" stroke="{c}"/><path d="M60 6L64 10L60 14L56 10Z" fill="{c}"/></svg>')


def leaf_orn(c, cls="st-orn"):
    return (f'<svg class="{cls}" viewBox="0 0 120 30" aria-hidden="true"><path d="M8 15H112" stroke="{c}" stroke-width=".8"/>'
            + "".join(f'<path d="{petal_d(4, 12)}" transform="translate({x} 15) rotate({r})" fill="{c}"/>' for x, r in ((40, -60), (48, 60), (72, 60), (80, -60)))
            + f'<circle cx="60" cy="15" r="3" fill="{c}"/></svg>')


def monogram_ring(c, cls="mono-ring"):
    ticks = "".join(f'<path d="M0 -92V{-88 if i % 5 else -84}" transform="rotate({i*6})" stroke="{c}" stroke-width="{1.2 if i % 5 == 0 else .6}"/>' for i in range(60))
    return (f'<svg class="{cls}" viewBox="-100 -100 200 200" aria-hidden="true"><circle r="96" fill="none" stroke="{c}" stroke-width=".8"/>'
            f'<g class="spin">{ticks}</g><circle r="78" fill="none" stroke="{c}" stroke-width=".8" stroke-dasharray="1 5"/></svg>')
