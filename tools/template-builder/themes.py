"""The 15 theme definitions."""
from orn import *

COMMON_HERO_CSS = """
.h-date{display:flex;align-items:center;justify-content:center;gap:14px;margin:18px auto 6px;font-family:var(--f-display);color:var(--ink)}
.hd-side{font-size:.74rem;letter-spacing:.24em;text-transform:uppercase;padding:8px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);min-width:104px}
.hd-day{font-size:3.1rem;line-height:1;color:var(--accent)}
.h-venue{font-size:.8rem;letter-spacing:.26em;text-transform:uppercase;color:var(--muted);margin-top:12px;max-width:340px}
.tagline{font-style:italic;color:var(--muted);margin:8px auto 4px;font-size:1.06rem;max-width:360px}
.scroll-hint{position:absolute;bottom:22px;left:50%;width:22px;height:36px;margin-left:-11px;border:1px solid var(--line);border-radius:12px}
.scroll-hint::after{content:"";position:absolute;left:50%;top:7px;width:3px;height:7px;margin-left:-1.5px;border-radius:2px;background:var(--gold);animation:sh 1.8s infinite}
@keyframes sh{0%{opacity:0;transform:translateY(0)}40%{opacity:1}100%{opacity:0;transform:translateY(12px)}}
"""


def hdate(d):
    return (f'<div class="h-date h-in" style="--d:{d}"><span class="hd-side" data-f="c.weekday"></span>'
            f'<span class="hd-day" data-f="c.day"></span><span class="hd-side"><span data-f="c.monthShort"></span> <span data-f="c.year"></span></span></div>')


def names(d, cls="names"):
    return (f'<h1 class="{cls} h-in" style="--d:{d}"><span data-f="partner1"></span>'
            f'<span class="amp">&amp;</span><span data-f="partner2"></span></h1>')


def T(d, key, cls="", tag="p"):
    return f'<{tag} class="{cls} h-in" style="--d:{d}" data-f="{key}"></{tag}>'


def zwj(s):
    return s.replace("{zwj}", "‍")


RSVP = {"deadline": "2027-01-20", "whatsapp": "94770000000", "endpoint": "", "maxGuests": 6}
BRAND = "Digital invitation · yourbrand.lk"

THEMES = []

# ---------------------------------------------------------------- 1
G = "#b0822a"
THEMES.append(dict(
    slug="01-poruwa-heritage", name="Poruwa Heritage", category="Traditional · Sinhala Buddhist",
    blurb="Maroon and temple gold with liyawel scrolls, oil lamps and a slow-turning lotus mandala.",
    theme_color="#6e161b",
    fonts="family=Cinzel:wght@400;600&family=Pinyon+Script&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Abhaya+Libre:wght@500;700",
    vars="--bg:#fbf4e6;--bg2:#f5e8cf;--ink:#3a1b12;--muted:#7a5a48;--accent:#7b1e22;--accent2:#9a3b1f;--gold:#b0822a;--gold-hi:#f7e0a0;--line:rgba(176,130,42,.5);--card:rgba(255,252,244,.8);--card-solid:#fffaf0;--on-accent:#fff6e2;--radius:2px;"
         "--f-display:'Cinzel',serif;--f-script:'Pinyon Script',cursive;--f-body:'Cormorant Garamond',serif;--f-native:'Abhaya Libre',serif;"
         "--op-bg:#6e161b " + flower_tile("rgba(240,200,120,.22)") + ";--op-line:rgba(240,200,120,.55);--op-ink:#f7e2b0;--seal:#b0822a;--seal-hi:#f3d68a;--seal-lo:#6f4c10;--seal-ink:#4a0f12",
    opener="doors",
    opener_decor=f'<div style="width:70%;opacity:.85">{mandala("#e8c178", "#e8c178", "spin-slow")}</div>',
    hero=(f'<div class="frame">{corner(G, "corner c1")}{corner(G, "corner c2")}{corner(G, "corner c3")}{corner(G, "corner c4")}</div>'
          f'<div class="h-mandala">{mandala(G, "#7b1e22", "spin-slow")}</div>'
          f'<div class="h-top h-in" style="--d:0">{lamp(G, "fl1a")}<p class="native gr" data-f="nativeGreeting"></p>{lamp(G, "fl1b")}</div>'
          + T(1, "greeting", "kicker") + T(2, "tagline", "tagline") + names(3, "names")
          + f'<div class="h-in" style="--d:4">{liyawel(G)}</div>' + hdate(5) + T(6, "venueLine", "h-venue")
          + '<span class="scroll-hint"></span>'),
    divider=liyawel(G), st_orn=small_lotus(G), ev_icon=lotus("#f3d9a4", "#e9c47f", G),
    css=COMMON_HERO_CSS + """
.hero{background:radial-gradient(ellipse at 50% 40%,#fffaf0 0,#fbf4e6 45%,#f1e0bf 100%)}
.frame{position:absolute;inset:14px;border:1px solid var(--line);pointer-events:none}
.frame::after{content:"";position:absolute;inset:6px;border:1px solid var(--line)}
.corner{position:absolute;width:84px;height:84px}.c1{top:-2px;left:-2px}.c2{top:-2px;right:-2px;transform:scaleX(-1)}.c3{bottom:-2px;left:-2px;transform:scaleY(-1)}.c4{bottom:-2px;right:-2px;transform:scale(-1)}
.h-mandala{position:absolute;width:min(560px,125vw);aspect-ratio:1;left:50%;top:50%;translate:-50% -50%;opacity:.13;pointer-events:none}
.h-mandala svg{width:100%;height:100%}
.h-top{display:flex;align-items:flex-end;justify-content:center;gap:20px}
.h-top .lamp{width:38px;height:auto}
.gr{font-size:clamp(2rem,9vw,2.8rem);color:var(--accent);line-height:1}
.names{margin:6px 0 0}
.names .amp{font-family:var(--f-display);font-size:.32em;letter-spacing:.3em;margin:6px 0}
.sec:nth-of-type(even){background:var(--bg2)}
.quote blockquote{color:var(--accent)}
.event{border-top:3px double var(--gold)}
.cd-box{border-color:var(--gold)}
""",
    theme={"particles": {"type": "petal", "colors": ["#b3342b", "#e8a33d", "#f3c96b", "#c0892f"], "size": [5, 10], "count": 26, "flip": True, "speed": .9}},
    data=dict(
        slug="chamath-nethmi", partner1="Chamath", partner2="Nethmi",
        fullName1="Chamath Dilshan Wijesinghe", fullName2="Nethmi Sanduni Karunaratne",
        parents1="Beloved son of Mr. & Mrs. Sunil Wijesinghe, Kurunegala",
        parents2="Beloved daughter of Mr. & Mrs. Ananda Karunaratne, Kandy",
        nativeGreeting="ආයුබෝවන්", greeting="Ayubowan", tagline="You are warmly invited to the wedding of",
        hostLine="With the blessings of the Noble Triple Gem, and together with our families, we request the pleasure of your company",
        inviteText="Join us as we step onto the poruwa and begin our life together — your presence will make our day complete.",
        quote="Two hearts, one path — may our journey be guided by kindness, patience and compassion.", quoteSource="Our promise",
        date="2027-02-18T09:47:00+05:30", venueLine="Earl's Regency · Kandy",
        events=[
            dict(name="Poruwa Ceremony", native=zwj("පෝරුව චාරිත්{zwj}රය"), time="2027-02-18T09:47:00+05:30", timeLabel="Auspicious time · 9.47 a.m.",
                 venue="Earl's Regency Hotel", address="Tennekumbura, Kandy", note="Kindly be seated by 9.15 a.m."),
            dict(name="Wedding Reception", native="මංගල සාදය", time="2027-02-18T12:00:00+05:30", timeLabel="12.00 noon onwards",
                 venue="Earl's Regency Hotel · Grand Ballroom", address="Tennekumbura, Kandy"),
            dict(name="Homecoming", time="2027-02-21T19:00:00+05:30", timeLabel="7.00 p.m. onwards", venue="Cinnamon Lakeside", address="Colombo 02"),
        ],
        dressCode="Traditional or formal attire — ivory, gold and deep maroon tones are welcome.", dressColors=["#7b1e22", "#b0822a", "#f5e8cf"],
        hashtag="#ChamathWedsNethmi", blessing="තෙරුවන් සරණයි", rsvp=dict(RSVP), brand=BRAND,
        labels={"countdown": "Counting down to the nekath", "events": "The Auspicious Day"},
    )))

# ---------------------------------------------------------------- 2
G = "#d9b25f"
THEMES.append(dict(
    slug="02-kandyan-royal", name="Kandyan Royal", category="Traditional · Luxury",
    blurb="Deep oxblood velvet, a gilded pun kalasa and shimmering gold script behind a theatre-curtain reveal.",
    theme_color="#3d0b0e",
    fonts="family=Cinzel+Decorative:wght@400;700&family=Alex+Brush&family=Marcellus&family=Noto+Serif+Sinhala:wght@400;600",
    vars="--bg:#3d0b0e;--bg2:#4a1014;--ink:#f6e6c4;--muted:#d8bf94;--accent:#f0cf85;--accent2:#f6e6c4;--gold:#d9b25f;--gold-hi:#fff2c4;--line:rgba(217,178,95,.5);--card:rgba(255,230,180,.06);--card-solid:#fdf3de;--on-accent:#3d0b0e;--radius:0;--input-bg:rgba(0,0,0,.2);"
         "--f-display:'Cinzel Decorative',serif;--f-script:'Alex Brush',cursive;--f-body:'Marcellus',serif;--f-native:'Noto Serif Sinhala',serif;"
         "--op-back:#1d0506;--cur:linear-gradient(90deg,rgba(0,0,0,.35),transparent 30%,rgba(255,255,255,.06) 50%,transparent 70%,rgba(0,0,0,.35)) 0 0/44px 100%,#7a1016;"
         "--valance:radial-gradient(circle at 50% 0,#f3d27a 0 7px,transparent 8px) 0 62px/28px 14px repeat-x,linear-gradient(#5a0b10,#8c1a1f 80%,#d9b25f 80% 86%,#5a0b10 86%);"
         "--op-ink:#f6e0a4;--seal:#a8141c;--seal-hi:#e0434b;--seal-lo:#5a0508;--seal-ink:#f6d98f",
    opener="curtain", opener_decor="",
    hero=(f'<div class="pat"></div><div class="royal">'
          f'<div class="h-in" style="--d:0">{punkalasa(G)}</div>'
          + T(1, "nativeGreeting", "native gr") + T(2, "tagline", "tagline") + names(3, "names shimmer")
          + f'<div class="h-in" style="--d:4">{liyawel(G)}</div>' + hdate(5) + T(6, "venueLine", "h-venue") + '</div>'),
    divider=liyawel(G), st_orn=diamond_orn(G), ev_icon=punkalasa(G),
    css=COMMON_HERO_CSS + """
.hero{background:radial-gradient(ellipse at 50% 35%,#6a1419,#3d0b0e 60%,#240507)}
.pat{position:absolute;inset:0;background:""" + flower_tile("rgba(217,178,95,.10)") + """;opacity:.9}
.royal{position:relative;border:1px solid var(--line);outline:1px solid var(--line);outline-offset:6px;padding:34px 18px 30px;max-width:520px;width:100%}
.royal::before,.royal::after{content:"◆";position:absolute;left:50%;translate:-50% 0;color:var(--gold);font-size:12px;background:#4a0e12;padding:0 8px}
.royal::before{top:-10px}.royal::after{bottom:-10px}
.punkalasa{width:92px;margin:0 auto 6px;filter:drop-shadow(0 0 16px rgba(240,200,110,.45))}
.gr{font-size:clamp(1.3rem,5.6vw,1.7rem);color:var(--gold)}
.names{font-size:clamp(3.2rem,15vw,6rem)}
.names .amp{font-family:var(--f-display);font-size:.3em;letter-spacing:.2em}
.hd-day{color:var(--gold)}
.sec:nth-of-type(even){background:var(--bg2)}
.st{color:var(--gold)}
.event{outline:1px solid var(--line);outline-offset:-8px}
.ev-ico{width:48px;height:60px}
.btn{--on-accent:#3d0b0e}
footer{background:#240507}
""",
    theme={"particles": {"type": "glitter", "colors": ["#f3d27a", "#d9b25f", "#fff2c4"], "size": [2, 5], "count": 45, "flip": True, "speed": .6, "glow": 6}, "openMs": 1800},
    data=dict(
        slug="isuru-hiruni", partner1="Isuru", partner2="Hiruni",
        fullName1="Isuru Madushanka Ekanayake", fullName2="Hiruni Dilhara Senanayake",
        parents1="Son of Mr. & Mrs. Gamini Ekanayake, Matale", parents2="Daughter of Mr. & Mrs. Upali Senanayake, Kandy",
        nativeGreeting=zwj("ශුභ විවාහ මංගල්{zwj}යය"), tagline="Request the honour of your presence at the Kandyan wedding of",
        hostLine="Mr. & Mrs. Gamini Ekanayake and Mr. & Mrs. Upali Senanayake cordially invite you to celebrate the union of their children",
        inviteText="A day of drums, tradition and togetherness — we would be honoured to have you with us.",
        quote="Where tradition meets forever, two families become one.", quoteSource="Isuru & Hiruni",
        date="2027-04-22T10:21:00+05:30", venueLine="Mahaweli Reach · Kandy",
        events=[
            dict(name="Poruwa Ceremony", native=zwj("පෝරුව චාරිත්{zwj}රය"), time="2027-04-22T10:21:00+05:30", timeLabel="Nekath · 10.21 a.m.", venue="Mahaweli Reach Hotel", address="35 P.B.A. Weerakoon Mawatha, Kandy", note="Kandyan dancers will welcome the couple at 9.45 a.m."),
            dict(name="Reception", native="මංගල සාදය", time="2027-04-22T12:30:00+05:30", timeLabel="12.30 p.m. onwards", venue="Mahaweli Reach Hotel · Ballroom", address="Kandy"),
            dict(name="Homecoming", time="2027-04-25T19:00:00+05:30", timeLabel="7.00 p.m. onwards", venue="The Kingsbury", address="48 Janadhipathi Mawatha, Colombo 01"),
        ],
        dressCode="Osariya, national dress or formal evening wear.", dressColors=["#7a1016", "#d9b25f", "#f6e6c4"],
        hashtag="#IsuruHiruniForever", blessing="තෙරුවන් සරණයි", rsvp=dict(RSVP), brand=BRAND,
        labels={"events": "Royal Celebrations"},
    )))

