"""Shared page skeleton, base CSS, openers and JS runtime."""
import json, os
MUSIC_JS = open(os.path.join(os.path.dirname(__file__), "music.js")).read()
MUSIC_INIT = r"""(()=>{const W=window.WEDDING,T=window.THEME||{},b=document.getElementById('music');if(!b||!window.WeddingMusic)return;
 const M=Object.assign({style:'musicbox'},T.music||{});M.url=W.music||'';WeddingMusic.init(b,M);
 const op=document.getElementById('opener');if(op&&W.musicOnOpen!==false)op.addEventListener('click',()=>{if(!WeddingMusic.playing)WeddingMusic.play()},{once:true});})();"""

BASE_CSS = r"""
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{background:var(--bg);color:var(--ink);font-family:var(--f-body);font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased;overflow-x:hidden}
body.locked{overflow:hidden;height:100svh}
img,svg{display:block;max-width:100%}
#fx{position:fixed;inset:0;pointer-events:none;z-index:40}
main{position:relative;z-index:1;overflow:hidden}
.sec{position:relative;padding:84px 20px;text-align:center}
.inner{max-width:760px;margin:0 auto;position:relative}
.native{font-family:var(--f-native)}
.st{font-family:var(--f-display);font-weight:400;font-size:clamp(1.6rem,6vw,2.4rem);line-height:1.2;color:var(--accent);letter-spacing:.04em}
.st-orn{width:120px;height:auto;margin:0 auto 14px;display:block}
.kicker{font-size:.72rem;letter-spacing:.32em;text-transform:uppercase;color:var(--muted)}
.muted{color:var(--muted)}
.rv{opacity:0;transform:translateY(30px);transition:opacity 1.1s ease,transform 1.1s cubic-bezier(.2,.7,.2,1);transition-delay:calc(var(--i,0)*140ms)}
.rv.vis{opacity:1;transform:none}
/* hero */
.hero{min-height:100svh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:64px 20px;position:relative;overflow:hidden}
.h-in{opacity:0;transform:translateY(22px)}
body.opened .h-in{animation:hin 1.3s cubic-bezier(.2,.7,.2,1) forwards;animation-delay:calc(.25s + var(--d,0)*.22s)}
@keyframes hin{to{opacity:1;transform:none}}
.names{font-family:var(--f-script);font-weight:400;font-size:clamp(3rem,14vw,6.2rem);line-height:1.08;color:var(--accent)}
.names .amp{display:block;font-size:.5em;line-height:1.1;color:var(--gold)}
.shimmer{background:linear-gradient(100deg,var(--gold) 0%,var(--gold) 35%,var(--gold-hi) 50%,var(--gold) 65%,var(--gold) 100%);background-size:250% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:shim 5s linear infinite}
@keyframes shim{from{background-position:150% 0}to{background-position:-100% 0}}
.spin-slow{animation:spin 80s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.flame{transform-box:fill-box;transform-origin:50% 100%;animation:flick 1.1s ease-in-out infinite alternate}
.glow{animation:glowp 2.2s ease-in-out infinite alternate}
@keyframes flick{0%{transform:scale(1,1) skewX(0)}40%{transform:scale(.92,1.08) skewX(3deg)}100%{transform:scale(1.04,.94) skewX(-3deg)}}
@keyframes glowp{from{opacity:.3}to{opacity:.65}}
.divider{width:min(320px,80vw);height:auto;margin:22px auto}
/* couple */
.host{max-width:560px;margin:0 auto 34px;font-style:italic;color:var(--muted)}
.couple{display:grid;grid-template-columns:1fr auto 1fr;gap:18px;align-items:center;max-width:640px;margin:0 auto}
.couple h3{font-family:var(--f-display);font-weight:400;font-size:clamp(1.25rem,4.6vw,1.7rem);color:var(--accent);line-height:1.25;margin-bottom:6px}
.couple p{font-size:.88rem;color:var(--muted)}
.couple .and{font-family:var(--f-script);font-size:2.6rem;color:var(--gold)}
.invite-text{max-width:560px;margin:36px auto 0;font-size:1.06rem}
@media(max-width:520px){.couple{grid-template-columns:1fr}.couple .and{line-height:1}}
/* quote */
.quote blockquote{font-family:var(--f-display);font-size:clamp(1.15rem,4.4vw,1.55rem);line-height:1.55;max-width:600px;margin:0 auto;font-style:italic}
.quote cite{display:block;margin-top:16px;font-style:normal;font-size:.76rem;letter-spacing:.28em;text-transform:uppercase;color:var(--muted)}
/* countdown */
.cd{display:flex;justify-content:center;gap:clamp(8px,2.6vw,16px);margin-top:30px}
.cd-box{width:clamp(66px,20vw,104px);padding:16px 4px 12px;border:1px solid var(--line);background:var(--card);border-radius:var(--radius,4px)}
.cd-n{display:block;font-family:var(--f-display);font-size:clamp(1.7rem,7vw,2.5rem);line-height:1.1;color:var(--accent);font-variant-numeric:tabular-nums}
.cd-l{font-size:.62rem;letter-spacing:.22em;text-transform:uppercase;color:var(--muted)}
.cd-n.flip{animation:flip .55s ease}
@keyframes flip{0%{transform:rotateX(90deg);opacity:0}100%{transform:none;opacity:1}}
.cd-date{margin-top:22px;color:var(--muted);letter-spacing:.1em}
/* events */
.events-grid{display:grid;gap:22px;margin-top:36px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
.event{background:var(--card);border:1px solid var(--line);border-radius:var(--radius,4px);padding:34px 22px 28px;position:relative}
.ev-ico{width:54px;height:54px;margin:0 auto 12px}
.ev-ico svg{width:100%;height:100%}
.ev-name{font-family:var(--f-display);font-weight:400;font-size:1.45rem;color:var(--accent);line-height:1.25}
.ev-native{font-family:var(--f-native);color:var(--gold);font-size:1rem;margin-top:2px}
.ev-date{margin-top:14px;font-size:.92rem}
.ev-time{font-family:var(--f-display);font-size:1.12rem;color:var(--accent2,var(--accent));margin-top:2px}
.ev-venue{margin-top:12px;font-weight:600}
.ev-addr,.ev-note{font-size:.86rem;color:var(--muted)}
.ev-note{margin-top:8px;font-style:italic}
.ev-actions{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:20px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:42px;padding:10px 20px;border-radius:var(--btn-radius,999px);background:var(--accent);color:var(--on-accent,#fff);border:1px solid var(--accent);font:inherit;font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;cursor:pointer;text-decoration:none;transition:transform .2s,box-shadow .2s,background .2s}
.btn:hover{transform:translateY(-2px);box-shadow:0 8px 20px -8px var(--accent)}
.btn.ghost{background:transparent;color:var(--accent)}
.btn:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
/* dress */
.dress p{max-width:520px;margin:10px auto 0}
.swatches{display:flex;gap:10px;justify-content:center;margin-top:18px}
.swatches span{width:30px;height:30px;border-radius:50%;border:1px solid var(--line)}
/* rsvp */
.rsvp-card{max-width:560px;margin:34px auto 0;background:var(--card);border:1px solid var(--line);border-radius:var(--radius,4px);padding:32px 22px;text-align:left}
.field{margin-bottom:18px}
.field>label,.field>.lbl{display:block;font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;color:var(--muted);margin-bottom:8px}
.field input[type=text],.field select,.field textarea{width:100%;font:inherit;font-size:1rem;color:var(--ink);background:var(--input-bg,transparent);border:1px solid var(--line);border-radius:var(--in-radius,3px);padding:11px 13px}
.field textarea{min-height:88px;resize:vertical}
.seg{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.seg label,.chk{display:flex;align-items:center;gap:10px;border:1px solid var(--line);border-radius:var(--in-radius,3px);padding:11px 12px;cursor:pointer;font-size:.95rem}
.chks{display:grid;gap:8px}
.seg input,.chk input{accent-color:var(--accent);width:18px;height:18px;flex:none}
.rsvp-actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:6px}
.rsvp-actions .btn{flex:1 1 200px}
.thanks{text-align:center;padding:20px 0}
.thanks .t-big{font-family:var(--f-script);font-size:2.8rem;color:var(--accent);line-height:1.1}
form.sent{display:none}
.deadline{margin-top:10px;color:var(--muted)}
/* footer */
footer{padding:70px 20px 110px;text-align:center}
.f-names{font-family:var(--f-script);font-size:clamp(2.2rem,9vw,3.4rem);color:var(--accent);line-height:1.1}
.f-tag{margin-top:10px;letter-spacing:.2em;color:var(--gold)}
.f-bless{margin-top:14px;font-family:var(--f-native);color:var(--muted)}
.brand{margin-top:34px;font-size:.66rem;letter-spacing:.24em;text-transform:uppercase;color:var(--muted);opacity:.7}
/* floating RSVP */
.fab{position:fixed;right:16px;bottom:16px;z-index:30;opacity:0;transform:translateY(20px);pointer-events:none;transition:.5s;box-shadow:0 10px 30px -10px rgba(0,0,0,.4)}
body.opened.scrolled .fab{opacity:1;transform:none;pointer-events:auto}
/* openers */
#opener{position:fixed;inset:0;z-index:100;cursor:pointer;overflow:hidden;transition:opacity .9s ease,visibility .9s}
#opener.gone{opacity:0;visibility:hidden}
.op-center{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:24px;z-index:5;transition:opacity .5s,transform .6s}
#opener.opening .op-center{opacity:0;transform:scale(.92)}
.op-guest{font-family:var(--f-display);font-size:clamp(1.1rem,4.6vw,1.5rem);color:var(--op-ink);margin-top:22px;max-width:320px;line-height:1.35}
.op-tap{margin-top:14px;font-size:.66rem;letter-spacing:.34em;text-transform:uppercase;color:var(--op-ink);opacity:.8;animation:pulse 2s ease-in-out infinite}
@keyframes pulse{50%{opacity:.35}}
.op-seal{width:96px;height:96px;border-radius:50%;display:grid;place-items:center;background:radial-gradient(circle at 35% 30%,var(--seal-hi),var(--seal) 60%,var(--seal-lo));box-shadow:0 6px 18px rgba(0,0,0,.35),inset 0 0 0 5px rgba(255,255,255,.08),inset 0 0 0 7px rgba(0,0,0,.12);color:var(--seal-ink);font-family:var(--f-display);font-size:1.9rem;letter-spacing:.06em;animation:sealb 2.4s ease-in-out infinite}
@keyframes sealb{50%{transform:scale(1.05)}}
/* doors */
.op-doors{perspective:1800px;background:var(--op-back,#000)}
.op-doors .door{position:absolute;top:0;bottom:0;width:50%;background:var(--op-bg);transition:transform 1.7s cubic-bezier(.7,0,.25,1);overflow:hidden;box-shadow:inset 0 0 60px rgba(0,0,0,.35)}
.op-doors .door.l{left:0;transform-origin:left center;border-right:1px solid var(--op-line)}
.op-doors .door.r{right:0;transform-origin:right center;border-left:1px solid var(--op-line)}
.op-doors.opening .door.l{transform:rotateY(-105deg)}
.op-doors.opening .door.r{transform:rotateY(105deg)}
.door-in{position:absolute;inset:18px;border:1px solid var(--op-line);display:flex;align-items:center;justify-content:center}
.door.r .door-in{transform:scaleX(-1)}
/* curtain */
.op-curtain{background:var(--op-back,#000)}
.op-curtain .cur{position:absolute;top:0;bottom:0;width:52%;background:var(--cur);transition:transform 1.8s cubic-bezier(.7,0,.25,1);z-index:2}
.op-curtain .cur.l{left:0;transform-origin:left top}
.op-curtain .cur.r{right:0;transform-origin:right top}
.op-curtain.opening .cur.l{transform:translateX(-96%) scaleX(.6)}
.op-curtain.opening .cur.r{transform:translateX(96%) scaleX(.6)}
.op-curtain .valance{position:absolute;left:0;right:0;top:0;height:74px;z-index:3;background:var(--valance);transition:transform 1.4s .4s}
.op-curtain.opening .valance{transform:translateY(-100%)}
/* envelope */
.op-env{background:var(--op-bg)}
.env{position:relative;width:min(84vw,380px);aspect-ratio:1.42;perspective:1200px}
.env>*{position:absolute}
.env-back{inset:0;background:var(--env-back);border-radius:6px}
.env-card{left:6%;right:6%;top:6%;bottom:8%;background:var(--card-solid,#fff);border-radius:4px;z-index:2;display:grid;place-items:center;text-align:center;padding:10px;transition:transform 1.1s .75s cubic-bezier(.3,.8,.3,1)}
.env-card .names{font-size:clamp(1.6rem,7vw,2.4rem)}
.env-front{inset:0;z-index:3;background:var(--env-front);clip-path:polygon(0 0,50% 56%,100% 0,100% 100%,0 100%);border-radius:6px}
.env-flap{left:0;right:0;top:0;height:62%;z-index:4;background:var(--env-flap);clip-path:polygon(0 0,100% 0,50% 100%);transform-origin:top center;transition:transform .8s ease,z-index 0s .4s;border-radius:6px 6px 0 0}
.env .op-seal{left:50%;top:58%;transform:translate(-50%,-50%);z-index:5;transition:opacity .4s,transform .4s;width:78px;height:78px;font-size:1.5rem;animation:none}
.op-env.opening .op-seal{opacity:0;transform:translate(-50%,-50%) scale(1.4)}
.op-env.opening .env-flap{transform:rotateX(180deg);z-index:1}
.op-env.opening .env-card{transform:translateY(-58%)}
.op-env .op-center{position:relative;inset:auto;height:100%;transition:none}
.op-env.opening .op-center{opacity:1;transform:none}
.op-env.opening .op-guest,.op-env.opening .op-tap{opacity:0;transition:opacity .4s}
/* minimal */
.op-min{background:var(--op-bg);transition:transform 1.2s cubic-bezier(.7,0,.25,1),opacity .9s,visibility .9s}
.op-min.opening{transform:translateY(-100%)}
.op-min .mono{font-family:var(--f-display);font-size:clamp(4rem,22vw,8rem);color:var(--op-ink);line-height:1;letter-spacing:.04em}
.op-min .line{display:block;width:0;height:1px;background:var(--op-ink);margin:22px auto 0;animation:grow 1.6s .3s forwards}
@keyframes grow{to{width:140px}}

.music{position:fixed;top:calc(14px + env(safe-area-inset-top,0px));right:14px;z-index:110;width:44px;height:44px;border-radius:50%;border:0;display:grid;place-items:center;cursor:pointer;background:var(--music-bg,rgba(255,255,255,.85));color:var(--accent);box-shadow:0 4px 14px rgba(0,0,0,.2)}
.music .m-on{display:none}.music[aria-pressed=true] .m-on{display:block}.music[aria-pressed=true] .m-off{display:none}
.music[aria-pressed=true]::after{content:"";position:absolute;inset:-4px;border-radius:50%;border:1px solid var(--gold);animation:ring 1.8s ease-out infinite}
@keyframes ring{from{transform:scale(.9);opacity:1}to{transform:scale(1.35);opacity:0}}
.music:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}.rv,.h-in{opacity:1!important;transform:none!important}}
"""

