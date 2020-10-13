#  Bulletins de sécurité

Cet article décrit tous les bulletins de sécurité qui s'appliquent à Google
Kubernetes Engine (GKE).

Les failles de sécurité sont souvent gardées secrètes jusqu'à ce que les
parties concernées aient eu la possibilité de les corriger. Si tel est le cas,
les [ notes de version ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=fr) de GKE font référence à des "mises à jour de
sécurité" jusqu'à la levée du secret. Les notes sont alors mises à jour pour
refléter les failles traitées par le correctif.

**Remarque** : Si vous exécutez des charges de travail mutualisées sur GKE,
veuillez accorder une attention particulière à ces bulletins. En effet, les
failles qu'ils décrivent sont davantage susceptibles de toucher les charges de
travail mutualisées. Pour obtenir une description technique des limites de
sécurité dans GKE et de l'impact de ces limites sur les charges de travail,
consultez l'article traitant de l' [ isolation au niveau des différentes
couches de la pile Kubernetes
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) .

Pour recevoir les derniers bulletins de sécurité, ajoutez l'URL de cette page
à votre [ lecteur de flux
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) . Vous pouvez
également ajouter l'URL du flux directement : `
https://cloud.google.com/feeds/kubernetes-engine-security-bulletins.xml `

##  GCP-2020-011

**Publié :** 2020-07-24  
Description  |  Niveau de gravité  |  Notes  
---|---|---  
  
Une faille réseau, [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) , a été récemment
détectée dans Kubernetes. Les services communiquent parfois avec d'autres
applications s'exécutant dans le même pod à l'aide de l'interface de
rebouclage local (127.0.0.1). Cette faille permet à un pirate informatique
ayant accès au réseau du cluster d'envoyer du trafic à l'interface de
rebouclage des pods et nœuds adjacents. Les services reposant sur l'interface
de rebouclage et non accessibles en dehors de leur pod peuvent être exploités.

Pour exploiter cette faille sur les clusters GKE, le pirate informatique doit
disposer de droits d'administrateur réseau sur le service Google Cloud
hébergeant le VPC du cluster. Cette faille seule n'accorde pas de privilèges
d'administrateur réseau au pirate informatique. Pour cette raison, le niveau
de gravité de cette faille est faible pour GKE.

####  Que dois-je faire ?

Pour corriger cette faille, [ mettez à jour
](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-
upgrades?hl=fr) les pools de nœuds de votre cluster vers les versions GKE
suivantes (ou ultérieures) :

  * 1.17.7-gke.0 
  * 1.16.11-gke.0 
  * 1.16.10-gke.11 
  * 1.16.9-gke.14 

####  Quelle faille ce correctif permet-il de résoudre ?

Ce correctif résout la faille suivante : [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) .

|

Faible

|

[ CVE-2020-8558 ](https://github.com/kubernetes/kubernetes/issues/92315)  
  
##  GCP-2020-009

**Publié :** 2020-07-15  Description  |  Niveau de gravité  |  Notes  
---|---|---  
  
Une faille d'élévation des privilèges, [ CVE-2020-8559
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8559) , a été
récemment détectée dans Kubernetes. Cette faille permet à un pirate
informatique ayant déjà compromis un nœud d'exécuter une commande dans
n'importe quel pod du cluster. Le pirate peut ainsi utiliser le nœud déjà
compromis pour en compromettre d'autres et potentiellement lire des
informations, ou provoquer des actions de destruction.

Notez que pour qu'un pirate informatique puisse exploiter cette faille, un
nœud de votre cluster doit déjà avoir été compromis. Cette faille, en elle-
même, ne compromettra pas les nœuds de votre cluster.

####  Que dois-je faire ?

[ Mettez à jour ](https://cloud.google.com/kubernetes-
engine/docs/concepts/cluster-upgrades?hl=fr) votre cluster vers une version
corrigée. Les clusters seront mis à jour automatiquement au cours des
prochaines semaines, et des versions corrigées seront disponibles d'ici le 19
juillet 2020 en suivant un calendrier accéléré des mises à jour manuelles. Les
versions suivantes du plan de contrôle GKE et les versions plus ultérieures
contiennent un correctif permettant de remédier à cette faille :

  * v1.14.10-gke.46 
  * v1.15.12-gke.8 
  * v1.16.9-gke.11 
  * v1.16.10-gke.9 
  * v1.16.11-gke.3+ 
  * v1.17.7-gke.6+ 

####  Quelle faille ce correctif permet-il de résoudre ?

Ce correctif réduit les risques liés à la faille CVE-2020-8559. La gravité de
cette faille est évaluée comme moyenne pour GKE, car elle nécessite que le
pirate informatique ait préalablement reçu des informations personnelles sur
le cluster, les nœuds et les charges de travail pour réaliser efficacement
cette attaque en plus de disposer d'une nœud compromis. Cette faille en elle-
même ne fournit pas un nœud compromis au pirate informatique.

|

Moyen

|

[ CVE-2020-8559 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8559)  
  
##  GCP-2020-007

**Date de publication** : 2020-06-01  
Description  |  Niveau de gravité  |  Notes  
---|---|---  
  
La faille SSRF (Server Side Request Forgery) [ CVE-2020-8555
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555) a été détectée
dans Kubernetes. Elle permet à certains utilisateurs autorisés de divulguer
jusqu'à 500 octets d'informations sensibles à partir du plan de contrôle du
réseau hôte. Le plan de contrôle de Google Kubernetes Engine (GKE) utilise des
contrôleurs Kubernetes. Il est donc concerné par cette faille. Nous vous
recommandons de [ mettre à jour ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-container-cluster?hl=fr) le plan de contrôle en
installant la dernière version du correctif, conformément à la procédure
expliquée ci-dessous. Il n'est pas nécessaire de mettre à niveau le nœud.  

####  Que dois-je faire ?

Pour la plupart des clients, aucune action n'est requise. La grande majorité
des clusters exécutent déjà une version corrigée. Les versions de GKE
suivantes, ainsi que les versions ultérieures, contiennent le correctif de
cette faille :

  * 1.14.7-gke.39 
  * 1.14.8-gke.32 
  * 1.14.9-gke.17 
  * 1.14.10-gke.12 
  * 1.15.7-gke.17 
  * 1.16.4-gke.21 
  * 1.17.0-gke.0 

Les clusters qui ont recours à des [ canaux de publication
](https://cloud.google.com/kubernetes-engine/docs/concepts/release-
channels?hl=fr) utilisent déjà les versions du plan de contrôle permettant de
réduire les risques liés à la faille.

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
  
Kubernetes a révélé la présence d'une [ faille
](https://github.com/kubernetes/kubernetes/issues/91507) autorisant un
conteneur privilégié à rediriger le trafic des nœuds vers un autre conteneur.
Le trafic TLS/SSH mutuel (entre le kubelet et le serveur d'API, ou en
provenance d'applications via le protocole mTLS) ne peut pas être lu ni
modifié par cette attaque. Tous les nœuds Google Kubernetes Engine (GKE) sont
affectés par cette faille. Par conséquent, nous vous recommandons de procéder
à la [ mise à niveau ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=fr) en installant la dernière version du correctif,
conformément à la procédure expliquée ci-dessous.

####  Que dois-je faire ?

Pour réduire les risques liés à cette faille, [ mettez
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=fr) votre plan de contrôle, puis vos nœuds en installant l'une des
versions corrigées répertoriées ci-dessous. Les clusters situés sur des canaux
de publication exécutent déjà une version corrigée aussi bien sur le plan de
contrôle que sur les nœuds :

  * 1.14.10-gke.36 
  * 1.15.11-gke.15 
  * 1.16.8-gke.15 

Très peu de conteneurs nécessitent généralement ` CAP_NET_RAW ` . Il faut donc
la bloquer par défaut, ainsi que d'autres fonctionnalités puissantes, via [
PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-
to/pod-security-policies?hl=fr) ou [ Anthos Policy Controller
](https://cloud.google.com/anthos-config-management/docs/concepts/policy-
controller?hl=fr) :

  * Supprimez la fonctionnalité ` CAP_NET_RAW ` des conteneurs : 
    * En appliquant cette mesure via [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=fr) à l'aide de la commande ci-dessous : 
        
                
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
        

    * Ou en utilisant Anthos Policy Controller/Gatekeeper, avec ce [ modèle de contrainte ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) et en appliquant ce dernier. Exemple : 
        
                
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
        

    * Ou en mettant à jour les spécifications du pod : 
        
                
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
  
  
##  GCP-2020-005

**Date de publication** : 07-05-2020  
**Dernière mise à jour** : 07-05-2020  Description  |  Niveau de gravité  |
Remarques  
---|---|---  
  
La faille [ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) a été récemment découverte dans le noyau
Linux. Elle permet de "s'échapper d'un conteneur" pour obtenir un accès root
(racine) sur le nœud hôte.

Cette faille affecte les nœuds Ubuntu exécutant Google Kubernetes Engine (GKE)
version 1.16 ou 1.17. Nous vous recommandons donc d'effectuer dès que possible
une mise à niveau en installant la dernière version du correctif, conformément
à la procédure décrite ci-dessous.

Les nœuds exécutant Container-Optimized OS ne sont pas concernés, ni ceux
exécutant GKE On-Prem.

####  Que dois-je faire ?

**Pour la plupart des clients, aucune action n'est requise. Seuls les nœuds
Ubuntu exécutant GKE version 1.16 ou 1.17 sont concernés.**

Avant tout, vous devez mettre à niveau votre nœud maître vers la toute
dernière version. Le correctif sera disponible dans Kubernetes 1.16.8-gke.12
et 1.17.4-gke.10, ainsi que dans les versions ultérieures. Pour vérifier la
disponibilité de ces correctifs, consultez les [ notes de version
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=fr) .

####  Quelle faille ce correctif permet-il de résoudre ?

Ce correctif réduit les risques liés à la faille suivante :

La faille [ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) affecte les versions 5.5.0 et ultérieures
du noyau Linux. Elle permet à un conteneur malveillant d'accéder en lecture et
en écriture à la mémoire du noyau, et ainsi d'exécuter des codes avec un accès
root par le biais d'un simple appel système "exec". La gravité de cette faille
est évaluée comme élevée.

|

Élevé

|

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835)  
  
  
##  GCP-2020-003

