#  Versionshinweise

Auf dieser Seite werden die Produktionsaktualisierungen von Cloud Code
dokumentiert. Hier finden Sie Ankündigungen neuer oder aktualisierter
Funktionen sowie Informationen zu Fehlerkorrekturen, bekannten Problemen und
eingestellten Funktionen.

Die neuesten Updates finden Sie auch auf der [ Seite "GitHub-Versionshinweise"
](https://github.com/GoogleCloudPlatform/cloud-code-
intellij/blob/master/CHANGELOG.md) .

Die neuesten Produktaktualisierungen für Google Cloud finden Sie auf der Seite
mit den [ Google Cloud-Versionshinweisen ](https://cloud.google.com/release-
notes?hl=de) .

Für neueste Produktaktualisierungen können Sie die URL der Seite in den [
Feedreader ](https://wikipedia.org/wiki/Comparison_of_feed_aggregators)
einfügen oder die Feed-URL direkt hinzufügen: `
https://cloud.google.com/feeds/cloud-code-for-intellij-release-notes.xml ` .

##  18.5.1

Cloud Code ist jetzt in PyCharm (Community und Professional) verfügbar.
Durchsuchen Sie Ihre Cloud Storage-Buckets und interagieren Sie mit Cloud
Source Repositories von PyCharm. Weitere IDEs folgen demnächst.

###  Hinzugefügt

  * Überarbeitetes Plug-in, mit dem sprachunabhängige Funktionen wie Cloud Storage und Cloud Source Repositories neben IDEA auch in anderen JetBrains IDEs verfügbar sind. [ 1896 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1896)

###  Geändert

  * Das verwaltete Cloud SDK wird nach der ersten manuellen Deaktivierung nicht mehr bei jedem IDE-Ladevorgang installiert. [ 2113 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/2113)

###  Behoben

  * Eine Ausnahme in 2018.2 EAP wurde behoben. [ 2124 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/2124)

##  18.4.1

###  Hinzugefügt

  * Verwalten Sie das Cloud SDK automatisch mit dem Google Cloud Tool-Plug-in – einschließlich Download, Installation und Aktualisierungen. Ein manuelles Herunterladen des SDK ist nicht mehr erforderlich. [ 673 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/673)
  * Vermeiden Sie dank integrierter Google Cloud Java BOM-Unterstützung Versionskonflikte aufgrund von Abhängigkeiten. Die BOM wird automatisch zusammen mit Google-Clientbibliotheken hinzugefügt. Überprüfungen der pom.xml tragen zusätzlich dazu bei, Versionskonflikte aufgrund von Abhängigkeiten zu vermeiden. [ 1921 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1921)
  * Erforderliche Umgebungsvariablen für den lokalen Zugriff auf Google Cloud APIs werden lokalen App Engine-Ausführungskonfigurationen automatisch hinzugefügt. [ 1917 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1917)

##  18.3.2

  * Es wurde ein Fehler behoben, der bei der IntelliJ IDEA-Version 2017.2 und früheren Versionen zu Initialisierungsfehlern führte. [ 1972 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1972)

##  18.3.1

###  Hinzugefügt

  * Es wurde die Möglichkeit hinzugefügt, Dienstkonten zu erstellen und Dienstkontoschlüssel aus dem IDE-Clientbibliotheksworkflow herunterzuladen. [ 1808 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1808)

###  Behoben

  * Das Problem, dass in einigen Fällen aufgrund einer fehlenden ` web.xml ` keine ` appengine-web.xml ` generiert wurde, wurde behoben. [ 1903 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1903)

##  18.2.1

###  Hinzugefügt

  * Es wurde die Google Cloud Java-Clientbibliothekserkennung und -erweiterung von der IDE hinzugefügt. [ 1806 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1806)
  * Es besteht jetzt die Möglichkeit, Google Cloud APIs über die IDE zu aktivieren. [ 1807 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1807)

###  Geändert

  * Die Nutzerfreundlichkeit der Cloud-Projektauswahl wurde deutlich verbessert. [ 1719 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1719)
  * Die Cloud-Projektauswahl wurde aktualisiert, sodass die letzte Auswahl gespeichert und vorbelegt wird. [ 1812 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1812)

###  Behoben

  * Das Fehlen der lokalen Standard-Ausführungsartefakte von App Engine wurde behoben. [ 1625 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1625)

##  18.1.1

###  Behoben

  * Fehler im Error Reporting-Mechanismus behoben. [ 1842 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1842)

##  17.12.2

###  Behoben

  * Fehler bei der Konfiguration der Analyseeigenschaften für die Analyse behoben. [ 1773 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1773)

##  17.12.1

Das Plug-in des Google-Kontos wurde in das Cloud Tools-Plug-in integriert und
ist keine separate Installation mehr. Wenn Sie bisher das Plug-in für
Kontotools installiert hatten, folgen Sie der neuen Dialogaufforderung, um es
zu entfernen. Starten Sie die IDE neu, damit keine Probleme auftreten.

###  Behoben

  * Es wurde ein Speicherfehler behoben, der bei Eingaben und Suchvorgängen für mehrere Projekte in der Cloud-Projektauswahl aufgetreten ist. [ 1742 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1742)

###  Geändert

  * Das Plug-in des Google-Kontos ist jetzt in das Google Cloud Tools-Plug-in integriert. Das Google-Konto-Plug-in muss nicht mehr separat installiert werden. [ 1735 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1735)

##  17.11.1

###  Hinzugefügt

  * Google Cloud Storage wurde in IntelliJ integriert. Sie können jetzt Ihre Buckets durchsuchen und deren Inhalt ansehen, ohne die IDE zu verlassen. [ 1696 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1696)
  * Such- und Filterfunktionen in der Cloud-Projektauswahl. [ 1660 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1660)
  * Das Menü "Tools" enthält jetzt die neue Option "Add App Engine framework support", um eine weitere Möglichkeit zu bieten, ein Projekt mit App Engine-Unterstützung zu versehen. [ 1685 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1685)

###  Behoben

  * Die Statusmeldung in der App Engine-Regionsanzeige wurde für den Fall korrigiert, dass kein Cloud-Projekt ausgewählt wurde. [ 1607 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1607)

##  17.9.2

Java 8 ist in der App Engine-Standardumgebung jetzt [ allgemein verfügbar
](https://cloudplatform.googleblog.com/2017/09/Java-8-on-App-Engine-Standard-
environment-is-now-generally-available.html) .

###  Geändert

  * Der neue Assistent für App Engine-Standardprojekte wurde so aktualisiert, dass standardmäßig Java 8-Anwendungen generiert werden. [ 1641 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1641)

##  17.9.1

###  Hinzugefügt

  * Es besteht jetzt die Möglichkeit, den Namen des bereitgestellten Artefakts für flexible App Engine-Bereitstellungen zu ändern. [ 1610 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1610)

###  Geändert

  * In Konfigurationen für flexible App Engine-Bereitstellungen wird das Artefakt jetzt standardmäßig im vorliegenden Zustand bereitgestellt, ohne es in ` target.jar ` oder ` target.war ` umzubenennen. [ 1151 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1151)
  * Der Name des Platzhalterartefakts in generierten Dockerfile-Vorlagen wurde geändert, um deutlicher darauf hinzuweisen, dass er vom Nutzer aktualisiert werden muss. [ 1648 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1648)
  * In Konfigurationen für App Engine-Standardbereitstellungen ist die Option "Update dos, dispatch, cron, queues, and datastore indexes" (Indexe für dos, dispatch, cron, queues und datastore aktualisieren) jetzt standardmäßig aktiviert. [ 1613 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1613)
  * In nativen Projekten mit Unterstützung für Endpoints Frameworks für App Engine wird jetzt Endpoints Version 2 verwendet. [ 1612 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1612)

###  Behoben

  * Der Fehler ` Deployment source not found ` bei Bereitstellung von Maven-Artefakten wurde behoben. [ 1220 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1220)
  * Die Größe des Nutzersymbols in HiDPI-Anzeigen wurde korrigiert. [ 1633 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1633)
  * Das Problem mit dem Downgrade des Plug-ins in IDEA 2017.3 EAP wurde behoben. [ 1631 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1631)

##  17.8.2

###  Behoben

  * Das Problem mit der Anzeige des Fehlers "Error: invalid_scope" bei der Anmeldung beim Google-Konto wurde behoben. [ 1598 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1598)

##  17.8.1

###  Hinzugefügt

  * Dem Menü "Google Cloud Tools" wurde ein Link für Feedback und zum Melden von Problemen hinzugefügt. [ 1560 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1560)

###  Geändert

  * Nutzer können jetzt Ausführungskonfigurationen für Bereitstellungen speichern, die teilweise fertiggestellt sind oder einen Fehlerstatus aufweisen. [ 1407 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1407)

###  Behoben

  * Der Konflikt mit der registrierten Docker-Sprache wurde behoben, der bei gleichzeitiger Ausführung des Plug-ins mit dem .ignore-Plug-in Probleme verursachte. [ 1535 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1535)
  * Die NPE beim Parsen der Haltepunkt-Zeitstempel von Cloud Debugger wurde behoben. [ 1537 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1537)
  * EAR wurde als zulässiger App Engine-Artefakttyp für Ausführungen auf dem lokalen Entwicklungsserver entfernt. [ 1190 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1190)
  * Bereitstellungen werden jetzt in mehreren IDE-Fenstern angezeigt. [ 1432 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1432)
  * Der Versuch, eine schreibgeschützte Sammlung zu ändern, führt nicht mehr zu einem Absturz. [ 1571 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1571)

##  17.6.2

###  Behoben

  * Die NPE wurde behoben, die immer dann aufgetreten ist, wenn bei der Konfiguration eines lokalen Entwicklungsservers das Standardattribut gefehlt hat. [ 1525 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1525)

##  17.6.1

###  Hinzugefügt

  * Flexibles App Engine-Attribut mit ` app.yaml ` und Dockerfile-Konfiguration. [ 1514 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1514)
  * Die Unterstützung des flexiblen App Engine-Frameworks wird erkannt. [ 1277 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1277)

###  Geändert

  * Der Nutzer hat jetzt die Möglichkeit, ein Docker-Verzeichnis statt nur eines Dockerfiles für flexible Bereitstellungen anzugeben. [ 1304 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1304)
  * Dem Nutzer wird im Bereitstellungsdialogfeld (sowohl flexible Umgebung als auch Standardumgebung) aktualisierter Inhalt angezeigt. [ 1477 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1477)

###  Behoben

  * Die Größe des Google-Avatars wurde in HiDPI-Anzeigen korrigiert. [ 1391 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1391)

##  17.2.5_2017

###  Hinzugefügt

  * Umgebungsvariablen in der lokalen App Engine-Standardausführungskonfiguration werden jetzt an den Entwicklungsserver übergeben. [ #1364 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1364)
  * Die in appengine-web.xml konfigurierten Umgebungsvariablen werden jetzt berücksichtigt und an den Entwicklungsserver übergeben. [ #377 ](https://github.com/GoogleCloudPlatform/appengine-plugins-core/issues/377)

##  17.2.4_2017

###  Hinzugefügt

  * Es wurde ein Kästchen zur Bereitstellung aller App Engine-Konfigurationsdateien während der Dienstbereitstellung hinzugefügt. [ #1346 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1346)

##  17.2.3_2017

###  Geändert

  * Das Flag zum Löschen des Datenspeichers wurde aus der Konfiguration des lokalen App Engine-Standardentwicklungsservers entfernt, da die aktuelle Version des Servers dieses nicht unterstützt. ( [ #1345 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1345) ) 

##  17.2.2_2017

###  Behoben

  * Ungültige Java-Laufzeitumgebung (JRE) beim Bereitstellen einer App Engine-Standardanwendung. ( [ #1316 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1316) ): 
    
        > Unable to stage app: Cannot get the System Java Compiler. Please use a JDK, not a JRE.
    

##  17.2.1

Frohes Neues Jahr an alle Cloud Code-Nutzer! Der erste Release dieses Jahres
ist in erster Linie ein Wartungsrelease. Falls Sie Authentifizierungsprobleme
bei Verwendung von Cloud Source Repositories und unserem Plug-in haben, sehen
Sie sich [ diese mögliche Lösung an
](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1174) .

Im Folgenden eine Liste der sichtbaren Änderungen:

###  Hinzugefügt

  * Unterstützung für mehrere Cloud Source Repositories für ein einzelnes GCP-Projekt. ( [ #1024 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1024) ) 
  * App Engine-Initialisierung und -Regionsauswahl. ( [ #1232 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1232) ) 

###  Behoben

  * Beim Anhalten von "dev_appserver" unter Windows tritt dieser Fehler auf: ` com.intellij.execution.ExecutionException ` . ( [ #1215 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1215) ) 
  * Der neue Assistent für App Engine-Standardprojekte sollte die Datei web.xml mit Servlet 2.5 generieren. ( [ #1194 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1194) ) 
  * Das Kästchen "Clear datastore" für den lokalen App Engine-Standardserver funktioniert nicht. ( [ #1188 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1188) ) 
  * Projekte, die gelöscht werden sollen, werden nicht mehr in der Projektauswahl angezeigt. ( [ #1119 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1119) ) 

Ausführliche Informationen finden Sie auf der Seite für unser [
Meilensteinrelease 17.2 ](https://github.com/GoogleCloudPlatform/google-cloud-
intellij/milestone/19?closed=1) .

##  16.11.6

###  Hinzugefügt

  * Erweiterter Google Cloud Tools-Menüpunkt mit verschiedenen Aktionsverknüpfungen. ( [ #1061 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1061) ). 
  * Prüfung auf die erforderliche Mindestversion des Cloud SDKs. ( [ #1051 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1051) ). 
  * Automatisches Erstellen aller relevanten Ausführungskonfigurationen für App Engine-Standardanwendungen. ( [ #1063 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1063) ). 
  * Das App Engine-Framework ist im neuen Projektassistenten dem Web-Framework untergeordnet. ( [ #1065 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1065) ). 

###  Behoben

  * Einzelne Bereitstellungsquellen werden jetzt im Bereich für die Anwendungsserverbereitstellung als separate Positionen angezeigt. ( [ #821 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/821) ). 
  * Validierung ungültiger Cloud SDK-Pfade unter Windows. ( [ #1091 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1091) ). 

##  16.10.5

WICHTIG: Für dieses Plug-in ist Version 133.0.0 des Cloud SDKs erforderlich,
damit der lokale Entwicklungsserver korrekt mit dem neuesten Java 8 SDK
ausgeführt wird. Führen Sie ` gcloud components update ` über Ihre Shell aus,
damit der neueste Cloud SDK-Release installiert ist.

###  Behoben

  * Im Fehlerbehebungsmodus des lokalen Entwicklungsservers treten keine Probleme mehr auf, wenn während der Ausführung des Servers Änderungen vorgenommen werden. ( [ #972 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/972) ) 
  * Der Hinweis auf einen ungültigen Cloud SDK-Pfad für den Entwicklungsserver wurde verständlicher formuliert. ( [ #1043 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1043) ) 
  * Die Namen von Ausführungskonfigurationen wurden mit dem Präfix "Google…" aktualisiert. ( [ #1021 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/1021) ) 

##  16.10.1

  * Beachten Sie, dass das Versionierungsschema in JJ.MM.i geändert wird. Wir planen einen monatlichen Releaserhythmus, um die Updateintervalle zu verkürzen. Außerdem wurde die Bezeichnung "Beta" entfernt. 
  * ACHTUNG: Der lokale App Engine-Entwicklungsserver funktioniert mit den neuesten JDK 8-Releases nicht mehr. ( [ #920 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/920) ). Dieses Problem sollte im nächsten App Engine SDK-Release, der bald verfügbar ist, behoben sein. 

###  Hinzugefügt

  * Import von App Engine-Standardbibliotheken im Attribut und Projektassistenten. ( [ #866 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/866) ) 
  * In App Engine-Standardanwendungen, die die Java 8-Sprachebene verwenden, wird darauf hingewiesen, dass Sprachebene 7 zu verwenden ist. [ 966 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/966)

###  Geändert

  * Die Labels und Symbole für die Ausführungskonfiguration wurden geändert. (Cloud Debugger heißt jetzt Cloud Debugger) ( [ #936 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/936) ) 

###  Behoben

  * Das Problem mit dem Fehlerbehebungsmodus des lokalen Entwicklungsservers wurde behoben. ( [ #928 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/928) ) 
  * Fehlgeschlagene Bereitstellung in flexibler Umgebung unter Windows 10. ( [ #937 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/937) ) 
  * Der Object Inspector in Cloud Debugger funktioniert wieder. ( [ #929 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/929) ) 
  * Snapshot-Zeitstempel von Cloud Debugger verursachen eine NPE. ( [ #919 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/919) ) 

##  1.0-beta – 14.09.2016

###  Hinzugefügt

  * Unterstützung der App Engine-Standardumgebung ( [ #767 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/issues/767) ) 
  * Zusätzliche Felder in der Bereitstellungskonfiguration ( [ #868 ](https://github.com/GoogleCloudPlatform/google-cloud-intellij/pull/868) ) 

##  0.9.7.5-beta – 29.08.2016

###  Hinzugefügt

  * Prüfung mit einer Aufforderung zum Hinzufügen eines neuen Nutzers, falls die jeweilige Bereitstellung für den authentifizierten Nutzer nicht zulässig ist. ( [ 837 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/837) ) 

##  0.9.6-beta – 23.06.2016

###  Hinzugefügt

  * Unterstützung von Bereitstellungen in der flexiblen App Engine _-Kompatibilitätsumgebung_ . ( [ #720 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/720) ) 
  * Unterstützung von Bereitstellungen in der App Engine-Standardumgebung. ( [ #665 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/665) ) 
  * Prüfung auf Kompatibilität des Cloud Tools-Plug-ins mit dem Konto-Plug-in. ( [ #651 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/650) ) 

###  Geändert

  * Das Eingabefeld für die Version befindet sich jetzt im Dialogfeld für die Bereitstellungskonfiguration auf oberster Ebene. ( [ #639 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/639) ) 

##  0.9.4-beta – 20.04.2016

###  Hinzugefügt

  * Menüpunkt für die Bereitstellung in der flexiblen App Engine-Umgebung im Menü "Tools". ( [ #635 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/635) ) 
  * Unterstützung für Maven-basierte Projekte als Quellen für Bereitstellungen in der flexiblen App Engine-Umgebung. ( [ #600 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/600) ) 

###  Geändert

  * Die Ausführung der Bereitstellung in der flexiblen App Engine-Umgebung kann abgebrochen werden. Dazu müssen Sie die Verbindung zu unserem App Engine-Anwendungsserver trennen. ( [ #581 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/581) ) 
  * Das in der flexiblen App Engine-Umgebung generierte Dockerfile und die Datei ` app.yaml ` werden jetzt standardmäßig am empfohlenen Speicherort in einem von Maven strukturierten Java-Projekt abgelegt. ( [ #575 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/575) ) 

###  Behoben

  * Anmeldefehler, der dazu führen konnte, dass beim Hinzufügen eines Nutzers kein aktiver Nutzer ausgewählt wurde. ( [ #644 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/644) ) 
  * Möglicher Fehler beim Rückgängigmachen einer App Engine-Bereitstellung. ( [ #599 ](https://github.com/GoogleCloudPlatform/gcloud-intellij/issues/599) ) 

