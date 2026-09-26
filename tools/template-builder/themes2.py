"""Premium collection: 10 themes (textures, curtains, envelopes, watercolor)."""
import json
from orn import *
from art import *
from engine2 import ICONS
from themes import COMMON_HERO_CSS, hdate, names, T, zwj

RSVP = {"deadline": "", "whatsapp": "94770000000", "endpoint": "", "maxGuests": 6}
BRAND = "Digital invitation · yourbrand.lk"


def silk_cv(**o):
    return f"<canvas class=\"silk-cv\" data-silk='{json.dumps(o)}'></canvas>"


def frieze(svg):
    return f'<div class="frieze">{svg}{svg}{svg}{svg}</div>'


def story(city="Colombo", place="Ella", lake="Kandy Lake"):
    return [
        dict(date="2019", title="The day we met", text=f"A friend's birthday in {city}, a shared umbrella and a conversation that never really ended."),
        dict(date="2022", title="Our first trip", text=f"Watching the sunrise together in {place} — the moment we both knew."),
        dict(date="2025", title="The proposal", text=f"A quiet evening by {lake}, a ring, a yes, and two very happy families."),
    ]


def data(**kw):
    d = dict(rsvp=dict(RSVP), brand=BRAND, music="", couplePhoto="", heroImage="", photos=[], albumSlots=6,
             storyIntro="Every love story is special, but ours is our favourite. Here are a few pages from it.")
    d.update(kw)
    return d


def bouquet(fid, cls="bouquet", scale=1.0):
    return (f'<svg class="{cls}" viewBox="0 0 390 300" aria-hidden="true"><defs>{wc_filter(fid)}</defs>'
            + leaf(60, 200, 1.3, -70, "#8fb08a", fid) + leaf(95, 225, 1.1, -30, "#6f9670", fid) + leaf(330, 190, 1.35, 70, "#7fa37d", fid) + leaf(295, 228, 1.1, 30, "#9ab894", fid)
            + eucalyptus(40, 250, 1.15, -62, "#a7bfae", fid) + eucalyptus(350, 255, 1.15, 62, "#a7bfae", fid) + eucalyptus(190, 110, .9, -8, "#b5c9ba", fid)
            + leaf(150, 110, .9, -20, "#8fb08a", fid) + leaf(245, 112, .9, 25, "#7fa37d", fid)
            + rose(120, 180, 1.45, ("#fbd3cb", "#f0a79e", "#cf6f69", "#9a3f3d"), fid, 10)
            + rose(275, 185, 1.3, ("#fde0d8", "#f4b8ad", "#dc877c", "#a8504a"), fid, 40)
            + rose(200, 135, .95, ("#fdeae4", "#f7cbc1", "#e7a093", "#b8665c"), fid, 70)
            + anemone(198, 222, 1.08, fid) + anemone(338, 132, .6, fid, 20)
            + blossom(58, 132, .75, fid, ("#fff4f1", "#f7d3cc", "#e5a397")) + blossom(80, 105, .5, fid, ("#fff4f1", "#f7d3cc", "#e5a397"))
            + hydrangea(330, 135, .55, fid, ("#f7e7e3", "#eecfc8", "#d9a79c")) + '</svg>')


def blossom_branch(fid, cls="bbranch"):
    fl = [(96, 64, .95, 10), (140, 96, 1.2, 40), (60, 118, .8, -20), (178, 60, .7, 70), (30, 70, .65, 0), (122, 150, .7, 15)]
    buds = [(200, 88), (18, 110), (160, 132)]
    return (f'<svg class="{cls}" viewBox="0 0 230 190" aria-hidden="true"><defs>{wc_filter(fid, 4)}</defs>'
            + branch(-10, 40, 210, 90, -30, "#9a735c", 3.2) + branch(70, 60, 130, 160, 10, "#9a735c", 2) + branch(40, 50, 20, 120, -6, "#9a735c", 1.6)
            + "".join(blossom(x, y, s, fid, rot=r) for x, y, s, r in fl)
            + "".join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="7" fill="#f3a3b3" filter="url(#{fid})"/>' for x, y in buds)
            + '</svg>')


def hydra_corner(fid, cls="hcorner"):
    return (f'<svg class="{cls}" viewBox="0 0 200 180" aria-hidden="true"><defs>{wc_filter(fid, 4)}</defs>'
            + leaf(120, 70, 1.1, 60, "#7f9f86", fid) + leaf(70, 120, 1.1, 150, "#91ae95", fid) + leaf(140, 30, .8, 95, "#a3bfa6", fid)
            + eucalyptus(150, 120, .9, 130, "#a9c0b3", fid)
            + hydrangea(60, 55, 1.2, fid) + hydrangea(118, 84, .8, fid, ("#dde6f5", "#b7c8e6", "#8199c9"))
            + blossom(28, 120, .55, fid, ("#ffffff", "#e7ecf5", "#9fb0cf")) + blossom(150, 48, .45, fid, ("#ffffff", "#e7ecf5", "#9fb0cf"))
            + '</svg>')


def lotus_line(c, cls="lotus-line"):
    return lotus("none", "none", c, cls)


P = []

# ============================================================ P1 Silk Perahera
G = "#b8995a"
SILK1 = dict(base="#f6efe4", shadow="#d9ccb7", hi="#fffdf8", angle=-35, seed=7)
per1 = perahera("#c8a25a", "#7a1f22", "#ecd392", "#c8a25a")
P.append(dict(
    slug="p01-silk-perahera", name="Silk Perahera", category="Premium · Kandyan traditional",
    blurb="Ivory silk drape, a fine gold mandala and a marching Kandyan perahera along the bottom.",
    theme_color="#7a1f22",
    fonts="family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Cinzel:wght@400;500&family=Noto+Serif+Sinhala:wght@400;500",
    vars="--bg:#f8f3ea;--bg2:#f2eadc;--ink:#3b2418;--muted:#7d6654;--accent:#7a1f22;--accent2:#9b5b2a;--gold:#b8995a;--gold-hi:#f1dfae;--line:rgba(184,153,90,.45);--card:rgba(255,253,248,.78);--card-solid:#fffdf8;--on-accent:#fff7ea;--radius:4px;"
         "--f-display:'Cormorant Garamond',serif;--f-script:'Cormorant Garamond',serif;--f-body:'Cormorant Garamond',serif;--f-native:'Noto Serif Sinhala',serif;--f-label:'Cinzel',serif;"
         "--op-ink:#6b4e2e;--op-names:#7a1f22;--ph-bg:linear-gradient(160deg,#efe4d1,#e2d2b6);--ph-ink:#8a6d3b;--nav-bg:rgba(255,251,244,.86)",
    opener="cover",
    coverbg=silk_cv(**SILK1) + f'<div class="mtop">{mandala_rich(G)}</div>' + frieze(per1),
    icon=ICONS["leaf"],
    hero=(silk_cv(**SILK1) + f'<div class="mtop spin-slow">{mandala_rich(G)}</div>'
          + '<div class="hero-in">' + T(0, "nativeGreeting", "native gr") + T(1, "labels.coverKicker", "eyebrow")
          + f'<span class="cv-rule h-in" style="--d:2"><i></i></span>' + names(3) + T(4, "c.dateOrd", "h-long")
          + T(5, "venueLine", "h-venue") + '</div>' + frieze(per1)),
    divider=liyawel(G), st_orn=small_lotus(G), ev_icon=lotus("#f3e3c0", "#ead3a0", G),
    footart=f'<div class="foot-frieze">{frieze(per1)}</div>',
    css=COMMON_HERO_CSS + """
.mtop{position:absolute;left:50%;top:0;width:min(640px,150vw);translate:-50% -52%;opacity:.9;pointer-events:none}
.mtop svg{width:100%;height:auto}
.op-cover .op-center{padding-top:14svh}
.cv-names{font-style:italic;font-weight:500}
.frieze{--frieze-h:74px}
.hero{padding-bottom:120px}
.hero-in{position:relative;display:flex;flex-direction:column;align-items:center;padding-top:14svh}
.gr{font-size:1.25rem;color:var(--gold);margin-bottom:12px}
.names{font-style:italic;font-weight:500;font-size:clamp(3rem,13vw,5.2rem);line-height:1.05}
.names .amp{font-size:.55em;color:var(--gold)}
.h-long{font-size:1.1rem;margin-top:14px}
.st{font-style:italic;font-weight:500;font-size:clamp(2rem,8vw,2.8rem)}
.sec:nth-of-type(even){background:var(--bg2)}
.event{border-top:2px solid var(--gold)}
.ev-ico{width:70px;height:48px}
.foot-frieze{position:relative;height:80px;overflow:hidden;background:#f2eadc}
footer{padding-bottom:40px}
.foot-frieze+*{margin-bottom:0}
main{padding-bottom:0}
body{padding-bottom:0}
""",
    theme={"particles": {"type": "sparkle", "colors": ["#e8cf8f", "#c8a25a"], "size": [2, 5], "count": 22, "speed": .35, "mode": "twinkle", "glow": 6},
           "music": {"key": 62, "bpm": 64, "prog": [[0, 4, 7], [5, 9, 12], [7, 11, 14], [0, 4, 7]], "pattern": [0, 2, 1, 2, 3, 2, 1, -1]}, "openMs": 1500},
    data=data(
        slug="pasindu-hansani", partner1="Pasindu", partner2="Hansani",
        fullName1="Pasindu Lakmal Herath", fullName2="Hansani Nimeshika Bandara",
        parents1="Son of Mr. & Mrs. Wimal Herath, Kandy", parents2="Daughter of Mr. & Mrs. Jayantha Bandara, Matale",
        nativeGreeting="ආයුබෝවන්", tagline="",
        hostLine="With the blessings of the Noble Triple Gem and our beloved parents, we invite you to our wedding",
        inviteText="Your presence at the poruwa would be the greatest blessing as we begin our life together.",
        quote="Hand in hand, from this auspicious moment to the last.", quoteSource="Pasindu & Hansani",
        date="2026-12-12T09:24:00+05:30", venueLine="Earl's Regency · Kandy",
        events=[
            dict(name="Poruwa Ceremony", native=zwj("පෝරුව චාරිත්{zwj}රය"), time="2026-12-12T09:24:00+05:30", timeLabel="Auspicious time · 9.24 a.m.", venue="Earl's Regency Hotel", address="Tennekumbura, Kandy", note="Kandyan drummers will welcome the couple at 9.00 a.m."),
            dict(name="Wedding Reception", native="මංගල සාදය", time="2026-12-12T12:00:00+05:30", timeLabel="12.00 noon onwards", venue="Earl's Regency · Grand Ballroom", address="Tennekumbura, Kandy"),
        ],
        story=story("Kandy", "Ella", "the Kandy Lake"),
        venue=dict(name="Earl's Regency Hotel", address="Tennekumbura, Kandy 20000", note="Parking is available at the hotel.", embed=False),
        dressCode="Traditional or formal — ivory, gold and maroon are welcome.", dressColors=["#7a1f22", "#b8995a", "#f6efe4"],
        hashtag="#PasinduWedsHansani", blessing="තෙරුවන් සරණයි",
        labels={"countdown": "Counting down to the nekath", "events": "The auspicious day"},
    )))