OPENERS = {
    "doors": """<div id="opener" class="op-doors" role="button" tabindex="0" aria-label="Open the invitation">
<div class="door l"><div class="door-in">%%DECOR%%</div></div><div class="door r"><div class="door-in">%%DECOR%%</div></div>
<div class="op-center"><div class="op-seal"><span data-f="c.initials"></span></div><p class="op-guest" data-f="c.guestLine"></p><p class="op-tap" data-f="labels.tap"></p></div></div>""",
    "curtain": """<div id="opener" class="op-curtain" role="button" tabindex="0" aria-label="Open the invitation">
<div class="cur l"></div><div class="cur r"></div><div class="valance"></div>
<div class="op-center">%%DECOR%%<div class="op-seal"><span data-f="c.initials"></span></div><p class="op-guest" data-f="c.guestLine"></p><p class="op-tap" data-f="labels.tap"></p></div></div>""",
    "envelope": """<div id="opener" class="op-env" role="button" tabindex="0" aria-label="Open the invitation">
<div class="op-center"><div class="env"><div class="env-back"></div><div class="env-card"><div>%%DECOR%%<p class="names"><span data-f="partner1"></span> &amp; <span data-f="partner2"></span></p></div></div>
<div class="env-front"></div><div class="env-flap"></div><div class="op-seal"><span data-f="c.initials"></span></div></div>
<p class="op-guest" data-f="c.guestLine"></p><p class="op-tap" data-f="labels.tap"></p></div></div>""",
    "minimal": """<div id="opener" class="op-min" role="button" tabindex="0" aria-label="Open the invitation">
<div class="op-center">%%DECOR%%<p class="op-guest" data-f="c.guestLine"></p><h2 class="mono" data-f="c.monogram"></h2><span class="line"></span><p class="op-tap" data-f="labels.tap"></p></div></div>""",
}

