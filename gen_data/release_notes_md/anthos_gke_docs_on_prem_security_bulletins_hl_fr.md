#  Bulletins de sécurité

Tous les bulletins de sécurité d'Anthos GKE On-Prem (GKE On-Prem) sont décrits
dans cette rubrique.

Les failles de sécurité sont souvent gardées secrètes jusqu'à ce que les
parties concernées aient eu la possibilité de les corriger. Si tel est le cas,
les [ Notes de version ](https://cloud.google.com/anthos/gke/docs/on-
prem/release-notes?hl=fr) de GKE font référence à des "mises à jour de
sécurité" jusqu'à la levée du secret. Les notes sont alors mises à jour pour
refléter les failles traitées par le correctif.

**Remarque :** Si vous exécutez des charges de travail mutualisées sur GKE On-
Prem, veuillez accorder une attention particulière à ces bulletins. En effet,
les failles qu'ils décrivent sont davantage susceptibles de toucher les
charges de travail mutualisées. Pour obtenir une description technique des
limites de sécurité dans GKE On-Prem et de l'impact de ces limites sur les
charges de travail, consultez l'article traitant de l' [ isolation au niveau
des différentes couches de la pile Kubernetes
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) .

Pour recevoir les dernières mises à jour concernant ce produit, ajoutez l'URL
de cette page à votre [ lecteur de flux
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) .

##  GCP-2020-007

**Date de publication** : 2020-06-01  
Description  |  Niveau de gravité  |  Notes  
---|---|---  
  
La faille SSRF (Server Side Request Forgery, falsification de requête côté
serveur) [ CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555) a été récemment détectée dans Kubernetes.
Elle permet à certains utilisateurs autorisés de divulguer jusqu'à 500 octets
d'informations sensibles depuis le réseau hôte du plan de contrôle. Le plan de
contrôle de Google Kubernetes Engine (GKE) utilise des contrôleurs Kubernetes.
Il est donc concerné par cette faille. Nous vous recommandons de mettre à
niveau le plan de contrôle en installant la dernière version du correctif,
conformément à la procédure expliquée ci-dessous. Aucune mise à niveau de nœud
n'est requise.  

####  Que dois-je faire ?

Les versions d'Anthos GKE On-Prem (GKE On-Prem) suivantes ou ultérieures
contiennent le correctif de cette faille :

  * Anthos 1.3.0 

Si vous utilisez une version précédente, [ mettez à niveau votre cluster
existant ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/upgrading?hl=fr) vers une version contenant le correctif.

####  Quelle faille ce correctif permet-il de résoudre ?

Ce correctif réduit les risques liés à la faille CVE-2020-8555. La gravité de
cette faille est évaluée comme moyenne pour GKE, car elle était difficile à
exploiter en raison des diverses mesures de renforcement des plans de
contrôle.

