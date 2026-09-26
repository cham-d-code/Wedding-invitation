// Local / VPS server: serves the website and the same API as the Azure Functions.
// Usage: node server.js   (then open http://localhost:8080)
// Data is kept in ./.data unless STORAGE_CONNECTION (Azure Blob) is set.
const http = require('http');
const fs = require('fs');
const path = require('path');
const ROOT = __dirname;
process.env.SITE_ROOT = process.env.SITE_ROOT || ROOT;
const core = require('./api/src/lib/core');
const PORT = process.env.PORT || 8080;

const TYPES = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.ico': 'image/x-icon', '.webp': 'image/webp', '.mp3': 'audio/mpeg', '.txt': 'text/plain' };

function readBody(req, limit = 12 * 1024 * 1024) {
  return new Promise((res, rej) => {
    const ch = []; let n = 0;
    req.on('data', d => { n += d.length; if (n > limit) { rej(new Error('too large')); req.destroy(); } else ch.push(d); });
    req.on('end', () => { try { res(ch.length ? JSON.parse(Buffer.concat(ch).toString('utf8')) : null); } catch (_) { res(null); } });
  });
}
function out(res, r) { res.writeHead(r.status, r.headers || {}); res.end(r.body); }

http.createServer(async (req, res) => {
  const u = new URL(req.url, 'http://x');
  const p = decodeURIComponent(u.pathname);
  const origin = `http://${req.headers.host}`;
  try {
    let m;
    if (p === '/api/invites' && req.method === 'POST') return out(res, await core.createInvite(await readBody(req)));
    if ((m = p.match(/^\/api\/invites\/([a-z0-9-]+)$/))) {
      if (req.method === 'GET') return out(res, await core.getInvite(m[1], u.searchParams.get('key')));
      if (req.method === 'PUT') return out(res, await core.updateInvite(m[1], u.searchParams.get('key'), await readBody(req)));
    }
    if (p === '/api/media' && req.method === 'POST') return out(res, await core.uploadMedia(await readBody(req)));
    if ((m = p.match(/^\/api\/media\/([A-Za-z0-9_-]+)$/))) return out(res, await core.getMedia(m[1]));
    if ((m = p.match(/^\/api\/rsvp\/([a-z0-9-]+)$/)) && req.method === 'POST') return out(res, await core.addRsvp(m[1], await readBody(req)));
    if ((m = p.match(/^\/api\/rsvps\/([a-z0-9-]+)$/))) return out(res, await core.listRsvps(m[1], u.searchParams.get('key')));
    if ((m = p.match(/^\/(?:api\/)?i\/([a-z0-9-]+)\/?$/))) return out(res, await core.render(m[1], origin));
    if (p.startsWith('/api/')) return out(res, core.json(404, { error: 'Not found' }));

    // static files
    let f = path.normalize(path.join(ROOT, p));
    if (!f.startsWith(ROOT) || /[\\/](api|\.data|node_modules)([\\/]|$)/.test(f.slice(ROOT.length))) return out(res, { status: 404, body: 'Not found' });
    if (fs.existsSync(f) && fs.statSync(f).isDirectory()) f = path.join(f, 'index.html');
    if (!fs.existsSync(f)) { const h = f + '.html'; if (fs.existsSync(h)) f = h; else return out(res, { status: 404, headers: { 'Content-Type': 'text/html' }, body: fs.readFileSync(path.join(ROOT, '404.html')) }); }
    res.writeHead(200, { 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream' });
    fs.createReadStream(f).pipe(res);
  } catch (e) {
    console.error(e);
    out(res, core.json(500, { error: 'Something went wrong. Please try again.' }));
  }
}).listen(PORT, () => console.log(`Mangala running on http://localhost:${PORT} (storage: ${core.storeKind})`));
