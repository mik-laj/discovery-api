#  Versionshinweise

Auf dieser Seite werden die Produktionsaktualisierungen für Cloud Data Loss
Prevention (DLP) dokumentiert. Prüfen Sie diese Seite regelmäßig auf Hinweise
zu neuen oder aktualisierten Features, bekannten Problemen und verworfenen
Funktionen.

**Aktuelle Version: v2**

Fügen Sie die URL dieser Seite Ihrem [ Feedreader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) hinzu, um die
neuesten Produktaktualisierungen zu erhalten.

##  4\. April 2019

**FEATURE:** Zusätzliche [ infoType-Detektoren
](https://cloud.google.com/dlp/docs/infotypes-reference?hl=de) hinzugefügt:

  * ` INDONESIA_NIK_NUMBER `
  * ` AUSTRALIA_PASSPORT `
  * ` BELGIUM_NATIONAL_ID_CARD_NUMBER `
  * ` GERMANY_TAXPAYER_IDENTIFICATION_NUMBER `
  * ` PASSPORT `
  * ` SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER `
  * ` SINGAPORE_PASSPORT `
  * ` TAIWAN_PASSPORT `
  * ` TURKEY_ID_NUMBER `

##  29\. März 2019

**FEATURE:** Neue crypto-basierte Tokenisierungsmethode hinzugefügt: [ `
CryptoDeterministicConfig `
](https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates?hl=de#cryptodeterministicconfig)
. Weitere Informationen finden Sie unter [ Transformationsreferenz
](https://cloud.google.com/dlp/docs/transformations-reference?hl=de) .

##  8\. März 2019

**FEATURE:** Neue [ Cloud DLP-UI-Beta
](https://console.cloud.google.com/security/dlp;source=7?hl=de) in der Google
Cloud Platform Console hinzugefügt.

##  11\. Februar 2019

**FIXED:** In der Dokumentation ist jetzt erklärt, welches Verhalten Nutzer
für [ ` ALL_BASIC ` ](https://cloud.google.com/dlp/docs/infotypes-
reference?hl=de) erwarten können.

**CHANGED:** Standardliste der infoTypes in [ ` ALL_BASIC `
](https://cloud.google.com/dlp/docs/infotypes-reference?hl=de) aktualisiert.

##  12\. Dezember 2018

**FIXED:** Anfragen zur De-Identifikation mit [ ` CryptoReplaceFfxFpeConfig `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2?hl=de#cryptoreplaceffxfpeconfig)
validieren das Alphabet des zu transformierenden Werts jetzt erwartungsgemäß
mit dem Transformationsalphabet. Dabei werden Werte mit Leerzeichen korrekt
abgelehnt, wenn Leerzeichen nicht Teil des Alphabets sind. Ungültige Anfragen
geben einen Fehler in der ` TransformationSummary ` mit der folgenden Meldung
aus: "CryptoReplaceFfxFpeConfig's 'alphabet' does not include all the
characters in the value being transformed; the set of distinct characters in
any given value being transformed by this transformation must be a subset of
the set of characters comprising the 'alphabet'." (Das Alphabet von
CryptoReplaceFfxFpeConfig enthält nicht alle Zeichen, die im zu
transformierenden Wert vorhanden sind. Der Satz von unterschiedlichen Zeichen
in einem durch diese Transformation zu transformierenden Wert muss eine
Teilmenge des Zeichensatzes sein, aus dem das "Alphabet" besteht.)

##  25\. Oktober 2018

**FEATURE:** Zusätzlicher [ infoType-Detektor
](https://cloud.google.com/dlp/docs/infotypes-reference?hl=de) hinzugefügt:

  * ` NORWAY_NI_NUMBER `

##  2\. Oktober 2018

**FEATURE:** Cloud Storage [ ` FileSet `
](https://cloud.google.com/dlp/docs/reference/rest/v2/InspectJobConfig?hl=de#fileset)
unterstützt nun auch die Verwendung von Filtern mit regulären Ausdrücken bei
der Angabe der von der Überprüfung ein- oder auszuschließenden Dateien. Dies
ist dann nützlich, wenn der zu durchsuchende Satz von Dateien nicht mit einem
Pfad und Platzhaltern genau ausgedrückt werden kann, wie z. B.:

  * Sie können alle Dateien durchsuchen, dabei aber bestimmte Dateien oder Ordner überspringen, die mit Sicherheit keine sensiblen Daten enthalten. 
  * Sie können nur Dateien durchsuchen, deren Endungen zu einer bestimmten Reihe von Dateiendungen zählen, beispielsweise nur TXT-, CSV- und JSON-Dateien. 
  * Sie können nur Dateien durchsuchen, deren Endungen nicht zu einer bestimmten Reihe von Dateiendungen zählen, und beispielsweise PDF-Dateien überspringen. 

##  19\. September 2018

**FEATURE:** Die [ Erweiterung vorhandener infoType-Detektoren
](https://cloud.google.com/dlp/docs/creating-custom-infotypes-rules?hl=de)
mithilfe von Ausschlussregeln und Hotword-Regeln wird jetzt unterstützt.

##  24\. August 2018

**FEATURE:** Zusätzlicher [ infoType-Detektor
](https://cloud.google.com/dlp/docs/infotypes-reference?hl=de) hinzugefügt:

  * ` DENMARK_CPR_NUMBER `

##  17\. August 2018

**FEATURE:** Zusätzliche [ InfoType-Detektoren
](https://cloud.google.com/dlp/docs/infotypes-reference?hl=de) hinzugefügt:

  * ` CANADA_DRIVERS_LICENSE_NUMBER `
  * ` DATE `
  * ` DATE_OF_BIRTH `
  * ` FEMALE_NAME `
  * ` FINLAND_NATIONAL_ID_NUMBER `
  * ` GCP_CREDENTIALS `
  * ` GENDER `
  * ` JAPAN_BANK_ACCOUNT `
  * ` JAPAN_DRIVERS_LICENSE_NUMBER `
  * ` MALE_NAME `
  * ` NETHERLANDS_PASSPORT `
  * ` SPAIN_DRIVERS_LICENSE_NUMBER `
  * ` SWEDEN_NATIONAL_ID_NUMBER `
  * ` SWEDEN_PASSPORT `
  * ` TIME `
  * ` US_STATE `

##  10\. August 2018

**FEATURE:** [ Große benutzerdefinierte Wörterbücher
](https://cloud.google.com/dlp/docs/creating-stored-infotypes?hl=de) werden
jetzt unterstützt. Cloud DLP kann jetzt nach Wörterbüchern mit bis zu
Dutzenden Millionen Einträgen suchen.

**FEATURE:** [ ` CloudStorageOptions `
](https://cloud.google.com/dlp/docs/reference/rest/v2/InspectJobConfig?hl=de#cloudstorageoptions)
unterstützt jetzt die Begrenzung der Menge der pro Datei zu prüfenden Byte
nach prozentualem Anteil.

**FEATURE:** [ ` BigQueryOptions `
](https://cloud.google.com/dlp/docs/reference/rest/v2/InspectJobConfig?hl=de#bigqueryoptions)
unterstützt jetzt die Begrenzung der Anzahl der zu prüfenden Zeilen pro Datei
nach prozentualem Anteil.

##  1\. Juni 2018

**FEATURE:** Die [ Delta-Präsenzschätzung
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2?hl=de#privacymetric)
, ein Risikomesswert, der verwendet wird, wenn die Mitgliedschaft im Dataset
selbst eine vertrauliche Information ist, wird jetzt unterstützt.

##  18\. Mai 2018

**FEATURE:** Das Flag ` sample_method ` wurde zu [ ` BigQueryOptions `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2?hl=de#bigqueryoptions)
und [ ` CloudStorageOptions `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2?hl=de#cloudstorageoptions)
hinzugefügt, um Scans auf eine Stichprobe des Inhalts zu beschränken. Dies ist
nützlich, um große Datasets effizienter zu durchsuchen, wenn nur bestimmt
werden soll, ob sich dort sensible Daten befinden, und keine Liste aller
Übereinstimmungen erforderlich ist.

##  25\. April 2018

**FEATURE:** Das Flag ` row_limit ` wurde zu [ ` BigQueryOptions `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2?hl=de#bigqueryoptions)
hinzugefügt, um Stichproben von Tabellen zu ermöglichen, anstatt alle Zeilen
zu prüfen.

**FEATURE:** Wörterbücher können jetzt aus Dateien geladen werden, die in
Cloud Storage gespeichert sind und aus durch Zeilenumbruch getrennten Listen
mit Wortgruppen bestehen. Dies geschieht mit dem Parameter `
cloud_storage_path ` in [ ` CustomInfoType.Dictionary `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2?hl=de#google.privacy.dlp.v2.CustomInfoType.Dictionary)
. Nützlich für die Freigabe von Wörterbüchern für benutzerdefinierte Prüfungen
über mehrere Anfragen hinweg.

**FEATURE:** Für Kunden, die Cloud Security Command Center verwenden, kann die
Zusammenfassung eines ` DlpJob ` mithilfe der neuen Aktion [ `
PublishSummaryToCscc `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2?hl=de#action)
in Cloud SCC veröffentlicht werden.

##  21\. März 2018

**Release zur allgemeinen Verfügbarkeit (General Availability, GA) von Cloud
Data Loss Prevention (DLP) API**

**FEATURE:** Die neue Version [ V2
](https://cloud.google.com/dlp/docs/reference/rest/v2?hl=de) der API wurde auf
den Markt gebracht.

**CHANGED:** Die Methode [ ` jobs.create `
](https://cloud.google.com/dlp/docs/reference/rest/v2/projects.dlpJobs/create?hl=de)
wurde als Ersatz für [ ` dataSource.analyze `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/projects.dataSource/analyze?hl=de)
und [ ` dataSource.inspect `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/projects.dataSource/inspect?hl=de)
hinzugefügt.

**CHANGED:** Das Objekt [ ` ContentItem `
](https://cloud.google.com/dlp/docs/reference/rest/v2/ContentItem?hl=de) wurde
mit einer [ ` BytesType `
](https://cloud.google.com/dlp/docs/reference/rest/v2/ByteContentItem?hl=de#BytesType)
-Enum zur Angabe des zu prüfenden Datentyps vereinfacht.

**CHANGED:** Das Objekt [ ` Finding `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2?hl=de#google.privacy.dlp.v2.Finding)
wurde um eine neue [ ` ContentLocation `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2?hl=de#contentlocation)
erweitert, um Ergebnisse aus verschiedenen Datentypen (wie Bildern,
Datensätzen und Dokumenten) besser zu melden.

**CHANGED:** Das Objekt [ ` InfoTypeStatistics `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/projects.dlpJobs?hl=de#InfoTypeStatistics)
wurde in [ ` InfoTypeStats `
](https://cloud.google.com/dlp/docs/reference/rest/v2/projects.dlpJobs?hl=de#InfoTypeStats)
umbenannt.

**DEPRECATED:** Die v2beta1- und v2beta2-APIs wurden eingestellt.

##  16\. Februar 2018

**FEATURE:** Neue [ ` JobTriggers `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/projects.jobTriggers?hl=de)
ermöglichen die Planung regelmäßiger Scans des Speichers. In Kombination mit
der neuen [ ` TimespanConfig `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/InspectJobConfig?hl=de#timespanconfig)
können Scans auf neue oder geänderte Inhalte in BigQuery und Cloud Storage
beschränkt werden.

**FEATURE:** Benutzerdefinierte Detektoren auf der Grundlage von [ regulären
Ausdrücken
](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/InspectConfig?hl=de#regex)
werden jetzt unterstützt.

**FEATURE:** Die Auswahl einer standardmäßigen [ Wahrscheinlichkeit
](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/InspectConfig?hl=de#Likelihood)
für [ ` CustomInfoType `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/InspectConfig?hl=de#custominfotype)
-Detektoren und zur Einstellung der Wahrscheinlichkeit mit einer neuen [ `
DetectionRule `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/InspectConfig?hl=de#detectionrule)
, die in der Nähe einer Übereinstimmung auf ähnlichen Inhalt prüft, wird jetzt
unterstützt.

**FEATURE:** Benachrichtigungen über den Abschluss von Risikoanalyse- und
Prüfjobs können jetzt an [ Cloud Pub/Sub
](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/InspectJobConfig?hl=de#Action)
gesendet werden.

##  14\. Dezember 2017

**FEATURE:** Die neue Version [ V2Beta2
](https://cloud.google.com/dlp/docs/reference/rest/v2beta2?hl=de) der API
wurde auf den Markt gebracht. Sie enthält eine Reihe neuer und verbesserter
Funktionen, darunter Vorlagen für die dauerhafte De-Identifikation und für
Inspektionskonfigurationen, eine vereinfachte Job-API für die Speicherprüfung
und Risikoanalyse und vieles mehr.

Tipps für die Migration:

  * API-Methoden vom Typ [ ` Content ` ](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/projects.content?hl=de) akzeptieren jetzt ein einzelnes ` ContentItem ` . 
  * [ ` InspectConfig ` ](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/InspectConfig?hl=de) hat jetzt eine Standardwahrscheinlichkeit. Wenn nicht festgelegt, werden deshalb Übereinstimmungen unterhalb von ` POSSIBLE ` automatisch ausgeschlossen. 
  * Ergebnisse einer Speicherinspektion werden jetzt immer in Ihrer eigenen BigQuery-Instanz gespeichert, sodass Sie mehr Kontrolle über den Speicherort Ihrer sensiblen Daten haben. 
  * [ ` content.redact ` ](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/content/redact?hl=de) wurde zugunsten von [ ` content.deidentify ` ](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/projects.content/deidentify?hl=de) für das Entfernen sensibler Daten aus Text und zugunsten von [ ` image.redact ` ](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/projects.image/redact?hl=de) für das Entfernen sensibler Daten aus Bildern verworfen. 
  * [ ` InspectConfig ` ](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/InspectConfig?hl=de) benötigt jetzt mindestens einen [ ` InfoType ` ](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/InfoType?hl=de) oder [ ` CustomInfoType ` ](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/InspectConfig?hl=de#custominfotype) . 
  * Vorgänge mit langer Laufzeit wurden durch [ ` DlpJob ` ](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/projects.dlpJobs?hl=de) -Objekte zur Risikoanalyse und Speicherprüfung ersetzt. [ ` inspect.operations.create ` ](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/inspect.operations/create?hl=de) wurde in [ ` dataSource.inspect ` ](https://cloud.google.com/dlp/docs/reference/rest/v2beta2/projects.dataSource/inspect?hl=de) umbenannt. 

##  22\. November 2017

**FEATURE:** [ ` dataSource.analyze `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/dataSource/analyze?hl=de)
wurde um einen neuen Messwert für die Risikoanalyse, die _k_ -Map-Schätzung,
erweitert.

##  20\. Oktober 2017

**FEATURE:** Durch die Erweiterung von [ ` InspectConfig `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/InspectConfig?hl=de)
um ` CustomInfoType ` wird jetzt die Suche nach Wörtern oder Wortgruppen aus
einem benutzerdefinierten Wörterbuch unterstützt. Diese Funktion ist in [ `
content.inspect `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/content/inspect?hl=de)
, [ ` content.redact `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/content/redact?hl=de)
, [ ` content.deidentify `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/content/deidentify?hl=de)
und [ ` inspect.operations.create `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/inspect.operations/create?hl=de)
aktiviert.

##  15\. September 2017

**FEATURE:** Durch die Einführung von [ ` content.deidentify `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/content/deidentify?hl=de)
wird jetzt die De-Identifikation von Inhalten unterstützt.

**FEATURE:** Durch die Einführung von [ ` dataSource.analyze `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/dataSource/analyze?hl=de)
werden jetzt Risikoanalysen in BigQuery unterstützt.

##  17\. August 2017

**FEATURE:** Durch die Erweiterung von [ ` InspectConfig `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/InspectConfig?hl=de)
um ` InfoTypeLimit ` kann jetzt die Anzahl der Übereinstimmungen pro `
InfoType ` begrenzt werden.

**FEATURE:** Durch die Erweiterung von [ ` inspect.operations.create `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/inspect.operations/create?hl=de)
um ` OperationConfig ` wird jetzt die Beschränkung der Anzahl der
Übereinstimmungen pro Datei, Cloud Datastore-Entität oder Datenbankzeile
unterstützt.

##  10\. August 2017

**FEATURE:** Durch Bereitstellen einer ` Table ` in [ ` ContentItem `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/ContentItem?hl=de)
wird jetzt das Durchsuchen und Entfernen strukturierter Daten in [ `
content.redact `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/content/redact?hl=de)
und [ ` content.inspect `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/content/inspect?hl=de)
unterstützt.

##  3\. August 2017

**FEATURE:** BigQuery kann jetzt mit [ ` inspect.operations.create `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/inspect.operations/create?hl=de)
gescannt werden.

**FEATURE:** Ergebnisse der Prüfung von BigQuery, Cloud Datastore und Cloud
Storage mit [ ` inspect.operations.create `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/inspect.operations/create?hl=de)
können jetzt in BigQuery gespeichert werden.

##  15\. Juni 2017

**FEATURE:** Das automatische Entfernen des gesamten Textes aus Bildern wird
jetzt unterstützt. Sie können jetzt auch benutzerdefinierte Farben zum Füllen
der Markierungsrahmen auswählen, wenn Sie mit [ ` content.redact `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/content/redact?hl=de)
Daten aus Bildern entfernen.

##  11\. Mai 2017

**FEATURE:** Das Filtern von [ Übereinstimmungen
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/InspectResult?hl=de#finding)
nach infoType und Wahrscheinlichkeit bei Verwendung von [ `
inspect.results.list `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/inspect.results.findings/list?hl=de)
wird jetzt unterstützt.

##  1\. Mai 2017

**FEATURE:** Ergebnisse der Prüfung von Cloud Datastore und Cloud Storage mit
[ ` inspect.operations.create `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/inspect.operations/create?hl=de)
können jetzt gespeichert werden. Die Ergebnisse werden in Cloud Storage
gespeichert.

##  23\. März 2017

**FEATURE:** Die automatische Entfernung von Übereinstimmungen in Bildern wird
jetzt unterstützt. Sie können jetzt mithilfe von [ ` content.redact `
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/content/redact?hl=de)
den [ Markierungsrahmen
](https://cloud.google.com/dlp/docs/reference/rest/v2beta1/InspectResult?hl=de#ImageLocation)
einer Übereinstimmung mit einer durchgehenden Farbe füllen.

##  9\. März 2017

**FEATURE:** Einführung der Cloud DLP API- **Betaversion** . Mit der DLP API
können Entwickler und Dateninhaber vertrauliche Elemente schnell und
skalierbar klassifizieren und sensible Daten so besser verstehen und
verwalten. Durchsuchen Sie kleine Texte und Bilder oder größere Datasets in
Cloud Storage und Cloud Datastore. Die Cloud DLP API ist derzeit als REST API
verfügbar.

