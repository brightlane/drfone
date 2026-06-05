# DrFoneGuide — Affiliate Site Builder

Static site generator for **https://brightlane.github.io/drfone/**  
Affiliate programme: Wondershare DrFone via LinkConnector

---

## Quick Start

```bash
python3 build.py
```

Output lands in `./dist/`. No dependencies — pure Python 3 standard library only.

---

## Deployment (GitHub Pages)

### Option A — Deploy from `docs/` folder (simplest)

```bash
python3 build.py
cp -r dist/* docs/
git add docs/
git commit -m "build: regenerate site"
git push
```

In your repo → **Settings → Pages → Source → Deploy from branch → `main` → `/docs`**

### Option B — Deploy from `gh-pages` branch

```bash
python3 build.py

# First time only — create orphan gh-pages branch
git checkout --orphan gh-pages
git rm -rf .

# Copy dist contents
cp -r dist/. .
git add .
git commit -m "initial deploy"
git push origin gh-pages
git checkout main

# Subsequent deploys
python3 build.py
git checkout gh-pages
cp -r dist/. .
git add .
git commit -m "build: update"
git push origin gh-pages
git checkout main
```

### Option C — GitHub Actions (automatic on push)

Create `.github/workflows/deploy.yml`:

```yaml
name: Build & Deploy

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run build
        run: python3 build.py

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
```

Every push to `main` will rebuild and redeploy automatically.

---

## Project Structure

```
.
├── build.py          ← single source of truth — run this
├── README.md         ← this file
└── dist/             ← generated output (do not edit manually)
    ├── index.html
    ├── data-recovery.html
    ├── ios-repair.html
    ├── android-repair.html
    ├── phone-transfer.html
    ├── whatsapp-transfer.html
    ├── screen-unlock.html
    ├── virtual-location.html
    ├── data-eraser.html
    ├── backup-restore.html
    ├── iphone-guide.html
    ├── android-guide.html
    ├── whatsapp-guide.html
    ├── unlock-guide.html
    ├── review.html
    ├── vs-competitors.html
    ├── pricing.html
    ├── ios-support.html
    ├── android-support.html
    ├── faq.html
    ├── about.html
    ├── contact.html
    ├── 404.html
    ├── sitemap.xml
    ├── robots.txt
    ├── llms.txt
    ├── humans.txt
    ├── .nojekyll
    └── assets/
        └── style.css
```

---

## Configuration

All global settings are at the top of `build.py`:

```python
BASE_URL  = "https://brightlane.github.io/drfone"   # canonical domain
BASE_PATH = "/drfone"                                 # subdirectory path
AFFILIATE = "https://www.linkconnector.com/ta.php?lc=007949070197004532&atid=drfoneweb"
```

Change `BASE_URL` and `BASE_PATH` if you ever move to a custom domain (e.g. `drfoneguide.com`).

---

## Adding a New Page

1. Add an entry to the `PAGES` list in `build.py`:

```python
("my-new-page", "Page Title", "Meta description here.", "feature"),
```

2. Add content logic in the `build()` function under the matching template key (`feature`, `guide`, `review`, etc.)

3. Run `python3 build.py`

Available template types:

| Key | Used for |
|-----|----------|
| `home` | Landing page |
| `feature` | Individual DrFone tool pages |
| `guide` | Step-by-step how-to articles |
| `review` | Expert review with ratings table |
| `compare` | Competitor comparison table |
| `pricing` | Pricing cards |
| `support` | Device compatibility lists |
| `faq` | Accordion FAQ |
| `about` | About / disclosure |
| `contact` | Contact page |
| `404` | Error page |

---

## SEO Features

Every page includes:

- Unique `<title>` and `<meta name="description">`
- `<link rel="canonical">` pointing to `brightlane.github.io/drfone/`
- Open Graph tags (`og:title`, `og:description`, `og:url`, `og:type`)
- Twitter Card tags
- `hreflang="en"` + `hreflang="x-default"` for global targeting
- JSON-LD Schema.org `WebPage` structured data
- `lastmod` date auto-updated on every build

**sitemap.xml** — all pages with:
- Priority: `1.0` (home), `0.9` (features/guides), `0.8` (info pages)
- `changefreq: monthly`
- `lastmod` set to build date

**robots.txt** — allows all crawlers, references sitemap.

**llms.txt** — [llmstxt.org](https://llmstxt.org) standard. Helps AI assistants (ChatGPT, Perplexity, Claude) understand and correctly cite your site.

---

## Affiliate Links

Every `Get DrFone` / `Download DrFone` / `Try DrFone` button uses:

```
https://www.linkconnector.com/ta.php?lc=007949070197004532&atid=drfoneweb
```

All affiliate links have `rel="nofollow sponsored"` and `target="_blank"` applied automatically.

The affiliate disclosure appears in the footer of every page and on the About page.

---

## Customisation Tips

**Change the colour scheme** — edit CSS variables at the top of `GLOBAL_CSS`:
```python
--primary: #0A2540;   # dark navy
--accent:  #00C6A2;   # teal green
--accent2: #FF6B35;   # orange
```

**Update testimonials** — edit the `TESTIMONIALS` list (6 items, shown on every feature page).

**Add a blog/news section** — add a `"blog"` template type and a loop that reads from a `posts/` directory of markdown files.

**Custom domain** — add a `CNAME` file to `dist/`:
```python
write(f"{DIST}/CNAME", "yourdomain.com")
```
Then update `BASE_URL` and `BASE_PATH = ""`.

---

## Requirements

- Python 3.6+
- No third-party packages
- Internet connection only needed at runtime (Google Fonts loaded via CDN in browser)

---

## Licence

This build script is provided for personal affiliate use.  
DrFone and Wondershare are trademarks of Wondershare Technology Co., Ltd.  
This site is not affiliated with or endorsed by Wondershare.
