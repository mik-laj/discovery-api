Vous consultez la documentation d'une version précédente de GKE On-Prem. [
Consultez la documentation la plus récente
](https://cloud.google.com/anthos/gke/docs/on-prem?hl=fr) .

#  Bulletins de sécurité

Tous les bulletins de sécurité d'Anthos GKE On-Prem sont décrits dans cette
rubrique.

Les failles de sécurité sont souvent gardées secrètes jusqu'à ce que les
parties concernées aient eu la possibilité de les corriger. Si tel est le cas,
les [ Notes de version ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.2/release-notes?hl=fr) de GKE On-Prem font référence à des
"mises à jour de sécurité" jusqu'à la levée du secret. Les notes sont alors
mises à jour pour refléter les failles traitées par le correctif.

**Remarque :** Si vous exécutez des charges de travail mutualisées sur GKE On-
Prem, veuillez accorder une attention particulière à ces bulletins. En effet,
les failles qu'ils décrivent sont davantage susceptibles de toucher les
charges de travail mutualisées. Pour obtenir une description technique des
limites de sécurité dans GKE On-Prem et de l'impact de ces limites sur les
charges de travail, consultez l'article traitant de l' [ isolation au niveau
des différentes couches de la pile Kubernetes
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) .

Pour recevoir les derniers bulletins de sécurité, ajoutez l'URL de cette page
à votre [ lecteur de flux
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) .

##  16 octobre 2019

Description  |  Niveau de gravité  |  Notes  
---|---|---  
  
La faille [ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) a été récemment découverte dans
Kubernetes. Elle permet à tout utilisateur autorisé d'effectuer des requêtes
POST afin de réaliser une attaque par déni de service à distance sur un
serveur d'API Kubernetes. Le comité de sécurité des produits (PSC, Product
Security Committee) Kubernetes a publié des informations complémentaires sur
cette faille. Pour les consulter, cliquez [ ici
](https://groups.google.com/forum/?hl=fr#!topic/kubernetes-security-
announce/jk8polzSUxs) .

Vous pouvez atténuer cette faille en limitant les clients disposant d'un accès
réseau à vos serveurs API Kubernetes.

######  Que dois-je faire ?

Nous vous recommandons de [ mettre à jour votre cluster
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.2/how-
to/upgrading-clusters?hl=fr) vers une version du correctif permettant de
remédier à cette faille dès sa mise à disposition.

Les versions du correctif correspondantes sont indiquées ci-dessous :

  * Anthos 1.1.1, qui exécute Kubernetes version 1.13.7-gke.30 

######  Quelle faille ce correctif permet-il de résoudre ?

Le correctif réduit les risques liés à la faille suivante : [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253) .

|

Élevé

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
##  23 août 2019

Description  |  Niveau de gravité  |  Notes  
---|---|---  
  
Nous avons récemment découvert et atténué une faille dans laquelle le proxy
RBAC utilisé pour sécuriser les points de terminaison de surveillance
n'autorisait pas correctement les utilisateurs. Par conséquent, les
statistiques provenant de certains composants sont disponibles pour les
utilisateurs non autorisés à partir du réseau du cluster interne. Les
composants suivants ont été affectés :

  * ` etcd `
  * ` etcd-events `
  * ` kube-apiserver `
  * ` kube-controller-manager `
  * ` kube-scheduler `
  * ` node-exporter `
  * ` kube-state-metrics `
  * ` prometheus `
  * ` alertmanager `

######  Que dois-je faire ?

Nous vous recommandons de [ mettre à jour
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.2/how-
to/upgrading-clusters?hl=fr) vos clusters vers la version [ 1.0.2-gke.3
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.2/downloads?hl=fr#gkectl_latest) , qui inclut le correctif de
cette faille, dès que possible.

|

M

|

[ Versions d'Anthos GKE On-Prem ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.2/downloads?hl=fr#gkectl_latest)  
  
##  22 août 2019

Description  |  Niveau de gravité  |  Notes  
---|---|---  
  
La communauté Kubernetes a récemment découvert une faille de sécurité, [
CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) , qui permet d'intervenir sur les
instances de [ ressources personnalisées
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) à l'échelle d'un cluster comme s'il s'agissait d'objets présents
dans tous les espaces de noms. Cela signifie que les comptes utilisateur et de
service ne disposant que d'autorisations RBAC au niveau de l'espace de noms
peuvent interagir avec des ressources personnalisées à l'échelle du cluster.
Pour exploiter cette faille, le pirate informatique doit disposer de
privilèges permettant d'accéder aux ressources de n'importe quel espace de
noms.

######  Que dois-je faire ?

Nous vous recommandons de [ mettre à jour
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.2/how-
to/upgrading-clusters?hl=fr) vos clusters vers la version [ 1.0.2-gke.3
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.2/downloads?hl=fr#gkectl_latest) , qui inclut le correctif de
cette faille, dès que possible.

######  Quelle faille ce correctif permet-il de résoudre ?

Le correctif limite les risques liés à la faille suivante : [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Moyen

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

