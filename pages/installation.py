"""Installation & Montage: layout follows Static pages/hysn-installation-montage-concept-v1 1.png.
Images in assets/img/installation/ are temporary crops from that concept."""
import math
from _lib import *


def _gear():
    pts = []
    for i in range(8):
        t = i * 45
        for r, a in ((6.7, t - 13), (8.7, t - 8), (8.7, t + 8), (6.7, t + 13)):
            pts.append(f"{12 + r * math.cos(math.radians(a)):.2f} {12 + r * math.sin(math.radians(a)):.2f}")
    return f'<path d="M{"L".join(pts)}z"/><circle cx="12" cy="12" r="3"/>'


_MON = '<rect x="3.4" y="4.4" width="17.2" height="11.8" rx="1.2"/><path d="M12 16.2v3.6M8.2 19.8h7.6"/>'
I = {
    "gear": _gear(),
    "monitor": _MON,
    "mon-check": _MON + '<path d="m8.9 10.4 2.1 2.1 4.1-4.2"/>',
    "mon-wave": _MON + '<path d="m6.6 12.6 2.6-3.2 2.6 2.2 2.6-3.4 2.9 2.6"/>',
    "search": '<circle cx="10.6" cy="10.6" r="6.2"/><path d="m15.2 15.2 5 5"/>',
    "truck": '<path d="M2.8 6.4h11v9.4H9M5 15.8H2.8V6.4"/><path d="M13.8 9.4h3.8l2.8 3.2v3.2h-1.4M13.8 15.8h1.6M13.8 9.4v6.4"/><circle cx="7" cy="16.8" r="1.9"/><circle cx="17.1" cy="16.8" r="1.9"/>',
    "check": '<path d="m5.2 12.6 4.4 4.4 9.2-9.6"/>',
    "scan": '<path d="M4 8.4V5.2A1.2 1.2 0 0 1 5.2 4h3.2M15.6 4h3.2A1.2 1.2 0 0 1 20 5.2v3.2M20 15.6v3.2a1.2 1.2 0 0 1-1.2 1.2h-3.2M8.4 20H5.2A1.2 1.2 0 0 1 4 18.8v-3.2"/><circle cx="12" cy="12" r="3"/>',
    "bracket": '<rect x="4" y="3.6" width="5.2" height="16.8" rx="1"/><path d="M9.2 8.2h7.2M9.2 15.8h7.2M16.4 6v12h3.6V6z"/><circle cx="6.6" cy="7" r=".6"/><circle cx="6.6" cy="17" r=".6"/>',
    "wrench": '<path d="M14.6 6.4a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.1-3.1a5.6 5.6 0 0 1-7.3 7.3L7 20a2 2 0 0 1-2.9-2.9l6.4-6.4a5.6 5.6 0 0 1 7.3-7.3z"/>',
    "cable": '<path d="M7.6 3.4v3M12.4 3.4v3M5.8 6.4h8.4v3.2a4.2 4.2 0 0 1-8.4 0z"/><path d="M10 13.8v1.8a3.6 3.6 0 0 0 3.6 3.6h.6a3.6 3.6 0 0 0 3.6-3.6v-1a2.6 2.6 0 0 1 2.6-2.6"/>',
    "doc-up": '<path d="M6.4 3.4h7.8l4 4v13.2H6.4z"/><path d="M14.2 3.4v4h4M12.3 17.6v-6.4M9.6 13.8l2.7-2.7 2.7 2.7"/>',
    "person": '<circle cx="12" cy="8" r="3.8"/><path d="M4.8 20.2v-.6a7.2 7.2 0 0 1 14.4 0v.6"/>',
    "headset": '<path d="M4.6 14v-2.2a7.4 7.4 0 0 1 14.8 0V14"/><rect x="3.4" y="12.8" width="3.8" height="5.8" rx="1.2"/><rect x="16.8" y="12.8" width="3.8" height="5.8" rx="1.2"/><path d="M18.7 18.6v.3a2.2 2.2 0 0 1-2.2 2.2h-3.2"/>',
    "broom": '<path d="M12 3v8.4"/><path d="M8.2 11.4h7.6l1.9 9H6.3z"/><path d="M10 15.6l-.5 4.8M14 15.6l.5 4.8M12 15.6v4.8"/>',
    "info": '<circle cx="12" cy="12" r="8.6"/><path d="M12 10.8v5.6M12 7.6v.2"/>',
}
ic = lambda n: icon(I.get(n, n))