# ---------------------------------------------------------------- 3
THEMES.append(dict(
    slug="03-nelum-lotus-pond", name="Nelum Lotus Pond", category="Traditional · Pastel",
    blurb="Soft blush and jade, a lotus blooming from rippling water, falling pink petals.",
    theme_color="#e8a0b4",
    fonts="family=Parisienne&family=Cormorant:ital,wght@0,400;0,500;1,400&family=Jost:wght@300;400&family=Abhaya+Libre:wght@500",
    vars="--bg:#fdf6f5;--bg2:#f6ecee;--ink:#4a3a40;--muted:#8d7880;--accent:#b8577a;--accent2:#4f8a82;--gold:#c9a15a;--gold-hi:#f4dca6;--line:rgba(184,87,122,.28);--card:#fffafa;--card-solid:#fffafa;--on-accent:#fff;--radius:18px;--in-radius:12px;"
         "--f-display:'Cormorant',serif;--f-script:'Parisienne',cursive;--f-body:'Jost',sans-serif;--f-native:'Abhaya Libre',serif;"
         "--op-bg:radial-gradient(circle at 50% 30%,#fff,#f6dde3);--env-back:#e6a3b5;--env-front:linear-gradient(160deg,#f3c2cf,#e9a9ba);--env-flap:linear-gradient(#f7d2dc,#eeb3c3);--op-ink:#8e3f5c;--seal:#b8577a;--seal-hi:#e28aa9;--seal-lo:#7a2d4a;--seal-ink:#fff3f6",
    opener="envelope", opener_decor=f'<div style="width:70px;margin:0 auto">{lotus("#f7c6d4", "#eea7bc", "#b8577a")}</div>',
    hero=(T(0, "nativeGreeting", "native gr") + T(1, "tagline", "tagline") + names(2) + hdate(3) + T(4, "venueLine", "h-venue")
          + f'<div class="pond"><div class="rip r1"></div><div class="rip r2"></div><div class="rip r3"></div>'
          f'<div class="big-lotus">{lotus("#f7c6d4", "#eea7bc", "#c46a88")}</div>'
          f'<div class="pad p1"></div><div class="pad p2"></div></div>'),
    divider=leaf_orn("#b8577a", "divider"), st_orn=small_lotus("#b8577a"), ev_icon=lotus("#f7c6d4", "#eea7bc", "#c46a88"),
    css=COMMON_HERO_CSS + """
.hero{justify-content:flex-start;padding-top:12svh;background:linear-gradient(#fff 0,#fdf1f3 55%,#e5f0ec 100%)}
.gr{font-size:clamp(1.5rem,6vw,2rem);color:var(--accent2)}
.names{color:var(--accent);font-size:clamp(3.2rem,15vw,6rem)}
.names .amp{font-family:var(--f-display);font-style:italic;color:var(--accent2)}
.hd-side{border-color:var(--line)}
.pond{position:absolute;left:0;right:0;bottom:0;height:30svh;min-height:190px;background:linear-gradient(#cfe5df,#a9cfc6);border-radius:50% 50% 0 0/22% 22% 0 0}
.rip{position:absolute;left:50%;top:44%;width:180px;height:44px;margin:-22px 0 0 -90px;border:1.5px solid rgba(255,255,255,.7);border-radius:50%;animation:rip 4.5s ease-out infinite}
.r2{animation-delay:1.5s}.r3{animation-delay:3s}
@keyframes rip{from{transform:scale(.5);opacity:.9}to{transform:scale(2.4);opacity:0}}
.big-lotus{position:absolute;left:50%;top:-18%;width:min(220px,56vw);translate:-50% 0;transform-origin:50% 100%;animation:bloom 2.4s 1s cubic-bezier(.2,.8,.2,1) both,bob 5s 3.4s ease-in-out infinite}
body:not(.opened) .big-lotus{animation-play-state:paused}
@keyframes bloom{from{transform:scale(.2) translateY(40px);opacity:0}to{transform:none;opacity:1}}
@keyframes bob{50%{transform:translateY(-6px)}}
.pad{position:absolute;width:110px;height:34px;border-radius:50%;background:radial-gradient(ellipse at 40% 40%,#7fb49f,#4f8a74);clip-path:polygon(0 0,46% 0,50% 50%,54% 0,100% 0,100% 100%,0 100%)}
.p1{left:8%;top:44%}.p2{right:6%;top:62%;width:80px;height:26px}
.sec:nth-of-type(even){background:var(--bg2)}
.event{box-shadow:0 18px 40px -26px rgba(184,87,122,.45)}
.ev-ico{width:74px;height:50px}
""",
    theme={"particles": {"type": "petal", "colors": ["#f6b8c9", "#f2a3ba", "#fbd3de", "#e98aa6"], "size": [5, 10], "count": 22, "flip": True, "speed": .8}, "openMs": 2000},
    data=dict(
        slug="ravindu-sanduni", partner1="Ravindu", partner2="Sanduni",
        fullName1="Ravindu Pramod Jayawardena", fullName2="Sanduni Imasha Gunasekara",
        parents1="Son of Mr. & Mrs. Nimal Jayawardena, Maharagama", parents2="Daughter of Mr. & Mrs. Kamal Gunasekara, Kottawa",
        nativeGreeting="මංගල ආරාධනය", tagline="Together with our families, we invite you to celebrate the marriage of",
        hostLine="With joyful hearts and the blessings of our parents",
        inviteText="Like the lotus that rises gently above the water, may our love grow pure and strong. Please bless us with your presence.",
        quote="Like the lotus, may our love rise above everything and bloom.", quoteSource="Ravindu & Sanduni",
        date="2027-03-11T08:34:00+05:30", venueLine="Waters Edge · Battaramulla",
        events=[
            dict(name="Poruwa Ceremony", time="2027-03-11T08:34:00+05:30", timeLabel="Auspicious time · 8.34 a.m.", venue="Waters Edge", address="316 Ethul Kotte Road, Battaramulla"),
            dict(name="Wedding Luncheon", time="2027-03-11T12:00:00+05:30", timeLabel="12.00 noon onwards", venue="Waters Edge · Lotus Ballroom", address="Battaramulla"),
        ],
        dressCode="Pastels and soft florals — think blush, jade and ivory.", dressColors=["#f6b8c9", "#a9cfc6", "#fdf6f5"],
        hashtag="#RaviSanduLotus", blessing="තෙරුවන් සරණයි", rsvp=dict(RSVP), brand=BRAND,
        labels={"countdown": "Until our lotus blooms"},
    )))

# ---------------------------------------------------------------- 4
THEMES.append(dict(
    slug="04-araliya-garden", name="Araliya Garden", category="Traditional · Floral",
    blurb="Fresh white and leaf green, swaying frangipani clusters, falling araliya blossoms.",
    theme_color="#3f5e45",
    fonts="family=Great+Vibes&family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Lora:ital,wght@0,400;1,400&family=Abhaya+Libre:wght@500",
    vars="--bg:#fffdf7;--bg2:#f3f5ec;--ink:#2e3a2f;--muted:#6b7a6c;--accent:#3f5e45;--accent2:#b8860b;--gold:#c99a2e;--gold-hi:#f4d88a;--line:rgba(63,94,69,.25);--card:#ffffff;--card-solid:#fff;--on-accent:#fffdf7;--radius:10px;--in-radius:8px;"
         "--f-display:'Playfair Display',serif;--f-script:'Great Vibes',cursive;--f-body:'Lora',serif;--f-native:'Abhaya Libre',serif;"
         "--op-bg:#e9eee2;--env-back:#5d7a60;--env-front:linear-gradient(160deg,#7c9a7c,#627f63);--env-flap:linear-gradient(#8fae8d,#6f8e6f);--op-ink:#3f5e45;--seal:#c99a2e;--seal-hi:#f3d27a;--seal-lo:#7f5e12;--seal-ink:#fffdf7",
    opener="envelope", opener_decor=f'<div style="width:60px;margin:0 auto 4px">{frangi_cluster("", "fgo")}</div>',
    hero=(f'<div class="fc tl">{frangi_cluster("frangi", "fg1")}</div><div class="fc br">{frangi_cluster("frangi", "fg2")}</div>'
          + T(0, "nativeGreeting", "native gr") + T(1, "tagline", "kicker") + names(2) + T(3, "c.dateLong", "h-long")
          + f'<div class="h-in" style="--d:4">{leaf_orn("#3f5e45", "divider")}</div>' + T(5, "venueLine", "h-venue")),
    divider=leaf_orn("#3f5e45", "divider"), st_orn=leaf_orn("#c99a2e"), ev_icon=frangi_cluster("", "fge"),
    css=COMMON_HERO_CSS + """
.hero{background:radial-gradient(circle at 50% 50%,#fff 0,#fffdf7 50%,#f1f4e8 100%)}
.fc{position:absolute;width:min(380px,78vw);pointer-events:none}
.fc .frangi{width:100%;height:auto;animation:sway 7s ease-in-out infinite;transform-origin:20% 20%}
.tl{top:-40px;left:-50px}.br{bottom:-50px;right:-60px;transform:rotate(180deg);width:min(300px,60vw)}
.br .frangi{animation-delay:-3s}
@keyframes sway{50%{transform:rotate(4deg) scale(1.02)}}
.gr{color:var(--accent2);font-size:1.4rem}
.kicker{margin-top:8px}
.names{margin:10px 0;font-size:clamp(3.4rem,16vw,6.4rem)}
.names .amp{font-family:var(--f-display);font-style:italic;font-size:.34em;color:var(--gold)}
.h-long{font-family:var(--f-display);font-style:italic;font-size:1.2rem}
.sec:nth-of-type(even){background:var(--bg2)}
.event{box-shadow:0 20px 40px -30px rgba(63,94,69,.6)}
.ev-ico{width:64px;height:64px}
.quote blockquote{color:var(--accent)}
""",
    theme={"particles": {"type": "flower", "colors": ["#ffffff", "#fff8e6", "#fdf1d2"], "center": "#f2b705", "size": [7, 12], "count": 16, "speed": .7, "alpha": .95}},
    data=dict(
        slug="sahan-tharushi", partner1="Sahan", partner2="Tharushi",
        fullName1="Sahan Lakshitha Perera", fullName2="Tharushi Nimasha Fonseka",
        parents1="Son of Mr. & Mrs. Ajith Perera, Gampaha", parents2="Daughter of Mr. & Mrs. Rohan Fonseka, Negombo",
        nativeGreeting="ආයුබෝවන්", tagline="Together with their families",
        hostLine="Mr. & Mrs. Ajith Perera and Mr. & Mrs. Rohan Fonseka joyfully invite you to the wedding of their children",
        inviteText="Surrounded by the scent of araliya and the people we love most, we will say our vows. We'd love for you to be there.",
        quote="In every blossom, a promise; in every season, us.", quoteSource="Sahan & Tharushi",
        date="2027-05-06T09:15:00+05:30", venueLine="Heritance Kandalama · Dambulla",
        events=[
            dict(name="Poruwa Ceremony", time="2027-05-06T09:15:00+05:30", timeLabel="Auspicious time · 9.15 a.m.", venue="Heritance Kandalama", address="Kandalama, Dambulla"),
            dict(name="Garden Reception", time="2027-05-06T12:00:00+05:30", timeLabel="12.00 noon onwards", venue="Heritance Kandalama · Lake Terrace", address="Dambulla"),
        ],
        dressCode="Garden formal — whites, greens and soft yellows.", dressColors=["#ffffff", "#8fae8d", "#f2c14e"],
        hashtag="#SahanAndTharushi", blessing="තෙරුවන් සරණයි", rsvp=dict(RSVP), brand=BRAND,
    )))

