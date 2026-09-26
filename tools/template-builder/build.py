import os, sys, json, copy
sys.path.insert(0, os.path.dirname(__file__))
from engine import page
from themes import THEMES

OUT = os.path.join(os.path.dirname(__file__), "..", "out")
os.makedirs(os.path.join(OUT, "templates"), exist_ok=True)
MUSIC = {'01': ('magulbera', {}), '02': ('magulbera', {'bpm': 120}), '03': ('magulflute', {}), '04': ('magulflute', {'root': 72}), '05': ('mangala', {}), '06': ('mangala', {'root': 65, 'bpm': 80}), '07': ('daf', {}), '08': ('daf', {'bpm': 84}), '09': ('organ', {}), '10': ('organ', {'bpm': 54}), '11': ('musicbox', {'key': 57, 'bpm': 62}), '12': ('musicbox', {'key': 64, 'bpm': 60, 'bell': True}), '13': ('musicbox', {'key': 65, 'bpm': 72}), '14': ('musicbox', {'key': 67, 'bpm': 76, 'bell': True}), '15': ('magulflute', {'bpm': 76, 'root': 76})}
meta = []
for t in THEMES:
    t = copy.deepcopy(t)
    from datetime import datetime, timedelta
    d = datetime.fromisoformat(t["data"]["date"])
    t["data"]["rsvp"]["deadline"] = (d - timedelta(days=28)).strftime("%Y-%m-%d")
    st, mo = MUSIC[t["slug"][:2]]
    t.setdefault("theme", {})["music"] = dict(style=st, **mo)
    if st == "daf": t["data"]["musicOnOpen"] = False
    html = page(t)
    fn = f'{t["slug"]}.html'
    with open(os.path.join(OUT, "templates", fn), "w", encoding="utf-8") as fh:
        fh.write(html)
    meta.append(dict(file=fn, name=t["name"], category=t["category"], blurb=t["blurb"], color=t["theme_color"]))
    print(f'{fn:34s} {len(html)//1024:4d} KB')
with open(os.path.join(OUT, "meta.json"), "w") as fh:
    json.dump(meta, fh, indent=1)
