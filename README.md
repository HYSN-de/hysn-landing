# HYSN Landing Page

Standalone one-page website. Plain HTML, CSS and JS: no build step, no server code, no external services.

## Before going live
   (street address, managing director, phone, VAT ID, hosting provider, log retention days).
2. If the domain is not `hysn.de`, replace `https://hysn.de` in `index.html`, `robots.txt` and `sitemap.xml`.

## Deploy
Upload the whole folder so `index.html` sits at the web root. Works on any static host:
- Netlify: drag and drop this folder at app.netlify.com/drop
- Vercel: `vercel deploy` inside this folder
- Classic hosting (IONOS, Strato, all-inkl): upload via FTP into the web root (`/`)

## Files
- `index.html`: the landing page
- `assets/css/hysn-light.css`: HYSN theme (colors in the `:root` block)
- `assets/css/main.css`, `assets/js/main.js`: Bizox template styles and animations
- `assets/img/`: images and the HYSN logo

## Contact
All contact buttons open a pre-filled email to info@hysn.de. A contact form can be added later.