# ---------------------------------------------------------------- 5
G = "#c7901e"
THEMES.append(dict(
    slug="05-mangalam-tamil", name="Mangalam", category="Hindu · Tamil traditional",
    blurb="Turmeric, kumkum red and brass — marigold thoranam, kuthuvilakku lamps, a turning kolam.",
    theme_color="#9e1020",
    fonts="family=Cinzel:wght@400;600&family=Tangerine:wght@700&family=EB+Garamond:ital@0;1&family=Noto+Serif+Tamil:wght@500;700",
    vars="--bg:#fff5de;--bg2:#fbe9c2;--ink:#3b1d0d;--muted:#80573a;--accent:#9e1020;--accent2:#c05a00;--gold:#c7901e;--gold-hi:#ffe08a;--line:rgba(199,144,30,.55);--card:#fffaf0;--card-solid:#fffaf0;--on-accent:#fff5de;--radius:6px;"
         "--f-display:'Cinzel',serif;--f-script:'Tangerine',cursive;--f-body:'EB Garamond',serif;--f-native:'Noto Serif Tamil',serif;"
         "--op-back:#2a0508;--op-bg:radial-gradient(circle,#e7b64a 0 3px,#8a5a0a 4px,transparent 5px) 0 0/46px 46px,linear-gradient(90deg,#7e0c18,#a3141f 50%,#7e0c18);--op-line:#e7b64a;--op-ink:#ffe9a8;--seal:#c7901e;--seal-hi:#ffe08a;--seal-lo:#7a520a;--seal-ink:#7e0c18",
    opener="doors", opener_decor=f'<div style="width:62%;background:#8e101b;border-radius:50%;padding:6px">{mandala("#f0c860", "#f0c860")}</div>',
    hero=(f'<div class="kolam-bg"></div>{thoranam()}'
          f'<p class="suli h-in" style="--d:0">உ<span>சிவமயம்</span></p>'
          + T(1, "nativeGreeting", "native gr")
          + f'<div class="h-row h-in" style="--d:2">{lamp(G, "fl5a", 3, "lamp klamp")}<div class="h-kolam">{mandala("#9e1020", "#c7901e", "spin-slow")}</div>{lamp(G, "fl5b", 3, "lamp klamp")}</div>'
          + T(3, "tagline", "tagline") + names(4) + hdate(5) + T(6, "venueLine", "h-venue")),
    divider=diamond_orn(G, "divider"), st_orn=diamond_orn("#9e1020"), ev_icon=lamp(G, "fl5e", 3),
    css=COMMON_HERO_CSS + """
.hero{background:radial-gradient(ellipse at 50% 45%,#fffaf0,#fff0cc 70%,#fbdf9f);padding-top:120px}
.kolam-bg{position:absolute;inset:0;background:""" + kolam_tile("rgba(158,16,32,.10)") + """}
.thoranam{position:absolute;top:0;left:50%;width:max(100%,520px);translate:-50% 0;height:auto}
.strand{animation:sw 3.4s ease-in-out infinite alternate}
@keyframes sw{from{transform:rotate(-4deg)}to{transform:rotate(4deg)}}
.suli{font-family:var(--f-native);font-size:1.6rem;color:var(--accent);line-height:1}
.suli span{display:block;font-size:.8rem;letter-spacing:.1em;margin-top:6px;color:var(--accent2)}
.gr{font-size:clamp(1.3rem,5.6vw,1.7rem);color:var(--accent);margin-top:10px}
.h-row{display:flex;align-items:center;justify-content:center;gap:10px;margin:8px 0}
.klamp{width:44px;height:auto}
.h-kolam{width:96px;height:96px}
.names{color:var(--accent);font-size:clamp(3.6rem,17vw,6.6rem);line-height:.95}
.names .amp{font-family:var(--f-display);font-size:.28em;color:var(--gold);margin:4px 0}
.sec:nth-of-type(even){background:var(--bg2)}
.event{border:2px solid var(--gold);box-shadow:inset 0 0 0 4px var(--card),inset 0 0 0 5px var(--gold)}
.ev-ico{width:44px;height:80px}
.st{color:var(--accent)}
footer{background:#9e1020;color:#fff5de}footer .f-names{color:#ffe08a}footer .f-bless{color:#ffe9b8;font-size:1.3rem}footer .brand{color:#fff}
""",
    theme={"particles": {"type": "marigold", "colors": ["#f7a21b", "#ffc93c", "#ef7d0d"], "size": [6, 11], "count": 20, "speed": .9}},
    data=dict(
        slug="karthik-meenakshi", partner1="Karthik", partner2="Meenakshi",
        fullName1="Karthik Sivakumar", fullName2="Meenakshi Balachandran",
        parents1="Son of Mr. & Mrs. Sivakumar, Nallur, Jaffna", parents2="Daughter of Mr. & Mrs. Balachandran, Wellawatte, Colombo",
        nativeGreeting="திருமண அழைப்பிதழ்", tagline="With the divine blessings of the Almighty, we invite you to the wedding of",
        hostLine="Mr. & Mrs. Sivakumar and Mr. & Mrs. Balachandran request the pleasure of your presence with family and friends",
        inviteText="Please grace the auspicious muhurtham with your presence and bless the couple as they begin their married life.",
        quote="Seven steps together, a lifetime of companionship.", quoteSource="Karthik & Meenakshi",
        date="2027-06-10T06:45:00+05:30", venueLine="Sri Kathiresan Kovil · Bambalapitiya",
        events=[
            dict(name="Muhurtham · Thali Kattu", native="முகூர்த்தம்", time="2027-06-10T06:45:00+05:30", timeLabel="Auspicious muhurtham · 6.45 – 8.00 a.m.",
                 venue="Sri Kathiresan Kovil", address="Galle Road, Bambalapitiya, Colombo 04"),
            dict(name="Wedding Lunch", native="திருமண விருந்து", time="2027-06-10T11:30:00+05:30", timeLabel="11.30 a.m. onwards", venue="Ramakrishna Mission Hall", address="Wellawatte, Colombo 06"),
            dict(name="Reception", native="வரவேற்பு", time="2027-06-12T18:30:00+05:30", timeLabel="6.30 p.m. onwards", venue="Hilton Colombo · Grand Ballroom", address="2 Sir Chittampalam A. Gardiner Mw, Colombo 02"),
        ],
        dressCode="Traditional — pattu sarees, veshti and bright festive colours.", dressColors=["#9e1020", "#f7a21b", "#2f7d32"],
        hashtag="#KarthikWedsMeenakshi", blessing="சுபம்", rsvp=dict(RSVP), brand=BRAND,
        labels={"countdown": "Counting down to the muhurtham", "events": "Auspicious Occasions"},
    )))

# ---------------------------------------------------------------- 6
G = "#e0bd6a"


def jasmine_strand(n=16):
    out = [f'<path d="M10 0V{n*16}" stroke="#e0bd6a" stroke-width=".8"/>']
    for k in range(n):
        y = 8 + k * 16
        out.append(f'<g transform="translate(10 {y})">{ring(5, 3, 6, 0, "#fffdf5", "#e8e0c8", .4)}<circle r="1.4" fill="#e0bd6a"/></g>')
    return f'<svg class="jas" viewBox="0 0 20 {n*16+6}" aria-hidden="true">{"".join(out)}</svg>'


