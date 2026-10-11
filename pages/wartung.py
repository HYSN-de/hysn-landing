"""Wartung & Betrieb: layout follows Static pages/hysn-maintenance-support-concept-v1 1.png.
Content changes against the concept: no response-time figure, no monitoring dashboards (now "Fernwartung" with photo and list),
no WhatsApp, no tiers or priorities (now "Beispiel-Pakete", described as starting points), no replacement devices, 5 years hardware warranty stated.
Spacing pass (09.10.2026): the concept's three overlapping sections (support channels, four-step flow, "Erst die Antwort")
are merged into one section "Von der Meldung zur Lösung"; footnotes moved into the section texts; shared .sec/.facts/.steps/.ways-grid/.qa."""
from _lib import *

# page-specific line icons on the 24x24 grid
I = dict(
    laptop='<path d="M5.4 6a1 1 0 0 1 1-1h11.2a1 1 0 0 1 1 1v9H5.4z"/><path d="M3 15h18l-1.1 3H4.1z"/>',
    sliders='<path d="M4 7h3.2M10.8 7H20M4 12h9.2M16.8 12H20M4 17h1.2M8.8 17H20"/><circle cx="9" cy="7" r="1.8"/><circle cx="15" cy="12" r="1.8"/><circle cx="7" cy="17" r="1.8"/>',
    truck='<path d="M3 16.2V6.6h10.6v9.6M13.6 9.6h3.9l2.9 3.2v3.4h-1.5M8.5 16.2h6.6M3 16.2h1.7"/><circle cx="6.6" cy="16.6" r="1.9"/><circle cx="16.9" cy="16.6" r="1.9"/>',
    search='<circle cx="10.6" cy="10.6" r="6.2"/><path d="m15.2 15.2 5 5"/>',
    gear='<circle cx="12" cy="12" r="2.8"/><circle cx="12" cy="12" r="6.4"/><path d="M12 2.8v2.8M12 18.4v2.8M2.8 12h2.8M18.4 12h2.8M5.5 5.5l2 2M16.5 16.5l2 2M5.5 18.5l2-2M16.5 7.5l2-2"/>',
    wrench='<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/>',
    monitor='<rect x="3.4" y="4.6" width="17.2" height="11.6" rx="1"/><path d="M9 20h6M12 16.2V20"/>',
    check='<path d="m5 12.6 4.3 4.3L19 7.2"/>',
    xcircle='<circle cx="12" cy="12" r="8.6"/><path d="m9.2 9.2 5.6 5.6M14.8 9.2l-5.6 5.6"/>',
    restart='<path d="M19.4 12a7.4 7.4 0 1 1-2.2-5.3"/><path d="M19.6 4.4v4.4h-4.4"/>',
    playlist='<path d="M4 6.5h11M4 11h11M4 15.5h6.5"/><path d="m14.6 13.6 5.4 3.2-5.4 3.2z"/>',
)
ic = lambda n, cls="ico": icon(I[n], cls) if n in I else ico(n, cls)
DOWN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v15M6 13l6 6 6-6"/></svg>'


def card_title(t):
    """Card heading with the arrow glued to the last word, so a wrapped title keeps its arrow next to the text."""
    head, _, last = t.rpartition(" ")
    return (head + " " if head else "") + f'<span class="nw">{last}{ARROW}</span>'


def card(rel, f, w, h, alt, title, desc, href):
    return (f'<a class="wb-card" href="{href}"><span class="wb-card-img"><img src="{rel}assets/img/wartung/{f}" alt="{alt}" width="{w}" height="{h}" loading="lazy"></span>'
            f'<span class="wb-card-t">{card_title(title)}</span><span class="wb-card-d">{desc}</span></a>')


