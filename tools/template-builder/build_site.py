"""Assemble the full website into /home/claude/site."""
import os, sys, json, shutil
sys.path.insert(0, os.path.dirname(__file__))
from orn import lotus, liyawel
from art import mandala_rich

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(SRC, "..", "out")
SITE = os.path.abspath(os.path.join(SRC, "..", ".."))

# ---------- copy templates + metadata ----------
for d in ("templates", "premium"):
    dst = os.path.join(SITE, d)
    if os.path.exists(dst): shutil.rmtree(dst)
    shutil.copytree(os.path.join(OUT, d), dst)
shutil.copy(os.path.join(SRC, "music.js"), os.path.join(SITE, "assets", "music.js"))

def tags(c):
    t, low = [], c.lower()
    if c.startswith("Premium"): t.append("Premium")
    for k, v in [("traditional", "Traditional"), ("sinhala", "Traditional"), ("hindu", "Hindu"), ("muslim", "Muslim"), ("catholic", "Catholic"),
                 ("luxury", "Luxury"), ("modern", "Modern"), ("floral", "Floral"), ("classic", "Modern")]:
        if k in low and v not in t: t.append(v)
    return t

m1 = json.load(open(os.path.join(OUT, "meta.json")))
m2 = json.load(open(os.path.join(OUT, "meta2.json")))
lst = []
for m in m2 + m1:
    f = m["file"] if "/" in m["file"] else "templates/" + m["file"]
    tid = os.path.basename(f)[:-5]
    lst.append(dict(id=tid, file=f, name=m["name"], category=m["category"], blurb=m["blurb"], color=m["color"], tags=tags(m["category"]), premium=f.startswith("premium/")))
json.dump(lst, open(os.path.join(SITE, "assets", "templates.json"), "w"), indent=1, ensure_ascii=False)
json.dump({t["id"]: {"file": t["file"], "name": t["name"], "premium": t["premium"]} for t in lst},
          open(os.path.join(SITE, "api", "src", "lib", "templates.json"), "w"), indent=1)
json.dump({"brand": "Mangala", "footer": "Digital invitation by Mangala"}, open(os.path.join(SITE, "api", "src", "lib", "site.json"), "w"), indent=1)

# ---------- shared partials ----------
LOGO = lotus("#f3d9a4", "#e9c47f", "#6e1a1f", "")
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Figtree:wght@400;500;600&display=swap" rel="stylesheet">'
ICON = lambda d: f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'


