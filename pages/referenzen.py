"""Referenzen: layout follows Static pages/hysn-case-studies-references-concept-v1 1.png.
Real references only (Haus des Döners, hyads screens in the REWE/EDEKA environment); the concept's
project tiles are shown as visualised use cases ("Einsatzmöglichkeiten"), never as completed projects."""
from _lib import *

# page-specific line icons on the 24x24 grid
I_STELE = '<rect x="7.2" y="2.8" width="9.6" height="15.2" rx="1"/><path d="M12 18v3.2M8.6 21.2h6.8M9.6 6.4h4.8M9.6 9.2h3"/>'
I_BOARDS = '<path d="M5.4 3v3.4M18.6 3v3.4"/><rect x="2.4" y="6.4" width="5.9" height="5" rx=".5"/><rect x="9.05" y="6.4" width="5.9" height="5" rx=".5"/><rect x="15.7" y="6.4" width="5.9" height="5" rx=".5"/><path d="M2.4 18h19.2M4.6 18v3M19.4 18v3"/>'
I_SHIELD = '<path d="M12 3.2 19 6v5.6c0 4.4-3 7.9-7 9.2-4-1.3-7-4.8-7-9.2V6z"/><path d="m8.9 12.1 2.2 2.2 4.1-4.4"/>'
I_SCREEN = '<rect x="3" y="4.6" width="18" height="11.8" rx="1"/><path d="M12 16.4v3.4M8.4 20h7.2"/>'
I_IMAGE = '<rect x="3.4" y="4.6" width="17.2" height="14.8" rx="1.2"/><path d="m3.8 16.6 4.8-4.8 3.8 3.8 2.6-2.6 5.2 5.2"/><circle cx="15.4" cy="9.2" r="1.6"/>'
I_ROOM = '<path d="M3 20.6h18M5.6 20.6V3.6h12.8v17"/><path d="M9.4 20.6v-6.2h5.2v6.2"/><path d="M8.6 7.4h2.4M13 7.4h2.4M8.6 10.6h2.4M13 10.6h2.4"/>'
I_MOUNT = '<rect x="5.4" y="6.6" width="13.2" height="8.6" rx=".8"/><path d="M3 3.4v17.2M3 9.2h2.4M3 12.6h2.4M12 15.2v2.6M9.4 20.6h5.2"/>'
I_CONTENT = '<rect x="3" y="4.6" width="18" height="11.8" rx="1"/><path d="M6.4 8.4h5.2M6.4 11.2h3.6"/><rect x="13.4" y="7.6" width="4.4" height="5.4" rx=".5"/><path d="M12 16.4v3.4M8.4 20h7.2"/>'