# ============================================================ P2 Silk Sage Lotus
G = "#a99a63"
SILK2 = dict(base="#eef0e9", shadow="#c7ccbf", hi="#ffffff", angle=-22, seed=3)
per2 = perahera("#b7a46b", "#3f5b47", "#e6dcb2", "#b7a46b")
P.append(dict(
    slug="p02-silk-sage-lotus", name="Sage Lotus Silk", category="Premium · Sinhala traditional",
    blurb="Pale sage silk with white lotus line art, a gold mandala crown and a sage perahera.",
    theme_color="#3f5b47",
    fonts="family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Marcellus+SC&family=Noto+Serif+Sinhala:wght@400",
    vars="--bg:#f4f5f0;--bg2:#eaede4;--ink:#2d3a30;--muted:#6d786d;--accent:#3f5b47;--accent2:#6d8a60;--gold:#a99a63;--gold-hi:#efe6c2;--line:rgba(120,140,110,.35);--card:rgba(255,255,255,.75);--card-solid:#fbfcf8;--on-accent:#f4f5f0;--radius:4px;"
         "--f-display:'Cormorant Garamond',serif;--f-script:'Cormorant Garamond',serif;--f-body:'Cormorant Garamond',serif;--f-native:'Noto Serif Sinhala',serif;--f-label:'Marcellus SC',serif;"
         "--op-ink:#4f6150;--op-names:#3f5b47;--ph-bg:linear-gradient(160deg,#e6ebdf,#d5dccc);--ph-ink:#5f7a5f;--nav-bg:rgba(250,251,247,.86)",
    opener="cover",
    coverbg=silk_cv(**SILK2) + f'<div class="mtop">{mandala_rich(G)}</div><div class="lotl">{lotus_line("#c4c9b6")}</div><div class="lotr">{lotus_line("#c4c9b6")}</div>' + frieze(per2),
    icon=ICONS["leaf"],
    hero=(silk_cv(**SILK2) + f'<div class="mtop">{mandala_rich(G)}</div><div class="lotl">{lotus_line("#c4c9b6")}</div><div class="lotr">{lotus_line("#c4c9b6")}</div>'
          + '<div class="hero-in">' + T(0, "nativeGreeting", "native gr") + T(1, "labels.coverKicker", "eyebrow")
          + f'<span class="cv-rule h-in" style="--d:2"><i></i></span>' + names(3) + T(4, "c.dateOrd", "h-long") + T(5, "venueLine", "h-venue") + '</div>' + frieze(per2)),
    divider=leaf_orn("#6d8a60", "divider"), st_orn=small_lotus("#6d8a60"), ev_icon=lotus("#f3f5ee", "#e2e8d9", "#6d8a60"),
    css=COMMON_HERO_CSS + """
.mtop{position:absolute;left:50%;top:0;width:min(640px,150vw);translate:-50% -52%;opacity:.85;pointer-events:none}.mtop svg{width:100%;height:auto}
.lotl,.lotr{position:absolute;bottom:90px;width:min(170px,42vw);opacity:.9}.lotl{left:-30px;rotate:12deg}.lotr{right:-30px;rotate:-12deg;transform:scaleX(-1)}
.lotus-line{width:100%;height:auto}
.op-cover .op-center{padding-top:14svh}
.cv-names{font-style:italic;font-weight:500}
.frieze{--frieze-h:70px;opacity:.95}
.hero{padding-bottom:120px}
.hero-in{position:relative;display:flex;flex-direction:column;align-items:center;padding-top:14svh}
.gr{font-size:1.2rem;color:var(--gold);margin-bottom:12px}
.names{font-style:italic;font-weight:500;font-size:clamp(3rem,13vw,5.2rem);line-height:1.05}
.names .amp{font-size:.55em;color:var(--gold)}
.h-long{font-size:1.1rem;margin-top:14px}
.st{font-style:italic;font-weight:500;font-size:clamp(2rem,8vw,2.8rem)}
.sec:nth-of-type(even){background:var(--bg2)}
.ev-ico{width:70px;height:48px}
""",
    theme={"particles": {"type": "petal", "colors": ["#ffffff", "#f4f6ef", "#e9efe2"], "size": [5, 9], "count": 16, "flip": True, "speed": .5},
           "music": {"key": 60, "bpm": 60, "bell": True, "pattern": [0, 1, 2, -1, 3, 2, 1, -1]}, "openMs": 1500},
    data=data(
        slug="kalana-dinithi", partner1="Kalana", partner2="Dinithi",
        fullName1="Kalana Sandeepa Wickramaratne", fullName2="Dinithi Oshadi Ranasinghe",
        parents1="Son of Mr. & Mrs. Sunil Wickramaratne, Kurunegala", parents2="Daughter of Mr. & Mrs. Chandana Ranasinghe, Gampaha",
        nativeGreeting="මංගල ආරාධනය",
        hostLine="Together with our families, we warmly invite you to celebrate our marriage",
        inviteText="A morning of tradition, an afternoon of celebration — we would love you to be there.",
        quote="Like a lotus rising from still water, may our love stay gentle and pure.", quoteSource="Kalana & Dinithi",
        date="2027-01-23T10:12:00+05:30", venueLine="Waters Edge · Battaramulla",
        events=[
            dict(name="Poruwa Ceremony", time="2027-01-23T10:12:00+05:30", timeLabel="Auspicious time · 10.12 a.m.", venue="Waters Edge", address="316 Ethul Kotte Road, Battaramulla"),
            dict(name="Luncheon", time="2027-01-23T12:30:00+05:30", timeLabel="12.30 p.m. onwards", venue="Waters Edge · Lotus Ballroom", address="Battaramulla"),
        ],
        story=story("Colombo", "Haputale", "Beira Lake"),
        venue=dict(name="Waters Edge", address="316 Ethul Kotte Road, Battaramulla", note="Complimentary valet parking at the main entrance.", embed=False),
        dressCode="Soft pastels and whites — sage, ivory and gold.", dressColors=["#3f5b47", "#eef0e9", "#a99a63"],
        hashtag="#KalanaAndDinithi", blessing="තෙරුවන් සරණයි",
    )))

