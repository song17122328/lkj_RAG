Lars Schnieder

# Communications-Based Train Control (CBTC)

Komponenten, Funktionen und Betrieb

4. Auflage

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/c37452aef236b811ba7abfaf5e94d870e8b35d79106c69751cf063dfe2c864af.jpg)

# Communications-Based Train Control (CBTC)

# SPRINGER NATURE

# FLASHCARDSINSIDE

# SN Flashcards Microlearning

Schnelles und effizientes Lernen mit digitalen Karteikarten – für Arbeit oder Schule!

# These Mochlichkeiten bieten Ihnen die SN Flashcards:

- Jederzeit und überall auf Ihrhem Smartphone, Tablet oder Computer lernen  
- Den Inhalt des Buches lernen und Ihr Wissen testen  
- Sich durch verschiedene, mit multimedialen Komponenten angereicherte Fragotypen motivieren setzen und zwischen drei Lernalalgorithmen (Langzeitgedächtnis-, Kurzezeitgedächtnis- oder Prüfungs-Modus) wahren  
- Ihre eigenen Fragen-Sets erstellen, um ihre Lernerführung zu personalisieren

# So greifen Sie auf ihre SN Flashcards zu:

1. Gehen Sie auf die 1. Seite des 1. Kapitals这部分 Buches und folgen Sie den Anweisungen in der Box, um sich für einen SN Flashcards-Account anzumelden und auf die Flashcards-Inhalte für diese Buch zuzugreifen.  
2. Laden Sie die SN Flashcards Mobile App aus dem Apple App Store oder Google Play Store herunter, öffnen Sie die App und folgen Sie den Anweisungen in der App.  
3. Wahlen Sie in der mobilen App oder der Web-App die Lernkarten für diesen Buch aus und beginnen Sie zu lernen!

Sollten Sie Schwierigkeiten haben, auf die SN Flashcards zuzugreifen, schreiben Sieitte eine E-Mail an customerservice@springernature.com und geben Sie in der Betreffzeile SN Flashcards und den Buchtitel an.

# Communications-Based Train Control (CBTC)

Komponenten, Funktionen und Betrieb

4. Auflage

Lars Schnieder

ESE Engineering und Software-Entwicklung GmbH

Braunschweig, Deutschland

ISBN 978-3-662-68951-6

ISBN 978-3-662-68952-3 (eBook)

https://doi.org/10.1007/978-3-662-68952-3

Die Deutsche Nationalbibliothek verzeichnet diese Publikation in der Deutschen Nationalbibliografie; detailierte bibliografische Daten sind im Internet über https://portal.dnb.de abrufbar.

$\odot$  Der/die Herausgeber bzw. der/die Autor(en), exklusiv lizenziert an Springer-Verlag GmbH, DE, ein Teil von Springer Nature 2020, 2021, 2022, 2024

Das Werk einschließlich aller seiner Teile ist urheberrechtlich geschützt. Jede Verwertung, die nicht ausdrücklich vom Urheberrechtsgesetz zugelassen ist, bedarf der vorherigen Zustimmung des Verlags. Das gilt insbesondere für Vervielfaltigungen, Bearbeitungen, Übersetzungen, Mikroverfilmen und die Einspeicherung und Verarbeitung in elektronischen Systemen.

Die Wiedergabe von allgemein beschreibenden Bezeichnungen, Marken, Unternehmensnamen etc. in thisom Werk bedeutet nicht, dass diese frei durch jedermann benutzt werden dürfen. Die Berechtigung zur Benutzung unterliegt, auch ohne gesonderten Hinweis hierzu, den Regeln des Markenrechts. Die Rechte des jeweiligen Zeicheninhabers sind zu beachten.

Der Verlag, die Autoren und die Herausgeber gehen davon aus, dass die Angaben und Informationen in thisem Werk zum Zeitpunkt der Veröffentlichung vollständig und korrekt sind. Weder der Verlag noch die Autoren oder die Herausgeber übernehmen, ausrücklich oder implizit, Gewähr für den Inhalt des Werkes, etwaige Fehler oder Äußerungen. Der Verlag bleibt im Hinblick auf geografische Zuordnungen und Gebietsbezeichnungen in ver-öffentlichen Karten und Institutionsadressen neutral.

Planung/Lektorat: Alexander Grün

Springer Vieweg ist ein Imprint der eingetragenen Gesellschaft Springer-Verlag GmbH, DE und ist ein Teil von Springer Nature.

Die Anschrift der Gesellschaft ist: Heidelberger Platz 3, 14197 Berlin, Germany

Wenn Sie diesen Produkt entsorgen, geben Sie das Papieritte zum Recycling.

# INNOVATIVE SOLUTIONS FOR ALL TYPES OF RAILWAYS

Stadler Signalling offers tailor-made signalling solutions in the Mainline, Branchline, Light Rail Vehicle (LRV), Metro and Depot segments, as well as digital solutions and services to ensure efficient, digital and sustainable rail operations.

www.stadlerrail.com

# Vorwort zur 4. Auflage

Jeden Tag nutzen Millionen Menschen den öffentlichen Personennahverkehr. Die Metropolen dieser Welt stüden ohne leistungsfähige Schienenverkehrssysteme jeder Tag vor dem Verkehrsinfarkt. Die vorhandene Schiereninfrastrukturstoß却彼ch vielerorts an die Grenzen ihrer Kapazität. Der Schlüssel zu einer Steigerung der Leistungsfähigkeit städtischer Schienenverkehrssysteme liegt in ihrer Automatisierung. In den letzten Jahrzehnten haben weltweit immer mehr Städte in leistungsfähige Schienenverkehrssysteme investiert. In Deutschland wurde lange Zeit nicht in die Modernisierung von U- und Stadtbahn-systemen investiert. Die technologische Basis in den Städten ist davon oftmales veraltet und hat an manchen Orten die Grenzen ihrer technischen Lebensdauer bereits übersritten. In einigen Städten werden daher die Verkehrsunternehmen in den nachsten Jahren ihre Infrastruktur umfassend erneuern. Es sind also auch in Deutschland erhebliche Investitionen in die Erneuerung der signaltechnischen Infrastruktur von U- und Stadtbahnsystemen zu erwarten. Dieses Buch stellt die gültigen normativen Grundlagen hochautomatisierter Schienenverkehrssysteme dar. Die Darstellung in thisem Buch basiert auf unseren Erfahrungen in der Beratung von Verkehrsunternehmen sowie是我的er praktischen Tätigkeit in der Prüfung von Bauunterlagen sowie der Durchführung von Prüfungen zur Inbetriebnahme von Zugsicherungsanlagen internationaler U- und Stadtbahren. Mein Dank gilt den Experten der Systemhäuser Alstom, Hitachi, Siemens und Stadler. Ich habe hier in vielen Fachgesprächen ein vertieftes Verständnis der komplexen technischen Zusammenhänge von CBTC-Systemen gewinnen können. Den folgenden Firmen und Betriebern danke ich für die freundliche Genehmigung zur Verwendung von Bilddateien in thisem Buch (Angaben in alphabetischer Reihenfolge):

Alstom Transport Deutschland GmbH  
- Deuta-Werke GmbH  
- Frauscher Sensortechnik GmbH  
HASLER RAIL AG  
Huber + Suhner AG  
Lenord, Bauer & Co. GmbH  
- PINTSCH GmbH

- Sitron Sensor GmbH  
Stadtwerke Verkehrsgesellschaft Frankfurt am Main mbH (VGF)  
VAG Verkehrss-Aktiengesellschaft Nurnberg  
VIA Consulting & Development GmbH

Ein persönlicher Dank für die vorliegende 4. Auflage dieseres Buches gilt Herrn Univ.-Prof. Dr.-Ing. Nils Nieuß. Er gab mir die Möglichkeit, im internationalen Studienprogramm Railway Systems Engineering an der RWTH Aachen ein eigenes Lehrangebot zu automatisierten Nahverkehrssystemen zu etablieren. Die Diskussionen mit den internationalen Studierenden motivieren mich zur kontinuierlichen Weiterentwicklung dieseres Buches. Darüber hinaus möchte ich mich bei den Mitarbeitern nationaler Verkehrsunternehmen (Stadtwerke Verkehrsgesellschaft Frankfurt am Main (VGF), Stuttgarter Straßenbahren AG, Hamburger Hochbahn AG, Münchner Verkehrsgesellschaft mbH (MVG) sowie VAG Nürnberg) sowie internationaler Verkehrsunternehmen (Wiener Linien, Metropolitan Area Transit Authority, sowie der Metro Dubai) bedanken. Für mich war es sehr wertvoll, mit Praktikern aus den Verkehrsunternehmen in vielen Diskussionen die betrieblichen Zusammenhänge eines automatisierten Bahnbetriebs zu erörtern. Zu gutter letzt danke ich是我的 Frau Juliane und unseren Zwillingen Clara und Christian davon, dass sie myne Leidenschaft für die Verkehrsautomatisierung akzeptieren und zuweilen auch teilen.

Braunschweig, Deutschland  
Juni 2024

Lars Schnieder

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/4a163bb48b93ba0acdb05527c16bfff860ed63b4525377d22e3a7bee66ce51e2.jpg)

# Gestalte die Zukunft der Mobilität!

Gestalte mit uns den CBTC Rollout in Deutschland und der Welt! Ob Vertrieb, Entwicklung, Projektleitung, Engineering, Logistik, Fertigung oder Montage: Du wills eine Karriere mit echtem Impact? Steige bei Siemens ein oder entdecke unsere Studie-Jobs!

# Inhaltsverzeichnis

1 Motivation und Hintergrund 1

1.1 Entwicklung urbaner Mobilität 2  
1.2 Vorteile automatisierter Schienenverkehrssysteme 5

Literatur 9

2 Systemkomponenten und Umsysteme automatischer Zugbeeinflussungssysteme 11

2.1 Systemkomponenten automatischer Zugbeinflussungssysteme 12

2.1.1 Streckenseitige Ausrüstung (ATP Wayside) 13  
2.1.2 Fahrzeugseitige Ausrüstung (ATP onboard und ATO onboard) 17  
2.1.3 Datenkommunikationsystem 18  
2.1.4 Zugleitsystem (Automatic train Supervision, ATS) 23

2.2 Umsysteme automatischer Zugbeeinflussungssysteme 27

Literatur 35

3 Automatisierungsgrade automatischer Zugbeeinflussungssysteme 37

3.1 Grade of Automation 0: Zugbetrieb auf Sight 40  
3.2 Grade of Automation 1: Nicht automatisierter Zugbetrieb 40  
3.3 Grade of Automation 2: Halbautomatischer Zugbetrieb 41  
3.4 Grade of Automation 3: Begleiteter Fahrerloser Zugbetrieb 41  
3.5 Grade of Automation 4: Unbegleiteter Fahrerloser Zugbetrieb 42

Literatur 42

4 Betriebsarten und Betriebsartenübergänge im automatisierten Betrieb . . . 43

4.1 Betriebsarten im Überblick 44

4.1.1 Betriebsarten fur den Regelbetrieb 45  
4.1.2 Betriebsarten für Gefahren- und Störzustände 46  
4.1.3 Betriebsarten fur Ausschaltzustände 48  
4.1.4 Betriebsarten für Fahrten auf nicht mit CBTC ausgerüsteten Bestandsstrecken 49

4.2 Betriebsartenübergänge in halbautomatischen betriebenen Systemen 50

4.2.1 Wechsel zwischen Restricted Mode und Supervised Manual Mode 50  
4.2.2 Wechsel zwischen Supervised Manual Mode und Automatic Mode 52  
4.2.3 Wechsel zwischen Automatic Mode und Full Automatic Mode bei Kehrfahrten 53  
4.2.4 Wechsel zwischen Automatic Mode und Full Automatic Mode im Betriebshof 55  
4.2.5 Wechsel zwischen Automatic Mode und Restricted Mode bei Störungen 56

4.3 Betriebsartenübergänge in unbegleitet fahrerlos betriebenen Systemen 58

4.3.1 Wechsel zwischen Ausschaltzuständen und unbegleitetem fahrerlosen Betrieb 58  
4.3.2 Wechsel zwischen Gefahr- und Störzuständen und unbegleitetem fahrerlosen Betrieb 59

Literatur. 59

5 Hauptfunktionen automatischer Zugbeeinflussungssysteme 61

5.1 Hauptfunktion Sichern der Zugbewegung 62

5.1.1 Oberfungion Sichern des Fahrwegs 62  
5.1.2 Oberfunktion Sichern der Abstandshaltung 65  
5.1.3 Oberfunktion Sichern der Geschwindigkeit und Richtung 66

5.2 Hauftfunktion Fahren des Fahrzeugs 76

5.2.1 Oberfungtion Bestimmendes Fahrprofils 76  
5.2.2 Oberfunktion Steuern der Züge in Abhängigkeit des Fahrprofils 79

5.3 Hauptfunktion Überwachen der Profilfreiheit 85

5.3.1 Oberfungtion Verhinderung der Kollision mit Objekten 85  
5.3.2 Oberfungkntion Verhinderung der Kollision mit Personen im Gleis 86

5.4 Hauptfunktion Überwachen des Fahrgastwechsels 89

5.4.1 Oberfunktion Steuern und Überwachen der Türfreigabe 89  
5.4.2 Oberfunktion Verhindern der Verletzung von Personen zwischen Fahrzeugen 90  
5.4.3 Oberfungtion Sichern der Bahnsteigkante 90  
5.4.4 Oberfunktion Sicherstellen der Abfertigungsbedingungen 98

5.5 Hauptfunktion Automatischer Zugbetrieb 100

5.5.1 Oberfunktion Einsetzen und Aussetzen von Fahrzeugen 100  
5.5.2 Oberfunktion Betriebenen Fahrzeugs zwischen betrieblichen Halten 101  
5.5.3 Oberfunktion Überwachung des Fahrzeugzustands. 103

5.6 Hauptfunktion Störfallerkennung und Störfallmanagement 105

5.6.1 Oberfungtion Fahrgastalarmmeldungen 105  
5.6.2 Oberfunktion Brandmeldung 108  
5.6.3 Oberfunktion Evakuierung. 111  
5.6.4 Oberfunktion Hinderniserkennung 114  
5.6.5 Oberfunktion Entgleisungserkennung 115

Literatur. 115

6 Verlächlichkeit automatischer Zugbeeinflussungssysteme 117

6.1 Sicherheit 118

6.1.1 Funktionale Sicherheit (Safety) 118  
6.1.2 Angriffssicherheit (Security) 124

6.2 Verfugbarkeit (Availability) 125

6.2.1 Optimierung der Instandhaltbarkeit (Maintainability) zur Steigerung der Verfügbarkeit 126  
6.2.2 Erhöhung der Zuverlösigkeit (Reliability) zur Steigerung der Verfügbarkeit 128  
6.2.3 Fehlertolerante Systeme zur Steigerung der Verfugbarkeit 129

Literatur. 130

7 Abwagung von Kosten und Nutzen automatischer Zugbeeinflussungssysteme 133

7.1 Ermittlung der Kostenkomponente mittels Lebenszykluskostenrechnung 134

7.1.1 Elemente der Lebenszykluskosten 134  
7.1.2 Berechnung der Lebenszykluskosten. 136  
7.1.3 Ergebnisse der Analyse der Lebenszykluskosten. 137

7.2 Ermittlung der Nutzenkomponente mit Betriebssimulationen und Verkehrsmodellen 138

7.2.1 Simulative Untersuchung der Leistungsfähigkeit signaltechnischer Ausrüstungsvarianten 138  
7.2.2utzung der hoheren Leistungsfähigkeit fur Anpassungen im OPNV-Angebot. 142  
7.2.3 Bewertung des verkehrlichen Nutzens von Anpassungen im ÖPNV-Angebot. 143

Literatur. 144

8 Umbau, Test und Inbetriebnahme automatischer Zugbeeinflussungssysteme 147

8.1 Definition der Migrationsstrategie 148

8.1.1 Doppelausrüstung der Fahrzeuge. 150  
8.1.2 Doppelausrüstung der Streckeneinrichtungen 151

8.2 Anwendungsspezifische Konfiguration automatischer Zugbeeinflussungssysteme 153

8.2.1 Kategorien streckenspezifischer Konfigurationsdaten 153  
8.2.2 Kategorien Fahrzeugspezifischer Konfigurationsdaten 154  
8.2.3 Qualitätsmerkmale von Konfigurationsdaten 154  
8.2.4 Qualitatssichernde Prozesse fur Konfigurationsdaten 155  
8.2.5 Erfassung streckenspezifischer Konfigurationsdaten 156

8.3 Umrüstung der Fahrzeuge mit CBTC-Fahrzeugausrüstung 156

8.3.1 Definition betrieblicher Anwendungsfälle 157  
8.3.2 Definition Mechanische Integration des CBTC-Fahrzeuggeräts 157  
8.3.3 Elektrische Integration des CBTC-Fahrzeuggeräts 159

8.4 Umrüstung der Strecke mit CBTC-Streckenausrüstung 160  
8.5 Definition der Teststrategie und Testdurchführung 162

8.5.1 Umwelttests 162  
8.5.2 Fabriktests 163  
8.5.3 Fahrzeugtests 164  
8.5.4 Testgleis im Betriebshof 165  
8.5.5 InbetriebnahmetestsderStreckeneinrichtung 166

8.6 Anpassung betrieblicher Regelwerke für den automatisierten Betrieb . 169

8.6.1 Prinzipien der Regelwerksanpassungen in Erneuerungsprojekten 169  
8.6.2 Ablauf der Regelwerkserstellung im Erneuerungsprojekt. 171  
8.6.3 Rollen und Verantwortlichkeiten der Regelwerkserstellung im Erneuerungsprojekt. 172

8.7 Schulung des Betriebspersonals. 174

8.7.1 Schulungen der Fahrer 174  
8.7.2 Schulungen der Fahrdienstleiter 175  
8.7.3 Schulungen des Instandhaltungspersonals 176

Literatur. 177

9 Perspektiven und zukünftige Herausforderungen 179

9.1 Entwicklung der installierten Basis 180  
9.2 Standardisierung von Systemlösungen 180  
9.3 Integration der Straβenverkehrstechnik in Stadtbahnsystemen 181  
9.4 Alternative Funktionsaufteilung zwischen Fahrzeug und Strecke. 183

9.4.1 Zentralisierung Sicherheitsrelevanter Anwendungen in Rechenzentren 183  
9.4.2 Fahrzeugzentrierte Funktionsallokation. 184

Literatur. 185

Stichwortverzeichnis 187

# Abkürzungsverzeichnis

ATC Automatic Train Control

ATO Automatic Train Operation

ATP Automatic Train Protection

ATS Automatic Train Supervision

CAPEX Capital Expenditures

CBTC Communications-Based Train Control

CCTV Closed Circuit Television

COTS Commercial off-the-shelf

DTO Driverless Train Operation

EMV Elektromagnetische Verträgelichkeit

GoA Grade of Automation

HMI Human Machine Interface

IP Internet Protocol

ITCS Intermodal Transport Control System

LCC Life Cycle Costs

LRU Line Replaceable Unit

LTE Long Term Evolution

MDT Mean Down Time

MTBF Mean Time Between Failure

MTTR Mean Time to Repair

MUT Mean Up Time

NTO Non-automated Train Operation

OC Object Controller

OPEX Operational Expenditures

ÖPNV Öffentlicher Personannahverkehr

QoS Quality of Service

RAMSS Reliability, Availability, Maintainability, Safety, Security

SCADA Supervisory Control and Data Acquisition

SIL Safety Integrity Level

STO Semi-automated Train Operation

<table><tr><td>TCMS</td><td>Train Control &amp; Monitoring System</td></tr><tr><td>TETRA</td><td>Terrestrial Trunked Radio</td></tr><tr><td>THR</td><td>Tolerable Hazard Rate</td></tr><tr><td>TOS</td><td>Train Operation On Sight</td></tr><tr><td>USV</td><td>Unterbrechungsfreiie Stromversorgung</td></tr><tr><td>UTO</td><td>Unmanned Train Operation</td></tr><tr><td>WLAN</td><td>Wireless Local Area Network</td></tr></table>

# Motivation und Hintergrund

1

# SN Flashcards

Als Käfer*in diesen Buches können Sie kostenlos unsere Flashcard-App „SN Flashcards" mit Fragen zur Wissenschaftung und zum Lernen von Buch-inhalten nutzen.

1. Gehen Sieitte auf https://flashcards.springernature.com/login und  
2.(erstellen Sie ein Benutzerkonto,indem Sie ihre Mailadresse angegeben und ein Password vergeben.  
3. Verwenden Sie den folgenden Link, um Zugang zu Ihr dem SN Flashcards Set zu halten:  $\triangleright$  https://sn.pub/sK5mLQ

Sollte der Link fehlen oder nicht Funktionieren, senden Sie unsitte eine E-Mail mit dem Betreff „SN Flashcards“ und dem Buchtitel an customerservice@springernature.com

Weltweitziehen immer mehr Menschen in die Städte. Gleichzeitig nimmt die Verkehrns- nachfrage stetig zu. Dort, wo aktuell noch keine leistungsfähigen öffentlichen Verkehrssysteme vorhanden sind, müssen diese neu errichtet werden. Dort, wo bestehende öffentliche Verkehrssysteme an die Grenzen ihrer Leistungsfähigkeit stoßen, müssen durch umfassende technische und betriebliche Maßnahmen Kapazitätssteigerungen erzielt werden. In thisem Abschnitt wird zunachst die weltweit zu beobachtende Entwicklung urbaner Mobilität beschreiben. Die hieraus resultierenden Herausforderungen können durch die Vorteile automatisierter Verkehrssysteme adressiert werden. Dies wird ebenfalls in thisem einführenden Kapitel beschreiben. In thisem Kapitel wird zunachst die Entwicklung der

urbanen Mobilität aufgezeichnet (vgl. Abschn. 1.1). Daraus wird die weltweit zu beobachtende Tendenz zum Einsatz zunehmendHigher automatisierter Schienenverkehrssysteme motiviert, deren Vorteile in Abschn. 1.2 dargestellt werden.

# 1.1 Entwicklung urbaner Mobilität

Zum ersten Mal in der Menschheitsgeschichte lebt die Mehrheit der Weltbevolkerung in den Städten. Bis zur Mitte des 21. Jahrhunderts werden voraussichtlich)sogar mehr als zwei Drittel der Erdbewohner in urbanen Zentren leben (United Nations 2015). Dieser raumstrukturelle Veränderungsprozess wird auch als Urbanisierung bezeichnet. Um die Bedürfnisse des tätiglichen Lebens zu befriedigen (Wohnen, Versorgung, Arbeit, Ausbildung, Erholung usw.), mussen die Menschen mobil sein und sich in ihrer Stadt fortbewegen konnen. Den zunehmenden Mobilitätsbedarf dem motorisierten Individualverkehr zu überlassen, ware ökologisch und gesamtwirtschaftlich verheerend. Nachhaltige Mobilitätskonzepte zu entwickeln, ist davon vor allem auch hinsichtlich des Ressourcenund Klimaschutzes ein wichtiges Anliegen. Hierbei nimmt ein leistungsfähiger öffentlicher Personennahverkehr (ÖPNV) eine zentrale Rolle ein. In den Industriestaaten schreiben parallel zu der zuvor beschriebenen Urbanisierung auch die Suburbanisierung (englisch suburban - am Stadtrand) voran. Suburbanisierung bezeichnet hierbei die Abwandlung stadtlicher Bevolkierung oder stadtlicher Funktionen wie beispelsweise Industrie und Dienstleistungen aus der Kernstadt in das stadtische Umland. Diese Abwandlung führt allgemein zu einer Zunahme der Penderbewegungen. Heraus resultiert eine höhere Belastung der Verkehrsinfrastruktur insbesondere in den morgendlichen und abendlichen Hauptverkehrszeiten.

Urbanisierung und Suburbansierung erfordern die Erhöhung der Beförderungskapazität städtischer Verkehrsininfrastrukturten. Die Beförderungskapazität bestimmt sich hierbei in der Betriebsplanung aus dem Produkt der Anzahl der Führten pro Stunde und der Gefäßgroße (Anzahl der verfügbaren Sitz- und Stehlplätze) der eingesetzten Fahrzeugflotte (Schnieder 2018). Die Beförderungskapazität wird somit wesentlich bestimmt von der Anzahl der Zugfahrten, die in einem bestimmten Betriebszeitaum auf einer Strecke in einer Fahrrichtung durchgeführt werden konnen. Dies wird auch als Leistungsfähigkeit einer Strecke bezeichnet (Adler et al. 1981). Die Leistungsfähigkeit ist abhängig von verschiedenen Faktoren wie die bestehende Infrastruktur, Charakteristika der Fahrzeuge und der Betriebsorganisation. Dies erfordert insgesamt einen ganzheitlichen Ansatz der Systemgestaltung, wie dieser im Ishikawa-Diagramm in Abb. 1.1 dargestellt ist. Die im Diagramm dargestellen Ansatzpunkte zur Erhöhung der Leistungsfähigkeit werden nachfolgend diskutiert:

- Optimierung der Fahrzeugengenschaften: Die eingesetzten Fahrzeuge leisten einen Beitrag zur Steigerung der Leistungsfähigkeit einer Strecke. Die Distanz zwischen Stationshalten, die Fahrzeuge mit der maximal zulässigen Geschwindigkeit fahren kon-

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/9f3cfaee6e56f533ab7979fd38b2837682b2b9db779903fc2258fd5063f18d18.jpg)  
Abb.1.1 Kapazitätserhöhung als ganzheitlicher Systemansatz. (Eigene Darstellung)

nen, kann erhöht werden, indem die Fahrzeuge eine verbesserte Fahrdynamik erhalten. Dies umfasst darüber einen higheren Beschleunigungsvermögen auch einhigheres Bremsvermögen. Darüber hinaus kann mit der Fahrgastwechselzeit in den Haltestellen ein weiterer Storeinfluss in städtischen Bahnsystemen adressiert werden. Um den Fahrgastwechsel in den Stationen zu beschleunigen, kann auch die Anzahl und Breite der Turen bewusst gestaltet werden (obwohl dies auf Kosten des Sitzplatzangebotes geht). In seltenen Fälle sind an beiden Seiten des Fahrzeugs Bahnsteige, sodass die Turen in den Haltestellen auf beiden Seiten geöffnet werden konnen. Die Betreiber verbinden hiermit die Hoffnung, dass die Fahrgäste das Fahrzeug auf der einen Seite besteigen und auf der anderen Seite verlassen. In der Praxis muss dies mit einer prazisen und verstandlichen Fahrgastinformation verknüpfert werden. Dies soll unnötige Hektik beim Haltestellenaufenthalt vermeiden und sicherstellen, dass die Fahrgäste den Zug nicht über die „falsche“ Seite verlassen.

- Optimierung der Gleistopologie: Durch die Gestaltung der Gleispläne können bestehende Einschränkungen reduziert werden. Beispiele hierfür sind veränderte Weichen und Gleisbogenradien für höhere Streckengeschwindigkeiten. Außen dem konnen bestehende Fahrstraßeusschlüsse behoben werden (Pachl 2016) sowie die Anordnung von Kreuzungs-und Überholstellen bei eingleisiger Betriebsführung geändert werden. Die Anzahl und Position von Kehr- und Abstellanlagen ist insbesondere für Störungen im Betriebsablauf relevant. Defekte Fahrzeuge konnen im Falle von Störungen in Kehr- und Abstellanlagen weggeschoben werden und behindern so nicht mehr den Betriebsablauf. Je mehr Kehr-

und Abstellanlagen im Linienverlauf zur Verfügung stehen,esto hoher ist die Flexibilität für den Disponenten in der Bearbeitung der Störung. Kehranlagen im Linienverlauf bieten darüber hinaus die Möglichkeit zum frühereitigen Abkehren von Fahrzeugumläufen im Falle von Versprütungen. Auf diese Weise kann eine Versprüttungsübertragung unterbunden werden und eine regelmäßiger Betriebsablauf wiederhergestellt werden.

- Optimierung der Stationsbauwerke: In Summe muss in städtischen Nahverkehrssystemen ein optimaler Fahrgastfluss erreicht werden. Dies bezieht in einem ganzheitlichen Ansatz auch die Stationsbauwerke mit in die Betrachtung ein. Durch breite Bahnsteige und eine gänstige Anordnung von Treppen, Fahrtreppen und Aufzügen konnen Reisende schnell die Station verlassen. Sie blockieren dann nicht den Bahnsteig für die aus dem nachsten eintreffenden Zug aussteigenden Fahrgäste. Damit die Fahrgäste den Stationsbereich unverzüglich verlassen konnen, ist auch eine adressatenerierte Fahrgastinformation im Sinne eines Gebäudefleitsystems unverzichtbar. Darüber hinausspiel auch das gewährte Abfertigungsvergfahren eine nicht zu vernachlässigende Rolle. So kann beispelsweise durch eine gezielte Unterstützung der Abfertigung durch Personal in den Stationen die Punktlichkeit insbesondere in den Hauptverkehrszeiten erhöht werden. Konnen durch die Anordnung von Bahnsteigtären Gefährdungen durch im Bahnsteigbereich in die Gleise fallende Personen ausgeschlossen werden, ist auch eine höhere Einfahrsgeschwindigkeit von Zügen möglich.  
- Optimierung des Betriebsprogramms: Ein Ansatz der Erhöhung der Leistungsfähigkeit über das Betriebsprogramm eines Schienenverkehrssystems ist die Reduktion der Verkehrs- und Betriebshaltezeiten. Dies geschieht zum Beispiel durch im Rahmen der Dispositionsstrategie getroffene Entscheidungen zum Haltentfall im Falle betrieblicher Störungen. Ein weiterer Ansatz ist die Umsetzung bedarfsgerechter Haltezeiten. Im Fahrplan sind theoretische Haltezeiten für jeder Station mit einer geschätzten durchschnittlichen Fahrgastwechselzeit vordefiniert. Die tatsächlichen Fahrgastströme sind jedoch nicht regelmäßig und zum Teil unvorhersebar. Infolgedessen können sich theoretische Haltezeiten als unzureichend erweisen, d. h. sie werden gegenüber den tatsächlichen Fahgasträmen unter- oder überschätzt. Im Falle einer zu kurzen Haltezeit im Verhältnis zur Fahrgastmenge auf dem Bahnsteig drängeln die Fahrgäste entweder beim Einsteigen in den Zug, was zu Tür- und Betriebsstörungen führen kann, oder die Fahrgäste warten auf den nachsten Zug. Umgekehrt warten die Fahrgäste bei zu langer Haltezeit an Bord, bis der Zug die Türen schließt und vom Bahnhof abfahr (Leveque 2020). Als weiterer Ansatz konnen heterogene Betriebsprogramme harmonisiert werden, um eine höhere Leistungsfähigkeit der Strecke zu erreichen. Ein Beispiel hierfür ist neben der Angleichung unterschiedlicher Zuggeschwindigkeiten die Bündelung von Trassen von Tügen unterschiedlicher Fahrrichtung bei eingleisiger Betriebsführung, bzw. die Zusammenfassung der Zugtrassen von Tügen gleicher Geschwindigkeit. Allerdings ist dieser Ansatz wegen der in der Regel zweigleisigen Betriebsführung und der oftmans überwiegend homogenen Struktur der Fahrzeugflotte bei leistungsfähigen städtischen Schierenverkehrssystemen ihrer theoretischer Natur. Ein weiterer Ansatz eines optimalen Betriebsprogramms ist die Umsetzung eines bedarfsgerechten Fahrzeugeinsatzes. Die Überwachung der Auslastung

von Stationen und Zügen erfolgt oftmals mittels Videüberwachung oder durch Sicherheitspersonal. Die Entwicklung der Passagierströme anhand von Daten technischer Systeme, die zur Personenzahlung dienen, erfasst und analysiert werden. Dazu gehoren stereoskopische Kameras (3D-Sensoren), Videüberwachungssysteme (CCTV-Kameras) und Ticketdrehkreuze. Der Betreiber kann diese Ist-Daten nutzen, um z. B. weitere Züge in das Netz einzubringen oder alternative Züge zu Netzabschnitten mit mehr Transportbedarf umzuleiten (Pancini Fitzek et al. 2021).

- Einsatz leistungsfähiger Zugsicherungssysteme: Kontinuierlich wirkende bidirektionale Zugbeeinflussungssysteme (Communications-Based Train Control, CBTC) nehmen in der Erhöhung der Leistungsfähigkeit einer Strecke eine zentrale Rolle ein. Den größten Einfluss hat hierbei, dass ein Übergang von einem Fahren im festen Raumabstand (englisch: fixed block) zu einem Fahren im wandernden Raumabstand (englisch: moving block) möglich wird. Darüber hinaus wirkt sich die Sicherungslogik der Fahrstraßensicherung ebenfalls positiv auf die Leistungsfähigkeit aus. Beispiele hierfür sind die für die Fahrstraßenbildung und -auflösung erforderlichen Zeiten. Diese können insbesondere durch einzel-elementweises Auflösen der Fahrstraße maßgeblich reduziert werden (Zoeller 2002). Außen dem erfolglichen Nachrucksignale die Vorbeifahrt des Folgezuges bereits nach dem Räumen eines Teils des Bahnsteigs vom vorausfahrenden Zug (Adler et al. 1981). Gleiswechselbetrieb bezeichnet die vollwertige Signalisierung der Streckengleise in beiden Fahrrichtungen. Bei vollausgebauten Strecken ist die Blockteilung in beiden Gleisen und Richtungen identisch. Damit bieten beside Gleise unabhängig von der Fahrrichtung dieserle Leistungsfähigkeit. In der Vergangenheit wurden zahlreiche Strecken für die Fahrten entgegen der gewöhnlichen Fahrrichtung mit weniger oder gaz ohne zwischenliegende Blockabschnittte ausgerüstet. Dem geringeren Aufwand bei Einrichtung und Instandhaltung stehen dann jedoch insbesondere im Störungsfall bei Sperrung eines Gleises oder bei Bauarbeiten eine deutliche Reduzierung der Leistungsfähigkeit gegenüber.

- Automatisierung der Betriebsführung: Durch den Einsatz einer automatischen Fahrund Bremssteuerung konnen Fahrzeitschwankungen des menschlichen Fahrers eliminiert werden. Die automatische Fahr- und Bremssteuerung steht hierbei in engem Zusammenhang mit einer vorausschauenden Disposition, da abhängig von der Betriebssituation die für den Zug optimale Fahrstrategyge ausgewählt werden kann. Des Weiteren werden Belegungskonflikte früherzeitig erkannt und durch angemessene Dispositions-strategien früherzeitig gelöst.

# 1.2 Vorteile automatisierter Schienenverkehrssysteme

Automatisierte Zugbeeinflussungssysteme vereinen die im vorherigen Abschnitt dargeistellen Beiträge leistungsfähiger Zugsicherungssysteme und der automatisierten Betriebsführung in einem ganzheitlichen Systemansatz. Vom Einsatz automatisierter Zugbeeinflussungssysteme erhoffen sich die Betreiber von Stadtschnellbahren mehrere positive Effekte. Diese werden nachfolgend dargestellt.

# Steigerung der Streckenleistungsfähigkeit

Automatisierte Zugbeeinflussungssysteme erhöht eine Steigerung der Leistungsfähigkeit ihrer Strecken und sind damit die Grundlage für die Erhöhung der Beförderungskapazität. Durch die kontinuierliche Überwachung der zulässigen Fahrweise der Züge konnen aktuell bei konventionellen Signalsystemen bestehende Durchrutschwege verkurzt werden, weil das automatisierte Zugbeeinflussungssystem das Fahrzeug eine Zielbremsung auf den jeweiligen Gefahrpunkt (beispelsweise eine nicht in Endlage gesicherte Weiche oder das Ende eines vorausfahrenden Zuges) überwacht. Hierdurch entfallen bei den Zugfolgezeiten Zeitanteile und die Leistungsfähigkeit der Strecke steigt entsprechend. Konnen Fahrzeuge einander im wandernden absoluten Bremswegabstand folgen, konnen Zugfolgezeiten weiter reduziert und die Leistungsfähigkeit von Strecken weiter erhöht werden. Der Kapazitätsgewinn kann durch ein Sperrzeitenbild verdutlicht werden. Sperrzeiten sind hierbei diejenigen Zeiten, in welcher der Fahrwegabschnitt durch eine Fahrt betrieblich beansprucht ist (Pachl 2016). Die Sperrzeit eines Gleisabschnitts wird durch zwei Zeitpunkte begrenzt. Dies ist zum einen der Zeitpunkt, zu dem der Gleisabschnitt frei sein muss, damit der Fahrzeugfuhrer keine Bremsung einleitet. Dies ist zum anderen der Zeitpunkt, zu dem der Zug den Gleisabschnitt wieder für eine andere Zugfahr freigibt. Beim Fahren im festen Raumabstand (das heißt bei konventionellen Zugbeeinflussungssystemen) nimmt das Sperrzeitenbild die Form einer Sperrzeitentreppe an. Die dichteste Zugfolge wird durch die Berührung der Sperrzeitentreppe vorgegeben. Mit CBTC-Systemen wird das Fahren im absoluten Bremswegabstand (wandernder Raumabstand) möglich. Hier Goes die treppenfürmige Darstellung des Sperrzeitenbildes in ein Sperrzeitenband über (Büker et al. 2019). Da wesentliche Sperrzeitenanteile (dunkelgrau) entfallen, konnen die Züge einander nun in dichteren Zeitabständen folgen (Abb. 1.2).

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/b1f4de83f6a40f6c2f1ef29dbf682a7101726d7c4beac7c0eaf919ef9c272fec.jpg)  
Abb. 1.2 Verkürzung der Zugfolgezeiten durch den Übergang vom Fahren im festen Raumabstand zum Fahren im wandernden Raumabstand. (In Anleitung an Pachl 2016)

# Steigerung der Betriebsqualität

Automatisierte Zugbeeinflussungssysteme erhöht werden. Hier wirken sich im Sinne eines umfassenden Verständnisses der Dienstleistungsqualität (vgl. DIN EN 13816:2002) verschiedene Hebel aus:

- Die Vollautomatisierung des Betriebes erlaubt durch den Verzicht auf den Fahrer eine Ausweitung der Betriebszeitraume. In Ballungsgebieten kann nunmehr eine Verkehrsbedienung rund um die Uhr erfolgen.  
- Durch die kürzeren Zugfolgezeiten werden kürzere Fahrplantakte möglich. Dies wird sich über kürzere Wartezeiten an den Stationen positiv auf kürzere Reisezeiten für die Fahrgäste aus.  
- Aus der hohenen Kapazität (mehr Fahrten pro Stunde und Fahrtrichtung) resultiert bei gleichbleibender Nachfrage ein besseres Platzangebot in den Fahrzeugen. Bestenfalls wird die Sitzplatzverfügbarkeit erhöht. In den Stößenkarten kann zumindest die pro Fahrgast verfügbarbare Stehfläche erhöht werden.  
- Die Automatisierung fordert die Punktlichkeit und Stabilität der Betriebsabwicklung durch die folgenden Aspekte:

- Elimination interner Störfaktoren wie Fahrzeitschwankungen: Die Automatisierung der Zugfahr t führt zu vorhersagbaren Fahrzeiten zwischen den betrieblichen Halten, da die Variationen der Geschwindigkeit durch den menschlichen Fahrer beseitigt werden.  
- Elimination externer Störfaktoren: EinHigher automatisierter Betrieb mit dem automatischen Öffnen und Schlieben der Turen in den Stationsbereichen reduziert die oftmals durch verlangerte Haltestellenaufenthalszeiten hervorgerufen Versprütungen im Linienverlauf. Oftmals verlangern sich die Haltestellenaufenthalszeiten, da noch in letzter Sekunde Fahrgäste in das Fahrzeug treten und den automatischen Türschliebsvorgang verzöbern. Außer dem kann in großen Netzen eine große Schwankung der zu- und aussteigenden Fahrgäste beobachtet werden. Dies ist beispielsweise typisch für Stationen mit einer intermodalen Vernetzung mit Fernbahnsystemen, wenn beispielsweise kurz zuvor ein voll besetzter Fernbahnzug angekommen ist.

- Schaffung von Kapazitätsreserven: In der Regel wird die theoretisch mögliche Leistungsfähigkeit (und damit die Kapazität) automatisierter Zugsicherungssysteme im Vergleich zu konventionellen Signalsystemen (so genannter design headway im Sinne einer technisch möglichen kürzesten Zugfolgezeit) im täglichen Betrieb nicht voll ausgeschöft (operational headway im Sinne der in der Fahrplanung berücksichtigten Zugfolgezeit). Daraus resultiert eine nicht ausgeschöpfte Streckenleistungsfähigkeit. Diese Reserve sorgt davon, dass bestehende Störungen im Betrieb wieder abgebaut werden können. Darüber hinaus können durch die Reduktion intern und externer Störfaktoren (vgl. die beiden Punkte zuvor) möglicherweise im Fahrplan berücksichtigte Regelzuschläge auf die Fahrzeiten (Pachl 2016) entfallen.

# Flexibilisierung des Ressourceneinsatzes

Automatisierte Zugbeeinflussungssysteme erhöhungene Flexibilisierung des Ressourceneinsatzes. In der hochsten Ausbaustufe des unbegleiteten fahrerlosen Betriebs (unmanned train operation, UTO) gelingt eine vollständige Entkoppelung des Fahrzeugeinsatzes von der Personalumlaufplanung (Schnieder 2018). Dispositionsentscheidungen können unverzüglich umgesetzt werden und die Fahrzeugeinheiten der aktuellen Verkehrsnachfrage folgend kurzfristig und flexibel ein- und ausgesetzt werden. Somit folgt die tatsächlich im Betrieb eingesetzte Kapazität (ausgedrückt als Produkt aus dem Fahrzeugeinsatz pro Stunde und der möglichen Fahrgastkapazität der im Betrieb eingesetzten Fahrzeugeinheiten) optimal der tatsächlichen Verkehrsnachfrage. Dies ist beisemple in Abb. 1.3 dargestellt. Es wird stets ausreichend Kapazität vorgehalten. Außerdem werden bei abnehmender Nachfrage unnottige Leerfahren den Fahrzeuge vermieden (Rumsey 2010). Des Weiteren gestaltet sich bei fahrerlosen Systemen die Störungsbehandlung einfacher, da weniger Restriktionen berücksichtigt werden müssen.

# Erhöhung der Sicherheit der Betriebsabwicklung

Automatisierte Zugbeeinflussungssysteme können die Sicherheit der Betriebsabwicklung erhöhen. Die Automatisierung von Schienenverkehrssystemen führt zu einem Sicherheitsgewinn. Da der Menschen aus der Sicherheitsverantwortung im Regelbetrieb herausgenommen wird, können menschliche Fehler ausgeschlossen werden.

# Höhere Wirtschaftlichkeit der Betriebsabwicklung

Automatisierte Zugbeeinflussungssysteme erhöhen die Wirtschaftlichkeit der Betriebsabwicklung. Maßgeblich hierfür sind die Lebenszykluskosten (Life Cycle Costs, LCC). Grundsätzlich müssen bei der Beschaffung von Zugsicherungssystemen die Beschaffungs-

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/4d2c0c1dedfe0a6781835f020c696a6526631e99260152d0032f94da5702d860.jpg)  
Abb.1.3 Flexibilisierung des Ressourceneinsatzes durch automatische Bahnsysteme. (VDV 2010)

kosten (Capital Expenditure, CAPEX) und die Betriebskosten (Operational Expenditure, OPEX) sorgfältig gegeneinander abgewogen werden. So können über die lange Betriebszeit der signaltechnischen Infrastruktur geringere Betriebskosten gegebenenfalls urprünglich höhere Investitionskosten aufwieden.

- Grundsätzliche Vorteile automatisierter Zugbeeinflussungssysteme liegen in einer deutlich geringen Zahl an Außenanlageelementen (beispielsweise durch den Verzicht auf ortsfeste Signale und eine deutliche Reduktion der Anzahl der streckenseitig erforderlichen Gleisfreimeldesysteme). Dies vereinfacht die Durchführung von Instandhaltungsaktivitäten in den kurzen nachtlichen Sperrpausen.  
- Automatisierte Zugbeeinflussungssysteme möglichchen eine energiesparende Fahrweise.  
- Bei vollständiger Automatisierung des Betriebs entfallen Personalkosten für die Fahrer auf den Fahrzeugen. Diese Effekt wird durch möglicherweise zusätzliches Personal in den Stationen für die Fahrgastbetreuung gegebenenfalls wieder teilweise kompensiert.  
- Die Automatisierung von Kehrfahren an Endhaltestellen reduziert den hierfür er-forderlichen Zeitbedarf und kann die Zahl der betrieblich erforderlichen Fahrzeuge re-duzieren (Rumsey 2010). Dies hat einen Einfluss sowohl auf die Kapitalkosten als auch auf die Betriebskosten der Fahrzeugflotte.  
- Durch eine gegebenenfalls höhere Kapazität und eine durch gestiegene Attractivität höhere Nachfrage können möglicherweise zusätzliche Fahrgelderlöse erwirtschaftet werden.

# Literatur

Adler G et al (Hrsg) (1981) Lexikon der Eisenbahn, 6. Aufl. VEB Verlag für Verkehrswesen, Berlin  
Büker T, Grafagnino T, Hennig E, Kuckelberg A (2019) Enhancement of blocking-time theory to represent future interlocking architectures. In: RailNorrköping 2019 - 8th International Conference on Railway Operations Modelling and Analysis (ICROMA), Norrköping, S 219-240  
DIN EN 13816:2002 Transport - Logistik und Dienstleistungen - Öffentlicher Personenverkehr; Definition, Festlegung von Leistungszielen und Messung der Servicequalität; Deutsche Fassung EN 13816:2002  
Leveque O (2020) Nachfragebasierte Verkehrslenkung in CBTC für ein besseres Fahrgasterlebnis. Signal + Draht 112(4):13-20  
Pachl J (2016) Systemtechnik des Schienenverkehrs - Bahnbetrieb planen, steuern und sichern. Springer Vieweg, Wiesbaden  
Pancini Fitzek T, Fabian J, Hartmut H (2021) Fahrgäste, Stationen & Züge im Mittelpunkt – bedarfsgerechter Betrieb während COVID-19 und darüber hinaus. Signal + Draht 113(1+2):6–11  
Rumsey A (2010) Semi-automatic, driverless and unattended operation of trains. Signal + Draht 102(3):43-46  
Schnieder L (2018) Betriebsplanung im öffentlichen Personennahverkehr - Ziele, Methoden, Konzept. Springer, Berlin  
United Nations, Department of Economic and Social Affairs, Population Division (2015) World urbanization prospects: the 2014 revision, (ST/ESA/SER.A/366)  
VDV (2010) 2010: Nachhaltiger Nahverkehr, Bd 1. VDV, Köln  
Zoeller H-J (2002) Handbuch der ESTW-Funktionen. Die Sicherungsebene im elektronischen Stellwerk. Tetzlaff, Hamburg

# Systemkomponenten und Umsysteme automatischer Zugbeeinflussungssysteme

2

# SN Flashcards

Als Käfer*in diesen Buches können Sie kostenlos unsere Flashcard-App „SN Flashcards" mit Fragen zur Wissenschaftung und zum Lernen von Buch-inhalten nutzen.

1. Gehen Sieitte auf https://flashcards.springernature.com/login und  
2. erstellen Sie ein Benutzerkonto, indem Sie ihre Mailadresse angegeben und ein Password vergehen.  
3. Verwenden Sie den folgenden Link, um Zugang zu Ihr dem SN Flashcards Set zu erhalten:  $\triangleright$  https://sn.pub/sK5mLQ

Sollte der Link fehlen oder nicht Funktionieren, senden Sie unsitte eine E-Mail mit dem Betreff „SN Flashcards“ und dem Buchtitel an customerservice@springernature.com

Automatische Zugbeeinflussungssysteme (Automatic Train Control, ATC) werden bei den Verkehrsrunternehmen bei Neuanlagen von Beginn an in eine zeitgleich aufgebaute Systemlandschaft integriert. Bei bestehenden Anlagen müssen automatische Zugbeeinflussungssysteme in die Landschaft bereits bestehender Steuerungssysteme integriert werden. Dieses Kapitel zeigt auf, wie automatische Zugbeeinflussungssysteme mit ihren Umsystemen in Beziehung stehen. In this dem Kapitel werden zunachst die Systemkomponenten automatischer Zugbeeinflussungssysteme erläutert (vgl. Abschn. 2.1). Anschliebend werden die Schnittstellen zu den Umsystemen beschreiben (vgl. Abschn. 2.2). Es wird dargestellt, welche Informationen sie von diesen empfangen und welche Informationen sie an

diese ausgegeben. Diese technischen Abhängigkeiten müssen bei der Erstellung von Lastenheften für automatische Zugbeeinflussungssysteme mit berücksichtigt werden.

# 2.1 Systemkomponenten automatischer Zugbeeinflussungssysteme

Automatische Zugbeeinflussungssysteme bestehen aus Fahrzeug- und streckenseitigen Komponenten. Die grundlegende Architektur ist in Abb. 2.1 dargestellt. Zum betteren Verständnis der folgenden Ausführungen werden vier zentrale Grundbegriffe für wesentliche Funktionsböcke den Ausführungen dieser Abschnitts vorangestellt:

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/b7501a4898388d8adcc5ecb2b3832de6d1971dd137761ef78c6eb404e61cc8c3.jpg)  
Abb.2.1 CBTC Systemüberblick in Anleitung an (Brückner 2017)

- Automatic Train Control: Dieser Begriff bezeichnet das technische System, welches einer automatisierten Betriebsführung dien, also sowohl eine sichere Fahrweise der Fahrzeuge erzwingt, als auch den Betrieb steuert. Ein ATC umfasst zwingend Automatic Train Protection (ATP) und kann in Abhängigkeit der Automatisierungsgrade zusätzliche Funktionsbausteine wie Automatic Train Operation und/oder Automatic Train Supervision (ATS) umfassen (IEEE 1474.1-1999). In Abb. 2.1 wird dieser umfassende Begriff durch die äußere Box im Schaubild dargestellt.  
- Automatic Train Protection (ATP): Teilsystem des ATC-Gesamtsystems, welche den signaltechnisch sicheren Schutz vor Kollisionen, Entgleisungen und anderen Gefährdungen sicherstellt. Wesentliche Funktionen sind hierbei die Sicherung der Fahrwege, die Ortung der Fahrzeuge sowie die Abstandsregelung. Anteile these Funktionskomplexes befinden sich sowohl an der Infrastruktur (ATP wayside) als auch auf dem Fahrzeug (ATP onboard). Basiert die Datenübertragung zwischen Fahrzeug und Strecke auf drahtloser Kommunikation (Funk), sprecht man in der Regel von einem Communications-Based Train Control System (CBTC).  
- Automatic Train Operation (ATO): Teilsystem des ATC-Gesamtsystems, welche üblicherweise vom Fahrer ausgeführte Tätigkeiten übernimmt (unter anderem Geschwindigkeitsregelung, Zielbremsung im Haltestellenbereich und Türsteuerung in den Stationsbereichen). Für eine optimale Betriebsabwicklung empfängt diese fahrzeugseitige Teilsystem streckenseitige Vorgaben aus dem Teilsystem ATS (IEEE 1474.1-1999).  
- Automatic Train Supervision (ATS): Teilsystem des ATC-Gesamtsystems, welche die Züge überwacht und gegebenenfalls Vorgaben an die ATO-Komponente gibt, so dass der Fahrplan eingehalten wird. Im Falle schwerwiegender Störungen im Betriebsablauf wird die optimale Dispositionsstrategie ermittelt und durch Vorgabe angepasster Führungsgrößen (bspw. veränderte Laufwege oder entfallende Stationshalte) an die Fahrzeuge im Betrieb umgesetzt (IEEE 1474.1-1999).

# 2.1.1 Streckenseitige Ausrüstung (ATP Wayside)

Hinsichtlich der Systemarchitektur konnen bei der streckseitigen Einrichtung unterscheidliche Systemvarianten unterschieden werden. Hierbei kann es sich entweder um eine Systemarchitektur handeln, bei der einem konventionellen Stellwerk ein CBTC-System überlagert ist (Overlay System). Alternativ kann es sich um eine vollintegrierte CBTC-Einrichtung handeln, bei der die Fahrwegsicherung durch das CBTC-Streckengerät übernommen wird (Schnieder 2020). Die streckseitige Ausrüstung besteht aus den folgenden Komponenten:

- Transponder zur Unterstützung der Lokalisierung des Fahrzeugs: Diese sind in der Regel nur passiv als Ortungsreferenzpunkte im Gleis montiert und übertragen lediglich eine Referenzinformation für die Synchronisierung der Weg- und Geschwindigkeits-

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/b6275cdf4e9551586efac00f1f067d295bdb9a8b2f2bda5da64f6d3dd5b05ba9.jpg)  
Ortsbake im Gleis (Thales)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/11de4f2107372ce36a6856a1f966d7286f6848f95d344b4b05d7e218bbbfa664.jpg)  
Eurobalise als Ortsbake (Alstom)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/1f6c29831a75efe6d35aa95c845cc249f31be6ced10498fb0c9de2a7203136f6.jpg)  
Eurobalise als Ortsbake (Siemens)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/08f8b7414e850d1e86dc3250b69bc2584ee295b2aba21121a240c077caa4bbca.jpg)  
Eurobalise als Ortsbake (Hitachi)  
Abb. 2.2 im Gleis montierte Ortsbaken (Quelle: eigene Abbildung (oben links und unter rechts), Alstom Transport Deutschland GmbH (rechts), Siemens Mobility GmbH (unter links))

messung des Fahrzeugs. Alternativ können die Transponder bei geringeren Automatisierungsgraden (beispelsweise im nicht automatisierten Zugbetrieb) als schaltbare Komponenten ausgeführst sein, welche veränderliche Datentelegramme an die Fahrzeuge übertragen. In thisem Fall können sie Fahrbefehle an das Fahrzeug übermitteln. Beispiele von Transpondern sind in Abb. 2.2 dargestellt.

- Einrichtungen zum Steuern und Überwachen beweglicher Fahrwegelemente: Insbesondere Weichen müssen für die Zugfahr in die korrekte Endlage gebracht werden und diese für die Zeitdauer ihrer Befahrung aufrechterhalten. Das Verlassen der Endlage muss safer erkannt und gemeldet werden.  
- Einrichtung zum Steuern und Überwachen der sekundären Gleisfreimeldung: Im Regelbetrieb ergibt sich die Gleisfreimeldung aus der Kenntnis der Zugvollständigkeit in Verbindung mit der Zugposition in der CBTC-Streckenzentrale. Dies wird auch als primäre Gleisfreimeldung bezeichnet. Im Betrieb ist es aus mehreren Gründen hereaus sinnvoll, eine reduzierte Gleisfreimeldung mit konventionellen Gleisfreimeldesystemen (beispelsweise Achszähler) vorzusehen. Dies wird auch als sekundäre Gleisfreimeldung bezeichnet. Grunde für eine sekundäre Gleisfreimeldung ist eine Leichtgängigkeit des Betriebs im Falle von Störungen, eine einfachere Abwicklung des Betriebs mit nicht mit CBTC ausgerüsteten Fahrzeugen (bspw. Baufahrzeuge, die nur mit vergleichsweise hohem Aufwand ausgerüst werden wurden) oder die Überwachung von der Übergänge zu benachbarten nicht ausgerüsteten Streckenbereichen (Aufnahme

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/71376e688825a5d47e22c71806d65d3f0dc5f63fb94ea4d105222f51ea6473be.jpg)  
Abb. 2.3 Sensoren eines Achszählsystems für die sekundäre Gleisfreimeldung. (Quelle: Frauscher Sensortechnik GmbH)

von Fahrzeugen in den CBTC-geführten Betrieb). Abb. 2.3 zeigt ein Montagebeispel von Achszahlsensoren im Gleis.

- Einrichtung zum Steuern und überwachen (reduzierter) ortsfester Signale: Je nach gewähler betrieblicher Rückfallebene kommt Signale zum Einsatz, über die Fahrten nicht mit CBTC-Fahrzeuggeräten ausgerüsteten Fahrzeugen zugelassen werden konnen. Für Fahrten mit CBTC-Fahrzeuggeräten ausgerüsteten Zügen sind ortsfeste Signale nicht mehr erforderlich, weil hier eine Führerstandssignalisierung konsequent umgesetzt wurde. Einige Betreiber fordern gegebenenfalls eine reduzierte ortsfeste Signalisierung, da in der Übergangsphase ein Mischbetrieb mit nicht ausgerüsteten Altfahrzeugen erforderlich ist, oder Vorkehrungen für einen Betrieb auf der Rückfallebene im Falle bspw. eines gestörten Funksystems getroffen werden sollen.  
- Einrichtungen zum Einlesen und zur Ausgabe diskreter digitaler Signale: Es mussen verschiedene Zustandsgroßen externer Systeme mit in Sicherungstechnische Abhängigkeiten eingebunden werden. Ein Beispiel hierfür ist das sichere Rücklesen des Zustands eines beweglichen Wehrtores für den Hochwasserschutz oder eines beweglichen Brandschutztores für die bauliche Abgrenzung von Brandabschnitten in Tunneln. Basierend auf der erkannten Endlage des Wehr- oder Brandschutztores werden Zugfahrten entweder zugelassen (Wehr- oder Brandschutztor offen) oder verhindert (Wehr- oder Brandschutztor geschlossen, bzw. Zustand unbekannt).  
- CBTC-Streckenzentrale: Die CBTC-Streckenzentrale stellt elementare sicherstechnische Abhängigkeiten her wie beispelssweise Flankenschutz zwischen benachbarten Weichen. Je nach Systemkonfiguration wird dies gegebenenfalls auch noch durch ein reduziertes Stellwerk technisch realisiert. Des Weiteren überwacht die CBTC-Streckenzentrale die Zugbewegungen in ihrem Stellbereich. Die Fahrzeuge senden regelmäßige auf einen streckenseitigen Referenzpunkt (Transponder) bezogene Positionsmeldungen an die Streckenzentrale. Hierbei dient der sowohl strecken- als

such fahrzeugseitig verwendete Streckenatlas als gemeinsames Koordinatensystem. Der Streckenatlas ist ein umfassendes Knoten-Kanten-Modell, welches statische und dynamische Attribute umfasst. Die statischen Attribute ändern sich im Betrieb nicht. Beispiele statischer Attribute des Streckenatlasses sind die Positionen der Transponder im Gleis, Neigungen und Gefäufe in den Streckenabschnitten, streckenseitige Geschwindigkeiten, Halteplätze in Stationen und in Abstellanlagen, die Ausführung der Bahnsteige in Seiten- oder Mittenlage sowie die Lage von Flucht- und Rettungswegen (vgl. Darstellung des Streckenatlasses in Abb. 2.4). Dynamische Attribute ändern sich im Betrieb. Beispiele dynamischer Attribute des Streckenatlasses sind Weichenlagen (rechts/links/unbestimmt), Freimeldeinformationen einer möglicherweise vorhandenen sekundären Gleisfreimeldung, gegebenenfalls von der Leitstelle eingegebene vorübergehende Langsamfahrstellen oder Befahrbarkeitssperren von Fahrwegelementen sowie bei Bedarf weitere Eingangsgrößen von Umsystemen. Da auch in der Fahrzeuginrichtung ein correspondierender Streckenatlas vorliegt führt dies zu einer vereinfachten Kommunikation zwischen ATP-Fahrzeug- und -Streckeneinrichtung. Basierend auf den Zugpositionen, Gefahrenpunkten und Restriktionen des Zugleitsystems berechnet die Streckeneinrichtung für Züge in ihrem Stellbereich zyklisch neu die jeweilige Fahrerlaubnis und überträgt diese per Funk auf die Fahrzeuge. Zudem wird die Übergabe und Übernahme von Zügen zu benachbarten Streckeneinrichtungen geregelt. Ebenso werden Einfahren in den, bzw. Ausfahren aus dem Überwachungsbereich des CBTC-Systems technisch gesichert. Ebenfalls obliegt der Streckeneinrichtung die Behandlung von Zügen mit technischen Störungen wie beispiesweise einem Kommunikationsverlust oder die Einfahr von nicht ausgerüsteten Zügen (beispiesweise Wartungsfahrzeuge) in den durch CBTC überwachten Bereich.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/cbf8b885c7bf004c82cfb09cc73583941c40fd1f57c91483232c842e165ffbec.jpg)  
Abb. 2.4 Streckenatlas als gemeinsames Koordinatensystem für Strecken- und Fahrzeugeinrichtungen

# 2.1.2 Fahrzeugseitige Ausrüstung (ATP onboard und ATO onboard)

Die Fahrzeugeinrichtung umfasst die folgenden Komponenten, welche aus Gründen der Verfügbarkeit in der Regel zweimal auf dem Fahrzeug vorgesehen sind:

- Der Fahrzeugrechner für die Automatic Train Protection (ATP) ist das zentrale Element der Fahrzeugausrüstung (vgl. Abb. 2.4). Als signaltechnisch sicheres System ist jeder der Fahrzeugrechner mindestens zweikanalig ausgeführrt. Ein zentrales Element des ATP-Fahrzeuggeräts ist ein mit der Streckeneinrichtung korrespondierender Strecken-atlas. Dieses Duplizieren des Streckenatlasses zu einer vereinfachten Kommunikation zwischen ATP-Fahrzeug- und -Streckeneinrichtung. Da alle Entfernungen eindeutig auf Ortsreferenzpunkte (Transponder) bezogen sind, kann sich die Kommunikation zwischen Fahrzeug und Strecke auf die Übertragung von Koordinaten (Ende der Fahr-erlaubnis oder Positionsmeldung des Fahrzeugs) beschränken. Im Gegensatz zu anderen Zugbeeinflussungssystemen wie dem European Train Control System (ETCS) muss über das Ende der Fahrterlaubnis hinaus kein vollständiges statisches Geschwindigkeits- und Gradientenprofil von der Strecke zum Fahrzeug übertragen werden (Schnieder 2020). Auf Grundlage der im Streckenatlas auf dem Fahrzeug vorhandenen Informationen erfolgt durch das Fahrzeuggerät die Überwachung der zulässigen Geschwindigkeit sowie die Überwachung der von der Streckeneinrichtung ermittelten Fahrterlaubnis (Automatic Train Protection, ATP).  
- Der Fahrzeugrechner für die Automatic Train Operation (ATO) ist die Fahrzeugkomponente, welche der Automatisierung der Betriebsabwicklung dient. Einfache Automatisierungsaufgaben umfassen die automatische Fahr- und Bremssteuerung zur Umsetzung einer von der Leittechnik (Automatic Train Supervision, ATS) vorgegebenen optimalen Fahrstrategy. Darüber hinaus bietet dieser Fahrzeugrechner die Möglichkeit, den Zug in verschiedenen Automatisierungsgraden bis hin zum vollautomatischen fahrerlosen Zugbetrieb zu betreiben.  
- Zugsteuerungs- und Managementsystem (Train Control and Management System, TCMS): Sowohl das ATP-Fahrzeuggerät als auch das ATO-Fahrzeuggerät müssen mit anderen Teilsystemen des Zuges Daten austauschen. Dies betriff insbesondere die die Brems- und Antriebskomponenten sowie die Türsteuierung. In modernen Fahrzeugarchitecturen sind die verschiedenen Fahrzeugteilsysteme über ein Zugkommunikationsnetz (Train Communication Network, TCN) miteinander vernetzt, welches sich durch eine hohe Zuverlösigkeit und kurze Reaktionszeiten auszeichnet. Hierbei können zur Anbindung verschiedener Teilsysteme entsprechliche auf den Fahrzeugen vorhandene Schnittstellentechnologien wie Wired Train Bus (WTB), Multifunction Vehicle Bus (MVB), Controller Area Network (CAN), serielle Verbindungen und Ethernet unterstützt werden.  
- Führerstandssignalisierung (Human Machine Interface, HMI): Hierüber erhalten der Fahrer – sofern im betreffenden Automatisierungsgrad noch vorhanden – die Möglichkeit zur Bedienung und Anzeige. Der Fahrer erhalten durch die Führerstandssignalisierung alle für die Betriebsabwicklung relevanten Informationen wie beispiesweise die maximal zulässige Geschwindigkeit, die aktuelle Geschwindigkeit des Fahrzeugs, den

Schliebfzustand der Türen, die räumliche Ausdehnung der vorliegenden Fahrerlaubnis sowie möglicherweise vorliegende Störungsmeldungen des Zugbeeinflussungssystems. Zusätzlich können auch Fahrplaninformationen auf dem Display dargestellt werden, um den Fahrer über den weiteren Fahrtverlauf zu informieren (Harborth 2019). Hierfür sendet die Leittechnik bei jeder Änderung (Zugnummernwechsel, Änderung der Stationen, Änderung von Abfahrtszeiten) den individuellen Fahrplan an den Zug. Zusätzlich können für die Stationsgleise zusätzliche Attribute angezeigt werden (Endstation der Fahrt, letzte Passagierstation der Fahrt, Station mit geplantem Kuppeln von Zügen, Station mit geplantem Trennen gekuppelter Züge, auszulassende Station wegen Haltentfall aus dispositiven Gründen). Die Anzeigefunktion kann durch zusätzliche akustische Alarme für den Fahrer unterstützt werden. Im Falle eines fahrerlosen Zugbetriebs (Automatisierungsgrade 3 oder 4) wird für die Bedienung des Fahrzeugs im Störungsfall in der Regel ein vereinfachter Notführung stand vorgesehen.

- Bedienelemente (Schalter, Taster und Leuchtmelder): Weitere im Führerstand vorhandene Bedienelemente umfassen Taster für die Quittierung von Alarmen und Sicherheitsrelevanten Bedienhandlungen des Fahrs, sofern für den betreffenden Automatisierungsgrad relevant. Ein Beispiel für eine betriebliche Situation, welche die Quittierung des Fahrs benötigt, ist der Übergang in eine Betriebsart mit geringerem Umfang an Überwachungsfunktionen. Bei halbautomatischen Systemen ist außer dem ein Taster zur Beendigung der Abfertigung des Fahrzeugs im Stationsbereich vorgesehen. Nach dessen Aktivierung beschleunigt das Fahrzeug automatisch aus dem Stationsbereich. Für den Störungsfall ist auf dem Fahrzeug ein Störschalter vorzusehen, mittels dessen das Fahrzeuggerät überbrück werden kann. Auf diese Weise werden die Sicherheitsfunktionen des Fahrzeuggeräts bewusst umgangen, sodass ein gestörtes Fahrzeug unter der vollständigen Sicherheitsverantwortung des Betriebspersonals den Streckenbereich verlassen kann.

# 2.1.3 DatenCOMMunikationsystem

Das DatenCOMMunikationssystem hat die Aufgabe, eine verlüssliche, bidirektionale Kommunikation zwischen allen Fahrzeug- und streckseitigen CBTC-Subsystemen bereitzustellen. Dies ist insofern eine Herausforderung, als dass die Kommunikation in CBTC-Systemen über offene Netze erfolgt, bei denen nicht zugelassene Zugriffe nicht ausgeschlossen werden konnen, keine Höchstzahl anschließlich Teilnehmer existiert und auch das Übertragungsmedium nicht betracht oder verbindlich festgelegt ist. Diese Unabhängigkeit vom Übertragungs-medium kommt insbesondere auch die Verwendung des Internet Protocols (IP) zum Ausdruck, was über den Lebenszyklus der signaltechnischen Einrichtungen grundsätzlich die Ablösung von Funkstandards ermöglich. Da über die Funkverbindung jedoch Sicherheitsrelevante Daten übertragen werden, muss die Kommunikation über diese offene Netze mit geeigneten Kommunikationsprotokollen abgesichert werden. Die eingesetzten Kommunikationsprotokolle müssen durch geeignete Sicherheitsmechanismen einen wirksamen Schutz unter anderen gegen Wiederholung, Auslassung, Einfugung, Resequenzierung, Verfalschung, Verzögerung und Manipulation bieten (vgl. DIN EN 50159:2011).

Die Auswahl des für den jeweiligen Anwendungsfall geeigneten Kommunikations-systems sollen die folgenden Kriterien berücksichtigten:

Realisierung einer lückenlosen bidirektonalen Funkabdeckung: Hierfür muss die Reichweite der Access Points bedacht werden, um eine kontinuierliche Verbindung von Fahrzeugen in Tunneln, in Einschnitten, auf Viadukten und auf ebeneriger Strecke zu ermöglich. Außen dem muss berücksichtigt werden, dass man es im Schienenverkehr mit beweglichen Objekten zu tun hat. Es muss also auch bei higheren Geschwindigkeiten ein nahezu verlust- und verzögerungsfreier Handover zwischen den Access Points realisiert werden (Schienbein 2018).  
- Verfügbarkeit: Für eine ausreichende Verfügbarkeit werden die Access Points in der Regel an redundante Glasfasernetze angeschlossen und über unterscheidliche Stromkreise mit der erforderlichen Betriebsspannung versorgt.  
- Ausreichende Bandbreiten: Es mussen ausreichende Bandbreiten vorgehalten werden, um mindestens die Sicherheitsrelevanten Steuerungsinformationen zwischen Strecke und Fahrzeug zu übertragen. Darüber hinaus ergeben sich möglicherweise weitere Bandbreitenbedarfe durch andere Dienste. Beispiele hierfür sind Führungsgrößen für die automatische Fahr- und Bremssteuerung (Automatic Train Operation, ATO) oder die Fahrgastinformationen auf dem Fahrzeug.  
- Garantierte Dienstguten (Quality of Service, QoS): Insbesondere bei Mobilfunknetzen wird die verfügbare Bandbreite je nach Anzahl der Teilnehmer, die sich in einer Mobilfunkzelle befinden, aufgeteilt. Dies macht es zum aktuellen Zeitpunkt unmöglich, bestimmte Dienstguten von entsprechenden Services zu garantieren (Schienbein 2018). Wichtig ist auch die Latenzzeit, da sicherheitsgerichtete Reaktionen der Streckeneinrichtung (beispielsweise Einkürzung einer Fahrerlaubnis) kurzfristig auf dem Fahrzeug vorhanden sein,Müssen.  
- Kosten (total cost of ownership): Es,müssen die Investitionskosten in eine eigene Infrastruktur (Capital Expenses, CAPEX) und laufende Kosten von Mobilfunkbeitragen (Operational Expenditures,OPEX)gegeninander abgewogen werden.  
- Zuteilung von Frenquenzen: Im Einzellt fall ist für den Einsatz funkbasierter Lösungen die (rechtliche) Verfügbarkeit der Funkfrequenzen mit der jeweils zuständigen nationalen Regulierungsbehörde abzustimmen. Gegebenenfalls erfordert dies eine Antrag auf Einzelzuteilung der Frequenz bei der betreffenden Regulierungsbehörde.  
- Zukunftssicherheit: Die Zukunftssicherheit muss beim Datencommunikationssystem berücksichtigt werden. Aufgrund der kurzlebigen Technologiezyklen der Nachrichtentechnik ist davon auszugehen, dass ein CBTC-System im Verlauf seines Lebenszyklus mit mehreren physikalischen Übertragungsmedien verwendet wird. Daher ist bereits früherzeitig in der Architektur eine spätere Migrationsfähigkeit mit zu bedenken. Dies wird in der Praxis beispiselsweise durch die Verwendung des Internetprotokolls, welches grundsätzlich technologieneutral gehalten ist. Dies gestattet einen späteren Wechsel des Kommunikationskanals. Außen dem werden die Sicherheitsrelevanten Aspekte der Kommunikation von der bloßen Datenübertragung getrennt. Die Gefährungsbeherrschung für Gefährdungen wie beispiselsweise Vertauschung und Verzögerungen erfolgt in siche

ren Rechnern auf den Fahrzeugen (CBTC Fahrzeuggerät), bzw. entlang der Strecke (CBTC Streckengerät). Der dazwischenliegende Kommunikationspfad wird als „grauer Kanal" angesehen. Über diesen kann. Über diesen kann – wegen der Anwendung der Sicherheitsmechanismen nach DIN EN 50159 – auch ohne eigenen Kenntnis der konkreten Ausprüfung des Datenübertragungskanal eine sichere Kommunikation erfolgen.

Für die Datenkommunikation sind grundsätzlich verschiedene Technologien geeignet. Kam früher konventionelle Linienleitertechnik (englisch: leaky feader) zum Einsatz, haben sich mittlerweile drahtlose Kommunikationssysteme allgemein durchgesetzt. Diese haben den Vorteil, dass sie eine größere Bandbreite haben und einfacher am Gleis verlegt und gewartet werden können. Technologisch können die Datenkommunikationssysteme auf verschienen Funkstandards basieren. Nachfolgend werden die entsprechenden technischen Möglichkeit beschreiben.

# Terrestrial Trunked Radio (TETRA)

Dieser Funkstandard verträgt bei Nahverkehrsbetreibern analoge Sprechfunknetze und bietet auch die Möglichkeit zur Datenübertragung. TETRA bietet die Möglichkeit von zentral vermittelten Verbindungen (Trunked Mode Operation, TMO), bei der zwei Endgeräte über eine oder mehrere Basisstationen kommunizieren, wobei die Verwaltung aller Verbindungen in einem Mobile Switching Center (MSC) erfolgt (Geistler und Schwab 2013).

# Mobilfunksysteme vierter Generation (LTE, Longterm Evolution) und fünfter Generation (5G)

Mobilfunk Kommunikationsnetze der füsten Generation (5G)ieten neben hohen Übertragungsratsen von bis zu 10.000 Mbit/s auch die Möglichkeit zu dedizierten Echtzeit-Anwendungen. Insbesondere im Vergleich zu WLAN-basierten Systemen wird kaum noch Aufwand für die Kabelverlegung besteht und eine nahezu vollständige Reduzierung der Glasfasernetze erreicht. Die gesamte entsprechende IT-Infrastruktur wird verschwinden. Es ist anzunehmen, dass der benöttigte Netzausbau in den nachsten Jahren in den Industriel-ländern erreicht werden wird und CBTC-Systeme mit dieser Technologie betrieben werden konnen (Eichner und Uhrig 2021). Hierbei gibt es grundsätzlich zwei Märglichkeiten:

- Funkbetrieb mit einer Network Slice: Mit dem 5G-Mobilfunkstandard gibt es nicht mehr „das Netz“ – sondern parallel betriebene, virtuelle Netze auf Basis einer gemeinsamen, physischen Infrastruktur. Jede einzeln „Scheibe“这意味着 Netzes ist ein isoliertes Ende-zu-Ende-Netzwerk, das maßgeschneidert auf die spezifischen Erfordernisse der einzelnen Anwendungen oder Kunden ist. Dabei behindert sich der Datenverkehr der einzelnen Slices nicht gegenseitig, da die Slices voneinander getrennt sind. Egal ob eine Anwendung besondere Ansprüche an eine hohe Bandbreite hat, weitere reaktionsschnell sein muss oder bestimmte Sicherheitskritische Anforderungen erfüllen muss. Die separates Scheiben des Netzwerks werden jedem einzelnen Anwendungsfall gerecht. Network Slicing ist softwaregesteuert, sodass die einzelnen Netzwerkscheiben einfach verwaltet werden konnen und flexibel anpassbar sind – zum Beispiel bei unvor

hergesehen. Ereignissen. So wird es möglich, dass jeder einzeln virtuellen Teilnetzwerk (Slice) bestimmte Funktionen zugeordnet werden können, damit es den individuellen Bedürfnissen der jeweiligen Anwendung entspricht.

- Betrieb eines Campus-Netzes: Ein Campus-Netz ist ein exklusives Mobilfunknetz für einen definierten räumlichen Bereich (bspw. einen Betriebshof), der auf die individuellen Bedürfnisse des Verkehrsrunternehmens zugeschnitten ist. In Deutschland stellt die Bundesnetzagentur davon den lizenzierten Frequenzbereich von 3,7 bis 3,8 GHz zur Vergebung. Das Campus-Netz wird hierbei als privates Netz betrieben, das heißt es funktioniert vollkommen getrennt vom öffentlichen Mobilfunknetz: Alle Komponenten der Infrastruktur von den Antennen über das Kernnetz hin zum Netzwerkserver befinden sich lokal auf dem Gliende des Verkehrsrunternehmens. Diese eigenständige private 5G-Architektur ermöglich eine besonderes einfache, sichere und schnelle Datenverarbeitung und eignet sich daher zur Unterstützung besondere anspruchsvoller und sicherheitskritischer Anwendungen.

# Wireless Local Area Networks (WLAN)

Drahtlose lokale Netzwerke (Wireless Local Area Networks, WLAN) haben sich in CBTC-Systemen weltgehend durchgesetzt. Abb. 2.5 zeigt exemplarisch die fahrzeug- und streckenseitigen Sende- und Empfangsantennen. Bei W-LAN handelt sich um ein Netz mit verhältnisbig Kurzer Reichweite. Daher konnen weiträumige Kommunikationsnetze nur durch den Aufbau mehrerer Access Points (Netzwerk-Zugangspunkte) aufgebaut werden. Dies bedeutet, dass sich die Reichweiten benachbarter Access Points überlagern. Auf diese Weise findet der Zug stets während seiner Fahrt entlang der Strecke einen neuen Access Point, mit dem er eine Verbindung aufbauen kann. Ein kritischer Punkt beim Roaming in CBTC-Systemen ist, einen bruchlosen Übergang der Kommunikationsverbindung beim Wechsel von einem Access Point zu einem anderen Access Point zu gewährleisten. Hierbei darf es nicht zu Abbrüchen in der Kommunikation oder zu Verzögerungen kommt. Eine

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/5953e3f6d79a641b9df4754cbed682fb0cb077936524aaa6e0fe07d7c05cce1f.jpg)  
Abb. 2.5 Fahrzeug- und streckenseitige Sende- und Empfangsantennen für W-LAN. (Quelle: Huber + Suhner AG)

mit Latenzzeiten behaftete Kommunikation zwischen Fahrzeug- und Streckeneinrichtung kann zu einem verspäteten Empfang eines Fahrbefehls führen, sodass der Zug eine unbeabsichtigte Zwangsbremse auslõst. Darüber hinaus werden in CBTC-Systemen oftmals benachbarte mit entsprechenden Frenzen betrieben, sodass ein Übergang von einem Access Point zum nachsten mit einem Frenzwechsel verbunden ist. Die wechselnden Frenzen in Kombination mit einer dichten Folge an vom Fahrzeug passierten Access Points (Die Häufigkeit von Übergängen ergibt sich aus dem Abstand der Access Points und der Geschwindigkeit des Zuges) führt dazu, dass die Handover-Algorithmen stationärer WLAN-Netzwerke unzureichend sind und die Hersteller von CBTC-Systemen für den Betrieb von W-LAN-Netzwerken im sogenannten Infrastrukturmodus spezielle Roaming-Algoremmen für CBTC-Systeme entwickelt haben. Im einfachsten Fall Funktioniert das Roaming in im Infrastrukturmodus betriebenen W-LAN-Netzen wie in Abb. 2.6 dargestellt (Farooq 2018):

- Schritt 1: Im Ausgangszustand sind beiden zugseitigen Empfangseinrichtungen mit einem streckenseitigen Access Point (n) verbunden. Während der Zug fahrht, sicht die Empfangseinrichtung an der Spitze des Zuges nach einem neuen Access Point  $(\mathrm{n} + 1)$ .

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/48324ec104c485e62e452038caccd8d0644355a051abf4139138c41c20d7822f.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/b01043259fde714693ea64b1d357307fac4ba00a1d2c58f6ef6cac44cb3fae8a.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/d5459b4166e9242ec37322bbe7d57d54ba36bdfd9610015dee617f25f0025e57.jpg)  
Abb.2.6 Roaming in drahtlosen Kommunikationsnetzen für CBTC-Systeme nach. (Farooq 2018)

Sobald eine neue Verbindung mit einem neuen Access Point  $(n + 1)$  hergestellt wird, bricht die Empfangseinrichtung am Anfang des Zuges die Verbindung zum vorherigen Access Point (n) ab. Die Empfangseinrichtung am Ende des Zuges besteht die Verbindung zum vorherigen Access Point (n) bei.

- Schritt 2: Im{nachsten Schritt stelt auch die Empfangseinrichtung am Ende des Zuges eine Verbindung zum Access Point  $(\mathrm{n} + 1)$  her und bricht die Verbindung zum Access Point (n) ab. Intelligente Roaming-Algorthmen verhindern, dass beide fahrzeugseitige Empfangseinrichtungen zeitgleich nach den nachsten Access Point an der Strecke suchen.  
- Schritt 3: Der erstige Schritt wird erneut durchgeführt. Die fahrzeugseitige Empfangseinrichtung am Anfang des Zuges baut eine Verbindung zum Access Point  $(n + 2)$  auf und bricht die Verbindung zum Access Point  $(n + 1)$  ab. Auf diese Weise „hangelt“ sich das Fahrzeug von Access Point zu Access Point und behält damit stets eine Funkverbindung bei.

Als Alternative zu dem zuvor dargestellen Betrieb einer W-LAN-Infrastruktur im Infrastrukturmodus konnen die W-LAN-Netze auch im ad-hoc-Modus betrieben werden. Hierbei wird eine direkte Funkverbindung zwischen mobilen und ortsfesten Einheiten spontan aufgebaut. Das zuvor dargestelle Roaming kann hierbei entfallen. Allerdings ist hierbei zu betrachten, dass durch das ad-hoc-Prinzip nunmehr vom Fahrzeug übermittelte Dateninhalte von mehreren streckseitigen Access Points empfangen werden konnen. Daher mussen die doppelt empfangenen Datenelemente dedupliziert werden. Bei der Daten-Deduplizierung werden eingehende Datenelemente untersucht und anschließend mit bereits gespeicherten Daten verglichen. Falls bestimmte Daten bereits vorhanden sind, werden diese verworfen. So wird sichergestellt, dass die eingehenden Daten nur einmal verarbeitet werden.

# 2.1.4 Zugleitsystem (Automatic train Supervision, ATS)

Die automatische Zugüberwachung übernimmt die vollständige Überwachung einer automatisierten Bahnlinie, wozu die Diagnostik der Streckeneinrichtungen, der Fahrzeuggeräte sowie des Kommunikationsnetzwerkes gehört. Disponenten haben mittels des ATS Eingriffsmöglichkeiten in den Zugbetrieb durch Anpassung beispielsweise von Haltezeiten in den Stationen, den Entfall von Stationshalten oder der Einrichtung temporärer Langsamfahrstellen. Darüber hinaus konnen über die Komponente ATS auch Zustandsgroßen externer Systeme wie SCADA (Supervisory Control and Data Acquisition) oder Fahrgastinformationssysteme angezeigt werden oder diese Systeme bedient werden. Abb. 2.7 zeigt exemplarisch die Leitstelle der Metro Sao Paulo. Oftmals wird - wie in Abb. 2.6 zu erkennen - das großräumige Betriebsgeschehen für alle Leitstellenmitarbeitende auf Projektnswänden dargestellt. Zusätzlich erhält der Bediener weitere für die sichere Abwicklung des Betriebs notwendige Informationen, wie beispisseweise

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/c3be3435dbd2a4b51eddd1e984257cbb2e5ac21cf6f0c339b62de3b5b0b49940.jpg)  
Abb.2.7 Leitstelle der Metro Sao Paulo. (Quelle: Alstom Transport Deutschland GmbH)

Bilder von Kameras zur Bahnsteigüberwachung. Dies ist in Abb. 2.7 auf der linken Seite zu erkennen. Das Zugleitsystem (ATS) zielt auf eine Verkehrsabwicklung entsprechend der Planung, eine Optimierung der Verkehrsqualität insbesondere bei Störungen sowie eine Optimierung des Bahnkundenservice ab. Leitsysteme im hochautomatisierten Nahverkehr sind grundsätzlich modular aufgebaut. Hierbei bauen die verschiedene Funktionskomplexe aufeinander auf. Die verschiedenen Funktionskomplexe werden nachfolgend beschrieben (Mücke 2005):

- Bedieren und Anzeigen (englisch: operation and display): Es werden relevante Systemzustände der Infrastruktur wie Weichenlagen und Besetztuzstände der Gleise dargestellt. Abb. 2.8 zeigt ein Beispiel der Bedien- und Anzeigeelemente des Bedienplatzsystems für Infrastruktur elemente der fahrerlosen U-Bahn in Nürnberg. Über die Menüleiste im oberen Teil des Bildes hat der Bediener die Möglichkeit zur Bereichs- und Bildanwahl. Imzentralen Bereich des Bildes ist die Detailübersicht über den ausgewählten Bedienbereich - hier die Station Ziegelstein - dargestellt. Per Mausclick konnen hier Sicherheitsrelevante Bedienhandlungen von Infrastrukturelementen (zum Beispiel das Umstellen von Weichen) durchgeführt werden. Im unteren Abschnitt des Bildes ist auf der linken Seite eine Auswahm möglicher Bediendialoge dargestellt. Auf der rechten Seite sind aktuell anliegende Sammelmeldungen für den ausgewählten Streckenbereich dargestellt. Zusätzlich konnen am Fahrdienstleiterarbeitsplatz weitere betrieblich relevante Informationen wie Versprüngsinformationen der aktiven Züge angezeigt werden (Harborth 2019).

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/e7075790e06ca4ec94063173f5700eaa94abab68c2163770b25db0464b44fb86.jpg)  
Abb. 2.8 Bedien- und Anzeigeelemente zur Steuerung von Infrastrukturelementen der fahrerlosen U-Bahn in Nürnberg. (Quelle: VAG Nürnberg; Siemens Mobility GmbH)

Des Weiteren ist es möglich, den Fahrdienstleiter durch Warnungsfunktionen auf spezielle betriebliche Zustände hinzuweisen. So gibt es beispelsweise die Möglichkeit, immer dann eine Warnung anzuzeigen, wenn für einen zug die Haltezeit an einer Station abgelaufen ist und bereits ein Fahrbefehl zur Ausfahr vtvorliegt, der Zug aber trotzem in einem konfigurierbaren Zeitraum nicht abfahrt. Für die Betriebsabwicklung in fahrerlosen Systemen ist auch die Bedienung automatisch verkehrender Fahrzeuge und ausgewählter Fahrzeugkomponenten über die grafische Bedienoberfläche der Fahrzeuglupe möglich (Brux 2007). Hierauf wird in Abschn. 5.6.1 naher eingegangen.

- Zuglaufverfolgung und Zugverwaltung (english: automatic train tracking): Die Anzeige von Zugstandorten in Übersichtsbildern gibt dem Fahrdienstleiter die Möglichkeit zur Disposition des Verkehrs. Hierzu werden Informationen über Zugbeginn, Zugnummernwechsel oder auch Kuppeln und Trennen von Zügen in der Regel dem Fahrplan entnommen. Die Funktion der Zuglaufverfolgung ist die funktionale Voraussetzung für die Zuglenkung (Heitzinger 2002).  
- Zuglenkung (englisch: automatic route setting): Die Zuglenkung automatisiert die zeitgerechte Einstellung von Fahrwegen. Hierbei schlägt die verfeinerte Prognoserechnung

auf Basis der hochfrequent übermittelten Positionsmeldungen der Fahrzeuge positiv zu Buche, da sich die Züge in Höherem Maße wie vorhergesagt verhalten. Dies ermittelcht eine verbesserte zeitgerechte Fahrstraßeinstellung. In der Zuglenkung konnen Fahrwegalternativen anhand alternativer Stationsgleise geplant werden. Das bedeutet, dass dann fur den entsprechenden Zug automatisch diese Fahrwegalternative gewählt wird, wenn der eigentliche Fahrweg gerade nicht zur Verfügung steht, weil dieser beispelsweise gerade durch einen Zug belegt ist. Also muss der Fahrdienstleiter bei solchen Belegungskonfliken nicht eingreifen, wenn der Zug durch automatische Nutzung der Fahrweg alternative in einer Station ausnahmsweise in ein andere Stationsgleis einfährt (Harborth 2019). Die Zuglenkung entlastet den Fahrdienstleiter von seinen regelmäßigen, planbaren Aufgaben. Er kann sich somit auf die Besonderheiten des Zugbetriebs konzentrierten. Fahrende Züge, CBTC-Streckeneinrichtungen, Zuglaufverfolgung und Zuglenkung bilden einen geschlossenen Regelkreis (Heitzinger 2002). Grundsätzlich konnen mit der Fahrplanbasierten Zuglenkung und der fahrztielbasierten Zuglenkung zwei unterscheidliche Zuglenkstrategien unterschieden werden. Die Fahrplanbasierte Zuglenkung erfordert die Funktion des Fahrplanmanagements.

- Fahrplanmanagement: Der Fahrplan ist unverzichtbare Grundlage für die Betriebsabwicklung und die Ressourcenplanung (Fahrzeug- und Personaleinsatz) in Verkehrsrunternehmen. Die der Betriebsabwicklung zu Grunde liegenden Fahrpläne werden in der Regel von einem bereits bestehendem Fahrplankonstruktionsystem erstellt. Der Fahrplan wird beim Systemstart und einmal tätiglich automatisch geladen. Hierbei werden Basisfahrpläne für Wochentage, Wochenenden, Feiertage oder Ferienrückreisetage angelegt (Pancini Fitzek et al. 2021). Zur Disposition von Zugfahrens sind Kenntnisse über den geplanten sowie den tatsächlichen Betriebszustand zwingend erforderlich. Der ursprünglich vorgesehene Zustand wird durch den Sollfahrplan eines Betriebstages beschreiben. Der Sollfahrplan wird auf einer theoretischen Schätzung des Fahrgastaufkommens erstellt. Der Fahrplan beinhaltet auch betriebliche Pufferzeiten für den Fahrplan und die Zugfolge, welche es ermögen, Störungen zu vermeiden und auszugleichen. Ebenfalls konnen zu Beginn eines Betriebstages tagesaktuelle Beschrankungen sowie Restriktionen (z. B. Geschwindigkeitseinschränkungen oder nicht verfügbare Infrastruktur) im Fahrplan berücksichtigt werden. Wahrend des tatsächlich durchgeführten Betriebes wird dieser Sollfahrplan durch (ungeplante) Ereignisse wie beispiselsweise eine erhöhte Fahrgastnachfrage gestört und als Prognosefahrplan fortlaufendactualisiert (Nieten et al. 2016).

- Konflikterkennung: Als Disposition wird die schnellstmögliche Wiederherstellung des Sollfahrplans bei Gewährleistung eines flüssigen Betriebs und einer Verbesserung der Gesamtpunktlichkeit verstanden. Hierzu ist es notwendig, den geplanten mit dem aktuellen Zustand abzugleichen, um sich anbahnende Konfakte früherzeitig zu erkennen. Hierzu wird der Prognosefahrplan basierend auf der Zuglaufverfolgung kontinuierlich fortgeschrieben. Basierend auf den Meldungen der Zuglaufverfolgungen wird die Bewegung eines Zuges in die Zukunft prognostiziert. Hierbei kommt in der Regel ein Zeit-Weg-Diagramm zum Einsatz, das den zeitlichen Verlauf der Zugfahren entlang

der Infrastruktur darstellt (Nieuwen et al. 2016). Bei der Verzögerung einer Zugfahr wird seine Zeit-Weg-Linie entsprechend angepasst, also zeitlich verschoben. Auf diese Weise gelingt es, zukünftig zu erwartende Konflikte zu prognostizieren. Ein solcher Konflikt ergibt sich beispelsweise, wenn zwei Zugfahrten ein Infrastrukturelement zeitgleich belegen都会 (Belegungskonflikt).

- Konfektösung: Hinsichtlich der Konfektösung bieten sich grundsätzlich mehrere – sowie räumliche als auch zeitliche – Handlungsoptionen. Eine Konfektösung kann darauf auch durch eine Kombination mehrerer Maßnahmen umgesetzt werden. Ein Beispiel einer räumlichen Anpassung von Zugfahrten ist beispelsweise die Wahl eines alternativen Laufwegs, das Brechen einer Zugfahr t oder (seltener) ihre Verlängerung. Beispiele zeitlicher Anpassung sind angepasste bzw. zusätzliche Haltezeiten oder geänderte Fahrgeschwindigkeiten und Fahrzeiten. In leistungsfähigen Nahverkehrssystemen kann durch die Leittechnik automatisch eine zeitliche Anpassung von Zugfahrten durch die Funktion der Zugabstandsdüberwachung und Beeinflussung der Zugeschwindigkeit (englisch: automatic train regulation) erfolgen. Grundlage dieser Strategie ist, dass der zeitliche Abstand von Zugfahrten eines der wesentlichen Qualitätskriterien der Verkehrsabwicklung im städtischen Nahverkehr ist. Auf Basis regelmäßiger Positionsmeldungen der Fahrzeuge können Prognosen durchgeführt und die Abstände zwischen den Zügen durch Geschwindigkeitsvorgaben automatisch geregelt werden. Die Leitstelle erhalten über das Datenkommunikationssystem aktuelle Zugstandortinformationen und Informationen über die aktuelle Geschwindigkeit von den Fahrzeugen. Die an das Fahrzeug übertragene Geschwindigkeit kann vom Fahrzeuggerät automatisch ausgeregt werden (als Führungsgröbe für das Teilsystem Automatic Train Operation).

- Fahrgastinformation: Auf Grundlage in der Leitstelle vorhandener Ist- und Sollzeiten konnen Prognosen über die weiteren Ankunfts- und Abfahrtszeiten errechnet und auf einem zentralen Server hinterlegt werden. Über standardisierte Datenformate konnen diese Informationen ausgegeben werden um auf Anzeigetafeln, Fahrtzielanzeigen oder als Echtzeit-Informationen auf mobilen Endgeräten der Fahrgäste angezeigt zu werden.

# 2.2 Umsysteme automatischer Zugbeeinflussungssysteme

CBTC-Systeme betten sich in einen Systemkontext ein. Dies ist in Abb. 2.9 dargestellt. Die einzelnen Umsysteme werden nachfolgend beschrieben.

# Fahrwegsicherung (bestehende Leit- und Sicherungstechnik)

In U-Bahn- und Stadtbahnsystemen sind in der Regel bereits leit- und sicherungstechnische Systeme in Einsatz. Diese müssen mit in die Systemgestaltung automatischer Zugbeeinflussungssysteme mit einbezogen werden. Beispielsweise kann auf ein bestehendes konventionelles Zugsicherungssystem (Fahren im festen Raumabstand) ein CBTC-System aufgesetzt werden (als Overlay). In dieser Variante werden die bestehenden Stellwerke mit

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/03b1db1c37ee16e7787f08e1237ce0bd5549ba89fa5b40e9fcf38a28c00231d0.jpg)  
Abb.2.9 Systemkontext von CBTC-Systemen. (IEC 62290-1:2014)

hierer Gleisfreimeldung und den von ihren gesteuerten Weichen und Signalen weiter genutzt. Zwischen den Stellwerken und dem automatischen Zugbeeinflussungssystem sind hierbei die folgenden Abhängigkeiten zu beachten:

- Informationen vom Stellwerk an das CBTC-System: Das vorhandene Stellwerk stellt und sichert die Fahrstraße. Es stellt dem CBTC-System darüber hinaus Informationen über Weichenlagen, Signalisierungszustände und Beleginformationen von Gleisfreimeldeabschnitten bereit. Die Streckenzentrale des CBTC-Systems ermittelt für Züge auf der Basis dieser Informationen (d. h. nach Sicherung der Fahrstraße durch das Stellwerk) die entsprechende Fahrterlaubnis und überträgt diese an die Fahrzeuge. Um die Kapazitätseffekte des Fahrens im wandernden Raumabstand zu erreichen, muss die Sicherungsglogik des vorhandenen Stellwerks allerdings tolerieren, dass sich gegeben falls mehrere Züge in einem Blockabschnitt befinden konnen (Brückner 2017).  
- Informationen vom CBTC-System an das Stellwerk: Das CBTC-System kennt die Standorte aller Fahrzeuge im Netz und fordert die erforderlichen Fahrstraße zeitgerecht an. In manchen Systemen ist eine ortsfeste Signalisierung als betriebliche Rückfallebene vorgesehen. Um in thisem Fall zu verhindern, dass ein Zugführer sich widespreadende Signalisierung an der Strecke und in der Führerstandssignalisierung besteht, kann die Kommandierung eines Signals auf einen speziellen Aspectigkeit gewünscht sein. Ein Beispiel hierfür ist die Dunkelschaltung der Signale. In anderen Situationen kann ein CBTC-System die Stellwerksinformationen ergänzen. Das CBTC-System hat beispelrscheinisse die Möglichkeit, den Stillstand des Zuges festzustehen, und kann daraufhin das Stellwerk informieren. Ist ein Zug in seinem Ziel

abschnitt zum Halten gekommen, kann die Auflösung eines zugehörigen Durchrutschwegs bzw. von dessen Elementen zeitlich verkurzt werden. Ebenso kann aufgrund der Zugposition die Freigabe von Elementen hinter dem Zug Schneller erfolgen. Hat der Zug ein Element vollständig geräumt, ist eine frühere Freigabe gegenüber einer zugewirkten Fahrstraßeuflösung basierend auf Gleisfreimeldeabschnitten möglich. Damit stehen diese Elemente früherzeitiger für die Nutzung in anderen Fahr Straßen zur Verfugung (Brückner 2017).

Gerade in Stadtbahnsystemen verkehren die Züge in wesentlichen Anteilen des Netzbereiches im öffentlichen Straßenraum. Hierfür müssen auch Schnittstellen zur Straβenverkehrstechnik (Lichtsignalanlagen und/oder Verkehrsrechner) vorgesehen werden. Durch eine gezielte Beeinflussung des Phasenablaufs der Lichtsignalanlagen in Kreuzungsbereichen wird eine möglich reibungslose Fahrt der Fahrzeuge im Zu- oder Ablauf höher automatisierter Tunnelstrecken im Zentrumsbereich möglich (Krimmling 2017).

# Fahrzeugsteuerung

Automatische Zugbeeinflussungssysteme weisen eine Schnittstelle zur Fahrzeugsteuerung auf. Es mussen für einen higher automatischen Betrieb deutlich mehr Informationen als für die eigentliche Fahr- und Bremssteuerung erforderlich vom Fahrzeuggerät ausgewertet werden, bzw. von thisem an die Fahrzeugsteuerung übergeben werden.

- Beispiele vom CBTC-Fahrzeuggerät von der Fahrzeugsteuerung eingelesener Zustandsgroßen sind Informationen über den aktuellen Zustand der verschiedene Bremssysteme des Fahrzeugs, Informationen über das Auslösen einer Hinderniserkennung (durch einen intelligenten Bahnräumer), das Auslösen der Entgleisungserkennung, das Ansprechen des Einklemmschutzes von Fahrgästen im Türbereich, sowie die Betätigung des Hebels im Fahrzeuginnern zur Notöffnung von Türen im Notfall.  
- Beispiele für vom CBTC-Fahrzeuggerät an die Fahrzeugsteuerung übergebene Kommandos sind beispelssweise die Traktionsabschaltung, die Übergabe von Bremsbefehlen für die Betriebs- und Zwangsbremse, Informationen für die Türsteuerung des Fahrzeugs sowie die Betätigung von Schiebetritten zur Verringerung der Spaltbreite zwischen Bahnsteig und Fahrzeug.

Insbesondere für fahrerlose Systeme sind darüber hinaus weitere Einrichtungen auf den Fahrzeugen erforderlich, um einen reibungslosen Betrieb auch im Falle von Störungen zu erhögenden:

- Für die Fahrgastrumbeobachtung sind in den Wagen mehrere Kameras installiert, sowie ein Fahrzeugsteuerrechner für die Funkommunikation zur Bildübertragung in die Leitstelle (Closed Circuit Television, CCTV). Verschiedene Videobildner (auch aus verschufenen Zügen) können in der Leitstelle auf Monitore aufgeschaltet werden. Nach einem Notruf oder der Betätigung der Notbremsung durch den Fahrgast kann so

die Situation im Fahrzeug von der Leitstelle aus beurteilt werden, ohne das Bedienstete zum Zug entsandt werden müssen (Brux 2007).

- Auf den Fahrzeugen finden die Fahrgäste eine Schnittstelle für den Fahrgastalarm vor. Hierbei handelt es sich um eine Anordnung mehrerer Einrichtungen in unmittelbarer Nachbarschaft zueinander bestehend aus Fahrgastalarmgriff (Notbremsgriff), Mikrofon (Sprecheinrichtung), Lautsprecher (Fahrgastrumbeschallung), optischen Anzeigern (Leuchtmeldern), Hinweisschildern und einer optionalen Verplombung zum Ausschluss unberechtigter Nutzung (DIN EN 16334-2:2020). Mit der Sprecheinrichtung konnen Fahrgäste aus dem Fahrzeug Heraus eine Sprechverbindung zu einer besetzten Betriebsstelle aufbauen. Sie konnen hierüber der Leitstelle Vorkommnissen melden. Die Sprechverbindungen laufen an dem Arbeitsplatz in der Leitstelle auf, von dem die Funktion der Fahrgastrumbeobachtung aufgeschaltet werden kann. Mit Hilfe der Funktion Fahrgastrumbeschallung kann der Bediener der Leitstelle – während er über die Fahrgastrumbeobachtung die Situation im Fahrzeug im Blick hat – die Fahrgäste im Zug gezielt ansprechen, situationsgerechte Anweisungen geben oder berühigend auf sie einwirken (Thomys 2006).

# Traktionsstromversorgung

Im Betrieb bestehen Wechselwirkungen zwischen den Zugsicherungssystemen und der Traktionsstromversorgung. Die Strecke zwischen den Stationen ist hierbei in mehrere Traktionsstrombereiche unterteilt. Das Überwachungssystem der Stromversorgung (Power SCADA) wird verwendet, um den Status des Stromnetzes zu steuern und zu visualisieren. Hier kann eine Schnittstelle zur Leittechnik vorgesehen werden, um verschiedene Sachverhalte des Regelbetriebs und des Störungsbetriebs in Bezug auf die Traktionsstromversorgung mit zu Unterstützung:

- Regelbetrieb: Im Regelbetrieb muss sichergestellt werden, dass die Züge mit dem entsprechenden Traktionsstrom versorgt werden. Darüber hinaus muss verhindert werden, dass Züge in Bereiche ohne Traktionsstromversorgung (beispielsweise durch eine instandhaltungsbedingte Abschaltung) oder mit einer für sie ungeeigneten Traktionsstromversorgung einfahren konnen. Ist beispiselsweise die Traktionsstromversorgung in einem Streckenbereich ausgeschaltet, * $\text{dürfen die Züge die letzte Station vor dem unterbrochenen Speiseabschnitt nicht verlassen.}$  Algorithmmen in der Leittechnik * $\text{konnen}$  einen energieoptimierten Betrieb unterstützen (Eichner und Uhrig 2021). Konkret besteht hier um die Reduktion elektrischer Lastspitzen. Diese verursichen bei Verkehrsrunternehmen hohe Netzentgelte und somit hohe Stromkosten, da besoin der elektrischen Energie auch die hochste bezogene Leistung bei der Abrechnung berücksichtigt wird. Eine Reduktion der Lastspitzen führt somit unmittelbar zu Kosteneinsparungen. Lastspitzen in der Traktionsstromversorgung * $\text{konnen reduziert werden}$ , wenn beispiselsweise die Fahrscheinene geschäften aufeinander abgestimmt werden. So kann beispiselsweise die im Bremsvorgang eines Zuges bei Einfahr in die Station rück

gewonnene Bremsenergie (Rekuperation) den erhöhten Leistungsbedarf des Antriebs eines aus der Station hersaus beschleunigenden Fahrzeugs teilweise kompensieren.

- Störungsbetrieb: Auch der Betrieb im Störungsfall muss von Beginn an mit bedacht werden. So muss beispelsweise im Falle einer Störung mit anschließender Evakuiierung der Fahrgäste sichergestellt werden, dass die Traktionsstromversorgung aus der Leitstelle hereaus wirksam unterbrochen werden kann. Auf diese Weise wird ausgeschlossen, dass die Fahrgäste auf ihrem Weg zum nachsten Notausstieg mit Hochspannung führenden Teilen in Berührung kommt und sich damit schwer verletzen. Dies ist insbesondere bei Bahnen von Relevanz, bei denen der Traktionsstrom über eine Stromschiene übertragen wird, welche von den Fahrgästen erreicht werden kann.

# Gebäudetechnik in Stationen

Gerade in Stationsbereichen,müssen diverse Zustandsinformationen verschiedener Umsysteme eingelesen und verarbeitet werden. Nahverkehrssysteme dieren in besonderer Weise dem sicheren Transport vieler Menschen. Um gerade in den morgendlichen und abendlichen Stoßzeiten einen optimalen Fahrgastfluss durch die Stationsbauwerke aufrechtzuerhalten,werden die Betriebszustände der Fahrtreppen und Aufzüge überwacht.Ist im Störungsfall nicht ausreichend sichergestellt,dass die Fahrgaste die Station verlassen konnen,konnen Zugfahrten während des Bestehens der Störung die Haltestelle möglicherweise nicht anfahren.Darüber hinaus gelten besondere Anforderungen an Einrichtungen zur Gewährleistung der Fahrgastsicherheit in Haltestellen bei einem Fahrbetrieb ohne Fahrzeugfuhrer.In Abhängigkeit der Zustände dieser Einrichtungen,müssen möglicherweise Sicherheitsgerichtete Reaktionen der automatischen Zugbeeinflussungssysteme angestoßen werden.Konkrete Beispiele hierfür umfassen:

- Sicherung der Bahnsteigkante über Bahnsteigtären: Wenn sich kein Zug in der Station befindet, erkennen oder verhindern Bahnsteigtären ein Eindringen von Fahrgästen in den Gleisbereich über die Bahnsteigkante. Im Falle eines erkannten Eindringens (beispiselsweise bei einem in den Gleisbereich fallenden Fahrgast) oder bei einem Ausfall technischer Einrichtungen, der zu einem Eindringen von Fahrgästen in den Gleisbereich führen kann (zum Beispiel offene Bahnsteigtären), wird die Einfahrten eines Zuges in diesen Gleisbereich durch das Signalsystem verhindert. Ebenfalls wird das Anfahrten eines Zuges bei geöffneten Bahnsteigtären verhindert.  
- Nothalttaster: Auf allen U-Bahnsteigen gibt es für jedem Gleis Nothaltgriffe auf dem Bahnsteig. Der Nothalt wirkt in der Regel immer nur für ein Gleis. Stürzt ein Fahrgast auf das Gleis, kann der Nothalt von den Fahrgästen betätigter werden. Die Züge, die sich auf diesen gleis dem Bahnsteig nähern, werden dadurch vor der Station sicher zum Stillstand gebracht. Ebenfalls werden in der Station wartende Züge bei Betätigung eines Nothalttasters an der Ausfahrheit gehindert. Solle ein Zug bei Auslösung eines Nothalts schon angefahrenn sein, wird er in den Stillstand gebracht.  
- Bahnsteigbeschallung: Die Aufgabe einer Bahnsteigbeschallung ist die Ansprache von Fahrgästen durch das Betriebspersonal. So können beispelsweise Warnhinweise an

Fahrgäste an der Bahnsteigkante bei nicht bestimmungsgemäßer Benutzung der Bahnanlagen ausgegeben werden. Des Weiteren konnen Verhaltensanweisungen an Fahrgäste bei Störungen gegeben werden oder eine Information über Rettungsmaßnahmen und zur Beruhigung nach eingetretenen Notfällen erfolgen. Die Bahnsteigbeschallung wird so ausgelegt, dass der Bahnsteig und der vom Bahnsteig aus erreichbare Gleisbereich akustisch erreicht wird (VDV 2000).

- Sprecheinrichtungen: Aufgabe von Sprecheinrichtungen ist die Herstellung einer Sprechverbindung von Fahrgästen im Stationsbereich zu einer besetzten Betriebsstelle zur Meldung von Vorkommnissen wie Unfälle (außerhalb des Überwachungsbereichs technischer Einrichtungen), hilfloser Personen, Bränden oder Fehlverhalten und Tätlichkeiten von Fahrgästen. Die Sprechverbindungen sollen an einem Arbeitsplatz in der Leitstelle auflaufen, von dem die Funktion der Bahnsteigkanten- und Bahnsteiggleisbeobachtung aufgeschaltet werden kann und darüber hinaus die für das Stillsetzen des Fahrbetriebs und die Fahrspanningsabschaltung notwendigen Bedienhandlungen ausgeführten werden können. In thisem Zusammenhang sollen vom Bedienplatz auch die erforderlichen Rettungs- und Ordnungsdienste alarmiert werden können (VDV 2000).  
- Bahnsteigkanten- und Bahnsteiggleisbeobachtung: Nach Ansprechen technischer Überwachungseinrichtungen soll über Videokameras eine Fernbeobachtung zur Beurteilung des eingetretenen Notfalls aus der Betriebsstelle Heraus möglich sein. Bei deaktivierter Überwachung des Bahnsteiggleises kann der Betrieb mittels Fernbeobachtung aufrechtehalten werden, wenn der einzusehende Bereich über den Bahnsteig hinaus auch den vom Bahnsteig aus erreichbaren Gleisbereich umfasst. Auch eine fernüberwachte Wiederaufnahme des Fahrbetriebs ist möglich, wenn Bilder verwechslungsfrei bereitgestellt werden (VDV 2000).  
- Bahnsteigabschlusssturen: Hierbei handelt es sich um Elemente der Einfriedung des Bahnköpers. Die Bahnsteigabschlusssturen erlauben den Zugang von den Sicherheitsräumen des an eine Station angrenzenden Streckenbereichs (auch als Fluchtweg) auf den Bahnsteig. Sie erlauben für Befugte Personen den Zutritt zu den Sicherheitsräumen des an die Station angrenzenden Streckenbereichs. Bahnsteigabschlusssturen sind überwacht. Lös der Alarm aus, führ das automatische Zugbeeinflussungssystem bei in die Station einfahrenden Fahrzeugene eine Zwangsbremsung aus.

# Infrastruktur (Ingenieurbauwerke und Gleisanlagen)

Gerade in leistungsfähigen städtischen Schnellbahnsystemen befinden sich wesentliche Anteile der Strecken in Tunnelbereichen. Dies betet den Vorteil einer Entflechtung des Schienenverkehrs vom Straβenverkehr. Allerdings sind hierfür weitergehende Anforderungen umzusetzen:

- Brandschutzeinrichtungen in Tunneln: Tunnelbereiche werden in Brandabschnittte eingeweilt. Brandabschnittte sind baulich abgegrenzte Bereiche innerhalb einer Verkehrssanlage, die im Falle eines Brandes das Feuer auf diesen Abschnitt beschränken sollen. In den verschiedene Brandabschnitten sind infrastrukturseitige Brandmelder instal

liert, die ausgewertet werden müssen. Bei erkanten kritischen Ereignissen wird diese Information an die Zugsicherungseinrichtung weitergegeben und Dort eine Sicherheitsgerichtete Reaktion ausgelöst. So werden beispelssweise Streckenbereiche in Tunneln entweder komplett für Zugfahrten gesperrt oder ein Zug fahrthohne Halt durch eine betroffene Haltestelle hindurch. Des weiteren kann die bauliche Abgrenzung benachbarter Brandabschnittte auch durch feuerhemmende sowie feuerbestandige Brandschutztre erreicht werden. Da diese Brandschutztre in den Gleisbereich verfahren bar sind müssen diese – wie Fluttore – mit in die signaltechnischen Abhängigkeiten vor Erteilung eines Fahrbefehls mit einbezogen werden.

- Tunnelventilation: Für den Fall eines erkannten Notfalls konnen die Tunnelventilationsysteme gezielt gesteuert werden, um eine Evakuierung von Fahrgästen zu unterstützen. Hierbei wird zunachst in Abhängigkeit des Ortes des Feuers entlang der Strecke der nachstgelegene Notausgang identifiziert. In Abhängigkeit der Fluchtrichtung der Fahrgäste werden die Tunnelventilatoren so gesteuert, dass der Rauch entsprechend der Fluchtrichtung der Fahrgäste abgesogen wird. Gegebenenfalls kann auch bei einem Lüfterausfall die Zugkapazität in dem hiervon betroffenen Streckenbereich begrenzt werden.  
- Einsatzen von Tunnellicht: Für die Evakuierung von Fahrgästen oder auch im Falle von Baustellen kann aus der Leitstelle Heraus das Licht im Tunnel angeschaltet werden. Da die Fahrzeugführung in thisem Fall mit der Anwesenheit von Personen im Gleis rechen müssen, sehen die Regelwerke der Betreiber in thisem Fall eine reduzierte Geschwindigkeit der Fahrzeuge vor. Wirde diese Information an das CBTC-System übergeben, kann die Einhaltung der Geschwindigkeitsvorgabe technisch vom Fahrzeuggerät erzwungen werden.  
- Eindingüberwachung in Tunnel: Das Eindingen unberechtigter Personen in den Tunnel über die Notausstiegslumen wird durch Einbruchmeldeanlagen erkannt. Ebenfalls wird das Eindingen unberechtigter Personen über den Tunnelmund von Sensoren erkannt und gemeldet. Wird das Eindingen unberechtigter Personen erkannt, erfolgt ein Alarm auf einer besetzten Leitstelle. Je nach betrieblichem Regelwerk der Betreiber erfolgt eine Sicherheitsgerichtete automatische Reaktion des Zugbeeinflussungssystems. So kann beispisseweise im halbautomatischen Betrieb die Streckeneinrichtung dem Fahrzeuggerät den Wechsel in eine Betriebsart mit higherer Fahrverantwortung befehlen. In thisum Fall kann der Fahrer nach entsprechender Quittierung das Fahrzeug auf einem technisch gesicherten Fahrweg und mit gültigem Fahrbefohl manuell mit reduzierter Geschwindigkeit durch den betroffenen Streckenbereich fahren. Alternativ wird die Strecke gesperrt, die bestehende Fahrerlaubnis eines Fahrzeugs gegebenenfalls eingekürzt und der Zug so an der Einfahr in den betroffenen Fahrwegabschnitt gehindert.  
- Hochwasserschutz in Tunnelanlagen: Behinden sich die Tunnel unter Flüssen, müssen beispisse Gewährdungen aus der externen Umwelt wie Überflutungen von Tunnel durch bewegliche Wehrtore unterbunden werden ohne Zugfahren zu gefährden. Dies bedeutet, dass beispisse bewegliche Tore in sicherungstechnische Abhängig-

keiten eingebunden werden müssen. Es muss sichergestellt werden, dass Fahrzeuge nicht in einen zu sperrenden oder gespernten Abschnitt einfahren und dann gegebenenfalls mit dem sich schliebenden oder geschlossenen Wehrtor kollidieren. Auch muss sichergestellt werden, dass ein Fahrzeug nicht in einem Gleisabschnitt von Wehrtoren eingeschlossen wird.

- Schierenbrucherkennung: Zulassungsbehörden können zusammen zustätliche Anforderungen zur Erkennung von Schierenbrücken stellen. In bestehenden Systemen werden möglicherweise Gleisstromkreise zur Frei- und Besetzmeldung von Gleisabschnitten eingesetzt. Diese können außer dem zum Erkennen von Schierenbrücken genutzt werden.kommen in CBTC-Systemen nun alternative Achszahlsysteme für die Gleisfreimeldung zum Einsatz, sind die Verkehrsunternehmen gezwungen, in Abstimmung mit der Aufsichtsbehörde eine Lösung zur kontinuierlichen Überwachung des Schienenzustandes zu finden, sodass Sicherheit, Punktlichkeit und geringere Instandhaltungskosten gewährleistet werden können.

# Fahrgastinformation

Der Fahrgast steht im Zentrum der Bemühungen der Verkehrssunternehmen um einen Betrieb, der qualitatsgerecht ist. Dies ist insbesondere dann wichtig, wenn dispositive Eingriffe in den Betriebsablauf individuelle Reiseketten der Fahrgäste massiv beeinflussen. Daher sind die Fahrgäste in geeigneter Form und verständlich zu informieren. Da beim automatischen Fahren auch die Halte- und Fahrzeiten automatisch je nach Fahrplanlage des betreffenden Zuges festgelegt werden, kann darauf basierend von der Leittechnik eine relativ exakte Prognose für die Ankunft des Zuges in den nachsten Stationen errechnet werden. Die Leittechnik ermittelt die erwarteten Ankünfte und Abfahrten in den nachsten Stationen aufgrund aktueller Fahrplanlage, erwarteter Halte- und Fahrzeiten sowie der Rückmeldungen des Zuges bezüglich seiner Fahrzeit bis zur actually nachsten Station. Da dies für alle aktiven Züge gemacht wird, kann die Leittechnik auch pro Station eine Listeder nachsten erwarteten Züge erstehen und an die Fahrgastinformation übergeben (Harborth 2019). Durch die Fahrgastinformationssysteme in den Haltestellen konnen dann Vorankündigungen und Ankündigungen in die Station einfahrender Fahrzeuge an Informationsdisplays angezeigt werden und automatisch korrespondierende Lautsprecher-durchsagen angestoßen werden.

Zusätzlich kann die Fahrgastinformation auf dem Fahrzeug durch das für automatische Zugbeeinflussungssysteme vorhandene hochverfügbare bidirektionale Datenkommunikationssystem verbessert werden. Beispielsweise kann den Fahgästen zusätzliche Information dargeboten werden, damit sich diese better im Verkehrssystem orientieren können (zum Beispiel Türoeffnung auf der rechten Seite, der linken Seite oder an beiden Seiten des Fahrzeugs im Stationsbereich in Verbindung mit der Aufforderung an die Fahgäste, das Fahrzeug auf einer bestimmen Seite zu verlassen). Außendem konnen weitere Mehrwerte für die Fahgäste geschaffen werden. Je nach verfügbarer Bandbreite kann das Datenkommunikationssystem auch für andere (nicht-sicherheitsrelevante) Anwendungen wie

Videodaten, Ankündigungen von Wartungsarbeiten oder anderen Fahrgastinformationen des Betreibers verwendet werden (Rahn 2011). Dies erhöht die Attraktivität des Schienenverkehrssystems für die Fahrgäste.

# Instandhaltung

Der hoher automatisierte Betrieb ohne Fahrer stellt wesentlich höhere Anforderungen an die Verfügbarkeit fahrzeug- und streckenseitiger Teilsysteme als beispisseweise ein halbautomatischer Betrieb mit einem Fahrer an Bord. In Bezug auf die Unterstützung der Instandhaltungsfunktion in Verkehrsunternehmen konnen Schnittstellen zu verschiedenen Umsystemen vorgesehen werden:

- Service- und Diagnosesysteme: Diese Systeme unterstützen eine korrektive Instandhaltung geben schon vor einem Service-Einsatz Informationen über die Störungsursache und defekte Baugruppen. Ist eine fahrzeug- oder streckenseitige Systemkomponente gestört, hat das große Auswirkungen und der betriebliche Aufwand für einen Betrieb auf der Rückfallebene ist hoch. Im Falle einer Störung ist also schnelles undzielgerichtetes Handeln gefordert. Die gestorte Komponente muss schnell erkannt werden und es mussen effektive Maßnahmen zur Behebung des Ausfalls ergriffen werden. Die Service- und Diagnosesysteme stehen sowohl Leitstellen- als auch den Werkstattmitarbeitern zur Verfügung. Über eine Unterstützung einer korrektiven Instandhaltung hinaus sind die Verkehrssunternehmen bestrebt, vorhandene Service- und Diagnosesysteme in Richtung einer Plattform für die zustandsorientierte oder better vorausschauende Instandhaltung weiterzuentwickeln. Diesträgt der Tatsache Rechnung, dass wegen der dichen Zugfolge in städtischen Verkehrssystemen Ausfälle im Betrieb unerwänscht sind.

- Betriebshofmanagementssysteme: Diese Systeme sorgen davon, dass die Schierenfahrzeuge für den täglichen FahrbetriebVBorbereitet und auf die richtige Fahrt disponiert sind. Betriebshofmanagementssysteme steuern samtliche Prozesse im Betriebshof von der Einfahrth der Fahrzeuge, über ihre Versorgung, Reparatur bis hin zu ihrer Abstellung. In Abhängigkeit des im System hinterlegten Kalenders der erforderlichen Aktivitäten bildet das Betriebshofmanagementssystem die Mission des Fahrzeugs. Diese Mission ist eine Serie von Fahraufträgen, welche durch die Automatisierungskomponente des Schierenfahrzeugs abgefahren werden kann. Die Interaktion automatischer Zugbeeinflussungssysteme mit Betriebshofmanagementssystemen ist die Grundlage einer automatischen Betriebsführung in Betriebshöfen.

# Literatur

Brückner D (2017) Lösungen für das automatisierte Fahren im Nahverkehr. Signal + Draht 109(6):6-11  
Brux G (2007) Automatischer Betrieb Projekt RUBIN - U-Bahn Nürnberg. EIK:211-227

DIN EN 16334-2:2020 Bahnanwendungen - Fahrgastalarmsystem - Teil 2: Systemanforderungen für städtische Schierenbahren. Deutsche Fassung EN 16334-2:2020  
DIN EN 50159:2011-04 Bahnanwendungen - Telekommunikationstechnik, Signaltechnik und Datenverarbeitungssysteme - Sicherheitsrelevante Kommunikation in Übertragungssystemen; Deutsche Fassung EN 50159:2010  
Eichner D, Uhrig B (2021) Innovationen in CBTC-Anwendungen. Signal + Draht 113(9):34-44  
Farooq J (2018) Performance analysis and evaluation of advance designs for radio communication systems for Communications-Based Train Control (CBTC). Dissertation, Technical University of Denmark  
Geistler A, Schwab M (2013) ETCS-L2-Zugsicherung mit alternativen Funklösungen. Signal + Draht 105(7+8):14-20  
Harborth M (2019) Operatives Fahrplansystem für automatisches Fahren. Signal + Draht 111(3):32-38  
Heitzinger J (2002) Erfahrungen mit dem modularen Leitsystem VICOS OC 501. Signal + Draht (94) 4:18-22  
IEC 62290-1:2014 Railway applications - urban guided transport management and command/control systems - part 1: system principles and fundamental concepts  
IEEE 1474.1-1999 IEEE standard for Communications-Based Train Control (CBTC) performance and functional requirements. IEEE, New York  
Krimmling J (2017) Ampelsteuerung - Warum die grüne Welle nicht immer Funktioniert. Springer, Berlin  
Mücke W (2005) Betriebsleittechnik im öffentlichen Verkehr. Eurailpress, Hamburg  
Nieußen N, Kogel B, Kuckelberg A (2016) Konfliktlösungsstrategien bei der Disposition im Eisenbahnwesen. EI-Eisenbahningenieur März:10-13  
Pancini Fitzek T, Joos F, Huber H (2021) Fahrgäste, Stationen & Züge im Mittelpunkt - bedarfsgerechter Betrieb während COVID-19 und darüber hinaus. Signal + Draht 113(1+2):6-11  
Rahn K (2011) Green Mobility – Effiziente Zugbeeinflussung mit CBTC-Systemen. Signal + Draht 103(10):26–29  
Schienbein M (2018) Trends und Anforderungen der Funkübertragung für Betriebsdaten und Passagierservices. Signal + Draht 110(7+8):23-30  
Schnieder L (2020) Funktionalsallokation in funkbasierten Zugbeeinflussungs-systemen - ein Vergleich. Eisenbahntechnische Rundschau 70(11):16-19  
Thomys M (2006) Fahrgastrumbeobachtung über Wireless LAN. Signal + Draht 98(7+8):23-32  
VDV (2000) Verband Deutscher Verkehrsunternehmen (VDV): VDV-Schrift 399 – Anforderungen an Einrichtungen zur Gewährleistung der Fahrgastssicherheit in Haltestellen bei Fahrbetrieb ohne Fahrzeugführer. VDV, Köln, Oktober 2000

# Automatisierungsgrade automatischer Zugbeeinflussungssysteme

3

# SN Flashcards

Als Käfer* in diesen Buches können Sie kostenlos unsere Flashcard-App „SN Flashcards" mit Fragen zur Wissenschaften und zum Lernen von Buchinhalten nutzen.

1. Gehen Sieitte auf https://flashcards.springernature.com/login und  
2.(erstellen Sie ein Benutzerkonto,indem Sie ihre Mailadresse angegeben und ein Password vergeben.  
3. Verwenden Sie den folgenden Link, um Zugang zu Ihr dem SN Flashcards Set zu erhalten:  $\triangleright$  https://sn.pub/sK5mLQ

Sollte der Link fehlen oder nicht Funktionieren, senden Sie unsitte eine E-Mail mit dem Betreff „SN Flashcards“ und dem Buchtitel an customerservice@springernature.com

Stadtische Schienenverkehrssysteme sind komplexe Menschen-Maschine-Systeme. In einschlagigen Standards werden Automatisierungsgrade definiert. Ausgangspunkt hierfür ist eine generische Beschreibung aller für den Betrieb eines städtischen Schienenverkehrssystems erforderlichen Funktionen. Auf thisem Funktionskatalog aufbauend wird dargestellt, wie durch aufeinander aufbauende Automatisierungsgrade (englisch: Grade of Automation, GoA) zunehmend mehr Funktionen von technischen Systemen übernommen werden. Der Mensch wird hierbei zunehmend entlastet (vgl. Tab. 3.1). In der hochsten Ausprüfung wird das System unbegleitet fahrerlos betrieben – eine Mitwirkung des Menschen an Bord des Zuges ist dann im Regelbetrieb nicht mehr erforderlich. Mit zunehmendem

Tab. 3.1 Überblick über die Automatisierungsgrade  

<table><tr><td rowspan="2" colspan="2">Grundlegende Sicherungsfunktionen im Bahnbetrieb</td><td>Onsight train operation TOS</td><td>Non-automated train operation NTO</td><td>Semi-automated train operation STO</td><td>Driverless train operation DTO</td><td>Unattended train operation UTO</td></tr><tr><td>GoA0</td><td>GoA1</td><td>GoA2</td><td>GoA3</td><td>GoA4</td></tr><tr><td rowspan="3">Sichern der Zugbewegung (Abschn. 5.1)</td><td>Sichern des Fahrweges</td><td>Bediener</td><td>technisches System</td><td>technisches System</td><td>technisches System</td><td>technisches System</td></tr><tr><td>Sichern der Abstandshaltung</td><td>Bediener</td><td>technisches System</td><td>technisches System</td><td>technisches System</td><td>technisches System</td></tr><tr><td>Sichern der Geschwindigkeit</td><td>Bediener</td><td>Bediener (teilw. Überwachung durch technisches System)</td><td>technisches System</td><td>technisches System</td><td>technisches System</td></tr><tr><td rowspan="2">Fahren des Fahrzeugs (Abschn. 5.2)</td><td>Ermittlung des optimalen Fahrprofils</td><td>Bediener</td><td>technisches System</td><td>technisches System</td><td>technisches System</td><td>technisches System</td></tr><tr><td>Regelung von Bremse und Traktion gemäß des optimalen Fahrprofils</td><td>Bediener</td><td>technisches System</td><td>technisches System</td><td>technisches System</td><td>technisches System</td></tr><tr><td rowspan="2">Überwachen der Profilfreiheit (Abschn. 5.3)</td><td>Verhinderung von Kollisionen mit Objeken</td><td>Bediener</td><td>Bediener</td><td>Bediener</td><td>technisches System</td><td>technisches System</td></tr><tr><td>Verhinderung von Kollisionen mit Personen</td><td>Bediener</td><td>Bediener</td><td>Bediener</td><td>technisches System</td><td>technisches System</td></tr></table>

<table><tr><td rowspan="3">Überwachen des Fahrgastwechsels (Abschn. 5.4)</td><td>Steuern und Überwachen der Türfreigabe</td><td>Bediener</td><td>Bediener</td><td>Bediener</td><td>technisches System oder Bediener</td><td>technisches System</td></tr><tr><td>Sichern der Bahnsteigkante</td><td>Bediener</td><td>Bediener</td><td>Bediener</td><td>technisches System oder Bediener</td><td>technisches System</td></tr><tr><td>Sicherstellung der Abfertigungsbedingungen</td><td>Bediener</td><td>Bediener</td><td>Bediener</td><td>technisches System oder Bediener</td><td>technisches System</td></tr><tr><td rowspan="2">Automatischer Zugbetrieb (Abschn. 5.5)</td><td>Ein- und Aussetzen von Fahrzeugen</td><td>Bediener</td><td>Bediener</td><td>Bediener</td><td>Bediener</td><td>technisches System</td></tr><tr><td>Überwachung des Fahrzeugzustands</td><td>Bediener</td><td>Bediener</td><td>Bediener</td><td>Bediener</td><td>technisches System</td></tr><tr><td>Störfallerkennung und Störfallmanagement (Abschn. 5.6)</td><td>Fahrzeugdägnose, Erkennung von Feuer und Rauch, Handlungen bei Störfläten</td><td>Bediener</td><td>Bediener</td><td>Bediener</td><td>Bediener</td><td>technisches System und/oder Bediener in Leitstelle</td></tr></table>

Automatisierungsgrad erhöhen naturgemäß die Anforderungen an das Signalsystem und die eingesetzten Fahrzeuge zu. Die einzelnen Funktionen werden in Kap. 5 bisher erlautert.

# 3.1 Grade of Automation 0: Zugbetrieb auf Sight

Beim Zugbetrieb auf Sicht (Train Operations on Sight, TOS) ist der Fahrzeugführer in vollem Umfang für die sichere Durchführung der Fahrzeugbewegung (insbesondere den Folgefahrscheinz) verantwortlich, da hier Fahrzeugseitig keinerlei Überwachung der zulässigen Fahrweise realisiert ist (IEC 62290-1:2014). Die Fahrzeuge verkehren auf eingeschrankt gesicherten Fahrwegen. Einzelweichensteuerungen stellen und sichern Weichen in der Endlage und zeigen dies dem Fahrzeugführer an. Einfache Fahrsignalanlagen gewährleisten an eingleisigen Strecken den Gegenfahrchutz. Bahnübergänge vermeiden Unfälle zwischen Straβenverkehrsteilnehmern und Schienenfahrzeugen. In komplexeren Streckentopologien erfolgt eine Fahrewegsicherung über Fahrstraße. Diese Automatisierungsrgrad kann in zwei Stufen unterschieden werden:

- Automatisierungsgrad 0a - nicht assistierter Zugbetrieb auf Sicht: Der Fahrer beobachtet stets den Verkehr in seinem Sichtfeld, den Fahrweg und die Höchstgeschwindigkeit. Er kontrolliert das Anfahren und das Bremsen, erkennt Gefahren-situationen und hält das Schienenfahrzeug bei Bedarf an. Die Fahrweise entspricht also dem Führer eines Personenkraftwagens (Pkw) im öffentlichen Straßenraum.  
- Automatisierungsgrad  $Ob$  - assistierter Zugbetrieb auf Sicht: Der Fahrer wird durch ein Fahrerassistenzsystem in einzelnen Aspekten seiner Fahraufgabe unterstützt. Sensoren erfassen hierbei das Verkehrsumfeld und Algorithmen analysieren die Fahrsituation. Der Fahrer wird über einen Warnhinweis zum rechtzeitigen und wichtigen Eingreifen aufgefordert (informierendes Assistenzsystem), beziehungsweise es erfolgt ein automatischer Eingriff in die Fahrdynamik des Schienenfahrzeugs (intervenierendes Assistenzsystem) und der Fahrer wird hierüber informiert (Jung et al. 2018).

# 3.2 Grade of Automation 1: Nicht automatisierter Zugbetrieb

Beim nicht automatisierten Zugbetrieb (Non-automated Train Operations, NTO) wird das Fahrzeug auf technisch geschlossen Fahrwegen vom Fahrer geführt (IEC 62290-1:2014). Technische Einrichtungen signalieren dem Fahrer, dass der Fahrweg technisch gesichert ist. Dies bedeutet, dass die Fahrzeugbewegung technisch vor Gegenfahrten, Flankenfahrten, Folgefahren und Unfälle mit systemfremden Verkehrsteilnehmern (Kraftfahrzeugen und Fußgängern) geschützt ist. Der Fahrzeugführ er führt das Fahrzeug gemäß der betrieblichen Vorgaben. Die Einhaltung der zulässigen Fahrweise wird auf dem Fahrzeug überwacht. Je nach konkreter Ausprüfung der Überwachung kann dieser Automatisierunggrad in zwei Stufen unterschieden werden:

- Automatisierungsgrad 1a - nicht automatisierter Zugbetrieb mit punktformiger Übertragung und Überwachung der zulässigen Fahrweise des Fahrzeugs: Hierbei erhält das Fahrzeug an einem diskreten Punkt entlang der Strecke eine Information über den Zustand des Signals. Das Fahrzeuggerät leitet im Bedarfsfall eine Sicherheitsgerichtete Reaktion ein. Diese Systeme dieren der Vermeidung der Überfahrt Halt zeigender Signale (Fahrspere).  
- Automatisierungsrad 1b - nicht automatisierter Zugbetrieb mit kontinuierlicher Übertragung und Überwachung der zulässigen Fahrweise des Fahrzeugs: Hierbei erhält das Fahrzeug von der Streckeneinrichtung Führungsgrößen, mit denen die Fahrzeugbewegung kontinuierlich überwacht werden kann. Diese Systeme überwachen die Einhaltung der zulässigen Fahrweise des Zuges kontinuierlich und gehen damit über den zuvor beschriebenen Funktionsumfang (Fahrspere) hinaus. Die Datenübertragung von der Strecke zum Fahrzeug kann entweder an diskreten Punkten oder kontinuierlich erfolgen.

# 3.3 Grade of Automation 2: Halbautomatischer Zugbetrieb

Beim halbautomatischen Zugbetrieb (Semi-automatic Train Operation, STO) die Steuerung der Traktionsleistung und der Bremsen wird von einem technischen System übernommen (IEC 62290-1:2014). Der Fahrer bleibt in dieser Automatisierungsgrad nach wie vor auf dem Führerstand. Er erteilt den Befehl für die Türoeffnung, überwacht den Fahrgastwechsel und fertigt den Zug in der Station ab. Liegen alle Abfertigungsbedingungen vor, erteilt er den Abfahrauftrag für eine sichere Abfahr des Zuges aus der Haltestelle. Der Fahrer überwacht die Fahrt zur{nachsten Station und kann in Gefahrensituationen那么简单 eingreifen (Rumsey 2010). Das Fahrzeug bremst selbsttätig mit einer hohen Genauigkeit auf die Zielposition in der{nachsten Station. Auf diese Weise kann eine von der Leitebene vorgegebene optimale Fahrstrategyvom Fahrzeug selbsttätig umgesetzt werden.

# 3.4 Grade of Automation 3: Begleiteter fahrerloser Zugbetrieb

Beim begleiteten fahrerlosen Zugbetrieb (Driverless Train Operation, DTO) kann sich der Fahrer vom Führerstand des Zuges entfern. Der Fahrer bleibt aber weiterhin an Bord des Zuges, um seine betrieblichen Aufgaben zu erfüllen und um im Falle des Funktionsausfalls der Automatisierungssysteme die Verantwortung für das Führren des Zuges über den hierfür vorgesehenen Notführung auf dem Fahrzeug unverzüglich wieder zu übernehmen. Da der Fahrer nach wie vor auf dem Fahrzeug ist, resultieren hieraus für die Entstörung und Wiederherstellung des Regelbetriebs Zeitgewinne im Vergleich zum im nachsten Abschnitt dargestellt den unbegleiteten fahrerlosen Zugbetrieb, bei dem das Betriebspersonal das Fahrzeug erst fußlaufig durch den Tunnel erreichen muss. Da der Fahrer in thisem Automatisierungsgrad die Fahrt des Zuges nicht mehr überwacht und die vor dem Zug liegende Strecke nicht mehr im Voraus einseen kann, stellt dieser Automatisierungs-

grad höhere Anforderungen an Gewährleistung der Profilfreiheit für die Zugfahrten (beispiselsweise durch fahrzeugseite Hinderisierungssysteme). Im Automatisierungsgrad DTO konnen die Türen und die Abfahrct des Zuges vom Bahnsteig entweder automatisch oder manuell von einem beliebigen Ort im Zugverband (und damit nicht zwingend vom Führerstand des Zuges) gesteuert werden. Dies wirkt sich insbesondere an Endhaltestellen positiv auf den Durchsatz aus, da die Zeit gespart werden kann, die bei geringeren Automatisierungsgraden für den Wechsel des Führerstandes erforderlich ist. Der Fahrzeugfuhrer muss nun nicht mehr den ganzen Zugverband entlang von einem Führerstand zum anderen gehen (Rumsey 2010).

# 3.5 Grade of Automation 4: Unbegleiteter fahrerloser Zugbetrieb

Der unbegleitete fahrerlose Zugbetrieb (Unmanned Train Operation, UTO) kann Zugbewegungen ohne Fahrgäste (zum Beispiel für Fahren in ein Abstellgleis oder in einem automatisiert betriebenen Depot) oder den Betrieb von Zügen im Fahrgastbetrieb ohne Begleitpersonen an Bord umfassen. Letzteres setzen voraus, dass der Zug bei Ausfallen von Steuerungssystemen ferngesteuert werden kann oder zumindest von entlang der Strecke verfügbarbarem Personal in möglichst kurzer Zeit erreicht werden kann. Gegebenenfalls ist es auch möglich, das Fahrzeug über die Darstellung der Führerstandsanzeige und Echtzeitkamerabildern aus der Leitstelle in der Rückfallebene situativ fernzusteuern. Im (Brandenburger et al. 2017) Störungsfall müssen die Fahrgäste an Bord aus der Leitstelle hereaus berühigt werden. Daher sind gute Kommunikationsverbindungen zwischen dem Fahrzeug und den Mitarbeitern des Verkehrsinternnehmens unerlässlich. Eine Automatisierung der Türsteuerung ist für diesen Automatisierungsgrad zwingend erforderlich und muss entsprechend sicher gestaltet sein. Dies bedeutet, dass eingeklemme Kleidungsstücken oder Personen safer erkannt werden müssen und in thisem Fall unmittelbar eineicherheitsgerichtete Reaktion eingeleitet wird. Ein erhöhter Schutz der Strecke vor dem Eindringen unberechtigter Personen sowie technische Systeme zur Hinderniserkennung sind ebenfalls erforderlich.

# Literatur

Brandenburger N, Naumann A, Grippenkoven J, Jipp M (2017) Der Train Operator - Situative Fernsteuerung von automatisierten Zügen. EI - Eisenbahningenieur 09/2017, S 13-15  
IEC 62290-1:2014 Railway applications - urban guided transport management and command/control systems - part 1: system principles and fundamental concepts  
Jung HS, Rüffer M, Schindler C (2018) Fahrerassistenzsysteme für die Straβenbahn. Nahverkehr 36(7+8):26-35  
Rumsey A (2010) Semi-automatic, driverless and unattended operation of trains. Signal + Draht 102(3):43-46

# Betriebsarten und Betriebsartenübergänge im automatisierten Betrieb

4

# SN Flashcards

Als Käfer*in diesen Buches können Sie kostenlos unsere Flashcard-App „SN Flashcards" mit Fragen zur Wissenschaftung und zum Lernen von Buch-inhalten nutzen.

1. Gehen Sieitte auf https://flashcards.springernature.com/login und  
2.(erstellen Sie ein Benutzerkonto,indem Sie ihre Mailadresse angegeben und ein Password vergeben.  
3. Verwenden Sie den folgenden Link, um Zugang zu Ihr dem SN Flashcards Set zu halten:  $\triangleright$  https://sn.pub/sK5mLQ

Sollte der Link fehlen oder nicht Funktionieren, senden Sie unsitte eine E-Mail mit dem Betreff „SN Flashcards“ und dem Buchtitel an customerservice@springernature.com

Die Zugbeeinflussungssysteme dieren einer optimalen Abwicklung des Betriebs. Hierfür stehen – in Abhängigkeit vom Ausstattungsgrad von Fahrzeug und Infrastruktur – unterscheidliche Betriebsarten zur Verfügung.Eine Betriebsart umfasst eine Teilmenge an Sicherungsfunktionen. Die verschiedene Betriebsarten werden in Abschn. 4.1 dargestellt. Zwischen den Betriebsarten sind diverse Übergänge möglich. Diese sind an eindeutige Kriterien geknupft und werden technisch überwacht. In Abschn. 4.2 werden die zwischen den Betriebsarten bestehenden Übergänge anhand ausgewählter Beispiele in halbautomatisch betriebenen Systemen erläutert. In Abschn. 4.3. werden exemplarische Betriebsartenübergänge in unbegleitet fahrerlosen Systemen napher ausgeführrt.

# 4.1 Betriebsarten im Überblick

Automatische Zugbeeinfluussysteme werden in verschiedene betrieblichen Situationen in verschiedenen Betriebsarten betreiben. Die Betriebsarten sind gekennzeichnet durch einen entsprechenden Umfang vom Zugbeeinfluussystem zur Verfügung stehenden Überwachungsfunktionen. Die Betriebsarten und Betriebsartenübergänge stellen einen (endlichen) Zustandsautomaten dar. Hierbei gibt es eine endliche Anzahl von Zuständen und definierte Übergangsbedingungen. Abb. 4.1 stellt einen Zustandsautomaten mit den üblichen Betriebsarten und Betriebsartenübergängen (Transitionen) dar. Diese Betriebsarten können unterschieden werden in Betriebsarten für den Regelbetrieb (vgl. Abschn. 4.1.1), Betriebsarten für Gefahren- und Störzustände (vgl. Abschn. 4.1.2), Betriebsarten für Ausschaltzustände (vgl. Abschn. 4.1.3) sowie Betriebsarten für nicht mit CBTC ausgerüstete Bestandsstrecken (vgl. Abschn. 4.1.4). Zusätzlich zu den in Abb. 4.1 dargestilten Betriebsarten konnen von den Betriebern im Einzelfall weitere Betriebsarten gewünscht werden. Beispiele hierfür sind ein ferngesteuerter Betrieb, bei dem die Leitstelle die Rolle des Fahrpersonals übernimmt oder die Umschaltung zwischen ver

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/0734c95364a486d1d88d2056231fe43bbd5527572f527a54116659d038fd9724.jpg)  
Abb. 4.1 Prinzipskizze eines Zustandsautomaten der Betriebsarten mit zwischen diesen bestimmenden Übergängen für einen halb automatischen Betrieb

schiedenenz Zugbeeinflussungssystemen, welche sich möglicherweise aus dem Migrations-konzept hereby ergibt (fahrzeugseitige Mehrfachausrücktung). Um den Zustandsautomaten für die Darstellung in thisem Buch übersichtlich zu halten, werden hier nur die grundlegenden Betriebsarten umrissen, die bei vielen Betriebern zum Einsatz kommt.

# 4.1.1 Betriebsarten für den Regelbetrieb

Es können verschiedene Betriebsarten für den Regelbetrieb unterschieden werden. Diese werden nachfolgend mit ihrem korrespondierenden Funktionsumfang umrissen.

# Nicht-automatisches Fahren in Vollüberwachung (Supervised Manual Mode)

These Betriebsart garantiert die kontinuierliche Geschwindigkeitsüberwachung und die gesamte Zugsicherung durch die CBTC-Fahrzeugausrüstung. Die CBTC-Fahrzeugausrüstung kann erst in diese Betriebsart wechseln, wenn alle benötigten Daten zur zulässigen Fahrweise des Zuges auf dem Fahrzeug vorhanden sind und der Standort des Zuges besteht ist. Dem Zug liegt eine Fahrerlaubnis vor, da der Sicherungszustand samtlicher vor dem Zug liegenden Gefahrenpunkte besteht ist. Die Einhaltung der gültigen Fahrerlaubnis kann vom Zugbeeinflussungssystem überwacht werden. Auf dem Fahrzeug liegt ein umfassendes statisches Geschwindigkeitsprofil vor. Die Einhaltung des statischen Geschwindigkeitsprofils wird durch das Fahrzeug überwacht. In dieser Betriebsart führt der Fahrzeugfuhrer das Fahrzeug durch Betätigten des Fahr- und Bremshebels manuell gemäß den Vorgaben zur zulässigen Geschwindigkeit. Da der Zug über eine ausreichend genaue Kenntnis seiner eigenen Position verfügt, kann die Freigabe von Türen (im Betrieb mit Bahnsteigtären) automatisch erfolgen. In dieser Betriebsart liegen Informationen über die Zugvollständigkeit vor, sodass die Züge einander im wandernden Raumabstand folgen konnen.

# Halbautomatisches Fahren in Vollüberwachung (Automatic Mode)

Bezüglich der verfügbaren Überwachungsfunktionen unterscheidet sich diese Betriebsart nicht vom zuvor dargestellen nicht-automatischem (d. h. manuellen) Fahren in Vollüberwachung (Supervised Manual Mode). Der Unterschied hierbei ist jedoch, dass der Fahrer in dieser Betriebsart von weiteren Aufgaben der Fahrzeugsteuerung entlastet wird. In dieser Betriebsart wird das Fahrzeug nach Bestätigung des Vorliegens der Abfertigungsbedingungen durch den Fahrer von der automatischen Fahr- und Bremssteuerung automatisch zum Haltepunkt in der nachsten Station geführt. Der Fahrer muss die Fahrt jederoch noch überwachen, da bei einem halbautomatischen Betrieb noch mit Hindernissen vor dem Fahrzeug gerechnet werden muss. Erreicht das Fahrzeug den Haltepunkt in der nachsten Station, werden die Türen des Fahrzeugs automatisch geöffnet.

# Unbegleitetes fahrerloses Fahren in Vollüberwachung (Full Automatic Mode)

In dieser Betriebsart ist, im Unterschied zum zuvor dargestellen halbautomatischem Fahren in Vollüberwachung kein Fahrer auf dem Führerstand des Fahrzeugs erforderlich. Durch technische Einrichtungen an Bord des Zuges, bzw. entlang der Strecke (bspw. durch

einen baulichen Gefährungsausschluss wie Bahnsteigtären) werden Kollisionen mit Objekten oder Personen im Gleis wirksam verhindert. Gleiches gilt für die Überwachung des zuvor vom Fahrer beobachteten Fahrgastwechsels. Das Fahrzeug ist in dieser Betriebsart in der Lage ohne Mitwirkung eines Bedieners alle mit seiner betrieblichen Mission im Zusammenhang stehenden einzelnen Fahraufträge durchzuführen. Umfassende Sensorik auf den Fahrgästen unterstützt die Erkennung von Störflällen, deren angemessene Behandlung jedoch eine Mitwirkung des Bedieners der Leitstelle erfordert. Bereits in Systemen, die im Fahrgastbetrieb nur halbautomatisch verkehren kann es vorgesehen sein, dass die Schienenfahrzeuge Fahrten in bestimmten Streckenabschnitten unbegleitet fahrerlos bewältigen. Beispiele hierfür ist kein anderer unbegleitet fahrerlos durchgeführten Kehre an der Endhaltestelle auch die Fahrt in einem automatisierten Betriebshof.

# 4.1.2 Betriebsarten für Gefahren- und Störzustände

Es können verschiedene Betriebsarten für Gefahren- und Störzustände unterschieden werden. Diese werden nachfolgend mit ihrem korrespondierenden Funktionsumfang umrissen.

# Zwangsbremse (Emergency Brake)

Kommen es zu einem Wechsel in diese Betriebsart, wird der Zug in den Stillstand gebremst. Der Stillstand ist durch den Triebfahrzeugführer zu quittieren. Eine Zwangsbremse wird bei den folgenden Ereignissen ausgelost:

- Odometriebehler: Bei Ausfall von Komponenten der Weg- und Geschwindigkeitsmessung ist das Fahrzeug nicht mehr ausreichend prazise lokalisiert. Die exakte Fahrzeugposition ist in thisem Fall mit einer große Unsicherheit besteht. Es muss schlimmstenfalls eine Kollision mit einem anderen Fahrzeug oder einem Hindernis an einem Gefahrpunkt angenommen werden. Das Fahrzeug reagiert dazu zur sicheren Seite und lost eine Zwangsbremse aus.  
- Fehler von sicheren Ausgaben des Fahrzeuggeräts: Fehlerhafte Ausgaben des CBTC-Fahrzeuggeräts an die Fahrzeugsteuerung müssen durch regelmäßige Self-testzyklen des Fahrzeuggeräts offenbart werden. Ein Beispiel einer solchen Sicherheits-relevanten Ausgabe ist das Ansprechen der Bremssysteme des Fahrzeugs. Wird ein Fehler offenbart, muss angenommen werden, dass die gegebenenfalls erforderliche Bremsung im Bedarfsfall zeitlich verzögert oder möglicherweise gar nicht ausgelöst wird. Daher reagiert das Fahrzeuggerät zur sicheren Seite und nimmt den sicheren Zustand ein (d. h. es besteht eine Zwangsbremsung aus).  
- Verlust der Zugvollständigkeit: Für den Fall, dass es zu einer unbeabsichtigen Zugtrennung kommt, wird eine Zwangsbremsung ausgelöst. Dies ist schon in den grundlegenden Betriebsvorschriften so gefordert (Forderung nach einer „durchgehenden und selbstätigten Bremse"). Die Auslösung der Zwangsbremse bei Verlust der Zugvollständigkeit ist eine Funktion, die schon durch die Leittechnik des Fahrzeugs realisiert wird.

- Abbruch der Funkverbindung: Für CBTC-Systeme ist die Aufrechterhaltung der Funkverbindung zwischen Fahrzeug und Strecke essenziell. Ist die Funkverbindung unterbrochen, konnen Positionsmeldungen des Zuges gar nicht oder nur zeitverzögert übertragen werden. Auch Verlängerungen von Fahrterlaubnissen werden mölicherweise gar nicht oder nur zeitverzögert an die Fahrzeuge übermittelt, was zu Einbußen in der Streckenleistungsfähigkeit und in Folge dessen zu Verzögerungen im Betrieb führen kann.  
- Ansprechen von Überwachungsfunktionen: Werden unzulässige betriebliche Zustände erkannt, erfolgt ein Ansprechen der Zwangsbremse. Beispiel hierfür ist ein unzulässige Rückrollen des Fahrzeugs, das Ansprechen der Stillstandsüberwachung, eine Verletzung der maximal zulässigen Geschwindigkeit, sowie ein Ansprechen der Türuberwachung bei unzulässiger Türoeffnung. Bei unbegleitetem fahrerlosen Betrieb werden weitere unzulässige betriebliche Zustände technisch erkannt und führen zu einer Zwangsbremsung. Beispiele hierfür sind das Auslösen des Entgleisungsdetektors oder die Auslösing eines intelligenten Bahnräumers zur Erkennung von Kollisionen mit Objekten oder Personen.

# Fahrzeuggeräte im Störungsfall ausgescheltet (Cutout Mode)

Fahrzeuggeräte müssen im Störungsfall ausgeschalten werden können. Hierzu dient ein im Führerstand des Fahrzeugs angeordneter Störschalter, der die Spanningsversorgung des Fahrzeuggeräts unterbricht. Nach dem Ausschalten des CBTC-Fahrzeuggerätes kann der Fahrzeugführer das Fahrzeug auf der betrieblichen Rückfallebene bewegen. Hierbei sind jeder keinerlei Überwachungsfunktionen aktiv. Die Fahrt wird also unter vollständiger Verantwortung des Fahrzeugführers durchgeführt. Maßgeblich hierfür sind die betrieblichen Regelwerke des jeweiligen Betreibers.

# Permissives Fahren im halbautomatischen Betrieb (Restricted Mode Manual)

Für einen reibungslosen halbautomatischen Betrieb muss auch eine Betriebsart vorgesehen werden, welche die Durchführung einer Zugfahr in einem Streckenabschnitt erhögt, für dessen Freisein keine Bestätigung vorliegt. Der Zug hat beim Erreichen des Endes seiner Fahrerlaubnis stets zu halten. Der Fahrzeugfuhrerarf derst dann weiterfahren, wenn er einen fernmündlichen Auftrag erhalten hat. In der Praxis kommt diese Betriebsart in verschiedenen betrieblichen Szenarien zur Anwendung. Fahrzeuge verkehren beispisseweise in einem Streckenbereich, der nicht mit CBTC-Streckeneinrichtungen ausgerüstet ist. Dies ist zum Beispiel bei Ein- und Ausfahren in Betriebshöfe der Fall. Auch nach einer Störung der CBTC-Streckeneinrichtung konnen Züge mit reduzierter Geschwindigkeit weiterfahren. Da im vorausliegenden Streckenabschnitt mit Hindernissen zu rechnen ist, damit die Geschwindigkeit in dieser Fall nur so hoch sein, dass der Zug bei einem Hindernis in seinem Fahrgleis mit Sicherheit zum Halten gebracht werden kann. Es gelten davon für das permissive Fahren die folgenden Abgrenzungen:

- Keine Überwachung des Überfahrens der gültigen Fahrerlaubnis. Das CBTC-Fahrzeuggerät kennt den möglicherweise vor dem Zug liegenden Gefahrpunkt nicht. Deshalb kann keine Überwachung der gültigen Fahrerlaubnis erfolgen. Der Fahrer muss die vor ihm liegende Strecke aktiv beobachten und ist in hohem Maße für die Sicherheit des Betriebs verantwortlich.

- Eingeschränkte Geschwindigkeitsüberwachung: Es wird nur die für diese Betriebsart zulässige Maximalgeschwindigkeit überwacht, da im Gegensatz zum nicht-automatischen Fahren in Vollüberwachung (Supervised Manual Mode), bzw. dem halbautomatischen Fahren in Vollüberwachung (Automatic Mode) keine Geschwindigkeitsprofile vorliegen.  
- Rückrollüberwachung: Das Zugbeeinflussungssystem führt eine Rückrollüberwachung durch. Das Fahrzeug kann also nur in die Fahrtrichtung des besetzten Führerstandes fahren. Rollt es unbeabsichtigt zurück, kommt es zum Bremseingriff.  
Informationen zur Zugvollständigkeit liegen in dieser Betriebsart vor.  
- Die Türfreigabe (im Betrieb mit Bahnsteigtären) erfolgt nur, wenn der Zug ein valides Ortungsergebnis hat. Andernfalls muss der Fahrer sich aktiv über die wirksame Unterdrückung der Türfreigabe hinwegsetzen (.,override").

# Permissives Fahren unbegleiteten fahrerlosen Betrieb (Restricted Mode Driverless)

Auch für einen reibungslosen unbegleiteten fahrerlosen Betrieb ist Betriebsart erforderlich, welche die Durchführung einer Zugfahr mit reduzierter Geschwindigkeit im Falle einer unklaren betrieblichen Situation oder einer Störung vorsieht:

- Betriebliche Behandlung von Störungen im unbegleiteten fahrerlosen Betrieb: Das Fahrzeug registriert eine Störung und kommt infolgedessen durch eine Zwangsbremsung zum Stillstand. Ein Beispiel hierfür ist die Überschreitung des Vertrauens-intervalls für die sichere Weg- und Geschwindigkeitsmessung durch erhöhten Schlupf, bzw. einen verpassten Transponder. Der Bediener der Leitstelle klärt aus der Ferne den betrieblichen Sachverhalt auf. Kann der Bediener durch seine Kenntnis des gesamtten betrieblichen Kontexts ausschreiben, dass sich ein anderer Zug in dem vor dem be-treffenden Zug liegenden Streckenbereich befindet, commandiert er aus der Leitstelle Heraus die Durchführung einer unbegleitet fahrerlosen Permissivfahr. Hierbei steueret die Komponente Automatic Train Protection (ATO) die Geschwindigkeit entsprechend der restruktiven Geschwindigkeitsvorgaben für diese Betriebsart, bis es den nachsten Transponder überfahrent, sich wieder ordnungsgemäß lokalisiert und dann einen gültigen Fahrbefehl für eine fahrerlose Fahrt empfangt.  
- Durchführung von „Bügelfahren“: Die erstige Fahrt eines Betriebstages wird im Restricted Mode Driverless durchgeführt. Die Geschwindigkeit ist hierbei reduziert, da sich nach der nachtlichen Sperrpause möglicherweise unzulässige Objekte innerhalb des Lichtraumprofils des Zuges befinden (bspw. hinterlassenes Werkzeug oder Material einer nachtlichen Baumaßnahme). Ein Begleiter ist während dieser Betriebsart auf dem Fahrzeug zugegen und kann im Falle erkanfter irregularer Betriebsbedingungen einen Zwangshalt auslösen und unmittelbar an der Störungsbehebung mitwirken.

# 4.1.3 Betriebsarten für Ausschaltzustände

Es können verschiedene Betriebsarten für Ausschaltzustände unterschieden werden. Diese werden nachfolgend mit ihrem korrespondierenden Funktionsumfang umrissen.

# Fahrzeug kurzfristig abgestellt (Fahrzeuggerät mit Spannungsvorsorgung über Pufferbatterie)

Im Regelbetrieb eines Nahverkehrssystems ist es nicht notwendig, das CBTC-Fahrzeuggerät ein- und auszuschalten (Sleep Mode). Die Überwachung der dauerhaften Einsatzfähigkeit erfolgt auch im Sleep-Modus über einen Watchdog-Mechanismus. Wird ein mit CBTC ausgestattetes Fahrzeug im CBTC-Bereich abgestellt und der Stromabnehmer gesenkt, so wird der letzte vom Fahrzeuggerät ermittelte Ort, wenn vorhanden, vom CBTC Fahrzeuggerät gespeichert. Das Fahrzeug verbleibt also auch bei seiner Abstellung lokalisiert. Nach einer definierten Zeit (bspw. 10 min) wird das CBTC-Fahrzeuggerät inklusive des Daten-kommunikationsssystems in den Sleep-Modus versetzt. Hierbei versorgt die Pufferbatterie die zur Realisierung des reduzierten Funktionsumfangs bestehtigten CBTC-Komponenten. Der Spanningspegel der Pufferbatterie wird durch das CBTC-Fahrzeuggerät überwacht. Wird ein Mindest-Spanningspegel dauerhaft untersritten, so wird eine Diagnosemeldung generiert und an die Instandhaltungsorganisation übermittelt. Wenn sich während des Abstellbetriebs innerhalb von 24 Stunden das Fahrzeug ohne Eigenantrieb bewegt, dann wird dies vom CBTC-Fahrzeuggerät bei Wiederanlauf erkannt (cold movement detection). Wenn sich das Fahrzeug nicht bewegt hat, wird der zuletzt gespeicherte Ort vom CBTC-Fahrzeuggerät verwendet. Nach dem Anschalten kann die gültige Ortungsinformation, sowievorhanden, verwendet werden. Wenn keine gültige Ortungsinformation im CBTC-Fahrzeuggerät vorhanden ist, gilt das Fahrzeug al nicht lokalisiert. In thisem Fall muss eine valide Ortsinformation erst durch Überfahren von Transpondern wieder ermittelt werden. Sobald das Fahrzeug wieder aufgerüstet ist und der Stromabnehmer gehoben wurde, wird die Pufferbatterie wieder über das Bordnetz des Fahrzeugs geladen.

# Fahrzeug längerfristig abgestellt (Fahrzeuggerät ohne Spannungsvorsorgung)

In dieser Betriebsart steht das Fahrzeug spanningslos im Betriebshof (No Power in Abb. 4.1). Mittels des Hauptschalters sind die gesamten elektrischen Anlagen des Triebfahrzeugs ausgeschelt. Nachdem das Fahrzeuggerät über eine gewisse Zeit über eine Pufferbatterie gespeist wurde (bspw. 24 Stunden) wird es stromlos geschelt. Da hierdurch auch das CBTC-Fahrzeuggerät spanningslos ist, kann diese keine Überwachungsfunktionen ausfahren. Um das Fahrzeug dennoch gegen unbeabsichtigte Bewegungen zu sichern, müssen hierfür beim Abstellen zusätzliche Bremsen aktiviert werden. Die Federspeicherbremse sichert das Fahrzeug hierbei gegen unbeabsichtigtes Wegrollen. Bei Spanningsverlust des Fahrzeuggeräts gehen auch Informationen über die letzte gültige Betriebsart des Fahrzeuggeräts und die Fahrzeugposition verloren. Zur Sicherstellung der ordnungsgemäßen Funktionalität des CBTC-Fahrzeuggeräts ist bei Wiederkehr der Spanningsversorgung ein Einschaltzyklus mit vollständiger Durchführung von Funktionstests zu durchlaufen.

# 4.1.4 Betriebsarten für Fahrten auf nicht mit CBTC ausgerüsteten Bestandsstrecken

In manchen Projektten muss von einer Bestandstechnik auf CBTC umgerüstet werden. Um dies zu Unterstützung, kann ein spezieller Betriebsmodus für die Doppelausrüstung von Fahrzeugen umgesetzt werden.

# Non Responsible/Other Train Control

Dieser Betriebsmodus erlaubt es, die CBTC-Fahrzeugausrückung voll eingeschaltet zu laßen und der bereits vorhandenen Fahrzeugausrückung des Bestandssystems die Verantwortung für die Zugsicherung zu übergeben. Dies erlaubt eine unverzügliches Fahrzeugseitige Umschaltung auf CBTC-Betrieb beim Passieren einer Migrationsgrenze, bzw. einer Station, die zwischen dem Streckenbereich mit der vorhandenen Ausrüstung und dem neu ausgerüsteten Bereich liegt (Eichner und Uhrig 2021). Dieser Systemübergang kann als fahrende oder als stehende Transition (d. h. im Stillstand in einer Station) ausgeführst sein. Das Zustandsübergangsdiagramm skizziert hier nur ansatzweise die möglichen Übergänge von und nach CBTC. Da auch aus den anderen zuvor dargestellen Betriebszuständen des CBTC-Fahrzeuggeräts Übergänge möglich sein konnen, führen die zusätzlichen Zustandsübergänge zu einer erheblichen Komplexitätszunahme des Systems.

# 4.2 Betriebsartenübergänge in halbautomatischen betriebenen Systemen

Im folgenden Abschnitt wird beschreiben, wie sich die Fahrzeuge in halbautomatisch betriebenen Systemen verhalten. Hierbei wird zunachst die Aufnahme in das manuelle Fahren unter Vollüberwachung des CBTC-Systems, bzw. die Entlassung aus dieser Betriebsart entlassen dargestellt (vgl. Abschn. 4.2.1). Der Wechsel zwischen dem manuellen Fahren unter Vollüberwachung und dem automatischen Fahren unter Vollüberwachung ist in Abschn. 4.2.2 dargestellt. Anschließlich wird dargestellt, wie ein Wechsel zwischen halbautomatischem Betrieb und einer fahrerlosen Kehre (vgl. Abschn. 4.2.3) geschehen kann. Abschn. 4.2.4. stellt die Übergabe von Fahrzeugen an eine automatisierte Betriebsführung im Depot, bzw. eine Übernahme von Fahrzeugen von einer automatisierten Betriebsführung im Depot dar. Darüber hinaus wird beschreiben, wie im Falle von Störungen der Fahrzeug- oder Streckeneinrichtungen Betrieb durchgeführt werden kann (vgl. Abschn. 4.2.4). Abb. 4.1 zeigt eine Übersicht der Betriebsarten mitzwischen diesen bestehenden Übergängen (Transitionen). An dieser Stelle werden nur ausgewählte Transitionen exemplarisch erlautert, da eine umfassende Darstellung den Rahmen这点es Buches sprengen wurde und die herstellerspezifischen Lösungskonzepte voneinander abweichen.

# 4.2.1 Wechsel zwischen Restricted Mode und Supervised Manual Mode

Das CBTC-System muss die räumliche Begrenzung des mit kontinuierlicher bidirektonaler Zugbeeinflussung ausgerüsteten Streckenbereichs kennen. Es muss rechtzeitig vor Aufnahme des Fahrzeugs in den Streckenbereich mit kontinuierlicher bi

direktrionaler Zugbeeinflussung geprüft werden, ob alle Bedingungen für eine Aufnahme in einen Betrieb im wandernden Raumabstand gegeben sind. Damit die Züge einander sicher im wandernden Raumabstand fahren konnen, muss eine spezifische Folge verschiedener Schritte durchlaufen werden. Diese Prozess wird auch als „Sieving" bezeichnet, da hier der englishen Wortbedeutung nach nicht mit CBTC-ausgerüstete Züge sprichwörtlich „ausgesiebt" werden und an der Einfahr in den Streckenbereich gehindert werden.

- Lokalisierung des Fahrzeugs: Als erster Schritt muss das Fahrzeuggerät die Position des Zuges im Netz erkennen und das Fahrzeug eindeutig im Streckenatlas verorten. Hierfür müssen die Komponenten für die Weg- und Geschwindigkeitsmessung einwandfrei arbeiten (Radar, Wegimpulsgeber und Antenne zum Auslesen der streckenseitigen Transponder). Des Weiteren stellt der Zug selbst die Vollständigkeit des Zugverbandes fest. Das Fahrzeug überfährt den ersten Transpondern im Gleis und kann sich im Streckenatlas entsprechend verorten. Das Fahrzeug überfährt anschließend einen zweiten Transponder im Gleis. Heraus kann das Fahrzeug zum einen seine Fahrtrichtung ableiten und zum anderen abgleichen, ob die vom Fahrzeug gemessene Distanz zwischen den beiden Transpondern zu den Werten im Streckenatlas passst.  
- Verbindungsaufbau zum Datenkommunikationssystem: Ist die Lokalisierung des Fahrzeugs erfolgreich verlaufen, wird eine Verbindung zum Datenkommunikationssystem aufgebaut. In this Zusammenhang erfolgt unter anderen auch ein Versionsabgleich zwischen fahrzeug- und streckenseitigem Streckenatlas. Nur wenn die Version des Streckenatlas auf der Streckenseite derjenigen auf der Fahrzeugseite entspricht, damit diese als gemeinsame Referenz für die von den Fahrzeugen an die Streckeneinrichtung versendete Positionsmeldungen verwendet werden, bzw. umgekehrt als gemeinsame Referenz für die von der Streckeneinrichtung an die Fahrzeug übermittelten Fahrbefehle dieren. Ist die Verbindung aufgebaut, sendet das Fahrzeug von nun an regelmäßige seine Positionsmeldungen an die Streckeneinrichtung.  
- Ausschluss nicht-lokalisierter Fahrzeuge: Damit ein Zug endgültig in das Fahren im wandernden Raumabstand aufgenommen werden kann, muss der Fahrer mit dem lokalisierten Fahrzeug den durch Gleisfreimeldesysteme begrenzten Streckenabschnitt mit reduzierter Geschwindigkeit auf Sicht befahren. Sobald sich der Zug in einer geringeren Entfernung zum Ende des Gleisfreimeldeabschnitts als der kürzesten anzunehmenden Länge eines auf der Strecke verkehrenden Zuges befindet, kann ausgeschlossen werden, dass sich noch ein weiterer Zug zwischen dem lokalisierten Zug und dem Ende des Gleisabschnitts in Fahrtrichtigung des Zuges befindet. Durch einen Abgleich des Status der sekundären Gleisfreimeldung mit den Funktogrammen des Zuges erfolgt der wirksame Ausschluss nicht-CBTC-geführter Fahrzeuge.

Die Auslegung des Gleisabschnitts mit Gleisfreimeldung und Transpondern ist auf die im Netz zu erwartenden Zugängen auszulegen. Außen dem muss sichergestellt werden,

dass der Zug früherzeitige eine Funkverbindung aufbauen kann. In Abhängigkeit des Ergebnisse der zuvor geschäderten Prüfungen erfolgen verschiedene Systemreaktionalen:

- Prüfung erfolgreich: Der Fahrzeugführer erhält eine Information auf der Führerstandsanzeige undbekommdtordie aktuellen Führungsgröbenfur das manuelle Führn des Fahrzeugs in Vollüberwachung (Supervised Manual Mode) angezeigt. In thisem Fall ist es nicht erforderlich, dass der Zug anhalt oder seine Geschwindigkeit bei Einfahrnt in den mit kontinuierlicher bidirektionaler Zugbeeinflussung ausgerüsteten Streckenbereich reduziert (es sei dess, dies ist aus anderen betrieblichen Gründen erforderlich).  
- Prüfung nicht erfolgreich: Der Fahrzeugführer erhält eine Information über die Störung des CBTC-Systems. In dieser Fall Übergabe von Fahrzeugen an eine automatisierte Betriebsführung im Depot, bzw. eine Übernahme von Fahrzeugen von einer automatisierten Betriebsführung im Depot dar. Andernfalls muss der Fahrer die geltenden betrieblichen Regel (beispielsweise für das Fahren auf Sicht) beachten. Diese Fahrt auf Sicht wird im Restricted Mode durchgeführt.

Das CBTC-System muss auch für die Entlassung des Fahrzeugs aus dem mit kontinuierlicher bidirektonaler Zugbeeinflussung ausgerüsteten Streckenbereich seine Bereichsgrenzen kennen. Bevor ein Zug den Bereich mit kontinuierlicher bidirektonaler Zugbeeinflussung verlässt, muss der Fahrzeugführer einen visuellen Hinweis auf der Führstandsanzeige erhalten, den dieser in der Regel quittieren muss.

- Der Hinweis auf das Verlassen des ausgerüsteten Streckenbereichs muss früherzeitig und in einer ausreichenden Distanz vor der Bereichsgrenze erfolgen.  
- Sobald der Wechselbekannt ist, wird das CBTC-System den Fahrer informieren, in welcher Automatisierungsstufe der Betrieb hinter der Systemgrenze fortgeführrt werden soll.

Im normalen Betriebsgeshehen sollen es für den Zug nicht erforderlich sein, bei der Entlassung aus dem Betrieb mit dem kontinuierlichen bidirektionalen Zugbeeinflussungsystem seine Geschwindigkeit zu reduzieren, es sei dess, dies ist aus betrieblichen Gründen geboten.

# 4.2.2 Wechsel zwischen Supervised Manual Mode und Automatic Mode

Die Aktivierung des halbautomatischen Fahrens (Automatic Mode) wird dem Fahrer in der Regel durch einen blinkenden Melder im Führerstand angezeigt. Hierbei müssen verschiedene Voraussetzungen gegeben sein.

- Die technischen Voraussetzungen für den Beginn einer Fahrt im halbautomatischen Betrieb sind erfüllt. Das heißt, der Rechner der Automatischen Fahr- und Bremssteuerung

(Automatic Train Operation, ATO) ist verfügbar und Funktionsfähig. Außen dem befindet sich das sichere CBTC-Fahrzeuggerät bereits in der Betriebsart Supervised Manual Mode. Dies bedeutet, dass eine gültige Fahrterlaubnis für das Fahrzeug vorliegt und das Fahrzeug somit Kenntnis über die zulässige Fahrweise hat. Darüber hinaus darf keine Notbremse aktiviert sein und der Fahr- und Bremshebel muss sich in neutraler Stellung befinden.

- Die betrieblichen Voraussetzungen für den Beginn einer Fahrt im halbautomatischen Betrieb sind erfüllt. Dies bedeutet, dass das Fahrzeug einen Fahrbefehl erhalten hat mit dem das Fahrzeug mit seiner gesamten Länge den Bahnsteigverlassen kann, die Türen fest verschlossen sind und die von der Leittechnik vorgegebene Wartezeit abgelaufen ist und der Zug also nicht vorzeitig die Haltestelle verlässt.

Mit Betätigung eines Starttasters übergibt der Fahrer die Verantwortung für die Regelung der Längsbewegung des Fahrzeugs (Bremsen und/oder Beschleunigen) an das Fahrzeuggerät. Das Fahrzeug wechselt dann in die Betriebsart Automatic Mode. Der Fahrer kann durch Auslenken des Fahr- und Bremshebels aus der neutralen Stellung jederzeit die Kontrolle über die Regelung der Längsbewegung des Fahrzeugs (Bremsen und/oder Beschleunigen) zurückerlangen. In thisem Fall wechselt das Fahrzeug vom Automatic Mode in die Betriebsart Supervised Manual Mode.

# 4.2.3 Wechsel zwischen Automatic Mode und Full Automatic Mode bei Kehrfahrten

Der konkrete Ablauf der Übergabe und Übernahme des Fahrzeugs kann auch anhand einer fahrerlosen Kehrfahrt an der Linienendhaltestelle verdutlicht werden (vgl. Abb. 4.2). Bei halbautomatisch betriebenen Strecken, kann eine fahrerlose Kehrfahrt betrieblich sinnvoll sein, da sie die technischen Wendezteiten verstürkt. Außendem erhöht die fahrerlose Kehre den Komfort für den Fahrer (beispielsweise durch Witterungsschutz).

Der Ablauf der fahrerlosen Kehrfahrt im halbautomatischen Betrieb ist in der nachfolgenden Tabelle dargestellt. Hierbei beschreiben die linke Tabellenspalte die Vorgehensweise bei einem Betrieb ohne Bahnsteigtären (Klein 2009). Die rechte Tabellenspalte beschreiben einen möglichen Ablauf für einen Betrieb mit Bahnsteigtären. Dort, wo beide

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/eda1937ab6bd54082c49161256a88237372e5c9a94a59cd62a814d29ef2e9fed.jpg)  
Abb.4.2 Ablauf einer fahrerlosen Kehre im halb automatischen Betrieb

Vorphensweisen einander gleichen, sind die Tabellenspalten miteinander verbunden. Die jeweiligen Spezifika, die voneinander abweichen sind in der jeweiligen Spalte dargestellt.

<table><tr><td>Kehrfahrt bei Betrieb ohne Bahnsteigtären</td><td>Kehrfahrt bei Betrieb mit Bahnsteigtären</td></tr><tr><td colspan="2">Aus der Zuglenkung hereaus wird für den in die Station eingefahrenen Zug die Sicherung des Fahrwegs aus der Station in die Kehranlage angestoßen.</td></tr><tr><td colspan="2">Nach erfolglicher Sicherung des Fahrweges erhält der Fahrer auf der Führerstandsanzeige eine Anforderung zum Start der fahrerlosen Kehrfahrt.</td></tr><tr><td>Der Fahrer verländst das Fahrzeug und Goes zu einem Schlüsselschalter am Ende des Bahnsteigs.</td><td>Der Fahrer verbleibt auf dem Fahrzeug.</td></tr><tr><td>Der Fahrer führt vom Bahnsteigende aus eine Sichteprüfung durch und prüft, ob der Gleisbereich zwischen Bahnsteigende und Kehranlage frei von Hindernissen ist. Er bestätigt dies bestätigt durch Betätigten des Schlüsselschalters am Bahnsteigende. Er erteilt damit einen Abfahrauftrag für den Zug zur Einfahr in die Kehranlage (vgl. Ziffer 1 in Abb. 4.2).</td><td>Der Fahrer erteilt einen Abfahrauftrag für den Zug zur Einfahr in die Kehranlage durch Betätigung einer Quittungstaste am aktiven (vorderen) Führerstand (Ziffer 1). Durch den baulichen Abschluss mit Bahnsteigtären muss nicht mit Hindernissen in der Kehranlage gerechnet werden. Der Fahrer kann nun durch den Führerstand am anderen Ende des Zuges gehen.</td></tr><tr><td colspan="2">Das Fahrzeug führt selbstständig in die Kehranlage ein und kommt dört im gewündsten Gleis vor dem Prellbock zum Stillstand.</td></tr><tr><td colspan="2">Der Zug rüstet automatisch den führenden Führerstand ab, wechselt den Führerstand und rüstet den Führerstand auf der anderen Fahrzeugseite für die Fahrt aus der Kehranlage auf (Ziffer 2).</td></tr><tr><td colspan="2">Aus der Zuglenkung hereaus wird der Führweg für die Ausfahr des Fahrzeugs aus der Kehranlage und die Einfahrt des Zuges in die Station eingestellt und technisch geschichert.</td></tr><tr><td>Der Fahrer wechselt auf den gegenüberliegenden Bahnsteig und Goes zum Schlüsselschalter am Bahnsteiganfang. Der Fahrer führt vom Bahnsteiganfang aus eine Sichteprüfung durch und prüft, ob der Gleisbereich zwischen Bahnsteiganfang und Kehranlage frei von Hindernissen ist (Ziffer 3). Er gekommen dazu angezeigt, dass der Fahrweg technisch gesichert ist.</td><td>Die Streckeneinrichtung erteilt nach erfolglicher Fahrwegsicherung einen Abfahrauftrag für den Zug zur Ausfahr aus der Kehranlage in das Stationsgleis (Ziffer 3). Das Fahrzeug verlässt die Kehranlage selbstständig (Ziffer 4) und fahr selbstständig bis zum Haltepunkt am Bahnsteigende des Stationsgleises (Ziffer 5). Durch den baulichen Abschluss mit Bahnsteigtären muss nicht mit Hindernissen in der Kehranlage und im Stationsgleis gerechnet werden.</td></tr><tr><td colspan="2">Das Fahrzeug führt selbstständig bis zu einer Übergabestelle am Bahnsteiganfang. Der Fahrer führt hierbei eine kontinuierliche Überwachung der Zugbewegung durch. In Notfällen kann der Zug jederzeit vom Fahrer durch Rückstellten des Schlüsselschalterszwangsgebremst werden. Das Fahrzeug kommt an der Übergabestelle am Bahnsteiganfang zum Stillstand (Ziffer 4).</td></tr><tr><td colspan="2">Der Fahrer steigt an der Übergabestelle in das Fahrzeug ein und besetzt den Führerstand. Der Fahrer setzt die Fahrt bis zum Haltepunkt im Ausfahrgleis der Station fort und überwacht den vor ihm liegenden Gleisbereich im Stationsbereich auf Freisein von Hindernissen. Der Fahrer bringt den Zug am Haltepunkt zum Stillstand (Ziffer 5).</td></tr><tr><td colspan="2">Der Fahrer erteilt eine Türffreigabe und überwacht den Fahrgastwechsel. Anschließlich beginnt er die Zugfahr zur{nachsten Station.</td></tr></table>

# 4.2.4 Wechsel zwischen Automatic Mode und Full Automatic Mode im Betriebshof

Betriebshöfe haben lediglich eine betriebliche Funktion, jedoch keine verkehrliche Bedeutung. Die Züge verkehren hier mit geringeren Geschwindigkeiten und sind nicht mit Fahrgästen besetzt. Außen dem sind Betriebshöfe weiträumig abgezäunt und es verkehrt hier nur vom Betreiber sicherheitsunterwiesenes Personal. Die Gefährungsbeherrschung gestaltet sich also in einigen Bereichen des Betriebshofs deutlich einfacher, weshalb sich die Vollautomatisierung der Fahrzeugbewegungen im Betriebshof - auch bei Systemen, die im Fahrgastbetrieb nur halbautomatisch betreiben werden - weltweit zunehmend durchschnitt. Hierbei sind mehrere Betriebsartenübergänge zu untersicken:

- Übernahme des Fahrzeugs vom halbautomatischen Betrieb auf der Strecke in den unbegleiteten fahrerlosen Betrieb im Betriebshof: Der Fahrer führt mit dem Fahrzeug in den Übergabahnsteig an der Grenze des Betriebshofs ein. Der Fahrer verlässt das Fahrzeug und übergibt die vollständige Kontrolle über das Fahrzeug an das CBTC-System. Das Fahrzeug verlässt den Übergabahnsteig und fahrht unbegleitet fahrerlos in den Betriebshof ein.  
- Durchführung unbegleitet fahrerloser Betriebsfahrten des Fahrzeugs im Betriebshof: Das Fahrzeug durchläuft im Betriebshof die Dort geplanten Arbeitsabläufe (beispelseweise Innen- und Außenreinigung, Waschen, Abstellung) und führte diese Stationen unbegleitet fahrerlos an.  
- Übernahme des Fahrzeugs vom unbegleiteten fahrerlosen Betrieb im Betriebshof in das Fahren auf Sicht im Bereich der Fahrzeuginstandhaltung: Im Betriebshof gibt es Betriebsbereiche, in denen mit nicht ausgerüsteten Fahrzeugen gerechnet werden muss. Dies betriff vor allem die Betriebsbereiche der leichten Fahrzeuginstandhaltung und der schweren Fahrzeuginstandhaltung, die insbesondere von defekten Fahrzeugen angesteuert werden. Hier werden die Fahrzeuge an das Instandhaltungspersonal übergeben und von diesen unter Personalverantwortung auf Sicht durch diesen Betriebsbereich gefahren, da hier wegen nicht georteter Fahrzeuge kein umfassender Gefährungsausschluss gegeben ist.  
- Übergabe des Fahrzeugs aus dem Fahren auf Sicht im Bereich der Fahrzeuginstandhaltung in den unbegleiteten fahrerlosen Betrieb im Betriebshof: Nachdem die Fahrzeuge die notwendigen Instandhaltungsmaßnahmen durchlaufen haben, werden sie an einer definierten Übergabestelle wieder an die automatisierte Depotsteuerung übergeben.  
- Übergabe des Fahrzeugs vom unbegleiteten fahrerlosen Betrieb im Betriebshof in den halbautomatischen Betrieb auf der Strecke: An der Grenze des Betriebshofs wird ein Übergabebahnsteig eingerichtet. Das Fahrzeug wird unbegleitet fahrerlos am Übergabebahnsteig bereitgestellt. Der Fahrer betritt das Fahrzeug am Übergabebahnsteig und übernimmt dört die Kontrolle über das Fahrzeug vom CBTC-System. Er verlässt mit dem Fahrzeug unter Fahrverantwortung die Übergabeplattform und nimmt halbautomatisch seine fahrplanmäßige Fahrt auf.

# 4.2.5 Wechsel zwischen Automatic Mode und Restricted Mode bei Störungen

Es ist betrieblich gefordert, auch im Falle einer Störung der CBTC-Einrichtungen oder der Datenkommunikation einen sicheren Zugbetrieb aufrecht zu erhalten. Hierbei ist jeder die Leistungsfähigkeit der Strecke stark eingeschränkt, da nur ein Betrieb mit reduzierten Geschwindigkeiten und durch die großen Abstände der sekundären Gleisfreimeldung entsprechend große Zugfolgezeiten möglich ist. Heraus folgt, dass das CBTC-System so gestaltet werden muss, dass auch im Störungsbetrieb ein{sicherer Betrieb auf der Rückfallebene möglich ist. Der Betreiber stellt möglicherweise Anforderungen an die Leistungsfähigkeit des Betriebs auf der Rückfallebene. Dies muss im Entwurf des Systems berücksichtigt werden. Auch im Störungsbetrieb sollte nach wie vor eine Überwachung der Fahrzeugbewegung möglich sein, ohne sich auf betriebliche Regelungen allein verlassen zu müssen. Dies kann entweder durch das CBTC-System selbst, ein konventionelles Zugsicherungssystem in der Rückfallebene oder eine Kombination aus beiden Systemen erreicht werden.

Für den Störungsbetrieb müssen zwei Arten von Ausfallen betrachtet werden:

- CBTC-Systemausfälle, die alle Züge in einem Streckenbereich betreffen: Für den Fall eines Systemausfalls, der alle mit CBTC ausgerüsteten Züge in einem Streckenbereich umfasst (beispelsweise der Ausfall eines CBTC-Streckengeräts oder der vollständige Ausfall der Datenkommunikation in einem Streckenbereich) müssen die Züge davon weiterhin sicher verkehren (vgl. IEEE 1474.1-2004):  
- gemäß der Vorgaben eines bestehenden (reduzierten) konventionellen Signalsystems,  
- unter strenger Beachtung betrieblicher Regelwerke (gegebenenfalls für das Fahren auf Sicht, welches dann in der Betriebsart Restricted Mode durchgeführt wird),  
- als Kombination aus beiden zuvor genannten Punkten.

In thisem Störungsbetrieb sollenen Überwachungsfunktionen der CBTC-Fahrzeugeinrichtungen weiterhin aktiv sein (wenn dies Sicherheitsforderlich ist). In der Praxis wird hier von den Fahrzeugeinrichtungen die zulässige Maximalgeschwindigkeit der Fahrzeuge im Störungsbetrieb überwacht (Restricted Mode).

- CBTC-Systemausfälle, die einen Zug in allen Streckenbereichen betreften: Es gibt Fälle, in denen ein mit CBTC ausgerüsteter Zug in einem beliebigen Streckenbereich gestört ist. Beispiele hierfür sind Ausfälle des DatenCOMMunikations-systems eines Fahrzeugs oder ein Ausfall der Komponenten für die Weg- und Geschwindigkeitsmessung eines Fahrzeugs. Auch in dieser Störungsfall muss das CBTC-System einen sicheren Betrieb gewährleisten (vgl. IEEE 1474.1-2004):

- gemäß den Vorgaben eines bestehenden (reduzierten) konventionellen Signalsystems,  
- innerhalb der Zuggeschwindigkeit, die vom Antriebsystem bereitgestellt werden kann (das betreffende Fahrzeug wird wegen der dauerhaft anstehenden Zwangsbremse in Folge der technischen Störungen vom Fahrer isoliert und verkehr im Cut Out Mode),

- unter strenger Beachtung betrieblicher Regelwerke für diesen Störungsfall,  
- als Kombination aus den zuvor genannten Punkten.

In thisem Störungsbetrieb sollen Überwachungsfunktionen der CBTC-Streckeneinrichtung und in anderen CBTC-Fahrzeugsystemen in vollem Umfang aufrechtenhalten werden. Abb. 4.3 zeigt ein Beispiel der betrieblichen Auswirkung einer Störung.

Im Störungsbetrieb wird das gestörtte Fahrzeug (vgl. Fahrzeug 2 in Abb. 4.3) die Fahrzeugseitig eingetretene Störung offenbaren. Ein Beispiel hierfür ist die Offenbarung einer Störung des Datenkommunikationssystems nach einer zu definierenden Anzahl erfolgloser Versuche des Verbindungsaufbauz zur CBTC-Streckeneinrichtung. In thisem Fall wird unmittelbar eine Sicherheitsgerichtete Reaktion (Zwangsbremsung) vom Fahrzeuggerät umgesetzt. Das Fahrzeuggerät wechseln in die für den Störungsfall vorgesehene Betriebsart (Emergeny Brake). Durch die Fahrzeugseitige Störung unterbleibt die zyklische Meldung des eigenen Fahrzeugstandortes an die CBTC-Streckeneinrichtung. Für den folgenden Zug 3 muss dazu die letzte gültige übertragene Position des Hecks des vorausfahrenden Zuges 2 als bestehender Gefahrenpunkt angenommen werden. Das Fahrzeug 3 erhält dazu von der CBTC-Streckeneinrichtung eine entsprechende Information und führt auf den Gefahrenpunkt eine Zielbremsung durch. Erst nach Quittierung durch den Fahrer darf Fahrzeug 3 mit einer überwachten geringen Geschwindigkeit weiterfahren, da der vorausliegende Streckenabschnitt durch ein Fahrzeug besetzt sein kann (Restricted Mode). An Bord von Fahrzeug 2 beträgt der Fahrer den Störschalter und führt das Fahrzeug gemäß der geltenden betrieblichen Regeln. Erst wenn das Fahrzeug über die Weichenverbindung 1 der Strecke ausgeschleust wurde und auch das sekundäre Gleisfreimeldesystem ein konsistentes Ergebnis meldet, kann der Betrieb auf der Linie wieder in den Regelbetrieb (manuellesfahren unter Vollüberwachung oder automatisches Fahren unter Vollüberwachung) übergeben.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/24a36ec7c012ae087d6ad2a7cd79c1f7306ed41940b1e7218f1d87d59d2f5e4b.jpg)  
Abb. 4.3 Betriebliche Auswirkung eines gestörten CBTC-Fahrzeuggeräts in Zeit-Weg-Linien-Darstellung

# 4.3 Betriebsartenübergänge in unbegleitet fahrerlos betriebenen Systemen

Im folgenden Abschnitt wird beschrieben, wie sich die Fahrzeuge in unbegleitet fahrerlos betriebenen Systemen verhalten. In Abschn. 4.3.1 wird der Wechsel zwischen Ausschaltzuständen und dem unbegleiteten fahrerlosen Betrieb dargestellt. In Abschn. 4.3.2 wird der Wechsel zwischen Gefahr- und Störzuständen und dem unbegleiteten fahrerlosen Betrieb dargestellt.

# 4.3.1 Wechsel zwischen Ausschaltzuständen und unbegleitetem fahrerlosen Betrieb

Bereits in Abschn. 4.1.3 sind zwei grundlegend entsprechliche Ausschaltzustände beschreiben worden. Diese unterscheiden sich wesentlich durch die Kenntnis der sicheren Position des Zuges auch nach Beendigung der Fahrzeugabstellung. Heraus resultieren entsprechlich leicht- oder aber schwergängige Betriebsverfahren zur Aufnahme eines unbegleiteten fahrerlosen Betriebs:

- Aufnahme des unbegleiteten fahrerlosen Betriebs nach kurzfristiger Abstellung des Fahrzeugs: In dieser Fall ist die Abstelldauer kürzer als die Stützzeit der Pufferbatterie. Das Fahrzeuggerät ist hier nie spanningslos und das Fahrzeug merkt sich seine letzte gültige Position. Die gültige Position ist Grundlage für die Anfrage und Erteilung einer Fahrerlaubnis. Liegt diese vor, kann das Fahrzeug unmittelbar unbegleitet fahrerlos mit den gültigen Höchstgeschwindigkeiten fahren.  
- Aufnahme des unbegleiteten fahrerlosen Betriebs nach langfristiger Abstellung des Fahrzeugs: In thisem Fall hat die Dauer der Fahrzeugabstellung die Stützzeit der Pufferbatterie übersritten und das Fahrzeuggerät wurde nicht mit Spannung versorgt. Das Fahrzeug hat seine sichere Position verloren und kann dazu nicht, wie zuvor im Zusammenhang mit der kurzfristigen Abstellung beschrieben, unmittelbar in den Full Automatic Mode wechseln. Vielmehr muss der Bediener mit seiner Kenntnis des gesamten betrieblichen Kontexts bestätigten, dass der vor dem Fahrzeug liegende Fahrweg frei ist. Er kommandiert das Fahrzeug in den Restricted Mode Driverless. In dieser Betriebsart kann das Fahrzeug eine projektierte Strecke mit reduzierter Geschwindigkeit fahrerlos fahren, bis es den nachsten Transponder überfahren hat und hierdurch ordnungsgemäß lokalisiert ist. Die ordnungsgemäße Lokalisierung ist die Grundlage der Anforderung einer Fahrerlaubnis. Liegt diese auf dem Fahrzeug vor, kann diese mit den gültigen Streckenhöchstgeschwindigkeiten verkehren.

# 4.3.2 Wechsel zwischen Gefahr- und Störzuständen und unbegleitetem fahrerlosen Betrieb

Das Fahrzeug kann aus dem unbegleiteten fahrerlosen Betrieb Heraus Störungen erkennen. Das Fahrzeug lost dann eine Zwangsbremsung aus und Goes in den sicheren Zustand. In thisem Fall erfolgt eine Meldung an die Leitstelle. Das Personal der Leitstelle interpretiert den aktuellen bestehenden betrieblichen Kontext. Es nutzt hierfür die auf der Lupendarstellung der Strecke verfügbare Informationen und greift nach Möglichkeit auf vorhandene Kamerabildner einer möglicherweise an der Fahrzeugfront installierten Kamera zu. Ist der betriebliche Kontext geklärt, wird dem Fahrzeug eine Permissivfahrt im unbegleiteten fahrerlosen Betrieb commandiert. Hierfür sind zwei Szenarien denkbar:

- Das Fahrzeug verliert seine sichere Position durch erhöhten Schlupf oder einen nicht gelesenen Transponder zur Weg- und Geschwindigkeitsmessung. Verliert das Fahrzeug seine sichere Position wird es in den Stillstand gebremst. Das Leitstellenpersonal prüft auf dem Bedienplatz, ob aktuell auf dem geplanten Fahrweg des Zuges mögliche Konfekte mit anderen Zugfahrten bestehen. Kann dies ausgeschlossen werden, wird die Freigabe für die Permissivfahrt erteilt. Das Fahrzeug führt mit der für die Permissivfahrt zugelassenen reduzierten Geschwindigkeit weiter, bis es den nachsten Transponder übergeführt und sich wieder lokalisieren kann. Auf Basis der gültigen Ortsinformation fordert das Fahrzeug eine Fahrterlaubnis an. Diese Fahrerlaubnis wird erteilt und das Fahrzeug setzen seine Fahrt gemäß derarin enthaltenen Geschwindigkeitsvorgaben fort.  
- Das Fahrzeug erkennt ein Objekt im Gleis und bredst in den Stillstand. Um diese unklare betriebliche Situation aufzulosen schaltet das Personal der Leitstelle ein Bild einer an der Front des Zuges installierten Kamera auf und führt eine Sichteprüfung des vor dem Zug liegenden Streckenabschnittes durch. Wird hier kein Objekt erkannt, wird die Permissivfahrt kommandiert. Das Fahrzeug setzen sich in Bewegung und führt mit der für die Permissivfahrt zugelassenen reduzierten Geschwindigkeit eine definierte Zeitspanne, bzw. einen definierten Streckenabschnitt weiter. Lös innerhalb dieser Zeitspanne, bzw. Wegstrecke die Hinderniserkennung (bspw. als Stereokameraystem) nicht erneut aus, wechselt das Fahrzeug von der Permissivfahrt darüber in den unbegleitet fahrerlosen Regelbetrieb.

# Literatur

Eichner D, Uhrig B (2021) Innovationen in CBTC-Anwendungen. Signal + Draht 113(9):34-44  
IEEE 1474.1-2004 IEEE standard for Communications-Based Train Control (CBTC) performance and functional requirements  
Klein R (2009) Die Möglichkeit der fahrerlosen Kehrfahrt bei der Münchner U-Bahn. Signal + Draht 101(10):16-17

# Hauptfunktionen automatischer Zugbeeinflussungssysteme

5

# SN Flashcards

Als Käfer*in diesen Buches können Sie kostenlos unsere Flashcard-App „SN Flashcards" mit Fragen zur Wissenschaftung und zum Lernen von Buch-inhalten nutzen.

1. Gehen Sieitte auf https://flashcards.springernature.com/login und  
2. erstellen Sie ein Benutzerkonto, indem Sie ihre Mailadresse angegeben und ein Password vergehen.  
3. Verwenden Sie den folgenden Link, um Zugang zu Ihr dem SN Flashcards Set zu erhalten:  $\triangleright$  https://sn.pub/sK5mLQ

Sollte der Link fehlen oder nicht Funktionieren, senden Sie unsitte eine E-Mail mit dem Betreff „SN Flashcards“ und dem Buchtitel an customerservice@springernature.com

Automatische Zugbeeinflussungssysteme weisen einenweitreichenden Funktionsumfang auf. Ausgehend von den Anforderungen an die sichere Durchführung des Bahnbetriebes zeigt these Kapitel systematisch die Hauptfunktionen automatischer Zugbeeinflussungssysteme auf. Ausgangspunkt der Darstellung ist die Sicherung der Zugbewegung, welche grundlegende Sicherungsfunktionen umfasst (Abschn. 5.1). Hierauf aufbauend werden weitergehende automatisierungstechnische Funktionen zum Fahren des Fahrzeugs vorgestellt (Abschn. 5.2). Mit der Überwachung der Profilfreiheit (Abschn. 5.3) und der Sicherung des Fahrgastwechsels (Abschn. 5.4) werden weitere für eine höhere Automation erforderliche Funktionen vorgestellt. Auf dem Weg zu einem vollständig fahrerlosen Betrieb

müssen weitere Funktionen technisch realisiert oder zumindest unterstützen werden wie der automatische Zugbetrieb (Abschn. 5.5) sowie die Störfallerkennung und das Störfallmanagement (Abschn. 5.6). Die einzelnen Sicherungsfunktionen werden nachfolgend vorgestellt.

# 5.1 Hauptfunktion Sichern der Zugbewegung

Die Hauptfunktion der Sicherung der Zugbewegungen besteht aus mehreren Oberfunktionen. Diese Oberfunktionen werden nachfolgend dargestellt.

# 5.1.1 Oberfunktion Sichern des Fahrwegs

Ein CBTC-System muss Fahrwegsicherungsfunktionen erfüllen, die denen konventioneller Stellwerkstechnik entsprechen. Hierdurch werden Kollisionen und Entgleisungen von Zügen vermieden. Dies umfasst verschiedene Sicherungsfunktionen zur Beherrschung von Risiken, die zum Entgleisen oder zu Kollisionen von Zügen führen können (Maschek 2018).

Die Entgleisung wird durch die folgenden Maßnahmen verhindert:

- Sicherung der beweglicher Fahrwegelemente (Weichen): Die Weichen werden in die korrekte Endlage gebracht und in diesererverschlossen. Dieser Verschluss muss so lange wirken, wie der betreffende Streckenabschnitt mit der Weiche von einem Zug belegt wird. Um ein Umstellen der Weiche unter einem fahrenden Zug und damit eine Entgleisung zu verhindern, müssen keinem eigentlichen Weichenverschluss (formschlüssige Verriegelung der Weichenzunge in Endlage) weitere Schutzmaßnahmen ergriffen werden (logischer Fahrstraßenverschluss).  
- Schutz vor unstetigen Stellen im Fahrweg: Da ein Schierenbruch zu Entgleisungen von Zügen führen kann, fordern manche Aufsichtsbehörden die technische Realisierung einer Schierenbrucherkennung. Dies kann technisch beispelse durch Gleiststromkreise erfolgen.

Die Kollision wird durch die folgenden Maßnahmen verhindert:

- Schutz vor systemeigenen Fahrzeugen. Dies umfasst geben einem wirsamen Ausschluss von Gegen- und Folgefahrten auch die Vermeidung einer seitlichen Einfahrten eines Zuges über eine Weichenverbindung in einen für einen anderen Zug freigegebenen Fahrweg (so genannte Flankenfahr). Für den Flankenschutz werden in der Planung Flankenschutzeinrichtungen (beispisseweise Schutzweichen, Gleissperren oder Lichtsignale) vorgesehen. In dieser Hinsicht ist insbesondere der Umgang mit nicht ausgerüsteten Fahrzeugen im Netz (beispisseweise Baufahrzeuge) invielen CBTC-

Plan entspricht dem fachtechnisch geprüften Plan

# CERSS Kompetenzzentrum Bahnsicherungstechnik

# Ingenieur- und Forschungsdienstleistungen für Bahnsysteme

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/22aca15097b6b7f71ec5610ee5d027bfd6ae1f470bcf6c05ef27170a997685cf.jpg)

Prozess- und Regelwerksbetrachtung

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/341097396c60b0fa23422ed975ae53708be772d5818580097e8a5a71719247ca.jpg)

Forschung und Entwicklung

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/bf7d05f04911a2da45ec947c5eaeb0185b0245609e28defae46374efcdba7d16.jpg)

Risiko- und Sicherheitsanalysen

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/94d87c4582cddc808754c66cb78bfb5ff7e284a566eb0850af298842d51d94a1.jpg)

Weiterbildung

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/c2e75b1f095af931f634ee234536372c9e20977948a9fa95c0c2f7d610ce267a.jpg)

Inspektionen

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/c785a6e5528294dd7be1b7df6b5ef46f6f7316ce4d479d126aec75e83068ff1e.jpg)

Ausrüstungsprojekten Gegenstand intensiver Diskussionen zwischen CBTC-Systemherstellern und Betreiber. Werden für diese Fahrzeuge keine CBTC-Einrichtungen vorgesehen, müssen betriebliche Ersatzmaßnahmen definiert und im Regelwerk verankert werden.

- Schutz vor externen Objekten. Kunden externe Einrichtungen, wie beisplesiwe Fluktore oder bewegliche Brandschutztore das Lichttraumprofil des Zuges verletzen, müssen diese vor Zulassung einer Zugfahr in ihre korrekte Endlage gebracht und in dieser verschlossen werden. Sie dürfen ihre korrekte Endlage auch nicht während einer frei gegebenen Zugfahr verlassen.  
Schutz vor systemfremden Verkehrsteilnehmern an niveaugleichen Kreuzungen: Ein CBTC-System kann Schnittstellen zu Bahnübergangssicherungseinrichtungen oder Lichtsignalanlagen aufweisen. Auf diese Weise soll sichergestellt werden, dass die Fahrt eines Zuges nur dann zugelassen wird, wenn eine Gefährung durch systemfremde Verkehrsteilnehmer ausgeschlossen wurde. Hierbei müssen Bahnübergänge und Lichtsignalanlagen vor der Befahrung durch den Zug eingeschaltet und vom Zug nach der Befahrung wieder ausgeschelt werden. Die Einschaltung kann bei hinter Bahnsteigen liegenden Lichtsignalanlagen und Bahnübergangen zeitverzögert erfolgen. Räumt ein Zug einen Bahnübergang oder eine Lichtsignalanlage mit mehreren Streckengleisen muss die Sicherung auch dann aufrechterhalten werden, wenn innerhalb eines vorderfinierten Zeitfensters ein Zug in Gegenrichtung den Bahnübergang wieder einschalten wurde. Ziel der Funktion ist es, einen gesicherten Bewegungsraum für die exklusive Durchführung einer spezifischen Zugbewegung zu schaffen (Ritter 2014).

# 5.1.2 Oberfungkion Sichern der Abstandshaltung

CBTC-Systeme unterstützen ein Fahren im wandernden Raumabstand (englisch: Moving Block). Für die Sicherung der Zugfolge muss ein plötzliches Anhalten des vorausfahrenden Zuges angenommen werden. Die relevante Norm spricht hier plakativ von einem „Brick Wall Stop". Dies bedeutet, dass in CBTC-Systemen ein Fahren im absoluten Bremsweg-abstand realisiert wird. Hierbei wird zwischen den Fahrzeugen stets der vollständige Bremsweg mit einem zusätzlichen Sicherheitszuschlag freigehalten (Abb. 5.1). Folgen

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/6d823bd4ffb7dd877f1aa2f2698285bbb6c576c318ce12185c9a5a1f01714155.jpg)  
Abb.5.1 Sicherung des Fahrens im absoluten Bremswegabstand. (Pachl 2016)

nicht CBTC-geführte Züge einander, können diese einander nur im festen Raumabstand (englisch: Fixed Block), das heißt im Abstand der reduzierten Freimeldeabschnittte (so genannte sekundäre Fremeldung) folgen. CBTC-Systeme ermitteln für den Zug den frei-gegebenen Fahrweg und das Ende der Fahrerlaubnis. Das Ende der Fahrerlaubnis ist die restruktivste Bedingung von folgenden:

- Das Ende der Fahrerlaubnis wird vom Zugende eines vorausfahrenden Zuges von dessen Ortungsfunktion unter Berücksichtigung seiner Ortungsungenaugkeit bestimmt.  
- Das Ende der Fahrerlaubnis ergibt sich aus der Grenze eines Fahrwegabschnitts, der von einem nicht mit CBTC ausgerüsteten Zug belegt wird. Die Länge dieseres Fahrwegabschnittes richtet sich nach der Abschnittsteilung des sekundären Gleisfreimeldesystems.  
- Das Ende der Fahrerlaubnis liegt am Ende eines Gleises, bzw. vor einem Prellbock.  
- Das Ende der Fahrerlaubnis ist eine Einfahr in einen Stellwerksbereich, wo die Fahrstraße nicht mit allen Sicherungsbedingungen eingelaufen ist (.,Fahrt auf Entsatzsignal).  
- Das Ende der Fahrerlaubnis ist die Grenze eines Fahrwegabschnitts, für den eine Gegenfahrt zugelassen ist.  
- Das Ende der Fahrerlaubnis ist die Einfahrt in einen Streckenabschnitt mit einem Bahnübergang, der in seiner Funktionseiste gestört ist.  
- Das Ende der Fahrerlaubnis ist die Grenze eines Fahrwegabschnitts mit eingerichteten Befahrbarkeitssperre (beispelseweise bei Baumaßnahmen, Brandereignissen oder abgeschalteter Traktionsstromversorgung).  
- Das Ende der Fahrerlaubnis ist eine Einfahrt in einen Streckenbereich, für den das Fahrzeug nicht geeignet ist. Hierbei kann es sich zum Beispiel um ein unpassendes Lichttraumprofil oder ein ungeeignetes Traktionsstromsystem handeln.

# 5.1.3 Oberfunktion Sichern der Geschwindigkeit und Richtung

Durch die Oberfunktion „Sichern der Geschwindigkeit“ sollen Gefährdungen aus dem Betrieb beherrscht werden:

- Vermeidung von Entgleisungen aufgrund unzeitiger Fahrtaufnahme und unangepasster Geschwindigkeiten beim Befahren des Fahrweges (insbesondere in Weichenbereichen und Gleisbogen).  
- Vermeidung von Kollisionen aufgrund unzeitiger Fahrtaufnahme, bzw. bei Annaherung an sicherungstechnisch erfassbare Hindernisse mit unangepasster Geschwindigkeit.

These Oberfunktion umfasst ihrerseits die Funktion des Erteilens der Fahrerlaubnis unter Berücksichtigung der zulässigen Geschwindigkeiten sowie die Funktion des Überwachens der Fahrbewegung innerhalb der vorgegebenen zulässigen Grenzen.

# Funktion Ereteilen der Fahrerlaubnis unter Berücksichtigung der zulässigen Geschwindigkeiten

Für das Verständnis der Randbedingungen der Erteilung der Fahrerlaubnis muss zunachst der Begriff des statischen Geschwindigkeitsprofils vom Begriff des dynamischen Geschwindigkeitsprofils differenziert werden.

Das staatische Geschwindigkeitsprofil umfasst infrastrukturelle Gegebenheiten (Gleisenigungen und Gefäle), Streckenhöchstgeschwindigkeiten, dauerhafte Geschwindigkeitsinschrankungen, Bahnsteiggleise mit eingeschränkter Durchfahrgeschwindigkeit (beispielsweise Stationsgleise) sowie von den Zuständen der Fahrwegelemente abhängige Geschwindigkeitsvorgaben (zulässige Weichengeschwindigkeiten insbesondere im abzweigenden Strang). Im CBTC-Fahrzeuggerät wird hierbei unter Berücksichtigung fahrzeugseitiger Vorgaben (wie beispielsweise die Zuglänge) ein für das Fahrzeug gültiges individuelles statisches Geschwindigkeitsprofil berechnet (vgl. Abb. 5.2).

Die statischen Geschwindigkeitsvorgaben konnen auf Betreiberwunsch im Sinne des Einrichtens und Rücknehmens vorübergehender Langsamfahrstellen aktiv aus der Leitstelle geändert werden. Aus der Leitstelle Heraus konnen vorübergehende Langsamfahrstellen eingerichtet werden. Befehle zur Einrichtung einer vorübergehenden Langsamfahrstelle gehören zu den sicherheitskritischen Befehlen in CBTC-Systemen. Vor Aktivierung einer vorübergehenden Langsamfahrstelle muss der Bediener in der Leitstelle davon sich kein Zug auf der Strecke befindet. Der Bediener der Leitstelle aktiviert die vorübergehenden Langsamfahrstelle mit einer registrierpflichtigen Bedienhandlung. Er wählt den Befehl zur Einrichtung einer vorübergehenden Langsamfahrstelle aus und quittiert diesen am Bedienplatz innerhalb eines definierten Zeitfensters. Nach der Quittierung wird die neue Geschwindigkeitsbeschränkung an das CBTC-Streckengerät weitergeleitet. Im CBTC-Streckengerät werden die Streckendaten im Streckenatlasactualisiert. Das CBTC-Streckengerät verfolgt das Fahrzeug über die von dieser ausgesendete Postionsmeldungen während der gesamten Fahrt entlang der Strecke. Eine vorübergehende Langsamfahrstelle wird tatsäch dann von der Strecke an das Fahrzeug übertragen, wenn sie für die aktuelle Position des Fahrzeugs relevant wird. Hierfür wird der Fahrbefohl, der

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/78c1905afcc597a9032f312973eec109c47a30ffe955336408b999b44a98f05b.jpg)  
Abb.5.2 Statisches Geschwindigkeitsprofil. (VDV 2014)

normalerweise nur aus einem definierten Wegpunkt entlang der Strecke besteht, um zusätzliche dynamische Informationen ergänzt. Durch den Telegrammverkehr vom Fahrzeug zur Strecke mit Quittierungen wird sichergestellt, dass das Fahrzeug die restruktiven Geschwindigkeitsvorgaben der vorübergehenden Langsamfahrstelle auch tatsächlich einght. Umgekehrt verhält es sich mit der Rücknahme einer vorübergehenden Langsamfahrstelle. Hierbei wird die vorübergehende Langsamfahrstelle aus dem Streckenatlas der Streckeneinrichtung gelöscht. In thisem Fall wird nur noch der reguläre Fahrbefehl von der Strecke zum Fahrzeug übermittelt. Die zusätzlichen vom Fahrzeug zu quittierenden dynamischen Informationen entfallen. Das Fahrzeug kann sich nunmehr die zulässige Fahrweise aus den Angaben des Streckenatlasses im Fahrzeuggerät wieder selbst ermitteltn.

Das dynamische Geschwindigkeitsprofil (Sicherheitsprofil) wird im CBTC-Fahrzeuggerät aus den Angaben des statischen Geschwindigkeitsprofils berechnet (vgl. Abb. 5.3). Es bildet die zulässige Geschwindigkeit des Fahrzeugs an jedem Punkt der Strecke bis zum Ende der aktuell gultigen Fahrerlaubnis ab. Hierbei gewährleistet die Betriebsbremskurve, dass an den jeweiligen Zielpunkten die Dort gultigen Geschwindigkeitsvorgaben eingehalten werden sowie das Fahrzeug am Ende der Fahrterlaubnis zum Stillstand kommt. Das Ende des Fahrterlaubnisbereichs ist somit zugleich der Fußpunkt der Betriebsbremskurve. Die Betriebsbremnsung ist die Bremsung des Fahrzeugs bis zu einer gewünschten Geschwindigkeit oder bis zum Stillstand des Zuges ohne Gefährung der Fahrgäste. Bei der Betriebsbremnsung)dürfen aus Sicherheits- und Komfortgründen für stehende Fahrgäste keine unzulässigen Dauerbremsvorzögerungen auftreten. Die Zwangsbremskurve stellt sicherr, dass das Fahrzeug bei Wahrnehmung einer Gefahr auf jeder Fall

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/f50c09148b603b6e2a15b244b52fde1b0389717b0bbd766af20f8073ded364dc.jpg)  
Abb. 5.3 Überwachung der sicheren Bremskurve in der CBTC-Fahrzeugeinrichtung. (In Anleitung an IEEE 1474.1-2004)

innerhalb der Schutzstrecke zum Stillstand kommt. Bei dieser Bremsung treten erhöhte Verzögerungen auf. Die damit möglich Gefährung der Fahrzeuginsassen wird ausgehen von der Gesamtgefährung hingenommen (TR Bremse 2008). Das Ende der Schutzstrecke ist also der Fußpunkt der Zwangsbremskurve.

In die Berechnung der Bremskurvenschar (bestehend aus Betriebs- und Zwangsbremse) fließen verschiedene Angaben ein wie beispelsweise

- die zulässige Zugänge  
- die vom CBTC-System zugelassene Überschreitung der Maximalgeschwindigkeit,  
- der maximale Geschwindigkeitsmessfehler der CBTC-Fahrzeugeinrichtung,  
- die maximal mögliche Beschleunigung des Zuges zum Zeitpunkt, zu dem eine Geschwindigkeitsüberschreitung durch die CBTC-Fahrzeugeinrichtung festgestellt wird,  
- die schlechteste Reaktionszeit (Ansprechzeit) für die Traktionsabschaltung infolge der Erkennung einer Geschwindigkeitsüberschreitung durch das CBTC-Fahrzeuggerät  
- die Ansprechzeit für die Zwangsbremse nach Feststellung einer Geschwindigkeitsüberschreitung durch das CBTC-Fahrzeuggerät. Die Ansprechzeit ist die Summe aus Verzugs- und Aufbauzeit. Als Verzugszeit (Totzeit) gilt der Zeitabschnitt, der mit der Einleitung einer Änderung der Bremsanforderung (Anlagen oder Lösen) beginnt und endet, wenn  $10\%$  der vorgegebenen Verzögerung erreicht worden sind. Als Aufbauzeit (Schwellzeit) gilt der Zeitabschnitt, der beginnt, wenn  $10\%$  der vorgegebenen Verzögerung erreicht worden sind (Ende der Verzugszeit) und endet, wenn  $90\%$  der vorgegebenen Verzögerung erreicht worden sind (TR Bremse 2008).  
- die garantierte Bremsverzögerung der Betriebsbremse und der Zwangsbremse, sowie  
- Gradienten (insbesondere Gefälle) im Sinne einer notwendigen Verständung der er-forderlichen Bremskraft bei einer Gefällefahrt.

Bei der Berechnung der Bremskurve kommt der vom Fahrzeughersteller garantierten Bremskurve eine große Bedeutung zu. Hierbei mussen die folgenden Aspekte mit berücksichtigt werden:

- die Bremseigenschaften des Fahrzeugs bei ebener Strecke,  
- die Bremseigenschaften des Fahrzeugs bei verschiedenen möglichen Umweltbedingungen,  
- eine Worst-case-Abschätzung von Latenzzeiten im Bremssystem (Zeitversatz der Traktionsabschaltung und Zeitversatz bis zum Wirksamwerden des Zwangsbremseingriffs).  
- die Berücksichtigung der maximalen Fahrzeugbesetzung (plus Schnee- und Eislasten), sowie  
- die Reibungsbedingungen zwischen Rad und Schiene (hohe oder niedrige Reibungs-koeffizienten).

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/53ca7e075204baca70c6ae38f3e08cc79308779fa26c5d379177b3a148838260.jpg)  
Abb. 5.4 Sicherungssprofil bei Geschwindigkeitswechseln auf einen higheren Wert. (VDV 2014)

Am Ende einer Langsamfahrstelle erfolgt ein Geschwindigkeitswechsel auf einen higheren Wert. Hierbei muss das Sicherungssprofil in Abhängigkeit der Zuglänge sicherstellen, dass die niedrigere Geschwindigkeit so lange wirkt, bis der Zugschluss den Bereich der Geschwindigkeitsinschänkung verlassen hat (vgl. Abb. 5.4). Eine solche Geschwindigkeitsinschänkung kann sowohl aus infrastrukturseitig vorgegeben Maximalgeschwindigkeiten (bspw. aus der Trassierung) oder aber aus betrieblichen Randbedingungen resultieren. Ein Beispiel für eine aus betrieblichen Randbedingungen resultierende reduzierte Geschwindigkeit ist eine Zugahrt in einer Betriebsart für einen Gefahrenzustand (vgl. Abb. 5.4).

Das CBTC-System muss für die Bestimmung des Fahrprofils seinen aktuellen Ort, seine aktuelle Geschwindigkeit sowie seine eigene Fahrtrichtung kennen. Hierbei muss die Ortung eines CBTC-Zuges sicher und GENU (das heißt in ausreichender Auflösung) sowohl die Spitze als auch das Ende des Zuges bestimmen. Die Bestimmung der Ortungs-information muss sich selbst initialisieren. Das bedeutet, dass ein Fahrzeug mit Eintritt in den CBTC-Bereich selbst seine Position ermitteln muss. Gleiches gilt bei Wiederherstellung der Funktion nach einem Ausfall. Hierbei muss das Fahrzeug seine eigene Position und seine eigene Länge ohne manuelle Eingabe ermitteln können.

# Funktion Überwachen der Fahrzeugbewegung innerhalb der vorgegebenen zulässigen Grenzen

An jedem Ort ist die durch das Sicherungssprofil vorgegebene erlaubte Fahrgeschwindigkeit zu überwachen (Ritter 2014). Auch soll durch eine Rückrollüberwachung eine unbeabsichtigte Bewegung des Fahrzeugs entgegen der zulässigen Fahrrichtung unterbunden werden. Für die Rückrollüberwachung wird eine maximal zulässige Wegstrecke im Fahrzeuggerät konfiguriert. Rollt das Fahrzeug stärker als zulässig darüber, erfolgt eine Zwangsbremsung an Bord des Fahrzeugs. Außen dem sendet das CBTC-Fahrzeuggerät einen Alarm an die Leitstelle, sodass das Betriebspersonal in der Leitstelle diese Information interpretieren kann und ggf. sicherheitsgerichtet in den Betrieb eingreifen kann.

Die Funktion der Überwachung der Fahrzeugbewegung innerhalb der vorgegebenen zulässigen Grenzen umfasst die folgenden Aspekte:

- Bestimmen der aktuellen Geschwindigkeit und Fahrtrichtung des Zuges,  
- Bestimmen des eigenen Fahrzeugortes relativ zum Sicherungssprofil,  
- Vergleich der aktuellen Geschwindigkeit und Fahrtrichtung mit den Vorgaben des Sicherungsprofils,  
- Anfordern der Zwangsbremsung bei Abweichung von zulässiger Geschwindigkeit und Fahrgrichtung, sowie gegebenenfalls die  
- Rücknahme des Zwangsbremskommandoes nach Unterschieden der maximal zulässigen Geschwindigkeit

Zur Überwachung der zulässigen Geschwindigkeit des Zuges ist die Ortung des Fahrzeugs elementar. Das CBTC-System muss Messungenaugkeiten der Ortung und Geschwindigkeitsmessung beherrschen. Hierbei müssen einerseits zufällige Messfehler korrigiert werden und systematische Messfehler vermieden werden:

- Zufällige Messfehler: Beruht das Funktionsprinzip der Weg- und Geschwindigkeitsmessung ausschließlich auf Drehzahlensoren, so führt mit zunehmender Geschwindigkeit der Schlupf (das heißt das Schleudern oder Gleiten) bei angetriebenen oder gebremsten Achem von Zügen zu einem zufälligen Messfehler. Auch bei vom Rad-Schiene-Kontakt unabhängigen Sensorprinzipien konnen sich sporadisch wirkende Umwelterinflüsse negativ auf das Messergebnis auswirken. Bei Doppler Radarsensoren kann eine Vereisung des Radarsensors oder eine eingeschränkte Reflektion durch Wasser im Gleis die gemessene Relativgeschwindigkeit über Grund verfüllschen.  
- Systematische Messfehler: Durch den Verschleib der Radreifen oder einen Radsatzwechsel kommt es bei einer auf Drehzahlensoren basierenden Weg- und Geschwindigkeitsmessung zwangslaufig zu Abweichungen des wahren Wertes vom gesessenen Wert. Wird hier der Raddurchmesser in der Software des Fahrzeuggeräts nicht korrigiert, werden die gezahlten Radumdrehungen systematisch mit dem falschen Radumfang multipliziert. Auch bei vom Rad-Schiene-Kontaktakt unabhängige Sensorprinzipien können sich systematische Fehler negativ auf das Messergebnis auswirken. Erfolgt die Montage eines Doppler Radarsensors fehlerhaft (bspw. verdrecht) oder wird ein fehlerhafter Kalibrierungswert verwendet, ist die vom Sensor gesessene Relativgeschwindigkeit systematisch fehlerbehafelt.

Um die zuvor genannten Aspekte zu beherrschen und eine möglichst hohe Ortungs-genaigung zu erhalten, werden einsersects mehrere entsprechliche Sensorprinzipien in Odometrieplattformen miteinander verknüpf (Diversität). Hierdurch gleichen sich die Stärken und Schwächen der innerhalb einer Odometrieplattform verwendeten Sensoren gegenüber aus. Ebenso ergeben sich für die Instandhaltung möglicherweise An

forderungen an eine regelmäßige Kalibration, sofern dies nicht durch geeignete Algorithmen seitens des CBTC-Systems kompensiert wird.

Die Hersteller verwenden für ihre CBTC-Systeme entsprechliche Komponenten für die Weg- und Geschwindigkeitsmessung. Diese werden nachfolgend vorgestellt.

# Drehzahlsensoren

Alle CBTC-Systeme verwenden an mindestens zwei unterschiedlichen nicht angetriebenen und/oder gebremsten Achsen des Fahrzeugs montierte Drehzahlensoren. Diese werden oftmals an den Achslagern montiert. Drehzahlensoren verfügen unabhängig von ihrem jeweiligen Wirkprinzip über zwei Sensorelemente, die zwei phasenverschobene Sensor-signale erzeugen. Aus der Phasenverschiebung der Sensorsignale lässt sich die Fahrtrichtung (FR) des Zuges bestimmen. Jeder Sensor erzeugt eine Anzahl von Wegimpulsen pro Messzyklus (WI). Gleichzeitig ist die Anzahl der Wegimpulse pro Radumdrehung besteht (W). Ist der im Fahrzeugrechner eingebene Raddurchmesser besteht  $(\mathrm{d_r})$ , kann hieraus die in einem Zeitinkrement (t) der zurückgelegte Teilweg mit dem folgenden Zusammenhang ermittelt werden:

$$
S _ {\text {T e i l w e g}} (t) = F R \times \pi \times d _ {r} \times \frac {W I (t)}{W} \tag {5.1}
$$

Für die Geschwindigkeit gilt entsprechend:

$$
v (t) = \frac {\pi \times d _ {r}}{\ddot {\mathrm {A}} t} \tag {5.2}
$$

Grundsatzlich können für Drehzahlensoren zwei unterschiedliche Wirkprinzipien unterschieden werden:

- Drehzahlensoren tasten ein ferromagnetisches Messzahnrad berührungslos ab. Die Sensoren zahlen auf diese Weise die Anzahl der Achsumdrehungen in einem bestimmten Zeitinterval (vgl. Abb. 5.5a auf der linken Seite).  
- Drehzahlensoren arbeiten als optisches System im Infrarotbereich. Der kontinuierliche Lichtstrom einer Sendediode wird durch eine rotierende Lochscheibe unterbrochen. Der Empfangstransistor erfasst den pulsierenden Lichtstrom und erzeugt eine Frequenz proportional zur Drehzahl der Achse (vgl. Abb. 5.5b auf der linken Seite).

Für eine genaue Weg- und Geschwindigkeitsmessung stellt der Schlupf, das heißt das bei Schierenfahrzeugen prinzipbedingte Gleiten und Schleudern von Stahlrädern auf Schienen aus Stahl eine Herausforderung dar. Eine ausschließlich auf Messungen an den Radsätzen basierende Weg- und Geschwindigkeitsmessung wird folglich bei higheren Geschwindigkeiten wegen des Schlupfes zunehmend ungenau. Allerdings kann diese Problemstellung durch zusätzliche technische Maßnahmen beherrscht werden. Hierfür kann beispiselsweise ein zusätzlicher Drehzahlsensor zur Messung der Motordrehzahl installiert werden. Dies ermöglich durch die Berücksichtigung derbekannten Übersetzung

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/35e5e376f16c08b94fa3e3aca86efd345f57ac3c54fa241febb1283e7389f099.jpg)  
a  
Anordnung der Drehzahlensoren am Messzahnrad

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/034fab15448b88c3ceba0b075ffcf9e5b8131b00e8df3dba12353e2341c99046.jpg)  
Montage des Drehzahl sensors am Drehgestell

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/410c9c043a07672b7fb220dd7742a6b1e995769df63c859ad85140240f959984.jpg)  
Abb. 5.5a Verwendung von Drehzahlensoren mit ferromagnetischen Messprinzip für die Weg- und Geschwindigkeitsmessung. (Quelle: Lenord, Bauer & Co. GmbH)  
b  
Funktionsprinzip eines optischen Drehzahlensensors  
Abb. 5.5b Verwendung von Drehzahlensoren mit fotoelektrischem Wirkprinzip für die Weg- und Geschwindigkeitsmessung. (Quelle: HASLERRAIL AG)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/30d73cdc47326d86ef832cc8726a5ca55eb70a7af5cd827af9452dd3ec1fa33b.jpg)  
Montage des Drehzahl sensors am Achslagerdeckel

des Getriebes die Berechnung des theoretisch zurückgelegten Weges, bzw. die korrespondierende Geschwindigkeit des Zuges. Durch den Vergleich mit den auf Grundlage der an der Achse montierten Drehzahlensoren ermittelten Weg- und Geschwindigkeitsinformationen, bzw. den hieraus abgeleiteten Differenzen kann die Weg- und Geschwindigkeitsmessung um den Anteil des Schlupfes korrigiert werden.

# Doppler Radarsensoren

Um unabhängig von der Radumdrehung die Geschwindigkeit eines Schienenfahrzeuges zu messen, werden zusätzliche Sensorprinzipien zur Distan- und Geschwindigkeitsmessung der Züge verwendet. Unter dem Fahrzeug installierte Radarsensoren strahlen in das Gleisbett. Das Sensorprinzip Goes davon aus, dass die ausgesendete Radarstrahlung durch die raue Oberfläche des Gleisbettes teilweise wieder zu einem Empfänger reflektiert

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/a093cb21bf9e4d5f9fd1bb38000a6ec54af48c623affd383c4f107cd5c72dd00.jpg)  
zweikanaliger Doppler Radarsensor

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/a8d95b12feb727adde6411ce7fde9d86be971d4409cce250db5ff3a9c65cc893.jpg)  
Radarsensor mit integrierter Schutzhaube für höhere Verfügbarkeit bei winterlichen Bedingungen  
Abb. 5.6 Verwendung von Doppler Radarsensoren für die Weg- und Geschwindigkeitsmessung. (Quelle: Deuta-Werke GmbH)

wird. Zur Auswertung wird die empfangene Frequenz des vom Sensor ausgesendeten Signals mit der Frenz des empfangenen Signals verglichen. Durch den Dopplereffekt kann aus dem Betrag der beobachteten Frequenzverschiebung die Relativgeschwindigkeit des Wagenkastens über Grund ermittelt werden. Aus dem Vorzeichen der Frenzverschreibung kann die Fahrrichtung des Fahrzeugs abgeleitet werden. Abb. 5.6 zeigt ein Beispiel für in der Praxis eingesetzte Doppler Radarsensoren. Für einen Einsatz bei winterlichen Bedingungen kann der Radarsensor um eine Schneeschutzhaube ergänzt werden.

# Beschleunigungssensoren

Mit eindimensionalen Beschleunigungssensoren lässt sich die Änderung der Geschwindigkeit des Fahrzeugs in der Ausrichtung des Beschleunigungssensors bestimmen. Diese Sensoren sind vom Rad-Schiene-Kontakt unabhängig und konnen die prinzipbedingten Nachteile von Wegimpulsgebern dazu ausgleichen.

# Ortsbaken

Allen CBTC-Systemen ist kein, dass sie zusätzlich zu den verschiedene Sensor-systemen in regelmäßigen Abständen ihre Positionen an ortsfesten Synchronisations-punkten korrigieren. Hierfür werden in regelmäßigen Abständen Ortsbaken im Gleis verlegt. Teilweise adaptieren die Hersteller hierfür die im Rahmen des einheitlichen europäischen Zugsicherungssystems (European Train Control System, ETCS) standardisierte Eurobalisen (vgl. Abb. 5.7). Diese werden von den Fahrzeugen beim Überfahrens ausgegeben.

Die Ortsbaken erfüllen mehrere Funktionen:

- Erhöhung der Ortungsgenauigkeit. Abb. 5.8 zeigt, wie in Abhängigkeit der vom Fahrzeug zurückgelegten Strecke durch den Schlupf (Schleudern und Gleiten) die UNSicherheit der Weg- und Geschwindigkeitsmessung (Abweichen von gemessener Entfernung zu tatsächlich zurückgelegter Entfernung) zunimmt. Dieses Konfidenzinterval wird bei Überfahrt einer Ortsbake reduziert. Hierbei ist allerdings keine komplette Reduktion der UNSicherheit zu erwarten. Dies liegt zum einen in der realisierbaren Verlegegenauigkeit

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/ebb1c537b17aab5d5873a8f8ff2c4e0471a9f6c65c7fc9124da0978d96dffcab.jpg)  
Montage des Transponders im Gleis

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/c2800aec6da798812dfc49657c682a73332e707b54e8425a22edb2f27c766c01.jpg)  
Montage der Fahrzeugantenne unter dem Fahrzeug

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/4c9f0b0c252168462f4467ef41b744d7275a46c325e718e35b1926d69ad56361.jpg)  
Abb. 5.7 Montage der Transponder im Testgleis der Hamburger Hochbahn AG und unter dem Fahrzeug vom Typ DT5 der Hamburger Hochbahn AG  
Abb. 5.8 Beherrschung der Ortungsungenauigkeit durch regelmäßige Synchronisation der Weg- und Geschwindigkeitsinformationen an festen Orts Marken

der Ortsbake im Gleis begründet. Zum anderen finding physikalisch bedingt die Übertragung der Datenpakete nicht an einem diskreten Punktstatt. Vielmehr wird die passive Ortsmake im Gleis schon vor Überfahrt durch die Antenne (durch die kegelförmige Wellenausbreitung) aktiviert und sendet Daten an das Fahrzeug. Soll also eine hohe Ortungsgenaugkeit erreicht werden (beispelsweise für das positionsgenaue Halten an Bahnsteigtüren im Stationsbereich), werden diese Synchronisationspunkte in entsprechend kurzen Abständen verlegt und bei Bedarf auch noch hoch genau eingemessen.

- Die zweite zentrale Funktion der Ortsbaken ist die korrekte Positionierung des Zuges im Gleis. Der Streckenatlas im CBTC Strecken- und Fahrzeuggerät enthalt jeweils die

Ortsbaken mit ihren eindeutigen Identifikationsnummern als Referenzpunkte, quasi als gemeinsames Koordinatensystem. Dies ist für den Fall erforderlich, dass der Zug sich nicht korrekt positionieren kann. Dies ist insbesondere dann der Fall, wenn beispelseweise das Datenkommunikationssystem nicht verfügbar ist oder aus anderen technischen Gründen keine korrekte Endlage der Weiche gebildet und an das Fahrzeug übertragen werden kann. In thisem Fall sind die regelmäßig im Gleis verlegten Transponder für eine korrekte Lokalisierung des Fahrzeugs wesentlich. Befährt zum Beispiel das Fahrzeug eine Weiche mit unbekanfter Endlage von der Spitze her, verliert es seine eindeutige Positionierung. Das Fahrzeug weiß nicht, auf welchem der beiden Richtungsgleise es sich befindet. Der Zug erhält jedoch wieder eine eindeutige Position-information durch die Überfahrt von Transpondern hinter der Weiche. Er kann Daher im Streckenatlas auf den korreksen Weichenstrang positioniert werden und kann seine aktuelle Position wieder in Bezug auf die letzte überfahrende Ortsmarke bestimmten und an die CBTC-Streckeneinrichtung melden.

# 5.2 Hauptfunktion Fahren des Fahrzeugs

Das Fahren des Fahrzeugs besteht aus den Oberfunktionen des Bestimmens des Fahrprofils sowie des Steuerns der Züge in Abhängigkeit des Fahrprofils. Diese Hauptfunktion setzt die zuvor beschriebene Hauptfunktion des Sicherns der Zugbewegung voraus.

# 5.2.1 Oberfunktion Bestimmendes Fahrprofils

Die Leittechnik (Automatic Train Supervision, ATS) kennt den aktuellen Betriebszustand nicht nur eines Fahrzeugs, sondern des Gesamtsystems mit all seinen Fahrzeugen. Die Leittechnik kanniharere optimale Regelung des Betriebs auf einer Linie unterstützen. Auf der übergeordneten Betrachtungsebene einer ganzen Linie kann die Leittechnik durch Vorgabe zeitlich versetzer Abfahrtszeiten in den Stationen beispelsweise die Anzahl gleichzeitig anfahrender Züge in einem Speiseabschnitt der Traktionsstromversorgung begrenzen, um die Lastspitze zu senken (Eichner und Uhrig 2021). Ein weiterer Anwendungsfall auf der übergeordneten Betrachtungsebene ist die Abstimmung der Ankunfts- und Abfahrzeiten von Fahrzeugen auf einer Linie zueinander, so dass die bei der Bremsung durch Rekuperation zurückgewonnene elektrische Energie eines Fahrzeug von einem anderen aus der Station ausfahrenden Fahrzeug genutzt werden kann (Eichner und Uhrig 2021). Dem einzelnen Fahrzeug gibt die Leittechnik somit übergeordnete Strategieentscheidungen zur optimalen Fahrweise vor. Innerhalb把这些 von übergeordneter Ebene gesetzten Rahmens konnen die einzelnen Fahrzeuge ihr eigenes Fahrprofil optimieren. Grundsätzlich bestehen die Strategieoptionen einer energieoptimalen oder einer zeit-optimalen Fahrweise, welche nachfolgend vorgestellt werden:

# Zeitoptimale Fahrzeugtrajektorie

Ausgangspunkt für die Berechnung einer energieoptimalen Fahrzeugtrajektorie ist die zeitoptimale Trajektorie (Spitzfahrttrajektorie) des Triebfahrzeugs. Um die Bewegungsbahn des Triebfahrzeugs auf dem kompletten Fahrweg vorausschauend berechnen zu konnen, besteht das ATO-Fahrzeuggerät die folgenden Angaben, die von der Leittechnik vorgegeben werden (Fahrtziel und Streckenführung bis zum Fahrtziel sowie die Richtfahrzeit bis zum Fahrtziel), die auf dem Triebfahrzeug hinterlegt sind (die im Streckenatlas enthaltene Streckentopologie sowie die im Fahrzeuggerät projektierten Fahrzeugparameter wie Masse, Fahrzeuglänge, Fahrwiderstand und Zugkraftkennlinien) sowie vom Triebfahrzeug selbst ermittelt werden (Fahrprofildaten gekennzeichnet durch Grenzgeschwindigkeiten, Langsamfahrstellen und Bremsverzögerungen sowie der Fahrzeugposition in Bezug auf das Streckennetz und die aktuelle Fahrzeuggeschwindigkeit). Beivorliegenden Versätungen kann die Fahrzeit des Zuges durch eine gezielte Beeinflussung der Fahrzeiten zwischen den Stationen (maximale Beschleunigung, maximale Fahrgeschwindigkeit und maximale Betriebsbremsverzögerung) sowie eine Variation der Haltestellenaufenthalszeiten bis hin zu der Vorgabe eines Haltentfalls in ausgewählten Stationen beeinfusst werden. Die Vorgaben der Leittechnik werden dem Fahrzeugfuhrer angezeigt (bei fahrerunterstützenden Systemen) oder von der automatisierungstechnischen Komponente (Automatic Train Operation, ATO) selbstständig in Befehle für die Fahrzeugsteuerung umgesetzt.

Die Umsetzung der zeitoptimalen Fahrstrategie ist in Abb. 5.9 dargestellt. Hierbei zeigt die obere Hälfte des Schaubildes eine Fahrschaulmie (Darstellung der zulässigen Geschwindigkeit über den Streckenverlauf). Ein maschineller Regler kann der durchbezogenen Linie (Geschwindigkeitsvorgabe) optimal folgen. Ein menschlicher Fahrzeugführer wird in der Regel unterhalb der zulässigen Geschwindigkeit bleiben und das Fahrzeug mittels des Fahr- und Bremshebels im Führerstand mit einer charakteristischen „Sägezahnbewegung" knapp unterhalb der Sollvorgabe führen. Mit dieser Fahrschaulmie korrespondiert das unter stehende Zeit-Weg-Linien-Diagramm. Hierbei wird deutlich, dass mit einer maschinellen Regelung eine Fahrzeitverkürzung möglich ist, da Zeitverluste durch Fahrzeitschwankungen eliminiert werden.

# Energieoptimale Fahrzeugtrajektorie

Gibt es die Betriebssituation her, kann auch eine energiaoptimale Fahrweise umgesetzt werden. Aus seinem Streckenatlas kennt das CBTC-System die Topologie des vor dem Fahrzeug liegenden Streckenabschnitts (Weichenradien, Neigung/Gefalle und die Position der Bahnsteige). Mithilfe dieser Daten in Kombination mit der aktuellen Geschwindigkeit, der eigenen Position und den von der Leittechnik über die Kommunikationsverbindung empfangenen Online-Fahrplandaten wird für das Fahrzeug eine energiaoptimale Fahrzeugträjektorie unter Einhaltung der vorgegebenen Fahrzeit ermittelt (Rahn 2011). Grundsatzlich müssen für die energiaoptimale Fahrzeugträjektorie mehrere Aspekte betrachtet werden:

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/dde58f28e9dace95917bd117c2c9adc353bb6b9045307de468ccefe69d2b08f1.jpg)  
Abb.5.9 Umsetzung einer zeitoptimalen Fahrweise in der ATO

- Variation von Antriebsabschlusspunkt und Beharrungsgeschwindigkeit: Beim Vorhandsein von Fahrzeitreserven erfolgt eine Reduzierung der Beharrungsgeschwindigkeit des Fahrzeugs. Da die konkreten Umschaltpunkte zwischen den zwei Phasen „Anfahren und Beharrungsfahrt" und „Beharrungsfahrt und Auslauf" nicht vorgegeben sind, müssen diese durch ein Optimierungsverfahren aus der Spitzfahrtrajektorie abgeleitet werden. Dies erfolgt für die Umschaltung von Anfahren auf Beharrungsfahrt durch eine Variation der Beharrungsgeschwindigkeit. Für die Umschaltung von Beharrungsfahrt auf Auslauf erfolgt dies durch eine Variation des Antriebsabschlusspunktes (Brückner und Isailovski 2010).  
- Mit Hilfe des Verfahrens „Auslauf vor Bremsung“ erfolgt eine Energieeinsparung des Triebfahrzeugs durch Nutzung der vom Streckenprofil abhängigen Hangabtriebskraft. Das Verfahren wird in Streckenabschnitten angewendet, in denen entsprechend des vorgegebenen Fahrprofils gebremst werden muss und der Verlauf der Fahrwiderstandskräfte innerhalb dieser Streckenabschnittte zum Abbremsen des Fahrzeugs (Fahrzeug befährt einen Abschnitt mit Steigung) führt oder die Beharrungsgeschwindigkeit unterhalb der entsprechenden Grenzgeschwindigkeit liegt und der Verlauf der Fahrwiderstandskräfte innerhalb dieser Streckenabschnittte zu einer Beschleunigung des Fahrzeugs führt (Fahrzeug befährt einen Gefällabschnitt). In diesen Streckenabschnitten ist der Antrieb faktisch abgeschelt. Das Triebfahrzeug nimmt keine Energie aus dem

Stromnetz auf. Für das weitere Fortbewegen des Triebfahrzeugs wird entweder seine kinetische Energie oder die über das bereits streckenprofil vorhandene potenzielle Energie genutzt (Brückner und Isailovski 2010).

- Neuberechnung bei veränderten Ausgangsbedingungen: Eine Neuberechnung der Fahrzeugträkterie erfolgt, wenn sich das Fahrprofil im Vergleich zur Ausgangslage soändert, dass es mit der aktuellen Sollträkterie kollidiert oder so viel freizügiger ist, dass zusätzliche Energiesparpotenziale genutzt werden konnen. Auch wenn im Falle von Betriebsstörungen das Triebfahrzeug der vorgegebenen optimalen Sollträkterie nicht folgen kann, erfolgt eine Neuberechnung (Brückner und Isailovski 2010).

Die Umsetzung der energieoptimalen Fahrstrategie ist in Abb. 5.10 auf der linken Seite dargestellt. Die Fahrschaulinie zeigt in thisem Fall, wie das Fahrzeug nach Erreichen der Maximalgeschwindigkeit (Cruising) die Traktionsleistung abschaltet und ausrollt (Coasting). Das Fahrzeug wird dann bei Erreichen der Haltestelle auf die exakte Halte-positionzielgebremst. Im unteren Bereich des Schaubildes wird in der Zeit-Weg-Linien-Darstellung deutlich, dass Fahrplanreserven durch das Coasting in Energieeinsparungen gewandelt werden konnen. Algorithmmen zur energiesparenden Fahrweise konnen bei Fahrplanreserven von  $5\%$  den Traktionsenergieverbrauch um etwa  $20\%$  reduzieren. Bei Vorgabe großer Fahrzeitreserven  $(20\%)$  sind Einsparungen von teilweise soccer  $50\%$  möglich (Brückner und Isailovski 2010). Dank reduzierter Geschwindigkeit in den Coasting-Phasen (Rollen) ist auch ein reduzierter Verschleib der Bremsen eine willkommen Nebenkwirkung (Rahn 2011). Auf der rechten Seite von Abb. 5.10 ist eine alternative Fahrstrategie dargestellt. Hier kann nach Abschluss des Fahrgastwechsels die Haltestellenaufenthaltszeit verkurzt werden. Um die geplante Ankunftszeit in der nachsten Station nicht zu gefährden, muss der Zug nicht so stark beschleunigen und kann früher ausrollen.

# 5.2.2 Oberfungtion Steuern der Züge in Abhängigkeit des Fahrprofils

Ein Schierenverkehrssystem kann als geschlossener Regelkreis aufgefasst werden. Ein Regelkreis besteht hierbei aus der geschlossenen Wirkkette von Messglied, Regler, Stellglied und Regelstrecke (vgl. Abb. 5.11). Dem Regler wird von außen eine Führungsgröbe vorgegeben. Gleichzeitig wirken auf die Regelstrecke externe Störungsgrößen. Regelkreise können auch vermascht werden. Abb. 5.11 zeigt mehrere Regelkreise, die auf eine gemeinsame Regelstrecke wirken.

Das Antriebs- und Bremssystem eines Schienenfahrzeugs folgt dem Regelkreisprinzip. Über Sensoren des Schienenfahrzeugs werden Weg- und Geschwindigkeitsinformationen erfasst (Messglied). Das Steuergerät des Zuges verarbeitet die erfassten Messgroßen und erhält darüber hinaus übergeordnete Führungsgrößen vom Teilsystem Automatic Train Operation (ATO). Heraus werden die Bremssysteme des Fahrzeugs und die Antriebe an-gesteuert (Stellglieder), um das Fahrzeug entsprechend der Vorgaben der Trajektorie der ATO über die Strecke zu bewegen (Regelstrecke). Dies ist in Abb. 5.11 als unterste Ebene der mehrstufigen Regelkreisstruktur dargestellt.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/39d4e388a5494842b680d4415b71590540b657179a63b921799322c427f3f34f.jpg)  
Abb. 5.10 Umsetzung einer energieoptimalen Fahrweise in der ATO

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/991e35fdf209d8b7fb6cf76a9760ce7f153361526db4c3b8ffb1dc61bd45d0e7.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/2c2d4c624c902c46f888f10d44c87aa8394d9c5a02a5e59da2d7a9b229e925fe.jpg)  
Abb.5.11 Steuern von Zügen als vermasche Regelkreisstruktur

Das Teilsystem Automatic Train Operation realisiert ebenfalls einen eigenen Regelkreis. Dieser ist dem Regelkreis der Triebfahrzeugregelung überlagert. Die von den Sensoren des Fahrzeugs erfassten Weg- und Geschwindigkeitsinformationen (Messglieder) werden im ATO-Fahrzeuggerät des Fahrzeugs mit übergeordneten Führungsgrößen aus der Dispositionsebene verknüpf (Regeleinrichtung). Die Fahrzeugträjektorie entstehen aus einer Wahl des in der aktuellen betrieblichen Situation optimalen Antriebsabschaltpunktes sowie der Beherrungsgeschwindigkeit des Fahrzeugs. Die ermittelte Trajektorie wird als Vorgabewert an das Steuergerät des Zuges übergeben. Über das Triebfahrzeug wirkt die ATO-Komponente mittelbar auf die Regelstrecke.

In der Leitstelle ist ein weiterer Regelkreis implementiert (Automatic Train Supervision, ATS). Dieser Regelkreis ist dem ATO-Teilsystem eines Fahrzeugs überlagert. Die CBTC-Streckeneinrichtung sendet die von den Fahrzeugen empfangenen Orts-informationen an die in den leittechnischen Systemen der Leitstelle implementierte Zuglaufverfolgung (Messglied). In der Leittechnik wird die aktuelle Betriebslage mit dem

Fahrplan verglichen (Regeleinrichtung). Erkannte Abweichungen resultieren in Dispositionsentscheidungen wie beispelssweise eine Verkürzung von Haltezeiten an den Stationen, ein Entfall von Stationshalten oder der Wahl alternative Laufwege des Fahrzeugs (Stellglied). Informationen über den disponierten Fahrplan werden per Funk an das Fahrzeug übermittelt. Gleichzeitig werden Stellbefehle an die Aktoren im Gleis (Weichen und gegebenenfalls auch reduzierte ortsfeste Signale) ausgegeben, sodass auch dieser äußere Regelkreis auf die gleiche Regelstrecke einwirkt (Abb. 5.11).

Zu guter letzzt ist auch die Erstellung und Anpassung des Fahrplans ein weiterer Regelkreis. In der Vergangenheit haben manuelle Prozesse und die Verwendung vor allem historischer Daten des Betriebsgesechens eine große Rolle bei der Fahrplanerstellung gespielt. Basierend auf diesen historischen Informationen werden Fahrpläne mit einer geplanten Zugkapazität (Anzahl von Fahren pro Fahrrichtung und Stunde) erstellt. Das Ergebnis ist ein Fahrplan mit einer Zugkapazität, der auf oftmals überholten Daten aus der Vergangenheit beruht. Diese Vorgehensweise ist unflexibel und erschwert Anpassungen an plötzlich notwendige Änderungen im Fahrplan und der Zugkapazität. Der Lösungsansatz ist die Einführung bedarfsgerechter Fahrpläne (Demand Responsive Transport, DRT). Hierzu werden verschiedene Datenquellen wie Auskunftsanfragen zu Fahrplänen, Ticketbuchungen oder Wettervorhorsagen analysiert, um Änderungen in der Nachfragesituation möglichst/genau vorherzusagen. Auf diese Weise konnen Fahrpläne berechnet werden, welche die prognostizierte Nachfrage berücksichtigten. Dies erlaubt es auch während eines Betriebstags kurzfristig auf einen Nachfrageanstieg mit einem verbesserten Zugeinsatz zu reagieren (Eichner und Uhrig 2021).

Abb. 5.12 zeigt ein Beispiel einer Führstandsanzeige eines CBTC-Systems des Systemherstellers Bombardier (Produkt Cityflo 650) für die Purple Line in der thailändischen Hauptstadt Bangkok. Anhand dieser Abbildung kann die Sichte eines Fahrs auf einen halbautomatischen Betrieb dargestellt werden. Hierbei wird deutlich, wie sich die Überwachungsfunktionen des CBTC-Fahrzeugeinrichtung auf der Führstandsanzeige darstellen.

Zentrales Element der Führerstandsanzeige ist die einem Tachometer nachempfundene Darstellung der für die Fahrzeugbewegung relevanten Geschwindigkeitsinformationen. Hierbei werden in dem dargestilten Beispiel die folgenden Geschwindigkeits-informationen dargestellt:

- Ist-Geschwindigkeit des Zuges: Der Zeigerausschlag stellt hierbei die aktuelle Geschwindigkeit des Zuges dar. Diese Geschwindigkeitsinformation ist als digitale Angabe ebenfalls im Mittelpunkt des Zeigers dargestellt.  
- Maximal zulässige Geschwindigkeit des Zuges: Das weiß Segment der Umrandung der Geschwindigkeitsskala der Tachometerdarstellung zeigt die aktuell zulässige Geschwindigkeit des Zuges. Sie beträgt im dargestellen Beispiel  $55\mathrm{km / h}$ .  
- Maximal zulässige Geschwindigkeitsüberschreitung des Zuges vor Wirksamwerden des automatischen Bremseingriffs: Das gelbe Segment der Umrandung der Geschwindigkeitsskala der Tachometerdarstellung zeigt die maximal zulässige Geschwindigkeitsüberschreitung von  $5\mathrm{km/h}$  an.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/bcc1c4855b44ca6bf0e97ac9a481b8552fa3acf3c25f8c3dc577f3e44d7aa77c.jpg)  
Abb. 5.12 Beispiel einer Führerstandsanzeige eines CBTC-Systems für den halbautomatischen Betrieb. (Quelle: Bombardier)

- Zielgeschwindigkeit des Zuges: Das graue Segment der Umrandung der Geschwindigkeitskala der Tachometerdarstellung zeigt die aktuellen gültige Zielgeschwindigkeit von  $35\mathrm{km / h}$ .  
- Zielentfernung des Geschwindigkeitswechsels: Auf der linken Seiteiben der Tachometerdarstellung ist eine vertikale Skala, welche die Zielentfernung darstellt. Hier wird im Betrieb ein vertikaler Balken angezeigt, welcher sich mit Annaherung an den Geschwindigkeitswechsel verkurzt. Die Färebung des Balkens zeigt an, ob eine Warngeschwindigkeit erreicht wurde (gelb) oder ob die maximal zulässige Geschwindigkeitsüberschreitung bereits übersritten wurde (rot).

Unterhalb der Tachometerdarstellung ist die aktuell aktive Betriebsart des Fahrzeugs dargeistellt (vgl. die Darstellung der Betriebsarten in Abschn. 4.2). Im betreffenden Beispiel stehen die folgenden Betriebsarten zur Auswahr:

- Automatic Mode (ATO): Das Fahrzeug befindet sich aktuell in dieser Betriebsart. Ein halbautomatischer Betrieb (semi-automated train operations, STO) ist möglich.  
Supervised Manual Mode (SM): Das Fahrzeug kann manuell vom Fahrzeugfuhrer gemäß den Vorgaben des Signalsystems geführt werden. Das Fahrzeug befindet sich darauf unter einer kontinuierlichen Überwachung eines durchgehenden Geschwindigkeitsprofils.

- Restricted Mode (RM): Im Falle von Befehlsfahrten oder im Falle von Störungen beispiselsweise des Kommunikationssystems eines vorausfahrenden Fahrzeugs kann auf Grund der fehlenden Information über einen wirksamen Gefährungsausschluss auf der vor dem Fahrzeug liegenden Strecke eine Fahrt auf Sicht erforderlich werden. Hierfür wird eine reduzierte Geschwindigkeit durch das Fahrzeuggerät überwacht.  
- Automatic Reversal Mode (AR): These Betriebsart erlaubt einen automatischen Fahrtrichtungsswechsel (Kehren) am Bahnsteig (so genannte Kurzwende).  
- Automatic Reversal Mode 2 (AR2): These Betriebsart erlaubt eine automatische Kehre über eine hinter dem Bahnsteig liegende Kehranlage (so genannte Langwende).

Da sich das Fahrzeug in dem dargestellen Beispiel im automatischen Betriebsmodus (ATO) befindet, werden dem Fahrer hier weitere weiter relevante Informationen angezeigt:

- Zug ist an korrekter Halteposition zum Stillstand gekommen: Über der dargestellen Uhrzeit auf der rechten Häufe des Displays ist ein Icon, welches den Zug symbolisch in seinem projektierten Haltebereich darstellt (stopping window). Ist das Icon – wie in Abb. 5.12 dargestellt – grün ausgeleucht, ist der Zug in dem projektierten Haltebereich zum Stehen gekommen. Ist dies nicht der Fall, ist das Icon grau. In dieser Fall,müssen der Fahrer betriebliche Ersatzhandlungen vornehmen.  
- Türfreigabesignal: Das gelbe Icon darüber quittungstaste („ACK“) auf der rechten Seite des Displays zeigt, auf welcher Seite des Fahrzeugs die Türen freigegeben sind. Im dargestellen Beispiel sind die Türen auf beiden Seiten des Fahrzeugs freigegeben.

Dies bedeutet, dass zur Beschleunigung des Fahrgastwechsels Fahrgäste auf einer Seite einsteigen und auf der anderen Seite des Fahrzeugs aussteigen können.

- Status Türoffnung: Die angedeuteten Fahrzeugtüren stellen dar, dass die Fahrzeugtüren aktuell geschlossen sind.  
- Systemstatus der Schnittstelle zur Fahrzeugleittechnik: Über der dargestellen Uhrzeit auf der rechten Häufige des Displays ist ein Icon „TCMS“ dargestellt. TCMS steht für die Anbindung des ATO-Fahrzeuggeräts an die Fahrzeugleittechnik (TCMS, Train Control & Management System). Ist das TCMS Icon grün, gibt es eine Kommunikation zwischen dem ATO-Fahrzeuggerät und der Fahrzeugleittechnik. Nur in thisem Fall kann der Zug automatisch fahren. Ist das TCMS Icon grau, gibt es keine Kommunikation zwischen dem ATO-Fahrzeuggerät und die Option des halbautomatischen Betriebs steht nicht zur Verfügung.  
- Aktueller ATO-Fahrbefehl an die Fahrzeugsteuerung: Auf der rechten unteren Seite des Displays ist ein M in einem Kreis dargestellt. Dieses Icon verdeutlich den aktuell vom ATO-Fahrzeuggerät an die Fahrzeugleittechnik übergebenen Befehl. Hierbei kann es sich um die Anforderung einer Beschleunigung handeln (M, Motoring), das Ausrollen für das energieeffiziente Fahren (C, Coasting), die Bremsung (B, Braking) oder der Stillstand im Stationsbereich (S, Stationary).

Der Fahrer erhält auf der Führstandsanzeige weitere Angaben zur Länge des Zugverbandes (aktuell ist dies ein gekuppelter Zugverband mit drei Einheiten), zum aktiven Fahrzeuggerät, zum Schliebzustand der Türen, eine Anzeige der nachsten Station (im Beispiel Bang Rak Yai) sowie Ereignisse (im Beispiel eine unerwartete Tüffnung, eine Aktivierung der Rückrollüberwachung, eine Verletzung der zulässigen Höchstgeschwindigkeit sowie die Auslösung der Zwangsbremsung). Ebenfalls dargestellt ist ein Quittungstaster  $(.,\mathsf{ACK}^{\prime \prime})$  zur Bestätigung beispiselsweise des Übergangs in einen Bereich mit Fahrerverantwortung nach Verlassen des im halb automatischen Betrieb betriebenen Streckenbereichs beispiselsweise bei Einfahr in einen nicht automatisierten Betriebshof.

# 5.3 Hauptfunktion Überwachen der Profilfreiheit

In geringeren Automatisierungsgraden ist der Fahrer für die Hauptfunktion Überwachung der Profilraumfreiheit verantwortlich. In higheren Automatisierungsgraden müssen die folgenden Oberfunktionen von einem CBTC-System mittels Schnittstellen zu externen Systemen übernommen werden.

# 5.3.1 Oberfungkntion Verhinderung der Kollision mit Objekten

In das Lichttraumprofil eines Zuges)durfen keine fremden Gegenstände hineinragen. Ist dies in Tunnelbereichen baulichweitreichend ausgeschlssen, sind außerhalb von Tunnel Weitergehende Maßnahmen zum Gefährungsauusschluss erforderlich. So konnen in den Außenbereichen Einfriedungen (Zäune) vorgesehen werden. In Abhängigkeit des Risikos sind ggf. weitere risikomindernde Maßnahmen erforderlich. Ein Beispiel hierfür sind überwachte elektronische „Reißeinen“, die das Eindringen großer Fremdkörper in das Lichttraumprofil erkennen. Ein Beispiel hierfür ist die in Mittellage einer mehrspurigen Autobahn errichtete Metro in Washington D.C. (USA). Hier ist die Strecke durch Einfriedungen (Betonabserrungen und Zaun) vom Straβenverkehr baulich getrennt. Zusätzlich wird die strukturelle Integrität des Zauns durch eine elektrische Reißeine überwacht. Der Riss des elektrischen Leiters wird offenbart und führt zu einer sichereitsgerichteten Reaktion des Zugbeeinflussungssystems.

Über den Schutz der Profilraumfreiheit hinaus muss CBTC-System auch verhindern, dass ein Zug in einen Streckenbereich einfährt, den dieser nicht gesichert befahren kann. Mögliche Grunde hierfür sind:

- mechanische Bedingungen wie das Lichtraumprofil von Fahrzeug und Strecke,  
- bauliche Bedingungen wie unzureichende Kurvenradien,  
- elektrische Bedingungen wie beispelseweise ein ungeeignetes Traktionsstromsystem,  
- andere vorübergehende Befahrbarkeitseinschrankungen wie zum Beispiel Baustellen oder  
- andere dauerhafte Befahrbarkeitseinschrankungen.

Leittechnische Systeme sehen vor, dass vorübergehende Befahrbarkeitseinschrankungen in CBTC-Systemen vom Bediener in der Leitstelle eingerichtet und darübergenommen werden können. Die CBTC-Streckeneinrichtung wird dann beispisse reduzierte Geschwindigkeiten oder Streckenspperrungen in der Erstellung von Fahrbefehlen in der Annaherung und bei der Durchfahr von Streckenbereichen mit Befahrbarkeitseinschrankungen berücksichtigten. Die Information über Befahrbarkeitseinschrankungen wird dem Fahrzeugfuhrer auf seiner Führstandsanzeige dargestellt. Die Fahrzeugeinrichtung überwacht die Einhaltung der reduzierten Geschwindigkeitsvorgabe oder der Streckenspperrung. Sie lost bei erkannten Abweichungen eine Zwangsreaktion aus.

# 5.3.2 Oberfunktion Verhinderung der Kollision mit Personen im Gleis

Die Gewährleistung der Profilraumfreiheit basiert auf verschiedene betrieblichen und technischen Maßnahmen. Fahrzeugseitig werden diese Maßnahmen durch eine Hindernisierung ergänzt. In Bezug auf die Verhinderung von Kollisionen mit Personen im Gleis muss entsprechenden werden zwischen der Verhinderung der Kollision mit „unberechtigten Dritten“, bzw. der Verhinderung der Kollision mit Instandhaltungspersonal.

Eine Kollision mit unberechtigten Dritten wird wie folgt beherrscht:

- Verhindern des Eindringens von Personen über den Tunnelmund: Ein Eindringen von Personen aus dem oberirdischen StreckenbereichCOMMEND in den unterirdischen Streckenbereich wird über am Tunnelportal verbaute Sensoren erkannt. Auf dieser Grundlage erfolgt eine Sicherheitsgerichtete Reaktion. Es wird beispielsweise ein Alarm auf der besetzten Leitstelle ausgelost. Dort wird beispielsweise das Tunnellicht zur Warning an die Fahrzeugführer angeschaltet und eine reduzierte Geschwindigkeit von der CBTC-Fahrzeugeinrichtung technisch erzwungen.  
- Verhindern des Eindringens von Personen über die Bahnsteigkante: Bei Stationen ohne Bahnsteigtären wird ein Eindringen von Personen über die Bahnsteigkante durch eine geeignete Sensorik erkannt (VDV 2000). Ebenso verhindern Bahnsteigtären ein Eindringen von Personen über die Bahnsteigkante (vgl. Abschn. 5.4.3).  
- Verhindern des Eindringens von Personen über den Kopfbereich der Bahnsteige: Ein Eindringen von Personen über den Kopfbereich der Bahnsteige wird durch bauliche Abtrennungen verhindert (überwachte Bahnsteigabschlussstüren). Turen zum Notgehweg entlang der Strecke setzen sich von der Station her nur von autorisierten Personen per Schlüssel öffnen. Um eine Evakuierung von der Strecke aus zu ermögen,{lassen sie die Turen von der bahnsteigabgewandten Seite auch ohne Schlüssel öffnen und schlagen zum Bahnsteig hin auf (VDV 2000). Die Turen sind alarmüberwacht. Zusätzlich wird eine Eindringüberwachung vorgesehen, damit keine Person über den Gleisbereich in den anschließenden Tunnelbereich gelangen kann. Hierfürkommen beispielsweise Infrarot-Lichtvorhänge oder Laserscanner zum Einsatz.  
- baulicher Gefährungsausschluss entlang der Strecke: Für einen hochautomatisierten Fahrbetrieb ist oftmals bereits durch bauliche Maßnahmen wie Einfriedungen oder gar

ein Betrieb im Tunnel ein weitreichender Schutz gegen das Eindringen von Personen oder Gegenständen in den Lichtraum eines fahrerlos verkehrenden Bahnsystems erreicht. In Deutschland mussen Einfriedungen oder ähnlich wirkende bauliche Einrichtungen mindestens  $1,20\mathrm{m}$  hoch sein (VDV 1997).

- Verhindern des Eindringens von Personen über Notausstiegsluken: Für die Entfluchtung von Tunnelbereichen werden entlang der Strecke Notausstiegsluken vorgesehen. Diese werden alarmüberwacht. Wird ein unberechtigter Eindringling erkannt, wird – wie zuvor dargestellt – eine sicherheitsgerichtete Reaktion ergriffen.  
- Verhindern des Eindringens von Personen aus liegengebliebenen Zügen: Unbefugte Personen können von einem Zug aus in den Streckenbereich eindringen (Selbstevakuiierung). Hierfür werden zum einen Warneinrichtungen im Zug bei Evakuierungen vorgesehen. Außen dem werden die Türen aller Züge zwischen den Haltestellen auf Geschlossenheit überwacht. Unzulässige Türoeffnungsversuche auf den Fahrzeugen werden erkannt und führen zu entsprechenden betrieblichen Maßnahmen (DIN EN 62267:2010).  
- Räumfahrten: Nach Betriebsunterbrechungen wird zunachst eine Fahrt durch einen Betriebsbediensteten an der Spitze des Zuges mit reduzierter Geschwindigkeit durchgehört. Der Betriebsbedienstete führt eine visuelle Räumungsprüfung durch. Der Betriebsbedienstete kann den Zug über eine Nothalttaste jederzeit zum Halten bringen. Der Betriebsbedienstete bestätigt dem Personal in der Leitstelle die erfolgreiche Durchführung der Räumungsprüfung, so dass anschließend der fahrerlose Regelbetrieb wieder aufgenommen werden kann.

Das Instandhaltungspersonal muss in der Lage sein, unter sicheren Bedingungen zu arbeiten. Daher muss gewährleistet werden, dass keine Züge in dem Bereich, in dem sie arbeiten, einfahren oder durchfahren konnen. Dies kann technisch durch unterscheidliche Maßnahmen unterstützen werden:

- Anforderung einer Gleissperrung durch das Instandhaltungspersonal über einen Schlüsselschalter. Schlüsselschalter sind manuell mit einem Schlüssel zu betätigende elektromechanische Schalter. Für die Fahrwegsicherung werden die Schalterkontakte eingelesen und je nach Schaltstellung ein Streckenbereich gespert. Im Regelbetrieb steckt der Schlüssel im Schlüsselschalter (Orloff und Aust 2016). Bei Bedarf fordert das Instandhaltungspersonal bei der Leitstelle eine Streckensperrung an. Wenn die Leitstelle die betriebliche Zulässigkeit der Einrichtung einer Baustelle geprüft hat, erteilt die Leitstelle die Freigabe für die Entnahme des Schlüssels durch das Instandhaltungspersonal. Der Besitz des Schlüssels stellt safer, dass das entsprechende Gleis für Züge gesetzt bleibt. Das Instandhaltungspersonal führt bei Räumung des Baustellenabschnitts eine Räumungsprüfung durch. Anschließend wird der Schlüssel wieder in die Schlüsselsperre gesteckt, sodass wieder in den Regelbetrieb übergegangen werden kann. Beim Einsatz von Schlüsselschalten für die Sperrung von Baustellenbereichen mussen bereits zum Zeitpunkt der Planung und Projektierung der Fahrweg

sicherung die genauen Abschnittte für die potenziellen Baustellenbereiche festgelegt werden. Darüber hinaus須en Fahrten zu den Positionen der Schlüsselschalter vorgenommen werden, bevor die Arbeiten am Gleis beginnen konnen. Zum Aufheben der Sperren sind wiederum Fahrten notwendig, um die Schlüssel wieder in dieselben Schlüsselschalter zu stecken.

- Einrichtung und Rücknahme von Befahrbarkeitssperren durch das Bedienpersonal in der Leitstelle. Hierzu können in der Leitstelle einzeln gleisabschnittte und Weichen gegen Befahrung gesamt werden. In thisem Fall werden Regelfahrten an der Einfahrt in den gespernten Gleisabschnitt gehindert. Die Arbeiten im Gleisabschnitt beginnen erst, wenn alle technischen Schutzmaßnahmen wirksam geworden sind und sich im Baustellenbereich keine Regelzüge mehr befinden. Baufahrzeuge können mit reduzierter Geschwindigkeit in den Streckenbereich einfahren und werden innerhalb des Baustellenbereichs auf eine reduzierte zulässige Maximalgeschwindigkeit überwacht (vgl. Abb. 5.13). Nach Abschluss der Bauarbeiten werden die zugehörigen Sperrungen der Fahrwegelelemente von der Leitstelle wieder aufgehoben und der Streckenbereich wieder für den Fahrbetrieb freiogegeben. Dieses Verfahren bindet die Fahrdienstleiter stark ein: sie müssen die notwendigen Sperren festlegen, ihre Einrichtung überwachen, während der laufenden Instandhaltungsarbeiten an Funktionsprüfungen mitworfen (bspw. Auslösen von Weichenumläufen), die Sperren im Anschluss wieder aufheben und damit mit den BaustellenleiternCOMMUNIZIEREN.  
- Sicherung von Baustellen im Gleisbereich mit mobilen Endgeräten: Baustellen können langfristig außerhalb der Leitstelle oder gegebenenfalls kurzfristig in der Leitstelle geplant werden. Hierfür werden Dauer und Startzeit sowie Schutzmaßnahmen (bspw. Lagevorgaben oder Befahrbarkeitssperren von Einzelelementen, z. B. zwecks Flankenschutz) festgelegt. Sobald der geplante Zeitpunkt für den Beginn eines Baustelleinsatzes erreicht ist, fordert der Baustellenleiter mittels eines mobilen Endgeräts die Verantwortung für die Baustelle an. Der Fahrdienstleiter stellt sich, dass der Fahrbetrieb auf dem Streckenabschnitt eingestellt wird und bewilligt die Übernahme der Kontrolle des Streckenabschnitts durch den Baustellenleiter. Der Baustellenleiter und sein Team beginnen die Arbeiten erst, wenn alle technischen Schutzmaßnahmen wirsam geworden sind und sich im Baustellenbereich keine Züge mehr befinden. Während der Wartungsarbeiten erforderliche Bedienungen zur Funktionsprüfung von Fahrweg-

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/a0cbd8710855235127741f1fb31af6b0d1d644b8b00161a1b3031f701cbedd0b.jpg)  
Abb.5.13 Absicherung von Baustellenbereichen mit CBTC-Systemen

elementen können vom Baustellenleiter selbst mit dem mobilen Endgerät ausgelöst werden. Das Personal der Leitstelle muss damit nicht mitvirken. Das Verfahren stellt sicher, dass der Baustellenleiter nur Weichen innerhalb des ihm zugeordneten Baustellenbereichs bedieren kann. Bei längeren Baustelleneinsätzen kann eine Baustelle von einem Baustellenteam auf ein nachfolgenden Team übertragen werden, etwa beim Schichtwechsel. Sobald die Arbeiten in der Baustelle abgeschlossen sind, betet der Baustellenleiter mittels des mobilen Endgeräts die Rückgabe der Baustelle an den Fahrdienstleiter an. Der Fahrdienstleiter übernimmt wieder die Kontrolle über den Streckenabschnitt,heits die zur Baustelle gehörigen Sperrungen wieder auf und gibt den Streckenabschnitt wieder für den Betrieb frei. Bei der Rückgabe von Baustellenbereichen kann der Baustellenleiter über das mobile Endgerät in Form kurzer Text-Nachrichten Hinweise an den Fahrdienstleiter geben, z. B. über vorübergehende Langsamfahrstellen. Wenn z. B. Arbeiten nicht vollständig abgeschlossen wurden und in derCOMMenden Nacht fortgeführten werden sollen, darf der Bereich inzwischen möglicherweise für den Betrieb nur mit reduzierter Geschwindigkeit frei gegeben werden (Ortloff und Aust 2016).

# 5.4 Hauptfunktion Überwachen des Fahrgastwechsels

Die folgenden Oberfunktionen sind für das fahrerlose Fahren zwingend erforderlich. Für niedrigere Automatisierungsgrade konnen diese Oberfunktionen nur teilweise technisch umgesetzt sein, da diese Oberfunktionen anteilig vom Betriebspersonal wahrgommen werden.

# 5.4.1 Oberfungtion Steuern und Überwachen der Türfreigabe

Grundsatzlich erlaubt das CBTC-System die Einfahr eines Zuges in eine Station nur dann, wenn die verfügbare Bahnsteiglänge mindestens der Zugänge (inklusive Sicherheitsabstände) entspricht und ein vorausfahrenender Zug bereits den Fahrbefehl zur Ausfahr enthalten hat und dessen Ausfahr aus dem Bahnhof bereits begonnen hat. Damit wird vermieden, dass ein einfahrender Zug nur mit einem Teil der Türen am Bahnsteig hält und Passagiere möglicherweise versuchen, die Außentüren zu öffnen (Einfahrbeschänkung). Ist der Zug in die Station eingefahren, wird die Türsteuerung von verschiedene technischen Kriterien abhängig gemacht. Diese technischen Abhängigkeiten stellen sicher, dass die folgenden Bedingungen erfüllt sind, bevor auf dem in die Station eingefahrenen Fahrzeug die Türfreigabe erteilt wird:

- Der Zug ist in der geforderten Genauigkeit am benannten Haltepunkt in der Station zum Stillstand gekommen.  
- Der Zug hat seinen Stillstand erkannt (Stillstandserkennung).

Die Zugtraktion ist deaktiviert.  
- Der Zug ist gegen unbeabsichtigte Bewegung gesichert. Die Stillstands- und Rückrollüberwachung sind aktiv.  
- Der Zug hat einen Auftrag zum Öffnen der Tur empfangen. Das heißt es gibt einen Bahnsteig seitlich des Zuges.

# 5.4.2 Oberfungkion Verhinder der Verletzung von Personen zwischen Fahrzeugen

Die Oberfunktion, Verhinder der Verletzung von Personen zwischen Fahrzeugen' soll Gefährdungen dadurch zwischen die Fahrzeuge fallende Reisende verhindern. Dies ist genau dann relevant, wenn in vollständig fahrerlosen Systemen auf Bahnsteigtären verzichtet werden soll (offene Systeme, siehe hierzu Darstellung im nachsten Abschnitt). Kritisch sind hierbei insbesondere die Kupplungsbereiche bei der Fahrt in Mehrfachtraktion. Die Überwachung des Kupplungsbereiches ist vor allem dann wichtig, wenn beispelseweise im Bahnsteigbereich mit unter Alkoholeinfluss stehende Personen oder Sehbehinderten berechnet werden miss. Auch bei großem Gedränge am Bahnsteig besteht die Gefahr, dass Personen zu Fallkommen konnen und in den Kupplungsbereich gelangen.

Technisch können hierbei fahrzeugseitige Kuppelbereichsüberwachungssysteme zum Einsatzkommen (beispelsweise nach dem Sender-Empfänger-Prinzip arbeitende Infarrotleisten zwischen den gekuppelten Fahrzeugen). Diese Sensorik wird beim Stillstand des Fahrzeugs im Bahnsteiggleis mit Erteilung der Türffreigabe aktiviert. Bei Ausfahrtdes Zuges aus dem Haltestellenbereich bleibt die Sensorik noch zehn Meter eingeschaltet (May et al. 2012). Bei Auslösen der Kuppelbereichsüberwachungssysteme muss Betriebspersonal per Augenschein die Situation überprüfen. Dafür muss auch der Sicherheitsraum unter dem Bahnsteig inpiziert werden, da sich eine Person hier nach ihrem Sturz in den Gleisbereich in Sicherheit gebracht haben kann. Außerdem ist eine Sichtprüfung des Bereichs unter dem Fahrzeug erforderlich. Die ausgeloste Kuppelbereichsüberwachung darf erst dann vom Betriebspersonal zurückgesetzt werden, wenn vollständig ausgeschlossen wurde, dass sich nach wie vor eine Person im Gefahrenbereich befindet.

Eine Alternative zu technischen Sicherungen wurde eine Teilabsprüfung des Bahnsteigs an der Halteposition der Kupplungsbereiche des Zuges.

# 5.4.3 Oberfungtion Sichern der Bahnsteigkante

Bei fahrerlosem Fahrbetrieb sind die Bahnsteigkanten zu sichern. Das heißt, dass keine Person unzulässigerweise zwischen Fahrzeug und Bahnsteig gelangen kann. Außerdemarf sich keine Person oder kein Gegenstand unterhalb der Bahnsteigkante befinden. DieMöglichkeiten zur technischen Sicherung der Bahnsteigkanten werden je nach Ausführungsvariante in geschlossene Systeme (mit Bahnsteigturen) und offene Systeme (ohne Bahnsteigturen) unterschieden. Beide Varianten werden nachfolgend beschrieben.

# Geschlossene Systeme (mit Bahnsteigtären)

Die eine Möglichkeit zur Umsetzung der Sicherung der Bahnsteigkanten sind Bahnsteigtären. Ein Beispiel hierfür ist in Abb. 5.14 dargestellt. Bahnsteigtären können in entsprechenden Varianten vorkommen.

- Deckenhohe Bahnsteigtären (platform screen door, PSD): Diese Türen erstrecken sich über die gesamte lichte Höhe der Station, d. h. von der Bahnsteigkante bis zur Decke der Station. Da zwischen dem oberen Ende der Tur und der Decke der Station kein Spalt verbleibt, wird der Luftautausch, bzw. die Luftzirkulation zwischen Station und angrenzenden Tunnelbereichen unterbrochen.  
- Hohe Bahnsteigtiiren (platform edge door, PED): These Türen erstrecken sich fast vollständig über die gesamte liche Höhe der Sation, jedoch verbleibt hier ein Spalt zwischen Tür und Decke der Station. Es ist also ein Luftzaustausch, bzw. eine Luftzirkulation zwischen Station und angrenzendem Tunnelbereich möglich.  
- Halbhöhe Bahnsteigtären (automatic platform gate, APG): These Türen werden nur bis zu einer Höhe von 1,60 m bis 1,70 m ausgeführrt. Wegen ihres geringeren Gewichts sind diese Bahnsteigtären für die nachträgliche Ausrüstung von Bahnsteigen vorteilchaft. Auch hier bleibt ein Luftzaustausch, bzw. eine Luftzirkulation zwischen Station und angrenzenden Tunnelbereichen möglich.

Neben einem Zugang zu den Türen im Fahrgastbereich kann auch eine Tür auf Höhe des Führerstandes vorgesehen werden, welche in der Station – zumindest bei einem halbauto

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/6093c4ce4cf67a3b74a338626f9981e1e4376edaf924fabe4d01b3a9df3fc11e.jpg)  
Abb.5.14 Beispiel von Bahnsteigtären im Stationsbereich. (Quelle: PINTSCH GmbH)

matischen Betrieb - einen Fahrerwechsel ermöglich. Unabhängig vom Typ der Bahnsteigtür ist ihre Steuerung an die CBTC-Streckeneinrichtung angebunden. Die Steuerung der Bahnsteigtür erfährt hierüber, ob sich ein Zug im Bahnhof befindet, ob dieser mit der geforderten Genauigkeit an der Zielposition zum Stillstand gekommen ist und ob die Zugtüren offen oder geschlossen sind. Für den Einsatz von Bahnsteigtären existierenDETAILIe Sicherheitsanforderungen, die nachfolgend vorgestellt werden:

- Vermeiden des mechanischen Versagens der Bahnsteigtür: Bahnsteigtären müssen gegen die zu erwartenden betrieblichen Beanspruchungen dimensioniert werden. Ist der Bahnsteig komplett von Bahnsteigtären abgeschlossen, sind insbesondere Beanspruchungen aus der Aerodynamik einfahrender Züge zu berücksichtigten. Hierbei kommt es zu einem Wechsel zwischen der Druckwelle vor einem einfahrenden Zug und einem Sog hinter einem ausfahrenden Zug. Vor dem Hintergrund einer hohen Zugfrequenz in städtischen Nahverkehrssystemen ist hierbei auch die Dauerfestigkeit bei vielen Lastzyklen eine bemessungsrelevante Höhe (EN 17168:2021).  
- Vermeidung der Türoffnung zur Unzeit: Die Bahnsteigtären werden erst freilegegeben, wenn ein Zug in die Station eingefahren und in dieser zum Stillstand gekommen ist. Öffnen sich die Bahnsteigtären ungewölt auf einem überfüllten Bahnsteig während der Zug gerade einrollt, entstehen erhebliche Sicherheitsrisiken. Das Öffnen der Bahnsteigtären suggeriert den Fahrgästen, dass der Einstiegsvorgang beginnen kann, sodass die Menschenmassen Richtung offener Bahnsteigtären stromen. Fähr genau in thisem Moment ein Zug ein oder beginnnt mit der Ausfahr, sind die Folgen katastrophal (Krins et al. 2016).  
- Vermeidung einer Fehlpositionierung von Fahrzeugen: Um eine minimale Öffnungseweite zwischen Fahrzeug und Bahnsteigür sicherzustellen, ist eine hohe Haltegenaugkeit der Fahrzeuge am Bahnsteig erforderlich. Dies erfordert eine genaue Wegmessung. Die Haltegenaugkeit wird in einem geometrischen Interval (+/- x mm) für eine Anzahl von Halten (x% der Stationshalte) angegeben. Die Haltegenaugkeit muss unter verschiedenen Einflussfaktoren erreichbar sein (bspw. Neigungen und Gefäle im Stationsbereich, zulässige Geschwindigkeit in der Anfahr, bzw. in der Station sowie verschiedene Besetzungsgrade der Fahrzeuge und darauf resultierenden Fahrzeuggewichten). Kommt das Fahrzeug nicht mit der gewünschten Genaugkeit an der Zielposition zum Stillstand ist ein Nachpositionieren des Fahrzeugs am Bahnsteig erforderlich. Hierbei werden mit dem Zurücksetzen und der Schleichfahrt zwei entsprechliche Fälle des Nachpositionierens unterschieden. Die Funktion Zurücksetzen erlaubt eine überwachte und geschützte Rückwärtsbewegung eines Zuges, der einen vorgesehenen Prázisionshalt am Bahnsteig überfahren hat. Im halbautomatischen Betrieb erfolgt das Nachpositionieren manuell durch den Fahrer mit einer Rückwärtsfahr im Rahmen der im Fahrzeuggerät konfigurierten Rückrolldistanz. Das Fahrzeug möglichst damit das Rückwärtsfahren, ohne dass der Führerstand gewechselt werden muss. Im unbegleiteten fahrerlosen Betrieb setzt sich das Fahrzeug automatisch, d. h. ohne manuelle Kommandierung in Bewegung. In beiden zuvor genannten Fälle sendet das Fahrzeug einen Alarm an die Leitstelle, weil es sich im Rahmen der konfigurierten

Rückrolldistanz entgegen der im Fahrweg vorgegebenen Fahrrichtung bewegt. Die Funktion Schleichfahrt erhöht es, den Zug nachzupositionieren, solle dieser vor dem vorgesehenen Prazisionshalt zum Stillstand kommt. Im halbautomatischen Betrieb erfolgt auch in thisem Fall das Nachpositionieren durch den Fahrer. Im unbegleiteten fahrerlosen Betrieb setzen sich das Fahrzeug automatisch, d. h. ohne manuelle Kommandierung in Bewegung, um die vorgesehene Halteposition zu erreichen. Zurücksetzen und Schleichfahrt konnen bei Bedarf auch manuell vom Bediener der Leitstelle aktiviert werden, wenn mit den automatischen Manövern der vorgesehene Halteplatz nicht erreicht werden konnte. Für den Fall, dass die Fehlpositionierung des Fahrzeugs auch durch Nachpositionieren nicht behoben werden kann, stellen Nottüren sicher, dass Fahrgäste auch aus fehlpositionierten Fahrzeugen aussteigen konnen. Nottüren müssen gegen unbefugte Betätigung von der Bahnsteigseite abgesichert werden und in eine Überwachung einbezogen werden (EN 17168:2021).

- Reziprozität der Türsteuerung: Fahrzeugtären gehen nur dann auf, wenn auch stationsseitig eine Funktionierende Bahnsteigür vorhanden ist (vgl. Abb. 5.16). Ebenso sollenn sich Zug- und Bahnsteigtären zur gleichen Zeit - und nicht zeitversetzt - öffnen und schließen. Halt beispelsweise, wie in Abb. 5.16 in der oberen Bildhälte dargestellt, ein Kurzzug in einer Station, bleiben die Bahnsteigtären hinter dem Zug geschlossen (Bahnsteigtären P9 bis P12 in Abb. 5.15). Ebenfalls bleiben Zug- oder Bahnsteigtären geschlossen, wenn die korrespondierende Bahnsteig- oder Zugür defect ist (Haspel und vom Hövel 2001). Dies ist in Abb. 5.16 bei Fahrzeugtür R2 und Bahnsteigtür P2 der Fall. Wenn eine Tur auf dem Fahrzeug oder der Station gegen Bedienung gespert ist, sollte dies dem Fahrgast visuell angezeigt werden (EN 17168:2021). In einigen seitenen Fälle ist der Zug auch länger als der Bahnsteig. Dieses Szenario ist in Abb. 5.15 in der unteren Bildhälte dargestellt. Die Fahrzeugtären R9 bis R12 * $\text{dürfen}$  in thisem Fall nicht geöffnet werden, da sich diese außerhalb des Bahnsteigbereichs befinden und die Fahrgäste nicht gefahrlos das Fahrzeug verlassen können.  
- Vermeiden des Einschlusses von Personen im Raum zwischen Bahnsteig- und Fahrzeugtür: Gegebenenfalls kann durch bauliche Maßnahmen sichergestellt werden, dass keine Person zwischen Bahnsteig- und Fahrzeugtür eingeschlossen werden kann (schraffierter Bereich in Abb. 5.16). Dies ist jeder nicht immer möglich. Zum einen ist der dynamische Fahrzeuglichtraum größler als die relevanten Abmessungen des Wagenkastens. Zum anderenweitet sich gerade bei Haltestellen in Kurvenlage durch die geometrischen Zusammenhänge zwischen Bahnsteigkante und Wagenkasten der Raum zwischen Bahnsteig- und Fahrzeugtür. Ein zusätzlicher Effekt bei Haltestellen in Kurvenlage ist die zusätzliche Neigung des Fahrzeugs durch eine mögliche Überhöhung der Bogenäuβeren Schiene. Ist der Abstand zwischen Wagenkasten und Bahnsteigtür zu groß, kann eine zusätzliche Sensorik (bspw. ein Laserscanner) vorgesehen werden. Nach schlieben der Bahnsteig- und Fahrzeugtüren tritt der Scanner in Aktion. Die Fahrtfreigabe wird erst erteilt, wenn eine Freimeldung der Scanner vorliegt.  
- Vermeiden, dass eine Person in den Spalt zwischen Bahnsteig und Wagenkasten fällt, sodassich nur der Oberkörper im schraffierten Bereich in Abb. 5.16 befindet. Hierfür konnen aktive oder passive Einrichtungen (bspw. Lückenfüllelemente aus Polyurethan)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/548bab43c26f17abd03b3b15775e1865e729c7f3f2c8964e59cc1be40a140d56.jpg)  
Abb.5.15 Reziprozität der Türsteuerung

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/20322178ee03134222557b6e1c1348f435d0bd1ac4438f8bb6cea042ef46b60a.jpg)  
Abb.5.16 Spalt zwischen Wagenkasten und Bahnsteigtür

vorgesehen werden. Die aktiven Einrichtungen konnen zum einen auf den Fahrzeugen in Form ausfahrbarer Schiebetritte vorgesehen werden. Hierbei sind zeitliche Abhängigkeiten bei Betätigung des Schiebetrittes zu beachten. Der Schiebetritt muss ausgefahren sein, bevor sich die Turen öffnen. Der Schiebetrittarf erst wieder eingefahren werden, wenn die Turen geschlossen sind. Zum anderen konnen die aktiven Ein

richtungen auch infrastrukturseitig (mechanical gap filler) vorgesehen werden. Grundsätzlich sind die Fahrgäste immer durch akustische Hinweise (.Mind the gap") auf die Gefahr des Spaltes zwischen Bahnsteig und Wagenkasten hinzuweisen (EN 17168:2021).

- Schutz von Personen gegen Einklemmen im Bereich der Bahnsteigtür: Um Personen und Gegenstände gegen Einklemmen im Bereich der Bahnsteigtür zu schützen, müssen verschiedene Maßnahmen angewendet werden. Personen sind vor dem Türschließvorgang optisch und akustisch zu warnen. Darüber hinaus ist eine unzulässige Krafteinwirkung auf eine eingeklemme Person oder einen eingeklemmen Gegenstand an den Schließkanten beispisseweise durch eine Kraftbegrenzung des Turantriebs oder eine Schließkantenüberwachung zu vermeiden. Auch ist das Verletzungsrisiko für Personen durch schließende Bahnsteigtären mittels entsprechender Gestaltung der Hauptschieb-kanten der Bahnsteigtür beispisseweise durch weiche Schließkanten zu minimieren.  
- Unterstützung der Evakuierung von Fahrgästen im Notfall: Es muss möglich sein, die Bahnsteigtür von der Gleisseite her zu öffnen, sodass in einem Notfall oder bei einem unerwarteten Fehler der Bahnsteigtür die Fahrgäste die Bahnsteigtüren mit geringem Kraftaufwand öffnen konnen (Selbstrettung). Umgekehrt muss auch die Zutrittsmöglichkeit zum Gleisbereich für die Fremdrettung sichergestellt werden. Daher muss die Türoeffnung der Bahnsteigtür für authorisiertes Personal von außen her per Hand möglich sein. Um Missbrauch durch unbefugte Personen vorzubeugen, sollte dies nur mit einem speziellen Schlüssel oder Gerät möglich sein (EN 17168:2021)

Der Einsatz von Bahnsteigtären hat die folgenden Vorteile:

- Komforterhöhung für Fahrgäste: Bahnsteigtären konnen den Komfort für Fahrgäste in unterirdischen Stationsbauwerken erhöhen. So ist es beispisseweise in warmen Ländern einfacher, die baulich von der Umgebung abgetrennten Bahnsteigbereiche zu klimatisieren. Dies kann zu Kosteneinsparungen und reduziertem Energieverbrauch führen, indem der Verbrauch von Heizung und Klimaanlage im Bahnhof gesenkt wird. Außen dem vermeiden Bahnsteigtären Belastigungen der Fahrgäste durch den Luftzug oder die Gerausche einfahrender Züge. Im Freien bieten Bahnsteigtären Schutz vor Witterungseinflüssen.  
- Kapazitätsgewinn: Haltestellenaufenthalszeiten limitieren in städtischen Nahverkehrssystemen die Kapazität. Ein positiver Effekt auf die Fahrgastwechselzeiten besteht beim Einsatz von Bahnsteigtären darin, dass sich die wartenden Fahrgäste bereits vor Einfahrts des Zuges entsprechend aufstellen konnen. Der Fahrgastwechsel kann sich dementsprechend disziplinierter vollziehen. Ein weiterer Kapazitätseffekt ergibt sich aus einer höheren Einfahrgeschwindigkeit der Züge in die Station. Um Gefährdungen durch vorbeifahrende Züge zu reduzieren wird die zulässige Geschwindigkeit von Zügen bei Vorbeifahr an Bahnsteigen ohne Bahnsteigtür reduziert. Diese Geschwindigkeitschränkung kann entfallen, wenn Bahnsteigtären Gefährdungen durch in den Gleisbereich gelangte Fahrgäste ausschlieben.

- Sicherheitsgewinn: Bahnsteigturen reduzieren das Unfallrisiko, insbesondere wenn Züge mit hoher Geschwindigkeit durch den Bahnhof fahren. Außendem schranken Sie den Zugang Unbefugter zu Gleisen und Tunnel ein.

Der Einsatz von Bahnsteigtären unterliegt den folgenden Einschränkungen, bzw. weist die folgenden Nachteile auf:

- Hohe Anforderungen an die Haltegenaigung der Züge: Vorgaben zur Haltegenaigung sind abhängig von der physikalischen Interaktion zwischen Stahlrad und Schiene. Sollte in der Migrationsphase ein Mischbetrieb mit nicht automatisierten Fahrzeugen vorgesehen sein, konnen von diesen die geforderten hohen Haltegenaigungkeiten möglicherweise nicht eingehalten werden.  
- Einsatzrunkungen im Fahrzeugeinsatz: In Bestandssystemen werden in der Regel verschiedene Zugtypen eingesetzt, die entsprechiche Turanordnungen und Zuglängen aufweisen. Beim Einsatz von Bahnsteigtären sind die Anordnungen und Abmessungen der Türen verbindlich festgelegt. Folglich konnen Züge im Betrieb nicht mehr variabel eingesetzt werden, sondern pro Linie nur noch mit demselben Zugtyp verkehren. Dies bringt für den Betreiber erhebliche Einsatzrunkungen im Fahrzeugumlauf mit sich. Darüber hinaus müssen die gewährten Abmessungen vom Betreiber bei zukünftigen Fahrzeugbeschaffungen als Randbedingung beachtet werden. Diese Einsatzrunkung kann durch Bahnsteigtürsysteme anteilig begegnet werden, bei denen die Türen am Bahnsteig je nach Zugtyp horizontal verfahren werden können.  
- Einbau bei Haltestellen in Kurvenlage schwierig: Vor Jahrzehnten wurden gegebenfalls Bahnsteige in Kurvenlage errichtet. Dies führt dazu, dass zwischen Fahrzeugen und Bahnsteigkante konstruktsbedingt ein großer Spalt entsteht. Für die Barrierefreiheit kann dieser Spalt mit Gap Fillern (beispielsweise Gummilippen aus Polyurethan) gefüllt werden. Allerdings besteht das Risiko, dass Fahrgäste zwischen Fahrzeug- und Bahnsteigtür eingeschlossen werden können.  
- Einbau schrankt verfügbarbare Breite bestehender Bahnsteige ein: Nach geltender Vorschriftenlage muss die Breite der Bahnsteige nach dem Verkehrsaufkommen unter Berücksichtigung der Stärke und Verflechtung der Fahrgastströme bemessen sein. Längs der Bahnsteigkante muss in Deutschland eine nutzbare Breite von mindestens  $2,0\mathrm{m}$  vorgesehen werden. Da bei Bahnsteigtären pro Seite von einem halben Meter Platzbedarf ausgegangen wird, wurden vorhandene Bahnsteige bei einem nachträglichen Einbau schmaler werden. Das wurde dazu führten, dass an einigen Haltestellen nicht mehr genug Platz vorhanden ware, um die Fahrgäste im Notfall sicher evakuieren zu konnen.  
- Eingeschränkte Traglast alter Bausubstanz: Mit 400 kg pro Meter trigen Bahnsteig-tären ein beachtliches Gewicht. Die Bausubstanz bestehender Bahnsteige ist ggf. zu schwach für diese Last. Hinzu kommt Hohlräume, die sich in einigen Stationen unter den Bahnsteigen befinden, um ins Gleis gefallenen Personen Schutz zu bieten. Dadurch wird die Traglast der Bahnsteige zusätzlich verringgert.

- Anpassungen der Tunnelbelüftung: Nach Einbau von Bahnsteigtären reicht in Tunnel möglicherweise der Luftzaustausch über die Haltestellen, Tunnelmündungen und Notausgabe nicht aus. Daher sind hier zusätzliche Maßnahmen der Tunnelventilation zu treffen.  
- Zuverlösigkeitsprobleme in Außenbereichen: Automatische Bahnsteigtüren, die der Witterung unmittelbar ausgesetzt, sind konnen Zuverlösigkeitsprobleme aufweisen. Fallen die Bahnsteigtüranlagen im Betrieb aus, hat das gravierenden Auswirkungen auf den Zugbetrieb.

# Offene Systeme (ohne Bahnsteigtären)

Eine Alternative zu geschlossenen Systemen mit Bahnsteigtären ist die Sicherung von Bahnsteigkanten mit technischen Überwachungseinrichtungen für den Gleisbereich, die verhindern, dass Personen von Fahrzeugen gefährdet werden. Dies ist beispelisse bei oberirdischen nicht als geschlossene Bahnhofsgebäude ausgeführten Stationen denkbar. Für die Erkennung möglicher Gefährdungen konnen verschiedene technische Systeme zum Einsatz kommt. Lös eines dieser Systeme aus, während sich der Zug bereits sehr nahe am Bahnsteig befindet, erfolgt eine Zwangsbremsung. Lös eines dieser Systeme aus und ist der Zug noch im Tunnel unterwegs und weiter entfernt, so fahrth der Zug gegebenenfalls bis kurz vor den Bahnsteig und kommt Dort zum Stillstand. Parallel dazu erfolgt eine Meldung an die besetzte Leitstelle (Dombrowsky et al. 2008). Beisephafte Lösungen für offene Systeme umfassen die folgenden Sensorprinzipien:

- Infrarot-Lichtschranken: Infrarot-Lichtschranken stoßen bei Erkennen von Personen oder größeren Gegenständen im Gleis je nach Entfernung des Zuges zum Gefahrenbereich unterscheidliche Sicherheitsgerichtete Reaktionen an.  
- Kontaktmatten: In frühen Projekten kamen auch Kontaktmatten zum Einsatz, welche die Anwesenheit von Personen oder Gegenstände ab einem bestimmten Gewicht detektieren konnten.

Grundsätzlich gilt, dass die offenen Systeme die Nachteile von geschlossenen Systemen mit Bahnsteigtären vermeiden, bzw. die Vorteile von geschlossenen Systemen mit Bahnsteigtären nicht erreichen. Insofern wird hier auf eine Wiederholung der im Abschnitt zu den geschlossenen Systemen mit Bahnsteigtären genannten Punkte verzichtet.

Weil sich offene Systeme ohne Bahnsteigtären in wesentlichem Umfang auf sensible Sensorsysteme stützen, werden hier zwei elementare Herausforderungen der Sensorik ergänzt:

- Falsch positive Objekterkennung wirkt betriebshemmend: Bei Sensorsystemen ist es wichtig, dass der sensorisch erfasste Sachverhalt auch der Realität entspricht. Bei einer falsch positiven Objekterkennung wird beispelseweise vom Sensor ein Objekt erkannt, obwohl tatsächlich kein Objekt im Gefahrenbereich ist. In thisem Fall wird eine Sicherheitsgerichtete Reaktion ohne konkreten Anlass ergriffen. Die Züge erhalten eine

Zwangsbremsung und es mussen aufwändige betriebliche Verfahren durchgeführt werden, um wieder in den Regelbetrieb überzugehen.

- Risiken durch falsch negative Objekterkennung: Bei einer falsch negativen Objekterkennung wird beispiselsweise vom Sensor kein Objekt erkannt, bzwohl sich tatsächlich ein Objekt im Gefahrenbereich befindet. In thisem Fall bleibt eine eigentlich erfolderliche Sicherheitsgerichtete Reaktion aus. Die Züge erhalten keine Zwangsbremsung und es kann zu einer Kollision des Zuges mit unberechtigten Personen im Gleis kommt.

# 5.4.4 Oberfungkion Sicherstellen der Abfertigungsbedingungen

Durch diese Basisfunktion wird sichergestellt, dass ein an einem Bahnsteig nach Verkehrshalt abfahrbereiter Zug (Fahrgastwechsel ordnungsgemäß abgeschlossen) nur dann abfährt, wenn das CBTC-Fahrzeuggerät geprüft hat, dass die folgenden Bedingungen erfüllt sind (Ritter 2014):

- Der Zug hat eine gültige Fahrerlaubnis zum Verlassen des Stationsgleises empfangen. Die Länge der Fahrerlaubnis ist mindestens so lang, dass der Zug den Bahnsteig komplett verlassen kann. Damit wird vermieden, dass ein aus einer Station aufhrender Zug nur mit einem Teil der Türen am Bahnsteig hält und Passagiere möglicherweise versuchen, die Außentüren zu öffnen (Ausfahrbeschränkung).  
- Der Zug kann den nachsten Haltepunkt erreichen. Dies bedeutet auch, dass der Nothalt-taster am Bahnsteig, den der Zug verlassen soll, nicht ausgelöst wurde. Ein Auslösen des Nothalt-tasters bei der Ausfahr des Zuges aus der Station hatte zur Folge, dass der Zug nach erfolgter Ausfahr unmittelbar hinter der Station zum Stillstand kommt.  
- Alle Türen des Zuges sind ordnungsgemäß geschlossen und keine Personen oder Gegenstände eingeklemmt. Hierbei kann der Schließvorgang auf zwei Arten eingeleitet werden. Beim lokalen Schließen wird an jeder Tur festgestellt, ob der Türbereich frei ist. Hierfürkommen unterschiedliche Sensorprinzipien wie Lichtschranken, Lichtgitter (vgl. Abb. 5.17) oder sonstige Detektionssysteme wie Trittstufenkontakte zum Einsatz. Anschließend wird die betreffende Tur nach einer optischen und akustischen Schlieb-warnung automatisch geschlossen. Beimzentralen Schließen wird der Beginn des Schließvorgangs optisch und akustisch angekündigigt und alle Türen des Zuges erhalten einenzentralen Schließbefehl von einem Fahrbediensteten (VDV 2017).  
- Es befinden sich keine Personen in dem Spalt zwischen Fahrzeug und Bahnsteigkante.  
- Es wurde nach dem alle zuvor genannten Bedingungen geprüft wurden ein Abfahtrauftrag für den Zug erweitert.

Bei Zügen, die nicht im unbegleiteten fahrerlosen Betrieb verkehren obliegt die Prüfung der Abfertigungsbedingungen dem Betriebspersonal (Kuhlmeyer 2020). Hierbei kann die Verantwortung für den Abfertigungsvorgang auch bei einer ortlichen Aufsicht der Station lie

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/3c521d787c5ff37a74ec117496a25741e82697cae6ba54b8de6e417d3ccddf03.jpg)  
Spiegel als Abfertigungshilfe am Bahnsteigende (Stadtwerke München)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/fb83c91855e79e00eebf2b8d4383c1269a6d214584d1a7d033958598d4f0a754.jpg)  
videogestützte Abfertigungshilfe auf dem Führerstand (Hamburger Hochbahn)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/f92528bd981256f06645be4de44acc72c628a63d7ec7a74b18c519a61374f875.jpg)  
videogestützte  
Abfertigungshilfe am Bahnsteigende (S-Bahn München)  
Abb. 5.17 Technische Hilfen zur Sicherstellung der Abfertigungsbedingungen im Betrieb mit Fahrzeugführner

gen, wird bei Schierenverkehrssystemen hoher Beförderungskapazität (U-Bahren und S-Bahren) jedoch meinst durch den Triebfahrzeugführer wahrgenommen (sog. Selfstabfertigung). In allen Fällen beobachtet das Betriebspersonal den Fahrgastwechsel (Kuhlmeyer 2020). Das Betriebspersonal stellt fest, dass augenscheinlich keine Personen oder Gegenstände in den Turen eingeklemmt sind. Das Betriebspersonal stellt ebenso augenscheinlich fest, dass keine Person in den Spalt zwischen Fahrzeug und Bahnsteigkante gefallen ist (Muhleck et al. 2022). Der Triebfahrzeugführer kann bei der Selfstabfertigung durch verschiedene Einrichtungen unterstützt werden. Dies ist im einfachsten Fall ein Spielgel am Bahnsteigende, über den er den rückliegenden Bahnsteigbereich einsehen kann (vgl. Abb. 5.17 links). Ein weiterer Ansatz zur Unterstützung der Zugabfertigung durch den Triebfahrzeugführer sind videogestützte Abfertigungsanlagen. Der prinzipielle Aufbau der videounterstützten Abfertigung sieht eine oder mehrere Kameras vor, die verschiedene Bereiche des Bahnsteigs abdecken. Dies erleichtert dem Triebfahrzeugführer insbesondere an stark frequentierten Stationen die Beobachtung des Fahrgastwechsels. Die Videobilder der Bahnsteigbereiche werden abschnittswise auf einem oder mehrere Bildschirme übertragen, die am Bahnsteig so platziert sind, dass die Triebfahrzeugführer sie von ihrem Halteplatz aus sehen können (vgl. Abb. 5.17 rechts). Bei einigen Verkehrsunternehmen werden die Videobilder auch drahtlos in den Führerstand übertragen und Dort angezeigt (vgl. Abb. 5.17 rechts).

Die zuvor genannten Aufgaben müssen bei einem Übergang in ein unbegleitetes fahrer-loses Fahren von technischen Einrichtungen übernommen werden. So konnen beispiele-weise die Fahrzeuge für den Ausschluss von Gefährdungen beim Schlieben der Türen mit einem Einklemmschutz und einer Einklemmerkennung ausgerüstet sein.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/6cf916538a499278d8cbc16b3da952178ae6701cb4b85e646045f3edf73b55fa.jpg)  
Berührungslose Türeberwachung durch Lichtgitter in Schienenfahrzeugen

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/bc74ecc1e260b16d16735a0a3b1d950d277b68505a5090cb625f9a87e52a2aca.jpg)  
Überwachung kleinster Objekte (beispielsweise Hundeleinen)  
Abb. 5.18 Lichtgitter im Türbereich gewährleisten einen unfallfreien Ein- und Ausstieg der Fahrgäste. (Quelle: Sitron Sensor GmbH).

- Einklemmschutz: Beim automatischen Schlieben einer Turk kann zum Beispiel eine Elektronik den Stromverbrauch der Türmotoren messen. Steigt dieser an, weil beispelsweise ein Gegenstand oder Menschen den Schliebsvorgang der Tur blockiert, gibt die Elektronik die Tur wieder frei. Ebenso konnen die Türkanten überwacht werden. Bleibt die Tur auch bei wiederholtem Schliebsversuch blockiert, wird die besetzte Leiststelle informiert, damit das Personal der Leitstelle sich ein Bild von der Lage im Fahrzeug verschaffen kann. Hierfür konnen Kameras im Fahrzeug oder Notsprechtstellen in den Fahrzeugen vorgesehen werden.  
- Mitschleiferkennung nach Beendigung des Schliebsvorgangs (Einklemmerkennung): Zusätzlich konnen die Turkanten mit einem technischen System ausgestattet werden, welche selbst)dinne Gegenstände (zum Beispiel eine Hundeleine) erkennt. Technisch kann dies durch Sensoren im Gummiprofil der Turen erkannt werden (Dombrowsky et al. 2008). Die Einklemmerkennung wird erst bei geschlossener Tur aktiviert und ist auch noch beim Anfahren eingeschaltet, um ein Mitschleifen von Personen oder Tieren zu verhindern (May et al. 2012). Das Ansprechen dieser Einrichtung bewirkt, dass entweder die Abfahr des Fahrzeugs verhindert oder seine Anfahr innerhalb einer entspreadend den betrieblichen Bedingungen plausiblen Zeit oder Strecke oder Geschwindigkeit abgebrochen wird und das Fahrzeug zum Stillstand kommt (VDV 2017). Bei fahrerlosen Systemen wird ein Alarm auf der Leitstelle ausgelost (Abb. 5.18).

# 5.5 Hauptfunktion Automatischer Zugbetrieb

Für einen automatischen fahrerlosen Zugbetrieb sind weitere Oberfunktionen erforderlich, welche nachfolgend vorgestellt werden.

# 5.5.1 Oberfunktion Einsetzen und Aussetzen von Fahrzeugen

Im automatischen fahrerlosen Zugbetrieb konnen voll automatisierte Abstellanlagen oder Depots vorgesehen werden. Hierbei konnen verschiedene betriebliche Handlungen

automatisiert vorgenommen werden. Auf diese Weise konnen die Betreiber durch spontanes Ein- und Aussetzen von Zügen kurzfristig auf Spitzen im Fahrgastaufkommen reagieren. Hierzu müssen unter anderem die folgenden Funktionen durchgeführt werden:

- Verhinderung einer Abfahr mit Fahrgästen in die Abstellanlage: Insbondere beim unbegleiteten fahrerlosen Betrieb ist kein Betriebsbediensteter begleitend im Zug oder in der Haltestelle anwesend, um den Zug zum Aussetzen vorzubereiten. Es sind beher Maßnahmen zu ergreifen, um das Risiko zu verhindern, dass ein Fahrgast in einem ausgesetzten Zug eingeschlossen wird. Um dies zu verhindern, konnen an der Endhaltestelle fahrzeugseitige Ansagen für das Aussetzen vorgesehen werden. Außendem kann das Personal der Betriebsleitstelle für das Fahrzeug unter Verwendung des im Fahrzeugvorhandenen CCTV-Systems (Closed Circuit Television) eine Räumungsprüfung durchführten und am Bedienplatz (Fahrzeuglupe) quittieren. Sollte davon ein Fahrgast an Bord des Zuges sein, kann dieser über eine Notsprechstelle an Bord des Fahrzeugs die Betriebsleitstelle kontaktieren (DIN EN 62267:2010).  
- Aussetzen und Abstellen des Zuges: Die Fahrzeuge erhalten einen Fahrbefehl in ein Abstellgleis. Hierbei wird das Heck eines zuvor abgestellten Fahrzeugs oder ein Gleisabschluss mit Prellbock bei der Ermittlung des Fahrbefehls berücksichtigt. Das abzustellende Fahrzeug fahrt bis auf die Schutzstrecke an den Gefahrpunkt heran.  
- Abrüsten des Zuges: Ist das Fahrzeug an der Zielposition angekommen sind, wird die Feststellbremse angelegt, um das stehende Fahrzeug gegen Abrollen zu sichern (TR Bremse 2008). Danach wird das Fahrzeug vom abgerüstet und in den Betriebszustand für das Abstellen versetzt.  
- Auflisten des Zuges: Bei Einsatzbeginn konnen die Fahrzeuge über ein Kommando der Leittechnik (Automatic train supervision, ATS) wieder aufgerüstet werden. Hierbei verländ das CBTC-Fahrzeuggerät den Betriebszustand für das Abstellen. Zur Herstellung der Betriebsbereitschaft wird die Feststellbremse gelöst (TR Bremse 2008) und das Fahrzeug ermittelt die Länge eines ggf. mehrfach gekuppelten Zugverbandes. Hierbei muss auch ein möglicherweise ungewolltes Kuppeln mit anderen abgestellten Fahrzeugen erkannt werden. Hierfür konnen zusätzliche Rollenschalter an der Mittelpufferkupplung vorgesehen werden. Zentrales Konstruktionselement der Scharfenbergkupplung ist eine drehbare Hakenscheibe (Herzstück). Diese nimmt im entkuppelten und im gekuppelten Zustand eine bestimmte Position ein, die über die Rollenschalter ausgegeben werden kann (vgl. Abb. 5.19). Darüber hinaus wird der Zugstatus überwacht und so vermieden, dass ein fehlerhafter Zug eingesetzt wird (DIN EN 62267:2010).  
- Einsetzen des Zuges: Die Fahrzeuge erhalten einen Fahrbefehl und setzen im gewünschten Fahrplantakt des Regelbetriebs ein.

# 5.5.2 Oberfungtion Betreiben eines Fahrzeugs zwischen betrieblichen Halten

Das Betrieben eines Zuges zwischen zwei betrieblichen Halten umfasst beispisse die Möglichkeit zu Fahrtrichtungswechseln. Fahrtrichtungswechsel passieren planmäßig an

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/2c970a2fdeb83519da540e92cde673ae2b8b7b1e49ff39af07973fcc5585e8a8.jpg)  
Abb.5.19 Rollenschalter zur Identifikation von Kuppelvorgängen (Beispiel: Fahrzeug vom Typ X für die fahrerlose Linie U5 der Wiener Linien)

den Endhaltestellen. Hierbei konnen Kurzkehren (der Zug kehrt am Bahnsteig) und Langkehren (der Zug fahr in das hinter dem Bahnsteig liegende Kehrgleis) unterschieden werden. Langkehren konnen (bei halbautomatischen Systemen, vgl. Abschn. 4.2.3) bei Bedarf auch fahrerlos durchgefuhrt werden.

Gegebenenfalls ist im Verlauf eines Betriebstages auch ein Umstellen von einem Kurzzugbetrieb (zum Beispiel zwei Wagen) auf einen Langzugbetrieb (zum Beispiel vier Wagen) und umgekehrt automatisch durch den Fahrplan oder manuell durch eine Bedienung in der Leitstelle möglich. Dies wird auch als Stärken (Kuppeln) und Schwächen (Trennen) von Zügen bezeichnet. So kann dynamisch auf Spitzen im Fahrgastaufkommen reagiert werden. Hierfür muss in halb automatischen Systemen das Kuppeln unterszt, bzw. bei Systemen ohne Fahrer das Kuppeln vollständig vom CBTC-System übernommen werden. Vor dem Hintergrund der erforderlichen Sicherheitsintegrität ist zu entscheiden, ob ein automatisches Kuppeln am Bahnsteig, auf der Strecke oder in der Abstellanlage gefordert ist. Ebenso ist zu entscheiden, ob ein Kuppeln mit oder ohne Fahrgäste erfolgen soll. Ein Kuppeln mit Fahrgästen bringt eben falls höhere Sicherheitsanforderungen mit sich. Die betrieblichen Vorgänge des Kuppelns, bzw. Entkuppelns werden nachfolgend für ein halb automatisches System beschreiben:

- Kuppeln unter CBTC-Verantwortung: Wenn Kuppeln durch den Fahrplan gefordert ist, fahrth das folgende Fahrzeug in der Betriebsart Vollüberwachung (Supervised Manual Mode) oder im halbautomatischen Betrieb (Automatic Mode) an das bereits wartende zu kuppelnde Fahrzeug heran, sowie es sein Fahrtbefehl zulässt. Das bereits wartende Fahrzeug ist in der Betriebsart Supervised Manual Mode oder im Automatic Mode im Stillstand. Nachdem der Fahrdienstleiter durch ein entsprechendes Kommando den Kupplungsvorgang erlaubt hat, wechselt der Fahrer des folgenden Fahrzeugs in die ihm daraufhin an der Führerstandsanzeige angebotene Kuppelfahrt. Das Fahrzeug kann dann mit überwachter Kuppelgeschwindigkeit (bspw.  $15\mathrm{km / h}$ ) an das bereits wartende

zu kuppelnde Fahrzeug heranfahren. Wenn die Fahrzeuge mechanisch und elektrisch gekuppelt haben, erkennen die CBTC-Fahrzeuggeräte den neuen Zugverband. Nach dem die Konfiguration des neuen Zugverbands durch das CBTC-System erkannt worden ist, kann der gekuppelte Zugverband die Fahrt in der Betriebsart Supervised Manual Mode oder Automatic Mode fortführren. Der neue Zugverband wird mit der im Fahrplan hinterlegten Fahrzeugkennung geführt.

- Entkuppeln unter CBTC-Verantwortung: Entkuppeln unter CBTC-Verantwortung ist an definierten Standorten möglich. Das aktive CBTC-Fahrzeuggerät des Zugverbandes befindet sich in der Betriebsart Supervised Manual Mode oder Automatic Mode im Stillstand an dem Ort, wo entsprechend des Fahrplans Entkuppeln vorgesehen ist. Nachdem der Fahrdienstleiter durch ein entsprechendes Kommando den Entkupplungsvorgang erlaubt hat, wechselt der Fahrer des hinteren Zugteils in die ihm daraufhin angebotene Betriebsart Kuppeln. Der Fahrer entkuppelt.beide Fahrzeuge entsprechend den für das Fahrzeug vorgesehenen Prozeduren. Nachdem die Fahrzeuge entkuppelt wurden, wird von beiden CBTC-Fahrzeuggeräten der nun entkuppelten Fahrzeugen die neue Konfiguration erkannt. Sie behalten beiden eine gültige Position und konnen dazuannah unmittelbar in der Betriebsart Supervised Manual Mode oder Automatic Mode den Betrieb fortsetzen. Die Fahrzeuge werden mit der im Fahrplan hinterlegten Fahrzeugkennung geführt.

# 5.5.3 Oberfunktion Überwachung des Fahrzeugzustands

Eine Fahrzeugdiagnose dient dazu, Fehler und Zustände der Fahrzeugausrüstung zu erkennen, welche die ordnungsgemäß Betriebsabwicklung beispiselsweise durch Liegenbleiben oder Unfälle beeinflussen konnen. Die Überwachung des Fahrzeugzustands muss technisch erfolgen, da der Fahrerstand abhängig vom Automatisierungsrgrad nicht mehr besetzt ist. Fehler und potenziell gefährliche Zustände des Fahrzeugs werden nicht mehr vom Fahrzeugfuhrer offenbart und durch darauf abgeleitete Maßnahmen (zum Beispiel ein angepasstes Fahrverhalten) durchihn beherrscht. Heraus resultieren spezifische Anforderungen (VDV 2014):

- Störungen im Fahrzeug müssen erkannt werden.  
- Bei erkranten die Betriebssicherheit gefährdende Störungen muss das Fahrzeug durch die Fahrzeugsteuerung sichereitsgerichtet stillgesetzt werden. Dies geschieht je nach Schwere der erkranten Störung durch eine Anfahrspere oder eine Sicherheitsbremsung.  
- Ein stillgesetztes Fahrzeug ist durch geeignete Maßnahmen abzusichern. Beispieleweise kann der Betrieb im Nachbargleis eingeschränkt werden, um eine etwaige Evakuierung der Fahrgäste im stillgesetzten Fahrzeug vorzubereiten.  
- Die Fahrdienstleiter muss die Fahrzeugstörung aus der Leitstelle Heraus beurteilen. Die Meldungen müssen hierbei für den Leitstellenmitarbeiter leicht verständlich sein, müssen klare Handlungshinweise geben und)dürfen nicht zu umfangreich sein (May et al. 2012).

Um diese Anforderungen zu erfüllen müssen Störungsmeldungen von der Fahrzeugsteuerung ermittelt und für das Fahrzeug im Zusammenhang mit anderen anstehenden Fahrzeugstörungen bewertet und kategoriert werden. Die folgenden Fehlerkategorien werden nach (VDV 2014) empfohlen:

- Störungskategorie A: Hierbei handelt es sich um einen liegengebliebenen oder still-gesetzen Zug bei erkannten die Betriebssicherheit gefährdenden Störungen. Der Fahr-dienstleiter muss mobiles Betriebspersonal zur Störungsbehebung oder Evakuierung der Fahrgäste direkt an den Ort auf der freiem Strecke entsenden.  
- Störungskategorie B: Hierbei handelt es sich um Störungen, bei denen der Fahrdienstleiter das sofortige Aussetzen des Fahrzeugs an einem geeigneten Ort (z. B. der nachsten Haltestelle) herbeiführt. Die Fahrgäste müssen hierfür in geeigneter Weise informiert werden und über eine Laatsprecherdurchsage an Bord des Fahrzeugs zum Aussteigen in der nachsten Haltestelle aufzufordern. Mobiles Betriebspersonal kann den Zug am Aussetzort erwarten.  
- Störungskategorie C: Hierbei handelt es sich um Störungen, bei denen die Fahrdienstleiter die aktuelle Fahrt bis zum Zielort zu Ende führen. Mobiles Betriebspersonal erwartet den Zug am Zielort oder der Zug wird bei nachster Gelegenheit bis zur Werkstatt überführ.  
- Störungskategorie  $D$ : Hierbei handelt es sich um Störungen, bei denen der Fahrdienst-leiter den Betriebseinsatz zu Ende führen kann. Der Zug wird dann bei einer ohnehin anstehenden turnusmaßigen Instandhaltung in die Werkstatt überführct.

Tab. 5.1 zeigt die Störungskategorien mit ihren betrieblichen Auswirkungen.  
Tab. 5.1 Störungskategorien im Überblick  

<table><tr><td>Störungs-kategorie</td><td>Aussetzen des Zuges</td><td>Einsatz mobilen Betriebspersonals</td><td>Auswirkungen auf die Fahrgäste</td><td>Werkstattzuführung</td></tr><tr><td>Kategorie A</td><td>Zug liegengeblieben/stillgesetzt auf freier Strecke</td><td>Entsendung auf frei Strecke</td><td>gegebenenfalls Evakuierung von frei Strecke einleiten</td><td>kurzfristiges Bergen des Zuges von frei Strecke</td></tr><tr><td>Kategorie B</td><td>sofort an geeignetem Ort</td><td>Ent sendung zum Aussetzort</td><td>Information über vorzeitigen Ausstieg am Aussetzort</td><td>Überführung bei{nachster Gelegenheit(spätestens am Ende des Betriebstages)</td></tr><tr><td>Kategorie C</td><td>Aussetzen am geplanten Zielort</td><td>Ent sendung zum Aussetzort</td><td>Keine Auswirkungen</td><td>Überführung bei{nachster Gelegenheit(spätestens am Ende des Betriebstages)</td></tr><tr><td>Kategorie D</td><td>nicht erforderlich</td><td>nicht erforderlich</td><td>Keine Auswirkungen</td><td>Überführung beiohneh in anstehender Wartung</td></tr></table>

# 5.6 Hauptfunktion Störfallerkennung und Störfallmanagement

Insbondere, wenn sich für den Betrieb kein Fahrzeugfuhrer mehr an Bord der Fahrzeuge befindet, müssen Störfälle automatisch erkannt werden. Hierbei gibt Störfälle, die durch fahrzeugseitige oder infrastrukturseitige technische Systeme automatisch erkannt werden. Es erfolgt in thisem Fall eine unverzüglichene automatische Meldung des Störfalls an die Leitstelle und die Umsetzung einer Sicherheitsgerichteten Reaktion des Automatisierungssystems im Betrieb. Beispiele hierfür sind die Aktivierung infrastruktur- oder fahrzeugseitiger fahrgastbezogener Sicherheitsysteme (Abschn. 5.6.1), das Auslösen infrastruktur- oder fahrzeugseitiger Brandmeldesysteme (Abschn. 5.6.2), die Evakuierung von Fahrgästen (Abschn. 5.6.3), das Auslösen der fahrzeugseitigen Hinderniserkennung (Abschn. 5.6.4) oder das Auslösen einer fahrzeugseitigen Entgleisungserkennung (Abschn. 5.6.5). Jeder Störfall erfordert ein manuelles Eingreifen des Betriebspersonals zur Entstörung.

# 5.6.1 Oberfunktion Fahrgastalarmmeldungen

Störfälle können durch Fahrgäste in den Fahrzeugen oder in Haltestellen erkannt werden. Die Fahrgäste melden die Störfälle durch geeignete technische Einrichtungen wie beispielsweise Einrichtungen für Sprechverbindungen zwischen Fahrgästen in den Haltestellen und der Leitstelle.

# Auswertung Fahrzeugseitiger Fahrgastalarmmeldungen

Ein Beispiel hierfür ist die Meldung eines Vorfalls auf einem Fahrzeug über eine Schnittstelle für den Fahrgastalarm. Die Schnittstelle für den Fahrgastalarm unterstützt verschiedene Funktionen (DIN EN 16334-2:2020).

- Mänglichkeit der Alarmierung der Betriebsleitstelle für die Fahrgäste im Notfall: Das Fahrgastalarmsystem befindet sich im Fahrgastbereich. Wird ein Fahrgastalarmgriff betätig, muss er in der aktivierten Position einrasten und sich deutlich sightbar von der unbetätigten Normalstellung unterschieden. Zusätzlich sollte der Fahrgast eine Rückmeldung über die Betätigung mittels eines optischen oder akustischen Signals erhalten. Das Betätigtes eines Fahrgastalarmgriffs wird dem Betriebspersonal in der Leitstelle angezeigt und von thisem quittiert. Die Leitstelle baut dann eine Sprechverbindung zum Fahrgast auf. An der Schnittstelle für den Fahrgastarm wird dem Fahrgast eine Rückmeldung angezeigt, wenn die Sprechverbindung in die Leitstelle zustande gekommen ist. Sollte eine Funktionstörung des Fahrgastalarmsystems erkannt werden, wird dies ebenfalls auf der Leitstelle angezeigt, damit entsprechende Maßnahmen eingeleitet werden konnen (DIN EN 16334-2).

- Anhalten des Zuges in Übereinstimmung mit den Betriebsvorschriften: Unter bestimmten Betriebsbedingungen (z. B. im Tunnel) kann eine Bremsüberbrückung gefordert sein. Hierbeiarfam Fahren zwischen Bahnhöfen oder an Orten, an denen

eine Passagierevakuierung schwierig ist (Tunnel) das Fahrgastalarmsystem nicht unmittelbar eine Bremsung anfordern. Dies erfordert eine Erkennung des Bahnsteigbereichsendes. Der Bereich des unmittelbaren Bremsens am Bahnsteig liegt zwischen dem Abfahrtsort des Zuges und dem Zugschluss des Zuges, der den Bahnsteig verlässt. Dies kann entweder durch Einbindung in ein Signalsystem erkannt werden (physische Erkennung) oder durch Auswertung der Deaktivierung der Türfreigabe und einer vom Fahrzeug zurückgelegten Distan erfolgen (nicht-physiche Erkennung).

- Erteilen einer Erlaubnis an den Zug je nach Bedingung weiterzufahren und an einem sicheren Ort zu halten: Das Fahrgastalarmsystem darf nur durch autorisiertes Personal in der Leitstelle zurückgesetzt werden. Dies darf nur dann aus der Leitstelle herself passieren, wenn ein CCTV (Closed Circuit Television) auf den Fahrzeugen eingesetzt wird. Da Fahrzeuge mehrere Fahrgastalarmgriffe haben, werden über die Fahrzeugsteuerung Informationen zur Lokalisierung des betätigten Fahrgastalarmgriffs im Zugverband bereitgestellt. Wenn ein CCTV verfügbar ist, damit das Fahrgastalarmsystem Informationen an das CCTV geben, um aufzuziegen, an welchem Ort ein Fahrgastalarmgriff betätigt wurde, um die vorrangige Überwachung des betreffenden Bereiches zu ermöglichen. Nachdem das Fahrgastalarmsystem darüberückgesetzt wurde, kann der Zug seine Fahrt bis zu einem sicheren Ort fortsetzen.

Über verschiedene Wege eingehende Störfallmeldungen werden auf einer Leitstelle angezeigt. Das Leitstellenpersonal kann von Dort die angemessene Sicherheitsgerichtete Reaktion anstoßen und eine geordnete Rückkehr in den Regelbetrieb koordinieren (beispielsweise die Evakuierung von Fahrgästen, vgl. Abschn. 5.6.2). Abb. 5.20 zeigt ein Beispiel der Bedienung und Anzeige für Fahrzeugseitige Einrichtungen auf der Leitstelle eines unbegleiteten fahrerlosen Systems.

# Auswertung infrastrukturseitiger Fahrgastalarmmeldungen

Auch infrastrukturseitige Alarme werden ausgewertet, dem Bediener auf dem Bedienplatz angezeigt (vgl. Abb. 5.21) und führen zu Systemreaktionen des Automatisierungssystems zur sicheren Seite. Diese Systemreaktionen erfordern bereits erfolns die Mitwirkung von Betriebspersonal zur Behebung der Störung. Dies gilt für exemplarisch für die folgenden Beispiele:

- Auslösen der Bahnsteiggleisüberwachung: Das Eindringen von Personen in den vom Bahnsteig aus erreichen Baren Gleisbereich muss technisch erkannt werden. Dies führt zu einer Sicherheitsgerichteten Reaktion des Automatisierungssystems. Diese Sachverhalt ist in Abb. 5.21 exemplarisch dargestellt. Über zähl- und protokollpflichte Bedienhandlung werden. Zur Steigerung der Verfügbarkeit bei Störungen kann ebenfalls über eine zähl- und protokollpflichtige Bedienhandlung der Leitstelle die Bahnsteiggleisüberwachung zurückgesetzt werden. Voraussetzung hierfür ist, dass ein wirksamer Gefährungsausschluss durch eine ständige Fernbeobachtung des betreffenden Gleisbereichs aus der Leitstelle gegeben ist oder durch Betriebspersonal vor Ort gegeben ist und das Betriebspersonal den Fahrbetrieb im Bedarfsfall stillsetzen kann (VDV 2000).

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/9018d531fcc6f06ba7ceaf230145724f9f5fb195dbbebce31287d8bc97f82868.jpg)  
Abb. 5.20 Fahrzeuglupe zur Anzeige von Systemzuständen der Fahrzeuge und zur Störfallbehandlung. (Quelle: VAG Nürnberg; Siemens Mobility GmbH)

- Auslösen des Nothaltschalters in der Station: Der Nothaltschalter ist Teil des fahrgastbezogenen Sicherheitsssystems in Halteststellen zum Stillsetzen des Fahrgastbetriebs im Notfall. Die konkre Reaktion des Automatisierungssystems umfasst neben einer Auslösing einer Notbremsung des in die Station einfahrenden Fahrzeugs auch die Abschaltung des Traktionsstroms im Eireignisfall. Für die Umsetzung der Schutzmaßnahmen ist im jeweiligen Einzelfall die konkre Stationstopologie zu berücksichtigten. Weist die Station einen mittig liegenden Bahnsteig mit zwei außen liegenden Stationsgleisen auf, kann die automatische Zwangsreaktion für jedem Stationsgleis einzeln erfolgen. Weist die Station jedoch außen liegende Bahnsteige mit zweiinnen liegenden Stationsgleisen auf, muss die automatische Zwangsreaktion (Abschaltung des Traktionsstroms) für beiden Stationsgleise erfolgen, da ein Übertreten von einem auf das andere Richtungsgleis möglich ist. Die Umsetzung der konkreten Projektierung ist also abhängig von der jeweiligen Stationstopologie. Der Nothaltschalter dient vornehmlich zum Abdecken von Gefahrenmomenten aus dem Fahrgastbetrieb im Bereich der Bahnsteigkante. Auch hier kann über eine zahl- und protokollpflichte Bedienhandlung die Meldung Nothalt zurückgesetzt werden. Ebenso kann über eine zahl- und proto

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/3bc9d44da92642a4f3da1abce4449c0d1d047ce19577d938854d7d1f67bd4640.jpg)  
Abb. 5.21 Ausschnitt des Bedien- und Anzeigesystems der fahrerlosen U-Bahn in Nürnberg zur Darstellung der Elementzustände des Bahnsteigsicherungssystems. (Quelle: VAG Nürnberg; Siemens Mobility GmbH)

kollpflichte Bedienhandlung der Nothalt zurückgesetzt werden. Es gelten die gleichen Voraussetzungen wie bei der zuvor dargestellen Deaktivierung der der Bahnsteiggleisüberwachung (VDV 2000).

- Auslösen der Eindringüberwachung: Das Eindringen von Personen in den benachbarten Gleisbereich von Stationen muss technisch erkannt werden. Dies ist in Abb. 5.21 exemplarisch dargestellt. Über eine zähl- und protokollpfliche Bedienhandlung kann die Meldung der Eindringüberwachung zurückgesetzt und ebenso deaktiviert werden. Eine Fortführung des Betriebs bei deaktivierter Eindringüberwachung ist nur dann möglich, wenn eine Fernbeobachtung des Eindringortes durch einen Betriebsbediensteten möglich ist und dieser den Fahrgastbetrieb im angrenzenden Streckenbereich stillsetzen kann. Alternativ kann der Fahrerstand mit einem Betriebsbediensteten zum Zwecke der Streckenbeobachtung besetzt werden (VDV 2000).

# 5.6.2 Oberfunktion Brandmeldung

Brände können durch Überhitzung und Kurzschlüsse in technischen Bereichen sowie durch Vandalismus oder Verstoße gegen Rauchverbote entstehen. Um früherzeitige eine durch Brand bzw. Rauch ausgegehende Gefährung der Fahrgäste zu verhindern, werden

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/34c28d83d2863047c975bb06f73dfcd8bab5012b9d06ba03587f8e8f502cee61.jpg)  
Rauchmelder im Fahrgastabteil (Dubai Metro)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/da0a5f9f840ec1acef8059975c35ff914fa8ca7c546e3a7b8d05df76a6455e85.jpg)  
Düse einer Wassernebelloschanlage (Metro Kopenhagen)  
Abb. 5.22 Installation von Wassernebelloschanlagen auf Schienenfahrzeugen

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/961e1836af7a1f7146cb3ba27cdf70467a53799fec6b9d880e7ca39ea7548f5b.jpg)  
Tank einer Loschanlage (Hamburger Hochbahn)

daher sowohl Infrastruktur als auch Fahrzeuge mit einer Brandmeldeanlage ausgestattet (vgl. Abb. 5.22 links für einen Sensor im Fahrzeuginnern). Hierbei kommt Sensoren mit verschiedenen Detektionsverfahren zum Einsatz, die auch miteinander kombiniert werden können:

- Fotoelektrisches Detektionsverfahren: Dieses Detektionsverfahren ist geeignet, eine Rauchentwicklung zu erkennen. Zentrales Element des�试es Detektionsverfahrens ist eine Lichtquelle (Infrarot- oder Laserstrahl) und eine Fotolinse als Sensor. Solange kein Rauch in die Kammer des Rauchmelders eindringt, wird der Lichtstrahl nicht gestört bzw. unterbrochen und trifft auf die Fotolinse. Dringen jedoch Rauchpartikel in die Rauchkammer des Melders ein, wird der Lichtstrahl durch die Rauchpartikel unterbrochen. Daraufhin bricht die Verbindung zum Fotosensor ab und der Alarm wird aktiviert.  
- Thermisches Detektionsverfahren: Dieses Detektionsverfahren ist geeignet, von einer Temperaturentwicklung auf ein Brandereignis zu schlieben. Nach thisem Detektionsverfahren arbeitende Sensoren erfassen die Umgebungstemperatur via Heißeiter. Heißeiter bestehen aus elektrisch leitendem Material, das bei hohen Temperaturen better Strom leitet als bei niedrigen. Steigt also die Umgebungstemperatur schnell genug an, erwartt sich auch der Heißeiter und es kommt zu Veränderungen in seiner Stromleitungsfähigkeit. Wird bei einer solchen Messung eine schnell ansteigende Temperatur festgestellt, lost ein Wärmemelder Alarm aus. Ebenso wird Alarm ausgelöst, sobald eine vorher konfigurierte Umgebungstemperatur übersritten wird.

Bei unterirdischen Verkehrsanlagen besteht die Gefahr einer extrem Schnellen Brandausbreitung. Daher kommt auf den Schierenenfahrzeugen zusätzlich zu den Sensoren auch Löschsysteme zum Einsatz. So kommt im Fahrgastrum von Zügen beispelsweise eine Wassernebellöschechnik zum Einsatz (vgl.Abb.5.22 in der Mitte). Diese Brandbekämpfungssanlagen verwenden Wasser als Löschnittel, das aus Düssen in feinsten Tropfen versprüht wird. Die Verwendung von Wassernebellöschanlagen betiet die folgenden Vorteile:

- Stickeffekt: Der Wassernebel verträgt beim Auftreffen auf die Flammen und durch die aus der unmittelbare Verdampfung resultierende Volumenverlösung des Wassernehels die Luft und damit den  $21\%$ igen Sauerstoffanteil vom Brandherd.

- Wärmebindung: Der Wassernebel erzeugt eine maximale Wärmebindung durch die sehr große Töpfchenoberfläche. Dies führt beispiselsweise zu einer Absenkung der Umgebungstemperatur von 1000 unter  $40^{\circ}\mathrm{C}$ .  
- effektive Rauchpartikelbindung: Als zusätzlicher Neben-effekt werden durch die Feinstropfen die entstehenden Rauchgase gebunden. Hierdurch wird die Sichteweite in den angrenzenden Bereichen stark erhöht und möglicherweise ein Fluchtweg safer geschützt.  
- geringerer Wasserverbrauch: Wassernebellöschanlagen besteht im Vergleich zu konventionellen Sprinkleranlagen eine deutlich keinere Wassermenge (20 % der Wassermenge eines konventionellen Sprinklers). Diese geringeren Wassermengen erzeugen deutlich geringere Wasserschäden.

Die Installation der Tanks für die Wasserversorgung erfolgtplatzsparend in existierenden Leerräumen (bspw. unter Sitzen, vgl. Abb. 5.22 auf der rechten Seite). Die Auslösung des Löschsystems kann über eine Kommunikationsleitung erfolgen (bspw. Train Control and Monitoring System, TCMS) erfolgen oder alternative bei einer definierten Temperatur automatisch auslösen. Der Einbau der Tanks für die Wasserversorgung erfolgt in handenen Leerräumen in der Fahrzeugkonstruktion (beispielsweise unter Sitzen).

# Systemreaction bei Ansprechen fahrzeugseitiger Brandmeldeanlagen

Brandmeldeanlagen sind in verschiedene den Komponenten des Fahrzeugs sowie im Fahrgastraum vorgesehen und direkt mit der Fahrzeugsteuerung verbunden. Bei Ansprechen des Fahrzeugseitigen Brandmeldesystems erfolgt eine ortselektive Meldung an die Leitstelle und wird in der Fahrzeuglupe (Abb. 5.20) angezeigt. Durch den Einsatz spezieller Funktionserhaltender Kabel im Fahrzeug wird erreicht, dass im Falle eines sich entwickelnden Brandes die Mindestfunktionen des Fahrzeugs aufrecht erhalten bleiben. Das Fahrzeug kann auf diese Weise sicher die{nachste Haltestelle erreichen, sodass dort eine Evakuierung erfolgen kann (Muller und Schmidt 2003). Die Fahrgastraumturen werden auf der vorgegebenen Seite durch eine Bedienhandlung auf der Fahrzeuglupe (Abb. 5.20) freigegeben. Die Turen konnen dann von den Fahrgästen geöffnet werden.

# Systemreaction bei Ansprechen infrastrukturseitiger Brandmeldeanlagen

Neben der Auswertung Fahrzeugseitiger Brandmeldungen müssen auch Brandmeldungen infrastrukturseitiger Einrichtungen ausgewertet werden. Darüber hinaus werden Sicherheitsgerichtete Reaktionen angestoßen:

- Bei erkannten Rauch in einer Haltstelle werden Züge, die sich in Annaherung befinden, die Haltestelle ohne Halt durchfahren. Züge, die sich in der vorhergehenden Haltestelle befinden, werden durch Unterbindung der Abfertigung von der Annaherung auf die Haltestelle zurückgehalten. Züge, die in Annaherung auf die vorhergehende Haltestelle sind, werden angehalten.

- Bei erkannten Rauch zwischen zwei Haltestellen werden Züge, die sich im betreffenden Streckenbereich befinden, weiterfahren, sofern keine Fahrtrestrictionen bestehen. Auch hier werden Züge in der vorhergehenden Haltestelle an der Ausfahr gehindert, bzw. in Anfahr auf die vorhergehende Haltestelle befindliche Züge angehalten.

# 5.6.3 Oberfungtion Evakuierung

Liegt eine kritische Betriebssituation vor, ist die Idealvorstellung das gezielte Stillsetzen des Fahrbetriebs. Ist dies nicht möglich, sind die Fahrgäste aus den Tunnelbereichen zu evakuieren, wobei zwischen Selfstrettung und Fremdrettung untersuchen wird. Eine Evakuierung kann auch als Kombination aus Selfst- und Fremdrettung umgesetzt werden. Eine große Rolle spielt in allen drei Fälle die situationsangemessene Information der Fahrgäste. Hierfür muss es möglich sein, die Fahrgäste über die eingetretene Störung zu informieren und sie über die erforderlichen Maßnahmen (gezieltes Stillsetzen des Fahrbetriebs, Selfst- und Fremdrettung) zu informieren.

# Gezieltes Stillsetzen des Fahrbetriebs

Bei einem gezielten Stillsetzen des Fahrbetriebs fahren die Züge nach Eintritt des kritischen Ereignisses noch bis zur nachsten Haltestelle, um die Fahrgäste aus dem Fahrzeug zu entlassen. Es soll nach Möglichkeit verhindert werden, dass Fahrzeuge im Tunnel zum Stillstand kommt. So wird verhindert, dass die Fahrgäste nicht beunruhigt sind, eine Notfalltūffnung anfordern und auf diese Weise die betrieblichen Herausforderungen in dieser Störungssituation noch weiter verschlimmern. Möglicherweise erfordert die Umsetzung dieser Strategie weitere Einrichtungen auf dem Fahrzeug. Ein Beispiel für die zur Umsetzung eines Havariekonzpts zusätzliche Einrichtungen auf dem Fahrzeug sind Batterien zur Speicherung von Traktionsenergie. Hierdurch kann im Falle von Ausfallen der Traktionsstromversorgung das Fahrzeug noch bis zur nachsten Haltestelle fahren, mindestens jedoch zum nachsten Notausgang zur Vereinfachung der Selfstrettung (siehe)nachster Abschnitt).

# Unterstützung der Selfstreitung von Fahrgästen

Selbstrettung ist die Fähigkeit zum richtigen Umgang mit Situationen, die das eigene Leben bedrohen. Der Betroffene ist zur Abwendung der Lebensbedrohung für sich selbst in der Lage, eine solche Situation zu erkennen und angemessen darauf zu reagieren. Bei der Selbstrettung ist zu berücksichtigten, dass aufgrund des eingetretenen Notfalls nicht bis zur Fremdrettung gewartet werden kann. Es muss Daher auch eine Turnotöffnung aus dem Innern des Fahrzeugs auch bei Ausfall der Stromversorgung der Türsteuerung möglich sein. Allerdings gelten für die Notöffnung einer Tür besondere Sicherheitsanforderungen:

- Vermeidung versehentlicher und missbrächlicher Türoeffnungen: Um Unfälle beim versehentlichen oder missbrächlichen Notöffnen von Türen zu verhindern, * $\text{dürfen}$  die

Fahrzeugtären nicht selbstständig offen. Es sollte daher bei der Gestaltung der Fahrzeugtären das Prinzip der zwei Handlungen angewendet werden. Dies ist zum Beispiel dann der Fall, wenn mit der ersten Handlung die Turnotöffnung von den Fahrgästen im Fahrzeug betätig wird. Mit der zweiten Handlung kann dann die Tur von den Fahrgästen von Hand aufgeschoben werden (VDV 2017).

- Automatische Aktivierung von Schutzmaßnahmen: Eine automatische Einrichtung einer Befahrbarkeitssperre für in der Gegenrichtung verkehrende oder folgende Züge kann erforderlich werden, um zu verhindern, dass vor einem Notfall flüchtende Fahrgäste mit anderen Zügen kollidieren. Diese Befahrbarkeitssperre kann beispielsweise automatisch gesetzt werden, wenn bei einem Zug eine unerwartete Tüffnung außerhalb einer Station erkannt wird. Gleiches gilt für die Fahrspannungsabschaltung (VDV 2000).  
- Eine Freigabe der Tur-Noentriebelung ist beispiselsweise für die Evakuierung relevant. Sobald sich der Zug in Bewegung setzt, wird die Tur-Noentriebelung gesperrt, da in thisem Fall bei Öffnung der Tur die Sicherheit der Fahrgäste nicht ausreichend sichergestellt ist (VDV 2017). Bleibt der Zug im Tunnel störungsbedingt stehen, so bleibt die Tur-Noentriebelung so lange gesperrt, bis entsprechende Sicherheitsmaßnahmen wie Anhalten des Gegenverkehr, Stromschiene spanningslos schalten und Einschalten der Tunnelbeleuchtung eingeleitet werden konnten. Erst dann wird die Turnotriebelung mit einer Bedienung auf der Fahrzeuglupe freiigegeben (Abb. 5.19) und den Fahrgästen ein gefahrloses Verlassen des Zuges ermöglich (Müller und Schmidt 2003).

# Unterstützung der Fremdrettung von Fahrgästen

Als Fremdrettung wird die Befähigung zum richtigen Umgang mit lebensbedrohenden Situationen anderer bezeichnet. Hierbei werden die Rettenden befähigt, solche Situationen zu erkennen, zu beurteilen und situationsbezogen zu reagieren. Die Rettenden sind in der Lage, ohne Eigengefährung anderen Personen Hilfe zu leisten. Das Ziel der Fremdrettung besteht darin, den Betroffenen aus der lebensbedrohenden Situation Herauszuhelfen. Bei Verkehrsbetreibern sind an der Fremdrettung nicht nur entsprechliche Stellen im Unternehmen zu beteiligungen, sondern auch Abstimmungen mit Behörden und Organisationen mit Sicherheitsaufgaben (BOS) zu treffen. Grundsätzlich konnen verschiedene Ansätze der Fremdrettung entsprechenden werden, die durch eine entsprechende Gestaltung technischer und organisorischer Maßnahmen unterstützen werden müssen:

- Notfalltūröffnung der Fahrzeugtur von außen: Fahrzeugseitig ist sicherzustellen, dass es den Betriebsbediensteten, bzw. dem Rettungsdienst möglich ist, das Fahrzeug von außen ohne den Einsatz spezieller Werkzeuge zu betreten. Eine Notfalltūröffnung von außen muss also möglich sein. Die Zugsicherungsanlage ist hierbei nicht beseitigt.  
- Ferngesteuerter Betrieb des Fahrzeugs aus der Leitstelle: Um ein besetztes Fahrzeug im Falle einer Störung aus dem Tunnel zu fahren, kann von den Betreibern auch ein ferngesteuerter Betrieb vorgesehen werden. Hierbei fahrht Leitstellenpersonal das Fahrzeug fernbedient aus der Leitstelle aus dem Gefahrenbereich. Hierzu konnen Fahrzeug-

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/3cd177183ec18455dd42ff5c5a51031592f91a2e72fac32edca399fe181a22d0.jpg)  
Abb.5.23 Kamera am Fahrzeug zur Fernsteuerung aus der Leitstelle (Beispiel: Fahrzeug vom Typ X für die fahrerlose Linie U5 der Wiener Linien)

seitig Kameras vorgesehen werden, über welche der vor dem Fahrzeug liegende Streckenbereich von der Leitstelle aus eingesehen werden kann (vgl. Abb. 5.23).

- Einsatz eines Rettungszuges: Für den Fall eines betriebsverhindernden Ausfalls eines fahrerlosen Zuges konnen Rettungszüge zur Bergung des havarierten Zuges zum Einsatz kommt. Der Bediener der Leitstelle communitiert über eine Sprechverbindung mit den Fahrgästen im Fahrzeug und analysiert den Status des havarierten Zuges aus der Ferne. Abhängig von der konkreten Situation bzw. der betrieblichen Gepflogenheiten des Betreibers konnen verschiedene Strategien zum Bergen der Fahrgäste zum Einsatz kommt. Die erstme Mochlichkeit ist, dass der Rettungszug von hinten möglichst dicht an den liegengebliebenen Zug heranfahrt und zum Stillstand kommt. Die Fahrgäste wechseln dann in das zweite Fahrzeug, welches die Fahrgäste in die nachstgelegene Station bringt. Die zweite Mochlichkeit ist, dass der Rettungszug auf dem Gegingleis auf Höhe des liegengebliebenen Zuges zum Stillstand kommt. Beide Züge öffnen die Türen und es werden Rettungsstege zwischen den Zügen ausgelegt, über welche die Fahrgäste in den anderen Zug übersteigen konnen. Anschließend bringt der Rettungszug die Fahrgäste zur nachstgelegenen Station. Die dritte Mochlichkeit ist, den liegengebliebenen Zug wegzuschiben. Dies ist ggf. aber nicht mit besetzen Fahrzeugen zulässig. In thisem Fall lassst der Bediener der Leitstelle alle Fahrgäste des (dem vorausfahrenden liegengebliebenen Fahrzeug folgenden) Rettungszuges an einer Station aussteigen. Er erteilt dem Rettungszug ein Kommando, sich dem havarierten Zug

zu nahern. Anschließlich wird eine automatische fahrerlose Kupplung des Rettungszuges mit dem havarierten Zug durchgeführt. Hierfür erhält der Rettungszug eine Erlaubnis zur Annaherung an den havarierten Zug mit niedriger Geschwindigkeit. Der Rettungszug kuppelt Mechanisch mit dem havarierten Zug und bildet mit thisem einen Zugverband. Anschließlich erfolgt eine Neukonfiguration des gebildeten Zugverbandes (beispielsweise neue Zugänge). Anschließlich schiebt, bzw. zieht der Rettungszug den havarierten Zug. Der Zugverband kommt in der nachsten Station an einer Position zum Stillstand, die ein sicheres Aussteigen der Fahrgäste ermöglich. Hierbei wird die Position etwaig vorhandener Bahnsteigtüren mit berücksichtigt.

# 5.6.4 Oberfunktion Hinderniserkennung

Für den automatischen Betrieb kann jeweils am fuhrenden Drehgestell ein aktiver Bahnräumer vorgesehen werden, der durch Hindernisse im Gleisbereich ausgelöst wird. Sollte ein Gegenstand auf diesen Bahnräumer treffen, erkennen Endlagenschalter den Druck auf den Bahnräumer und losen eine nicht aufhebbare Bremsung bis zum Stillstand aus (May et al. 2012). Es wird in thisem Fall eine Meldung auf der Fahrzeuglupe (Abb. 5.20) in der besetzten Leitstelle angezeigt, sodass von Dort weitere betriebliche Maßnahmen veranlasst werden konnen (VDV 1997). Mobiles Betriebspersonal stellt durch eine Sichtkontrolle sicher, dass die die Hinderniserkennung auslösende Bedingung nicht mehr vorliegt. In thisem Fall kann das Leitstellenpersonal über eine registrierpflichtige Bedienhandlung die ausgelöste Hinderniserkennung zurücksetzen. Anschließend kann das Fahrzeug die Fahrt fortsetzen. Ein Beispiel eines aktiven Bahnräumers ist in Abb. 5.24 dargestellt.

# Abb.5.24 Aktiver

Bahnraumer zur

Hinderniserkennung am fuhrenden Drehgestell

(Beispiel: Fahrzeug vom Typ X für die fahrerlose Linie U5 der Wiener Linien)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/780b5929a0f723f21dfb26efab9a59835b3e2e3afbf4d607a6cc225fb6d599b4.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/0e365d6b60f03838d093f3f2ee9bf6a8a51d446238e9a761b0547e47d4bd9c3c.jpg)  
Abb. 5.25 Beschleunigungssensor am fuhrenden Fahrwerk zur Entgleisungserkennung (Beispiel: Fahrzeug vom Typ X für die fahrerlose Linie U5 der Wiener Linien)

# 5.6.5 Oberfunktion Entgleisungserkennung

Es mussen auf dem Fahrzeug Einrichtungen vorhanden sein, die mindestens das führende Fahrwerk auf Entgleisung überwachen konnen (Müller und Schmidt 2003). Technisch kann dies beispelsweise über Beschleunigungssensoren an den Achsen erkannt werden. Die Beschleunigungssensoren erkennen, wenn ein Räderpaar nicht mehr auf der Schiene aufsitzt. Wird eine Entgleisung erkannt, muss eine Bremsung des Fahrzeugs bis zum Still-stand erfolgen. Darüber hinaus muss die Entgleisung der besetzten Betriebsstelle gemeldet und auf der Fahrzeuglupe (Abb. 5.19) als Notfallmeldung angezeigt werden (VDV 1997). Das Personal der Betriebsleitstelle ergreift dann erforderliche betriebliche Maßnahmen wie bspw. Anhalten des Gegenverkehr's (DIN EN 62267:2010). Mobiles Betriebspersonal führt eine Sichtkontrolle am Fahrzeug durch und entscheidet vor Ort über das weitere Vorgehen. Im Falle einer fehlerhaft ausgelösten Entgleisungsmeldung wird das Leitstellen-personal informiert, welches über eine registrierpflichtige Bedienhandlung auf der Fahrzeuglupe (Abb. 5.19) die ausgelöste Entgleisungserkennung zurücksetzt. Anschließlich kann das Fahrzeug die Fahrt fortsetzen. Ein Beispiel eines am führenden Fahrwerk angebrachten Beschleunigungssensors zur Entgleisungserkennung ist in Abb. 5.25 dargeistellt.

# Literatur

Brückner N, Isailovski A (2010) CrCo - Ein Algorithmus zum Einsparen von Fahrennergie. Signal + Draht 102:43-46  
DIN EN 16334-2:2020 Bahnanwendungen - Fahrgastalarmsystem - Teil 2: Systemanforderungen für städtische Schierenbahnen. Deutsche Fassung EN 16334-2:2020  
DIN EN 62267:2010 Bahnanwendungen - Automatischer städtischer schienengebundener Personennahverkehr (AUGT) - Sicherheitsanforderungen. Deutsche Fassung EN 62267:2009

Dombrowsky H, Müller R, May A, Seitzinger E (2008) Premiere für Deutschlands erstene automatisierte U-Bahn. Nahnverkehr 26(5):8-16  
Eichner D, Uhrig B (2021) Innovationen in CBTC-Anwendungen. Signal + Draht 113:34-44. EN17168:2021-09: Platform barrier systems  
Haspel U, vom Hövel R (2001) Risikobeherrschung nach CENELEC bei der fahrerlosen Metro Kopenhagen. Eisenbahntechn Rundsch 50(7/8):418-426  
IEEE 1474.1-2004 - IEEE standard for Communications-Based Train Control (CBTC) performance and functional requirements  
Krins ST, Rudall Y, Ruiter T (2016) Ein autarkes System zur Steuerung von Bahnsteigtären. Signal + Draht 108(11):16-21  
Kuhlmeyer T (2020) Technische Abfertigungshilfen. Eisenbahningenieur 07/2020, S 46-50  
Maschek U (2018) Sicherung des Schienenverkehrs - Grundlagen und Planung der Leit- und Sicherungstechnik. Springer Vieweg, Wiesbaden  
May A, Luber T, Meier-Alt B (2012) Aktuelle Entwicklungen im Nürnberg U-Bahn-System. Eisenbahntechn Rundsch 61(1+2):40-4  
Mühleck K-H, et al (2022) Betriebliche Aufgaben im Zugbegleitdienst: Fachwissen für Zugbegleiter und Kundenbetreuer - Teil 3. Deine Bahn 10/2022, S 28-35  
Müller R, Schmidt K (2003) Eine automatische U-Bahn für Nürnberg – Technische Besonderheiten der AGT-Fahrzeuge für Nürnberg. Eisenbahntech Rundsch 52(11):679–685  
Orloff A, Aust F (2016) Controlguide OCS - Sicherung von Baustellen im Gleisbereich mit mobilen Geräten. Signal + Draht 108:39-49  
Pachl J (2016) Systemtechnik des Schierenverkehrs - Bahnbetrieb planen, steuern und sichern. Springer Vieweg, Wiesbaden  
Rahn K (2011) Green Mobility - Effiziente Zugbeeinflussung mit CBTC-Systemen. Signal + Draht 103(10):26-29  
Ritter N (2014) Signal- und Zugsicherungsanlagen für Nahverkehrsbahnen. Signal + Draht 106(11):15-25  
TR Bremse (2008) Technische Regeln für die Bemessung und Prüfung der Bremsen von Fahrzeugen nach der Verordnung über den Bau und Betrieb der Straßenbahren. Ausgabe: Dezember 2008  
Verband Deutscher Verkehrsunternehmen (1997) BOStrab-Richtlinien für den Fahrbetrieb ohne Fahrzeugfuhrer (FoF), Entwurf, Januar 1997  
Verband Deutscher Verkehrsunternehmen (2000) VDV-Schrift 399. Anforderungen an Einrichtungen zur Gewährleistung der Fahrgastssicherheit in Haltestellen bei Fahrbetrieb ohne Fahrzeugführer  
Verband Deutscher Verkehrsunternehmen (2014) VDV-Schrift 336-2. Funktionale Anforderungen für Signal- und Zugssicherungsanlagen sowie Betriebsleitsysteme des städtischen schienengebundenen Personennahverkehrs. Teil 2. Zugssicherungsanlagen. VDV, Köln  
Verband Deutscher Verkehrsunternehmen (2017) VDV-Schrift 157: Anforderungen an den Einklemm- und Verletzungsschutz sowie an Notöffnungseinrichtungen an Türen von Personenfahrzeugen nach BOStrab. VDV, Köln

# Verlässlichkeit automatischer Zugbeeinflussungssysteme

6

# SN Flashcards

Als Käfer*in diesen Buches können Sie kostenlos unsere Flashcard-App „SN Flashcards" mit Fragen zur Wissenschaftung und zum Lernen von Buch-inhalten nutzen.

1. Gehen Sieitte auf https://flashcards.springernature.com/login und  
2.(erstellen Sie ein Benutzerkonto,indem Sie ihre Mailadresse angegeben und ein Password vergeben.  
3. Verwenden Sie den folgenden Link, um Zugang zu Ihr dem SN Flashcards Set zu halten:  $\triangleright$  https://sn.pub/sK5mLQ

Sollte der Link fehlen oder nicht Funktionieren, senden Sie unsitte eine E-Mail mit dem Betreff „SN Flashcards“ und dem Buchtitel an customerservice@springernature.com

Ziel eines Bahnsystems ist die Bereitstellung einer bestimmten Stufe der Ausprüfung des Schienenverkehrs, der fahrplangemäß und safer ist. Neben den eigentlichen funktionalen Anforderungen müssen automatische Zugbeeinflussungssysteme auch nicht-funktionale Anforderungen erfüllen. Die Verlässlichkeit als Systemeigenschaft automatischer Zugbeeinflussungssysteme wird im englishen Sprachgebrauch auch mit der Abkürzung RAMSS bezeichnet. Hierbei stehen die einzelnen Buchstaben für spezifische Aspekte, die in der Systemgestaltung automatisierter Zugbeeinflussungssysteme mit berücksichtigt werden müssen.

Reliability (Zuverlüssigkeit),  
- Availability (Verfügbarkeit),  
- Maintainability (Instandhaltbarkeit),  
- Safety (Sicherheit im Sinne eines Schutzes der Umwelt vor Systemversagen),  
- Security (Angriffssicherheit, das heißt Sicherheit im Sinne eines Schutzes des Systems vor Störeinflüssen aus der externen Umwelt).

Theseinien Aspekte werden in den folgenden Abschnittn naher beleuchtet.

# 6.1 Sicherheit

Die übergeordnete Zielstellung der Betreiber von Nahverkehrssystemen ist ein sicherer und ordnungsgemäßer Betrieb. Hierbei müssen zwei unterscheidliche Aspekte betrachtet werden. Zum einen geht es um den Schutz der Fahrgäste und der Umwelt vor Systemversagen. Dies ist Gegenstand der funkionalen Sicherheit (englisch: Safety) und wird in Abschn. 6.1.1 dargestellt. Zum anderen geht es aber auch um den Schutz des Systems vor unberechtigten Zugriff Dritter (englisch: Security). Dies ist ebenfalls Gegenstand einerzielgerichteten Systemgestaltung und wird daher in Abschn. 6.1.2 dargestellt. Getreu der Devise „what's not secure is not safe" bestehen zwischen diesen beiden Sicherheits-aspekten Wechselwirkungen.

# 6.1.1 Funktionale Sicherheit (Safety)

Sicherheit ist die „Freiheit von unvertretbaren Risiken“. Das Risiko ist hierbei die Kombination aus der Wahrscheinlichkeit, mit der ein Schaden auftritt und dem Ausmaß diesen Schadens. Hierfür hat sich in den hierfür relevanten Normen (DIN EN 50126-1:2018-10; DIN EN 50129:2019-06) ein Verfahren etabliert, welche im Entwicklungsprocess eine klar definierte Schnittstelle zwischen den Betriebsanforderungen des Betreibers einschließlich der Umgebung und dem Sicherungssystem als der technischen Lösung des Herstellers etabliert. Hinsichtlich der Sicherheit wird diese Schnittstelle durch eine List von Gefährduren bestimmt, die zu einem Unfall führen können. Das Ergebnis der Risiko-analysen sind Gefährungsstraten, die mit dem Zugsicherungssystem verbunden sind. Wenn das mit dem Zugsicherungssystem verbundene Risiko geringer als ein vorgegebener Risikogrenzwert ist, dann werden diese Gefährungsstraten tolerierbare Gefährungsstraten (Tolerable Hazard Rate, THR) genannt.

In thisem Zusammenhang sind die Aufgaben des Betreibers die folgenden:

- FestlegungfunctionalerAnforderungen fur das betreffende System. Die Anforderungen sind zunachst unabhängig von dessen konkreter technischer Ausführung. Hierbei kann auf einschlagige Standards zurückgegriffen werden. So enthalt beispielese DIN EN

62267 auf hoher Betrachtungsebene gehaltene Sicherheitsanforderungen. Diese sind anwendbar auf automatische städtische fahrer- oder begleiterlose Systeme, die auf einem (vom übrigen Verkehr) unabhängigen Bahnkörper verkehren (DIN EN 62267:2010).

- Identification systemrelevanter Gefährdungen: Die Gefährungsidentifikation beinhaltet eine systematische Analyse eines Systems. Diese hat zum Ziel, Gefährdungen, die sich während des Lebenszyklusses eines Systems ergeben konnen, zu erkennen.  
- Analyse der Folge von Gefährdungen: Die Folgenanalyse befasst sich mit der Quantifizierung wahrscheinlicher Konsequenzen, die sich aus einer identifizierten Gefährdung ergeben können.  
- Um sicherzustellen, dass das gewährte Risiko tolerierbar ist, konnen verschiedene Risikoakzeptanzprinzipen zur Anwendung kommt (Anwendung von Regelwerken, Vergleich mit Referenzsystemen oder eine explizite Risikoabschätzung). Nach der Wahl und Anwendung des Risikoakzeptanzprinzips wird der Prozess mit der Risikobeurteilung und der Festlegung von Sicherheitsanforderungen fortgesetzt.  
- Ableitung tolerierbarer Gefährungsstraten, beispelssweise mittels einer geeigneten Risikoanalysemethode (Braband 2005).

Der Hersteller ist verpflichtet, eine Gefährungsbeherrschung zu argumentieren. Dies umfasst die folgenden Aspekte:

- Festlegung der konkreten Systemarchitektur unter Berücksichtigung der tolerierbaren Gefährungsstraten für jeder Gefährung.  
- Analyse der Ursachen für jeder Gefährlung.  
- Verfeinerung der Sicherheitsanforderungen im Sinne einer Zuweisung der Geldaufnahmssatz, SIL) auf die betreffenden Teilsysteme.  
- Dokumentation eines Sicherheitsnachweises (englisch: Safety Case). Der zentrale Bestandteil des Sicherheitsnachweises ist der Technische Sicherheitsbericht (englisch: Technical Safety Report). Gegenstand des Sicherheitsnachweises ist die Betrachtung des korrekten funktionalen Verhaltens des Systems. Dies bedeutet, dass alle in der Risikoanalyse identifizierten Gefährdungen durch Schutzfunktionen des Zug-sicherungssystems auch tatsächlich erfüllt werden. Ebenfalls wird gezeigt, dass Ausfallauswirkungen (Einfach- und Mehrfachausfälle) beherrsch werden, sowie ein siche-rer Betrieb beiethoden externen Umwelteinflüssen sichergestellt werden kann (vgl. DIN EN 50129:2019-06). In Bezug auf die Kommunikation zwischen Fahrzeug- und Streckeneinrichtungen mussen Gefährdungen durch Wiederholung, Auslassung, Ein-fugung, Verfalschung, Verzögerung und Manipulation übertragener Informationen beherrsch werden. Hierfür sind technische Maßnahmen zur Absicherung der Ende-zu-Ende-Verbindung in einschlögigen Standards für Bahnanwendungen (vgl. DIN EN 50159:2011-04) vorgegeben.

Wegen der großen Bedeutung der Risikoanalyse wird diese nachfolgend vertieft behandelt. Die DIN EN 50126 legt für die Durchführung der Risikoanalyse kein bestimmtes Verfahren fest. Zur Einstufung des Risikos schlägt sie qualitative Kategorien für die Häufigkeit und den Schweregrad vor. Die Risikobewertung muss durch Kombination der Häufigkeit des Eintritts eines Gefahrenfalls mit der Schwere der Konsequenzen erfolgen. Die Risikobewertung soll im Ergebnis eine qualitive Kategorie ermitteln, die der notwendigen Risikominderung entspricht. Aus der notwendigen Risikominderung konnen dann Sicherheitsintegratssanforderungen (Sicherheitsintegritätsslevel, SIL) abgeleitet werden.

Es besteht eine Vielzahl verschiedener methodischer Ansätze für die Durchführung von Risikoanalysen. Diese können in qualitative Ansätze (beispielsweise Expertenschätzungen), semi-quantitative Ansätze (beispielsweise Risikographen) oder quantitative Ansätze (beispielsweise simulationsbasierte Ansätze) unterschieden werden. Da eine gesamte Darstellung der Bandbreite verschiedener Risikoanalysemethoden den Rahmen dieseres Buches sprengen wurde, wird im Folgenden exemplarisch auf zwei ausgewählte semi-quantitative Risikoanalysemethode eingegangen. Für eine umfassende Darstellung wird auf weiterführende Fachliteratur verwiesen (Schnieder und Schnieder 2013).

# Ermittlung der Sicherheitsintegratitsanforderung mittels Risikograph

Der Verband Deutscher Verkehrsunternehmen hat in (VDV 2008) einen Vorschlag ausgarbeitet, wie der Risikograph nach DIN EN 61508-5 für Zugsicherungsanlagen genutzt werden kann. Eine analoge Anwendung des Risikographen zur Ermittlung sicherheitstechnischer Anforderungen für die elektrische Ausrüstung von Schienenfahrzeugen erfolgt in (VDV 2005) und (VDV 2009). Für die Bestimmung der Risikominderung werden insgesamt vier verschiedene Risikoparameter verwendet. Die Auswahl der Risikoparameter sowie die darauf basierende Ableitung des Sicherheitsintegritätslevels (SIL) wird exemplarisch für die Funktion der Überwachung der vorgegebenen Grenzgeschwindigkeit (abhängig von der Streckentopografiaie, vorübergehenden Langsamfahrstellen, Nothalten oder Zielpunkten) dargestellt. Die Auswirkung beim Fehlerfall dieser Schutzfunktion ist, dass eine Überschreitung der vorgegebenen Grenzgeschwindigkeit nicht erkannt wird und darüber keine Zwangsbremsung erfolgt. Dies kann letzt den Endes zu einem Zusammenstoß mit anderen Fahrzeugen oder zu einer Entgleisung führen. Die Risikoparameter konnen für das gewährte Beispiel wie folgt gewählt werden:

- Bestimmung der Auswirkung des Vorfalls  $C$  (Consequence) mit den Merkmalsauspragungen von geringen Verletzungen (C1), schweren irreversiblen Verletzungen einer oder mehrerer Personen oder dem Tod einer Person (C2), dem Tod mehrerer Personen (C3) oder dem Tod sehr vieleren Personen (C4). Im gewählten Beispiel muss bei einer Entgleistung oder einem Zusammenstoß von Zügen mit maximal mehreren Totengerechnet werden. Deshalb wird für den Risikoparameter C für das gewählte Beispiel die Ausprüfung C3 gewählt.  
- Bestimmung der Häufigkeit und Zeit des Aufenthalts im Gefahrenbereich  $F$  (Frequency) mit den Merkmalsausprüngungen eines seltenen bis früerten Aufhalt im gefährlichen

Bereich (F1), oder einem früfigen bis dauernden Aufenthalt im gefährlichen Bereich (F2). In dem gewählten Beispiel ist von einem dauerhaften Fahrgastaufenthalt in den Zügen auszugehen. Deshalb wird für den Risikoparameter F die Ausprüfung F2 gewählt.

- Bestimmung der Möglichkeit, den gefährlichen Vorfall zu vermeiden  $P$  (Probability) mit den Ausprüungen der Möglichkeit unter bestimmten Bedingungen (P1) oder der Unmöglichkeit zur Vermeidung eines gefährlichen Vorfalls (P2). Im gewählten Beispiel besteht keine Möglichkeit zur Vermeidung eines gefährlichen Vorfalls. Deshalb wird für den Parameter P die Ausprüfung P2 gewählt.  
- Bestimmung der Wahrscheinlichkeit des unerwünschten Ereignisses W mit den Merkmailen einer sehr geringen Wahrscheinlichkeit unerwünschter Ereignisse und nur weniger unerwünschten Ereignissen (W1), einer geringen Wahrscheinlichkeit unerwünschter Ereignisse und nur weniger unerwünschten Ereignissen (W2) oder einer relativ hohen Wahrscheinlichkeit, dass unerwünschte Ereignisse auftreten und*häufige unerwünschte Ereignisse sind wahrscheinlich (W3). Im gewählten Beispiel ist mit einem unmittelbaren Eintritt der Gefährung bei einer Geschwindigkeitsüberschreitung des Fahrzeugs zu rechnen. Aus thisem Grund wird fur den Risikoparameter W die Ausprüfung W3 gewählt.

Abb. 6.1 zeigt, wie die Auswahr der einzelnen Risikoparameter im Risikograph zu einer nachvollziehbaren Ableitung eines Sicherheitsintegratätslevels für die betrachtete Funktion führt (VDV 2008). Demnach ist die betrachtete Funktion mit einem Sicherheitsintegratätslevel SIL 4 auszulegen.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/4c5fc8eab80838c772974855b728986f00818e23ae2baa8d0a4941c850ff60ce.jpg)  
Abb.6.1 Bestimmung des Sicherheitsintegratitslevels (SIL) nach VDV-Schrift 331

# Ermittlung der Sicherheitsintegritätsanforderung mittels Risikomatrix

Ein weiterer semi-quantitativer Ansatz der Risikoanalyse ist die Risikomatrix nach DIN EN 50126-1. Hierfür müssen die beiden Risikokomponenten der Wahrscheinlichkeit oder der Häufigkeit des Aufretens von Ereignissen sowie des Schweregrads des etwaigen Schadens für mögliche betrieblicher Gefährdungen anhand qualitativer Kriterien ermittelt werden. In einem deutschen CBTC-Projekt wurden die qualitativen Kategorien für die Gefährungsrate  $\lambda$  (gefährliche Ereignisse pro Stunde) wie folgt definiert:

- Häufig: Das Ereignis wird Häufig staatfinden (tolerierbare fonctionale Ausfallrate  $\lambda < 10^{-5} / \mathrm{h}$ ; anzuwenden ist Sicherheitsintegritätslevel SIL 0)  
- wahrscheinlich: Das Ereignis wird voraussichtlich oft auftreten (tolerierbare Funktionale Ausfallrate  $10^{-6} / \mathrm{h} < \lambda \leq 10^{-5} / \mathrm{h}$ ; anzuwenden ist Sicherheitsintegratitslevel SIL 1)  
- gelegentlich: Das Ereignis wird voraussichtlich mehrere Male aufreten (tolerierbare Funktionale Ausfallrate  $10^{-7} / \mathrm{h} < \lambda \leq 10^{-6} / \mathrm{h}$ ; anzuwenden ist Sicherheitsintegratitslevel SIL 2)  
- setten: Es kann davon ausgegangenen werden, dass das Ereignis auftreten wird (tolerierbare Funktionale Ausfallrate  $10^{-8} / \mathrm{h} < \lambda \leq 10^{-7} / \mathrm{h}$ ; anzuwenden ist Sicherheitsintegratits-level SIL 3)  
- unwahrscheinlich: Es kann angenommen werden, dass das Ereignis ausnahmsweise auftenen kann (tolerierbare Funktionale Ausfallrate  $10^{-9} / \mathrm{h} < \lambda \leq 10^{-8} / \mathrm{h}$ ; anzuwenden ist Sicherheitsintegratitslevel SIL 4)  
sehr unwahrscheinlich: Es kann angenommen werden, dass das Ereignis nicht auftritt (tolerierbare funktionale Ausfallrate  $\lambda \leq 10^{-9} / \mathrm{h}$ ; anzuwenden ist Sicherheitsintegratits-level SIL 4)

Im gleichen Projekt wurden - gingefüglich von der DIN EN 50126-1 abweichend - die folgenden qualitativen Kategorien für das Schadensausmaß verwendet:

- katastrophal: Unfalltote und/oder zahlreiche Schwerverletzte (und/oder schwere Umweltschäden)  
- kritisch: einzelner Unfalltoter und/oder Schwerverletzter (und/oder nennenswerte Unfallschäden)  
- marginal: petite Verletzung (und/oder nennenswerte Bedrohung der Umwelt)  
- unbedeutend: mögliche gingüige Verletzung

Die Kategorien des Schadensausmaßes und der Schadensschwere können in einer Matrix miteinander verschränkt werden. Die Kategorien für den Schweregrad sind hierbei in der horizontalen Achse dargestellt. Die Kategorien für die Häufigkeit einer Gefährdung sind in der vertikalen Achse dargestellt. Jedes der Felder der Matrix entspricht einem Risiko als Kombination von Häufigkeit und Schadensschwere. Jedem dieser Risiken kann nun eine Risikoakzeptanzkategorie zugeordnet werden. In dem zuvor geschilderten Projekt wurden nach DIN EN 50126-1 die Risikoakzeptanzkategorien wie folgt gewählt:

- untragbar: Das Risiko muss eliminiert werden (rote Farbcodierung in der Risikobewertungsmatrix).  
- unerwünscht: Das Risikoarfurakzeptiert werden, wenn eine Minderung nicht durchfuhrbar ist und die Zustimmung des Betreibers oder der Technischen Aufsichtsbehörde vorliegt (orangefarbene Farbcodierung in der Risikobewertungsmatrix).  
- tolerierbar: Das Risiko kann unter der Voraussetzung angemessener Maßnahmen (z. B. Instandhaltungsverfahren und -regeln und mit Zustimmung des Betreibers) toleriert und akzeptiert werden (gelbfarbene Farbcodierung in der Risikobewertungsmatrix).  
- vernachlässigbar: Das Risiko ist ohne Zustimmung des Betreibers akzeptabel (grüne Farbcodierung in der Risikobewertungsmatrix).

Die Anwendung der Risikomatrix soll auch hier mit der Funktion der Überwachung der vorgegebenen Grenzgeschwindigkeit verdeutlicht werden. Im Fehlerfall dieser Schutzfunktion überschreitet der Zug die zulässige Geschwindigkeit und das Fahrzeuggerät gibt in thisem Fall fehlerhaft keinen Zwangsbremsbefehl aus. Die Anwendung der Risikomatrix soll die Frage beantworten, mit welcher Sicherheitsintegrität diese Funktion bereitgestellt werden muss.

Die Durchführung der Risikoanalyse beginnnt mit einer Bewertung des initialen Risikos (vor risikoreduzierenden Maßnahmen). Hierbei wird die Häufigkeit des Überschreitens des Geschwindigkeitsgrenzwertes als „gelegentlich“ angenommen. Das Schadensausmaß wird hierbei jeder als „katastrophal“ angenommen, weil mit tölich verunglickten Fahrgästen gerechnet werden muss. Die Verknüpfung von Häufigkeit und Schadensschwere führt in der Risikobewertungsmatrix zu einem als „untragbar“ bewerteten Risiko. Das Ergebnis der initialen Risikobewertung ist in Abb. 6.2 als dunkelgrau hinterlegter Kreis vermerkt. Für diese Risiko ist eine Reduktion zwingend erforderlich.

Das Risiko kann reduziert werden, wenn beispissewe die Häufigkeit des gefährlichen Ereignisses reduziert wird. Dies gelingt beispissewe, wenn die Funktion mit einer higheren Sicherheitsintegritätstufe entwickelt wird. Die Annahme ist hierbei, dass bei einem higheren Sicherheitsintegritätslevel durch umfangreichere Maßnahmen im Entwurf und der Implementierung der Schutzfungtion zum einen zufällige Fehler im Betrieb

<table><tr><td colspan="5">Risikobewertungsmatrix nach DIN EN 50126-1</td></tr><tr><td rowspan="2">Häufigkeit einesGefahrenfalls</td><td colspan="4">Gefahrenstufen</td></tr><tr><td>unbedeutend</td><td>marginal</td><td>kritisch</td><td>katastrophal</td></tr><tr><td>häufig</td><td>unerwänscht</td><td>untragbar</td><td>untragbar</td><td>untragbar</td></tr><tr><td>wahrscheinlich</td><td>tolerabel</td><td>unerwänscht</td><td>untragbar</td><td>untragbar</td></tr><tr><td>gelegentlich</td><td>tolerabel</td><td>unerwänscht</td><td>unerwänscht</td><td>untragbar</td></tr><tr><td>selten</td><td>vernachlässigbar</td><td>tolerabel</td><td>unerwänscht</td><td>unerwänscht</td></tr><tr><td>unwahrrscheinlich</td><td>vernachlässigbar</td><td>vernachlässigbar</td><td>tolerabel</td><td>unerwänscht</td></tr><tr><td>sehr unwahrscheinlich</td><td>vernachlässigbar</td><td>vernachlässigbar</td><td>vernachlässigbar</td><td>tolerabel</td></tr></table>

Abb.6.2 Bestimmung des erforderlichen Sicherheitsintegratitslevels (SIL) nach DIN EN 50126-1

sicher beherrsch und zum anderen gefährliche Systemzustände durch mögliche systematische Fehler vermieden werden konnen. Es stellt sich also die Frage, wie welt die Häufigkeit reduziert werden muss, um das Restrisiko (englisch: residual risk) in den Bereich eines mindestens „tolerierbaren“ Risikos zu bringen. In thisem Fall wurde das Restrisiko mit Einschränkungen (bspw. Umsetzung angemessener Maßnahmen und Zustimmung des Betreibers, siehe oben) akzeptabel. Mit Blick auf die Risikobewertungsmatrix damit die Häufigkeit für ein tolierbares Risiko bei gleichzeitig katastrophalem Schadenausmaß nur „sehr unwahrscheinlich“ sein. Die tolierbare Gefährungsrate in dieser Fall liegt gemäß Risikobewertungsmatrix bei  $\lambda \leq 10^{-9} / \mathrm{h}$ . Dies entspricht einer Sicherheitsintegritätsstufe SIL4. Das Ergebnis der Bewertung des Restrisikos ist in Abb. 6.2 als hellgrau hinterlegter Kreis dargestellt. Der Pfeil zwischen dem dunkelgrauen und dem hellgrauen Kreis symbolisiert die erreichte Risikoreduktion. Es sind also gemäß DIN EN 50129 umfangreiche Maßnahmen zur Vermeidung systematischer Fehler, bzw. zur sicheren Beherrschung zufälliger Fehler im Betrieb umzusetzen.

# 6.1.2 Angriffssicherheit (Security)

Stadtische Schierenverkehrssysteme sind kritische Verkehrsinfrastrukturten (vgl. BSI-KritisV 2016). Ihr Funktionieren ist für die Wirtschaft und unser gesellschaftliches Zusammenleben essenziell. Schutzziele bezeichneten hier den Zustand von Verkehrssystemen, der bei einem unberechtigten Zugriff Dritter erhalten bleiben soll. Insgesamt werden vier verschiedene Schutzziele unterschieden: die Verfügbarkeit, die Integrität, die Authenticität sowie die Vertraulichkeit. Die effektive Erreichung der zuvor genannten Schutzziele in kritischen Verkehrsininfrastrukturten erfordert das aufeinander abgestimmte Zusammenwirken von technischen, organisatorischen, und physischen Schutzmaßnahmen. Ein solch umfassendes Schutzkonzept wird auch als „tiefgestaffelte Verteidigung“ (englisch: Security in depth) bezeichnet (Schnieder 2020). Dieser Konzeption liegt die Vorstellung zu Grunde, dass eine einzeln Schutzmaßnahme allein keinem ausreichenden Schutz gegen unberechtigten Zugriff Dritter bietet. Die wirksame Anordnung mehrerer voneinander unabhängiger Barrieren vermag jeder die Wahrscheinlichkeit eines erfolgreichen Zugriffs von außen deutlich zu reduzieren. Die verschiedenen Kategorien der Schutzmaßnahmen werden nachfolgend vorgestellt.

- Technische Schutzmaßnahmen: Eine zentrale Komponente von CBTC-Systemen ist das Datenübertragungssystem, welche eine sichere, zeitgerechte und zugriffsgeschützte Übertragung von Informationen zwischen Fahrzeug - und Streckeneinrichtungen ermögen muss. Hierbei ist vor allem auch ein unberechtigter Zugriff oder eine Manipulation der Daten zu verhindern. Daher werden CBTC-Systeme durch eine Security-Architektur gegen unberechtigte Zugriffe Dritter geschützt (zum Beispiel durch Firewalls). Die Auswahl technischer Schutzmaßnahmen gegen einen unberechtigten

Zugriff Dritter erfolgt auf der Grundlage internationaler Standards (vgl. DIN IEC 62443-3-3:2015-06). Beispiele von technischen Maßnahmen sind eine Verschlussung und Authentifizierung über Internet Protocol Security (IPsec) unter Verwendung von kryptografischen Hash-Funktionen (beispelsweise HMAC-SHA-256) sowie zusätzliche technische Maßnahmen wie ein zyklischer Schlüsselaustausch.

- Organisatorische Schutzmaßnahmen: Für einen umfassenden Schutz der für die Verkehrsteuerung erforderlichen informationstechnischen Systeme ist die Einrichtung eines umfassenden Informationssicherheitsmanagementsystems (ISMS) durch das Verkehrstunnehmer ratsam (Schnieder und Magerkurth 2018a). Vorgaben an ein solches Managementsystem ergeben sich unter anderen aus dem internationalen Standard DIN EN ISO 27001. Hierbei werden, einem risikoorientierten Ansatz folgend, bestehende Angriffspunkte für unberechtigte Zugriffe von außen identifiziert und geschlossen. Darüber hinaus werden organisatorische Vorkehrungen getroffen im Sinne verbindlich definieter Prozesse, Rollen und Verantwortlichkeiten, um unberechtigte Zugriffe zu offenbaren und durch eine prompte Reaktion (Schnieder und Magerkurth 2018b) zügig zu schreiben.  
- Maßnahmen des physischen Zugriffsschutzes: Gewisse Bedrohungen setzen einen direkten (physischen) Zugriff auf die informationstechnischen Systeme des Betreibers voraus. Ein möglicher Angreifer muss für einen erfolgreichen Zugriff auf konkrete Assets in mehrere Schutzzonen eindringen. Durch die Anordnung von Alarmsystemen, Zutritskontrollsystemen sowie der Auswahl von Schliebsystemen wirsamer Widersstandsklassen wird ein unberechtigter Zugriff wesentlich erschwert.

# 6.2 Verfügbarkeit (Availability)

Die Verfugbarkeit automatisierter Zugbeeinflussungssysteme ist für ihren sicheren Betrieb essenziell. Verfugbarkeit bezeichnet „die Fähigkeit eines Produkts, in einem Zustand zu sein, in dem es unter vorgegebenen Bedingungen zu einem vorgegebenen Zeitpunkt oder während einer vorgegebenen Zeitspanne eine geforderte Funktion erfüllen kann unter der Voraussetzung, dass die geforderten äußerten Hilfsmittel bereitstehen.“ (DIN EN 50126-1: 2018). Eine Maximierung der Verfugbarkeit lässt sich herunterbrechen auf mehrere Teilaspekte:

- Minimierung der mittleren Ausfallzeit: Dieses Ziel wird durch die Verbesserung der Instandhaltbarkeit (Maintainability) erreicht. Dies ist in Abschn. 6.2.1 beschrieben.  
- Maximierung der mittleren Klarzeit: Dieses Ziel wird durch die Erhöhung der Zuverlösigkeit (Reliability) erreicht. Dies ist in Abschn. 6.2.2 beschrieben.  
- Fehlertoleranz: Gestaltung der technischen Systeme, dass dieseriotz Beeinträchtigung einzelner Komponenten ihre Funktion dennoch erfüllen. Dies ist in Abschn. 6.2.3 beschreiben.

# 6.2.1 Optimierung der Instandhaltbarkeit (Maintainability) zur Steigerung der Verfügbarkeit

Die Minimierung der mittleren Ausfallzeit (englisch: mean down time, MDT) ist ein weiterer Ansatzpunkt zur Steigerung der Verfügbarkeit des städtischen Schienenverkehrssystems (vgl. Abb. 6.3). Zu dieser Zweck werden die Zugsicherungsanlagen entsprechend instandhaltbar gestaltet. Hierbei bezeichnet Instandhaltbarkeit (Maintainability), die Wahrscheinlichkeit, dass für eine Komponente unter gegebenen Einsatzbedingungen eine bestimmte Instandhaltungsmaßnahme innerhalb einer festgelegten Zeitspanne ausgeführt werden kann". Hierbei wird zwischen einer préventiven und einer korrektiven Instandhaltung unterschieden. Präventive Instandhaltung bezeichnet hierbei die Instandhaltung in vorgegebenen Zeitabständen oder nach vorgegebenen Kriterien, die zur Verringerung der Ausfallwahrscheinlichkeit oder der Vermeidung der Verschlechterung der Funktion einer Einheit vorgesehen ist (DIN EN 50126-1:2018-10). Demgegenüber handelt sich bei der korrektiven Instandhaltung um die nach Erkennung des Fehlzustands durchgeführte Instandhaltung, die das Produkt wieder in einen Zustand versetzt, in dem es eine geforderte Funktion erfüllen kann (DIN EN 50126-1:2018-10). Bezüglich der korrektiven Instandhaltungsaktivitäten können verschiedene Ebenen unterschieden werden:

- Erste Instandhaltungsebene: Auf dieser Ebene erfolgt die Lokalisierung und der Aus-tausch einer fehlerhaften kleinsten tauschbaren Einheit (line replaceable unit, LRU). Dies schlieBt Test- und Nachweisaktivitäten mit ein. Die defekte kleinste tauschbare Einheit wird der zweiten Instandhaltungsebene übergeben. Aktivitäten der ersten Instandhaltungsebene werden an der Strecke oder direkt auf dem Fahrzeug in der Werkstatt durchgefuhrt. Für diese Tätigkeiten werden Werkzeuge wie Messinstrumente und Laptops benötigt (Guizard 2006).  
- Zweite Instandhaltungsebene: Diese Instandhaltungsebene identifiziert den Fehler und ersetzt das fehlerhafte Bauteil in derkleinsten tauschbaren Einheit (beispelsweise eine fehlerhafte Baugruppe in einem Baugrupppenträger). Es erfolgt ein abschlussender Funktionstest. Die fehlerhafte Komponente wird der dritten Instandhaltungsebene übergeben, wohingegen die funktionsfähige kleiste tauschbare Einheit der ersten Instandhaltungsebene übergeben wird. Aktivitäten der zweiten Instandhaltungsebene erfolgen in der Werkstatt, da spezielle Werkzeuge für die Wiederherstellung der Funktionsfähigkeit erforderlich sind (Guizard 2006).

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/d6e8c2fe16d6e056ac8543df81e45b35d0663fa610f6042bc27fa56ae0772e58.jpg)  
Abb.6.3 Zusammenhang der Kenngroßen der Verfügbarkeit

- Dritte Instandhaltungsebene: Diese Instandhaltungsaktivitäten erfolgen beim Hersteller. Hier werden fehlerhafte Bauteile identifiziert und getauscht. Es erfolgt ein Funktionstest. Die reparierte Baugruppe wird der zweiten Instandhaltungsebene bereitgestellt. Diese Instandhaltungsebene erfordert spezielle Prüfadapter, die nur beim Hersteller zur Verflügung stehen (Guizard 2006).

Die Instandhaltbarkeit kann durch die folgenden Aspekte positiv beeinflusst werden, um in der Praxis möglichst kurze Zeiten zur Wiederherstellung der Betriebsfähigkeit des städtischen Schierenverkehrssystems nach Störungen zu erreichen:

- Diagnosesysteme: Jede technische Komponente sowohl der streckenseitigen als auch der fahrzeugseitigen Einrichtungen wird kontinuierlich auf ihre Funktionsfähigkeit überwacht. Da die Fahrzeuge durch den Streckenatlas und die fahrzeugautarke Ortung über weitreichende Informationen verfügen, konnen sie von ihren erkannte Ausfälle oder Abweichungen in der Infrastruktur an die Leitstelle melden. Beispiele hierfür sind erkannte defekte Transponder entlang der Strecke oder erkannte zu geringe Feldstärken der streckenseitigen Access Points des Datenübertragungssystems. Ist eine Komponente ausgefallen, wird dies offenbart und eine Störmdellung in der Leitstelle angezeigt. Auf Basis der lokalisierten Fehler konnen voraussichtlich erforderliche Ersatzteile bestimmt werden und je nach Dringlichkeit der Fehlerbehebung Maßnahmen zur Entstörung (beispielsweise Abarbeitung von Wartungsaufträgen am Tag oder in der Nachsperrpause) disponiert werden.  
- Tauschkomponenten: Die Hersteller geben für jeder eingesetzte Komponente eine Mean Time Between Failures (kurz MTBF) an. Dies ist die englishe Bezeichnung für die mittlere Betriebsdauer zwischen Ausfallen für reparierbare Einheiten. Unter „Betriebsdauer" versteht man die Betriebszeit zwischen zwei aufeinanderfolgenden Ausfallen einer instandsetzbaren Einheit. Zusammen mit dem Mengengerüst der gesamten Anlage und den logistischen Verzugsdauern (Lieferfristen der Hersteller) kann der erforderliche Ersatzteilbedarf abgeschätzt werden, sodass der Hersteller für einen ausreichenden Ersatzteilvorrat sorgen kann.  
- Ausgebildetes Personal: Für die Instandhaltung ist qualifiziertes Personal erforderlich. Die Einführung hochautomatisierter Zugbeeinflussungssysteme erfordert für die Verkehrsrunternehmen eine Anpassung ihrer Organisation. Dies liegt in zwei Effekten begründet. Zum einen verlagern sich die Instandhaltungsaktivitäten durch die deutlich reduzierten Außenanlagenkomponenten und die aufwändigere Instandhaltung der Fahrzeugeinrichtungen in den Betriebshof. Zum anderen verändern sich insbesondere für die Instandhaltung der Infrastruktur die durchzuführenden Instandhaltungsaktivitäten deutlich, da nun – in deutlichem Gegensatz zu traditionellen signaltechnischen Systemen – fast ausschließlich Netzwerkkomponenten instandzuhalten sind (Rüffer et al. 2019). Insbesondere bei fahrerlosem Betrieb ist für die Beurteilung von Zeiten zur Entstörung und zur Wiederherstellung des Regelbetriebs auch die Frage relevant, wo sich Betriebspersonal aufhält, welches auf die Fahrzeuge im Störungsfall bedieten kann.

Beim unbegleiteten fahrerlosen Betrieb (UTO) sind – sofern keine Möglichkeit zur situativen Fernsteuerung des Fahrzeugs aus der Leitstelle Heraus gegeben ist – möglicherweise erhebliche Verzugszeiten durch erforderliche Fußwege des Betriebspersonals zum gestörten Fahrzeug zu berücksichtigten.

- Remote Software Update: Gerade bei einer groben Fahrzeugflotte stellen sich Softwareupdates als außerordentlich aufwändig hers aus. Die Hersteller von CBTC-Systemen bieten thereof Lösungen zum sicheren Fernladen von Fahrzeugeinrichtungen über drahtlose Kommunikationsysteme an. Dies spart Zeit und Ressourcen in der Instandhaltung.

# 6.2.2 Erhöhung der Zuverlösigkeit (Reliability) zur Steigerung der Verfügbarkeit

Die Maximierung der mittleren Klarzeit (engl.: mean up time, MUT) ist ein Ansatzpunkt zur Steigerung der Verfügbarkeit des städtischen Schienenverkehrssystems (vgl. Abb. 6.2). Zu diesen Zweck werden die Fahrzeug- und Streckeneinrichtungen entsprechend zuverlüssig gestaltet. Zuverlösigkeit bezeichnet hierbei die „Wahrscheinlichkeit damit, dass eine Einheit ihre geförderte Funktion unter gegebenen Bedingungen für eine gegebene Zeitspanne [...] erfüllen kann". Durch die folgenden Maßnahmen in der Gestaltung elektronischer Systeme kann auf die Zuverlöigkeit Einfluss genommen werden:

- Einsatz betriebsbewährter Komponenten: Eine Komponente gilt als betriebsbewährt, wenn eine entsprechend dokumentierte Untersuchung ergeben hat, dass Nachweise aus früheren Einsatz belegen, dass die Komponente für den Einsatz in einem sicherheitstechnischen System geeignet ist. Hierbei werden hohe Anforderungen an die Dokumentation von Felderfahrens gestellt. So muss beispelsweise die Spezifikation unverändert sein und es dürfen keine oder nur unbedeutende Fehler aufgetreten sein. Außen dem müssen die Beobachtungen auf einer ausreichenden Anzahl an Betriebsstunden beruhen.  
- Einsatz qualifizierter Komponenten: dieser Ansatz ist insbesondere in der Automobilindustrie ausgeprägt. Die Qualifizierung elektronischer Komponenten kann Branchenstandards folgen. Um eine Qualifizierung gemäß dieser Standards zu erhalten, muss eine Komponente einen strengen Prozess mit entsprechenden Prüfungen bestehen (bspw. Klimatests).  
- Derating: Üblicherweise besteht eine Reserve zwischen den Konstruktsgrenzen eines Bauteils und den im Betrieb auftretenden Belastungen. Somit ist ein Bauteil oder System, dass unterhalb seiner Auslegungsgrenze betrieben wird, zuverlässiger als ein Bauteil, das an oder oberhalb seiner Auslegungsgrenze betrieben wird. Durch Derating kann also die Zuverlässigkeit erhöht, bzw. die Lebensdauer einer Komponente gesteigert werden.  
- Fehlererkennung und Fehlerkorrektur: Bei der Speicherung, Verarbeitung und Übertragung von Daten können Fehler auftreten. Fehler entstehen hierbei durch das Ändern, Löschen oder Hinzufügen von Bits. Beim Behandeln von Fehler gibt es zwei Möglichkeiten. Die Fehlererkennung zeigt an, dass ein Fehler aufgetreten ist. Bei der Fehlerkorrektur wird der Fehler nicht nur erkannt, sondern auch gleich behoben.

# 6.2.3 Fehlertolerante Systeme zur Steigerung der Verfügbarkeit

Technische Systeme, die/TRZ Beeinträchtigung einzelner Komponenten ihre Funktion weiterhin erfüllen, werden als fehlertolerant bezeichnet. Redundanz bezeichnet hierbei das Vorhandensein von mehr als für die sichere Ausführung der vorgesehenen Aufgabe notwendigen Mittel. Die Anwendung von Redundanz führt dazu, dass eine Betrachtungs-heit ihre vorgesehene Aufgabe auch ei einer begrenzten Anzahl von Ausfallen auch weiterhin ausführten kann. Betrachtungseinheiten, für die diese Eigenschaften zuteffen, bereits fehlertolerant. In Bezug auf die Umsetzung der Fehlertoleranz konnen unterscheid-liche Redundanzkonzepte entsprechenden werden:

- Funktionsbeteiligte Redundanz (heiße Redundanz, english: active redundancy): Wahlrend des fehlerfrei Betriebs sind alle mehrfach vorhandenen Systemkomponenten an der Funktionserfüllung beseitigt. Im Fehlerfall übernehmen die intakten Komponenten die Aufgabe der defekten Komponente unverzüglich.  
- Nicht funktionsbeteiligte Redundanz (Standbyredundanz, english passive redundancy): Redundanz, bei der die zusätzlichen Mittel eingeschaltet sind, aber erst bei Störung oder Ausfall an der Ausführung der vorgesehenen Aufgabe beteiligt sind.  
- Kalte Redundanz (englisch: cold redundancy): Redundanz, bei der die zusätzlichen Mittel zur Ausführung der vorgesehenen Aufgabe erst bei Störung oder Ausfall eingeschaltet werden.

Beiselhafte Ansätze der Gestaltung fehltoleranter Systeme sind nachfolgend in Bezug auf die einzelnen Systemkomponenten von CBTC-Systemen aufgeführ:

- Die Fahrzeugeinrichtungen verfügen über eine so genannte „Head-Tail-Redundanz“. Das bedeutet, dass es in jedem Zug zwei sichere Rechner gibt (jeweils einen an jedem Ende des Zuges). Im Normalbetrieb ist eine Fahrzeugeinrichtung aktiv und die Fahrzeugeinrichtung am anderen Fahrzeugende ist passiv. Die passive Fahrzeugeinrichtung hat keine Kontrolle über den Zug, verfügt aber in seinen Streckenatlas über ein aktuellen Prozessabbild. Die aktive Fahrzeugeinrichtung ist nicht notwendigerweise diejenige am vorderen Ende des Zuges. Um die Ausfallsicherheit zu verbessern, ist das System mit einer automatischen, nahtlosen Umschaltung zwischen den beiden Fahrzeugeinrichtungen an Bord ausgestattet.  
- DiezentralenStreckeneinrichtungen sind ebenfals mehrkanalig ausgelegt. Hierkommen für die sicheren Rechner der CBTC-Streckenzentrale beispielsweise 2-von-3 Rechnersysteme zum Einsatz. Für den Fall, dass ein Rechnerkanal ausfällt, sind nach wie vor zwei Rechnerkanäfeur die Bearbeitung der Sicherheitstechnischen Funktionen im Betrieb. Bei CBTC-Systemen wirkt sich außerdem positiv aus, dass weniger technische Komponenten im Gleis verbaut sind, da weitestgehend – wenn nicht gar vollständig – auf eine sekundäre Gleisfreimeldung und ortsfeste Signale verzichtet werden kann.  
- Auch beim DatenCOMMunikationssystem stellen verschiedene Arten von Redundanz sicher, dass ein Ausfall eines Geräts die Leistung des Betriebs nicht negativ beein-

trächtigt. So ist die redundante Hardware des DatenCOMMunikationssystems über zwei redundante Strom- und Glasfaserkabel mit möglichst abweichender Leitungsführung an die CBTC-Streckeneinrichtung angebunden. Für den Fall, dass ein Glasfaserkabel durchtrennt ist, ist noch eine zweite Datenverbindung vorhanden, so dass der Betrieb aufrechterhalten werden kann. Darüber hinaus verfügen die Access Points jeweils über mehrere Antennen und sind in ausreichend kurzen Abschnitten entlang der Strecke installiert, dass ein Zug zu jeder Zeit mehrere Access Points erreichen kann. Jede Nachrlicht des CBTC-Systems wird verdoppelt und über zwei Pfade versendet.

- Auch in der Betriebsleittechnik (Automatic Train Supervision, ATS) dient Redundanz der Steigerung der Verfügbarkeit des Systems. Bei der Redundanz wird zwischen „cold standby“ und „hot standby“ entsprechenden. Die Arbeitsplatzrechner arbeiten im „cold standby“. Dafür gibt es in der Leitstelle mehr Arbeitsplatzrechner als Bediener. Wenn ein Arbeitsplatzrechner ausfällt, wechselt der Bediener den Arbeitsplatz und loggt sich Dort wieder ein. Die Server hingegen arbeiten im „hot standby“. Dabei verarbeitet der passive Server alle ankommenden Daten von den Schnittstellen. Der passive Server unterscheidet sich dadurch vom aktiven, dass er keine Ausgaben durchgeführt. Der aktive und der passive Server überwachen sich gegenseitig. Es erfolgt eine automatische Übernahme der Funktion des aktiven Servers durch den passiven Server, nachdem der passive Server den Ausfall des aktiven Servers erkannt hat. Es erfolgt eine Aktualisierung des passiven Servers durch den aktiven nach Wiederanlaufen des passiven Servers. Fällt der passive Server aus, erfolgt eine Information an den Fahrdienstleiter oder den Wartungstechniker (Mücke 2005). Um auch gegen den Fall des kompletten Ausfalls der Leitstelle gewappnet zu sein konnen teilweise im Netz verteilte ortliche Bedienplätze vorgesehen werden oder aber eine vollständig ausgerüstete zweite Leitstelle an einem anderen Ort.

- Unterbrechungsfreie Stromversorgung (USV, bzw. english: Uninterruptible Power Supply, UPS): Diese Systeme dieren der Sicherstellung der Stromversorgung kritischer elektrischer Geräte bei Störungen im Stromnetz, wie beispelsweise kurzfristigen Stromausfälle und Stromschwankungen in Form von Über- oder Unterspannungen. Dies betriftt insbesondere diezentralenStreckeneinrichtungen sowie die Betriebsleittechnik.

# Literatur

Braband J (2005) Risikoanalysen in der Eisenbahn-Automatisierung. Eurailpress, Hamburg  
DIN EN 50126-1:2018-10 Bahnanwendungen - Spezifikation und Nachweis von Zuverlösigkeit, Verfügbarkeit, Instandhaltbarkeit und Sicherheit (RAMS) - Teil 1: Generischer RAMS-Prozess; Deutsche Fassung EN 50126-1:2017 (DIN EN 50126-1 2018)  
DIN EN 50129:2019-06 Bahnanwendungen - Telekommunikationstechnik, Signaltechnik und Datenverarbeitungssysteme - Sicherheitsrelevante elektronische Systeme für Signaltechnik; Deutsche Fassung EN 50129:2018  
DIN EN 50159:2011-04 Bahnanwendungen - Telekommunikationstechnik, Signaltechnik und Datenverarbeitungssysteme - Sicherheitsrelevante Kommunikation in Übertragungssystemen; Deutsche Fassung EN 50159:2010

DIN EN 62267:2010 DIN EN 62267:2020-07: Automatischer städtischer schienengebundener Personennahverkehr (AUGT) - Sicherheitsanforderungen. Deutsche Fassung EN 62267:2009  
DIN IEC 62443-3-3:2015-06 Industrielle Kommunikationsnetze - IT-Sicherheit für Netze und Systeme - Teil 3-3: Systemanforderungen zur IT-Sicherheit und Security-Level (IEC 62443-3-3:2013 + Cor.:2014)  
Guizard M (2006) Maintenance is a priority for communication based train control solutions. Signal + Draht 98(4):35-37  
Mücke W (2005) Betriebsleittechnik im öffentlichen Verkehr. Eurailpress, Hamburg  
Rüffer M, Schmidt C, Jung C, Schnieder L (2019) Innovation und Digitalisierung im Signal- und Zugsicherungsdienst. Nahverkehr 37(7+8):46-50  
Schnieder L (2020) Security Engineering - Ein ganzheitlicher Ansatz zum Schutz Kritischer Infrastrukturien im Verkehr, 2. Aufl. Springer, Berlin  
Schnieder L, Magerkurth G (2018a) Notfallmanagementpläne für Schienenverkehrssysteme als Bestandteil eines Informationssicherheitsmanagementsystems (ISMS). Eisenbahntech Rundsch 67(11):47-50  
Schnieder L, Magerkurth G (2018b) Schutz kritischer Infrastrukturten im ÖPNV – Aufbau eines zertifizierungsfähigen Informationssicherheitsmanagementsystems (ISMS). Nahverkehr 36(11):39–43  
Schnieder E, Schnieder L (2013) Verkehrssicherheit: Maße und Modelle, Methoden und Maßnahmen für den Straßen- und Schienenverkehr. Springer, Berlin  
Verband Deutscher Verkehrsunternehmen (VDV) (2005) VDV-Schrift 161-1: Sicherheitstechnische Anforderungen an die elektrische Ausrüstung von Stadt- und U-Bahn-Fahrzeugen; Teil 1: Grundlagen. VDV, Köln  
Verband Deutscher Verkehrsunternehmen (VDV) (2009) VDV-Schrift 161-2: Sicherheitstechnische Anforderungen an die elektrische Ausrüstung von Stadt- und U-Bahn-Fahrzeugen; Teil 2: Sicherheitsintegratätsanforderungen an fahrzeugbezogene elektrische/elektronische/programmierbare elektronische Schutzfunktionen (E/E/PE). VDV, Köln  
Verband Deutscher Verkehrsunternehmen (2008) Sicherheitsintegritätsanforderungen für Signal-und Zugsicherungsanlagen gemäß BOSTrab. VDV-Schrift 331  
Verordnung zur Bestimmung Kritischer Infrastrukturten nach dem BSI-Gesetz (BSI-Kritisverordnung - BSI-KritisV) (22. April 2016) (BGBl. I S. 958). Zuletzt geändert durch Art. 1 V. v. 21.06.2017 (BGBl. I S. 1903)

# Abwädigung von Kosten und Nutzen automatischer Zugbeeinflussungssysteme

7

# SN Flashcards

Als Käfer*in diesen Buches können Sie kostenlos unsere Flashcard-App „SN Flashcards" mit Fragen zur Wissenschaftung und zum Lernen von Buch-inhalten nutzen.

1. Gehen Sieitte auf https://flashcards.springernature.com/login und  
2.(erstellen Sie ein Benutzerkonto,indem Sie ihre Mailadresse angegeben und ein Password vergeben.  
3. Verwenden Sie den folgenden Link, um Zugang zu Ihr dem SN Flashcards Set zu halten:  $\triangleright$  https://sn.pub/sK5mLQ

Sollte der Link fehlen oder nicht Funktionieren, senden Sie unsitte eine E-Mail mit dem Betreff „SN Flashcards" und dem Buchtitel an customerservice@springernature.com

Kosten-Nutzen-Analysen werden in zahlreichen Bereichen der öffentlichen Daseinsvorsorge zur Entscheidungsunterstützung eingesetzt. So verpflichtet in Deutschland etwa § 7 Bundeshaushaltsordnung die öffentlichen Körperschaften dazu, vor einer Ausgabe eine Wirtschaftlichkeitsuntersuchung durchzuführen (vgl. hierzu Arnold 2017; Kossak 2018). Kosten-Nutzen-Analysen sind eine solche Form der Wirtschaftlichkeitsuntersuchung. Dieser Abschnitt stellt dar, welche Betrachtungen bei der Einführung automatischer Zugbeeinflussungssysteme auf der Kostenseite durchgeführt werden (Abschn. 7.1). Des Weiteren stellt dieser Abschnitt

dar, wie der Nutzen von Verkehrsininfrastrukturprojekten ermittelt wird (Abschn. 7.2). Überwiegt der Nutzen die Kosten, qualifiziert dies eine Infrastrukturmaßnahme für eine Förderung aus öffentlichen Haushaltsmitteln.

# 7.1 Ermittlung der Kostenkomponente mittels Lebenszykluskostenrechnung

Investitionen in die Automatisierung von Stadtstchnellbahnsystemen sind in der Regel mit einem hohen Investitionsvolumen verbunden (Capital Expenditure, CAPEX). Gleichzeitig weisen diese Investitionsgüter eine sehr lange Lebensdauer auf. Falsche Entscheidungen zu Beginn des Lebenszyklus können dazu nur schwer und wenn dann nur mit erheblichem Aufwand korrigiert werden. Aus thisem Grund hat sich in den letzten Jahrzehnten in der öffentlichen Beschaffung das Konzept der Lebenszykluskosten (life cycle costs, LCC) durchgesetzt (DIN IEC 60300-3-3:1999). Demnach wird die über einen langfristigen Investitionszeitaum (beispielsweise 25 Jahre) insgesamt wirtschaftliche Investitionsalternative beschäft. Hierbei konnen zum Beispiel gingere Instandhaltungsaufwände (Operational Expenditure, OPEX) in der Phase des Betriebs teilweise höhere initiale Beschaffungskosten kompensieren (Wolberg und Kiefer 2000).

# 7.1.1 Elemente der Lebenszykluskosten

Die Gesamtheit aller Kosten wird im so genannten „Kostenwurfel“ (vgl. Abb. 7.1) dargeistl. Nachfolgend werden die drei Dimensionen des Kostenwurfels nach (DIN IEC 60300-3-3:1999) eingeführt. Die erstige Seite des Wurfels ist die technische Struktur des betrachteten Zugbeeinflussungssystems. Dies wird auch als Produktaufbruchstruktur bezeichnet. Die zweite Seite des Wurfels sind die in der Analyse betrachteten Lebenszyklusphasen. Dies wird auch als Kostenaufbruchstruktur bezeichnet. Die dritte Seite des Wurfels sind schließlich die in der Wirtschaftlichkeitsbetrachtung berücksichtigten Kostenarten.

Produktaufbruchstruktur (vertikale Achse des Kostenwurfels): Die vertikale Achse des „Kostenwurfels" (vgl. Abb. 7.1) ist die Produktaufbruchstruktur (englisch: Product-/Work Breakdown Structure, kurz: PBS/WBS). Sie umfasstiben der technischen Struktur des betrachteten Systems auch Unterstützungende Dienstleistungen und Arbeitspakete. Hier wird der betrachtete Technikumfang aufgegliedert und definiert, was für Kosten anfallen. Die LCC-Analyse für die Leit- und Sicherungstechnik von Schienenverkehrsunternehmen kann sich hierbei an in der Literatur diskutierte Produktaufbruchstrukturen (Gutsche 2010) orientieren. Die Produktaufbruchstruktur besteht beim Fahren auf Zugsicherung aus den Elementen der Außenanlage (Gleisfreimeldeeinrichtungen wie Achszahlsysteme oder Gleiststromkreise, bewegliche Fahrwegelemente wie Weichen und Gleissperren sowie ortsfeste Signale), der Innenanlage (je nach Art des Stellwerks Relaisgestelle oder Rechnerschränke mit den zugehörigen Kabelabschlussgestellen), der Leittechnik (Zuglenkrechner sowie Bedien- und Anzeigesysteme) und der Art der Zugbeeinflussung. Hierbei müssen für

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/554700fd31a014759861702b3376a20af2050603d790564fd89f2ae0e83eb2d1.jpg)  
Abb. 7.1 Verschiedene Perspektiven auf die Lebenszykluskosten

CBTC-Systeme auch die Komponenten des gewählten Datenkommunikationsssystems mit betrachtet werden. Ist die Produktaufbruchstruktur modelliert, konnen für den zu betrachtenden Streckenabschnitt die konkreten Mengenwerte ergänzt werden, so dass sich hieraus eine Stückliste (englisch: bill of quantity, BoQ) ergibt. Für möglicherweise bestehende Mengenrisiken sollenn hier bereits Vorkehrungen getroffen werden.

Kostenaufbruchstruktur, Lebenszyklusphasen (horizontal Achse des Kostenwurfels): Die horizontale Achse des „Kostenwurfels“ in Abb. 7.1 besteht Kostenaufbruchstruktur (english: Cost Breakdown Structure, kurz CBS). Sie zeigt, in welcher Phase des Lebenszyklus die jeweiligen Kosten anfallen. Beispielsweise sind dies die drei Hauptphasen: Beschaffung, Betrieb (Instandhaltung) und Entsorgung. Der grundsätzliche Aufbau einer Kostenaufbruchstruktur für Bahnanwendungen ist in der Regel vor allem geprügt durch die Investitionskosten, die Kosten für den Betrieb (Betriebspersonal, Energie sowie Kosten für System-Unverfügbarkeit im Sinne von Verspfatungen) und die Kosten für die Instandhaltung. Hierbei müssen die einzelnen Instandhaltungsaktivitäten pro Komponente der Produktaufbruchstruktur betrachtet werden. Aus den Instandhaltungsanweisungen der Hersteller und/oder rechtlichen Vorgaben resultieren Aufwände für regelmäß durchzuführende Sichtprüfungen (Inspektionen). Aus den Zuverlösigkeitskennwerten der einzelnen Komponenten können darüber hinaus Annahmen abgeleitet werden, wie früig es zu einem Komponentenausfall kommt wird. Außerdem sind kein den Ersatzteilkosten auch Annahmen über die für eine Instandsetzung erforderlichen Zeiten (Mean Time to Repair, MTTR) besteht, die hier ebenfalls zu berücksichtigten sind (Wolberg und Kiefer 2000).

Kostenarten: Die dritte Dimension, welche den Kostenwürfel entstehen{lätst, stellen die Kostenarten (englisch: Cost Categories, kurz CC) dar. Die Kostenarten benennen die Bereiche, die Kosten verursachen und gliedern diese in kostenverursachende Elemente (englisch: Cost Elements, kurz CE) auf. Bei der Betrachtung eines kostenverursachenden Elements befindet man sich demzufolge auf derkleinsten Betrachtungsebene. Es konnen verschiedene Kostenarten unterschieden werden, wie beispelsweise Materialkosten, Personalkosten, Werkzeugkosten und Entsorgungskosten. Beispiele für Kostenelemente sind beispelsweise Kosten für Roh-, Hilfs- und Betriebsstoffe, Kosten für die Wartung eines Weichenantriebes oder die Entsorgung eines Relais. Die Angaben für die Kostenarten stammen idealerweise aus einem bei dem Betreiber eingesetzten Softwaresystem (Hannusch 2015).Auch bei der Abschätzung der einzelnen Kostenpositionen sollen Risiken, beispelsweise in Bezug auf zu erwartende zukünftige Preissteigerungen, mit berücksichtigt werden. Einen Ansatz, die zukünftige Kostenentwicklung in die Berechnung der Lebenszykluskosten mit einzubeziehen konnte die Extrapolation verschiedener für einzelne Kostenpositionen zutreffender Indizes (bspw. Arbeitskostenindex) darstellen.

# 7.1.2 Berechnung der Lebenszykluskosten

Die Berechnung der Lebenszykluskosten erfolgt mittels so genannter dynamische Investitionsrechnungsverfahren. Hierbei werden die bei den langen Lebensdauern von Zug-

sicherungsanlagen erheblichen Unterschiede im Anfallen von Zahlungen (Aufwendungen aber auch Erträge) einer Investition berücksichtigt. Die Idee ist hierbei, dass alle über den Lebenslauf einer geplanten Investition anfallenden vermögenswirksamen Zahlungen auf den Beginn einer Planung abgezinst werden (Huch et al. 1997). Dieser Kapitalwert ist das Entscheidungskriterium für den Vergleich unterschiedlicher Investitionssalternativen. Der Kapitalwert bildet sich als Differenz zwischen der Summe aller auf den Anfangszeitpunkt abgezinsten Einzahlungen und der Summe aller auf den Anfangszeitpunkt abgezinsten Auszahlungen, die mit dieser Investition zusammenhängen. Für die relative Vorteilhafigkeit können die Investitionssalternativen entsprechend der Höhe des Kapitalwerts geordnet werden. Der Kapitalwert  $C_0$  einer Investitionssalternative über einen Zeitraum t berechnet sich auf Basis periodenspezifischer Einzahlungen  $E_t$  und Auszahlungen  $A_t$  sowie des kalkulatorischen Zinssatzes i zu:

$$
C _ {0} = \sum_ {t = 1} ^ {n} \frac {\left(E _ {t} - A _ {t}\right)}{\left(1 + i\right) ^ {t}}
$$

# 7.1.3 Ergebnisse der Analyse der Lebenszykluskosten

Über die lange Lebensdauer signaltechnischer Einrichtungen weisen automatische Zugbeeinflussungssysteme im Vergleich zu konventionellen Bahnsystemen hinsichtlich ihrer Lebenszykluskosten erhebliche Vorteile auf. Diese werden nachfolgend skizziert:

- Reduzierte Anzahl Außenanlageenelemente der Streckeneinrichtung: Durch die kontinuierliche Datenübertragung zwischen Fahrzeugen und Strecke kann auf einen Großteil der ortsfesten Sensorik zur Gleisfreimeldung verzichtet werden. Sofern nicht von der Zulassungsbehörde anders gefordert, können auch ortsfeste Signale vollständig entfallen, da nunmehr eine Führstandssignalisierung mit einer entsprechend hohen Verfügbarkeit vorliegt. Die geringe Anzahl an Außenanlageenelementen resultiert darüber geringen Anschaffungskosten auch in erheblichen Einsparungen für die Instandhaltung.  
- Energieeinsparung: Die kontinuierliche Datenübertragung zwischen Fahrzeug- und Streckeneinrichtung liegt die Grundlage für die automatische Fahr- und Bremssteuerung (Automatic Train Operation, ATO). Hierdurch gelingt – sofern die Betriebssituation es zulässt – die Umsetzung einer energiesparenden Fahrweise mit Einsparung entsprechender Kosten für die Traktionsenergie. Die energiesparende Fahrweise resultiert hierbei kein dem optimalen Auffahren der eigenen Trajektorie auch aus vermiedenen Folgeversprüften.  
- Einsparung von Personalkosten: Im unbegleiteten fahrerlosen Betrieb verkehrende Bahnen benötigen für den betrieblichen Ablauf kein Personal. Je nach System kann die Bereitstellung und die Abstellung von Zügen sowie die Beförderung von Fahrgästen effizienter gestaltet werden. Darüber hinaus konnen mit unbegleitet fahrerlos ver

kehrenden Bahnen weitere Verkehrsangebote entwickelt werden, die heute mit hohen Personalkosten (Nacht- oder Sonn- und Feiertagszuschänge) und Einschnitten im Privatleben des Betriebspersonals verbunden sind. Auf diese Weise wird durch die Automatisierung beispelssweise ein durchgängiger U-Bahnbetrieb auch während der Nacht oder ein uneingeschränkter Verkehr an Feiertagen möglich.

- Zusätzliche Fahrgeldeinnahmen: Die dichtere Zugfolge führt zu einer Steigerung der Attractivität des öffentlichen Personennahverkehrs. Zusätzliche Fahrgäste bedeuten mehr Umsatz für die Verkehrsrunternehmen.

# 7.2 Ermittlung der Nutzenkomponente mit Betriebssimulationen und Verkehrsmodellen

Für die Ermittlung des Nutzens einer signaltechnischen Erneuerung muss zunachst die Einfluss des CBTC-Systems auf die Leistungsfähigkeit der entsprechenden Strecken betrachtet werden. Dies geschieht mittels betriebswissenschaftlicher Untersuchungen, was in Abschn. 7.2.1NJaher ausgefuhrt wird. In der Regel wird durch CBTC-Systeme ein positiver Beitrag auf die Leistungsfähigkeit der betrachteten Strecke nachgewiesen. Dies eröffnet Freiheitsgrade hinsichtlich der Definition zusätzlicher Ansgebote des öffentlichen Personenannahverkehrs (OPNV), was in Abschn. 7.2.2 beschrieben wird. Um einen gesellschaftlichen Nutzen aus den zusätzlichen Bedienungsangeboten (Fahrplanfahrten) zu ermitteln, müssen die gesamten verkehrlichen Effekte betrachtet werden. Hierzu kommt Verkehrsrödelle zum Einsatz. Dies wird in Abschn. 7.2.3 beschreiben. Der auf dieser Basis ermittelten Nutzenkomponente kann die zuvor dargestellen Kostenkomponente (Lebenszykluskostenrechnung) zur Ableitung eines Kosten-Nutzen-Faktors gegenübergestellt werden.

# 7.2.1 Simulative Untersuchung der Leistungsfähigkeit signaltechnischer Ausrüstungsvarianten

Mit der Betriebssimulation{lssst sich das Leistungsverhalten fur verschiedene Infrastrukturund Betriebsprogrammvarianten fur einen gegebenen Untersuchungszeitraum grundsatzlich bewerten und vergleichen. Die Betriebssimulation kann Auskunft darüber geben, in welchem Auslastungsbereich sich der aktuelle oder ein geplanter Fahrplan bewegt und wie große eventuell vorhandene Kapazitätsreserven (bezogen auf den betrachteten Netzausschnitt) sind. In CBTC-Projekten werden Betriebssimulationen mit Hilfe einer geeigneten Simulationssoftware durchgefuhrt. Die folgenden Abschnittte beschreiben die im Rahmen einer Betriebssimulation durchzuführenden aufeinander aufbauenden Schritte (Becker et al. 2019).

# Vorbereitung des Simulationsmodells

Für den in der Simulation zu betrachtenden Streckenbereich müssen die für die Durchführung der verschiedene Betrachtungen erforderlichen Grunddaten des Simulations

modells erfasst werden. Grundlage einer Betriebssimulation sind im Wesentlichen die nachfolgend dargestellt den drei Gruppen von Daten (Ostermann et al. 2005):

Infrastrukturdaten: Die Infrastruktur des zu simulierenden Netzes des Betreibers wird mittels eines Grafikeditors entworfen und verwaltet. Hierbei werden die wesentlichen Merkmale der Strecke als Knoten-Kanten-Modell abgebildet. Es handelt sich hierbei um kanten- oder knotenbewertete Grafen (Becker et al. 2019). An jeder Stelle, an der sich ein Attribut der Streckeändert, wird im Modell ein Knoten gesetzt. Die Infrastruktur wird hierbei oftmais von Hand aufgenommen. Die benöttigten Daten können wie folgt unterschieden werden:

- Daten zur Gleistopologie wie Weichen, Kreuzungen und Gleisenden.  
- Daten zur Sicherungsglogik wie Signale, Spezifika der eingesetzten Zugsicherungs-Systeme (Fahrstraßelogik), Lage und Länge von Gleisfreimeldeabschnitten und technische Reaktionszeiten (Umlaufzeiten von Weichenantriben, Fahrstraße bildezeiten und weitere Details wie beispelsweise eine einzelementweise Auflösung von Fahrstraße).  
- Vorgaben für die zulässige und mögliche Fahrweise der Fahrzeuge wie das Gradientenprofil (Neigungen und Gefäle) sowie zulässige Geschwindigkeiten beispielsweise bedingt durch Bogenradien (zum Beispiel in abzweigenden Weichensträngen).  
- Betriebsbeeinflussende Daten wie Haltepositionen und Nutzlängen der Bahnsteige  
Referenz- und Messpunkte.

Fahrplan- und Betriebsdaten: Für eine realistische Abbildung des Betriebs werden Fahrplane in das Simulationswerkzeug eingegeben. Hierbei werden verschiedene Aspekte differenziert:

- Modellierung des Soll-Fahrplans: Die im Simulationsmodell zu berücksichtigenden Daten umfassen die Grunddaten des Soll-Fahrplans von den Einbruchstellen des Zuges in den betrachteten Netzausschnitt. Konkrete Parameter umfassen hierbei:

- Modellierung der Haltezeiten. Hierbei werden Verkehrshaltezeiten, das heißt dem Fahrgastwechsel dienenden Haltestellenaufenthalte (minimale Haltezeiten und Sollhaltezeiten) abgebildet. Des Weiteren werden möglicherweise noch Haltezeit-reserven im Fahrplan berücksichtigt. Darüber hinaus werden auch Betriebshaltezeiten abgebildet. Betriebshaltezeiten dienen nicht unmittelbar dem Fahrgastwechsel. Ein Beispiel hierfür sind zusätzliche im Fahrplan zu berücksichtigende Zeitanteile für das Kehren von Fahrzeugen an den Endhaltestellen (Wendezüge), das Kuppeln und Trennen von Zügen (Flügelzugkonzepte) sowie gegebenenfalls die Abwicklung geplanter Rangierfahrten.  
- Modellierung der Fahrzeiten mit Abfahrts- und Ankunftszeiten in den Stationen, Sollfahrzeiten und (Regel-)Zuschlagen auf die Fahrzeit zur Kompensation mölicher Störungen im Betriebsablauf.

- Modellierung weiterer Zeitanteile, welche durch die Umstiege von Fahrgästen erforderlich werden. Ein Beispiel hierfür ist die logische Verknüpfung zweier Zugfahrten durch die Berücksichtigung von Anschlussbeziehungen. Ist der zubringende Zug verspätet, wird bei einer Anschlussbinding die Versprüfung auf den abbringenden den Zug übertragen.

- Daten des Ist-Betriebsgeschehens: Um das reale Betriebsgeschehen im betrachteten Netzausschnitt abzubilden, werden einbrechende Züge mit einer Versprüngsverteilung beaufschlag. Diese wird repräsentiert durch eine Versprüungsfunktion und solle einer möglich realen Versprüungsverteilung an dieser Stelle entsprechen (beispielsweise aus Daten des Intermodal Transport Control Systems, ITCS). Über den Laufweg der Fahrzeuge können darüber hinaus Primäreversprüungen (verlangerte technische Fahrzeit, Haltezeit) induziert werden, welche ebenfalls durch Verteilungsfunktionen beschreiben werden. Zusätzlich sollenn auch für die Haltestellen im betrachteten Netzausschnitt Versprüungsverteilungen vorliegen, damit diese später mit den Simulationsergebnissen verglichen werden konnen (Büker et al. 2021).

Fahrzeugdaten pro Fahrzeugbaureihe: Für die Stadtbahnfahrzeuge werden die technischen Daten aller in der Simulation vorkommenden Fahrzeuge und Fahrzeugkombinationsen verwaltet. Konkret betriff dies von den Fahrzeugherstellern vorgegebene (und im CBTC-Fahrzeugrechner projektierte) garantierte Bremsverzögerungen sowie das üblicherweise im Betrieb realisierte Beschleunigungsverhalten der Fahrzeuge, Laufwiderstandsdaten, die Anzahl der Wagen pro Zug sowie die Zugänge.

# Validation und Kalibrierung der Betriebssimulation

Um eine hohe Aussagekraft der Simulationsergebnisse zu erhalten, muss diesen valide sein. Daher wird man vor Beginn der Simulationsmodell auf den Prüfstand stellen (Becker et al. 2019). Dies geschieht in zweierlei Hinsicht:

- Frühzeitige Durchführung von Simulationen, um Lücken oder möglicherweise unzureichend modellierte Aspekte im Simulationsmodell zu offenbaren. Hierzu werden auf Grundlage des hinterlegten Fahrplans früherzeitig Simulationslaufe gestartet, um das Simulationsmodell bei Bedarf zu korrigieren.  
- In einem weiteren Schritt wird das Simulationsmodell kalibriert. Dies stellt sich, dass das Simulationsmodell eine valide Abbildung der Wirklichkeit darstellt und zu den gleichen Ergebnissen führt, wie diese sich auch im realen Betrieb einstehen. Hierfür wird der Ist-Zustand der Betriebsabwicklung auf zu betrachtenden Strecke modelliert. Zur Bewertung der aktuellen Betriebsqualität werden die Versprütungen aus den Simulationsergebnissen bei der durchgeführten Betriebssimulation betrachtet (Cui und Martin 2014). Hierfür werden die Versprütungen an den relevanten Fahrzeitmesspunkten (den Stationen) gemessen und mit den vorliegenden Werten aus dem Intermodal Transport Control System (ITCS) des Betreibers verglichen.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/b319d86306f7509f11df87e7f71baed1574acd2f4fdc19c4167a0541aef0516b.jpg)  
Abb. 7.2 Beiselhafte Darstellung eines Simulationsmodells. (Quelle: VIA Consulting & Development GmbH)

Abb. 7.2 zeigt das Zusammenwirken der verschiedene Modellbestandteile in einem Simulationswerkzeug. In der oberen Bildhälfte ist die zulässige Fahrweise des Zuges in einem statischen Geschwindigkeitsprofil darestellt. Unterhalb der zulässigen Geschwindigkeit ist die vom Zug tatsächlich realisierte Geschwindigkeit darestellt. In der unteren Bildhälfte sind die Zeit-Weg-Linien (Sperrzeitenbänder) der Zugfahrten darestellt. Die Zahlen in Abb. 7.2 markieren Charakteristika, wie sie sich in einem CBTC-System ergeben. In der Darstellung der vom Zug realisierten Fahrweise wird deutlich, dass die maximal zulässige Geschwindigkeit nicht erreicht wird, weil der Zug schon früherzeitig auf das Geschwindigkeitsziel bremst (Ziffer 1). Hinter dem Zielbahnsteig schließt sich ein Kehrgleis mit einer geringen zulässigen Geschwindigkeit von  $25\mathrm{km / h}$  an (Ziffer 2). In der unteren Bildhälfte wird deutlich, dass die erreichbaren Zugfolgezeiten in städtischen Bahnsystemen wesentlich durch die Haltestellenaufenthaltszeiten bestimmt werden (Ziffer 3). Ebenfalls wird deutlich, dass die Sperrzeitenbilder von der Fahrzeuggeschwindigkeit abhängen. Die Nachbelegung (Teil des Sperrzeitenbandes unterhalb der Zeit-Weg-Linie eines Zuges) wachst mit fallender Geschwindigkeit (vgl. Ziffer 4). Die Vorbelegung (Teil des Sperrzeitenbandes oberhalb der Zeit-Weg-Linie eines Zuges) wachst überproportional zur Geschwindigkeit (vgl. Ziffer 5). Zuletzt wird auch deutlich, dass Weichenlagen ebenfalls einen Einfluss auf die Sperrzeitenbänder haben. Die Weiche ist ein zu sichernder (ortsfester) Gefahrenpunkt. Ihr korrekte Endlage muss vor Zulassen einer Zugfahrth vorhanden sein (Büker et al. 2019). Aus thisem Grund zeigt sich diese früherezeitige Beanspruchung der Weiche für die Zugfahrth in der Vorbelegung für die jeweilige Zugfahrth (vgl. Ziffer 6).

# Durchführung der Simulationsläufe

Um für das jeweilige Entscheidungsproblem zu validen Aussagen zukommen, werden in der Regel mehrere Varianten des Simulationsmodells dem jeweiligen Nachweisziel fol-

gend modifiziert und durchlaufen (Becker et al. 2019). Im Sinne des Monte-Carlo-Verfahrens wird für jedem betrachtete Simulationsszenario eine ausreichende Menge von Simulationslaufen durchgeführt, so dass hieraus statistisch belastbare Kennzahlen resultieren. Jeder Simulationslauf erhält als Input eine Liste zufällig generierter primärer Ver-, spätungsdaten, welche zug- und betriebsstellenspezifisch sind (Büker et al. 2021). Die Erstellung der entsprechenden Simulationsszenarien erfolgt nach dem in der Verkehrssplanung üblichen Mitfall-/Ohnefall-Prinzip.

- Ohne-Fall: Durchführung des aktuellen Fahrplanangebots mit aktueller Technik: Dieses stellt die Referenz für alle Änderungen im System dar. Umtragfähige Simulationsergebnisse zu erhalten, war diese Simulationsmodell Gegenstand der zuvor dargeistellen Validierung und Kalibrierung.  
- Mit-Fall 1: Durchführung des aktuellen Fahrplanangebotes mit zukünftiger Technik: Durch den Übergang von einer konventionellen Zugsicherung mit Fahrsperre zu einem CBTC-System gelingt ein Übergang vom Fahren im festen Raumabstand zu einem Fahren im wandernden Raumabstand. Hierdurch beeinflussen sich die Züge nicht mehr gegenseitig und es kommt nicht mehr zu einer Versprüungsübertragung. Hierdurch entstehen Kapazitätsreserven.  
- Mit-Fall 2: Hochskalieren des Fahrplanangebotes mit zukünftiger Technik: Die zukünftig gewünschten Fahrplantakte werden in der Betriebssimulation abgebildet. Hierdurch kann bewertet werden, innieweit noch Kapazitätsreserven bestehen und in welchem Auslastungsbereich die Strecke betrieben wird.

Die Ergebnisse der einzelnen Simulationsläufe werden jeweils für sich ausgewertet. Die Ergebnisse der entsprechenden Simulationsläufe werden einander gegenübergestellt, um die relative Vorteilhafigkeit der entsprechenden untersuchen Systemvarianten zu analysieren und für die nachgelagerten Entscheidungsprozesse (unter anderem zur Forderwürdigkeit des jeweiligen Projekts) transparent und nachvollziehbar zu Dokumentieren.

# 7.2.2 Nutzung der hohenen Leistungsfähigkeit für Anpassungen im ÖPNV-Angebot

In städtischen Räumen ist das Bedienungsangebot spurgeführter Verkehrssysteme im wesentlichen bereits heute durch die Struktur der vorhandenen Verkehrsanlagen, bzw. die vorhandene Zugsicherung eingeschränkt. Da konventionelle Zugsicherungsanlagen lediglich das Fahren im festen Raumabstand unterstützen kann die Kapazität in bestehenden Netzen möglicherweise noch durch die Gefäßgroßen der Fahrzeuge (bspw. Betrieb mit längeren Fahrzeugen) erhöht werden. Auf Grund baulicher Restriktionen wiebspw. Bahnsteiglängen ist auch this gegebenenfalls nicht möglich. Hier zeigt sich, dass die durch CBTC-Systeme mögliche Abkehr vom Fahren im festen Raumabstand, bzw. der damit verbundene Übergang zu einem Fahren im wandernden Raumabstand weitergehende

Potenziale zur Angebotsverbesserung im öffentlichen Personennahverkehr (ÖPNV) eröffnet. Diese Potenziale stellen sich wie folgt dar:

- Angebotsausweitungen: Durch die geringen Zugfolgezeiten konnen auf einer Linie mehr Fahrten pro Fahrrichtung und Stunde abgewickelt werden. Dies erlaubt beispiselsweise die Einführung neuer Linien. Aus Sight des Fahrgastes wirken sich mögliche neue Direktlinien, bei denen auf bestimmen Verkehrsrelationen für die Fahrgaste die Notwendigkeit zu Umstiegen entfällt unmittelbar positiv auf die wahrgenommene Dienstleistungsqualität aus.  
- Verbesserung der Betriebsqualität: Bei schienengebundenen Verkehrssystemen besteht die Leistungsfähigkeit die Anzahl an Zugfahrten dar, welche auf einer Schiereninfrastruktur unter Einhaltung einer zulässigen Betriebsqualität abgewickelt werden kann. Die Anzahl fahrbarer Zugfahrten wird maßgeblich durch den Ausbauzustand der zugrundeliegenden Infrastruktur beeinflusst. Hierfür ist insbesondere das verbaute Zug-sicherungssystem maßgeblich. Wir nun die Leistungsfähigkeit erhöht, hat dies - sofern es nicht zu einer Angebotsausweitung kommt - zunachst positive Effekte auf die Betriebsqualität. Dies verbessert die von den Fahrgästen wahrgenommene Dienst-leistungsqualität durch geringere Störungen im Betriebsablauf und hieraus resultierende Verspfatungen.  
- Reisezeitgewinne: Dies beschreiben Veränderungen der Reisezeit der Fahrgäste beim Mitfall gegenüber dem Ohnefall. Aus Sight des Fahrgastes führen beispiselsweise dichtere Fahrplantakte (resultierend aus Angebotsausweitungen, siehe oben) zu kürzeren Wartezeiten an den Stationen. Dies wirkt sich somit unmittelbar positiv auf die Reisezeit aus.

# 7.2.3 Bewertung des verkehrlichen Nutzens von Anpassungen im ÖPNV-Angebot

Neben der Vermeidung von Verkehr trägt vor allem die Verkehrsverlagerung auf umwelt-schonendere Verkehrsträger dazu bei, die negativen Auswirkungen von Verkehr auf die Umwelt einzudammen. Die von der Verkehrspolitik gesetzten Rahmenbedingungen playen eine Schlüsselrolle bei der Ermöglichung von Verkehrsverlagerung. Im Personenverkehr kann die Verkehrsverlagerung vom motorisierten Individualverkehr auf den Öffentlichen Personenverkehr u. a. durch einen stärkeren Ausbau der öffentlichen Verkehrsangebote gefördert werden. Die signaltechnische Erneuerung von städtischen Schierenverkehrssystemen hoher Leistungsfähigkeit ermöglich - wie bereits zuvor dargeistellt - den Ausbau öffentlicher Verkehrsangebote.

Da die Investition in die signaltechnische Erneuerung erhebliche finanzielle Mittel bindet, ist hier der Nachweis der Sinnhaftigkeit dieser Maßnahmen im Zusammenhang des Gesamtverkehrsnetzes zu führen. Hierbei kommt es vor allem darauf an zu prognostizieren, welchen Einfluss die Verbesserungen des Angebots im öffentlichen Personennahver

kehr auf die tatsächliche Verkehrsnachfrage in der betrachten Region haben werden. Um diese Frage nach den verkehrlichen Nutzenwirkungen qualifiziert beantwerten zu konnen,kommen Verkehrsnachfragemodell zum Einsatz. Dafür wird das das Betrachtungsgebiet in gleichwertige Verkehrszellen eingeteilt. Die große, Homogenität und Verfügbarkeit soziodemographischer Daten beeinflusst die Genauigkeit der späteren Ergebnisse des Nachfragemodells. Untereinander sind die Verkehrszellen durch Verkehrslinien verbunden.Verkehrszellen und Verkehrslinien zusammen ergeben das Netzmodell. Auf Basis des Netzmodells kann nun in mehreren aufeinander aufbauenden Schritten die Verkehrsnachfrage ermittelt werden:

- Verkehrserzeugung: Jede Verkehrszelle ist Quelle oder Senke von Verkehrsbezehungen. Je nachdem, ob eine Zelle als Wohn- oder als Arbeitsstätte dient, werden zu unterscheidlichen Zeiten unterschiedliche Verkehrsmengen erzeugt. Diese Daten konnen aus der Statistik entnommen oder berechnet werden.  
- Verkehrsverteilung: Durch die Berechnung der Verkehrserzeugung bleibt unklar, auf welche anderen Verkehrszellen sich der Verkehr verteil. Es gibt unterscheidliche mathematisch formulierte Zielwahlmodelle. Als Ergebnis der Anwendung Zielwahlmodelle kann die verkehrliche Verflechtung der Verkehrszellen unterinander im betrachten Raum in Form einer Quelle-Ziel-Matrix dargestellt werden.  
- Verkehrsaufteilung (Verkehrsmittelwahl): Bei der Verkehrsmittelwahl wird die Aufteilung des Verkehrs auf individuelle (MIV = motorisierter Individualverkehr, NIV = nicht-motorisierter Individualverkehr) und öffentliche Verkehrsmittel (ÖV) - der sogenannte Modal Split - ermittelt.  
- Verkehrsumlegung (Verkehrswegewahl): Bei der Verkehrsumlegung wird bestimmt, welche Route der Verkehr wählt, um von der Quelle zum Ziel zu gelangen.

Auch die Nachfragemodelle werden mittels Ohnefall-/Mitfallprinzip vergleichend betrachtet. Dadurch, dass die Einführung von CBTC-Systemen Angebotsverbesserungen der Nahverkehrsbetreiber erhögt, werden in diesen Modellen Nutzen der Reisenden in Form von Reisezeitgewinnen und auch hieraus resultierende Verkehrsverlagerungen zwischen den Verkehrsträgern bewertbar. Insbesondere der Verkehrsverlagerung auf umweltschonendere Verkehrsträger wird vor dem Hintergrund einer forcierten Umwelt- und Klimapolitik ein gesellschaftlicher Nutzen zugesprochen.

# Literatur

Arnold M (2017) Standardisierte Bewertung Version 2016 - Ergebnisse der Weiterentwicklung und Fortschreibung, Nahverkehr 35(9):42-46  
Becker M, Büker T, Hennig E, Felix K (2019) Sound evaluation of simulation results. In: RailNorrköping 2019 - 8th International Conference on Railway Operations Modelling and Analysis (ICROMA), Norrköping, S 99-115

Büker T, Grafagnino T, Hennig E, Kuckelberg A (2019) Enhancement of blocking-time theory to represent future interlocking architectures. In: RailNorrköping 2019 - 8th International Conference on Railway Operations Modelling and Analysis (ICROMA), Norrköping, S 219-240  
Büker T, Schnieder L, van Hovell M, Meurer D (2021) Eisenbahnbetriebswissenschaftliche Untersuchung von CBTC-Systemen. Signal + Draht 113(9):25-33  
Cui Y, Martin U (2014) Algorithmus zur automatisierten Kalibrierung von Modellen bei der Betriebssimulation. Eisenbahntechn Rundsch 63(11):10-14  
DIN IEC 60300-3-3:1999-03 Zuverlüssigkeitsmanagement – Teil 3: Anwendungsleitfaden – Hauptabschn 3: Betrachtung der Lebenszykluskosten (IEC 60300-3-3:1996)  
Gutsche K (2010) Integrierte Bewertung von Investitions- und Instandhaltungsstrategien für die Bahnsicherungstechnik, Bd 9. Berichte aus dem DLR-Institut für Verkehrssystemtechnik, Braunschweig  
Hannusch G (2015) Anforderungen an IT-Systeme für das Asset Management im Bahnverkehr. Eisenbahningenieur 65(7):34-36  
Huch B, Behme W, Ohlendorf T (1997) Rechnungswesenorientiertes Controlling - Ein Leitfaden für Studium und Praxis. Physica, Heidelberg  
Kossak A (2018) Reaktivierung des allgemeinen Schierenenpersonenverkehrs auf der Kandertalstrecke - Teil1. Eisenbahntechn Rundsch 67(6):22-25  
Ostermann N, Schlögel A, Oster M, Messauer C (2005) Anwendungen der Betriebssimulation. Elektrotech Informationstech (e&i) 122(4):124-130  
Wolberg J, Kiefer J (2000) Life Cycle Costs - Die Kosten von Betrieb, Wartung und Verfügbarkeit. Signal + Draht 92(6):19-22

# Umbau, Test und Inbetriebnahme automatischer Zugbeeinflussungssysteme

8

# SN Flashcards

Als Käfer*in diesen Buches können Sie kostenlos unsere Flashcard-App „SN Flashcards" mit Fragen zur Wissenschaftung und zum Lernen von Buch-inhalten nutzen.

1. Gehen Sieitte auf https://flashcards.springernature.com/login und  
2. erstellen Sie ein Benutzerkonto, indem Sie ihre Mailadresse angegeben und ein Password vergehen.  
3. Verwenden Sie den folgenden Link, um Zugang zu Ihr dem SN Flashcards Set zu erhalten:  $\triangleright$  https://sn.pub/sK5mLQ

Sollte der Link fehlen oder nicht Funktionieren, senden Sie unsitte eine E-Mail mit dem Betreff „SN Flashcards" und dem Buchtitel an customerservice@springernature.com

Die Erneuerung der Signaltechnik wird insbesondere in Europa in den nachsten Jahren immer bedeutender, da ein Großteil der bestehenden Infrastruktur der U-Bahnsysteme in den Großstädten mehr als 30 Jahre alt ist (de Silvestre 2005). Viele Betreiber stehen aus folgenden Gründen vor Ersatzinvestitionen:

- Obsoleszenz: Ersatzteile für die bestehenden signaltechnischen Anlagen sind nicht mehr lieferbar (Laumen und Henning 2012). Dies stellt eine große Herausforderung für die Instandhaltung und die Aufrechterhaltung eines sicheren und ordnungsgemäß Betriebs dar (McCullough 2008).

- Kapazität: Mit den bestehenden signaltechnischen Systemen kann die zunehmende Verkehrsnachfrage zukünftig nicht mehr qualitätsgerecht bedient werden. Dichtere Zugfolgen sind mit den bestehenden signaltechnischen Anlagen nicht mehr realisierbar (McCullough 2008).

Damit in den Infrastrukturern der U-Bahn- und Stadtbahnbetreiber eine Umrüstung bestehender Signaltechnik auf die zukünftige CBTC-Systeme erfolgreich ist, sind sinnvolle Migrationsstrategien zu entwickeln. Dies wird in Abschn. 8.1 geheldt. Grundlage einer erfolglichen Projektumsetzung ist die Projektierung von Streckeneinrichtungen und Fahrzeugeinrichtungen, was in den Abschn. 8.2 und 8.3 beschrieben wird. Den Nachweis über die korrekte Realisierung der automatisierungstechnischen Funktionen liefert ein effektives Testmanagement. Dies wird in Abschn. 8.4 geheldt. Vor Aufnahme des Betriebes muss das betriebliche Regelwerk erstellt werden, bzw. im Rahmen eines Erneuerungsprojekts angepasst werden (Abschn. 8.5). Abschlussbend müssen – wie in Abschn. 8.6 dargestellt – verschiedene Zielgruppen des Betriebers zu den neuen Technologien geschult werden.

# 8.1 Definition der Migrationsstrategie

Die richtige Wahl der Erneuerungsstrategie ist einer der wichtigen Erfolgsfaktoren. Dies gilt insbesondere für Projekte, die nicht „auf der grünen Wiese“ (englisch: green field projects) realisiert werden. Es gibt keine zu berücksichtigende Einflüsse und spezifische Einschränkungen, die bei der Definition der geeigneten Erneuerungsstrategie mit bedacht werden müssen. Die Entscheidung wird zusätzlich noch dadurch erschwert, dass die gewählte Ernueuerungsstrategie einen enormen Kosteneffekt aufweist. Verschiedene Ernueuerungsstrategien werden nachfolgend mit ihren bestehenden Einschränkungen, sowie den jeweiligen Vor- und Nachteilen beschreiben.

Die nachfolgenden Zielsetzungen gelten unabhängig von der gewählten Erneuerungs-strategie:

- Minimierung der Auswirkungen von Streckensperrungen auf den Fahrgastbetrieb: Ein möglichst ungehinderter Bauablauf erfordert während der Umsetzung der Erneuerungs-strategie Streckensperrungen. Hierbei mussen die Streckensperrungen selbst früherzeitig geplant werden. Hierbei gibt es zwei unterscheidliche Strategien:

- Ausschließlich Nutzung von Nachsperrpaufen: Der erste Ansatz ist die ausschließlich Nutzung von Nachsperrpaufen (in der Regel 3 bis 4 Stunden in jeder Nacht) für die Installationsarbeiten. Diese Strategie hat den unbestreitbaren Vorteil, dass sie keine Auswirkungen für die Fahrgäste hat. Das Fahrplanangebot wird auch während der Bauphase ohne Einschränkungen aufrechterhalten und muss nicht durch kostenträchtige Schienenersatzverkehrte kompensiert werden. Nachteil dieser Strategie ist, dass durch die für das tägliche Einrücken in den Baustellenbereich und die Räu

mung der Baustelle erforderlichen Vor- und Nachlaufzeiten sowie die in der Regel kurze Zeit einer nachtlichen Sperrpause sehr weniger Zeit für die Durchführung der erforderlichen Bauarbeiten verbleibt. Der Baufortschnitt vollzieht sich davon weniger zugig und die Bauzeit erstreckt sich hierdurch über einen längeren Zeitraum. Da über die eigentlichen Lohnkosten hinaus noch erhebliche Zuschläge für Nacharbeit zu zahlen sind, bringt diese Strategie auch erhebliche Kosten mit sich.

Vollsperrung der Strecke: Ein gegensatzlicher Ansatz ist die Vollsperrung der Strecke. Die komplete Sperrung ermöglicht einen optimalen Bauablauf, da Vor- und Nachlaufzeiten für die tägliche Einrichtung und Rücknahme von Baustellenbereichen entfallen. Da die Arbeiten in thisem Ansatz nicht zwingend nachts durchgeführt werden müssen, konnen bei thisem Ansatz die erheblichen Zusatzkosten für Zuschläge für Nacharbeit entfallen. Allerdings sind mit thisem Ansatz massive Auswirkungen für die Fahrgäste verbunden, da das Fahrtenangebot komplett entfällt und mit Schienenersatzverkehren aufgefangen werden muss. Aus thisem Grund werden Vollsperrungen in der Regel vorzugsweise in den Sommerferien durchgeführt, da hier durch die ohnehin geringere Verkehrsnachfrage weniger Fahrgäste von den Streckenspperrungen betroffen sind. Außer dem müssen die eingesparten Kosten für Nachzuschläge und Produktivitätsgewinne sorgfältig gegen die erheblichen Zusatzkosten für umfangreiche Produktivitätsgewinne sorgfältig gegen die erheblichen Zusatzkosten für umfangreiche Schienenersatzverkehre abgewogen werden.

Gewährleistung einer ausreichenden Fahrzeuganzahl für den Betrieb: Neben den zuvor beschrieben Streckensperrungen muss auch die Ausrüstung der Fahrzeuge von Beginn an mit bedacht werden. Für die Ausrüstung der Fahrzeuge müssen diese für einen gewissen Zeitraum außer Betrieb genommen werden, um in der Werkstatt mit der neuen Fahrzeugausrüstung versehen zu werden. Hierdurch reduziert sich während des Migrationszeitraums zumeist die Fahrzeugreserve, wenn nicht gar die Anzahl der für den Betrieb zur Verfugung stehenden Fahrzeuge. Die Umbaustrategie muss dazu früherzeitig mit dem für die Fahrzeuge verantwortlichen Unternehmensbereich abgestimmt werden. Außer dem müssen auch geeignete Werkstattkapazitäten (Gruben und Testgleise) für die Durchführung der Fahrzeugumrüstung zur Verfugung stehen.

- Minimierung der technischen und betrieblichen Risiken während der Migrationsphase: Hierbei sind unter anderen auch Rückwirkungen von Veränderungen im Gesamtsystem zu bewerten. So ist beispelsweise bei einer nachträglichen Ergänzung von Bahnsteigtären zu prüfen, inwieweit Bahnsteigflächen für das Fahrgastaufkommen (Wartefläche) oder für die Entfluchtung im Falle eines Notfalls noch ausreichend sind. Außen dem führt das nachträgliche Einbringen von Bahnsteigtären im Stationsbereich zu weiteren nachträglichen Änderungen beispelsweise hinsichtlich der Be- und Entlüfung.  
- Minimierung der Kosten für die Migrationsphase: Hierbei sind auch die Investitions- und Betriebskosten etwaiger Doppelausrüstungen von Fahrzeugen und Infrastruktur zu bewerten. Jede zusätzlich vorgehaltene Einrichtung muss beispelsweise regelmäß inspi Ziert und instand gehalten werden.

Um das Projektrisiko zu口中ern, werden während der Bauphase streckendeite Umschalteinrichtungen zwischen dem alten Zugsicherungssystem und dem neuen Zug-sicherungssystem sowie mögliche Rückfallebenen zwischen dem neuen und dem bestehenden Zugsicherungssystem empfohlen. Die CBTC-Streckeneinrichtung (Streckenzentrale, Funksystem und Ortungsreferenzpunkte) kann beispelseweise als Overlay-System zu einem bestehenden Zugsicherungssystem installiert werden. Auf jeder Fall sind die projektspezifischen Besonderheiten bei der Auswahl der Erneuerungsstrategie zu berücksichtigten. Im Folgenden werden mit der Doppelausrückung von Fahrzeugen und der Doppelausrückung der Infrastruktur die beiden unterscheidlichen Strategieoptionen beschrieben und hinsichtlich ihrer Vor- und Nachteile bewertet.

# 8.1.1 Doppelausrüstung der Fahrzeuge

Eine mögliche Strategie für die Ernneuerung der Zugsicherung im Netz eines Betreibers ist die Doppelausrüstung von Fahrzeugen und der abschnittsweise Umbau des gesamten Netzes. Die Migration erfolgt hierbei wie folgt:

Alle Züge werden mit den neuen CBTC-Fahrzeuggeräten ausgerüstet. Darüber hinaus sind (zumindest im ersten Bauabschnitt) alle Streckeneinrichtungen bereits installiert worden. Eine neue Leitstelle wird - parallel zum Betrieb der bestehenden Leittechnik - eingerichtet. Auf dieser Grundlage konnen während der Tageszeiten ohne Betrieb (in der Regel nachts) zunachst statice Tests und im Anschluss dynamische Tests für das neue Zugbeeinflussungssystem durchgeführt werden. Für die Durchführung der Testaktivitäten werden die Weichen und andere notwendige Fahrwegelelemente über eine Umschalteinrichtung mit dem neuen Zugsicherungssystem verbunden. Nach den nachtlichen Testphasen wird die Kontrolle über die Weichen und die anderen Feldelemente über die Umschalteinrichtung wieder an das bestehende Zugsicherungssystem zurückgegeben. Sobald die dynamischen Tests vollständig durchgeführt worden sind, kann im ersten Abschnitt der Betrieb mit dem neuen Zugbeeinflussungssystem aufgenommen werden. Deshalb müssen bereits früherzeitig im Projekt alle Züge, die in diesen Streckenabschnitt einfahren, über die entsprechende CBTC-Fahrzeugeinrichtungen verfügen. Auf diese Weise werden Schritt für Schritt die{nachsten Bauabschnittte entlang der Linie mit CBTC-Streckeneinrichtungen in Betrieb genommen, bis die komplette Linie umgerüstet ist. Ist der Probebetriefb mit dem neuen Zugbeeinflussungssystem erfolgreich verlaufen, konnen die Altsysteme Rückgebaut werden. Diese Erneuerungsstrategie erfordert in der Übergangsphase eine Systemumschaltung zwischen dem bestehenden Zugbeeinflussungssystem und dem neuen Zugbeeinflussungssystem an den Grenzen der jeweiligen Baustufen. An einer definierten Systemwechselstelle schaltet der Fahrer zwischen den Zugbeeinflussungssystemen um. Hierfür werden in der Regel Stationsaufenthalte genutzt, da der Zug hier halt. Die Grenze muss mit Sorgfalt ausgewählten werden. Die Stellwerksgrenzen des Altsystems müssen hierbei mit berücksichtigt werden. Eine Systemgrenze innerhalb eines Stellwerksbereichs des Altsystems erfordert umfassende Änderungen im

Bestandssystem, die möglichst vermieden werden sollenen. Die Anzahl der Systemwechselstellen sollte so gering wie möglich sein, da jeder Systemwechselstelle bzw nur vorübergehender Natur ist, jedoch eine umfassende Projektierung erfordert. Die Leitebene kann oft ohne aufwändige Daten Schnittstellen realisiert werden (Arpaci und Schwarte 2013).

These Erneuerungsstrategie weist die folgenden Vor- und Nachteile auf:

Die Vorteile dieser Erneuerungsstrategie sind wie folgt:

- Eine schrittweise Erneuerung der signaltechnischen Infrastruktur ist möglich.  
- Jede Bauphase verfügbar im Abschnitt über ein einheitliches Betriebskonzept. Es gibt in einem Abschnitt keinen Mischbetrieb mit verschiedenen Zugbeeinflussungssystemen.

Die Nachteile dieser Erneuerungsstrategie sind wie folgt:

- Zum Zeitpunkt der Umrüstung des ersten Streckenabschnitts müssen bereits alle in thisem Abschnitt verkehrenden Züge über eine CBTC-Fahrzeugeinrichtung verfügen.  
- Es werden Systemwechselstellen besteht, an denen die Umschaltung zwischen altem Zugbeeinflussungssystem und dem neuen Zugbeeinflussungssystem erfolgt.  
- Möglicherweise stellt die Installation einer zweiten Fahrzeugeinrichtung technisch eine unlosbare Aufgabe dar, da auf den Fahrzeugen keine ausreichenden Einbau-räume für eine vorübergehende zweite Fahrzeugeinrichtung vorhanden sind.

# 8.1.2 Doppelausrücktung der Streckeneinrichtungen

Die zweite mögliche Erneuerungsstrategie ist die doppelte Ausrüstung der Streckenbereiche, sodass ein Mischbetrieb von Fahrzeugen mit konventionellem Zugbeeinflussungssystem und Fahrzeugen mit CBTC-Fahrzeuggeräten möglich wird. Hierbei werden in einer ersten Projektphase alle CBTC-Streckengeräte im gesamten Netz installiert. Hierbei erhält das neue Zugsicherungssystem die für die Steuerung und Überwachung der Komponenten des alten Zugsicherungssystems erforderlichen technischen Schnittstellen.

Erhalten beispelssweise in einem alten Zugbeeinflussungssystem die Fahrzeuge die Informationen über ihre zulässige Fahrweise über von Gleisstromkreisen übertragene Geschwindigkeitscodes, muss das neue Stellwerk ebenfalls über eine Schnittstelle zu diesen Gleisstromkreisen verfügen. Eine neue Leittechnik wird parallel zur bestehenden Leittechnik eingerichtet. Diese Erneuerungsstrategie erfordert im Gegensatz zu der im vorherigen Abschnitt dargestellen Doppelausrüstung von Fahrzeugen nicht, dass in der ersten Phase schon alle Züge mit der CBTC-Fahrzeugeinrichtung ausgestattet werden. Sobald alle Teilsysteme installiert worden sind und die statischen Tests abgeschlossen sind, können die dynamischen Tests beginnen. Dies erfolgt in der Regel außerhalb der regulären Betriebszeiten (das heißt in der Regel nachts). Die Steuerung und Überwachung der Weichenantriebe, Signale und Komponenten des bestehenden Zugsicherungssystems werden mittels Umschalteinrichtung auf das neue Zugsicherungssystem umgestellt. Nach

dem Test wird die Steuerung und Überwachung wieder an das Altsystem übergeben. Sobald die dynamischen Tests abgeschlossen sind, kann der Fahrgastbetrieb im Mischbetrieb aufgenommen werden (Arpaci und Schwarte 2013).

Das neue Zugbeeinflussungssystem erkennt automatisch mit CBTC ausgerüstete Fahrzeuge. Die CBTC-Fahrzeuge werden im Abstandshalteverfahren des Fahrens im wandernden Raumabstand (mit absolutem Bremswegabstand) geführt. Die noch nicht mit CBTC ausgerüsteten Fahrzeuge werden wie bisher auch vom bestehenden Zugbeeinflussungssystem geführt. Hierbei konnen die Altechniken unterscheidlich ausgeprügt sein wie beispelsweise ein punktformiges Zugbeeinflussungssystem, welche lediglich das Überfahren eines Halt zeigenden Signals verhindert oder aber ein ätheres kontinuierlich wirkendes Zugbeeinflussungssystem, welches Informationen über die zulässige Fahrweise über Geschwindigkeitscodes auf das Fahrzeug übermittelt. Das neue Zugbeeinflussungssystem stellt sichere, dass im Mischbetrieb zwischen Fahrzeugen mit CBTC und ohne CBTC ausreichende Abstände zwischen den Zugfahrenen eingehalten werden.

Üblicherweise werden alle Teilsysteme ersetzt, wenn eine Linie wegen Obsoleszenz (das heißt Teilsysteme sind nicht mehr lieferbar) erneuert werden muss. Daher werden in dieser Beispiel alte Gleisfreimeldesysteme und Zugbeeinflussungseinrichtungen in einer zweiten Phase ersetzt. Eine neue Gleisfreimeldung mit Achszählsystemen kann muhelos parallel zu bestehenden Gleisfreimeldesystemen installiert werden. Während der Migrationsphase kommt bereits das neue Zugbeeinflussungssystem zum Einsatz. Nur die Software muss später für die Tests des letzten Abschnitts ohne das Altsystem getauscht werden. Dies erfolgt in der Betriebspause. Sobald die dynamischen Tests mit der finalen Systemkonfiguration abgeschlossen sind, kann das letzte Altsystem abgeschaltet werden. Bevor dies allerdings passieren kann, müssen alle Züge, welche auf der Linie verkehren, mit CBTC ausgerüstet sen. Züge mit dem Altsystem konnen nicht mehr auf der Linie verkehren.

Der letzte Schritt ist der Rückbau des Altsystems, sobald der Testbetrieb erfolgreich absolviert wurde. Diese Ansatz der Migration hat die folgenden Vor- und Nachteile:

Die Vorteile dieser Erneuerungsstrategie sind wie folgt:

- Nicht alle Fahrzeuge müssen zu einem frühen Zeitpunkt mit CBTC ausgerüstet sein.  
- Es gibt keine Baustufenschnittstelle mit einem Systemwechsel.

Die Nachteile dieser Erneuerungsstrategie sind wie folgt:

- Es mussen komplexe Simulationen durchgeführt und Schnittstellen zur bestehenden Signaltechnik implementiert werden.  
- Es mussen zwei Testphasen mit entsprechenden Systemkonfigurationen durchgeführten werden.  
- Es bestehen zu einem Zeitpunkt verschiedene Betriebskonzepte in einem Streckenabschnitt in Abhängigkeit des Ausrüstungszustands des jeweiligen Zugtyps.

Die Doppelausrüstung von Streckeneinrichtungen wird oftmals dann ausgewählt, wenn eine Fahrzeugflotte nichtrechtzeitig verfügbar ist oder wenn nur neue Fahrzeuge ausgerüstet werden sollen oder konnen.

# 8.2 Anwendungsspezifische Konfiguration automatischer Zugbeeinflussungssysteme

Leit- und Sicherungssysteme im Eisenbahnverkehr müssen individuell an die strecken-, betriebs- und Fahrzeugspezifischen Randbedingungen angepasst werden. Diese Anpassung oder Konfiguration des Systems wird auch als Projektierung bezeichnet. Für einen sicheren Betrieb muss sichergestellt werden, dass die Projektierungsdaten fehlerfrei sind. Eine fehlerhafte Projektierung (wie zum Beispiel eine fehlerhaft projetierte zulässige Geschwindigkeit) kann somit trotz der nachgewiesenen Fehlerfreiheit der anwendungsunabhängigen Software des CBTC-Systems zu einem Versagen einer Sicherheitsrelevanten Funktion führen. In der Ausführungsphere erstellt der Systemhersteller alle herstellerspezifischen Ausfuhrungsunterlagen für die Strecken- und Fahrzeugeinrichtungen, die auf den Eingangsdaten des Betreibers basieren. Der Arbeitsaufwand des Herstellers im Rahmen der Ausführungsphere sowie die Kosten der Projektierung sind sehr stark abhängig von der Qualität der Eingangsdaten des Betreibers. Nachfolgend werden Aspekte der Projektierung von Strecken- und Fahrzeugeinrichtungen automatischer Zugbeeinflussungssysteme dargestellt (Schroeder 2002).

# 8.2.1 Kategorien streckenspezifischer Konfigurationsdaten

Das Datenmodell des Streckenatlasses muss ein umfassendes Bild über die Schiereninfrastruktur mit allen Sicherheitsrelevanten Parametern enthalten. Konkret umfassen die streckenspezifischen Projektierungsdaten die folgenden Kategorien:

- Gleisgeometrie: Grundsätzlich wird zunachst die Geometrie der Gleise erfasst. Die Erfassung der Geometrie kann durch bereits digital vorliegende Daten, digitalisierte Planzeichnungen oder aus der geometrischen Vermessung staatfinden, wie es heute in der Praxis schon durchgeführt wird.  
- Gleistopologie: Im nachsten Schritt wird die Topologie aus der Geometrie abgeleitet. Topologische Knotenpunkte sind Weichen oder Gleisenden; Kreuzungsweichen werden topologisch durch bis zu vier Weichen repräsentiert. Die topologischen Punkte werden aus der Geometrie berechnet und die dazwischenliegenden Streckenelemente als topologische Gleiskanten identifiziert. Ergebnis eine ist eine Topologie, bei der die geometrisch beschriebenen Streckeneigenschaften auf Kanten mit wahren langen bezogen sind.  
- Ergänzung weiterer streckenspezifischer Daten: Die Aufnahme der weiteren streckenspezifischen Daten kann parallel zur Aufnahme der Topologie erfolgen, indem auf dem Weg von einem Referenzpunkt zum nachsten besoin den Daten zur Aufnahme der Topologie diese Daten mit entsprechender Genauigkeit aufgenommen werden. Beispiele sind Angaben zu Belastbarkeit des Oberbaus, Lichtraumprofil, Notbremsüberbrückung oder Traktionsstromversorgung.

# 8.2.2 Kategorien Fahrzeugspezifischer Konfigurationsdaten

CBTC-Systeme haben Bremsmodelle, die gemäß der für das jeweilige Fahrzeug Charakteristischen Parameter in anwendungsspezifisch konfigurierbaren Systemen hinterlegt werden. Möglichkeit müssen diese Parameter durch praktische Erprobungen ermittelt werden. Zu bestimmen sind die folgenden Fahrzeugparameter:

- Traktionsabschaltung: Zeit vom Einleiten einer Zwangsbremsung bis die Zugkraft abgebaut ist.  
- Reaktionszeit: Zeit bis zur Übertragung des Brems signals im Zugverband und die Aufbauzeit der Bremskraft in den Bremsssystemen der einzelnen Wagien.  
- Bremsverzögerung: Mittlere Verzögerung während der Abbremsung, gestaffelt nach verschiedenen Geschwindigkeitsbereichen.

Die Bremsmodelle werden in der Regel für jeder Fahrzeugserie entsprechlich parametrisiert. Die Parameter konnen für die Betriebsbremsung und für die Zwangsbremsung für jedem Bremsmodell entsprechlich festgelegt werden. Sicherheitsrelevant ist nur die Zwangsbremsung.

# 8.2.3 Qualitätsmerkmale von Konfigurationsdaten

Durch welche Eigenschaften der Eingangsdaten oder der Projektierungsdaten kann die geforderte Qualität von Projektierungsdaten beschreiben werden? Zur Beschreibung der Qualität von Eingangsdaten wurden in (Schroeder 2002) folgende wesentlichen Qualitäts-merkmale identifiziert:

- Strukturelle Konsistenz: Die strukturelle Konsistenz bezieht sich auf die Abbildung der real existierenden physikalischen Objekte (Gleis, Weiche, usw.) als Informationen innerhalb eines Datenmodells. So dürfen zwischen zwei benachbarten Gleisabschnitten keine Sprünge in ihrer Lage existieren. Zwei Datenquellen dürfen nicht einen eindeutigen Punkt in der Realwelt mit zwei nicht eindeutig ineinander überführbaren Koordinaten beschreiben (Schroeder 2002).  
- Vollständigkeit: Der Wirkbereich einer Zugsicherungsanlage muss informationsstechnisch vollständig über Projektierungsparameter beschreiben sein. Eine unvollständige Beschreibung des realen Streckenabbildes führt dazu, dass die Technik ihre Sicherungsfunktion nicht vollständig über den gesamten Wirkbereich wahrnehmen kann (Schroeder 2002).  
- Aktualität: Projektierungsdaten können nach der Häufigkeit der Aktualisierungen in staatische und dynamische Daten unterschieden werden. Für Projektierungsdaten, diehäufig geändert werden müssen oder nur über einen kurzen Zeitraum beschränkt gültig

sind (zum Beispiel temporäre Langsamfahrstellen), ist die Aktualität der Daten ein wesentliches Qualitätsmerkmal (Schroeder 2002).

- Genauigkeit: CBTC fordert, im Gegensatz zu konventionellen Systemen, metergenaue Angaben zu Standorten von sümttlichen relevanten Streckenelementen wie Signalen (sofern vorhanden), Balisen oder Weichen. Daher sind auch geeignete Messmethoden zu definieren.  
- Korrektheit: Durch „Papierprozesse“ und fehlende Schnittstellen findet eine Übergabe der Daten zwischen Projektphasen möglich in nicht maschinell lesbaren Formaten statt. Der deshalb notwendige manuelle Datentransfer ist durch hohe Aufwände und Fehleranfälligkeit geprägt. Wünschenswert sind durchgängige digitale Prozesse ohne Medienbrüche.

# 8.2.4 Qualitätssichernde Prozesse für Konfigurationsdaten

Für die Entwicklung und Einführung von Zugsicherungssystemen müssen in Europa harmonisierte Sicherheitsnormen berücksichtigt werden. Anforderungen, die die Projektierung eines technischen Systems betreffen, leiten sich der DIN EN 50128 ab. In dieser Kapitel wird unterschieden zwischen der generischen Software (in der Regel Programme), die eine Zulassung für einen bestimmten Typ einer Zugsicherungstechnik hat, und den Projektierungsdaten, die je nach dem Anwendungsfall entsprechend generiert und im Laufe des Systemlebenszyklus gepflegt werden müssen. Im Rahmen der Qualitätssicherung für die Projektierungsdatenmusten die folgenden Dokumente erstellt werden:

- Daten-Generierungsplan: In dieser Dokument wird der Prozess der Datengenerierung beschreiben. Insbesondere müssen die einzelnen Verfahren zur Daten-Generierung sowie die verwendeten Softwaretools dargestellt werden, die im Rahmen des Datengenerungsprozesses verwendet werden. Insofern ist es erforderlich, dass darüber becharakterung der Datenerfassung auch alle qualitatssichernden Prozesse erlautert werden. Für manuelle Handlungen muss die Qualifikation des eingesetzten Personen festgelegt werden. Für die verwendeten Werkzeuge (Soft- und Hardware) muss dargestellt werden (Koch et al. 2014; Schütte et al. 2008), dass diese frei von systematischen oder zufälligen Fehlern arbeiten. Gegebenenfalls muss auch die Unabhängigkeit zwischen der eigentlichen Datengenerierung sowie der Verifikation und Validation der projektierten Daten nachgewiesen werden (DIN EN 50128:2012-03).  
- Daten-Testplan: In einem Daten-Testplan werden alle anzuwenden, qualitäts-sichernden Maßnahmen festgehalten, die im Rahmen des Daten-Generierungsplans spezifiziert worden sind. Beispiele hierfür sind Testberichte, sowie Berichte im Rahmen der Verifikation und Validation der Projektierungsdaten (DIN EN 50128:2012-03).  
- Daten-Testbericht: Die Ergebnisse der im Testplan spezifizierten Tests werden in einem Testbericht dokumentiert (DIN EN 50128:2012-03).

# 8.2.5 Erfassung streckenspezifischer Konfigurationsdaten

Ausgangspunkt für die Projektierung von Streckeneinrichtungen sind Bestandspläne. Bestandspläne (englisch: „as built documentation" oder im weiteren Verlauf des Lebenszyklus auch „as maintained documentation") stellen den gegenwärtigen Zustand der Bahnanlagen und deren früherer Umgebung dar. In der Regel umfassen die Angaben die Beschreibung samtlicher Bahnanlagen, Kilometrierungen der Gleise, geodatische Lage und Höhenfestpunkte, Krümmungs- und Neigungsverhältnisse der Gleise, Bauarten der Weichen und Kreuzungen, Gleisabstände, Gleisnummern, Signal- und Fahrstraßebeziehnungen sowie Weichengrenzzeichen. Diese Unterlagen unterliegen einer Fortführungspflicht und sollen nach Möglichkeit zu jederzeit korrekt und aktuell sein (Adler et al. 1981). Die Hersteller von CBTC-Systemen benötigen all diese Angaben, um auf dieser Grundlage die Umbaumaßnahmen zu planen sowie die anwendungsspezifische Konfiguration des CBTC-Systems zu erstellen. Dort wo Bestandspläne nicht in der geforderten Qualität vorliegen, müssen diese zu Beginn eines Projekts mit hohem Aufwand aktivell erstellt werden. Falsche oder ungenaue Daten wie beispelsweise Distanzen konnen im Prozess der Realisierung, der Abnahme und im Betrieb large unentdeckt bleiben. Dies kann zu zeit- und kostenintensiver Fehlersuche, sporadischen Störungen im Betrieb, betrieblichen Einschränkungen oder Behinderungen und in Extremfällen zu potenziellen Gefährduren führen (Schütte et al. 2008).

Ein Beispiel, Projektierungsdaten effizient zu erfassen ist der Einsatz von Gleisgeometriemessfahrzeugen zur prazisen Aufzeichnung der mit CBTC auszurustenden Strecke. Die von den Fahrzeugen erfassten Daten fließen nach entsprechender Nachprozessierung in den Aufbau des Streckenatlasses ein, der in den CBTC-Systemen sowohl an Bord von Zügen als auch in den Streckeneinrichtungen als gemeinsames Koordinatensystem von Fahrzeugen und Strecken verwendet wird. Die Gleisgeometriemessfahrzeuge sind in der Lage, die Gleislage mit hochster Prazision zu erkennen sowie aufzuzeichnen. Sümmtliche Messungen werden von elektromechanischen, inertialen oder Lasermesseinrichtungen und einem elektronischen Datenverarbeitungssystem kontinuierlich aufgezeichnet. Idealerweise befinden sich die messtechnischen Einrichtungen auf einem für das jeweilige Netz zugelassenen Messfahrzeug. Auf diese Weise wird eine Aufzeichnung und die Speicherung der gesessenen Daten sowie eine Echtzeitauswertung bei Messgeschwindigkeiten von bis zu  $90\mathrm{km / h}$  möglich (Cabrera 2009).

# 8.3 Umrüstung der Fahrzeuge mit CBTC-Fahrzeugausrüstung

Die Fahrzeuge des Betreibers müssen mit CBTC-Fahrzeuggeräten ausgestattet werden. Hierbei kann es sich um neue Fahrzeuge handeln. In Bestandsnetzen müssen auch vorhandene Fahrzeuge umgerüstet werden. Bei der Ausrüstung von Fahrzeugen müssen Aspekte der betrieblichen, Mechanischen und elektrischen Integration zwischen Fahrzeug-

bauer und CBTC-Hersteller betrachtet werden (Schnieder et al. 2021). Außer dem*Müssen auch die wesentlichen Fahrzeugparameter (bspw. garantierte Bremskurven) abgestimmter werden.

# 8.3.1 Definition betrieblicher Anwendungsfälle

Ausgangspunkt der Projektierung der Fahrzeugeinrichtungen ist immer die Erstellung eines Betriebskonzepts. Hierbei muss – ausgehend von der betrachteten Automatisierungsstufe –dezidiert betrachtet werden, wie der Baukasten eines CBTC-Systems in der Betriebsabwicklung konkret angewendet werden soll. Zu betrachtende Aspekte sind hierbei unter anderem die Aufnahme in und die Entlassung aus verschiedene Automatisierungsgraden sowie die Führung des Fahrzeugs in verschiedenen Betriebsarten (mit korrespondierenden Überwachungsfunktionen). Wesentlich ist – gerade bei einem Betrieb in GoA4 – insbesondere der betriebliche Ablauf bei technischen Störungen sowie Notfall- und Rettungskonzepte. Die verschiedene betrieblichen Anwendungsfälle müssen in den folgenden Integrationsschritten hinsichtlich ihrer Auswirkung auf die konkreten technischen Eigenschaften des CBTC-Systems betrachtet werden.

# 8.3.2 Definition Mechanische Integration des CBTC-Fahrzeuggeräts

Gemeinsam mit dem Lieferanten des CBTC-Systems und der mit dem Fahrzeugumbau beauftragten Firma wird die Positionierung der erforderlichen CBTC-Komponenten an und in den Fahrzeugen festgelegt. Hierbei sind vor allem die folgenden Komponenten in das Fahrzeug zu integrieren:

- Gehäuse (Geräteschrank/Geräteschränke oder Unterflurcontainer) für die zentralen und im Zugverband redundanten Rechnereinheiten. Dies umfasst Baugruppenträger für die Sicherheitsrelevanten Funktionen des Zugbeeinflussungssystems (Automatic Train Protection, ATP), für Funktionen der nicht sicheren Fahrzeugsteuerung einschließlich der automatisierten Fahr-/Bremssteuerung und der automatischen Türsteuerung (Automatic Train Operation, ATO) sowie Steckerfelder für die Übernahme und Übergabe weiterer Signale von und zur Fahrzeugsteuerung zur Übernahme weiterer Automatisierungsfunktionen für höhere Automatisierungsgrade (bspw. Auf- und Abrüsten des Fahrzeugs).  
- Konventionelle Schaltungstechnik zur Anpassung der Einzelsignale zwischen Zug-sicherungssystem und Fahrzeug. Fahrzeugsignale müssen aus Sicherheitsgründen oft für das Zugsicherungssystem aufgereitet werden (Bereitstellung 2-kanaliger Signale). Signale die vom Zugsicherungssystem ausgegeben werden, können oft die Fahrzeugkomponenten nicht direkt ansteuern.

- Komponenten für die Kommunikation mit der Streckenausrüstung. Hierbei müssen Fahrzeuganten unter dem Fahrzeug für das Auslesen von Transpondern für die Synchronisation der Weg- und Geschwindigkeitsmessung positioniert werden. Dafür müssen Produktspezifische physikalische Besonderheiten, wie ausreichende eisenfreie Bereiche um die Antenne berücksichtigt werden. Auch muss für diese zusätzlichen Anbauten unter dem Fahrzeug die Profilfreiheit nachgewiesen werden, das heißt sie)dürfen nicht soweit in den Gleisbereich ragen, dass sie beispelssweise mit bereits vorhandenen streckenseitiger Antennen von Altsystemen in Kontakt kommt. Des Weiteren müssen Funkantennen für die kontinuierliche, bidirektionale Datenübertragung zwischen Fahrzeug und Strecke auf den Fahrzeugen vorgesehen werden. Ein wichtiges Kriterium für den Anschluss der Funkantennen sind die zulässigen maximalen Leitungslangen hin zu den entsprechenden Rechnerkomponenten sowie die Dämpfung durch Verbindungselemente. Die Funkantennen werden von den Betreibern bevorzugt hinter der Frontscheibe des Fahrzeugs installiert. Hierbei ist zu prufen, ob es sich um mit Metall bedampfte Scheiben handelt, die unter anderem davon sorgen, dass weniger Sonne in den Führerstand fällt. Leider dampfen oder reflektieren solche metallbedampften Scheiben auch den Mobilfunkempfang erheblich, sodass andere Einbauorte für die Funkantennen auf dem Fahrzeug gefunden werden müssen.  
- Komponenten zur direkten Weg- und Geschwindigkeitsmessung. Hierbei kann es sich je nach dem Odometriebkonzept des jeweiligen Herstellers um verschiedene technische Komponenten handeln. Bei Wegimpulsgebern müssen frei Achslagerdeckel idealerweise nicht gebremster oder nicht angetriebener Achsen im Zugverband identifiziert werden. Auch die Verwendung eines gemeinsamen Polrads mit anderen Wegimpulsgebern der Fahrzeugsteuerung ist möglich. Die Radarsensoren sind so anzuordnen, dass die Radarkegel sich ungestört ausbreiten und Reflection von Untergrund ungestört empfangen werden können. Auch für möglicherweise eingesetzte Beschleunigungsgieber gibt es zu berücksichtigende Randbedingungen bei der Positionierung im Fahrzeug.  
- Komponenten des Datenbusnetzwerks des Zugsicherungssystems. CBTC Systeme besitzen ein eigene, von der Fahrzeugsteuerung unabhängiges Datenbusnetzwerk (meist Ethernet). Eine wichtige Komponente im Datenbusnetzwerk des CBTC Systems ist ein Modem für die Datenübertragung zwischen Fahrzeug und Strecke, welches wegen den zulässigen Leitungslangen zu den Antennen nicht im Bereich derzentralen Recheneinheit untergebracht werden kann. Hinzu kommt abhängig von der Fahrzeug-konfiguration diverse Switches beispisseweise zur Signalverständigung.  
- Bedien- und Anzeigeelemente. Selfest Fahrzeuge, die hauptsächlich im begleiteten fahrerlosen oder unbegleiteten fahrerlosen Betrieb verkehren sollen, benötigen zusätzliche Bedien- und Anzeigeelemente für das Zugsicherungssystem. Beispiele hierfür sind die Displays, Taster und Störschalter. Diese sind gemäß den Vorgaben einschlögiger technischer Regelwerke auf dem Führstand anzuordnen (vgl. UIC (2002) und DIN EN 16186-1:2019-04). Hierbei müssen abide der Einhaltung normativer Sichtfelder bei der Integration von Komponenten in den Führstand auch Aspekte der Ergonomie mit Berücksichtigung finden.

Mechanische Integration bedeutet hierbei, entsprechend große Bauräume für die Komponenten im und am Fahrzeug zu identifizieren. Auch muss dazu Sorge getragen werden, dass die betreffenden Komponenten in einer Art und Weise befestigt werden müssen, dass diese dauerhaft den dynamischen Beanspruchungen des Bahnbetriebs standhalten. Außer dem)dürfen durch die Befestigungen keine Sicherheitsrelevanten Bauteile (z. B. Drehgestelle) in ihrer Substanz geschwacht werden. Bei Nachrüstungen ist auch das Gewicht des Fahrzeugs zu berücksichtigten. So darf durch die zusätzlichen Komponenten für ein Zugsicherungssystem die zulässige Achstast nicht übersritten werden.

# 8.3.3 Elektrische Integration des CBTC-Fahrzeuggeräts

Allgemein ist das CBTC-System in die vorhandene Fahrzeugsteuerung zu integrieren. Hierbei muss bei Bestandsfahrzeugen die bestehende elektrische Ausrüstung des Fahrzeugs erfasst werden. Die Fahrzeugseitigen Schnittstellen (Input/Output) sind kein fonctionellen Stromlaufplänen zu beschreiben. Gerade bei Bestandsfahrzeugen ist zu prüfen, ob die Anforderungen an Sicherheitsfunktionen im Bereich der Fahrzeugsteuerung den aktuellen Sicherheitsanforderungen entsprechen (vgl. VDV (2009) und IEC 62267). Gegebenenfalls sind in Abstimmung mit der Zulassungsbehörde (z. B. Technische Aufsichtsbehörde, TAB) Modifikationen an der Fahrzeugsteuerung erforderlich. In der Regel kommt es hier zu einem größeren Abstimmungsbedarf zwischen dem Fahrzeughersteller und dem Lieferanten des CBTC-Systems. Die Signale zwischen Fahrzeugsteuerung und CBTC-System konnen in sichere und nicht-sichere Signale unterteilt werden.

- Sichere Signale/Funktionen: (SIL  $\geq 1$ ): Beispiele für sichere Eingangssignale von der Fahrzeugsteuerung an das CBTC-System sind Bestätigungsstaster, Taster für den Start des halb automatischen Betriebs, Status der Sicherheitsbremse, Türstatus, Zugintegrität, Kuppelstatus. Beispiele für sichere Ausgangssignale des CBTC-Systems zur Fahrzeugsteuerung sind unter anderen die Ansteuerung der Sicherheitsbremse, die sichere Antriebsspere, bzw. Traktionsfreigabe (oft in Bestandsfahrzeugen Fahrzeugseite nicht vorhanden), die Türfreigabe und die Blockierung der Türen (Freigabe Türnotentriebelung).  
- Nicht-sichere Signale/Funktionen  $(SIL < 1)$ : Diese Signale sind zu definieren. Hier ist jeweils festzulegen, wie die Signale im Bereich der Fahrzeugsteuerung abgegriffen werden sollen, bzw. an diese übergeben werden sollen. Neben Hardwareänderungen am Fahrzeug sind ggf. auch Änderungen im Bereich der Software der Fahrzeugsteuerung erforderlich. Bevorzug wird die Übertragung nicht{sicherer Signale über den jeweiligen Fahrzeugbus (z. B. Multifunction Vehicle Bus, MVB oder Ethernet-Consist Network, ECN). Bei Bestands Fahrzeugen muss oft auf die Übertragung von Einzelsignalen zwischen Zugsicherungssystem und Fahrzeugsteuerung zusückgegriffen werden.

# 8.4 Umrüstung der Strecke mit CBTC-Streckenausrüstung

Die Umrüstung der Streckeneinrichtung auf das neue CBTC-System ist Gegenstand detailierter Planungen. Es hat sich allgemein bewährt, die gesamte Baumaßnahme in einzelne Baustufen zu trennen. Hierbei müssen die Baustufenschnittstellen sowohl in technischer als auch in betrieblicher Hinsicht sauber geplant werden. In der Regel beginn den die Baumaßnahmen in einem schwach befahrenen Streckenabschnitt in der Peripherie, um die Auswirkungen auf den Betrieb möglichst gering zu halten. Sind die eingesetzte Technik und die Bauabläufe erprobt, folgen betrieblichhigher belastete Streckenbereiche.

Der Umfang der Umrüstung bestimmt die konkrete Bauablaufplanung. Hierbei ist eine Betrachtung erforderlich, welche Komponenten ggf. wiederverwendet werden können oder ob Komponenten des neuen CBTC-Systems parallel zum Bestandssystem installiert werden können:

- Optionale Lichtsignale: Falls erforderlich können neue Lichtsignale parallel zu den bestehenden Lichtsignalen des Bestandssystems installiert werden. Die Signale unterstützen einen möglichen Mischbetrieb oder einen Betrieb auf der Rückfallebene in CBTC-Systemen.  
- Komponenten der sekundären Gleisfreimeldung: Achszahler für die sekundäre Gleisfreimeldung können problemlos als Rückfallebene parallel zu herkömmlichen Gleisfreimeldesystemen installiert werden.  
- Kabelanlage: Die Installation der neuen CBTC-Streckenausrüstung erfordert nach wie vor die Verlegung mehrerer Kupfer- und Glasfaserkabel entlang der Strecke. Der Zustand der bestehenden Kabeltröge muss untersucht werden. Manchmal sind neue Kabeltröge Kabelkanäle unvermeidlich, da die alten Kabeltröge nicht mehr verwendet werden konnen.  
- Technikräume: Die Standorte und die Anzahl der vorhandenen technischen Gebäude ergeben sich zumeist aus der Architektur und Technologie des Altsystems. Für neue Systeme gelten andere Zwänge. Auch zwischen den Anbietern gibt es Unterschiede. Typischerweise haben neue Systeme einen mehrentralen Ansatz. Die Vor- und Nachteile der Beibehaltung bestehender Standorte oder der Auswahl neuer Standorte müssen gegeneinander abgewogen werden.  
- Leitstelle: Die neue Betriebsleitstelle kann parallel zur alten Betriebsleitstelle eingerichtet werden. Hierbei wird wegen der technischen Komplexität mein auf technische Schnittstellen zwischen altem und neuem System verzichtet.

Zur Risikominderung und Minimierung der betrieblichen Auswirkungen während der Migration, werden streckenseitige Umschalteinrichtungen zwischen den neuen Zugsicherungsanlage und dem Bestandssystem empfohlen. Die neue Zugsicherungsanlage sollenen über

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/a0bb8592a834acc202ee45437515dfb5af36a5d956290c623ca14d303639c466.jpg)  
Abb.8.1 Kennzeichnung ungültiger Signale nach erfolgter Umschaltung

eine Umschalteinrichtung mit den Feldelementen (Weichenantrorie, Signale) verbunden sein. Die Umschalteinrichtung ermöglicht eine effiziente Prüfung und Inbetriebnahme während der betriebsfrei den Zeit.

Ist die Umschaltung erfolgreich vorgenommen und das CBTC-System im Fahrgastbetrieb, müssen die Signale des Altsystems als ungültig gekennzeichnet werden (vgl. Abb. 8.1). Dies geschieht durch Abdecken oder eine besondere Kennzeichnung (bspw. ein weißes Kreuz mit schwarzem Rand). Ist über eine gewisse Zeitspanne der störungsfreiheit Fahrgastbetrieb erfolgreich nachgewiesen worden, kann zu guter letzt die Demontage der Komponenten des Altsystems erfolgen. Dies ist in der Regel nicht mehr zeitkritisch und kann über einen längeren Zeitraum innerhalb der verfügbaren nachtlichen Sperrpausen ohne negative Auswirkungen auf den Fahrgastbetrieb erfolgen.

# 8.5 Definition der Teststrategie und Testdurchführung

CBTC-Systeme sind komplex und weisen weitere in Bezug auf das konkrete Kundenprojekt konfigurierbare Merkmale auf. Die Erfahrung der Hersteller mit der Inbetriebnahme von CBTC-Systemen und umfassende Testaktivitäten gewährleisten, dass ein richerer Fahrgastbetrieb aufgenommen werden kann. Die von den Herstellern verfolgten Teststrategien zielen darauf ab, Testaktivitäten im Feld auf das absoluterliche Mindestmaß zu beschränken. Allerdings können Testaktivitäten im Feld aus folgenden Gründen nicht vollständig vermieden werden (Diemunsch 2016):

- Betreiberspezifische Anpassungen: Die Betreiber fordern eine betrieberspezifische Zugsicherungstechnik, welche sie auf ihre spezifischen Besonderheiten anpassen möchen. Dies ist beispelsweise dann der Fall, wenn die Betreiber zusätzlich Funktionen fordern, die nicht dem Standardfunktionsumfang der herstellerspezifischen Produkte entsprechen. Teilweise sind die Betreiber aber auch zu Anpassungen gezwungen. Dies ist beispelsweise dann der Fall, wenn Fahrzeugeinrichtungen in die vorhandene Fahrzeugflotte integriert werden müssen. Die Tests insbesondere der Integration der Fahrzeugeinrichtungen in die Fahrzeuge können nicht im Hause des Herstellers durchgeführten werden.  
- Konkrete Gegebenheiten im Feld: Wesentliche Effekte zeigen sich erst bei einer praktischen Erprobung im Feld. So erfordern beispisse weisung die Zugortung als auch die Datenübertragung über Funk besondere Tests. Bei funkbasierten Systemen ist im Feld eine ausreichende Ausleuchting der Strecke durch ausreichend wie Testfahrten zu bestätigten.

Das Erfordernis, Testaktivitäten zu optimieren wird insbesondere dadurch verträkt, dass es sich bei einer Vielzahl aktueller CBTC-Projekte um eine Modernisierung von Zug-sicherungssystemen in bestehenden Anlagen handelt. Hier muss der Umbau der Zug-sicherungsanlagen mit minimalen Auswirkungen auf den Fahrgastbetrieb erfolgen. Diese Randbedingung erhöht die Komplexität der Projekte durch den auf die (kurzen) nachtlichen Sperrpausen beschränkten Zugang zur Strecke für die Montage, Tests und Inbetriebnahme. Aus thisem Grund müssen die Testaktivitäten optimiert werden, um einen Umbau während des laufenden Betriebs zu ermögenlichen. Dies geschieht dadurch, dass möglichst viele Tests bereits in den Testlaboren der Hersteller oder auf dedizierten Testgleisen der Betreiber durchgeführt werden.

# 8.5.1 Umwelttests

Bereits in der Entwicklung der generischen Anwendungen werden die entwickelten CBTC-Systeme gegen zu erwartende Umwelteinflüsse getestet. Diese Testergebnisse

werden für die spezifische Anwendung dahingehend überprüft, ob die in dem Test nachgewiesen Umweltereigenschaften auch für das betreffende Projekt zuteffen. Weichen die tatsächlichen Umweltereigenschaften von den spezifierten Umweltereigenschaften des Produkts ab, muss eine Änderungsauskirkungsanalyse durchgeführt werden. Der Nachweis der Umweltereigenschaften umfasst die folgenden Aspekte:

- Elektromagnetische Verträgelichkeit (EMV): Hierbei wird einerseits bewertet, ob auf den Prüfling wirkende elektromagnetische Felder einen Einfluss auf diesen haben. Anderersects werden auch die vom Prüfling emittierten elektromagnetischen Felder bewertet. Grundlage der Prüfungen sind einschlagige harmonisierte Normen (DIN EN 50121-1:2017).  
- Klimatests: Bei diesen Tests wird der Prüfling extremen Maximal- und Minimaltemperatoren ausgesetzt. Hierbei wird eine definierte Anzahl an Temperaturzyklen durchlaufen. Ebenso wird der Prüfling entsprechenden Luftfeuchtgkeiten ausgesetzt (DIN EN 50155:2018).  
- Mechanische Tests: Das Betriebsmittel muss ohne Verschlechterung der Eigenschaften ohne Fehlfunktionen Schwing- und Schockeinwirkungen, wie sie im Betrieb auftreten konnen, standhalten. Bei den genormten Testzyklen wird der Prüfling einer hochfrequentenSchwingung ausgesetzt. Weitere Tests umfassen Schocktests, welche eine mechanische Belastung in Form eines Stoßes simulieren (DIN EN 61373:2011-04).  
Schutz elektrischer Betriebsmittel: Die Gehäuse elektrischer Betriebsmittel erfüllen verschiedene Schutzarten. Die Schutzarten zielen zum einen auf den Schutz von Personen gegen Berühren unter Spannung stehender Teile innerhalb der Gehäuse ab (Berührungsschutz). Darüber hinaus dienen die Gehäuse dem Schutz des Betriebsmittels gegen Eindringen von Fremdkörpern, einschließlich Staub (Fremdkörperschutz). Außen dem schützen die Gehäuse das Betriebsmittel gegen schädliche Einwirkungen durch das Eindringen von Wasser (Wasserschutz). Die Schutzart durch ein Gehäuse wird anhand genormter Prüfverfahren nachgewiesen. Zur Klassifizierung dieser Schutzart wird der so genannte IP-Code verwendet (DIN EN 60529:2014-09).

# 8.5.2 Fabriktests

Um Testaktivitäten im Feld weltgehend zu minimieren werden umfassende Tests in den Testcentern der Hersteller durchgeführt (Wigger 2016). Hierbei wird das CBTC-System in Simulationsumgebungen eingebettet. Auf diese Weise wird das CBTC-System bevor die Software im Feld getestet wird unter kontrollierten Bedingungen „auf Herz und Nieren“ getestet. Hierdurch wird schon früherzeitig eine welt reichende Anforderungsermittlung nachgewiesen und mögliche Fehler in der Software erkannt. Oftmals nimmt auch der

Betreiber an den Testaktivitäten teil (Factory Acceptance Test, FAT). Die folgenden Teststellungen können in den Testcentern der Hersteller effektiv bearerbeitet werden:

- Tests interner Schnittstellen des CBTC-Systems: Alle Nachrichten zwischen Leittechnik und dem Fahrzeuggerät, der Leittechnik und dem Streckengerät sowie zwischen dem Strecken- und dem Fahrzeuggerät werden getestet. Hierbei können Tests entweder auf realer oder emulierter Hardware durchgeführt werden.  
- CBTC-Funktionstests: Abgeleitet von den funktionalen Anforderungen im Projekt werden alle Funktionen mindestens an einer Stelle im Netz exemplarisch getestet.  
- Größmögliche Testabdeckung externer Schnittstellen: Hier muss insbesondere die Schnittstelle zwischen dem Streckengerät und dem konventionellen Zugsicherungssystem (Stellwerke) vollständig getestet werden. Gleichfalls sind aufwändige Tests der Schnittstelle zur Leittechnik erforderlich. Hierfür müssen Schnittstellensimulationen von den Herstellern selbst aufgebaut werden oder von den Herstellern externer Umsysteme bereitgestellt werden.  
- Fehlereinstreuungstests: Im Testcenter können Fehlereinstreuungstests durchgeführt werden, die im Feld so nicht getestet werden konnen. Ein Beispiel hierfür ist die Vertauschung oder Verfällschung von Botschaften auf dem Funkkanal zum Nachweis der Wirksamkeit der getroffenen Sicherheitsmechanismen des Kommunikationsprotokolls.  
- Unterstützung von Feldtests durch Nachstellen von Fehlern: Das Ziel der Tester im Feld ist es, einen erfolglichen Nachweis der korrekten Funktion zu führen und nicht, Fehler aufzuspären. Sobald die Tester im Feld einen Fehler erkennen, wird er den Testern im Testcenter gemeldet. Im Testcenter wird der Fehler mit der Hilfe von Entwicklern und Projektierern nachgestellt und analysiert. Die gewonnenen Erkennnisse fließen in einen Korrekturstand der Software zur Inbetriebnahme ein. Kann der Fehler bis zur Inbetriebnahme nicht behoben werden, kann das CBTC-System gegebenenfalls vorübergehend mit betrieblichen Einschränkungen in Betrieb genommen werden.

# 8.5.3 Fahrzeugtests

Ein wesentlicher Anteil an Projektaktivitäten erfolgt im Zusammenhang mit der Integration der CBTC-Fahrzeugeinrichtungen in die Fahrzeuge des Betreibers. Hierbei werden im Verlaufe eines Projekts verschiedene Tests mit den Fahrzeugen durchgeführt. Dies erfordert in der Regel eine enge Abstimmung zwischen dem Hersteller der CBTC-Systeme und dem Fahrzeughersteller.

- Ermittlung der Fahrzeugeigenschaften: Diese Testaktivität dient nicht dem Nachweis. Es mussen im Projekt viel mehr früherzeitig die (fahrodynamischen) Eigenschaften der Fahrzeuge erfasst und mit dem Fahrzeughersteller und Betreiber abgestimmt werden. Eine wesentliche Information sind Aussagen über die garantierte Zwangsbremsverzögerung, aber wegen der ATO-Funktion (Automatic Train Operation) auch die mog

liche Beschleunigung der Züge auf ebener Strecke. Die Angaben fließen in die projektspezifische Konfiguration der Software der ATP- und ATO-Fahrzeuggeräte ein.

- Mechanische und elektrische Tests: Die ersten beiden Fahrzeuge eines Typs werden in der Regel als Prototypen umgesetzt. Hierbei wird die mechanische Integration der eingebauten CBTC-Komponenten weitere beachtet und es werden letzte offene Punkte geklärrt. Die elektrischen Verbindungen werden genauso getestet wie die Kommunikation mit anderen elektronischen Systemen an Bord des Fahrzeugs. Die Tests an den Prototypenfahrzeugen erstreckten sich in der Regel über mehrere Wochen.  
- Statische und dynamische Inbetriebnahmetests der Fahrzeuginrichtung: Für jedem instalierte Fahrzeug wird die korrekte Montage der Fahrzeugeinrichtung geprüft. Für den Nachweis der korreksen Funktion der Sensoren für die Weg- und Geschwindigkeitsmessung ist eine kurze Fahrzeugbewegung erforderlich. Für die ATO müssen auch die Fahrzeugeigenschaften (Fahrodynamik) noch einmal betrachtet werden. Da die Ermittlung der Fahrzeugeigenschaften nur an ausgewählten Fahrzeugen durchgeführt wurde, können die tatsächlichen Fahrzeugeigenschaften in der Flotte abweichen. In thisem Fall kann es erforderlich werden, dass die projektspezifische Konfiguration der Fahrzeugsoftware an die Erkenntnisse der Fahrzeugtests angepasst werden muss. Um den Nachweis der korreksen Funktion der CBTC-Schutzfunktion für jeder Fahrzeugtyp zu erbringen, muss die CBTC-Streckeneinrichtung (Streckengerät und Funkausleuchtung) für mindestens einen Streckenbereich (zum Beispiel ein Testgleis im Betriebshof des Betreibers) vorhanden sein.

# 8.5.4 Testgleis im Betriebshof

In Projektiven werden üblicherweise Testgleise mit CBTC-Streckeneinrichtungen ausgerüstet. Diese Testgleise befinden sich üblicherweise auf Betriebshöfen oder in ihrer unmittelbaren Nachbarschaft. Hierbei sollen nach Möglichkeit alle betrieblich relevanten Streckenkconfigurationen und Anlagenelemente (beispelsweise verwendete Signatypen) vorgesehen werden. Die Topologie des Testgleises sollte so gewählt werden, dass eine Aufnahme und Entlassung in einen automatischen Betrieb sowie ein Halt an einer oder mehreren virtuellen Halteststellen abgebildet werden kann.

Die Einrichtung eines Testgleises ist aus mehrlei Gründen sinnvoll:

- Test der Fahrzeugeinrichtung: Nachweis der korrekten Funktion der Schnittstellen zwischen Fahrzeugeinrichtung und Fahrzeugleittechnik für die ersten Prototypenfahrzeuge.  
- Systemtests: Nachweis der betrieberspezifischen CBTC-Funktionen  
- Statische und dynamische Inbetriebnahmetests für Serienfahrzeuge: Für jedem installierte Fahrzeug werden nach erfolgter Installation ausgewählte Testfälle durchgeführt. Diese umfassen beispisse weise den Aufbau einer Funkverbindung, die Lokalisierung

nach Überfahr tner Ortsbake, den Empfang eines Fahrbefehls, eine anschlieBende kurze Fahrt und einen Abbau der Funkverbindung.

Schulung: Die Fahrzeugführer müssen früherzeitig in den Betrieb mit dem neuen Zug-sicherungssystem eingewiesen werden. Zu diesersem Zweck muss das Testgleis eine ausreichende Länge aufweisen.  
- Regressiontests: In der Ausrüstungsphase entstehende Korrekturände der Software werden vorab im Testgleis getestet. Dies gilt auch für Korrekturen und Änderungen nach Aufnahme des Fahrgastbetriebs.

# 8.5.5 Inbetriebnahmetestsder Streckeneinrichtung

Die Tests an der Streckeneinrichtung erfolgen in mehreren aufeinander aufbauenden Schritten:

# Übereinstimmungsprüfung

Bevor die Durchführung vonfunctionalen Testfällen beginnen kann, muss die korrekte Ausführung der Installation getestet werden. Hierbei wird kein den korrekten Ausführung der Kabelarbeiten und der Erdung insbesondere die korrekte Zuordnung der reilen Außenanlageenelemente zu ihren logischen Entsprechungen in der Software der CBTC-Streckeneinrichtung und der Leittechnik geprüft. Der Abschluss dieser Teststufe markiert den Übergang von der Installationsphase in die Testphase.

# Tests des DatenCOMMunikationsssystems (insbesondere Funk)

Neben anderen CBTC-Subsystemen ist das Datenkommunikationssystem das erst zu stallierende und zu testende System. Es werden Glasfaserkabel zwischen den Technikräumen entlang der Strecke verlegt und getestet. Ebenso werden Netzwerk-Switche installiert und getestet. Ein Netzwerkmanagement-System zur Verwaltung des Netzwerks muss vor Testdurchführungvorhanden sein. Hierüber konnen Nachweise zu korrekten Konfigurationen der Netzwerkswitche, der Datentransferraten sowie Latenzzeiten im Netzwerk erfasst werden. Aufbauend auf dieser Betrachtung des Netzwerks entlang der Strecke kann die eine ausreichende Funkabdeckung entlang der Strecke nachgewiesen werden. Der Nachweis der Funkabdeckung erfordert mindestens ein mit spezieller Messausrücktung ausgerüstetes Fahrzeug. Alternativ kann auch eine Messeinrichtung auf Fahrzeugen installiert werden, die im regulären Fahrgastbetrieb „mitschwinnen“. Prüfwerkzeuge messen zum einen die Stärke des elektromagnetischen Feldes der Funkverbindung auf dem Fahrzeug. Gleichzeitig konnen auch kontinuierlich Datenpakete über den Funkkanal gesendet werden, um die Paketverlustrate zu überwachen. Sollte das Fahrzeug über zwei redundante Fahrzeuggeräte an jedem Zugende verfügen, werden diese Tests gleichzeitig für beiden Fahrzeuggeräte durchgeführt. Die Züge fahren für die Durchführung der Funkabdeckungstests zunachst mit langsamer Geschwindigkeit. Hierbei kann auch gezeigt werden, dass das Hand-over der Funkverbindung zwischen benachbarten Access Points bruchlos funktioniert. Es ist ebenfalls sinnvoll, worst-case-Bedingungen zu testen. Dies ist beispielsweise dann der Fall, wenn Access Points welt voneinander halten sind oder die

Signalausbreitung zwischen Access Points und Fahrzeug durch ein oder zwei zwischenstehende Fahrzeuge abgesch Chattet ist. Anschließlich erfolgen Tests mit maximal zulässiger Streckengeschwindigkeit in allen Streckenbereichen. Der Test der Funkstrecke ist essenziell für das Fortschreiben den Testaktivitäten. Bestehen Lücken in der Funkabdeckung, können die funkionalen Testfälle (beispielsweise zur Lokalisierung des Zuges) nicht durchgeführt werden.

# Nachweis der Ortungsfunktion

These Tests weisen nach, dass der Zug in der Lage ist, seine Position hinreichend genau zu bestimmen und seine aktuelle Position im Streckennetz auf dem Fahrzeug zur Verfügung zu haben. Die Tests zum Nachweis der Ortungsfungkction setzen voraus, dass die Information über die Weichenlagen in der CBTC-Streckeneinrichtung vorhanden sind und dass eine Funkverbindung zwischen der CBTC-Streckeneinrichtung und der CBTC-Fahrzeugeinrichtung besteht. Neben den Testaktivitäten zum Datenkommunikationssystem ist der Nachweis der Ortungsfungkction die zweite Testaktivität im Feld. Diese beiden Nachweise sind die Grundlage für einen CBTC-Betrieb. Obwohl diese elementaren Funktionen nur einen kleinen Teil des Funktionsumfangs der CBTC-Systeme ausmachen, sind für diese Nachweise weitere Sperrpausen erforderlich, da diese Tests auf allen Gleisen in beiden Fahrchtroughten durchgeführt werden müssen.

# Integrationtests

Die Integration umfasst sowohl das Zusammenwirken der einzelnen Teilsysteme der CBTC-Systemlösung eines Herstellers als auch das Zusammenwirken mit den externen Schnittstellen des CBTC-Systems in der Systemlandschaft des Betreibers. Als Beispiel sind hier Schnittstellen zur Fahrgastinformation, Gebäudefomatisierung, Traktionsstromversorgung aber möglicherweise auch anderer signaltechnischer Systeme genannot (beispielsweise Stellwerke) für den Fall, dass die CBTC-Systemlösung als Overlay zu einer bestehenden Fahrwegssicherung eingesetzt werden soll (Brückner 2017).

# Funktiontests

Nachdem die Tests für das Datenkommunikationssystem, die Ortungsfunktion und die Systemintegration erfolgreich verlaufen sind, können funktionale Tests durchgeführt werden. In der Regel werden hierfür Testumfänge aus den Fabriktests wiederholt. Die Herausforderung im Testmanagement liegt hierbei darin, eine sinnvolle Auswahl der zu testenden Funktionen einsersects zu treffen und anderersects die erforderliche räumliche Testabdeckung zu definieren. Stehen zunachst die Sicherheitsrelevanten Funktionen im Vordergrund, werden hierauf aufbauend die automatisierungstechnischen Anteile getestet:

- Funktionstest Automatic Train Protection: Hierzu werden Nachweise konkreter Schutzfunktionen wie die Verhinderung der Überfahr t eines Gefahrpunktes getestet. Ebenso kann das Setzen und das Rücknehmen einer vorübergehenden Langsamfahrstelle für jeder Stellbereich einer CBTC-Streckeneinrichtung exemplarisch getestet werden.

- Funktionstest Automatic Train Operation: Für den Nachweis einer korrekten automatischen Steuerung der Züge gemäß der gültigen Geschwindigkeitsvorgaben werden spezifische Tests durchgeführt. Hierbei werden verschiedene Fahrzeuggeschwindigkeiten und Geschwindigkeitswechsel im statischen Geschwindigkeitsprofil getestet, um zu zeigen, dass der Zug die gewünschten Geschwindigkeitsvorgaben effektiv umsetzt. Gleiches gilt für die Haltegenauigkeit im Stationsbereich. Diese Tests erfolgen für alle Gleise in beiden Fahrtrichtungen.  
- Funktionstest Automatic Train Supervision: Auch wenn der Großteil leittechnischer Funktionen bereits im Testcenter der Hersteller getestet werden kann, werden einzelste komplexe leittechnische Funktionen erst wirsam im Feld getestet. Eine erstene Funktion, die getestet werden kann ist die Zuglaufverfolgung. Hierauf aufbauend konnen die Wechselwirkungen zwischen der Zuglaufverfolgung und dem Fahrplanmanagementssystem (beispielsweise hinsichtlich der Zuordnung von Fahrplanfahrten zu Zügen) sowie Funktionen der Konflikterkennung und Konfliktlösung getestet werden.

# Site Acceptance Tests (SAT)

Der Betreiber kann es sich vorbehalten, alle Testaktivitäten im Projekt zu begleiten und die vorgelegten Testnachweise zu bestätigten (Wigger 2016). In der Regel werden für den SAT aus der Systemanforderungsspezifikation abgeleitete Testfälle durchgeführt. Um den Ziel-termin für die Inbetriebnahme des CBTC-Systems sicherzustellen, kann die Betriebsaufnahme zunachst gegebenenfalls nur mit einem reduzierten Funktionsumfang erfolgen. Komplexere (leittechnische) Funktionen können dann in Abstimmung mit dem Betreiber zu einem späteren Zeitpunkt ergänzt werden.

# Betriebserprobung (Schattenbetrieb)

Der Schattenbetrieb ist ein Testkonzept für Erneuerungsprojekte. Hierbei liegt die Sicherheitsverantwortung im bestehenden Zugsicherungssystem. Das neue Zugsicherungssystem lauft parallel mit und empfängt alle relevanten Führungsgrößen, greift bei erkannten Abweichungen aber nicht aktiv in den Prozess ein. Diese Phase kann sich möglicherweise über mehrere Monate erstrecken. In einem nachsten Schritt können zwischen den regulären Zugfahrten einzelne Zugfahrten ohne Fahrgäste unter CBTC-Überwachung durchgeführt werden. Verlaufen auch diese erfolgreich, kann eine Freigabe für den Betrieb mit Fahrgästen erfolgen (Dombrowsky et al. 2008).

# Zuverlässigkeitserprobung

These Testaktivitäten haben zum Ziel, den Nachweis zu erbringen, dass das CBTC-System die vertraglich fixierten Performance-Kennwerte (RAMSS) erfüllt. Hierfür werden bereits zum Zeitpunkt der Vertragsunterzeichnung zwischen Hersteller und Betreiber die konkreten Modalitäten der Nachweisführung festgelegt. Die Festlegungen umfassen die relevanten Kenngroßen (zum Beispiel die Mean Time Between Failure, MTBF), die zu beitrachtende Grundgesamtheit (beispisseweise eine Linie), den Zeitraum der Tests sowie statistische Randbedingungen des Nachweisverfahrens (beispisseweise Chi-Quadrat-Tests mit einem bestimmten Konfidenzintervall). Die Nichteinhaltung der Zuverlässigkeitskennwerte ist gegebenenfalls mit einer Vertragsstraße belegt.

# 8.6 Anpassung betrieblicher Regelwerke für den automatisierten Betrieb

In den Verkehrsrunternehmen legen Dienstanweisungen legen fest, wie die rechtlichen Vorgaben im jeweiligen Verkehrsrunternehmen umzusetzen sind (Schröter 2008). Nachfolgend werden zunachst die grundlegenden Prinzipien beschreiben, die der Erstellung des betrieblichen Regelwerks für eine exemplarische fahrerlose Linie zu Grunde liegen (Abschn. 8.5.1). Es schließt sich eine Darstellung der gewährten Vorgehensweise mit den Meilensteinen und Aufgaben an, die sich in die Logik eines Sicherungstechnischen Ausrüstungsprojekts eingfegt (Abschn. 8.5.2). Abschlussend erfolgt eine Darstellung der Rollen und Verantwortlichkeiten in Bezug auf die Erstellung der betrieblichen Regelungen (Abschn. 8.5.3).

# 8.6.1 Prinzipien der Regelwerksanpassungen in Erneuerungsprojekten

Die Erstellung der betrieblichen Regelwerke für eine fahrerlose U-Bahn-Linie zum Beispiel orientiert sich an mehreren grundlegenden Prinzipien (Schnieder 2024).

# Prinzip 1: Führzeitiger Beginn der projetbegleitenden Ausarbeitung des betrieblichen Regelwerks

Dieses Prinzip ist wichtig, da die systemtechnische Ausprüfung einer fahrerlosen U-Bahn-Linie und die betrieblichen Regeln wechselseitig aufeinander bezogen sind. Die gegenseitigen Bezüge stellen sich wie folgt dar:

- Auswirkungen des (bestehenden) betrieblichen Regelwerks auf den (zu währenden) technischen Entwurf: Die bestehenden oder gewünschten betrieblichen Regelungen sind Ausdruck der Anforderungen des jeweiligen Verkehrsunternehmens. Diese Anforderungen wirken sich auf Details der vom Hersteller gewählten technischen Lösung aus. Gerade in der Phase der Pflichtenhefterstellung ist es dazu wesentlich, dass Hersteller und Betreiber hier eng und partnerschaftlich zusammenarbeiten (Abb. 8.2).  
- Auswirkungen des (zu währenden) technischen Entwurfs auf das (bestehende) betriebliche Regelwerk: Die vom Hersteller gewählten technischen Lösungen beeinflussen die betrieblichen Regelungen des Verkehrsunternehmens für die Betriebsabwicklung auf

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/75c5087a762c99362d28001ce6dbaa5963366f08bd0f0550a7c702a4c1019a78.jpg)  
Abb. 8.2 Wechselseitige Beziehung zwischen betrieblichem Regelwerk und Entwurfsent-scheidungen

der fahrerlosen Linie – insbesondere auch deshalb, weil die Durchführung eines unbegleiteten fahrerlosen Betriebs für den jeweiligen Betreiber oftmals neu ist. In der Phase der Pflichtenhfterstellung ist die Grobarchitektur bereits zum Großteil festgelegt und gilt davon als Randbedingung für alle weiteren Entwurfsschritte im Projekt (Abb. 8.2). Im weiteren Verlauf des Projekts resultieren zu berücksichtigende Anwendungsbedingungen aus dem Validierungsbericht (DIN EN 50128:2012-03) sowie aus den im technischen Sicherheitsbericht des Sicherheitsnachweises definierten Sicherheitsbezogenen Anwendungsbedingungen (DIN EN 50129:2019-06), die einer unabhängigen Sicherheitsbewertung (DIN EN 50126-1:2018-10) unterworfen werden.

# Prinzip 2: Einbindung aller beteiligten Interessengruppen in den Erstellungsprozess des betrieblichen Regelwerks

Hierbei werden die verschieden Interessengruppen früherzeitig identifiziert und ihre Rolle und Mitwirkung bei der Erstellung des betrieblichen Regelwerks festgelegt. Außen dem wird festgelegt, welche Zielgruppen im betrieblichen Regelwerk angesprochen werden müssen (z. B. Instandhaltungspersonal, Fahrdienstleiter und Fahrpersonal). Die Planung und der Betrieb einer fahrerlosen U-Bahn-Linie erfordern das reibungslose und aufeinander abgestimmte Zusammenwirken verschiedener interner Funktionen des Verkehrsunternehmens. Daher wird für die Erstellung des betrieblichen Regelwerks eine interne Arbeitsgruppe unter Leitung eines Koordinators des Verkehrsunternehmens einberufen, die sich unter anderen aus Fahrpersonal, Fahrdienstleiter sowie Instandhaltungspersonal für Fahrzeuge und Streckeneinrichtungen zusammensetzt. Diese interdisciplinäre Zusammenstellung der Arbeitsgruppe stellt safer, dass das betriebliche Regelwerk im Konsens verschiedener Unternehmensbereiche erstellt wird und damit im Projektverlauf auf eine höhere Akzeptanz besteht. Planung und Vorbereitung des Betriebs einer fahrerlosen U-Bahn-Linie erfordern darüber hinaus das aufeinander abgestimmte Zusammenwirken verschiedener Funktionen des Herstellers der Sicherungstechnischen Einrichtungen (z. B. Teilsystemverantwortliche) sowie des Fahrzeugherstellers. Zudem müssen externe Interessengruppen mit in den Prozess eingebunden werden. Dies ist beispisse die Technische Aufsichtsbehörde sowie Vertreter von Behörden und Organisationen mit Sicherheitsaufgaben (BOS) wie Polizei und Feuerwehr. Abb. 8.3 stellt den kollaborativen Ansatz der Ausarbeitung des betrieblichen Regelwerks dar (Schnieder 2024).

# Prinzip 3: Anleitung an bewährte Regelungen (evolutionärer Ansatz)

Die Verkehrsrunternehmen betreiben in der Regel seit mehreren Jahrzehnten umfassende Verkehrssysteme. Dadurch verfügen sie zumindest für den Automatisierungsgrad 1 (NTO, non-automated train operation) über ein umfassendes und in der Praxis bewährtes Regelwerk. Gegebenenfalls wird these Regelwerk um einen halb automatischen Betrieb im Automatisierungsgrad 2 (STO, semi-automated train operation) ergänzt und fortgeschrieben und muss letztlich auf den Automatisierungsgrad 4 (UTO, unattended train operation) angepasst werden (Abb. 8.3). Dieser evolutionäre Ansatz birgt zwei Vorteile:

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/081429537414bc8d0d0eed52fa1a86f976c40af9edb45ad166f5315fb2e9917b.jpg)  
Abb. 8.3 Partnerschaftliche Zusammenarbeit verschiedener Beteiligter in der Fortentwicklung des bestehenden betrieblichen Regelwerks

- Das Verkehrsunternehmen verfügt bereits über eine lange Erfahrung im Betrieb eines U-Bahn-Systems. Es ist davon auszugehen, dass hier alle Details des Regelbetriebs vollumfänglich beschrieben sind (Vollständigkeit des zu erstellenenden Regelwerks). Gleiches gilt für eine angemessene Beschreibung des Betriebs auf der Rückfallebene nach relevanten Störfläten (,,so viel wie nötig, so weniger wie möglich").  
Die Weiterentwicklung des Regelwerks stellt die Akzeptanz innerhalb des Verkehrsunternehmens sicher. Außen dem können sich im Rahmen der Schulung die Teilnehmer, die ggf. schon vorher in anderen Unternehmensbereichen des Verkehrsunternehmens aktiv waren, Schneller mit den neuen/ergänzten/geänderten Regeln vertraut machen, da diese im Grundszatz bereits bestimmten Regelungen nicht widerprechen.

# 8.6.2 Ablauf der Regelwerkserstellung im Erneuerungsprojekt

Die Erstellung des betrieblichen Regelwerks für die fahrerlose U-Bahn-Linie erfolgt in mehreren aufeinander aufbauenden Phasen. jeder Phase schließt mit einem definierten Qualitätsprüpfpunkt ab.

- Phase 1: Die Auswirkungen der neuen Systemanforderungen auf die bestehenden betrieblichen Regeln und Vorschriften werden bewertet. Das Ergebnis dieser Phase ist eine erste Version der neuen Betriebsvorschriften und -verfahren zusammen mit einer Liste offener Punkte, die von einer gemeinsamen Arbeitsgruppe des Betreibers und des Herstellers des Sicherungssystems gehandelt werden müssen.  
- Phase 2: In der zweiten Phase implementiert der Hersteller die neue Systemlösung und führt Testaktivitäten im Labor durch. In der Regel kommt der Kunde in die Räumlichkeiten des Herstellers, um sich ein Bild von den erzielten Fortschritten zu machen. Dies wird als Factory Acceptance Test (FAT) bezeichnet. Während des FAT lauf das System in einer simulierten Umgebung, in der eine erste Version der Betriebsleitstelle in Betrieb ist. Dieder Aufbau kann zur Validierung der ersten Version der Betriebsvorschriften und -verfahren verwendet werden. Das Ergebnis ist eine zweite Version der neuen Betriebsvorschriften und -verfahren zusammen mit eineractualisierten Listederoffenen Punkte.

- Phase 3: Bei typischen sicherungstechnischen Projekten wird der Betreiber hochstwahrscheinlich Schulungseinrichtungen für das Personal der Betriebsleitzentrale (Schult et al. 2015) und für die Fahrer (Dydak 2019) bestehen. Beide Einrichtungen werden zu einem bestimmten Zeitpunkt betriebsbereit sein. Während der Schulungen werden die Fahrer und das Personal der Betriebsleitzentrale mit dem neuen System sowie mit den neuen Betriebsregeln und -verfahren vertraut gemacht. Dies ist eine gute Gelegenheit, die neuen Betriebsvorschriften weiter zu validieren. Das Ergebnis ist eine dritte Version der Betriebsvorschriften und -verfahren zusammen mit eineractualisierten Listeder offenen Punkte.  
- Phase 4: Für die Durchführung von Integrationstests wird eine Teststrecke eingerichtet. Das Personal des Betreibers wird auf der Teststrecke zum ersten Mal mit dem neuen Sicherungssystem interagieren. Dies ist der ersten Schritt von einer simulierten Umgebung zu realen „physischen“ Anlagen. Dies ist besonderss wichtig für Betriebsvorschriften und -verfahren zu Wartungsaspekten. Aus thisem Grund bieten die Tests auf der Teststrecke weitere Möglichkeiten für die Validierung des neuen Regelwerks. Ergebnisse sind eine vierte Version der Betriebsvorschriften und -verfahren sowie eineactualisierte List der offenen Punkte.  
- Phase 5: Das neue Signalsystem wird umfassenden Testaktivitäten in der realen Betriebsumgebung unterzogen. Das Personal des Betreibers, sowohl an Bord der Züge als auch in der Betriebsleitzentrale, wird diese Aktivitäten gemeinsam durchführten. Eventuell fehlende Regelungen, Fehler oder missverständliche Formulierungen können so erkannt und behoben werden. Dies ist die letzte Chance, das Regelwerk zu validieren, bevor das System in den Echtbetrieb Goes. Das Ergebnis dieser Phase ist der fünfte (und letzte) Satz von Betriebsvorschriften und -verfahren. Offene Fragen werden an die Betriebsphase weitergeleitet und müssen im Rahmen der regelmäßigen Aktualisierungen des Regelwerks durch den Betreiber geheldt werden.

Für die Arbeiten in jeder der oben genannten Phasen müssen die Aufgaben clar zugewiesen werden. Dies kann durch Matrizen erreicht werden, aus denen hervorgelt, wer verantwortlich ist, wer rechtschaftspflichtig ist, wer Unterstützung tätig ist und wer informiert werden muss (RACI-Matrix). Wenn dies zu einem frühen Zeitpunkt in einem Projekt vereinbart wird, verläuft die Aktualisierung der Betriebsvorschriften und -verfahrensreibungslos und der Erfolg des Projekts ist sichergestellt.

# 8.6.3 Rollen und Verantwortlichkeiten der Regelwerkserstellung im Erneuerungsprojekt

An der Erstellung der betrieblichen Regel im Projekt der Ertüchtigung einer Linie für den unbegleiteten fahrerlosen Betrieb wirken verschiedene Rollen mit. Die Mitwirkenden repräsentieren bzw. jeweils die verschiedenen Interessengruppen:

An der Ausarbeitung des Regelwerks zu beteiligende interne Stakeholder des Verkehrsunternehmens und ihre Aufgaben:

- Koordinator des Verkehrsunternehmens: Koordiniert die Betrieberaktivitäten in Bezug auf die Anpassung des betrieblichen Regelwerks, stimmt die Umsetzung der zu regeln-den Sachverhalte mit den Fachbereichen des Betreibers ab, koordiniert die Freigabe des Regelwerks durch den Betriebsleiter des Verkehrsunternehmens, stimmt sich mit den verschiedenen internen Fachbereichen des Verkehrsunternehmens ab, kommuniziert die Abstimmungsergebnisse termingerecht an den Koordinator des Herstellers.  
- Fachbereiche des Verkehrsrunternehmens: An der Einführung des fahrerlosen Betriebs sind vielse Unterschiedliche Funktionen im Unternehmen beteiligt (Sicherungstechnik, Fahrzeug, Betrieb, Infrastruktur, etc.). Die Bedürfnisse der Fachbereiche werden im Rahmen der Koordination aufgegriffen und flieben in die Weiterentwicklung des Regelwerks ein.  
- Betriebsleiter: Das Verkehrsinunternehmen hat einen Betriebsleiter zu bestellen. Diese Person ist bei allen Entscheidungen, die die Betriebsführung beeinflussen, einzubeziehen; dies umfasst insbesondere das betriebliche Regelwerk. Außen dem gibt sie das betriebliche Regelwerk in letzter Instanz frei (Straβenbahn-Bau- und Betriebsordnung vom 11. Dezember 1987).

An der Ausarbeitung des Regelwerks zu beteiligende interne Stakeholder des Herstellers und ihre Aufgaben:

- Koordinator des Herstellers: Koordiniert in dieser Rolle die Herstelleraktivitäten in Bezug auf die Anpassung des betrieblichen Regelwerks, formuliert die zu regelnden Sachverhalte und leitet diese zur Umsetzung im Regelwerk an den Koordinator des Verkehrsrunternehmens weiter.  
- Fachbereiche der Hersteller: Überführten die Pflichtenheftanforderungen in ein Produktkonzept und weisen das korrekte funktionale Verhalten und das Verhalten des Systems im Fehlerfall nach. Heraus resultieren sicherheitsbezogene Anwendungsregeln, die ggf. im betrieblichen Regelwerk berücksichtigt werden müssen.

An der Ausarbeitung des Regelwerks zu beseiligende Externe und ihre Aufgaben:

- Behörden und Organisationen mit Sicherheitsverantwortung (BOS): Die Organisationsennehmen öffentliche Aufgaben zur Gefahrenabwehr oder Schadensbekämpfung wahr. Hierbei handelt es sich beispisseweise um die Polizei und die Feuerwehr.  
- Gutachter: Die Technische Aufsichtsbehörde kann sich in der Wahrnehmung ihrer Sicherheitsaufsicht unabhängiger Sachverständiger bedieren. Diese werden regelmäß über den Fortschritt der Erarbeitung des betrieblichen Regelwerks informiert. Etwaige Auflagen aus den Gutachten fließen bei Bedarf in die Weiterentwicklung des betrieblichen Regelwerks ein.

- Technische Aufsichtsbehörde (TAB): Aufsichtsbehörde des betreffenden Bundeslandes, die den sicheren und ordnungsgemäßen Betrieb des Verkehrsunternehmens überwacht. Etwaige Anforderungen der TAB müssen im betrieblichen Regelwerk berücksichtigt werden.

Die Verantwortlichkeiten sind exemplarisch einer RACI-Matrix darstellbar. Hierfür stehen die einzelnen Buchstaben für den jeweiligen Grad der Einbindung der beseitigten Personen (R - Responsible; A - Accountable; C - Consulted; I - Informed).

# 8.7 Schulung des Betriebspersonals

Bereits früherzeitig vor Aufnahme des Fahrgastbetriebs mit der neuen Technologie müssen verschiedene Zielgruppen im Unternehmen im Umgang mit CBTC-Systemen geschult werden. In thisem Abschnitt werden die Qualifikationsbedarfe aus Sicht von vier verschiedenen Zielgruppen dargestellt. Im konkreten Ausrüstungsprojekt müssen die Betreiber früherzeitig dafür Sorge tragen, dass die Schulung vom strukturiert Hersteller in die Höhe des Betreibers übergeben wird. Hierfür haben sich in internationalen Projekten Train-the-Trainer-Konzepte vielfach bewährt.

# 8.7.1 Schulungenden Fahrer

Die Fahrer müssen das CBTC System umfassend kenenlernen. Sie müssen die verschiedenen Betriebsarten, die Anzeigen des Führerstandsdisplays sowie auf diesen dargestellte Alarme und Informationen verstehen, korrekt interpretieren und im Betrieb in geeignete Reaktionen umsetzen. Hierbei須sen in der Schulung die folgenden Inhalte abgedeckt werden:

- Einweisung in die Führerstandsanzeige mit ihren Anzeigen und Bedienelementen  
- Darstellung der Komponenten der CBTC-Fahrzeugeinrichtung  
- Darstellungen der Bedienhandlungen in den verschiedenen betrieblichen Situationen (Aufrüsten des Fahrzeugs, Durchführung einer Permissivfahrt, manuelle Steuerung des Zuges entlang eines kontinuierlichen Überwachungsprofils, Führren des Zuges im halb automatischen Betrieb, Durchführung einer Kehrfahrt, Bergung liegengebliebener Fahrzeuge)  
- Üben des Fahrens unter Nutzung der gesamten Bandbreite der zulässigen Betriebsartenwechsel

Die Schulungen werden durch geeignete Schulungseinrichtungen unterstützt. Da zum Zeitpunkt der Schulungsdurchführung die Anlagen noch nicht in vollem Umfang in Be

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/5ed14756f51a17bffe17ca8cf623f27a36e5bdc05d4fbee7efcb425cc73d3c32.jpg)  
Abb. 8.4 Fahrsimulator für Fahrerschulungen. (Quelle: Stadtwerke Verkehrsgesellschaft Frankfurt am Main mbH, VGF)

trieb sind,kommen hierfür in der Regel Simulatoren fur die Fahrzeugeinrichtungen (Dydak 2019) zum Einsatz. Ein beispielhafter Fahrsimulator ist in Abb. 8.4 dargestellt.

# 8.7.2 Schulungen der Fahrdienstleiter

Das Personal auf der Leitstelle muss über ein welt reichendes betriebliches Wissen über das CBTC-System verfügen. Dies umfasst zum einen Betriebsführung im Regelbetrieb als auch die Betriebsführung auf der Rückfallebene. Hierzu müssen die Fahrdienstleiter ein umfassendes Verständnis der verschiedenen Betriebsarten haben. Sie müssen alle Bedienhandlungen, sowie Alarme und Informationen der Leittechnik verstehen und diese in angemessene betriebliche Entscheidungen umsetzen. Hierbei müssen in der Schulung die folgenden Inhalte abgedeckt werden:

- Funktionen der Fahrwegsicherung (gegebenenfalls Stellwerksfunktionen) sowie Sicherheitsrelevante Bedienhandlungen über die Leittechnik. Diese Inhalte werden durch gezielte praktische Übungen vertief.  
- Einführung in die Diagnose und Wartungseinrichtungen damit Interpretation anstehender Störmeldungen.

- Funktionen und Einrichtungen der automatischen Zugüberwachung (ATS). Inbesondere Einführungen in Funktionen und Bedienhandlungen für die Zuglaufverfolgung (Automatic Train Tracking, ATT) und Zuglenkung (Automatic Route Setting, ARS) sowie möglicherweise weiterer Dispositionsfunktionen.  
- Vertiefung der Lerninhalte durch gezielte praktische Übungen.

Die Schulungen werden durch geeignete Schulungseinrichtungen untersätzt. Da zum Zeitpunkt der Schulungsdurchführung die Anlagen noch nicht in vollem Umfang in Betrieb sind,kommen hierfür in der Regel Simulatoren fur die die Leitstellenbedienung (Schult et al. 2015) zum Einsatz. These Simulatoren bilden alle relevanten Details der Originalsysteme nach,um Trainingsbedürfnisse zu erfüllen.Die Bedienoberflächen werden mit der gleichen Bedienoberfläche das Originalsystem nachgebildet.Gleiches gilt fur das zugrunde liegende Verhalten der Sicherungssysteme. Es kann hier eine realistische Topografie oder eine virtuelle Strecke nachgebildet werden.Der Zugbetrieb erfolgt auf der Grundlage eines Fahrplans, die Züge verkehren mit einer realistischen Fahrdynamik auf Basis von Zugkräften der Triebfahrzeuge, Zugmassen und -längen sowie Strecken- und Fahrstraßegeschwindigkeiten. Ein Schulungssimulator besteht meist aus einem Lehrer-Arbeitsplatz und mehreren Schuler-Arbeitsplätzen.Dem Trainer stehen eine große Auswahl von Fehlfunktionen und Störungen zur Verfugung. Dies konnen Elementstörungen (Weichen, Signale etc.), Systemstörungen (Störungen von Streckeneinrichtungen oder des Datenkommunikationssystems etc.) oder auch betriebliche Störungen (Zug fahrt über einen Gefahrpunkt hinaus, reduzierte Geschwindigkeit etc.) sein. Alle Störungen konnen in Störungsszenarien fur standardisierte Tests zusammengefasst werden. Zur Nachbereitung einer Ausbildungseinheit stehen Zustandsspeicherfunktionen und Auswertungen zu Betriebsführung (Verspatungsminuten) und Bedienung zur Verfugung (Demitz et al. 2016).

# 8.7.3 Schulungen des Instandhaltungspersonals

Die Schulung des Instandhaltungspersonals kann in zwei unterscheidliche Zielgruppen differenziert werden:

Schulungen für die Instandhaltung der Streckeneinrichtungen: Ziel dieser Schulung ist es, ein umfassendes Verständnis für die Instandhaltung der Streckenausrüstung und die Ausrüstung in der Leitstelle zu vermitteln. Hierbei werden die folgenden Komponenten abgedeckt:

- Instandhaltung von Komponenten der Fahrwegsicherung (möglicherweise auch Stellwerk, Weichenantriebe, sekundäre Gleisfreimeldung, falls vorgesehen auch ortsfeste Signale)  
- Instandhaltung der CBTC Streckeneinrichtung (Transponder und CBTC-Streckengerät)  
- Instandhaltung der Leitstellentechnik  
- Instandhaltung des Datenkommunikationsssystems inklusive der hierfür erforderlichen Netzwerkkomponenten

Schulungen für die Instandhaltung der Fahrzeugeinrichtungen: Das Ziel dieser Schulung ist es, ein umfassendes Verständnis für die Wartung der Fahrzeugausrüstung zu vermitteln:

- Instandhaltung von Komponenten des Führerstands (Führerstandsdisplay und Taster)  
- Instandhaltung des Fahrzeugrechners (ATP und ATO)  
- Instandhaltung der Fahrzeugseitigen Anteile des Datenkommunikationssystems

# Literatur

Adler G et al (Hrsg) (1981) Lexikon der Eisenbahn, 6. Aufl. VEB Verlag für Verkehrswesen, Berlin  
Arpaci M, Schwarte A (2013) Refurbishment of metro and commuter railways with CBTC to realize driverless systems. Signal + Draht 105(7+8):42-47  
Brückner D (2017) Lösungen für das automatisierte Fahren im Nahverkehr. Signal + Draht 109(6):6-11  
Cabrera A (2009) Gleisgeometriemessung in New York City. Eisenbahntechn Rundsch 58(12):712-715  
Demitz J, Steffen W, István H (2016) RBC-Bedienoberflächen im internationalen Vergleich. EI - Eisenbahningenieur 2016:38-41  
Diemunsch K (2016) Testing communications-based train control. In: Richard Y (Hrsg) Advances in communications-based train control systems. CRC Press, Boca Raton, S 15-41  
DIN EN 16186-1:2019-04 Bahnanwendungen- Führerraum - Teil 1: Anthropometrische Daten und Sichtbedingungen. Deutsche Fassung EN 16816-1:214+A1:2018  
DIN EN 50126-1:2018-10 Bahnanwendungen - Spezifikation und Nachweis von Zuverlösigkeit, Verfügbarkeit, Instandhaltbarkeit und Sicherheit (RAMS) - Teil 1: Generischer RAMS-Prozess; Deutsche Fassung EN 50126-1:2017  
DIN EN 50128:2012-03 Bahnanwendungen - Telekommunikationstechnik, Signaltechnik und Datenverarbeitungssysteme - Software für Eisenbahnsteuerungs- und Überwachungssysteme; Deutsche Fassung EN 50128:2011  
DIN EN 50129:2019-06 Bahnanwendungen - Telekommunikationstechnik, Signaltechnik und Datenverarbeitungssysteme - Sicherheitsbezogene elektronische Systeme für Signaltechnik; Deutsche Fassung EN 50129:2018 + AC:2019  
DIN EN 60529:2014-09 Schutzarten durch Gehäuse (IP-Code)  
DIN EN 61373:2011-04 Bahnanwendungen - Betriebsmittel von Schierenfahrzeugen - Prüfungen für Schwingen und Schocken  
Dombrowsky H, Müller R, May A, Seitzinger E (2008) Première für Deutschlands erstene automatisierte U-Bahn. Nahnverker 26(5):8-16  
Dydak P (2019) Warum Fahrsimulatoren? Vorteile und Grenzen these technischen Hilfsmittels bei der Aus- und Weiterbildung. Nahverkehr 37(1+2):12-15  
IEC 62267 (2009) Railway applications - Automated urban guided transport (AUGT) - Safety requirements, Edition 1.0, 2009-07  
Koch G, Schütte J, Benedikt W (2014) SAT-valid: Tool-gestützte Prüfung und Validierung von ETCS-Streckenausrüstungen. Signal + Draht 106(3):18-22  
Laumen H, Henning S (2012) Obsoleszenz im Bereich LST. Signal + Draht 104(4):6-12  
McCullough I (2008) Trends in modern Masstransit train control. Signal + Draht 100(10):41-47  
Schnieder L (2024) Entwicklung von Regelwerken für den automatisierten Betrieb. Beitrag angenommen zur Veröffentlichung. Eisenbahningenieur 74(2024):1/2

Schnieder L, Rainer D, Harald F (2021) Integration von CBTC-Systemen in Schienenfahrzeuge. Eisenbahntech Rundschau 6:30-33  
Schroeder M (2002) Qualitätsmanagement von Projektierungsdaten für Zugsicherungssysteme. Signal + Draht 94(1+2):14-18  
Schröter R (2008) Dienstanweisungen nach BOStrab. Der Nahverkehr 7+8, 29-36  
Schult J, Rege G, Carroué C (2015) Betriebs- und Stellwerkssimulation BEST bei der üstra Hannoversche Verkehrsbetriebe AG. Signal + Draht 107(4):18-21  
Schütte J, Jurtz S, Manschewski H-W (2008) SAT.engine - eine innovative Plattform zur Unterstützung von ETCS-Projekten. Signal + Draht 100(3):17-22  
de Silvestre E (2005) CBTC applied to re-signalling metro lines upgrades performance. Signal + Draht 97(5):39-41  
Straßenbahn-Bau- und Betriebsordnung vom 11. Dezember 1987 (BGBl. I S. 2648), zuletzt geändert durch Antikel 1 der Verordnung vom 1. Oktober 2019 (BGBl. I S. 1410)  
UIC 651:2002-07 Layout of driver's cabs in locomotives, railcars, multiple unit trains and driving trailer  
VDV-Schrift 161-2 (2009) Sicherheitstechnische Anforderungen an die elektrische Ausrüstung (10/2009)  
Wigger P (2016) Verantwortlichkeiten bei Neubau, Erweiterung oder Modernisierung eines Nahverkehrssystems. Signal + Draht 108(3):49-61

# Perspektiven und zukünftige Herausforderungen

9

# SN Flashcards

Als Käfer*in diesen Buches können Sie kostenlos unsere Flashcard-App „SN Flashcards" mit Fragen zur Wissenschaftung und zum Lernen von Buch-inhalten nutzen.

1. Gehen Sieitte aufhttps://flashcards.springernature.com/login und  
2. erstellen Sie ein Benutzerkonto, indem Sie ihre Mailadresse angegeben und ein Password vergehen.  
3. Verwenden Sie den folgenden Link, um Zugang zu Ihr dem SN Flashcards Set zu halten:  $\triangleright$  https://sn.pub/sK5mLQ

Sollte der Link fehlen oder nicht Funktionieren, senden Sie unsitte eine E-Mail mit dem Betreff „SN Flashcards“ und dem Buchtitel an customerservice@springernature.com

Communications-Based Train Control Systeme haben sich in den letzten Jahrzehnten weltweit de facto als Standard herausgebildet (UITP 2019). Alle Systemhäuser haben mittlerweile in vielen Projekten Erfahrungen in der praktischen Realisierung gesammelt. Dies betrifrft sowohl Neubauprojekte als auch komplexe Umbauten der signaltechnischen Infrastruktur „unter rollendem Rad". Die CBTC-Ausrüstung städtischer Bahnsysteme wird zukünftig weiter zunehmen (vgl. Abschn. 9.1). Allerdings sind zukünftig von den Betriebern und den Systemherstellern weitere Herausforderungen zu losen. Dies ist kein der aktuell fehlenden Standardisierung der herstellerspezifischen Systemlösungen (vgl. Abschn. 9.2) auch eine Integration von CBTC-Systemen in die Systemtechnik und Ver

kehrsplanung des Straβenverkehrs Dort, wo Stadtbahnsysteme die Verkehrsfläche mit anderen Verkehrsteilnehmern teilen (vgl. Abschn. 9.3). Hinsichtlich zukünftiger Entwicklungsperspektiven sind auch aktuelle Entwicklungen in der Systemarchitektur relevant. Diese Themen werden in Abschn. 9.4 hinsichtlich einer alternative Funktionsaufteilung zwischen Fahrzeug- und Streckeneinrichtungen erörtert.

# 9.1 Entwicklung der installierten Basis

Viele Städte weltweit haben in den letzten Jahren bereits neue Systeme mitCOMMunikationsbasierten Zugsicherungssystemen in Betrieb genommen. Diese Trend wird sich zukünftig fortsetzen. Im nachsten Jahrzehn ist weltweit eine rapide Zunahme fahrerloser Systeme absehbar (UITP 2019). Prognosen auf Grundlage bereits bestätigter Projekte zeigen, dass sich die Streckenlänge fahrerloser Metrosysteme von insgesamt  $1026\mathrm{km}$  im Jahre 2018 in den nachsten zehn Jahren auf mehr als  $3800\mathrm{km}$  mehr als verdreifachten wird (vgl. Abb. 9.1). Der große Anteil wird hierbei auf die erwarteten Eröffnungen neuer Linien entfallen. Der überwiegende Anteil hiervon allgemein in Asien, bzw. speziell in China (Schnieder 2019a). Ein geringer Anteil ( $7\%$  der Streckenlänge) wird auf europäische Modernisierungssprojekte entfallen. Auch in Deutschland ist dieser Trend inzwischen angekommen. In Nürnbergblick der Betreiber inzwischen fast zehn Jahre Betriebserfahrung mit einem fahrerlosen System zurück. In Wien haben die Arbeiten für die Einführung einer fahrerlosen U-Bahn Linie (U5) begonnen (Heinrich et al. 2019). In Hamburg wird der Neubau einer fahrerlosen Linie der U-Bahn erwogen und die bestehenden Linien U2 und U4 werden in den nachsten Jahren in den halbautomatischen Betrieb überführ. Im Stadtbahnsystem der Stadt Frankfurt am Main werden die innerstädtischen Tunnelstrecken in den nachsten Jahren mit einem CBTC-System für den halbautomatischen Betrieb ertuchtigt. Weitere Betreiber im deutschensprachigen Raum befassen sich konkret mit der Systemauswahl und bereiten Ersatzinvestitionen in ihren Netzen vor. CBTC-Systeme werden daher in absehbarer Zukunft in Deutschland zunehmend zum Einsatz kommt.

# 9.2 Standardisierung von Systemlösungen

Bislang sind die CBTC-Systemlösungen ausschließlich propietär. Durch die große Heterogenität von Nahverkehrssystemenzeichnet sich - den Bemühungen einiger ausgewählter Betreiber großer U-Bahn- und Stadtbahnsysteme zum Trotz - nicht ab, dass sich an thisem Zustand in absehbarer Zukunft etwas ändern wird. Damit sind die Betreiber mit ihrer Investitionsentscheidung über den gesamten Lebenszyklus der Anlage an einen Hersteller gebunden. Ursächlich hierfür sind die fehlende Interoperabilität und Aus-tauschbarkeit von Komponenten.

- Interoperabilität bezeichnet die Möglichkeit, dass im Netz eines Betreibers Fahrzeug mit CBTC-Fahrzeugeinrichtungen eines Herstellers mit den Streckeneinrichtungen anderer Herstellers wechselwirken können. Um eine solche Interoperabilität zu erreichen,.musten CBTC-Systeme am Luftspalt zwischen Fahrzeug und Strecke logisch und physikalisch standardisiert sein (McCullough 2008). Dies ist aktuell nicht der Fall.  
- Austauschbarkeit beteutet die Möglichkeit, Elemente des CBTC-Systems gegen Sub-systeme/Komponenten eines anderen Herstellers auszubauschen. Hierbei soll es möglich sein, einzelne Elemente des CBTC-Systems austauschen zu konnen, ohne das gesamte System ersetzen zu müssen. Die Austauschbarkeit braucht standardisierte CBTC-Systemarchitecturen mit wohldefinierten Schnittstellen. Dies setzt unter andere eine einheitliche Zuordnung von Funktionen auf Systemkomponenten voraus (McCullough 2008). Zukünftig konnten Betreiber in ihren Ausschreibungen Anleihen an im Betrieb von Eisenbahnen etablierte standardisierte Schnittstellen zu Nachbarsystemen (Stellwerke, Leitstelle und Funkstreckenzentrale) sowie zu dezentralen Feld-elementen (bspw. für Weichen und Gleisfreimeldung)ephemn (Elsweiler 2014). Durch die Eulynx-In initiative liegen hier in der Praxis bewährte standardisierte Schnittstellen vor, von denen auch Nahverkehrsbetreiber profitieren konnten (Muller 2021).

Das insbesondere für Vollbahren europaweit und herstellerübergreifend einheitlich definierte European Train Control System (ETCS) ist ein expliziter Gegenwert zu den proprietären CBTC-Systemlösungen. ETCS Level 3 und CBTC-Systeme sind einander hinsichtlich ihrer potenziellen wirtschaftlichen Auswirkungen im Sinne reduzierter Lebenszykluskosten vergleichbar. Einen klaren Vorteil weist das ETCS hinsichtlich der Austauschbarkeit und Interoperabilität auf. Demgegenüber weist CBTC tatsäch dann Vorteile auf, wenn hohe Zugdichten gefordert werden und eine hohe Automatisierung (Driverless Train Operation oder höher) angestrebt wird. Wenn eine ausreichende Kapazität auch ohne das Fahren im wandernden Raumabstand geschaffen werden kann, konnen die Vorteile des ETCS möglicherweise zukünftig auch für die Nahverkehrsunternehmen genutzt werden (Schnieder 2019b, 2020).

# 9.3 Integration der Straβenverkehrstechnik in Stadtbahnsystemen

Für Stadtbahnsysteme ist die Einbindung der Straβenverkehrstechnik essenziell. Die durch das Fahren im wandernden Raumabstand in den zentralen Tunnelabschnitten realisierbaren kürzeren Zugfolgezeiten mit den hereaus resultierenden Kapazitätsgewinnen (Anzahl Zugfahrten pro Fahrtrichtung und Stunde) sind nur dann zu realisieren, wenn der Zufluss in die, bzw. der Abfluss aus den in der Regel halb automatisch betriebenen Tunnelstrecken ebenfalls signifikant verbessert wird. Bislang treffen aus dem Oberflächenbereich

in die zentrale Tunnelstrecke einbrechende Fahrzeuge ungleich verteil im Takt der Umlaufzeit der Lichtsignalanlagen (in der Regel 90 Sekunden) im Zulauf der Tunnelstrecken ein und verursachen Dort Versprütungen im Betriebsablauf. Dadurch, dass das Bestandsysteme bereits an ihrer rechnerischen Kapazitätsgrenze betrieben werden und den gesamten Tag über dichte Fahrplantakte gefahren werden, kann diese Versprüfung über den Betriebstag hinweg nicht wieder abgebaut werden. Parallel zur systemtechnischen Erneuerung der Tunnelstrecken ist davon auch eine Steigerung der Leistungsfähigkeit der zu- und abbringenden im Fahren auf Sicht betriebenen Außenste von Stadtbahnsystemen zwingend geboten. Hierfür müssen in Abstimmung mit dem jeweiligen Straβenverkehramt der Kommune verschiedene Architekturvarianten der Anbindung an das CBTC-System gegeneinander abgewogen werden (Sandrock und Riegelhuth 2014):

- Dezentrale Kommunikation zwischen Stadtbahnfahrzeugen und Lichtsignalanlagen: Klassischerweise geschieht die Beeinflussung von Lichtsignalanlagen durch eine Interaktion zwischen dem Stadtbahnfahrzeug und dem Steuererat der Lichtsignalanlage. Hierbei kommt bislang Bake-Funk-Systeme im Sinne einer dezentralen OPNV-Priorisierung zum Einsatz. Fahrt ein Fahrzeug in den Erfassungsbereich einer orts-festen Bake, sendet das Fahrzeug ein Funktelegramm an den Empfänger der in der Nähe befindlichen Lichtsignalanlage. Das Stadtbahnfahrzeug sendet eine Anmeldung an das Steuererat. Um Reisezeiten zu reduzieren, werden Rotphasen der Lichtsignalanlage gekürzt und Grünphasen verlangert. Alternativ werden Phasen eingefügt, entfallen oder werden getauscht. Das Stadtbahnfahrzeug erhalten grüne Licht noch bevors die Haltelinie erreicht, so dass es nicht abbremsen muss. Nachdem das Stadtbahnfahrzeug die Kreuzung passiert hat, sendet es eine Abmeldenachricht an das Steuererat (Rüffer et al. 2019).

- Zentralenbasierte Kopplung von Stadtbahnfahrzeugen und Lichtsignalanlagen. Die Kommunen betreiben in der Regel eine Verkehrsmanagementzentrale. Bereits seit längerer Zeit haben die Kommunen die strategische Weichenstellung für den Einsatz herstellerunabhängiger Schnittstellenstandards in der Straβenverkehrstechnik vorgenommen, was unter dem Stichwort Open Communication Interface for Road Traffic Control Systems (OCIT) subsummiert wird. Dies umfasst bislang im Wesentlichen die sogenannte OCIT-Outstations Schnittstelle (OCIT-O) zur Verbindung der Lichtsignalsteuergeräte mit dem zentralen Verkehrsrechner. Über den Aufbau einer so genannten OCIT-Schnittstelle „Center-to-Center" (OCIT-C) wird es in dieser Architekturvariante zukünftig möglich, die Leitebene des CBTC-Systems mit dem Verkehrsrechner der Kommune zu verbinden. Von der Leitebene des CBTC-Systems übertragene Zustandsdaten führen zu einer gezielten Priorisierung von Stadtbahnfahrzeugen an Lichtsignalgeregelten Knoten im Straβenverkehrnetz (Rüffer et al. 2019).

Neben der zuvor dargestellen systemtechnischen Integration müssen ebenfalls verkehrplanerische Aspekte mit betrachtet werden. Hier kann es sinnvoll sein, gezielt Parameter wie Umlaufzeiten zu variieren und an der Koordination mehrerer hintereinanderliegender Knoten zu arbeiten.

# 9.4 Alternative Funktionsaufteilung zwischen Fahrzeug und Strecke

In Abschn. 2.1 wurde eine exemplarische Systemarchitektur für CBTC-Systeme vorgestellt, wie sie bislang allgemein bei den verschiedenen Herstellern üblich war. Neue technologische Entwicklungen erfolgsorientierter Anwendungen in Rechenzentren dargestellt. Abschn. 9.4.1 eine Zentralisierung Sicherheits-relevanter Anwendungen in Rechenzentren dargestellt. Abschn. 9.4.2 stellt eine Fahrzeug-zentrierte Sicht vor, welche die zuvor streckenseitige Logik auf das Fahrzeug portiert. Beiden Ansätzen ist gemeins, dass nur noch Steuerungen zum Stellen und Überwachen einzelner Fahrwegelemente direkt entlang der Strecke verbleiben.

# 9.4.1 Zentralisierung Sicherheitsrelevanter Anwendungen in Rechenzentren

Die grundlegende Idee these Ansatzes ist es, die Logik der Fahrewegsicherung und der streckenseitigen Komponenten der Zugbeeinflussung in einem Rechenzentrum zu betreiben. Die zentrale Logik des Rechenzentrums ist über ein IP-basiertes Netzwerk mit Steuerungseinrichtungen verbunden, welche nur die Stell- und Überwachungslogik für die einzelnen Fahrwegelemente enthalten (OC, object controller). Technisch ist das Rechenzernum mit COTS-Komponenten ausgeführrt. COTS steht hierbei für Commercial off-the-shelf, d. h. es handelt sich hier um Komponenten „von der Stange". Dies umfasst sowohl Hardware- als auch Softwareprodukte, die baugleich und in große Stückzahlen hergestellt und verkauf werden. Durch den sehr hohen Grad der Zentralisierung im Rechenzentrum entsteht der Bedarf nach erweiterten Verfügbarkeitsmechanismen, Denn es muss nicht nur der Ausfall einer einzelnen COTS-Hardware, sondern auch der Totalausfall des Rechenzentrums (etwa infolge von Stromausfall, Überschwemmung, Feuer) beherrscht werden. für hochste Verfügbarkeit ist es deshalb notwendig, dass ein Rechenzentrum als Ganzes redundant an verschiedene Orten installiert und betrieben werden kann (Steffens und Hempel 2023). Vorteile these Konzepts ergeben sich hinsichtlich der Instandhaltungs- und Updatepolitik. So ist es oftmales nicht mehr notwendig zur Anlage zu

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-11/4a62bc17-5b63-49ab-9a86-3a43cc7f4295/cbf76459909d3c618bfd4d702116dee9ff8fdeac8cc49cd903bef1cbb78ffdf0.jpg)  
Abb. 9.1 COTS-Hardware basiertes Rechenzentrum mit geografischer Redundanz

fahren, um diagnose- und teilweise auch Wartungsarbeiten durchzuführen. Durch den Betrieb wesentlicher Systembestandteile im Rechenzentrum ergeben sich darüber hinaus möglicherweise Synergieeffekte mit anderen IT-Wartungspersonal beispisse im Bereich der Kommunikationstechnik (Abb. 9.1).

# 9.4.2 Fahrzeugzentrierte Funktionsallokation

Bei dieser Systemausprägung entfallen in konventionellen CBTC-Architekturen (vgl. Abschn. 2.1) zuvor zentral verortete Funktionanteile in der Infrastruktur (Schnieder 2020). Dies kann sehr deutlich am Streckenatlas festgemacht werden, der in konventionellen CBTC-Architekturen sowohl auf dem Fahrzeug als auch in den Infrastrukturkomponenten, quasi als „gemeinsames Koordinatensystem“, vorgehalten wurde. Durch eine direkte Kommunikation der Fahrzeuge unterinander (Vehicle to Vehicle Communication, V2V) über das streckenseitige Datenkommunikationssystem teilen sich die Fahrzeuge relevante Gefahrpunkte wie das Heck des vorausfahrendenden Zuges direkt mit. Hierdurch entfallen Reaktionszeiten zur Signalverarbeitung in zwischenliegenden streckenseitigen Sicherungssystemen. Ein weiterer Unterschied ist die ausschließlich direkte Steuerung beweglicher Fahrwegelelemente und Beanspruchung von Gleisabschnitten durch

das Fahrzeug selbst auf der Grundlage einer unmittelbaren Kommunikation des Fahrzeugs mit dem Feldelement-Controller (quasi Einzelweichensteuerungen). War für die zuvor dargestelle konventionelle Systemausprüfung eine Zuglaufverfolgung (Automatic Train Tracking, ATT) und Zuglenkung (Automatic Route Setting, ARS) durch die Auswertung von der Streckenseite bereitgestellter Zustandsgroßen von der Leitstelle prägend (Mücke 2005), beruht die Fahwegauswahl und die Anforderung der korrekten Endlage der einzelnen hierfür erforderlichen beweglichen Fahrwegelemente nun auf dem individuellen „Einsatzauftrag" (Mission), der jedem Fahrzeug direkt aus der Leitstelle übermittelt wird. Dies bedeutet, dass die sicherungstechnische Bemessung (beispielsweise von Streckenlägen wie Durchrutschwegen, Blockabschnittsteilungen oder Zeitanteilen wie geschwindigkeitsabhängige Einschlzahlen) sowie die Darstellung im Streckenatlas nicht mehr statisch anhand der Flotteneigenschaften (beispisse weise bei Einschlzahlen als „Worst Case" dem schnellsten Fahrzeug) erfolgt. Diese Strecken und Zeitanteile werden nur von jedem Fahrzeug anhand seiner eigenen fahrodynamischen Eigenschaften berechnet. Dies erhöht die Flexibilität der Nutzung der Infrastruktur und gestattet eine Optimierung der erreichbaren Zugfolgezeiten.

# Literatur

Elsweiler B (2014) Beyond ETCS – Interoperable interfaces and more. IRSE NEWS 198, S 2  
Heinrich N, Stuchlik C, Schnieder L (2019) Automatisierung der Linie U5 in Wien. Eisenbahntechn Rundsch 68(6):24-27  
International Association of Public Transport (UITP) (2019) World report on metro automation. Brüssel  
McCullough I (2008) Trends in modern mass-transit train control. Signal + Draht 100(10):41-47  
Mücke W (2005) Betriebsleittechnik im öffentlichen Verkehr, 2. Aufl. Eurailpress, Hamburg  
Müller R (2021) Digitale Stellwerke tragen die Digitalisierung der Bahn. EIK - Eisenbahningenieurkompendium 2021. Eurailpress, Hamburg, S 180-201  
Rüffer M, Schmidt C, Schnieder L (2019) Erneuerung der Zugsicherung als Chance für die Automatisierung von Stadtbahnsystemen. Eisenbahntechn Rundsch 68(9):19-23  
Sandrock M, Riegelhuth G (2014) Verkehrssmanagementzentralen in Kommunen - Eine vergleichende Darstellung. Springer, Berlin  
Schnieder L (2019a) Stand und Perspektive von Metrosystemen in China. Eisenbahntechn Rundsch 68(7+8):10-13  
Schnieder L (2019b) Zugbeeinflussungssysteme für Stadtbahnen im Vergleich. EI - Eisenbahn-ingenieur 69(11):31-34  
Schnieder L (2020) Funktionsallokation in funkbasierten Zugbeeinflussungssystemen - ein Vergleich. ETR - Eisenbahntechnische Rundchau 70(11):16-19  
Steffens S, Hempel T (2023) Vom Digitalen Stellwerk in die Cloud. Deine Bahn 8:22-27

# Stichwortverzeichnis

# A

Abfertigung 18, 98, 110

Abfertigungsbedingungen 98

Abfertigungsverfahren 78

"Access Point" 127, 130, 166

Access Points 19, 21, 23

Ausfahrbeschränkung 98

,Austauschbarkeit180,181

Automatic Route Setting" (ARS) 25, 185

siehe auch Zuglenkung 25, 185

Automatic Train Control (ATC) 11, 13

Automatic Train Operation (ATO) 13, 27

Automatic Train Protection (ARP) 13

Automatic Train Protection (ATP) 13

Automatic Train Supervision (ATS) 13, 23

Automatic Train Tracking (ATT) 25

siehe auch Zuglaufverfolgung 25

,Automatisierungsgrad

GoA 3 - begleiteter fahrerloser

Zugbetrieb" 90

Automatisierungsgrad 13, 14, 17, 18, 40, 85, 103

GoA 0-Zugbetrieb auf Sight 40,84

GoA 1 - halbautomatischer Zugbetrieb 41

GoA 1-nicht automatisierter Zugbetrieb 40,85

GoA 3 - begleiteter fahrerloser Zugbetrieb 41

GoA 3-vollautomatischer fahrerloser Betrieb 55

"Automatisierungsgrad" 89

"Availability" 118, 125

# B

Bahnsteigtür 86, 90-93, 95, 97

Bahnübergang 65

,Bandbreite" 120, 174

Befahrbarkeitseinschänkung 85

Befahrbarkeitssperre 88

Beschaffungskosten 8

,Betriebshof49,55,85,127,165

,Betriebskosten"9,149

,Betriebssimulation"138,140,142

Bremskurve 68

# C

"Capital Expenditure" (CAPEX) 9, 134

siehe auch Beschaffungskosten 134

"Categories" 136

siehe auch Kostenarten 136

"Cost Breakdown Structure" (CBS) 136

siehe auch Kostenaufbruchstruktur 136

# D

„Datumkommunikationssystem“ 56,76,129, 166,167,176,184

design headway 7

"Disposition" 5, 13, 25, 26, 176

"Doppelausrüstung"

Fahrzeuge 149, 150

Strecke 151

# E

Einfahrbschrankung 89

Einklemmerkennung 99,100

Einklemmschutz 100

,Elektromagnetische Verträglichkeit" (EMV) 163

Evakuierung 86,95,103,105 106,110-112

# F

"Factory Acceptance Test" (FAT) 164

Fahrerlaubnis 45, 47, 58, 66-68, 98

,Fahrgastinformation"3,4,167

Fahrstraβenverschluss 62

Fahrstrategie 17, 77, 79

Fehlerkategorie 104

Fixed Block 5, 66

Fixed Blockstand

siehe auch fester Raumabstand 66

Flankenschutz 15,62,88

,Führerstandsanzeige" 82,83,85,102,174

# G

Gegenfahrschutz 66

Geschwindigkeitsprofil, statistisches 67, 68

"Gleisfreimeldung" 129, 137, 152, 181  
sekundäre 129, 160, 176

Gleisfreimeldung

primäre 14

sekundäre 14

Gleiten 71, 72, 74

Grade of Automation (GoA) 40-42 siehe auch Automatisierungsgrad 40

# H

Handover 19, 22

headway 7

Hinderniserkennung 59,86,105,114

# 1

"Inbetriebnahme" 161, 162, 164

,Inbetriebnahmetest 165,166

,Informationssicherheitsmanagementsystem" (ISMS) 125

,Infrastruktur, kritische 124

,Integrationstest" 172

"Interoperabilität 181, 182

# K

Kehrfahrt, fahrerlose 53

,Kostenart" 134,136

,Kostenaufbruchstruktur 134

# L

"Lebenszykluskosten" 8, 134, 136, 137, 181

Lichtraumprofil 65, 66, 85

"Lichtsinalanlage" (LSA) 65, 182

"Life Cycle Costs" (LCC) 8, 134

# M

"Maintainability" 118, 126

,Migrationsstrategie" 148

Moving Block 5, 65

siehe auch Raumabstand, wandernder 65

# N

Nachpositionieren 92

,Non-automated Train Operations" (NTO) 40  
siehe auch Automatisierungsgrad 40

Notfuhrstand 18

# 0

,Operational Expenditure" (OPEX) 9, 134 operational headway 7

,Ortsbake" 74

Radarsensor 71

"Ortung" 13,48,49,66,70,71,75

Beschleunigungssensor 115

"Ortungsgenaugigkeit 74

# P

"Product Breakdown Structure" 134

siehe auch Produktaufbruchstruktur 134

"Produktaufbruchstruktur" 134

# R

"Ruumabstand"Wandernder 45, 51, 181

Ruumabstand fester 5,27 wandernder 6,28

,Raumabstandwanderndner152

"Reliability" 118, 125, 128

,Risikoanalyse" 118-120,122,123

,Risikograf 120,121

Roaming 21-23

Rückrollüberwachung 48

# S

,Safety"118,119

,Schleichfahrt 92

,Schleudern" 71,72,74

"Schlupf' 71, 72, 74 Gleiten 72

"Security" 118, 124 siehe auch Verlässlichkeit 118

,Semi-automated Train Operation" (STO) 83 siehe auch Automatisierungsgrad 83

,Sicherheit 90,118-120,122-124

,Sicherheitsintegritätsevel" (SIL) 119-121, 123

,Sicherheitsnachweis" 119

,Sieving"51

„Site Acceptance Test“ (SAT) 168

Sperrzeit 6

Sperrzeitenband 6

Sperrzeitentreppe 6

"Stellwerk" 13, 15, 27, 28, 134, 150, 164, 167, 176, 181

"Störungsbetrieb" 56

,StraBenverkehrstechnik" 181

"Streckenatlas 16,51,67,75,77

# T

,Technischer Sicherheitsbericht119

,Test"152,163,165,167,171

"Testcenter" 163, 164, 168

"Testgleis" 149, 162, 165, 166

"Testlabor 162

"Train Operations on Sight" (TOS) 40  
siehe auch Automatisierungsgrad 40

"Training" 176

Fahrdienstleiter 175

Fahrertraining 174

Instandhaltertraining 176

"Traktionsstromversorgung" 66, 76, 111, 153, 167

“Turfreigabe"84,89,90,106

# U

"Ubereinstimmungsprüfung" 166

"Umselttest" 162

"Umweltbedingung" Klima 2, 163

Unmanned Train Operation (UTO) 8

siehe auch Automatisierungsgrad 8

# V

"Verfugbarkeit 106, 118, 124, 125, 128, 130, 137, 144

Ausfallzeit, mittlere 125

Klarzeit, mittlere 125

,Verlässlichkeit" 117

Angriffssicherheit 118

Instandhaltbarkeit 125

Sicherheit 122

# W

"Weichenverschluss" 62

Wireless Local Area Networks (WLAN) 21

# Z

"Zugfolgezeit 6,7,56,181,185 siehe auch headway 185

"Zuglaufverfolgung" 25, 168, 176, 185

"Zuglenkung" 25, 26, 176, 185

,Zurücksetzen"92

,Zu verlüssigkeit" 97, 118