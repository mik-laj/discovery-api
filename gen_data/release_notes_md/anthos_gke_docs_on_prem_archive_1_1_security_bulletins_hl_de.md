Sie betrachten die Dokumentation für eine frühere Version von GKE On-Prem. [
Sehen Sie sich die aktuelle Dokumentation an
](https://cloud.google.com/anthos/gke/docs/on-prem?hl=de) .

#  Sicherheitsbulletins

Alle Sicherheitsbulletins für GKE On-Prem werden in diesem Thema beschrieben.

Sicherheitslücken werden häufig geheim gehalten, bis die betroffenen Parteien
die Möglichkeit hatten, sie zu beheben. In diesen Fällen wird in den [
Versionshinweisen ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/release-notes?hl=de) von GKE On-Prem von "Security Updates"
(Sicherheitsupdates) gesprochen, bis die Geheimhaltungsverpflichtung
aufgehoben wurde. Sobald das geschehen ist, werden die Hinweise mit
Informationen über die durch den Patch behobene Sicherheitslücke aktualisiert.

**Hinweis** : Wenn Sie Workloads mit mehreren Mandanten in GKE On-Prem
ausführen, achten Sie besonders auf diese Bulletins. Bei ihnen ist die
Wahrscheinlichkeit größer, dass sie durch diese Sicherheitslücken gefährdet
sind. Eine technische Beschreibung der Sicherheitsgrenzen in GKE On-Prem und
deren Auswirkungen auf Arbeitslasten finden Sie unter [ Isolation at different
layers of the Kubernetes stack
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) .

Um die neuesten Sicherheitsbulletins zu erhalten, fügen Sie die URL dieser
Seite zu Ihrer [ Feed-Reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) hinzu.

##  16\. Oktober 2019

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
In Kubernetes wurde kürzlich eine in [ CVE-2019-11253
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253) beschriebene
Sicherheitslücke festgestellt. Sie erlaubt Nutzern, die POST-Anfragen stellen
dürfen, DoS-Remoteangriffe auf Kubernetes API-Server. Das Kubernetes Product
Security Committee (PSC) hat [ zusätzliche Informationen
](https://groups.google.com/forum/?hl=de#!topic/kubernetes-security-
announce/jk8polzSUxs) zu dieser Sicherheitslücke veröffentlicht.

Sie können diese Sicherheitslücke minimieren, indem Sie beschränken, welche
Clients Netzwerkzugriff auf Ihre Kubernetes API-Server haben.

######  Was soll ich tun?

Wir empfehlen ein [ Upgrade Ihrer Cluster
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/upgrading-clusters?hl=de) auf eine Patchversion, die den
Fehler behebt, sobald sie verfügbar ist.

Die Patchversionen, die das Update enthalten, sind unten aufgeführt:

  * Anthos 1.1.1 führt die Kubernetes-Version 1.13.7-gke.30 aus 

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
der für die Sicherung von Monitoring-Endpunkten verwendete RBAC-Proxy die
Nutzer nicht richtig autorisierte. Daher sind Messwerte aus bestimmten
Komponenten für nicht autorisierte Nutzer innerhalb des internen
Clusternetzwerks verfügbar. Die folgenden Komponenten waren betroffen:

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

Wir empfehlen Ihnen, [ ein Upgrade
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/upgrading-clusters?hl=de) Ihrer Cluster auf Version [
1.0.2-gke.3 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/downloads?hl=de#gkectl_latest) auszuführen, die den Patch für
diese Sicherheitslücke so schnell wie möglich enthält.

|

Mittel

|

[ GKE On-Prem-Releases ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/downloads?hl=de#gkectl_latest)  
  
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

Wir empfehlen Ihnen, [ ein Upgrade
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/upgrading-clusters?hl=de) Ihrer Cluster auf Version [
1.0.2-gke.3 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/downloads?hl=de#gkectl_latest) auszuführen, die den Patch für
diese Sicherheitslücke so schnell wie möglich enthält.

######  Welche Sicherheitslücke wird mit diesem Patch behoben?

Der Patch entschärft die Sicherheitslücke [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Mittel

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