# ============================================================ P3 Velvet Seal
G = "#c9a460"
VELVET = f"{noise_uri(.35, .95)},{gold_floral_tile('rgba(201,164,96,.34)')},radial-gradient(ellipse at 50% 45%,#2f5a4a,#143328 70%,#0b2019)"
P.append(dict(
    slug="p03-velvet-seal", name="Velvet Seal", category="Premium · Luxury",
    blurb="Emerald velvet with gold botanical line art, a velvet envelope and a gold wax seal.",
    theme_color="#143328",
    fonts="family=Cinzel:wght@400;500&family=Pinyon+Script&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400",
    vars="--bg:#11291f;--bg2:#153226;--ink:#efe6cf;--muted:#b9c4b4;--accent:#e2c67e;--accent2:#f4e7c4;--gold:#c9a460;--gold-hi:#fff0c2;--line:rgba(201,164,96,.4);--card:rgba(255,255,255,.04);--card-solid:#f7f1e2;--on-accent:#11291f;--radius:2px;--input-bg:rgba(0,0,0,.2);"
         "--f-display:'Cinzel',serif;--f-script:'Pinyon Script',cursive;--f-body:'Cormorant Garamond',serif;--f-native:'Cormorant Garamond',serif;--f-label:'Cinzel',serif;"
         "--op-ink:#e8d7a8;--op-names:#e2c67e;--e2-paper:" + noise_uri(.4, .95) + ",linear-gradient(170deg,#2b5a49,#1a3e31);--e2-flap:" + noise_uri(.4, .95) + ",linear-gradient(180deg,#336a56,#1f4638);--e2-inner:#0f2a20;--e2-ink:#e8d7a8;"
         "--ph-bg:linear-gradient(160deg,#1c3f32,#0f2a20);--ph-ink:#c9a460;--nav-bg:rgba(17,41,31,.82);--nav-ink:#efe6cf;--music-bg:rgba(239,230,207,.92)",
    opener="envelope2",
    coverbg=f'<div class="velvet"></div>',
    seal="",  # filled in build (needs initials)
    hero=('<div class="velvet"></div>' + f'<div class="h-seal h-in" style="--d:0">{{SEAL}}</div>'
          + T(1, "labels.invited2", "eyebrow") + names(2) + f'<span class="cv-rule h-in" style="--d:3"><i></i></span>'
          + T(4, "c.dateOrd", "h-long") + T(5, "venueLine", "h-venue")),
    divider=diamond_orn(G, "divider"), st_orn=diamond_orn(G), ev_icon=star8(G),
    css=COMMON_HERO_CSS + """
.velvet{position:absolute;inset:0;background:""" + VELVET + """}
.h-seal{width:110px;margin-bottom:20px;filter:drop-shadow(0 8px 14px rgba(0,0,0,.4))}
.names{font-size:clamp(3.4rem,15vw,5.8rem);color:var(--accent);line-height:1}
.names .amp{font-family:var(--f-display);font-size:.28em;color:var(--gold);margin:6px 0}
.h-long{font-size:1.1rem;margin-top:12px}
.hero .eyebrow{color:var(--accent2)}
.sec{background:""" + f"{gold_floral_tile('rgba(201,164,96,.07)')},var(--bg)" + """}
.sec:nth-of-type(even){background:""" + f"{gold_floral_tile('rgba(201,164,96,.07)')},var(--bg2)" + """}
.st{color:var(--accent)}
.event{outline:1px solid rgba(201,164,96,.25);outline-offset:-7px}
.ev-ico{width:40px;height:40px}
footer{background:#0b2019}
""",
    theme={"particles": {"type": "glitter", "colors": ["#f3d98a", "#c9a460", "#fff0c2"], "size": [2, 5], "count": 30, "flip": True, "speed": .5, "glow": 5},
           "music": {"key": 57, "bpm": 62, "prog": [[0, 3, 7], [8, 12, 15], [3, 7, 10], [10, 14, 17]]}, "openMs": 2600},
    seal_colors=("#f6dc92", "#c9a045", "#7a5714"),
    data=data(
        slug="gihan-malsha", partner1="Gihan", partner2="Malsha",
        fullName1="Gihan Ravishka Jayasuriya", fullName2="Malsha Tharindi Weerasinghe",
        parents1="Son of Mr. & Mrs. Rohitha Jayasuriya", parents2="Daughter of Mr. & Mrs. Nalin Weerasinghe",
        hostLine="Together with their families, request the honour of your presence at the celebration of their marriage",
        inviteText="An evening of candlelight, velvet and gold — we would be delighted to have you with us.",
        quote="Grow old along with me; the best is yet to be.", quoteSource="Robert Browning",
        date="2027-02-27T18:30:00+05:30", venueLine="Cinnamon Life · Colombo",
        events=[
            dict(name="Ceremony", time="2027-02-27T18:30:00+05:30", timeLabel="6.30 p.m.", venue="Cinnamon Life · Grand Ballroom", address="Colombo 02"),
            dict(name="Dinner & Dance", time="2027-02-27T20:00:00+05:30", timeLabel="8.00 p.m. until late", venue="Cinnamon Life · Grand Ballroom", address="Colombo 02"),
        ],
        story=story("Colombo", "Nuwara Eliya", "Galle Face"),
        venue=dict(name="Cinnamon Life at City of Dreams", address="Justice Akbar Mawatha, Colombo 02", note="Valet parking at the hotel lobby entrance.", embed=False),
        dressCode="Black tie — emerald, black and gold.", dressColors=["#143328", "#c9a460", "#efe6cf"],
        hashtag="#GihanAndMalsha", blessing="",
        labels={"invited2": "You are invited", "dearGuest": "Dear Guest"},
    )))

