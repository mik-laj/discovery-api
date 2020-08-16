A new version of Anthos GKE on AWS was released on August 5. See the [ release
notes ](https://cloud.google.com/anthos/gke/docs/aws/release-notes?hl=de) for
information on breaking changes.

#  Sicherheitsbulletins

Informationen zu Sicherheitsbulletins für Anthos GKE on AWS (GKE on AWS)

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

Damit diese Sicherheitslücke in Clustern von GKE on AWS ausgenutzt wird, muss
ein Angreifer die [ Quell-Ziel-Prüfungen
](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html) auf
den EC2-Instanzen im Cluster deaktivieren. Dazu muss der Angreifer auf den
EC2-Instanzen AWS-IAM-Berechtigungen für ` ModifyInstanceAttribute ` oder `
ModifyNetworkInterfaceAttribute ` haben. Aus diesem Grund wurde dieser
Sicherheitslücke von GKE on AWS ein niedriger Schweregrad zugewiesen.

####  Was soll ich tun?

Aktualisieren Sie Ihren Cluster auf eine Patchversion, um diese
Sicherheitslücke zu schließen. Bei den folgenden geplanten Versionen von GKE
on AWS oder neueren Versionen soll diese Sicherheitslücke behoben werden:

  * GKE on AWS 1.4.2 

####  Welche Sicherheitslücke wird mit diesem Patch behoben?

Mit diesem Patch wird die folgende Sicherheitslücke behoben: [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) .

|

Niedrig

|

[ CVE-2020-8558 ](https://github.com/kubernetes/kubernetes/issues/92315)  
  
##  GCP-2020-009

**Veröffentlicht:** 15.7.2020  Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
Vor Kurzem wurde in Kubernetes eine Sicherheitslücke zur Rechteausweitung, [
CVE-2020-8559 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8559)
, entdeckt. Diese Sicherheitslücke ermöglicht es einem Angreifer, der bereits
einen Knoten manipuliert hat, in jedem Pod im Cluster einen Befehl
auszuführen. Der Angreifer kann dadurch mit dem bereits manipulierten Knoten
andere Knoten manipulieren und potenziell Informationen lesen oder destruktive
Aktionen ausführen.

Damit ein Angreifer diese Sicherheitslücke ausnutzen kann, muss bereits ein
Knoten im Cluster manipuliert worden sein. Diese Sicherheitslücke allein lässt
also nicht die Manipulation von Knoten in Ihrem Cluster zu.

####  Was soll ich tun?

GKE on AWS GA (1.4.1, verfügbar ab Ende Juli 2020) oder höher enthält den
Patch für diese Sicherheitslücke. Wenn Sie eine ältere Version verwenden, [
laden Sie eine neue Version des anthos-gke-Befehlszeilentools herunter
](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites?hl=de) und
erstellen Sie Ihre Verwaltungs- und Nutzercluster neu.

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
wie unten beschrieben auf die neueste Patchversion zu aktualisieren. Ein
Knotenupgrade ist nicht erforderlich.  

####  Was soll ich tun?

Anthos GKE on AWS (GKE on AWS) v0.2.0 oder höher enthält bereits den Patch für
diese Sicherheitslücke. Wenn Sie eine ältere Version verwenden, [ laden Sie
eine neue Version des anthos-gke-Befehlszeilentools herunter
](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites?hl=de) und
erstellen Sie Ihre Verwaltungs- und Nutzercluster neu.

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
empfehlen Ihnen, wie unten beschrieben ein Upgrade auf die neueste
Patchversion durchzuführen.

####  Was soll ich tun?

[ Laden Sie das anthos-gke-Befehlszeilentool herunter
](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites?hl=de) ,
das die folgende Version oder eine neuere Version enthält und erstellen Sie
Ihre Verwaltungs- und Nutzercluster neu:

  * aws-0.2.1-gke.7 

Sehr wenige Container benötigen normalerweise ` CAP_NET_RAW ` . Diese und
andere leistungsstarke Funktionen sollten standardmäßig über [ Anthos Policy
Controller ](https://cloud.google.com/anthos-config-
management/docs/concepts/policy-controller?hl=de) oder durch Aktualisieren
Ihrer Pod-Spezifikationen blockiert werden:

So entfernen Sie die ` CAP_NET_RAW ` -Funktion aus Containern:

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

