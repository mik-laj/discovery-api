You are viewing documentation for a previous version of Anthos GKE on-prem. [
View the latest documentation ](https://cloud.google.com/anthos/gke/docs/on-
prem?hl=de) .

#  Sicherheitsbulletins

Alle Sicherheitsbulletins für Anthos GKE On-Prem (GKE On-Prem) werden in
diesem Thema beschrieben.

Sicherheitslücken werden häufig geheim gehalten, bis die betroffenen Parteien
die Möglichkeit hatten, sie zu beheben. In diesen Fällen verweisen die [
Versionshinweise ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.3/release-notes?hl=de) von GKE On-Prem auf
"Sicherheitsupdates", bis das Embargo aufgehoben wurde. Sobald das geschehen
ist, werden die Hinweise mit Informationen über die durch den Patch behobene
Sicherheitslücke aktualisiert.

**Hinweis:** Wenn Sie Workloads mit mehreren Mandanten in GKE On-Prem
ausführen, achten Sie besonders auf diese Bulletins. Bei ihnen ist die
Wahrscheinlichkeit größer, dass sie durch diese Sicherheitslücken gefährdet
sind. Eine technische Beschreibung der Sicherheitsgrenzen in GKE On-Prem und
deren Auswirkungen auf Arbeitslasten finden Sie unter [ Isolation auf
verschiedenen Ebenen des Kubernetes-Stapels
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) .

Um die neuesten Sicherheitsbulletins zu erhalten, fügen Sie die URL dieser
Seite Ihrem [ Feed-Reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) hinzu.

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
wie unten beschrieben auf die neueste Patchversion zu aktualisieren. Ein
Knotenupgrade ist nicht erforderlich.  

####  Was soll ich tun?

Die folgenden Anthos GKE On-Prem-Versionen (GKE On-Prem) oder höher enthalten
die Fehlerkorrektur für diese Sicherheitslücke:

  * Anthos 1.3.0 

Wenn Sie eine frühere Version verwenden, [ aktualisieren Sie Ihren vorhandenen
Cluster ](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.3/how-
to/upgrading?hl=de) auf eine Version, die diese Fehlerkorrektur enthält.

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
empfehlen Ihnen, ein Upgrade auf die neueste Patchversion auszuführen.

####  Was soll ich tun?

[ Aktualisieren Sie Ihre Cluster
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.3/how-
to/upgrading?hl=de) auf die folgende oder eine neuere Version, um diese
Sicherheitslücke für Anthos GKE On-Prem (GKE On-Prem) zu beheben:

  * Anthos 1.3.2 

Sehr wenige Container benötigen normalerweise ` CAP_NET_RAW ` . Diese und
andere leistungsstarke Funktionen sollten standardmäßig über [ Anthos Policy
Controller ](https://cloud.google.com/anthos-config-
management/docs/concepts/policy-controller?hl=de) oder durch Aktualisieren
Ihrer Pod-Spezifikationen blockiert werden:

  * So entfernen Sie die ` CAP_NET_RAW ` -Funktion aus Containern: 
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
  
  
##  GCP-2020-004

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
In Kubernetes wurde kürzlich eine in [ CVE-2019-11254
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11254) beschriebene
Sicherheitslücke festgestellt. Sie erlaubt Nutzern, die POST-Anfragen stellen
dürfen, DoS-Remoteangriffe auf Kubernetes API-Server. Das Kubernetes Product
Security Committee (PSC) hat [ zusätzliche Informationen
](https://groups.google.com/g/kubernetes-security-
announce/c/wuwEwZigXBc?hl=de) zu dieser Sicherheitslücke veröffentlicht.

Sie können diese Sicherheitslücke minimieren, indem Sie beschränken, welche
Clients Netzwerkzugriff auf Ihre Kubernetes API-Server haben.

####  Was soll ich tun?

Wir empfehlen Ihnen, Ihre Cluster so bald wie möglich auf eine Patchversion zu
aktualisieren, die diese Fehlerkorrektur enthält.

Die Patchversionen, mit denen die Sicherheitslücke behoben wird, sind unten
aufgeführt:

  * Anthos 1.3.0, auf dem Kubernetes Version 1.15.7-gke.32 ausgeführt wird 

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
  
##  16\. Oktober 2019

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
In Kubernetes wurde kürzlich eine in [ CVE-2019-11253
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253) beschriebene
Sicherheitslücke festgestellt. Sie erlaubt Nutzern, die POST-Anfragen stellen
dürfen, die Ausführung von DoS-Angriffen (Denial of Service) auf Kubernetes
API-Server. Das Kubernetes Product Security Committee (PSC) hat [ zusätzliche
Informationen ](https://groups.google.com/forum/?hl=de#!topic/kubernetes-
security-announce/jk8polzSUxs) zu dieser Sicherheitslücke veröffentlicht.

Sie können diese Sicherheitslücke minimieren, indem Sie beschränken, welche
Clients Netzwerkzugriff auf Ihre Kubernetes API-Server haben.

######  Was soll ich tun?

Wir empfehlen, so bald wie möglich ein [ Upgrade Ihrer Cluster
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.3/how-
to/upgrading-clusters?hl=de) auf eine Patchversion auszuführen, die eine
entsprechende Fehlerkorrektur enthält.

Die Patchversionen mit dieser Fehlerkorrektur sind unten aufgeführt:

  * Anthos 1.1.1, führt die Kubernetes-Version 1.13.7-gke.30 aus 

######  Welche Sicherheitslücke wird mit diesem Patch behoben?

Der Patch entschärft die Sicherheitslücke [ CVE-2019-11253
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253) .

|

Hoch

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
##  23\. August 2019

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
Wir haben vor Kurzem eine Sicherheitslücke entdeckt und beseitigt, durch die
der für Sicherheitsmonitoring-Endpunkte verwendete RBAC-Proxy die Nutzer nicht
richtig autorisierte. Daher sind Messwerte aus bestimmten Komponenten für
nicht autorisierte Nutzer innerhalb des internen Clusternetzwerks verfügbar.
Die folgenden Komponenten waren betroffen:

  * ` etcd `
  * ` etcd-events `
  * ` kube-apiserver `
  * ` kube-controller-manager `
  * ` kube-scheduler `
  * ` node-exporter `
  * ` kube-state-metrics `
  * ` prometheus `
  * ` alertmanager `

######  Was soll ich tun?

Wir empfehlen Ihnen, so schnell wie möglich [ ein Upgrade
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.3/how-
to/upgrading-clusters?hl=de) Ihrer Cluster auf Version [ 1.0.2-gke.3
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.3/downloads?hl=de#gkectl_latest) auszuführen, die den Patch für
diese Sicherheitslücke enthält.

|

Mittel

|

[ Anthos GKE-On-Premises-Releases
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.3/downloads?hl=de#gkectl_latest)  
  
##  22\. August 2019

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
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

Wir empfehlen Ihnen, so schnell wie möglich [ ein Upgrade
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.3/how-
to/upgrading-clusters?hl=de) Ihrer Cluster auf Version [ 1.0.2-gke.3
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.3/downloads?hl=de#gkectl_latest) auszuführen, die den Patch für
diese Sicherheitslücke enthält.

######  Welche Sicherheitslücke wird mit diesem Patch behoben?

Der Patch entschärft die Sicherheitslücke [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Mittel

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

