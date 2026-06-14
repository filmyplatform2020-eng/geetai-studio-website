# GeetAI Studio Website

Static marketing site for [GeetAI Studio](https://geetaistudio.com) — 30 AI-powered business tools.

## Structure

```
├── index.html          # Main landing page (Cloudflare Pages entry)
├── geetai.html         # Same as index.html (legacy filename)
├── tools/              # 30 individual tool pages
├── products/           # Vault source markdown (34-product catalog)
├── tool_descriptions.md # Gumroad + website copy blurbs
├── wrangler.toml       # Cloudflare Pages config
└── ASSETS_NEEDED.md    # Favicon + OG image checklist
```

## Local preview

```bash
cd geetai-studio-website
python3 -m http.server 8080
# Open http://localhost:8080
```

## Deploy to Cloudflare Pages

### Option A — Git integration (recommended)

1. Push this repo to GitHub (see below).
2. Cloudflare Dashboard → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**.
3. Select repo `geetai-studio-website`.
4. Build settings:
   - **Framework preset:** None
   - **Build command:** *(leave empty)*
   - **Build output directory:** `/` (root)
5. Deploy. Default URL: `geetai-studio.pages.dev`.
6. When domain is ready: **Custom domains** → add `geetaistudio.com` (DNS handled separately — do not touch until domain is purchased).

### Option B — Wrangler CLI (one-click deploy)

```bash
npm install -g wrangler   # or: npx wrangler
wrangler login
wrangler pages deploy . --project-name=geetai-studio
```

### Option C — Direct upload

Drag the project folder into Cloudflare Pages dashboard (no Git required).

## Regenerate tool pages

After editing tool metadata:

```bash
python3 scripts/generate_site.py
```

## GitHub setup

```bash
cd geetai-studio-website
git init
git add .
git commit -m "Initial GeetAI Studio website — landing page, 30 tool pages, products"
gh auth login   # if token expired
gh repo create geetai-studio-website --public --source=. --remote=origin --push
```

## Notes

- Favicon and OG image paths are configured; add actual files per `ASSETS_NEEDED.md`.
- Tool pages link to Gumroad (`aniketgai.gumroad.com`) for purchases.
- Do not commit credentials or `.env` files.
