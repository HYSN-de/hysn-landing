# HYSN site

Static German website for HYSN (RA Vision GmbH). No server code, no tracking, no external requests.

## Build and preview

```
python3 _build.py              # build every page
python3 _build.py faq          # build only pages/faq.py
python3 _serve.py               # preview without browser caching at http://localhost:8080/
```

## Deploy (Cloudflare Workers)

The repository is the website: the built HTML is committed, so Cloudflare needs no build step.
`wrangler.jsonc` serves this folder as static assets; `.assetsignore` keeps `pages/`, the `_*.py` scripts, this README and the config off the public site.
Unknown addresses get `404.html`; `/kontakt` redirects to `/kontakt/`.

1. Edit, run `python3 _build.py`, check with `python3 _serve.py`.
2. Commit and push to `main`. With Workers Builds connected to this repository, Cloudflare deploys every push
   (deploy command `npx wrangler deploy`, no build command). Without it: `npx wrangler deploy` from this folder.

## Structure

| Path | What it is |
|---|---|
| `_lib.py` | Company data (`SITE`), icons, buttons, shared header and footer, page wrapper |
| `wrangler.jsonc`, `.assetsignore` | Cloudflare Workers config and the files that must not be published |
| `pages/notfound.py` | `404.html` (absolute links, served at any depth) |
| `pages/<name>.py` | One module per page: `body(rel)` returns the page HTML, `PAGES` lists the output files |
| `assets/css/site.css` | Shared theme and components |
| `assets/css/pages/<name>.css` | Styles used by one page only |
| `assets/img/<name>/` | Reviewed generated images used by each page |
| `assets/img/image-manifest.json` | Current image dimensions, descriptions and content versions, applied to image tags during the build |
| `assets/js/site.js` | Header states, mobile menu, back-to-top, smooth scrolling, scroll reveals, heading word reveal, logo carousel, before/after slider, contact form that opens the mail program |
| `assets/js/vendor/lenis.js` | Smooth scrolling (Lenis 1.0.16, local copy from the landing page); off for touch and reduced motion |

Company data (address, phone, email, register) lives only in `SITE` in `_lib.py`.
Stylesheet and script links get a content version (`?v=…`) at build time, so rebuild after editing CSS or JS.

## Shared components in `site.css`

Markup examples for all of these are in `pages/kontakt.py`.

| Class | Use |
|---|---|
| `.wrap` | Page width container (full-width layout, 1840 px max) |
| `--sec-y`, `--sec-y-sm`, `--head-gap`, `--grid-gap`, `--card-pad`, `--stack` | Spacing scale. Use these instead of fixed pixel values so every page keeps one rhythm |
| `.sec`, `.sec--band` | Content section with the shared vertical padding; `--band` adds the pale background |
| `.sec-head`, `.sec-note` | Eyebrow + h2 + `.sub` above the content (spaced by `--head-gap`); small caption under it |
| `.split` | Heading column left, content right; stacks below 1180 px |
| `.facts` + `.fact` | Icon strip under a hero (any number of columns) |
| `.steps` | Numbered steps (`<ol>`, `.ring` icon, `b` number, `h3`, `p`) on a connecting line; any number |
| `.eyebrow`, `h1`, `h2`, `h3`, `.lead`, `.sub`, `.small` | Type scale |
| `.btn` / `btn(href, label)` | Black button with arrow |
| `.tlink` / `tlink(href, label)` | Underlined text link with arrow; `.tlink--plain` without underline |
| `.chero` | Photo hero: text left, photo right fading into white. Use with `body_class="hero-page"` so the header sits transparent on the photo |
| `.cform`, `.cside`, `.expect` | Form with sidebar |
| `.next` + `.flow` | Pale band with numbered steps on a connecting line |
| `.ways` + `.ways-grid` | Four columns with dividers, icon, label, value, text link |
| `.person` | Wide photo left, text panel right |
| `.place` | Text, Germany map (`MAP`), stacked words |
| `.qa` + `.faq` | Two-column FAQ with plus/minus accordion (`<details>`). site.js animates every `.faq`/`.faq-list` answer, keeps one answer open per section (per topic on the FAQ page; a search may show several) and holds the clicked question in place. Mark at most one answer `open` per section in the page module |
| `.cta` | Closing banner with the hysn.de ribbon (`RIBBON`), `.cta-text`, `.cta-brand` |
| `.legal` | Impressum and Datenschutz text |
| `.compare` | Before/after slider (drag, keyboard, one sweep on first view); markup in `pages/start.py` |
| `.logos` | Logo carousel (autoplay, arrows, pause, drag, grey to colour) |
| `.marquee` | Outlined words drifting sideways above the footer |

## Motion

The effects come from the hysn.de landing page and work on every page without per-page code:
button labels roll and arrows swap on hover (`_lib._motion()` adds `.btn-t`, `.i-arr`, `.i-down` at build time),
text links draw an ink underline, menu items get a growing underline, photo cards zoom (`.zoom`, set by site.js),
content blocks rise in while scrolling (card grids and lists one item after another), larger photos open like a curtain,
section headings brighten word by word, step lines draw in, hero photos settle, the closing ribbon drifts and the map dot pulses.
With `prefers-reduced-motion` nothing moves and nothing is hidden.

## Pages

Start (`index.html`, carried over from the hysn.de landing page), Kontakt, FAQ, Content Creation, Installation & Montage, Wartung & Betrieb, DOOH & hyads, Partnerprogramm, Referenzen, Impressum, Datenschutz.
Referenzen accepts a filter in the address (`referenzen/#gastro`, `#handel`, `#events`, `#kommunen`, `#buero`, `#franchise`); the start page links there.
Not built yet: Über uns (`ueber-uns/`; concept `Static pages/About.png`). Header and footer leave links to unbuilt pages out (`built()` in `_lib.py`, which also knows every page of the current build run), so the link appears as soon as `pages/ueber-uns.py` exists.

## Open items

- Datenschutz section 2 describes hosting on Cloudflare (Cloudflare's data processing agreement is part of its self-serve terms, free plan included). If hosting changes, update section 2. Section 4 says the site sets no cookies: do not switch on Cloudflare features that set cookies (Bot Fight Mode, challenges, Web Analytics with cookies) without updating it.
- The 90 concept crops were replaced on 9 October 2026. Thirteen large images remain below the original requested pixel dimensions; native files were preserved without upscaling. Review targets and delivery notes in the adjacent `Bilder-neu-erstellen` folder.
- When replacing an image, update its dimensions, description and SHA-256 content-version prefix in `assets/img/image-manifest.json`, then rebuild. The build writes matching attributes and versioned URLs into the pages.
