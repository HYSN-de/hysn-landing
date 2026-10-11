"""Partnerprogramm: layout follows Static pages/hysn-partner-program-concept-v1 1.png.
Revenue model per client: 10 % during refinancing, 20 % after amortisation (the concept's 20 %/35 % is wrong).
Pilot and monthly reporting are not confirmed; the concept's pilot section is reframed as a placement example."""
import math
from _lib import *


def _gear():
    """Eight-tooth gear outline on the 24x24 grid, same line weight as the shared icons."""
    pts = []
    for i in range(8):
        a = i * math.pi / 4
        for da, r in ((-0.36, 7.0), (-0.2, 9.2), (0.2, 9.2), (0.36, 7.0)):
            pts.append(f"{12 + r * math.cos(a + da):.2f} {12 + r * math.sin(a + da):.2f}")
    return f'<path d="M{" L".join(pts)}z"/><circle cx="12" cy="12" r="3"/>'


I = {
    "gear":   _gear(),
    "bars":   '<rect x="4.2" y="12.4" width="3.8" height="7.6" rx=".8"/><rect x="10.1" y="8.4" width="3.8" height="11.6" rx=".8"/><rect x="16" y="4" width="3.8" height="16" rx=".8"/>',
    "eye":    '<path d="M2.6 12S6.2 5.8 12 5.8 21.4 12 21.4 12 17.8 18.2 12 18.2 2.6 12 2.6 12z"/><circle cx="12" cy="12" r="3"/>',
    "wrench": '<path d="M14.6 6.4a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.4-3.4a5.6 5.6 0 0 1-7.4 7.4l-6.5 6.5a2 2 0 0 1-2.8-2.8l6.5-6.5a5.6 5.6 0 0 1 7.4-7.4z"/>',
    "search": '<circle cx="10.6" cy="10.6" r="6.2"/><path d="m15.2 15.2 5.2 5.2"/>',
    "next":   '<path d="M4 12h15M14 7l5 5-5 5"/>',
}
ic = lambda n, cls="ico": icon(I.get(n, n), cls)
DOWN = f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONS["down"]}</svg>'


