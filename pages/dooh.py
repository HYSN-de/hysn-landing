"""DOOH & hyads: layout follows Static pages/hysn-dooh-hyads-concept-v1 1.png.
Two audiences (Werbetreibende / Standort-Partner), marked with "01 /" and "02 /" eyebrows and their own band tint, as in the concept.
Revenue model per client: Betreibermodell 10 % during refinancing, then 20 % after amortisation; Co-Investment 50/50;
Eigeninvestition (the concept still shows 20 % / 35 %). Terms match the partner page (Werbekunden, Werbeeinnahmen)."""
from _lib import *

# page-specific line icons (24x24 grid, stroke only)
I_LAYERS = '<path d="m12 3.6 8.4 4.4-8.4 4.4L3.6 8z"/><path d="m3.6 12 8.4 4.4 8.4-4.4M3.6 16 12 20.4l8.4-4.4"/>'
I_GEAR = ('<path d="M18.8 10.3 21.1 10.6 21.1 13.4 18.8 13.7 18 15.6 19.4 17.5 17.5 19.4 15.6 18 13.7 18.8 13.4 21.1 10.6 21.1 10.3 18.8 '
          '8.4 18 6.5 19.4 4.6 17.5 6 15.6 5.2 13.7 2.9 13.4 2.9 10.6 5.2 10.3 6 8.4 4.6 6.5 6.5 4.6 8.4 6 10.3 5.2 10.6 2.9 13.4 2.9 '
          '13.7 5.2 15.6 6 17.5 4.6 19.4 6.5 18 8.4z"/><circle cx="12" cy="12" r="3"/>')
I_MEGA = '<path d="M3.8 9.6v4.8h3.4l7.6 4.4V5.2L7.2 9.6z"/><path d="M7.2 14.4v4.4h2.6v-3M18 9.2a4 4 0 0 1 0 5.6M20.2 7a7 7 0 0 1 0 10"/>'
I_STORE = ('<path d="M4.6 11.4V20h14.8v-8.6"/><path d="M3.4 9.2 5.2 4h13.6l1.8 5.2a2.4 2.4 0 0 1-4.3 1.4 2.4 2.4 0 0 1-4.3 0 2.4 2.4 0 0 1-4.3 0'
           'A2.4 2.4 0 0 1 3.4 9.2z"/><path d="M10 20v-4.8h4V20M2.8 20h18.4"/>')
I_TOTEM = '<rect x="4.6" y="2.8" width="14.8" height="14.6" rx=".8"/><path d="M12 17.4v3.6M8.2 21h7.6"/><path d="m10.4 7.4 4.6 2.7-4.6 2.7z"/>'
I_POSTER = '<rect x="3.6" y="3.4" width="16.8" height="12.4" rx=".6"/><path d="M8.4 20.6 9.8 15.8M15.6 20.6l-1.4-4.8M7 7.6h6.4M7 10.6h10"/>'
I_PHONE = '<rect x="7.4" y="2.6" width="9.2" height="18.8" rx="2"/><path d="M10.8 5.2h2.4"/><path d="M12 15.4s-2.8-1.7-2.8-3.6a1.4 1.4 0 0 1 2.8-.5 1.4 1.4 0 0 1 2.8.5c0 1.9-2.8 3.6-2.8 3.6z"/>'
I_SEARCH = '<circle cx="10.6" cy="10.6" r="6"/><path d="m15 15 5.4 5.4"/>'
I_PLAY = '<circle cx="12" cy="12" r="8.6"/><path d="M10.2 8.6v6.8l5.2-3.4z"/>'
I_BARS = '<path d="M5.4 19.6v-5.2M10 19.6V10.2M14.6 19.6v-7.2M19.2 19.6V5.4M3 20.4h18"/>'
I_SHIELD = '<path d="M12 3.2 19 6v5.6c0 4.4-3 7.6-7 9.2-4-1.6-7-4.8-7-9.2V6z"/><path d="m8.8 12 2.2 2.2 4.4-4.6"/>'
I_INFO = '<circle cx="12" cy="12" r="8.6"/><path d="M12 10.8v5.6M12 7.6v.4"/>'
I_ROTATE = '<path d="M19.4 12a7.4 7.4 0 1 1-2.2-5.2"/><path d="M19.6 4.2v3.4h-3.4"/>'
I_CHECK = '<path d="M20 12a8 8 0 1 1-4.4-7.2"/><path d="m8.4 11.2 3.2 3.2 8-8.4"/>'
I_NEXT = '<path d="M3.5 12h16M13.5 6l6 6-6 6"/>'


