"""Premium engine: cover screens, music, bottom menu, story, album, venue."""
import json, os
from engine import BASE_CSS, JS, DEFAULT_LABELS

SILK_JS = open(os.path.join(os.path.dirname(__file__), "silk.js")).read()
from engine import MUSIC_JS, MUSIC_INIT

PREMIUM_LABELS = {
    "coverKicker": "The wedding of", "openBtn": "Open invitation", "invited2": "You are invited",
    "tapSeal": "Tap the seal to open", "dearGuest": "Our dear guest",
    "storyKicker": "Our story", "storyTitle": "How it all began",
    "eventsKicker": "Save the date", "albumKicker": "Moments", "albumTitle": "Our album",
    "venueKicker": "Location", "venueTitle": "The venue", "rsvpKicker": "Be our guest",
    "photoCouple": "Your couple photo", "photo": "Photo",
    "navHome": "Home", "navStory": "Story", "navEvents": "Events", "navAlbum": "Album", "navVenue": "Venue", "navRsvp": "RSVP",
    "music": "Music",
}

ICONS = {
    "sparkle": '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M12 2l1.8 6.2L20 10l-6.2 1.8L12 18l-1.8-6.2L4 10l6.2-1.8zM19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z" fill="currentColor"/></svg>',
    "leaf": '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M5 19C5 10 11 4 20 4c0 9-6 15-15 15zm0 0l8-8" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M12 20s-7-4.4-7-10a4 4 0 017-2.6A4 4 0 0119 10c0 5.6-7 10-7 10z" fill="currentColor"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M3 6h18v12H3zM3 6l9 7 9-7" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>',
    "hand": '<svg class="hand" viewBox="0 0 64 64" width="64" height="64" aria-hidden="true"><path d="M24 34V12a4 4 0 018 0v18l0-6a4 4 0 018 0v6-3a4 4 0 018 0v4-2a4 4 0 018 0v14c0 10-7 17-17 17h-3c-6 0-10-3-13-8l-8-13a4 4 0 016-5l5 6z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M18 8a14 14 0 0120 0" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" class="hand-wave"/></svg>',
}

MAP_SVG = '''<svg viewBox="0 0 320 170" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="320" height="170" fill="var(--map-bg)"/>
<path d="M-10 120C60 100 90 130 160 104S270 60 330 76" stroke="var(--map-road)" stroke-width="14" fill="none"/>
<path d="M-10 120C60 100 90 130 160 104S270 60 330 76" stroke="var(--map-bg)" stroke-width="1" stroke-dasharray="6 6" fill="none"/>
<path d="M120 -10L150 180M230 -10L200 180M-10 40H330" stroke="var(--map-road)" stroke-width="6" fill="none"/>
<path d="M40 -10L70 180M280 -10L300 180M-10 150H330" stroke="var(--map-road)" stroke-width="3" fill="none" opacity=".7"/>
<circle cx="260" cy="130" r="22" fill="var(--map-park)"/><rect x="18" y="56" width="60" height="34" rx="6" fill="var(--map-park)"/>
<g class="pin" transform="translate(172 70)"><ellipse cx="0" cy="30" rx="10" ry="3.5" fill="#0003"/><path d="M0 30C-4 20-14 12-14 0a14 14 0 0128 0c0 12-10 20-14 30z" fill="var(--accent)"/><circle cy="0" r="5.5" fill="var(--map-bg)"/></g></svg>'''

