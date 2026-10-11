"""HYSN site library: company data, icons, shared header/footer and the page wrapper.
Every page lives in pages/<name>.py and does `from _lib import *`. Build with: python3 _build.py [name ...]
Company data lives in SITE below (source: client's letterhead, email info@hysn.de)."""
import re, sys, pathlib, urllib.parse, html as H, json, hashlib
sys.dont_write_bytecode = True

ROOT = pathlib.Path(__file__).resolve().parent
IMAGE_META = json.loads((ROOT / "assets/img/image-manifest.json").read_text(encoding="utf-8"))
SITE = dict(
    company="RA Vision GmbH", street="Brunnenweg 19", zip="64331", city="Weiterstadt",
    phone="+49 6150 807 98 11", phone_href="+4961508079811",
    mobile="+49 151 44 300 333", mobile_href="+4915144300333",
    email="info@hysn.de", court="Amtsgericht Darmstadt", hrb="HRB 109713",
    md="Raqeeb Khan", vat="DE361573242",
)
S = {k: H.escape(v) for k, v in SITE.items()}

ICONS = {
 "phone":  '<path d="M6.6 3.8h2.8l1.4 4-2 1.3a10.6 10.6 0 0 0 6.1 6.1l1.3-2 4 1.4v2.8a2 2 0 0 1-2.1 2A15.4 15.4 0 0 1 4.6 5.9a2 2 0 0 1 2-2.1z"/>',
 "mail":   '<rect x="3.4" y="5.4" width="17.2" height="13.2" rx="1.4"/><path d="m4 6.6 8 6.4 8-6.4"/>',
 "pin":    '<path d="M12 21s-6.5-6.1-6.5-11.2a6.5 6.5 0 0 1 13 0C18.5 14.9 12 21 12 21z"/><circle cx="12" cy="9.8" r="2.3"/>',
 "chat":   '<path d="M5 4.8h14a1.6 1.6 0 0 1 1.6 1.6v8.6a1.6 1.6 0 0 1-1.6 1.6h-8.4L6 20.2v-3.6H5A1.6 1.6 0 0 1 3.4 15V6.4A1.6 1.6 0 0 1 5 4.8z"/><path d="M7.8 9.4h8.4M7.8 12.4h5.4"/>',
 "hand":   '<path d="M8 12.5V6.8a1.4 1.4 0 0 1 2.8 0v4.7M10.8 11V5.4a1.4 1.4 0 0 1 2.8 0V11M13.6 11V6.4a1.4 1.4 0 0 1 2.8 0v6.8"/><path d="M16.4 10.2a1.4 1.4 0 0 1 2.8 0v3.6a6.6 6.6 0 0 1-6.6 6.6h-.6a6 6 0 0 1-4.8-2.4L4.7 14.6a1.4 1.4 0 0 1 2.1-1.8L8 14"/>',
 "one":    '<circle cx="12" cy="12" r="8.6"/><path d="m8.2 12.3 2.6 2.6 5.1-5.4"/>',
 "clock":  '<circle cx="12" cy="12" r="8.6"/><path d="M12 7.2V12l3.2 2"/>',
 "people": '<circle cx="12" cy="7.4" r="2.6"/><circle cx="5.8" cy="9.2" r="2.1"/><circle cx="18.2" cy="9.2" r="2.1"/><path d="M7.6 18.6v-1.4a4.4 4.4 0 0 1 8.8 0v1.4M2.6 17.6v-.8a3.2 3.2 0 0 1 4.6-2.9M21.4 17.6v-.8a3.2 3.2 0 0 0-4.6-2.9"/>',
 "cube":   '<path d="M12 3 20 7.5v9L12 21l-8-4.5v-9z"/><path d="m4 7.5 8 4.5 8-4.5M12 12v9"/>',
 "pencil": '<path d="m15.5 4.5 4 4L9 19H5v-4z"/><path d="m13.5 6.5 4 4"/>',
 "doc":    '<path d="M6.4 3.4h7.8l4 4v13.2H6.4z"/><path d="M14.2 3.4v4h4M9.2 12h5.6M9.2 15h5.6M9.2 18h3.4"/>',
 "camera": '<path d="M4 7.6h3.2l1.6-2.4h6.4l1.6 2.4H20a1 1 0 0 1 1 1v9.8a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V8.6a1 1 0 0 1 1-1z"/><circle cx="12" cy="13" r="3.6"/>',
 "cal":    '<rect x="3.6" y="5" width="16.8" height="15.4" rx="1.2"/><path d="M3.6 9.6h16.8M8 3.2v3.6M16 3.2v3.6"/>',
 "down":   '<path d="M12 4v15M6 13l6 6 6-6"/>',
}
ico = lambda n, cls="ico": f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICONS[n]}</svg>'
# icon(): a shared icon by name, or raw SVG markup on the 24x24 grid (use this for page-specific icons; never edit ICONS from a page)
icon = lambda n, cls="ico": f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICONS.get(n, n)}</svg>'
# mailto(): a mail link to info@hysn.de with a prepared subject line
mailto = lambda subject: "mailto:" + SITE["email"] + "?subject=" + urllib.parse.quote(subject)
ARROW = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4"/></svg>'
btn = lambda href, label, ghost=False: f'<a class="btn{" btn--ghost" if ghost else ""}" href="{href}">{label}{ARROW}</a>'
tlink = lambda href, label, icon=None, extra="": (f'<a class="tlink{extra}" href="{href}">{label}'
                                                + (f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[icon]}</svg>' if icon else ARROW) + '</a>')

NAV = [("Start", "index.html"), ("Über uns", "ueber-uns/"),
       ("Leistungen", None, [("Content Creation", "leistungen/content-creation/"), ("Installation & Montage", "leistungen/installation-montage/"),
                             ("Wartung & Betrieb", "leistungen/wartung-betrieb/"), ("DOOH & hyads", "leistungen/dooh-hyads/")]),
       ("Referenzen", "referenzen/"), ("Partnerprogramm", "partnerprogramm/"), ("Kontakt", "kontakt/")]

# built(): whether a link target exists or is being built in this run (_build.py fills PLANNED);
# links to unbuilt pages (Über uns) are left out until those pages exist
PLANNED = set()
def built(href):
    target = href + "index.html" if href.endswith("/") else href
    return target in PLANNED or (ROOT / target).exists()

def home(rel, cls=""):
    """The logo, linked to the start page once it exists."""
    img = f'<img src="{rel}assets/img/logo/hysn-logo.svg" alt="HYSN" width="1485" height="234">'
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{rel}index.html" aria-label="HYSN Startseite">{img}</a>' if built("index.html") else f'<span{c}>{img}</span>'

def header(rel, current):
    def link(label, href):
        cur = ' aria-current="page"' if href == current else ""
        return f'<a href="{rel}{href}"{cur}>{H.escape(label)}</a>'
    items, mobile = "", ""
    for item in NAV:
        if len(item) == 2 and not built(item[1]):
            continue
        if len(item) == 3:
            sub = "".join(f"<li>{link(l, h)}</li>" for l, h in item[2])
            cur = ' class="is-cur"' if any(h == current for _, h in item[2]) else ""
            items += f'<li class="has-sub"><a href="{rel}{item[2][0][1]}"{cur}>{item[0]}</a><ul class="sub-menu">{sub}</ul></li>'
            mobile += f'<li class="mgroup">{item[0]}</li>' + "".join(f'<li class="sub-list">{link(l, h)}</li>' for l, h in item[2])
        else:
            items += f"<li>{link(*item)}</li>"; mobile += f"<li>{link(*item)}</li>"
    return f"""<a class="skip" href="#inhalt">Zum Inhalt springen</a>
<header class="top"><div class="wrap">
  {home(rel, "logo")}
  <nav class="nav" aria-label="Hauptnavigation"><ul>{items}</ul>{btn(rel + "kontakt/#anfrage", "Erstgespräch anfragen")}</nav>
  <details class="mnav"><summary aria-label="Menü"><svg class="ico ico-bars" viewBox="0 0 24 24"><path d="M3 7h18M3 12h18M3 17h18"/></svg><svg class="ico ico-x" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6 6 18"/></svg></summary>
    <div class="mpanel" data-lenis-prevent><ul>{mobile}</ul>{btn(rel + "kontakt/#anfrage", "Erstgespräch anfragen")}</div></details>
</div></header>"""

def footer(rel):
    links = [("Start", "index.html"), ("Über uns", "ueber-uns/"), ("Leistungen", "leistungen/content-creation/"),
             ("Referenzen", "referenzen/"), ("Partnerprogramm", "partnerprogramm/"), ("FAQ", "faq/"), ("Kontakt", "kontakt/")]
    nav = "".join(f'<li><a href="{rel}{h}">{l}</a></li>' for l, h in links if built(h))
    return f"""<footer class="foot"><div class="wrap">
  <div class="foot-row">
    <div class="foot-brand">{home(rel)}<span>Eine Marke der {S["company"]}.</span></div>
    <nav aria-label="Footer"><ul>{nav}</ul></nav>
  </div>
  <div class="foot-legal"><span>© 2026 {S["company"]} · {S["street"]}, {S["zip"]} {S["city"]} · {S["court"]} {S["hrb"]}</span>
    <ul><li><a href="{rel}datenschutz/">Datenschutz</a></li><li><a href="{rel}impressum/">Impressum</a></li><li><a href="{rel}kontakt/">Kontakt</a></li></ul></div>
</div></footer>"""

def _lines(m):
    """Wrap each <br>-separated line of an h1/h2 in a span, so phones can balance every line on its own."""
    tag, attrs, inner = m.group(1), m.group(2), m.group(3)
    parts = re.split(r"<br\s*/?>", inner)
    if len(parts) < 2:
        return m.group(0)
    for part in parts:  # leave headings alone where a tag spans a line break
        if len(re.findall(r"<(?!/|br)[a-z][^>]*(?<!/)>", part)) != len(re.findall(r"</[a-z][^>]*>", part)):
            return m.group(0)
    return f"<{tag}{attrs}>" + "<br>".join(f'<span class="ln">{x}</span>' for x in parts) + f"</{tag}>"

def _image_tag(match):
    """Apply current image descriptions, native dimensions and cache versions."""
    tag = match.group(0)
    src = re.search(r'\bsrc="([^"]*)"', tag)
    if not src:
        return tag
    url = urllib.parse.urlsplit(H.unescape(src.group(1)))
    if url.scheme or url.netloc:
        return tag
    meta = IMAGE_META.get(url.path.lstrip("./"))
    if not meta:
        return tag
    query = dict(urllib.parse.parse_qsl(url.query, keep_blank_values=True))
    query["v"] = meta["version"]
    updates = dict(src=urllib.parse.urlunsplit(url._replace(query=urllib.parse.urlencode(query))),
                   width=meta["width"], height=meta["height"], alt=meta["alt"])
    for name, value in updates.items():
        attr = f'{name}="{H.escape(str(value), quote=True)}"'
        pattern = rf'\b{name}="[^"]*"'
        if re.search(pattern, tag):
            tag = re.sub(pattern, lambda m: attr, tag, count=1)
        else:
            tag = re.sub(r'(\s*/?>)$', lambda m: " " + attr + m.group(1), tag)
    return tag


def _btn_label(m):
    """Wrap a button label so it can roll up to a copy of itself on hover (site.css .btn-t)."""
    open_tag, label, svg, close = m.group(1), m.group(3), m.group(4), m.group(5)
    if "<" in label or not label.strip():
        return m.group(0)
    text = label.strip()
    return f'{open_tag}<span class="btn-t"><span data-t="{text}">{text}</span></span>{svg}{close}'

def _motion(out):
    """Markup hooks for the shared hover effects: button labels, arrow icons, map pulse."""
    out = re.sub(r'(<(a|button)\b[^>]*\bclass="btn\b[^"]*"[^>]*>)(.*?)(<svg\b.*?</svg>)\s*(</\2>)', _btn_label, out, flags=re.S)
    out = re.sub(r'<svg(?![^>]*\bclass=)([^>]*)>(?=<path d="M2 8h11M9 4l4 4-4 4"/>)', r'<svg class="i-arr"\1>', out)
    out = re.sub(r'<svg(?![^>]*\bclass=)([^>]*)>(?=<path d="M12 4v15M6 13l6 6 6-6"/>)', r'<svg class="i-down"\1>', out)
    out = re.sub(r'<circle class="dot" cx="([\d.]+)" cy="([\d.]+)" r="[\d.]+"/>', lambda m: f'<circle class="pulse" cx="{m.group(1)}" cy="{m.group(2)}" r="8"/>' + m.group(0), out)
    return out

def _asset_version(m):
    """Stylesheets and scripts get a content version in their URL, so a browser never pairs a new page with an old cached file."""
    url = m.group(2)
    f = ROOT / url[url.index("assets/"):]
    return f'{m.group(1)}="{url}?v={hashlib.sha256(f.read_bytes()).hexdigest()[:10]}"' if f.exists() else m.group(0)

def page(path, title, desc, current, body, body_class="", css=(), rel=None):
    # rel: prefix for site links; "/" makes them absolute (the 404 page is served at any depth)
    rel = ("../" * (len(pathlib.PurePosixPath(path).parts) - 1)) if rel is None else rel
    out = f"""<!doctype html>
<html lang="de"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{H.escape(title)}</title><meta name="description" content="{H.escape(desc)}">
<link rel="icon" href="{rel}assets/img/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{rel}assets/css/site.css">{"".join(f'<link rel="stylesheet" href="{rel}assets/css/{c}">' for c in css)}
</head><body{(' class="' + body_class + '"') if body_class else ""}>
{header(rel, current)}
<main id="inhalt">
{body(rel)}
</main>
{footer(rel)}
<script src="{rel}assets/js/vendor/lenis.js" defer></script>
<script src="{rel}assets/js/site.js" defer></script>
</body></html>
"""
    out = re.sub(r"<img\b[^>]*>", _image_tag, out)
    out = _motion(out)
    out = re.sub(r'(href|src)="([^"?#]*assets/(?:css|js)/[^"?#]+\.(?:css|js))"', _asset_version, out)
    out = re.sub(r"<(h[12])([^>]*)>(.*?)</\1>", _lines, out, flags=re.S)
    out = re.sub(r"(\d) (%|€)", "\\1\u00a0\\2", out)  # keep "10 %" and "99 €" on one line
    f = ROOT / path; f.parent.mkdir(parents=True, exist_ok=True); f.write_text(out, encoding="utf-8"); print("wrote", path)

MAP = (ROOT / "assets/img/deutschland-path.txt").read_text()
RIBBON = (ROOT / "assets/img/ribbon.svg.txt").read_text().replace('class="hy-ribbon"', 'class="ribbon"')
