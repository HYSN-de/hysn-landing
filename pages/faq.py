"""FAQ: layout follows Static pages/hysn-faq-concept-v1 1.png.
Sections: photo hero, search with five quick links, sticky topic sidebar + eight accordion groups (6 questions each),
direct help strip, closing ribbon banner. Search is a client-side live filter (assets/js/pages/faq.js)."""
from _lib import *

# Page-specific line icons on the 24x24 grid (thin strokes, no fills, like the shared set).
PI = {
 "info":    '<circle cx="12" cy="12" r="8.6"/><path d="M12 10.8v5.6M12 7.7v.1"/>',
 "tag":     '<path d="M3.6 12.2V4.6a1 1 0 0 1 1-1h7.6l8.2 8.2a1.4 1.4 0 0 1 0 2l-6.6 6.6a1.4 1.4 0 0 1-2 0z"/><circle cx="8.2" cy="8.2" r="1.5"/>',
 "layers":  '<path d="M12 3.6 20.4 8 12 12.4 3.6 8z"/><path d="m3.6 12 8.4 4.4 8.4-4.4M3.6 16l8.4 4.4 8.4-4.4"/>',
 "wrench":  '<path d="M14.6 6.4a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.4-3.4a5.6 5.6 0 0 1-7.4 7.4l-6.3 6.3a2 2 0 0 1-2.8-2.8l6.3-6.3a5.6 5.6 0 0 1 7.4-7.4z"/>',
 "image":   '<rect x="3.4" y="4.4" width="17.2" height="15.2" rx="1.2"/><circle cx="8.6" cy="9.2" r="1.6"/><path d="m3.8 17.6 5-4.8 3.6 3.2 3.4-3 4.6 4.2"/>',
 "headset": '<path d="M4.4 15v-3a7.6 7.6 0 0 1 15.2 0v3"/><path d="M4.4 13.4h2.4v5.2H5.6a1.2 1.2 0 0 1-1.2-1.2zM19.6 13.4h-2.4v5.2h1.2a1.2 1.2 0 0 0 1.2-1.2z"/><path d="M18.4 18.6c0 1.4-1.6 2.2-4.4 2.2"/>',
 "chart":   '<rect x="4" y="12.4" width="3.6" height="7.6" rx="1.8"/><rect x="10.2" y="7.6" width="3.6" height="12.4" rx="1.8"/><rect x="16.4" y="3.8" width="3.6" height="16.2" rx="1.8"/>',
 "doc":     ICONS["doc"],
 "search":  '<circle cx="10.6" cy="10.6" r="6.6"/><path d="m15.4 15.4 5 5"/>',
}
pi = lambda n: icon(PI[n])

PHONE, EMAIL = SITE["phone"], SITE["email"]