def body(rel):
    img = lambda f, alt, w, h, extra='loading="lazy"': f'<img src="{rel}assets/img/partner/{f}" alt="{alt}" width="{w}" height="{h}" {extra}>'
    anfrage = rel + "kontakt/#anfrage"
    hyads = rel + "leistungen/dooh-hyads/"

    facts = [
        ("pin", "Standort zuerst", "Wir prüfen die Eignung vor jeder Vereinbarung."),
        ("gear", "HYSN übernimmt den Betrieb", "Screen, Inhalte, Werbekunden. 5&nbsp;Jahre Garantie auf die Hardware."),
        ("bars", "30+ aktive Werbescreens", "Im REWE- und <span class='nw'>EDEKA-Umfeld</span>, vermarktet über unser Netzwerk hyads."),
        ("people", "Persönlich in Rhein-Main", "Beratung und Service vor Ort, Lieferung deutschlandweit."),
    ]
    facts_html = "".join(f'<li>{ic(i)}<div><h3>{t}</h3><p>{d}</p></div></li>' for i, t, d in facts)

    nodes = [
        ("pin", "Sie stellen die Fläche", "Einen abgestimmten Platz und einen Ansprechpartner vor Ort."),
        ("gear", "HYSN betreibt den Screen", "Hardware, Montage, Inhalte und Werbekunden."),
        ("bars", "Die Einnahmen werden geteilt", "Auf Basis der gebuchten Werbung und Ihrer Vereinbarung."),
    ]
    nodes_html = f'<span class="pp-arrow">{ic("next")}</span>'.join(
        f'<div class="pp-node">{ic(i)}<div><h3>{t}</h3><p>{d}</p></div></div>' for i, t, d in nodes)

    types = [
        ("standort-supermarkt.jpg", 566, 282, "Werbestele im hellen Eingangsbereich eines Supermarkts neben der Obstauslage",
         "Supermarkt-Eingang", "Lokale Werbung dort, wo täglich eingekauft wird."),
        ("standort-fitness.jpg", 558, 282, "Hochformat-Screen neben dem Empfang eines Fitnessstudios",
         "Fitnessstudio-Empfang", "Eine feste Zielgruppe und Wartezeit beim Check-in."),
        ("standort-tankstelle.jpg", 562, 282, "Werbescreen im Shop einer Tankstelle neben der Kaffeetheke",
         "Tankstelle & Shop", "Sichtbar im täglichen Ablauf Ihrer Kunden."),
        ("standort-buero.jpg", 566, 312, "Hochformat-Werbedisplay im öffentlichen Eingangsbereich eines Einzelhandelsgeschäfts",
         "Einzelhandel & Ladeneingang", "Lokale Werbung im Blickfeld Ihrer Kunden."),
        ("standort-apotheke.jpg", 558, 312, "Hochformat-Screen in einer hellen Apotheke",
         "Apotheke & Praxis", "Ein kontrolliertes Umfeld mit Wartezeit."),
        ("standort-stadt.jpg", 562, 312, "Freistehende digitale Stele auf einem belebten Platz in der Innenstadt",
         "Städte & öffentlicher Raum", "Information für Bürger neben lokaler Werbung."),
    ]
    types_html = "".join(f'<figure>{img(f, alt, w, h)}<figcaption><h3>{H.escape(t)}</h3><p>{d}</p></figcaption></figure>'
                         for f, w, h, alt, t, d in types)

    checks = [("people", "Besucherfrequenz"), ("eye", "Sichtbarkeit des Screens"), ("clock", "Verweildauer"),
              ("wrench", "Technische Machbarkeit"), ("bars", "Lokale Werbenachfrage")]
    checks_html = "".join(f'<li>{ic(i)}<span>{t}</span></li>' for i, t in checks)

    tick = lambda items: '<ul class="pp-ticks">' + "".join(f"<li>{ico('one')}<span>{t}</span></li>" for t in items) + "</ul>"
    hysn_does = ["Auswahl und technische Einrichtung des Screens", "Lieferung, Montage und Inbetriebnahme",
                 "Planung und Ausspielung der Inhalte", "Akquise und Betreuung der Werbekunden",
                 "Inhalte und Einstellungen per Fernzugriff", "Abrechnung der Werbeeinnahmen nach Vertrag"]
    you_get = ["Einen vereinbarten Anteil an den Werbeeinnahmen", "Einen professionellen digitalen Screen",
               "Platz für eigene Hinweise nach Absprache", "Abgestimmte Werbekategorien und Ausschlüsse",
               "5&nbsp;Jahre Garantie auf die Hardware", "Ein Modell, das auch für weitere Standorte passt"]

    steps = [("mail", "Anfrage", "Standort, Adresse, möglicher Platz und geschätzte Besucherzahl."),
             ("search", "Standortprüfung", "Sichtbarkeit, Machbarkeit und Werbepotenzial."),
             ("doc", "Vereinbarung", "Modell, Anteile, Laufzeit, Strom und Regeln für Inhalte."),
             ("gear", "Montage & Betrieb", "Installation, Start und laufende Vermarktung.")]
    steps_html = "".join(f'<li><span class="pp-ring">{ic(i)}</span><div class="pp-step"><b>{n:02d}</b><div><h3>{H.escape(t)}</h3><p>{d}</p></div></div></li>'
                         for n, (i, t, d) in enumerate(steps, 1))

    rotation = [("rotation-werbung.jpg", 171, "Werbemotiv mit Kaffee und Croissant", "Gebuchte Werbung"),
                ("rotation-standort.jpg", 176, "Motiv mit Hinweisen für den Standort", "Informa&shy;tionen Ihres Standorts"),
                ("rotation-hinweise.jpg", 174, "Bergmotiv mit HYSN-Logo", "Netzwerk- und Service&shy;hinweise")]
    rotation_html = "".join(f'<figure>{img(f, alt, w, 134)}<figcaption>{t}</figcaption></figure>' for f, w, alt, t in rotation)

    faq = [
        ("Wie lange läuft eine Partnerschaft?",
         "Die Laufzeit hängt vom Modell, der Investition und dem Standort ab. Wir legen sie vor der Installation in der Vereinbarung fest.", True),
        ("Was ist, wenn wir die Partnerschaft beenden möchten?",
         "Kündigungsfristen und was danach mit der Hardware passiert, regelt die Vereinbarung. Sie kennen diese Punkte, bevor Sie unterschreiben.", False),
        ("Wer bezahlt den Strom?",
         "Das regeln wir in der Vereinbarung für Ihren Standort. Strom und andere standortspezifische Kosten klären wir vorab, nicht erst im laufenden Betrieb.", False),
        ("Können wir bestimmte Werbekunden ausschließen?",
         "Welche Kategorien nicht laufen sollen, etwa direkte Wettbewerber oder sensible Themen, besprechen wir vor dem Start mit Ihnen und halten es in der Vereinbarung fest.", False),
        ("Können wir eigene Inhalte zeigen?",
         "Nach Absprache ja. Wie viel Platz Ihre eigenen Hinweise in der Rotation bekommen, steht in der Vereinbarung. Änderungen schicken Sie uns einfach per Nachricht.", False),
        ("Was ist, wenn die Werbenachfrage gering ist?",
         "Dann fallen auch die Einnahmen geringer aus. Deshalb prüfen wir vorher, ob Ihr Standort für lokale Werbekunden interessant ist, und rechnen mit Beispielwerten statt mit Garantien.", False),
        ("Wie wird unser Anteil abgerechnet?",
         "Die Abrechnung der Werbeeinnahmen ist im Vertrag geregelt. Berechnungsgrundlage und Ablauf legen wir im Angebot für Ihren Standort fest.", False),
        ("Ab wann können Werbeeinnahmen entstehen?",
         "Sobald der Screen läuft und Werbung gebucht ist. Wann das der Fall ist, hängt von der Vorbereitung des Standorts und der Nachfrage ab. Einen realistischen Zeitplan nennen wir Ihnen im Angebot.", False),
        ("Was ist, wenn wir unsere Besucherzahl nicht genau kennen?",
         "Eine grobe Schätzung genügt für den Anfang, zum Beispiel Kassenvorgänge pro Tag. Den Rest klären wir bei der Standortprüfung.", False),
        ("Können wir mehrere Standorte einbringen?",
         "Ja. Wir prüfen jeden Standort einzeln und schlagen ein Modell vor, das sich auf weitere Standorte übertragen lässt.", False),
    ]
    faq_html = "".join(f'<details{" open" if o else ""}><summary>{H.escape(q)}</summary><p>{H.escape(a)}</p></details>' for q, a, o in faq)

    return f"""
<section class="chero pp-hero"><div class="chero-img">{img("partner-hero.jpg", "Digitale Werbestele mit Kaffeewerbung im hellen Eingangsbereich eines Supermarkts", 1130, 512, 'fetchpriority="high"')}</div>
  <div class="wrap"><div class="chero-text">
    <span class="eyebrow">Partnerprogramm für Standorte</span>
    <h1>Ihre Kundenfrequenz<br>wird zur Einnahmequelle.</h1>
    <p class="lead">Sie stellen eine gut sichtbare Fläche bereit. HYSN installiert einen Werbescreen, vermarktet ihn an lokale Werbekunden und beteiligt Sie an den Werbeeinnahmen.</p>
    <div class="actions">{btn(anfrage, "Standort prüfen lassen")}<a class="btn btn--ghost" href="#modelle">Modelle ansehen{DOWN}</a></div>
    <p class="note">{ico("one")}Im Betreibermodell investiert HYSN in die Hardware. Sie stellen die Fläche.</p>
  </div></div>
</section>

<section class="pp-facts" aria-label="Das Partnerprogramm in Kürze"><h2 class="vh">Das Partnerprogramm in Kürze</h2><div class="wrap"><ul>{facts_html}</ul></div></section>

<section class="pp-how"><div class="wrap">
  <div class="pp-how-text">
    <span class="eyebrow">So funktioniert die Partnerschaft</span>
    <h2>Ihr Standort.<br>Wir übernehmen den&nbsp;Betrieb.</h2>
    <p class="sub">Eine klare Aufteilung der Aufgaben, von der ersten Standortprüfung bis zum laufenden Betrieb.</p>
    <div class="pp-nodes">{nodes_html}</div>
    <div class="pp-how-foot"><p class="small">Ob sich ein Standort wirtschaftlich eignet, prüfen wir vor jeder Vereinbarung. Die Werbung vermarkten wir über unser Netzwerk hyads.</p>{tlink(hyads, "So funktioniert hyads")}</div>
  </div>
  <div class="pp-how-img">{img("partner-betrieb.jpg", "Digitale HYSN-Stele mit Bergmotiv, daneben ein aufgeklappter Laptop auf einem hellen Tisch", 804, 431)}</div>
</div></section>

<section class="pp-types" id="standorte"><div class="wrap">
  <div class="pp-types-head">
    <div><span class="eyebrow">Passt Ihr Standort?</span><h2>Regelmäßige Besucher.<br>Sichtbare Möglichkeiten.</h2>
      <p class="sub">Beispiele für mögliche Standorttypen. Unsere aktiven Werbescreens laufen heute im REWE- und <span class="nw">EDEKA-Umfeld</span>, weitere Standorttypen prüfen wir im Einzelfall.</p></div>
    {tlink("#eignung", "Worauf es bei der Prüfung ankommt", "down")}
  </div>
  <div class="pp-types-grid">{types_html}</div>
</div></section>

<section class="pp-check" id="eignung"><div class="wrap">
  <div><h2>Zuerst zählt<br>der richtige Platz.</h2>
    <p class="sub">Nicht jeder Standort passt. Für den Anfang genügen eine grobe Schätzung der Besucherzahl und ein paar Fotos.</p></div>
  <ul>{checks_html}</ul>
</div></section>

<section class="pp-models" id="modelle"><div class="wrap">
  <div class="pp-models-head"><span class="eyebrow">Das passende Modell</span><h2>Drei Wege zur<br>Partnerschaft.</h2></div>
  <div class="pp-models-grid">
    <article class="pp-model pp-model--a">
      <span class="pp-label">Modell A</span><h3>Betreibermodell</h3>
      <p>HYSN investiert in Screen und Montage und refinanziert die Hardware über die Werbeeinnahmen. Sie stellen die Fläche.</p>
      <div class="pp-stages"><div><strong>10&nbsp;%</strong><span>während der Refinanzierung</span></div><span class="pp-arrow">{ic("next")}</span><div><strong>20&nbsp;%</strong><span>nach der Amortisation</span></div></div>
      <p class="pp-model-sub">Ihr Anteil an den Werbeeinnahmen des Screens, vor und nach der Refinanzierung der Hardware.</p>
      <p class="pp-model-note">Keine Investition in Hardware auf Ihrer Seite, sofern der Standort geeignet ist.</p>
    </article>
    <article class="pp-model">
      <span class="pp-label">Modell B</span><h3>Co-Investment</h3>
      <p>HYSN und Sie investieren gemeinsam, die Werbeeinnahmen werden hälftig geteilt.</p>
      <div class="pp-big"><strong>50/50</strong><span>Aufteilung der Werbeeinnahmen</span></div>
      <p class="pp-model-sub">Die endgültigen Konditionen legen wir im Angebot für Ihren Standort fest.</p>
      <p class="pp-model-note">Für einen einzelnen Standort oder mehrere Standorte.</p>
    </article>
    <article class="pp-model">
      <span class="pp-label">Modell C</span><h3>Eigeninvestition</h3>
      <p>Sie kaufen die Hardware selbst. HYSN liefert, montiert und richtet den Screen ein.</p>
      <div class="pp-big pp-big--word"><strong>Eigentum</strong><span>Volle Kontrolle, volle Einnahmen</span></div>
      <p class="pp-model-sub">Der Screen gehört Ihnen.</p>
      <p class="pp-model-note">Wartung und Betrieb übernehmen wir auf Wunsch.</p>
    </article>
  </div>
  <p class="pp-models-note">Endgültige Aufteilung, Berechnungsgrundlage, Strom, Laufzeit und Zuständigkeiten legen wir im Angebot für Ihren Standort fest. Werbeeinnahmen sind nicht garantiert.</p>
</div></section>

<section class="pp-calc"><div class="wrap">
  <div class="pp-calc-head"><span class="eyebrow">Beispielrechnung</span><h2>Umsatz und Ihr Anteil.<br>Klar getrennt.</h2></div>
  <div class="pp-calc-body"><div class="pp-calc-vals">
    <div><strong>594&nbsp;€</strong><span>Werbeeinnahmen pro Monat<br>6&nbsp;Werbekunden à&nbsp;ca.&nbsp;99&nbsp;€</span></div>
    <div><strong>59,40&nbsp;€</strong><span>Ihr Anteil bei 10&nbsp;%<br>während der Refinanzierung</span></div>
    <div><strong>118,80&nbsp;€</strong><span>Ihr Anteil bei 20&nbsp;%<br>nach der Amortisation</span></div>
  </div>
  <p class="pp-calc-note">Beispielwert, keine Garantie. Die beiden Anteile gelten für unterschiedliche Phasen und werden nicht addiert. Die tatsächlichen Einnahmen hängen von der Buchung ab, die endgültige Aufteilung legen wir im Angebot fest.</p></div>
</div></section>

<section class="pp-scope"><div class="wrap">
  <h2>HYSN betreibt.<br>Ihr Team bleibt entlastet.</h2>
  <div class="pp-scope-cols">
    <div><h3>Das übernimmt HYSN</h3>{tick(hysn_does)}</div>
    <div><h3>Ihr Standort erhält</h3>{tick(you_get)}</div>
  </div>
  <p class="pp-scope-note">Ihr Team stellt die Fläche, den Zugang vor Ort und die nötigen Freigaben. Strom und standortspezifische Kosten legen wir vorab in der Vereinbarung fest.</p>
</div></section>

<section class="pp-steps"><div class="wrap">
  <div><span class="eyebrow">Vom ersten Kontakt bis zum Betrieb</span><h2>Ein überlegter Start.<br>Ein klarer Weg.</h2></div>
  <div><ol>{steps_html}</ol>
    <p class="pp-steps-note">Wann der Screen startet und wie gut er gebucht ist, hängt von der Vorbereitung des Standorts und der Nachfrage ab.</p></div>
</div></section>

<section class="pp-place"><div class="wrap">
  <div class="pp-place-text">
    <h2>Aus einer freien Wand<br>wird ein Werbeplatz.</h2>
    <p class="sub">Oft genügt eine ungenutzte Fläche im Eingangsbereich. Wir prüfen, ob Sichtbarkeit, Laufweg und Technik passen und ob der Platz für lokale Werbekunden interessant ist.</p>
    {btn(anfrage, "Standort prüfen lassen")}
  </div>
  <div class="pp-place-imgs">
    <figure><div class="pp-ba">{img("platzierung-vorher.jpg", "Eingangsbereich mit leerer Holzwand neben der Glasfront", 430, 300)}<span class="pp-tag">Vorher</span></div><figcaption>Eine ungenutzte Fläche im Eingang.</figcaption></figure>
    <figure><div class="pp-ba">{img("platzierung-nachher.jpg", "Derselbe Eingangsbereich mit einer digitalen Werbestele vor der Holzwand", 430, 300)}<span class="pp-tag">Nachher</span></div><figcaption>Ein betreuter digitaler Werbeplatz.</figcaption></figure>
    <p class="pp-place-label">Beispielhafte Darstellung einer Platzierung</p>
  </div>
</div></section>

<section class="pp-content"><div class="wrap">
  <div class="pp-content-text">
    <span class="eyebrow">Inhalte, die passen</span>
    <h2>Ihr Umfeld.<br>Abgestimmte Regeln.</h2>
    <p class="sub">Die Regeln für die Werbung legen wir fest, bevor der Screen startet.</p>
    {tick(["Kategorien und passende Werbekunden abstimmen", "Wettbewerber oder sensible Inhalte ausschließen", "Eigene Informationen einbinden, wenn vereinbart"])}
  </div>
  <div class="pp-content-visual">
    <div class="pp-content-screen">{img("inhalte-screen.jpg", "Hochformat-Display mit HYSN-Motiv neben einer Pflanze", 315, 332)}</div>
    <div class="pp-rotation"><div class="pp-rotation-card"><h3>Beispiel für eine Rotation</h3><div class="pp-rotation-grid">{rotation_html}</div></div>
      <p class="pp-rotation-note">Beispielhafte Rotation. Den Mix der Inhalte legen wir für jeden Standort fest.</p></div>
  </div>
</div></section>

<section class="qa pp-qa"><div class="wrap">
  <div><span class="eyebrow">Gut zu wissen</span><h2>Partnerfragen,<br>klar beantwortet.</h2></div>
  <div class="faq">{faq_html}</div>
</div></section>

<section class="cta pp-cta">{RIBBON}<div class="wrap">
  <div class="cta-text">
    <div><span class="eyebrow">Gemeinsam Standorte entwickeln</span>
      <h2>Was kann Ihr<br>Standort leisten?</h2>
      <p class="sub">Schicken Sie uns Adresse, möglichen Platz und ein paar Fotos. Wir sagen Ihnen, ob und wie es weitergeht.</p></div>
    <div class="pp-cta-act"><div class="actions">{btn(anfrage, "Standort prüfen lassen")}<a class="btn btn--ghost" href="tel:{S["phone_href"]}">Persönlich sprechen{ARROW}</a></div>
      <p class="small">Die erste Prüfung ist kostenlos und verpflichtet Sie zu nichts.</p>
      <p class="pp-cta-contact pp-cta-direct"><a href="mailto:{S["email"]}">{S["email"]}</a><a href="tel:{S["phone_href"]}">{S["phone"]}</a></p></div>
  </div>
  <div class="cta-brand"><span>Menschen</span><span>Standorte</span><span>Möglichkeiten</span><i></i><img src="{rel}assets/img/logo/hysn-logo.svg" alt="HYSN" width="1485" height="234">
    <p class="pp-cta-contact"><a href="mailto:{S["email"]}">{S["email"]}</a><a href="tel:{S["phone_href"]}">{S["phone"]}</a></p></div>
</div></section>"""


PAGES = [dict(path="partnerprogramm/index.html", title="Partnerprogramm für Standorte | HYSN Digital Signage",
              desc="Ihre Kundenfrequenz als Einnahmequelle: HYSN installiert und betreibt einen Werbescreen an Ihrem Standort, Sie erhalten einen Anteil der Werbeeinnahmen.",
              current="partnerprogramm/", body=body, body_class="hero-page", css=["pages/partner.css"])]