OPENERS2 = {
    "cover": """<div id="opener" class="op-cover" role="button" tabindex="0" aria-label="Open the invitation">
<div class="cv-bg">%%COVERBG%%</div>
<div class="op-center">%%DECOR%%<p class="cv-kicker" data-f="labels.coverKicker"></p><span class="cv-rule"><i></i></span>
<h2 class="cv-names"><span data-f="partner1"></span> <em>&amp;</em> <span data-f="partner2"></span></h2>
<p class="cv-date" data-f="c.dateOrd"></p><p class="cv-guest" data-f="c.guestOnly" data-opt></p>
<span class="cv-btn">%%ICON%%<span data-f="labels.openBtn"></span></span></div>%%COVERFG%%</div>""",
    "curtain2": """<div id="opener" class="op-cur2" role="button" tabindex="0" aria-label="Open the invitation">
<div class="cv-bg">%%COVERBG%%</div><div class="c2 l"></div><div class="c2 r"></div><div class="rod"></div>
<div class="op-center">%%DECOR%%</div></div>""",
    "envelope2": """<div id="opener" class="op-env2" role="button" tabindex="0" aria-label="Open the invitation">
<div class="cv-bg">%%COVERBG%%</div>
<div class="op-center"><p class="e2-kick" data-f="labels.invited2"></p><p class="e2-names"><span data-f="partner1"></span> &amp; <span data-f="partner2"></span></p>
<div class="env2"><div class="e2-back"></div><div class="e2-letter"><span class="e2-mono" data-f="c.monogram"></span><span class="e2-date" data-f="c.dateShort"></span></div>
<div class="e2-front"></div><div class="e2-flapw"><div class="e2-flap"></div></div><p class="e2-to" data-f="c.envTo"></p><div class="e2-seal">%%SEAL%%</div></div>
<p class="e2-tap" data-f="labels.tapSeal"></p></div>%%COVERFG%%</div>""",
}

