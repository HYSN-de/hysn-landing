"""Content Creation & Animation: layout follows Static pages/hysn-content-creation-animation-concept-v1 1.png."""
from _lib import *

IMG = "assets/img/content_creation/"

# page-specific line icons on the 24x24 grid (stroke only, like the shared set)
I_EYE = '<path d="M2.8 12s3.4-6.2 9.2-6.2 9.2 6.2 9.2 6.2-3.4 6.2-9.2 6.2S2.8 12 2.8 12z"/><circle cx="12" cy="12" r="2.8"/>'
I_LAYERS = '<path d="m12 3.6 8.6 4.6-8.6 4.6-8.6-4.6z"/><path d="m3.4 12.4 8.6 4.6 8.6-4.6"/><path d="m3.4 16.2 8.6 4.6 8.6-4.6"/>'
I_FORMATS = '<rect x="2.8" y="8" width="11.4" height="8" rx="1"/><rect x="15.8" y="4.4" width="5.4" height="15.2" rx="1"/>'
I_REFRESH = '<path d="M19.4 9.2A7.8 7.8 0 0 0 5.6 7.4"/><path d="M4.6 14.8a7.8 7.8 0 0 0 13.8 1.8"/><path d="M5.2 3.6v4.2h4.2"/><path d="M18.8 20.4v-4.2h-4.2"/>'
I_FOLDER = '<path d="M3.4 6.4a1.2 1.2 0 0 1 1.2-1.2h4.6l2 2.2h8.2a1.2 1.2 0 0 1 1.2 1.2v9.8a1.2 1.2 0 0 1-1.2 1.2H4.6a1.2 1.2 0 0 1-1.2-1.2z"/><path d="M3.4 10.2h17.2"/>'
I_SCREEN = '<rect x="3" y="4.4" width="18" height="12.4" rx="1.2"/><path d="M9 20.4h6M12 16.8v3.6"/>'
I_SCREEN_OK = I_SCREEN + '<path d="m9.2 10.8 2 2 3.8-4"/>'
I_IMAGE = '<rect x="3.4" y="4.4" width="17.2" height="15.2" rx="1.2"/><circle cx="8.6" cy="9.4" r="1.7"/><path d="m3.8 17.4 5-4.8 4 3.8 2.8-2.6 4.8 4.2"/>'
I_MOTION = '<path d="M9 12h11M16.2 8.2 20 12l-3.8 3.8"/><path d="M3.4 8.4h4.2M2.6 12h3.6M3.4 15.6h4.2"/>'
I_DIST = '<path d="M3.4 5.4v13.2M20.6 5.4v13.2M6.6 12h10.8"/><path d="M9 9.6 6.6 12 9 14.4M15 9.6l2.4 2.4-2.4 2.4"/>'
I_NEXT = '<circle cx="12" cy="12" r="8.6"/><path d="m10.6 8.6 3.4 3.4-3.4 3.4"/>'
DOWN = f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONS["down"]}</svg>'
# second copy of the ribbon for the reception example screen, with its own gradient ids
RIBBON_SCREEN = RIBBON.replace('class="ribbon"', 'class="cc-rib"').replace("rb1", "ccrb1").replace("rb2", "ccrb2").replace("rb3", "ccrb3")


def keep_arrow(title):
    """Keep the arrow on the same line as the last word."""
    head, _, last = title.rpartition(" ")
    return (head + " " if head else "") + f'<span class="nw">{last}{ARROW}</span>'


