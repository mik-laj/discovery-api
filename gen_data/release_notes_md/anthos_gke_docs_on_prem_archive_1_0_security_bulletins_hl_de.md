Sie betrachten die Dokumentation für eine frühere Version von GKE On-Prem. [
Sehen Sie sich die aktuelle Dokumentation an
](https://cloud.google.com/anthos/gke/docs/on-prem?hl=de) .

#  Sicherheitsbulletins

Alle Sicherheitsbulletins für GKE On-Prem werden in diesem Thema beschrieben.

Sicherheitslücken werden häufig geheim gehalten, bis die betroffenen Parteien
die Möglichkeit hatten, sie zu beheben. In diesen Fällen beziehen sich die [
Versionshinweise ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/release-notes?hl=de) von GKE On-Prem auf
"Sicherheitsupdates", bis das Embargo aufgehoben wurde. Sobald das geschehen
ist, werden die Hinweise mit Informationen über die durch den Patch behobene
Sicherheitslücke aktualisiert.

**Hinweis** : Wenn Sie Workloads mit mehreren Mandanten in GKE On-Prem
ausführen, achten Sie besonders auf diese Bulletins. Bei ihnen ist die
Wahrscheinlichkeit größer, dass sie durch diese Sicherheitslücken gefährdet
sind. Eine technische Beschreibung der Sicherheitsgrenzen in GKE und deren
Auswirkungen auf Arbeitslasten finden Sie unter [ Isolation at different
layers of the Kubernetes stack
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) .

Fügen Sie die URL dieser Seite Ihrem [ Feed-Reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) hinzu, damit Sie
die neuesten Sicherheitsbulletins erhalten.

##  23\. August 2019

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
Wir haben vor Kurzem eine Sicherheitslücke entdeckt und gemindert, bei der der
RBAC-Proxy, der zum Schutz der Monitoring-Endpunkte verwendet wird, Nutzer
nicht korrekt autorisiert hat. Daher sind Messwerte aus bestimmten Komponenten
für nicht autorisierte Nutzer innerhalb des internen Cluster-Netzwerks
verfügbar. Die folgenden Komponenten waren betroffen:

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

Wir empfehlen Ihnen, so schnell wie möglich ein [ Upgrade
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/how-
to/administration/upgrading-clusters?hl=de) Ihrer Cluster auf die Version [
1.0.2-gke.3 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/downloads?hl=de#gkectl_latest) durchzuführen, die den Patch
für diese Sicherheitslücke enthält.

|

Mittel

|

[ GKE On-Prem Releases ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/downloads?hl=de#gkectl_latest)  
  
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

Wir empfehlen Ihnen, so schnell wie möglich ein [ Upgrade
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/how-
to/administration/upgrading-clusters?hl=de) Ihrer Cluster auf die Version [
1.0.2-gke.3 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/downloads?hl=de#gkectl_latest) durchzuführen, die den Patch
für diese Sicherheitslücke enthält.

######  Welche Sicherheitslücke wird mit diesem Patch behoben?

Der Patch entschärft die Sicherheitslücke [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Mittelgroß

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