BODY = """
<main>
<section class="hero">%%HERO%%</section>

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

<section class="sec quote"><div class="inner rv">
  %%STORN%%
  <blockquote data-f="quote" data-opt="sec"></blockquote><cite data-f="quoteSource" data-opt></cite>
</div></section>

<section class="sec countdown-sec"><div class="inner">
  %%STORN%%<h2 class="st rv" data-f="labels.countdown"></h2>
  <div class="cd rv" id="countdown"></div>
  <p class="cd-date rv" data-f="c.dateLong"></p>
</div></section>

<section class="sec events-sec" id="events-sec"><div class="inner">
  %%STORN%%<h2 class="st rv" data-f="labels.events"></h2>
  <div class="events-grid" id="events"></div>
</div></section>

<section class="sec dress"><div class="inner rv">
  %%STORN%%<h2 class="st" data-f="labels.dress"></h2>
  <p data-f="dressCode" data-opt="sec"></p><div class="swatches" id="swatches"></div>
</div></section>

<section class="sec rsvp-sec" id="rsvp"><div class="inner">
  %%STORN%%<h2 class="st rv" data-f="labels.rsvp"></h2>
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
</main>
<a class="btn fab" href="#rsvp" data-f="labels.rsvpShort"></a>
<button class="music" id="music" type="button" aria-pressed="false">
<svg class="m-on" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M4 9h4l5-4v14l-5-4H4z" fill="currentColor"/><path d="M16 8.5a5 5 0 010 7M18.5 6a8.5 8.5 0 010 12" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
<svg class="m-off" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M4 9h4l5-4v14l-5-4H4z" fill="currentColor"/><path d="M16.5 9.5l5 5M21.5 9.5l-5 5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
<span class="sr" data-f="labels.music"></span></button>
<template id="ev-ico">%%EVICON%%</template>
"""

