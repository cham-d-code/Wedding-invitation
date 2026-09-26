# Template builder

Python scripts that generate every invitation template, then assemble the website.

```bash
pip install pillow   # not required for building; only for the preview scripts you may add
python3 build.py        # 15 classic templates  -> tools/out/templates
python3 build2.py       # 10 premium templates  -> tools/out/premium
python3 build_site.py   # copies templates into the site and regenerates the HTML pages
```

- `themes.py` / `themes2.py` — colours, fonts, artwork and sample wording for each design
- `engine.py` / `engine2.py` — shared page layout, animations, RSVP, countdown, bottom menu
- `orn.py` / `art.py` — the ornaments and artwork (mandalas, perahera, florals, seals…), all drawn in code
- `music.js` — the built-in music for each tradition; `silk.js` — the silk fabric renderer

Add a design by copying one entry in `themes.py` or `themes2.py`, then run the three build steps.
Note: `build_site.py` rewrites index.html, templates.html, create.html, dashboard.html, privacy.html and 404.html.
Edit page copy there, not in the generated HTML.
