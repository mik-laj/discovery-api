#  Python 3 – Versionshinweise

Python [ 2.7
](https://cloud.google.com/appengine/docs/standard/python/release-notes?hl=de
"Diese Seite in der Python 2.7-Laufzeit ansehen") /  3.7  |  Java [ 8
](https://cloud.google.com/appengine/docs/standard/java/release-notes?hl=de
"Diese Seite in der Java 8-Laufzeit ansehen") / [ 11
](https://cloud.google.com/appengine/docs/standard/java11/

release-notes?hl=de "Diese Seite in der Java 11-Laufzeit ansehen") |  PHP [ 5
](https://cloud.google.com/appengine/docs/standard/php/release-notes?hl=de
"Diese Seite in der PHP 5-Laufzeit ansehen") / [ 7
](https://cloud.google.com/appengine/docs/standard/php7/

release-notes?hl=de "Diese Seite in der PHP 7-Laufzeit ansehen") |  [ Ruby
](https://cloud.google.com/appengine/docs/standard/ruby/

release-notes?hl=de "Diese Seite in der Ruby-Laufzeit ansehen") |  Go [ 1.9
](https://cloud.google.com/appengine/docs/standard/go/release-notes?hl=de
"Diese Seite in der Go 1.9-Laufzeit ansehen") / [ 1.11
](https://cloud.google.com/appengine/docs/standard/go111/

release-notes?hl=de "Diese Seite in der Go 1.11-Laufzeit ansehen") / [ 1.12
](https://cloud.google.com/appengine/docs/standard/go112/

release-notes?hl=de "Diese Seite in der Go 1.12-Laufzeit ansehen") |  [
Node.js ](https://cloud.google.com/appengine/docs/standard/nodejs/

release-notes?hl=de "Diese Seite in der Node.js-Laufzeit ansehen")