JS = r"""
(()=>{
const W=window.WEDDING,T=window.THEME||{};
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const tz=W.timezone||'Asia/Colombo',loc=W.locale||'en-GB';
const get=(o,p)=>p.split('.').reduce((a,k)=>a==null?a:a[k],o);
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const fmt=(dt,o)=>new Intl.DateTimeFormat(loc,{timeZone:tz,...o}).format(dt);
const Q=new URLSearchParams(location.search),guest=(Q.get('to')||'').trim();
const D=new Date(W.date);
const C={
 dateLong:fmt(D,{weekday:'long',day:'numeric',month:'long',year:'numeric'}),
 dateShort:fmt(D,{day:'numeric',month:'long',year:'numeric'}),
 day:fmt(D,{day:'2-digit'}),month:fmt(D,{month:'long'}),monthShort:fmt(D,{month:'short'}),monthNum:fmt(D,{month:'2-digit'}),
 year:fmt(D,{year:'numeric'}),weekday:fmt(D,{weekday:'long'}),
 dateDots:fmt(D,{day:'2-digit'})+' . '+fmt(D,{month:'2-digit'})+' . '+fmt(D,{year:'numeric'}),
 time:fmt(D,{hour:'numeric',minute:'2-digit',hour12:true}),
 initials:(W.partner1||' ')[0]+(W.partner2||' ')[0],
 monogram:(W.partner1||' ')[0]+' & '+(W.partner2||' ')[0],
 guestLine:guest?(W.labels.dear+' '+guest):W.labels.invited,
 deadlineLine:W.rsvp&&W.rsvp.deadline?W.labels.kindly+' '+fmt(new Date(W.rsvp.deadline+'T12:00:00'),{day:'numeric',month:'long',year:'numeric'}):''
};
const val=k=>k.startsWith('c.')?C[k.slice(2)]:get(W,k);
$$('[data-f]').forEach(el=>{const v=val(el.dataset.f);
 if(v==null||v===''){if(el.hasAttribute('data-opt')){(el.dataset.opt==='sec'?el.closest('section'):el).remove()}return}
 el.textContent=v});
document.title=W.partner1+' & '+W.partner2+' — '+(W.labels.titleSuffix||'Wedding Invitation');

/* events */
const ico=$('#ev-ico')?$('#ev-ico').innerHTML:'';
const evEl=$('#events');
if(evEl)evEl.innerHTML=(W.events||[]).map((e,i)=>{const t=new Date(e.time);
 const q=encodeURIComponent(e.mapQuery||[e.venue,e.address].filter(Boolean).join(', '));
 return `<article class="event rv" style="--i:${i}"><div class="ev-ico">${ico}</div>
 <h3 class="ev-name">${esc(e.name)}</h3>${e.native?`<p class="ev-native">${esc(e.native)}</p>`:''}
 <p class="ev-date">${fmt(t,{weekday:'long',day:'numeric',month:'long',year:'numeric'})}</p>
 <p class="ev-time">${esc(e.timeLabel||fmt(t,{hour:'numeric',minute:'2-digit',hour12:true}))}</p>
 <p class="ev-venue">${esc(e.venue)}</p>${e.address?`<p class="ev-addr">${esc(e.address)}</p>`:''}
 ${e.note?`<p class="ev-note">${esc(e.note)}</p>`:''}
 <div class="ev-actions"><a class="btn" target="_blank" rel="noopener" href="https://www.google.com/maps/search/?api=1&query=${q}">${esc(W.labels.map)}</a>
 <button class="btn ghost" type="button" data-ics="${i}">${esc(W.labels.calendar)}</button></div></article>`}).join('');

/* add to calendar (.ics) */
const icsT=d=>d.toISOString().replace(/[-:]/g,'').replace(/\.\d{3}/,'');
const icsE=s=>String(s).replace(/([,;\\])/g,'\\$1');
document.addEventListener('click',ev=>{const b=ev.target.closest('[data-ics]');if(!b)return;
 const x=W.events[+b.dataset.ics],s=new Date(x.time),en=x.end?new Date(x.end):new Date(s.getTime()+4*36e5);
 const ics=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Wedding Invite//EN','BEGIN:VEVENT','UID:'+s.getTime()+'-'+b.dataset.ics+'@invite',
 'DTSTAMP:'+icsT(new Date()),'DTSTART:'+icsT(s),'DTEND:'+icsT(en),'SUMMARY:'+icsE(W.partner1+' & '+W.partner2+' — '+x.name),
 'LOCATION:'+icsE([x.venue,x.address].filter(Boolean).join(', ')),'END:VEVENT','END:VCALENDAR'].join('\r\n');
 const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([ics],{type:'text/calendar'}));
 a.download=(W.partner1+'-'+W.partner2+'-'+x.name).toLowerCase().replace(/[^a-z0-9]+/g,'-')+'.ics';document.body.appendChild(a);a.click();a.remove()});

/* countdown */
const cd=$('#countdown');
if(cd){cd.innerHTML=['days','hours','minutes','seconds'].map(u=>`<div class="cd-box"><span class="cd-n" data-u="${u}">00</span><span class="cd-l">${esc(W.labels[u])}</span></div>`).join('');
 const tick=()=>{const ms=Math.max(0,D-new Date());const v={days:Math.floor(ms/864e5),hours:Math.floor(ms/36e5)%24,minutes:Math.floor(ms/6e4)%60,seconds:Math.floor(ms/1e3)%60};
  for(const u in v){const el=$(`[data-u="${u}"]`,cd),s=String(v[u]).padStart(2,'0');if(el.textContent!==s){el.textContent=s;el.classList.remove('flip');void el.offsetWidth;el.classList.add('flip')}}};
 tick();setInterval(tick,1000)}

/* dress-code swatches */
const sw=$('#swatches');if(sw&&W.dressColors)sw.innerHTML=W.dressColors.map(c=>`<span style="background:${esc(c)}"></span>`).join('');

/* RSVP */
const F=$('#rsvp-form');
if(F){const E=F.elements;if(guest)E.gname.value=guest;
 for(let i=1;i<=(W.rsvp.maxGuests||6);i++)E.guests.add(new Option(i,i));
 const re=$('#rsvp-events');if((W.events||[]).length>1)re.innerHTML=W.events.map(e=>`<label class="chk"><input type="checkbox" name="ev" value="${esc(e.name)}" checked><span>${esc(e.name)}</span></label>`).join('');else $('#ev-field').remove();
 const sync=()=>{const no=E.attending.value==='no';['#guests-field','#ev-field'].forEach(s=>{const x=$(s);if(x)x.style.display=no?'none':''})};
 F.addEventListener('change',sync);
 const data=()=>({name:E.gname.value.trim(),attending:E.attending.value,guests:E.attending.value==='yes'?+E.guests.value:0,
  events:E.attending.value==='yes'?$$('input[name=ev]:checked',F).map(x=>x.value):[],message:E.message.value.trim()});
 const ok=()=>{if(!E.gname.value.trim()){E.gname.focus();E.gname.setAttribute('aria-invalid','true');return false}E.gname.removeAttribute('aria-invalid');return true};
 const done=p=>{F.classList.add('sent');$('#rsvp-thanks').hidden=false;$('#rsvp-thanks .t-msg').textContent=p.attending==='yes'?W.labels.thanksYes:W.labels.thanksNo};
 F.addEventListener('submit',async e=>{e.preventDefault();if(!ok())return;const p=data();
  if(W.rsvp.endpoint){try{await fetch(W.rsvp.endpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({...p,invite:W.slug||'',couple:W.partner1+' & '+W.partner2})})}catch(_){}}
  done(p)});
 const wa=$('#rsvp-wa');
 if(!W.rsvp.whatsapp)wa.remove();else wa.addEventListener('click',()=>{if(!ok())return;const p=data();
  const t=[`RSVP — ${W.partner1} & ${W.partner2}`,`Name: ${p.name}`,p.attending==='yes'?`Attending: Yes (${p.guests} guest${p.guests>1?'s':''})`:'Attending: Sorry, can\'t make it',
   p.events.length?`Events: ${p.events.join(', ')}`:'',p.message?`Message: ${p.message}`:''].filter(Boolean).join('\n');
  window.open('https://wa.me/'+String(W.rsvp.whatsapp).replace(/\D/g,'')+'?text='+encodeURIComponent(t),'_blank','noopener');done(p)})}

/* reveal on scroll */
const io=new IntersectionObserver(es=>es.forEach(x=>{if(x.isIntersecting){x.target.classList.add('vis');io.unobserve(x.target)}}),{threshold:.12,rootMargin:'0px 0px -40px 0px'});
$$('.rv').forEach(el=>io.observe(el));
addEventListener('scroll',()=>document.body.classList.toggle('scrolled',scrollY>innerHeight*.8),{passive:true});

/* particles */
let fxOn=false;
function fx(){const P=T.particles;if(fxOn||!P||matchMedia('(prefers-reduced-motion: reduce)').matches)return;fxOn=true;
 const c=$('#fx'),x=c.getContext('2d');let w,h;const dpr=Math.min(2,devicePixelRatio||1);
 const rs=()=>{w=c.width=innerWidth*dpr;h=c.height=innerHeight*dpr};rs();addEventListener('resize',rs);
 const R=(a,b)=>a+Math.random()*(b-a),dir=P.dir||1;
 const mk=init=>({x:R(0,w),y:init?R(0,h):(dir>0?R(-60,-20)*dpr:h+R(20,60)*dpr),s:R(P.size[0],P.size[1])*dpr,
  vy:(P.mode==='twinkle'?R(.02,.08):R(.35,1))*(P.speed||1)*dpr,vx:R(-.25,.25)*dpr,r:R(0,6.28),vr:R(-.02,.02),sw:R(0,6.28),
  c:P.colors[Math.floor(Math.random()*P.colors.length)],a:R(.55,1),tw:R(0,6.28)});
 const n=Math.round(P.count*(innerWidth<600?.6:1)),ps=Array.from({length:n},()=>mk(true));
 const TAU=Math.PI*2,S={
  petal(p){const s=p.s;x.beginPath();x.moveTo(0,-s);x.bezierCurveTo(s*.85,-s*.5,s*.6,s*.7,0,s);x.bezierCurveTo(-s*.6,s*.7,-s*.85,-s*.5,0,-s);x.fill()},
  flower(p){const s=p.s;for(let i=0;i<5;i++){x.save();x.rotate(i*TAU/5);x.beginPath();x.ellipse(0,-s*.5,s*.3,s*.5,0,0,TAU);x.fill();x.restore()}x.fillStyle=P.center||'#f2b705';x.beginPath();x.arc(0,0,s*.16,0,TAU);x.fill()},
  sparkle(p){const s=p.s;x.beginPath();for(let i=0;i<8;i++){const rr=i%2?s*.16:s,a=i*Math.PI/4;x.lineTo(Math.cos(a)*rr,Math.sin(a)*rr)}x.closePath();x.fill()},
  dot(p){x.beginPath();x.arc(0,0,p.s*.3,0,TAU);x.fill()},
  leaf(p){const s=p.s;x.beginPath();x.moveTo(0,-s);x.quadraticCurveTo(s*.75,0,0,s);x.quadraticCurveTo(-s*.75,0,0,-s);x.fill();x.strokeStyle='rgba(255,255,255,.35)';x.lineWidth=dpr*.7;x.beginPath();x.moveTo(0,-s);x.lineTo(0,s);x.stroke()},
  bubble(p){x.lineWidth=dpr;x.strokeStyle=p.c;x.beginPath();x.arc(0,0,p.s*.5,0,TAU);x.stroke();x.beginPath();x.arc(-p.s*.18,-p.s*.18,p.s*.1,0,TAU);x.fill()},
  glitter(p){x.fillRect(-p.s*.35,-p.s*.35,p.s*.7,p.s*.7)},
  marigold(p){const s=p.s;for(let i=0;i<10;i++){x.save();x.rotate(i*TAU/10);x.beginPath();x.ellipse(0,-s*.42,s*.2,s*.42,0,0,TAU);x.fill();x.restore()}x.fillStyle='rgba(150,60,0,.55)';x.beginPath();x.arc(0,0,s*.16,0,TAU);x.fill()}
 };
 const loop=t=>{x.clearRect(0,0,w,h);
  for(const p of ps){p.sw+=.012;p.y+=p.vy*dir;p.x+=p.vx+Math.sin(p.sw)*.35*dpr;p.r+=p.vr;
   if((dir>0&&p.y>h+60*dpr)||(dir<0&&p.y<-60*dpr)||p.x<-80*dpr||p.x>w+80*dpr)Object.assign(p,mk(false));
   x.save();x.translate(p.x,p.y);x.rotate(p.r);if(P.flip)x.scale(1,Math.cos(p.sw*3+p.tw));
   let al=p.a*(P.alpha||1);if(P.mode==='twinkle')al*=.25+.75*Math.abs(Math.sin(t/900+p.tw));
   if(dir<0)al*=Math.min(1,p.y/(h*.35));x.globalAlpha=Math.max(0,al);x.fillStyle=p.c;
   if(P.glow){x.shadowBlur=P.glow*dpr;x.shadowColor=p.c}S[P.type](p);x.restore()}
  requestAnimationFrame(loop)};requestAnimationFrame(loop)}

/* opener */
const op=$('#opener');
const reveal=()=>{document.body.classList.remove('locked');document.body.classList.add('opened');fx()};
if(!op||Q.has('open')){op&&op.remove();reveal()}
else{document.body.classList.add('locked');
 const open=()=>{if(op.classList.contains('opening'))return;op.classList.add('opening');
  setTimeout(()=>{op.classList.add('gone');reveal()},T.openMs||1700);setTimeout(()=>op.remove(),(T.openMs||1700)+1000)};
 op.addEventListener('click',open);op.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();open()}});
 setTimeout(()=>op.focus({preventScroll:true}),50)}
})();
"""

