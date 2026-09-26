/* Couple dashboard: RSVPs, totals, CSV export, personalised guest links. */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const Q = new URLSearchParams(location.search);
  const id = Q.get('id'), key = Q.get('key');
  let data = null;
  const base = () => id ? `${location.origin}${(window.SITE && SITE.invitePath) || '/i/'}${id}` : ($('#base-url').value || '').trim().replace(/[?#].*$/, '');

  function stats(rows) {
    const yes = rows.filter(r => r.attending === 'yes');
    const guests = yes.reduce((a, r) => a + (r.guests || 0), 0);
    const perEvent = {};
    (data.events || []).forEach(e => perEvent[e] = 0);
    yes.forEach(r => (r.events || []).forEach(e => perEvent[e] = (perEvent[e] || 0) + (r.guests || 0)));
    $('#stats').innerHTML = [
      ['Replies', rows.length], ['Attending', yes.length], ['Guests coming', guests], ['Can’t come', rows.length - yes.length],
    ].map(([l, v]) => `<div class="stat"><b>${v}</b><span>${l}</span></div>`).join('');
    $('#per-event').innerHTML = Object.keys(perEvent).length > 1 ? Object.entries(perEvent).map(([e, n]) => `<li><span>${esc(e)}</span><b>${n}</b></li>`).join('') : '';
  }
  function table(rows) {
    const t = $('#rows');
    if (!rows.length) { t.innerHTML = '<tr><td colspan="6" class="empty">No replies yet. Share your invitation and RSVPs will appear here.</td></tr>'; return; }
    t.innerHTML = rows.map(r => `<tr><td>${esc(r.name)}</td><td><span class="pill ${r.attending === 'yes' ? 'ok' : 'no'}">${r.attending === 'yes' ? 'Attending' : 'Not attending'}</span></td>
      <td class="num">${r.attending === 'yes' ? r.guests : '—'}</td><td>${esc((r.events || []).join(', '))}</td><td>${esc(r.message || '')}</td>
      <td class="when">${new Date(r.at).toLocaleString('en-GB', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' })}</td></tr>`).join('');
  }
  function csv() {
    const rows = [['Name', 'Attending', 'Guests', 'Events', 'Message', 'Replied at'], ...data.rsvps.map(r => [r.name, r.attending, r.guests, (r.events || []).join('; '), r.message || '', r.at])];
    const txt = rows.map(r => r.map(v => `"${String(v).replace(/"/g, '""')}"`).join(',')).join('\r\n');
    const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob(['﻿' + txt], { type: 'text/csv' }));
    a.download = `${id}-rsvps.csv`; document.body.appendChild(a); a.click(); a.remove();
  }
  async function load() {
    const r = await fetch(`/api/rsvps/${encodeURIComponent(id)}?key=${encodeURIComponent(key)}`);
    const j = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(j.error || 'Could not load RSVPs.');
    data = j;
    $('#couple').textContent = j.couple;
    $('#when').textContent = new Date(j.date).toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric', timeZone: 'Asia/Colombo' });
    $('#inv-link').value = base(); $('#view').href = base();
    $('#edit').href = `create.html?id=${encodeURIComponent(id)}&key=${encodeURIComponent(key)}`;
    stats(j.rsvps); table(j.rsvps);
    $('#updated').textContent = 'Updated ' + new Date().toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' });
  }

  /* guest links */
  function links() {
    const names = $('#guests').value.split('\n').map(s => s.trim()).filter(Boolean).slice(0, 300);
    const b = base();
    if (!b) { $('#links').innerHTML = '<li class="muted">Enter your invitation link above first.</li>'; return; }
    const msg = $('#msg').value;
    $('#links').innerHTML = names.map((n, i) => {
      const url = `${b}?to=${encodeURIComponent(n)}`;
      const text = msg.replace(/\{name\}/g, n).replace(/\{link\}/g, url);
      return `<li><div><b>${esc(n)}</b><input type="text" readonly value="${esc(url)}" id="gl-${i}" aria-label="Link for ${esc(n)}"></div>
        <span><button type="button" class="btn small ghost" data-copy="gl-${i}">Copy</button><a class="btn small" target="_blank" rel="noopener" href="https://wa.me/?text=${encodeURIComponent(text)}">WhatsApp</a></span></li>`;
    }).join('');
  }
  document.addEventListener('click', e => { const c = e.target.closest('[data-copy]'); if (c) { const i = document.getElementById(c.dataset.copy); UI.copy(i.value, i); } });
  $('#guests').addEventListener('input', links); $('#msg').addEventListener('input', links);
  $('#base-url').addEventListener('input', links);
  $('#csv').addEventListener('click', csv);
  $('#refresh').addEventListener('click', () => load().catch(e => UI.toast(e.message)));
  try { const g = localStorage.getItem('mangala-guests-' + (id || 'x')); if (g) $('#guests').value = g; } catch (_) {}
  $('#guests').addEventListener('change', () => { try { localStorage.setItem('mangala-guests-' + (id || 'x'), $('#guests').value); } catch (_) {} });

  if (!id || !key) {
    $('#rsvp-area').hidden = true; $('#nokey').hidden = false; $('#base-row').hidden = false;
    try { const mine = JSON.parse(localStorage.getItem('mangala-mine') || '[]'); if (mine.length) $('#mine').innerHTML = '<p class="lbl" style="margin-top:14px">Invitations created on this device</p><ul class="mine">' + mine.map(m => `<li><a href="dashboard.html?id=${encodeURIComponent(m.slug)}&key=${encodeURIComponent(m.key)}">${esc(m.names)}</a> <span class="muted">/i/${esc(m.slug)}</span></li>`).join('') + '</ul>'; } catch (_) {}
    links(); return;
  }
  load().then(links).catch(e => { $('#rsvp-area').innerHTML = `<p class="notice err">${esc(e.message)} Check that you opened the full dashboard link you were given.</p>`; });
})();