# ============================================================ P4 Silk Letter
G = "#b99a58"
SILK4 = dict(base="#eeeeec", shadow="#bfbfba", hi="#ffffff", angle=-18, seed=5)
P.append(dict(
    slug="p04-silk-letter", name="Silk Letter", category="Premium · Classic",
    blurb="Dove-grey silk, a sage paper envelope and a gold wax seal pressed with a little tree.",
    theme_color="#7f8574",
    fonts="family=Pinyon+Script&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Marcellus",
    vars="--bg:#f6f5f1;--bg2:#eeede7;--ink:#33362f;--muted:#767a70;--accent:#5d6653;--accent2:#8b9181;--gold:#b99a58;--gold-hi:#f0dfb0;--line:rgba(139,145,129,.35);--card:#ffffff;--card-solid:#fffdf9;--on-accent:#fff;--radius:6px;"
         "--f-display:'Cormorant Garamond',serif;--f-script:'Pinyon Script',cursive;--f-body:'Cormorant Garamond',serif;--f-native:'Cormorant Garamond',serif;--f-label:'Marcellus',serif;"
         "--op-ink:#62675d;--op-names:#a88738;--e2-paper:" + noise_uri(.25, .9) + ",linear-gradient(170deg,#979d8d,#858b7b);--e2-flap:" + noise_uri(.25, .9) + ",linear-gradient(180deg,#a2a898,#8d9383);--e2-inner:#6f7566;--e2-ink:#f4f1e6;"
         "--ph-bg:linear-gradient(160deg,#e9e9e2,#d9dbd0);--ph-ink:#8b9181",
    opener="envelope2",
    coverbg=silk_cv(**SILK4),
    hero=(silk_cv(**SILK4) + '<div class="hero-card">' + f'<div class="h-in" style="--d:0">{sprig("#8b9181", "tsprig", 6, "#a9ae9f")}</div>'
          + T(1, "labels.invited2", "eyebrow") + names(2) + T(3, "hostShort", "tagline") + hdate(4) + T(5, "venueLine", "h-venue") + '</div>'),
    divider=leaf_orn("#8b9181", "divider"), st_orn=leaf_orn(G), ev_icon=sprig("#8b9181", "", 5, "#a9ae9f"),
    css=COMMON_HERO_CSS + """
.hero-card{position:relative;background:rgba(255,255,255,.72);backdrop-filter:blur(2px);padding:34px 26px 30px;border:1px solid rgba(185,154,88,.45);outline:1px solid rgba(185,154,88,.3);outline-offset:6px;max-width:420px;width:100%;display:flex;flex-direction:column;align-items:center;box-shadow:0 30px 60px -30px rgba(0,0,0,.35)}
.tsprig{width:26px;rotate:90deg;margin:0 auto 6px}
.names{color:var(--gold);font-size:clamp(3rem,13vw,4.8rem);line-height:1.1}
.names .amp{font-size:.5em;color:var(--accent2)}
.sec:nth-of-type(even){background:var(--bg2)}
.st{font-style:italic;font-size:clamp(2rem,8vw,2.7rem)}
.ev-ico{width:30px;height:62px}
""",
    theme={"particles": {"type": "petal", "colors": ["#ffffff", "#f1efe8"], "size": [4, 8], "count": 14, "flip": True, "speed": .5},
           "music": {"key": 65, "bpm": 58, "bell": True}, "openMs": 2600},
    seal_colors=("#f3d98a", "#c49b3f", "#6e4f12"), seal_emblem="tree",
    data=data(
        slug="chanuka-sewwandi", partner1="Chanuka", partner2="Sewwandi",
        fullName1="Chanuka Dilan Amarasinghe", fullName2="Sewwandi Piyumi Dias",
        parents1="Son of Mr. & Mrs. Anura Amarasinghe", parents2="Daughter of Mr. & Mrs. Lalith Dias",
        hostShort="request the honour of your presence at the celebration of their marriage",
        hostLine="Together with their families", inviteText="Join us for vows, a garden lunch and an afternoon among the people we love.",
        quote="I have found the one whom my soul loves.", quoteSource="Song of Solomon 3:4",
        date="2026-12-27T10:30:00+05:30", venueLine="Grand Monarch · Colombo",
        events=[
            dict(name="Wedding Ceremony", time="2026-12-27T10:30:00+05:30", timeLabel="10.30 a.m.", venue="Grand Monarch", address="Thalawathugoda, Colombo"),
            dict(name="Garden Luncheon", time="2026-12-27T12:30:00+05:30", timeLabel="12.30 p.m. onwards", venue="Grand Monarch · Garden Terrace", address="Thalawathugoda"),
        ],
        story=story("Colombo", "Mirissa", "Bolgoda Lake"),
        venue=dict(name="Grand Monarch", address="Thalawathugoda, Colombo", note="Parking available on site.", embed=False),
        dressCode="Garden formal — soft greys, sage and ivory.", dressColors=["#8b9181", "#eeeeec", "#b99a58"],
        hashtag="#ChanukaSewwandi", blessing="",
        labels={"dearGuest": "Our Dear Guest"},
    )))

# ============================================================ P5 Royal Curtain
G = "#c49b4c"
P.append(dict(
    slug="p05-royal-curtain", name="Royal Curtain", category="Premium · Grand traditional",
    blurb="Heavy crimson velvet curtains part to reveal an ivory and gold palace-style invitation.",
    theme_color="#6d0f10",
    fonts="family=Cinzel+Decorative:wght@400;700&family=Cinzel:wght@400&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Noto+Serif+Sinhala:wght@400",
    vars="--bg:#fbf6ec;--bg2:#f4ecdc;--ink:#3a1b12;--muted:#7a5b48;--accent:#7a1414;--accent2:#9b5b2a;--gold:#c49b4c;--gold-hi:#f6e1a6;--line:rgba(196,155,76,.5);--card:#fffdf7;--card-solid:#fffdf7;--on-accent:#fff6e2;--radius:2px;"
         "--f-display:'Cinzel Decorative',serif;--f-script:'Cinzel Decorative',serif;--f-body:'Cormorant Garamond',serif;--f-native:'Noto Serif Sinhala',serif;--f-label:'Cinzel',serif;"
         "--op-ink:#f3dcc0;--cur2:" + noise_uri(.28, .8) + "," + curtain_bg("#7b1111", "#330404", "#a32222", 3) + ";--cur-hem:#2a0303;"
         "--ph-bg:linear-gradient(160deg,#f1e4ca,#e4cfa8);--ph-ink:#9b7a3c",
    opener="curtain2",
    coverbg=f'<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 45%,#fffaf0,#f1e3c6)"></div><div class="c-mand">{mandala_rich(G)}</div>',
    decor=ICONS["hand"] + '<p class="op-tap" style="margin-top:18px;color:#f3dcc0" data-f="labels.tap"></p>',
    hero=(f'<div class="royal-frame"><div class="rf-corner a">{corner(G)}</div><div class="rf-corner b">{corner(G)}</div><div class="rf-corner c">{corner(G)}</div><div class="rf-corner d">{corner(G)}</div></div>'
          f'<div class="h-mand spin-slow">{mandala_rich(G)}</div>'
          f'<div class="h-top h-in" style="--d:0">{lamp(G, "rfl1")}<p class="native gr" data-f="nativeGreeting"></p>{lamp(G, "rfl2")}</div>'
          + T(1, "labels.coverKicker", "eyebrow") + names(2, "names shimmer") + f'<div class="h-in" style="--d:3">{liyawel(G)}</div>' + hdate(4) + T(5, "venueLine", "h-venue")),
    divider=liyawel(G), st_orn=small_lotus(G), ev_icon=punkalasa(G),
    css=COMMON_HERO_CSS + """
.c-mand{position:absolute;left:50%;top:50%;width:min(560px,130vw);translate:-50% -50%;opacity:.35}
.hand{width:74px;height:74px;filter:drop-shadow(0 4px 8px rgba(0,0,0,.4))}
.hero{background:radial-gradient(circle at 50% 45%,#fffdf6,#f6ead2 70%,#ecdab6)}
.royal-frame{position:absolute;inset:14px;border:1.5px solid var(--gold);outline:1px solid var(--line);outline-offset:-8px;pointer-events:none}
.rf-corner{position:absolute;width:80px}.rf-corner svg{width:100%;height:auto}
.rf-corner.a{top:-2px;left:-2px}.rf-corner.b{top:-2px;right:-2px;transform:scaleX(-1)}.rf-corner.c{bottom:-2px;left:-2px;transform:scaleY(-1)}.rf-corner.d{bottom:-2px;right:-2px;transform:scale(-1)}
.h-mand{position:absolute;width:min(600px,140vw);left:50%;top:50%;translate:-50% -50%;opacity:.16;pointer-events:none}
.h-top{display:flex;align-items:flex-end;justify-content:center;gap:18px}.h-top .lamp{width:36px;height:auto}
.gr{font-size:1.4rem;color:var(--accent)}
.hero .eyebrow{margin-top:16px}
.names{font-size:clamp(2.6rem,12vw,4.6rem);line-height:1.1;margin:6px 0;--gold:#9a7428;--gold-hi:#e9c979}
.names .amp{font-family:var(--f-label);font-size:.4em}
.st{font-size:clamp(1.5rem,6vw,2.1rem)}
.sec:nth-of-type(even){background:var(--bg2)}
.event{border:1px solid var(--gold);outline:1px solid var(--line);outline-offset:-7px}
.ev-ico{width:44px;height:56px}
footer{background:#6d0f10;color:#f6e7cc}footer .f-names{color:#f6e1a6}footer .f-bless,footer .brand{color:#f6e7cc}
""",
    theme={"particles": {"type": "glitter", "colors": ["#f3d27a", "#c49b4c", "#fff2c4"], "size": [2, 5], "count": 34, "flip": True, "speed": .6},
           "music": {"key": 62, "bpm": 70, "prog": [[0, 4, 7], [5, 9, 12], [7, 11, 14], [5, 9, 12]]}, "openMs": 2200},
    data=data(
        slug="tharaka-imesha", partner1="Tharaka", partner2="Imesha",
        fullName1="Tharaka Madushan Senarath", fullName2="Imesha Kaushalya Rathnayake",
        parents1="Son of Mr. & Mrs. Dayananda Senarath, Kegalle", parents2="Daughter of Mr. & Mrs. Karunasena Rathnayake, Kandy",
        nativeGreeting=zwj("ශුභ විවාහ මංගල්{zwj}යය"),
        hostLine="With the blessings of the Triple Gem, our families request the pleasure of your company",
        inviteText="Please join us for a day of Kandyan tradition, drums and celebration.",
        quote="May our home be filled with kindness, and our hearts with each other.", quoteSource="Tharaka & Imesha",
        date="2027-03-20T09:05:00+05:30", venueLine="Mahaweli Reach · Kandy",
        events=[
            dict(name="Poruwa Ceremony", native=zwj("පෝරුව චාරිත්{zwj}රය"), time="2027-03-20T09:05:00+05:30", timeLabel="Nekath · 9.05 a.m.", venue="Mahaweli Reach Hotel", address="35 P.B.A. Weerakoon Mawatha, Kandy"),
            dict(name="Reception", native="මංගල සාදය", time="2027-03-20T12:00:00+05:30", timeLabel="12.00 noon onwards", venue="Mahaweli Reach · Ballroom", address="Kandy"),
            dict(name="Homecoming", time="2027-03-24T19:00:00+05:30", timeLabel="7.00 p.m. onwards", venue="The Kingsbury", address="Colombo 01"),
        ],
        story=story("Kandy", "Knuckles", "the Kandy Lake"),
        venue=dict(name="Mahaweli Reach Hotel", address="35 P.B.A. Weerakoon Mawatha, Kandy", note="Kandyan dancers welcome guests from 8.30 a.m.", embed=False),
        dressCode="Osariya, national dress or formal wear.", dressColors=["#7a1414", "#c49b4c", "#fbf6ec"],
        hashtag="#TharakaImesha", blessing="තෙරුවන් සරණයි",
        labels={"tap": "Tap to open", "countdown": "Counting down to the nekath"},
    )))