# (id, sidebar/heading title, icon, links [(href, label)], questions [(id, question, answer, example or None)])
CATS = [
 ("allgemein", "Allgemein & Einstieg", "info", [], [
  ("allgemein-angebot", "Was bietet HYSN genau an?",
   "Digitale Bildschirme mit allem, was dazugehört: Beratung, Hardware, Content, Montage und Betrieb aus einer Hand. Sie haben einen Ansprechpartner statt vieler Dienstleister. An geeigneten Standorten können Bildschirme über unser Werbenetzwerk hyads zusätzlich Werbeeinnahmen bringen.", None),
  ("allgemein-zielgruppe", "Für wen ist HYSN das Richtige?",
   "Für Gastronomie, Handel und Filialbetriebe, für Städte und Kommunen sowie für Standortpartner, die ihre Fläche für Werbung öffnen möchten. Ein Beispiel: Bei Haus des Döners laufen seit Juni 2025 drei digitale Menüboards an einem Standort, jeden Tag. Ob ein Bildschirm an Ihrem Standort einen klaren Zweck erfüllt, klären wir im Erstgespräch.", None),
  ("allgemein-start", "Wie starten wir ein Projekt?",
   "Mit einer kurzen Nachricht oder einem Anruf. Im kostenlosen Erstgespräch klären wir Standort, Ziel und Rahmen; Fotos Ihrer Fläche helfen dabei. Danach erhalten Sie ein schriftliches Angebot und entscheiden in Ruhe, ob es weitergeht.", None),
  ("allgemein-dauer", "Wie lange dauert es bis zum laufenden Bildschirm?",
   "Das hängt vor allem von Hardware, Montage und Content-Umfang ab. Ein einzelnes Menüboard ist schneller umgesetzt als eine Lösung für mehrere Standorte. Einen konkreten Zeitplan erhalten Sie mit dem Angebot.", None),
  ("allgemein-region", "Wo ist HYSN tätig?",
   f"Unser Sitz ist in {SITE['city']} im Rhein-Main-Gebiet. Hier betreuen wir Sie persönlich vor Ort, geliefert wird deutschlandweit. Wie Montage und Service vor Ort außerhalb der Region laufen, klären wir im Angebot.", None),
  ("allgemein-komplett", "Liefert HYSN nur Hardware oder alles aus einer Hand?",
   "Unser Ansatz ist die Lösung aus einer Hand: Beratung, Hardware, Content, Montage und Betrieb kommen von uns, Sie müssen keine Einzelgewerke koordinieren. Welche dieser Leistungen Sie tatsächlich brauchen, klären wir gemeinsam.", None),
 ]),
 ("preise", "Preise & Investition", "tag", [("kontakt/#anfrage", "Projekt besprechen")], [
  ("preise-kosten", "Was kostet ein Bildschirmsystem?",
   "Das hängt von Bildschirmtyp, Größe, Anzahl, Montage und Content ab, deshalb nennen wir keinen Pauschalpreis. Nach dem Erstgespräch erhalten Sie ein Angebot mit klarem Leistungsumfang und Preis.", None),
  ("preise-minimum", "Gibt es eine Mindestinvestition?",
   "Einen pauschalen Mindestbetrag gibt es nicht; der Umfang richtet sich nach Ihrem Projekt und steht im Angebot. Sprechen Sie uns auch an, wenn Sie zunächst mit einem einzelnen Bildschirm beginnen möchten.", None),
  ("preise-modelle", "Welche Finanzierungsmodelle gibt es?",
   "Drei: Kauf, Co-Investment oder Betreibermodell. Beim Kauf gehört die Hardware Ihnen, beim Co-Investment teilen wir Investition und Werbeerlöse, beim Betreibermodell investiert HYSN und Sie erhalten einen Anteil an den Werbeeinnahmen. Welches Modell passt, hängt vor allem davon ab, ob auf dem Bildschirm Werbung laufen soll.", None),
  ("preise-umfang", "Was ist im Angebot enthalten?",
   "Der vereinbarte Umfang Ihres Projekts: Hardware, Montage und Content, auf Wunsch auch ein Wartungspaket. Optionale Leistungen sind darin getrennt aufgeführt. So sehen Sie vor der Entscheidung, wofür Sie bezahlen.", None),
  ("preise-kauf", "Müssen wir die Bildschirme kaufen?",
   "Nein. Neben dem Kauf gibt es das Co-Investment und das Betreibermodell, bei dem HYSN die Hardware finanziert und über Werbeeinnahmen refinanziert. Das Betreibermodell kommt vor allem für Standorte infrage, an denen Werbung gezeigt werden kann.", None),
  ("preise-individuell", "Warum gibt es keine Preisliste?",
   "Weil kein Standort wie der andere ist: Wandaufbau, Lichtverhältnisse, Bildschirmgröße und Content-Umfang verändern den Aufwand deutlich. Ein individuelles Angebot zeigt Ihnen von Anfang an, was Ihr Projekt tatsächlich kostet. Einen Richtwert gibt es nur für Werbekunden im hyads-Netzwerk: Lokale Werbung auf einer Stele kostet ab ca. 99 € im Monat.", None),
 ]),
 ("hardware", "Hardware & Technik", "layers", [], [
  ("hardware-groesse", "Welche Bildschirmgröße passt zu uns?",
   "Das hängt vom Betrachtungsabstand, vom Raum, vom Lichteinfall und davon ab, was gezeigt werden soll. Wir sehen uns Ihre Fläche an, gern zuerst anhand von Fotos, und empfehlen dann Größe, Format und Montageart.", None),
  ("hardware-led-lcd", "Was ist der Unterschied zwischen LED und LCD?",
   "LCD-Displays zeigen auf kurze Distanz ein sehr feines Bild und eignen sich etwa für Menüboards und Innenräume. LED-Wände bestehen aus Modulen, lassen sich in großen Formaten bauen und sind sehr hell, sinnvoll für große Flächen und größere Abstände. Was an Ihrem Standort passt, klären wir in der Beratung.", None),
  ("hardware-aussen", "Funktionieren die Bildschirme auch im Außenbereich?",
   "Dafür braucht es spezielle Geräte, die wetterfest und deutlich heller sind als Innen-Displays; ein normaler Innenbildschirm ist für draußen nicht geeignet. Ob eine Außenlösung an Ihrem Standort sinnvoll und möglich ist, prüfen wir im Erstgespräch.", None),
  ("hardware-sonne", "Ist der Bildschirm auch bei Sonnenlicht gut lesbar?",
   "Das hängt von der Helligkeit des Geräts und vom Standort ab. Im Schaufenster oder an sonnigen Plätzen braucht es hellere Displays als im Innenraum. Deshalb fragen wir vorab nach Ausrichtung und Lichteinfall und berücksichtigen das bei der Empfehlung.", None),
  ("hardware-lebensdauer", "Wie lange hält die Hardware?",
   "Auf die Hardware geben wir 5\u00a0Jahre Garantie. Wie lange ein Gerät darüber hinaus läuft, hängt von Modell, Betriebsstunden und Umgebung ab. Wenn Sie die laufende Betreuung abgeben möchten, sind Wartungspakete möglich.", None),
  ("hardware-software", "Welche Player und Software werden verwendet?",
   "Das legen wir passend zu Ihrem Projekt fest und nennen es im Angebot. Sie müssen sich nicht selbst darum kümmern: Inhalte ändern wir auf Ihre Nachricht hin, Einstellungen prüfen und passen wir aus der Ferne an.", None),
 ]),
 ("installation", "Installation & Montage", "wrench", [("leistungen/installation-montage/", "Installation & Montage ansehen")], [
  ("installation-wer", "Wer montiert die Bildschirme?",
   "HYSN übernimmt Montage und Einrichtung als Teil der Lösung aus einer Hand. Im Rhein-Main-Gebiet sind wir persönlich vor Ort. Für andere Regionen klären wir im Angebot, wie die Montage organisiert wird.", None),
  ("installation-dauer", "Wie lange dauert die Montage?",
   "Das hängt von Anzahl, Größe und Befestigung ab: Ein einzelnes Wand-Display ist schneller montiert als eine LED-Wand oder eine Stele. Termin und Zeitbedarf stimmen wir vorher mit Ihnen ab, damit Ihr Betrieb weiterlaufen kann.", None),
  ("installation-elektrik", "Brauchen wir einen Elektriker?",
   "Das hängt vom Standort ab. Ein Bildschirm braucht Strom in der Nähe und für Änderungen aus der Ferne eine Internetverbindung. Fehlt etwas davon, sagen wir Ihnen vorab, welche Arbeiten nötig sind; wer sie übernimmt, wird im Angebot festgelegt.", None),
  ("installation-wand", "Was, wenn unsere Wand nicht geeignet ist?",
   "Dann suchen wir eine andere Befestigung, zum Beispiel einen Standfuß oder eine freistehende Stele. Wir sehen uns die Wand vorab an, gern zuerst anhand von Fotos, und schlagen eine passende Lösung vor.", None),
  ("installation-zeiten", "Montieren Sie auch außerhalb der Öffnungszeiten?",
   "Nach Absprache ja. Nennen Sie uns Ihre Öffnungszeiten und Ihren Wunschtermin, dann planen wir die Montage so, dass Ihr Betrieb möglichst wenig gestört wird.", None),
  ("installation-vorbereitung", "Was sollten wir vor der Montage vorbereiten?",
   "Wenig: freien Zugang zur Fläche, Strom in der Nähe und, falls vorhanden, die Zugangsdaten für das Netzwerk vor Ort. Was an Ihrem Standort genau nötig ist, besprechen wir vor dem Termin mit Ihnen.", None),
 ]),
 ("content", "Content", "image", [("leistungen/content-creation/", "Content Creation ansehen")], [
  ("content-selbst", "Müssen wir die Inhalte selbst erstellen?",
   "Nein. Wir gestalten Ihre Inhalte, zum Beispiel Menüboards, Angebote oder Werbemotive, passend für Ihre Bildschirme. Sie liefern Logo, Preise und vorhandene Fotos, den Rest übernehmen wir.", None),
  ("content-material", "Können wir eigene Fotos und Videos verwenden?",
   "Ja. Schicken Sie uns Ihr Material, wir bereiten es für Format und Auflösung Ihrer Bildschirme auf. Fehlt passendes Material, besprechen wir, wie wir es ergänzen.", None),
  ("content-tempo", "Wer setzt Änderungen an den Inhalten um?",
   "Wir. Sie schreiben uns, was sich ändern soll, und wir passen es aus der Ferne an. Größere Änderungen, etwa ein neues Motiv, stimmen wir vorher mit Ihnen ab.", None),
  ("content-aenderung", "Wie ändern wir Preise oder Angebote?",
   "Mit einer kurzen Nachricht an uns. Sie brauchen dafür keine Schulung und keine eigene Software: Wir setzen die Änderung um und spielen sie auf Ihre Bildschirme.", None),
  ("content-formate", "Welche Dateien brauchen Sie von uns?",
   "Schicken Sie uns, was Sie haben: Logo, Fotos, Videos, Ihre bisherige Speisekarte oder Preisliste. Um die Aufbereitung für Ihre Bildschirme kümmern wir uns.", None),
  ("content-standorte", "Geht das auch für mehrere Standorte?",
   "Ja. Sie haben einen Ansprechpartner für alle Standorte. Inhalte und Einstellungen passen wir aus der Ferne an. Wie Lieferung, Montage und Content über mehrere Standorte laufen, planen wir gemeinsam mit Ihnen.", None),
 ]),
 ("wartung", "Wartung & Support", "headset", [("leistungen/wartung-betrieb/", "Wartung & Betrieb ansehen")], [
  ("wartung-ausfall", "Was passiert, wenn ein Bildschirm ausfällt?",
   "Sie melden sich bei uns, und wir prüfen zuerst aus der Ferne, ob Inhalte oder Einstellungen die Ursache sind. Lässt sich das Problem so nicht lösen, stimmen wir einen Termin vor Ort ab; das hängt von Ihrer Region ab. Für die Hardware gelten 5\u00a0Jahre Garantie.", None),
  ("wartung-reaktion", "Wer kümmert sich um eine Störung?",
   "Ihr persönlicher Ansprechpartner bei HYSN, kein Callcenter. Wir prüfen zuerst aus der Ferne, ob sich das Problem direkt lösen lässt. Ist ein Termin vor Ort nötig, stimmen wir ihn mit Ihnen ab.", None),
  ("wartung-erreichbar", "Wie erreichen wir Sie bei einer Störung?",
   f"Per Telefon unter {PHONE} oder per E-Mail an {EMAIL}. Wir antworten persönlich. Ein Foto oder ein kurzes Video der Störung hilft uns bei der ersten Einschätzung.", None),
  ("wartung-garantie", "Was deckt die Garantie ab?",
   "Auf die Hardware gibt es 5\u00a0Jahre Garantie. Was im Einzelnen abgedeckt ist, steht in Ihrem Angebot; fragen Sie gern vorab danach.", None),
  ("wartung-fern", "Lassen sich Probleme aus der Ferne lösen?",
   "Vieles ja: Inhalte und Einstellungen prüfen und ändern wir aus der Ferne, ohne dass jemand anreisen muss. Bei einem Hardware-Defekt ist ein Termin vor Ort nötig.", None),
  ("wartung-pakete", "Gibt es Wartungspakete?",
   "Ja. Was ein Paket umfasst, zum Beispiel Fernwartung, Inhaltsänderungen oder Einsätze vor Ort, stimmen wir individuell mit Ihnen ab.", None),
 ]),
 ("dooh", "DOOH & Werbeeinnahmen", "chart", [("leistungen/dooh-hyads/", "DOOH & hyads ansehen"), ("partnerprogramm/", "Partnerprogramm ansehen")], [
  ("dooh-ertrag", "Wie viel kann ein Werbebildschirm einbringen?",
   "Das hängt von Lage, Sichtbarkeit, Verweildauer und der Nachfrage lokaler Werbekunden ab. Eine Einnahmengarantie geben wir nicht. Stattdessen rechnen wir Ihnen vorab ein realistisches Beispiel für Ihren Standort durch.", None),
  ("dooh-werbekunden", "Wer findet die Werbekunden?",
   "Wir, über unser Werbenetzwerk hyads mit über 30 aktiven Werbebildschirmen im REWE- und EDEKA-Umfeld. Lokale Werbung gibt es dort ab ca. 99 € im Monat, pro Stele sind es etwa 6 Werbekunden. Sie stellen den Standort, Vermarktung und Inhalte übernehmen wir.", None),
  ("dooh-ausschluss", "Können wir bestimmte Werbekunden ausschließen?",
   "Sprechen Sie das im Erstgespräch an, etwa wenn direkte Wettbewerber nicht auf Ihrem Bildschirm erscheinen sollen. Welche Ausschlüsse möglich sind, klären wir gemeinsam und halten sie im Vertrag fest.", None),
  ("dooh-keine", "Was, wenn sich keine Werbekunden finden?",
   "Dann gibt es in dieser Zeit keine Werbeeinnahmen; garantierte Einnahmen versprechen wir bewusst nicht. Deshalb prüfen wir vorab, ob Ihr Standort genug Sichtbarkeit bietet, und rechnen mit realistischen Beispielwerten statt mit Wunschzahlen.", None),
  ("dooh-anteil", "Wie werden die Werbeeinnahmen aufgeteilt?",
   "Im Betreibermodell investiert HYSN in die Hardware. Sie erhalten 10 % der Werbeeinnahmen, solange der Bildschirm refinanziert wird, und 20 % nach der Amortisation. Im Co-Investment teilen wir die Werbeeinnahmen 50/50. Investieren Sie selbst, behalten Sie die volle Kontrolle und die vollen Einnahmen.",
   "Beispielwert, keine Garantie: 6 Werbekunden à ca. 99 € ergeben 594 € Werbeeinnahmen im Monat. Ihr Anteil: 59,40 € während der Refinanzierung, danach 118,80 €. Aufteilung und Auszahlung regelt Ihr Angebot."),
  ("dooh-standort", "Eignet sich jeder Standort für Werbung?",
   "Nein. Entscheidend sind Laufkundschaft, Sichtbarkeit und Verweildauer, zum Beispiel im Eingangsbereich eines Supermarkts. Wir prüfen das vorab und sagen Ihnen offen, wenn sich ein Standort nicht eignet.", None),
 ]),
 ("vertraege", "Verträge & Laufzeiten", "doc", [], [
  ("vertraege-laufzeit", "Wie lange läuft ein Vertrag?",
   "Das hängt vom Modell ab: Kauf, Co-Investment, Betreibermodell und Wartungspaket haben jeweils eigene Bedingungen. Die Laufzeit steht im Angebot, sodass Sie sie kennen, bevor Sie unterschreiben.", None),
  ("vertraege-ende", "Was passiert am Ende der Laufzeit?",
   "Das regelt Ihr Vertrag: ob er sich verlängert, neu verhandelt wird oder endet. Wir sprechen das schon beim Angebot an, damit Sie es vor der Unterschrift wissen.", None),
  ("vertraege-kuendigung", "Können wir vorzeitig kündigen?",
   "Ob und zu welchen Bedingungen eine vorzeitige Kündigung möglich ist, steht im Vertrag. Fragen Sie uns vorab danach, wir erklären Ihnen die Regelung, bevor Sie unterschreiben.", None),
  ("vertraege-eigentum", "Wem gehört der Bildschirm nach Vertragsende?",
   "Beim Kauf gehört er Ihnen. Beim Co-Investment und beim Betreibermodell wird die Eigentumsfrage im Vertrag geregelt, einschließlich dessen, was am Ende der Laufzeit mit der Hardware passiert.", None),
  ("vertraege-kosten", "Mit welchen laufenden Kosten müssen wir rechnen?",
   "Das hängt davon ab, was wir dauerhaft für Sie übernehmen sollen, etwa ein Wartungspaket oder regelmäßige Inhaltsänderungen. Dazu kommen Strom und gegebenenfalls ein Internetanschluss am Standort. Alle laufenden Positionen stehen im Angebot.", None),
  ("vertraege-angebot", "Bekommen wir ein schriftliches Angebot?",
   "Ja. Nach dem Erstgespräch erhalten Sie ein schriftliches Angebot mit Leistungsumfang, Modell, Laufzeit und Kosten. Erst wenn Sie zustimmen, geht es weiter.", None),
 ]),
]