def head(title, desc, extra=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta name="theme-color" content="#6e1a1f">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="assets/site.css">{extra}
<script src="assets/config.js"></script>
</head>
<body>"""


def header(active=""):
    def a(href, label):
        cur = ' aria-current="page"' if active == href else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    return f"""<header class="site-head"><div class="wrap">
<a class="logo" href="index.html">{LOGO}<span data-site="brand">Mangala</span></a>
<button class="menu-btn" type="button" aria-label="Menu" aria-expanded="false"><svg width="26" height="26" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7h18M3 12h18M3 17h18" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button>
<nav class="nav" aria-label="Main">{a("templates.html", "Designs")}{a("index.html#how", "How it works")}{a("index.html#pricing", "Pricing")}{a("index.html#faq", "FAQ")}{a("dashboard.html", "My invitations")}
<a class="btn small" href="create.html">Create invitation</a></nav></div></header>"""


FOOT = """<footer class="site-foot"><div class="wrap">
<div><a class="logo" href="index.html" style="font-size:1.35rem">""" + LOGO + """<span data-site="brand">Mangala</span></a><p style="margin-top:8px" data-site="tagline"></p></div>
<nav aria-label="Footer"><a href="templates.html">Designs</a><a href="create.html">Create</a><a href="dashboard.html">My invitations</a><a href="index.html#pricing">Pricing</a><a href="privacy.html">Privacy</a><a data-wa="">WhatsApp us</a><a data-mail></a></nav>
<p>© <span data-year></span> <span data-site="brand">Mangala</span></p></div></footer>"""


def page(name, title, desc, body, active="", scripts="", extra_head=""):
    html = head(title, desc, extra_head) + header(active) + body + FOOT + '\n<script src="assets/site.js"></script>' + scripts + "\n</body>\n</html>\n"
    open(os.path.join(SITE, name), "w", encoding="utf-8").write(html)


open(os.path.join(SITE, "assets", "favicon.svg"), "w").write(LOGO.replace("<svg ", '<svg xmlns="http://www.w3.org/2000/svg" '))

# ---------- home ----------
features = [
    (ICON('<path d="M21 12a9 9 0 11-4-7.5L21 3v5h-5"/><path d="M8 12l3 3 5-6"/>'), "Opens straight from WhatsApp", "Guests tap a link — no app, no download. Your names and date show in the WhatsApp preview."),
    (ICON('<path d="M4 5h16v14H4z"/><path d="M8 9h8M8 13h5"/><path d="M15 16l2 2 3-4"/>'), "RSVPs and headcount", "Guests reply in seconds. Your dashboard adds up attending guests per event, ready for the hotel's catering count."),
    (ICON('<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/>'), "A personal link for every guest", "“Dear Uncle Sunil & Family” greets them on the envelope and fills in their RSVP."),
    (ICON('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'), "Nekath and muhurtham times", "Each event carries its auspicious time, a live countdown, directions and add-to-calendar."),
    (ICON('<path d="M9 18V5l11-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="17" cy="16" r="3"/>'), "Music for your tradition", "Magul bera, nadaswaram, daf or church organ play as the invitation opens — or use your own song."),
    (ICON('<path d="M3 7l9-4 9 4-9 4z"/><path d="M3 12l9 4 9-4M3 17l9 4 9-4"/>'), "Sinhala, Tamil and English", "Write in any language, with proper fonts for Sinhala, Tamil and Arabic."),
]
music = [("magulbera", "Magul bera", "Kandyan drums and horanewa"), ("magulflute", "Soft flute", "Gentle Sinhala flute and drums"), ("mangala", "Mangala vadyam", "Nadaswaram, thavil and tanpura"),
         ("daf", "Daf", "Frame drum, no melody"), ("organ", "Church organ", "Pachelbel’s Canon in D"), ("musicbox", "Music box", "Soft and modern")]
faqs = [
    ("How do guests open the invitation?", "They tap the link you send on WhatsApp, Viber, SMS or email. It opens in the phone’s browser with no app to install, and works on any smartphone."),
    ("Can we write it in Sinhala or Tamil?", "Yes. Every text field accepts Sinhala, Tamil, Arabic or English, and the designs load proper fonts for each script."),
    ("How do RSVPs work?", "Guests pick attending or not, how many people are coming and which events. Replies appear on your private dashboard, where you can download them as a spreadsheet. Guests can also reply on WhatsApp if you add your number."),
    ("Can we change details after sending?", "Yes. Edit from your dashboard and the same link updates for everyone. There is no need to resend."),
    ("Do we still need printed cards?", "Many couples send both. The digital invitation carries the details that change, like maps, times and RSVPs, while a small printed card goes to elders who prefer paper."),
    ("How do we pay?", "Create and preview for free. When you’re ready to share it with guests, message us on WhatsApp and pay by bank transfer or card link."),
    ("Is our information private?", "Your invitation is only visible to people who have the link. RSVPs are only visible on your private dashboard link."),
]
home = f"""
<main>
<section class="hero"><div class="hero-mandala">{mandala_rich("#b98f45")}</div><div class="wrap">
<div><p class="eyebrow">Digital wedding invitations · Sri Lanka</p>
<h1>Invitations your guests open with <em>a single tap</em></h1>
<p class="lede">Choose a design made for poruwa ceremonies, muhurthams, nikahs and church weddings. Add your nekath times, photos and music, then share one link on WhatsApp and watch the RSVPs arrive.</p>
<div class="ctas"><a class="btn" href="create.html">Create your invitation</a><a class="btn ghost" href="templates.html">Browse 25 designs</a></div>
<div class="langs"><span>Sinhala</span><span>Tamil</span><span>English</span><span>WhatsApp-ready</span></div></div>
<div class="hero-phones" aria-label="Live invitation examples — tap to open">
<div class="phone p1" data-src="premium/p01-silk-perahera.html" data-title="Silk Perahera example"></div>
<div class="phone p2" data-src="premium/p07-sakura-blush.html" data-title="Sakura Blush example"></div></div>
</div></section>

<div class="wrap"><div class="traditions">
<div><b>Poruwa</b><span>Nekath times &amp; homecoming</span></div><div><b>Muhurtham</b><span>Tamil Hindu ceremonies</span></div>
<div><b>Nikah</b><span>Nikah &amp; walima</span></div><div><b>Nuptial Mass</b><span>Church weddings</span></div><div><b>Modern</b><span>Beach, garden, city</span></div></div></div>

<section class="section"><div class="wrap">
<div class="sec-head"><p class="eyebrow">Everything in one link</p><h2>More than a pretty card</h2><p>Your invitation handles the questions guests always ask: where, when, how to get there and whether they’re coming.</p></div>
<div class="features">{''.join(f'<article class="feature"><div class="ic">{i}</div><h3>{h}</h3><p>{p}</p></article>' for i, h, p in features)}</div></div></section>

<section class="section tint" id="how"><div class="wrap">
<div class="sec-head"><p class="eyebrow">How it works</p><h2>Ready in an evening</h2></div>
<div class="steps"><div class="step"><h3>Pick a design</h3><p>Traditional, Tamil, Muslim, Catholic, luxury or modern. Every design is animated and made for phones.</p></div>
<div class="step"><h3>Add your details</h3><p>Names, parents, events, auspicious times, venues, photos and music. You see every change live.</p></div>
<div class="step"><h3>Share and relax</h3><p>Send your link, or a personal link per guest, on WhatsApp. RSVPs collect on your dashboard.</p></div></div></div></section>

<section class="section"><div class="wrap"><div class="sec-head center"><p class="eyebrow">25 designs</p><h2>Find the one that feels like you</h2><p>Tap a design to start with it.</p></div></div>
<div class="showcase" id="showcase" data-ids="p01-silk-perahera,05-mangalam-tamil,p03-velvet-seal,07-nikah-noor,p08-rose-garden,09-holy-matrimony,p06-emerald-drape,13-modern-minimal,p05-royal-curtain"></div>
<p style="text-align:center;margin-top:10px"><a class="btn ghost" href="templates.html">See all designs</a></p></section>

<section class="section tint"><div class="wrap"><div class="sec-head"><p class="eyebrow">Music</p><h2>Music that belongs at your wedding</h2><p>Each design plays music suited to its tradition when it opens. Tap to listen.</p></div>
<div class="music-grid">{''.join(f'<button type="button" class="music-card" data-style="{s}" aria-pressed="false"><span class="play"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4l13 8-13 8z" fill="currentColor"/></svg></span><span><b>{n}</b><span>{d}</span></span></button>' for s, n, d in music)}</div></div></section>

<section class="section" id="pricing"><div class="wrap"><div class="sec-head center"><p class="eyebrow">Pricing</p><h2>One price per wedding</h2><p>No subscriptions. Create and preview for free, and pay when you’re ready to share.</p></div>
<div class="plans" id="plans"></div></div></section>

<section class="section tint" id="faq"><div class="wrap"><div class="sec-head center"><p class="eyebrow">Questions</p><h2>Good to know</h2></div>
<div class="faq">{''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs)}</div></div></section>