def body(rel):
    anfrage = rel + "kontakt/#anfrage"
    fotos = mailto("Standortfotos für meine Montage")
    down = f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONS["down"]}</svg>'
    LAZY = ' loading="lazy"'
    contact = lambda cls: f'<p class="{cls}"><a href="mailto:{S["email"]}">{S["email"]}</a><a href="tel:{S["phone_href"]}">{S["phone"]}</a></p>'
    img = lambda f, alt, w, h, extra="": f'<img src="{rel}assets/img/installation/{f}" alt="{alt}" width="{w}" height="{h}"{extra}>'

    strip = [
        ("people", "Ein Ansprechpartner", "Hardware, Montage und Einrichtung aus einer Hand."),
        ("gear", "Geprüfte Übergabe", "Eingerichtet, getestet und erklärt."),
        ("pin", 'Persönlich in <span class="nw">Rhein-Main</span>', "Lieferung deutschlandweit, Montage je nach Region."),
        ("monitor", "Vorhandene Displays", "Montage nach technischer Prüfung."),
    ]
    strip_html = "".join(f'<div class="ins-strip-item">{ic(i)}<div><strong>{t}</strong><p>{d}</p></div></div>' for i, t, d in strip)

    cards = [
        ("beispiel-restaurant-menueboards.jpg", 406, 347, "Drei ausgerichtete Menüboards über einer Restauranttheke", "Menüboards in der Gastronomie", "Ausgerichtet auf den Blick Ihrer Gäste."),
        ("beispiel-eingang-stele.jpg", 401, 347, "Digitale Stele im gläsernen Eingangsbereich eines Geschäfts", "Stelen im Eingangsbereich", "Gut sichtbar, ohne den Weg zu versperren."),
        ("beispiel-outdoor-stele.jpg", 402, 347, "Digitale Info-Stele auf einem Platz in der Innenstadt", "Info-Stelen im Außenbereich", "Geplant für Standort und Witterung."),
        ("beispiel-empfang-videowand.jpg", 412, 347, "Videowand aus vier Displays hinter einem Empfangstresen", "Videowände am Empfang", "Panel für Panel auf einer Linie."),
    ]
    cards_html = "".join(f'<figure class="ins-card">{img(f, a, w, h, LAZY)}<figcaption><h3>{t}</h3><p>{d}</p></figcaption></figure>' for f, w, h, a, t, d in cards)

    scope = [
        ("scan", "Standortprüfung", "Fläche, Sichtachsen und bauliche Voraussetzungen."),
        ("bracket", "Passende Halterungen", "Ausgewählt für Display und Untergrund."),
        ("wrench", "Fachgerechte Montage", "Sorgfältig positioniert und ausgerichtet."),
        ("cable", "Kabelmanagement", "Geplante Kabelwege, sauberer Abschluss."),
        ("mon-wave", "Geräte-Einrichtung", "Displays, Player und Netzwerk."),
        ("doc-up", "Inhalte aufspielen", "Ihre Inhalte, direkt auf dem Display geprüft."),
        ("mon-check", "Funktionstest", "Wiedergabe, Verbindung und Steuerung."),
        ("people", "Einweisung Ihres Teams", "Abläufe und Ansprechpartner erklärt."),
    ]
    scope_html = "".join(f'<li>{ic(i)}<div><strong>{t}</strong><span>{d}</span></div></li>' for i, t, d in scope)

    mounts = [
        ("befestigung-wand.jpg", 320, 333, "Flaches Display an einer hellen Wand montiert", "Wandmontage", "Flach und sicher, wo die Wand trägt."),
        ("befestigung-decke.jpg", 318, 333, "Display an zwei Deckenstangen abgehängt", "Deckenmontage", "Stabil abgehängt, wo die Wand nicht trägt."),
        ("befestigung-stele.jpg", 314, 333, "Freistehende digitale Stele in einer hellen Halle", "Freistehende Stelen", "Flexibel im Raum platziert."),
        ("befestigung-outdoor.jpg", 321, 333, "Digitale Stele im Außenbereich auf festem Sockel", "Outdoor-Installation", "Geplant für Wind und Wetter."),
        ("befestigung-multiscreen.jpg", 320, 333, "Vier Menüboards in einer Reihe über einer Theke", "Multi-Screen-Systeme", "Bündig und auf gleicher Höhe."),
    ]
    mounts_html = "".join(f'<figure class="ins-card">{img(f, a, w, h, LAZY)}<figcaption><h3>{t}</h3><p>{d}</p></figcaption></figure>' for f, w, h, a, t, d in mounts)

    steps = [
        ("search", "Standortprüfung", "Maße, Untergrund und Zeitplan."),
        ("doc", "Planung & Vorbereitung", "Halterungen, Geräte und Material."),
        ("truck", "Anlieferung", "Abgestimmte Lieferung an Ihren Standort."),
        ("gear", "Montage & Einrichtung", "Montieren, anschließen, ausrichten, testen."),
        ("check", "Übergabe", "Ein laufendes System und klare nächste Schritte."),
    ]
    steps_html = "".join(f'<div><span class="ring">{ic(i)}</span><b>{n:02d}</b><h3>{t}</h3><p>{d}</p></div>' for n, (i, t, d) in enumerate(steps, 1))

    checks = ["Untergrund und Traglast", "Strom und Kabelwege", "Netzwerkzugang", "Belüftung und Wärme", "Schutz und Reinigung", "Display- und Content-Format"]
    checks_html = "".join(f"<li>{ico('one')}{c}</li>" for c in checks)

    hand = [
        ("one", "Getestetes System", "Display, Player, Netzwerk und Inhalte."),
        ("person", "Klare Abläufe", "Inhalte ändern Sie per Nachricht an uns."),
        ("headset", "Direkter Kontakt", "Sie wissen, wen Sie anrufen."),
        ("broom", "Aufgeräumte Fläche", "Verpackung und Montagereste entfernt."),
    ]
    hand_html = "".join(f'<div>{ic(i)}<h3>{t}</h3><p>{d}</p></div>' for i, t, d in hand)

    hysn = ["Geräte und passende Halterungen", "Kabel, Player und Werkzeug", "Ausrichtung und Einrichtung", "Content-Test und Funktionsprüfung", "Koordination und Übergabe"]
    site = ["Zugang und freie Montagefläche", "Stromanschluss oder abgestimmte Vorbereitung", "Netzwerkzugang, wo nötig", "Ansprechpartner vor Ort für Freigaben", "Zustimmung des Eigentümers, wo nötig"]
    li = lambda xs: "".join(f"<li>{ico('one')}{x}</li>" for x in xs)

    faq = [
        ("Übernimmt HYSN auch Elektroarbeiten?", "Wir planen den Strombedarf und stimmen feste Elektroarbeiten mit qualifizierten Elektrofachkräften oder Ihrer Haustechnik ab. Wer was übernimmt, legen wir vor dem Termin fest.", True),
        ("Wie lange dauert die Montage?", "Das hängt von Anzahl und Größe der Displays, vom Untergrund und vom Zugang ab. Nach der Standortprüfung nennen wir Ihnen einen realistischen Zeitrahmen.", False),
        ("Kann außerhalb der Öffnungszeiten montiert werden?", "Nach Absprache ja. Nennen Sie uns Ihre Öffnungszeiten und Ihren Wunschtermin frühzeitig, dann planen wir die Montage so, dass Ihr Betrieb möglichst wenig gestört wird.", False),
        ("Was, wenn die Wand nicht geeignet ist?", "Dann zeigen wir Ihnen Alternativen, etwa eine andere Position, eine Deckenmontage oder eine freistehende Stele. Das klären wir bei der Standortprüfung, vor dem ersten Bohrloch.", False),
        ("Binden Sie die Displays in unser Netzwerk ein?", "Ja, in Abstimmung mit Ihrer IT. Wir richten Displays und Player ein, verbinden sie mit dem Netzwerk und prüfen die Wiedergabe vor Ort. Die Anforderungen klären wir vorab.", False),
        ("Wer kümmert sich um Genehmigungen im Außenbereich?", "Das ist projektabhängig. Wir klären mit Ihnen früh, welche Genehmigungen nötig sind und wer sie einholt. Die Zuständigkeit wird im Angebot festgelegt.", False),
        ("Sind Halterungen und Werkzeug enthalten?", "Die geplanten Halterungen, Kabel, Player und das Montagewerkzeug bringen wir mit. Was genau enthalten ist, steht in Ihrem Angebot.", False),
        ("Montieren Sie auch Displays, die wir anderswo gekauft haben?", "Grundsätzlich ja, nach technischer Prüfung. Wir prüfen vorab Maße, Gewicht, Zustand und Kompatibilität und sagen Ihnen offen, ob eine Montage sinnvoll ist.", False),
    ]
    faq_html = "".join(f'<details{" open" if o else ""}><summary>{H.escape(q)}</summary><p>{H.escape(a)}</p></details>' for q, a, o in faq)

    return f"""
<section class="chero ins-hero"><div class="chero-img">{img("montage-hero-menueboards.jpg", "Drei bündig montierte Menüboards über einer Restauranttheke, rechts ein Techniker mit Tablet", 1128, 626, ' fetchpriority="high"')}</div>
  <div class="wrap"><div class="chero-text">
    <span class="eyebrow">Installation &amp; Montage</span>
    <h1>Sauber montiert.<br>Voll einsatzbereit.</h1>
    <p class="lead">Menüboards, Stelen, Displays und Videowände: montiert, eingerichtet und getestet für Ihren Standort.</p>
    <div class="actions">{btn(anfrage, "Montage anfragen")}<a class="btn ins-ghost" href="#beispiele">Beispiele ansehen{down}</a></div>
    <p class="note">Ein Ansprechpartner von der Standortprüfung bis zur Übergabe.</p>
  </div></div>
</section>

<section class="ins-strip" aria-label="Das Wichtigste in Kürze"><div class="wrap">{strip_html}</div></section>

<section class="ins-result" id="beispiele"><div class="wrap">
  <div class="ins-head">
    <div><span class="eyebrow">Das fertige Ergebnis</span><h2>Als gehörte es<br>schon immer dazu.</h2><p class="sub">Präzise ausgerichtet. Durchdacht platziert. Sauber abgeschlossen.</p></div>
    <p class="ins-label">Beispielhafte Darstellungen</p>
  </div>
  <div class="ins-cards">{cards_html}</div>
</div></section>

<section class="ins-scope"><div class="wrap">
  <div class="ins-scope-text">
    <span class="eyebrow">Mehr als Montage</span>
    <h2>Eine Installation.<br>Ein laufendes System.</h2>
    <p class="sub">Montage, technische Einrichtung und Übergabe, abgestimmt auf Ihren Standort.</p>
    <p class="small">Der genaue Umfang wird in Ihrem Angebot festgelegt.</p>
  </div>
  <ul class="ins-scope-list">{scope_html}</ul>
</div></section>

<section class="ins-mounts"><div class="wrap">
  <span class="eyebrow">Die richtige Befestigung</span>
  <h2>Jeder Raum braucht<br>den passenden Halt.</h2>
  <div class="ins-cards ins-cards--5">{mounts_html}</div>
</div></section>

<section class="next ins-ablauf"><div class="wrap">
  <div><span class="eyebrow">Von der Prüfung zur Übergabe</span><h2>Fünf Schritte.<br>Klar geplant.</h2></div>
  <div class="flow">{steps_html}</div>
</div></section>

<section class="ins-ready"><div class="wrap">
  <div class="ins-ready-img">{img("montage-wasserwaage.jpg", "Techniker richtet eine Wandhalterung mit der Wasserwaage aus, daneben ein Tablet mit Grundriss", 913, 550, ' loading="lazy"')}</div>
  <div class="ins-ready-text">
    <span class="eyebrow">Planung vor dem ersten Bohrloch</span>
    <h2>Keine Wand<br>ist wie die andere.</h2>
    <p class="sub">Glas, Trockenbau, Mietflächen, enge Grundrisse und Außenstandorte brauchen die richtige Einschätzung.</p>
    <ul class="ins-checks">{checks_html}</ul>
    <div class="ins-inset">{ic("info")}<p><strong>Vorhandene Displays?</strong> Wir prüfen zuerst Maße, Gewicht, Zustand und Kompatibilität.</p></div>
    <p class="small">Feste Elektroarbeiten stimmen wir mit qualifizierten Elektrofachkräften ab. Genehmigungen für Außenstandorte sind projektabhängig.</p>
  </div>
</div></section>

<section class="ins-hand"><div class="wrap">
  <div><span class="eyebrow">Die Übergabe</span><h2>Bereit für Ihr Team.<br>Nicht nur montiert.</h2></div>
  <div class="ins-hand-grid">{hand_html}</div>
</div></section>

<section class="place ins-region"><div class="wrap">
  <div>
    <span class="eyebrow">Nah an Ihrem Projekt</span>
    <h2>Zuhause in Rhein-Main.<br>Lieferung deutschlandweit.</h2>
    <p class="sub">Unsere Kernregion: Weiterstadt, Darmstadt, Frankfurt, Offenbach, Mainz und Wiesbaden. Geliefert wird deutschlandweit; Montage vor Ort je nach Region und Projektumfang.</p>
  </div>
  <svg class="map" viewBox="-10 -10 370 492" role="img" aria-label="Deutschlandkarte mit markierter Region Rhein-Main">
    <path class="land" d="{MAP}"/><path class="area" d="M78 262c14-14 40-18 58-8 16 9 22 28 16 46-6 17-22 30-42 32-21 2-40-8-46-26-5-15 2-32 14-44z"/>
    <circle class="dot" cx="109.5" cy="300" r="6"/><text x="124" y="306">Rhein-Main</text></svg>
  <div class="ins-date">{ico("cal")}<div>
    <h3>Ein Eröffnungstermin im Blick?</h3>
    <p>Nennen Sie uns Ihren Wunschtermin frühzeitig. Montage außerhalb der Öffnungszeiten nach Absprache.</p>
    {btn(anfrage, "Wunschtermin abstimmen")}
  </div></div>
</div></section>

<section class="ins-ba"><div class="wrap">
  <div><span class="eyebrow">Der Unterschied liegt im Detail</span><h2>Von improvisiert<br>zu integriert.</h2><p class="small">Beispielhafter Vergleich</p></div>
  <div class="ins-ba-pair">
    <figure><div class="ins-ba-img">{img("vergleich-vorher.jpg", "Vorher: drei ungleich hoch montierte Displays, Kabel hängen sichtbar von der Decke und an der Wand", 581, 274, ' loading="lazy"')}<span class="ins-tag">Vorher</span></div><figcaption>Ungleiche Höhen. Sichtbare Kabel.</figcaption></figure>
    <figure><div class="ins-ba-img">{img("vergleich-nachher.jpg", "Nachher: drei bündig nebeneinander montierte Menüboards ohne sichtbare Kabel", 598, 270, ' loading="lazy"')}<span class="ins-tag">Nachher</span></div><figcaption>Gleiche Höhe. Keine sichtbaren Kabel.</figcaption></figure>
  </div>
</div></section>

<section class="ins-split"><div class="wrap">
  <h2>Ein klarer Plan<br>vor dem Termin.</h2>
  <div class="ins-split-col"><h3>Das übernimmt HYSN</h3><ul>{li(hysn)}</ul></div>
  <div class="ins-split-col"><h3>Ihr Standort</h3><ul>{li(site)}</ul></div>
  <p class="ins-split-note small">Geräte, Vorbereitung vor Ort und Zuständigkeiten stimmen wir vor dem Termin ab und halten sie im Angebot fest.</p>
</div></section>

<section class="qa ins-qa"><div class="wrap">
  <div><span class="eyebrow">Gut zu wissen</span><h2>Ihre Fragen<br>zur Montage.</h2></div>
  <div class="faq">{faq_html}</div>
</div></section>

<section class="cta ins-cta">{RIBBON}<div class="wrap">
  <div class="cta-text">
    <span class="eyebrow">Ihr nächster Schritt</span>
    <h2>Ihr Display.<br>Montiert und bereit.</h2>
    <p class="sub">Senden Sie uns Fotos vom Standort, ungefähre Maße, Angaben zum Display und Ihren Wunschtermin. Wir zeigen Ihnen den nächsten sinnvollen Schritt.</p>
    <div class="actions">{btn(anfrage, "Montage anfragen")}<a class="btn ins-ghost" href="{fotos}">Standortfotos senden{ARROW}</a></div>
    {contact("ins-cta-contact ins-cta-contact--text")}
    <p class="small">Die erste Einschätzung ist kostenlos und unverbindlich.</p>
  </div>
  <div class="cta-brand"><span>Menschen</span><span>Standorte</span><span>Möglichkeiten</span><i></i><img src="{rel}assets/img/logo/hysn-logo.svg" alt="HYSN" width="1485" height="234">
    {contact("ins-cta-contact")}</div>
</div></section>"""


PAGES = [dict(path="leistungen/installation-montage/index.html", title="Installation & Montage | HYSN Digital Signage",
              desc="Displays, Menüboards, Stelen und Videowände sauber montiert, eingerichtet und getestet. Ein Ansprechpartner von der Standortprüfung bis zur Übergabe.",
              current="leistungen/installation-montage/", body=body, body_class="hero-page", css=["pages/installation.css"])]
