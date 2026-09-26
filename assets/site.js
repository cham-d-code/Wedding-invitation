/* Shared site behaviour: menu, config fill, pricing, lazy phone previews, template gallery, toast, copy. */
(() => {
  const S = window.SITE || {};
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const money = n => (S.currency || 'LKR') + ' ' + Number(n).toLocaleString('en-US');

  // menu
  const mb = $('.menu-btn'), nav = $('.nav');
  if (mb) mb.addEventListener('click', () => { const o = nav.classList.toggle('open'); mb.setAttribute('aria-expanded', o); });

  // config text + WhatsApp links
  $$('[data-site]').forEach(el => { const v = S[el.dataset.site]; if (v) el.textContent = v; });
  $$('[data-wa]').forEach(a => { a.href = `https://wa.me/${S.whatsapp}?text=${encodeURIComponent(a.dataset.wa || 'Hi! I would like to create a digital wedding invitation.')}`; a.target = '_blank'; a.rel = 'noopener'; });
  $$('[data-mail]').forEach(a => { a.href = 'mailto:' + S.email; a.textContent = S.email; });
  $$('[data-year]').forEach(el => el.textContent = new Date().getFullYear());

  // pricing
  const plans = $('#plans');
  if (plans && S.plans) plans.innerHTML = S.plans.map(p => `<article class="plan${p.featured ? ' featured' : ''}">
    <h3>${esc(p.name)}</h3><p class="price">${esc(money(p.price))}<small>${esc(p.note || '')}</small></p>
    <ul>${p.features.map(f => `<li>${esc(f)}</li>`).join('')}</ul>
    <a class="btn${p.featured ? '' : ' ghost'}" href="/create.html?plan=${encodeURIComponent(p.id)}">Start with ${esc(p.name)}</a></article>`).join('');

  // scale the 390px-wide invitation to the phone frame
  const fit = () => $$('.phone').forEach(ph => { const f = ph.querySelector('iframe'); if (f && ph.clientWidth) f.style.transform = `scale(${ph.clientWidth / 390})`; });
  addEventListener('resize', fit); addEventListener('load', fit);
  // lazy live phones: <div class="phone" data-src="...">
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return; const ph = e.target; io.unobserve(ph);
    const f = document.createElement('iframe'); f.src = ph.dataset.src; f.title = ph.dataset.title || 'Invitation preview'; f.setAttribute('tabindex', '-1');
    ph.prepend(f); fit();
  }), { rootMargin: '300px' });
  const watch = () => $$('.phone[data-src]:not([data-w])').forEach(p => { p.dataset.w = 1; io.observe(p); });
  watch();

  // template gallery / showcase
  async function templates() { const r = await fetch('/assets/templates.json'); return r.json(); }
  const grid = $('#tgrid');
  if (grid) templates().then(list => {
    const tags = ['All', 'Premium', 'Traditional', 'Hindu', 'Muslim', 'Catholic', 'Luxury', 'Floral', 'Modern'];
    const chips = $('#chips');
    chips.innerHTML = tags.map(t => `<button type="button" class="chip" data-t="${t}">${t}</button>`).join('');
    grid.innerHTML = list.map(t => `<article class="tcard" data-tags="${esc(t.tags.join(' '))}">
      <div class="phone" data-src="${esc(t.file)}" data-title="${esc(t.name)} preview"></div>
      <p class="cat">${esc(t.category)}</p><h3>${esc(t.name)}${t.premium ? '<span class="tag-prem">PREMIUM</span>' : ''}</h3><p class="b">${esc(t.blurb)}</p>
      <div class="acts"><a class="btn small" href="/create.html?t=${encodeURIComponent(t.id)}">Use this design</a>
      <a class="btn small ghost" href="${esc(t.file)}" target="_blank" rel="noopener">Full screen</a></div></article>`).join('');
    watch();
    const set = g => { $$('.chip', chips).forEach(c => c.setAttribute('aria-pressed', c.dataset.t === g)); $$('.tcard', grid).forEach(c => c.hidden = !(g === 'All' || c.dataset.tags.split(' ').includes(g))); };
    chips.addEventListener('click', e => { const c = e.target.closest('.chip'); if (c) { set(c.dataset.t); history.replaceState(null, '', '#' + c.dataset.t.toLowerCase()); } });
    const h = (location.hash || '').slice(1); set(tags.find(t => t.toLowerCase() === h) || 'All');
  });
  const show = $('#showcase');
  if (show) templates().then(list => {
    const pick = (show.dataset.ids || '').split(',');
    show.innerHTML = pick.map(id => list.find(t => t.id === id)).filter(Boolean).map(t => `<a class="item" href="/create.html?t=${encodeURIComponent(t.id)}" style="text-decoration:none">
      <div class="phone" data-src="${esc(t.file)}" data-title="${esc(t.name)} preview"><span class="ph-shield"></span></div><b>${esc(t.name)}</b><span>${esc(t.category)}</span></a>`).join('');
    watch();
  });

  // music samples on the home page
  let current = null;
  $$('.music-card').forEach(b => b.addEventListener('click', () => {
    if (!window.WeddingMusic) return;
    const on = b.getAttribute('aria-pressed') === 'true';
    $$('.music-card').forEach(x => x.setAttribute('aria-pressed', 'false'));
    if (current) { current.stop(); current = null; }
    if (!on) { current = window.WeddingMusic.create({ style: b.dataset.style }); current.play(); b.setAttribute('aria-pressed', 'true'); }
  }));

  // helpers for other scripts
  window.UI = {
    toast(msg) { let t = $('.toast'); if (!t) { t = document.createElement('div'); t.className = 'toast'; t.setAttribute('role', 'status'); document.body.appendChild(t); } t.textContent = msg; t.classList.add('on'); clearTimeout(t._h); t._h = setTimeout(() => t.classList.remove('on'), 2600); },
    async copy(text, input) { try { await navigator.clipboard.writeText(text); UI.toast('Copied'); } catch (_) { if (input) { input.select(); document.execCommand && document.execCommand('copy'); UI.toast('Copied'); } } },
    esc, money, templates, fit,
  };
})();