BODY2 = """
<main>
<section class="hero" id="home">%%HERO%%</section>

<section class="sec couple-sec"><div class="inner">
  %%DIVIDER%%
  <p class="host rv" data-f="hostLine" data-opt></p>
  <div class="couple rv">
    <div><h3 data-f="fullName1"></h3><p data-f="parents1" data-opt></p></div>
    <div class="and">&amp;</div>
    <div><h3 data-f="fullName2"></h3><p data-f="parents2" data-opt></p></div>
  </div>
  <p class="invite-text rv" data-f="inviteText" data-opt></p>
</div></section>

<section class="sec story" id="story"><div class="inner">
  <p class="eyebrow rv" data-f="labels.storyKicker"></p><h2 class="st rv" data-f="labels.storyTitle"></h2>%%STORN%%
  <div class="story-photo rv"><div class="ph arch" data-photo="couplePhoto"></div></div>
  <p class="story-intro rv" data-f="storyIntro" data-opt></p>
  <ol class="timeline" id="timeline"></ol>
</div></section>

<section class="sec quote"><div class="inner rv">
  %%STORN%%<blockquote data-f="quote" data-opt="sec"></blockquote><cite data-f="quoteSource" data-opt></cite>
</div></section>

<section class="sec events-sec" id="events"><div class="inner">
  <p class="eyebrow rv" data-f="labels.eventsKicker"></p><h2 class="st rv" data-f="labels.countdown"></h2>%%STORN%%
  <div class="cd rv" id="countdown"></div>
  <p class="cd-date rv" data-f="c.dateLong"></p>
  <h2 class="st st-sub rv" data-f="labels.events"></h2>
  <div class="events-grid" id="events"></div>
</div></section>

<section class="sec album" id="album"><div class="inner">
  <p class="eyebrow rv" data-f="labels.albumKicker"></p><h2 class="st rv" data-f="labels.albumTitle"></h2>%%STORN%%
  <div class="album-grid" id="album-grid"></div>
</div></section>

<section class="sec venue" id="venue"><div class="inner">
  <p class="eyebrow rv" data-f="labels.venueKicker"></p><h2 class="st rv" data-f="labels.venueTitle"></h2>%%STORN%%
  <div class="venue-card rv"><div class="map" id="map">%%MAP%%</div>
    <div class="venue-body"><h3 data-f="venue.name"></h3><p class="muted" data-f="venue.address"></p><p class="ev-note" data-f="venue.note" data-opt></p>
    <div class="ev-actions"><a class="btn" id="venue-dir" target="_blank" rel="noopener" data-f="labels.map"></a></div></div></div>
</div></section>

<section class="sec dress"><div class="inner rv">
  %%STORN%%<h2 class="st" data-f="labels.dress"></h2>
  <p data-f="dressCode" data-opt="sec"></p><div class="swatches" id="swatches"></div>
</div></section>

<section class="sec rsvp-sec" id="rsvp"><div class="inner">
  <p class="eyebrow rv" data-f="labels.rsvpKicker"></p><h2 class="st rv" data-f="labels.rsvp"></h2>%%STORN%%
  <p class="deadline rv" data-f="c.deadlineLine" data-opt></p>
  <div class="rsvp-card rv">
    <form id="rsvp-form" novalidate>
      <div class="field"><label for="gname" data-f="labels.yourName"></label><input type="text" id="gname" name="gname" required autocomplete="name"></div>
      <div class="field"><span class="lbl" data-f="labels.attending"></span><div class="seg">
        <label><input type="radio" name="attending" value="yes" checked><span data-f="labels.accept"></span></label>
        <label><input type="radio" name="attending" value="no"><span data-f="labels.decline"></span></label></div></div>
      <div class="field" id="guests-field"><label for="guests" data-f="labels.guests"></label><select id="guests" name="guests"></select></div>
      <div class="field" id="ev-field"><span class="lbl" data-f="labels.which"></span><div class="chks" id="rsvp-events"></div></div>
      <div class="field"><label for="message" data-f="labels.message"></label><textarea id="message" name="message"></textarea></div>
      <div class="rsvp-actions"><button class="btn" type="submit" data-f="labels.send"></button><button class="btn ghost" type="button" id="rsvp-wa" data-f="labels.whatsapp"></button></div>
    </form>
    <div class="thanks" id="rsvp-thanks" hidden><p class="t-big" data-f="labels.thanks"></p><p class="t-msg"></p></div>
  </div>
</div></section>

<footer>
  %%DIVIDER%%
  <p class="f-names"><span data-f="partner1"></span> &amp; <span data-f="partner2"></span></p>
  <p class="f-tag" data-f="hashtag" data-opt></p>
  <p class="f-bless" data-f="blessing" data-opt></p>
  <p class="brand" data-f="brand" data-opt></p>
</footer>
%%FOOTART%%
</main>
<nav class="bnav" id="bnav" aria-label="Sections"></nav>
<button class="music" id="music" type="button" aria-pressed="false">
<svg class="m-on" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M4 9h4l5-4v14l-5-4H4z" fill="currentColor"/><path d="M16 8.5a5 5 0 010 7M18.5 6a8.5 8.5 0 010 12" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
<svg class="m-off" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M4 9h4l5-4v14l-5-4H4z" fill="currentColor"/><path d="M16.5 9.5l5 5M21.5 9.5l-5 5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
<span class="sr" data-f="labels.music"></span></button>
<div class="lightbox" id="lightbox" hidden><img alt=""><button type="button" aria-label="Close">&times;</button></div>
<template id="ev-ico">%%EVICON%%</template>
"""