THEMES.append(dict(
    slug="06-kovil-emerald", name="Kovil Emerald", category="Hindu · Luxury",
    blurb="Emerald and temple gold with a glowing gopuram outline and swaying jasmine strands.",
    theme_color="#0c3a2d",
    fonts="family=Cinzel:wght@400;600&family=Rouge+Script&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Noto+Serif+Tamil:wght@500;700",
    vars="--bg:#0c3a2d;--bg2:#0f4636;--ink:#f3ead2;--muted:#c9d8c4;--accent:#f0d58a;--accent2:#fff;--gold:#e0bd6a;--gold-hi:#fff4c8;--line:rgba(224,189,106,.45);--card:rgba(255,255,255,.05);--card-solid:#fbf6e6;--on-accent:#0c3a2d;--radius:4px;--input-bg:rgba(0,0,0,.18);"
         "--f-display:'Cinzel',serif;--f-script:'Rouge Script',cursive;--f-body:'Cormorant Garamond',serif;--f-native:'Noto Serif Tamil',serif;"
         "--op-back:#03140f;--op-bg:" + kolam_tile("rgba(224,189,106,.28)") + ",linear-gradient(90deg,#082a20,#0e4535 50%,#082a20);--op-line:rgba(224,189,106,.6);--op-ink:#f0d58a;--seal:#e0bd6a;--seal-hi:#fff0b8;--seal-lo:#8a6a1c;--seal-ink:#0c3a2d",
    opener="doors", opener_decor=f'<div style="width:78%">{gopuram(G)}</div>',
    hero=(f'<div class="jas-wrap l">{jasmine_strand()}{jasmine_strand(11)}</div><div class="jas-wrap r">{jasmine_strand(11)}{jasmine_strand()}</div>'
          f'<div class="gop h-in" style="--d:6">{gopuram(G)}</div>'
          + T(0, "nativeGreeting", "native om") + T(1, "tagline", "tagline") + names(2, "names shimmer")
          + f'<div class="h-in" style="--d:3">{diamond_orn(G, "divider")}</div>' + hdate(4) + T(5, "venueLine", "h-venue")),
    divider=diamond_orn(G, "divider"), st_orn=diamond_orn(G), ev_icon=gopuram(G),
    css=COMMON_HERO_CSS + """
.hero{background:radial-gradient(ellipse at 50% 30%,#155a46,#0c3a2d 55%,#062519);justify-content:flex-start;padding-top:16svh}
.gop{position:absolute;bottom:0;left:50%;width:min(400px,86vw);translate:-50% 0;opacity:.3;filter:drop-shadow(0 0 12px rgba(240,213,138,.5))}
.jas-wrap{position:absolute;top:0;display:flex;gap:10px;z-index:1}
.jas-wrap.l{left:10px}.jas-wrap.r{right:10px}
.jas{width:18px;height:auto;transform-origin:top center;animation:jsw 4s ease-in-out infinite alternate}
.jas:nth-child(2){animation-delay:-2s}
@keyframes jsw{from{transform:rotate(-2.5deg)}to{transform:rotate(2.5deg)}}
.om{font-size:1.1rem;color:var(--gold);letter-spacing:.04em;max-width:260px}
.t-06-kovil-emerald .tagline{max-width:250px}
.jas{width:14px!important}
.t-06-kovil-emerald .hero>*:not(.gop):not(.jas-wrap){position:relative;z-index:2;text-shadow:0 2px 12px #0c3a2d}
.names{font-size:clamp(3.6rem,17vw,6.8rem)}
.names .amp{font-family:var(--f-display);font-size:.28em;letter-spacing:.3em}
.hd-day{color:var(--gold)}
.sec:nth-of-type(even){background:var(--bg2)}
.st{color:var(--gold)}
.ev-ico{width:84px;height:84px}
.event{border-color:var(--line);background:linear-gradient(rgba(255,255,255,.06),rgba(255,255,255,.02))}
footer{background:#062519}
""",
    theme={"particles": {"type": "flower", "colors": ["#fffdf5", "#fbf6e6"], "center": "#e0bd6a", "size": [4, 7], "count": 22, "speed": .6, "glow": 8}},
    data=dict(
        slug="niroshan-thivya", partner1="Niroshan", partner2="Thivya",
        fullName1="Niroshan Rajendran", fullName2="Thivya Mahendran",
        parents1="Son of Mr. & Mrs. Rajendran, Batticaloa", parents2="Daughter of Mr. & Mrs. Mahendran, Kotahena, Colombo",
        nativeGreeting="திருமண அழைப்பிதழ்", tagline="By the grace of God, and with the blessings of our elders, we invite you to the wedding of",
        hostLine="The families of Rajendran and Mahendran humbly request your presence and blessings",
        inviteText="Your blessings are the most precious gift — please join us for the muhurtham and the celebrations that follow.",
        quote="Two families, one joy — may this union be as enduring as the temple stone.", quoteSource="Niroshan & Thivya",
        date="2027-08-26T07:30:00+05:30", venueLine="Sri Ponnambalavaneswarar Kovil · Colombo 13",
        events=[
            dict(name="Muhurtham", native="முகூர்த்தம்", time="2027-08-26T07:30:00+05:30", timeLabel="Auspicious time · 7.30 – 9.00 a.m.", venue="Sri Ponnambalavaneswarar Kovil", address="Kotahena, Colombo 13"),
            dict(name="Reception", native="வரவேற்பு", time="2027-08-26T18:30:00+05:30", timeLabel="6.30 p.m. onwards", venue="Cinnamon Grand · Oak Room", address="77 Galle Road, Colombo 03"),
        ],
        dressCode="Festive traditional — silks, gold and jewel tones.", dressColors=["#0c3a2d", "#e0bd6a", "#fbf6e6"],
        hashtag="#NiroThivya", blessing="சுபம்", rsvp=dict(RSVP), brand=BRAND,
        labels={"events": "Auspicious Occasions"},
    )))

# ---------------------------------------------------------------- 7
G = "#d8b56a"
THEMES.append(dict(
    slug="07-nikah-noor", name="Nikah Noor", category="Muslim · Classic",
    blurb="Midnight teal with an arched mihrab frame, Bismillah calligraphy and hanging gold stars.",
    theme_color="#0b2a3a",
    fonts="family=Amiri:wght@400;700&family=Italianno&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Marcellus",
    vars="--bg:#0b2a3a;--bg2:#0e3345;--ink:#f1e9d6;--muted:#b9c7c9;--accent:#e8cc8a;--accent2:#fff;--gold:#d8b56a;--gold-hi:#fff2c6;--line:rgba(216,181,106,.45);--card:rgba(255,255,255,.05);--card-solid:#fbf5e6;--on-accent:#0b2a3a;--radius:120px 120px 6px 6px;--btn-radius:4px;--input-bg:rgba(0,0,0,.18);"
         "--f-display:'Marcellus',serif;--f-script:'Italianno',cursive;--f-body:'Cormorant Garamond',serif;--f-native:'Amiri',serif;"
         "--op-back:#04121a;--op-bg:" + star8_tile("rgba(216,181,106,.28)") + ",linear-gradient(90deg,#08202d,#0f3a4e 50%,#08202d);--op-line:rgba(216,181,106,.6);--op-ink:#f0d58a;--seal:#d8b56a;--seal-hi:#fff0b8;--seal-lo:#8a6a1c;--seal-ink:#0b2a3a",
    opener="doors", opener_decor=f'<div style="width:60%;opacity:.9">{star8(G, "", "rgba(216,181,106,.12)")}</div>',
    hero=(f'<div class="pat"></div><div class="archbox">{arch(G)}'
          f'<div class="stars"><i style="--l:28%;--h:70px"></i><i style="--l:50%;--h:40px"></i><i style="--l:72%;--h:86px"></i></div>'
          f'<div class="arch-in">'
          + f'<div class="h-in" style="--d:0">{crescent(G)}</div>' + T(1, "nativeGreeting", "native bism")
          + T(2, "greeting", "kicker") + T(3, "tagline", "tagline") + names(4, "names shimmer") + hdate(5) + T(6, "venueLine", "h-venue")
          + '</div></div>'),
    divider=diamond_orn(G, "divider"), st_orn=star8(G, "st-orn st8"), ev_icon=star8(G, "", "rgba(216,181,106,.12)"),
    css=COMMON_HERO_CSS + """
.hero{background:radial-gradient(ellipse at 50% 30%,#14465c,#0b2a3a 60%,#061a24)}
.pat{position:absolute;inset:0;background:""" + star8_tile("rgba(216,181,106,.09)") + """}
.archbox{position:relative;width:min(92vw,440px);aspect-ratio:300/500;display:flex}
.arch-frame{position:absolute;inset:0;width:100%;height:100%}
.arch-in{position:relative;margin:auto;padding:40% 24px 12%;display:flex;flex-direction:column;align-items:center}
.stars i{position:absolute;top:18%;left:var(--l);width:1px;height:var(--h);background:linear-gradient(transparent,var(--gold));transform-origin:top;animation:jsw 3.5s ease-in-out infinite alternate}
.stars i:nth-child(2){animation-delay:-1.5s;top:9%}
.stars i::after{content:"✦";position:absolute;bottom:-9px;left:-6px;color:var(--gold);font-size:13px;font-style:normal;text-shadow:0 0 8px #ffe7a6}
@keyframes jsw{from{transform:rotate(-4deg)}to{transform:rotate(4deg)}}
.crescent{width:46px;margin:0 auto 6px;filter:drop-shadow(0 0 10px rgba(255,230,160,.6))}
.bism{font-size:clamp(1.3rem,6vw,1.8rem);color:var(--gold);line-height:1.6}
.names{font-size:clamp(3.4rem,15vw,5.8rem);line-height:.95;margin:6px 0}
.names .amp{font-family:var(--f-display);font-size:.3em}
.hd-side{min-width:92px}
.hd-day{color:var(--gold)}
.sec:nth-of-type(even){background:var(--bg2)}
.st{color:var(--gold)}
.st8{width:40px}
.event{padding-top:46px}
.ev-ico{width:50px}
.f-bless{font-size:1.25rem;line-height:1.9}
footer{background:#061a24}
""",
    theme={"particles": {"type": "sparkle", "colors": ["#f3d98f", "#fff2c6", "#d8b56a"], "size": [3, 7], "count": 30, "speed": .5, "dir": -1, "glow": 8, "mode": "twinkle"}},
    data=dict(
        slug="imran-ayesha", partner1="Imran", partner2="Ayesha",
        fullName1="Mohamed Imran Farook", fullName2="Fathima Ayesha Nizar",
        parents1="Son of Al-Haj M. H. Farook & Mrs. Farook, Kandy", parents2="Daughter of Mr. & Mrs. A. R. Nizar, Dehiwala",
        nativeGreeting="بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ", greeting="Assalamu Alaikum",
        tagline="With the blessings of Allah, we invite you to the Nikah of",
        hostLine="Al-Haj M. H. Farook and Mr. A. R. Nizar, together with their families, request the honour of your presence",
        inviteText="Your presence and duas would mean the world to us as we begin this blessed journey.",
        quote="And among His signs is that He created for you spouses from among yourselves, that you may find tranquillity in them; and He placed between you affection and mercy.",
        quoteSource="Qur'an · Surah Ar-Rum 30:21",
        date="2027-01-15T16:00:00+05:30", venueLine="The Kingsbury · Colombo",
        events=[
            dict(name="Nikah Ceremony", native="نكاح", time="2027-01-15T16:00:00+05:30", timeLabel="4.00 p.m. (after Asr)", venue="The Kingsbury · Ocean Room", address="48 Janadhipathi Mawatha, Colombo 01"),
            dict(name="Walima Reception", native="وليمة", time="2027-01-17T19:00:00+05:30", timeLabel="7.00 p.m. onwards", venue="Galadari Hotel · Grand Ballroom", address="64 Lotus Road, Colombo 01"),
        ],
        dressCode="Modest formal attire.", dressColors=["#0b2a3a", "#d8b56a", "#f1e9d6"],
        hashtag="#ImranWedsAyesha", blessing="بَارَكَ ٱللَّٰهُ لَكُمَا وَبَارَكَ عَلَيْكُمَا وَجَمَعَ بَيْنَكُمَا فِي خَيْرٍ",
        rsvp=dict(RSVP), brand=BRAND,
        labels={"invited": "You are invited to our Nikah", "countdown": "Counting down, insha'Allah", "thanksYes": "Jazakallahu khairan — we can't wait to see you."},
    )))