def body(rel):
    img = f"{rel}assets/img/dooh/"
    ask_ad = mailto("Werbeplatz anfragen")
    ask_offer = mailto("Kampagnenangebot anfordern")
    ask_site = mailto("Standort prüfen lassen")
    ask_partner = mailto("Standortpartner werden")

    faq_ad = [
      ("Wie viele Menschen sehen meine Werbung?", "Das hängt von Standort, Sichtbarkeit des Screens und Laufzeit ab. Feste Kontaktzahlen versprechen wir nicht. Welche Standorte zu Ihrer Zielgruppe passen, zeigen wir Ihnen im Angebot.", True),
      ("Was kostet eine Kampagne?", "Lokale Werbung gibt es ab ca. 99 € pro Monat. Den genauen Preis für Ihre Standorte und Ihre Laufzeit nennen wir Ihnen vorab im Angebot.", False),
      ("Wie schnell kann meine Kampagne starten?", "Digitale Motive brauchen weder Druck noch Aushang. Steht Ihr Motiv und ist ein Werbeplatz frei, kann es zügig losgehen. Den Starttermin legen wir im Angebot fest.", False),
    ]
    faq_pa = [
      ("Was kann mein Standort einbringen?", "Im Betreibermodell erhalten Sie 10 % der Werbeeinnahmen während der Refinanzierung und 20 % nach der Amortisation. Im Co-Investment teilen wir 50/50, bei Eigeninvestition gehören die Einnahmen Ihnen. Garantiert sind sie nicht.", False),
      ("Was muss mein Team tun?", "Sehr wenig. HYSN übernimmt Beratung, Hardware, Montage, Inhalte und Betrieb. Inhalte und Einstellungen prüfen und passen wir aus der Ferne an. Für eigene Hinweise genügt eine Nachricht an uns.", False),
      ("Und wenn wir aussteigen möchten?", "Laufzeit und Kündigung regelt der Vertrag. Beides besprechen wir vor dem Start offen und halten es im Angebot fest.", False),
    ]
    faq = lambda items: "".join(f'<details{" open" if o else ""}><summary>{H.escape(q)}</summary><p>{H.escape(a)}</p></details>' for q, a, o in items)

    places = [
      ("dooh-ort-supermarkt.jpg", 377, 252, "Supermärkte & Lebensmittelhandel", "Eingang eines Lebensmittelmarkts mit digitaler Werbestele"),
      ("dooh-ort-passage.jpg", 575, 362, "Passagen & Durchgangsbereiche", "Ladenpassage in einem Einkaufszentrum mit Werbestele und Passanten"),
      ("dooh-ort-gastronomie.jpg", 584, 368, "Gastronomie & Cafés", "Restauranttheke mit Gästen und Personal, darüber digitale Screens"),
      ("dooh-ort-innenstadt.jpg", 411, 256, "Innenstädte & öffentlicher Raum", "Fußgängerzone mit digitaler Werbestele"),
      ("dooh-ort-handel.jpg", 418, 256, "Handel & Showrooms", "Modegeschäft mit Werbestele im Hochformat"),
    ]
    places_html = "".join(f'<figure class="dh-place"><div class="dh-place-img"><img src="{img}{f}" alt="{H.escape(alt)}" width="{w}" height="{h}" loading="lazy"></div>'
                          f'<figcaption>{H.escape(cap)}</figcaption></figure>' for f, w, h, cap, alt in places)

    return f"""
<section class="chero dh-hero"><div class="chero-img"><img src="{img}dooh-hero.jpg" alt="Digitale Werbestele mit einem Café-Motiv für Kaffee und Croissant in einem hellen Einkaufsbereich" width="940" height="504" fetchpriority="high"></div>
  <div class="wrap"><div class="chero-text">
    <span class="eyebrow">DOOH &amp; hyads</span>
    <h1>Lokal werben – oder mit Ihrem Standort verdienen.</h1>
    <p class="lead">hyads ist das lokale Werbescreen-Netzwerk von HYSN: digitale Werbung dort, wo Menschen einkaufen, warten und vorbeigehen.</p>
    <div class="actions">{btn(ask_ad, "Werbeplatz anfragen")}{btn(ask_partner, "Standortpartner werden", ghost=True)}</div>
    <p class="note">{ico("one")}Ein Partner für Planung, Content, Wiedergabe und Technik. Ihre Anfrage ist unverbindlich.</p>
  </div></div>
</section>

<section class="dh-facts"><h2 class="vh">Auf einen Blick</h2><div class="wrap">
  <div>{ico("pin")}<div><h3>Sichtbar im Alltag</h3><p>30+ aktive Werbescreens im REWE- und EDEKA-Umfeld.</p></div></div>
  <div>{icon(I_LAYERS)}<div><h3>Flexible Motive</h3><p>Motive per Nachricht austauschen, ohne Druck und Aushang.</p></div></div>
  <div>{icon(I_GEAR)}<div><h3>Rundum betreut</h3><p>Planung, Content, Wiedergabe und Technik aus einer Hand.</p></div></div>
</div></section>

<section class="dh-paths"><div class="wrap">
  <h2>Zwei Wege, dabei&nbsp;zu&nbsp;sein.</h2>
  <div class="dh-paths-grid">
    <article class="dh-path dh-path--ad">
      <div class="dh-path-text">
        <p class="dh-path-label">{icon(I_MEGA)}Für Werbetreibende</p>
        <h3>Ihre Botschaft am richtigen Ort.</h3>
        <p>Für lokale Unternehmen, Dienstleister und Marken, die in ihrer Region auf Screens werben möchten.</p>
        {tlink("#werbetreibende", "Werbemöglichkeiten ansehen", extra=" tlink--plain")}
      </div>
      <div class="dh-path-img"><img src="{img}dooh-werbetreibende.jpg" alt="Werbestele im Hochformat in einem Geschäft, Passant im Vorbeigehen" width="314" height="504" loading="lazy"></div>
    </article>
    <article class="dh-path dh-path--pa">
      <div class="dh-path-text">
        <p class="dh-path-label">{icon(I_STORE)}Für Standortpartner</p>
        <h3>Mehr aus Ihrer Fläche machen.</h3>
        <p>Für Standorte mit regelmäßigem Publikumsverkehr und einem gut sichtbaren Platz für einen Screen.</p>
        {tlink("#standort-partner", "Partnermodell ansehen", extra=" tlink--plain")}
      </div>
      <div class="dh-path-img"><img src="{img}dooh-standortpartner.jpg" alt="Digitale Werbestele in einem hellen Innenbereich mit Publikumsverkehr" width="385" height="342" loading="lazy"></div>
    </article>
  </div>
  <p class="dh-define"><strong>DOOH</strong> steht für Digital Out-of-Home: Werbung auf digitalen Screens an realen Orten.</p>
</div></section>


<section class="dh-adv dh-tint-ad" id="werbetreibende"><div class="wrap">
  <div class="dh-adv-text">
    <span class="eyebrow">01 / Für Werbetreibende</span>
    <h2>Sichtbar werden.<br>Lokal relevant.</h2>
    <p class="sub">Erreichen Sie Menschen dort, wo sie einkaufen und essen gehen: in Ihrer Region, mitten im Alltag Ihrer Kunden.</p>
    {btn(ask_ad, "Verfügbare Standorte anfragen")}
    <p class="small">Wie viele Menschen Ihre Werbung sehen, hängt von Standort, Sichtbarkeit des Screens und Laufzeit ab.</p>
  </div>
  <div class="dh-adv-img"><img src="{img}dooh-werbung-supermarkt.jpg" alt="Kundin mit Einkaufstaschen vor einer digitalen Werbestele" width="352" height="329" loading="lazy"></div>
  <div class="dh-adv-panel">
    <div class="dh-finder">
      <div class="dh-finder-main">
        <h3>Wo Ihre Werbung läuft</h3>
        <dl class="dh-facts-list">
          <div><dt>Netzwerk</dt><dd>30+ aktive Werbescreens</dd></div>
          <div><dt>Preis</dt><dd>ab ca. 99 € pro Monat</dd></div>
          <div><dt>Pro Stele</dt><dd>Platz für ca. 6 Werbekunden</dd></div>
        </dl>
        <ul class="dh-types">
          <li>Supermärkte im REWE- und EDEKA-Umfeld</li>
          <li>Gastronomie</li>
        </ul>
      </div>
      <figure class="dh-finder-map">
        <svg class="map" viewBox="-10 -10 370 492" role="img" aria-label="Deutschlandkarte mit markierter Region Rhein-Main">
          <path class="land" d="{MAP}"/><path class="area" d="M78 262c14-14 40-18 58-8 16 9 22 28 16 46-6 17-22 30-42 32-21 2-40-8-46-26-5-15 2-32 14-44z"/>
          <circle class="dot" cx="109.5" cy="300" r="6"/><text x="124" y="306">Rhein-Main</text></svg>
        <figcaption>Persönlich betreut aus Weiterstadt im Rhein-Main-Gebiet</figcaption>
      </figure>
    </div>
    <p class="small">Freie Standorte und Laufzeiten bestätigen wir mit Ihrer Anfrage.</p>
  </div>
</div></section>

<section class="dh-mix"><div class="wrap">
  <div>
    <span class="eyebrow">Ihr Platz im Mediamix</span>
    <h2>Präsenz vor Ort.<br>Botschaft flexibel.</h2>
    <p class="sub">Wählen Sie die Mischung, die zu Ihrer Kampagne passt.</p>
  </div>
  <div class="dh-mix-grid">
    <div>{icon(I_TOTEM)}<h3>hyads DOOH</h3><p>Sichtbar am Ort des Einkaufs. Motive sind digital und während der Kampagne änderbar.</p></div>
    <div>{icon(I_POSTER)}<h3>Plakat</h3><p>Große, vertraute Fläche. Druck und Aushang brauchen Vorlauf, das Motiv bleibt gleich.</p></div>
    <div>{icon(I_PHONE)}<h3>Social Media</h3><p>Genaue Zielgruppen online. Im Feed wird allerdings schnell weitergescrollt.</p></div>
  </div>
</div></section>

<section class="dh-steps dh-tint-ad"><div class="wrap">
  <div class="dh-steps-top">
    <div><span class="eyebrow">Von der Idee zur lokalen Kampagne</span><h2>In drei Schritten<br>auf den Screen.</h2></div>
    <div class="flow">
      <div><span class="ring">{icon(I_SEARCH)}</span><b>01</b><h3>Region und Ziel festlegen</h3><p>Welche Standorte, welche Zielgruppe, welcher Zeitraum.</p></div>
      <div><span class="ring">{ico("pencil")}</span><b>02</b><h3>Motiv vorbereiten</h3><p>Sie liefern Ihr Motiv, oder HYSN gestaltet es für Sie.</p></div>
      <div><span class="ring">{icon(I_PLAY)}</span><b>03</b><h3>Freigeben und starten</h3><p>Wir planen die Ausspielung und spielen Änderungen ein.</p></div>
    </div>
  </div>
  <div class="dh-offer">
    <div class="dh-offer-text">
      <h3>Eine Kampagne nach Ihrem Bedarf.</h3>
      <p>Der Preis richtet sich nach Standort, Anzahl der Screens, Laufzeit und Gestaltung. Sie erhalten vorab ein schriftliches Angebot.</p>
      {btn(ask_offer, "Kampagnenangebot anfordern")}
      <p class="small">Laufzeit und Budget legen wir gemeinsam fest.</p>
    </div>
    <div class="dh-offer-img"><img src="{img}dooh-motiv-formate.jpg" alt="Dasselbe Café-Motiv auf einem Screen im Hochformat und einem im Querformat" width="729" height="345" loading="lazy"></div>
    <div class="dh-offer-side">
      <h3>Kein Motiv zur Hand?</h3>
      <p>HYSN gestaltet bildschirmfertige Motive und Animationen, im Hoch- und im Querformat.</p>
      {tlink(rel + "leistungen/content-creation/", "Content Creation ansehen", extra=" tlink--plain")}
    </div>
  </div>
</div></section>


<section class="dh-partner" id="standort-partner"><div class="wrap">
  <div class="dh-partner-text">
    <span class="eyebrow">02 / Für Standortpartner</span>
    <h2>Ihr Standort<br>kann mehr.</h2>
    <p class="sub">Professionell betreute Werbung lokaler Unternehmen auf Ihrer Fläche, mit einem vereinbarten Anteil an den Werbeeinnahmen für Sie.</p>
    <div class="dh-points">
      <div>{icon(I_BARS)}<div><strong>Werbeeinnahmen</strong><p>Ihr Anteil richtet sich nach dem Modell, die Höhe nach Lage und Werbenachfrage.</p></div></div>
      <div>{icon(I_GEAR)}<div><strong>Betreut von HYSN</strong><p>Montage, Inhalte und Betrieb, mit 5 Jahren Garantie auf die Hardware.</p></div></div>
      <div>{icon(I_SHIELD)}<div><strong>Inhalte nach Ihren Regeln</strong><p>Sie bestimmen Branchen, Qualität und Ausschlüsse.</p></div></div>
    </div>
    <div class="actions">{btn(ask_site, "Standort prüfen lassen")}{tlink(rel + "partnerprogramm/", "Zum Partnerprogramm", extra=" tlink--plain")}</div>
  </div>
  <div class="dh-partner-img"><img src="{img}dooh-standort-eingangshalle.jpg" alt="Großzügiger Innenbereich mit Pflanzen und einer digitalen Werbestele im Hochformat" width="900" height="569" loading="lazy"></div>
</div></section>

<section class="dh-share dh-tint-pa"><div class="wrap">
  <div class="dh-share-head">
    <span class="eyebrow">Das Erlösmodell</span>
    <h2>Klare Anteile.<br>Fest vereinbart.</h2>
    <p class="sub">Drei Modelle zur Wahl. Welches zu Ihrem Standort passt, klären wir gemeinsam.</p>
  </div>
  <div class="dh-share-body">
    <div class="dh-share-grid">
      <div class="dh-share-col dh-share-col--op"><span class="dh-share-tag">Betreibermodell</span>
        <div class="dh-stages"><div><b class="dh-num">10 %</b><span>während der Refinanzierung</span></div><span class="dh-arrow">{icon(I_NEXT)}</span><div><b class="dh-num">20 %</b><span>nach der Amortisation</span></div></div>
        <p>HYSN investiert, Sie stellen die Fläche.</p></div>
      <div class="dh-share-col"><span class="dh-share-tag">Co-Investment</span>
        <div class="dh-stages"><div><b class="dh-num">50/50</b><span>Aufteilung der Werbeeinnahmen</span></div></div>
        <p>Gemeinsam mit HYSN investiert.</p></div>
      <div class="dh-share-col"><span class="dh-share-tag">Eigeninvestition</span>
        <div class="dh-stages"><div><b class="dh-num dh-num--word">Eigentum</b><span>volle Kontrolle, volle Einnahmen</span></div></div>
        <p>Sie kaufen die Hardware selbst.</p></div>
    </div>
    <p class="dh-share-note"><strong>Beispielrechnung pro Stele:</strong> 6 Werbekunden à ca. 99 € ergeben 594 € Werbeeinnahmen im Monat. Ihr Anteil läge bei ca. 59 € während der Refinanzierung, ca. 119 € nach der Amortisation oder ca. 297 € im Co-Investment. Beispielwert, keine Garantie; die endgültige Aufteilung legen wir im Angebot fest.</p>
  </div>
</div></section>

<section class="dh-places"><div class="wrap">
  <div class="dh-places-head">
    <span class="eyebrow">Wo ein Screen passen kann</span>
    <h2>Orte mit Menschen.<br>Raum für Werbung.</h2>
    <p class="sub">Entscheidend sind regelmäßiger Publikumsverkehr und ein gut sichtbarer Platz.</p>
  </div>
  <div>
    <div class="dh-places-grid">{places_html}
      <div class="dh-place dh-place--ask">{icon(I_STORE)}<h3>Ihr Standort ist anders?</h3><p>Wir prüfen Sichtbarkeit, Strom und Montage.</p>{tlink(ask_site, "Standort prüfen lassen", extra=" tlink--plain")}</div>
    </div>
    <p class="dh-places-note">Beispielhafte Umgebungen. Ob ein Screen passt, klären wir für jeden Standort einzeln.</p>
  </div>
</div></section>

<section class="dh-rules dh-tint-pa"><div class="wrap">
  <div class="dh-rules-text">
    <h2>Werbung, die zu<br>Ihrem Standort passt.</h2>
    <p class="sub">Die Regeln legen wir gemeinsam fest, bevor die erste Kampagne läuft.</p>
    <ul class="dh-checks">
      <li>{icon(I_CHECK)}Zugelassene Werbebranchen festlegen</li>
      <li>{icon(I_CHECK)}Unpassende Branchen oder Wettbewerber ausschließen</li>
      <li>{icon(I_CHECK)}Eigene Hinweise mit lokalen Kampagnen kombinieren</li>
    </ul>
  </div>
  <div class="dh-rules-img"><img src="{img}dooh-inhalte-stele.jpg" alt="Werbestele im Hochformat mit einem Motiv für Kaffee und Croissant" width="483" height="336" loading="lazy"></div>
  <div class="dh-playlist">
    <h3>Beispiel-Ablauf auf Ihrem Screen</h3>
    <ol>
      <li><span class="dh-pl-ico">{icon(I_INFO)}</span><div><strong>Ihre Informationen</strong><p>Angebote und Öffnungszeiten, per Nachricht aktualisiert.</p></div></li>
      <li><span class="dh-pl-ico">{icon(I_MEGA)}</span><div><strong>Freigegebene Werbung</strong><p>Motive aus vereinbarten Branchen.</p></div></li>
      <li><span class="dh-pl-ico">{icon(I_ROTATE)}</span><div><strong>Lokale Kampagnen</strong><p>Im Wechsel für Ihren Standort geplant.</p></div></li>
    </ol>
    <p class="dh-pl-note">Beispielhafter Ablauf, Regeln pro Standort vereinbart.</p>
  </div>
</div></section>

<section class="dh-review"><div class="wrap">
  <div class="dh-review-head">
    <span class="eyebrow">In drei Schritten zum Angebot</span>
    <h2>Vom Standortfoto<br>zum Angebot.</h2>
    <p class="small">Die erste Einschätzung ist kostenlos und unverbindlich.</p>
  </div>
  <ol class="dh-review-steps">
    <li><span class="ring">{ico("camera")}</span><div><b>01</b><h3>Standort beschreiben</h3><p>Adresse, Art des Standorts, möglicher Platz und ein paar Fotos.</p></div></li>
    <li><span class="ring">{icon(I_SEARCH)}</span><div><b>02</b><h3>Potenzial prüfen</h3><p>Sichtbarkeit, Strom, Montage und passende Werbekunden.</p></div></li>
    <li><span class="ring">{ico("doc")}</span><div><b>03</b><h3>Angebot erhalten</h3><p>Modell, Umfang und Aufteilung, schriftlich festgehalten.</p></div></li>
  </ol>
  <div class="dh-review-cta">{btn(ask_site, "Standortprüfung anfragen")}</div>
</div></section>

<section class="dh-qa"><div class="wrap">
  <div><span class="eyebrow">Gut zu wissen</span><h2>Antworten auf<br>Ihre Fragen.</h2></div>
  <div class="dh-qa-cols">
    <div class="dh-qa-col dh-qa-col--ad"><h3>Für Werbetreibende</h3><div class="faq">{faq(faq_ad)}</div></div>
    <div class="dh-qa-col dh-qa-col--pa"><h3>Für Standortpartner</h3><div class="faq">{faq(faq_pa)}</div></div>
  </div>
</div></section>

<section class="cta dh-cta">{RIBBON}<div class="wrap">
  <div class="cta-text">
    <span class="eyebrow">Lokal sichtbar werden</span>
    <h2>Eine Botschaft für Ihre Region.<br>Ein Standort, der&nbsp;mehr&nbsp;kann.</h2>
    <p class="sub">Wählen Sie den nächsten Schritt, der zu Ihnen passt.</p>
    <div class="actions">{btn(ask_ad, "Werbeplatz in meiner Region anfragen")}{btn(ask_partner, "Standortpartner werden", ghost=True)}</div>
    <p class="small">Unverbindlich und kostenlos. Sie entscheiden, ob es weitergeht.</p>
    <p class="dh-cta-contact"><a href="mailto:{S["email"]}">{S["email"]}</a><a href="tel:{S["phone_href"]}">{S["phone"]}</a></p>
  </div>
  <div class="cta-brand"><span>Menschen</span><span>Standorte</span><span>Möglichkeiten</span><i></i>
    <div class="dh-brandrow"><img src="{rel}assets/img/logo/hysn-logo.svg" alt="HYSN" width="1485" height="234"><span class="dh-hyads">hyads</span></div>
    <p class="dh-contact"><a href="mailto:{S["email"]}">{S["email"]}</a><a href="tel:{S["phone_href"]}">{S["phone"]}</a></p></div>
</div></section>"""


PAGES = [dict(path="leistungen/dooh-hyads/index.html", title="DOOH & hyads | HYSN Digital Signage",
              desc="Lokal werben ab ca. 99 € im Monat auf 30+ Werbescreens im REWE- und EDEKA-Umfeld, oder mit Ihrem Standort Werbeeinnahmen erzielen: hyads von HYSN.",
              current="leistungen/dooh-hyads/", body=body, body_class="hero-page", css=["pages/dooh.css"])]
