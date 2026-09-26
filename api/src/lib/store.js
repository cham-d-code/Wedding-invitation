// Storage: Azure Blob Storage when a connection string is set, otherwise local files in ./.data
const fs = require('fs');
const path = require('path');

const CONN = process.env.STORAGE_CONNECTION || process.env.AzureWebJobsStorage || '';
const useBlob = CONN && !/UseDevelopmentStorage=true/.test(CONN) || process.env.FORCE_BLOB === '1';
const DATA_DIR = process.env.DATA_DIR || path.join(__dirname, '..', '..', '..', '.data');

let svc = null;
async function container(name) {
  if (!svc) { const { BlobServiceClient } = require('@azure/storage-blob'); svc = BlobServiceClient.fromConnectionString(CONN); }
  const c = svc.getContainerClient(name);
  await c.createIfNotExists();
  return c;
}
const streamToBuffer = async s => { const ch = []; for await (const d of s) ch.push(Buffer.isBuffer(d) ? d : Buffer.from(d)); return Buffer.concat(ch); };

const fileStore = {
  async put(bucket, key, buf, type) {
    const p = path.join(DATA_DIR, bucket, key);
    await fs.promises.mkdir(path.dirname(p), { recursive: true });
    await fs.promises.writeFile(p, buf);
    if (type) await fs.promises.writeFile(p + '.type', type);
  },
  async get(bucket, key) {
    const p = path.join(DATA_DIR, bucket, key);
    try {
      const buf = await fs.promises.readFile(p);
      let type = null; try { type = (await fs.promises.readFile(p + '.type')).toString(); } catch (_) {}
      return { buf, type };
    } catch (_) { return null; }
  },
  async list(bucket, prefix) {
    const dir = path.join(DATA_DIR, bucket, prefix);
    try { return (await fs.promises.readdir(dir)).filter(f => !f.endsWith('.type')).map(f => prefix + f); } catch (_) { return []; }
  },
};

const blobStore = {
  async put(bucket, key, buf, type) {
    const c = await container(bucket);
    await c.getBlockBlobClient(key).uploadData(buf, { blobHTTPHeaders: { blobContentType: type || 'application/json' } });
  },
  async get(bucket, key) {
    const c = await container(bucket);
    const b = c.getBlobClient(key);
    try { const r = await b.download(); return { buf: await streamToBuffer(r.readableStreamBody), type: r.contentType }; }
    catch (e) { if (e.statusCode === 404) return null; throw e; }
  },
  async list(bucket, prefix) {
    const c = await container(bucket); const out = [];
    for await (const b of c.listBlobsFlat({ prefix })) out.push(b.name);
    return out;
  },
};

module.exports = useBlob ? blobStore : fileStore;
module.exports.kind = useBlob ? 'blob' : 'file';