# ---------------------------------------------------------------- 8
G = "#c49a52"
THEMES.append(dict(
    slug="08-rose-nikah", name="Rose Nikah", category="Muslim · Soft & romantic",
    blurb="Dusty rose and ivory, geometric lattice and swinging glowing lanterns.",
    theme_color="#b86b77",
    fonts="family=Amiri:wght@400;700&family=Pinyon+Script&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Josefin+Sans:wght@300;400",
    vars="--bg:#fbf2ee;--bg2:#f5e4df;--ink:#4b3036;--muted:#8f7075;--accent:#9e4f5c;--accent2:#b86b77;--gold:#c49a52;--gold-hi:#f4dca6;--line:rgba(184,107,119,.3);--card:#fffaf8;--card-solid:#fffaf8;--on-accent:#fff;--radius:14px;--in-radius:10px;"
         "--f-display:'Cormorant Garamond',serif;--f-script:'Pinyon Script',cursive;--f-body:'Josefin Sans',sans-serif;--f-native:'Amiri',serif;"
         "--op-bg:" + star8_tile("rgba(184,107,119,.16)", 48) + ",#f5e4df;--env-back:#b86b77;--env-front:linear-gradient(160deg,#d494a0,#c07a87);--env-flap:linear-gradient(#e0a9b3,#c98894);--op-ink:#9e4f5c;--seal:#c49a52;--seal-hi:#f4dca6;--seal-lo:#7d5e22;--seal-ink:#fff",
    opener="envelope", opener_decor=f'<div style="width:40px;margin:0 auto 4px">{star8(G)}</div>',
    hero=(f'<div class="pat"></div><div class="lanterns">{lantern(G, "lg1", "lantern a")}{lantern(G, "lg2", "lantern b")}{lantern(G, "lg3", "lantern c")}</div>'
          + T(0, "nativeGreeting", "native bism") + T(1, "greeting", "kicker") + T(2, "tagline", "tagline") + names(3)
          + f'<div class="h-in" style="--d:4">{diamond_orn(G, "divider")}</div>' + hdate(5) + T(6, "venueLine", "h-venue")),
    divider=diamond_orn(G, "divider"), st_orn=star8(G, "st-orn st8"), ev_icon=lantern(G, "lge"),
    css=COMMON_HERO_CSS + """
.hero{background:radial-gradient(ellipse at 50% 55%,#fffaf8,#fbf2ee 55%,#f1dcd6);padding-top:190px}
.pat{position:absolute;inset:0;background:""" + star8_tile("rgba(184,107,119,.10)", 48) + """;-webkit-mask:radial-gradient(ellipse at 50% 50%,transparent 30%,#000 75%);mask:radial-gradient(ellipse at 50% 50%,transparent 30%,#000 75%)}
.lanterns{position:absolute;top:0;left:0;right:0;display:flex;justify-content:center;gap:clamp(30px,12vw,90px);pointer-events:none}
.lantern{width:46px;height:auto;transform-origin:top center;animation:lsw 3.6s ease-in-out infinite alternate}
.lantern.a{width:40px;margin-top:-30px;animation-delay:-1s}.lantern.b{width:56px;margin-top:10px}.lantern.c{width:40px;margin-top:-50px;animation-delay:-2.2s}
@keyframes lsw{from{transform:rotate(-5deg)}to{transform:rotate(5deg)}}
.lglow{animation:glowp 1.8s ease-in-out infinite alternate}
.bism{font-size:clamp(1.3rem,6vw,1.8rem);color:var(--accent);line-height:1.6}
.names{font-size:clamp(3.2rem,15vw,6rem);margin:8px 0}
.names .amp{font-family:var(--f-display);font-style:italic;font-size:.34em;color:var(--gold)}
.hd-side{font-family:var(--f-body)}
.sec:nth-of-type(even){background:var(--bg2)}
.st8{width:36px}
.ev-ico{width:34px;height:84px}
.event{box-shadow:0 20px 40px -30px rgba(158,79,92,.6)}
.f-bless{font-size:1.2rem;line-height:1.9}
""",
    theme={"particles": {"type": "dot", "colors": ["#ffcf73", "#ffb84d", "#ffe3a6"], "size": [4, 9], "count": 24, "speed": .5, "dir": -1, "glow": 12, "alpha": .8}},
    data=dict(
        slug="rizwan-hafsa", partner1="Rizwan", partner2="Hafsa",
        fullName1="Mohamed Rizwan Ismail", fullName2="Hafsa Shazna Cassim",
        parents1="Son of Mr. & Mrs. M. S. Ismail, Beruwala", parents2="Daughter of Mr. & Mrs. A. H. Cassim, Colombo 06",
        nativeGreeting="بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ", greeting="Assalamu Alaikum",
        tagline="Together with our families, we joyfully invite you to celebrate the Nikah of",
        hostLine="With gratitude to Allah and the love of our families",
        inviteText="Please join us with your duas as we are joined in marriage, and stay to share a meal with us at the Walima.",
        quote="And We created you in pairs.", quoteSource="Qur'an · Surah An-Naba 78:8",
        date="2027-03-05T17:00:00+05:30", venueLine="Galadari Hotel · Colombo",
        events=[
            dict(name="Nikah", time="2027-03-05T17:00:00+05:30", timeLabel="5.00 p.m.", venue="Colombo Grand Mosque", address="Grandpass Road, Colombo 12", note="Ladies' seating available in the upper hall."),
            dict(name="Walima Dinner", time="2027-03-05T19:30:00+05:30", timeLabel="7.30 p.m. onwards", venue="Galadari Hotel · Ballroom", address="64 Lotus Road, Colombo 01"),
        ],
        dressCode="Modest and elegant — blush, ivory and gold tones.", dressColors=["#b86b77", "#fbf2ee", "#c49a52"],
        hashtag="#RizwanHafsa", blessing="بَارَكَ ٱللَّٰهُ لَكُمَا وَبَارَكَ عَلَيْكُمَا وَجَمَعَ بَيْنَكُمَا فِي خَيْرٍ",
        rsvp=dict(RSVP), brand=BRAND,
        labels={"invited": "You are invited to our Nikah", "thanksYes": "Jazakallahu khairan — we can't wait to see you."},
    )))

# ---------------------------------------------------------------- 9
G = "#b8913e"
door_panel = ('<svg viewBox="0 0 120 300" style="width:74%;height:auto" aria-hidden="true"><g fill="none" stroke="#e6c98a" stroke-width="1.5">'
              '<path d="M12 290V70A48 48 0 0 1 108 70V290Z"/><path d="M22 280V74A38 38 0 0 1 98 74V280Z" stroke-width=".8"/>'
              '<path d="M60 36V130M40 64H80" stroke-width="3"/><path d="M22 170H98M22 225H98" stroke-width=".8"/></g></svg>')
THEMES.append(dict(
    slug="09-holy-matrimony", name="Holy Matrimony", category="Catholic · Classic church",
    blurb="Ivory and gilded gold, a cathedral arch with a radiant cross and doves in flight.",
    theme_color="#1f2a44",
    fonts="family=Cinzel:wght@400;600&family=Pinyon+Script&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400",
    vars="--bg:#fbf8f1;--bg2:#f3eee2;--ink:#1f2a44;--muted:#5f6679;--accent:#1f2a44;--accent2:#8a6a24;--gold:#b8913e;--gold-hi:#f4dea0;--line:rgba(184,145,62,.4);--card:#fffdf8;--card-solid:#fffdf8;--on-accent:#fbf8f1;--radius:140px 140px 4px 4px;--btn-radius:2px;"
         "--f-display:'Cinzel',serif;--f-script:'Pinyon Script',cursive;--f-body:'Cormorant Garamond',serif;--f-native:'Cormorant Garamond',serif;"
         "--op-back:#1a0f06;--op-bg:linear-gradient(90deg,rgba(0,0,0,.25),transparent 12%,transparent 88%,rgba(0,0,0,.25)),repeating-linear-gradient(90deg,#5b371c 0 9px,#613b1f 9px 10px,#553219 10px 19px);--op-line:rgba(230,201,138,.6);--op-ink:#f6e7c1;--seal:#b8913e;--seal-hi:#f4dea0;--seal-lo:#6f5212;--seal-ink:#1f2a44",
    opener="doors", opener_decor=door_panel,
    hero=(f'<div class="rays"></div><div class="doves">{dove("#c9d1e3", "dove d1")}{dove("#dfe4ef", "dove d2")}</div>'
          f'<div class="archbox">{arch(G, pointed=False)}<div class="arch-in">'
          f'<div class="h-in" style="--d:0">{cross(G)}</div>' + T(1, "greeting", "kicker") + T(2, "tagline", "tagline") + names(3)
          + T(4, "nativeGreeting", "hm") + hdate(5) + T(6, "venueLine", "h-venue") + '</div></div>'),
    divider=diamond_orn(G, "divider"), st_orn=cross(G, "st-orn stc", False), ev_icon=cross(G),
    css=COMMON_HERO_CSS + """
.hero{background:radial-gradient(ellipse at 50% 20%,#fff,#fbf8f1 50%,#efe7d4)}
.rays{position:absolute;left:50%;top:22%;width:180vmax;height:180vmax;translate:-50% -50%;background:repeating-conic-gradient(from 0deg,rgba(212,176,96,.10) 0 4deg,transparent 4deg 12deg);-webkit-mask:radial-gradient(circle,#000 0,transparent 45%);mask:radial-gradient(circle,#000 0,transparent 45%);animation:spin 120s linear infinite}
.archbox{position:relative;width:min(92vw,440px);aspect-ratio:300/500;display:flex}
.arch-frame{position:absolute;inset:0;width:100%;height:100%}
.arch-in{position:relative;margin:auto;padding:26% 36px 10%;display:flex;flex-direction:column;align-items:center}
.cross{width:72px;margin:0 auto}
.names{font-size:clamp(3.2rem,14.5vw,5.6rem);line-height:1;margin:8px 0}
.names .amp{font-family:var(--f-display);font-size:.3em;color:var(--gold)}
.hm{font-family:var(--f-display);letter-spacing:.3em;text-transform:uppercase;font-size:.78rem;color:var(--accent2);margin-top:6px}
.hd-side{min-width:92px}
.doves{position:absolute;inset:0;pointer-events:none}
.dove{position:absolute;width:58px;opacity:0}
body.opened .dove{animation:fly 16s linear infinite}
.d1{top:14%;animation-delay:1s!important}.d2{top:24%;width:42px;animation-delay:6s!important}
@keyframes fly{0%{transform:translateX(-80px) translateY(0);opacity:0}8%{opacity:.95}50%{transform:translateX(55vw) translateY(-30px)}92%{opacity:.9}100%{transform:translateX(110vw) translateY(-10px);opacity:0}}
.dove .wing,.dove .wing2{transform-box:fill-box;transform-origin:100% 100%;animation:flap .5s ease-in-out infinite alternate}
.dove .wing2{transform-origin:0 100%}
@keyframes flap{to{transform:scaleY(.25)}}
.sec:nth-of-type(even){background:var(--bg2)}
.event{padding-top:56px}
.ev-ico{width:54px}
.stc{width:34px}
.quote blockquote{color:var(--accent)}
""",
    theme={"particles": {"type": "petal", "colors": ["#ffffff", "#fbf1e0", "#f3e3c3"], "size": [5, 9], "count": 20, "flip": True, "speed": .6}},
    data=dict(
        slug="shehan-natasha", partner1="Shehan", partner2="Natasha",
        fullName1="Shehan Anthony Fernando", fullName2="Natasha Marie Perera",
        parents1="Son of Mr. & Mrs. Anthony Fernando, Negombo", parents2="Daughter of Mr. & Mrs. Clement Perera, Wattala",
        greeting="Together with their families", tagline="request the honour of your presence at the marriage of",
        nativeGreeting="The Sacrament of Holy Matrimony",
        hostLine="Mr. & Mrs. Anthony Fernando and Mr. & Mrs. Clement Perera invite you to share in the joy of their children's marriage",
        inviteText="Please join us as we exchange our vows before God, our families and friends, followed by a celebration of love.",
        quote="Love is patient and kind … Love bears all things, believes all things, hopes all things, endures all things.",
        quoteSource="1 Corinthians 13:4, 7",
        date="2027-12-04T15:30:00+05:30", venueLine="St. Lucia's Cathedral · Kotahena",
        events=[
            dict(name="Nuptial Mass", time="2027-12-04T15:30:00+05:30", timeLabel="3.30 p.m.", venue="St. Lucia's Cathedral", address="Kotahena, Colombo 13", note="Kindly be seated by 3.15 p.m."),
            dict(name="Wedding Reception", time="2027-12-04T19:00:00+05:30", timeLabel="7.00 p.m. onwards", venue="Galle Face Hotel · Regency Ballroom", address="2 Galle Road, Colombo 03"),
        ],
        dressCode="Formal — suits and elegant evening wear.", dressColors=["#1f2a44", "#b8913e", "#fbf8f1"],
        hashtag="#ShehanAndNatasha", blessing="What God has joined together, let no one put asunder.", rsvp=dict(RSVP), brand=BRAND,
    )))