DEFAULT_LABELS = {
    "tap": "Tap to open",
    "dear": "Dear",
    "invited": "You are cordially invited",
    "countdown": "Counting down to the day",
    "events": "Wedding Celebrations",
    "dress": "Dress Code",
    "rsvp": "Kindly Respond",
    "rsvpShort": "RSVP",
    "kindly": "Kindly respond by",
    "yourName": "Your name",
    "attending": "Will you attend?",
    "accept": "Joyfully accept",
    "decline": "Regretfully decline",
    "guests": "Number of guests",
    "which": "Attending",
    "message": "A note for the couple (optional)",
    "send": "Send RSVP",
    "whatsapp": "RSVP on WhatsApp",
    "thanks": "Thank you",
    "thanksYes": "We can't wait to celebrate with you.",
    "thanksNo": "You will be missed. Thank you for letting us know.",
    "map": "Directions",
    "calendar": "Add to calendar",
    "days": "Days", "hours": "Hours", "minutes": "Minutes", "seconds": "Seconds",
    "titleSuffix": "Wedding Invitation",
    "music": "Music",
}


def page(t):
    labels = dict(DEFAULT_LABELS)
    labels.update(t["data"].pop("labels", {}))
    data = dict(t["data"])
    data["labels"] = labels
    data.setdefault("timezone", "Asia/Colombo")
    data.setdefault("brand", "")
    wedding_json = json.dumps(data, ensure_ascii=False, indent=2)
    theme_json = json.dumps(t.get("theme", {}), ensure_ascii=False)
    opener = OPENERS[t["opener"]].replace("%%DECOR%%", t.get("opener_decor", ""))
    body = (BODY.replace("%%HERO%%", t["hero"])
            .replace("%%DIVIDER%%", t["divider"])
            .replace("%%STORN%%", t["st_orn"])
            .replace("%%EVICON%%", t["ev_icon"]))
    og_title = f'{data["partner1"]} &amp; {data["partner2"]} — Wedding Invitation'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{data["partner1"]} &amp; {data["partner2"]} — Wedding Invitation</title>
