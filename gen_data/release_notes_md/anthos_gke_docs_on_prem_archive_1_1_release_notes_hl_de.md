#  Versionshinweise

Auf dieser Seite werden die Produktionsaktualisierungen von GKE On-Prem
dokumentiert. Prüfen Sie diese Seite regelmäßig auf Hinweise zu neuen oder
aktualisierten Features, Fehlerkorrekturen, bekannten Problemen und
verworfenen Funktionen.

Weitere Informationen

  * [ Downloads ](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=de)
  * [ Versionsverwaltung und Upgrades ](https://cloud.google.com/anthos/gke/docs/on-prem/versioning-and-upgrades?hl=de)
  * [ GKE On-Prem upgraden ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=de)

Die neuesten Produktaktualisierungen für Google Cloud finden Sie auf der Seite
mit den [ Google Cloud-Versionshinweisen ](https://cloud.google.com/release-
notes?hl=de) .

Für neueste Produktaktualisierungen können Sie die URL der Seite in den [
Feedreader ](https://wikipedia.org/wiki/Comparison_of_feed_aggregators)
einfügen oder die Feed-URL direkt hinzufügen: `
https://cloud.google.com/feeds/gkeonprem-release-notes.xml ` .

##  19\. November 2018

Die GKE-On-Premix-Version 1.1.2-gke.0 ist jetzt verfügbar. So laden Sie die
OVA der Version 1.1.2-gke.0 herunter: ` gkectl ` und Upgrade-Bundle siehe [
Downloads ](https://cloud.google.com/anthos/gke/docs/on-
prem/downloads?hl=de#latest) . Anschließend finden Sie weitere Informationen
unter [ Administrator-Workstation aktualisieren
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=de) und
[ Cluster aktualisieren ](https://cloud.google.com/anthos/gke/docs/on-
prem/how-to/upgrading?hl=de) .

Diese Patchversion beinhaltet die folgenden Änderungen:

###  Neue Funktionen

**FEATURE:**

Veröffentlicht: [ Härtung Ihres Clusters
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/security/hardening-your-cluster?hl=de) .

**FEATURE:**

Veröffentlichung von [ Clustern verwalten
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/managing-clusters?hl=de) .

###  Korrekturen

**FIXED:**

Das bekannte Problem vom  5\. November  wurde behoben.

**FIXED:**

Das bekannte Problem vom  8\. November  wurde behoben.

###  Bekannte Probleme

**ISSUE:**

Wenn Sie mehrere Rechenzentren in vSphere ausführen, gibt ` gkectl diagnose
cluster ` möglicherweise den folgenden Fehler zurück, den Sie ignorieren
können:

    
    
    Checking storage...FAIL
    path '*' resolves to multiple datacenters

**ISSUE:**

Wenn Sie einen vSAN-Datenspeicher ausführen, gibt ` gkectl diagnose cluster `
möglicherweise den folgenden Fehler aus, den Sie ignorieren können:

    
    
    PersistentVolume [NAME]: virtual disk "[[DATASTORE_NAME]]
    [PVC]" IS NOT attached to machine "[MACHINE_NAME]" but IS listed in the Node.Status

##  8\. November 2018

**ISSUE:**

In der GKE On-Prem-Version 1.1.1-gke.2 verhindert ein bekanntes Problem die
Erstellung von Clustern, die für die Verwendung einer Docker-Registry
konfiguriert sind. Sie konfigurieren eine Docker-Registry, indem Sie das Feld
` privateregistryconfig ` der GKE On-Prem-Konfigurationsdatei ausfüllen. Die
Clustererstellung schlägt mit einem Fehler wie ` Failed to create root
cluster: could not create external client: could not create external control
plane: docker run error: exit status 125 ` fehl.

Eine Update ist für Version 1.1.2 vorgesehen. Wenn Sie in der Zwischenzeit
einen Cluster erstellen möchten, der für die Verwendung einer Docker-Registry
konfiguriert ist, übergeben Sie das Flag ` --skip-validation-docker ` an `
gkectl create cluster ` .

##  5\. November 2018

**ISSUE:**

Die Konfigurationsdatei von GKE On-Prem enthält das Feld ` vcenter.datadisk `
, das nach einem Pfad zu einer Datei einer virtuellen Maschine (VDMK) sucht.
Bei der Installation wählen Sie einen Namen für das VMDK aus. Standardmäßig
erstellt GKE On-Prem ein VMDK und speichert es im Stammverzeichnis Ihres
vSphere-Datenspeichers.

Wenn Sie einen vSAN-Datenspeicher verwenden, müssen Sie im Datenspeicher einen
Ordner erstellen, in dem das VMDK gespeichert werden soll. Sie geben den
vollständigen Pfad zum Feld an, z. B. ` datadisk: anthos/gke/docs/on-
prem/datadisk.vmdk ` und GKE On-Prem speichert das VMDK in diesem Ordner.

Wenn Sie den Ordner erstellen, weist vSphere dem Ordner eine universell
eindeutige Kennung (UUID) zu. Obwohl Sie den Ordnerpfad zur GKE On-Prem-
Konfiguration angeben, sucht die vSphere API nach der UUID des Ordners.
Derzeit kann dieser Konflikt dazu führen, dass die Erstellung von Clustern und
Upgrades fehlschlagen.

Eine Update ist für Version 1.1.2 vorgesehen. In der Zwischenzeit müssen Sie
die UUID des Ordners und nicht den Pfad des Ordners angeben. Folgen Sie der
aktuell verfügbaren Anleitung zur Problemumgehung unter [ Cluster
aktualisieren ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/upgrading-
clusters?hl=de#admin_datadisk_folder) und in den Installationsthemen.

##  25\. Oktober 2019

Die GKE On-Prem-Version 1.1.1-gke.2 ist jetzt verfügbar. Informationen zum
Herunterladen der OVA ` gkectl ` und des Upgrade-Bundles von Version
1.1.1-gke.2 finden Sie unter [ Downloads
](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=de#latest) .
Anschließend finden Sie weitere Informationen unter [ Administrator-
Workstation aktualisieren ](https://cloud.google.com/anthos/gke/docs/on-
prem/how-to/upgrading?hl=de) und [ Cluster aktualisieren
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=de) .

Diese Patchversion beinhaltet die folgenden Änderungen:

###  Neue Funktionen

**FEATURE:**

**Erforderliche Aktion:** Mit dieser Version wird die Mindestversion von `
gcloud ` auf der Admin-Workstation auf 256.0.0 aktualisiert. Sie sollten Ihre
[ Admin-Workstation aktualisieren
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/upgrading-admin-workstation?hl=de) . Anschließend sollten
Sie die [ Cluster aktualisieren ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/upgrading-clusters?hl=de) .

**FEATURE:**

Die Open-Source- [ CoreOS Toolbox ](https://github.com/coreos/toolbox) ist
jetzt in allen GKE On-Prem-Clusterknoten enthalten. Diese Reihe von Tools ist
nützlich bei der Behebung von Knotenproblemen. Siehe [ Debugging von
Knotenproblemen mithilfe der Toolbox
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/support/toolbox?hl=de) .

###  Korrekturen

**FIXED:**

Ein Problem wurde behoben, bei dem Cluster, die mit OIDC konfiguriert waren,
nicht aktualisiert werden konnten.

**FIXED:**

Behoben: [ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) in [ Sicherheitsbulletins
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/security-
bulletins?hl=de#october-16-2019) beschrieben.

**FIXED:**

Das Problem, dass Clustermesswerte aufgrund einer unterbrochenen Verbindung
zur Google Cloud verloren gehen, wurde behoben. Wenn die Verbindung eines GKE
On-Prem-Clusters zur Google Cloud für einen bestimmten Zeitraum unterbrochen
wird, werden die Messwerte dieses Clusters jetzt vollständig
wiederhergestellt.

**FIXED:**

Ein Problem wurde behoben, bei dem die Aufnahme von Administratorcluster-
Messwerten langsamer war als die Aufnahme von Nutzercluster-Messwerten.

###  Bekannte Probleme

**ISSUE:**

Für Nutzercluster, die statische IP-Adressen und ein anderes Netzwerk als ihr
Administratorcluster verwenden: Wenn Sie die Netzwerkkonfiguration des
Nutzerclusters überschreiben, kann die Steuerungsebene des Nutzers
möglicherweise nicht gestartet werden. Dies liegt daran, dass das Netzwerk des
Nutzerclusters verwendet wird, dem Administratorcluster jedoch eine IP-Adresse
und ein Gateway zugewiesen werden.

Als Behelfslösung können Sie die MachineDeployment-Spezifikation jeder
Nutzersteuerungsebene aktualisieren, um das richtige Netzwerk zu verwenden.
Löschen Sie anschließend alle Maschinen der Steuerungsebene für die Nutzer,
damit vom MachineDeployment neue Maschinen erstellt werden:

  1.     # List MachineDeployments in the admin cluster
        kubectl get machinedeployments --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

  2.     # Update a user control plane MachineDeployment from your shell
        kubectl edit machinedeployment --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] [MACHINEDEPLOYMENT_NAME]

  3.     # List Machines in the admin cluster
        kubectl get machines --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

  4.     # Delete user control plane Machines in the admin cluster
        kubectl delete machines --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] [MACHINE_NAME]

##  26\. September 2019

Die GKE On-Prem-Version 1.1.0-gke.6 ist jetzt verfügbar. Informationen zum
Herunterladen des ` gkectl ` und des Upgrade-Bundles von Version 1.1.0-gke.6
finden Sie unter [ Downloads ](https://cloud.google.com/anthos/gke/docs/on-
prem/downloads?hl=de#latest) . Lesen Sie dann [ Cluster aktualisieren
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=de) .

Diese Nebenversion enthält die folgenden Änderungen:

###  Neue Funktionen

**FEATURE:**

Die Standard-Kubernetes-Version für Clusterknoten ist nun Version
1.13.7-gke.20 (bisher 1.12.7-gke.19).

**FEATURE:**

**Erforderliche Aktion:** Ab Version 1.1.0-gke.6 erstellt GKE On-Prem jetzt
vSphere-Regeln des Typs [ Distributed Resource Scheduler (DRS)
](https://www.vmware.com/products/vsphere/drs-dpm.html) für die Knoten Ihres
Nutzerclusters (vSphere-VMs), sodass sie auf mindestens drei physische Hosts
in Ihrem Rechenzentrum verteilt werden.

**Diese Funktion ist standardmäßig für alle neuen und vorhandenen
Nutzercluster mit Version 1.1.0-gke.6 aktiviert.**

Für diese Funktion muss die vSphere-Umgebung die folgenden Bedingungen
erfüllen:

  * VMware DRS muss aktiviert sein. VMware DRS erfordert die vSphere Enterprise Plus-Lizenzversion. Informationen zum Aktivieren von DRS finden Sie unter [ VMWare DRS in einem Cluster aktivieren ](https://kb.vmware.com/s/article/1034280) . 
  * Das im Feld ` vcenter ` Ihrer GKE On-Prem-Konfigurationsdatei angegebene vSphere-Nutzerkonto muss die Berechtigung ` Host.Inventory.EditCluster ` haben. 
  * Es sind mindestens drei physische Hosts verfügbar. 

Wenn Sie diese Funktion _nicht_ für Ihre vorhandenen Nutzercluster aktivieren
möchten, z. B. wenn Sie nicht genügend Hosts haben, um die Funktion zu
übernehmen, führen Sie die folgenden Schritte aus, _bevor_ Sie Ihre
Nutzercluster aktualisieren:

  1. Öffnen Sie die vorhandene GKE On-Prem-Konfigurationsdatei. 
  2. Fügen Sie unter der Spezifikation ` usercluster ` das Feld ` antiaffinitygroups ` hinzu, wie in der [ Dokumentation ` antiaffinitygroups ` ](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-to/installation/install?hl=de#antiaffinitygroups) beschrieben: 
    
        usercluster:
          ...
          antiaffinitygroups:
            enabled: false
    

  3. Speichern Sie die Datei. 
  4. Verwenden Sie die Konfigurationsdatei zur Aktualisierung. Ihre Cluster werden aktualisiert, aber die Funktion ist nicht aktiviert. 

**FEATURE:**

Sie können jetzt die [ Standardspeicherklasse
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/default-storage-class?hl=de) für Ihre Cluster festlegen.

**FEATURE:**

Sie können jetzt [ Container Storage Interface (CSI) 1.0
](https://github.com/container-storage-interface/spec) als Speicherklasse für
Ihre Cluster verwenden.

**FEATURE:**

Mit ` gkectl delete cluster --force ` können Sie jetzt [ defekte oder
fehlerhafte Nutzercluster löschen
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/deleting-a-user-cluster?hl=de#delete_unhealthy_cluster) .

**FEATURE:**

Sie können jetzt mit dem Container-Image ` debug-toolbox ` [ Knotenprobleme
diagnostizieren ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/support/debug-toolbox?hl=de) .

**FEATURE:**

Sie können nun [ Validierungen überspringen
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/install?hl=de#skip_validate) , die von ` gkectl ` -Befehlen
ausgeführt werden.

**FEATURE:**

Das von ` gkectl diagnose snapshot ` erstellte Tarball-Paket enthält jetzt
standardmäßig ein Log der Befehlsausgabe.

**FEATURE:**

Fügt dem Flag ` gkectl diagnose snapshot ` ` --seed-config ` hinzu. Wenn Sie
das Flag übergeben, wird die lokale GKE-Konfigurationsdatei des Clusters in
den von ` snapshot ` generierten Tarball aufgenommen.

###  Änderungen

**CHANGED:**

Das Feld ` gkeplatformversion ` wurde aus der Konfigurationsdatei von GKE On-
Prem entfernt. Geben Sie zum Angeben der Version eines Clusters das Bundle der
Version im Feld ` bundlepath ` an.

**CHANGED:**

Sie müssen die vSphere-Berechtigung ` Host.Inventory.EditCluster ` hinzufügen,
bevor Sie [ ` antiaffinitygroups `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/install?hl=de#antiaffinitygroups) verwenden können.

**CHANGED:**

Sie geben jetzt in ` gkectl diagnose snapshot ` eine Konfigurationsdatei an,
indem Sie die ` --snapshot-config ` (früher ` --config ` ) übergeben. Siehe [
Clusterprobleme diagnostizieren ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/support/diagnose?hl=de#diagnose_snapshot) .

**CHANGED:**

Erfassen Sie nun die Konfigurationsdatei Ihres Clusters mit ` gkectl diagnose
snapshot ` , indem Sie ` --snapshot-config ` (früher ` --config ` ) übergeben.
Weitere Informationen finden Sie unter [ Clusterprobleme diagnostizieren
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/support/diagnose?hl=de#diagnose_snapshot) .

**CHANGED:**

` gkectl diagnose ` -Befehle geben jetzt einen Fehler zurück, wenn Sie die
kubeconfig eines Nutzerclusters und nicht die kubeconfig eines
Administratorclusters angeben.

**CHANGED:**

Sie werden von der Cloud Console benachrichtigt, wenn ein Upgrade für einen
registrierten Nutzercluster verfügbar ist.

###  Bekannte Probleme

**ISSUE:**

Ein bekanntes Problem verhindert, dass Cluster der Versionen 1.0.11,
1.0.1-gke.5 und 1.0.2-gke.3, die OIDC verwenden, auf Version 1.1 aktualisiert
werden. Ein Update ist für Version 1.1.1 vorgesehen. Wenn Sie einen Cluster
der Version 1.0.11, 1.0.1-gke.5 oder 1.0.2-gke.3 mit OIDC konfiguriert haben,
können Sie kein Upgrade ausführen. Erstellen Sie einen Cluster der Version
1.1, indem Sie [ GKE On-Prem installieren
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/install?hl=de) .

##  22\. August 2019

Die GKE On-Prem-Version 1.0.2-gke.3 ist jetzt verfügbar. Diese Patch-Version
enthält die folgenden Änderungen:

###  Neue Funktionen

**FEATURE:**

Seesaw wird jetzt für den manuellen Lastenausgleich unterstützt.

**FEATURE:**

Sie können jetzt für Administratoren- und Nutzercluster ein anderes vSphere-
Netzwerk angeben.

**FEATURE:**

Sie können jetzt Nutzercluster mit ` gkectl ` löschen. Siehe [ Einen
Nutzercluster löschen ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/deleting-a-user-cluster?hl=de) .

###  Änderungen

**CHANGED:** ` gkectl diagnose snapshot ` ruft jetzt Logs von den
Steuerungsebenen des Nutzerclusters ab.

**CHANGED:**

Die GKE On-Prem-OIDC-Spezifikation wurde mit mehreren neuen Feldern
aktualisiert: ` kubectlredirecturl ` , ` scopes ` , ` extraparams ` und `
usehttpproxy ` .

**CHANGED:**

Calico wurde auf Version 3.7.4 aktualisiert.

**CHANGED:**

Die Systemmesswerte von Cloud Monitoring wurden von `
external.googleapis.com/prometheus/ ` in ` kubernetes.io/anthos/ ` geändert.
Wenn Sie Messwerte oder Benachrichtigungen erfassen, aktualisieren Sie Ihre
Dashboards mit dem nächsten Präfix.

###  Fest

**FIXED:**

[ Eine Sicherheitslücke von CVE-2019-11247 wurde behoben
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/security-
bulletins?hl=de#august-22-2019) .

**FIXED:**

[ Eine Sicherheitslücke im RBAC-Proxy wurde behoben
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/security-
bulletins?hl=de#august-23-2019) .

##  30\. Juli 2019

Die GKE On-Prem-Version 1.0.1-gke.5 ist jetzt verfügbar. Diese Patch-Version
enthält die folgenden Änderungen:

###  Neue Funktionen

**FEATURE:**

[ GKE On-Prem-Spickliste ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/reference/cheatsheet?hl=de) veröffentlicht.

###  Änderungen

**CHANGED:**

` gkectl check-config ` prüft jetzt auch die Knoten-IP-Verfügbarkeit, wenn Sie
statische IP-Adressen verwenden.

**CHANGED:**

` gkectl prepare ` prüft jetzt, ob eine VM vorhanden ist, und wird in vsphere
als Vorlage markiert, bevor versucht wird, das OVA-Image der VM hochzuladen.

**CHANGED:**

Bietet Unterstützung für die Angabe eines vCenter-Clusters und eines
Ressourcenpools in diesem Cluster.

**CHANGED:**

Aktualisiert den BIG-IP-Controller F5 auf Version 1.9.0.

**CHANGED:**

Aktualisiert den Istio-Ingress-Controller auf Version 1.2.2.

###  Korrekturen

**FIXED:**

Behebt Probleme mit der Persistenz von Registry-Daten in der Docker-Registry
der Administrator-Workstation.

**FIXED:**

Behebt Probleme mit der Validierung, die prüft, ob der Name eines
Nutzerclusters bereits verwendet wird.

##  25\. Juli 2019

Die GKE On-Prem-Version 1.0.11 ist jetzt verfügbar.

##  17\. Juni 2019

GKE On-Prem ist jetzt allgemein verfügbar. Version 1.0.10 enthält die
folgenden Änderungen:

###  Upgrade von Beta-1.4 auf 1.0.10

Führen Sie vor dem Upgrade Ihrer Beta-Cluster auf die erste Version mit
allgemeiner Verfügbarkeit die unter [ Upgrade von GKE On-Prem-Beta auf
allgemeine Verfügbarkeit ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/upgrading/from-beta?hl=de) beschriebenen Schritte aus
und lesen Sie die folgenden Punkte:

  * Wenn Sie eine Betaversion vor Beta-1.4 verwenden, führen Sie zuerst ein Upgrade auf Beta-1.4 durch. 

  * Wenn Ihre Beta-Cluster ihre eigenen L4-Lastenausgleichsmodule ausführen, nicht die Standardeinstellung "F5 BIG-IP", müssen Sie Ihre Cluster löschen und neu erstellen, um die aktuelle GKE On-Prem-Version auszuführen. 

  * Wenn Ihre Cluster von Beta-1.3 auf Beta-1.4 aktualisiert wurden, führen Sie vor dem Upgrade _für jeden Nutzercluster_ den folgenden Befehl aus: 
    
        kubectl delete crd networkpolicies.crd.projectcalico.org

  * Die Bestätigung des vCenter-Zertifikats ist jetzt erforderlich. ( ` vsphereinsecure ` wird nicht mehr unterstützt.) Wenn Sie ein Upgrade Ihrer Beta-1.4-Cluster auf 1.0.10 ausführen, müssen Sie in der Upgrade-Konfigurationsdatei ein öffentliches Zertifikat für die vertrauenswürdige Stammzertifizierungsstelle von vCenter bereitstellen. 

  * Sie müssen _alle_ Ihrer laufenden Cluster umstellen. Damit dieses Upgrade erfolgreich ist, können Ihre Cluster nicht in einem gemischten Versionsstatus ausgeführt werden. 

  * Sie müssen zuerst Ihre Administratorcluster auf die neueste Version und dann Ihre Nutzercluster aktualisieren. 

###  Neue Funktionen

**FEATURE:**

Sie können jetzt den [ manuellen Load-Balancing-Modus
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/manual-lb?hl=de) zur Konfiguration eines L4-Load-Balancers
aktivieren. Sie können weiterhin den Standard-Load-Balancer F5 BIG-IP
verwenden.

**FEATURE:**

Der konfigurationsgesteuerte Installationsprozess von GKE On-Prem wurde
aktualisiert. Sie installieren jetzt deklarativ mithilfe einer einzelnen [
Konfigurationsdatei ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/overview?hl=de#config) .

**FEATURE:**

Fügt ` gkectl create-config ` hinzu, die eine Konfigurationsdatei für die
lokale Installation von GKE, das Upgrade vorhandener Cluster und das Erstellen
zusätzlicher Nutzercluster in einer vorhandenen Installation generiert.
Dadurch werden der Installationsassistent und ` create-config.yaml ` aus
früheren Versionen ersetzt. Weitere Informationen finden Sie in der
aktualisierten Dokumentation für [ GKE On-Prem installieren
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/install?hl=de#generate_config) .

**FEATURE:**

Fügt ` gkectl check-config ` hinzu, das die GKE On-Prem-Konfigurationsdatei
validiert. Weitere Informationen finden Sie in der aktualisierten
Dokumentation für [ GKE On-Prem installieren
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/install?hl=de#validate_config) .

**FEATURE:**

Fügt ` gkectl prepare ` ein optionales ` --validate-attestations ` -Flag
hinzu. Mit diesem Flag wird sichergestellt, dass die Container-Images auf
Ihrer Verwaltungs-Workstation von Google erstellt und signiert wurden und
bereit für die Bereitstellung sind. Weitere Informationen finden Sie in der
aktualisierten Dokumentation für [ GKE On-Prem installieren
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/install?hl=de#prepare) .

###  Änderungen

**CHANGED:**

Aktualisiert Kubernetes-Version auf 1.12.7-gke.19. Sie können jetzt [ Ihre
Cluster auf diese Version aktualisieren
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/upgrading-clusters?hl=de) . Sie können keine Cluster mehr
erstellen, auf denen die Kubernetes-Version 1.11.2-gke.19 ausgeführt wird.

Wir empfehlen Ihnen, Ihren Administratorcluster zu aktualisieren, bevor Sie
ein Upgrade Ihrer Nutzerclusters ausführen.

**CHANGED:**

Aktualisiert den Istio Ingress-Controller auf Version 1.1.7.

**CHANGED:**

Die Bestätigung des vCenter-Zertifikats ist jetzt erforderlich. ( `
vsphereinsecure ` wird nicht mehr unterstützt.) Sie geben das Zertifikat im
Feld ` cacertpath ` der GKE On-Prem-Konfigurationsdatei an.

Wenn ein Client den vCenter-Server aufruft, muss der vCenter-Server dem Client
seine Identität nachweisen, indem er ein Zertifikat vorlegt. Dieses Zertifikat
muss von einer Zertifizierungsstelle signiert sein. Das Zertifikat darf nicht
selbst signiert sein.

Wenn Sie ein Upgrade Ihrer Beta-1.4-Cluster auf 1.0.10 ausführen, müssen Sie
in der Upgrade-Konfigurationsdatei ein öffentliches Zertifikat für die
vertrauenswürdige Stammzertifizierungsstelle von vCenter bereitstellen.

###  Bekannte Probleme

**ISSUE:**

Das [ Aktualisieren von Clustern
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/upgrading-
clusters?hl=de) kann zu Unterbrechungen oder Ausfallzeiten für Arbeitslasten
führen, die [ PodDisauseBudgets
](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-
disruption-budgets-work) (PDBs) verwenden.

**ISSUE:**

Sie können Beta-Cluster, die das [ manuelle Load-Balancing
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/manual-lb?hl=de) verwenden, möglicherweise nicht auf die GKE
On-Prem-Version 1.0.10 aktualisieren. Wenn Sie mit diesen Clustern ein Upgrade
ausführen und weiterhin Ihren eigenen Load-Balancer verwenden möchten, müssen
Sie die Cluster neu erstellen.

##  24\. Mai 2019

Die GKE On-Prem-Betaversion 1.4.7 ist jetzt verfügbar. Dieser Release enthält
die folgenden Änderungen:

###  Neue Funktionen

**FEATURE:**

Im Befehl [ ` gkectl diagnose snapshot `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.4/how-
to/administration/diagnose?hl=de#capture_admin) ist der Parameter ` --admin-
ssh-key-path ` jetzt optional.

###  Änderungen

**CHANGED:**

Am 8. Mai 2019 haben wir eine Änderung an Connect eingeführt, dem Dienst, mit
dem Sie über die Cloud Console mit Ihren GKE On-Prem-Clustern interagieren
können. Wenn Sie den neuen Connect-Agent verwenden möchten, müssen Sie Ihre
Cluster noch einmal in der Cloud Console registrieren oder auf Anthos GKE On-
Prem Beta-1.4 aktualisieren.

Ihre GKE On-Prem-Cluster und die darauf ausgeführten Arbeitslasten
funktionieren weiterhin ohne Unterbrechung. Ihre Cluster sind jedoch erst in
der Cloud Console sichtbar, wenn Sie sie neu registrieren oder ein Upgrade auf
Beta-1.4 ausführen.

Stellen Sie vor der erneuten Registrierung oder dem Upgrade sicher, dass Ihr
Dienstkonto die Rolle ` gkehub.connect ` hat. Wenn Ihr Dienstkonto außerdem
die alte Rolle clusterregistry.connect hat, sollten Sie diese Rolle auch
entfernen.

Gewähren Sie Ihrem Dienstkonto die Rolle "gkehub.connect":

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

Wenn Ihr Dienstkonto die alte ` clusterregistry.connect ` -Rolle hat,
entfernen Sie die alte Rolle:

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/clusterregistry.connect"

Registrieren Sie den Cluster neu oder führen Sie ein Upgrade auf Anthos GKE
On-Prem-Beta-1.4 aus.

So [ registrieren Sie den Cluster noch einmal
](https://cloud.google.com/kubernetes-engine/connect/updating-agent?hl=de) :

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \
          --context=[USER_CLUSTER_CONTEXT] \
          --service-account-key-file=[LOCAL_KEY_PATH] \
          --kubeconfig-file=[KUBECONFIG_PATH] \
          --project=[PROJECT_ID]
          

[ Upgrade auf Anthos GKE On-Prem Beta-1.4:
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.4/how-
to/administration/upgrading-a-cluster?hl=de) :

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  Bekannte Probleme

**ISSUE:**

Aufgrund eines Problems kann der Connect-Agent während eines Upgrades nicht
auf die neue Version aktualisiert werden. Führen Sie nach dem Upgrade eines
Clusters den folgenden Befehl aus, um dieses Problem zu umgehen:

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  13\. Mai 2019

###  Bekannte Probleme

**ISSUE:**

Cluster, die von Version Beta-1.2 auf Beta-1.3 aktualisiert wurden, sind
möglicherweise von einem bekannten Problem betroffen, das die
Konfigurationsdatei des Clusters beschädigt und zukünftige Cluster-Upgrades
verhindert. Dieses Problem betrifft alle zukünftigen Clusterupgrades.

Sie können dieses Problem beheben, indem Sie Cluster löschen und neu
erstellen, die von Beta-1.2 auf Beta-1.3 aktualisiert wurden.

Um das Problem zu beheben, ohne den Cluster zu löschen und neu zu erstellen,
müssen Sie die Secrets jedes Clusters neu codieren und anwenden. Führen Sie
diese Schritte aus:

  1. Ruft den Inhalt der im Admincluster gespeicherten ` create-config ` -Secrets ab. Dies muss für das Secret ` create-config ` im Namespace kube-system und für die Secrets ` create-config ` im Namespace jedes Nutzerclusters durchgeführt werden: 
    
        kubectl get secret create-config -n kube-system -o jsonpath={.data.cfg} | base64 -d > kube-system_create_secret.yaml
    
        kubectl get secret create-config -n [USER_CLUSTER_NAME] -o jsonpath={.data.cfg} | base64 -d > [USER_CLUSTER_NAME]_create_secret.yaml

  2. Öffnen Sie für jeden Nutzercluster die Datei ` [USER_CLUSTER_NAME]  _create_secret.yaml ` in einem Editor. Wenn die Werte für ` registerserviceaccountkey ` und ` connectserviceaccountkey ` nicht ` REDACTED ` sind, ist keine weitere Aktion erforderlich: Die Secrets müssen nicht neu codiert und in den Cluster geschrieben werden. 
  3. Öffnen Sie die ursprüngliche ` create_config.yaml ` -Datei in einem anderen Editor. 
  4. Ersetzen Sie in ` [USER_CLUSTER_NAME]  _create_secret.yaml ` die Werte ` registerserviceaccountkey ` und ` connectserviceaccountkey ` durch die Werte aus der ursprünglichen ` create_config.yaml ` -Datei. Speichern Sie die geänderte Datei. 
  5. Wiederholen Sie die Schritte 3 bis 5 für jeden ` [USER_CLUSTER_NAME]  _create_secret.yaml ` und die Datei ` kube-system_create_secret.yaml ` . 
  6. Base64-Codierung für jede ` [USER_CLUSTER_NAME]  _create_secret.yaml ` -Datei und die ` kube-system_create_secret.yaml ` -Datei: 
    
        cat [USER_CLUSTER_NAME]_create_secret.yaml | base64 > [USER_CLUSTER_NAME]_create_secret_create_secret.b64
    
        cat kube-system-cluster_create_secret.yaml | base64 >kube-system-cluster_create_secret.b64

  7. Ersetzen Sie das Feld ` data[cfg] ` in jedem Secret im Cluster durch den Inhalt der entsprechenden Datei: 
    
        kubectl edit secret create-config -n [USER_CLUSTER_NAME]
    
      # kubectl edit opens the file in the shell's default text editor
      # Open `first-user-cluster_create_secret.b64` in another editor, and replace
      # the `cfg` value with the copied value
      # Make sure the copied string has no newlines in it!

  8. Wiederholen Sie Schritt 8 für jedes ` [USER_CLUSTER_NAME]  _create_secret.yaml ` -Secret und für das ` kube-system_create_secret.yaml ` -Secret. 
  9. Um sicherzustellen, dass die Aktualisierung erfolgreich war, wiederholen Sie Schritt 1. 

##  7\. Mai 2019

Die GKE On-Prem-Betaversion 1.4.1 ist jetzt verfügbar. Dieser Release enthält
die folgenden Änderungen:

###  Neue Funktionen

**FEATURE:**

Im Befehl [ ` gkectl diagnose snapshot `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.4/how-
to/administration/diagnose?hl=de#capture_admin) ist der Parameter ` --admin-
ssh-key-path ` jetzt optional.

###  Änderungen

**CHANGED:**

Am 8. Mai 2019 haben wir eine Änderung an Connect eingeführt, dem Dienst, mit
dem Sie über die Cloud Console mit Ihren GKE On-Prem-Clustern interagieren
können. Wenn Sie den neuen Connect-Agent verwenden möchten, müssen Sie Ihre
Cluster noch einmal in der Cloud Console registrieren oder auf Anthos GKE On-
Prem Beta-1.4 aktualisieren.

Ihre GKE On-Prem-Cluster und die darauf ausgeführten Arbeitslasten
funktionieren weiterhin ohne Unterbrechung. Ihre Cluster sind jedoch erst in
der Cloud Console sichtbar, wenn Sie sie neu registrieren oder ein Upgrade auf
Beta-1.4 ausführen.

Stellen Sie vor der erneuten Registrierung oder Aktualisierung sicher, dass
Ihr Dienstkonto die Rolle gkehub.connect hat. Wenn Ihr Dienstkonto außerdem
die alte Rolle clusterregistry.connect hat, sollten Sie diese Rolle auch
entfernen.

Gewähren Sie Ihrem Dienstkonto die Rolle "gkehub.connect":

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

Wenn Ihr Dienstkonto die alte Rolle clusterregistry.connect hat, entfernen Sie
die alte Rolle:

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/clusterregistry.connect"

Registrieren Sie den Cluster neu oder führen Sie ein Upgrade auf Anthos GKE
On-Prem-Beta-1.4 aus.

So [ registrieren Sie den Cluster noch einmal
](https://cloud.google.com/kubernetes-engine/connect/updating-agent?hl=de) :

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \
          --context=[USER_CLUSTER_CONTEXT] \
          --service-account-key-file=[LOCAL_KEY_PATH] \
          --kubeconfig-file=[KUBECONFIG_PATH] \
          --project=[PROJECT_ID]
          

[ Upgrade auf Anthos GKE On-Prem Beta-1.4:
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.4/how-
to/administration/upgrading-a-cluster?hl=de) :

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  Bekannte Probleme

**ISSUE:**

Aufgrund eines Problems kann der Connect-Agent während eines Upgrades nicht
auf die neue Version aktualisiert werden. Führen Sie nach dem Upgrade eines
Clusters den folgenden Befehl aus, um dieses Problem zu umgehen:

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  25\. April 2019

Die GKE On-Prem-Betaversion 1.3.1 ist jetzt verfügbar. Dieser Release enthält
die folgenden Änderungen:

###  Neue Funktionen

**FEATURE:**

Der ` gkectl diagnose snapshot ` -Befehl hat jetzt einen [ ` --dry-run `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.3/how-
to/administration/diagnose?hl=de#performing_a_dry_run_for_a_snapshot) -Flag.

**FEATURE:**

Der Befehl ` gkectl diagnose snapshot ` unterstützt jetzt vier [ Szenarien
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.3/how-
to/administration/diagnose?hl=de#snapshot_scenarios) .

**FEATURE:**

Der Befehl ` gkectl diagnose snapshot ` unterstützt jetzt reguläre Ausdrücke
zum Angeben von Namespaces.

###  Änderungen

**CHANGED:**

Istio 1.1 ist jetzt der standardmäßige [ Ingress-Controller
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.3/how-
to/administration/upgrading-a-cluster?hl=de#upgrading_the_ingress_controller)
. Der Ingress-Controller wird im ` gke-system ` -Namespace für Administrator-
und Nutzercluster ausgeführt. Dies ermöglicht eine einfachere TLS-Verwaltung
für Ingress. Um das Ingress-Verfahren zu aktivieren oder Ingress nach einem
Upgrade wieder zu aktivieren, folgen Sie der Anleitung unter [ Ingress
aktivieren ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/beta-1.3/how-to/installation/install?hl=de#enabling_ingress)
.

**CHANGED:**

Das ` gkectl ` -Tool verwendet für Bootstrapping nicht mehr Minikube oder KVM.
Dies bedeutet, dass Sie die verschachtelte Virtualisierung nicht auf der VM
Ihrer Administrator-Workstation aktivieren müssen.

###  Bekannte Probleme

**ISSUE:**

Der Ingress-Controller von GKE On-Prem verwendet Istio 1.1 mit automatischer
Secret-Erkennung. Der Knoten-Agent für die Secret-Erkennung kann jedoch nach
dem Löschen des Secrets keine Secret-Updates erhalten. Löschen Sie also keine
Secrets. Wenn Sie ein Secret löschen müssen und Ingress-TLS danach
fehlschlägt, starten Sie den Ingress-Pod im gke-system-Namespace manuell neu.

##  11\. April 2019

Die GKE On-Prem-Betaversion 1.2.1 ist jetzt verfügbar. Dieser Release enthält
die folgenden Änderungen:

###  Neue Funktionen

**FEATURE:**

GKE On-Prem-Cluster stellen jetzt über [ Connect
](https://cloud.google.com/kubernetes-engine/connect?hl=de) automatisch eine
Verbindung zu Google her.

**FEATURE:**

Sie können jetzt bis zu drei Steuerungsebenen pro Nutzercluster ausführen.

###  Änderungen

**CHANGED:**

` gkectl ` validiert jetzt vSphere- und F5 BIG-IP-Anmeldedaten, um Cluster zu
erstellen.

###  Bekannte Probleme

**ISSUE:**

Eine Regression führt dazu, dass ` gkectl diagnose snapshot ` -Befehle den
falschen SSH-Schlüssel verwenden. Dadurch wird verhindert, dass der Befehl
Informationen aus Nutzerclustern erfasst. Zur Umgehung von Supportfällen
müssen Sie möglicherweise eine SSH-Verbindung zu einzelnen Nutzerclusterknoten
herstellen und Daten manuell erfassen.

##  2\. April 2019

Die GKE On-Prem-Betaversion 1.1.1 ist jetzt verfügbar. Dieser Release enthält
die folgenden Änderungen:

###  Neue Funktionen

**FEATURE:**

Sie installieren GKE jetzt lokal mit einer [ Open Virtual Appliance (OVA)
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.1/how-
to/installation/getting-started?hl=de#download_ova) , einem vorkonfigurierten
VM-Image, das mehrere Befehlszeilentools enthält. Diese Änderung vereinfacht
die Installation und entfernt eine Virtualisierungsebene. Sie müssen ` gkectl
` nicht mehr in einem Docker-Container ausführen.

Wenn Sie GKE On-Prem-Versionen vor Beta-1.1.1 installiert haben, sollten Sie
eine neue Administrator-Workstation gemäß der dokumentierten Anleitung
erstellen. Kopieren Sie nach der Installation der neuen Administrator-
Workstation alle SSH-Schlüssel, Konfigurationsdateien, kubeconfigs und alle
anderen benötigten Dateien von Ihrer vorherigen Workstation auf die neue.

**FEATURE:**

Zusätzliche Dokumentation für die [ Sicherung und Wiederherstellung von
Clustern ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/beta-1.1/how-to/administration/backing-up?hl=de) .

**FEATURE:**

Sie können jetzt die Authentifizierung für Cluster mit OIDC und ADFS
konfigurieren. Weitere Informationen finden Sie unter [ Mit OIDC und ADFS
authentifizieren ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/beta-1.1/how-to/security/oidc-adfs?hl=de) und [
Authentifizierung ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/concepts/authentication?hl=de) .

###  Änderungen

**CHANGED:**

Sie müssen jetzt den privaten Schlüssel eines Administratorclusters verwenden,
um ` gkectl diagnose snapshot ` auszuführen.

**CHANGED:**

Während der Installation wurde eine Konfigurationsoption für die
Bereitstellung von Multi-Master-Nutzerclustern hinzugefügt.

**CHANGED:**

Die [ Connect-Dokumentation ](https://cloud.google.com/kubernetes-
engine/connect?hl=de) wurde migriert.

###  Korrekturen

**FIXED:**

Das Clusternetzwerk wurde unterbrochen, wenn ein Knoten unerwartet entfernt
wurde. Dieses Problem wurde behoben.

###  Bekannte Probleme

**ISSUE:**

Die Konfigurationsverwaltung von GKE On-Prem wurde von Version 0.11 auf 0.13
aktualisiert. Mehrere Komponenten des Systems wurden umbenannt. Sie müssen
einige Schritte ausführen, um die Ressourcen der vorherigen Versionen zu
bereinigen und eine neue Instanz zu installieren.

Wenn Sie eine aktive Instanz der Konfigurationsverwaltung haben:

  1. Deinstallieren Sie die Instanz: 
    
        kubectl -n=nomos-system delete nomos --all

  2. Gewährleisten Sie, dass der Namespace der Instanz keine Ressourcen enthält: 
    
        kubectl -n nomos-system get all

  3. Löschen Sie den Namespace: 
    
        kubectl delete ns nomos-system

  4. Löschen Sie die CRD: 
    
        kubectl delete crd nomos.addons.sigs.k8s.io

  5. Löschen Sie alle Kube-Systemressourcen für den Betreiber: 
    
        kubectl -n kube-system delete all -l k8s-app=nomos-operator

Wenn Sie keine aktive Instanz der Konfigurationsverwaltung haben:

  1. Löschen Sie den Konfigurationsmanager-Namespace: 
    
        kubectl delete ns nomos-system

  2. Löschen Sie die CRD: 
    
        kubectl delete crd nomos.addons.sigs.k8s.io

  3. Löschen Sie alle Kube-Systemressourcen für den Betreiber: 
    
        kubectl -n kube-system delete all -l k8s-app=nomos-operator

##  12\. März 2019

Die GKE On-Prem-Betaversion 1.0.3 ist jetzt verfügbar. Dieser Release enthält
die folgenden Änderungen:

###  Korrekturen

**FIXED:**

Das Problem, dass Docker-Zertifikate am falschen Speicherort gespeichert
wurden, wurde behoben.

##  4\. März 2019

Die GKE On-Prem-Betaversion 1.0.2 ist jetzt verfügbar. Dieser Release enthält
die folgenden Änderungen:

###  Neue Funktionen

**FEATURE:**

Sie können jetzt ` gkectl version ` ausführen, um zu prüfen, welche Version
von ` gkectl ` Sie ausführen.

**FEATURE:**

Sie können jetzt [ Nutzercluster auf zukünftige Betaversionen aktualisieren
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.0/how-
to/administration/upgrading-a-cluster?hl=de) .

**FEATURE:**

[ Anthos Config Management ](https://cloud.google.com/anthos-config-
management/docs?hl=de) Version 0.11.6 ist jetzt verfügbar.

**FEATURE:**

Stackdriver Logging ist jetzt auf jedem Knoten aktiviert. Standardmäßig
repliziert der Logging-Agent Logs für Ihr GCP-Projekt nur für
Steuerungsebenendienste, Cluster-API, vspare-Controller, Calico, BIG-IP-
Controller, Envoy-Proxy, Connect, Anthos Config Management, Prometheus und
Grafana, Steuerungsebene von Istio und Docker. Anwendungscontainerlogs sind
standardmäßig ausgeschlossen, können aber optional aktiviert werden.

**FEATURE:**

Stackdriver Prometheus-Sidecar erfasst Messwerte für dieselben Komponenten wie
der Logging-Agent.

**FEATURE:**

[ Kubernetes-Netzwerkrichtlinien
](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
werden jetzt unterstützt.

###  Änderungen

**CHANGED:**

Sie können jetzt IP-Blöcke in der Clusterspezifikation aktualisieren, um den
IP-Bereich für einen bestimmten Cluster zu erweitern.

**CHANGED:**

Wenn Cluster, die Sie in der Alphaphase installiert haben, nach der
Betaversion von Google getrennt wurden, müssen Sie sie möglicherweise noch
einmal verbinden. Weitere Informationen finden Sie unter [ Manuelles
Registrieren eines User-Clusters
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/registering-a-user-cluster?hl=de) .

**CHANGED:**

[ Einstieg ](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/getting-started?hl=de) wurde mit den Schritten zur Aktivierung
Ihres Dienstkontos und zur Ausführung von ` gkectl prepare ` aktualisiert.

**CHANGED:**

` gkectl diagnose snapshot ` erfasst jetzt nur Konfigurationsdaten und
schließt Logs aus. Mit diesem Tool werden Details zu Ihrer Umgebung erfasst,
bevor ein Supportfall geöffnet wird.

**CHANGED:**

Unterstützung für die optionale Konfiguration des SNAT-Pool-Namens für F5 BIG-
IP zum Zeitpunkt der Clustererstellung. Damit kann der Wert "--vs-snat-Pool-
Name" auf dem [ F5-BIG-IP-Controller
](https://clouddocs.f5.com/products/connectors/k8s-bigip-ctlr/v1.8/)
konfiguriert werden.

**CHANGED:**

Sie müssen nun einen VIP für Add-ons angeben, die im Administratorcluster
ausgeführt werden.

###  Korrekturen

**FIXED:**

Die Größenänderungsvorgänge für Cluster wurden verbessert, um ein
unbeabsichtigtes Löschen von Knoten zu verhindern.

##  07\. Februar 2019

Die lokale GKE-Alphaversion 1.3 ist jetzt verfügbar. Dieser Release enthält
die folgenden Änderungen:

###  Neue Funktionen

**FEATURE:**

Während der Installation können Sie jetzt YAML-Dateien mit ` nodeip ` -Blöcken
zur Konfiguration von statischem IPAM bereitstellen.

###  Änderungen

**CHANGED:**

Sie müssen nun ein Laufwerk mit 100 GB in vSphere Datastore bereitstellen. GKE
On-Prem verwendet das Laufwerk zum Speichern einiger wichtiger Daten, z. B.
etcd. Weitere Informationen finden Sie im Hilfeartikel [ Systemanforderungen
](https://cloud.google.com/anthos/gke/docs/on-prem/requirements?hl=de) .

**CHANGED:**

Sie können jetzt nur noch ` nodeip ` -Blöcke mit Hostnamen in Kleinbuchstaben
angeben.

**CHANGED:**

GKE On-Prem erzwingt nun eindeutige Namen für Nutzercluster.

**CHANGED:**

Messwertendpunkte und APIs, die Istio-Endpunkte verwenden, werden jetzt mit
mTLS und rollenbasierter Zugriffssteuerung gesichert.

**CHANGED:**

Die externe Kommunikation von Grafana ist deaktiviert.

**CHANGED:**

Verbesserungen bei der Systemdiagnose von Prometheus und Alertmanager.

**CHANGED:**

Prometheus verwendet jetzt einen sicheren Port zum Kopieren von Messwerten.

**CHANGED:**

Mehrere Updates zu Grafana-Dashboards

###  Bekannte Probleme

**ISSUE:**

Wenn Ihr vCenter-Nutzerkonto ein Format wie ` DOMAIN\USER ` verwendet, müssen
Sie möglicherweise den umgekehrten Schrägstrich ( ` DOMAIN\\USER ` ) mit
Escapezeichen versehen. Führen Sie diesen Schritt unbedingt aus, wenn Sie
während der Installation zur Eingabe des Nutzerkontos aufgefordert werden.

##  23\. Januar 2019

Die lokale GKE-Alphaversion 1.2.1 ist jetzt verfügbar. Dieser Release enthält
die folgenden Änderungen:

###  Neue Funktionen

**FEATURE:**

Sie können jetzt ` gkectl ` zum [ Löschen von Administratorclustern
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/deleting-an-admin-cluster?hl=de) verwenden.

###  Änderungen

**CHANGED:**

Mit ` gkectl diagnose snapshot ` -Befehlen können Sie jetzt Knoten angeben,
während Sie Snapshots von Remotebefehlsergebnissen und -dateien erfassen.

##  14\. Januar 2019

Die lokale GKE-Alphaversion 1.1.2 ist jetzt verfügbar. Diese Version enthält
die folgenden Änderungen:

###  Neue Funktionen

**FEATURE:**

Sie können jetzt den ` gkectl prepare ` -Befehl verwenden, um Container-Images
von GKE On-Prem per Pull und Push zu übertragen, wodurch das Skript `
populate_registry.sh ` eingestellt wird.

**FEATURE:**

` gkectl prepare ` fordert Sie nun zur Eingabe von Informationen zu Ihrem
vSphere-Cluster und -Ressourcenpool auf.

**FEATURE:**

Sie können jetzt den Befehl ` gkectl create ` verwenden, um Nutzercluster zu
erstellen und vorhandenen Administratorsteuerungsebenen hinzuzufügen, indem
Sie eine vorhandene kubeconfig-Datei übergeben, wenn Sie während der
Clustererstellung dazu aufgefordert werden.

**FEATURE:**

Sie können jetzt bei der Clustererstellung ein Ingress-TLS-Secret für
Administrator- und Nutzercluster übergeben. Die folgende neue
Eingabeaufforderung wird angezeigt:

` Do you want to use TLS for Admin Control Plane/User Cluster ingress? `

Wenn TLS-Secret und -Zertifikate bereitgestellt werden, kann ` gkectl ` das
Ingress-TLS einrichten. HTTP wird bei der TLS-Installation nicht automatisch
deaktiviert.

###  Änderungen

**CHANGED:**

GKE On-Prem führt jetzt die Kubernetes-Version **1.11.2-gke.19** aus.

**CHANGED:**

Der Standard-Footprint für GKE On-Prem hat sich geändert:

  * Die Mindestspeicheranforderung für Nutzerclusterknoten beträgt jetzt 8.192 Millionen. 

**CHANGED:**

GKE On-Prem führt jetzt die minikube-Version **0.28.0** aus.

**CHANGED:**

Der GKE-Richtlinienmanager wurde auf Version **0.11.1** aktualisiert.

**CHANGED:**

` gkectl ` fordert Sie nicht mehr auf, standardmäßig eine Proxykonfiguration
anzugeben.

**CHANGED:**

Im Nutzercluster-Namespace gibt es drei neue ConfigMap-Ressourcen: ` cluster-
api-etcd-metrics-config ` , ` kube-etcd-metrics-config ` und ` kube-apiserver-
config ` . GKE On-Prem verwendet diese Dateien, um den Proxy-Container mit
Messwerten schnell zu laden.

**CHANGED:**

"kube-apiserver" -Ereignisse befinden sich jetzt in einer eigenen etcd. Sie
können kube-etcd-Ereignisse im Namespace Ihres Nutzerclusters sehen.

**CHANGED:**

Cluster-API-Controller verwenden jetzt die Leader-Bestimmung.

**CHANGED:**

vSphere-Anmeldedaten werden jetzt aus Anmeldedatendateien abgerufen.

**CHANGED:**

` gkectl diagnose ` -Befehle funktionieren jetzt sowohl mit Administrator- als
auch mit Nutzerclustern.

**CHANGED:**

` gkectl diagnose snapshot ` kann jetzt Snapshots von Remote-Dateien auf dem
Knoten, Ergebnisse von Remote-Befehlen auf den Knoten und Prometheus-Abfragen
erstellen.

**CHANGED:**

` gkectl diagnose snapshot ` kann nun Snapshots in mehreren parallelen Threads
erstellen.

**CHANGED:**

Mit ` gkectl diagnose snapshot ` können Sie jetzt festlegen, welche Wörter aus
den Snapshot-Ergebnissen ausgeschlossen werden sollen.

###  Korrekturen

**FIXED:**

Probleme mit Minikube-Caching, die zu unerwarteten Netzwerkaufrufen geführt
haben, wurden behoben.

**FIXED:**

Ein Problem beim Abrufen von F5 BIG-IP-Anmeldedaten wurde behoben.
Anmeldedaten werden jetzt aus einer Datei mit Anmeldedaten anstelle von
Umgebungsvariablen gelesen.

###  Bekannte Probleme

**ISSUE:**

Die folgende [ ` govmomi ` ](https://github.com/vmware/govmomi) Warnung wird
möglicherweise angezeigt, wenn Sie ` gkectl prepare ` ausführen:

` Warning: Line 102: Unable to parse 'enableMPTSupport' for attribute 'key' on
element 'Config' `

**ISSUE:**

Das Ändern der Größe von Nutzerclustern kann zu einem versehentlichen Löschen
oder Neuerstellen von Knoten führen.

**ISSUE:**

PersistentVolumes können nicht bereitgestellt werden, was den Fehler `
devicePath is empty ` erzeugt. Als Behelfslösung können Sie den zugehörigen
PersistentVolumeClaim löschen und neu erstellen.

**ISSUE:**

Das Ändern der Größe von IPAM-Adressblöcken bei Verwendung der statischen IP-
Zuordnung für Knoten wird in der Alphaphase nicht unterstützt. Um dieses
Problem zu umgehen, sollten Sie mehr IP-Adressen zuweisen, als Sie derzeit
benötigen.

**ISSUE:**

Bei langsamen Laufwerken kann die VM-Erstellung Zeitüberschreitung haben und
zum Fehlschlagen der Bereitstellung führen. Löschen Sie in diesem Fall alle
Ressourcen und versuchen Sie es noch einmal.

##  19\. Dezember 2018

GKE On-Prem Alpha 1.0.4 ist jetzt verfügbar. Diese Version enthält die
folgenden Änderungen:

###  Korrekturen

**FIXED:**

Die durch [ CVE-2018-1002105
](https://github.com/kubernetes/kubernetes/issues/71411) verursachte
Sicherheitslücke wurde behoben.

##  30\. November 2018

GKE On-Prem Alpha 1.0 ist jetzt verfügbar. Die folgenden Änderungen sind in
dieser Version enthalten:

###  Änderungen

**CHANGED:**

GKE On-Prem-Alphaversion 1.0 führt Kubernetes 1.11 aus.

**CHANGED:**

Der Standard-Footprint für GKE On-Prem hat sich geändert:

  * Die Administrator-Steuerungsebene führt drei Knoten aus, die 4 CPUs und 16 GB Arbeitsspeicher verwenden. 
  * Die Nutzersteuerungsebene führt einen Knoten mit 4 CPUs und 16 GB Arbeitsspeicher aus. 
  * Nutzercluster führen mindestens drei Knoten aus, die 4 CPUs und 16 GB Speicher belegen. 

**CHANGED:**

Unterstützung für die Prometheus-Einrichtung mit Hochverfügbarkeit.

**CHANGED:**

Unterstützung für benutzerdefinierte Alert Manager-Konfiguration.

**CHANGED:**

Prometheus wurde von **2.3.2** auf **2.4.3** aktualisiert.

**CHANGED:**

Grafana wurde von **5.0.4** auf **5.3.4** aktualisiert.

**CHANGED:**

Kube-state-metrics wurde von **1.3.1** auf **1.4.0** aktualisiert.

**CHANGED:**

Alert Manager wurde von **1.14.0** auf **1.15.2** aktualisiert.

**CHANGED:**

Node_exporter wurde von **1.15.2** auf **1.16.0** aktualisiert.

###  Korrekturen

**FIXED:**

Die durch [ CVE-2018-1002103
](https://github.com/kubernetes/minikube/issues/3208) verursachte
Sicherheitslücke wurde behoben.

###  Bekannte Probleme

**ISSUE:**

PersistentVolumes können nicht bereitgestellt werden, was den Fehler `
devicePath is empty ` erzeugt. Als Behelfslösung können Sie den zugehörigen
PersistentVolumeClaim löschen und neu erstellen.

**ISSUE:**

Das Ändern der Größe von IPAM-Adressblöcken bei Verwendung der statischen IP-
Zuordnung für Knoten wird in der Alphaphase nicht unterstützt. Um dieses
Problem zu umgehen, sollten Sie mehr IP-Adressen zuweisen, als Sie derzeit
benötigen.

**ISSUE:**

GKE On-Prem-Alphaversion 1.0 erfüllt noch nicht alle Konformitätstests.

**ISSUE:**

Pro Administratorcluster kann nur ein Nutzercluster erstellt werden. Wenn Sie
zusätzliche Nutzercluster erstellen möchten, erstellen Sie einen weiteren
Administratorcluster.

##  31\. Oktober 2018

GKE lokal EAP 2.1 ist jetzt verfügbar. Die folgenden Änderungen sind in dieser
Version enthalten:

###  Änderungen

**CHANGED:**

Wenn Sie gleichzeitig Administrator- und Nutzercluster erstellen, können Sie
die F5 BIG-IP-Anmeldedaten des Administratorclusters wiederverwenden, um den
Nutzercluster zu erstellen. Außerdem erfordert die Befehlszeile jetzt die
Bereitstellung von BIG-IP-Anmeldedaten. Diese Anforderung kann mit ` --dry-run
` nicht übersprungen werden.

**CHANGED:**

F5 BIG-IP-Controller wurde auf die neueste OSS-Version 1.7.0 aktualisiert.

**CHANGED:**

Zur Verbesserung der Stabilität bei langsamen vSphere-Maschinen beträgt das
Zeitlimit für die Erstellung von Clustermaschinen jetzt 15 Minuten (vorher
fünf Minuten).

##  17\. Oktober 2018

GKE On-Premises EAP 2.0 ist jetzt verfügbar. Die folgenden Änderungen sind in
dieser Version enthalten:

###  Änderungen

**CHANGED:**

Support für GKE Connect.

**CHANGED:**

Support für Monitoring.

**CHANGED:**

Support für die Installation mit privaten Registrys.

**CHANGED:**

Support für das Front-End des L7-Load-Balancers als L4-VIP auf F5 BIG-IP.

**CHANGED:**

Support der statischen IP-Zuordnung für Knoten während des Cluster-Bootstraps.

###  Bekannte Probleme

**ISSUE:**

Pro Administratorcluster kann nur ein Nutzercluster erstellt werden. Wenn Sie
zusätzliche Nutzercluster erstellen möchten, erstellen Sie einen weiteren
Administratorcluster.

**ISSUE:**

Clusterupgrades werden in EAP 2.0 nicht unterstützt.

**ISSUE:**

Bei langsamen Laufwerken kann die VM-Erstellung Zeitüberschreitung haben und
zum Fehlschlagen der Bereitstellung führen. Löschen Sie in diesem Fall alle
Ressourcen und versuchen Sie es noch einmal.

**ISSUE:**

Im Rahmen des Cluster-Bootstrapping-Prozesses wird eine kurzlebigere Minikube-
Instanz ausgeführt. Die verwendete Minikube-Version hat die Sicherheitslücke [
CVE-2018-1002103 ](https://github.com/kubernetes/minikube/issues/3208) .