# ---------------------------------------------------------------- 10
THEMES.append(dict(
    slug="10-rose-window", name="Rose Window", category="Catholic · Stained glass",
    blurb="Deep cathedral navy with a slowly turning, glowing stained-glass rose window.",
    theme_color="#0f1830",
    fonts="family=Cinzel:wght@400;600&family=Italianno&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400",
    vars="--bg:#0f1830;--bg2:#131e3a;--ink:#eef0f7;--muted:#aab3cc;--accent:#f1d890;--accent2:#fff;--gold:#c9a14a;--gold-hi:#fff0c0;--line:rgba(201,161,74,.4);--card:rgba(255,255,255,.04);--card-solid:#f7f3ea;--on-accent:#0f1830;--radius:6px;--input-bg:rgba(0,0,0,.2);"
         "--f-display:'Cinzel',serif;--f-script:'Italianno',cursive;--f-body:'Cormorant Garamond',serif;--f-native:'Cormorant Garamond',serif;"
         "--op-bg:radial-gradient(circle at 50% 40%,#1b2a52,#0a1022);--op-ink:#f1d890",
    opener="minimal", opener_decor=f'<div style="width:150px;margin:0 auto 8px" class="spin-slow">{rose_window()}</div>',
    hero=(f'<div class="rw h-in" style="--d:0">{rose_window("rose spin-slow")}</div>'
          + T(1, "nativeGreeting", "kicker") + T(2, "tagline", "tagline") + names(3, "names")
          + f'<div class="h-in" style="--d:4">{diamond_orn("#c9a14a", "divider")}</div>' + hdate(5) + T(6, "venueLine", "h-venue")),
    divider=diamond_orn("#c9a14a", "divider"), st_orn=cross("#c9a14a", "st-orn stc", False), ev_icon=rose_window(),
    css=COMMON_HERO_CSS + """
.hero{background:radial-gradient(ellipse at 50% 28%,#1f3163,#0f1830 55%,#080d1c)}
.rw{width:min(250px,62vw);aspect-ratio:1;border-radius:50%;box-shadow:0 0 60px 10px rgba(120,150,255,.25),0 0 120px 30px rgba(180,40,80,.15);margin-bottom:22px;position:relative}
.rw::after{content:"";position:absolute;inset:0;border-radius:50%;background:radial-gradient(circle at 35% 30%,rgba(255,255,255,.35),transparent 45%);mix-blend-mode:screen;animation:glowp 3s ease-in-out infinite alternate}
.rose{width:100%;height:100%}
.names{color:#fff;font-size:clamp(3.8rem,18vw,7rem);line-height:.9;text-shadow:0 0 24px rgba(160,180,255,.35)}
.names .amp{font-family:var(--f-display);font-size:.25em;color:var(--gold);letter-spacing:.3em;margin:8px 0}
.kicker{color:var(--accent)}
.hd-day{color:var(--accent)}
.sec:nth-of-type(even){background:var(--bg2)}
.st{color:var(--accent)}
.stc{width:30px}
.ev-ico{width:64px;height:64px}
.event{border-color:var(--line)}
footer{background:#080d1c}
""",
    theme={"particles": {"type": "sparkle", "colors": ["#e0445f", "#4f7df0", "#f2c14e", "#2fb58a", "#a46be0"], "size": [3, 7], "count": 28, "speed": .4, "mode": "twinkle", "glow": 10}, "openMs": 1200},
    data=dict(
        slug="ruwan-michelle", partner1="Ruwan", partner2="Michelle",
        fullName1="Ruwan Joseph Silva", fullName2="Michelle Anne de Mel",
        parents1="Son of Mr. & Mrs. Joseph Silva, Moratuwa", parents2="Daughter of Dr. & Mrs. Ivan de Mel, Colombo 05",
        nativeGreeting="Holy Matrimony", tagline="With joyful hearts we invite you to witness the marriage of",
        hostLine="Together with their families, and by the grace of God",
        inviteText="As we promise our lives to each other before God, we ask you to pray with us and celebrate with us.",
        quote="Where you go I will go, and where you lodge I will lodge; your people shall be my people, and your God my God.",
        quoteSource="Ruth 1:16",
        date="2027-09-18T16:00:00+05:30", venueLine="All Saints' Church · Borella",
        events=[
            dict(name="Wedding Mass", time="2027-09-18T16:00:00+05:30", timeLabel="4.00 p.m.", venue="All Saints' Church", address="Borella, Colombo 08"),
            dict(name="Reception", time="2027-09-18T19:30:00+05:30", timeLabel="7.30 p.m. onwards", venue="Cinnamon Grand · Grand Ballroom", address="77 Galle Road, Colombo 03"),
        ],
        dressCode="Black tie optional — jewel tones encouraged.", dressColors=["#b3123a", "#1d4fa8", "#127a5a", "#e0a526"],
        hashtag="#RuwanAndMichelle", blessing="What God has joined together, let no one put asunder.", rsvp=dict(RSVP), brand=BRAND,
    )))

# ---------------------------------------------------------------- 11
G = "#d4af5a"
THEMES.append(dict(
    slug="11-golden-opulence", name="Golden Opulence", category="Luxury · Art deco",
    blurb="Black lacquer and liquid gold — Gatsby-style frames, a sunburst crest and falling gold leaf.",
    theme_color="#0b0b0b",
    fonts="family=Bodoni+Moda:ital,wght@0,400;0,600;1,400&family=Italiana&family=Josefin+Sans:wght@300;400",
    vars="--bg:#0b0b0b;--bg2:#121212;--ink:#efe6d2;--muted:#a79b83;--accent:#e6c77a;--accent2:#fff;--gold:#d4af5a;--gold-hi:#fff3c8;--line:rgba(212,175,90,.45);--card:rgba(255,255,255,.03);--card-solid:#111;--on-accent:#0b0b0b;--radius:0;--btn-radius:0;--in-radius:0;--input-bg:#050505;"
         "--f-display:'Italiana',serif;--f-script:'Bodoni Moda',serif;--f-body:'Josefin Sans',sans-serif;--f-native:'Italiana',serif;"
         "--op-bg:radial-gradient(circle at 50% 40%,#1c1a14,#050505);--env-back:#2a2418;--env-front:linear-gradient(160deg,#3a3122,#211c13);--env-flap:linear-gradient(#4a3f2a,#2c261a);--op-ink:#e6c77a;--seal:#b8872b;--seal-hi:#ffe39a;--seal-lo:#5e420c;--seal-ink:#111",
    opener="envelope", opener_decor=f'<div style="width:90px;margin:0 auto">{sunburst(G)}</div>',
    hero=(f'<div class="deco">{deco_corner(G, "dc a")}{deco_corner(G, "dc b")}{deco_corner(G, "dc c")}{deco_corner(G, "dc d")}</div>'
          f'<div class="h-in" style="--d:0">{sunburst(G)}</div>' + T(1, "tagline", "kicker") + names(2, "names shimmer")
          + f'<div class="deco-date h-in" style="--d:3"><span data-f="c.weekday"></span><b data-f="c.day"></b><span data-f="c.month"></span><b data-f="c.year"></b></div>'
          + T(4, "venueLine", "h-venue")),
    divider=diamond_orn(G, "divider"), st_orn=diamond_orn(G), ev_icon=sunburst(G),
    css=COMMON_HERO_CSS + """
.hero{background:radial-gradient(ellipse at 50% 30%,#1d1a12,#0b0b0b 60%)}
.env-back,.env-front{box-shadow:inset 0 0 0 1px rgba(212,175,90,.5)}
.deco{position:absolute;inset:16px;border:1px solid var(--line);pointer-events:none}
.deco::after{content:"";position:absolute;inset:8px;border:1px solid rgba(212,175,90,.25)}
.dc{position:absolute;width:70px;height:70px}.dc.a{top:-1px;left:-1px}.dc.b{top:-1px;right:-1px;transform:scaleX(-1)}.dc.c{bottom:-1px;left:-1px;transform:scaleY(-1)}.dc.d{bottom:-1px;right:-1px;transform:scale(-1)}
.sunburst{width:min(240px,62vw);margin:0 auto 18px}
.kicker{max-width:300px;line-height:1.9}
.names{font-family:'Bodoni Moda',serif;font-style:italic;font-size:clamp(3rem,14vw,5.8rem);line-height:1;margin:16px 0 8px;letter-spacing:.01em}
.names .amp{font-family:var(--f-display);font-style:normal;font-size:.36em;margin:4px 0}
.deco-date{display:grid;grid-template-columns:repeat(4,auto);gap:0;margin:22px auto 8px;border:1px solid var(--line)}
.deco-date>*{padding:10px 12px;border-right:1px solid var(--line);font-size:.72rem;letter-spacing:.24em;text-transform:uppercase;display:flex;align-items:center}
.deco-date>*:last-child{border-right:0}
.deco-date b{font-family:var(--f-display);font-weight:400;font-size:1.3rem;letter-spacing:.06em;color:var(--gold)}
@media(max-width:420px){.deco-date{grid-template-columns:auto auto}.deco-date>*:nth-child(2){border-right:0}.deco-date>*:nth-child(-n+2){border-bottom:1px solid var(--line)}.deco-date>*{justify-content:center}}
.st{font-family:var(--f-display);letter-spacing:.2em;text-transform:uppercase;font-size:clamp(1.3rem,5vw,1.9rem);color:var(--gold)}
.sec:nth-of-type(even){background:var(--bg2)}
.event{outline:1px solid rgba(212,175,90,.2);outline-offset:-8px}
.ev-ico{width:90px;height:46px}
.f-names{font-family:'Bodoni Moda',serif;font-style:italic;color:var(--gold)}
.thanks .t-big{font-family:'Bodoni Moda',serif;font-style:italic}
.couple .and{font-family:'Bodoni Moda',serif;font-style:italic}
""",
    theme={"particles": {"type": "glitter", "colors": ["#f3d27a", "#d4af5a", "#fff3c8", "#b8872b"], "size": [3, 7], "count": 40, "flip": True, "speed": .7}},
    data=dict(
        slug="dinuk-amaya", partner1="Dinuk", partner2="Amaya",
        fullName1="Dinuk Senal Abeywickrama", fullName2="Amaya Chenuli Gunawardena",
        parents1="Son of Mr. & Mrs. Priyantha Abeywickrama", parents2="Daughter of Mr. & Mrs. Lalith Gunawardena",
        tagline="The pleasure of your company is requested at the wedding celebration of",
        hostLine="An evening of elegance, champagne and celebration",
        inviteText="Dinner, dancing and a night to remember — we would be delighted to celebrate with you.",
        quote="All that glitters is gold when it's shared with you.", quoteSource="Dinuk & Amaya",
        date="2027-06-12T18:30:00+05:30", venueLine="Shangri-La · Colombo",
        events=[
            dict(name="Poruwa & Vows", time="2027-06-12T18:30:00+05:30", timeLabel="6.30 p.m.", venue="Shangri-La Colombo · Lotus Ballroom", address="1 Galle Face, Colombo 02"),
            dict(name="Gala Reception", time="2027-06-12T20:00:00+05:30", timeLabel="8.00 p.m. until late", venue="Shangri-La Colombo · Lotus Ballroom", address="1 Galle Face, Colombo 02"),
        ],
        dressCode="Black tie — black, champagne and gold.", dressColors=["#0b0b0b", "#d4af5a", "#efe6d2"],
        hashtag="#DinukAmayaGala", blessing="", rsvp=dict(RSVP), brand=BRAND,
        labels={"events": "The Evening", "rsvp": "RSVP"},
    )))

