/* Create / edit an invitation: form ⇄ state, live preview, photo & music upload, publish or download. */
(() => {
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const Q = new URLSearchParams(location.search);
  const EDIT = { id: Q.get('id'), key: Q.get('key') };
  const TZ = '+05:30';
  const get = (o, p) => p.split('.').reduce((a, k) => a == null ? a : a[k], o);
  const put = (o, p, v) => { const ks = p.split('.'); let x = o; ks.slice(0, -1).forEach(k => { if (typeof x[k] !== 'object' || x[k] === null) x[k] = {}; x = x[k]; }); x[ks.at(-1)] = v; };
  const clone = o => JSON.parse(JSON.stringify(o));
  const toLocal = iso => { if (!iso) return ''; const m = /^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2})/.exec(iso); return m ? m[1] : ''; };
  const fromLocal = v => v ? `${v}:00${TZ}` : '';

  let TPL = [], tpl = null, defaults = {}, theme = {}, state = {}, touched = new Set(), media = {};
  const MUSIC = [
    ['', 'Design default'], ['magulbera', 'Sinhala magul bera (drums & horanewa)'], ['magulflute', 'Sinhala soft flute & drums'],
    ['mangala', 'Tamil mangala vadyam (nadaswaram & thavil)'], ['daf', 'Daf frame drum (no melody)'], ['organ', 'Church organ (Canon in D)'], ['musicbox', 'Music box / soft piano'],
  ];

  const SECTIONS = [
    { id: 'couple', title: 'The couple', open: true, fields: [
      ['partner1', 'First name', 'text', { req: 1, half: 1 }], ['partner2', 'Partner’s first name', 'text', { req: 1, half: 1 }],
      ['fullName1', 'Full name', 'text', { half: 1 }], ['fullName2', 'Partner’s full name', 'text', { half: 1 }],
      ['parents1', 'Parents line', 'text', { hint: 'e.g. Son of Mr. & Mrs. Sunil Perera, Kandy' }], ['parents2', 'Partner’s parents line'] ] },
    { id: 'date', title: 'Date & wording', fields: [
      ['date', 'Main date and time', 'datetime', { req: 1, half: 1, hint: 'The countdown runs to this moment (Sri Lanka time).' }], ['venueLine', 'Venue (short)', 'text', { half: 1, hint: 'Shown under your names' }],
      ['nativeGreeting', 'Greeting in Sinhala, Tamil or Arabic', 'text', { hint: 'e.g. ආයුබෝවන් · திருமண அழைப்பிதழ் · بِسْمِ ٱللَّٰهِ' }], ['greeting', 'Greeting in English', 'text'],
      ['tagline', 'Line above your names'], ['hostLine', 'Invitation from the families', 'textarea'], ['inviteText', 'A few words to your guests', 'textarea'],
      ['quote', 'Quote or verse', 'textarea'], ['quoteSource', 'Quote source', 'text', { half: 1 }], ['hashtag', 'Wedding hashtag', 'text', { half: 1 }], ['blessing', 'Closing blessing'] ] },
    { id: 'events', title: 'Events', custom: 'events' },
    { id: 'story', title: 'Our story', premium: 1, custom: 'story' },
    { id: 'venue', title: 'Venue & map', premium: 1, fields: [['venue.name', 'Venue name'], ['venue.address', 'Address'], ['venue.note', 'Note for guests', 'text', { hint: 'Parking, entrance, dress reminders' }]] },
    { id: 'photos', title: 'Photos', premium: 1, custom: 'photos' },
    { id: 'music', title: 'Music', custom: 'music' },
    { id: 'rsvp', title: 'RSVP & dress code', fields: [
      ['rsvp.whatsapp', 'WhatsApp number for RSVPs', 'tel', { hint: 'Country code first, e.g. 94771234567. Leave empty to hide the WhatsApp button.' }],
      ['rsvp.deadline', 'Reply by', 'date', { half: 1 }], ['rsvp.maxGuests', 'Most guests per reply', 'number', { half: 1 }], ['dressCode', 'Dress code', 'textarea'] ] },
    { id: 'labels', title: 'Section headings', fields: [['labels.countdown', 'Countdown heading'], ['labels.events', 'Events heading'], ['labels.rsvp', 'RSVP heading'], ['labels.tap', 'Opening prompt']] },
  ];

  /* ---------- form rendering ---------- */
  function fieldHtml([k, label, type = 'text', o = {}]) {
    const id = 'f-' + k.replace(/\./g, '-');
    const req = o.req ? ' required' : '';
    let input;
    if (type === 'textarea') input = `<textarea id="${id}" data-k="${k}"${req}></textarea>`;
    else if (type === 'datetime') input = `<input type="datetime-local" id="${id}" data-k="${k}" data-t="dt"${req}>`;
    else input = `<input type="${type === 'tel' ? 'tel' : type === 'date' ? 'date' : type === 'number' ? 'number' : 'text'}" id="${id}" data-k="${k}"${type === 'number' ? ' min="1" max="20" data-t="num"' : ''}${req}>`;
    return `<div class="field${o.half ? ' half' : ''}"><label for="${id}">${esc(label)}${o.req ? ' *' : ''}</label>${input}${o.hint ? `<span class="hint">${esc(o.hint)}</span>` : ''}</div>`;
  }
  function renderForm() {
    $('#sections').innerHTML = SECTIONS.map((s, i) => `<details class="ed-sec" id="sec-${s.id}"${s.open ? ' open' : ''}>
      <summary><span class="n">${i + 2}</span>${esc(s.title)}${s.premium ? '<span class="tag-prem">PREMIUM</span>' : ''}</summary>
      <div class="ed-body">${s.premium ? '<p class="notice prem-note" hidden>This section appears in premium designs. Pick a premium design above to use it.</p>' : ''}
      ${s.fields ? `<div class="fgrid">${s.fields.map(fieldHtml).join('')}</div>` : `<div id="custom-${s.custom}"></div>`}</div></details>`).join('');
  }

  function fillForm() {
    $$('[data-k]').forEach(el => {
      const v = get(state, el.dataset.k);
      el.value = el.dataset.t === 'dt' ? toLocal(v) : (v ?? '');
    });
    renderEvents(); renderStory(); renderPhotos(); renderMusic();
    const prem = !!tpl.premium;
    $$('.prem-note').forEach(n => n.hidden = prem);
    ['story', 'venue', 'photos'].forEach(id => $$(`#sec-${id} input, #sec-${id} textarea, #sec-${id} button`).forEach(x => x.disabled = !prem));
  }

  document.addEventListener('input', e => {
    const el = e.target.closest('[data-k]'); if (!el) return;
    let v = el.value;
    if (el.dataset.t === 'dt') v = fromLocal(v);
    if (el.dataset.t === 'num') v = Math.max(1, Math.min(20, parseInt(v, 10) || 1));
    put(state, el.dataset.k, v); touched.add(el.dataset.k);
    if (el.dataset.k === 'date' && state.events && state.events.length === 1 && !touched.has('events')) { state.events[0].time = v; }
    changed();
  });

  /* ---------- events ---------- */
  function renderEvents() {
    const box = $('#custom-events'); const ev = state.events || [];
    box.innerHTML = ev.map((e, i) => `<div class="rep" data-i="${i}">
      <div class="rep-head"><b>Event ${i + 1}</b><span><button type="button" class="icon-btn" data-ev="up" aria-label="Move up"${i ? '' : ' disabled'}>↑</button><button type="button" class="icon-btn" data-ev="down" aria-label="Move down"${i < ev.length - 1 ? '' : ' disabled'}>↓</button><button type="button" class="icon-btn" data-ev="del" aria-label="Remove event">✕</button></span></div>
      <div class="fgrid">
      <div class="field half"><label for="ev-${i}-name">Name</label><input type="text" id="ev-${i}-name" data-e="name" value="${esc(e.name)}" placeholder="Poruwa Ceremony"></div>
      <div class="field half"><label for="ev-${i}-native">Name in Sinhala / Tamil (optional)</label><input type="text" id="ev-${i}-native" data-e="native" value="${esc(e.native || '')}"></div>
      <div class="field half"><label for="ev-${i}-time">Date and time</label><input type="datetime-local" id="ev-${i}-time" data-e="time" value="${esc(toLocal(e.time))}"></div>
      <div class="field half"><label for="ev-${i}-tl">Time as shown</label><input type="text" id="ev-${i}-tl" data-e="timeLabel" value="${esc(e.timeLabel || '')}" placeholder="Auspicious time · 9.47 a.m."></div>
      <div class="field half"><label for="ev-${i}-venue">Venue</label><input type="text" id="ev-${i}-venue" data-e="venue" value="${esc(e.venue || '')}"></div>
      <div class="field half"><label for="ev-${i}-addr">Address</label><input type="text" id="ev-${i}-addr" data-e="address" value="${esc(e.address || '')}"></div>
      <div class="field"><label for="ev-${i}-note">Note (optional)</label><input type="text" id="ev-${i}-note" data-e="note" value="${esc(e.note || '')}"></div></div></div>`).join('')
      + `<button type="button" class="btn small ghost" id="ev-add">+ Add event</button>`;
  }
  $('#sections')?.addEventListener('input', () => {});
  document.addEventListener('input', e => {
    const x = e.target.closest('[data-e]'); if (!x) return; const i = +x.closest('.rep').dataset.i;
    const v = x.dataset.e === 'time' ? fromLocal(x.value) : x.value;
    state.events[i][x.dataset.e] = v; touched.add('events'); changed();
  });
  document.addEventListener('click', e => {
    const b = e.target.closest('[data-ev]'), add = e.target.closest('#ev-add'); if (!b && !add) return;
    const ev = state.events = state.events || [];
    if (add) ev.push({ name: '', time: state.date || '', timeLabel: '', venue: '', address: '' });
    else { const i = +b.closest('.rep').dataset.i, a = b.dataset.ev;
      if (a === 'del') { if (ev.length === 1) return UI.toast('Keep at least one event'); ev.splice(i, 1); }
      if (a === 'up' && i > 0) [ev[i - 1], ev[i]] = [ev[i], ev[i - 1]];
      if (a === 'down' && i < ev.length - 1) [ev[i + 1], ev[i]] = [ev[i], ev[i + 1]]; }
    touched.add('events'); renderEvents(); changed();
  });

  /* ---------- story ---------- */
  function renderStory() {
    const box = $('#custom-story'); const st = state.story || [];
    box.innerHTML = `<div class="field"><label for="f-storyIntro">Introduction</label><textarea id="f-storyIntro" data-k="storyIntro">${esc(state.storyIntro || '')}</textarea></div>`
      + st.map((s, i) => `<div class="rep" data-i="${i}"><div class="rep-head"><b>Moment ${i + 1}</b><span><button type="button" class="icon-btn" data-st="del" aria-label="Remove moment">✕</button></span></div>
      <div class="fgrid"><div class="field half"><label for="st-${i}-d">When</label><input type="text" id="st-${i}-d" data-s="date" value="${esc(s.date)}" placeholder="2019"></div>
      <div class="field half"><label for="st-${i}-t">Title</label><input type="text" id="st-${i}-t" data-s="title" value="${esc(s.title)}"></div>
      <div class="field"><label for="st-${i}-x">What happened</label><textarea id="st-${i}-x" data-s="text">${esc(s.text)}</textarea></div></div></div>`).join('')
      + `<button type="button" class="btn small ghost" id="st-add">+ Add a moment</button>`;
  }
  document.addEventListener('input', e => { const x = e.target.closest('[data-s]'); if (!x) return; state.story[+x.closest('.rep').dataset.i][x.dataset.s] = x.value; touched.add('story'); changed(); });
  document.addEventListener('click', e => {
    if (e.target.closest('#st-add')) { (state.story = state.story || []).push({ date: '', title: '', text: '' }); touched.add('story'); renderStory(); changed(); }
    const d = e.target.closest('[data-st="del"]'); if (d) { state.story.splice(+d.closest('.rep').dataset.i, 1); touched.add('story'); renderStory(); changed(); }
  });

  /* ---------- photos ---------- */
  const shrink = (file, max = 1400) => new Promise((res, rej) => {
    const img = new Image(), u = URL.createObjectURL(file);
    img.onload = () => { const s = Math.min(1, max / Math.max(img.width, img.height)); const c = document.createElement('canvas');
      c.width = Math.round(img.width * s); c.height = Math.round(img.height * s); c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
      URL.revokeObjectURL(u); res(c.toDataURL('image/jpeg', .82)); };
    img.onerror = () => rej(new Error('That file could not be read as an image.')); img.src = u;
  });
  const thumb = (src, attrs) => `<div class="thumb"${attrs}>${src ? `<img src="${esc(src)}" alt="">` : '<span>No photo</span>'}${src ? '<button type="button" class="icon-btn" aria-label="Remove photo" data-rm>✕</button>' : ''}</div>`;
  function renderPhotos() {
    const box = $('#custom-photos'); const al = state.photos || [];
    box.innerHTML = `<div class="fgrid">
      <div class="field half"><span class="lbl">Couple photo</span>${thumb(state.couplePhoto, ' data-ph="couplePhoto"')}<label class="btn small ghost upl">Upload<input type="file" accept="image/*" data-up="couplePhoto" hidden></label><span class="hint">Shown in the story section.</span></div>
      <div class="field half"><span class="lbl">Main illustration</span>${thumb(state.heroImage, ' data-ph="heroImage"')}<label class="btn small ghost upl">Upload<input type="file" accept="image/*" data-up="heroImage" hidden></label><span class="hint">Used by designs with an artwork slot (e.g. Ivory Lattice).</span></div></div>
      <div class="field" style="margin-top:16px"><span class="lbl">Album (up to 9 photos)</span><div class="album-ed">${al.map((p, i) => thumb(p, ` data-al="${i}"`)).join('')}</div>
      <label class="btn small ghost upl">Add photos<input type="file" accept="image/*" multiple data-up="photos" hidden></label></div>`;
  }
  document.addEventListener('change', async e => {
    const inp = e.target.closest('[data-up]'); if (!inp) return; const k = inp.dataset.up;
    try {
      if (k === 'photos') { state.photos = state.photos || []; for (const f of [...inp.files].slice(0, 9 - state.photos.length)) state.photos.push(await shrink(f, 1400)); }
      else state[k] = await shrink(inp.files[0], 1400);
      touched.add(k); renderPhotos(); changed();
    } catch (err) { UI.toast(err.message); }
  });
  document.addEventListener('click', e => {
    const r = e.target.closest('[data-rm]'); if (!r) return; const t = r.closest('.thumb');
    if (t.dataset.ph) state[t.dataset.ph] = ''; else state.photos.splice(+t.dataset.al, 1);
    touched.add(t.dataset.ph || 'photos'); renderPhotos(); changed();
  });

  /* ---------- music ---------- */
  let sample = null;
  function renderMusic() {
    const def = (theme.music && theme.music.style) || 'musicbox';
    const cur = (state.__music && state.__music.style) || '';
    const name = MUSIC.find(m => m[0] === def)[1];
    $('#custom-music').innerHTML = `<div class="fgrid">
      <div class="field"><label for="f-music-style">Built-in music</label><select id="f-music-style">${MUSIC.map(([v, l]) => `<option value="${v}"${v === cur ? ' selected' : ''}>${esc(v ? l : `${l}: ${name}`)}</option>`).join('')}</select>
      <button type="button" class="btn small ghost" id="m-sample" style="justify-self:start">▶ Listen</button></div>
      <div class="field"><span class="lbl">Or your own song (MP3, up to 8 MB)</span><div class="copyrow"><input type="text" id="f-music-url" placeholder="https://… or upload" value="${esc(media.musicName || (state.music && !state.music.startsWith('blob:') ? state.music : ''))}" aria-label="Song link"><label class="btn small ghost upl">Upload<input type="file" accept="audio/mpeg" id="f-music-file" hidden></label></div>
      <span class="hint">Only use music you have the rights to share.</span></div>
      <label class="check"><input type="checkbox" id="f-music-auto"${state.musicOnOpen === false ? '' : ' checked'}> Start music when the invitation is opened</label></div>`;
  }
  document.addEventListener('change', e => {
    if (e.target.id === 'f-music-style') { const v = e.target.value; if (v) state.__music = { style: v }; else delete state.__music; touched.add('__music'); if (sample) { sample.stop(); sample = null; } changed(); }
    if (e.target.id === 'f-music-auto') { state.musicOnOpen = e.target.checked; touched.add('musicOnOpen'); changed(); }
    if (e.target.id === 'f-music-file') { const f = e.target.files[0]; if (!f) return; if (f.size > 8 * 1024 * 1024) return UI.toast('Please choose an MP3 under 8 MB'); media.musicFile = f; media.musicName = f.name; state.music = URL.createObjectURL(f); touched.add('music'); renderMusic(); changed(); }
  });
  document.addEventListener('input', e => { if (e.target.id === 'f-music-url') { state.music = e.target.value.trim(); media.musicFile = null; media.musicName = ''; touched.add('music'); changed(); } });
  document.addEventListener('click', e => {
    if (!e.target.closest('#m-sample')) return;
    if (sample) { sample.stop(); sample = null; e.target.textContent = '▶ Listen'; return; }
    const st = (state.__music && state.__music.style) || (theme.music && theme.music.style) || 'musicbox';
    sample = WeddingMusic.create(Object.assign({}, theme.music || {}, { style: st })); sample.play(); e.target.textContent = '■ Stop';
  });

  /* ---------- template picker ---------- */
  function renderPicker() {
    const plan = Q.get('plan');
    $('#tpick').innerHTML = ['Classic', 'Premium'].map(g => `<p class="tp-g">${g} designs${g === 'Premium' ? '<span class="tag-prem">PREMIUM</span>' : ''}</p><div class="tp-row">`
      + TPL.filter(t => !!t.premium === (g === 'Premium')).map(t => `<button type="button" class="tp" data-t="${esc(t.id)}" aria-pressed="false" style="--c:${esc(t.color)}"><i></i><span>${esc(t.name)}</span><small>${esc(t.category.replace('Premium · ', ''))}</small></button>`).join('') + '</div>').join('');
    if (plan === 'classic') $('#tpick').prepend(Object.assign(document.createElement('p'), { className: 'hint', textContent: 'Classic plan: choose any classic design.' }));
  }
  document.addEventListener('click', e => { const b = e.target.closest('.tp'); if (b) chooseTemplate(b.dataset.t); });

  async function loadTemplate(id) {
    const t = TPL.find(x => x.id === id) || TPL[0];
    const html = await (await fetch(t.file)).text();
    const d = JSON.parse(/\/\*WEDDING\*\/([\s\S]*?)\/\*END\*\//.exec(html)[1]);
    const th = JSON.parse(/\/\*THEME\*\/([\s\S]*?)\/\*END\*\//.exec(html)[1]);
    return { t, d, th, html };
  }
  async function chooseTemplate(id, keepAll) {
    const { t, d, th } = await loadTemplate(id);
    const old = state; tpl = t; theme = th; defaults = d;
    const next = clone(d);
    if (keepAll) Object.assign(next, clone(old), { labels: Object.assign({}, d.labels, old.labels || {}) });
    else touched.forEach(p => { const v = get(old, p); if (v !== undefined) put(next, p, clone(v)); });
    state = next;
    $$('.tp').forEach(b => b.setAttribute('aria-pressed', b.dataset.t === t.id));
    $('#tname').textContent = t.name;
    fillForm(); changed(true);
  }

  /* ---------- preview ---------- */
  const pv = $('#pv'); let pvTimer, pvScroll = 0, opening = false;
  function writePreview() {
    try { localStorage.setItem('mangala-preview', JSON.stringify(state)); return true; }
    catch (_) { try { const s = clone(state); s.photos = (s.photos || []).slice(0, 3); localStorage.setItem('mangala-preview', JSON.stringify(s)); return true; } catch (e) { return false; } }
  }
  function refresh(withOpening) {
    if (!writePreview()) UI.toast('Preview is limited: too many large photos');
    try { pvScroll = pv.contentWindow ? pv.contentWindow.scrollY : 0; } catch (_) { pvScroll = 0; }
    opening = !!withOpening;
    pv.src = `${tpl.file}?preview${withOpening ? '' : '&open'}&r=${Date.now()}`;
  }
  pv.addEventListener('load', () => { if (!opening && pvScroll) try { pv.contentWindow.scrollTo(0, pvScroll); } catch (_) {} });
  function changed(now) {
    saveDraft();
    clearTimeout(pvTimer); pvTimer = setTimeout(() => refresh(false), now ? 0 : 700);
    $('#status').textContent = 'Draft saved on this device';
  }
  $('#replay').addEventListener('click', () => refresh(true));
  $('#pv-open').addEventListener('click', () => { writePreview(); window.open(`${tpl.file}?preview`, '_blank', 'noopener'); });
  $('#show-preview').addEventListener('click', () => { document.body.classList.add('pv-on'); UI.fit(); refresh(true); });
  $('#hide-preview').addEventListener('click', () => document.body.classList.remove('pv-on'));

  /* ---------- drafts ---------- */
  const DKEY = EDIT.id ? `mangala-edit-${EDIT.id}` : 'mangala-draft';
  function saveDraft() {
    const d = { template: tpl.id, state, touched: [...touched] };
    try { localStorage.setItem(DKEY, JSON.stringify(d)); } catch (_) { try { const s = clone(state); s.photos = []; s.couplePhoto = ''; s.heroImage = ''; localStorage.setItem(DKEY, JSON.stringify({ ...d, state: s })); } catch (__) {} }
  }
  function loadDraft() { try { return JSON.parse(localStorage.getItem(DKEY) || 'null'); } catch (_) { return null; } }
  $('#reset').addEventListener('click', async () => {
    const box = $('#confirm'); box.hidden = false;
  });
  $('#confirm-no').addEventListener('click', () => $('#confirm').hidden = true);
  $('#confirm-yes').addEventListener('click', async () => {
    $('#confirm').hidden = true; try { localStorage.removeItem(DKEY); } catch (_) {} touched = new Set(); state = {}; media = {}; await chooseTemplate(tpl.id); UI.toast('Started over with the sample wording');
  });

  /* ---------- validation ---------- */
  function problems() {
    const p = [];
    if (!String(state.partner1 || '').trim() || !String(state.partner2 || '').trim()) p.push('Enter both first names.');
    if (!state.date || isNaN(new Date(state.date))) p.push('Choose the main date and time.');
    if (!(state.events || []).length || state.events.some(e => !e.name || !e.time)) p.push('Give every event a name and a date.');
    return p;
  }

  /* ---------- publish ---------- */
  const api = async (method, url, body) => {
    const r = await fetch(url, { method, headers: { 'Content-Type': 'application/json' }, body: body ? JSON.stringify(body) : undefined });
    let j = null; try { j = await r.json(); } catch (_) {}
    if (!r.ok) { const e = new Error((j && j.error) || `Server error (${r.status})`); e.status = r.status; throw e; }
    return j;
  };
  const fileToDataUrl = f => new Promise((res, rej) => { const r = new FileReader(); r.onload = () => res(r.result); r.onerror = rej; r.readAsDataURL(f); });
  async function uploadAll(d) {
    const up = async v => (typeof v === 'string' && v.startsWith('data:')) ? (await api('POST', '/api/media', { dataUrl: v })).url : v;
    d.couplePhoto = await up(d.couplePhoto); d.heroImage = await up(d.heroImage);
    d.photos = await Promise.all((d.photos || []).map(up));
    if (media.musicFile) { d.music = (await api('POST', '/api/media', { dataUrl: (await fileToDataUrl(media.musicFile)).replace(/^data:audio\/mp3/, 'data:audio/mpeg') })).url; state.music = d.music; media.musicFile = null; }
    else if (d.music && d.music.startsWith('blob:')) d.music = '';
    // keep the uploaded URLs so the next publish doesn't upload again
    state.couplePhoto = d.couplePhoto; state.heroImage = d.heroImage; state.photos = d.photos;
    return d;
  }
  $('#publish').addEventListener('click', async () => {
    const pr = problems(); if (pr.length) return showErrors(pr);
    const btn = $('#publish'); btn.disabled = true; btn.textContent = 'Publishing…';
    try {
      const d = await uploadAll(clone(state));
      let slug = EDIT.id, key = EDIT.key;
      if (EDIT.id) await api('PUT', `/api/invites/${encodeURIComponent(EDIT.id)}?key=${encodeURIComponent(EDIT.key)}`, { template: tpl.id, data: d });
      else { const r = await api('POST', '/api/invites', { template: tpl.id, data: d }); slug = r.slug; key = r.key; remember(slug, key, d); }
      saveDraft(); showPublished(slug, key, !!EDIT.id);
    } catch (e) {
      if (!e.status || e.status === 404 || e.status === 405) showOffline(); else showErrors([e.message]);
    } finally { btn.disabled = false; btn.textContent = EDIT.id ? 'Save changes' : 'Publish & get link'; }
  });
  function remember(slug, key, d) {
    try { const all = JSON.parse(localStorage.getItem('mangala-mine') || '[]'); all.unshift({ slug, key, names: `${d.partner1} & ${d.partner2}`, at: Date.now() }); localStorage.setItem('mangala-mine', JSON.stringify(all.slice(0, 20))); } catch (_) {}
  }
  function modal(html) { const m = $('#modal'); $('#modal .box').innerHTML = html + '<p style="margin-top:22px"><button type="button" class="btn ghost" data-close>Close</button></p>'; m.hidden = false; $('#modal .box').focus(); }
  $('#modal').addEventListener('click', e => { if (e.target.id === 'modal' || e.target.closest('[data-close]')) $('#modal').hidden = true; });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') { $('#modal').hidden = true; $('#confirm').hidden = true; } });
  function showErrors(list) { modal(`<h2>Almost there</h2><ul class="errs">${list.map(x => `<li>${esc(x)}</li>`).join('')}</ul>`); }
  function showPublished(slug, key, updated) {
    const inv = `${location.origin}${(window.SITE && SITE.invitePath) || '/i/'}${slug}`, dash = `${location.origin}/dashboard.html?id=${slug}&key=${encodeURIComponent(key)}`;
    const wa = `https://wa.me/?text=${encodeURIComponent(`You're invited to our wedding! ${inv}`)}`;
    modal(`<p class="eyebrow">${updated ? 'Changes saved' : 'Your invitation is live'}</p><h2>${esc(state.partner1)} &amp; ${esc(state.partner2)}</h2>
      <div class="field" style="margin-top:18px"><span class="lbl">Invitation link — share this with guests</span><div class="copyrow"><input type="text" readonly value="${esc(inv)}" id="o-inv" aria-label="Invitation link"><button type="button" class="btn small" data-copy="o-inv">Copy</button></div></div>
      <div class="field" style="margin-top:14px"><span class="lbl">Your private dashboard — RSVPs, guest links and editing</span><div class="copyrow"><input type="text" readonly value="${esc(dash)}" id="o-dash" aria-label="Dashboard link"><button type="button" class="btn small" data-copy="o-dash">Copy</button></div>
      <span class="hint">Keep this link private. Anyone with it can see RSVPs and edit your invitation.</span></div>
      <p style="display:flex;gap:10px;flex-wrap:wrap;margin-top:18px"><a class="btn gold" href="${esc(wa)}" target="_blank" rel="noopener">Share on WhatsApp</a><a class="btn ghost" href="${esc(dash)}">Open dashboard</a><a class="btn ghost" href="${esc(inv)}" target="_blank" rel="noopener">View invitation</a></p>`);
  }
  document.addEventListener('click', e => { const c = e.target.closest('[data-copy]'); if (c) { const i = document.getElementById(c.dataset.copy); UI.copy(i.value, i); } });
  function showOffline() {
    modal(`<h2>Publishing isn’t connected yet</h2><p class="muted" style="margin-top:10px">This copy of the website is running without its server, so it can’t create a link. You can still download the finished invitation as a single file and host it anywhere.</p>
      <p style="margin-top:18px"><button type="button" class="btn" id="dl2">Download invitation file</button></p>`);
    $('#dl2').addEventListener('click', download);
  }

  /* ---------- download standalone HTML ---------- */
  async function download() {
    const pr = problems(); if (pr.length) return showErrors(pr);
    const { html } = await loadTemplate(tpl.id);
    const d = clone(state);
    if (media.musicFile) d.music = (await fileToDataUrl(media.musicFile));
    else if (d.music && d.music.startsWith('blob:')) d.music = '';
    const music = d.__music; delete d.__music; if (d.rsvp) d.rsvp.endpoint = '';
    let out = html.replace(/\/\*WEDDING\*\/[\s\S]*?\/\*END\*\//, () => `/*WEDDING*/${JSON.stringify(d, null, 2).replace(/</g, '\\u003c')}/*END*/`);
    if (music) out = out.replace(/\/\*THEME\*\/([\s\S]*?)\/\*END\*\//, (m, j) => { const th = JSON.parse(j); th.music = Object.assign({}, th.music || {}, music); return `/*THEME*/${JSON.stringify(th)}/*END*/`; });
    out = out.replace(/<title>[\s\S]*?<\/title>/, `<title>${esc(d.partner1)} &amp; ${esc(d.partner2)} — Wedding Invitation</title>`);
    const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([out], { type: 'text/html' }));
    a.download = `${String(d.partner1 + '-' + d.partner2).toLowerCase().replace(/[^a-z0-9]+/g, '-')}-invitation.html`; document.body.appendChild(a); a.click(); a.remove();
    UI.toast('Invitation downloaded');
  }
  $('#download').addEventListener('click', download);

  /* ---------- boot ---------- */
  (async () => {
    TPL = await UI.templates(); UI.fit();
    renderPicker(); renderForm();
    if (EDIT.id && EDIT.key) {
      $('#mode').textContent = 'Edit your invitation'; $('#publish').textContent = 'Save changes';
      try {
        const r = await api('GET', `/api/invites/${encodeURIComponent(EDIT.id)}?key=${encodeURIComponent(EDIT.key)}`);
        state = r.data; SECTIONS.forEach(() => {}); touched = new Set(Object.keys(r.data));
        await chooseTemplate(r.template, true);
        $('#dash-link').hidden = false; $('#dash-link').href = `dashboard.html?id=${encodeURIComponent(EDIT.id)}&key=${encodeURIComponent(EDIT.key)}`;
        return;
      } catch (e) { modal(`<h2>Couldn’t open this invitation</h2><p class="muted" style="margin-top:10px">${esc(e.message)}</p>`); }
    }
    const dr = loadDraft();
    const want = Q.get('t');
    if (dr && (!want || want === dr.template)) { state = dr.state; touched = new Set(dr.touched || []); await chooseTemplate(dr.template, true); $('#status').textContent = 'Restored your draft'; }
    else {
      const plan = Q.get('plan');
      const first = want || (plan === 'premium' || plan === 'royal' ? TPL.find(t => t.premium).id : TPL[0].id);
      if (dr) { state = dr.state; touched = new Set(dr.touched || []); }
      await chooseTemplate(first);
    }
  })();
})();