def body(rel):
    benefits = [
        (I_EYE, "Für Screens gestaltet", "Aus der Distanz klar lesbar."),
        (I_LAYERS, "Design und Animation", "Ein durchgängiger Prozess aus einer Hand."),
        (I_FORMATS, "Formate, die passen", "Hoch- und Querformat, auch mehrteilig."),
        (I_REFRESH, "Bestehende Screens", "Neuer Content für Ihre vorhandenen Displays."),
    ]
    ben_html = "".join(f'<li>{icon(i)}<div><h3>{t}</h3><p>{d}</p></div></li>' for i, t, d in benefits)

    # (image, width, alt, href, viewer tab or None, title, text); each link leads to the section or example that shows it
    cards = [
        ("cc-menueboards.jpg", 336, "Mehrteiliges Menüboard mit Bowls über einer Restaurant-Theke", "#einsatz", None, "Animierte Menüboards", "Speisen, Bestseller und Tagesangebote."),
        ("cc-food-visuals.jpg", 331, "Nahaufnahme einer Bowl mit Gemüse und frischen Kräutern", "#beispiele", 1, "Produkt- und Food-Visuals", "Bilder, aufbereitet für große Displays."),
        ("cc-aktionen.jpg", 332, "Werbestele mit Sommer-Aktion und Orangen in einem Einkaufszentrum", "#beispiele", 2, "Aktionen und Kampagnen", "Angebote mit klarem Blickfang."),
        ("cc-markenloops.jpg", 331, "Animiertes Markenmotiv mit geschwungenem Band auf dunklem Grund", "#formate", None, "Marken-Loops und Animation", "Bewegte Markenbotschaften für Empfang und LED-Wand."),
        ("cc-dooh.jpg", 330, "Digitale Außenstele mit Café-Kampagne in einer Fußgängerzone", rel + "leistungen/dooh-hyads/", None, "Lokale DOOH-Kampagnen", "Motive für lokale Werbescreens, auch im hyads-Netzwerk."),
    ]
    tab_attr = lambda t: f' data-cc-tab="{t}"' if t else ""
    cards_html = "".join(
        f'<a class="cc-card" href="{href}"{tab_attr(t)}><span class="cc-card-img"><img src="{rel}{IMG}{f}" alt="{alt}" width="{w}" height="392" loading="lazy"></span>'
        f'<h3>{keep_arrow(title)}</h3><p>{d}</p></a>'
        for f, w, alt, href, t, title, d in cards)

    def fig(cls, f, w, h, alt, href, title, text, tab=None):
        return (f'<figure class="cc-fig {cls}"><div class="cc-fig-img"><img src="{rel}{IMG}{f}" alt="{alt}" width="{w}" height="{h}" loading="lazy"></div>'
                f'<figcaption><a href="{href}"{tab_attr(tab)}>{keep_arrow(title)}</a><span>{text}</span></figcaption></figure>')

    menu = [("Bowls", "8,50 €"), ("Salate", "7,50 €"), ("Wraps", "7,50 €"), ("Getränke", "3,50 €"), ("Desserts", "4,00 €")]
    menu_html = "".join(f"<li><span>{n}</span><span>{p}</span></li>" for n, p in menu)
    offers = [("Erdbeeren", "Schale, 500 g", "2,49 €"), ("Spargel, weiß", "1 kg", "7,99 €"), ("Kirschen", "Schale, 500 g", "3,99 €")]
    offers_html = "".join(f"<li><span><b>{n}</b>{s}</span><strong>{p}</strong></li>" for n, s, p in offers)
    tabs = [("cc-t1", "Menüboard"), ("cc-t2", "Handel"), ("cc-t3", "Stadtinfo"), ("cc-t4", "Empfang")]
    radios = "".join(f'<input class="cc-radio" type="radio" name="cc-tab" id="{i}"{" checked" if n == 0 else ""}>' for n, (i, _) in enumerate(tabs))
    labels = "".join(f'<label for="{i}">{t}</label>' for i, t in tabs)
    play = ('<svg class="cc-i-play" viewBox="0 0 24 24" aria-hidden="true"><path d="M8.6 5.8v12.4l9.6-6.2z"/></svg>'
            '<svg class="cc-i-pause" viewBox="0 0 24 24" aria-hidden="true"><path d="M8.6 6v12M15.4 6v12"/></svg>')

    steps = [
        (ico("chat"), "Kurzes Gespräch", "Ihre Ziele, Ihre Zielgruppe und Ihr Standort."),
        (icon(I_FOLDER), "Material sichten", "Logo, Bilder, Inhalte und Screen-Details."),
        (ico("pencil"), "Gestalten und animieren", "Layouts und Bewegung, abgestimmt mit Ihnen."),
        (icon(I_SCREEN_OK), "Liefern und ausspielen", "Fertig für Ihre Screens. Spätere Änderungen übernehmen wir."),
    ]
    steps_html = "".join(f'<div><span class="ring">{i}</span><b>{n:02d}</b><h3>{t}</h3><p>{d}</p></div>' for n, (i, t, d) in enumerate(steps, 1))

    package = ["Content-Konzept und klare visuelle Hierarchie", "Gestaltung mit Food- und Produktbildern", "Animation und Kampagnenvarianten",
               "Hoch- und Querformat, auch für mehrteilige Menüboards", "4K-fähige Dateien, wo Ihr Screen es braucht", "Preisänderungen ohne Neudruck",
               "Abstimmung und Freigabe vor dem Start", "Änderungen per Nachricht, HYSN aktualisiert für Sie"]
    package_html = "".join(f"<li>{ico('one')}{p}</li>" for p in package)

    faq = [
        ("Müssen wir eigene Fotos liefern?", "Nein. Wir sichten Ihre vorhandenen Bilder und bereiten sie für den Screen auf. Fehlt passendes Bildmaterial, besprechen wir gemeinsam, wie wir es lösen.", True),
        ("Welche Dateien erhalten wir?", "Bildschirmfertige Dateien im Format, das Ihre Screens und Ihr Player brauchen, auf Wunsch 4K-fähig. Die Details legen wir im Angebot fest.", False),
        ("Wie ändern wir später Inhalte?", "Per Nachricht. Schreiben Sie uns, was sich ändern soll, zum Beispiel einen Preis oder ein Tagesangebot. HYSN aktualisiert die Inhalte für Sie, eine Schulung ist dafür nicht nötig.", False),
        ("Was, wenn wir keinen Styleguide haben?", "Kein Problem. Logo und ein paar Bilder reichen für den Start. Daraus entwickeln wir einen stimmigen Auftritt für Ihre Screens, eine externe Agentur brauchen Sie dafür nicht.", False),
        ("Wir haben schon ein Design. Geht das?", "Ja. Wir passen vorhandene Gestaltungen an Ihre Screen-Formate an und animieren sie auf Wunsch.", False),
        ("Welche Bildschirmformate unterstützen Sie?", "Hoch- und Querformat sowie mehrteilige Menüboards. Das genaue Format richtet sich nach Ihren Displays, auch für bestehende Screens.", False),
        ("Wie läuft die Abstimmung ab?", "Sie sehen die Entwürfe, bevor etwas auf Ihren Screens läuft, und geben uns Ihr Feedback gesammelt zurück. Wie viele Abstimmungsrunden enthalten sind, steht in Ihrem Angebot.", False),
    ]
    faq_html = "".join(f'<details{" open" if o else ""}><summary>{icon(I_NEXT)}<span>{H.escape(q)}</span></summary><p>{H.escape(a)}</p></details>' for q, a, o in faq)

    return f"""
<section class="chero cc-hero"><div class="chero-img"><img src="{rel}{IMG}cc-hero.jpg" alt="Hochformat-Display mit Food-Motiv, großes Querformat-Display mit Markenmotiv und ein Laptop mit Schnittprogramm" width="1120" height="565" fetchpriority="high"></div>
  <div class="wrap"><div class="chero-text">
    <span class="eyebrow">Content Creation &amp; Animation</span>
    <h1>Content, der auf<br>Ihren Screens wirkt.</h1>
    <p class="lead">Bildschirmfertige Gestaltung, Animation und Kampagnen für Menüboards, Werbedisplays, LED-Wände und lokale Werbung.</p>
    <div class="actions"><a class="btn" href="#beispiele">Content-Beispiele ansehen{DOWN}</a>{btn(rel + "kontakt/#anfrage", "Ihren Content besprechen", ghost=True)}</div>
    <p class="note">{ico("chat")}<span>Kein aufwendiges Briefing – wir entwickeln den Content aus einem kurzen Gespräch.</span></p>
  </div></div>
</section>

<section class="cc-benefits"><h2 class="vh">Ihre Vorteile</h2><div class="wrap"><ul class="cc-ben">{ben_html}</ul></div></section>

<section class="cc-services"><div class="wrap">
  <div class="cc-head"><div><span class="eyebrow">Content, der funktioniert</span><h2>Gute Screens verdienen<br>guten Content.</h2></div>
    <p class="sub">Klare Hierarchie, Bewegung mit Zweck und Bilder, die auf großen Displays funktionieren.</p></div>
  <div class="cc-cards">{cards_html}</div>
</div></section>

<section class="cc-context" id="einsatz"><div class="wrap cc-ctx">
  <div class="cc-ctx-head"><span class="eyebrow">Content im Einsatz</span><h2>Verschiedene Orte.<br>Ein klarer Zweck.</h2><p class="cc-note">Beispielhafte Content-Konzepte</p></div>
  {fig("cc-fig--tall", "cc-restaurant.jpg", 584, 570, "Restaurant-Theke mit vier abgestimmten Menüboards", rel + "referenzen/", "Restaurant-Menüboards", "Damit die nächste Bestellung leichter fällt.")}
  {fig("cc-fig--a", "cc-handel.jpg", 575, 366, "Werbestele mit Pflanzenmotiv in einer Ladenpassage", rel + "leistungen/dooh-hyads/", "Werbung im Handel", "Eigene Angebote und lokale Werbung im Wechsel.")}
  {fig("cc-fig--b", "cc-stadtinfo.jpg", 552, 366, "Info-Stele mit Stadtinformationen auf einem Platz in der Innenstadt", "#beispiele", "Stadtinformation", "Bekanntmachungen, Termine und Werbung klar getrennt.", 3)}
  {fig("cc-fig--wide", "cc-empfang.jpg", 1148, 284, "Empfangsbereich mit großem Begrüßungsdisplay hinter dem Tresen", "#beispiele", "Büro und Empfang", "Besucher mit einem einheitlichen Markenauftritt begrüßen.", 4)}
</div></section>

<section class="cc-viewer" id="beispiele"><div class="wrap">
  <div class="cc-view">
    {radios}
    <div class="cc-tabs"><span class="eyebrow">Content-Beispiel</span><div class="cc-tablist">{labels}</div></div>
    <div class="cc-screen">
      <div class="cc-panels">
      <div class="cc-panel cc-p1" role="group" aria-label="Beispiel Menüboard">
        <div class="cc-m-hero"><img src="{rel}{IMG}cc-bowl.jpg" alt="Bowl mit Hähnchen, Gemüse und Kräutern" width="378" height="301" loading="lazy">
          <div class="cc-m-copy"><b>Mediterrane <br>Bowl</b><span>Frische Zutaten. <br>Täglich&nbsp;zubereitet.</span></div></div>
        <div class="cc-m-list"><b>Unser Menü</b><ul>{menu_html}</ul><small>Guten Appetit</small></div>
      </div>
      <div class="cc-panel cc-p2" role="group" aria-label="Beispiel Aktionsscreen im Handel">
        <div class="cc-o-hero"><small>Aktion der Woche</small><b>Frisch ins<br>Wochenende.</b><span>Obst und Gemüse aus der Region.</span></div>
        <div class="cc-o-list"><ul>{offers_html}</ul><small>Nur solange der Vorrat&nbsp;reicht</small></div>
      </div>
      <div class="cc-panel cc-p3" role="group" aria-label="Beispiel Stadtinformation">
        <div class="cc-c-top"><b>Stadtinfo</b><span>Willkommen in der Innenstadt</span></div>
        <div class="cc-c-col"><small>Veranstaltungen</small><p><b>Wochenmarkt</b>Samstag, 8 bis 13 Uhr, Marktplatz</p><p><b>Sommerkonzert</b>Freitag, 19 Uhr, Stadtpark</p></div>
        <div class="cc-c-col"><small>Hinweise</small><p><b>Bauarbeiten Bahnhofstraße</b>Umleitung ist ausgeschildert</p><p><b>Bürgerbüro</b>Termine nach Vereinbarung</p></div>
        <div class="cc-c-ad"><small>Anzeige</small><b>Café am Markt</b><span>Frühstück bis 11 Uhr</span></div>
      </div>
      <div class="cc-panel cc-p4" role="group" aria-label="Beispiel Begrüßung am Empfang">{RIBBON_SCREEN}
        <div class="cc-w-copy"><small>Empfang</small><b>Willkommen.</b><span>Schön, dass Sie da sind.</span></div>
        <p class="cc-w-foot"><span>Besprechungsraum&nbsp;2</span><i> · </i><span>3.&nbsp;Obergeschoss</span></p>
      </div>
      </div>
      <div class="cc-player" hidden><button class="cc-play" type="button" aria-label="Abspielen">{play}</button>
        <div class="cc-prog" aria-hidden="true"><i></i><i></i><i></i><i></i></div><span class="cc-time" aria-hidden="true">0:00 / 0:24</span></div>
    </div>
    <p class="cc-view-note">Gestaltungsbeispiele. Preise, Angebote, Termine und Hinweise aktualisieren wir auf Ihre Nachricht hin.</p>
  </div>
  <div class="cc-view-text">
    <span class="eyebrow">Bewegung mit Zweck</span>
    <h2>Ein Screen.<br>Eine klare Aufgabe.</h2>
    <p class="sub">Den Blick führen. Das Angebot klar zeigen. Die Botschaft leicht verständlich halten.</p>
    <ul class="cc-points"><li>{icon(I_EYE)}Auf einen Blick lesbar</li><li>{icon(I_MOTION)}Bewegung, die lenkt statt ablenkt</li><li>{icon(I_DIST)}Gemacht für den Betrachtungsabstand</li></ul>
  </div>
</div></section>

<section class="cc-steps"><div class="wrap">
  <div><span class="eyebrow">Vom Gespräch zum Screen</span><h2>Vier Schritte<br>zu Ihrem Content.</h2></div>
  <div class="flow cc-flow">{steps_html}</div>
</div></section>

<section class="cc-brief"><div class="wrap">
  <div class="cc-brief-head"><h2>Was Sie haben,<br>reicht zum Start.</h2><p>Keine fertigen Entwürfe oder perfekten Fotos nötig.</p></div>
  <div class="cc-brief-main">
    <div class="cc-needs">
      <div>{ico("doc")}<div><h3>Ihre Inhalte</h3><p>Speisen, Produkte, Angebote oder Kampagnendetails.</p></div></div>
      <div>{icon(I_IMAGE)}<div><h3>Ihr Markenauftritt</h3><p>Logo, Farben und Bilder, falls vorhanden.</p></div></div>
      <div>{icon(I_SCREEN)}<div><h3>Ihre Screen-Details</h3><p>Ausrichtung, Auflösung und Standort.</p></div></div>
    </div>
    <ul class="cc-scope"><li>Kleine Änderungen per Nachricht</li><li>Saisonale Aktionen eingeplant</li><li>Ganz ohne Schulung</li></ul>
  </div>
</div></section>

<section class="cc-pack" id="formate"><div class="wrap">
  <div class="cc-pack-main">
    <div class="cc-pack-head"><span class="eyebrow">Ein Paket, das passt</span><h2>Eine Idee.<br>Jedes Screen-Format.</h2></div>
    <p class="sub">Der Umfang richtet sich nach Ihren Screens, Ihren Inhalten und danach, wie oft sich etwas ändert.</p>
    <figure class="cc-f1"><img src="{rel}{IMG}cc-format-quer.jpg" alt="Querformat-Display mit Markenmotiv" width="435" height="225" loading="lazy"><figcaption>Querformat</figcaption></figure>
    <figure class="cc-f2"><img src="{rel}{IMG}cc-format-hoch.jpg" alt="Hochformat-Display mit demselben Markenmotiv" width="176" height="344" loading="lazy"><figcaption>Hochformat</figcaption></figure>
    <figure class="cc-f3"><img src="{rel}{IMG}cc-format-led.jpg" alt="Breites LED-Display mit demselben Markenmotiv" width="435" height="267" loading="lazy"><figcaption>LED-Wand</figcaption></figure>
  </div>
  <div class="cc-pack-list">
    <h3>Ihr Paket kann enthalten</h3>
    <ul>{package_html}</ul>
    <p class="cc-note">Formate und Leistungen richten sich nach Ihrem Display und Player. Der Umfang wird im Angebot festgelegt.</p>
  </div>
</div></section>

<section class="cc-ba" id="vorher-nachher"><div class="wrap">
  <div class="cc-ba-head"><h2>Gleiche Screens.<br>Klarere Botschaft.</h2><p class="cc-note">Beispielhafte Gegenüberstellung</p></div>
  <figure><span class="cc-tag">Vorher</span><img src="{rel}{IMG}cc-vorher.jpg" alt="Menüboards mit uneinheitlichen Burger- und Getränkefotos" width="588" height="239" loading="lazy"><figcaption>Uneinheitliche Bilder und Layouts.</figcaption></figure>
  <figure><span class="cc-tag">Nachher</span><img src="{rel}{IMG}cc-nachher.jpg" alt="Dieselben Menüboards mit abgestimmtem Layout und klaren Speisenbildern" width="631" height="239" loading="lazy"><figcaption>Ein abgestimmtes, bildschirmfertiges Menü.</figcaption></figure>
</div></section>

<section class="qa cc-qa"><div class="wrap">
  <div><span class="eyebrow">Gut zu wissen</span><h2>Ihre Fragen<br>zum Content.</h2></div>
  <div class="faq cc-faq">{faq_html}</div>
</div></section>

<section class="cta cc-cta">{RIBBON}<div class="wrap">
  <div class="cta-text">
    <span class="eyebrow">Gemeinsam starten</span>
    <h2>Was zeigen Ihre<br>Screens als Nächstes?</h2>
    <p class="sub">Für neue Displays oder Screens, die schon hängen. Ein kurzes Gespräch genügt für den Start.</p>
    <p class="small">Persönlicher Ansprechpartner, kein Callcenter.</p>
  </div>
  <div class="cc-cta-act">
    <div class="actions">{btn(rel + "kontakt/#anfrage", "Content besprechen")}{btn("tel:" + S["phone_href"], "Team anrufen", ghost=True)}</div>
    <p class="cc-cta-contact"><a href="mailto:{S["email"]}">{S["email"]}</a><a href="tel:{S["phone_href"]}">{S["phone"]}</a></p>
  </div>
  <div class="cta-brand"><span>Menschen</span><span>Standorte</span><span>Möglichkeiten</span><i></i><img src="{rel}assets/img/logo/hysn-logo.svg" alt="HYSN" width="1485" height="234"></div>
</div></section>
<script src="{rel}assets/js/pages/content_creation.js" defer></script>"""


PAGES = [dict(path="leistungen/content-creation/index.html", title="Content Creation & Animation | HYSN Digital Signage",
              desc="Menüboards, Aktionen und Kampagnen bildschirmfertig gestaltet und animiert, im Hoch- und Querformat. Spätere Änderungen übernimmt HYSN für Sie.",
              current="leistungen/content-creation/", body=body, body_class="hero-page", css=["pages/content_creation.css"])]
