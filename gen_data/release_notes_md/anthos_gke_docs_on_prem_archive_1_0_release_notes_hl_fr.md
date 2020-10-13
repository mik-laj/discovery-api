#  Notes de version

Cette page documente les mises à jour en production d'Anthos GKE On-Prem.
Consultez-la régulièrement pour obtenir des informations sur les
fonctionnalités nouvelles ou mises à jour, les corrections de bugs, les
problèmes connus et les fonctionnalités obsolètes.

Voir également :

  * [ Téléchargements ](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=fr)
  * [ Gestion des versions et mises à jour ](https://cloud.google.com/anthos/gke/docs/on-prem/versioning-and-upgrades?hl=fr)
  * [ Mettre à niveau les clusters ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=fr)
  * [ Mettre à niveau le poste de travail administrateur ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=fr)

Vous pouvez consulter les dernières mises à jour de produits pour l'ensemble
de Google Cloud sur la page [ Notes de version de Google Cloud
](https://cloud.google.com/release-notes?hl=fr) .

Pour recevoir les dernières mises à jour concernant ce produit, ajoutez l'URL
de cette page à votre [ lecteur de flux
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou ajoutez l'URL
du flux directement : ` https://cloud.google.com/feeds/gkeonprem-release-
notes.xml `

##  22 août 2019

La version 1.0.2-gke.3 de GKE On-Prem est désormais disponible. Ce correctif
inclut les modifications suivantes :

###  Nouvelles fonctionnalités

**FEATURE:**

Seesaw est désormais compatible avec l'équilibrage de charge manuel.

**FEATURE:**

Vous pouvez désormais spécifier un autre réseau vSphere pour les clusters
d'administrateur et d'utilisateur.

**FEATURE:**

Vous pouvez désormais supprimer des clusters d'utilisateur à l'aide de `
gkectl ` . Consultez la section [ Supprimer un cluster d'utilisateur
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/how-
to/administration/deleting-a-user-cluster?hl=fr) .

###  Modifications

**CHANGED:** ` gkectl diagnose snapshot ` récupère désormais les journaux des
plans de contrôle du cluster d'utilisateur.

**CHANGED:**

La spécification OIDC de GKE On-Prem a été mise à jour avec plusieurs champs
nouveaux : ` kubectlredirecturl ` , ` scopes ` , ` extraparams ` et `
usehttpproxy ` .

**CHANGED:**

Calico a été mis à jour vers la version 3.7.4.

**CHANGED:**

Les métriques système de Cloud Monitoring sont passées de `
external.googleapis.com/prometheus/ ` à ` kubernetes.io/anthos/ ` . Si vous
effectuez le suivi des métriques ou des alertes, mettez à jour vos tableaux de
bord avec le préfixe suivant.

###  Correction

**FIXED:**

[ Correction d'une faille de CVE-2019-11247
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/security-
bulletins?hl=fr#august-22-2019) .

**FIXED:**

[ Correction d'une faille dans le proxy RBAC
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/security-
bulletins?hl=fr#august-23-2019) .

##  30 juillet 2019

La version 1.0.1-gke.5 de GKE On-Prem est désormais disponible. Ce correctif
inclut les modifications suivantes :

###  Nouvelles fonctionnalités

**FEATURE:**

[ Aide-mémoire GKE On-Prem ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/reference/cheatsheet?hl=fr) publié.

###  Modifications

**CHANGED:**

` gkectl check-config ` vérifie également la disponibilité des adresses IP de
nœuds si vous utilisez des adresses IP statiques.

**CHANGED:**

` gkectl prepare ` vérifie maintenant si une VM existe et est marquée comme
modèle dans vSphere avant d'essayer d'importer l'image OVA de la VM.

**CHANGED:**

Ajoute la compatibilité pour la spécification d'un cluster vCenter et d'un
pool de ressources dans ce cluster.

**CHANGED:**

Met à jour le contrôleur F5 BIG-IP vers la version 1.9.0.

**CHANGED:**

Met à jour le contrôleur Istio Ingress vers la version 1.2.2.

###  Corrections

**FIXED:**

Corrige les problèmes de persistance des données de registre avec le registre
Docker du poste de travail administrateur.

**FIXED:**

Corrige la validation qui vérifie si le nom d'un cluster d'utilisateur est
déjà utilisé.

##  17 juin 2019

GKE On-Prem est désormais accessible à tous. La version 1.0.10 inclut les
modifications suivantes :

###  Mettre à niveau de la version bêta 1.4 à la version 1.0.10

Avant de mettre à niveau vos clusters bêta vers la première version de
disponibilité générale, suivez les étapes décrites dans la section [ Passer de
la version bêta de GKE On-Prem à la disponibilité générale
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/how-
to/upgrading/from-beta?hl=fr) et examinez les points suivants:

  * Si vous exécutez une version bêta antérieure à la version 1.4, assurez-vous de passer d'abord à la version 1.4. 

  * Si vos clusters bêta exécutent leurs propres équilibreurs de charge L4 (et non F5 BIG-IP par défaut), vous devez les supprimer et les recréer pour exécuter la dernière version de GKE On-Prem. 

  * Si vos clusters ont été mis à jour vers les versions bêta 1.4 et bêta 1.3, exécutez la commande suivante _pour chaque cluster d'utilisateur_ avant la mise à jour : 
    
        kubectl delete crd networkpolicies.crd.projectcalico.org

  * La validation du certificat vCenter est désormais obligatoire. (La valeur ` vsphereinsecure ` n'est plus acceptée.) Si vous mettez à jour vos clusters bêta 1.4 vers la version 1.0.10, vous devez fournir un certificat public CA racine de confiance vCenter dans le fichier de configuration de la mise à jour. 

  * Vous devez mettre à jour _tous_ vos clusters en cours d'exécution. Pour que cette mise à jour réussisse, vos clusters ne peuvent pas s'exécuter dans une version mixte. 

  * Vous devez d'abord mettre à niveau vos clusters d'administrateur vers la dernière version, puis mettre à niveau vos clusters d'utilisateurs. 

###  Nouvelles fonctionnalités

**FEATURE:**

Vous pouvez maintenant activer le [ mode d'équilibrage de charge manuel
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/installation/manual-lb?hl=fr) pour configurer un équilibreur de charge L4.
Vous pouvez toujours choisir d'utiliser l'équilibreur de charge par défaut, F5
BIG-IP.

**FEATURE:**

Le processus d'installation basé sur la configuration de GKE On-Prem a été mis
à jour. Vous pouvez désormais procéder à une déclaration de manière
déclarative à l'aide d'un [ fichier de configuration
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/concepts/overview?hl=fr#config) unique.

**FEATURE:**

Ajout de ` gkectl create-config ` , qui génère un fichier de configuration
pour l'installation de GKE On-Prem, la mise à jour des clusters existants et
la création de clusters d'utilisateur supplémentaires dans une installation
existante. Ceci remplace l'assistant d'installation et ` create-config.yaml `
des versions précédentes. Consultez la documentation mise à jour pour [
installer GKE On-Prem ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/installation/install?hl=fr#generate_config) .

**FEATURE:**

Ajoute ` gkectl check-config ` , qui valide le fichier de configuration GKE
On-Prem. Consultez la documentation mise à jour pour [ installer GKE On-Prem
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/installation/install?hl=fr#validate_config) .

**FEATURE:**

Ajoute une option ` --validate-attestations ` facultative à ` gkectl prepare `
. Cette option vérifie que les images de conteneur incluses dans votre poste
de travail administrateur ont été créées et signées par Google et sont prêtes
à être déployées. Consultez la documentation mise à jour pour [ installer GKE
On-Prem ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/installation/install?hl=fr#prepare) .

###  Modifications

**CHANGED:**

Met à niveau Kubernetes vers la version 1.12.7-gke.19. Vous pouvez désormais [
mettre à niveau vos clusters ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/administration/upgrading-clusters?hl=fr) vers
cette version. Vous ne pouvez plus créer de clusters exécutant Kubernetes
version 1.11.2-gke.19.

Nous vous recommandons de mettre à jour votre cluster d'administrateur avant
de mettre à jour vos clusters d'utilisateurs.

**CHANGED:**

Met à jour le contrôleur d'entrée Istio vers la version 1.1.7.

**CHANGED:**

La validation du certificat vCenter est désormais obligatoire. La valeur `
vsphereinsecure ` n'est plus acceptée.) Vous fournissez le certificat dans le
champ ` cacertpath ` du fichier de configuration GME On-Prem.

Lorsqu'un client appelle le serveur vCenter, ce dernier doit prouver son
identité au client en présentant un certificat. Ce certificat doit être signé
par une autorité de certification. Il ne doit pas être autosigné.

Si vous mettez à jour vos clusters bêta 1.4 vers la version 1.0.10, vous devez
fournir un certificat public CA racine de confiance vCenter dans le fichier de
configuration de la mise à jour.

###  Problèmes connus

**ISSUE:**

[ La mise à jour des clusters ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/upgrading-clusters?hl=fr) peut entraîner des
interruptions ou des temps d'arrêt pour les charges de travail qui utilisent [
PodDisruptionBudgets
](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-
disruption-budgets-work) (PDB).

**ISSUE:**

Vous ne pourrez peut-être pas mettre à niveau les clusters bêta qui utilisent
le [ mode d'équilibrage manuel de charge
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/installation/manual-lb?hl=fr) vers GKE version 10.10. Pour mettre à niveau
et continuer à utiliser votre propre équilibreur de charge avec ces clusters,
vous devez recréer les clusters.

##  24 mai 2019

La version bêta 1.4.7 de G GKE On-Prem est désormais disponible. Cette version
inclut les modifications suivantes :

###  Nouvelles fonctionnalités

**FEATURE:**

Dans la commande [ ` gkectl diagnose snapshot `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
to/administration/diagnose?hl=fr#capture_admin) , le paramètre ` --admin-ssh-
key-path ` est désormais facultatif.

###  Modifications

**CHANGED:**

Le 8 mai 2019, nous avons apporté une modification à Connect, le service qui
vous permet d'interagir avec vos clusters GKE On-Prem à l'aide de Cloud
Console. Pour utiliser le nouvel agent Connect, vous devez enregistrer à
nouveau vos clusters avec Cloud Console, ou vous devez passer à Anthos GKE On-
Prem version bêta-1.4.

Vos clusters GKE On-Prem et les charges de travail qui y sont exécutées
continueront à fonctionner sans interruption. Toutefois, vos clusters ne
seront pas visibles dans Cloud Console tant que vous ne les aurez pas
réenregistrés ou que vous ne passerez à la version bêta 1.4.

Avant de vous réinscrire ou d'effectuer la mise à niveau, assurez-vous que
votre compte de service dispose du rôle ` gkehub.connect ` . En outre, si
votre compte de service dispose de l'ancien rôle clusterregistry.connec, il
est recommandé de supprimer ce rôle.

Attribuez le rôle gkehub.connect à votre compte de service :

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

Si votre compte de service a l'ancien rôle ` clusterregistry.connect ` ,
supprimez l'ancien rôle :

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/clusterregistry.connect"

Réenregistrez votre cluster ou passez à Anthos GKE On-Prem version bêta-1.4.

Pour [ réenregistrer votre cluster ](https://cloud.google.com/kubernetes-
engine/connect/updating-agent?hl=fr) :

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \
          --context=[USER_CLUSTER_CONTEXT] \
          --service-account-key-file=[LOCAL_KEY_PATH] \
          --kubeconfig-file=[KUBECONFIG_PATH] \
          --project=[PROJECT_ID]

Pour [ passer à Anthos GKE On-Prem version bêta-1.4
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
to/administration/upgrading-a-cluster?hl=fr) :

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  Problèmes connus

**ISSUE:**

Un problème empêche l'agent Connect d'être mis à jour vers la nouvelle version
lors d'une mise à niveau. Pour contourner ce problème, exécutez la commande
suivante après la mise à jour d'un cluster :

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  13 mai 2019

###  Problèmes connus

**ISSUE:**

Les clusters mis à niveau de la version bêta-1.2 vers la version bêta-1.3
peuvent être affectés par un problème connu qui endommage le fichier de
configuration du cluster et empêche les futures mises à niveau de cluster. Ce
problème affecte toutes les futures mises à niveau de clusters.

Vous pouvez résoudre ce problème en supprimant et en recréant des clusters mis
à jour de la version bêta-1.2 vers la version bêta-1.3.

Pour résoudre le problème sans supprimer ni recréer le cluster, vous devez
réencoder et appliquer les secrets de chaque cluster. Procédez comme suit :

  1. Récupérez le contenu des secrets ` create-config ` stockés dans le cluster d'administrateur. Cette opération doit être effectuée pour le secret ` create-config ` dans l'espace de noms kube-system et pour les secrets ` create-config ` dans l'espace de noms de chaque cluster d'utilisateur : 
    
        kubectl get secret create-config -n kube-system -o jsonpath={.data.cfg} | base64 -d > kube-system_create_secret.yaml
    
        kubectl get secret create-config -n [USER_CLUSTER_NAME] -o jsonpath={.data.cfg} | base64 -d > [USER_CLUSTER_NAME]_create_secret.yaml

  2. Pour chaque cluster d'utilisateur, ouvrez le fichier ` [USER_CLUSTER_NAME]  _create_secret.yaml ` dans un éditeur. Si les valeurs de ` registerserviceaccountkey ` et ` connectserviceaccountkey ` ne sont pas ` REDACTED ` , aucune autre action n'est requise : les secrets n'ont pas besoin d'être réencodés et écrits dans le cluster. 
  3. Ouvrez le fichier ` create_config.yaml ` d'origine dans un autre éditeur. 
  4. Dans ` [USER_CLUSTER_NAME]  _create_secret.yaml ` , remplacez les valeurs ` registerserviceaccountkey ` et ` connectserviceaccountkey ` par les valeurs du fichier ` create_config.yaml ` d'origine. Enregistrez le fichier modifié. 
  5. Répétez les étapes 3 à 5 pour chaque fichier ` [USER_CLUSTER_NAME]  _create_secret.yaml ` et pour le fichier ` kube-system_create_secret.yaml ` . 
  6. Encodez en base64 chaque fichier ` [USER_CLUSTER_NAME]  _create_secret.yaml ` et le fichier ` kube-system_create_secret.yaml ` : 
    
        cat [USER_CLUSTER_NAME]_create_secret.yaml | base64 > [USER_CLUSTER_NAME]_create_secret_create_secret.b64
    
        cat kube-system-cluster_create_secret.yaml | base64 >kube-system-cluster_create_secret.b64

  7. Remplacez le champ ` data[cfg] ` de chaque secret du cluster par le contenu du fichier correspondant : 
    
        kubectl edit secret create-config -n [USER_CLUSTER_NAME]
    
      # kubectl edit opens the file in the shell's default text editor
      # Open `first-user-cluster_create_secret.b64` in another editor, and replace
      # the `cfg` value with the copied value
      # Make sure the copied string has no newlines in it!

  8. Répétez l'étape 8 pour chaque secret ` [USER_CLUSTER_NAME]  _create_secret.yaml ` et pour le secret ` kube-system_create_secret.yaml ` . 
  9. Pour vous assurer que la mise à jour a réussi, répétez l'étape 1. 

##  7 mai 2019

La version bêta 1.4.1 de GKE On-Prem est désormais disponible. Cette version
inclut les modifications suivantes :

###  Nouvelles fonctionnalités

**FEATURE:**

Dans la commande [ ` gkectl diagnose snapshot `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
to/administration/diagnose?hl=fr#capture_admin) , le paramètre ` --admin-ssh-
key-path ` est désormais facultatif.

###  Modifications

**CHANGED:**

Le 8 mai 2019, nous avons apporté une modification à Connect, le service qui
vous permet d'interagir avec vos clusters GKE On-Prem à l'aide de Cloud
Console. Pour utiliser le nouvel agent Connect, vous devez enregistrer à
nouveau vos clusters avec Cloud Console, ou vous devez passer à Anthos GKE On-
Prem version bêta-1.4.

Vos clusters GKE On-Prem et les charges de travail qui y sont exécutées
continueront à fonctionner sans interruption. Toutefois, vos clusters ne
seront pas visibles dans Cloud Console tant que vous ne les aurez pas
réenregistrés ou que vous ne passerez à la version bêta 1.4.

Avant de vous réinscrire ou d'effectuer la mise à niveau, assurez-vous que
votre compte de service dispose du rôle gkehub.connect. De plus, si votre
compte de service dispose de l'ancien rôle clusterregistry.connect, il est
recommandé de le supprimer.

Attribuez le rôle gkehub.connect à votre compte de service :

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

Si votre compte de service dispose de l'ancien rôle clusterregistry.connect,
supprimez-le :

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/clusterregistry.connect"

Réenregistrez votre cluster ou passez à Anthos GKE On-Prem version bêta-1.4.

Pour [ réenregistrer votre cluster ](https://cloud.google.com/kubernetes-
engine/connect/updating-agent?hl=fr) :

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \
          --context=[USER_CLUSTER_CONTEXT] \
          --service-account-key-file=[LOCAL_KEY_PATH] \
          --kubeconfig-file=[KUBECONFIG_PATH] \
          --project=[PROJECT_ID]

Pour [ passer à Anthos GKE On-Prem version bêta-1.4
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
to/administration/upgrading-a-cluster?hl=fr) :

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  Problèmes connus

**ISSUE:**

Un problème empêche l'agent Connect d'être mis à jour vers la nouvelle version
lors d'une mise à niveau. Pour contourner ce problème, exécutez la commande
suivante après la mise à jour d'un cluster :

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  25 avril 2019

La version bêta 1.3.1 de GKE On-Prem est désormais disponible. Cette version
inclut les modifications suivantes :

###  Nouvelles fonctionnalités

**FEATURE:**

La commande ` gkectl diagnose snapshot ` dispose désormais d'une option [ `
--dry-run ` ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/beta-1.3/how-
to/administration/diagnose?hl=fr#performing_a_dry_run_for_a_snapshot) .

**FEATURE:**

La commande ` gkectl diagnose snapshot ` est désormais compatible avec quatre
[ scénarios ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/beta-1.3/how-
to/administration/diagnose?hl=fr#snapshot_scenarios) .

**FEATURE:**

La commande ` gkectl diagnose snapshot ` accepte désormais les expressions
régulières pour spécifier des espaces de noms.

###  Modifications

**CHANGED:**

Istio 1.1 est désormais le [ contrôleur d'entrée
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.3/how-
to/administration/upgrading-a-cluster?hl=fr#upgrading_the_ingress_controller)
par défaut. Le contrôleur d'entrée s'exécute dans l'espace de noms ` gke-
system ` pour les clusters d'administrateur et d'utilisateur. Cela facilite la
gestion TLS pour Ingress. Pour activer l'entrée ou la réactiver après une mise
à niveau, suivez les instructions de la section [ Activer l'entrée
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.3/how-
to/installation/install?hl=fr#enabling_ingress) .

**CHANGED:**

L'outil ` gkectl ` n'utilise plus Minikube et KVM pour l'amorçage. Cela
signifie que vous n'avez pas besoin d'activer la virtualisation imbriquée sur
la VM de votre poste de travail administrateur.

###  Problèmes connus

**ISSUE:**

Le contrôleur d'entrée de GKE On-Prem utilise Istio 1.1 avec la détection
automatique des secrets. Cependant, l'agent de nœud pour la découverte des
secrets peut ne pas obtenir les mises à jour des secrets après leur
suppression. Évitez donc de supprimer des secrets. Si vous devez supprimer un
secret et que TLS d'entrée échoue par la suite, redémarrez manuellement le pod
d'entrée dans l'espace de noms gke-system.

##  11 avril 2019

La version 1.3.1 de GKE On-Prem est désormais disponible. Cette version inclut
les modifications suivantes :

###  Nouvelles fonctionnalités

**FEATURE:**

Les clusters GKE On-Prem se reconnectent automatiquement à Google à l'aide de
[ Connect ](https://cloud.google.com/kubernetes-engine/connect?hl=fr) .

**FEATURE:**

Vous pouvez désormais exécuter jusqu'à trois plans de contrôle par cluster
d'utilisateur.

###  Modifications

**CHANGED:**

` gkectl ` valide maintenant les identifiants vSphere et F5 BIG-IP en créant
des clusters.

###  Problèmes connus

**ISSUE:**

En raison d'une régression, les commandes ` gkectl diagnose snapshot `
utilisent la mauvaise clé SSH, ce qui empêche la commande de collecter des
informations à partir des clusters d'utilisateurs. Pour contourner ce
problème, vous devrez peut-être passer à SSH dans des nœuds de cluster
d'utilisateur individuels et collecter manuellement les données.

##  2 avril 2019

La version 1.1.1 de GKE On-Prem est désormais disponible. Cette version inclut
les modifications suivantes :

###  Nouvelles fonctionnalités

**FEATURE:**

Désormais, vous installez GKE On-Prem avec [ Open Virtual Appliance (OVA)
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.1/how-
to/installation/getting-started?hl=fr#download_ova) , une image de machine
virtuelle préconfigurée comprenant plusieurs outils d'interface de ligne de
commande. Cette modification facilite les installations et supprime une couche
de virtualisation. Vous n'avez plus besoin d'exécuter ` gkectl ` dans un
conteneur Docker.

Si vous avez installé des versions de GKE On-Prem antérieures à la version
bêta 1.1.1, vous devez créer un poste de travail administrateur en suivant les
instructions fournies. Après avoir installé le nouveau poste de travail
administrateur, copiez depuis votre ancien poste de travail les clés SSH, les
fichiers de configuration, les fichiers kubeconfig et tous les autres fichiers
dont vous avez besoin.

**FEATURE:**

Documentation ajoutée pour [ sauvegarder et restaurer des clusters
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.1/how-
to/administration/backing-up?hl=fr) .

**FEATURE:**

Vous pouvez désormais configurer l'authentification pour les clusters à l'aide
d'OIDC et d'ADFS. Pour en savoir plus, consultez les sections [ Procéder à
l'authentification à l'aide d'OIDC et d'ADFS
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.1/how-
to/security/oidc-adfs?hl=fr) et [ Authentification
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/concepts/authentication?hl=fr) .

###  Modifications

**CHANGED:**

Désormais, vous devez utiliser la clé privée d'un cluster d'administration
pour exécuter ` gkectl diagnose snapshot ` .

**CHANGED:**

Ajout d'une option de configuration lors de l'installation pour le déploiement
de clusters d'utilisateurs multimaître.

**CHANGED:**

La [ documentation sur Connect ](https://cloud.google.com/kubernetes-
engine/connect?hl=fr) a été migrée.

###  Corrections

**FIXED:**

La mise en réseau de cluster pouvait être interrompue lorsqu'un nœud était
supprimé de manière inattendue. Ce problème a été résolu.

###  Problèmes connus

**ISSUE:**

La gestion de la configuration de GKE Om-Prem a été mise à niveau de la
version 0.11 à la version 0.13. Plusieurs composants du système ont été
renommés. Vous devez prendre des mesures pour nettoyer les ressources des
versions précédentes et installer une nouvelle instance.

Si vous disposez d'une instance active de gestion de la configuration :

  1. Désinstallez l'instance : 
    
        kubectl -n=nomos-system delete nomos --all

  2. Assurez-vous que l'espace de noms de l'instance ne comporte aucune ressource : 
    
        kubectl -n nomos-system get all

  3. Supprimez l'espace de noms : 
    
        kubectl delete ns nomos-system

  4. Supprimez le CRD : 
    
        kubectl delete crd nomos.addons.sigs.k8s.io

  5. Supprimez toutes les ressources kube-system de l'opérateur : 
    
        kubectl -n kube-system delete all -l k8s-app=nomos-operator

Si vous n'avez pas d'instance active de la gestion de la configuration :

  1. Supprimez l'espace de noms de gestion de configuration : 
    
        kubectl delete ns nomos-system

  2. Supprimez le CRD: 
    
        kubectl delete crd nomos.addons.sigs.k8s.io

  3. Supprimez toutes les ressources kube-system de l'opérateur : 
    
        kubectl -n kube-system delete all -l k8s-app=nomos-operator

##  13 mars 2018

La version bêta 1.0.3 de G GKE On-Prem est désormais disponible. Cette version
inclut les modifications suivantes :

###  Corrections

**FIXED:**

Correction d'un problème qui entraînait l'enregistrement des certificats
Docker au mauvais endroit.

##  4 mars 2019

La version bêta 1.0.2 de GKE On-Prem est désormais disponible. Cette version
inclut les modifications suivantes :

###  Nouvelles fonctionnalités

**FEATURE:**

Vous pouvez désormais exécuter ` gkectl version ` pour vérifier la version de
` gkectl ` que vous utilisez.

**FEATURE:**

Vous pouvez désormais [ mettre à jour les clusters d'utilisateurs
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.0/how-
to/administration/upgrading-a-cluster?hl=fr) vers les futures versions bêta.

**FEATURE:**

La version 0.11.6 d' [ Anthos Config Management
](https://cloud.google.com/anthos-config-management/docs?hl=fr) est désormais
disponible.

**FEATURE:**

Stackdriver Logging est désormais activé sur chaque nœud. Par défaut, l'agent
Logging réplique les journaux dans votre projet GCP pour les services du plan
de contrôle, l'API de cluster, le contrôleur vSphere, Calico, le contrôleur
BIG-IP, le proxy Envoy, Connect, Anthos Config Management, les services
Prometheus et Grafana, le plan de contrôle Istio et Docker.Les journaux de
conteneur d'application sont exclus par défaut, mais peuvent éventuellement
être activés.

**FEATURE:**

Le side-car Stackdriver Prometheus capture les métriques des mêmes composants
que l'agent Logging.

**FEATURE:**

Les [ règles de réseau Kubernetes
](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
sont désormais compatibles.

###  Modifications

**CHANGED:**

Vous pouvez désormais mettre à jour les blocs d'adresses IP dans la
spécification du cluster pour étendre la plage d'adresses IP d'un cluster
donné.

**CHANGED:**

Si les clusters que vous avez installés en version alpha ont été déconnectés
de Google après la phase bêta, vous devrez peut-être les reconnecter.
Consultez la section [ Enregistrer manuellement un cluster d'utilisateur
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/installation/registering-a-user-cluster?hl=fr) .

**CHANGED:**

La page [ Premiers pas ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/installation/getting-started?hl=fr) a été mise
à jour avec les étapes pour activer votre compte de service et exécuter `
gkectl prepare ` .

**CHANGED:**

` gkectl diagnose snapshot ` collecte désormais uniquement les données de
configuration et exclut les journaux.Cet outil permet de capturer les détails
de votre environnement avant d'ouvrir une demande d'assistance.

**CHANGED:**

Compatibilité avec la configuration facultative du nom de pool SNAT pour F5
BIG-IP au moment de la création du cluster. Cela permet de configurer la
valeur "--vs-snat-pool-name" sur le [ contrôleur d'adresse F5 BIG-IP
](https://clouddocs.f5.com/products/connectors/k8s-bigip-ctlr/v1.8/) .

**CHANGED:**

Vous devez à présent fournir un VIP pour les modules complémentaires qui
s'exécutent dans le cluster d'administrateur.

###  Corrections

**FIXED:**

Les opérations de redimensionnement du cluster ont été améliorées pour
empêcher la suppression accidentelle des nœuds.

##  7 février 2019

La version 1.3 de GKE On-Prem est désormais disponible. Cette version inclut
les modifications suivantes :

###  Nouvelles fonctionnalités

**FEATURE:**

Lors de l'installation, vous pouvez désormais fournir des fichiers YAML avec
blocs ` nodeip ` pour configurer IPAM statique.

###  Modifications

**CHANGED:**

Vous devez maintenant provisionner un disque de 100 Go dans vSphere Datastore.
GKE On-Prem utilise le disque pour stocker certaines de ses données vitales,
telles que etcd. Reportez-vous à l'article [ Configuration système requise
](https://cloud.google.com/anthos/gke/docs/on-prem/requirements?hl=fr) .

**CHANGED:**

Vous ne pouvez désormais fournir que des noms d'hôte en minuscules aux blocs `
nodeip ` .

**CHANGED:**

GKE On-Prem applique désormais des noms uniques pour les clusters
d'utilisateurs.

**CHANGED:**

Les points de terminaison de métriques et les API utilisant les points de
terminaison Istio sont désormais sécurisés à l'aide de mTLS et d'un contrôle
d'accès basé sur les rôles.

**CHANGED:**

La communication externe par Grafana est désactivée.

**CHANGED:**

Améliorations apportées à la vérification de l'état de Prometheus et
Alertmanager.

**CHANGED:**

Prometheus utilise désormais un port sécurisé pour récupérer les métriques.

**CHANGED:**

Plusieurs mises à jour des tableaux de bord Grafana.

###  Problèmes connus

**ISSUE:**

Si votre compte d'utilisateur vCenter utilise un format tel que ` DOMAIN\USER
` , vous devrez peut-être faire échapper la barre oblique inverse ( `
DOMAIN\\USER ` ). Assurez-vous de le faire lorsque vous êtes invité à saisir
le compte d'utilisateur lors de l'installation.

##  23 janvier 2019

La version alpha 1.2.1 de GKE On-Prem est désormais disponible. Cette version
inclut les modifications suivantes :

###  Nouvelles fonctionnalités

**FEATURE:**

Vous pouvez désormais utiliser ` gkectl ` pour [ supprimer des clusters
d'administrateur ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/administration/deleting-an-admin-cluster?hl=fr)
.

.

###  Modifications

**CHANGED:**

Les commandes ` gkectl diagnose snapshot ` vous permettent désormais de
spécifier des nœuds lors de la capture d'instantanés des résultats et des
fichiers des commandes à distance.

##  14 janvier 2019

La version alpha 1.1.1 de GKE On-Prem est désormais disponible. Cette version
inclut les modifications suivantes :

###  Nouvelles fonctionnalités

**FEATURE:**

Vous pouvez maintenant utiliser la commande ` gkectl prepare ` pour extraire
et transférer les images de conteneur de GKE On-Prem, ce qui rend le script `
populate_registry.sh ` obsolète.

**FEATURE:**

` gkectl prepare ` vous invite désormais à saisir des informations sur votre
cluster vSphere et votre pool de ressources.

**FEATURE:**

Vous pouvez maintenant utiliser la commande ` gkectl create ` pour créer et
ajouter des clusters d'utilisateurs aux plans de contrôle d'administrateur
existants en transmettant un fichier kubeconfig existant lorsque vous y êtes
invité pendant la création du cluster.

**FEATURE:**

Vous pouvez désormais transmettre un secret TLS Ingress pour les clusters
d'administrateur et d'utilisateur au moment de la création du cluster. La
nouvelle invite suivante s'affiche :

` Do you want to use TLS for Admin Control Plane/User Cluster ingress? `

La spécification du secret et des certificats TLS permet à ` gkectl ` de
configurer le TLS d'entrée. Le protocole HTTP n'est pas automatiquement
désactivé avec l'installation TLS.

###  Modifications

**CHANGED:**

GKE On-Prem exécute désormais la version **1.11.2-gke.19** de Kubernetes.

**CHANGED:**

L'empreinte par défaut de GKE On-Prem a changé:

  * La mémoire minimale requise pour les nœuds de cluster d'utilisateur est désormais de 8 192 M. 

**CHANGED:**

GKE On-Prem exécute désormais la version minikube **0.28.0** .

**CHANGED:**

GKE Policy Management a été mis à jour vers la version **0.11.1** .

**CHANGED:**

` gkectl ` ne vous invite plus à fournir une configuration de proxy par
défaut.

**CHANGED:**

Il existe trois nouvelles ressources ConfigMap dans l'espace de noms du
cluster d'utilisateur : ` cluster-api-etcd-metrics-config ` , ` kube-etcd-
metrics-config ` et ` kube-apiserver-config ` . GKE On-Prem utilise ces
fichiers pour amorcer rapidement le conteneur proxy de métriques.

**CHANGED:**

Les événements kube-apiserver sont désormais actifs dans leur propre etcd.
Vous pouvez voir kube-etcd-events dans l'espace de noms de votre cluster
d'utilisateurs.

**CHANGED:**

Les contrôleurs d'API de cluster utilisent désormais le choix de responsable.

**CHANGED:**

Les identifiants vSphere sont désormais extraits des fichiers d'identifiants.

**CHANGED:**

Les commandes ` gkectl diagnose ` fonctionnent désormais avec les clusters
d'administrateur et d'utilisateur.

**CHANGED:**

` gkectl diagnose snapshot ` peut désormais prendre des instantanés de
fichiers distants sur le nœud, des résultats de commandes à distance sur les
nœuds et des requêtes Prometheus.

**CHANGED:**

` gkectl diagnose snapshot ` peut désormais prendre des instantanés dans
plusieurs threads parallèles.

**CHANGED:**

` gkectl diagnose snapshot ` vous permet désormais de spécifier les mots à
exclure des résultats de l'instantané.

###  Corrections

**FIXED:**

Résolution des problèmes de mise en cache de minikube provoquant des appels
réseau inattendus.

**FIXED:**

Résolution du problème lié à l'extraction des identifiants identifiants F5
BIG-IP. Les identifiants sont désormais lus à partir d'un fichier
d'identifiants au lieu d'utiliser des variables d'environnement.

###  Problèmes connus

**ISSUE:**

L'avertissement [ ` govmomi ` ](https://github.com/vmware/govmomi) suivant
peut s'afficher lorsque vous exécutez ` gkectl prepare ` :

` Warning: Line 102: Unable to parse 'enableMPTSupport' for attribute 'key' on
element 'Config' `

**ISSUE:**

Le redimensionnement de clusters d'utilisateur peut entraîner la suppression
ou la recréation involontaire du nœud.

**ISSUE:**

L'installation des ressources PersistentVolume peut échouer et générer
l'erreur ` devicePath is empty ` . Pour contourner ce problème, supprimez et
recréez l'objet PersistentVolumeClaim associé.

**ISSUE:**

Le redimensionnement des blocs d'adresses IPAM si vous utilisez l'allocation
d'adresses IP statiques pour les nœuds n'est pas disponible en version alpha.
Pour contourner ce problème, envisagez d'allouer plus d'adresses IP que
nécessaire.

**ISSUE:**

Sur les disques lents, la création de VM peut expirer et entraîner l'échec des
déploiements. Dans ce cas, supprimez toutes les ressources et réessayez.

##  19 décembre 2018

GKE On-Prem alpha 1.0.4 est désormais disponible. Cette version inclut les
modifications suivantes :

###  Corrections

**FIXED:**

La faille provoquée par [ CVE-2018-1002105
](https://github.com/kubernetes/kubernetes/issues/71411) a été corrigée.

##  30 novembre 2018

GKE On-Prem alpha 1.0 est désormais disponible. Les modifications suivantes
sont incluses dans cette version :

###  Modifications

**CHANGED:**

GKE On-Prem alpha 1.0 exécute Kubernetes 1.11.

**CHANGED:**

L'empreinte par défaut de GKE On-Prem a changé:

  * Le plan de contrôle d'administration exécute trois nœuds, qui utilisent 4 processeurs et 16 Go de mémoire. 
  * Le plan de contrôle d'utilisateur exécute un nœud qui utilise 4 processeurs et 16 Go de mémoire. 
  * Les clusters d'utilisateurs exécutent au moins trois nœuds, qui utilisent 4 processeurs et 16 Go de mémoire. 

**CHANGED:**

Compatibilité avec la configuration de Prometheus à haute disponibilité.

**CHANGED:**

Compatibilité avec la configuration personnalisée d'Alert Manager.

**CHANGED:**

Prometheus a été mis à niveau de **2.3.2** à **2.4.3** .

**CHANGED:**

Grafana a été mis à niveau de **5.0.4** à **5.3.4** .

**CHANGED:**

Les métriques kube-state sont passées de **1.3.1** à **1.4.0** .

**CHANGED:**

Alert Manager a été mis à niveau de **1.14.0** à **1.15.2** .

**CHANGED:**

node_exporter est passé de **1.15.2** à **1.16.0** .

###  Corrections

**FIXED:**

La faille provoquée par [ CVE-2018-1002103
](https://github.com/kubernetes/minikube/issues/3208) a été corrigée.

###  Problèmes connus

**ISSUE:**

L'installation des ressources PersistentVolume peut échouer et générer
l'erreur ` devicePath is empty ` . Pour contourner ce problème, supprimez et
recréez l'objet PersistentVolumeClaim associé.

**ISSUE:**

Le redimensionnement des blocs d'adresses IPAM si vous utilisez l'allocation
d'adresses IP statiques pour les nœuds n'est pas disponible en version alpha.
Pour contourner ce problème, envisagez d'allouer plus d'adresses IP que
nécessaire.

**ISSUE:**

GKE On-Prem alpha 1.0 ne passe pas encore tous les tests de conformité.

**ISSUE:**

Vous ne pouvez créer qu'un seul cluster d'utilisateur par cluster
d'administrateur. Pour créer des clusters d'utilisateurs supplémentaires,
créez un autre cluster d'administrateur.

##  31 octobre 2018

GKE On-Prem EAP 2.1 est désormais disponible. Les modifications suivantes sont
incluses dans cette version :

###  Modifications

**CHANGED:**

Lorsque vous créez des clusters d'administrateur et d'utilisateur
simultanément, vous pouvez à présent réutiliser les identifiants BIG-IP F5 du
cluster d'administrateur pour créer le cluster d'utilisateur. De plus, la CLI
exige désormais que les identifiants BIG-IP soient fournis. Cette condition ne
peut pas être ignorée à l'aide de ` --dry-run ` .

**CHANGED:**

Contrôleur BIG-IP F5 mis à jour pour utiliser la dernière version d'OSS,
1.7.0.

**CHANGED:**

Pour améliorer la stabilité des machines vSphere lentes, le délai d'expiration
de création de la machine en cluster est désormais de 15 minutes (cinq minutes
auparavant).

##  17 octobre 2018

GKE On-Prem EAP 2.0 est désormais disponible. Les modifications suivantes sont
incluses dans cette version :

###  Modifications

**CHANGED:**

Compatibilité avec GKE Connect.

**CHANGED:**

Assistance pour la surveillance

**CHANGED:**

Assistance pour l'installation à l'aide de registres privés

**CHANGED:**

Prise en charge de la mise au premier plan de l'équilibreur de charge L7 en
tant que VIP L4 sur F5 BIG-IP.

**CHANGED:**

Prise en charge de l'allocation d'adresses IP statiques pour les nœuds lors du
démarrage du cluster.

###  Problèmes connus

**ISSUE:**

Vous ne pouvez créer qu'un seul cluster d'utilisateur par cluster
d'administrateur. Pour créer des clusters d'utilisateurs supplémentaires,
créez un autre cluster d'administrateur.

**ISSUE:**

Les mises à jour de cluster ne sont pas compatibles avec EAP 2.0.

**ISSUE:**

Sur les disques lents, la création de VM peut expirer et entraîner l'échec des
déploiements. Dans ce cas, supprimez toutes les ressources et réessayez.

**ISSUE:**

Dans le cadre du processus d'amorçage du cluster, une instance minikube
éphémère est exécutée. La version de Minikube utilisée a la faille de sécurité
[ CVE-2018-1002103 ](https://github.com/kubernetes/minikube/issues/3208) .