# ============================================================ P6 Emerald Drape
G = "#c9a55c"
SILK6 = dict(base="#4d6b5a", shadow="#1b3327", hi="#a9c9b1", angle=84, seed=5, spec=.3)
P.append(dict(
    slug="p06-emerald-drape", name="Emerald Drape", category="Premium · Luxury",
    blurb="Deep green satin drapes on a gold rod, names on the curtain and a glowing gold button.",
    theme_color="#1b3327",
    fonts="family=Cinzel+Decorative:wght@400&family=Cinzel:wght@400&family=Cormorant+Garamond:ital,wght@0,400;1,400&family=Montserrat:wght@400;500",
    vars="--bg:#152b21;--bg2:#1a3328;--ink:#f1ead8;--muted:#b8c6b8;--accent:#e2c77f;--accent2:#fff;--gold:#c9a55c;--gold-hi:#fff0c0;--line:rgba(201,165,92,.4);--card:rgba(255,255,255,.05);--card-solid:#f7f2e4;--on-accent:#152b21;--radius:10px;--input-bg:rgba(0,0,0,.2);"
         "--f-display:'Cinzel Decorative',serif;--f-script:'Cinzel Decorative',serif;--f-body:'Cormorant Garamond',serif;--f-native:'Cormorant Garamond',serif;--f-label:'Montserrat',sans-serif;"
         "--op-ink:#f1ead8;--cur2:" + noise_uri(.2, .8) + "," + curtain_bg("#4f6d5b", "#1d3528", "#7d9a86", 8) + ";--cur-hem:#12241b;--rod:linear-gradient(#f6e2a4,#b8913f 60%,#8c6a24);--rod-h:14px;"
         "--ph-bg:linear-gradient(160deg,#23443a,#152b21);--ph-ink:#c9a55c;--nav-bg:rgba(21,43,33,.85);--nav-ink:#f1ead8;--music-bg:rgba(241,234,216,.92)",
    opener="curtain2",
    coverbg=silk_cv(**SILK6),
    decor=('<span class="heart-ic">' + ICONS["heart"] + '</span><p class="cv-kicker" style="color:#e2c77f;margin-top:14px">You\'re invited</p>'
           '<h2 class="dr-names"><span data-f="partner1"></span><span class="amp">&amp;</span><span data-f="partner2"></span></h2>'
           '<p class="dr-sub" data-f="labels.drSub"></p><span class="cv-btn gold">' + ICONS["sparkle"] + '<span data-f="labels.openBtn"></span></span>'
           '<p class="op-tap" style="margin-top:18px" data-f="labels.tapBegin"></p>'),
    hero=(silk_cv(**SILK6) + '<div class="hero-glass">' + T(0, "labels.coverKicker", "eyebrow") + names(1, "names shimmer")
          + T(2, "labels.drSub", "tagline") + hdate(3) + T(4, "venueLine", "h-venue") + '</div>'),
    divider=diamond_orn(G, "divider"), st_orn=diamond_orn(G), ev_icon=star8(G),
    css=COMMON_HERO_CSS + """
.heart-ic svg{width:44px;height:44px;color:#d9b562;filter:drop-shadow(0 4px 8px rgba(0,0,0,.35))}
.dr-names{font-family:'Cinzel Decorative',serif;font-weight:400;font-size:clamp(2.6rem,12vw,3.6rem);line-height:1.15;color:#fffaf0;text-shadow:0 3px 14px rgba(0,0,0,.45);margin-top:10px;display:flex;flex-direction:column}
.dr-names .amp{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:.5em;color:#e2c77f}
.dr-sub{font-style:italic;color:#f1ead8;margin-top:8px;font-size:1.05rem}
.cv-btn.gold{--cv-btn:#3a4d3f;background:linear-gradient(180deg,#f3e0a8,#cfae63 55%,#b8913f);border:1px solid #fff2c6;box-shadow:0 0 0 4px rgba(243,224,168,.25),0 10px 24px rgba(0,0,0,.35);color:#33452f;font-weight:500;animation:cvb 2.6s ease-in-out infinite}
.hero-glass{position:relative;padding:40px 24px;max-width:430px;width:100%;border-radius:18px;background:rgba(10,25,18,.35);backdrop-filter:blur(3px);border:1px solid rgba(226,199,127,.35);display:flex;flex-direction:column;align-items:center}
.names{font-size:clamp(2.6rem,12vw,4rem);line-height:1.12}
.names .amp{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:.5em}
.hd-day{color:var(--gold)}
.st{font-size:clamp(1.5rem,6vw,2.1rem);color:var(--accent)}
.sec:nth-of-type(even){background:var(--bg2)}
.ev-ico{width:40px;height:40px}
.btn{font-family:var(--f-label)}
footer{background:#0f2018}
""",
    theme={"particles": {"type": "sparkle", "colors": ["#f3e0a8", "#c9a55c"], "size": [3, 6], "count": 22, "speed": .4, "mode": "twinkle", "glow": 8},
           "music": {"key": 60, "bpm": 64, "prog": [[9, 12, 16], [5, 9, 12], [0, 4, 7], [7, 11, 14]]}, "openMs": 2200},
    data=data(
        slug="dilshan-nadeesha", partner1="Dilshan", partner2="Nadeesha",
        fullName1="Dilshan Pramuditha Silva", fullName2="Nadeesha Anuradhi Perera",
        parents1="Son of Mr. & Mrs. Premasiri Silva", parents2="Daughter of Mr. & Mrs. Gamini Perera",
        hostLine="Together with their families", inviteText="Dinner, dancing and a night under the chandeliers — it won't be the same without you.",
        quote="You are my sun, my moon and all my stars.", quoteSource="E. E. Cummings",
        date="2027-05-15T18:30:00+05:30", venueLine="Shangri-La · Colombo",
        events=[
            dict(name="Poruwa & Vows", time="2027-05-15T18:30:00+05:30", timeLabel="6.30 p.m.", venue="Shangri-La Colombo · Lotus Ballroom", address="1 Galle Face, Colombo 02"),
            dict(name="Reception", time="2027-05-15T20:00:00+05:30", timeLabel="8.00 p.m. until late", venue="Shangri-La Colombo · Lotus Ballroom", address="Colombo 02"),
        ],
        story=story("Colombo", "Sigiriya", "Galle Face Green"),
        venue=dict(name="Shangri-La Colombo", address="1 Galle Face, Colombo 02", note="Complimentary parking for guests.", embed=False),
        dressCode="Formal evening — emerald, black and gold.", dressColors=["#1b3327", "#c9a55c", "#f1ead8"],
        hashtag="#DilshanNadeesha", blessing="",
        labels={"drSub": "Request the honour of your presence", "tapBegin": "Tap to begin", "coverKicker": "The wedding of"},
    )))