PREMIUM_CSS = r"""
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.eyebrow{font-family:var(--f-label,var(--f-body));font-size:.7rem;letter-spacing:.34em;text-transform:uppercase;color:var(--gold);margin-bottom:10px}
.st{text-wrap:balance}
.st-sub{margin-top:64px}
.sec{scroll-margin-top:10px}
body{padding-bottom:0}
/* cover */
.cv-bg{position:absolute;inset:0;overflow:hidden;transition:transform 1.6s cubic-bezier(.6,0,.2,1),filter 1.6s}
.cv-bg canvas,.cv-bg>svg{position:absolute;inset:0;width:100%;height:100%}
.op-cover.opening .cv-bg,.op-env2.opening .cv-bg{transform:scale(1.12);filter:blur(3px)}
.op-cover .op-center{gap:0}
.cv-kicker,.e2-kick{font-family:var(--f-label,var(--f-body));font-size:.7rem;letter-spacing:.42em;text-transform:uppercase;color:var(--op-ink);opacity:.85}
.cv-rule{display:flex;align-items:center;gap:10px;margin:22px 0 18px;color:var(--gold)}
.cv-rule::before,.cv-rule::after{content:"";width:64px;height:1px;background:currentColor;opacity:.7}
.cv-rule i{width:7px;height:7px;background:currentColor;transform:rotate(45deg)}
.cv-names{font-family:var(--f-script);font-weight:400;font-size:clamp(2.2rem,10vw,3.4rem);color:var(--op-names,var(--accent));line-height:1.15}
.cv-names em{font-style:normal;color:var(--gold)}
.cv-date{margin-top:10px;color:var(--op-ink);font-size:1.02rem}
.cv-guest{margin-top:16px;font-style:italic;color:var(--op-ink)}
.cv-btn{margin-top:30px;display:inline-flex;align-items:center;gap:10px;padding:14px 26px;border:1.5px solid var(--cv-btn,var(--accent));color:var(--cv-btn,var(--accent));border-radius:999px;font-family:var(--f-label,var(--f-body));font-size:.72rem;letter-spacing:.3em;text-transform:uppercase;background:var(--cv-btn-bg,transparent);box-shadow:var(--cv-btn-shadow,none);animation:cvb 2.6s ease-in-out infinite}
@keyframes cvb{50%{transform:translateY(-3px)}}
.op-cover .op-center>*{animation:cvin 1.2s both}
.op-cover .op-center>*:nth-child(2){animation-delay:.15s}.op-cover .op-center>*:nth-child(3){animation-delay:.3s}.op-cover .op-center>*:nth-child(4){animation-delay:.45s}.op-cover .op-center>*:nth-child(5){animation-delay:.6s}.op-cover .op-center>.cv-btn{animation:cvin 1.2s .8s both,cvb 2.6s 2s ease-in-out infinite}
@keyframes cvin{from{opacity:0;transform:translateY(16px)}}
/* realistic curtain */
.op-cur2 .c2{position:absolute;top:0;bottom:0;width:50.6%;background:var(--cur2);z-index:2;transition:transform 2.1s cubic-bezier(.65,0,.25,1),filter 2.1s;box-shadow:0 0 40px rgba(0,0,0,.5)}
.op-cur2 .c2::before{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.45),transparent 18%,transparent 70%,rgba(0,0,0,.4)),radial-gradient(ellipse at 50% 40%,rgba(255,255,255,.08),transparent 60%)}
.op-cur2 .c2::after{content:"";position:absolute;left:0;right:0;bottom:0;height:34px;background:radial-gradient(ellipse 22px 16px at 50% 0,transparent 96%,var(--cur-hem) 100%) 0 0/44px 34px repeat-x;opacity:.9}
.op-cur2 .c2.l{left:0;transform-origin:0 0}.op-cur2 .c2.r{right:0;transform-origin:100% 0}
.op-cur2.opening .c2.l{transform:scaleX(.14) skewY(4deg);filter:brightness(.8)}
.op-cur2.opening .c2.r{transform:scaleX(.14) skewY(-4deg);filter:brightness(.8)}
.op-cur2 .rod{position:absolute;top:0;left:0;right:0;height:var(--rod-h,0);background:var(--rod);z-index:3;box-shadow:0 3px 8px rgba(0,0,0,.4)}
.op-cur2 .op-center{z-index:4}
.hand{color:var(--op-ink);animation:tapme 1.8s ease-in-out infinite}
.hand-wave{animation:pulse 1.8s infinite}
@keyframes tapme{0%,100%{transform:translateY(0)}40%{transform:translateY(6px) scale(.96)}}
/* envelope 2 */
.op-env2 .op-center{justify-content:space-between;padding:12svh 20px 9svh}
.e2-names{font-family:var(--f-script);font-size:clamp(1.8rem,8vw,2.4rem);color:var(--op-names,var(--gold));margin-top:8px}
.env2{position:relative;width:min(84vw,360px);aspect-ratio:1.45;perspective:1400px;filter:drop-shadow(0 22px 26px rgba(0,0,0,.35))}
.env2>*{position:absolute}
.e2-back{inset:0;background:var(--e2-inner);border-radius:4px}
.e2-letter{left:5%;right:5%;top:5%;height:88%;background:var(--card-solid);border-radius:3px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;transition:transform 1s .95s cubic-bezier(.3,.8,.3,1);box-shadow:0 2px 8px rgba(0,0,0,.15)}
.e2-mono{font-family:var(--f-script);font-size:2.2rem;color:var(--accent)}
.e2-date{font-size:.7rem;letter-spacing:.3em;text-transform:uppercase;color:var(--muted)}
.e2-front{inset:0;background:var(--e2-paper);clip-path:polygon(0 0,50% 52%,100% 0,100% 100%,0 100%);border-radius:4px}
.e2-front::after{content:"";position:absolute;inset:0;background:linear-gradient(160deg,transparent 40%,rgba(0,0,0,.12))}
.e2-flapw{left:0;right:0;top:0;height:64%;z-index:4;transform-origin:top center;transition:transform .9s .3s cubic-bezier(.5,0,.3,1),z-index 0s .75s;filter:drop-shadow(0 3px 3px rgba(0,0,0,.22))}
.e2-flap{position:absolute;inset:0;background:var(--e2-flap);clip-path:polygon(0 0,100% 0,52% 97%,50% 100%,48% 97%)}
.e2-to{left:0;right:0;top:20%;z-index:5;text-align:center;font-family:var(--f-script);font-size:1.35rem;color:var(--e2-ink);transition:opacity .3s}
.e2-seal{left:50%;top:64%;width:84px;height:84px;margin:-42px 0 0 -42px;z-index:6;transition:transform .45s,opacity .45s}
.e2-seal svg{width:100%;height:100%}
.e2-tap{font-family:var(--f-label,var(--f-body));font-size:.68rem;letter-spacing:.42em;text-transform:uppercase;color:var(--op-ink);animation:pulse 2.2s infinite}
.op-env2.opening .e2-seal{transform:scale(1.35) rotate(-12deg);opacity:0}
.op-env2.opening .e2-to{opacity:0}
.op-env2.opening .e2-flapw{transform:rotateX(180deg);z-index:1}
.op-env2.opening .e2-letter{transform:translateY(-62%)}
.op-env2.opening .e2-kick,.op-env2.opening .e2-names,.op-env2.opening .e2-tap{opacity:0;transition:opacity .5s}
.op-env2.opening .op-center{opacity:1;transform:none}
.op-env2.opening .env2{animation:envzoom .9s 1.8s forwards}
@keyframes envzoom{to{transform:scale(1.25);opacity:0}}
/* silk canvas + frieze */
.silk-cv{position:absolute;inset:0;width:100%;height:100%;display:block}
.frieze{position:absolute;left:0;bottom:0;display:flex;width:max-content;animation:march 60s linear infinite;pointer-events:none}
.frieze svg{height:var(--frieze-h,78px);width:auto;flex:none}
@keyframes march{to{transform:translateX(-50%)}}
/* story */
.story-photo{max-width:300px;margin:30px auto 0}
.ph{position:relative;width:100%;aspect-ratio:4/5;border-radius:var(--ph-radius,6px);overflow:hidden;background:var(--ph-bg);display:grid;place-items:center;background-size:cover;background-position:center}
.ph.arch{border-radius:999px 999px 8px 8px;aspect-ratio:3/4;outline:1px solid var(--line);outline-offset:8px}
.ph.empty::before{content:attr(data-mono);font-family:var(--f-script);font-size:3.2rem;color:var(--ph-ink);opacity:.8}
.ph.empty::after{content:attr(data-label);position:absolute;bottom:14px;left:0;right:0;text-align:center;font-size:.62rem;letter-spacing:.3em;text-transform:uppercase;color:var(--ph-ink);opacity:.8}
.story-intro{max-width:520px;margin:34px auto 0}
.timeline{list-style:none;max-width:560px;margin:40px auto 0;position:relative;text-align:left;padding-left:34px}
.timeline::before{content:"";position:absolute;left:10px;top:6px;bottom:6px;width:1px;background:linear-gradient(var(--gold),var(--line))}
.timeline li{position:relative;padding-bottom:30px}
.timeline li::before{content:"";position:absolute;left:-29px;top:6px;width:11px;height:11px;border-radius:50%;background:var(--bg);border:1.5px solid var(--gold);box-shadow:0 0 0 4px var(--bg)}
.tl-date{font-size:.7rem;letter-spacing:.28em;text-transform:uppercase;color:var(--gold)}
.tl-title{font-family:var(--f-display);font-size:1.35rem;color:var(--accent);line-height:1.3;margin:2px 0 4px}
.tl-text{font-size:.95rem;color:var(--muted)}
/* album */
.album-grid{display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:120px;gap:10px;margin-top:34px}
.album-grid .ph{aspect-ratio:auto;height:100%;cursor:pointer;border-radius:var(--ph-radius,6px)}
.album-grid .ph:nth-child(1){grid-column:span 2;grid-row:span 2}
.album-grid .ph:nth-child(4){grid-row:span 2}
.album-grid .ph:nth-child(5){grid-column:span 2}
.album-grid .ph.empty::before{font-size:1.8rem}
.album-grid .ph.empty::after{bottom:8px;font-size:.55rem}
@media(min-width:640px){.album-grid{grid-auto-rows:170px}}
.lightbox{position:fixed;inset:0;z-index:120;background:rgba(0,0,0,.88);display:grid;place-items:center;padding:20px}
.lightbox[hidden]{display:none}
.lightbox img{max-width:100%;max-height:86vh;border-radius:4px}
.lightbox button{position:absolute;top:14px;right:18px;background:none;border:0;color:#fff;font-size:2.4rem;cursor:pointer}
/* venue */
.venue-card{margin:34px auto 0;max-width:560px;background:var(--card);border:1px solid var(--line);border-radius:var(--radius,6px);overflow:hidden}
.map{height:190px;position:relative;--map-bg:var(--bg2);--map-road:var(--card-solid);--map-park:color-mix(in srgb,var(--gold) 22%,var(--bg2))}
.map svg,.map iframe{width:100%;height:100%;border:0;display:block}
.map .pin{animation:pin 2s ease-in-out infinite}
@keyframes pin{50%{transform:translate(172px,64px)}}
.venue-body{padding:24px 20px 26px}
.venue-body h3{font-family:var(--f-display);font-weight:400;font-size:1.45rem;color:var(--accent)}
/* bottom nav + music */
.bnav{position:fixed;left:50%;bottom:calc(12px + env(safe-area-inset-bottom,0px));transform:translate(-50%,30px);opacity:0;pointer-events:none;z-index:60;display:flex;gap:2px;padding:5px;border-radius:999px;background:var(--nav-bg,rgba(255,255,255,.82));backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);box-shadow:0 10px 30px -12px rgba(0,0,0,.35),0 0 0 1px var(--line);transition:.5s;max-width:calc(100vw - 20px);overflow-x:auto;scrollbar-width:none}
body.opened.navon .bnav{opacity:1;transform:translate(-50%,0);pointer-events:auto}
.bnav a{flex:none;padding:9px 11px;border-radius:999px;font-size:.6rem;letter-spacing:.14em;text-transform:uppercase;color:var(--nav-ink,var(--ink));text-decoration:none;font-family:var(--f-label,var(--f-body));transition:background .3s,color .3s}
.bnav a.on{background:var(--accent);color:var(--on-accent)}
.bnav a:focus-visible,.music:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.music{position:fixed;top:calc(14px + env(safe-area-inset-top,0px));right:14px;z-index:110;width:44px;height:44px;border-radius:50%;border:0;display:grid;place-items:center;cursor:pointer;background:var(--music-bg,rgba(255,255,255,.85));color:var(--accent);box-shadow:0 4px 14px rgba(0,0,0,.2)}
.music .m-on{display:none}.music[aria-pressed=true] .m-on{display:block}.music[aria-pressed=true] .m-off{display:none}
.music[aria-pressed=true]::after{content:"";position:absolute;inset:-4px;border-radius:50%;border:1px solid var(--gold);animation:ring 1.8s ease-out infinite}
@keyframes ring{from{transform:scale(.9);opacity:1}to{transform:scale(1.35);opacity:0}}
footer{padding-bottom:130px}
.fab{display:none}
"""

