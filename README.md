# Mangala — digital wedding invitations

A complete website for selling animated digital wedding invitations in Sri Lanka.

| Page | What it does |
|---|---|
| `index.html` | Home page: features, how it works, designs, music samples, pricing, FAQ |
| `templates.html` | All 25 live designs with filters (Premium, Traditional, Hindu, Muslim, Catholic, Luxury, Floral, Modern) |
| `create.html` | Editor: pick a design, fill in details, events, story, photos and music with a live phone preview. Publish to get a link, or download a single HTML file |
| `dashboard.html` | The couple's private page: RSVPs, totals per event, spreadsheet download, personal guest links with WhatsApp buttons, edit link |
| `/i/<names>` | The published invitation, e.g. `yourdomain.lk/i/kasun-dilini`, with the couple's names and date in the WhatsApp link preview |

## 1. Change your brand, contacts and prices
Edit `assets/config.js` (brand name, WhatsApp number, email, plan prices and features).
The footer line shown inside invitations is in `api/src/lib/site.json`.

## 2. Run it on your computer
Needs Node.js 18 or newer. No install step.
```bash
node server.js
# open http://localhost:8080
```
Invitations, photos and RSVPs are saved in the `.data` folder.

## 3. Deploy to Azure (recommended)
Uses **Azure Static Web Apps** (site + Functions API) and a **Storage account** (Blob) for invitations, photos and RSVPs.

1. Create a Storage account (Standard, LRS is fine). Copy its connection string.
2. Push this folder to a GitHub repository.
3. In the Azure portal create a **Static Web App** → link the repo → Build preset *Custom* →
   App location `/`, API location `api`, Output location *(empty)*.
   (Or use the included workflow in `.github/workflows` with the deployment token as the
   `AZURE_STATIC_WEB_APPS_API_TOKEN` secret.)
4. Static Web App → **Environment variables** → add `STORAGE_CONNECTION` = your connection string.
5. Add your custom domain under **Custom domains**.

Containers `invites`, `media` and `rsvps` are created automatically on first use.

After deploying, publish a test invitation and open its `/i/...` link. If it shows "Invitation not found",
set `invitePath: "/api/i/"` in `assets/config.js` (both link styles are served by the API).

### Other hosting
- **Any VPS / Azure App Service / Render / Railway:** run `node server.js` (set `PORT`). Set `STORAGE_CONNECTION` to use Blob Storage,
  otherwise data is kept in `.data` on the server's disk (back it up). For Blob Storage run `npm install @azure/storage-blob` in `api/` first.
- **Static only (no server):** the site still works for browsing and designing, and customers can download their invitation as a file,
  but publishing links and RSVP collection need the API.

## API
| Method | Path | Purpose |
|---|---|---|
| POST | `/api/invites` | Create `{template, data}` → `{slug, key}` |
| GET / PUT | `/api/invites/{slug}?key=` | Load / update (needs the private key) |
| GET | `/i/{slug}` or `/api/i/{slug}` | Rendered invitation |
| POST | `/api/rsvp/{slug}` | Guest RSVP |
| GET | `/api/rsvps/{slug}?key=` | RSVP list for the dashboard |
| POST | `/api/media` · GET `/api/media/{id}` | Photo (≤2 MB) / MP3 (≤8 MB) upload and download |

The private key is stored hashed (SHA-256). Anyone holding the dashboard link can see RSVPs and edit, so couples should keep it private.

## Editing or adding designs
The designs are generated from Python in `tools/template-builder` — see its README.
Every template reads its details from one `WEDDING` block between `/*WEDDING*/ … /*END*/` markers; the server swaps in each couple's details.

## Not built yet (worth adding before scaling)
- **Payments and plan limits.** Anyone can publish for free today; the pricing is shown but not enforced. Add a `paid` flag per invite
  (e.g. show a small "preview" banner until you mark it paid) and a payment link (PayHere, Stripe or bank transfer).
- **Admin page** to list, mark paid and delete invitations (for now use Azure Storage Explorer).
- **Abuse protection:** rate limiting and a size quota per IP on `/api/media` and `/api/invites` (e.g. Azure Front Door WAF rules).
- **Expiry:** invitations don't expire yet; a timer-triggered Function can remove old ones based on the plan.
- **Share image:** the WhatsApp preview uses the couple photo when there is one; a generated card image per design would look better.

## Content notes
- Sample couples, parents and venues in the designs are placeholders.
- Check the Sinhala, Tamil and Arabic lines and the quoted verses with native speakers before launch.
- The built-in music is generated live in the browser (no audio files). Couples can upload an MP3 they have the rights to.