def body(rel):
    down = f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v15M6 13l6 6 6-6"/></svg>'

    proof = [
        (I_STELE, "30+ Werbescreens", "Aktiv im REWE- und EDEKA-Umfeld, im hyads-Netzwerk mit lokalen Werbekunden."),
        (I_BOARDS, "Haus des Döners seit Juni\u00a02025", "Drei digitale Menüboards an einem Standort, täglich im Betrieb."),
        (I_SHIELD, "Alles aus einer Hand", "Beratung, Hardware, Content, Montage und Betrieb, mit 5 Jahren Garantie auf die Hardware."),
    ]
    proof_html = "".join(f'<div class="rf-proof-item">{icon(i)}<div><h3>{t}</h3><p>{p}</p></div></div>' for i, t, p in proof)

    steps = [
        ("Ausgangslage", "Sie zeigen uns Ihre Fläche und sagen, was die Screens leisten sollen."),
        ("Gestaltung", "Klare Kategorien, Preise und Food-Bilder. Den Content erstellen wir."),
        ("Montage", "Displays, Halterungen und Kabelwege, sauber an Ihrem Standort montiert."),
        ("Betrieb", "Änderungen per Nachricht, ohne Schulung. 5 Jahre Garantie auf die Hardware."),
    ]
    steps_html = "".join(f'<li><b>{i:02d}</b><h3>{t}</h3><p>{p}</p></li>' for i, (t, p) in enumerate(steps, 1))

    seq = [("ablauf-vorher.jpg", 268, "Vorher", "Gedruckte Menütafeln über einer Theke"),
           ("ablauf-montage.jpg", 264, "Montage", "Drei montierte, noch ausgeschaltete Displays über der Theke"),
           ("ablauf-fertig.jpg", 264, "Im Betrieb", "Drei digitale Menüboards mit Speisen und Preisen"),
           ("ablauf-content.jpg", 277, "Im Detail", "Nahaufnahme eines Menüboards mit Food-Bild")]
    arrow = '<svg class="rf-seq-arrow" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4"/></svg>'
    seq_html = arrow.join(f'<figure><img src="{rel}assets/img/referenzen/{f}" alt="Visualisierung: {H.escape(a)}" width="{w}" height="204" loading="lazy"><figcaption>{c}</figcaption></figure>'
                          for f, w, c, a in seq)

    tabs = [("alle", "Alle"), ("gastro", "Gastronomie"), ("handel", "Handel"), ("events", "Events"),
            ("kommunen", "Kommunen"), ("buero", "Büro"), ("franchise", "Franchise")]
    tabs_html = "".join(f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k == "alle" else "false"}">{l}</button>' for k, l in tabs)

    # (categories for the filter, label, image, w, h, alt, title, text, link, link label)
    uses = [
        ("handel", "Handel", "einsatz-eingang.jpg", 566, 328, "Hochformat-Werbestele im gläsernen Eingangsbereich eines Marktes",
         "Werbestele im Eingangsbereich", "Lokale Werbung dort, wo jeder Kunde vorbeikommt.", "leistungen/dooh-hyads/", "Zum hyads-Netzwerk"),
        ("handel", "Handel", "einsatz-markt.jpg", 554, 328, "Hochformat-Screen mit Obstmotiv neben der Obst- und Gemüseabteilung",
         "Screen im Verkaufsraum", "Angebote und lokale Kampagnen in einer Playlist.", "leistungen/content-creation/", "Content erstellen lassen"),
        ("gastro", "Gastronomie", "einsatz-theke.jpg", 563, 328, "Drei Menüboards im Querformat über einer Restauranttheke",
         "Menüboards an der Theke", "Kategorien, Preise und Angebote klar gegliedert.", "#haus-des-doeners", "Zur Referenz Haus des Döners"),
        ("events", "Events", "einsatz-event.jpg", 566, 310, "Große LED-Wand auf einer Konferenzbühne vor Publikum",
         "LED-Wand für Bühne und Event", "Ein Blickfang für Bühneninhalte und Präsentationen.", "leistungen/installation-montage/", "Montage planen"),
        ("kommunen", "Kommunen", "einsatz-stadt.jpg", 554, 310, "Digitale Info-Stele auf einem Platz in der Innenstadt",
         "Info-Stele im Stadtraum", "Bürgerinformation und lokale Werbung auf einer Fläche.", "partnerprogramm/", "Modell für Städte ansehen"),
        ("buero", "Büro", "einsatz-buero.jpg", 563, 310, "Besprechungsraum mit großem interaktivem Display",
         "Display im Besprechungsraum", "Präsentieren, markieren und gemeinsam arbeiten.", "kontakt/#anfrage", "Beratung anfragen"),
        ("franchise gastro", "Franchise", "einsatz-filialen.jpg", 441, 296, "Digitale Menüboards mit Speisen über einer Theke",
         "Menüboards für Filialbetriebe", "Ein einheitliches Design, Preise je Filiale anpassbar.", "leistungen/content-creation/", "Content für Filialen ansehen"),
        ("handel kommunen", "Handel · Kommunen", "einsatz-fassade.jpg", 554, 315, "Großer LED-Screen an der Fassade eines Geschäftshauses",
         "LED-Fläche an der Fassade", "Eine Werbefläche, abgestimmt auf Gebäude und Umfeld.", "leistungen/installation-montage/", "Installation & Montage"),
        ("handel buero", "Handel · Büro", "einsatz-showroom.jpg", 563, 315, "Videowand aus vier Displays in einem hellen Showroom",
         "Videowand im Showroom", "Eine große Fläche für Produkte und Markenbilder.", "leistungen/content-creation/", "Content für Videowände ansehen"),
    ]
    def use(c):
        cats, label, img, w, h, alt, title, text, href, lab = c
        href = href if href.startswith("#") else rel + href
        label = label.replace(" · ", " ·\u00a0")
        return (f'<article class="rf-card" data-cat="{cats}"><div class="rf-card-img"><img src="{rel}assets/img/referenzen/{img}" alt="Visualisierung: {H.escape(alt)}" width="{w}" height="{h}" loading="lazy"></div>'
                f'<div class="rf-card-body"><p class="rf-card-meta"><span>{label}</span><em>Visualisierung</em></p><h3>{title}</h3><p>{text}</p>{tlink(href, lab, extra=" tlink--plain")}</div></article>')
    uses_html = "".join(use(c) for c in uses)
    # only shown in the 2-column layout when an odd number of tiles is visible, so the last tile never stands alone
    uses_html += (f'<aside class="rf-more"><div class="rf-more-box"><span class="eyebrow">Ihr Standort</span><h3>Ihr Format ist nicht dabei?</h3>'
                  f'<p>Wir planen den passenden Screen für Ihren Standort mit Ihnen, von der Idee bis zur Montage.</p>{btn(rel + "kontakt/#anfrage", "Format besprechen")}</div></aside>')

    film = [(I_ROOM, "Der Raum"), (I_MOUNT, "Die Montage"), (I_CONTENT, "Der Content"), ("clock", "Der Alltag")]
    film_html = "".join(f'<li>{icon(i)}<span>{t}</span></li>' for i, t in film)

    return f"""
<section class="chero rf-hero">
  <div class="chero-img rf-hero-img">
    <div class="rf-hero-main"><img src="{rel}assets/img/referenzen/hero-foyer.jpg" alt="Visualisierung: Foyer mit großem Wanddisplay hinter dem Empfang" width="1120" height="391" fetchpriority="high"></div>
    <div class="rf-hero-row">
      <img src="{rel}assets/img/referenzen/hero-gastronomie.jpg" alt="Visualisierung: Restauranttheke mit drei Menüboards" width="516" height="259">
      <img src="{rel}assets/img/referenzen/hero-event.jpg" alt="Visualisierung: LED-Wand auf einer Eventbühne" width="536" height="259">
    </div>
    <span class="rf-tag rf-tag--hero">Visualisierungen</span>
  </div>
  <div class="wrap"><div class="chero-text">
    <span class="eyebrow">Referenzen</span>
    <h1>Räume, die<br>Menschen bewegen.</h1>
    <p class="lead">Eine echte Referenz aus der Gastronomie, dazu typische Einsätze von Menüboard bis LED-Wand. Finden Sie das Format für Ihren Standort.</p>
    <div class="actions"><a class="btn" href="#einsatz">Formate entdecken{down}</a>{btn(rel + "kontakt/#anfrage", "Ähnliches Projekt besprechen", ghost=True)}</div>
    <p class="note">{ico("chat")}Erstgespräch kostenlos und unverbindlich</p>
    <p class="note rf-note-vis">{icon(I_IMAGE)}Alle Bilder auf dieser Seite sind Visualisierungen, keine Kundenfotos.</p>
  </div></div>
</section>

<section class="rf-proof" aria-label="Fakten auf einen Blick"><h2 class="vh">Fakten auf einen Blick</h2><div class="wrap">{proof_html}</div></section>

<section class="rf-uses" id="einsatz"><div class="wrap">
  <span class="eyebrow">Einsatzmöglichkeiten</span>
  <h2>Finden Sie das Format,<br>das zu Ihrem Standort passt.</h2>
  <p class="sub">Typische Einsatzszenarien als Visualisierung, keine abgeschlossenen Projekte.</p>
  <div class="rf-filter" role="group" aria-label="Einsatzmöglichkeiten nach Branche filtern">{tabs_html}</div>
  <div class="rf-grid-clip"><div class="rf-grid">{uses_html}</div></div>
  <p class="rf-uses-note">Alle Bilder in diesem Bereich sind Visualisierungen. Welche Lösung zu Ihrem Standort passt, klären wir im Erstgespräch.</p>
</div></section>

<section class="rf-spot" id="haus-des-doeners"><div class="wrap">
  <span class="eyebrow">Referenz im Fokus</span>
  <div class="rf-spot-grid">
    <figure class="rf-spot-img"><img src="{rel}assets/img/referenzen/menueboards-theke.jpg" alt="Visualisierung: Theke mit drei digitalen Menüboards" width="1072" height="426" loading="lazy">
      <figcaption class="rf-tag">Visualisierung · kein Foto des Standorts</figcaption></figure>
    <div class="rf-spot-text">
      <h2>Drei Menüboards für<br>Haus des Döners.</h2>
      <p class="rf-meta"><span>Gastronomie</span> <span><i>·</i>Menüboards</span></p>
      <dl class="rf-facts">
        <div><dt>{ico("cal")}Seit</dt><dd>Juni 2025</dd></div>
        <div><dt>{icon(I_BOARDS)}Umfang</dt><dd>Drei digitale Menüboards an einem Standort</dd></div>
        <div><dt>{ico("clock")}Betrieb</dt><dd>Täglich</dd></div>
      </dl>
      {btn(rel + "kontakt/#anfrage", "Menüboard-Projekt anfragen")}
    </div>
  </div>
</div></section>

<section class="rf-steps"><div class="wrap">
  <span class="eyebrow">Ablauf in vier Schritten</span>
  <ol class="rf-steps-grid">{steps_html}</ol>
</div></section>

<section class="rf-seq"><div class="wrap">
  <div class="rf-seq-head"><h2>So kommt<br>alles zusammen.</h2><p class="sub">Typischer Ablauf als Visualisierung, keine Fotos eines Kundenstandorts.</p></div>
  <div class="rf-seq-row">{seq_html}</div>
</div></section>

<section class="rf-net" id="hyads"><div class="wrap">
  <div class="rf-net-text">
    <span class="eyebrow">Referenz · hyads-Netzwerk</span>
    <h2>Werbescreens im<br>REWE- und EDEKA-Umfeld.</h2>
    <p class="sub">Über 30 aktive Screens im hyads-Netzwerk zeigen die Werbung lokaler Unternehmen, dort, wo täglich eingekauft wird. Standortpartner erhalten einen Anteil der Werbeeinnahmen.</p>
    <ul class="rf-net-points">
      <li>{ico("pin")}<span><b>30+ aktive Screens</b> im REWE- und EDEKA-Umfeld</span></li>
      <li>{ico("people")}<span><b>Platz für ca. 6</b> Werbekunden pro Stele</span></li>
      <li>{icon(I_SCREEN)}<span><b>Ab ca. 99 €/Monat</b> für lokale Werbung</span></li>
    </ul>
    {btn(rel + "leistungen/dooh-hyads/", "Werben im hyads-Netzwerk")}
  </div>
  <figure class="rf-net-img">
    <img src="{rel}assets/img/referenzen/hyads-innen.jpg" alt="Visualisierung: Werbestele im Eingangsbereich eines Einkaufsumfelds" width="377" height="382" loading="lazy">
    <img src="{rel}assets/img/referenzen/hyads-aussen.jpg" alt="Visualisierung: Werbestele im Außenbereich" width="275" height="367" loading="lazy">
    <figcaption>Visualisierung</figcaption>
  </figure>
</div></section>


<section class="rf-film"><div class="wrap">
  <figure class="rf-film-img"><img src="{rel}assets/img/referenzen/hero-foyer.jpg" alt="Visualisierung: Großes Wanddisplay im Foyer, davor der Empfang" width="1120" height="391" loading="lazy">
    <figcaption class="rf-tag">Visualisierung</figcaption></figure>
  <div class="rf-film-text">
    <span class="eyebrow">Vom Aufbau bis zum Bild</span>
    <h2>Die Details zwischen<br>den Bildern.</h2>
    <p class="sub">Ein Screen wirkt erst, wenn Raum, Montage, Content und Alltag zusammenpassen. Wir planen alle vier mit Ihnen, aus einer Hand.</p>
    <ul class="rf-film-points">{film_html}</ul>
  </div>
</div></section>

<section class="rf-region"><div class="wrap">
  <div class="rf-region-text">
    <h2>Nah an Ihrem Standort.</h2>
    <p class="sub">Persönlich im Rhein-Main-Gebiet, Lieferung deutschlandweit, Einsätze vor Ort je nach Region.</p>
    <ul class="rf-region-row"><li>Beratung</li><li>Hardware</li><li>Content</li><li>Montage</li><li>Betrieb</li></ul>
  </div>
  <svg class="rf-map" viewBox="-10 -10 370 492" role="img" aria-label="Deutschlandkarte mit markierter Region Rhein-Main">
    <path class="land" d="{MAP}"/><circle class="dot" cx="109.5" cy="300" r="9"/><text x="128" y="312">Rhein-Main</text></svg>
  <p class="rf-region-cap">Die Karte zeigt unseren regionalen Schwerpunkt, nicht einzelne Projektstandorte.</p>
</div></section>

<section class="cta rf-cta">{RIBBON}<div class="wrap">
  <div class="cta-text">
    <span class="eyebrow">Ihr nächstes Projekt</span>
    <h2>Eine ähnliche Idee?<br>Wir planen sie mit Ihnen.</h2>
    <p class="sub">Erzählen Sie uns von Standort, Ziel und Nutzung der Screens. Wir zeigen Ihnen einen sinnvollen nächsten Schritt.</p>
    <div class="actions">{btn(rel + "kontakt/#anfrage", "Ähnliches Projekt besprechen")}{btn("tel:" + S["phone_href"], "Direkt anrufen", ghost=True)}</div>
    <p class="small">Unverbindliches Erstgespräch mit konkreter Einschätzung für Ihren Standort.</p>
  </div>
  <div class="cta-brand"><span>Menschen</span><span>Standorte</span><span>Möglichkeiten</span><i></i><img src="{rel}assets/img/logo/hysn-logo.svg" alt="HYSN" width="1485" height="234"></div>
</div></section>
<script src="{rel}assets/js/pages/referenzen.js" defer></script>"""


PAGES = [dict(path="referenzen/index.html", title="Referenzen | HYSN Digital Signage",
              desc="HYSN-Referenzen: drei digitale Menüboards bei Haus des Döners seit Juni 2025, 30+ Werbescreens im REWE- und EDEKA-Umfeld und typische Einsätze.",
              current="referenzen/", body=body, body_class="hero-page", css=["pages/referenzen.css"])]
