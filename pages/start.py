"""Start (index.html): the hysn.de landing page (repo root index.html) carried over into the site, section by section and
with its motion (logo carousel, before/after slider, marquee, reveals). Links now go to the site's pages instead of anchors.
Content changes against the landing: current phone number and region list (Weiterstadt instead of Dreieich),
no response-time line ("werktags zeitnah" is not confirmed), legal texts via the shared footer pages instead of dialogs.
Customer logos: all nine were supplied and confirmed by the client (confirmed to us on 11.10.2026)."""
from _lib import *

I = dict(
    layers='<path d="M12 3.5 21 8l-9 4.5L3 8z"/><path d="m3 12 9 4.5 9-4.5"/><path d="m3 16 9 4.5 9-4.5"/>',
    bars='<rect x="3.5" y="12" width="3.8" height="8" rx=".4"/><rect x="10.1" y="8" width="3.8" height="12" rx=".4"/><rect x="16.7" y="4" width="3.8" height="16" rx=".4"/>',
    search='<circle cx="10.6" cy="10.6" r="6.2"/><path d="m15.2 15.2 5 5"/>',
    gear='<circle cx="12" cy="12" r="2.8"/><circle cx="12" cy="12" r="6.4"/><path d="M12 2.8v2.8M12 18.4v2.8M2.8 12h2.8M18.4 12h2.8M5.5 5.5l2 2M16.5 16.5l2 2M5.5 18.5l2-2M16.5 7.5l2-2"/>',
    monitor='<rect x="3.4" y="4.6" width="17.2" height="11.6" rx="1"/><path d="M9 20h6M12 16.2V20"/>',
    check='<path d="m5 12.6 4.3 4.3L19 7.2"/>',
    route='<circle cx="6" cy="18" r="2.2"/><circle cx="18" cy="6" r="2.2"/><path d="M8.2 18H15a3 3 0 0 0 0-6H9a3 3 0 0 1 0-6h6.8"/>',
    swap='<path d="M9 7 4 12l5 5M15 7l5 5-5 5"/>',
    prev='<path d="M14.5 5.5 8 12l6.5 6.5"/>', next='<path d="M9.5 5.5 16 12l-6.5 6.5"/>',
    pause='<path d="M9 6v12M15 6v12"/>', play='<path d="m8.5 6 9 6-9 6z"/>',
)
ic = lambda n, cls="ico": icon(I[n], cls) if n in I else ico(n, cls)
DOWN = f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONS["down"]}</svg>'