# ============================================================ P7 Sakura Blush
BLUSH_BG = f"{noise_uri(.12, .7)},radial-gradient(ellipse at 30% 20%,#fff 0,transparent 50%),radial-gradient(ellipse at 80% 70%,#f9dfe3,transparent 55%),linear-gradient(#fdf1f2,#fae6e8)"
P.append(dict(
    slug="p07-sakura-blush", name="Sakura Blush", category="Premium · Watercolor floral",
    blurb="Blush watercolor paper, cherry-blossom branches and a gold-ringed monogram — pretty and playful.",
    theme_color="#c0647a",
    fonts="family=Great+Vibes&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@400;500",
    vars="--bg:#fdf3f4;--bg2:#fae8ea;--ink:#4a2f36;--muted:#8f6f77;--accent:#b85a72;--accent2:#c69a52;--gold:#c69a52;--gold-hi:#f1d9a3;--line:rgba(184,90,114,.25);--card:rgba(255,255,255,.8);--card-solid:#fffafa;--on-accent:#fff;--radius:18px;--in-radius:12px;"
         "--f-display:'Cormorant Garamond',serif;--f-script:'Great Vibes',cursive;--f-body:'Cormorant Garamond',serif;--f-native:'Cormorant Garamond',serif;--f-label:'Montserrat',sans-serif;"
         "--op-ink:#8f6f77;--op-names:#b85a72;--cv-btn:#fff;--cv-btn-bg:linear-gradient(135deg,#d57d93,#b85a72);--cv-btn-shadow:0 10px 24px -8px rgba(184,90,114,.7);"
         "--ph-bg:linear-gradient(160deg,#fbe3e7,#f2c9d1);--ph-ink:#b85a72;--ph-radius:16px",
    opener="cover",
    coverbg=f'<div class="blush"></div><div class="bb l">{blossom_branch("wb1")}</div><div class="bb r">{blossom_branch("wb2")}</div>',
    decor='<span class="pill-day" data-f="c.weekday"></span><p class="sd-script">Save the date</p><div class="mono-ring"><span data-f="c.monogram"></span></div>',
    icon=ICONS["heart"],
    hero=(f'<div class="blush"></div><div class="bb l">{blossom_branch("wb3")}</div><div class="bb r">{blossom_branch("wb4")}</div>'
          '<div class="hero-in">' + '<span class="pill-day h-in" style="--d:0" data-f="c.weekday"></span>'
          + '<p class="sd-script h-in" style="--d:1">Save the date</p>' + '<div class="mono-ring h-in" style="--d:2"><span data-f="c.monogram"></span></div>'
          + names(3) + T(4, "tagline", "tagline")
          + '<div class="date-badge h-in" style="--d:5"><span data-f="c.monthShort"></span><b data-f="c.day"></b></div>'
          + T(6, "venueLine", "h-venue") + '</div>'),
    divider=leaf_orn("#b85a72", "divider"), st_orn=leaf_orn("#c69a52"),
    ev_icon=f'<svg viewBox="-40 -40 80 80"><defs>{wc_filter("wbe", 3)}</defs>{blossom(0, 0, 1.1, "wbe")}</svg>',
    css=COMMON_HERO_CSS + """
.blush{position:absolute;inset:0;background:""" + BLUSH_BG + """}
.bb{position:absolute;top:-10px;width:min(250px,60vw)}.bb svg{width:100%;height:auto}
.bb.l{left:-30px}.bb.r{right:-30px;transform:scaleX(-1)}
.bb svg{animation:sway 7s ease-in-out infinite alternate;transform-origin:0 20%}
@keyframes sway{to{transform:rotate(2.5deg)}}
.pill-day{font-family:var(--f-label);font-size:.62rem;letter-spacing:.36em;text-transform:uppercase;color:var(--gold);border:1px solid var(--gold);border-radius:999px;padding:6px 18px;background:rgba(255,255,255,.6)}
.sd-script{font-family:var(--f-script);font-size:clamp(2.4rem,11vw,3.2rem);color:var(--gold);margin:14px 0 6px;line-height:1}
.mono-ring{width:150px;height:150px;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle,#fff 55%,#fdf0f1);box-shadow:0 0 0 6px #f7d9df,0 0 0 7px rgba(198,154,82,.6),0 18px 34px -14px rgba(184,90,114,.55);margin:8px 0 18px}
.mono-ring span{white-space:nowrap;font-family:var(--f-script);font-size:2.7rem;color:var(--gold)}
.op-cover .op-center{padding-top:8svh}
.hero{padding-top:90px}
.hero-in{position:relative;display:flex;flex-direction:column;align-items:center}
.names{font-size:clamp(2.9rem,12vw,4.4rem);line-height:1.1}
.names .amp{font-size:.6em;color:var(--gold);display:inline;margin:0 .1em}
.names>span{display:inline}
.date-badge{width:84px;height:84px;border-radius:50%;background:linear-gradient(145deg,#d57d93,#b0506a);color:#fff;display:grid;place-content:center;text-align:center;box-shadow:0 12px 24px -10px rgba(176,80,106,.8);margin:18px 0 6px}
.date-badge span{font-size:.6rem;letter-spacing:.3em;text-transform:uppercase}.date-badge b{font-weight:400;font-family:var(--f-display);font-size:1.7rem;line-height:1}
.sec:nth-of-type(even){background:var(--bg2)}
.st{font-family:var(--f-script);font-size:clamp(2.4rem,10vw,3.2rem);color:var(--accent);letter-spacing:0}
.event{box-shadow:0 20px 40px -30px rgba(184,90,114,.6)}
.ev-ico{width:48px;height:48px}
.btn{font-family:var(--f-label)}
""",
    theme={"particles": {"type": "flower", "colors": ["#fbd3da", "#f7c0cc", "#fde5ea"], "center": "#e8899f", "size": [5, 9], "count": 18, "speed": .6},
           "music": {"key": 67, "bpm": 72, "bell": True, "decay": 1.5}, "openMs": 1500},
    data=data(
        slug="janith-dulani", partner1="Janith", partner2="Dulani",
        fullName1="Janith Sahan Kulatunga", fullName2="Dulani Hasara Wijeratne",
        parents1="Son of Mr. & Mrs. Nihal Kulatunga", parents2="Daughter of Mr. & Mrs. Ranjith Wijeratne",
        tagline="Request the pleasure of your company at their wedding celebration",
        hostLine="With love and joy, together with our families",
        inviteText="Blossoms, laughter and the people we love most — come celebrate with us.",
        quote="In all the world, there is no heart for me like yours.", quoteSource="Maya Angelou",
        date="2026-12-27T19:00:00+05:30", venueLine="Cinnamon Grand · Colombo",
        events=[
            dict(name="Poruwa Ceremony", time="2026-12-27T17:30:00+05:30", timeLabel="Auspicious time · 5.30 p.m.", venue="Cinnamon Grand · Atrium", address="77 Galle Road, Colombo 03"),
            dict(name="Reception", time="2026-12-27T19:00:00+05:30", timeLabel="7.00 p.m. onwards", venue="Cinnamon Grand · Grand Ballroom", address="77 Galle Road, Colombo 03"),
        ],
        story=story("Colombo", "Ella", "Beira Lake"),
        venue=dict(name="Cinnamon Grand Colombo", address="77 Galle Road, Colombo 03", note="Enter from Galle Road; valet at the lobby.", embed=False),
        dressCode="Pastels and florals — blush, cream and gold.", dressColors=["#f6c3cd", "#fdf3f4", "#c69a52"],
        hashtag="#JanithDulaniBloom", blessing="",
        labels={"coverKicker": "The wedding of", "countdown": "Counting the days", "events": "Celebrations"},
    )))