Un pirate informatique autorisé à créer un pod avec certains types de volumes
intégrés (comme GlusterFS, Quobyte, StorageFS ou ScaleIO) ou à créer un objet
StorageClass, peut activer l'envoi de requêtes ` GET ` ou ` POST ` par ` kube-
controller-manager ` _sans_ que le corps de la requête contrôlée par le pirate
provienne du réseau hôte du maître. Ces types de volumes étant rarement
employés sur GKE, leur utilisation récente constitue un bon signal de
détection.

Associés à des moyens permettant de partager les résultats de la commande `
GET/POST ` avec le pirate (via des journaux, par exemple), ils peuvent
entraîner la divulgation d'informations sensibles. Nous avons mis à jour les
pilotes de stockage concernés afin de supprimer les risques de telles
divulgations.

|

Moyen

|

[ CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555)  
  
##  GCP-2020-006

**Date de publication** : 2020-06-01  
Description  |  Niveau de gravité  |  Notes  
---|---|---  
  
Kubernetes a divulgué une [ faille
](https://github.com/kubernetes/kubernetes/issues/91507) qui permet à un
conteneur privilégié de rediriger le trafic de nœuds vers un autre conteneur.
Le trafic TLS/SSH mutuel (entre le kubelet et le serveur d'API, ou en
provenance d'applications via le protocole mTLS) ne peut pas être lu ni
modifié par cette attaque. Tous les nœuds Google Kubernetes Engine (GKE) sont
affectés par cette faille. Par conséquent, nous vous recommandons de procéder
à la mise à niveau en installant la dernière version du correctif,
conformément à la procédure expliquée ci-dessous.

####  Que dois-je faire ?

Pour réduire les risques liés à cette faille dans Anthos GKE On-Prem (GKE On-
Prem), [ mettez à niveau vos clusters
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=fr)
vers la version suivante ou ultérieure :

  * Anthos 1.3.2 

Très peu de conteneurs nécessitent généralement ` CAP_NET_RAW ` . Il faut donc
la bloquer par défaut, ainsi que d'autres fonctionnalités puissantes, via [
Anthos Policy Controller ](https://cloud.google.com/anthos-config-
management/docs/concepts/policy-controller?hl=fr) ou en mettant à jour les
spécifications du pod :

  * Supprimez la fonctionnalité ` CAP_NET_RAW ` des conteneurs : 
    * En utilisant Anthos Policy Controller/Gatekeeper, avec ce [ modèle de contrainte ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) et en appliquant ce dernier. Exemple : 
        
                
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
        

    * En mettant à jour les spécifications du pod : 
        
                
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
        

####  Quelle faille ce correctif permet-il de résoudre ?

Ce correctif réduit les risques liés à la faille suivante :

La faille décrite dans l'article [ Problème Kubernetes 91507
](https://github.com/kubernetes/kubernetes/issues/91507) est liée à la
fonctionnalité ` CAP_NET_RAW ` (qui fait partie de l'ensemble de
fonctionnalités par défaut du conteneur). Elle configure de manière
malveillante la pile IPv6 sur le nœud, et redirige le trafic de nœuds vers le
conteneur contrôlé par le pirate. Cela permet au pirate d'intercepter ou de
modifier le trafic en provenance du nœud ou à destination de celui-ci. Le
trafic TLS/SSH mutuel (entre le kubelet et le serveur d'API, ou en provenance
d'applications via le protocole mTLS) ne peut pas être lu ni modifié par cette
attaque.

|

Moyen

|

[ Problème Kubernetes 91507
](https://github.com/kubernetes/kubernetes/issues/91507)  
  
  
##  GCP-2020-004

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
La faille [ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) a été récemment découverte dans
Kubernetes. Elle permet à tout utilisateur autorisé d'effectuer des requêtes
POST afin de réaliser une attaque par déni de service à distance sur un
serveur d'API Kubernetes. Le comité de sécurité des produits (PSC, Product
Security Committee) Kubernetes a publié des informations complémentaires sur
cette faille. Pour les consulter, [ cliquez ici
](https://groups.google.com/g/kubernetes-security-
announce/c/wuwEwZigXBc?hl=fr) .

Vous pouvez réduire les risques liés à cette faille en limitant les clients
disposant d'un accès réseau à vos serveurs d'API Kubernetes.

####  Que dois-je faire ?

Nous vous recommandons de mettre à jour vos clusters vers des versions de
correctif contenant le correctif de cette faille dès que ces versions sont
disponibles.

Les versions du correctif correspondantes sont indiquées ci-dessous :

  * Anthos 1.3.0, qui exécute la version 1.15.7-gke.32 de Kubernetes 

####  Quelles failles ce correctif permet-il de résoudre ?

Ce correctif permet de résoudre la faille de déni de service (DoS) suivante :

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) .

|

Moyen

|

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
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
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading-
clusters?hl=fr) vers une version du correctif permettant de remédier à cette
faille dès sa mise à disposition.

Les versions du correctif correspondantes sont indiquées ci-dessous :

  * Anthos 1.1.1, qui exécute la version 1.13.7-gke.30 de Kubernetes 

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
  
Nous avons récemment découvert et corrigé une faille de sécurité : le proxy
RBAC sécurisant les points de terminaison de surveillance n'autorisait pas
correctement les utilisateurs. Par conséquent, les statistiques de certains
composants étaient à la disposition des utilisateurs non autorisés au sein du
réseau de cluster interne. Les composants suivants ont été affectés :

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
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading-
clusters?hl=fr) vos clusters vers la version [ 1.0.2-gke.3
](https://cloud.google.com/anthos/gke/docs/on-
prem/downloads?hl=fr#gkectl_latest) , qui inclut le correctif de cette faille,
dès que possible.

|

M

|

[ Versions d'Anthos GKE On-Prem ](https://cloud.google.com/anthos/gke/docs/on-
prem/downloads?hl=fr#gkectl_latest)  
  
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
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading-
clusters?hl=fr) vos clusters vers la version [ 1.0.2-gke.3
](https://cloud.google.com/anthos/gke/docs/on-
prem/downloads?hl=fr#gkectl_latest) , qui inclut le correctif de cette faille,
dès que possible.

######  Quelle faille ce correctif permet-il de résoudre ?

Le correctif limite les risques liés à la faille suivante : [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Moyen

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