# ---------------------------------------------------------------- 12
C = "#e8d2a6"
THEMES.append(dict(
    slug="12-midnight-champagne", name="Midnight Champagne", category="Luxury · Evening",
    blurb="Starry midnight navy with champagne foil, a turning monogram dial and twinkling stars.",
    theme_color="#0d1530",
    fonts="family=Cinzel:wght@400;600&family=Allura&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400",
    vars="--bg:#0d1530;--bg2:#111b3b;--ink:#f1e8d6;--muted:#aeb5cb;--accent:#e8d2a6;--accent2:#fff;--gold:#e8d2a6;--gold-hi:#fffaf0;--line:rgba(232,210,166,.35);--card:rgba(255,255,255,.04);--card-solid:#fbf6ec;--on-accent:#0d1530;--radius:50px;--in-radius:12px;--input-bg:rgba(0,0,0,.2);"
         "--f-display:'Cinzel',serif;--f-script:'Allura',cursive;--f-body:'Cormorant Garamond',serif;--f-native:'Cormorant Garamond',serif;"
         "--op-back:#050914;--cur:linear-gradient(90deg,rgba(0,0,0,.4),transparent 30%,rgba(255,255,255,.07) 50%,transparent 70%,rgba(0,0,0,.4)) 0 0/40px 100%,#1a2550;"
         "--valance:radial-gradient(circle at 50% 0,#e8d2a6 0 6px,transparent 7px) 0 62px/24px 12px repeat-x,linear-gradient(#0d1530,#1f2c5c 80%,#e8d2a6 80% 85%,#0d1530 85%);"
         "--op-ink:#e8d2a6;--seal:#e8d2a6;--seal-hi:#fffaf0;--seal-lo:#9c8452;--seal-ink:#0d1530",
    opener="curtain", opener_decor="",
    hero=(f'<div class="mono-wrap h-in" style="--d:0">{monogram_ring(C)}<span class="mono-txt" data-f="c.initials"></span></div>'
          + T(1, "tagline", "kicker") + names(2, "names shimmer") + hdate(3) + T(4, "venueLine", "h-venue")),
    divider=diamond_orn(C, "divider"), st_orn=diamond_orn(C), ev_icon=monogram_ring(C),
    css=COMMON_HERO_CSS + """
.hero{background:radial-gradient(ellipse at 50% 110%,#2a3a74,transparent 60%),radial-gradient(ellipse at 50% 0,#17214a,#0d1530 70%)}
.mono-wrap{position:relative;width:min(200px,50vw);aspect-ratio:1;margin-bottom:26px}
.mono-ring{width:100%;height:100%}
.mono-ring .spin{animation:spin 60s linear infinite;transform-origin:center}
.mono-txt{position:absolute;inset:0;display:grid;place-items:center;font-family:var(--f-display);font-size:clamp(2.2rem,11vw,3.4rem);letter-spacing:.14em;color:var(--gold);padding-left:.14em}
.names{font-size:clamp(3.6rem,17vw,6.8rem);line-height:.95;margin:10px 0}
.names .amp{font-family:var(--f-display);font-size:.26em;letter-spacing:.3em}
.sec:nth-of-type(even){background:var(--bg2)}
.st{color:var(--gold)}
.event{border-radius:24px}
.ev-ico{width:54px;height:54px}
footer{background:#080e22}
""",
    theme={"particles": {"type": "dot", "colors": ["#fffaf0", "#e8d2a6", "#cfd8ff"], "size": [2, 6], "count": 70, "speed": .3, "mode": "twinkle", "glow": 8}},
    data=dict(
        slug="kavindu-senuri", partner1="Kavindu", partner2="Senuri",
        fullName1="Kavindu Sachintha Herath", fullName2="Senuri Tharaka Wickramasinghe",
        parents1="Son of Mr. & Mrs. Nandana Herath", parents2="Daughter of Mr. & Mrs. Sarath Wickramasinghe",
        tagline="Under a sky full of stars, join us for the wedding of",
        hostLine="Together with our families, we invite you to an evening of love and celebration",
        inviteText="Cocktails at sunset, dinner under the stars and dancing until midnight — it wouldn't be complete without you.",
        quote="You are my today and all of my tomorrows.", quoteSource="Kavindu & Senuri",
        date="2027-10-09T18:00:00+05:30", venueLine="Cinnamon Life · Colombo",
        events=[
            dict(name="Ceremony", time="2027-10-09T18:00:00+05:30", timeLabel="6.00 p.m.", venue="Cinnamon Life · Sky Terrace", address="Colombo 02"),
            dict(name="Dinner & Dancing", time="2027-10-09T19:30:00+05:30", timeLabel="7.30 p.m. until midnight", venue="Cinnamon Life · Grand Ballroom", address="Colombo 02"),
        ],
        dressCode="Evening formal — midnight blues, silver and champagne.", dressColors=["#0d1530", "#e8d2a6", "#aeb5cb"],
        hashtag="#KaviSenuriUnderTheStars", blessing="", rsvp=dict(RSVP), brand=BRAND,
        labels={"countdown": "Until our starry night"},
    )))

# ---------------------------------------------------------------- 13
THEMES.append(dict(
    slug="13-modern-minimal", name="Modern Minimal", category="Modern · Editorial",
    blurb="Gallery-white editorial layout with oversized serif type, a clean grid and crisp reveals.",
    theme_color="#111111",
    fonts="family=Instrument+Serif:ital@0;1&family=Syne:wght@400;600&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500",
    vars="--bg:#f4f2ee;--bg2:#ebe8e2;--ink:#111;--muted:#6d6a64;--accent:#111;--accent2:#c2522d;--gold:#c2522d;--gold-hi:#e98a66;--line:rgba(17,17,17,.18);--card:#fff;--card-solid:#fff;--on-accent:#f4f2ee;--radius:0;--btn-radius:0;--in-radius:0;"
         "--f-display:'Instrument Serif',serif;--f-script:'Instrument Serif',serif;--f-body:'DM Sans',sans-serif;--f-native:'DM Sans',sans-serif;"
         "--op-bg:#111;--op-ink:#f4f2ee",
    opener="minimal", opener_decor="",
    hero=('<div class="grid-lines"><i></i><i></i><i></i></div>'
          '<div class="mm-top h-in" style="--d:0"><span data-f="greeting"></span><span data-f="c.dateDots"></span></div>'
          '<h1 class="mm-names"><span class="ln"><span data-f="partner1"></span></span><span class="ln amp2"><span>&amp;</span></span><span class="ln"><span data-f="partner2"></span></span></h1>'
          + T(4, "tagline", "mm-tag")
          + '<div class="mm-bot h-in" style="--d:5"><span data-f="venueLine"></span><span data-f="c.weekday"></span></div>'),
    divider='<span class="mm-rule"></span>', st_orn='<span class="mm-num"></span>', ev_icon="",
    css=COMMON_HERO_CSS + """
.hero{align-items:stretch;justify-content:space-between;text-align:left;padding:28px 22px}
.grid-lines{position:absolute;inset:0;display:grid;grid-template-columns:repeat(4,1fr);pointer-events:none}
.grid-lines i{border-right:1px solid var(--line);transform:scaleY(0);transform-origin:top;transition:transform 1.6s cubic-bezier(.7,0,.2,1)}
.grid-lines i:nth-child(2){transition-delay:.15s}.grid-lines i:nth-child(3){transition-delay:.3s}
body.opened .grid-lines i{transform:none}
.mm-top,.mm-bot{position:relative;display:flex;justify-content:space-between;gap:12px;font-family:'Syne',sans-serif;font-size:.72rem;letter-spacing:.2em;text-transform:uppercase}
.mm-names{position:relative;font-family:var(--f-display);font-weight:400;font-size:clamp(4.2rem,24vw,11rem);line-height:.86;letter-spacing:-.02em;margin-top:auto}
.mm-names .ln{display:block;overflow:hidden}
.mm-names .ln>span{display:inline-block;transform:translateY(105%);transition:transform 1.3s cubic-bezier(.2,.8,.2,1)}
.mm-names .ln:nth-child(2)>span{transition-delay:.15s}.mm-names .ln:nth-child(3)>span{transition-delay:.3s}
body.opened .mm-names .ln>span{transform:none}
.amp2{font-style:italic;color:var(--accent2);padding-left:18vw}
.mm-tag{position:relative;font-family:var(--f-display);font-style:italic;font-size:1.3rem;max-width:340px;margin:18px 0 auto;color:var(--muted)}
.mm-bot{border-top:1px solid var(--ink);padding-top:12px}
.mm-rule{display:block;width:64px;height:2px;background:var(--accent2);margin:0 auto 30px}
.sec{border-top:1px solid var(--line)}
.st{font-family:var(--f-display);font-size:clamp(2.4rem,10vw,4rem);letter-spacing:-.01em;line-height:1;color:var(--ink)}
main{counter-reset:sec}
.mm-num{display:block;font-family:'Syne',sans-serif;font-size:.7rem;letter-spacing:.3em;color:var(--accent2);margin-bottom:10px;counter-increment:sec}
.mm-num::before{content:"0" counter(sec) " /"}
.couple h3{font-family:var(--f-display);font-size:2rem;color:var(--ink)}
.couple .and{font-family:var(--f-display);font-style:italic;color:var(--accent2)}
.quote blockquote{font-size:clamp(1.6rem,6.5vw,2.6rem);line-height:1.2;font-style:italic}
.cd-box{border-radius:0;background:transparent;border:0;border-left:1px solid var(--line)}
.cd-box:first-child{border-left:0}
.cd-n{font-size:clamp(2.4rem,11vw,4rem);color:var(--ink)}
.ev-ico{display:none}
.event{text-align:left;border:1px solid var(--ink);padding:26px 22px}
.ev-name{font-size:2rem}
.ev-actions{justify-content:flex-start}
.btn{letter-spacing:.14em}
.f-names{font-family:var(--f-display);font-style:italic}
.thanks .t-big{font-family:var(--f-display);font-style:italic}
.op-min .mono{font-family:'Instrument Serif',serif;font-style:italic}
""",
    theme={"openMs": 1200},
    data=dict(
        slug="yohan-piumi", partner1="Yohan", partner2="Piumi",
        fullName1="Yohan Chathura Silva", fullName2="Piumi Hansika Dissanayake",
        parents1="", parents2="", greeting="We're getting married",
        tagline="Save the date and come celebrate with us.",
        hostLine="", inviteText="Good food, great music and all our favourite people in one room. That's the plan — and you're part of it.",
        quote="Whatever our souls are made of, his and mine are the same.", quoteSource="Emily Brontë",
        date="2027-11-20T17:00:00+05:30", venueLine="Park Street Mews · Colombo",
        events=[
            dict(name="Ceremony", time="2027-11-20T17:00:00+05:30", timeLabel="5.00 p.m.", venue="Park Street Mews", address="50/1 Park Street, Colombo 02"),
            dict(name="Party", time="2027-11-20T19:00:00+05:30", timeLabel="7.00 p.m. — late", venue="Park Street Mews · Courtyard", address="Colombo 02"),
        ],
        dressCode="Smart casual. Neutrals and a pop of colour.", dressColors=["#111111", "#f4f2ee", "#c2522d"],
        hashtag="#YohanPlusPiumi", blessing="", rsvp=dict(RSVP), brand=BRAND,
        labels={"tap": "Open", "invited": "An invitation", "countdown": "Countdown", "events": "The Plan", "rsvp": "RSVP", "dress": "What to wear"},
    )))