**Date de publication** : 31-03-2020  
**Dernière mise à jour** : 31-03-2020  Description  |  Niveau de gravité  |
Remarques  
---|---|---  
  
La faille [ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) a été récemment découverte dans
Kubernetes. Elle permet à tout utilisateur autorisé d'effectuer des requêtes
POST afin de réaliser une attaque par déni de service à distance sur un
serveur d'API Kubernetes. Le comité de sécurité des produits (PSC, Product
Security Committee) Kubernetes a publié des informations complémentaires sur
cette faille. Pour les consulter, [ cliquez ici
](https://groups.google.com/forum/?hl=fr#!topic/kubernetes-security-
announce/wuwEwZigXBc) .

Les clusters GKE qui utilisent des [ réseaux autorisés maîtres
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=fr) et des [ clusters privés sans accès à un point de terminaison
public ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=fr#private_master) réduisent les risques liés à cette faille.

####  Que dois-je faire ?

Nous vous recommandons de mettre à niveau votre cluster vers une version du
correctif permettant de remédier à cette faille.

Les versions du correctif correspondantes sont indiquées ci-dessous :

  * 1.13.12-gke.29 
  * 1.14.9-gke.27 
  * 1.14.10-gke.24 
  * 1.15.9-gke.20 
  * 1.16.6-gke.1 

####  Quelles failles ce correctif permet-il de résoudre ?

Ce correctif permet de résoudre la faille de déni de service (DoS) suivante :

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) .

|

Moyen

|

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  GCP-2020-002

**Date de publication** : 23-03-2020  
**Dernière mise à jour** : 23-03-2020  Description  |  Niveau de gravité  |
Remarques  
---|---|---  
  
La communauté Kubernetes a divulgué [ deux failles de déni de service
](https://groups.google.com/forum/?hl=fr#!topic/kubernetes-security-
announce/2UOlsba2g0s) , l'une affectant le serveur d'API et l'autre ayant des
conséquences sur les kubelets. Pour en savoir plus, reportez-vous aux
problèmes Kubernetes [ 89377
](https://github.com/kubernetes/kubernetes/issues/89377) et [ 89378
](https://github.com/kubernetes/kubernetes/issues/89378) .

####  Que dois-je faire ?

Tous les utilisateurs de GKE sont protégés contre la faille CVE-2020-8551 tant
que les utilisateurs non approuvés ne peuvent pas envoyer de requêtes au sein
du réseau interne du cluster. L'utilisation des [ réseaux autorisés maîtres
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=fr) réduit également les risques liés à la faille CVE-2020-8552.

####  Quand des correctifs seront-ils appliqués ?

Les correctifs de la faille CVE-2020-8551 nécessitent une mise à niveau des
nœuds. Les versions du correctif permettant de réduire les risques liés à
cette faille sont indiquées ci-dessous :

  * 1.15.10-gke* 
  * 1.16.7-gke* 

Remarque : Cette faille n'affecte pas les versions 1.14.x et antérieures. Par
conséquent, aucun correctif n'est requis.

Les correctifs de la faille CVE-2020-8552 nécessitent une mise à niveau du
maître. Les versions du correctif permettant de réduire les risques liés à
cette faille sont indiquées ci-dessous :

  * 1.14.10-gke.32 
  * 1.15.10-gke* 
  * 1.16.7-gke* 

|

Moyen

|

[ CVE-2020-8551 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8551)  
[ CVE-2020-8552 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8552)  
  
##  21 janvier 2020 (dernière mise à jour le 24 janvier 2020)

**Date de publication** : 21-01-2020  
**Dernière mise à jour** : 24-01-2020  Description  |  Niveau de gravité  |
Remarques  
---|---|---  
  
**Mise à jour du 24/01/2020** : le processus de mise à disposition des
versions corrigées est en cours et devrait s'achever le 25 janvier 2020.

* * *

Microsoft a révélé la présence d'une faille dans l'API Windows Crypto et son
processus de validation des signatures à courbes elliptiques. Pour en savoir
plus, consultez le [ communiqué de Microsoft
](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) .

**Que dois-je faire ?**

**Pour la plupart des clients, aucune action n'est requise. Seuls les nœuds
qui exécutent Windows Server sont concernés.**

Les clients qui utilisent les nœuds Windows Server doivent mettre à jour à la
fois les nœuds et les charges de travail en conteneur exécutées sur ceux-ci,
en installant les versions corrigées pour réduire les risques liés à cette
faille.

**Pour mettre à jour les conteneurs, procédez comme suit :**