def body(rel):
    anfrage = rel + "kontakt/#anfrage"
    stoerung = mailto("Störung an unserem Bildschirm")

    strip = [
        ("people", "Ein Ansprechpartner", "Für Technik, Inhalte und Service-Einsätze."),
        ("laptop", "Zuerst aus der Ferne", "Viele Anliegen lösen wir per Fernwartung."),
        ("pin", "Vor Ort, wenn nötig", "Vorbereitete Einsätze, je nach Region."),
        ("sliders", "Passender Umfang", "Abgestimmt auf Ihre Bildschirme."),
    ]
    strip_html = "".join(f'<div class="fact">{ic(i)}<div><h3>{t}</h3><p>{d}</p></div></div>' for i, t, d in strip)

    services = [
        ("wartung-fernwartung.jpg", 327, 288, "Mitarbeiter prüft auf dem Tablet die Einstellungen eines Wanddisplays", "Fernwartung", "Inhalte, Playlists, Neustarts und Einstellungen aus der Ferne.", "#fernwartung"),
        ("wartung-stoerung.jpg", 330, 287, "Großes Wanddisplay mit Berglandschaft und HYSN-Schriftzug", "Störungshilfe", "Player, Wiedergabe und Konfiguration prüfen.", "#ablauf"),
        ("wartung-inhalte.jpg", 331, 288, "Drei digitale Menüboards mit Speisen und Angeboten", "Inhalts-Updates", "Menüs, Angebote und Aktionen, einfach per Nachricht.", rel + "leistungen/content-creation/"),
        ("wartung-vor-ort.jpg", 329, 288, "Techniker in HYSN-Jacke prüft eine digitale Stele vor Ort", "Vor-Ort-Service", "Hardware- und Standortprüfung, je nach Region.", "#pflege"),
        ("wartung-pflege.jpg", 325, 288, "Hand reinigt einen ausgeschalteten Bildschirm mit einem Mikrofasertuch", "Planmäßige Wartung", "Sichtprüfung, Updates und Bildeinstellungen.", "#pflege"),
    ]
    services_html = "".join(card(rel, *x) for x in services)

    contexts = [
        ("wartung-restaurant.jpg", 240, 300, "Drei Menüboards über der Theke eines Restaurants", "Gastronomie", "Neue Preise per Nachricht, Wiedergabe aus der Ferne geprüft.", "#fernwartung"),
        ("wartung-handel.jpg", 246, 308, "Hochformat-Display im Eingangsbereich eines Supermarkts", "Handel", "Störungen prüfen und Inhalte für Aktionen tauschen.", "#ablauf"),
        ("wartung-aussen.jpg", 252, 315, "Digitale Stele auf einem belebten Platz mit Bäumen", "Außenbereich", "Geplante Sichtprüfung und Pflege der Stele.", "#pflege"),
        ("wartung-standorte.jpg", 208, 260, "Digitale Stele im hellen Foyer eines Bürogebäudes", "Mehrere Standorte", "Ein Ansprechpartner, Inhalte für alle Standorte.", "#umfang"),
    ]
    contexts_html = "".join(card(rel, *x) for x in contexts)

    schritte = [
        ("doc", "01", "Störung melden", "Standort, Bildschirm und ein Foto oder eine kurze Beschreibung."),
        ("search", "02", "Aus der Ferne prüfen", "Player, Verbindung, Inhalte und Einstellungen."),
        ("gear", "03", "Aus der Ferne beheben", "Wo möglich: Neustart oder Einstellungen korrigieren."),
        ("wrench", "04", "Einsatz vor Ort planen", "Falls nötig: die richtigen Leute und das passende Material."),
    ]
    schritte_html = "".join(f'<li><span class="ring">{ic(i)}</span><b>{n}</b><h3>{t}</h3><p>{d}</p></li>' for i, n, t, d in schritte)

    remote = [("playlist", "Inhalte und Playlists prüfen und anpassen"), ("restart", "Bildschirme und Player neu starten"),
              ("gear", "Einstellungen prüfen und korrigieren"), ("chat", "Inhalts-Updates per Nachricht einspielen")]
    remote_html = "".join(f"<li>{ic(i)}<span>{t}</span></li>" for i, t in remote)

    plans = [
        ("Inhaltspflege", "Für einzelne Bildschirme",
         ["Inhalts-Updates per Nachricht", "Neue Preise, Angebote, Aktionen", "Keine Schulung nötig", "Fernwartung bei Störungen", "Vor-Ort-Termine nach Absprache"],
         "Inhaltspflege anfragen"),
        ("Technische Betreuung", "Für Bildschirme im täglichen Einsatz",
         ["Fernwartung und Neustarts", "Fehlersuche aus der Ferne", "Wartung nach Vereinbarung", "Vor-Ort-Service je nach Region", "Inhalts-Updates nach Umfang"],
         "Betreuung anfragen"),
        ("Rundum-Betrieb", "Für mehrere Standorte und Stelen",
         ["Ein Ansprechpartner für alles", "Inhalte für alle Standorte", "Fernwartung und Updates", "Wartungsbesuche vorausgeplant", "Vor-Ort-Einsätze koordiniert"],
         "Rundum-Betrieb anfragen"),
    ]
    plans_html = "".join(
        f'<div class="wb-plan"><div class="wb-plan-head"><h3>{t}</h3><p class="wb-plan-for">{f}</p></div><ul>' + "".join(f"<li>{ic('check')}{x}</li>" for x in rows)
        + f'</ul>{btn(anfrage, b)}</div>' for t, f, rows, b in plans)

    care = [("Sichtprüfung", "Gehäuse, Halterungen, Belüftung und sichtbare Abnutzung."),
            ("Software-Updates", "Firmware und Player-Einstellungen, wenn nötig."),
            ("Bildeinstellungen", "Helligkeit, Format und Sichtbedingungen am Standort."),
            ("Inhalte prüfen", "Laufen die richtigen Inhalte zur richtigen Zeit?")]
    care_html = "".join(f"<li>{ic('one')}<strong>{t}</strong><span>{d}</span></li>" for t, d in care)

    incl = ["Fernwartung von Inhalten und Einstellungen", "Inhaltsänderungen im vereinbarten Umfang", "Planmäßige Wartungsbesuche wie vereinbart", "5 Jahre Garantie auf die Hardware von HYSN"]
    excl = ["Schäden durch äußere Einwirkung oder falsche Nutzung", "Fremdgeräte, die wir noch nicht geprüft haben", "Umzug von Bildschirmen oder größere Umbauten", "Inhaltsänderungen über den vereinbarten Umfang hinaus"]
    incl_html = "".join(f"<li>{ic('check')}{x}</li>" for x in incl)
    excl_html = "".join(f"<li>{ic('xcircle')}{x}</li>" for x in excl)

    faq = [
        ("Wie melden wir eine Störung?", "Rufen Sie uns an oder schreiben Sie eine E-Mail mit Standort, Gerät und dem sichtbaren Problem. Ein Foto oder ein kurzes Video hilft bei der ersten Einschätzung.", True),
        ("Wie erreichen wir Sie?", "Per Telefon oder E-Mail. Sie sprechen mit einem persönlichen Ansprechpartner, nicht mit einem Callcenter.", False),
        ("Was passiert, wenn ein Bildschirm komplett ausfällt?", "Zuerst prüfen wir aus der Ferne, ob Verbindung, Player oder Einstellungen die Ursache sind. Lässt sich das so nicht lösen, planen wir einen Einsatz vor Ort.", False),
        ("Wie oft kommt jemand zur Wartung vorbei?", "Das legen wir in Ihrem Wartungspaket fest, abgestimmt auf Standort, Gerät und Nutzung. Bei Bedarf prüfen und passen wir Einstellungen auch aus der Ferne an.", False),
        ("Wie ändern wir unsere Inhalte?", "Per Nachricht: Schicken Sie uns neue Preise, Bilder oder Texte, wir spielen sie ein. Eine Schulung ist dafür nicht nötig.", False),
        ("Welcher Umfang passt zu uns?", "Das klären wir im Gespräch. Die drei Beispiel-Pakete auf dieser Seite sind ein Ausgangspunkt. Den tatsächlichen Umfang vereinbaren wir individuell und halten ihn im Angebot fest.", False),
        ("Betreuen Sie auch Bildschirme anderer Anbieter?", "Das prüfen wir im ersten Gespräch. Wir schauen uns Geräte, Player und Zugang an und sagen Ihnen offen, ob und wie eine Betreuung möglich ist.", False),
        ("Welche Garantie gilt für die Hardware?", "Auf die Hardware von HYSN gibt es 5 Jahre Garantie. Die Einzelheiten stehen in Ihrem Angebot.", False),
    ]
    faq_html = "".join(f'<details{" open" if o else ""}><summary>{H.escape(q)}</summary><p>{H.escape(a)}</p></details>' for q, a, o in faq)

    return f"""
<section class="chero wb-hero"><div class="chero-img"><img src="{rel}assets/img/wartung/wartung-hero.jpg" alt="Servicetechniker in HYSN-Jacke prüft mit dem Tablet eine digitale Stele im Freien" width="922" height="456" fetchpriority="high"></div>
  <div class="wrap"><div class="chero-text">
    <span class="eyebrow">Wartung &amp; Betrieb</span>
    <h1>Ihre Bildschirme<br class="wb-m"> laufen.<br class="wb-d"> Wenn nicht,<br class="wb-m"> sind wir da.</h1>
    <p class="lead">Fernwartung, planmäßige Wartung und Vor-Ort-Service für Displays, Menüboards, digitale Stelen und LED-Wände.</p>
    <div class="actions">{btn(anfrage, "Wartung anfragen")}<a class="btn btn--ghost" href="#umfang">Pakete ansehen{DOWN}</a></div>
    <p class="note">{ic("monitor")}Auch für Bildschirme, die nicht von HYSN stammen – wir prüfen das im ersten Gespräch.</p>
  </div></div>
</section>

<section class="facts wb-facts"><h2 class="vh">Auf einen Blick</h2><div class="wrap">{strip_html}</div></section>

<section class="sec sec--band wb-services"><div class="wrap">
  <div class="sec-head">
    <span class="eyebrow">Betreuung nach der Installation</span>
    <h2>Alles, was Ihre Bildschirme<br>am Laufen hält.</h2>
    <p class="sub">Welche Leistungen Sie nutzen, richtet sich nach Ihrem System und dem vereinbarten Umfang.</p>
  </div>
  <div class="wb-cards wb-cards--5">{services_html}</div>
</div></section>

<section class="sec wb-help" id="ablauf"><div class="wrap">
  <div class="sec-head">
    <span class="eyebrow">Von der Meldung zur Lösung</span>
    <h2>Ein Problem.<br>Ein klarer Weg zu uns.</h2>
    <p class="sub">Ein Ansprechpartner, persönlich von der Meldung bis zur Lösung. Zuerst bekommen Sie eine technische Einschätzung und den nächsten Schritt. Wie lange eine Reparatur dauert, hängt von der Störung ab.</p>
  </div>
  <ol class="steps">{schritte_html}</ol>
  <div class="wb-reach" id="kanaele">
    <h3 class="eyebrow">Ihr Draht zu uns</h3>
    <div class="ways-grid">
      <div>{ic("phone")}<h3>Telefon</h3><a class="big" href="tel:{S["phone_href"]}">{S["phone"]}</a><p>Für Störungen im laufenden Betrieb. Mobil <a class="nw" href="tel:{S["mobile_href"]}">{S["mobile"]}</a></p></div>
      <div>{ic("camera")}<h3>Foto oder Video</h3><a class="big" href="{stoerung}">Störung zeigen</a><p>Ein Foto oder kurzes Video per E-Mail hilft bei der ersten Einschätzung.</p></div>
      <div>{ic("mail")}<h3>E-Mail</h3><a class="big" href="mailto:{S["email"]}">{S["email"]}</a><p>Für Inhalts-Updates und dokumentierte Anfragen.</p></div>
      <div>{ic("truck")}<h3>Vor-Ort-Service</h3><span class="big">Nach der Diagnose</span><p>Persönlich im Rhein-Main-Gebiet, sonst je nach Region.</p></div>
    </div>
  </div>
  <p class="sec-note">Welche Schritte nötig sind, hängt von der Störung, dem Zugang und dem vereinbarten Umfang ab.</p>
</div></section>

<section class="sec sec--band wb-remote" id="fernwartung"><div class="wrap">
  <div class="wb-remote-text">
    <span class="eyebrow">Fernwartung</span>
    <h2>Aus der Ferne geprüft.<br>Oft ohne Anfahrt gelöst.</h2>
    <p class="sub">Viele Anliegen erledigen wir per Fernzugriff: Wir prüfen und ändern Inhalte, Playlists und Einstellungen und starten Geräte bei Bedarf neu, ohne dass jemand zu Ihnen kommen muss. Ob Fernwartung für Ihre Geräte möglich ist, prüfen wir vorab.</p>
    <div class="wb-points">
      <div>{ic("people")}<span>Ein fester Ansprechpartner</span></div>
      <div>{ic("pin")}<span>Für jeden Ihrer Standorte</span></div>
      <div>{ic("chat")}<span>Inhalts-Updates per Nachricht</span></div>
    </div>
  </div>
  <div class="wb-remote-media">
    <div class="wb-remote-img"><img src="{rel}assets/img/wartung/wartung-fernwartung-gross.jpg" alt="Servicetechniker in HYSN-Jacke stellt per Tablet ein großes Wanddisplay ein" width="550" height="244" loading="lazy"></div>
    <div class="wb-remote-list"><span class="eyebrow">Aus der Ferne erledigt</span><ul>{remote_html}</ul></div>
  </div>
</div></section>

<section class="sec wb-contexts"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Wartung im Alltag</span><h2>Andere Orte.<br>Derselbe Ablauf.</h2></div>
  <div class="wb-cards wb-cards--4">{contexts_html}</div>
  <p class="sec-note">Beispielhafte Einsatzszenarien</p>
</div></section>

<section class="sec sec--band wb-plans" id="umfang"><div class="wrap">
  <div class="sec-head">
    <span class="eyebrow">Beispiel-Pakete</span>
    <h2>Der Umfang, der<br>zu Ihnen passt.</h2>
    <p class="sub"><strong>Umfang wird individuell vereinbart.</strong> Leistungen, Einsätze und Kosten halten wir im Angebot fest.</p>
  </div>
  <div class="wb-plans-grid">{plans_html}</div>
</div></section>

<section class="sec wb-care" id="pflege"><div class="wrap">
  <div class="wb-care-img"><img src="{rel}assets/img/wartung/wartung-wartungsbesuch.jpg" alt="Digitale Stele im Außenbereich zwischen Bäumen" width="316" height="307" loading="lazy"></div>
  <div class="wb-care-text">
    <span class="eyebrow">Vorausplanen</span>
    <h2>Wartung fest<br>im Kalender.</h2>
    <p class="sub">Wie oft wir vorbeikommen, legen wir in Ihrem Wartungspaket fest.</p>
    <ul class="wb-care-list">{care_html}</ul>
    <p class="wb-route"><span>Einsatz nötig?</span><b>Diagnose{ARROW}</b><b>Zugang planen{ARROW}</b><b>Material vorbereiten{ARROW}</b><b>Testen und dokumentieren</b></p>
  </div>
</div></section>

<section class="sec sec--band wb-cover"><div class="wrap split">
  <div class="sec-head"><span class="eyebrow">Klarer Rahmen</span><h2>Was dazugehört.<br>Was extra ist.</h2></div>
  <div class="wb-cover-cols">
    <div><h3>Enthalten nach Vereinbarung</h3><ul class="wb-in">{incl_html}</ul></div>
    <div><h3>Gesondert zu klären</h3><ul class="wb-out">{excl_html}</ul></div>
  </div>
</div></section>

<section class="qa wb-qa"><div class="wrap">
  <div><span class="eyebrow">Gut zu wissen</span><h2>Ihre Fragen.<br>Unsere Antworten.</h2></div>
  <div class="faq">{faq_html}</div>
</div></section>

<section class="cta wb-cta">{RIBBON}<div class="wrap">
  <div class="cta-text">
    <div>
      <span class="eyebrow">Betreuung, die mitläuft</span>
      <h2>Support planen.<br>Den Kopf frei behalten.</h2>
      <p class="sub">Erzählen Sie uns von Ihren Bildschirmen, Standorten und Ihrem Alltag. Wir schlagen Ihnen einen passenden Umfang vor.</p>
    </div>
    <div>
      <div class="actions">{btn(anfrage, "Wartung anfragen")}{btn("tel:" + S["phone_href"], "Team anrufen", ghost=True)}</div>
      <p class="wb-direct"><a href="mailto:{S["email"]}">{S["email"]}</a><a href="tel:{S["phone_href"]}">{S["phone"]}</a></p>
      <p class="small">Erstgespräch kostenlos und unverbindlich.</p>
    </div>
  </div>
  <div class="cta-brand"><span>Menschen</span><span>Standorte</span><span>Möglichkeiten</span><i></i><img src="{rel}assets/img/logo/hysn-logo.svg" alt="HYSN" width="1485" height="234"></div>
</div></section>"""


PAGES = [dict(path="leistungen/wartung-betrieb/index.html", title="Wartung & Betrieb | HYSN Digital Signage",
              desc="Fernwartung, planmäßige Wartung und Vor-Ort-Service für Displays, Menüboards und Stelen. Ein Ansprechpartner, 5 Jahre Garantie auf die Hardware. HYSN, Rhein-Main.",
              current="leistungen/wartung-betrieb/", body=body, body_class="hero-page", css=["pages/wartung.css"])]