# ---------------------------------------------------------------- 14
THEMES.append(dict(
    slug="14-coastal-vows", name="Coastal Vows", category="Modern · Beach",
    blurb="Sunset sand and ocean teal with rolling animated waves and palm silhouettes — made for Bentota and Galle.",
    theme_color="#1f6f78",
    fonts="family=Allura&family=Josefin+Sans:wght@300;400;600&family=Lora:ital@0;1",
    vars="--bg:#f6efe3;--bg2:#efe4d1;--ink:#20393d;--muted:#6f7f7c;--accent:#1f6f78;--accent2:#d9744f;--gold:#d9744f;--gold-hi:#f7b99c;--line:rgba(31,111,120,.25);--card:#fffaf2;--card-solid:#fffaf2;--on-accent:#fff;--radius:20px;--in-radius:10px;"
         "--f-display:'Josefin Sans',sans-serif;--f-script:'Allura',cursive;--f-body:'Lora',serif;--f-native:'Lora',serif;"
         "--op-bg:linear-gradient(#fde2c4,#f6efe3 60%,#bfe0dc);--env-back:#1f6f78;--env-front:linear-gradient(160deg,#3d9ea3,#2a8088);--env-flap:linear-gradient(#63b7b8,#3d9ea3);--op-ink:#1f6f78;--seal:#d9744f;--seal-hi:#f7b99c;--seal-lo:#8e3d20;--seal-ink:#fff",
    opener="envelope", opener_decor='<p class="kicker" style="color:#1f6f78;margin-bottom:4px">Save the date</p>',
    hero=('<div class="sun"></div>' + f'<div class="palm-l">{palm("#2b4a48")}</div><div class="palm-r">{palm("#2b4a48")}</div>'
          + T(0, "greeting", "kicker") + names(1) + T(2, "tagline", "tagline") + hdate(3) + T(4, "venueLine", "h-venue") + waves()),
    divider=leaf_orn("#1f6f78", "divider"), st_orn=leaf_orn("#d9744f"),
    ev_icon='<svg viewBox="0 0 60 60" aria-hidden="true"><circle cx="30" cy="26" r="12" fill="#f7b99c"/><path d="M4 40q6-5 13 0t13 0 13 0 13 0M4 48q6-5 13 0t13 0 13 0 13 0" stroke="#1f6f78" stroke-width="2.4" fill="none" stroke-linecap="round"/></svg>',
    css=COMMON_HERO_CSS + """
.hero{background:linear-gradient(#fbd9b8 0,#fde9d2 35%,#f6efe3 70%);justify-content:flex-start;padding-top:14svh}
.sun{position:absolute;left:50%;bottom:26%;width:min(340px,80vw);aspect-ratio:1;translate:-50% 50%;border-radius:50%;background:radial-gradient(circle,#ffd3a8,#f7b99c 55%,transparent 70%);opacity:.9;animation:sunrise 3s 1s both}
body:not(.opened) .sun{animation-play-state:paused}
@keyframes sunrise{from{transform:translateY(80px);opacity:0}to{transform:none;opacity:.9}}
.palm-l,.palm-r{position:absolute;bottom:14%;width:min(170px,34vw);transform-origin:bottom center;animation:palm 6s ease-in-out infinite alternate}
.palm-l{left:-30px}.palm-r{right:-30px;transform:scaleX(-1);animation-name:palmr}
@keyframes palm{from{rotate:-2deg}to{rotate:2deg}}
@keyframes palmr{from{rotate:2deg}to{rotate:-2deg}}
.waves{position:absolute;left:0;right:0;bottom:0;height:24svh;min-height:150px;overflow:hidden}
.wv{position:absolute;left:0;bottom:0;width:200%;max-width:none;height:100%;animation:wave 14s linear infinite}
.w2{animation-duration:10s;animation-direction:reverse}.w3{animation-duration:18s}.w4{animation-duration:22s;animation-direction:reverse}
@keyframes wave{to{transform:translateX(-50%)}}
.kicker{color:var(--accent2)}
.names{font-size:clamp(4rem,19vw,7.4rem);line-height:.9;margin:8px 0}
.names .amp{font-family:var(--f-display);font-size:.2em;letter-spacing:.3em;color:var(--accent2);margin:8px 0}
.hd-side{font-family:var(--f-display)}
.hd-day{font-family:var(--f-display);font-weight:300}
.sec:nth-of-type(even){background:var(--bg2)}
.st{font-weight:300;letter-spacing:.2em;text-transform:uppercase;font-size:clamp(1.2rem,5vw,1.7rem)}
.event{box-shadow:0 20px 40px -30px rgba(31,111,120,.6)}
.ev-time{color:var(--accent2)}
.cd-box{border-radius:14px}
footer{background:linear-gradient(#f6efe3,#cfe6e2)}
""",
    theme={"particles": {"type": "bubble", "colors": ["rgba(255,255,255,.9)", "rgba(191,224,220,.9)"], "size": [6, 14], "count": 16, "speed": .5, "dir": -1}, "openMs": 2000},
    data=dict(
        slug="kevin-anjali", partner1="Kevin", partner2="Anjali",
        fullName1="Kevin Rehan Jansz", fullName2="Anjali Sachini Mendis",
        parents1="Son of Mr. & Mrs. Rohan Jansz", parents2="Daughter of Mr. & Mrs. Nihal Mendis",
        greeting="Barefoot & in love", tagline="Join us on the sand as we say I do.",
        hostLine="Sunset vows by the Indian Ocean",
        inviteText="Kick off your shoes and celebrate with us — sunset vows, fresh seafood and dancing under the palms.",
        quote="I love you more than the ocean has waves.", quoteSource="Kevin & Anjali",
        date="2027-03-27T16:30:00+05:30", venueLine="Taj Bentota Resort & Spa",
        events=[
            dict(name="Beach Ceremony", time="2027-03-27T16:30:00+05:30", timeLabel="4.30 p.m. · sunset vows", venue="Taj Bentota Resort & Spa · Beach Lawn", address="Bentota", note="Flat shoes or bare feet recommended!"),
            dict(name="Seaside Reception", time="2027-03-27T18:30:00+05:30", timeLabel="6.30 p.m. until late", venue="Taj Bentota · Poolside Terrace", address="Bentota"),
        ],
        dressCode="Beach formal — linen, pastels and sandals.", dressColors=["#1f6f78", "#f7b99c", "#f6efe3"],
        hashtag="#KevinAnjaliSaidIDo", blessing="", rsvp=dict(RSVP), brand=BRAND,
        labels={"countdown": "Until we hit the beach", "events": "Beach Day"},
    )))

# ---------------------------------------------------------------- 15
THEMES.append(dict(
    slug="15-tea-country", name="Tea Country", category="Modern · Botanical",
    blurb="Misty hill-country greens with layered tea terraces, arching leaf sprigs and drifting leaves.",
    theme_color="#34462f",
    fonts="family=Ballet:opsz@16..72&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Figtree:wght@300;400;500",
    vars="--bg:#f3efe6;--bg2:#e9e6d8;--ink:#2c3527;--muted:#6d7563;--accent:#34462f;--accent2:#b86a45;--gold:#b86a45;--gold-hi:#e7a585;--line:rgba(52,70,47,.22);--card:#fbf9f3;--card-solid:#fbf9f3;--on-accent:#f3efe6;--radius:8px;--in-radius:6px;"
         "--f-display:'Cormorant Garamond',serif;--f-script:'Ballet',cursive;--f-body:'Figtree',sans-serif;--f-native:'Cormorant Garamond',serif;"
         "--op-bg:linear-gradient(#e9eee0,#dfe6d3);--env-back:#4a6340;--env-front:linear-gradient(160deg,#6f8a5e,#5a7650);--env-flap:linear-gradient(#8aa276,#6f8a5e);--op-ink:#34462f;--seal:#b86a45;--seal-hi:#e7a585;--seal-lo:#6e3219;--seal-ink:#f3efe6",
    opener="envelope", opener_decor=f'<div style="width:28px;margin:0 auto">{sprig("#6f8a5e", "", 5, "#9fb38e")}</div>',
    hero=('<div class="mist"></div>' + hills()
          + f'<div class="wreath"><div class="sp l">{sprig("#4a6340", "", 7, "#7d8f69")}</div><div class="sp r">{sprig("#4a6340", "", 7, "#7d8f69")}</div>'
          + '<div class="wr-in">' + T(0, "greeting", "kicker") + names(1) + T(2, "tagline", "tagline") + '</div></div>'
          + hdate(3) + T(4, "venueLine", "h-venue")),
    divider=leaf_orn("#4a6340", "divider"), st_orn=leaf_orn("#b86a45"), ev_icon=sprig("#4a6340", "", 5, "#7d8f69"),
    css=COMMON_HERO_CSS + """
.hero{background:linear-gradient(#f6f4ec,#eef0e4 60%,#dfe6d3);justify-content:flex-start;padding-top:12svh}
.hills{position:absolute;left:0;right:0;bottom:0;height:30svh;min-height:180px}
.hl{position:absolute;left:0;bottom:0;width:130%;max-width:none;height:100%;animation:drift 30s ease-in-out infinite alternate}
.h1{height:100%;animation-duration:40s}.h2{height:78%;animation-duration:32s;animation-direction:alternate-reverse}.h3{height:58%}.h4{height:36%;animation-duration:26s;animation-direction:alternate-reverse}
@keyframes drift{from{transform:translateX(0)}to{transform:translateX(-18%)}}
.mist{position:absolute;left:-20%;right:-20%;bottom:18svh;height:120px;background:radial-gradient(ellipse,rgba(255,255,255,.85),transparent 70%);filter:blur(6px);z-index:1;animation:mist 16s ease-in-out infinite alternate}
@keyframes mist{to{transform:translateX(12%)}}
.wreath{position:relative;padding:30px 44px 10px;z-index:2}
.sp{position:absolute;top:0;width:60px;height:auto}
.sp svg{width:100%;height:auto}
.sp.l{left:-10px;transform:rotate(-8deg)}.sp.r{right:-10px;transform:scaleX(-1) rotate(-8deg)}
.sp svg{transform-origin:20% 95%;animation:sway 6s ease-in-out infinite alternate}
@keyframes sway{to{transform:rotate(3deg)}}
.kicker{color:var(--accent2)}
.names{font-size:clamp(3.2rem,15vw,5.8rem);line-height:1.3;margin:6px 0}
.names .amp{font-family:var(--f-display);font-style:italic;font-size:.5em;color:var(--accent2);line-height:.8}
.h-date,.h-venue{position:relative;z-index:2}
.sec:nth-of-type(even){background:var(--bg2)}
.ev-ico{width:34px;height:70px}
.event{border-top:3px solid var(--accent)}
.quote blockquote{color:var(--accent)}
footer{background:#34462f;color:#f3efe6}footer .f-names{color:#f3efe6}footer .brand{color:#f3efe6}
""",
    theme={"particles": {"type": "leaf", "colors": ["#6f8a5e", "#9fb38e", "#4a6340", "#b86a45"], "size": [6, 11], "count": 18, "flip": True, "speed": .7}},
    data=dict(
        slug="dilan-ishara", partner1="Dilan", partner2="Ishara",
        fullName1="Dilan Kaveesha Rathnayake", fullName2="Ishara Madhavi Bandara",
        parents1="Son of Mr. & Mrs. Premasiri Rathnayake, Badulla", parents2="Daughter of Mr. & Mrs. Wasantha Bandara, Nuwara Eliya",
        greeting="Up in the hills", tagline="we invite you to celebrate our wedding among the tea.",
        hostLine="Together with our families",
        inviteText="Cool mountain air, a cup of our finest and the people we love. Come celebrate with us in the hill country.",
        quote="Love grows slowly, like the finest tea — and is always worth the wait.", quoteSource="Dilan & Ishara",
        date="2027-04-17T10:05:00+05:30", venueLine="Heritance Tea Factory · Nuwara Eliya",
        events=[
            dict(name="Poruwa Ceremony", time="2027-04-17T10:05:00+05:30", timeLabel="Auspicious time · 10.05 a.m.", venue="Heritance Tea Factory", address="Kandapola, Nuwara Eliya", note="It gets chilly — bring a wrap!"),
            dict(name="Luncheon", time="2027-04-17T12:30:00+05:30", timeLabel="12.30 p.m. onwards", venue="Heritance Tea Factory · Garden Marquee", address="Kandapola, Nuwara Eliya"),
        ],
        dressCode="Garden formal — earthy greens, terracotta and cream.", dressColors=["#34462f", "#b86a45", "#f3efe6"],
        hashtag="#DilanIsharaInTheHills", blessing="", rsvp=dict(RSVP), brand=BRAND,
        labels={"events": "The Day"},
    )))
