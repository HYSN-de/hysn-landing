"""404 page (404.html at the root). Cloudflare Workers serves it for every address that does not exist, at any depth,
so it uses absolute links (rel="/")."""
from _lib import *


def body(rel):
    links = [("Content Creation", "leistungen/content-creation/"), ("Installation & Montage", "leistungen/installation-montage/"),
             ("Wartung & Betrieb", "leistungen/wartung-betrieb/"), ("DOOH & hyads", "leistungen/dooh-hyads/"),
             ("Referenzen", "referenzen/"), ("Partnerprogramm", "partnerprogramm/"), ("Häufige Fragen", "faq/"), ("Kontakt", "kontakt/")]
    links_html = "".join(f'<li>{tlink(rel + h, H.escape(l), extra=" tlink--plain")}</li>' for l, h in links)
    return f"""
<section class="sec nf"><div class="wrap">
  <div class="sec-head">
    <span class="eyebrow">Fehler 404</span>
    <h1>Diese Seite gibt es nicht.</h1>
    <p class="lead">Vielleicht hat sich die Adresse geändert oder sie enthält einen Tippfehler. Von hier aus finden Sie schnell weiter.</p>
  </div>
  <div class="nf-actions">{btn(rel, "Zur Startseite")}{btn(rel + "kontakt/", "Kontakt aufnehmen", ghost=True)}</div>
  <ul class="nf-links">{links_html}</ul>
</div></section>"""


PAGES = [dict(path="404.html", title="Seite nicht gefunden | HYSN", desc="Diese Seite gibt es nicht. Hier finden Sie weiter zu den Leistungen, Referenzen und zum Kontakt von HYSN.",
              current="", body=body, css=["pages/notfound.css"], rel="/")]
