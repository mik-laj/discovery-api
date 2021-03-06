#  Versionshinweise

Auf dieser Seite werden Produktionsaktualisierungen für Migrate for Compute
Engine dokumentiert. Prüfen Sie diese Seite regelmäßig auf Hinweise zu neuen
oder aktualisierten Features, Fehlerkorrekturen, bekannten Problemen und
verworfenen Funktionen.

Die neuesten Produktaktualisierungen für Google Cloud finden Sie auf der Seite
mit den [ Google Cloud-Versionshinweisen ](https://cloud.google.com/release-
notes?hl=de) .

Für neueste Produktaktualisierungen können Sie die URL der Seite in den [
Feedreader ](https://wikipedia.org/wiki/Comparison_of_feed_aggregators)
einfügen oder die Feed-URL direkt hinzufügen: `
https://cloud.google.com/feeds/migrate-for-compute-engine-release-notes.xml `
.

Eine Liste der Builds für diesen und andere Versionen finden Sie im [ Build-
Verlauf ](https://cloud.google.com/migrate/compute-engine/docs/build-
history?hl=de) .

##  Anforderungen und Betriebssystemunterstützung

Weitere Informationen finden Sie unter [ Anforderungen
](https://cloud.google.com/migrate/compute-
engine/docs/4.10/concepts/requirements?hl=de) und [ Unterstützte
Betriebssysteme ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/supported-os-versions?hl=de) .

##  4.10 Neue Funktionen

###  Cloud Console-Integration

**FEATURE:**

V4.10 lässt sich in die [ GCP Console ](https://cloud.google.com/cloud-
console/?hl=de) integrieren, um eine nahtlose Bereitstellung des
Migrationsmanagers sowie die Erstellung der erforderlichen Dienstkonten zu
ermöglichen.

###  Bereitstellung in einer Umgebung mit privatem Zugriff

**FEATURE:**

V4.10 unterstützt die Bereitstellung in Umgebungen mit aktiviertem privatem
API-Zugriff. In diesen Umgebungen wird das System ohne öffentliche IP-Adresse
bereitgestellt und benötigt für den Zugriff auf Cloud-APIs privaten Zugriff.
Siehe [ Migrationsmanager konfigurieren
](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-to/configure-
manager/configuring-migration-manager?hl=de) .

###  Optionale Bereitstellung des vCenter-Plug-ins

**FEATURE:**

In V4.10 wird die Option zur Bereitstellung in einer lokalen vCenter-
Quellumgebung mit oder ohne Bereitstellung des vCenter-Plug-ins eingeführt.
Wenn Sie kein vCenter-Plug-in bereitstellen, können Sie mehrere Migrate-
Systeme mit derselben vCenter-Umgebung verbinden. Siehe [ VMware vCenter-
Umgebung registrieren ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/how-to/configure-manager/configuring-vms-
vm?hl=de#register_the_vmware_vcenter_environment) .

###  Benutzerdefiniertes Skript von vorher/nachher beim Upgrade von Windows
2008 auf 2012 unterstützen

**FEATURE:**

In V4.10 wird die Unterstützung für die Ausführung benutzerdefinierter Skripts
vor und nach der Einführung des Windows-Upgrades eingeführt. Sie können der VM
benutzerdefinierte Skripts hinzufügen. Weitere Informationen finden Sie unter
[ Windows Server-VMs aktualisieren ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/how-to/upgrading-vms/upgrading-windows-vms?hl=de) .

###  Unterstützung bei der Migration von Azure Gen2-Instanzen zu Compute
Engine

**FEATURE:**

In Version 4.10 wird die Migration von einer [ Azure Gen2
](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/supported-os-versions?hl=de) -Instanz zu einer
Compute Engine-Instanz mit Unterstützung von UEFI unterstützt.

###  Automatische Betriebssystemerkennung und Lizenzzuweisung

**FEATURE:**

Mit V4.10 wird die automatische Identifizierung des migrierten Betriebssystems
eingeführt, das der migrierten VM standardmäßig die richtige Lizenz zuweist.
In Szenarien, in denen Sie VMs mit der Windows BYOL-Lizenz oder der Linux
Premium-Lizenz migrieren möchten, müssen Sie diese als Eingaben im Runbook
bereitstellen. Weitere Informationen finden Sie im [ Abschnitt zur
Lizenzierung ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/runbooks?hl=de) in der Dokumentation.

##  4.10.1

###  Behobene Probleme

**FIXED:**

Ein Problem mit der Windows-Partitionserkennung für bestimmte Volume-
Strukturen wurde behoben.

**FIXED:**

Azure-Laufwerke über 4 TB werden jetzt unterstützt.

##  4.10

###  Behobene Probleme

**FIXED:**

Ein Problem mit AWS-ena-Treibern, die Windows-Images nach der Migration
abstürzen ließen, wurde behoben.

##  4.10

###  Bekannte Probleme

**ISSUE:**

**#160405343:** Aufgrund einer [ Änderung des Verhaltens
](https://www.suse.com/support/kb/doc/?id=000019633) im Aktivierungsablauf für
SUSE schlägt die Konfiguration von Repositories auf SUSE Enterprise Linux-
Instanzen jetzt nach dem Trennen fehl.

**Problemumgehung** : Sie können die folgende Problemumgehung vor dem Trennen
verwenden (entweder vor der Migration oder vor dem Trennen).

  1. Befolgen Sie die Anleitung für Situation 4 unter [ https://www.suse.com/support/kb/doc/?id=000019633 ](https://www.suse.com/support/kb/doc/?id=000019633) , um die erforderlichen Pakete für Compute Engine als Tar.gz-Datei herunterzuladen. 
  2. **Für SLES 12.x** führen Sie die folgenden Befehle aus: 
    
        sha1sum late_instance_offline_update_gce_SLE12.tar.gz
    tar -xf late_instance_offline_update_gce_SLE12.tar.gz
    cd x86_64/
    zypper --no-refresh --no-remote --non-interactive in *.rpm

  3. **Für SLES 15.x** führen Sie die folgenden Befehle aus: 
    
        sha1sum late_instance_offline_update_gce_SLE15.tar.gz
    tar -xf late_instance_offline_update_gce_SLE15.tar.gz
    cd x86_64/
    zypper --no-refresh --no-remote --non-interactive in *.rpm

**ISSUE:**

**#149004085:** Ubuntu 14 aus der lokalen Umgebung kann nach dem Trennen des
Netzwerks möglicherweise nicht gestartet werden.

**Problemumgehung:** Stellen Sie eine Verbindung über die serielle Konsole her
und fügen Sie die Netzwerkschnittstelle manuell mit DHCP hinzu.

**ISSUE:**

**#145086776:** In seltenen Fällen können ältere Versionen von RHEL7 während
des Streamings hängen bleiben oder eine Kernel-Panic auslösen. Dieses Problem
wurde in späteren Versionen von RHEL7 behoben.

**Problemumgehung:** Führen Sie ` sudo yum update ` vor der Migration aus, um
das System zu aktualisieren.

**ISSUE:**

**#145644737:** Bei Klonen, die in Azure oder AWS von Instanzen von Linux-
Distributionen erstellt wurden, die cloud-init verwenden, kann es nach der
Installation des Linux-Präpakets zu Problemen beim Starten kommen.

**Problemumgehung:** Deinstallieren Sie das Paket vor dem Klonen und
installieren Sie es neu, wenn Sie die Migration vorbereiten.

**ISSUE:**

**#143313211:** Bei der Migration von RHEL 6.8-VM können Kunden Boot-Probleme
im Cloud-Ziel erfahren.

RHEL 6.x-Systeme, die die Kernel-Version 2.6.32-xxx und LVM verwenden,
erreichen beim Booten in Compute Engine während der Migration möglicherweise
eine Kernel-Panic.

**Problemumgehung:** Der Kernel sollte vor der Migration auf Version
2.6.32-754 aktualisiert werden.

**ISSUE:**

**#143262721:** Die Migration einer VM von Azure schlägt fehl, wenn das
Datenlaufwerk größer als 4 Terabyte ist.

Derzeit unterstützt Migrate for Compute Engine die Migration von Azure-VMs mit
Datenlaufwerken, die größer als 4 TB sind.

**Problemumgehung:** Stellen Sie sicher, dass das Datenlaufwerk der VM kleiner
als 4 TB ist.

**ISSUE:**

**#131532690:** Run-in-Cloud- und Migrationsvorgänge können für Windows Server
2016-Arbeitslasten fehlschlagen, wenn Symantec Endpoint Protection (SEP)
installiert ist. Dies kann auch der Fall sein, wenn SEP scheinbar deaktiviert
ist.

**Problemumgehung:** Ändern Sie die Netzwerkschnittstellenbindungen der
Arbeitslast, um die SEP-Option zu entfernen.

  1. Laden Sie [ Microsoft Network VSP Bind (nvspbind) ](https://gallery.technet.microsoft.com/Hyper-V-Network-VSP-Bind-cf937850) herunter. 
  2. Installieren Sie Microsoft_Nvspbind_package.EXE in c:\temp. 
  3. Öffnen Sie eine Eingabeaufforderung als Administrator und führen Sie Folgendes aus: 
    
        nvspbind.exe /d * symc_teefer2

**ISSUE:**

**#131614405:** Wenn das Velostrata-Vorbereitungspaket im RPM-Format auf SUSE
Linux Enterprise Server 11 installiert ist, erhält die VM zusätzlich zur
vorhandenen statischen IP-Konfiguration eine DHCP-IP-Adresse. Dieses Problem
tritt auf, wenn die VM lokal in einem Subnetz gestartet wird, das mit DHCP-
Diensten aktiviert ist.

Hinweis: Das Problem tritt nicht auf, wenn das Subnetz keine DHCP-Dienste hat.
Die Kommunikation mit der ursprünglichen statischen IP-Adresse hat keine
Auswirkungen auf die Konnektivität.

**ISSUE:**

**#131637800:** Nach der Registrierung des Velostrata-Plug-ins wird beim
Ausführen des Cloud-Erweiterungsassistenten nach Abschluss des Vorgangs
möglicherweise der Fehler "XXXXXXXXXX" angezeigt.

**Problemumgehung:** Heben Sie die Registrierung des Velostrata-Plug-ins auf,
starten Sie den vSphere-Webclient neu und registrieren Sie dann das Plug-in
noch einmal. Wenden Sie sich an den Support, wenn das Problem weiterhin
besteht.

**ISSUE:**

**#131548730:** Wenn eine VM in Run-in-Cloud verschoben wird und eine
Sicherungslösung auf VM-Ebene eines Drittanbieters einen temporären Snapshot
enthält, werden die regelmäßigen Migrate for Compute Engine-
Rückschreibvorgänge nicht abgeschlossen, selbst wenn die Sicherungslösung den
temporären Snapshot gelöscht hat. Der Zähler für Schreibvorgänge ohne Commit
auf der VM zeigt eine zunehmende Größe an. Es wird kein lokaler Prüfpunkt für
die Konsistenz erstellt.

**Problemumgehung:** Wählen Sie die Aktion "Lokal ausführen" für die VM aus
und warten Sie, bis die Aufgabe abgeschlossen ist. Dadurch werden alle
ausstehenden Schreibvorgänge übernommen. Wählen Sie dann noch einmal die Run-
in-Cloud-Aktion aus. Beachten Sie, dass das Commit für alle ausstehenden
Schreibvorgänge eine Weile dauern kann. Verwenden Sie nicht die Option
"Erzwingen", da dies zum Verlust der Schreibvorgänge ohne Commit führt.

**ISSUE:**

**#131605387:** Durch einen Neustart von vCenter werden Velostrata-Aufgaben in
vCenter von der Benutzeroberfläche entfernt. Dies ist eine vCenter-
Einschränkung.

**Problemumgehung:** Verwenden Sie das Velostrata PowerShell-Modul, um
verwaltete Velostrata-VMs oder Cloud-Erweiterungsaufgaben zu überwachen, die
derzeit ausgeführt werden.

**ISSUE:**

**#131638716:** Bei einem ESXi-Host im Wartungsmodus schlägt der Vorgang fehl
und bleibt in der Rollback-Phase hängen, wenn eine VM in die Cloud verschoben
wird.

**Problemumgehung:** Brechen Sie die Run-in-Cloud-Aufgabe manuell ab,
migrieren Sie die VM zu einem anderen ESXi-Host im Cluster und wiederholen Sie
den Run-in-Cloud-Vorgang.

**ISSUE:**

**#131638455:** Ein Run-in-Cloud-Vorgang schlägt mit dem Fehler fehl: "Fehler
beim Erstellen des virtuellen Maschinen-Snapshots. Der Vorgang kann im
aktuellen Status nicht ausgeführt werden (ausgeschaltet)".

**Problemumgehung:** Die VM-Snapshot-Datei von VM verweist möglicherweise auf
einen nicht vorhandenen Snapshot. Wenden Sie sich an den Support, um
Unterstützung zur Behebung des Problems zu erhalten.

**ISSUE:**

**#131534862:** In seltenen Fällen werden nach dem erneuten lokalen Ausführen
einer Arbeitslast Workload VMDKs gesperrt. In bestimmten Fällen ist dies auf
Netzwerkunterbrechungen zwischen der Velostrata Management Appliance und dem
ESXi-Host zurückzuführen, auf dem die Arbeitslast ausgeführt wird.

Hinweis: Das Problem behebt sich nach 1–2 Stunden von selbst.

**ISSUE:**

**#131550214:** Während des Trennvorgangs schlägt der Vorgang möglicherweise
mit der folgenden Fehlermeldung fehl: "Vorgang wurde abgebrochen".

**Problemumgehung:** Wiederholen Sie den Vorgang zum Trennen.

**ISSUE:**

**#131650367:** Beim Ausführen eines Trennvorgangs nach einem Abbruch eines
Trennvorgangs kann die Aktion fehlschlagen.

**Problemumgehung:** Wiederholen Sie den Vorgang.

**ISSUE:**

**#131649978:** Bei bestimmten Systemausfällen werden Velostrata-Komponenten
von vCenter getrennt. In diesem Fall wird ein Ereignis möglicherweise nicht
gesendet, was dazu führt, dass der Alarm nicht ordnungsgemäß eingestellt oder
nicht ordnungsgemäß gelöscht wird.

**Problemumgehung:** Löschen Sie den Alarm manuell in vCenter.

**ISSUE:**

**#131532549:** Bei Arbeitslasten mit einem Windows-Computer mit einer
Einzelhandelslizenz ist die Lizenz bei der Rückgabe aus der Cloud nicht
vorhanden.

**Problemumgehung:** Installieren Sie die Lizenz neu.

**ISSUE:**

**#131555885:** Der vCenter-Vorgang "Export einer OVA" ist verfügbar, wenn die
VM in der Cloud im Cache-Modus ausgeführt wird. Dieser Vorgang führt jedoch zu
einem beschädigten OVA.

**Problemumgehung:** Erstellen Sie nach dem Trennen nur eine OVA.

**ISSUE:**

**#131647857:** In seltenen Fällen bleibt die Instanz ohne Tag, wenn eine
Instanz einer Cloud-Komponente erstellt wird und das System ausfällt, bevor
sie getaggt wird. Eine vollständige Bereinigung oder Reparatur des CE ist
nicht zulässig.

**Problemumgehung:** Taggen Sie die Instanz manuell und führen Sie dann
"Reparieren" aus.

**ISSUE:**

**#131537125:** Die Hochverfügbarkeit von Cloud-Erweiterungen funktioniert
nicht für Arbeitslasten, auf denen Ubuntu OS mit LVM-Konfiguration ausgeführt
wird.

**Problemumgehung:** Aktualisieren Sie den Kernel auf Version 3.13.0-161 oder
höher.

**ISSUE:**

**#131560126:** Suse12: Aufgrund eines Programmfehlers im SUSE-Kernel, der
älter als 4.2 ist, werden Konfigurationen mit BTRFS-Bereitstellungen mit
Subvolumes nicht unterstützt.

**Problemumgehung:** Führen Sie ein Upgrade auf SUSE-Version mit Kernel >= 4.2
(SP2) durch.

**ISSUE:**

**#131533480:** Wenn Sie den Assistenten zum Erstellen von Cloud-Erweiterungen
verwenden, wird bei Verwendung einer ungültigen HTTP-Proxy-Adresse keine
Warnmeldung generiert.

**Problemumgehung:** Löschen Sie das CE und erstellen Sie dann das CE mit
einer gültigen HTTP-Proxyadresse.

**ISSUE:**

**#131647654:** Run On-premises wurde erfolgreich ausgeführt, der Status ist
jedoch mit dem Fehler "Fehler beim Konsolidieren von Snapshots"
gekennzeichnet.

**Problemumgehung:** Konsolidieren Sie Snapshots über vCenter und löschen Sie
den Fehler manuell.

**ISSUE:**

**#131558198:** Der PowerShell-Client für Cloud Runbook meldet Fehler, wenn er
auf PowerShell 3.0 ausgeführt wird

**Problemumgehung:** Führen Sie ein Upgrade auf PowerShell 4.0 durch

**ISSUE:**

**#131533056:** Bei der Migration von RHEL 7.4 von AWS zu Google Cloud wird
der Google Cloud-Agent nicht automatisch installiert.

**Problemumgehung:** Entfernen Sie den AWS-Agent manuell und installieren Sie
den Google Cloud-Agent

**ISSUE:**

**#131532713:** Wenn nach der Offline-Migration von Windows 2003R2 manuell
eine NIC gelöscht wird, kann sie möglicherweise nicht automatisch erkannt und
automatisch neu installiert werden.

Problemumgehung: Der VM-Speicher kann an eine andere VM angehängt werden und
der NIC-Registrierungseintrag kann manuell mit einer ähnlichen VM als Referenz
importiert werden. Wenden Sie sich an den Support.

**ISSUE:**

**#131532666:** Bei Linux-Versionen, die mit Kernel-Version 2.6.32 ausgeführt
werden, kann es zu Fehlern beim sitzungsspezifischen Speicherzugriff kommen.
Diese sind beim Streaming über iSCSI wahrscheinlicher.

Problemumgehung: Aktualisieren Sie den Kernel. Das Problem wird nach der
Trennung wahrscheinlich verringert.

**ISSUE:**

**#131532846:** Bestimmte Firewalls und Antivirenprogramme können dazu führen,
dass Windows-VMs durch das Blockieren von iSCSI-Traffic in die Cloud
verschoben werden.

Problemumgehung: Entfernen Sie den betroffenen Dienst während der Migration
und installieren Sie ihn nach dem Trennen neu.

**ISSUE:**

**#131532882:** In bestimmten Fällen kann das Starten von Run-in-Cloud während
eines Windows-Updates dazu führen, dass das Update plötzlich beendet wird und
nicht in der Cloud gestartet werden kann.

Problemumgehung: Erlauben Sie dem System, das Windows-Update abzuschließen
und/oder sperren Sie Windows-Updates vor der Migration.

**ISSUE:**

**#135664281:** Wenn bei der Migration von Azure zu Google Cloud-Migration ein
Vorgang abgeschlossen oder abgebrochen wird, können von Velostrata erstellte
Ressourcen möglicherweise in der Ressourcengruppe der ursprünglichen Instanz
verbleiben.

**ISSUE:**

**#133137658:** Szenario: Keine Netzwerkverbindung zwischen Migration Manager
und VSphere

Auswirkungen auf den Kunden: Die Run-In-Cloud-Aufgabe bleibt aufgrund eines
fehlgeschlagenen Aufrufs von getReadSessions in VSphere hängen.

**Problemumgehung:** Stellen Sie die Netzwerkverbindung wieder her. Falls
nicht, brechen Sie die Aufgabe ab und versuchen Sie es noch einmal.

**ISSUE:**

**#135573857** Szenario: Beim Verschieben einer VM mit "Flag "force" zurück in
die lokale Umgebung bleibt die VM von Velostrata verwaltet, wenn der Snapshot
nicht konsolidiert wird. Run-In-Cloud auf derselben VM kann fehlschlagen, da
es auf verwalteten VMs nicht zulässig ist.

**Problemumgehung:** Warten Sie einige Minuten und versuchen Sie es dann
wieder.

**ISSUE:**

**#137082702:** In seltenen Fällen ist der Vorgang zum Aufheben der Trennung
erfolgreich, die VM-Instanz kann jedoch nicht gestartet werden.

**Problemumgehung** : Verschieben Sie die Instanz zurück und dann wieder in
die Cloud.

