#  Sicherheitsbulletins

In diesem Thema werden alle Sicherheitsbulletins für Google Kubernetes Engine
(GKE) beschrieben.

Sicherheitslücken werden häufig geheim gehalten, bis die betroffenen Parteien
die Möglichkeit hatten, sie zu beheben. In diesen Fällen wird in den [
Versionshinweisen ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=de) von GKE von "Security Updates" (Sicherheitsupdates) gesprochen,
bis die Geheimhaltungsverpflichtung aufgehoben wurde. Sobald das geschehen
ist, werden die Hinweise mit Informationen über die durch den Patch behobene
Sicherheitslücke aktualisiert.

**Hinweis** : Diese Sicherheitsbulletins sind insbesondere dann zu beachten,
wenn Sie Arbeitslasten für mehrere Mandanten in GKE ausführen. Bei ihnen ist
die Wahrscheinlichkeit größer, dass sie durch diese Sicherheitslücken
gefährdet sind. Eine technische Beschreibung der Sicherheitsgrenzen in GKE und
deren Auswirkungen auf Arbeitslasten finden Sie unter [ Isolation at different
layers of the Kubernetes stack
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) .

Fügen Sie die URL dieser Seite in den [ Feedreader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ein oder fügen
Sie die Feed-URL direkt hinzu, um die neuesten Sicherheitsbulletins zu
erhalten: ` https://cloud.google.com/feeds/kubernetes-engine-security-
bulletins.xml `

##  GCP-2020-011

**Veröffentlicht:** 24.7.2020  
Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
Bei Kubernetes wurde vor Kurzem eine Sicherheitslücke im Netzwerk, [
CVE-2020-8558 ](https://github.com/kubernetes/kubernetes/issues/92315) ,
entdeckt. Dienste kommunizieren manchmal über die lokale Loopback-
Schnittstelle (127.0.0.1) mit anderen Anwendungen, die im gleichen Pod
ausgeführt werden. Diese Sicherheitslücke ermöglicht einem Angreifer mit
Zugriff auf das Netzwerk des Clusters, Traffic an die Loopback-Schnittstelle
von angrenzenden Pods und Knoten zu senden. Dienste, die darauf angewiesen
sind, dass die Loopback-Schnittstelle außerhalb ihres Pods nicht zugänglich
ist, könnten ausgenutzt werden.

Um diese Sicherheitslücke in GKE-Clustern auszunutzen, benötigt ein Angreifer
Netzwerkadministratorrechte in der Google Cloud, die die VPC des Clusters
hostet. Diese Sicherheitslücke allein gewährt einem Angreifer keine
Netzwerkadministratorberechtigungen. Aus diesem Grund wurde dieser
Sicherheitslücke in GKE ein niedriger Schweregrad zugewiesen.

####  Was soll ich tun?

[ Aktualisieren ](https://cloud.google.com/kubernetes-
engine/docs/concepts/cluster-upgrades?hl=de) Sie die Knotenpools Ihres
Clusters auf die folgenden GKE-Versionen (und höher), um diese
Sicherheitslücke zu beheben:

  * 1.17.7-gke.0 
  * 1.16.11-gke.0 
  * 1.16.10-gke.11 
  * 1.16.9-gke.14 

####  Welche Sicherheitslücke wird mit diesem Patch behoben?

Mit diesem Patch wird die folgende Sicherheitslücke behoben: [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) .

|

Min.

|

[ CVE-2020-8558 ](https://github.com/kubernetes/kubernetes/issues/92315)  
  
##  GCP-2020-009

**Veröffentlicht:** 15.7.2020  Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
Kürzlich wurde in Kubernetes eine Sicherheitslücke zur Rechteausweitung, [
CVE-2020-8559 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8559)
, ermittelt. Diese Sicherheitslücke ermöglicht es einem Angreifer, der bereits
einen Knoten manipuliert hat, in jedem Pod im Cluster einen Befehl
auszuführen. Der Angreifer kann dadurch mit dem bereits manipulierten Knoten
andere Knoten manipulieren und potenziell Informationen lesen oder schädigende
Aktionen ausführen.

Damit ein Angreifer diese Sicherheitslücke nutzen kann, muss bereits ein
Knoten im Cluster manipuliert worden sein. Diese Sicherheitslücke allein
beeinträchtigt also noch keine Knoten in Ihrem Cluster.

####  Was soll ich tun?

Führen Sie ein [ Upgrade ](https://cloud.google.com/kubernetes-
engine/docs/concepts/cluster-upgrades?hl=de) des Clusters auf eine gepatchte
Version durch. Die Cluster werden in den nächsten Wochen automatisch
aktualisiert. Patchierte Versionen sind am 19. Juli 2020 für einen
beschleunigten manuellen Upgradezeitplan verfügbar. Die folgenden Versionen
der GKE-Steuerungsebene enthalten die Fehlerkorrektur für diese
Sicherheitslücke:

  * v1.14.10-gke.46 
  * v1.15.12-gke.8 
  * v1.16.9-gke.11 
  * v1.16.10-gke.9 
  * v1.16.11-gke.3+ 
  * v1.17.7-gke.6+ 

####  Welche Sicherheitslücke wird mit diesem Patch behoben?

Diese Patches beheben die Sicherheitslücke CVE-2020-8559. Diese
Sicherheitslücke von GKE wird mit dem Schweregrad "Mittel" eingestuft, da der
Angreifer Informationen aus erster Hand über den Cluster, die Knoten und
Arbeitslasten benötigt, um diesen Angriff wirksam zu nutzen, wenn bereits ein
anderer Knoten manipuliert wurde. Diese Sicherheitslücke selbst bietet dem
Angreifer keinen manipulierten Knoten.

|

Mittel

|

[ CVE-2020-8559 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8559)  
  
##  GCP-2020-007

**Veröffentlicht:** 01.06.2020  
Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
Serverseitige Anfragefälschung (Server Side Request Forgery, SSRF), [
CVE-2020-8555 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555)
, wurde kürzlich in Kubernetes entdeckt und ermöglicht bestimmten
autorisierten Nutzern, bis zu 500 Byte vertraulicher Informationen aus dem
Hostnetzwerk der Steuerungsebene abzurufen. Die Google Kubernetes Engine-
Steuerungsebene (GKE) verwendet Controller von Kubernetes und ist daher von
dieser Sicherheitslücke betroffen. Wir empfehlen Ihnen, die Steuerungsebene
wie unten beschrieben [ auf die neueste Patchversion zu aktualisieren
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=de) . Ein Knotenupgrade ist nicht erforderlich.  

####  Was soll ich tun?

Bei den meisten Kunden sind keine weiteren Maßnahmen erforderlich. Die
überwiegende Mehrheit der Cluster führt bereits eine Patchversion aus. Bei den
folgenden GKE-Versionen sowie alle neueren Versionen wurde diese
Sicherheitslücke behoben:

  * 1.14.7-gke.39 
  * 1.14.8-gke.32 
  * 1.14.9-gke.17 
  * 1.14.10-gke.12 
  * 1.15.7-gke.17 
  * 1.16.4-gke.21 
  * 1.17.0-gke.0 

Cluster mit [ Release-Versionen ](https://cloud.google.com/kubernetes-
engine/docs/concepts/release-channels?hl=de) verwenden bereits Versionen der
Steuerungsebene mit Risikominderung.

####  Welche Sicherheitslücke wird mit diesem Patch behoben?

Diese Patches beheben die Sicherheitslücke CVE-2020-8555. Diese
Sicherheitslücke wird in GKE mit dem Schweregrad "Mittel" bewertet, da sie
aufgrund verschiedener Härtungsmaßnahmen der Steuerungsebene nur schwer
ausgenutzt werden konnte.

Ein Angreifer mit Berechtigungen zum Erstellen eines Pods mit bestimmten
integrierten Volume-Typen (GlusterFS, Quobyte, StorageFS, ScaleIO) oder
Berechtigungen zum Erstellen einer StorageClass kann ` kube-controller-manager
` dazu veranlassen, ` GET ` -Anfragen oder ` POST ` -Anfragen _ohne_ von ihm
kontrolliertem Anfragetext über das Master-Hostnetzwerk zu senden. Diese
Volume-Typen werden selten auf GKE verwendet. Neue Nutzungsfälle dieser
Volume-Typen können also ein hilfreiches Signal zur Angriffserkennung sein.

Wird der Angriff mit einer Methode kombiniert, um die Ergebnisse von `
GET/POST ` beispielsweise durch Logs zurück an den Angreifer zu senden, kann
das zur Offenlegung von vertraulichen Informationen führen. Wir haben die
entsprechenden Speichertreiber aktualisiert, um das Risiko von Schwachstellen
zu beheben.

|

Mittel

|

[ CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555)  
  
##  GCP-2020-006

**Veröffentlicht:** 01.06.2020  
Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
Kubernetes hat eine [ Sicherheitslücke
](https://github.com/kubernetes/kubernetes/issues/91507) entdeckt, die es
einem berechtigten Container ermöglicht, Knoten-Traffic an einen anderen
Container weiterzuleiten. Gegenseitiger TLS/SSH-Traffic, z. B. zwischen dem
Kubelet und dem API-Server oder Traffic von Anwendungen, die mTLS verwenden,
kann durch diesen Angriff nicht gelesen oder geändert werden. Alle GKE-Knoten
(Google Kubernetes Engine) sind von dieser Sicherheitslücke betroffen. Wir
empfehlen Ihnen, ein [ Upgrade auf die neueste Patchversion
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=de) durchzuführen.

####  Was soll ich tun?

Sie können als Gegenmaßnahme für diese Sicherheitslücke [ ein Upgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=de) Ihrer Steuerungsebene durchführen. Aktualisieren Sie dann Ihre
Knoten auf eine der unten aufgelisteten Patchversionen. Cluster mit Release-
Versionen führen sowohl auf der Steuerungsebene als auch auf Knoten bereits
Patchversionen aus:

  * 1.14.10-gke.36 
  * 1.15.11-gke.15 
  * 1.16.8-gke.15 

Sehr wenige Container benötigen normalerweise ` CAP_NET_RAW ` . Diese und
andere leistungsstarke Funktionen sollten standardmäßig durch [
PodSecurityPolicy-Controller ](https://cloud.google.com/kubernetes-
engine/docs/how-to/pod-security-policies?hl=de) oder [ Anthos Policy
Controller ](https://cloud.google.com/anthos-config-
management/docs/concepts/policy-controller?hl=de) blockiert werden.

  * So entfernen Sie die ` CAP_NET_RAW ` -Funktion aus Containern: 
    * Durch Erzwingung mit [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=de) : 
        
                
        # Require dropping CAP_NET_RAW with a PSP
        apiversion: extensions/v1beta1
        kind: PodSecurityPolicy
        metadata:
          name: no-cap-net-raw
        spec:
          requiredDropCapabilities:
            -NET_RAW
             ...
             # Unrelated fields omitted
        

    * Durch Verwendung von Anthos Policy Controller/Gatekeeper mit dieser [ Einschränkungsvorlage ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) und Anwendung der Vorlage. Beispiel: 
        
                
        # Dropping CAP_NET_RAW with Gatekeeper
        # (requires the K8sPSPCapabilities template)
        apiversion: constraints.gatekeeper.sh/v1beta1
        kind:  K8sPSPCapabilities
        metadata:
          name: forbid-cap-net-raw
        spec:
          match:
            kinds:
              - apiGroups: [""]
              kinds: ["Pod"]
            namespaces:
              #List of namespaces to enforce this constraint on
              - default
            # If running gatekeeper >= v3.1.0-beta.5,
            # you can exclude namespaces rather than including them above.
            excludedNamespaces:
              - kube-system
          parameters:
            requiredDropCapabilities:
              - "NET_RAW"
        

    * Durch Aktualisieren der Pod-Spezifikationen: 
        
                
        # Dropping CAP_NET_RAW from a Pod:
        apiVersion: v1
        kind: Pod
        metadata:
          name: no-cap-net-raw
        spec:
          containers:
            -name: may-container
             ...
            securityContext:
              capabilities:
                drop:
                  -NET_RAW
        

####  Welche Sicherheitslücke wird mit diesem Patch behoben?

Dieser Patch dient zur Entschärfung der folgenden Sicherheitslücke:

Die Sicherheitslücke, die unter [ Kubernetes-Problem 91507
](https://github.com/kubernetes/kubernetes/issues/91507) beschrieben ist.
Dabei kann die ` CAP_NET_RAW ` -Funktion (im standardmäßigen Container-
Funktionsset enthalten) den IPv6-Stack auf dem Knoten schädlich konfigurieren
und den Knoten-Traffic an den vom Angreifer kontrollierten Container
weiterleiten. Dadurch kann der Angreifer ausgehenden und eingehenden Traffic
des Knotens abfangen und ändern. Gegenseitiger TLS/SSH-Traffic, z. B. zwischen
dem Kubelet und dem API-Server oder Traffic von Anwendungen, die mTLS
verwenden, kann durch diesen Angriff nicht gelesen oder geändert werden.

|

Mittel

|

[ Kubernetes-Problem 91507
](https://github.com/kubernetes/kubernetes/issues/91507)  
  
  
##  GCP-2020-005

**Veröffentlicht:** 07.05.2020  
**Zuletzt aktualisiert:** 07.05.2020  Beschreibung  |  Schweregrad  |
Hinweise  
---|---|---  
  
Vor Kurzem wurde im Linux-Kernel eine Sicherheitslücke entdeckt, die unter [
CVE-2020-8835 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8835)
beschrieben wird. Sie ermöglicht Container-Escape, um Root-Berechtigungen auf
dem Hostknoten zu erhalten.

GKE-Ubuntu-Knoten (Google Kubernetes Engine) mit GKE 1.16 oder 1.17 sind von
dieser Sicherheitslücke betroffen. Wir empfehlen Ihnen, so bald wie möglich
wie unten beschrieben ein Upgrade auf die neueste Patchversion durchzuführen.

Knoten mit Container-Optimized OS sind nicht betroffen. Knoten, die auf GKE
On-Prem ausgeführt werden, sind nicht betroffen.

####  Was soll ich tun?

**Bei den meisten Kunden sind keine weiteren Maßnahmen erforderlich. Nur GKE-
Ubuntu-Knoten mit GKE 1.16 oder 1.17 sind betroffen.**

Führen Sie zuerst ein Upgrade auf die neueste Version für den Master durch.
Dieser Patch ist in Kubernetes 1.16.8-gke.12, 1.17.4-gke.10 und neueren
Releases verfügbar. Informationen zur Verfügbarkeit der Patches finden Sie in
den [ Versionshinweisen ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=de) .

####  Welche Sicherheitslücke wird mit diesem Patch behoben?

Dieser Patch dient zur Entschärfung der folgenden Sicherheitslücke:

In [ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) wird eine Sicherheitslücke in der Linux
Kernel-Version 5.5.0 und neueren Versionen beschrieben, die es einem
schädlichen Container mit minimaler Nutzerinteraktion in Form eines
ausführbaren Befehls ermöglicht, Lese- und Schreibvorgänge im Kernel-Speicher
durchzuführen und so auf dem Hostknoten Code auf Root-Ebene auszuführen. Der
Schweregrad dieser Sicherheitslücke ist "Hoch".

|

Hoch

|

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835)  
  
  
##  GCP-2020-003

**Veröffentlicht:** 31.03.2020  
**Zuletzt aktualisiert:** 31.03.2020  Beschreibung  |  Schweregrad  |
Hinweise  
---|---|---  
  
In Kubernetes wurde kürzlich eine in [ CVE-2019-11254
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11254) beschriebene
Sicherheitslücke festgestellt. Sie erlaubt Nutzern, die POST-Anfragen stellen
dürfen, DoS-Remoteangriffe auf Kubernetes API-Server. Das Kubernetes Product
Security Committee (PSC) hat [ zusätzliche Informationen
](https://groups.google.com/forum/?hl=de#!topic/kubernetes-security-
announce/wuwEwZigXBc) zu dieser Sicherheitslücke veröffentlicht.

In GKE-Clustern, die [ autorisierte Masternetzwerke
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=de) verwenden, und [ privaten Clustern ohne öffentlichen Endpunkt
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=de#private_master) tritt diese Sicherheitslücke seltener auf.

####  Was soll ich tun?

Wir empfehlen ein Upgrade Ihres Clusters auf eine Patchversion, mit der diese
Sicherheitslücke behoben wird.

Die Patchversionen, mit denen die Sicherheitslücke behoben wird, sind unten
aufgeführt:

  * 1.13.12-gke.29 
  * 1.14.9-gke.27 
  * 1.14.10-gke.24 
  * 1.15.9-gke.20 
  * 1.16.6-gke.1 

####  Welche Sicherheitslücken werden mit diesem Patch behoben?

Mit dem Patch wird die folgende DoS-Sicherheitslücke (Denial of Service)
behoben:

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)

|

Mittel

|

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  GCP-2020-002

**Veröffentlicht:** 23.03.2020  
**Zuletzt aktualisiert:** 23.03.2020  Beschreibung  |  Schweregrad  |
Hinweise  
---|---|---  
  
Es wurden [ zwei DoS-Sicherheitslücken
](https://groups.google.com/forum/?hl=de#!topic/kubernetes-security-
announce/2UOlsba2g0s) in Kubernetes offengelegt. Die eine betrifft den API-
Server, die andere Kubelets. Weitere Einzelheiten finden Sie in den
Kubernetes-Problemen [ 89377
](https://github.com/kubernetes/kubernetes/issues/89377) und [ 89378
](https://github.com/kubernetes/kubernetes/issues/89378) .

####  Was soll ich tun?

GKE-Nutzer sind vor CVE-2020-8551 geschützt, sofern nur vertrauenswürdige
Nutzer Anfragen innerhalb des internen Netzwerks des Clusters senden dürfen.
Bei Verwendung [ autorisierter Masternetzwerke
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=de) tritt CVE-2020-8552 außerdem seltener auf.

####  Wann gibt es einen Patch?

Patches für CVE-2020-8551 erfordern ein Upgrade des Knotens. Die
Patchversionen, mit denen die Sicherheitslücke entschärft wird, sind unten
aufgeführt:

  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

Hinweis: Version 1.14.x und früher sind von der Sicherheitslücke nicht
betroffen und benötigen keine Patches.

Patches für CVE-2020-8552 erfordern ein Masterupgrade. Die Patchversionen, mit
denen die Sicherheitslücke entschärft wird, sind unten aufgeführt:

  * 1.14.10-gke.32 
  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

|

Mittel

|

[ CVE-2020-8551 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8551)  
[ CVE-2020-8552 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8552)  
  
##  21\. Januar 2020; zuletzt aktualisiert am 24. Januar 2020

**Veröffentlicht:** 21.01.2020  
**Zuletzt aktualisiert:** 24.01.2020  Beschreibung  |  Schweregrad  |
Hinweise  
---|---|---  
  
**Aktualisierung vom 24. Januar 2020:** Die Einführung von Patchversionen hat
bereits begonnen und wird bis zum 25. Januar 2020 abgeschlossen.

* * *

Microsoft hat eine Sicherheitslücke in der Windows Crypto API und ihrer
Validierung von Elliptische-Kurven-Signaturen offengelegt. Weitere
Informationen finden Sie in der [ Offenlegung von Microsoft
](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) .

**Was soll ich tun?**

**Bei den meisten Kunden sind keine weiteren Maßnahmen erforderlich. Es sind
nur Knoten betroffen, die Windows Server ausführen.**

Kunden, die Windows Server-Knoten verwenden, müssen sowohl die Knoten als auch
die containerisierten Arbeitslasten, die auf diesen Knoten ausgeführt werden,
auf gepatchte Versionen aktualisieren, um diese Sicherheitslücke zu
verringern.

**So aktualisieren Sie die Container:**

Erstellen Sie Ihre Container mit den aktuellen Basis-Container-Images von
Microsoft und wählen Sie dabei ein [ servercore
](https://hub.docker.com/_/microsoft-windows-servercore) \- oder [ nanoserver
](https://hub.docker.com/_/microsoft-windows-nanoserver) -Tag mit LastUpdated-
Zeit vom 14. Januar 2020 oder später aus.

**So aktualisieren Sie die Knoten:**

Die Einführung von Patchversionen hat bereits begonnen und wird bis zum 24.
Januar 2020 abgeschlossen.

Sie können entweder bis zu diesem Zeitpunkt warten und ein Knotenupgrade für
eine GKE-Patchversion vornehmen oder mit Windows Update jederzeit den
aktuellen Windows-Patch manuell bereitstellen.

Die Sicherheitslücke wurde in folgenden Patchversionen entschärft:

  * 1.14.7-gke.40 
  * 1.14.8-gke.33 
  * 1.14.9-gke.23 
  * 1.14.10-gke.17 
  * 1.15.7-gke.23 
  * 1.16.4-gke.22 

**Welche Sicherheitslücken werden mit diesem Patch behoben?**

Dieser Patch dient zur Entschärfung der folgenden Sicherheitslücken:

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601) – Diese Sicherheitslücke wird auch als [
Windows Crypto API-Spoofing-Sicherheitslücke
](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) bezeichnet. Sie könnte dazu genutzt werden,
bösartige ausführbare Dateien vertrauenswürdig zu machen oder dem Angreifer
Man-in-the-Middle-Angriffe zu ermöglichen und vertrauliche Informationen über
TLS-Nutzerverbindungen mit der betroffenen Software zu entschlüsseln.

|

NVD Base Score: 8,1 (hoch)

|

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601)  
  
  
##  14\. November 2019

**Veröffentlicht:** 14.11.2019  
**Zuletzt aktualisiert:** 14.11.2019  Beschreibung  |  Schweregrad  |
Hinweise  
---|---|---  
  
Kubernetes hat in den Sidecar-Containern [ ` external-provisioner `
](https://github.com/kubernetes-csi/external-provisioner) , [ ` external-
snapshotter ` ](https://github.com/kubernetes-csi/external-snapshotter) und [
` external-resizer ` ](https://github.com/kubernetes-csi/external-resizer) für
kubernetes-csi ein Sicherheitsproblem festgestellt, das die meisten Versionen
der in [ Container Storage Interface-Treibern (CSI) ](https://kubernetes-
csi.github.io/docs/drivers.html) gebündelten Sidecar-Container betrifft.
Weitere Informationen erhalten Sie in der [ Mitteilung zu Kubernetes
](https://github.com/kubernetes/kubernetes/issues/85233) .

**Was soll ich tun?**  
**Diese Sicherheitslücke wirkt sich nicht auf verwaltete GKE-Komponenten
aus.** Sie können betroffen sein, wenn Sie Ihre eigenen CSI-Treiber in [ GKE
Alpha-Clustern ](https://cloud.google.com/kubernetes-
engine/docs/concepts/alpha-clusters?hl=de) verwalten, in denen GKE Version
1.12 oder höher ausgeführt wird. Wenden Sie sich in diesem Fall bezüglich
einer Upgrade-Anleitung an Ihren CSI-Treiberanbieter.

**Welche Sicherheitslücken werden mit diesem Patch behoben?**  
[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255) : Diese CVE-Sicherheitslücke tritt in den
Sidecar-Containern [ ` external-provisioner ` ](https://github.com/kubernetes-
csi/external-provisioner) , [ ` external-snapshotter `
](https://github.com/kubernetes-csi/external-snapshotter) und [ ` external-
resizer ` ](https://github.com/kubernetes-csi/external-resizer) für `
kubernetes-csi ` auf. Sie kann zu nicht autorisierten Datenzugriffen und
Änderungen führen. Das betrifft die meisten Versionen der in [ CSI-Treibern
](https://kubernetes-csi.github.io/docs/drivers.html) gebündelten Sidecar-
Container.

|

Mittel

|

[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255)  
  
  
##  12\. November 2019

**Veröffentlicht:** 12.11.2019  
**Zuletzt aktualisiert:** 12.11.2019  Beschreibung  |  Schweregrad  |
Hinweise  
---|---|---  
  
Intel hat CVE-Sicherheitslücken festgestellt, bei denen Daten Angriffen
ausgesetzt sein können, die durch Interaktion einer spekulativen Ausführung
mit dem mikroarchitektonischen Status erfolgen. Weitere Informationen erhalten
Sie in folgendem [ Intel-Blog
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) .

**In der Hostinfrastruktur, in der Kubernetes Engine ausgeführt wird, werden
Arbeitslasten von Kunden isoliert. Keine weiteren Maßnahmen sind erforderlich,
es sei denn, Sie führen nicht vertrauenswürdigen Code in Ihren eigenen GKE-
Clustern für mehrere Mandanten aus _und_ verwenden N2-, M2- oder C2-Knoten. **
Für GKE-Instanzen auf N1-Knoten sind keine neuen Maßnahmen erforderlich.

Bei lokaler Ausführung von Anthos GKE hängt die Anfälligkeit von der Hardware
ab. Bitte prüfen Sie in folgendem [ Intel-Blog
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) , ob Ihre Infrastruktur betroffen ist.

####  Was soll ich tun?

**Sie sind nur betroffen, wenn Sie Knotenpools mit N2-, M2- oder C2-Knoten
verwenden _und_ wenn diese Knoten in Ihren eigenen GKE-Clustern für mehrere
Mandanten nicht vertrauenswürdigen Code ausführen. **

**Starten Sie Ihre Knoten neu, damit der Patch angewendet wird.** Am
einfachsten starten Sie alle Knoten in Ihrem Knotenpool mit dem [ Upgrade-
Vorgang ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=de#upgrade_nodes) neu. Sie erzwingen dadurch den Neustart aller
Knoten im betroffenen Knotenpool.  

Hinweis: Während eines Upgrades ist keine Versionsänderung erforderlich. Mit
dem Flag ` cluster-version ` können Sie ein Upgrade auf dieselbe Knotenversion
starten.

####  Welche Sicherheitslücken werden mit diesem Patch behoben?

Dieser Patch dient zur Entschärfung der folgenden Sicherheitslücken:

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)
: Diese CVE-Sicherheitslücke wird auch als TSX Async Abort (TAA) bezeichnet.
TAA bietet einen anderen Pfad für die Daten-Exfiltration mit denselben
mikroarchitektonischen Datenstrukturen, die auch durch [ Microarchitectural
Data Sampling (MDS) ](https://cloud.google.com/kubernetes-
engine/docs/security-bulletins?hl=de#may-14-2019) gefährdet waren.

[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)
: Das ist eine DoS-Sicherheitslücke (Denial of Service) auf VM-Hosts, über die
ein schädlicher Gast einen ungeschützten Host zum Absturz bringen kann. Diese
CVE-Sicherheitslücke wird auch als "Machine Check Error on Page Size Change"
bezeichnet. Das betrifft nicht GKE.

|

Mittel

|

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)  
[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)  
  
##  22\. Oktober 2019

**Veröffentlicht:** 22.10.2019  
**Zuletzt aktualisiert:** 22.10.2019  Beschreibung  |  Schweregrad  |
Hinweise  
---|---|---  
  
Im Zusammenhang mit der Programmiersprache Go wurde kürzlich eine in [
CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276) beschriebene Sicherheitslücke
festgestellt. Sie kann sich auf Kubernetes-Konfigurationen auswirken, die
einen Authentifizierungsproxy verwenden. Weitere Informationen erhalten Sie in
der [ Mitteilung zu Kubernetes
](https://groups.google.com/forum/?hl=de#!topic/kubernetes-security-
announce/PtsUCqFi4h4) .

Da Kubernetes Engine keine Konfiguration eines Authentifizierungsproxys
zulässt, ist es nicht von dieser Sicherheitslücke betroffen.

|

Kein Flag

|

[ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276)  
  
  
##  16\. Oktober 2019

**Veröffentlicht:** 16.10.2019  
**Zuletzt aktualisiert:** 24.10.2019  Beschreibung  |  Schweregrad  |
Hinweise  
---|---|---  
  
**Aktualisierung vom 24. Oktober 2019** : Ab sofort sind in allen Zonen
Patchversionen verfügbar.

* * *

In Kubernetes wurde kürzlich eine in [ CVE-2019-11253
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253) beschriebene
Sicherheitslücke festgestellt. Sie erlaubt Nutzern, die POST-Anfragen stellen
dürfen, DoS-Remoteangriffe auf Kubernetes API-Server. Das Kubernetes Product
Security Committee (PSC) hat [ zusätzliche Informationen
](https://groups.google.com/forum/?hl=de#!topic/kubernetes-security-
announce/jk8polzSUxs) zu dieser Sicherheitslücke veröffentlicht.

In GKE-Clustern, die [ autorisierte Masternetzwerke
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=de) verwenden, und [ privaten Clustern ohne öffentlichen Endpunkt
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=de#private_master) tritt diese Sicherheitslücke seltener auf.

######  Was soll ich tun?

Wir empfehlen ein Upgrade Ihrer Cluster auf eine Patchversion, die den Fehler
behebt, sobald sie verfügbar ist. Patchversionen in allen Zonen werden
voraussichtlich mit dem für die Woche vom 14. Oktober geplanten GKE-Release
bereitgestellt.

Die Patchversionen, mit denen die Sicherheitslücke entschärft wird, sind unten
aufgeführt.

  * 1.12.10-gke.15 
  * 1.13.11-gke.5 
  * 1.14.7-gke.10 
  * 1.15.4-gke.15 

######  Welche Sicherheitslücken werden mit diesem Patch behoben?

Dieser Patch dient zur Entschärfung der folgenden Sicherheitslücken:

CVE-2019-11253 ist eine DoS-Sicherheitslücke (Denial of Service).

|

Hoch

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
  
##  16\. September 2019

**Veröffentlicht:** 16.09.2019  
**Zuletzt aktualisiert:** 16.10.2019  Beschreibung  |  Schweregrad  |
Hinweise  
---|---|---  
  
Dieses Bulletin ist seit der ursprünglichen Veröffentlichung aktualisiert
worden.

Im Zusammenhang mit der Programmiersprache Go wurden kürzlich die neuen DoS-
Sicherheitslücken (Denial of Service) [ CVE-2019-9512
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9512) und [
CVE-2019-9514 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514)
festgestellt. In GKE könnten Nutzer dadurch schädliche Anfragen erstellen, die
zu einem extrem hohen CPU-Verbrauch auf dem Kubernetes API-Server führen und
damit unter Umständen die Verfügbarkeit der Steuerungsebene des Clusters
reduzieren. Weitere Informationen finden Sie in der [ Mitteilung zur
Programmiersprache Go ](https://groups.google.com/forum/?hl=de#!topic/golang-
announce/65QixT3tcmg) .

######  Was soll ich tun?

Wir empfehlen ein Upgrade Ihres Clusters auf die neueste Patchversion, mit der
diese Sicherheitslücke entschärft wird, sobald die Version verfügbar ist. Laut
[ Veröffentlichungszeitplan ](https://cloud.google.com/kubernetes-
engine/docs/release-notes-archive?hl=de#september_16_2019) sollten die neuen
Patchversionen in allen Zonen mit dem nächsten GKE-Release bereitgestellt
werden.

Die Patchversionen, mit denen die Sicherheitslücke entschärft wird, sind unten
aufgeführt.

  * **Aktualisierung vom 16. Oktober 2019** : 1.12.10-gke.15 
  * 1.13.10-gke.0 
  * 1.14.6-gke.1 

######  Welche Sicherheitslücke wird mit diesem Patch behoben?

Dieser Patch dient zur Entschärfung der folgenden Sicherheitslücken:

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) und [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) sind DoS-
Sicherheitslücken (Denial of Service).

|

Hoch

|

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512)  
[ CVE-2019-9514 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9514)  
  
  
##  5\. September 2019

**Veröffentlicht:** 05.09.2019  
**Zuletzt aktualisiert:** 05.09.2019

Das Bulletin für die Korrektur der im Bulletin vom  31\. Mai 2019
dokumentierten Sicherheitslücke wurde aktualisiert.

##  22\. August 2019

**Veröffentlicht:** 22.08.2019  
**Zuletzt aktualisiert:** 22.08.2019

Das Bulletin vom  5\. August 2019  wurde aktualisiert. Die Korrektur für die
in dem früheren Bulletin dokumentierte Sicherheitslücke [ ist verfügbar
](https://cloud.google.com/kubernetes-engine/docs/release-notes-
archive?hl=de#august_22_2019) .

##  8\. August 2019

**Veröffentlicht:** 08.08.2019  
**Zuletzt aktualisiert:** 08.08.2019

Das Bulletin vom  5\. August 2019  wurde aktualisiert. Die Korrektur für die
in diesem Bulletin dokumentierte Sicherheitslücke ist voraussichtlich im
nächsten GKE-Release verfügbar.

##  5\. August 2019

**Veröffentlicht:** 05.08.2019  
**Zuletzt aktualisiert:** 09.08.2019  Beschreibung  |  Schweregrad  |
Hinweise  
---|---|---  
  
Dieses Bulletin ist seit der ursprünglichen Veröffentlichung aktualisiert
worden.

Kubernetes hat kürzlich die Sicherheitslücke [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) festgestellt.
Dadurch können clusterbezogene [ benutzerdefinierte Ressourceninstanzen
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) wie mit einem Namespace versehene Objekte behandelt werden, die in
allen Namespaces existieren. Das bedeutet, dass Nutzer und Dienstkonten, die
lediglich RBAC-Berechtigungen auf Namespace-Ebene haben, mit clusterbezogenen
benutzerdefinierten Ressourcen interagieren können. Damit der Angreifer diese
Sicherheitslücke nutzen kann, benötigt er Zugriffsrechte auf die Ressource in
einem Namespace.

######  Was soll ich tun?

Wir empfehlen ein [ Upgrade ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=de) Ihres Clusters auf die neuste
Patchversion, mit der der diese Sicherheitslücke entschärft wird, sobald die
Version verfügbar ist. Die Patchversionen werden voraussichtlich mit dem
nächsten GKE-Release in allen Zonen bereitgestellt. Die Sicherheitslücke wurde
in folgenden Patchversionen entschärft:

  * 1.11.10-gke.6 
  * 1.12.9-gke.13 
  * 1.13.7-gke.19 
  * 1.14.3-gke.10 ( [ Rapid Channel ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels?hl=de) ) 

######  Welche Sicherheitslücke wird mit diesem Patch behoben?

Der Patch entschärft die Sicherheitslücke [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Mittel

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)  
  
##  3\. Juli 2019

**Veröffentlicht:** 03.07.2019  
**Zuletzt aktualisiert:** 03.07.2019  Beschreibung  |  Schweregrad  |
Hinweise  
---|---|---  
  
Eine Patchversion von ` kubectl ` zur Behebung von CVE-2019-11246 steht jetzt
mit [ ` gcloud ` 253.0.0 ](https://cloud.google.com/sdk/docs/release-
notes?hl=de#kubernetes_engine) bereit. Weitere Informationen finden Sie im
Sicherheitsbulletin vom 25. Juni 2019  .

**Hinweis:** Der Patch ist nicht in ` kubectl ` 1.11.10 verfügbar.

|

Hoch

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  3\. Juli 2019

**Veröffentlicht:** 25.06.2019  
**Zuletzt aktualisiert:** 03.07.2019  Beschreibung  |  Schweregrad  |
Hinweise  
---|---|---  
  
######  Aktualisierung vom 3. Juli 2019

Zum Zeitpunkt der letzten Aktualisierung waren noch keine Patches für die
Versionen 1.11.9 und 1.11.10 verfügbar. Jetzt wurde 1.11.10-gke.5 als Upgrade-
Ziel für beide 1.11-Versionen veröffentlicht.

Aktuell sind die GKE-Master gepatcht. In der Google-Infrastruktur, in der
Kubernetes Engine ausgeführt wird, wurde die Sicherheitslücke mit einem Patch
behoben.

Master der Version 1.11 werden demnächst eingestellt. In der Woche vom 8. Juli
2019 ist ein automatisches Upgrade auf 1.12 geplant. Sie können eine der
folgenden Maßnahmen ergreifen, um Knoten auf eine Patchversion zu
aktualisieren.

  * Führen Sie bis 8. Juli 2019 das Knotenupgrade auf 1.11.10-gke.5 durch. Nach diesem Datum werden die Versionen 1.11 nach und nach aus der Liste der verfügbaren Upgrade-Ziele entfernt. 
  * Aktivieren Sie [ automatische Upgrades ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades?hl=de) für Knoten der Version 1.11 und lassen Sie zu, dass für die Knoten zusammen mit den Mastern ein Upgrade auf 1.12 durchgeführt wird. 
  * Führen Sie ein [ manuelles Upgrade ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=de) der Master und Knoten auf eine korrigierte Version 1.12 durch. 

Nachfolgend das ursprüngliche Bulletin vom 24. Juni 2019:

* * *

######  Aktualisierung vom 24. Juni 2019

Seit 22. Juni 2019, 21:40 Uhr UTC stehen die unten aufgeführten Patchversionen
für Kubernetes bereit. Master zwischen den Kubernetes-Versionen 1.11.0 und
1.13.6 werden automatisch auf eine Patchversion aktualisiert. Wenn Sie keine
mit diesem Patch kompatible Version ausführen, führen Sie vor dem Upgrade
Ihrer Knoten ein Upgrade auf eine der unten aufgeführten kompatiblen
Masterversionen durch.

**Aufgrund der Schwere dieser Sicherheitslücken empfehlen wir ungeachtet
dessen, ob Sie automatische Knotenupgrades aktiviert haben, möglichst umgehend
ein[ manuelles Upgrade ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-container-cluster?hl=de) Ihrer Knoten und Master auf eine
dieser Versionen durchzuführen. **

Die Patchversionen:

  * 1.11.8-gke.10 
  * 1.12.7-gke.24 
  * 1.12.8-gke.10 
  * 1.13.6-gke.13 

Nachfolgend das ursprüngliche Bulletin vom 18. Juni 2019:

* * *

Netflix hat vor Kurzem drei TCP-Sicherheitslücken in Linux-Kernels
festgestellt:

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

Diese CVEs werden zusammen als [ NFLX-2019-001
](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-
party/2019-001.md) bezeichnet.

Nicht gepatchte Linux-Kernels können für remote ausgelöste DoS-Angriffe
(Denial of Service) anfällig sein. **Google Kubernetes Engine-Knoten, die
nicht vertrauenswürdigen Netzwerktraffic senden oder empfangen, sind
betroffen. Zum Schutz Ihrer Arbeitslasten empfehlen wir zur Entschärfung die
folgenden Schritte.**

######  Kubernetes-Master

  * Kubernetes-Master, die den Traffic mithilfe von [ autorisierten Netzwerken ](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks?hl=de) auf vertrauenswürdige Netzwerke begrenzen, sind nicht betroffen. 

  * Auf Mastern für GKE-Cluster, die von Google verwaltet werden, wird in den nächsten Tagen automatisch eine Patchversion installiert. Auf Kundenseite sind keine Maßnahmen erforderlich. 

######  Kubernetes-Knoten

Knoten, die den Traffic auf vertrauenswürdige Netzwerke begrenzen, sind nicht
betroffen. Hierzu zählen folgende Cluster:

  * Cluster mit Knoten, die durch eine Firewall von nicht vertrauenswürdigen Netzwerken isoliert sind, oder [ private Cluster ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters?hl=de) , die keine öffentlichen IP-Adressen verwenden. 
  * Cluster ohne öffentliche Load-Balancer-Dienste 

Google arbeitet derzeit an einer permanenten Entschärfung dieser
Sicherheitslücken in Form einer neuen Knotenversion. Wir aktualisieren dieses
Bulletin und senden eine E-Mail an alle GKE-Kunden, sobald die permanente
Korrektur bereitsteht.

Bis die permanente Korrektur verfügbar ist, haben wir ein Kubernetes DaemonSet
erstellt, mit dem zur Entschärfung die Hostkonfiguration ` iptables ` geändert
wird.

#####  Was soll ich tun?

Wenden Sie das Kubernetes DaemonSet mit dem folgenden Befehl auf alle Knoten
in Ihrem Cluster an. Dadurch werden die auf dem Knoten vorhandenen Regeln `
iptables ` durch eine weitere Regel vom Typ ` iptables ` ergänzt, um die
Sicherheitslücke zu entschärfen. **Führen Sie den Befehl für jedes Google
Cloud-Projekt einmal pro Cluster aus.**

    
    
    
    kubectl apply -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

Da Ipv6 in GKE nicht unterstützt wird, ist keine Regel vom Typ "ip6tables"
erforderlich.

Sobald die Patchversion verfügbar ist und Sie ein Upgrade aller potenziell
betroffenen Knoten durchgeführt haben, können Sie das DaemonSet mit dem
folgenden Befehl entfernen. **Führen Sie den Befehl für jedes Google Cloud-
Projekt einmal pro Cluster aus.**

    
    
    
    kubectl delete -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

|  Hoch  
Mittel  
Mittel  
|  [ CVE-2019-11477 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11477)  
[ CVE-2019-11478 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11478)  
[ CVE-2019-11479 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11479)  
  
  
##  25\. Juni 2019

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
**Aktualisierung vom 3. Juli 2019:** Dieser Patch steht für ` gcloud ` 253.0.0
für ` kubectl ` Version 1.12.9, 1.13.6, 1.14.2 und neuere Releases bereit.

**Hinweis:** Der Patch ist nicht in 1.11.10 verfügbar.

* * *

Kubernetes hat kürzlich die Sicherheitslücke [ CVE-2019-11246
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11246) festgestellt.
Dadurch kann ein Angreifer, der Zugriff auf einen Vorgang vom Typ ` kubectl cp
` sowie die Codeausführung in einem Container hat, Dateien auf dem Host
ändern. Der Angreifer hat die Möglichkeit, Dateien auf dem Hostdateisystem zu
ersetzen und zu erstellen. Weitere Informationen erhalten Sie in der [
Mitteilung zu Kubernetes
](https://groups.google.com/forum/?hl=de#!topic/kubernetes-security-
announce/NLs2TGbfPdo) .

**Von dieser Sicherheitslücke sind alle` gcloud ` -Versionen für Google
Kubernetes Engine (GKE) betroffen. Wir empfehlen daher ein Upgrade auf die
neueste Patchversion von ` gcloud ` , sobald sie bereitsteht. ** Diese
Sicherheitslücke wird in einer der nächsten Patchversionen entschärft.

######  Was soll ich tun?

Eine Patchversion von ` kubectl ` wird im nächsten ` gcloud ` -Release
bereitgestellt. Sie können auch selbst [ direkt ein Upgrade von ` kubectl `
](https://kubernetes.io/docs/tasks/tools/install-kubectl/) ausführen.

Verfolgen Sie die Verfügbarkeit des Patches in den [ Versionshinweisen zu `
gcloud ` ](https://cloud.google.com/sdk/docs/release-notes?hl=de) .

######  Welche Sicherheitslücke wird mit diesem Patch behoben?

Durch die Sicherheitslücke [ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) erhalten Angreifer Zugriff auf einen
Vorgang vom Typ ` kubectl cp ` sowie die Codeausführung in einem Container und
können Dateien auf dem Host ändern. Angreifer haben die Möglichkeit, Dateien
im Hostdateisystem zu ersetzen oder zu erstellen.

|

Hoch

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  18\. Juni 2019

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
Docker hat kürzlich die Sicherheitslücke [ CVE-2018-15664
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-15664) festgestellt.
Angreifer können darüber Code in einem Container ausführen, um einen extern
initiierten Vorgang vom Typ ` docker cp ` zu hacken. Angreifer haben die
Möglichkeit, den Ort, an dem eine Datei im Hostdateisystem geschrieben wird,
beliebig zu ändern.

**Von dieser Sicherheitslücke sind alle Google Kubernetes Engine-Knoten (GKE)
betroffen, die Docker ausführen. Wir empfehlen ein Upgrade auf die neueste
Patchversion, sobald sie bereitsteht. Diese Sicherheitslücke wird in einer der
nächsten Patchversionen entschärft.**

**Alle Google Kubernetes Engine-Master (GKE) vor Version 1.12.7 führen Docker
aus und sind von dieser Sicherheitslücke betroffen.** Da Nutzer in GKE auf dem
Master keinen Zugriff auf ` docker cp ` haben, ist das Risiko dieser
Sicherheitslücke für GKE-Master begrenzt.

#####  Was soll ich tun?

Betroffen sind nur Knoten, auf denen Docker ausgeführt wird, sofern der Befehl
` docker cp ` oder ein ähnlicher API-Befehl ausgeführt wird, der gehackt
werden kann. Das sollte in Kubernetes-Umgebungen relativ selten der Fall sein.
Knoten, die [ COS mit containerd ](https://cloud.google.com/kubernetes-
engine/docs/concepts/using-containerd?hl=de) ausführen, sind nicht betroffen.

Damit Sie ein Knotenupgrade durchführen können, ist zuerst ein [ Masterupgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=de#upgrading_the_cluster) auf die Patchversion erforderlich. Sobald
der Patch bereitsteht, können Sie wahlweise selbst ein Masterupgrade
durchführen oder warten, bis Google es automatisch ausführt. Der Patch ist im
nächsten GKE-Patch in Docker 18.09.7 verfügbar. **Dieser Patch gilt nur für
GKE Version 1.13 und höher.**

Im Zuge der regelmäßigen Upgrades werden die Cluster-Master automatisch auf
die gepatchte Version aktualisiert. Sie können auch selbst ein Masterupgrade
durchführen, sobald die Patchversion bereitsteht.

Wir aktualisieren dieses Bulletin, sobald die Patchversionen bereitstehen.
Informationen zur Verfügbarkeit der Patches finden Sie in den [
Versionshinweisen ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=de) .

#####  Welche Sicherheitslücke wird mit diesem Patch behoben?

Dieser Patch dient zur Entschärfung der folgenden Sicherheitslücke:

Über die Sicherheitslücke [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) können Angreifer, die zur Codeausführung
in einem Container berechtigt sind, einen extern initiierten Vorgang vom Typ `
docker cp ` hacken. Angreifer haben die Möglichkeit, den Ort, an dem eine
Datei im Hostdateisystem geschrieben wird, beliebig zu ändern.

|  Hoch  |  
  
##  31\. Mai 2019

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
Dieses Bulletin ist seit der ursprünglichen Veröffentlichung aktualisiert
worden.

######  Aktualisierung vom 2. August 2019

Zum Zeitpunkt des ursprünglichen Bulletins waren nur 1.13.6-gke.0 bis
1.13.6-gke.5 betroffen. Aufgrund einer Regression sind jetzt alle Versionen
1.13.6.x betroffen. Wenn Sie 1.13.6 verwenden, führen Sie möglichst umgehend
ein Upgrade auf 1.13.7 durch.

Kubernetes hat in Kubelet Version 1.13.6 und 1.14.2 die Sicherheitslücke [
CVE-2019-11245 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11245)
festgestellt. Container können dadurch als UID 0 ausgeführt werden, was in der
Regel dem Nutzer ` root ` zugeordnet ist, selbst wenn im Container-Image ein
anderer Nutzer angegeben ist. **Wenn Ihre Container unter einem Nicht-Root-
Nutzer ausgeführt werden und Sie eine Version zwischen 1.13.6-gke.0 und
1.13.6-gke.6 ausführen, empfehlen wir, im Cluster, dessen Container nicht als
UID 0 ausgeführt werden sollen, auf allen Pods` RunAsUser ` festzulegen. **

Wenn für den Nicht-Root-Wert ` USER ` angegeben ist, weil beispielsweise der
Wert ` USER ` in einem Dockerfile festgelegt wurde, können unerwartete
Verhaltensweisen auftreten. Container, die zum ersten Mal auf einem Knoten
ausgeführt werden, respektieren die angegebene UID. Aufgrund des Fehlers wird
der Container jedoch ab der zweiten Ausführung ungeachtet der angegebenen UID
als UID 0 ausgeführt. Das ist in der Regel eine unerwünschte eskalierte
Berechtigung, die zu einem unerwarteten Verhalten der Anwendung führen kann.

#####  Wie stelle ich fest, ob ich eine betroffene Version verwende?

Listen Sie mit dem folgenden Befehl alle Knoten und deren Kubelet-Version auf:

    
    
    
    kubectl get nodes -o=jsonpath='{range .items[*]}'\
    '{.status.nodeInfo.machineID}'\
    '{"\t"}{.status.nodeInfo.kubeletVersion}{"\n"}{end}'

Wenn in der Ausgabe die unten angegebenen Kubelet-Versionen aufgelistet
werden, sind Ihre Knoten betroffen:

  * v1.13.6 
  * v1.14.2 

#####  Wie stelle ich fest, ob meine spezielle Konfiguration betroffen ist?

Wenn Ihre Container unter einem Nicht-Root-Nutzer ausgeführt werden und Sie
eine Knotenversion zwischen 1.13.6-gke.0 und 1.13.6-gke.6 ausführen, ist Ihre
Konfiguration mit Ausnahme der folgenden Fälle betroffen:

  * Pods, die für den PodSecurityContext ` runAsUser ` einen gültigen Nicht-Root-Wert angeben, sind nicht betroffen und funktionieren erwartungsgemäß. 
  * Auch PodSecurityPolicies, die die Einstellung ` runAsUser ` erzwingen, sind nicht betroffen und funktionieren weiter erwartungsgemäß. 
  * Pods, die ` mustRunAsNonRoot:true ` angeben, starten nicht als UID 0. Der Start schlägt jedoch generell fehl, wenn sie von diesem Problem betroffen sind. 

#####  Was soll ich tun?

Legen Sie auf allen Pods im Cluster, die nicht als UID 0 ausgeführt werden
sollen, den [ RunAsUser-Sicherheitskontext
](https://kubernetes.io/docs/tasks/configure-pod-container/security-
context/#set-the-security-context-for-a-pod) fest. Sie können diese
Konfiguration mit einer [ PodSecurityPolicy
](https://kubernetes.io/docs/concepts/policy/pod-security-policy/) anwenden.

|  Mittel  |  [ CVE-2019-11245 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2019-11245)  
  
##  14\. Mai 2019

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
**Aktualisierung von 11. Juli 2019** : Der Patch ist in 1.11.10-gke.4,
1.12.8-gke.6 und 1.13.6-gke.5 verfügbar, die in der Woche vom 28. Mai 2019
veröffentlicht wurden, sowie in neueren Releases.

Die folgenden CVEs (Common Vulnerabilities and Exposures) wurden von Intel
festgestellt:

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

Diese CVEs werden zusammen als Microarchitectural Data Sampling (MDS)
bezeichnet. Diese Sicherheitslücken bringen das Risiko mit sich, dass Daten
Angriffen ausgesetzt sind, die durch Interaktion einer spekulativen Ausführung
mit dem mikroarchitektonischen Status erfolgen. Weitere Informationen erhalten
Sie im folgenden [ Intel-Blog
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) .

**Die Hostinfrastruktur, auf der Kubernetes Engine ausgeführt wird, dient
dazu, Arbeitslasten von Kunden voneinander zu isolieren. Sie sind nicht
betroffen, es sei denn, sie würden in Ihren eigenen GKE-Clustern für mehrere
Mandanten nicht vertrauenswürdigen Code ausführen.**

**Für Kunden, die in Kubernetes Engine in ihren eigenen Diensten für mehrere
Mandanten nicht vertrauenswürdigen Code ausführen, stellt das eine besonders
schwerwiegende Sicherheitslücke dar.** Zur Entschärfung in Kubernetes Engine
können Sie das Hyper-Threading in Ihren Knoten deaktivieren. Von diesen
Sicherheitslücken sind nur Google Kubernetes Engine-Knoten (GKE) betroffen,
die mehrere CPUs verwenden. Hinweis: VMs vom Typ n1-standard-1 (GKE-
Standardeinstellung), g1-small und f1-micro stellen der Gastumgebung nur eine
vCPU bereit, sodass Hyper-Threading nicht deaktiviert werden muss.

Zusätzliche Sicherheitsfunktionen, durch die Flush-Funktionen möglich sind,
werden in einer nächsten [ Patchversion ](https://cloud.google.com/kubernetes-
engine/release-notes?hl=de) bereitgestellt. Im Zuge der regelmäßigen Upgrades
werden die Master und Knoten in den nächsten Wochen automatisch auf die
gepatchte Version aktualisiert. **Der Patch allein reicht nicht aus, um die
von dieser Sicherheitslücke ausgehende Gefahr zu bekämpfen. Die nachfolgenden
Maßnahmen werden empfohlen.**

Wenn Sie GKE On-Prem ausführen, sind Sie je nach verwendeter Hardware unter
Umständen betroffen. Weitere Informationen finden Sie in der [ Mitteilung zu
Intel ](https://www.intel.com/content/www/us/en/security-
center/advisory/intel-sa-00233.html) .

####  Was soll ich tun?

**Sie sind nicht betroffen, es sei denn, Sie würden in Ihren GKE-Clustern für
mehrere Mandanten nicht vertrauenswürdigen Code ausführen.**

**Erstellen Sie für Knoten in Kubernetes Engine neue Knotenpools mit
deaktiviertem Hyper-Threading und verlagern Sie Ihre Arbeitslasten auf die
neuen Knoten.**

Hinweis: VMs vom Typ n1-standard-1, g1-small und f1-micro stellen der
Gastumgebung nur eine vCPU bereit, sodass Hyper-Threading nicht deaktiviert
werden muss.

**Warnung:**

  * Die Deaktivierung des Hyper-Threadings kann sich schwerwiegend auf die Leistung Ihrer Cluster und Anwendung auswirken. Prüfen Sie vor der Bereitstellung in Ihren Produktionsclustern, ob das akzeptabel ist. 
  * Hyper-Threading kann in GKE auf der Knotenpoolebene durch Bereitstellung eines DaemonSet deaktiviert werden. Durch die Bereitstellung dieses DaemonSet werden jedoch alle Knoten im Knotenpool gleichzeitig neu gestartet. Daher wird empfohlen, einen neuen Knotenpool in Ihrem Cluster zu erstellen, das DaemonSet bereitzustellen, um Hyper-Threading in diesem Knotenpool zu deaktivieren, und Ihre Arbeitslasten anschließend zum neuen Knotenpool zu migrieren. 

So erstellen Sie einen neuen Knotenpool mit deaktiviertem Hyper-Threading:

  1. Erstellen Sie in Ihrem Cluster einen neuen Knotenpool mit dem Knotenlabel ` cloud.google.com/gke-smt-disabled=true ` : 
    
        
    gcloud container node-pools create smt-disabled --cluster=[CLUSTER_NAME] \
        --node-labels=cloud.google.com/gke-smt-disabled=true

  2. Stellen Sie das DaemonSet diesem neuen Knotenpool bereit. Das DaemonSet wird nur auf Knoten mit dem Label ` cloud.google.com/gke-smt-disabled=true ` ausgeführt. Es deaktiviert Hyper-Threading und startet dann den Knoten neu. 
    
        
    kubectl create -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform/\
    k8s-node-tools/master/disable-smt/gke/disable-smt.yaml

  3. Prüfen Sie, ob die DaemonSet-Pods ausgeführt werden. 
    
        
    kubectl get pods --selector=name=disable-smt -n kube-system

Sie sollten eine Antwort ähnlich der folgenden erhalten:

    
        
    NAME                READY     STATUS    RESTARTS   AGE
    
    disable-smt-2xnnc   1/1       Running   0          6m

  4. Prüfen Sie, ob in den Logs der Pods "SMT has been disabled" angegeben wird. 
    
        
    kubectl logs disable-smt-2xnnc disable-smt -n kube-system

Hinweis: Bootoptionen können nicht geändert werden, wenn auf dem Knoten die
Funktion [ Sicherer Start ](https://cloud.google.com/kubernetes-
engine/docs/how-to/shielded-gke-nodes?hl=de#secure_boot) aktiviert ist. Wenn
die Funktion "Sicherer Start" aktiviert ist, muss sie [ deaktiviert
](https://cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-
nodes?hl=de#disabling) werden, bevor das DaemonSet erstellt wird.

Das DaemonSet muss auf den Knotenpools weiter ausgeführt werden, damit die
Änderungen automatisch auf die neu im Pool erstellten Knoten angewendet
werden. Die Knotenerstellung kann durch automatische Knotenreparaturen,
manuelle oder automatische Upgrades und Autoscaling ausgelöst werden.

Wenn Sie Hyper-Threading wieder aktivieren möchten, erstellen Sie den
Knotenpool noch einmal, ohne das DaemonSet bereitzustellen. Migrieren Sie dann
Ihre Arbeitslasten zum neuen Knotenpool.

Wir empfehlen auch ein manuelles Upgrade Ihrer Knoten, sobald der Patch
bereitsteht. Führen Sie zuerst ein [ Masterupgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=de#upgrading_the_cluster) auf die neueste Version durch. Die GKE-
Master werden im Zuge der regelmäßigen Upgrades automatisch aktualisiert.

Dieses Bulletin wird mit den Patchversionen aktualisiert, sobald diese
bereitstehen.

####  Welche Sicherheitslücke wird mit diesem Patch behoben?

Dieser Patch dient zur Entschärfung der folgenden Sicherheitslücken:

[ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
, [ CVE-2018-12127 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2018-12127) , [ CVE-2018-12130
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130) , [
CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091) :
Diese Sicherheitslücken nutzen die spekulative Ausführung. Diese CVEs werden
allgemein als "Microarchitectural Data Sampling" bezeichnet. Diese
Sicherheitslücken bringen das Risiko mit sich, dass Daten Angriffen ausgesetzt
sind, die durch Interaktion einer spekulativen Ausführung mit dem
mikroarchitektonischen Status erfolgen.  |  Mittel  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  5\. April 2019

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
Kürzlich wurden die Sicherheitslücken [ CVE-2019-9900
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900) und [
CVE-2019-9901 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)
in [ Envoy ](https://www.envoyproxy.io/) festgestellt.

Envoy ist in [ Istio ](https://istio.io/) eingebettet. Durch die
Sicherheitslücken kann die Istio-Richtlinie in manchen Fällen umgangen werden.

Wenn Sie Istio in Google Kubernetes Engine (GKE) aktiviert haben, können Sie
von diesen Sicherheitslücken betroffen sein. **Wir empfehlen, Ihre betroffenen
Cluster auf die neueste Patchversion zu aktualisieren, sobald sie bereitsteht.
Führen Sie außerdem ein Upgrade Ihrer Istio-Sidecar-Container durch. Eine
Anleitung finden Sie unten.**

####  Was soll ich tun?

**Aufgrund des Schweregrads dieser Sicherheitslücken empfehlen wir Folgendes
ungeachtet dessen, ob Sie automatische Knotenupgrades aktiviert haben:**

  1. **Führen Sie ein[ manuelles Upgrade ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=de) Ihres Clusters durch, sobald der Patch bereitsteht. **
  2. **Führen Sie gemäß der[ Dokumentation zu Sidecar-Upgrades ](https://archive.istio.io/v1.5/docs/setup/upgrade/cni-helm-upgrade/#control-plane-upgrade) ein Upgrade Ihrer Sidecar-Container durch. **

Die Patchversionen werden heute vor 19:00 Uhr PDT für alle GKE-Projekte
bereitgestellt.

Dieser Patch wird in den folgenden GKE-Versionen verfügbar sein. Neue Cluster
verwenden standardmäßig die Patchversion, sobald sie in den
Sicherheitsbulletins von GKE angekündigt wird. Wenn Sie neue Cluster jedoch
vor dem 15. April 2019 erstellt haben, müssen Sie die zu verwendende
Patchversion angeben. Die Knoten von GKE-Kunden, die keine [ automatischen
Knotenupgrades ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-
auto-upgrades?hl=de) aktiviert haben und keine manuellen Upgrades durchführen,
werden in der folgenden Woche automatisch mit Patchversionen aktualisiert.

Patchversionen:

  * 1.10.12-gke.14 
  * 1.11.6-gke.16 
  * 1.11.7-gke.18 
  * 1.11.8-gke.6 
  * 1.12.6-gke.10 
  * 1.13.4-gke.10 

####  Welche Sicherheitslücke wird mit diesem Patch behoben?

Dieser Patch dient zur Entschärfung der folgenden Sicherheitslücken:

[ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) und [ CVE-2019-9901.
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) Mehr darüber
können Sie im [ Blog zu Istio ](https://istio.io/blog/2019/announcing-1.1.2)
lesen.

|  Hoch  |

  * [ CVE-2019-9900 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900)
  * [ CVE-2019-9901. ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)

  
  
##  1\. März 2019

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
**Aktualisierung vom 22. März 2019** : Dieser Patch ist in Kubernetes
1.11.8-gke.4, 1.13.4-gke.1 und neueren Releases verfügbar. Der Patch ist noch
nicht in 1.12 verfügbar. Informationen zur Verfügbarkeit der Patches finden
Sie in den [ Versionshinweisen ](https://cloud.google.com/kubernetes-
engine/docs/release-notes-archive?hl=de#march_19_2019) .

Kubernetes hat kürzlich die neue DoS-Sicherheitslücke (Denial of Service) [
CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) festgestellt. Nutzer, die Patchanfragen
stellen dürfen, können dadurch eine schädliche Anfrage vom Typ "json-patch"
erstellen, die auf dem Kubernetes API-Server übermäßig viel CPU und
Arbeitsspeicher verbraucht. Dadurch kann die Verfügbarkeit der Steuerungsebene
des Clusters sinken. Weitere Informationen erhalten Sie in der [ Mitteilung zu
Kubernetes ](https://groups.google.com/forum/?hl=de#!topic/kubernetes-
announce/vmUUNkYfG9g) . **Von diesen Sicherheitslücken sind alle GKE-Master
(Google Kubernetes Engine) betroffen. Diese Sicherheitslücke wird in einer der
nächsten Patchversionen entschärft. Im Zuge der regelmäßigen Upgrades werden
die Cluster-Master in den nächsten Wochen automatisch auf die gepatchte
Version aktualisiert.**

####  Was soll ich tun?

**Es sind keine Maßnahmen erforderlich. Die GKE-Master werden im Zuge der
regelmäßigen Upgrades automatisch aktualisiert.** Falls Ihnen das zu lange
dauert, können Sie auch ein [ Masterupgrade manuell initiieren
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=de#upgrading_the_cluster) .

Dieses Bulletin wird mit den verfügbaren Patchversionen aktualisiert. Hinweis:
Der Patch ist nur in Versionen ab 1.11 verfügbar, nicht aber in 1.10.

####  Welche Sicherheitslücke wird mit diesem Patch behoben?

Dieser Patch dient zur Entschärfung der folgenden Sicherheitslücke:

Über die Sicherheitslücke [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) kann ein Nutzer einen Patch vom Typ
"json-patch" erstellen, der auf dem Kubernetes API-Server übermäßig viel CPU
verbraucht. Dadurch kann die Verfügbarkeit der Steuerungsebene des Clusters
sinken.

|  Mittel  |  [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100)  
  
##  11\. Februar 2019 (runc)

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
Die Open Containers Initiative (OCI) hat vor Kurzem eine neue Sicherheitslücke
( [ CVE-2019-5736
](https://groups.google.com/a/opencontainers.org/forum/m/?hl=de#!topic/dev/Tc1ELm-8oDI)
) [ in runc entdeckt ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) , durch die ein Container Root-
Berechtigungen für den Hostknoten erhalten kann.

**Ihre GKE-Ubuntu-Knoten sind von diesen Sicherheitslücken betroffen. Wir
empfehlen, so schnell wie möglich ein[ Upgrade auf die neueste Patchversion
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=de) durchzuführen, wie unten beschrieben. **

####  Was soll ich tun?

Führen Sie zuerst ein Upgrade auf die neueste Version für den Master durch.
Dieser Patch ist verfügbar in Kubernetes 1.10.12-gke.7, 1.11.6-gke.11,
1.11.7-gke.4, 1.12.5-gke.5 sowie neueren Releases. Informationen zur
Verfügbarkeit der Patches finden Sie in den [ Versionshinweisen
](https://cloud.google.com/kubernetes-engine/docs/release-notes-
archive?hl=de#february-11-2019) .

Es sind nur Ubuntu-Knoten in GKE betroffen. COS-Knoten betrifft diese
Sicherheitslücke nicht.

Die neue Version von runc benötigt mehr Arbeitsspeicher. Falls Sie niedrige
Speicherlimits (< 16 MB) festgelegt haben, müssen Sie unter Umständen den für
Container zugewiesenen Arbeitsspeicher anpassen.

####  Welche Sicherheitslücke wird mit diesem Patch behoben?

Dieser Patch dient zur Entschärfung der folgenden Sicherheitslücke:

In [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) wird eine Sicherheitslücke in runc
beschrieben, die es einem schädlichen Container mit minimaler
Nutzerinteraktion in Form eines ausführbaren Befehls ermöglicht, das runc-
Hostbinärprogramm zu überschreiben und so auf dem Hostknoten Code auf Root-
Ebene auszuführen. Container, die nicht als Root ausgeführt werden, sind davon
nicht betroffen. Der Schweregrad dieser Sicherheitslücke ist "Hoch".

|  Hoch  |  [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736)  
  
##  11\. Februar 2019 (Go)

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
**Aktualisierung vom 25. Februar 2019:** Der Patch ist nicht, wie zuvor
mitgeteilt, in 1.11.7-gke.4 verfügbar. Wenn Sie 1.11.7 verwenden, können Sie
wahlweise ein Downgrade auf 1.11.6 oder ein Upgrade auf 1.12 durchführen oder
bis zur Bereitstellung von Patch 1.11.7 in der Woche vom 4. März 2019 warten.

Im Zusammenhang mit der Programmiersprache Go wurde vor Kurzem eine neue
Sicherheitslücke ( [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486) ) entdeckt. Hierbei handelt es sich um
eine Denial of Service-Sicherheitslücke (DoS) in den Implementierungen der
Elliptische-Kurven-Kryptografie für die elliptischen Kurven P-521 und P-384.
In Google Kubernetes Engine (GKE) könnten Nutzer auf diese Weise schädliche
Anfragen erstellen, die zu einem extrem hohen CPU-Verbrauch auf dem Kubernetes
API-Server führen und damit unter Umständen die Verfügbarkeit der
Steuerungsebene des Clusters reduzieren. Weitere Informationen finden Sie in
der [ Mitteilung zur Programmiersprache Go
](https://groups.google.com/forum/?hl=de#!topic/golang-announce/mVeX35iXuSw) .

**Von diesen Sicherheitslücken sind alle GKE-Master (Google Kubernetes Engine)
betroffen. Mit der[ neuesten Patchversion
](https://cloud.google.com/kubernetes-engine/docs/release-notes-
archive?hl=de#february-11-2019) lässt sich diese Sicherheitslücke entschärfen.
Im Zuge der regelmäßigen Upgrades werden die Cluster-Master in den nächsten
Wochen automatisch auf die gepatchte Version aktualisiert. **

####  Was soll ich tun?

**Es sind keine Maßnahmen erforderlich. Die GKE-Master werden im Zuge der
regelmäßigen Upgrades automatisch aktualisiert.** Falls Ihnen das zu lange
dauert, können Sie auch ein [ Masterupgrade manuell initiieren
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=de#upgrading_the_cluster) .

Dieser Patch ist verfügbar in GKE 1.10.12-gke.7, 1.11.6-gke.11, 1.11.7-gke.4,
1.12.5-gke.5 sowie neueren Releases.

####  Welche Sicherheitslücke wird mit diesem Patch behoben?

Dieser Patch dient zur Abschwächung der folgenden Sicherheitslücke:

CVE-2019-6486 ist eine Sicherheitslücke in den Implementierungen der
Elliptische-Kurven-Kryptografie für die elliptischen Kurven P-521 und P-384.
Nutzer können so Eingaben erstellen, die zu einem extrem hohen CPU-Verbrauch
führen.

|  Hoch  |  [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486)  
  
##  3\. Dezember 2018

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
In Kubernetes wurde vor Kurzem eine neue Sicherheitslücke festgestellt, und
zwar [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105) . Dadurch können Nutzer mit relativ
niedrigen Berechtigungen die Autorisierung für die Kubelet-APIs umgehen und so
für jeden Pod auf jedem Knoten im Cluster beliebige Vorgänge ausführen.
Weitere Informationen erhalten Sie in der [ Mitteilung zu Kubernetes
](https://groups.google.com/forum/?hl=de#!topic/kubernetes-
announce/GVllWCg6L88) . **Von diesen Sicherheitslücken sind alle Google
Kubernetes Engine-Master (GKE) betroffen. Wir haben die Cluster allerdings
bereits auf die[ aktuellen Patchversionen
](https://cloud.google.com/kubernetes-engine/docs/release-notes-
archive?hl=de#november-12-2018) aktualisiert. Es sind keine Maßnahmen
erforderlich. **

####  Was soll ich tun?

**Es sind keine Maßnahmen erforderlich. Die GKE-Master wurden bereits
aktualisiert.**

Dieser Patch ist verfügbar in GKE 1.9.7-gke.11, 1.10.6-gke.11, 1.10.7-gke.11,
1.10.9-gke.5 und 1.11.2-gke.18 sowie neueren Versionen.

####  Welche Sicherheitslücke wird mit diesem Patch behoben?

Dieser Patch dient zur Entschärfung der folgenden Sicherheitslücke:

Über die Sicherheitslücke CVE-2018-1002105 können Nutzer mit relativ geringen
Berechtigungen die Autorisierung für die Kubelet-APIs umgehen. Nutzer haben
dadurch die Möglichkeit, erweiterbare Anfragen zur Eskalation sowie beliebige
Aufrufe an die Kubelet-API zu senden. Das gilt als kritische Sicherheitslücke
in Kubernetes. In Anbetracht einiger Details in der Implementierung von GKE,
die den nicht autorisierten Eskalationspfad verhinderten, wird diese
Sicherheitslücke mit dem Schweregrad "Hoch" bewertet.

|  Hoch  |  [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105)  
  
##  13\. November 2018

Beschreibung  
---  
  
**Update vom 16.11.2018:** Widerruf und Wechsel aller potenziell betroffenen
Tokens wurden abgeschlossen. Es sind keine weiteren Maßnahmen erforderlich.

Google hat kürzlich ein Problem mit dem Plug-in Calico Container Network
Interface (CNI) entdeckt, das in bestimmten Konfigurationen vertrauliche
Informationen protokollieren kann. Dieses Problem wird unter Tigera Technical
Advisory [ TTA-2018-001 ](https://www.projectcalico.org/security-bulletins/)
geführt.

  * Beim Logging auf Debug-Ebene schreibt das Calico CNI-Plug-in die Konfiguration des Kubernetes API-Clients in die Logs. 
  * Das Calico CNI schreibt auch das Kubernetes API-Token auf Informationsebene in die Logs, wenn das Feld "k8s_auth_token" in der CNI-Netzwerkkonfiguration angegeben wurde. 
  * Wenn beim Logging auf Debug-Ebene entweder in der Konfigurationsdatei von Calico oder als von Calico verwendete Umgebungsvariable das Dienstkonto-Token explizit angegeben wird, schreiben Calico-Komponenten (calico/node, felix, CNI) diese Information in die Logdateien. 

Diese Tokens haben die folgenden Berechtigungen:  
      
    
    
    bgpconfigurations.crd.projectcalico.org     [create get list update watch]
    bgppeers.crd.projectcalico.org              [create get list update watch]
    clusterinformations.crd.projectcalico.org   [create get list update watch]
    felixconfigurations.crd.projectcalico.org   [create get list update watch]
    globalbgpconfigs.crd.projectcalico.org      [create get list update watch]
    globalfelixconfigs.crd.projectcalico.org    [create get list update watch]
    globalnetworkpolicies.crd.projectcalico.org [create get list update watch]
    globalnetworksets.crd.projectcalico.org     [create get list update watch]
    hostendpoints.crd.projectcalico.org         [create get list update watch]
    ippools.crd.projectcalico.org               [create get list update watch]
    networkpolicies.crd.projectcalico.org       [create get list update watch]
    nodes                                       [get list update watch]
    pods                                        [get list watch patch]
    namespaces                                  [get list watch]
    networkpolicies.extensions                  [get list watch]
    endpoints                                   [get]
    services                                    [get]
    pods/status                                 [update]
    networkpolicies.networking.k8s.io           [watch list]
            
  
---  
  
Google Kubernetes Engine-Cluster mit aktivierter Cluster-Netzwerkrichtlinie
und aktivem Stackdriver Logging haben Calico-Dienstkonto-Tokens in Stackdriver
protokolliert. Cluster ohne aktivierte Netzwerkrichtlinien sind davon nicht
betroffen.

Es steht ein Update zur Verfügung, mit dem das Calico CNI-Plug-in dahingehend
geändert wird, dass es nur auf der Warnstufe protokolliert und ein neues
Dienstkonto verwendet. Der reparierte Calico-Code wird mit einem späteren
Release bereitgestellt.

Im Laufe der nächsten Woche führen wir einen rollierenden Widerruf aller
potenziell betroffenen Tokens durch. Dieses Bulletin wird aktualisiert, wenn
der Widerruf abgeschlossen ist. **Ihrerseits sind keine weiteren Maßnahmen
erforderlich.** (Der Durchlauf wurde am 16.11.2018 abgeschlossen.)

Wenn Sie diese Tokens sofort wechseln möchten, können Sie nachstehenden Befehl
ausführen. Das neue Secret für das Dienstkonto sollte innerhalb weniger
Sekunden automatisch erstellt werden:  
  
kubectl get sa --namespace kube-system calico -o template --template '{{(index
.secrets 0).name}}' | xargs kubectl delete secret --namespace kube-system  
---  
  
####  Erkennung

GKE protokolliert alle Zugriffe auf den API-Server. Mit nachstehender
Stackdriver-Abfrage können Sie feststellen, ob ein Calico-Token außerhalb des
erwarteten IP-Bereichs von Google Cloud verwendet wurde. Beachten Sie dabei,
dass nur Einträge für Aufrufe von außerhalb des GCP-Netzwerks zurückgegeben
werden. Sie können dies nach Bedarf an Ihre Umgebung anpassen.  
  
---  
      
    
    
    resource.type="k8s_cluster"
    protoPayload.authenticationInfo.principalEmail="system:serviceaccount:kube-system:calico"
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.34.208.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.35.192.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.35.200.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.59.80.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.192.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.208.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.216.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.220.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.222.0/24")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.224.0.0/13")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "162.216.148.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "162.222.176.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "173.255.112.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "192.158.28.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.192.112.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.223.232.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.223.236.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "23.236.48.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "23.251.128.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.204.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.208.0.0/13")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "107.167.160.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "107.178.192.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.2.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.4.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.8.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.16.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.32.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.64.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.192.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.240.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.8.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.16.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.32.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.64.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.128.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "104.154.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "104.196.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "208.68.108.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.184.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.188.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.202.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.192.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.224.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.192.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.196.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.198.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.199.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.199.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.200.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "2600:1900::/35")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.224.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.232.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.234.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.192.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.236.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.240.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.232.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.4.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.220.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.242.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.244.0.0/14")
            
  
---  
  
##  14\. August 2018

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
Die folgenden CVEs (Common Vulnerabilities and Exposures) wurden [ von Intel
festgestellt ](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) :

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) (für [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (für Betriebssysteme und [ SMT ](https://en.wikipedia.org/wiki/Hyper-threading) ) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (für Virtualisierung) 

Diese CVEs werden zusammen als "L1 Terminal Fault (L1TF)" bezeichnet.

Durch diese L1TF-Sicherheitslücken wird die spekulative Ausführung des
Prozessors für Angriffe auf die Konfiguration von Datenstrukturen auf
Prozessorebene ausgenutzt. "L1" bezeichnet den Level-1-Datencache (L1D), eine
kleine On-Core-Ressource für die Beschleunigung des Speicherzugriffs.

Weitere Informationen zu diesen Sicherheitslücken und zu den empfohlenen
Maßnahmen für Compute Engine finden Sie im [ Google Cloud-Blogpost
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=de) .

####  Auswirkungen auf Google Kubernetes Engine

Die Infrastruktur, in der Kubernetes Engine ausgeführt wird und Cluster und
Knoten von Kunden voneinander isoliert werden, ist vor bekannten Angriffen
geschützt.

Kubernetes Engine-Knotenpools, die das Container-Optimized OS-Image (COS) von
Google verwenden und für die [ automatische Upgrades
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=de) aktiviert sind, werden automatisch auf die Patchversionen
unseres COS-Images aktualisiert, sobald sie verfügbar sind. Dies gilt seit
20.08.2018.

Bei Kubernetes Engine-Knotenpools, für die keine [ automatischen Upgrades
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=de) aktiviert sind, müssen [ manuelle Upgrades
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=de) durchgeführt werden, sobald Patchversionen des COS-
Images verfügbar sind.

|  Hoch  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  6\. August 2018; letzte Aktualisierung: 5. September 2018

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Aktualisierung vom 05.09.2018

Kürzlich wurde [ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) festgestellt. Wie bei [ CVE-2018-5390
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390) wird eine
Sicherheitslücke bei Netzwerken auf Kernel-Ebene beschrieben, durch die die
Effektivität von DoS-Angriffen (Denial of Service) auf anfällige Systeme
erhöht wird. Der Unterschied besteht im Wesentlichen darin, dass CVE-2018-5391
über IP-Verbindungen ausgenutzt werden kann. Dieses Bulletin wurde
aktualisiert und deckt nun beide Sicherheitslücken ab.

####  Beschreibung

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ("SegmentSmack") beschreibt eine Netzwerk-
Sicherheitslücke auf Kernel-Ebene. Dadurch wird die Effektivität von DoS-
Angriffen (Denial of Service) über TCP-Verbindungen auf anfällige Systeme
erhöht.

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ("FragmentSmack") beschreibt eine
Netzwerk-Sicherheitslücke auf Kernel-Ebene. Dadurch wird die Effektivität von
DoS-Angriffen (Denial of Service) über IP-Verbindungen auf anfällige Systeme
erhöht.

####  Auswirkungen auf Google Kubernetes Engine

Seit dem 11.08.2018 sind Kubernetes Engine-Master vor beiden Sicherheitslücken
geschützt. Außerdem sind alle Kubernetes Engine-Cluster, die für automatische
Upgrades konfiguriert sind, vor beiden Sicherheitslücken geschützt. Kubernetes
Engine-Knotenpools, die nicht für [ automatische Upgrades
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=de) konfiguriert sind und zum letzten Mal vor dem 11.08.2018
aktualisiert wurden, sind von beiden Sicherheitslücken betroffen.

####  Patchversionen

Aufgrund des Schweregrads dieser Sicherheitslücke empfehlen wir die
Durchführung eines [ manuellen Upgrades ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=de#upgrading-nodes) der Knoten,
sobald die Patches verfügbar sind.

|  Hoch  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  30\. Mai 2018

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
Es wurde kürzlich eine Sicherheitslücke in Git entdeckt, die eine
Rechteausweitung in Kubernetes zulässt, wenn unberechtigte Nutzer Pods mit
gitRepo-Volumes erstellen dürfen. Das CVE ist mit dem Tag [ CVE-2018-11235
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11235)
gekennzeichnet.

####  Bin ich betroffen?

Sie sind von dieser Sicherheitslücke betroffen, wenn folgende Bedingungen
erfüllt sind:

  * Nicht vertrauenswürdige Nutzer können Pods erstellen (oder eine Pod-Erstellung auslösen). 
  * Von nicht vertrauenswürdigen Nutzern erstellte Pods unterliegen Beschränkungen zur Vermeidung des Host-Root-Zugriffs (z. B. über [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=de) ). 
  * Von nicht vertrauenswürdigen Nutzern erstellte Pods sind zur Verwendung des Volume-Typs "gitRepo" berechtigt. 

Alle Kubernetes Engine-Knoten sind gefährdet.

####  Was soll ich tun?

Verhindern Sie die Verwendung des Volume-Typs "gitRepo". Wenn Sie Volumes vom
Typ gitRepo mit der PodSecurityPolicy verbieten möchten, lassen Sie ` gitRepo
` in der Whitelist ` volumes ` Ihrer PodSecurityPolicy weg.

Ein vergleichbares gitRepo-Volume-Verhalten erzielen Sie, wenn Sie ein Git-
Repository von einem initContainer in ein EmptyDir-Volume klonen:

    
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: git-repo-example
    spec:
      initContainers:
        # This container clones the desired git repo to the EmptyDir volume.
        - name: git-clone
          image: alpine/git # Any image with git will do
          args:
            - clone
            - --single-branch
            - --
            - https://github.com/kubernetes/kubernetes # Your repo
            - /repo # Put it in the volume
          securityContext:
            runAsUser: 1 # Any non-root user will do. Match to the workload.
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
          volumeMounts:
            - name: git-repo
              mountPath: /repo
      containers:
        ...
      volumes:
        - name: git-repo
          emptyDir: {}

####  Welcher Patch behebt diese Sicherheitslücke?

Zukünftigen Kubernetes Engine-Releases wird ein entsprechender Patch
hinzugefügt. Weitere Informationen werden hier zukünftig zur Verfügung
gestellt.

|  Mittel  |

  * [ CVE-2018-11235 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11235)

  
  
##  21\. Mai 2018

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
Im Linux-Kernel wurden verschiedene Sicherheitslücken erkannt, bei denen eine
Rechteausweitung oder ein Denial of Service (durch einen Kernel-Absturz) über
einen nicht privilegierten Prozess möglich sind. Diese CVEs sind mit den Tags
[ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) , [ CVE-2018-8897
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897) und [
CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)
gekennzeichnet. Alle Kubernetes Engine-Knoten sind von diesen
Sicherheitslücken betroffen. Es wird empfohlen, ein [ Upgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=de) auf die neueste Patchversion durchzuführen (siehe
unten).

####  Was soll ich tun?

Führen Sie zuerst ein Upgrade auf die neueste Version für den Master durch.
Dieser Patch ist in Kubernetes Engine 1.8.12-gke.1, Kubernetes Engine
1.9.7-gke.1 und Kubernetes Engine 1.10.2-gke.1 verfügbar. Diese Releases
umfassen sowohl Patches für Images von Container-Optimized OS als auch für
Ubuntu.

Wenn Sie vorher einen neuen Cluster erstellen, müssen Sie die Patchversion
angeben, damit sie verwendet wird. Für Knoten, für die [ automatische Upgrades
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=de) aktiviert sind und keine manuellen Upgrades durchgeführt
werden, wird in den nächsten Wochen automatisch ein Upgrade auf Patchversionen
durchgeführt.

####  Welche Sicherheitslücken werden mit diesem Patch behoben?

Dieser Patch dient zur Entschärfung der folgenden Sicherheitslücken:

[ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) : Diese Sicherheitslücke betrifft den
Linux-Kernel. Nicht privilegierte Nutzer oder Prozesse können einen Absturz
des System-Kernels auslösen und damit einen DoS-Angriff oder eine
Rechteausweitung verursachen. Diese Sicherheitslücke wird mit dem Schweregrad
"Hoch" bewertet, mit einem CVSS-Wert (Common Vulnerability Scoring System,
etwa "Allgemeines Verwundbarkeitsbewertungssystem") von 7,8.

[ CVE-2018-8897 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-8897) : Diese Sicherheitslücke betrifft den
Linux-Kernel. Nicht privilegierte Nutzer oder Prozesse können einen Absturz
des System-Kernels auslösen und damit einen DoS-Angriff verursachen. Diese
Sicherheitslücke wird mit dem Schweregrad "Mittel" bewertet, mit einem CVSS
von 6,5.

[ CVE-2018-1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) : Diese Sicherheitslücke betrifft den KVM-
Hypervisor des Linux-Kernels. Nicht privilegierte Prozesse können einen
Absturz des Guest-Kernels auslösen oder erweiterte Berechtigungen erlangen.
Diese Sicherheitslücke wurde in der Infrastruktur behoben, in der Kubernetes
Engine ausgeführt wird. Kubernetes Engine ist somit nicht betroffen. Diese
Sicherheitslücke wurde mit dem Schweregrad "Hoch" bewertet, mit einer CVSS-
Punktzahl von 8,0.

|  Hoch  |

  * [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199)
  * [ CVE-2018-8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
  * [ CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)

  
  
##  12\. März 2018

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
Beim Kubernetes-Projekt wurden [ vor Kurzem neue Sicherheitslücken
festgestellt ](https://groups.google.com/forum/?hl=de#!topic/kubernetes-
security-announce/P7lBjbjDKd8) , und zwar [ CVE-2017-1002101
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101) und [
CVE-2017-1002102 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2017-1002102) . Durch diese Sicherheitslücken haben
Container Zugriff auf Dateien außerhalb des Containers. Alle Kubernetes
Engine-Knoten sind von diesen Sicherheitslücken betroffen. Wir empfehlen, so
schnell wie möglich ein Upgrade auf die neueste Patchversion durchzuführen,
wie unten beschrieben.

####  Was soll ich tun?

Aufgrund des Schweregrads dieser Sicherheitslücken empfehlen wir die
Durchführung eines [ manuellen Upgrades ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-container-cluster?hl=de) der Knoten, sobald der
Patch verfügbar ist. Diese Empfehlung gilt unabhängig davon, ob automatische
Upgrades aktiviert sind oder nicht. Der Patch ist ab dem 16. März für alle
Kunden verfügbar. Gemäß dem [ Releasezeitplan
](https://cloud.google.com/kubernetes-engine/docs/release-notes-
archive?hl=de#march-12-2018) kann er je nach Zone, in der sich Ihr Cluster
befindet, auch schon früher für Sie verfügbar sein.

Führen Sie zuerst ein Upgrade auf die neueste Version für den Master durch.
Dieser Patch wird in Kubernetes 1.9.4-gke.1, Kubernetes 1.8.9-gke.1 und
Kubernetes 1.7.14-gke.1 verfügbar sein. Neue Cluster verwenden die
Patchversion standardmäßig ab dem 30. März. Wenn Sie bereits vor diesem Datum
einen neuen Cluster erstellen, müssen Sie die Patchversion angeben, damit sie
verwendet wird.

Knoten, für die [ automatische Upgrades ](https://cloud.google.com/kubernetes-
engine/docs/concepts/node-auto-upgrades?hl=de) aktiviert sind und keine
manuellen Upgrades durchgeführt werden, werden bis zum 23. April automatisch
auf Patchversionen aktualisiert. Aufgrund des Schweregrads dieser
Sicherheitslücke empfehlen wir jedoch die Durchführung eines [ manuellen
Upgrades ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=de) der Knoten, sobald der Patch verfügbar ist.

####  Welche Sicherheitslücken werden mit diesem Patch behoben?

Mit diesem Patch werden die folgenden beiden Sicherheitslücken behoben:

Die Sicherheitslücke CVE-2017-1002101 ermöglicht Containern, die [ Subpfad
](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath) -Volume-
Bereitstellungen verwenden, den Zugriff auf Dateien außerhalb des Volumes.
Dies bedeutet Folgendes: Wenn Sie den Containerzugriff auf Hostpfad-Volumes
mit PodSecurityPolicy blockieren, kann ein Angreifer, der in der Lage ist,
Pods zu aktualisieren oder zu erstellen, jeden beliebigen Hostpfad durch
Verwendung eines anderen Volume-Typs bereitstellen.

Aufgrund der Sicherheitslücke CVE-2017-1002102 können Container, die bestimmte
Volume-Typen verwenden, wie z. B. Secrets, Konfigurationspläne, projizierte
Volumes oder abwärtsgerichtete API-Volumes, Dateien außerhalb des Volumes
löschen. Das heißt, wenn ein Container, der einen dieser Volume-Typen
verwendet, gehackt wurde oder wenn Sie nicht vertrauenswürdigen Nutzern das
Erstellen von Pods ermöglichen, kann ein Angreifer diesen Container zum
Löschen von beliebigen Dateien auf dem Host nutzen.

Weitere Informationen zur Korrektur finden Sie im [ Kubernetes-Blogpost
](https://kubernetes.io/blog/2018/04/04/fixing-subpath-volume-vulnerability/)
.

|  Hoch  |

  * [ CVE-2017-1002101 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101)
  * [ CVE-2017-1002102 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102)