JS2 = r"""
(()=>{
const W=window.WEDDING,T=window.THEME||{};
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const mono=(W.partner1||' ')[0]+'&'+(W.partner2||' ')[0];
/* silk canvases */
const silks=$$('canvas[data-silk]');const paint=()=>silks.forEach(c=>{if(c.offsetParent!==null||c.closest('#opener'))drawSilk(c,JSON.parse(c.dataset.silk))});
paint();let rt;addEventListener('resize',()=>{clearTimeout(rt);rt=setTimeout(paint,250)});
/* photos */
const setPh=(el,url,label)=>{if(url){el.style.backgroundImage=`url("${url}")`;el.dataset.full=url;el.classList.remove('empty')}else{el.classList.add('empty');el.dataset.mono=mono;el.dataset.label=label}};
$$('[data-photo]').forEach(el=>setPh(el,W[el.dataset.photo],W.labels.photoCouple));
const ag=$('#album-grid');
if(ag){const ph=(W.photos&&W.photos.length)?W.photos:Array.from({length:W.albumSlots||6},()=>'');
 ag.innerHTML=ph.map(()=>'<button type="button" class="ph rv"></button>').join('');
 $$('.ph',ag).forEach((el,i)=>{setPh(el,ph[i],W.labels.photo+' '+(i+1));el.style.setProperty('--i',i%3)});
 if(!(W.photos&&W.photos.length)&&W.hideEmptyAlbum)$('#album').remove()}
const lb=$('#lightbox');
document.addEventListener('click',e=>{const p=e.target.closest('.album-grid .ph');if(p&&p.dataset.full){$('img',lb).src=p.dataset.full;lb.hidden=false}
 if(e.target===lb||e.target.closest('#lightbox button'))lb.hidden=true});
/* story */
const tl=$('#timeline');if(tl){if(W.story&&W.story.length)tl.innerHTML=W.story.map((s,i)=>`<li class="rv" style="--i:${i}"><p class="tl-date">${esc(s.date)}</p><h3 class="tl-title">${esc(s.title)}</h3><p class="tl-text">${esc(s.text)}</p></li>`).join('');else tl.remove()}
/* venue */
if(W.venue){const q=encodeURIComponent(W.venue.mapQuery||[W.venue.name,W.venue.address].join(', '));
 $('#venue-dir').href='https://www.google.com/maps/search/?api=1&query='+q;
 if(W.venue.embed)$('#map').innerHTML=`<iframe loading="lazy" title="Map" src="https://maps.google.com/maps?q=${q}&output=embed"></iframe>`}
else{const v=$('#venue');v&&v.remove()}
/* bottom nav + scrollspy */
const secs=[['home','navHome'],['story','navStory'],['events','navEvents'],['album','navAlbum'],['venue','navVenue'],['rsvp','navRsvp']].filter(([id])=>document.getElementById(id));
const nav=$('#bnav');nav.innerHTML=secs.map(([id,k])=>`<a href="#${id}" data-s="${id}">${esc(W.labels[k])}</a>`).join('');
const spy=new IntersectionObserver(es=>es.forEach(x=>{if(x.isIntersecting){$$('a',nav).forEach(a=>a.classList.toggle('on',a.dataset.s===x.target.id))}}),{rootMargin:'-45% 0px -50% 0px'});
secs.forEach(([id])=>spy.observe(document.getElementById(id)));
addEventListener('scroll',()=>document.body.classList.toggle('navon',scrollY>innerHeight*.35),{passive:true});
})();
"""


