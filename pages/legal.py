"""Impressum and Datenschutz."""
from _lib import *

def impressum(rel):
    return f"""<div class="wrap"><article class="legal">
<h1>Impressum</h1>
<h2>Angaben gemäß § 5 DDG</h2><p>{S["company"]}<br>{S["street"]}<br>{S["zip"]} {S["city"]}<br>Deutschland</p>
<h2>Vertreten durch</h2><p>Geschäftsführer: {S["md"]}</p>
<h2>Kontakt</h2><p>Telefon: <a href="tel:{S["phone_href"]}">{S["phone"]}</a><br>E-Mail: <a href="mailto:{S["email"]}">{S["email"]}</a></p>
<h2>Registereintrag</h2><p>Registergericht: {S["court"]}<br>Registernummer: {S["hrb"]}</p>
<h2>Umsatzsteuer-ID</h2><p>Umsatzsteuer-Identifikationsnummer gemäß § 27a Umsatzsteuergesetz:<br>{S["vat"]}</p>
<h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2><p>{S["md"]}<br>Anschrift wie oben</p>
<h2>Marken</h2><p>HYSN und hyads sind Marken der {S["company"]}.</p>
<h2>Verbraucherstreitbeilegung</h2><p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
<h2>Haftung für Inhalte</h2><p>Die Inhalte dieser Website wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte übernehmen wir jedoch keine Gewähr. Als Diensteanbieter sind wir für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich.</p>
<h2>Bildnachweise</h2><p>Die Abbildungen auf dieser Website sind Visualisierungen typischer Einsatzszenarien und wurden teilweise mit KI-Werkzeugen erstellt.</p>
</article></div>"""

def datenschutz(rel):
    return f"""<div class="wrap"><article class="legal">
<h1>Datenschutzerklärung</h1>
<h2>1. Verantwortlicher</h2><p>Verantwortlich für die Datenverarbeitung auf dieser Website ist die {S["company"]}, {S["street"]}, {S["zip"]} {S["city"]}, E-Mail: <a href="mailto:{S["email"]}">{S["email"]}</a>. Weitere Angaben finden Sie im <a href="{rel}impressum/">Impressum</a>.</p>
<h2>2. Hosting und Server-Logfiles</h2><p>Diese Website wird über Cloudflare bereitgestellt (Cloudflare, Inc., 101 Townsend Street, San Francisco, CA 94107, USA). Beim Aufruf der Website verarbeitet Cloudflare automatisch Informationen in sogenannten Server-Logfiles, die Ihr Browser übermittelt:</p>
<ul><li>IP-Adresse</li><li>Datum und Uhrzeit des Zugriffs</li><li>aufgerufene Seite bzw. Datei</li><li>Browsertyp und -version, Betriebssystem</li><li>Referrer-URL (zuvor besuchte Seite)</li></ul>
<p>Die Verarbeitung erfolgt auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO. Unser berechtigtes Interesse liegt in der technisch fehlerfreien und schnellen Auslieferung der Website sowie in ihrer Sicherheit, etwa dem Schutz vor Angriffen. Cloudflare speichert die Logfiles nur so lange, wie es für diese Zwecke erforderlich ist, und löscht sie anschließend, sofern keine längere Aufbewahrung zu Beweiszwecken erforderlich ist. Mit Cloudflare besteht ein Vertrag zur Auftragsverarbeitung nach Art. 28 DSGVO.</p>
<p>Cloudflare kann Daten auch in den USA verarbeiten. Cloudflare ist nach dem EU-U.S. Data Privacy Framework zertifiziert; die Übermittlung erfolgt auf Grundlage des Angemessenheitsbeschlusses der Europäischen Kommission (Art. 45 DSGVO). Ergänzend sieht der Vertrag mit Cloudflare die Standardvertragsklauseln der Europäischen Kommission vor (Art. 46 DSGVO).</p>
<h2>3. Kontaktaufnahme per E-Mail und Telefon</h2><p>Wenn Sie uns per E-Mail oder Telefon kontaktieren, auch über das Anfrageformular, das Ihre Nachricht in Ihrem E-Mail-Programm vorbereitet, verarbeiten wir Ihre Angaben (z. B. Name, E-Mail-Adresse, Telefonnummer, Angaben zu Ihrem Standort sowie übermittelte Fotos), um Ihre Anfrage zu bearbeiten. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO, sofern Ihre Anfrage auf den Abschluss eines Vertrags gerichtet ist, im Übrigen Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an der Beantwortung von Anfragen). Wir löschen die Daten, sobald sie für die Bearbeitung nicht mehr erforderlich sind und keine gesetzlichen Aufbewahrungspflichten entgegenstehen.</p>
<h2>4. Keine Cookies, kein Tracking</h2><p>Diese Website setzt keine Cookies, verwendet keine Analyse- oder Tracking-Werkzeuge und bindet keine Inhalte externer Anbieter ein. Schriften und Skripte werden direkt von dieser Website geladen.</p>
<h2>5. SSL- bzw. TLS-Verschlüsselung</h2><p>Diese Website nutzt aus Sicherheitsgründen eine SSL- bzw. TLS-Verschlüsselung. Eine verschlüsselte Verbindung erkennen Sie an „https://“ in der Adresszeile Ihres Browsers.</p>
<h2>6. Ihre Rechte</h2><p>Sie haben jederzeit das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16 DSGVO), Löschung (Art. 17 DSGVO), Einschränkung der Verarbeitung (Art. 18 DSGVO) und Datenübertragbarkeit (Art. 20 DSGVO). Soweit die Verarbeitung auf Art. 6 Abs. 1 lit. f DSGVO beruht, können Sie ihr aus Gründen, die sich aus Ihrer besonderen Situation ergeben, jederzeit widersprechen (Art. 21 DSGVO). Wenden Sie sich dazu an <a href="mailto:{S["email"]}">{S["email"]}</a>.</p>
<h2>7. Beschwerderecht bei der Aufsichtsbehörde</h2><p>Sie haben das Recht, sich bei einer Datenschutz-Aufsichtsbehörde zu beschweren. Zuständig für uns ist der Hessische Beauftragte für Datenschutz und Informationsfreiheit, Postfach 3163, 65021 Wiesbaden.</p>
<p style="margin-top:36px;color:var(--muted)">Stand: Oktober 2026</p>
</article></div>"""


PAGES = [dict(path="impressum/index.html", title="Impressum | HYSN", desc="Impressum der RA Vision GmbH, Marke HYSN.", current="", body=impressum),
         dict(path="datenschutz/index.html", title="Datenschutz | HYSN", desc="Datenschutzerklärung der RA Vision GmbH, Marke HYSN.", current="", body=datenschutz)]