<section class="cta-band">{mandala_rich("#f3d9a4", "bg")}<div class="wrap" style="position:relative"><h2>Start your invitation tonight</h2><p>It’s free to create and preview.</p><a class="btn" href="create.html">Create your invitation</a></div></section>
</main>"""
page("index.html", "Mangala — Digital Wedding Invitations for Sri Lanka", "Animated digital wedding invitations for Sri Lankan weddings: poruwa, muhurtham, nikah and church. RSVPs, nekath times, music and WhatsApp sharing.",
     home, scripts='\n<script src="assets/music.js"></script>')

# ---------- designs ----------
page("templates.html", "Designs — Mangala", "25 animated wedding invitation designs for Sinhala, Tamil, Muslim, Catholic and modern weddings.", """
<main class="section" style="padding-top:56px"><div class="wrap">
<div class="sec-head"><p class="eyebrow">25 designs</p><h2>Choose your design</h2><p>Every design is live: tap a phone to play its opening and scroll inside it. Each one plays music suited to its tradition.</p></div>
<div class="chips" id="chips" role="group" aria-label="Filter designs"></div>
<div class="tgrid" id="tgrid"></div></div></main>""", active="templates.html")

# ---------- create ----------
EDITOR_CSS = """<style>
.editor{display:grid;grid-template-columns:minmax(0,1fr) 420px;gap:40px;max-width:1280px;margin:0 auto;padding:32px 20px 120px;align-items:start}
.ed-top h1{font-size:clamp(2rem,4vw,2.8rem)}
.ed-top .status{font-size:.82rem;color:var(--muted);margin-top:4px}
.ed-sec{background:var(--card);border:1px solid var(--line-2);border-radius:var(--radius);margin-top:14px}
.ed-sec>summary{list-style:none;cursor:pointer;padding:18px 20px;font-family:var(--f-display);font-size:1.45rem;font-weight:500;display:flex;align-items:center;gap:12px}
.ed-sec>summary::-webkit-details-marker{display:none}
.ed-sec>summary::after{content:"";margin-left:auto;width:9px;height:9px;border-right:1.5px solid var(--muted);border-bottom:1.5px solid var(--muted);transform:rotate(45deg);transition:transform .2s}
.ed-sec[open]>summary::after{transform:rotate(225deg)}
.ed-sec .n{width:30px;height:30px;border-radius:50%;border:1px solid var(--gold);display:grid;place-items:center;font-size:1rem;color:var(--maroon);flex:none}
.ed-body{padding:4px 20px 22px}
.fgrid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.fgrid>.field{grid-column:span 2}.fgrid>.field.half{grid-column:span 1}
@media(max-width:560px){.fgrid>.field.half{grid-column:span 2}}
.tp-g{font-size:.78rem;font-weight:600;margin:14px 0 8px;color:var(--muted)}
.tp-row{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}
.tp{display:grid;grid-template-columns:auto 1fr;gap:2px 10px;align-items:center;text-align:left;font:inherit;background:#fff;border:1px solid var(--line-2);border-radius:12px;padding:10px 12px;cursor:pointer;color:var(--ink)}
.tp i{grid-row:span 2;width:22px;height:22px;border-radius:50%;background:var(--c);box-shadow:inset 0 0 0 2px rgba(255,255,255,.6)}
.tp span{font-size:.88rem;font-weight:600;line-height:1.2}.tp small{font-size:.72rem;color:var(--muted);line-height:1.2}
.tp[aria-pressed=true]{border-color:var(--maroon);box-shadow:0 0 0 2px var(--maroon)}
.rep{border:1px solid var(--line-2);border-radius:12px;padding:14px;margin-bottom:12px;background:var(--ivory)}
.rep-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;font-size:.88rem}
.icon-btn{background:#fff;border:1px solid var(--line-2);border-radius:8px;width:32px;height:32px;cursor:pointer;margin-left:4px;color:var(--ink)}
.icon-btn[disabled]{opacity:.35;cursor:default}
.thumb{position:relative;width:120px;aspect-ratio:3/4;border-radius:10px;overflow:hidden;background:var(--paper);display:grid;place-items:center;font-size:.75rem;color:var(--muted);border:1px solid var(--line-2)}
.thumb img{width:100%;height:100%;object-fit:cover}
.thumb .icon-btn{position:absolute;top:6px;right:6px;margin:0;width:28px;height:28px}
.album-ed{display:flex;flex-wrap:wrap;gap:10px}.album-ed .thumb{width:92px;aspect-ratio:1}
.upl{justify-self:start;margin-top:8px}
.ed-preview{position:sticky;top:88px;display:flex;flex-direction:column;align-items:center;gap:14px}
.ed-preview .phone{--pw:360px}
.pv-acts{display:flex;gap:8px;flex-wrap:wrap;justify-content:center}
.ed-actions{position:sticky;bottom:0;z-index:20;margin-top:18px;background:rgba(251,246,238,.92);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-top:1px solid var(--line-2);padding:14px 0 calc(14px + env(safe-area-inset-bottom,0px));display:flex;gap:10px;flex-wrap:wrap}
.ed-actions .btn{flex:1 1 180px}
#show-preview,#hide-preview{display:none}
.errs{margin:14px 0 0;padding-left:20px;color:var(--err)}
.tag-prem{margin-left:8px}
@media(max-width:1000px){
 .editor{grid-template-columns:1fr}
 .ed-preview{display:none}
 body.pv-on .ed-preview{display:flex;position:fixed;inset:0;z-index:150;background:rgba(30,15,10,.92);padding:16px;justify-content:center;top:0}
 body.pv-on .ed-preview .phone{--pw:min(340px,calc((100vh - 110px)*.462))}
 #show-preview{display:inline-flex}#hide-preview{display:inline-flex}
}
</style>"""
page("create.html", "Create your invitation — Mangala", "Design your digital wedding invitation: pick a design, add your details and share one link.", """
<main class="editor">
<div class="ed-form">
<div class="ed-top"><p class="eyebrow" id="tname">Loading…</p><h1 id="mode">Create your invitation</h1><p class="status" id="status" role="status">Your draft saves on this device as you type.</p>
<p style="margin-top:10px"><a class="btn small ghost" id="dash-link" hidden href="#">Back to dashboard</a></p></div>
<div class="ed-sec" style="padding:18px 20px"><p style="font-family:var(--f-display);font-size:1.45rem;display:flex;gap:12px;align-items:center"><span class="n" style="width:30px;height:30px;border-radius:50%;border:1px solid var(--gold);display:grid;place-items:center;font-size:1rem;color:var(--maroon)">1</span>Choose a design</p><div id="tpick"></div></div>
<div id="sections"></div>
<div class="ed-actions"><button type="button" class="btn ghost" id="show-preview">Preview</button><button type="button" class="btn ghost" id="download">Download file</button><button type="button" class="btn" id="publish">Publish &amp; get link</button></div>
<p style="margin-top:14px;font-size:.85rem" class="muted">Want to start again? <button type="button" id="reset" style="background:none;border:0;color:var(--maroon);text-decoration:underline;cursor:pointer;font:inherit">Reset to the sample wording</button></p>
</div>
<aside class="ed-preview" aria-label="Live preview">
<div class="phone"><iframe id="pv" title="Live preview of your invitation"></iframe></div>
<div class="pv-acts"><button type="button" class="btn small ghost" id="replay">Replay opening</button><button type="button" class="btn small ghost" id="pv-open">Open full screen</button><button type="button" class="btn small" id="hide-preview">Back to editing</button></div>
</aside>
</main>
<div class="modal" id="modal" hidden><div class="box" tabindex="-1" role="dialog" aria-modal="true"></div></div>
<div class="modal" id="confirm" hidden><div class="box" role="dialog" aria-modal="true"><h2>Start again?</h2><p class="muted" style="margin-top:10px">This clears your draft on this device and loads the sample wording for this design.</p>
<p style="display:flex;gap:10px;margin-top:20px"><button type="button" class="btn" id="confirm-yes">Yes, start again</button><button type="button" class="btn ghost" id="confirm-no">Keep my draft</button></p></div></div>""",
     active="create.html", scripts='\n<script src="assets/music.js"></script>\n<script src="assets/create.js"></script>', extra_head=EDITOR_CSS)

# ---------- dashboard ----------
DASH_CSS = """<style>
.dash{max-width:1100px;margin:0 auto;padding:40px 20px 100px}
.dash h1{font-size:clamp(2.2rem,5vw,3.2rem)}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:28px}
.stat{background:var(--card);border:1px solid var(--line-2);border-radius:var(--radius);padding:18px}
.stat b{display:block;font-family:var(--f-display);font-size:2.4rem;font-weight:500;line-height:1;color:var(--maroon);font-variant-numeric:tabular-nums}
.stat span{font-size:.82rem;color:var(--muted)}
@media(max-width:640px){.stats{grid-template-columns:1fr 1fr}}
.per-event{list-style:none;padding:0;margin:14px 0 0;display:flex;flex-wrap:wrap;gap:8px}
.per-event li{background:var(--paper);border-radius:999px;padding:6px 14px;font-size:.85rem;display:flex;gap:8px}
.panel{background:var(--card);border:1px solid var(--line-2);border-radius:var(--radius);padding:22px;margin-top:22px}
.panel h2{font-size:1.7rem}
.panel-head{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:14px}
.tbl{overflow-x:auto}
table{width:100%;border-collapse:collapse;font-size:.9rem}
th{text-align:left;font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600;padding:10px;border-bottom:1px solid var(--line)}
td{padding:12px 10px;border-bottom:1px solid var(--line-2);vertical-align:top}
td.num{font-variant-numeric:tabular-nums;text-align:right}th.num{text-align:right}
td.when{white-space:nowrap;color:var(--muted);font-size:.82rem}
td.empty{text-align:center;color:var(--muted);padding:34px}
.pill{display:inline-block;border-radius:999px;padding:3px 10px;font-size:.76rem;font-weight:600;white-space:nowrap}
.pill.ok{background:#e4f2e8;color:var(--ok)}.pill.no{background:#f7e6e6;color:var(--err)}
.links{list-style:none;padding:0;margin:16px 0 0;display:grid;gap:8px}
.links li{display:flex;gap:12px;align-items:center;justify-content:space-between;flex-wrap:wrap;border:1px solid var(--line-2);border-radius:12px;padding:10px 12px;background:var(--ivory)}
.links li>div{display:grid;gap:4px;flex:1;min-width:200px}.links input{font-size:.8rem;min-height:36px}
.links li>span{display:flex;gap:6px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14px}@media(max-width:700px){.two{grid-template-columns:1fr}}
.mine{padding-left:18px}
</style>"""
page("dashboard.html", "Dashboard — Mangala", "See RSVPs and share personal guest links for your wedding invitation.", """
<main class="dash">
<p class="eyebrow">Your dashboard</p><h1 id="couple">My invitations</h1><p class="muted" id="when"></p>
<div id="nokey" hidden class="panel"><h2>Open your dashboard</h2><p class="muted" style="margin-top:8px">Use the private dashboard link you received when you published your invitation. You can still make personal guest links below for any invitation link.</p><div id="mine"></div>
<p style="margin-top:16px"><a class="btn" href="create.html">Create an invitation</a></p></div>
<div id="rsvp-area">
<div class="panel"><div class="panel-head"><h2>Your invitation</h2><span style="display:flex;gap:8px;flex-wrap:wrap"><a class="btn small ghost" id="view" target="_blank" rel="noopener">View</a><a class="btn small" id="edit">Edit invitation</a></span></div>
<div class="copyrow"><input type="text" readonly id="inv-link" aria-label="Invitation link"><button type="button" class="btn small" data-copy="inv-link">Copy link</button></div></div>
<div class="stats" id="stats"></div><ul class="per-event" id="per-event"></ul>
<div class="panel"><div class="panel-head"><h2>Replies</h2><span style="display:flex;gap:8px;align-items:center;flex-wrap:wrap"><span class="muted" id="updated" style="font-size:.8rem"></span><button type="button" class="btn small ghost" id="refresh">Refresh</button><button type="button" class="btn small" id="csv">Download spreadsheet</button></span></div>
<div class="tbl"><table><thead><tr><th>Name</th><th>Reply</th><th class="num">Guests</th><th>Events</th><th>Message</th><th>When</th></tr></thead><tbody id="rows"><tr><td colspan="6" class="empty">Loading…</td></tr></tbody></table></div></div>
</div>
<div class="panel"><h2>Personal guest links</h2><p class="muted" style="margin-top:6px">Each guest sees their own name on the envelope, and their RSVP is filled in. Type one name per line.</p>
<div class="field" id="base-row" hidden style="margin-top:14px"><label for="base-url">Invitation link</label><input type="url" id="base-url" placeholder="https://yourdomain.lk/i/your-names"></div>
<div class="two" style="margin-top:14px"><div class="field"><label for="guests">Guest names</label><textarea id="guests" rows="7" placeholder="Uncle Sunil &amp; Family&#10;Aunty Kamala&#10;Nimal &amp; Priya"></textarea></div>
<div class="field"><label for="msg">WhatsApp message</label><textarea id="msg" rows="7">Dear {name}, with joy we invite you to our wedding. Please open your invitation here: {link}</textarea><span class="hint">{name} and {link} are filled in for each guest.</span></div></div>
<ul class="links" id="links"></ul></div>
</main>""", active="dashboard.html", scripts='\n<script src="assets/dashboard.js"></script>', extra_head=DASH_CSS)

# ---------- privacy + 404 ----------
page("privacy.html", "Privacy — Mangala", "How Mangala handles your invitation details and RSVPs.", """
<main class="section" style="padding-top:56px"><div class="wrap" style="max-width:720px">
<p class="eyebrow">Privacy</p><h1 style="font-size:clamp(2.2rem,5vw,3.2rem);margin-top:10px">Your details stay yours</h1>
<div style="display:grid;gap:16px;margin-top:24px" class="muted">
<p><b style="color:var(--ink)">What we store.</b> The details you enter for your invitation (names, dates, venues, wording, photos and music you upload) and the RSVPs your guests send: their name, reply, number of guests, events and message.</p>
<p><b style="color:var(--ink)">Who can see it.</b> Your invitation is visible to anyone with its link. RSVPs are visible only through your private dashboard link. We don’t sell or share your data.</p>
<p><b style="color:var(--ink)">Drafts.</b> While you design, your draft is saved in your own browser until you publish.</p>
<p><b style="color:var(--ink)">Deleting.</b> Message us on <a data-wa="Hi! Please delete my invitation and RSVPs.">WhatsApp</a> or email <a data-mail></a> and we’ll delete your invitation, photos and RSVPs.</p>
</div></div></main>""")
page("404.html", "Page not found — Mangala", "This page doesn’t exist.", """
<main class="section" style="text-align:center"><div class="wrap"><p class="eyebrow">404</p><h1 style="font-size:3rem;margin-top:10px">This page isn’t here</h1>
<p class="muted" style="margin-top:12px">If you were opening an invitation, check the link you were sent.</p><p style="margin-top:24px"><a class="btn" href="index.html">Go to the home page</a></p></div></main>""")

# ---------- hosting config ----------
json.dump({
    "routes": [{"route": "/i/*", "rewrite": "/api/i"}],
    "navigationFallback": {"rewrite": "/404.html", "exclude": ["/assets/*", "/templates/*", "/premium/*", "/api/*"]},
    "responseOverrides": {"404": {"rewrite": "/404.html"}},
    "globalHeaders": {"X-Content-Type-Options": "nosniff", "Referrer-Policy": "strict-origin-when-cross-origin"},
    "platform": {"apiRuntime": "node:20"},
}, open(os.path.join(SITE, "staticwebapp.config.json"), "w"), indent=2)
print("site built:", len(lst), "templates")