Zusätzlich zu den nachfolgenden Versionshinweisen finden Sie Informationen zu
bekannten Problemen auch in der [ Problemverfolgung
](https://issuetracker.google.com/issues?q=componentid%3A187191%2B&hl=de) .

Fügen Sie die URL dieser Seite Ihrem [ Feedreader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) hinzu, um die
neuesten Produktaktualisierungen zu erhalten.

##  30\. Juli 2019

  * Das Tool AppCfg und das ältere eigenständige App Engine SDK, die über die Dateien ` GoogleAppEngineLauncher.dmg ` , ` GoogleAppEngine.msi ` und ` google_appengine.zip ` bereitgestellt werden, sind jetzt veraltet. Google wird den Support am 30. Juli 2020 beenden. 
  * Die Funktionen des App Engine SDK werden ausschließlich über das [ Cloud SDK ](https://cloud.google.com/sdk/docs?hl=de) bereitgestellt. Weitere Informationen finden Sie unter [ Zum Cloud SDK migrieren ](https://cloud.google.com/appengine/docs/standard/java/sdk-gcloud-migration?hl=de) . 

##  18\. April 2019

  * App Engine ist jetzt in der Region ` asia-northeast2 ` (Osaka, Japan) verfügbar. 

##  15\. April 2019

  * App Engine ist jetzt in der Region ` europe-west6 ` (Zürich, Schweiz) verfügbar. 

##  9\. April 2019

  * [ Cloud Tasks ](https://cloud.google.com/tasks/docs?hl=de) ist jetzt allgemein verfügbar und kann verwendet werden, um Aufgaben einzurichten, die außerhalb von Nutzeranfragen asynchron ausgeführt werden sollen. 

  * [ Serverloser VPC-Zugriff ](https://cloud.google.com/appengine/docs/standard/python3/connecting-vpc?hl=de) ist jetzt in der Betaversion verfügbar. Der serverlose VPC-Zugriff ermöglicht Ihrer Anwendung, eine Verbindung zu internen Ressourcen in Ihrem VPC-Netzwerk herzustellen, z. B. Compute Engine-VM-Instanzen, Cloud Memorystore-Instanzen und mehr. 

##  4\. April 2019

  * Die Python 3-Laufzeit wurde auf Version 3.7.3 aktualisiert. 

##  11\. Januar 2019

  * Die Python 3-Laufzeit wurde auf Version 3.7.2 aktualisiert. 

##  14\. Dezember 2018

  * Die [ Python 3.7-Laufzeit ](https://cloud.google.com/appengine/docs/standard/python3?hl=de) für die App Engine-Standardumgebung ist jetzt allgemein verfügbar. 

##  12\. Dezember 2018

  * Das Python SDK wurde auf Version 1.9.81 aktualisiert. 
  * Alle Anwendungen wurden auf BSD-Netzwerk-Sockets umgestellt. Anwendungen müssen nicht angepasst werden. 
  * Die [ Sockets API ](https://cloud.google.com/appengine/docs/standard/python/sockets?hl=de) ist jetzt allgemein verfügbar. 

##  16\. November 2018

  * nginx ist jetzt der Standardwebserver. Anwendungen müssen nicht angepasst werden. 

##  31\. Oktober 2018

  * Die Python 3-Laufzeit wurde auf Python Version 3.7.1 aktualisiert. 
  * Die Python 3-Laufzeit unterstützt rekursive Einträge in der Datei ` requirements.txt ` . 

##  22\. Oktober 2018

  * App Engine ist jetzt in der Region ` asia-east2 ` (Hongkong) verfügbar. 

##  8\. August 2018

  * Die [ Python 3.7-Laufzeit ](https://cloud.google.com/appengine/docs/standard/python3?hl=de) für die App Engine-Standardumgebung befindet sich jetzt in der Betaphase. 
  * Eine Liste der [ Unterschiede zwischen Python 2.7- und Python 3.7-Laufzeiten ](https://cloud.google.com/appengine/docs/standard/python3/python-differences?hl=de) ist verfügbar. 

##  10\. Juli 2018

  * App Engine ist jetzt in der Region ` us-west2 ` (Los Angeles) verfügbar. 

##  2\. Juli 2018

In der [ Konfiguration der automatischen Skalierung
](https://cloud.google.com/appengine/docs/standard/python3/config/appref?hl=de#scaling_elements)
wurde ein Fehler behoben, bei dem App Engine wahllos Instanzen herunterfuhr,
wenn die Einstellung ` max_instances ` verwendet wurde.

##  15\. Mai 2018

  * Schrittweise Einführung eines Upgrades auf das automatische Skalierungssystem abgeschlossen: 
    * Verbesserte Effizienz, die generell dazu führt, dass die Instanzkosten für viele Nutzer bis zu 6 % und die _Ladeanfragen_ bis zu 30 % sinken. Ladeanfragen sind die erste Anfrage an eine neue Instanz. 
    * Mit der neuen Einstellung für die maximale Instanzzahl können Sie die Gesamtzahl der zu planenden Instanzen begrenzen. 
    * Mit der neuen Einstellung für die Mindestanzahl der Instanzen können Sie angeben, wie viele Instanzen für die Anwendung mindestens weiterhin ausgeführt werden sollen. 
    * Mit der neuen Einstellung für die CPU-Zielauslastung können Sie das Verhältnis zwischen Latenz und Kosten optimieren. 
    * Mit der neuen Einstellung für den Zieldurchsatz können Sie optimieren, ab welcher Anzahl gleichzeitiger Anfragen neue Instanzen gestartet werden. 
    * Keine residenten Instanzen bei der automatischen Skalierung mehr. Wenn Sie zuvor die Einstellung ` min_idle_instances ` verwendet haben, wurden die Mindestzahl der inaktiven Instanzen in der Cloud Console früher als _Resident_ und die verbleibenden Instanzen als _Dynamisch_ gekennzeichnet. Im neuen Planer sind alle Instanzen für die automatische Skalierung als _Dynamisch_ kennzeichnet. Das grundlegende Verhalten ähnelt jedoch weiterhin dem bisherigen Verhalten. Wenn Sie ` min_idle_instances ` verwenden und Aufwärmanfragen aktivieren, wird auch in Zeiten ohne Traffic mindestens die festgelegte Anzahl dynamischer Instanzen ausgeführt. 
    * Weitere Informationen finden Sie in der [ Dokumentation zur automatischen Skalierung ](https://cloud.google.com/appengine/docs/standard/python3/config/appref?hl=de#scaling_elements) . 

##  14\. Dezember 2017

  * Verbesserte Dokumentation der Zugriffssteuerung zum Bereitstellen von Anwendungen mit IAM-Rollen und Dienstkonten: 

    * [ Vordefinierte App Engine-Rollen ](https://cloud.google.com/appengine/docs/standard/python3/access-control?hl=de#predefined_app_engine_roles)
    * [ Bereitstellung mit IAM-Rollen ](https://cloud.google.com/appengine/docs/standard/python3/granting-project-access?hl=de#deploying_using_iam_roles)
    * [ Erforderliche Berechtigungen ](https://cloud.google.com/appengine/docs/admin-api/access-control?hl=de#required_permissions)

##  31\. Oktober 2017

  * App Engine ist jetzt in der Region ` asia-south1 ` (Mumbai, Indien) verfügbar. 

##  11\. Oktober 2017

  * Ankündigung der allgemeinen Verfügbarkeit der [ App Engine-Firewall ](https://cloud.google.com/appengine/docs/standard/python3/creating-firewalls?hl=de)

##  13\. September 2017

  * Sie können jetzt verwaltete Zertifikate verwenden, um SSL zu Ihrer benutzerdefinierten Domain hinzuzufügen. Sobald Sie Ihrer Anwendung die benutzerdefinierte Domain zugeordnet haben, stellt App Engine automatisch ein SSL-Zertifikat bereit, verwaltet die Aktualisierung, bevor es abläuft, und widerruft es, wenn Sie die benutzerdefinierte Domain entfernen. Verwaltete Zertifikate befinden sich in der Betaphase. Weitere Informationen finden Sie unter [ Benutzerdefinierte Domains mit SSL sichern ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=de) . 

  * Wenn Sie eine vorhandene Domainzuordnung und ein SSL-Zertifikat haben, funktioniert die Domain weiterhin wie erwartet. Sie können auch ein [ Upgrade auf verwaltete SSL-Zertifikate ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=de#updating_to_managed_ssl_certificates) durchführen. 

  * Die ` gcloud ` -Befehle und die Admin API-Methoden zum [ Zuordnen benutzerdefinierter Domains ](https://cloud.google.com/appengine/docs/standard/python3/mapping-custom-domains?hl=de) sind jetzt allgemein verfügbar. Dazu gehören [ ` gcloud domains verify ` ](https://cloud.google.com/sdk/gcloud/reference/domains?hl=de) und [ ` apps.authorizedDomains.list ` ](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.authorizedDomains/list?hl=de) . Wenn Sie jedoch verwaltete SSL-Zertifikate einsetzen möchten, verwenden Sie die Betabefehle und -methoden, die unter [ Benutzerdefinierte Domains mit SSL sichern ](https://cloud.google.com/appengine/docs/standard/python3/securing-custom-domains-with-ssl?hl=de) aufgeführt sind. 

##  5\. September 2017

  * App Engine ist jetzt in der Region ` southamerica-east1 ` (São Paulo, Brasilien) verfügbar 

##  1\. August 2017

  * App Engine ist jetzt in der Region ` europe-west3 ` (Frankfurt, Deutschland) verfügbar. 

##  18\. Juli 2017

  * App Engine ist jetzt in der Region ` australia-southeast1 ` (Sydney, Australien) verfügbar 

##  6\. Juni 2017

  * App Engine ist jetzt in der Region ` europe-west2 ` (London) verfügbar. 
  * Sie können jetzt mit den Betafunktionen in der Admin API und im ` gcloud ` -Befehlszeilentool [ benutzerdefinierte Domains und SSL-Zertifikate erstellen und verwalten ](https://cloud.google.com/appengine/docs/standard/python3/mapping-custom-domains?hl=de) . 

##  9\. Mai 2017

  * App Engine ist jetzt in der Region ` us-east4 ` (North Virginia, USA) verfügbar 

##  27\. Oktober 2016

  * Die Channel- und XMPP-Dienste sind [ veraltet ](https://cloud.google.com/appengine/docs/deprecations?hl=de) . Diese Dienste werden am 31. Oktober 2017 eingestellt. 

##  1\. August 2016

**Hinweise zur Admin API**

  * Version 1 der [ Admin API ](https://cloud.google.com/appengine/docs/admin-api?hl=de) ist jetzt allgemein verfügbar. 

##  1\. August 2016 – Version 1.9.42

**Hinweise zur Python 3.7-Laufzeit**

  * Dieser Release enthält kein neues Python 3.7 SDK. Python 3.7-Nutzer sollten weiterhin das SDK 1.9.40 verwenden. 

##  18\. Juli 2016 – Version 1.9.40

  * Version 1.9.39 wurde übersprungen. 

  * LeaseTasksByTag-Anfragen sind auf 25 Anfragen pro Sekunde beschränkt 

  * Für Server- und Clientfehler zeigt das App Engine-Dashboard nun die Statusfehler pro URL genauer an. 

  * In der GCP Console gibt es eine neue [ App Engine-Anleitung ](https://console.cloud.google.com/start/appengine?hl=de) . Wählen Sie die gewünschte Sprache aus und starten Sie die interaktive Anleitung direkt in der Console. 

  * Das Limit für Cronjobs wurde auf 250 erhöht 

##  1\. Juli 2016

**Cloud Datastore**

  * Die neuen [ Cloud Datastore-Preise ](https://cloud.google.com/appengine/pricing?hl=de#costs-for-datastore-calls) gelten ab jetzt. 

##  25\. Mai 2016 – Version 1.9.38

  * Für den Fehler, der von URL Fetch für eine Anfrage an einen Port außerhalb der zulässigen Bereiche (80–90, 440–450, 1024–65535) zurückgegeben wird, wird jetzt immer wie dokumentiert ` INVALID_URL ` angezeigt. 

**Cloud Datastore**

  * Beim Durchführen eines Commits für eine gruppenübergreifende Transaktion sind die für neue oder aktualisierte Entitäten zurückgegebenen Versionsnummern identisch. Bisher hatten Entitäten in einer Gruppe, für die ein Commit als Teil einer gruppenübergreifenden Transaktion durchgeführt wurde, die gleiche Versionsnummer, Entitäten in verschiedenen Gruppen aber möglicherweise unterschiedliche Versionsnummern. Mit dieser Änderung wird gewährleistet, dass alle neuen und aktualisierten Entitäten unabhängig von ihrer Entitätengruppe eine identische Versionsnummer haben, wenn für sie als Teil einer gruppenübergreifenden Transaktion ein Commit durchgeführt wird. Wie bisher erhalten Entitäten, die nicht aktualisiert werden, keine neue Versionsnummer. 

##  4\. Mai 2016 – Version 1.9.37

Enthält allgemeine Fehlerbehebungen und Verbesserungen.

##  2\. Mai 2016

**Flexible App Engine-Umgebung**

  * Die [ Ruby-Laufzeit ](https://cloud.google.com/appengine/docs/flexible/ruby?hl=de) ist jetzt für die flexible App Engine-Umgebung verfügbar. 

##  18\. April 2016 – Version 1.9.36

Als Reaktion auf Nutzeranfragen unterstützt die App Engine Users API jetzt wie
die anderen App Engine-Module IAM-Rollen und Gruppenerweiterungen. Dadurch
gilt jeder Projektinhaber, -bearbeiter oder -betrachter bzw. App Engine-
Administrator für die Users API als "Admin", unabhängig davon, ob dem Nutzer
die Rolle direkt oder über die Mitgliedschaft in einer Gruppe zugewiesen
wurde. *In diesem Release werden, falls vorhanden, Fehlerdetails in den
Fehlermeldungen für den Ausnahmetyp "OverQuota" dokumentiert.

##  24\. März 2016 – Version 1.9.35

  * Die verwalteten VMs von App Engine wurden in [ flexible App Engine-Umgebung ](https://cloud.google.com/appengine/docs/flexible?hl=de) umbenannt. 
  * Nachverfolgungszeitstempel stimmen jetzt mit Logzeitstempeln überein. 

##  4\. März 2016 – Version 1.9.34

  * Das Standardkontingent für das Abrufen von URLs für abgerechnete Anwendungen wurde erhöht. Ausführliche Informationen finden Sie auf der [ Seite "Kontingente" ](https://cloud.google.com/appengine/docs/quotas?hl=de#UrlFetch) . 

##  17\. Februar 2016 – Version 1.9.33

  * Der URL-Pfad "/form" ist nun zulässig und wird an Anwendungen weitergeleitet. Bisher wurde dieser Pfad blockiert. 

##  3\. Februar 2016 – Version 1.9.32

  * Auswahlmöglichkeiten zum Erstellen von Containern für verwaltete VMs 

Mit den Befehlen ` gcloud preview app deploy ` (und ` mvn gcloud:deploy ` )
können Sie Ihre Artefakte auf unsere Server hochladen und einen Container zur
Bereitstellung Ihrer Anwendung in der verwalteten VM-Umgebung erstellen.

Für das Erstellen des Container-Image per Fernzugriff gibt es zwei
Möglichkeiten. Standardmäßig wird der Container auf einer temporären
virtuellen Compute Engine-Maschine erstellt, auf der Docker installiert ist.
Alternativ können Sie den Dienst [ Cloud Build
](https://cloud.google.com/cloud-build/docs?hl=de) verwenden. Führen Sie dazu
diese Schritte aus:

    1. [ Aktivieren Sie die Cloud Build API ](https://support.google.com/cloud/answer/6158841?hl=de) für Ihr Projekt. 
    2. Rufen Sie den Befehl ` gcloud config set app/use_cloud_build True ` auf. Dadurch wird beim Aufruf von ` gcloud preview app deploy ` immer der Dienst verwendet. Mit dem Befehl ` gcloud config set app/use_cloud_build False ` können Sie zum Standardverhalten zurückzukehren. 

##  14\. Januar 2016 – Version 1.9.31

App Engine unterstützt jetzt Google Groups: Wenn eine Google Group einem
Projekt als Mitglied hinzugefügt wird, erhalten die anderen Gruppenmitglieder
Zugriff auf App Engine. Wenn eine Google Group z. B. ein Mitbearbeiter bei
einem Projekt ist, haben jetzt alle Gruppenmitglieder Mitbearbeiterzugriff auf
die App Engine-Anwendung.

##  30\. November 2015 – Version 1.9.30

Header für Requests in Push-Warteschlangen, die für Aufgaben von
Aufgabenwarteschlangen ohne Nutzlast erstellt wurden, enthalten jetzt einen
Content-Length-Eintrag "0". Bisherige Headers für derartige Requests
enthielten keinen Content-Length-Eintrag.

##  30\. November 2015 – Version 1.9.29

  * Die Tiefe der Warteschlange wird für nicht vorhandene Warteschlangen, für zum Löschen markierte Warteschlangen und beim Ausfall von Warteschlangentabellen nicht mehr berechnet und gespeichert. 
  * Für Entwickler, die die [ Endpoints API ](https://cloud.google.com/appengine/docs/standard/python/endpoints/create_api?hl=de#defining_the_api_endpointsapi) verwenden, wurde zum @Api-Hinweis ein identifizierbarer boolescher Parameter hinzugefügt, mit dem Nutzer die API-Erkennung deaktivieren können. Bei Verwendung dieser Funktion können einige Clientbibliotheken (z. B. JavaScript) und API Explorer nicht mehr verwendet werden, da sie auf der Erkennung basieren. 

##  29\. Oktober 2015 – Version 1.9.28

Die Prospective Search API, die am 14. Juli 2015 eingestellt wurde, ist jetzt
auf vorhandene Nutzer beschränkt. Sie wird am 1. Dezember 2015 vollständig
abgeschaltet. *Verbesserte Genauigkeit von Geo-Filtern in Suchabfragen.

##  25\. September 2015 – Version 1.9.27

Anwendungen, die neu für die Abrechnung aktiviert werden, haben jetzt
standardmäßig ein unbegrenztes Tagesbudget statt eines maximalen Tagesbudgets
von 0 $. Dies verhindert unerwünschte Ausfälle aufgrund von
Budgetüberschreitungen. Zur Festlegung einer Obergrenze für die täglichen
Kosten Ihrer Anwendung geben Sie nach der Aktivierung der Abrechnung ein
Budget in den [ App Engine-Einstellungen
](https://console.cloud.google.com/project/_/appengine/settings?hl=de) an.
Weitere Informationen finden Sie unter [ Tagesbudget festlegen
](https://cloud.google.com/appengine/docs/developers-
console?hl=de#setting_a_daily_budget) .

Datastore

  * Fehlerkorrektur: Wiederholte numerische Facetten sind jetzt erlaubt. 
  * Die Facettensuche ist jetzt eine GA-Funktion. 

##  27\. August 2015 – Version 1.9.26

  * oauth2client-Bibliothek wurde auf Version [ 1.4.2 ](https://github.com/google/oauth2client/blob/master/CHANGELOG.md) aktualisiert. 
  * Das Menü "Mit Kontext anzeigen" wurde MVM-Anwendungslogs mit "thread_id" oder "request_id" als Feld im Logeintrag hinzugefügt. Dadurch können Sie Anwendungslogs auf der Basis dieser Felder sortieren. 
  * Anwendungen können für die aktuelle Arbeitslast bereitgestellt werden. Es lässt sich auch eine elastische Bereitstellung auf Basis von VM- und Anwendungsmesswerten konfigurieren. 
  * Auf die Remote-API kann jetzt mithilfe von OAuth2-Anmeldedaten unter https://developers.google.com/identity/protocols/application-default-credentials zugegriffen werden. 
  * Sie können RequestPayloadTooLargeException für URLFetch-Requests mit zu großen Nutzlasten verwenden. 

##  14\. August 2015 – Version 1.9.25

  * PyAMF Version 0.7.2 (Beta) wurde hinzugefügt. 
  * Menüs in der Admin-Konsole leiten an die GCP Console weiter. Ausgewählte Dienste wie die Admin-Logs sind weiterhin in der Admin-Konsole verfügbar. 
  * Datastore lässt jetzt Eigenschaften zur Darstellung einer leeren Liste zu. 
  * Fehlgeschlagene Aufgaben in Warteschlangen, die mit einem "retry_limit" von Null konfiguriert sind, werden nicht mehr wiederholt. 

