import os, sys, json, copy
from datetime import datetime, timedelta
sys.path.insert(0, os.path.dirname(__file__))
from engine2 import page2
from themes2 import P
from art import wax_seal, tree_emblem
OUT = os.path.join(os.path.dirname(__file__), "..", "out")
os.makedirs(os.path.join(OUT, "premium"), exist_ok=True)
MUSIC = {'p01': ('magulbera', {}), 'p02': ('magulflute', {}), 'p03': ('musicbox', {'key': 57, 'bpm': 62, 'prog': [[0, 3, 7], [8, 12, 15], [3, 7, 10], [10, 14, 17]]}), 'p04': ('musicbox', {'key': 65, 'bpm': 58, 'bell': True}), 'p05': ('magulbera', {'bpm': 116}), 'p06': ('musicbox', {'key': 60, 'bpm': 64, 'prog': [[9, 12, 16], [5, 9, 12], [0, 4, 7], [7, 11, 14]]}), 'p07': ('musicbox', {'key': 67, 'bpm': 72, 'bell': True, 'decay': 1.5}), 'p08': ('musicbox', {'key': 65, 'bpm': 66}), 'p09': ('organ', {}), 'p10': ('magulflute', {'root': 72})}
meta = []
for t in P:
    t = copy.deepcopy(t)
    d = t["data"]
    d["rsvp"]["deadline"] = (datetime.fromisoformat(d["date"]) - timedelta(days=28)).strftime("%Y-%m-%d")
    if "seal_colors" in t:
        c1, c2, c3 = t["seal_colors"]
        em = tree_emblem(c3) if t.get("seal_emblem") == "tree" else ""
        txt = "" if em else f'{d["partner1"][0]} · {d["partner2"][0]}'
        t["seal"] = wax_seal("ws" + t["slug"][:3], c1, c2, c3, txt, em, ink=c3 + "cc")
        t["hero"] = t["hero"].replace("{SEAL}", wax_seal("wh" + t["slug"][:3], c1, c2, c3, txt, em, ink=c3 + "cc", seed=8))
    st, mo = MUSIC[t["slug"][:3]]
    t.setdefault("theme", {})["music"] = dict(style=st, **mo)
    if st == "daf": t["data"]["musicOnOpen"] = False
    html = page2(t)
    fn = f'{t["slug"]}.html'
    open(os.path.join(OUT, "premium", fn), "w", encoding="utf-8").write(html)
    meta.append(dict(file="premium/" + fn, name=t["name"], category=t["category"], blurb=t["blurb"], color=t["theme_color"]))
    print(f'{fn:30s} {len(html)//1024:4d} KB')
json.dump(meta, open(os.path.join(OUT, "meta2.json"), "w"), indent=1)