def page2(t):
    labels = dict(DEFAULT_LABELS)
    labels.update(PREMIUM_LABELS)
    labels.update(t["data"].pop("labels", {}))
    data = dict(t["data"])
    data["labels"] = labels
    data.setdefault("timezone", "Asia/Colombo")
    wedding_json = json.dumps(data, ensure_ascii=False, indent=2)
    theme_json = json.dumps(t.get("theme", {}), ensure_ascii=False)
    op = OPENERS2[t["opener"]]
    for k in ("COVERBG", "DECOR", "ICON", "COVERFG", "SEAL"):
        op = op.replace(f"%%{k}%%", t.get(k.lower(), ""))
    body = (BODY2.replace("%%HERO%%", t["hero"]).replace("%%DIVIDER%%", t["divider"]).replace("%%STORN%%", t["st_orn"])
            .replace("%%EVICON%%", t["ev_icon"]).replace("%%MAP%%", MAP_SVG).replace("%%FOOTART%%", t.get("footart", "")))
    js_extra = JS.replace("C={", "C={dateOrd:(()=>{const n=+fmt(D,{day:'numeric'}),s=(n%100>10&&n%100<14)?'th':({1:'st',2:'nd',3:'rd'}[n%10]||'th');return fmt(D,{weekday:'long'})+', '+n+s+' '+fmt(D,{month:'long',year:'numeric'})})(),"
                                  "dateOrdShort:(()=>{const n=+fmt(D,{day:'numeric'}),s=(n%100>10&&n%100<14)?'th':({1:'st',2:'nd',3:'rd'}[n%10]||'th');return n+s+' '+fmt(D,{month:'long',year:'numeric'})})(),"
                                  "guestOnly:guest?W.labels.dear+' '+guest:'',envTo:guest||W.labels.dearGuest,", 1)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{data["partner1"]} &amp; {data["partner2"]} — Wedding Invitation</title>