# ============================================================ P8 Rose Garden
P.append(dict(
    slug="p08-rose-garden", name="Rose Garden", category="Premium · Watercolor floral",
    blurb="Cream paper with a lush watercolor bouquet of roses, anemones and eucalyptus.",
    theme_color="#b0605a",
    fonts="family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Cormorant+Garamond:ital,wght@0,400;1,400&family=Pinyon+Script",
    vars="--bg:#faf6f1;--bg2:#f4ede5;--ink:#3a2c2a;--muted:#8c7a74;--accent:#3a2c2a;--accent2:#b0605a;--gold:#c07a72;--gold-hi:#f4c9bf;--line:rgba(176,96,90,.25);--card:#fffdfa;--card-solid:#fffdfa;--on-accent:#fff;--radius:8px;"
         "--f-display:'Playfair Display',serif;--f-script:'Playfair Display',serif;--f-body:'Cormorant Garamond',serif;--f-native:'Cormorant Garamond',serif;--f-label:'Cormorant Garamond',serif;"
         "--op-ink:#9c7f78;--op-names:#3a2c2a;--e2-paper:" + noise_uri(.12, .9) + ",linear-gradient(170deg,#f3e6db,#ead8ca);--e2-flap:" + noise_uri(.12, .9) + ",linear-gradient(180deg,#f7ece3,#ecdccf);--e2-inner:#d9c3b3;--e2-ink:#9c5a54;"
         "--ph-bg:linear-gradient(160deg,#f5e6df,#ecd3cb);--ph-ink:#b0605a",
    opener="envelope2",
    coverbg=f'<div class="paper"></div><div class="cv-bq top">{bouquet("wr1")}</div><div class="cv-bq bot">{bouquet("wr2")}</div>',
    hero=('<div class="paper"></div>' + T(0, "tagline", "eyebrow") + names(1) + T(2, "hostShort", "tagline") + T(3, "c.weekday", "eyebrow wk")
          + T(4, "c.dateShort", "h-long") + T(5, "venueLine", "h-venue") + f'<div class="bq h-in" style="--d:6">{bouquet("wr3")}</div>'),
    divider=leaf_orn("#8fb08a", "divider"), st_orn=leaf_orn("#b0605a"),
    ev_icon=f'<svg viewBox="-45 -45 90 90"><defs>{wc_filter("wre", 3)}</defs>{rose(0, 0, .95, ("#fbd3cb", "#f0a79e", "#cf6f69", "#9a3f3d"), "wre")}</svg>',
    css=COMMON_HERO_CSS + """
.paper{position:absolute;inset:0;background:""" + f"{noise_uri(.1, .8)},radial-gradient(ellipse at 50% 30%,#fffdf9,#f6eee5)" + """}
.cv-bq{position:absolute;left:50%;width:min(460px,120vw);translate:-50% 0}.cv-bq svg{width:100%;height:auto}
.t-p08-rose-garden .op-env2 .op-center{padding-bottom:24svh}
.cv-bq.top{top:-215px;transform:rotate(180deg)}.cv-bq.bot{bottom:-190px}
.hero{justify-content:flex-start;padding-top:12svh;padding-bottom:0}
.hero .eyebrow{color:var(--accent2)}
.names{font-size:clamp(3rem,13vw,4.8rem);line-height:1.08;margin:8px 0}
.names .amp{font-family:'Pinyon Script',cursive;font-size:.5em;color:var(--accent2)}
.wk{margin-top:14px;margin-bottom:0}
.h-long{font-family:var(--f-display);font-size:1.4rem}
.bq{position:relative;width:min(460px,118vw);margin-top:auto}.bq svg{width:100%;height:auto}
.bq svg{animation:bloomin 2.2s .4s both}
@keyframes bloomin{from{transform:scale(.85) translateY(30px);opacity:0}}
.st em{font-style:italic;color:var(--accent2)}
.st{font-size:clamp(1.8rem,7vw,2.5rem)}
.sec:nth-of-type(even){background:var(--bg2)}
.ev-ico{width:60px;height:60px}
""",
    theme={"particles": {"type": "petal", "colors": ["#f6c0b6", "#fbd3cb", "#f0a79e"], "size": [5, 9], "count": 16, "flip": True, "speed": .55},
           "music": {"key": 65, "bpm": 66}, "openMs": 2600},
    seal_colors=("#e8a09a", "#b0605a", "#5e2522"), seal_emblem="tree",
    data=data(
        slug="supun-kaveesha", partner1="Kaveesha", partner2="Supun",
        fullName1="Kaveesha Nethmini Gunawardena", fullName2="Supun Tharindu Karunaratne",
        parents1="Daughter of Mr. & Mrs. Asoka Gunawardena", parents2="Son of Mr. & Mrs. Nimal Karunaratne",
        tagline="Together with their families", hostShort="request the honour of your presence at the celebration of their marriage",
        hostLine="With joyful hearts", inviteText="A seaside afternoon, a garden of roses and a promise we can't wait to make.",
        quote="Whatever our souls are made of, his and mine are the same.", quoteSource="Emily Brontë",
        date="2026-12-27T15:00:00+05:30", venueLine="Hikkaduwa Beach Resort",
        events=[
            dict(name="Ceremony", time="2026-12-27T15:00:00+05:30", timeLabel="3.00 p.m.", venue="Hikkaduwa Beach Resort · Garden", address="Galle Road, Hikkaduwa"),
            dict(name="Sunset Reception", time="2026-12-27T17:30:00+05:30", timeLabel="5.30 p.m. until late", venue="Hikkaduwa Beach Resort · Terrace", address="Hikkaduwa"),
        ],
        story=story("Galle", "Unawatuna", "Koggala Lake"),
        venue=dict(name="Hikkaduwa Beach Resort", address="Galle Road, Hikkaduwa", note="Free parking beside the resort.", embed=False),
        dressCode="Garden formal — soft pinks, creams and greens.", dressColors=["#f0a79e", "#faf6f1", "#8fb08a"],
        hashtag="#KaveeshaAndSupun", blessing="",
        labels={"countdown": "Until we say “I do”", "eventsKicker": "Counting the days", "dearGuest": "Our Dear Guest"},
    )))

# ============================================================ P9 Blue Hydrangea
P.append(dict(
    slug="p09-blue-hydrangea", name="Blue Hydrangea", category="Premium · Watercolor floral",
    blurb="Soft cream paper framed by dusty-blue hydrangeas, navy italic names and a faded couple photo.",
    theme_color="#34466b",
    fonts="family=Playfair+Display:ital,wght@0,400;1,400;1,500&family=Inter:wght@300;400&family=Cormorant+Garamond:ital,wght@0,400;1,400",
    vars="--bg:#fbf8f2;--bg2:#f2f1ec;--ink:#28324a;--muted:#6f778a;--accent:#34466b;--accent2:#b99a58;--gold:#b99a58;--gold-hi:#f0dfb0;--line:rgba(52,70,107,.2);--card:#ffffff;--card-solid:#fff;--on-accent:#fff;--radius:12px;--in-radius:8px;"
         "--f-display:'Playfair Display',serif;--f-script:'Playfair Display',serif;--f-body:'Cormorant Garamond',serif;--f-native:'Cormorant Garamond',serif;--f-label:'Inter',sans-serif;"
         "--op-ink:#6f778a;--op-names:#34466b;--cv-btn:#fff;--cv-btn-bg:linear-gradient(90deg,#8193b3,#34466b);--cv-btn-shadow:0 12px 26px -10px rgba(52,70,107,.8);"
         "--ph-bg:linear-gradient(160deg,#e6ebf3,#d2dbea);--ph-ink:#34466b;--ph-radius:12px",
    opener="cover",
    coverbg=f'<div class="paper2"></div><div class="hc tl">{hydra_corner("wh1")}</div><div class="hc br">{hydra_corner("wh2")}</div><div class="ghost ph" data-photo="couplePhoto"></div>',
    decor='',
    icon="",
    hero=(f'<div class="paper2"></div><div class="hc tl">{hydra_corner("wh3")}</div><div class="hc br">{hydra_corner("wh4")}</div>'
          + T(0, "labels.invited2", "eyebrow") + '<h1 class="names h-in" style="--d:1"><span data-f="partner1"></span><span class="amp">&amp;</span><span data-f="partner2"></span></h1>'
          + f'<span class="cv-rule h-in" style="--d:2"><i></i></span>' + T(3, "labels.envLine", "tagline") + hdate(4) + T(5, "venueLine", "h-venue")),
    divider=diamond_orn("#b99a58", "divider"), st_orn=diamond_orn("#b99a58"),
    ev_icon=f'<svg viewBox="-40 -40 80 80"><defs>{wc_filter("whe", 3)}</defs>{hydrangea(0, 0, .95, "whe")}</svg>',
    css=COMMON_HERO_CSS + """
.paper2{position:absolute;inset:0;background:""" + f"{noise_uri(.08, .8)},radial-gradient(ellipse at 50% 40%,#fffdf9,#f5f1e8)" + """}
.hc{position:absolute;width:min(230px,56vw)}.hc svg{width:100%;height:auto}
.hc.tl{top:-20px;left:-30px}.hc.br{bottom:-20px;right:-30px;transform:rotate(180deg)}
.hc svg{animation:sway 8s ease-in-out infinite alternate;transform-origin:20% 20%}
@keyframes sway{to{transform:rotate(3deg)}}
.ghost{position:absolute;left:50%;bottom:0;width:min(360px,90vw);height:34svh;translate:-50% 0;border-radius:0;opacity:.18;-webkit-mask:linear-gradient(transparent,#000 60%);mask:linear-gradient(transparent,#000 60%)}
.ghost.empty::before,.ghost.empty::after{display:none}
.cv-names{font-family:'Playfair Display',serif;font-style:italic;font-size:clamp(2.8rem,12vw,3.8rem);display:flex;flex-direction:column;line-height:1.1}
.cv-names em{font-family:'Playfair Display',serif;font-size:.6em;color:#b99a58}
.cv-btn{border:0;letter-spacing:.34em}
.names{font-style:italic;font-weight:400;font-size:clamp(3rem,13vw,4.6rem);line-height:1.1}
.names .amp{font-size:.55em;color:var(--gold)}
.st{font-style:italic;font-size:clamp(1.9rem,7.5vw,2.6rem)}
.sec:nth-of-type(even){background:var(--bg2)}
.eyebrow{color:var(--muted)}
.ev-ico{width:50px;height:50px}
.btn{font-family:var(--f-label);letter-spacing:.24em}
""",
    theme={"particles": {"type": "petal", "colors": ["#c9d7ef", "#dde6f5", "#ffffff"], "size": [4, 8], "count": 14, "flip": True, "speed": .5},
           "music": {"key": 64, "bpm": 60, "bell": True}, "openMs": 1500},
    data=data(
        slug="shanil-rashmi", partner1="Rashmi", partner2="Shanil",
        fullName1="Rashmi Anjalika Fernando", fullName2="Shanil Dimuth Mendis",
        parents1="Daughter of Mr. & Mrs. Clarence Fernando", parents2="Son of Mr. & Mrs. Ivan Mendis",
        hostLine="Together with their families", inviteText="A little invitation, made just for you — we hope you'll celebrate with us.",
        quote="Love is patient, love is kind.", quoteSource="1 Corinthians 13:4",
        date="2027-02-13T16:00:00+05:30", venueLine="Galle Face Hotel · Colombo",
        events=[
            dict(name="Wedding Ceremony", time="2027-02-13T16:00:00+05:30", timeLabel="4.00 p.m.", venue="St. Mary's Church", address="Dehiwala"),
            dict(name="Reception", time="2027-02-13T19:00:00+05:30", timeLabel="7.00 p.m. onwards", venue="Galle Face Hotel · Regency Ballroom", address="2 Galle Road, Colombo 03"),
        ],
        story=story("Colombo", "Kalpitiya", "Diyawanna Oya"),
        venue=dict(name="Galle Face Hotel", address="2 Galle Road, Colombo 03", note="Parking available at the Galle Face Green car park.", embed=False),
        dressCode="Formal — dusty blues, navy and ivory.", dressColors=["#34466b", "#c9d7ef", "#fbf8f2"],
        hashtag="#RashmiAndShanil", blessing="",
        labels={"coverKicker": "You are invited", "envLine": "A little invitation, made just for you.", "openBtn": "Open invitation", "invited2": "You are invited"},
    )))