# Quick links under the search field: (category, question to open, icon, label, question text)
QUICK = [
 ("preise", "preise-kosten", "tag", "Preise", "Was kostet ein Bildschirmsystem?"),
 ("installation", "installation-dauer", "wrench", "Montage", "Wie lange dauert die Montage?"),
 ("content", "content-selbst", "image", "Content", "Erstellt HYSN unsere Inhalte?"),
 ("wartung", "wartung-ausfall", "headset", "Support", "Was tun bei einem Ausfall?"),
 ("vertraege", "vertraege-laufzeit", "doc", "Verträge", "Wie lange läuft der Vertrag?"),
]


def body(rel):
    e = H.escape
    n_q = sum(len(c[4]) for c in CATS)

    def qa(qid, q, a, ex, first):
        exp = f'<p class="faq-ex">{e(ex)}</p>' if ex else ""
        return (f'<details id="{qid}"{" open" if first else ""}><summary>{e(q)}</summary>'
                f'<div class="faq-a"><p>{e(a)}</p>{exp}</div></details>')

    groups = ""
    for cid, title, ic, links, qs in CATS:
        more = "".join(tlink(rel + h, e(l), extra=" tlink--plain") for h, l in links)
        groups += f"""
    <section class="faq-cat{" is-first" if cid == CATS[0][0] else ""}" id="{cid}" aria-labelledby="{cid}-h">{pi(ic)}<h3 id="{cid}-h">{e(title)}</h3>
      <div class="faq-list">{"".join(qa(*q, i == 0) for i, q in enumerate(qs))}</div>{f'<p class="faq-more">{more}</p>' if more else ""}
    </section>"""

    active = ' class="is-active" aria-current="location"'
    nav = "".join(f'<li><a href="#{cid}"{active if i == 0 else ""}>{pi(ic)}<span>{e(title)}</span><b>{len(qs)}</b></a></li>'
                  for i, (cid, title, ic, links, qs) in enumerate(CATS))
    quick = "".join(f'<a href="#{cid}" data-open="{qid}">{pi(ic)}<span><b>{e(label)}</b>{e(q)}</span></a>'
                    for cid, qid, ic, label, q in QUICK)
    termin = mailto("Terminanfrage")

    return f"""
<section class="chero faq-hero"><div class="chero-img"><img src="{rel}assets/img/faq/faq-hero.jpg" alt="Hochformat-Display mit Bergmotiv in einem hellen Büro, davor Laptop und Notizbuch" width="1020" height="512" fetchpriority="high"></div>
  <div class="wrap"><div class="chero-text">
    <span class="eyebrow">Häufige Fragen</span>
    <h1><span>Klare Antworten.</span> <span>Ein klarer nächster Schritt.</span></h1>
    <p class="lead">Von der Wahl des Bildschirms über Montage und Inhalte bis zur laufenden Betreuung: Hier finden Sie die Antworten, die für Ihr Projekt zählen.</p>
    <p class="faq-hero-for">Für Unternehmen, Kommunen und Standortpartner.</p>
  </div></div>
</section>

<section class="faq-find" id="suche" aria-labelledby="suche-h"><div class="wrap">
  <span class="eyebrow" id="suche-h">Antwort finden</span>
  <form class="faq-search" role="search" action="#fragen">
    <div class="faq-field"><label class="faq-vh" for="faq-q">Fragen durchsuchen</label>{pi("search")}
      <input id="faq-q" type="search" placeholder="Stichwort eingeben, z. B. Preis, Montage, Garantie, LED oder Werbung …" data-alt="Stichwort, z. B. Preis, Montage oder Garantie …|Stichwort, z. B. Garantie …|Z. B. Garantie, LED …|Stichwort …" autocomplete="off" spellcheck="false"></div>
    <button class="btn faq-go" type="submit"><span>Suchen</span>{ARROW}</button>
  </form>
  <div class="faq-status" aria-live="polite">
    <p data-faq-hits hidden><span data-n></span> {tlink("#fragen", "Zu den Antworten", "down", " tlink--plain")}</p>
    <p data-faq-none hidden>Keine passende Frage gefunden – fragen Sie uns direkt. {tlink(rel + "kontakt/#anfrage", "Frage stellen", extra=" tlink--plain")}</p>
  </div>
  <nav class="faq-quick" aria-label="Häufigste Fragen">{quick}</nav>
</div></section>

<section class="faq-main" id="fragen" aria-labelledby="fragen-h"><div class="wrap">
  <aside class="faq-side"><div class="faq-side-in">
    <p class="faq-side-h" id="themen-h">Themen</p>
    <nav class="faq-nav" aria-labelledby="themen-h"><ul>{nav}</ul></nav>
    <div class="faq-help"><div class="faq-help-card">
      <p class="faq-help-h">Frage nicht dabei?</p>
      <p class="faq-help-txt">Schreiben Sie uns, was Sie vorhaben.</p>
      {btn(rel + "kontakt/#anfrage", "Frage stellen")}
      <a href="mailto:{S["email"]}">{ico("mail")}{S["email"]}</a>
      <a href="tel:{S["phone_href"]}">{ico("phone")}{S["phone"]}</a>
    </div></div>
  </div></aside>

  <div class="faq-col">
    <div class="faq-colhead"><h2 id="fragen-h">Alle Antworten nach Thema.</h2><p><span data-faq-total>{n_q} Fragen · {len(CATS)} Themen</span><button class="faq-reset" type="button" data-faq-reset hidden>Suche zurücksetzen</button></p></div>{groups}
  </div>
</div></section>

<section class="faq-ask" id="direkt"><div class="wrap">
  <div class="faq-ask-text">
    <span class="eyebrow">Noch eine Frage offen?</span>
    <h2>Fragen Sie uns direkt.</h2>
    <p class="sub">Schreiben Sie uns, welcher Bildschirm, welcher Standort oder welches Detail noch unklar ist. Ein paar Stichworte reichen für den Anfang.</p>
  </div>
  <div class="faq-ways">
    <a href="mailto:{S["email"]}">{ico("mail")}<span><b>E-Mail an unser Team</b>{S["email"]}</span></a>
    <a href="tel:{S["phone_href"]}">{ico("phone")}<span><b>Anrufen</b>{S["phone"]}</span></a>
  </div>
  <div class="faq-ask-act">
    {btn(rel + "kontakt/#anfrage", "Meine Frage stellen")}
    <a class="faq-btn-line" href="{termin}">Gesprächstermin anfragen{ARROW}</a>
    <p class="small">Persönlicher Ansprechpartner, kein Callcenter.</p>
  </div>
</div></section>

<section class="cta faq-cta">{RIBBON}<div class="wrap">
  <div class="cta-text">
    <div class="faq-cta-copy">
      <span class="eyebrow">Kostenloses Erstgespräch</span>
      <h2>Von der Frage<br>zum klaren Plan.</h2>
      <p class="sub">Wir helfen Ihnen, den nächsten sinnvollen Schritt für Ihren Standort zu finden.</p>
    </div>
    <div class="faq-cta-act"><div class="actions">{btn(rel + "kontakt/#anfrage", "Erstgespräch vereinbaren")}</div></div>
    <p class="small faq-cta-note">Unverbindlich. Sie&nbsp;entscheiden, ob es weitergeht.</p>
  </div>
  <div class="cta-brand"><span>Menschen</span><span>Standorte</span><span>Möglichkeiten</span><i></i><img src="{rel}assets/img/logo/hysn-logo.svg" alt="HYSN" width="1485" height="234"></div>
</div></section>
<script src="{rel}assets/js/pages/faq.js" defer></script>"""


PAGES = [dict(path="faq/index.html", title="Häufige Fragen | HYSN Digital Signage",
              desc="Antworten zu Kosten, Hardware, Montage, Content, Wartung, Werbeeinnahmen und Verträgen: alles, was Sie vor einem Digital-Signage-Projekt mit HYSN wissen sollten.",
              current="faq/", body=body, body_class="hero-page", css=["pages/faq.css"])]