<meta name="description" content="You are invited to celebrate our wedding.">
<meta property="og:title" content="{data["partner1"]} &amp; {data["partner2"]} — Wedding Invitation">
<meta property="og:description" content="You are invited to celebrate our wedding. Tap to open your invitation.">
<meta property="og:type" content="website">
<meta name="theme-color" content="{t["theme_color"]}">
<!-- Template: {t["name"]} ({t["category"]}) — premium collection -->
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{t["fonts"]}&display=swap" rel="stylesheet">
<style>
:root{{{t["vars"]}}}
{BASE_CSS}
{PREMIUM_CSS}
/* ===== theme: {t["name"]} ===== */
{t["css"]}
</style>
</head>
<body class="t-{t["slug"]}">
<script>
/* =====================================================================
   WEDDING DETAILS — edit this block (or inject it from your platform).
   Personalise per guest: add ?to=Uncle%20Sunil%20%26%20Family to the link.
   Photos: set couplePhoto / heroImage to an image URL, and photos: [urls].
   Music: set music to an .mp3 URL, or leave "" for the built-in music (style set in THEME.music).
   rsvp.endpoint: POST JSON here ("" to disable). rsvp.whatsapp: number with
   country code for WhatsApp RSVPs ("" hides the button). Add ?open to skip the cover.
   ===================================================================== */
window.WEDDING = /*WEDDING*/{wedding_json}/*END*/;
window.THEME = /*THEME*/{theme_json}/*END*/;
/* Live preview from the Create page (same site): ?preview reads the draft from localStorage */
(function(){{try{{var q=new URLSearchParams(location.search);if(!q.has('preview'))return;var d=localStorage.getItem('mangala-preview');if(!d)return;
var o=JSON.parse(d),W=window.WEDDING;o.labels=Object.assign({{}},W.labels||{{}},o.labels||{{}});window.WEDDING=Object.assign({{}},W,o);
if(o.__music)window.THEME.music=Object.assign({{}},window.THEME.music||{{}},o.__music);}}catch(e){{}}}})();
</script>
{op}
<canvas id="fx" aria-hidden="true"></canvas>
{body}
<script>{SILK_JS}</script>
<script>{js_extra}</script>
<script>{JS2}</script>
<script>{MUSIC_JS}</script>
<script>{MUSIC_INIT}</script>
</body>
</html>
"""