# ============================================================ P10 Ivory Lattice
G = "#b8913f"
P.append(dict(
    slug="p10-ivory-lattice", name="Ivory Lattice", category="Premium · Minimal traditional",
    blurb="Crisp ivory with a faint gold lattice, a fine gold frame and a slot for your couple illustration.",
    theme_color="#8a6a2a",
    fonts="family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,400&family=Cinzel:wght@400&family=Noto+Serif+Sinhala:wght@400",
    vars="--bg:#fdfbf6;--bg2:#f7f2e7;--ink:#2e2418;--muted:#7a6a55;--accent:#2e2418;--accent2:#8a6a2a;--gold:#b8913f;--gold-hi:#f2dca2;--line:rgba(184,145,63,.4);--card:#fffefb;--card-solid:#fffefb;--on-accent:#fff;--radius:2px;"
         "--f-display:'Cormorant Garamond',serif;--f-script:'Cormorant Garamond',serif;--f-body:'Cormorant Garamond',serif;--f-native:'Noto Serif Sinhala',serif;--f-label:'Cinzel',serif;"
         "--op-ink:#8a6a2a;--op-names:#2e2418;--cv-btn:#8a6a2a;"
         "--ph-bg:linear-gradient(160deg,#f7efdd,#ecdcb9);--ph-ink:#8a6a2a;--ph-radius:2px",
    opener="cover",
    coverbg='<div class="lattice"></div><div class="gframe"></div>',
    icon=ICONS["mail"],
    hero=('<div class="lattice"></div><div class="gframe"></div>' + T(0, "tagline", "eyebrow")
          + f'<div class="h-in" style="--d:1">{diamond_orn(G, "divider sm")}</div>'
          + '<h1 class="names h-in" style="--d:2"><span data-f="partner1"></span> <span class="amp">&amp;</span> <span data-f="partner2"></span></h1>'
          + f'<div class="h-in" style="--d:3">{diamond_orn(G, "divider sm")}</div>' + T(4, "hostShort", "tagline")
          + T(5, "c.weekday", "eyebrow wk") + T(6, "c.dateOrdShort", "big-date") + T(7, "timeLine", "eyebrow") + T(8, "venueLine", "h-venue")
          + f'<div class="hero-art h-in" style="--d:9"><div class="ph" data-photo="heroImage"></div><div class="art-fallback">{punkalasa(G)}</div></div>'),
    divider=diamond_orn(G, "divider"), st_orn=diamond_orn(G), ev_icon=punkalasa(G),
    css=COMMON_HERO_CSS + """
.lattice{position:absolute;inset:0;background:""" + star8_tile("rgba(184,145,63,.13)", 56) + """}
.gframe{position:absolute;inset:18px;border:1.5px solid rgba(184,145,63,.8);pointer-events:none}
.op-cover .op-center{gap:0}
.cv-names{font-family:'Cormorant Garamond',serif;font-weight:400;font-size:clamp(2.4rem,10vw,3rem)}
.hero{justify-content:flex-start;padding:12svh 36px 0}
.divider.sm{width:110px;margin:16px auto}
.names{font-weight:400;font-size:clamp(2.2rem,10vw,3.4rem);line-height:1.2}
.names>span{display:inline}.names .amp{display:inline;font-style:italic;font-size:.8em}
.wk{margin-top:18px;margin-bottom:4px}
.big-date{font-style:italic;font-size:clamp(1.9rem,8vw,2.6rem);line-height:1.2}
.hero-art{position:relative;width:min(260px,64vw);margin-top:auto;padding-top:20px}
.hero-art .ph{aspect-ratio:3/4;background-color:transparent}
.hero-art .ph.empty{display:none}
.hero-art .ph:not(.empty)+.art-fallback{display:none}
.art-fallback{width:120px;margin:10px auto 26px;opacity:.9}
.st{font-weight:400;font-size:clamp(1.9rem,7.5vw,2.6rem)}
.sec:nth-of-type(even){background:var(--bg2)}
.event{border:1px solid var(--line)}
.ev-ico{width:44px;height:56px}
""",
    theme={"particles": {"type": "sparkle", "colors": ["#e8cf8f", "#b8913f"], "size": [2, 5], "count": 14, "speed": .3, "mode": "twinkle", "glow": 5},
           "music": {"key": 62, "bpm": 60}, "openMs": 1500},
    data=data(
        slug="nuwan-chathurika", partner1="Nuwan", partner2="Chathurika",
        fullName1="Nuwan Isuru Samarakoon", fullName2="Chathurika Madhavi Alwis",
        parents1="Son of Mr. & Mrs. Piyadasa Samarakoon", parents2="Daughter of Mr. & Mrs. Hemantha Alwis",
        tagline="Together with their families", hostShort="Request the honour of your presence at the celebration of their marriage",
        timeLine="At 10.30 a.m.", hostLine="With the blessings of our parents",
        inviteText="Please join us for the poruwa ceremony followed by lunch.",
        quote="Two souls with but a single thought, two hearts that beat as one.", quoteSource="Friedrich Halm",
        date="2026-12-27T10:30:00+05:30", venueLine="Grand Monarch · Colombo",
        events=[
            dict(name="Poruwa Ceremony", time="2026-12-27T10:30:00+05:30", timeLabel="Auspicious time · 10.30 a.m.", venue="Grand Monarch", address="Thalawathugoda"),
            dict(name="Luncheon", time="2026-12-27T12:30:00+05:30", timeLabel="12.30 p.m. onwards", venue="Grand Monarch · Ballroom", address="Thalawathugoda"),
        ],
        story=story("Colombo", "Kitulgala", "Diyawanna Lake"),
        venue=dict(name="Grand Monarch", address="Thalawathugoda, Colombo", note="Parking available on site.", embed=False),
        dressCode="Traditional or formal — ivory and gold.", dressColors=["#fdfbf6", "#b8913f", "#2e2418"],
        hashtag="#NuwanChathurika", blessing="තෙරුවන් සරණයි",
    )))