Recréez vos conteneurs à l'aide des dernières images de conteneurs de base de
Microsoft. Pour cela, sélectionnez un tag [ servercore
](https://hub.docker.com/_/microsoft-windows-servercore) ou [ nanoserver
](https://hub.docker.com/_/microsoft-windows-nanoserver) dont la mise à jour
la plus récente a été effectuée le 14 janvier 2020 ou après cette date.

**Pour mettre à jour les nœuds, procédez comme suit :**

Le processus de mise à disposition des versions corrigées est en cours et
s'achèvera d'ici le 24 janvier 2020.

Vous pouvez soit patienter jusqu'à cette date et effectuer une mise à jour des
nœuds en installant une version corrigée de GKE, soit utiliser Windows Update
pour déployer le dernier correctif Windows manuellement à tout moment.

Vous trouverez ci-dessous la liste des versions du correctif permettant de
réduire les risques liés à cette faille :

  * 1.14.7-gke.40 
  * 1.14.8-gke.33 
  * 1.14.9-gke.23 
  * 1.14.10-gke.17 
  * 1.15.7-gke.23 
  * 1.16.4-gke.22 

**Quelles failles ce correctif permet-il de résoudre ?**

Ce correctif réduit les risques liés aux failles suivantes :

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601) (aussi appelée la [ faille de spoofing de
l'API Windows Crypto ](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) ) : un pirate peut l'exploiter pour faire en
sorte que ses fichiers exécutables malveillants soient considérés comme
fiables ou encore pour procéder à des attaques de type MITM ("man in the
middle") afin de déchiffrer des informations confidentielles diffusées via les
connexions TLS associées aux logiciels concernés par la faille.

|

Score de base NVD : 8,1 (élevé)

|

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601)  
  
  
##  14 novembre 2019

**Date de publication** : 14-11-2019  
**Dernière mise à jour** : 14-11-2019  Description  |  Niveau de gravité  |
Remarques  
---|---|---  
  
La communauté Kubernetes a divulgué une faille de sécurité dans les side-cars
kubernetes-csi [ ` external-provisioner ` ](https://github.com/kubernetes-
csi/external-provisioner) , [ ` external-snapshotter `
](https://github.com/kubernetes-csi/external-snapshotter) et [ ` external-
resizer ` ](https://github.com/kubernetes-csi/external-resizer) . Celle-ci
affecte la plupart des versions des side-cars regroupés dans les [ pilotes
Container Storage Interface (CSI) ](https://kubernetes-
csi.github.io/docs/drivers.html) . Pour en savoir plus, consultez le [
communiqué de Kubernetes
](https://github.com/kubernetes/kubernetes/issues/85233) .

**Que dois-je faire ?**  
**Cette faille n'a pas d'incidence sur les composants GKE gérés.** Vous pouvez
être affecté si vous gérez vos propres pilotes CSI dans des [ clusters alpha
GKE ](https://cloud.google.com/kubernetes-engine/docs/concepts/alpha-
clusters?hl=fr) exécutant GKE version 1.12 ou ultérieure. Si vous êtes
concerné par ce problème, renseignez-vous auprès de votre fournisseur de
pilotes CSI afin d'obtenir les instructions de mise à niveau.

**Quelles failles ce correctif permet-il de résoudre ?**  
[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255) : cette faille CVE concerne les side-cars
` kubernetes-csi ` [ ` external-provisioner ` ](https://github.com/kubernetes-
csi/external-provisioner) , [ ` external-snapshotter `
](https://github.com/kubernetes-csi/external-snapshotter) et [ ` external-
resizer ` ](https://github.com/kubernetes-csi/external-resizer) . Elle peut
permettre d'accéder aux données d'un volume ou de procéder à leur mutation
sans autorisation. Elle affecte la plupart des versions des side-cars
regroupés dans les [ pilotes CSI ](https://kubernetes-
csi.github.io/docs/drivers.html) .

|

Moyen

|

[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255)  
  
  
##  12 novembre 2019

**Date de publication** : 12-11-2019  
**Dernière mise à jour** : 12-11-2019  Description  |  Niveau de gravité  |
Remarques  
---|---|---  
  
Intel a divulgué des failles CVE qui permettent des interactions entre
l'exécution spéculative et l'état microarchitectural afin d'exposer les
données. Pour en savoir plus, consultez le [ communiqué d'Intel
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) .

**L'infrastructure hôte qui exécute Kubernetes Engine isole les charges de
travail des clients. À moins que vous n'exécutiez du code non approuvé dans
vos propres clusters GKE mutualisés _et_ que vous n'utilisiez des nœuds N2, M2
ou C2, aucune autre action n'est requise. ** Pour les instances GKE exécutées
sur des nœuds N1, aucune nouvelle action n'est requise.

Si vous exécutez Anthos GKE On-Prem, l'exposition dépend du matériel. Veuillez
comparer votre infrastructure à celle décrite dans le [ communiqué d'Intel
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) .

####  Que dois-je faire ?

**Vous n'êtes affecté que si vous utilisez des pools de nœuds N2, M2 ou C2
_et_ si ces nœuds utilisent du code non approuvé dans vos propres clusters GKE
mutualisés. **

**Le redémarrage des nœuds permet d'appliquer le correctif.** Le moyen le plus
simple de redémarrer l'ensemble des nœuds de votre pool consiste à effectuer
une opération de [ mise à niveau ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=fr#upgrade_nodes) . Celle-ci force
le redémarrage de tous les nœuds du pool concerné.  

Remarque : Il n'est pas nécessaire de changer de version lors d'une mise à
niveau. Vous pouvez lancer une mise à niveau vers la même version d'un nœud
avec l'option ` cluster-version ` .

####  Quelles failles ce correctif permet-il de résoudre ?

Ce correctif réduit les risques liés aux failles suivantes :

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)
: cette faille CVE est également appelée TSX Async Abort (TAA). L'attaque TAA
fournit un autre moyen d'exfiltrer des données qui utilise les mêmes
structures de données microarchitecturales que celles exploitées par les
failles [ Microarchitectural Data Sampling (MDS)
](https://cloud.google.com/kubernetes-engine/docs/security-
bulletins?hl=fr#may-14-2019) .

[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)
: faille de déni de service (DoS) affectant les hôtes des machines virtuelles
de sorte qu'un système invité malveillant puisse provoquer le plantage d'un
hôte non protégé. Cette faille CVE est également appelée "Machine Check Error
on Page Size Change" (Erreur de vérification de machine lors de la
modification de la taille de page). Elle n'affecte pas GKE.

|

Moyen

|

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)  
[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)  
  
##  22 octobre 2019

**Date de publication** : 22-10-2019  
**Dernière mise à jour** : 22-10-2019  Description  |  Niveau de gravité  |
Remarques  
---|---|---  
  
La faille [ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276) a été récemment découverte dans le
langage de programmation Go. Elle peut affecter les configurations Kubernetes
utilisant un proxy d'authentification. Pour en savoir plus, consultez le [
communiqué de Kubernetes
](https://groups.google.com/forum/?hl=fr#!topic/kubernetes-security-
announce/PtsUCqFi4h4) .

Kubernetes Engine n'est pas affecté par cette faille, car il ne permet pas la
configuration d'un proxy d'authentification.

|

Aucun

|

[ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276)  
  
  
##  16 octobre 2019

**Date de publication** : 16-10-2019  
**Dernière mise à jour** : 24-10-2019  Description  |  Niveau de gravité  |
Remarques  
---|---|---  
  
**Mise à jour du 24/10/2019** : les versions corrigées sont désormais
disponibles dans toutes les zones.

* * *

La faille [ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) a été récemment découverte dans
Kubernetes. Elle permet à tout utilisateur autorisé à effectuer des requêtes
POST de réaliser une attaque par déni de service à distance sur un serveur
d'API Kubernetes. Le comité de sécurité des produits (PSC, Product Security
Committee) Kubernetes a publié des informations complémentaires sur cette
faille. Pour les consulter, [ cliquez ici
](https://groups.google.com/forum/?hl=fr#!topic/kubernetes-security-
announce/jk8polzSUxs) .

Les clusters GKE qui utilisent des [ réseaux autorisés maîtres
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=fr) et des [ clusters privés sans accès à un point de terminaison
public ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=fr#private_master) réduisent les risques liés à cette faille.

######  Que dois-je faire ?

Nous vous recommandons de mettre à niveau votre cluster vers une version du
correctif permettant de remédier à cette faille dès sa mise à disposition.
Elle devrait être proposée dans toutes les zones avec la version de GKE
planifiée pour la semaine du 14 octobre.

Les versions du correctif permettant de limiter les risques liés à cette
faille sont indiquées ci-dessous.

  * 1.12.10-gke.15 
  * 1.13.11-gke.5 
  * 1.14.7-gke.10 
  * 1.15.4-gke.15 

######  Quelles failles ce correctif permet-il de résoudre ?

Ce correctif réduit les risques liés aux failles suivantes :

CVE-2019-11253 est une faille par déni de service (DoS).

|

Élevé

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
  
##  16 septembre 2019

**Date de publication** : 16-09-2019  
**Dernière mise à jour** : 16-10-2019  Description  |  Niveau de gravité  |
Remarques  
---|---|---  
  
Ce bulletin a été mis à jour depuis sa publication initiale.

Le langage de programmation Go a récemment découvert de nouvelles failles de
sécurité, [ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) et [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) . Il s'agit de
failles par déni de service (DoS). Dans GKE, elles permettent à un utilisateur
de créer des requêtes malveillantes qui surutilisent le processeur du serveur
d'API Kubernetes, ce qui risque de réduire la disponibilité du plan de
contrôle du cluster. Pour en savoir plus, consultez le [ communiqué sur le
langage de programmation Go
](https://groups.google.com/forum/?hl=fr#!topic/golang-announce/65QixT3tcmg) .

######  Que dois-je faire ?

Nous vous recommandons de mettre à niveau votre cluster vers la dernière
version du correctif, qui permet de limiter les risques liés à cette faille,
dès sa mise à disposition. Elle devrait être proposée dans toutes les zones
avec la prochaine version de GKE, selon le [ calendrier des lancements
](https://cloud.google.com/kubernetes-engine/docs/release-notes-
archive?hl=fr#september_16_2019) .

Les versions du correctif permettant de limiter les risques liés à cette
faille sont indiquées ci-dessous.

  * **Mise à jour du 16 octobre 2019** : 1.12.10-gke.15 
  * 1.13.10-gke.0 
  * 1.14.6-gke.1 

######  Quelles failles ce correctif permet-il de résoudre ?

Ce correctif réduit les risques liés aux failles suivantes :

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) et [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) sont des
failles par déni de service (DoS).

|

Élevé

|

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512)  
[ CVE-2019-9514 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9514)  
  
  
##  5 septembre 2019

**Date de publication** : 05-09-2019  
**Dernière mise à jour** : 05-09-2019

Le bulletin concernant le correctif de la faille documentée dans le bulletin
du  31 mai 2019  a été mis à jour.

##  22 août 2019

**Date de publication** : 22-08-2019  
**Dernière mise à jour** : 22-08-2019

Le bulletin du  5 août 2019  a été mis à jour. Le correctif de la faille
documentée dans le bulletin antérieur est [ disponible
](https://cloud.google.com/kubernetes-engine/docs/release-notes-
archive?hl=fr#august_22_2019) .

##  8 août 2019

**Date de publication** : 08-08-2019  
**Dernière mise à jour** : 08-08-2019

Le bulletin du  5 août 2019  a été mis à jour. Le correctif de la faille
documentée dans ce bulletin devrait être disponible dans la prochaine version
de GKE.

##  5 août 2019

**Date de publication** : 05-08-2019  
**Dernière mise à jour** : 09-08-2019  Description  |  Niveau de gravité  |
Remarques  
---|---|---  
  
Ce bulletin a été mis à jour depuis sa publication initiale.

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

Nous vous recommandons de [ mettre à niveau
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=fr) votre cluster vers la dernière version du correctif, qui permet
de limiter les risques liés à cette faille, dès sa mise à disposition. Elle
devrait être proposée dans toutes les zones avec la prochaine version de GKE.
Les versions du correctif permettant de limiter les risques liés à cette
faille sont indiquées ci-dessous.

  * 1.11.10-gke.6 
  * 1.12.9-gke.13 
  * 1.13.7-gke.19 
  * 1.14.3-gke.10 ( [ canal rapide ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels?hl=fr) ) 

######  Quelle faille ce correctif permet-il de résoudre ?

Le correctif limite les risques liés à la faille suivante : [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Moyen

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)  
  
##  3 juillet 2019

**Date de publication** : 03-07-2019  
**Dernière mise à jour** : 03-07-2019  Description  |  Niveau de gravité  |
Remarques  
---|---|---  
  
Une version corrigée de ` kubectl ` permettant de remédier à la faille
CVE-2019-11246 est désormais disponible avec [ ` gcloud ` 253.0.0
](https://cloud.google.com/sdk/docs/release-notes?hl=fr#kubernetes_engine) .
Pour en savoir plus, consultez le  bulletin de sécurité du 25 juin 2019  .

**Remarque** : Le correctif n'est pas disponible dans ` kubectl ` 1.11.10.

|

Élevé

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  3 juillet 2019

**Date de publication** : 25-06-2019  
**Dernière mise à jour** : 03-07-2019  Description  |  Niveau de gravité  |
Remarques  
---|---|---  
  
######  Mise à jour du 3 juillet 2019

Lors de notre dernière mise à jour, les correctifs des versions 1.11.9 et
1.11.10 n'étaient pas encore disponibles. Nous avons publié 1.11.10-gke.5 en
tant que cible de mise à niveau des deux versions 1.11.

À l'heure actuelle, les instances maîtres de GKE ont été corrigées, de même
que l'infrastructure de Google qui exécute Kubernetes Engine. Celle-ci est
donc protégée contre cette faille.

Les instances maîtres 1.11 seront bientôt obsolètes. La mise à niveau vers la
version 1.12 est planifiée pour s'exécuter automatiquement la semaine du 8
juillet 2019. Vous pouvez exécuter l'une des actions suggérées ci-dessous pour
mettre à niveau les nœuds vers une version corrigée.

  * Procédez à la mise à niveau des nœuds vers 1.11.10-gke.5 d'ici le 8 juillet 2019. Après cette date, les versions 1.11 commenceront à être supprimées de la liste des cibles de mise à niveau disponibles. 
  * Activez les [ mises à niveau automatiques ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades?hl=fr) sur les nœuds 1.11 et faites en sorte qu'elles aient lieu lorsque les instances maîtres sont mises à niveau vers la version 1.12. 
  * [ Mettez à niveau manuellement ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=fr) les instances maîtres et les nœuds vers une version 1.12 corrigée. 

Bulletin initial du 24 juin 2019 :

* * *

######  Mise à jour du 24 juin 2019

Depuis le 22/06/2019 21:40 UTC, nous avons mis à disposition les versions
corrigées de Kubernetes qui sont indiquées ci-dessous. Les instances maîtres
exécutant des versions de Kubernetes comprises entre 1.11.0 et 1.13.6 seront
automatiquement mises à niveau vers une version corrigée. Si vous n'exécutez
pas une version compatible avec ce correctif, procédez à la mise à niveau vers
une version compatible de l'instance maître (voir la liste ci-dessous) avant
de mettre à niveau les nœuds.

**En raison de la gravité de ces failles, que la mise à niveau automatique des
nœuds soit activée ou non, nous vous recommandons de[ mettre à niveau
manuellement ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-container-cluster?hl=fr) dès que possible les nœuds et les
instances maîtres vers l'une de ces versions. **

Versions corrigées :

  * 1.11.8-gke.10 
  * 1.12.7-gke.24 
  * 1.12.8-gke.10 
  * 1.13.6-gke.13 

Bulletin initial du 18 juin 2019 :

* * *

Récemment, Netflix a révélé trois failles TCP dans les noyaux Linux :

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

Ces failles CVE sont collectivement désignées par l'appellation [
NFLX-2019-001 ](https://github.com/Netflix/security-
bulletins/blob/master/advisories/third-party/2019-001.md) .

Les noyaux Linux non corrigés peuvent être vulnérables face aux attaques par
déni de service déclenchées à distance. **Les nœuds Google Kubernetes Engine
qui envoient ou reçoivent du trafic réseau non approuvé sont affectés. Par
conséquent, nous vous recommandons de suivre les procédures de limitation des
risques qui sont présentées ci-dessous pour protéger vos charges de travail.**

######  Instances maîtres Kubernetes

  * Les instances maîtres Kubernetes utilisant des [ réseaux autorisés ](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks?hl=fr) pour limiter le trafic vers les réseaux approuvés ne sont pas affectées. 

  * Les instances maîtres des clusters GKE, qui sont gérées par Google, seront corrigées automatiquement dans les prochains jours. Aucune action n'est requise de la part du client. 

######  Nœuds Kubernetes

Les nœuds qui limitent le trafic vers les réseaux approuvés ne sont pas
affectés. Ils correspondent à des clusters présentant les caractéristiques
suivantes :

  * Nœuds qui sont protégés par un pare-feu contre les réseaux non approuvés ou qui n'ont pas d'adresse IP publique ( [ clusters privés ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters?hl=fr) ) 
  * Clusters ne disposant pas de service LoadBalancer public 

Google prépare un correctif permanent pour ces failles. Il sera proposé sous
la forme d'une nouvelle version de nœud. Nous mettrons à jour ce bulletin et
enverrons un e-mail à tous les clients GKE pour les avertir de la
disponibilité de ce correctif.

En attendant que le correctif permanent soit disponible, nous avons créé un
DaemonSet Kubernetes qui met en œuvre les mesures d'atténuation en modifiant
la configuration ` iptables ` de l'hôte.

#####  Que dois-je faire ?

Appliquez le DaemonSet Kubernetes à tous les nœuds de votre cluster en
exécutant la commande ci-dessous. Vous ajoutez ainsi une règle ` iptables `
aux règles ` iptables ` existantes du nœud afin de limiter les risques liés à
la faille. **Exécutez la commande une fois pour chaque cluster et chaque
projet Google Cloud.**

    
    
    
    kubectl apply -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

Le protocole Ipv6 n'étant pas compatible avec GKE, aucune règle "ip6tables"
n'est requise.

Dès qu'une version de nœud corrigée sera disponible et que vous aurez mis à
niveau tous les nœuds susceptibles d'être affectés, vous pourrez supprimer le
DaemonSet à l'aide de la commande ci-dessous. **Exécutez la commande une fois
pour chaque cluster et chaque projet Google Cloud.**

    
    
    
    kubectl delete -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

|  Élevé  
Moyen  
Moyen  
|  [ CVE-2019-11477 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11477)  
[ CVE-2019-11478 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11478)  
[ CVE-2019-11479 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11479)  
  
  
##  25 juin 2019

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
**Mise à jour du 03/07/2019** : ce correctif est disponible dans ` gcloud `
253.0.0 pour les versions 1.12.9, 1.13.6 et 1.14.2 de ` kubectl ` , ainsi que
les versions plus récentes.

**Remarque** : Le correctif n'est pas disponible dans la version 1.11.10.

* * *

La communauté Kubernetes a récemment découvert la faille [ CVE-2019-11246
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11246) , qui permet
à un pirate informatique ayant accès à une opération ` kubectl cp ` et à
l'exécution de code dans un conteneur de modifier les fichiers se trouvant sur
l'hôte. Par le biais de cette attaque, le pirate est en mesure de remplacer ou
de créer un fichier dans le système de fichiers de l'hôte. Pour en savoir
plus, consultez le [ communiqué de Kubernetes
](https://groups.google.com/forum/?hl=fr#!topic/kubernetes-security-
announce/NLs2TGbfPdo) .

**Toutes les versions de` gcloud ` sur Google Kubernetes Engine (GKE) sont
affectées par cette faille. Par conséquent, nous vous recommandons de procéder
à la mise à niveau vers la dernière version du correctif de ` gcloud `
lorsqu'elle sera disponible. ** Une prochaine version du correctif permettra
de limiter les risques liés à cette faille.

######  Que dois-je faire ?

Une version corrigée de ` kubectl ` sera disponible dans une prochaine version
de ` gcloud ` . Vous pouvez également procéder vous-même à la [ mise à niveau
de ` kubectl ` directement ](https://kubernetes.io/docs/tasks/tools/install-
kubectl/) .

Pour vérifier la disponibilité de ce correctif, consultez les [ notes de
version de ` gcloud ` ](https://cloud.google.com/sdk/docs/release-notes?hl=fr)
.

######  Quelle faille ce correctif permet-il de résoudre ?

La faille [ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) permet à un pirate informatique ayant
accès à une opération ` kubectl cp ` et à l'exécution de code dans un
conteneur de modifier les fichiers se trouvant sur l'hôte. Par le biais de
cette attaque, le pirate peut être en mesure de remplacer ou de créer un
fichier dans le système de fichiers de l'hôte.

|

Élevé

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  18 juin 2019

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
Docker a récemment découvert la faille [ CVE-2018-15664
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-15664) , qui permet
à un pirate informatique pouvant exécuter du code dans un conteneur de
détourner une opération ` docker cp ` lancée en externe. Par le biais de cette
attaque, le pirate est en mesure de remplacer l'endroit où un fichier est
écrit par un emplacement arbitraire dans le système de fichiers de l'hôte.

**Tous les nœuds Google Kubernetes Engine (GKE) exécutant Docker sont affectés
par cette faille. Par conséquent, nous vous recommandons de procéder à la mise
à niveau vers la dernière version du correctif dès qu'elle sera disponible.
Une prochaine version du correctif permettra de limiter les risques liés à
cette faille.**

**Toutes les instances maîtres Google Kubernetes Engine (GKE) antérieures à la
version 1.12.7 exécutent Docker et sont affectées par cette faille.** Sur GKE,
les utilisateurs n'ont pas accès à ` docker cp ` sur l'instance maître. Par
conséquent, les risques liés à cette faille sont limités pour les instances
maîtres de GKE.

#####  Que dois-je faire ?

Seuls les nœuds exécutant Docker sont affectés, et uniquement lorsqu'une
commande ` docker cp ` (ou une API équivalente) susceptible d'être piratée est
exécutée. Ce cas de figure devrait se présenter assez rarement dans un
environnement Kubernetes. Les nœuds exécutant [ COS avec containerd
](https://cloud.google.com/kubernetes-engine/docs/concepts/using-
containerd?hl=fr) ne sont pas affectés.

Pour mettre à niveau vos nœuds, vous devez d'abord [ mettre à niveau votre
instance maître ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=fr#upgrading_the_cluster) vers la version corrigée.
Lorsque le correctif sera disponible, vous pourrez lancer une mise à niveau de
l'instance maître ou attendre que Google procède automatiquement à cette
opération. Le correctif sera disponible dans Docker 18.09.7, qui figurera dans
un prochain correctif de GKE. **Ce correctif ne sera proposé que pour les
versions 1.13 et ultérieures de GKE.**

Nous mettrons automatiquement à niveau les instances maîtres du cluster vers
la version corrigée, selon le rythme de mise à niveau habituel. Vous pourrez
également lancer vous-même une mise à niveau des instances maîtres lorsque la
version corrigée sera disponible.

Nous mettrons à jour ce bulletin en y ajoutant les versions contenant un
correctif une fois qu'elles seront disponibles. Pour vérifier la disponibilité
de ces correctifs, consultez les [ notes de version
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=fr) .

#####  Quelle faille ce correctif permet-il de résoudre ?

Ce correctif réduit les risques liés à la faille suivante :

La faille [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) permet à un pirate informatique pouvant
exécuter du code dans un conteneur de détourner une opération ` docker cp `
lancée en externe. Par le biais de cette attaque, le pirate est en mesure de
remplacer l'endroit où un fichier est écrit par un emplacement arbitraire dans
le système de fichiers de l'hôte.

|  Élevé  |  
  
##  31 mai 2019

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
Ce bulletin a été mis à jour depuis sa publication initiale.

######  Mise à jour du 2 août 2019

Au moment de la publication du bulletin initial, seules les versions
1.13.6-gke.0 à 1.13.6-gke.5 étaient affectées. En raison d'une régression,
toutes les versions 1.13.6.x sont désormais concernées. Si vous exécutez la
version 1.13.6, procédez le plus rapidement possible à la mise à niveau vers
la version 1.13.7.

Le projet Kubernetes a divulgué la faille [ CVE-2019-11245
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11245) dans les kubelets
v1.13.6 et v1.14.2. Celle-ci peut entraîner l'exécution des conteneurs en tant
qu'UID 0 (qui correspond généralement à l'utilisateur ` root ` ), même si un
autre utilisateur est spécifié dans l'image de conteneur. **Si vos conteneurs
s'exécutent en tant qu'utilisateur non racine, et si vous utilisez une version
de nœud comprise entre 1.13.6-gke.0 et 1.13.6-gke.6, nous vous recommandons de
définir` RunAsUser ` sur tous les pods du cluster dont les conteneurs ne
doivent pas s'exécuter en tant qu'UID 0. **

Si une valeur ` USER ` non racine est spécifiée (par exemple, avec la valeur `
USER ` définie dans un fichier Dockerfile), un comportement inattendu peut se
produire. Lorsqu'un conteneur s'exécute pour la première fois sur un nœud, il
respecte l'UID spécifié. Toutefois, en raison de cette faille, le conteneur
est défini en tant qu'UID 0 lors de la deuxième exécution (et des exécutions
ultérieures) quel que soit l'UID spécifié. Cela est généralement dû à une
élévation de privilège indésirable et peut engendrer un comportement inattendu
de l'application.

#####  Comment savoir si j'exécute une version affectée ?

Exécutez la commande suivante pour répertorier tous les nœuds et la version de
kubelet associée :

    
    
    
    kubectl get nodes -o=jsonpath='{range .items[*]}'\
    '{.status.nodeInfo.machineID}'\
    '{"\t"}{.status.nodeInfo.kubeletVersion}{"\n"}{end}'

Si les versions de kubelet suivantes sont renvoyées dans le résultat, vos
nœuds sont affectés :

  * v1.13.6 
  * v1.14.2 

#####  Comment savoir si ma configuration spécifique est affectée ?

Si vos conteneurs s'exécutent en tant qu'utilisateur non racine, et si vous
utilisez une version de nœud comprise entre 1.13.6-gke.0 et 1.13.6-gke.6,
votre configuration est affectée sauf dans les cas suivants :

  * Les pods qui spécifient une valeur non racine valide pour le PodSecurityContext ` runAsUser ` ne sont pas affectés et continuent à fonctionner comme prévu. 
  * Les règles PodSecurityPolicy qui appliquent un paramètre ` runAsUser ` ne sont pas affectées non plus et continuent à fonctionner comme prévu. 
  * Les pods qui spécifient ` mustRunAsNonRoot:true ` ne sont pas lancés en tant qu'UID 0, mais ne démarrent pas lorsqu'ils sont affectés par ce problème. 

#####  Que dois-je faire ?

Définissez le [ contexte de sécurité RunAsUser
](https://kubernetes.io/docs/tasks/configure-pod-container/security-
context/#set-the-security-context-for-a-pod) sur tous les pods du cluster qui
ne doivent pas s'exécuter en tant qu'UID 0. Vous pouvez appliquer cette
configuration à l'aide d'une règle [ PodSecurityPolicy
](https://kubernetes.io/docs/concepts/policy/pod-security-policy/) .

|  Moyen  |  [ CVE-2019-11245 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2019-11245)  
  
##  14 mai 2019

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
**Mise à jour du 11/06/2019** : le correctif est disponible dans les versions
1.11.10-gke.4, 1.12.8-gke.6 et 1.13.6-gke.5 publiées la semaine du 28/05/2019,
ainsi que dans les versions plus récentes.

Intel a divulgué les failles CVE suivantes :

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

Ces failles CVE sont collectivement désignées par l'appellation
"Microarchitectural Data Sampling (MDS)". En raison de l'interaction entre
l'exécution spéculative et l'état microarchitectural, elles comportent un
risque d'exposition des données. Pour en savoir plus, consultez le [
communiqué d'Intel ](https://www.intel.com/content/www/us/en/security-
center/advisory/intel-sa-00233.html) .

**L'infrastructure hôte qui exécute Kubernetes Engine isole les charges de
travail des clients les unes des autres. Vous n'êtes pas affecté à moins que
vous n'exécutiez du code non approuvé dans vos propres clusters GKE
mutualisés.**

**Cette faille s'avère particulièrement grave pour les clients qui exécutent
du code non approuvé au sein de leurs propres services mutualisés dans
Kubernetes Engine.** Pour limiter les risques engendrés dans Kubernetes
Engine, désactivez l'Hyper-Threading dans vos nœuds. Seuls les nœuds Google
Kubernetes Engine (GKE) utilisant plusieurs processeurs sont affectés par ces
failles. Notez que les VM n1-standard-1 (type de machine GKE par défaut),
g1-small et f1-micro n'exposent qu'un processeur virtuel à l'environnement
invité. Il n'est donc pas nécessaire de désactiver l'Hyper-Threading.

D'autres protections permettant d'activer la fonctionnalité de vidage seront
intégrées à une prochaine [ version du correctif
](https://cloud.google.com/kubernetes-engine/release-notes?hl=fr) . Nous
mettrons automatiquement à niveau les instances maîtres et les nœuds vers la
version corrigée au cours des prochaines semaines, selon le rythme de mise à
niveau habituel. **Le correctif ne permet pas, à lui seul, de limiter
l'exposition à cette faille. Pour connaître les actions recommandées,
consultez les informations ci-dessous.**

Si vous exécutez GKE On-Prem, vous pouvez être affecté selon le matériel que
vous utilisez. Veuillez vous reporter au [ communiqué d'Intel
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) .

####  Que dois-je faire ?

**Vous n'êtes pas affecté à moins que vous n'exécutiez du code non approuvé
dans vos propres clusters GKE mutualisés.**

**Pour les nœuds s'exécutant dans Kubernetes Engine, créez des pools de nœuds
en désactivant l'Hyper-Threading et reprogrammez vos charges de travail sur
les nouveaux nœuds.**

Notez que les VM n1-standard-1, g1-small et f1-micro n'exposent qu'un
processeur virtuel à l'environnement invité. Il n'est donc pas nécessaire de
désactiver l'Hyper-Threading.

**Avertissement :**

  * La désactivation de l'Hyper-Threading peut avoir de graves conséquences sur les performances de vos clusters et de vos applications. Assurez-vous que les répercussions sont acceptables avant de procéder au déploiement sur vos clusters de production. 
  * Vous pouvez désactiver l'Hyper-Threading au niveau du pool de nœuds GKE en déployant un DaemonSet. Toutefois, le déploiement de ce DaemonSet entraîne le redémarrage simultané de tous les nœuds du pool. Par conséquent, il est recommandé de créer un pool de nœuds dans le cluster, de déployer le DaemonSet pour désactiver l'Hyper-Threading dans ce pool, puis de migrer les charges de travail vers le nouveau pool. 

Pour créer un pool de nœuds en désactivant l'Hyper-Threading, procédez comme
suit :

  1. Créez un pool de nœuds portant le libellé ` cloud.google.com/gke-smt-disabled=true ` dans votre cluster : 
    
        
    gcloud container node-pools create smt-disabled --cluster=[CLUSTER_NAME] \
        --node-labels=cloud.google.com/gke-smt-disabled=true

  2. Déployez le DaemonSet dans ce nouveau pool de nœuds. Le DaemonSet ne s'exécute que sur les nœuds portant le libellé ` cloud.google.com/gke-smt-disabled=true ` . Il désactive l'Hyper-Threading, puis redémarre les nœuds. 
    
        
    kubectl create -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform/\
    k8s-node-tools/master/disable-smt/gke/disable-smt.yaml

  3. Assurez-vous que les pods DaemonSet sont en cours d'exécution. 
    
        
    kubectl get pods --selector=name=disable-smt -n kube-system

Vous devriez recevoir une réponse semblable à celle-ci :

    
        
    NAME                READY     STATUS    RESTARTS   AGE
    
    disable-smt-2xnnc   1/1       Running   0          6m

  4. Vérifiez que le message "SMT has been disabled" (SMT a été désactivé) s'affiche dans les journaux des pods. 
    
        
    kubectl logs disable-smt-2xnnc disable-smt -n kube-system

Remarque : Les options de démarrage ne peuvent pas être modifiées si la
fonctionnalité de [ démarrage sécurisé ](https://cloud.google.com/kubernetes-
engine/docs/how-to/shielded-gke-nodes?hl=fr#secure_boot) est activée sur le
nœud. Si le démarrage sécurisé est activé, il doit être [ désactivé
](https://cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-
nodes?hl=fr#disabling) avant que le DaemonSet soit créé.

Le DaemonSet doit rester en cours d'exécution sur le pool de nœuds pour que
les modifications soient automatiquement appliquées aux nœuds qui seront créés
dans le pool. Des créations de nœuds peuvent être déclenchées par les
processus de réparation automatique, de mise à niveau manuelle ou automatique,
et d'autoscaling des nœuds.

Pour réactiver l'Hyper-Threading, vous devez recréer le pool de nœuds sans
déployer le DaemonSet fourni, puis migrer vos charges de travail vers le
nouveau pool.

Nous vous recommandons également de mettre à niveau manuellement les nœuds une
fois que le correctif sera disponible. Avant tout, vous devez [ mettre à
niveau votre instance maître ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=fr#upgrading_the_cluster) vers la
version la plus récente. Les instances maîtres de GKE seront automatiquement
mises à niveau au rythme habituel.

Nous mettrons à jour ce bulletin en y ajoutant les versions contenant un
correctif une fois qu'elles seront disponibles.

####  Quelles failles ce correctif permet-il de résoudre ?

Ce correctif réduit les risques liés aux failles suivantes :

[ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
, [ CVE-2018-12127 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2018-12127) , [ CVE-2018-12130
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130) et [
CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091) :
ces failles exploitent l'exécution spéculative. Ces failles CVE sont
collectivement désignées par l'appellation "Microarchitectural Data Sampling".
En raison de l'interaction entre l'exécution spéculative et l'état
microarchitectural, elles comportent un risque d'exposition des données.  |
Moyen  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  5 avril 2019

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
Les failles de sécurité [ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) et [ CVE-2019-9901
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) ont été
récemment découvertes dans [ Envoy ](https://www.envoyproxy.io/) .

[ Istio ](https://istio.io/) intègre Envoy, et ces failles permettent le
contournement de la règle Istio dans certains cas.

Si vous avez activé Istio sur Google Kubernetes Engine (GKE), vous pouvez être
affecté par ces failles. **Nous vous recommandons de mettre à niveau le plus
rapidement possible les clusters affectés vers la dernière version du
correctif, de même que les side-cars Istio (voir les instructions ci-
dessous).**

####  Que dois-je faire ?

**En raison de la gravité de ces failles, que la mise à niveau automatique des
nœuds soit activée ou non, nous vous recommandons d'exécuter les opérations
suivantes :**

  1. **[ Mettez à niveau manuellement ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=fr) votre cluster dès que le correctif est disponible. **
  2. **Mettez à niveau vos side-cars en vous reportant à la[ documentation correspondante ](https://archive.istio.io/v1.5/docs/setup/upgrade/cni-helm-upgrade/#control-plane-upgrade) . **

Les versions corrigées seront mises à disposition pour tous les projets GKE
aujourd'hui avant 19:00 PDT.

Ce correctif sera disponible dans les versions de GKE qui sont indiquées ci-
dessous. Les nouveaux clusters utiliseront par défaut les versions corrigées à
compter de l'annonce de celles-ci sur la page des bulletins de sécurité de
GKE, laquelle doit avoir lieu le 15 avril 2019. Si vous créez un cluster avant
cette date, vous devrez spécifier la version corrigée pour qu'il l'utilise.
Les nœuds des clients GKE qui ont activé les [ mises à niveau automatiques des
nœuds ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-
upgrades?hl=fr) et ne procèdent pas à des mises à niveau manuelles seront mis
à niveau automatiquement vers les versions corrigées au cours de la semaine
suivante.

Versions corrigées :

  * 1.10.12-gke.14 
  * 1.11.6-gke.16 
  * 1.11.7-gke.18 
  * 1.11.8-gke.6 
  * 1.12.6-gke.10 
  * 1.13.4-gke.10 

####  Quelles failles ce correctif permet-il de résoudre ?

Ce correctif réduit les risques liés aux failles suivantes :

[ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) et [ CVE-2019-9901
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) . Pour en
savoir plus sur ces failles, consultez le [ blog Istio
](https://istio.io/blog/2019/announcing-1.1.2) .

|  Élevé  |

  * [ CVE-2019-9900 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900)
  * [ CVE-2019-9901 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)

  
  
##  1er mars 2019

Description  |  Niveau de gravité  |  Notes  
---|---|---  
  
**Mise à jour du 22/03/2019** : ce correctif est disponible dans Kubernetes
1.11.8-gke.4 et 1.13.4-gke.1, ainsi que dans les versions plus récentes. Il
n'est pas encore inclus dans la version 1.12. Pour vérifier sa disponibilité,
consultez les [ notes de version ](https://cloud.google.com/kubernetes-
engine/docs/release-notes-archive?hl=fr#march_19_2019) .

La communauté Kubernetes a récemment découvert une nouvelle faille par déni de
service, [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) . Celle-ci permet à un utilisateur
autorisé à envoyer des requêtes "patch" de créer une requête "json-patch"
malveillante. Cette requête surutilise le processeur et la mémoire du serveur
d'API Kubernetes, ce qui peut limiter la disponibilité du plan de contrôle du
cluster. Pour en savoir plus, consultez le [ communiqué de Kubernetes
](https://groups.google.com/forum/?hl=fr#!topic/kubernetes-
announce/vmUUNkYfG9g) . **Cette faille affecte l'ensemble des instances
maîtres de Google Kubernetes Engine (GKE). Une prochaine version du correctif
permettra de limiter les risques liés à cette faille. Nous mettrons
automatiquement à niveau les instances maîtres du cluster vers la version
corrigée au cours des prochaines semaines, selon le rythme de mise à niveau
habituel.**

####  Que dois-je faire ?

**Aucune action n'est requise. Les instances maîtres de GKE seront
automatiquement mises à niveau au rythme habituel.** Pour accélérer le
processus, vous pouvez [ lancer manuellement la mise à niveau d'une instance
maître ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=fr#upgrading_the_cluster) .

Nous mettrons à jour ce bulletin en y ajoutant les versions contenant un
correctif. Notez que le correctif ne sera pas proposé dans la version 1.10. Il
ne sera disponible que dans les versions 1.11 et ultérieures.

####  Quelle est la faille prise en charge par ce correctif ?

Ce correctif réduit les risques liés à la faille suivante :

La faille [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) permet à un utilisateur de créer
spécifiquement un correctif de type "json-patch" qui surutilise le processeur
du serveur d'API Kubernetes, ce qui peut limiter la disponibilité du plan de
contrôle du cluster.

|  Moyen  |  [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100)  
  
##  11 février 2019 (runc)

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
L'Open Containers Initiative (OCI) [ a récemment découvert
](https://groups.google.com/a/opencontainers.org/forum/m/?hl=fr#!topic/dev/Tc1ELm-8oDI)
une nouvelle faille de sécurité ( [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) ) dans runc. Celle-ci permet de
"s'échapper d'un conteneur" pour obtenir un accès root (racine) sur le nœud
hôte.

**Cette faille affecte les nœuds Ubuntu dans Google Kubernetes Engine (GKE).
Nous vous recommandons donc d'effectuer dès que possible une[ mise à niveau
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=fr) vers la dernière version du correctif conformément à la
procédure décrite ci-dessous. **

####  Que dois-je faire ?

Avant tout, vous devez mettre à niveau votre nœud maître vers la toute
dernière version. Ce correctif est disponible dans Kubernetes 1.10.12-gke.7,
1.11.6-gke.11, 1.11.7-gke.4 et 1.12.5-gke.5, ainsi que dans les versions plus
récentes. Pour vérifier sa disponibilité, consultez les [ notes de version
](https://cloud.google.com/kubernetes-engine/docs/release-notes-
archive?hl=fr#february-11-2019) .

Sachez que seuls les nœuds Ubuntu dans GKE sont affectés. Les nœuds exécutant
COS ne sont pas concernés.

Sachez que la nouvelle version de runc nécessite davantage de mémoire. Vous
devrez donc peut-être mettre à niveau la mémoire allouée aux conteneurs si
vous avez défini des limites de mémoire peu élevées (< 16 Mo).

####  Quelle est la faille prise en charge par ce correctif ?

Ce correctif réduit les risques liés à la faille suivante :

La faille [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) affecte l'environnement d'exécution de
conteneurs runc. Elle permet à un conteneur malveillant d'écraser le fichier
binaire runc du nœud hôte et d'accéder ainsi en écriture à son répertoire
racine (root) par le biais d'un simple appel système "exec". Les conteneurs
qui ne s'exécutent pas en mode root ne sont pas affectés. La gravité de cette
faille est évaluée comme élevée.

|  Élevé  |  [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736)  
  
##  11 février 2019 (Go)

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
**Mise à jour du 25/02/2019** : comme indiqué précédemment, le correctif n'est
pas disponible dans 1.11.7-gke.4. Si vous exécutez la version 1.11.7, vous
pouvez revenir à la version 1.11.6, procéder à la mise à niveau vers la
version 1.12 ou attendre que le prochain correctif de la version 1.11.7 soit
mis à disposition la semaine du 04/03/2019.

Le langage de programmation Go a récemment découvert une nouvelle faille de
sécurité, [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486) . Il s'agit d'une faille par déni de
service (DoS) dans les mises en œuvre de cryptographie sur les courbes
elliptiques P-521 et P-384. Dans Google Kubernetes Engine (GKE), elle peut
permettre à un utilisateur de créer des requêtes malveillantes qui
surutilisent le processeur du serveur de l'API Kubernetes, ce qui peut réduire
la disponibilité du plan de contrôle du cluster. Pour en savoir plus,
consultez le [ communiqué sur le langage de programmation Go
](https://groups.google.com/forum/?hl=fr#!topic/golang-announce/mVeX35iXuSw) .

**Cette faille affecte l'ensemble des instances maîtres de Google Kubernetes
Engine (GKE). La[ dernière version du correctif
](https://cloud.google.com/kubernetes-engine/docs/release-notes-
archive?hl=fr#february-11-2019) permet de limiter les risques qu'elle
engendre. Nous mettrons automatiquement à niveau les maîtres de cluster vers
la version incluant le correctif au cours des prochaines semaines, selon le
rythme de mise à niveau habituel. **

####  Que dois-je faire ?

**Aucune action n'est requise. Les instances maîtres de GKE seront
automatiquement mises à niveau au rythme habituel.** Pour accélérer le
processus, vous pouvez [ lancer manuellement la mise à niveau d'une instance
maître ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=fr#upgrading_the_cluster) .

Ce correctif est disponible dans GKE 1.10.12-gke.7, 1.11.6-gke.11,
1.11.7-gke.4 et 1.12.5-gke.5, ainsi que dans les versions plus récentes.

####  Quelle est la faille prise en charge par ce correctif ?

Ce correctif réduit les risques liés à la faille suivante :

La faille CVE-2019-6486 affecte les mises en œuvre de cryptographie sur les
courbes elliptiques P-521 et P-384. Elle permet à un utilisateur de créer des
entrées qui surutilisent le processeur.

|  Élevé  |  [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486)  
  
##  3 décembre 2018

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
Kubernetes a récemment découvert une nouvelle faille de sécurité, [
CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105) , qui permet à un utilisateur disposant
d'un niveau de privilèges relativement faible de contourner les autorisations
d'accès aux API du kubelet. Par conséquent, cet utilisateur peut exécuter des
opérations arbitraires pour tous les pods sur n'importe quel nœud du cluster.
Pour en savoir plus, consultez le [ communiqué de Kubernetes
](https://groups.google.com/forum/?hl=fr#!topic/kubernetes-
announce/GVllWCg6L88) . **Cette faille affectait l'ensemble des instances
maîtres de Google Kubernetes Engine (GKE), et nous avons déjà procédé à la
mise à niveau des clusters vers les[ dernières versions du correctif
](https://cloud.google.com/kubernetes-engine/docs/release-notes-
archive?hl=fr#november-12-2018) . Aucune action n'est requise. **

####  Que dois-je faire ?

**Aucune action n'est requise. Les instances maîtres de GKE ont déjà été mises
à niveau.**

Ce correctif est disponible dans GKE 1.9.7-gke.11, 1.10.6-gke.11,
1.10.7-gke.11, 1.10.9-gke.5 et 1.11.2-gke.18 ainsi que dans les versions plus
récentes.

####  Quelle est la faille prise en charge par ce correctif ?

Ce correctif réduit les risques liés à la faille suivante :

La faille CVE-2018-1002105 permet à un utilisateur disposant d'un niveau de
privilèges relativement faible de contourner les autorisations d'accès aux API
du kubelet. Un utilisateur autorisé à effectuer des requêtes de mise à niveau
peut ainsi obtenir une élévation de privilège et envoyer des appels
arbitraires aux API du kubelet. Cette faille de Kubernetes est considérée
comme critique. Au vu de certaines informations concernant la mise en œuvre de
GKE qui empêchaient les élévations de privilège non authentifiées, cette
vulnérabilité est considérée comme une faille de sécurité de gravité élevée.

|  Élevé  |  [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105)  
  
##  13 novembre 2018

Description  
---  
  
**Mise à jour du 16 novembre 2018** : la révocation et la rotation de tous les
jetons potentiellement impactés sont terminées. Aucune action supplémentaire
n'est requise.

Google a récemment détecté un problème dans le plug-in CNI (Container Network
Interface) Calico qui peut, dans certaines configurations, consigner des
informations sensibles. Référence de suivi du problème : Tigera Technical
Advisory [ TTA-2018-001 ](https://www.projectcalico.org/security-bulletins/) .

  * Lors de l'exécution avec la journalisation de niveau "Débogage", le plug-in CNI Calico écrit la configuration cliente de l'API Kubernetes dans les journaux. 
  * L'interface CNI Calico écrit également le jeton d'API Kubernetes dans les journaux de niveau "Information", si le champ "k8s_auth_token" est défini sur la configuration réseau CNI. 
  * De plus, lors de l'exécution avec la journalisation de niveau "Débogage", si le jeton du compte de service est explicitement défini, soit dans le fichier de configuration Calico lu par Calico, soit en tant que variables d'environnement utilisées par Calico, les composants Calico ("calico/node", "felix" et "CNI") écrivent ces informations dans les fichiers journaux. 

Ces jetons disposent des autorisations suivantes :  
      
    
    
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
  
Les clusters Google Kubernetes Engine sur lesquels une stratégie de réseau de
cluster et Stackdriver Logging sont activés ont consigné les jetons de compte
de service Calico dans Stackdriver. Les clusters sur lesquels aucune stratégie
de réseau de cluster n'est activée ne sont pas affectés.

Nous avons déployé un correctif qui migre le plug-in CNI Calico afin que ce
dernier n'effectue la journalisation qu'au niveau d'avertissement et qu'il
utilise un nouveau compte de service. Le code Calico corrigé sera déployé dans
une version ultérieure.

Au cours de la semaine prochaine, nous allons effectuer une révocation
progressive de tous les jetons potentiellement impactés. Ce bulletin sera mis
à jour dès que la révocation sera terminée. **Aucune action supplémentaire de
votre part n'est nécessaire.** (Cette rotation est terminée depuis le 16
novembre 2018.)

Si vous souhaitez alterner ces jetons immédiatement, vous pouvez exécuter la
commande ci-dessous. Le nouveau secret du compte de service devrait être
recréé automatiquement en quelques secondes :  
  
kubectl get sa --namespace kube-system calico -o template --template '{{(index
.secrets 0).name}}' | xargs kubectl delete secret --namespace kube-system  
---  
  
####  Détection

Les journaux GKE accèdent tous au serveur d'API. Pour déterminer si un jeton
Calico a été utilisé depuis une plage d'adresses IP autre que celle prévue par
Google Cloud, vous pouvez exécuter la requête Stackdriver suivante. Veuillez
noter que cette commande ne renverra des enregistrements que pour les appels
effectués en dehors du réseau GCP. Il est conseillé de la personnaliser selon
les besoins de votre environnement spécifique.  
  
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
  
##  14 août 2018

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
[ Intel a divulgué ](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) les failles CVE suivantes :

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) (pour [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (pour les systèmes d'exploitation et [ SMT ](https://en.wikipedia.org/wiki/Hyper-threading) ) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (pour la virtualisation) 

Ces failles CVE sont collectivement désignées sous le nom de "L1 Terminal
Fault (L1TF)".

Ces failles L1TF exploitent l'exécution spéculative en attaquant la
configuration des structures de données au niveau du processeur. "L1" fait
référence au cache des données L1D (Level-1 Data), une petite ressource sur le
cœur qui permet d'accélérer l'accès à la mémoire.

Lisez [ cet article du blog Google Cloud
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=fr) pour en savoir plus sur ces failles et les
protections de Compute Engine.

####  Impact sur Google Kubernetes Engine

L'infrastructure qui exécute Kubernetes Engine, et qui isole les clusters et
les nœuds client les uns des autres, est protégée contre les attaques connues.

Les pools de nœuds Kubernetes Engine qui utilisent l'image Container-Optimized
OS (COS) de Google et pour lesquels la [ mise à niveau automatique
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=fr) est activée seront automatiquement mis à niveau vers les
versions corrigées de notre image COS. Ces versions seront disponibles dès le
20 août 2018.

Les pools de nœuds Kubernetes Engine pour lesquels la [ mise à niveau
automatique ](https://cloud.google.com/kubernetes-engine/docs/concepts/node-
auto-upgrades?hl=fr) n'est pas activée devront être [ manuellement mis à
niveau ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=fr) dès que les versions corrigées de notre image COS
seront disponibles.

|  Élevé  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  6 août 2018 (dernière mise à jour le 5 septembre 2018)

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Mise à jour du 5 septembre 2018

La faille [ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) a été divulguée récemment. Tout comme [
CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
, il s'agit d'une faille réseau au niveau du noyau. Celle-ci rend les attaques
par déni de service (DoS) plus efficaces dans les systèmes vulnérables. La
principale différence réside dans le fait que la faille CVE-2018-5391 est
exploitable sur les connexions IP. Nous avons mis à jour ce bulletin afin de
traiter de ces deux failles.

####  Description

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ("SegmentSmack") fait référence à une
faille réseau au niveau du noyau. Celle-ci rend les attaques par déni de
service (DoS) plus efficaces dans les systèmes vulnérables, via les connexions
TCP.

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ("FragmentSmack") fait référence à une
faille réseau au niveau du noyau. Celle-ci rend les attaques par déni de
service (DoS) plus efficaces dans les systèmes vulnérables, via les connexions
IP.

####  Impact sur Google Kubernetes Engine

Depuis le 11 août 2018, toutes les instances maîtres de Kubernetes Engine sont
protégées contre ces deux failles. Par ailleurs, tous les clusters Kubernetes
Engine qui ont été configurés pour être mis à niveau automatiquement sont
également protégés contre ces deux failles. Les pools de nœuds Kubernetes
Engine qui ne sont pas configurés pour [ être mis à niveau automatiquement
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=fr) , et qui ont été mis à niveau manuellement pour la dernière
fois avant le 11 août 2018, sont affectés par ces deux failles.

####  Versions corrigées

En raison de la gravité de cette faille, nous vous recommandons de [ mettre à
niveau manuellement ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=fr#upgrading-nodes) vos nœuds dès que le correctif
sera disponible.

|  Élevé  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  30 mai 2018

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
Une faille a récemment été détectée dans Git. Celle-ci peut entraîner
l'élévation des privilèges dans Kubernetes si des utilisateurs non privilégiés
sont autorisés à créer des pods avec des volumes gitRepo. La faille CVE est
identifiée par le tag [ CVE-2018-11235 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-11235) .

####  Suis-je concerné ?

Cette faille vous concerne si toutes les affirmations suivantes s'appliquent à
votre cas :

  * Les utilisateurs non approuvés peuvent créer des pods (ou déclencher la création de pods). 
  * Les pods créés par des utilisateurs non approuvés disposent de restrictions pour empêcher l'accès à la racine de l'hôte (par exemple, via [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=fr) ). 
  * Les pods créés par des utilisateurs non approuvés sont autorisés à utiliser le type de volume "gitRepo". 

Tous les nœuds Kubernetes Engine sont vulnérables.

####  Que dois-je faire ?

Interdisez l'utilisation du type de volume "gitRepo". Pour effectuer cette
opération avec PodSecurityPolicy, omettez ` gitRepo ` dans la liste blanche `
volumes ` de votre règle PodSecurityPolicy.

Il est possible d'obtenir un comportement équivalent du volume "gitRepo" en
clonant un dépôt Git dans un volume "EmptyDir" à partir d'un conteneur
"initContainer" :

    
    
    
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

####  Quel correctif résout cette faille ?

Un correctif sera intégré à une version ultérieure de Kubernetes Engine.
Revenez consulter cette page pour en savoir plus.

|  Moyen  |

  * [ CVE-2018-11235 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11235)

  
  
##  21 mai 2018

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
Plusieurs failles ont été détectées récemment dans le noyau Linux. Elles
peuvent entraîner l'élévation des privilèges ou le déni de service (via le
plantage du noyau) à partir d'un processus non privilégié. Ces failles CVE
sont identifiées par les tags [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) , [ CVE-2018-8897
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897) et [
CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)
. Tous les nœuds Kubernetes Engine sont affectés par ces failles. Nous vous
recommandons donc d'effectuer une [ mise à niveau
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=fr) vers la dernière version du correctif conformément à
la procédure ci-dessous.

####  Que dois-je faire ?

Avant tout, vous devez mettre à niveau votre instance maître vers la toute
dernière version. Ce correctif est disponible dans Kubernetes Engine
1.8.12-gke.1, Kubernetes Engine 1.9.7-gke.1 et Kubernetes Engine 1.10.2-gke.1.
Ces versions incluent des correctifs pour les images Container-Optimized OS et
Ubuntu.

Si vous créez un nouveau cluster avant la mise à niveau, vous devez spécifier
la version corrigée avec laquelle il doit être utilisé. Les clients qui ont
activé la [ mise à niveau automatique des nœuds
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=fr) et qui ne procèdent pas à une mise à niveau manuelle verront
leurs nœuds mis à niveau vers les versions corrigées dans les prochaines
semaines.

####  Quelles failles ce correctif permet-il de résoudre ?

Ce correctif réduit les risques liés aux failles suivantes :

[ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) : cette faille affecte le noyau Linux.
Elle permet à un utilisateur ou à un processus non privilégié d'entraîner le
plantage du noyau du système, ce qui conduit à une attaque DoS ou à une
élévation des privilèges. La gravité de cette faille est évaluée comme élevée,
et son score CVSS est de 7,8.

[ CVE-2018-8897 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-8897) : cette faille affecte le noyau Linux.
Elle permet à un utilisateur ou à un processus non privilégié d'entraîner le
plantage du noyau du système, ce qui conduit à une attaque DoS. La gravité de
cette faille est évaluée comme moyenne, et son score CVSS est de 6,5.

[ CVE-2018-1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) : cette faille affecte l'hyperviseur KVM
du noyau Linux. Elle permet à un processus non privilégié d'entraîner le
plantage du noyau invité ou, potentiellement, d'obtenir des privilèges. Cette
faille est résolue dans l'infrastructure sur laquelle s'exécute Kubernetes
Engine. Ce dernier n'est donc pas affecté. La gravité de cette faille est
évaluée comme élevée, et son score CVSS est de 8,0.

|  Élevé  |

  * [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199)
  * [ CVE-2018-8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
  * [ CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)

  
  
##  12 mars 2018

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
Le projet Kubernetes a [ récemment divulgué
](https://groups.google.com/forum/?hl=fr#!topic/kubernetes-security-
announce/P7lBjbjDKd8) de nouvelles failles de sécurité, [ CVE-2017-1002101
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101) et [
CVE-2017-1002102 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2017-1002102) , qui permettent à un conteneur d'accéder
aux fichiers situés en dehors de celui-ci. Tous les nœuds Kubernetes Engine
sont affectés par ces failles. Nous vous recommandons donc d'effectuer dès que
possible une mise à niveau vers la dernière version munie du correctif. La
procédure de mise à niveau est expliquée ci-dessous.

####  Que dois-je faire ?

En raison de la gravité de ces failles, que la mise à niveau automatique des
nœuds soit activée ou non, nous vous recommandons de [ mettre à niveau
manuellement ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-container-cluster?hl=fr) vos nœuds dès que le correctif est
disponible. Celui-ci sera mis à la disposition de tous les clients au plus
tard le 16 mars. Toutefois, en fonction du [ calendrier des lancements
](https://cloud.google.com/kubernetes-engine/docs/release-notes-
archive?hl=fr#march-12-2018) , vous pourriez avoir accès à ce correctif plus
tôt, selon la zone dans laquelle se trouve votre cluster.

Avant tout, vous devez mettre à niveau votre instance maître vers la toute
dernière version. Ce correctif sera disponible dans Kubernetes 1.9.4-gke.1,
Kubernetes 1.8.9-gke.1 et Kubernetes 1.7.14-gke.1. Par défaut, à compter du 30
mars, les nouveaux clusters utiliseront la version corrigée. Toutefois, si
vous créez un nouveau cluster avant la mise à niveau, vous devrez spécifier la
version corrigée avec laquelle il doit être utilisé.

Les clients Kubernetes Engine qui ont activé la [ mise à niveau automatique
des nœuds ](https://cloud.google.com/kubernetes-engine/docs/concepts/node-
auto-upgrades?hl=fr) et qui ne procèdent pas à une mise à niveau manuelle
verront leurs nœuds mis à niveau vers les versions corrigées d'ici le 23
avril. Toutefois, en raison de la nature de ces failles, nous vous
recommandons de [ mettre à niveau manuellement
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=fr) vos nœuds dès que le correctif sera disponible.

####  Quelles failles ce correctif permet-il de résoudre ?

Ce correctif réduit les risques liés aux deux failles suivantes :

La faille CVE-2017-1002101 permet aux conteneurs utilisant des montages de
volume de [ sous-chemin
](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath)
d'accéder aux fichiers en dehors du volume. Par conséquent, si la stratégie
"PodSecurityPolicy" empêche les conteneurs d'accéder au chemin d'accès à
l'hôte, un pirate autorisé à mettre à jour ou à créer des pods peut monter un
chemin d'accès à l'hôte à l'aide d'un autre type de volume.

La faille CVE-2017-1002102 permet aux conteneurs utilisant certains types de
volumes (y compris les secrets, les mappages de configuration, les volumes
prévus ou les volumes d'API Downward) de supprimer des fichiers en dehors du
volume. Par conséquent, si la sécurité d'un conteneur utilisant l'un de ces
types de volumes est compromise, ou si un utilisateur non approuvé est
autorisé à créer des pods, un pirate peut se servir de ce conteneur pour
supprimer des fichiers arbitraires sur l'hôte.

Pour en savoir plus sur ce correctif, consultez [ cet article sur le blog
Kubernetes ](https://kubernetes.io/blog/2018/04/04/fixing-subpath-volume-
vulnerability/) .

|  Élevé  |

  * [ CVE-2017-1002101 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101)
  * [ CVE-2017-1002102 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102)