<meta name="description" content="You are invited to celebrate our wedding.">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="You are invited to celebrate our wedding. Tap to open your invitation.">
<meta property="og:type" content="website">
<meta name="theme-color" content="{t["theme_color"]}">
<!-- Template: {t["name"]} ({t["category"]}) -->
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{t["fonts"]}&display=swap" rel="stylesheet">
<style>
:root{{{t["vars"]}}}
{BASE_CSS}
/* ===== theme: {t["name"]} ===== */
{t["css"]}
</style>
</head>
<body class="t-{t["slug"]}">
<script>
/* =====================================================================
   WEDDING DETAILS — edit this block (or inject it from your platform).
   Personalise per guest by adding ?to=Uncle%20Sunil%20%26%20Family to the link.
   Add ?open to skip the opening animation. music: .mp3 URL, or "" for the built-in music.
   rsvp.endpoint: POST JSON here (leave "" to disable). rsvp.whatsapp: number
   with country code for WhatsApp RSVPs (leave "" to hide the button).
   ===================================================================== */
window.WEDDING = /*WEDDING*/{wedding_json}/*END*/;
window.THEME = /*THEME*/{theme_json}/*END*/;
/* Live preview from the Create page (same site): ?preview reads the draft from localStorage */
(function(){{try{{var q=new URLSearchParams(location.search);if(!q.has('preview'))return;var d=localStorage.getItem('mangala-preview');if(!d)return;
var o=JSON.parse(d),W=window.WEDDING;o.labels=Object.assign({{}},W.labels||{{}},o.labels||{{}});window.WEDDING=Object.assign({{}},W,o);
if(o.__music)window.THEME.music=Object.assign({{}},window.THEME.music||{{}},o.__music);}}catch(e){{}}}})();
</script>
{opener}
<canvas id="fx" aria-hidden="true"></canvas>
{body}
<script>{JS}</script>
<script>{MUSIC_JS}</script>
<script>{MUSIC_INIT}</script>
</body>
</html>
"""
