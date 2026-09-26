// Platform-neutral API logic, used by Azure Functions (src/functions) and the local server (server.js).
const crypto = require('crypto');
const fs = require('fs');
const path = require('path');
const store = require('./store');
const TEMPLATES = require('./templates.json');     // { id: { file, name, premium } }
const SITE = require('./site.json');               // { brand, domain }

const json = (status, obj, extra = {}) => ({ status, headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', ...extra }, body: JSON.stringify(obj) });
const sha = s => crypto.createHash('sha256').update(String(s)).digest('hex');
const rand = n => crypto.randomBytes(n).toString('base64url').slice(0, n);
const slugify = s => String(s || '').normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 40);
const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const validSlug = s => /^[a-z0-9-]{3,60}$/.test(s || '');
const MAX_INVITE = 3 * 1024 * 1024;

async function loadInvite(slug) {
  if (!validSlug(slug)) return null;
  const r = await store.get('invites', slug + '.json');
  return r ? JSON.parse(r.buf.toString('utf8')) : null;
}
async function saveInvite(slug, inv) { await store.put('invites', slug + '.json', Buffer.from(JSON.stringify(inv)), 'application/json'); }

function cleanData(data) {
  if (!data || typeof data !== 'object') throw new Error('Missing invitation details.');
  const d = JSON.parse(JSON.stringify(data));
  if (!d.partner1 || !d.partner2) throw new Error('Both names are required.');
  if (!d.date || isNaN(new Date(d.date))) throw new Error('A valid wedding date is required.');
  delete d.rsvp?.endpoint;
  // images must be our own media URLs or https links, never inline data (keeps invites small)
  const okImg = u => !u || /^\/api\/media\/[A-Za-z0-9_-]+$/.test(u) || /^https:\/\//.test(u);
  for (const k of ['couplePhoto', 'heroImage']) if (!okImg(d[k])) d[k] = '';
  if (Array.isArray(d.photos)) d.photos = d.photos.filter(okImg).slice(0, 12);
  if (d.music && !/^https:\/\/|^\/api\/media\//.test(d.music)) d.music = '';
  return d;
}

async function createInvite(body) {
  const { template, data } = body || {};
  if (!TEMPLATES[template]) return json(400, { error: 'Unknown template.' });
  let d; try { d = cleanData(data); } catch (e) { return json(400, { error: e.message }); }
  const base = slugify(`${d.partner1}-${d.partner2}`) || 'invite';
  let slug = base, n = 1;
  while (await loadInvite(slug)) slug = `${base}-${++n}`;
  const key = rand(24);
  const now = new Date().toISOString();
  await saveInvite(slug, { template, data: d, keyHash: sha(key), created: now, updated: now });
  return json(201, { slug, key });
}

async function getInvite(slug, key) {
  const inv = await loadInvite(slug);
  if (!inv) return json(404, { error: 'Invitation not found.' });
  if (!key || sha(key) !== inv.keyHash) return json(403, { error: 'Wrong or missing edit key.' });
  return json(200, { template: inv.template, data: inv.data, created: inv.created, updated: inv.updated });
}

async function updateInvite(slug, key, body) {
  const inv = await loadInvite(slug);
  if (!inv) return json(404, { error: 'Invitation not found.' });
  if (!key || sha(key) !== inv.keyHash) return json(403, { error: 'Wrong or missing edit key.' });
  const { template, data } = body || {};
  if (template && !TEMPLATES[template]) return json(400, { error: 'Unknown template.' });
  try { inv.data = cleanData(data); } catch (e) { return json(400, { error: e.message }); }
  if (template) inv.template = template;
  inv.updated = new Date().toISOString();
  await saveInvite(slug, inv);
  return json(200, { slug });
}

async function uploadMedia(body) {
  const m = /^data:(image\/(jpeg|png|webp)|audio\/mpeg);base64,([A-Za-z0-9+/=]+)$/.exec(body?.dataUrl || '');
  if (!m) return json(400, { error: 'Upload a JPEG, PNG, WebP image or an MP3 file.' });
  const buf = Buffer.from(m[3], 'base64');
  const limit = m[1] === 'audio/mpeg' ? 8 * 1024 * 1024 : 2 * 1024 * 1024;
  if (buf.length > limit) return json(413, { error: 'File is too large.' });
  const id = rand(20);
  await store.put('media', id, buf, m[1]);
  return json(201, { url: `/api/media/${id}` });
}

async function getMedia(id) {
  if (!/^[A-Za-z0-9_-]{10,40}$/.test(id || '')) return { status: 404, body: '' };
  const r = await store.get('media', id);
  if (!r) return { status: 404, body: '' };
  return { status: 200, headers: { 'Content-Type': r.type || 'application/octet-stream', 'Cache-Control': 'public, max-age=31536000, immutable' }, body: r.buf, isBinary: true };
}

async function addRsvp(slug, body) {
  const inv = await loadInvite(slug);
  if (!inv) return json(404, { error: 'Invitation not found.' });
  const b = body || {};
  const name = String(b.name || '').trim().slice(0, 100);
  if (!name) return json(400, { error: 'Please enter your name.' });
  const rec = {
    name, attending: b.attending === 'no' ? 'no' : 'yes',
    guests: Math.max(0, Math.min(20, parseInt(b.guests, 10) || 0)),
    events: Array.isArray(b.events) ? b.events.slice(0, 10).map(x => String(x).slice(0, 80)) : [],
    message: String(b.message || '').slice(0, 600),
    at: new Date().toISOString(),
  };
  if (rec.attending === 'no') { rec.guests = 0; rec.events = []; }
  await store.put('rsvps', `${slug}/${Date.now()}-${rand(6)}.json`, Buffer.from(JSON.stringify(rec)), 'application/json');
  return json(201, { ok: true });
}

async function listRsvps(slug, key) {
  const inv = await loadInvite(slug);
  if (!inv) return json(404, { error: 'Invitation not found.' });
  if (!key || sha(key) !== inv.keyHash) return json(403, { error: 'Wrong or missing edit key.' });
  const names = await store.list('rsvps', slug + '/');
  const rows = [];
  for (const n of names) { const r = await store.get('rsvps', n); if (r) rows.push(JSON.parse(r.buf.toString('utf8'))); }
  rows.sort((a, b) => a.at < b.at ? 1 : -1);
  return json(200, { couple: `${inv.data.partner1} & ${inv.data.partner2}`, date: inv.data.date, events: (inv.data.events || []).map(e => e.name), rsvps: rows });
}

const tplCache = {};
async function templateHtml(file, origin) {
  if (tplCache[file]) return tplCache[file];
  const root = process.env.SITE_ROOT;
  let html = null;
  if (root) { try { html = await fs.promises.readFile(path.join(root, file), 'utf8'); } catch (_) {} }
  if (!html) { const r = await fetch(`${origin}/${file}`); if (!r.ok) throw new Error('Template unavailable'); html = await r.text(); }
  tplCache[file] = html;
  return html;
}

async function render(slug, origin) {
  const inv = await loadInvite(slug);
  if (!inv) return { status: 404, headers: { 'Content-Type': 'text/html; charset=utf-8' }, body: `<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Invitation not found</title><body style="font-family:Georgia,serif;text-align:center;padding:80px 20px;color:#3b2418;background:#fbf6ee"><h1 style="font-weight:400">Invitation not found</h1><p>Please check the link you were sent.</p></body>` };
  const t = TEMPLATES[inv.template];
  let html = await templateHtml(t.file, origin);
  const tplData = JSON.parse(/\/\*WEDDING\*\/([\s\S]*?)\/\*END\*\//.exec(html)[1]);
  const d = { ...tplData, ...inv.data, labels: { ...tplData.labels, ...(inv.data.labels || {}) } };
  d.slug = slug;
  d.rsvp = { ...(tplData.rsvp || {}), ...(inv.data.rsvp || {}), endpoint: `/api/rsvp/${slug}` };
  d.brand = SITE.footer || '';
  const music = d.__music; delete d.__music;
  const safe = JSON.stringify(d).replace(/</g, '\\u003c');
  html = html.replace(/\/\*WEDDING\*\/[\s\S]*?\/\*END\*\//, () => `/*WEDDING*/${safe}/*END*/`);
  if (music) html = html.replace(/\/\*THEME\*\/([\s\S]*?)\/\*END\*\//, (m, j) => { const th = JSON.parse(j); th.music = { ...(th.music || {}), ...music }; return `/*THEME*/${JSON.stringify(th).replace(/</g, '\\u003c')}/*END*/`; });
  const names = `${d.partner1} & ${d.partner2}`;
  const when = new Date(d.date).toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric', timeZone: d.timezone || 'Asia/Colombo' });
  const title = `${names} — Wedding Invitation`;
  const desc = `You are invited to celebrate the wedding of ${names} on ${when}${d.venueLine ? ' · ' + d.venueLine : ''}. Tap to open your invitation.`;
  html = html.replace(/<title>[\s\S]*?<\/title>/, `<title>${esc(title)}</title>`)
    .replace(/<meta property="og:title" content="[^"]*">/, `<meta property="og:title" content="${esc(title)}">`)
    .replace(/<meta property="og:description" content="[^"]*">/, `<meta property="og:description" content="${esc(desc)}">`)
    .replace(/<meta name="description" content="[^"]*">/, `<meta name="description" content="${esc(desc)}">`);
  if (d.couplePhoto || d.heroImage) {
    const img = d.couplePhoto || d.heroImage, abs = img.startsWith('/') ? origin + img : img;
    html = html.replace('<meta property="og:type" content="website">', `<meta property="og:type" content="website"><meta property="og:image" content="${esc(abs)}">`);
  }
  return { status: 200, headers: { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-cache' }, body: html };
}

module.exports = { createInvite, getInvite, updateInvite, uploadMedia, getMedia, addRsvp, listRsvps, render, json, storeKind: store.kind };
