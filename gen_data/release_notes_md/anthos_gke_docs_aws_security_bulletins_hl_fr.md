A new version of Anthos GKE on AWS was released on August 5. See the [ release
notes ](https://cloud.google.com/anthos/gke/docs/aws/release-notes?hl=fr) for
information on breaking changes.

#  Bulletins de sécurité

Découvrez les bulletins de sécurité pour Anthos GKE sur AWS (GKE sur AWS).

##  GCP-2020-011

**Date de publication :** 2020-07-24  
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

Pour exploiter cette faille sur des clusters GKE sur AWS, un pirate doit
désactiver les [ vérifications source/destination
](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html) sur
les instances EC2 du cluster. Pour ce faire, le pirate informatique doit
disposer des autorisations AWS IAM pour ` ModifyInstanceAttribute ` ou `
ModifyNetworkInterfaceAttribute ` sur les instances EC2. Par conséquent, la
gravité de cette faille a été évaluée comme moyenne pour GKE sur AWS.

####  Que dois-je faire ?

Pour résoudre cette faille, mettez à niveau votre cluster vers une version
incluant le correctif. Les versions suivantes de GKE sur AWS et les versions
ultérieures devraient inclure le correctif de cette faille :

  * GKE sur AWS 1.4.2 

####  Quelle faille ce correctif permet-il de résoudre ?

Ce correctif résout la faille suivante : [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) .

|

Faible

|

[ CVE-2020-8558 ](https://github.com/kubernetes/kubernetes/issues/92315)  
  
##  GCP-2020-009

**Date de publication :** 2020-07-15  Description  |  Niveau de gravité  |
Notes  
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

La version en disponibilité générale de GKE sur AWS (1.4.1, disponible fin
juillet 2020) ou version ultérieure inclut le correctif de cette faille. Si
vous utilisez une version précédente, [ téléchargez une nouvelle version de
l'outil de ligne de commande anthos-gke
](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites?hl=fr) ,
puis recréez vos clusters de gestion et d'utilisateur.

####  Quelle faille ce correctif permet-il de résoudre ?

Ce correctif réduit les risques liés à la faille CVE-2020-8559. La gravité de
cette faille est évaluée comme moyenne pour GKE, car elle nécessite que le
pirate informatique ait préalablement reçu des informations personnelles sur
le cluster, les nœuds et les charges de travail pour réaliser efficacement
cette attaque en plus de disposer d'un nœud compromis. Cette faille en elle-
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
  
La faille SSRF (Server Side Request Forgery, falsification de requête côté
serveur) [ CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555) a été récemment détectée dans Kubernetes.
Elle permet à certains utilisateurs autorisés de divulguer jusqu'à 500 octets
d'informations sensibles depuis le réseau hôte du plan de contrôle. Le plan de
contrôle de Google Kubernetes Engine (GKE) utilise des contrôleurs Kubernetes.
Il est donc concerné par cette faille. Nous vous recommandons de mettre à jour
le plan de contrôle en installant la dernière version du correctif,
conformément à la procédure expliquée ci-dessous. Il n'est pas nécessaire de
mettre à niveau le nœud.  

####  Que dois-je faire ?

Anthos GKE sur AWS (GKE sous AWS) v0.2.0 ou version ultérieure inclut déjà le
correctif de cette faille. Si vous utilisez une version précédente, [
téléchargez une nouvelle version de l'outil de ligne de commande anthos-gke
](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites?hl=fr) ,
puis recréez vos clusters de gestion et d'utilisateur.

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

[ Téléchargez l'outil de ligne de commande anthos-gke
](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites?hl=fr)
avec la version suivante ou ultérieure, puis recréez vos clusters de gestion
et d'utilisateur :

  * aws-0.2.1-gke.7 

Très peu de conteneurs nécessitent généralement ` CAP_NET_RAW ` . Il faut donc
la bloquer par défaut, ainsi que d'autres fonctionnalités puissantes, via [
Anthos Policy Controller ](https://cloud.google.com/anthos-config-
management/docs/concepts/policy-controller?hl=fr) ou en mettant à jour les
spécifications du pod :

Supprimez la fonctionnalité ` CAP_NET_RAW ` des conteneurs :

  * En utilisant Anthos Policy Controller/Gatekeeper, avec ce [ modèle de contrainte ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) et en l'appliquant. Exemple : 
    
        
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