def body(rel):
    anfrage = rel + "kontakt/#anfrage"
    fotos = mailto("Standortfotos für mein Projekt")

    facts = [("people", "Ein Ansprechpartner", "Beratung, Hardware, Content, Montage und Betrieb aus einer Hand."),
             ("layers", "Über 30 aktive Screens", "Im laufenden Betrieb, unter anderem im REWE- und EDEKA-Umfeld."),
             ("pin", "Rhein-Main &amp; deutschlandweit", "Persönliche Betreuung vor Ort, Umsetzung bundesweit."),
             ("bars", "Werbeeinnahmen möglich", "Geeignete Standorte können über hyads mit lokaler Werbung Einnahmen erzielen.")]
    facts_html = "".join(f'<div class="fact">{ic(i)}<div><h3>{t}</h3><p>{d}</p></div></div>' for i, t, d in facts)

    # (file, name, extra class, optical size at rest and on hover, max width/height inside the card)
    logos = [("mercedes-benz", "Mercedes-Benz", "", "1;1.045;84%;64%"), ("rewe", "REWE", " logo-card--fill", "1.02;1.07"),
             ("edeka", "EDEKA", "", "1.13;1.18;88%;92%"), ("boss", "BOSS", " logo-card--fill", "1.18;1.23"),
             ("clever-fit", "clever fit", "", "1;1.05;72%;88%"), ("haus-des-doeners", "Das Haus des Döners", " logo-card--fill logo-card--contain", "1.16;1.21"),
             ("loewen-frankfurt", "Löwen Frankfurt", "", "1.06;1.11;76%;100%"), ("bam-bam-kebup", "BAM BAM KEB’UP", " logo-card--fill", "1.01;1.06"),
             ("k-beautyhouse", "K Beautyhouse", "", "1;1.05;72%;84%")]
    def logo(f, name, cls, size):
        v = size.split(";")
        style = f"--s:{v[0]};--hs:{v[1]}" + (f";--mw:{v[2]};--mh:{v[3]}" if len(v) > 2 else "")
        return f'<div class="logo-card{cls}" role="listitem" style="{style}"><img src="{rel}assets/img/start/marken/{f}.jpg" alt="{name}" draggable="false"></div>'
    logos_html = "".join(logo(*x) for x in logos)

    eco = [("eco-hardware.jpg", "Display-Hardware", "Menüboards, Stelen und LED-Wände, passend zu Licht, Abstand und Nutzung. Mit 5 Jahren Garantie.", rel + "referenzen/#einsatz", "Formate ansehen"),
           ("eco-content.jpg", "Content &amp; Animation", "Menüs, Angebote und Kampagnen, bildschirmfertig gestaltet. Ohne externe Agentur.", rel + "leistungen/content-creation/", "Content Creation"),
           ("eco-install.jpg", "Montage &amp; Einrichtung", "Montiert, eingerichtet und getestet. Sie übernehmen ein laufendes System.", rel + "leistungen/installation-montage/", "Installation &amp; Montage"),
           ("eco-support.jpg", "Betrieb &amp; Support", "Preis geändert? Eine Nachricht genügt. Updates und Support auch nach dem Start.", rel + "leistungen/wartung-betrieb/", "Wartung &amp; Betrieb")]
    eco_html = "".join(f'<a class="st-eco-card" href="{h}"><div class="st-eco-text"><h3>{t}</h3><p>{d}</p>'
                       f'<span class="st-more">{m}{ARROW}</span></div><div class="st-eco-img"><img src="{rel}assets/img/start/{f}" alt="" loading="lazy"></div></a>'
                       for f, t, d, h, m in eco)

    ind = [("sol-restaurant.jpg", "Gastronomie &amp; Menüboards", "Menüboards, Bestellterminals und Schaufenster-Screens. Preise und Angebote ändern Sie ohne Neudruck.", rel + "referenzen/#gastro"),
           ("sol-retail.jpg", "Handel &amp; Supermärkte", "Angebote dort zeigen, wo Kunden entscheiden: Stelen im Eingang, Screens am Regal und im Schaufenster.", rel + "referenzen/#handel"),
           ("sol-led-lcd.jpg", "Events &amp; LED-Wände", "LED-Wände und Videowalls für Bühne, Messestand und Foyer. Zum Kauf oder zur Miete, montiert und betreut.", rel + "referenzen/#events"),
           ("sol-automotive.jpg", "Autohäuser &amp; Außenflächen", "Outdoor-Stelen und Showroom-Displays, hell genug für Tageslicht. Aktionen und Modelle sichtbar bis zur Straße.", anfrage),
           ("sol-education.jpg", "Bildung &amp; Interaktive Displays", "Interaktive Whiteboards für Unterricht und Präsentation, Info-Displays für Flur und Foyer.", anfrage),
           ("sol-healthcare.jpg", "Praxen, Kliniken &amp; Empfang", "Ruhige, klare Information für Patienten und Besucher: Wegführung, Wartezeiten und Hinweise statt Aushängen am Tresen.", anfrage)]
    def title(t):  # the arrow stays glued to the last word when the title wraps
        head, _, last = t.rpartition(" ")
        return (head + " " if head else "") + f'<span class="nw">{last}{ARROW}</span>'
    ind_html = "".join(f'<a class="st-ind-card" href="{h}"><span class="st-ind-img"><img src="{rel}assets/img/start/{f}" alt="" loading="lazy"></span>'
                       f'<h3>{title(t)}</h3><p>{d}</p></a>' for f, t, d, h in ind)

    features = [("monitor", "Bildschirmfertiges Design"), ("chat", "Updates per Nachricht, ohne Schulung"), ("layers", "Einheitliche Kampagnen für mehrere Standorte")]
    features_html = "".join(f"<li>{ic(i)}<span>{t}</span></li>" for i, t in features)

    steps = [("search", "Standort klären", "Sie beschreiben Fläche, Ziel und Inhalte. Fotos oder ein Grundriss reichen."),
             ("monitor", "Setup empfehlen", "Sie erhalten passende Display-Typen, Größen, Montageart und Betriebskonzept."),
             ("pencil", "Content vorbereiten", "Menüs, Angebote oder Kampagnen werden im richtigen Format für Ihre Screens gestaltet."),
             ("gear", "Installieren &amp; betreiben", "Montiert, eingerichtet, vor dem Start getestet. Danach Updates und Support auf Wunsch.")]
    steps_html = "".join(f'<li><span class="ring">{ic(i)}</span><b>0{n}</b><h3>{t}</h3><p>{d}</p></li>' for n, (i, t, d) in enumerate(steps, 1))

    ba = ["Preise per Nachricht ändern statt neu drucken", "Tagesangebote automatisch zur richtigen Uhrzeit", "Bestseller und Kombis genau im Bestellmoment sichtbar"]
    ba_html = "".join(f"<li>{ic('one')}<span>{x}</span></li>" for x in ba)

    checks = ["Hardware nach Licht, Abstand und Nutzung gewählt, nicht nach Katalog", "Content von Anfang an eingeplant, nicht nachträglich angehängt",
              "Montage abgestimmt auf Ihre Öffnungszeiten und den laufenden Betrieb", "Nach dem Start erreichbar: Updates, Support, Erweiterung"]
    checks_html = "".join(f"<li>{ic('check')}<span>{x}</span></li>" for x in checks)

    words = ["Restaurants", "Handel &amp; Supermärkte", "Events &amp; Messen", "Städte &amp; Kommunen", "Autohäuser", "Bildung", "Praxen &amp; Büros", "Franchise"]
    marquee_html = "".join(f"<span>{w}</span><em>·</em>" for w in words)

    return f"""
<section class="chero st-hero"><div class="chero-img"><img src="{rel}assets/img/start/hero.jpg" alt="Große Digital-Signage-Wand in einem hellen Atrium" fetchpriority="high"></div>
  <div class="wrap"><div class="chero-text">
    <span class="eyebrow">Full-Service Digital Signage</span>
    <h1>Sichtbar am<br>Standort.<br>Ohne Aufwand.</h1>
    <p class="lead">Wir helfen Restaurants, Einzelhändlern, Standortpartnern und Kommunen, ihre Flächen mit digitalen Displays zu modernisieren und sichtbarer zu kommunizieren — ohne dass sie Hardware, Content, Installation und Betrieb selbst koordinieren müssen.</p>
    <div class="actions">{btn(anfrage, "Display-Projekt besprechen")}<a class="btn btn--ghost" href="#branchen">Lösung für meine Branche{DOWN}</a></div>
    <p class="note">{ico("chat")}Kostenloses Erstgespräch. Fotos oder ein Grundriss reichen für eine erste Einschätzung.</p>
  </div></div>
</section>

<section class="facts st-facts"><h2 class="vh">Auf einen Blick</h2><div class="wrap">{facts_html}</div></section>

<section class="sec st-trust" id="kunden"><div class="wrap">
  <div class="st-head">
    <div><span class="eyebrow">Ausgewählte Kunden</span><h2 id="st-kunden">Marken, die auf<br>HYSN vertrauen.</h2></div>
    <p class="sub">Vom lokalen Lieblingsbetrieb bis zur internationalen Marke: Unternehmen aus Gastronomie, Handel, Automotive, Fitness und Sport setzen auf unsere Display-Lösungen.</p>
  </div>
  <div class="logos" role="region" aria-roledescription="Karussell" aria-labelledby="st-kunden">
    <div class="logos-track" role="list" tabindex="0" aria-label="Kundenlogos" data-lenis-prevent-wheel>{logos_html}</div>
    <div class="logos-bar">
      <p class="logos-hint"><i aria-hidden="true"></i><span class="t-pointer">Auf ein Logo zeigen für Farbe · ziehen zum Blättern</span><span class="t-touch">Logo antippen für Farbe · wischen zum Blättern</span></p>
      <div class="logos-progress" aria-hidden="true"><i></i></div>
      <div class="logos-ctrl"><button type="button" data-logos="prev" aria-label="Vorherige Marke">{ic("prev", "")}</button><button type="button" data-logos="pause" aria-pressed="false" aria-label="Logo-Karussell pausieren">{ic("pause", "i-pause")}{ic("play", "i-play")}</button><button type="button" data-logos="next" aria-label="Nächste Marke">{ic("next", "")}</button></div>
    </div>
  </div>
</div></section>

<section class="sec sec--band st-eco" id="leistungen"><div class="wrap">
  <div class="sec-head">
    <span class="eyebrow">Leistungen aus einer Hand</span>
    <h2>Ein Display ist schnell gekauft.<br>Wirkung entsteht im Betrieb.</h2>
    <p class="sub">Sie bekommen nicht nur ein Gerät, sondern ein System, das im Tagesgeschäft läuft: von der Standortberatung bis zum laufenden Support.</p>
  </div>
  <div class="st-eco-grid">{eco_html}</div>
</div></section>

<section class="sec st-ind" id="branchen"><div class="wrap">
  <div class="st-head st-head--end">
    <div><span class="eyebrow">Lösungen nach Einsatzbereich</span><h2>Nicht jede Fläche braucht<br>denselben Bildschirm.</h2></div>
    {tlink(anfrage, "Anderen Einsatzfall besprechen")}
  </div>
  <div class="st-ind-grid">{ind_html}</div>
</div></section>

<section class="sec sec--band st-content"><div class="wrap">
  <div class="st-content-text">
    <span class="eyebrow">Content, der wirkt</span>
    <h2>Der Screen ist nur so gut wie sein Content.</h2>
    <p class="sub">Deshalb entstehen Menüs, Angebote, Stadtinfos und Kampagnen von Anfang an bildschirmfertig: lesbar aus der Distanz, im richtigen Format, zentral aktualisierbar.</p>
    {btn(rel + "leistungen/content-creation/", "Content Creation ansehen")}
  </div>
  <div class="st-content-img"><img src="{rel}assets/img/start/content.jpg" alt="Digitales Menüboard und zentrale Content-Verwaltung am Laptop" loading="lazy"></div>
  <ul class="st-list">{features_html}</ul>
</div></section>

<section class="sec st-process" id="ablauf"><div class="wrap">
  <div class="st-head st-head--end">
    <div><span class="eyebrow">Unser Ablauf</span><h2>Vier Schritte, bis<br>der Screen läuft.</h2></div>
    {tlink(rel + "faq/", "Häufige Fragen")}
  </div>
  <ol class="steps">{steps_html}</ol>
</div></section>

<section class="sec sec--band st-ba"><div class="wrap">
  <div class="st-ba-text">
    <span class="eyebrow">Der Unterschied im Alltag</span>
    <h2>Von gedruckten Karten zu drei Menüboards.</h2>
    <p class="sub">Dieselbe Theke, vorher und nachher. Ziehen Sie den Regler: Vorher kostete jede Preisänderung neue Druckdaten und Wartezeit. Nachher genügt eine Nachricht.</p>
    <ul class="st-list st-list--sm">{ba_html}</ul>
    {btn(anfrage, "Menüboard für mein Restaurant planen")}
  </div>
  <div>
    <div class="compare">
      <img src="{rel}assets/img/start/before.jpg" alt="Vorher: Restaurant-Theke mit gedruckten Menütafeln und handschriftlichen Preiskorrekturen" loading="lazy" draggable="false">
      <div class="compare-after"><img src="{rel}assets/img/start/after.jpg" alt="Nachher: dieselbe Theke mit drei digitalen Menüboards" loading="lazy" draggable="false"></div>
      <span class="compare-label compare-label--before">Vorher</span><span class="compare-label compare-label--after">Nachher</span>
      <div class="compare-handle" aria-hidden="true"><span class="compare-knob">{ic("swap", "")}</span></div>
      <input class="compare-range" type="range" min="0" max="100" value="50" step="1" aria-label="Vorher-Nachher-Vergleich: Regler verschieben">
    </div>
    <div class="compare-caps"><p><strong>Vorher</strong>Gedruckte Karte. Jede Änderung ein Neudruck.</p><p><strong>Nachher</strong>Drei Menüboards. Änderungen per Nachricht.</p></div>
    <p class="sec-note">Beispielhafter Anwendungsfall</p>
  </div>
</div></section>

<section class="sec st-value"><div class="wrap">
  <h2>Ein Projekt. Ein Ansprechpartner.<br>Eine Verantwortung.</h2>
  <ul class="st-checks">{checks_html}</ul>
</div></section>

<section class="st-split" id="hyads">
  <div class="st-split-text">
    <span class="eyebrow">HYSN + hyads</span>
    <h2>Ihr Standort<br>kann mehr.</h2>
    <p class="sub">Supermärkte, Kommunen und andere Standorte mit viel Kundenverkehr können über hyads einen Werbescreen betreiben lassen. Sie stellen die Fläche, hyads übernimmt Werbekunden, Inhalte und Technik. Möglich als Betreibermodell, Co-Investment oder Eigeninvestition.</p>
    <div class="actions">{btn(rel + "partnerprogramm/", "Partnerprogramm ansehen")}{tlink(rel + "leistungen/dooh-hyads/", "Werben mit hyads")}</div>
    <p class="small">Sie erhalten eine realistische Beispielrechnung, keine Umsatzversprechen.</p>
  </div>
  <div class="st-split-img"><img src="{rel}assets/img/start/dooh.jpg" alt="Digitale Werbestele auf einem belebten Stadtplatz" loading="lazy"></div>
</section>

<section class="sec sec--band st-region"><div class="wrap">
  <div>
    <span class="eyebrow">Persönlich vor Ort</span>
    <h2>Nah an Ihrem Standort.</h2>
    <p class="sub">Beratung, Montage und Service persönlich im Rhein-Main-Gebiet: Weiterstadt, Darmstadt, Frankfurt, Offenbach, Mainz und Wiesbaden. Deutschlandweite Umsetzung je nach Projektumfang.</p>
    <div class="st-points"><div>{ic("pin")}<span>Beratung und Montage vor Ort</span></div><div>{ic("route")}<span>Rollout über mehrere Standorte</span></div></div>
    {tlink(rel + "kontakt/", "Beratungstermin vereinbaren")}
  </div>
  <svg class="map" viewBox="-10 -10 370 492" role="img" aria-label="Deutschlandkarte mit markierter Region Rhein-Main">
    <path class="land" d="{MAP}"/><path class="area" d="M78 262c14-14 40-18 58-8 16 9 22 28 16 46-6 17-22 30-42 32-21 2-40-8-46-26-5-15 2-32 14-44z"/>
    <circle class="dot" cx="109.5" cy="300" r="6"/><text x="124" y="306">Rhein-Main</text></svg>
</div></section>

<section class="cta st-cta" id="kontakt">{RIBBON}<div class="wrap">
  <div class="cta-text">
    <span class="eyebrow">Kostenloses Erstgespräch</span>
    <h2>Welcher Screen passt<br>zu Ihrem Standort?</h2>
    <p class="sub">Schicken Sie uns Standort, Branche und gewünschte Nutzung. Sie erhalten eine erste Einschätzung zu Technik, Content, Montage und dem sinnvollen nächsten Schritt, keine Standardliste.</p>
    <div class="actions">{btn(anfrage, "Display-Projekt einschätzen lassen")}{btn(fotos, "Standortfotos senden", ghost=True)}</div>
    <p class="st-direct"><a href="mailto:{S["email"]}">{S["email"]}</a><a href="tel:{S["phone_href"]}">{S["phone"]}</a></p>
    <p class="small">Persönlicher Ansprechpartner, kein Callcenter.</p>
  </div>
  <div class="cta-brand"><span>Menschen</span><span>Standorte</span><span>Möglichkeiten</span><i></i><img src="{rel}assets/img/logo/hysn-logo.svg" alt="HYSN" width="1485" height="234"></div>
</div></section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">{marquee_html}</div></div>"""


PAGES = [dict(path="index.html", title="HYSN | Digital Signage für Gastronomie, Handel, Events und Kommunen",
              desc="Digitale Menüboards, Werbestelen und LED-Wände für Gastronomie, Handel, Events und Kommunen. Beratung, Hardware, Content, Montage und Betrieb aus einer Hand.",
              current="index.html", body=body, body_class="hero-page", css=["pages/start.css"])]
