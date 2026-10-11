"""Kontakt: layout follows Static pages/hysn-contact-concept-v1 1.png (reference implementation for the other pages)."""
from _lib import *

def body(rel):
    faq = [
      ("Wer meldet sich bei mir?", "Ein Ansprechpartner von HYSN, persönlich und nicht aus einem Callcenter. Dabei stellen wir Ihnen meist ein paar Fragen zu Ihrem Standort und Ihren Anforderungen.", True),
      ("Verpflichte ich mich damit zu etwas?", "Nein. Das erste Gespräch ist kostenlos und unverbindlich. Sie entscheiden danach, ob und wie es weitergeht.", False),
      ("Was, wenn HYSN nicht die richtige Lösung ist?", "Dann sagen wir Ihnen das offen. Ein Projekt, das an Ihrem Standort nicht funktioniert, hilft niemandem.", False),
      ("Welche Angaben brauchen Sie von mir?", "Standort, Branche und Ihr Ziel genügen für den Anfang. Fotos der Fläche oder ein Grundriss helfen, Größe und Montage einzuschätzen.", False),
    ]
    faq_html = "".join(f'<details{" open" if o else ""}><summary>{H.escape(q)}</summary><p>{H.escape(a)}</p></details>' for q, a, o in faq)
    branchen = ["Gastronomie", "Handel & Supermärkte", "Events & Messen", "Autohäuser", "Bildung", "Praxen & Empfang", "Büro & Unternehmen", "Städte & Kommunen", "Franchise & Filialen", "Sonstiges"]
    opts = '<option value="" selected>Branche auswählen (optional)</option>' + "".join(f"<option>{H.escape(b)}</option>" for b in branchen)
    photos = "mailto:" + S["email"] + "?subject=" + "Standortfotos%20f%C3%BCr%20mein%20Projekt"
    termin = "mailto:" + S["email"] + "?subject=" + "Terminanfrage"
    return f"""
<section class="chero"><div class="chero-img"><img src="{rel}assets/img/kontakt-hero.jpg" alt="Begrüßung in einer hellen Lobby mit großem Hochformat-Display" width="910" height="644" fetchpriority="high"></div>
  <div class="wrap"><div class="chero-text">
    <span class="eyebrow">Kontakt</span>
    <h1>Jedes gute Projekt beginnt mit einem Gespräch.</h1>
    <p class="lead">Erzählen Sie uns von Ihrem Standort und Ihren Zielen. Wir helfen Ihnen, die passende Display-Lösung zu finden, mit ehrlicher Beratung und klaren nächsten Schritten.</p>
    <div class="actions">{btn("#anfrage", "Projekt beschreiben")}{tlink("#direkt", "Lieber anrufen oder mailen", "down", " tlink--plain")}</div>
    <p class="note">{ico("chat")}Persönliche Antwort, kein Callcenter</p>
  </div></div>
</section>

<section class="cform" id="anfrage"><div class="wrap">
  <div class="cform-main">
    <span class="eyebrow">Sprechen wir über Ihr Projekt</span>
    <h2>Ein paar Angaben.<br>Ein sinnvoller erster Schritt.</h2>
    <p class="sub">Kein technisches Briefing nötig. Schreiben Sie einfach, was Sie vorhaben.</p>
    <form data-mailto-form="{S["email"]}" novalidate>
      <div class="form-grid">
        <div class="field"><label for="f-name">Name<b>*</b></label><input id="f-name" name="name" autocomplete="name" required></div>
        <div class="field"><label for="f-email">E-Mail-Adresse<b>*</b></label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="f-firma">Unternehmen</label><input id="f-firma" name="firma" autocomplete="organization"></div>
        <div class="field"><label for="f-tel">Telefon</label><input id="f-tel" name="telefon" type="tel" autocomplete="tel"></div>
        <div class="field field--full"><label for="f-branche">Branche</label><select id="f-branche" name="branche">{opts}</select></div>
        <div class="field field--full"><label for="f-msg">Wie können wir helfen?<b>*</b></label><textarea id="f-msg" name="nachricht" required placeholder="Erzählen Sie uns von Ihrem Projekt, Ihrem Standort oder Ihrer Frage."></textarea></div>
      </div>
      <div class="form-foot">
        <button class="btn" type="submit">Beratung anfragen{ARROW}</button>
        <p class="small">Beim Absenden öffnet sich Ihr E-Mail-Programm mit Ihrer Anfrage. Ihre Angaben nutzen wir nur, um Ihnen zu antworten. <a href="{rel}datenschutz/">Datenschutz</a></p>
        <p class="small" data-sent hidden>Ihr E-Mail-Programm sollte sich jetzt geöffnet haben. Falls nicht, schreiben Sie uns direkt an <a href="mailto:{S["email"]}">{S["email"]}</a>.</p>
      </div>
    </form>
  </div>
  <aside class="cside" aria-label="Was Sie erwarten können">
    <h3>Was Sie erwarten können</h3>
    <div class="expect">{ico("chat")}<div><strong>Eine persönliche Antwort</strong><p>Von einem Ansprechpartner, mit konkreten Rückfragen statt Standardtexten.</p></div></div>
    <div class="expect">{ico("people")}<div><strong>Kein Verkaufsdruck</strong><p>Ein erstes Gespräch, um zu klären, was sinnvoll ist.</p></div></div>
    <div class="expect">{ico("cube")}<div><strong>Ein Partner für alles</strong><p>Hardware, Content, Montage und Betrieb, mit 5 Jahren Garantie auf die Hardware.</p></div></div>
    <div class="direct-mini"><p>Lieber direkt sprechen?</p>
      <a href="tel:{S["phone_href"]}">{ico("phone")}{S["phone"]}</a><a href="mailto:{S["email"]}">{ico("mail")}{S["email"]}</a></div>
    <div class="cside-img"><img src="{rel}assets/img/kontakt-seite.jpg" alt="Büro mit großem Hochformat-Display am Fenster" width="623" height="348" loading="lazy"></div>
  </aside>
</div></section>

<section class="next"><div class="wrap">
  <div><span class="eyebrow">So geht es weiter</span><h2>Klarheit bei<br>jedem Schritt.</h2></div>
  <div class="flow">
    <div><span class="ring">{ico("chat")}</span><b>01</b><h3>Ihre Anfrage kommt an</h3><p>Wir lesen jede Nachricht persönlich.</p></div>
    <div><span class="ring">{ico("pencil")}</span><b>02</b><h3>Wir lernen Ihr Projekt kennen</h3><p>Sie bekommen eine Antwort mit konkreten Rückfragen zu Ihrem Standort.</p></div>
    <div><span class="ring">{ico("doc")}</span><b>03</b><h3>Sie wählen den nächsten Schritt</h3><p>Ein Konzept oder Angebot, nur wenn es passt.</p></div>
  </div>
</div></section>

<section class="ways" id="direkt"><div class="wrap">
  <span class="eyebrow">Ihr bevorzugter Weg zu uns</span>
  <h2>Starten Sie das Gespräch<br>auf Ihre Weise.</h2>
  <div class="ways-grid">
    <div>{ico("phone")}<h3>Telefon</h3><a class="big" href="tel:{S["phone_href"]}">{S["phone"]}</a><p>Für kurze Fragen und eine erste Beratung. Mobil: <a class="nw" href="tel:{S["mobile_href"]}">{S["mobile"]}</a></p>{tlink("tel:" + S["phone_href"], "Anrufen")}</div>
    <div>{ico("mail")}<h3>E-Mail</h3><a class="big" href="mailto:{S["email"]}">{S["email"]}</a><p>Für Pläne, Fotos oder eine Projektbeschreibung.</p>{tlink("mailto:" + S["email"], "E-Mail schreiben")}</div>
    <div>{ico("camera")}<h3>Standortfotos</h3><span class="big">Fotos Ihrer Fläche senden</span><p>Für eine schnelle erste Einschätzung von Größe und Montage.</p>{tlink(photos, "Fotos per E-Mail senden")}</div>
    <div>{ico("cal")}<h3>Termin</h3><span class="big">Einen Termin finden</span><p>Besprechen Sie Ihr Projekt telefonisch, per Video oder vor Ort.</p>{tlink(termin, "Termin anfragen")}</div>
  </div>
</div></section>

<section class="person">
  <div class="person-img"><img src="{rel}assets/img/kontakt-beratung.jpg" alt="Beratungsgespräch am Tisch, im Hintergrund ein großes Display" width="1115" height="502" loading="lazy"></div>
  <div class="person-text">
    <span class="eyebrow">Ihr Ansprechpartner</span>
    <h2>Jemand, der Ihr Projekt versteht.</h2>
    <p class="sub">Im ersten Gespräch geht es um Ihre Fläche, Ihre Ziele und darum, was im Alltag Ihres Standorts funktioniert.</p>
    <p class="org">{S["company"]} / HYSN</p>
    <p class="small">Beratung · Planung · Umsetzung · Betrieb</p>
    {tlink(rel + ("ueber-uns/" if built("ueber-uns/") else "index.html"), "HYSN kennenlernen")}
  </div>
</section>

<section class="place"><div class="wrap">
  <div>
    <span class="eyebrow">Unser Standort</span>
    <h2>Nah an Ihrem Projekt.</h2>
    <p class="sub">Termine nach Absprache: telefonisch, per Video oder bei Ihnen vor Ort. Den passenden nächsten Schritt legen wir gemeinsam fest.</p>
    <div class="addr">{ico("pin")}<div><strong>{S["company"]}</strong>{S["street"]}, {S["zip"]} {S["city"]}<br>Rhein-Main, Deutschland</div></div>
    {btn(termin, "Termin anfragen")}
    <p class="small place-note">Kostenlos und unverbindlich.</p>
  </div>
  <svg class="map" viewBox="-10 -10 370 492" role="img" aria-label="Deutschlandkarte mit markierter Region Rhein-Main">
    <path class="land" d="{MAP}"/><path class="area" d="M78 262c14-14 40-18 58-8 16 9 22 28 16 46-6 17-22 30-42 32-21 2-40-8-46-26-5-15 2-32 14-44z"/>
    <circle class="dot" cx="109.5" cy="300" r="6"/><text x="124" y="306">Rhein-Main</text></svg>
  <div class="stack"><span>Regional</span><span>Persönlich</span><span>Deutschlandweit</span><i></i></div>
</div></section>

<section class="qa"><div class="wrap">
  <div><span class="eyebrow">Bevor Sie schreiben</span><h2>Ein wenig mehr Klarheit.</h2></div>
  <div class="faq">{faq_html}</div>
</div></section>

<section class="cta">{RIBBON}<div class="wrap">
  <div class="cta-text">
    <span class="eyebrow">Kostenloses Erstgespräch</span>
    <h2>Eine Nachricht.<br>Neue Möglichkeiten.</h2>
    <p class="sub">Erzählen Sie uns, was Sie vorhaben. Wir zeigen Ihnen, was als Nächstes sinnvoll ist.</p>
    <div class="actions">{btn("#anfrage", "Projekt besprechen")}<a class="tlink tlink--plain" href="mailto:{S["email"]}">{S["email"]}</a></div>
    <p class="small">Unverbindlich. Sie entscheiden, ob es weitergeht.</p>
  </div>
  <div class="cta-brand"><span>Menschen</span><span>Standorte</span><span>Möglichkeiten</span><i></i><img src="{rel}assets/img/logo/hysn-logo.svg" alt="HYSN" width="1485" height="234"></div>
</div></section>"""


PAGES = [dict(path="kontakt/index.html", title="Kontakt | HYSN Digital Signage",
              desc="Erzählen Sie uns von Ihrem Standort: kostenloses Erstgespräch zu Menüboards, Werbestelen und LED-Wänden. HYSN, Weiterstadt im Rhein-Main-Gebiet.",
              current="kontakt/", body=body, body_class="hero-page")]
