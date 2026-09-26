// Azure Functions (Node.js v4 programming model) — thin wrappers around lib/core.js
const { app } = require('@azure/functions');
const core = require('../lib/core');

const origin = req => {
  const h = req.headers;
  const host = h.get('x-forwarded-host') || h.get('host');
  const proto = (h.get('x-forwarded-proto') || 'https').split(',')[0];
  return `${proto}://${host}`;
};
const body = async req => { try { return await req.json(); } catch (_) { return null; } };
const send = r => ({ status: r.status, headers: r.headers, body: r.body });
const wrap = fn => async (req, ctx) => {
  try { return send(await fn(req)); }
  catch (e) { ctx.error(e); return send(core.json(500, { error: 'Something went wrong. Please try again.' })); }
};

app.http('invitesCreate', { methods: ['POST'], authLevel: 'anonymous', route: 'invites',
  handler: wrap(async req => core.createInvite(await body(req))) });
app.http('invitesOne', { methods: ['GET', 'PUT'], authLevel: 'anonymous', route: 'invites/{slug}',
  handler: wrap(async req => req.method === 'GET'
    ? core.getInvite(req.params.slug, req.query.get('key'))
    : core.updateInvite(req.params.slug, req.query.get('key'), await body(req))) });
app.http('mediaUpload', { methods: ['POST'], authLevel: 'anonymous', route: 'media',
  handler: wrap(async req => core.uploadMedia(await body(req))) });
app.http('mediaGet', { methods: ['GET'], authLevel: 'anonymous', route: 'media/{id}',
  handler: wrap(async req => core.getMedia(req.params.id)) });
app.http('rsvpAdd', { methods: ['POST'], authLevel: 'anonymous', route: 'rsvp/{slug}',
  handler: wrap(async req => core.addRsvp(req.params.slug, await body(req))) });
app.http('rsvpList', { methods: ['GET'], authLevel: 'anonymous', route: 'rsvps/{slug}',
  handler: wrap(async req => core.listRsvps(req.params.slug, req.query.get('key'))) });
// /i/{slug} is rewritten here by staticwebapp.config.json; /api/i/{slug} also works directly
app.http('render', { methods: ['GET'], authLevel: 'anonymous', route: 'i/{slug?}',
  handler: wrap(async req => {
    let slug = req.params.slug;
    if (!slug) { const orig = req.headers.get('x-ms-original-url') || ''; slug = (orig.match(/\/i\/([a-z0-9-]+)/) || [])[1]; }
    return core.render(slug, origin(req));
  }) });
