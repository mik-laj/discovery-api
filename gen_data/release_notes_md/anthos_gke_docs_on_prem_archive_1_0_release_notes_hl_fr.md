#  Notes de version

Cette page documente les mises à jour en production d'Anthos GKE On-Prem.
Consultez-la régulièrement pour obtenir des informations sur les
fonctionnalités nouvelles ou mises à jour, les corrections de bugs, les
problèmes connus et les fonctionnalités obsolètes.

Voir alo:

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
inclut les modifications suivantes:

###  Nouvelles fonctionnalités

**FEATURE:**

Seesaw est désormais compatible avec l'équilibrage de charge manuel.

**FEATURE:**

Vous pouvez désormais spécifier un autre réseau vSphere pour les clusters
d'administrateur et d'utilisateur.

**FEATURE:**

Vous pouvez désormais supprimer des clusters utilisateur en utilisant ` gkectl
` . Voir [ Suppression d'un cluster utilisateur
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/how-
to/administration/deleting-a-user-cluster?hl=fr) .

###  Modifications

**CHANGED:** ` gkectl diagnose snapshot ` récupère désormais les journaux des
plans de contrôle du cluster utilisateur.

**CHANGED:**

La spécification OIDC de GKE sur site a été mise à jour avec plusieurs
nouveaux champs: ` kubectlredirecturl ` , ` scopes ` , ` extraparams ` et `
usehttpproxy ` .

**CHANGED:**

Calico a été mis à jour vers la version 3.7.4.

**CHANGED:**

Le préfixe des métriques système de Cloud Monitoring est passé de `
external.googleapis.com/prometheus/ ` à ` kubernetes.io/anthos/ ` . Si vous
effectuez le suivi des statistiques ou des alertes, mettez à jour vos tableaux
de bord avec le préfixe suivant.

###  Correction

**FIXED:**

[ Correction d'une faille CVE-2019-11247
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/security-
bulletins?hl=fr#august-22-2019) .

**FIXED:**

[ Correction d'une faille dans le proxy RBAC
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/security-
bulletins?hl=fr#august-23-2019) .

##  30 juillet 2019

La version 1.0.1-gke.5 de GKE On-Prem est désormais disponible. Ce correctif
inclut les modifications suivantes:

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

Ajoute la compatibilité avec la spécification d'un cluster vCenter et d'un
pool de ressources dans ce cluster.

**CHANGED:**

Met à jour le contrôleur F5 BIG-IP vers la version 1.9.0.

**CHANGED:**

Met à jour le contrôleur Istio Ingress vers la version 1.2.2.

###  Corrections

**FIXED:**

Résout les problèmes de persistance des données du registre avec le registre
Docker du poste de travail administrateur.

**FIXED:**

Corrige la validation qui vérifie si le nom d'un cluster utilisateur est déjà
utilisé.

##  17 juin 2019

GKE On-Prem est désormais accessible à tous. La version 1.0.10 inclut les
modifications suivantes:

###  Mettre à niveau de la version bêta 1.4 à la version 1.0.10

Avant de mettre à niveau vos clusters bêta vers la première version de
disponibilité générale, suivez les étapes décrites dans la section [ Passer de
la version bêta de GKE On-Prem à la disponibilité générale
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/how-
to/upgrading/from-beta?hl=fr) et examinez les points suivants:

  * Si vous exécutez une version bêta antérieure à la version 1.4, assurez-vous de passer d'abord à la version 1.4. 

  * Si vos clusters bêta exécutent leurs propres équilibreurs de charge L4 (et non F5 BIG-IP par défaut), vous devez les supprimer et les recréer pour exécuter la dernière version de GKE On-Prem. 

  * Si vos clusters sont passés de bêta-1.3 à la version bêta-1.4, exécutez la commande suivante _pour chaque cluster utilisateur_ avant de procéder à la mise à niveau: 
    
        kubectl delete crd networkpolicies.crd.projectcalico.org

  * La validation du certificat vCenter est désormais obligatoire. (La valeur ` vsphereinsecure ` n'est plus acceptée.) Si vous mettez à niveau vos clusters bêta 1.4 vers la version 1.0.10, vous devez fournir un certificat public d'autorité de certification racine vCenter de confiance dans le fichier de configuration de mise à niveau. 

  * Vous devez mettre à niveau _tous_ vos clusters en cours d'exécution. Pour que cette mise à jour réussisse, vos clusters ne peuvent pas s'exécuter dans un état de version mixte. 

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
à jour. Vous effectuez maintenant l'installation déclarative à l'aide d'un [
fichier de configuration ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/concepts/overview?hl=fr#config) unique.

**FEATURE:**

Ajoute ` gkectl create-config ` , qui génère un fichier de configuration pour
installer GKE On-Prem, mettre à niveau les clusters existants et créer des
clusters d'utilisateurs supplémentaires dans une installation existante. Cette
opération remplace l'assistant d'installation et ` create-config.yaml ` des
versions précédentes. Consultez la documentation mise à jour pour [ installer
GKE on-prem ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/installation/install?hl=fr#generate_config) .

**FEATURE:**

Ajoute ` gkectl check-config ` , qui valide le fichier de configuration GKE
On-Prem. Consultez la documentation mise à jour pour [ installer GKE On-Prem
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/installation/install?hl=fr#validate_config) .

**FEATURE:**

Ajoute un indicateur ` --validate-attestations ` facultatif à ` gkectl prepare
` . Cet indicateur vérifie que les images de conteneur incluses dans votre
poste de travail administrateur ont été créées et signées par Google et sont
prêtes pour le déploiement. Consultez la documentation mise à jour pour [
installer GKE On-Prem ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/installation/install?hl=fr#prepare) .

###  Modifications

**CHANGED:**

Met à niveau la version Kubernetes vers la version 1.12.7-gke.19. Vous pouvez
désormais [ mettre à jour vos clusters
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/administration/upgrading-clusters?hl=fr) vers cette version. Vous ne pouvez
plus créer de clusters qui exécutent Kubernetes version 1.11.2-gke.19.

Nous vous recommandons de mettre à jour votre cluster d'administration avant
de mettre à jour vos clusters d'utilisateurs.

**CHANGED:**

Met à jour le contrôleur d'entrée Istio vers la version 1.1.7.

**CHANGED:**

La validation du certificat vCenter est désormais obligatoire. La valeur `
vsphereinsecure ` n'est plus acceptée.) Vous fournissez le certificat dans le
champ ` cacertpath ` du fichier de configuration GME On-Prem.

Lorsqu'un client appelle le serveur vCenter, ce dernier doit prouver son
identité au client en présentant un certificat. Ce certificat doit être signé
par une autorité de certification. Le certificat ne doit pas être autosigné.

Si vous mettez à niveau vos clusters bêta 1.4 vers la version 1.0.10, vous
devez fournir un certificat public d'autorité de certification racine vCenter
de confiance dans le fichier de configuration de mise à niveau.

###  Problèmes connus

**ISSUE:**

[ La mise à niveau des clusters ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/upgrading-clusters?hl=fr) peut entraîner des
interruptions ou des interruptions pour les charges de travail qui utilisent [
PodDisruptionBudgets
](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-
disruption-budgets-work) (PDBs).

**ISSUE:**

Vous ne pourrez peut-être pas mettre à niveau les clusters bêta utilisant le [
Mode manuel d'équilibrage de la charge
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/latest/how-
to/installation/manual-lb?hl=fr) à la version 1.0.10 de GKE On-Prem. Pour
mettre à niveau et continuer à utiliser votre propre équilibreur de charge
avec ces clusters, vous devez recréer les clusters.

##  24 mai 2019

La version bêta 1.4.7 de GKE On-Prem est désormais disponible. Cette version
inclut les modifications suivantes:

###  Nouvelles fonctionnalités

**FEATURE:**

Dans la commande [ ` gkectl diagnose snapshot `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
to/administration/diagnose?hl=fr#capture_admin) , le paramètre ` --admin-ssh-
key-path ` est désormais facultatif.

###  Modifications

**CHANGED:**

Le 8 mai 2019, nous avons modifié le service Connect for Anthos, qui vous
permet d'interagir avec vos clusters GKE On-Prem à l'aide de Cloud Console.
Pour utiliser le nouvel agent Connect for Anthos, vous devez réenregistrer vos
clusters auprès de Cloud Console ou passer à Anthos GKE On-Prem bêta-1.4.

Vos clusters GKE On-Prem et les charges de travail qui y sont exécutées
continueront à fonctionner sans interruption. Toutefois, vos clusters ne
seront pas visibles dans Cloud Console tant que vous ne les aurez pas
réenregistrés ou que vous ne passerez à la version bêta 1.4.

Avant de vous réinscrire ou d'effectuer la mise à niveau, assurez-vous que
votre compte de service dispose du rôle ` gkehub.connect ` . De même, si votre
compte de service est associé à l'ancien rôle clusterregistry.connect, nous
vous recommandons de supprimer ce rôle.

Attribuez le rôle gkehub.connect à votre compte de service:

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

Si votre compte de service possède l'ancien rôle ` clusterregistry.connect ` ,
supprimez l'ancien rôle:

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/clusterregistry.connect"

Réenregistrez votre cluster ou passez à Anthos GKE On-Prem version bêta-1.4.

Pour [ réinscrire votre cluster ](https://cloud.google.com/kubernetes-
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

Un problème empêche l'agent Connect for Anthos d'être mis à jour vers la
nouvelle version lors d'une mise à niveau. Pour contourner ce problème,
exécutez la commande suivante après la mise à niveau d'un cluster:

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  13 mai 2019

###  Problèmes connus

**ISSUE:**

Les clusters mis à niveau de la version bêta-1.2 vers la version bêta-1.3
peuvent être affectés par un problème connu qui endommage le fichier de
configuration du cluster et empêche les futures mises à niveau de cluster. Ce
problème affecte toutes les futures mises à niveau de cluster.

Vous pouvez résoudre ce problème en supprimant et en recréant les clusters mis
à niveau de la version bêta 1.2 vers la version 1.3.

Pour résoudre le problème sans supprimer ni recréer le cluster, vous devez
réencoder et appliquer les secrets de chaque cluster. Procédez comme suit :

  1. Obtenez le contenu des secrets ` create-config ` stockés dans le cluster d'administration. Cela doit être fait pour le paramètre ` create-config ` Secret dans l'espace de noms kube-system et pour les secrets ` create-config ` dans l'espace de noms de chaque cluster utilisateur: 
    
        kubectl get secret create-config -n kube-system -o jsonpath={.data.cfg} | base64 -d > kube-system_create_secret.yaml
    
        kubectl get secret create-config -n [USER_CLUSTER_NAME] -o jsonpath={.data.cfg} | base64 -d > [USER_CLUSTER_NAME]_create_secret.yaml

  2. Pour chaque cluster d'utilisateurs, ouvrez le fichier ` [USER_CLUSTER_NAME]  _create_secret.yaml ` dans un éditeur. Si les valeurs de ` registerserviceaccountkey ` et ` connectserviceaccountkey ` ne sont pas ` REDACTED ` , aucune autre action n'est requise: les secrets n'ont pas besoin d'être réencodés et écrits dans le cluster. 
  3. Ouvrez le fichier ` create_config.yaml ` d'origine dans un autre éditeur. 
  4. Dans ` [USER_CLUSTER_NAME]  _create_secret.yaml ` , remplacez les valeurs ` registerserviceaccountkey ` et ` connectserviceaccountkey ` par les valeurs du fichier d'origine ` create_config.yaml ` . Enregistrez le fichier modifié. 
  5. Répétez les étapes 3 à 5 pour chaque fichier ` [USER_CLUSTER_NAME]  _create_secret.yaml ` et pour le fichier ` kube-system_create_secret.yaml ` . 
  6. Encodez en base64 chaque fichier ` [USER_CLUSTER_NAME]  _create_secret.yaml ` et le fichier ` kube-system_create_secret.yaml ` : 
    
        cat [USER_CLUSTER_NAME]_create_secret.yaml | base64 > [USER_CLUSTER_NAME]_create_secret_create_secret.b64
    
        cat kube-system-cluster_create_secret.yaml | base64 >kube-system-cluster_create_secret.b64

  7. Remplacez le champ ` data[cfg] ` de chaque code secret du cluster par le contenu du fichier correspondant: 
    
        kubectl edit secret create-config -n [USER_CLUSTER_NAME]
    
      # kubectl edit opens the file in the shell's default text editor
      # Open `first-user-cluster_create_secret.b64` in another editor, and replace
      # the `cfg` value with the copied value
      # Make sure the copied string has no newlines in it!

  8. Répétez l'étape 8 pour chaque secret ` [USER_CLUSTER_NAME]  _create_secret.yaml ` et pour le secret ` kube-system_create_secret.yaml ` . 
  9. Pour vous assurer que la mise à jour a réussi, répétez l'étape 1. 

##  7 mai 2019

La version 1.4.1 de la version bêta GKE On-Prem est désormais disponible.
Cette version inclut les modifications suivantes:

###  Nouvelles fonctionnalités

**FEATURE:**

Dans la commande [ ` gkectl diagnose snapshot `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.4/how-
to/administration/diagnose?hl=fr#capture_admin) , le paramètre ` --admin-ssh-
key-path ` est désormais facultatif.

###  Modifications

**CHANGED:**

Le 8 mai 2019, nous avons modifié le service Connect for Anthos, qui vous
permet d'interagir avec vos clusters GKE On-Prem à l'aide de Cloud Console.
Pour utiliser le nouvel agent Connect for Anthos, vous devez réenregistrer vos
clusters auprès de Cloud Console ou passer à Anthos GKE On-Prem bêta-1.4.

Vos clusters GKE On-Prem et les charges de travail qui y sont exécutées
continueront à fonctionner sans interruption. Toutefois, vos clusters ne
seront pas visibles dans Cloud Console tant que vous ne les aurez pas
réenregistrés ou que vous ne passerez à la version bêta 1.4.

Avant de vous réinscrire ou de procéder à la mise à jour, assurez-vous que
votre compte de service est associé au rôle gkehub.connect. En outre, si votre
compte de service possède l'ancien rôle clusterregister.connect, il est
recommandé de supprimer ce rôle.

Attribuez le rôle gkehub.connect à votre compte de service:

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

Si votre compte de service a l'ancien rôle clusterregistry.connect, supprimez
l'ancien rôle:

    
    
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

Un problème empêche l'agent Connect for Anthos d'être mis à jour vers la
nouvelle version lors d'une mise à niveau. Pour contourner ce problème,
exécutez la commande suivante après la mise à niveau d'un cluster:

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  25 avril 2019

La version 1.3.1 de la version bêta de GKE On-Prem est désormais disponible.
Cette version inclut les modifications suivantes:

###  Nouvelles fonctionnalités

**FEATURE:**

La commande ` gkectl diagnose snapshot ` comporte désormais un indicateur [ `
--dry-run ` ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/beta-1.3/how-
to/administration/diagnose?hl=fr#performing_a_dry_run_for_a_snapshot) .

**FEATURE:**

La commande ` gkectl diagnose snapshot ` prend désormais en charge quatre [
scénarios ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/beta-1.3/how-
to/administration/diagnose?hl=fr#snapshot_scenarios) .

**FEATURE:**

La commande ` gkectl diagnose snapshot ` accepte désormais les expressions
régulières permettant de spécifier des espaces de noms.

###  Modifications

**CHANGED:**

Istio 1.1 est désormais le [ contrôleur Ingress
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.3/how-
to/administration/upgrading-a-cluster?hl=fr#upgrading_the_ingress_controller)
par défaut. Le contrôleur Ingress s'exécute dans l'espace de noms ` gke-system
` pour les clusters d'administrateur et d'utilisateur. Cela facilite la
gestion TLS pour Ingress. Pour activer Ingress ou la réactiver après une mise
à niveau, suivez les instructions de la section [ Activer Ingress
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.3/how-
to/installation/install?hl=fr#enabling_ingress) .

**CHANGED:**

L'outil ` gkectl ` n'utilise plus Minikube et KVM pour l'amorçage. Cela
signifie que vous n'avez pas besoin d'activer la virtualisation imbriquée sur
la VM de votre poste de travail administrateur.

###  Problèmes connus

**ISSUE:**

Le contrôleur d'entrée GKE On-Prem utilise Istio 1.1 avec détection
automatique de secrets. Cependant, l'agent de nœud pour la découverte de
secrets peut ne pas obtenir les mises à jour de secret après la suppression du
secret. Évitez donc de supprimer les secrets. Si vous devez supprimer un
secret et que TLS Ingress échoue par la suite, redémarrez manuellement le pod
Ingress dans l'espace de noms gke-system.

##  11 avril 2019

La version 1.2.1 de la version bêta de GKE On-Prem est désormais disponible.
Cette version inclut les modifications suivantes:

###  Nouvelles fonctionnalités

**FEATURE:**

Les clusters GKE On-Prem se reconnectent automatiquement à Google à l'aide de
[ Connect for Anthos ](https://cloud.google.com/kubernetes-
engine/connect?hl=fr) .

**FEATURE:**

Vous pouvez désormais exécuter jusqu'à trois plans de contrôle par cluster
utilisateur.

###  Modifications

**CHANGED:**

` gkectl ` valide maintenant les identifiants vSphere et F5 BIG-IP en créant
des clusters.

###  Problèmes connus

**ISSUE:**

Une régression oblige les commandes ` gkectl diagnose snapshot ` à utiliser la
mauvaise clé SSH, ce qui empêche la commande de collecter des informations
auprès des clusters utilisateur. Pour contourner les problèmes d'assistance,
vous devrez peut-être vous connecter en SSH à des nœuds de cluster
d'utilisateurs individuels et collecter manuellement des données.

##  2 avril 2019

La version bêta 1.1.1 de GKE On-Prem est désormais disponible. Cette version
inclut les modifications suivantes:

###  Nouvelles fonctionnalités

**FEATURE:**

Vous installez maintenant GKE On-Prem avec un [ Open Virtual Appliance (OVA)
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.1/how-
to/installation/getting-started?hl=fr#download_ova) , une image de machine
virtuelle préconfigurée qui inclut plusieurs outils d'interface de ligne de
commande. Cette modification facilite les installations et supprime une couche
de virtualisation. Vous n'avez plus besoin d'exécuter ` gkectl ` dans un
conteneur Docker.

Si vous avez installé des versions GKE On-Prem antérieures à la version
bêta-1.1.1, vous devez créer un poste de travail administrateur en suivant les
instructions fournies. Après avoir installé le nouveau poste de travail
administrateur, copiez les clés SSH, les fichiers de configuration, les
fichiers kubeconfigs et tous les autres fichiers dont vous avez besoin de
votre ancien poste de travail.

**FEATURE:**

Ajout de la documentation sur la [ sauvegarde et la restauration des clusters
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.1/how-
to/administration/backing-up?hl=fr) .

**FEATURE:**

Vous pouvez désormais configurer l'authentification pour les clusters à l'aide
d'OIDC et d'ADFS. Pour en savoir plus, consultez les pages [ S'authentifier
avec OIDC et ADFS ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/beta-1.1/how-to/security/oidc-adfs?hl=fr) et [
Authentification ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/concepts/authentication?hl=fr) .

###  Modifications

**CHANGED:**

Vous devez maintenant utiliser la clé privée d'un cluster d'administrateur
pour exécuter ` gkectl diagnose snapshot ` .

**CHANGED:**

Ajout d'une option de configuration lors de l'installation pour le déploiement
des clusters multimaître d'utilisateurs.

**CHANGED:**

La [ documentation Connect for Anthos ](https://cloud.google.com/kubernetes-
engine/connect?hl=fr) a été migrée.

###  Corrections

**FIXED:**

Résolution du problème d'interruption de la mise en réseau du cluster lors de
la suppression inattendue d'un nœud.

###  Problèmes connus

**ISSUE:**

La gestion de la configuration de GKE On-Prem est passée de la version 0.11 à
la version 0.13. Plusieurs composants du système ont été renommés. Vous devez
prendre quelques mesures pour nettoyer les ressources des versions précédentes
et installer une nouvelle instance.

Si vous disposez d'une instance active de gestion de la configuration:

  1. Désinstallez l'instance: 
    
        kubectl -n=nomos-system delete nomos --all

  2. Assurez-vous que l'espace de noms de l'instance ne comporte aucune ressource: 
    
        kubectl -n nomos-system get all

  3. Supprimez l'espace de noms : 
    
        kubectl delete ns nomos-system

  4. Supprimez le CRD: 
    
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
inclut les modifications suivantes:

###  Corrections

**FIXED:**

Le problème qui entraînait l'enregistrement des certificats Docker au mauvais
endroit a été résolu.

##  4 mars 2019

La version bêta 1.0.2 de GKE On-Prem est désormais disponible. Cette version
inclut les modifications suivantes:

###  Nouvelles fonctionnalités

**FEATURE:**

Vous pouvez maintenant exécuter ` gkectl version ` pour vérifier la version de
` gkectl ` que vous utilisez.

**FEATURE:**

Vous pouvez désormais [ mettre à niveau les clusters d'utilisateurs
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.0/beta-1.0/how-
to/administration/upgrading-a-cluster?hl=fr) vers les futures versions bêta.

**FEATURE:**

La version 0.11.6 d' [ Anthos Config Management
](https://cloud.google.com/anthos-config-management/docs?hl=fr) est désormais
disponible.

**FEATURE:**

Stackdriver Logging est désormais activé sur chaque nœud. Par défaut, l'agent
de journalisation réplique les journaux dans votre projet GCP uniquement pour
les services plan de contrôle, cluster API, vSphere controller, Calico, BIG-IP
controller, Envoy proxy, Connect for Anthos, Anthos Config Management,
Prometheus and Grafana, le plan de contrôle Istio et Docker.Les journaux de
conteneur d'application sont exclus par défaut, mais peuvent éventuellement
être activés.

**FEATURE:**

Stackdriver Prometheus side-car capture les métriques des mêmes composants que
l'agent de journalisation.

**FEATURE:**

Les [ règles de réseau Kubernetes
](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
sont désormais acceptées.

###  Modifications

**CHANGED:**

Vous pouvez maintenant mettre à jour les blocs d'adresses IP dans la
spécification du cluster pour étendre la plage d'adresses IP d'un cluster
donné.

**CHANGED:**

Si les clusters que vous avez installés pendant la phase alpha étaient
déconnectés de Google après la phase bêta, vous devrez peut-être les connecter
de nouveau. Reportez-vous à la section [ Enregistrement manuel d'un cluster
d'utilisateurs. ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/installation/registering-a-user-cluster?hl=fr)

**CHANGED:**

La page [ Premiers pas ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/installation/getting-started?hl=fr) a été mise
à jour avec les étapes d'activation de votre compte de service et d'exécution
de ` gkectl prepare ` .

**CHANGED:**

` gkectl diagnose snapshot ` ne collecte plus que les données de configuration
et exclut les journaux.Cet outil permet de capturer les détails de votre
environnement avant d'ouvrir une demande d'assistance.

**CHANGED:**

Prise en charge de la configuration facultative du nom de pool SNAT pour F5
BIG-IP au moment de la création du cluster. "Cela peut être utilisé pour
configurer la valeur" "--vs-snat-pool-name" "sur" [ Contrôleur BIG-IP F5
](https://clouddocs.f5.com/products/connectors/k8s-bigip-ctlr/v1.8/) .

**CHANGED:**

Vous devez maintenant fournir une adresse IP virtuelle pour les modules
complémentaires exécutés dans le cluster d'administration.

###  Corrections

**FIXED:**

Les opérations de redimensionnement du cluster ont été améliorées pour éviter
toute suppression involontaire de nœud.

##  7 février 2019

La version 1.3 de GKE On-Prem alpha est désormais disponible. Cette version
inclut les modifications suivantes:

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

GKE on-prem applique désormais des noms uniques pour les clusters
d'utilisateurs.

**CHANGED:**

Les points de terminaison de métriques et les API qui utilisent des points de
terminaison Istio sont désormais sécurisés à l'aide de mTLS et d'un contrôle
d'accès basé sur les rôles.

**CHANGED:**

La communication externe de Grafana est désactivée.

**CHANGED:**

Améliorations apportées à la vérification de l'état de Prometheus et
Alertmanager.

**CHANGED:**

Prometheus utilise désormais un port sécurisé pour récupérer les métriques.

**CHANGED:**

Plusieurs mises à jour des tableaux de bord Grafana

###  Problèmes connus

**ISSUE:**

Si votre compte utilisateur vCenter utilise un format tel que ` DOMAIN\USER `
, vous devrez peut-être échapper la barre oblique inverse ( ` DOMAIN\\USER `
). Assurez-vous de le faire lorsque vous êtes invité à saisir le compte
utilisateur lors de l'installation.

##  23 janvier 2019

La version 1.2.1 alpha de GKE On-Prem est désormais disponible. Cette version
inclut les modifications suivantes:

###  Nouvelles fonctionnalités

**FEATURE:**

Vous pouvez désormais utiliser ` gkectl ` pour [ supprimer des clusters
d'administration ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.0/latest/how-to/administration/deleting-an-admin-cluster?hl=fr)
.

.

###  Modifications

**CHANGED:**

Les commandes ` gkectl diagnose snapshot ` vous permettent désormais de
spécifier des nœuds lors de la capture d'instantanés de résultats et de
fichiers de commandes à distance.

##  14 janvier 2019

La version alpha 1.1.2 de GKE On-Prem est désormais disponible. Cette version
inclut les modifications suivantes:

###  Nouvelles fonctionnalités

**FEATURE:**

Vous pouvez maintenant utiliser la commande ` gkectl prepare ` pour extraire
et transférer les images de conteneur de GKE On-Prem, ce qui rend le script `
populate_registry.sh ` obsolète.

**FEATURE:**

` gkectl prepare ` Vous êtes maintenant invité à saisir des informations sur
votre cluster et votre pool de ressources.

**FEATURE:**

Vous pouvez désormais utiliser la commande ` gkectl create ` pour créer et
ajouter des clusters utilisateur à des plans de contrôle d'administration
existants en transmettant un fichier kubeconfig lorsque vous y êtes invité.

**FEATURE:**

Vous pouvez désormais transmettre un code secret TLS d'entrée pour les
clusters administrateur et utilisateur au moment de la création du cluster. La
nouvelle invite suivante s'affiche:

` Do you want to use TLS for Admin Control Plane/User Cluster ingress? `

La fourniture du code secret et des certificats TLS permet à ` gkectl ` de
configurer le protocole TLS d'Ingress. HTTP n'est pas automatiquement
désactivé lors de l'installation de TLS.

###  Modifications

**CHANGED:**

GKE On-Prem exécute désormais la version **1.11.2-gke.19** de Kubernetes.

**CHANGED:**

L'empreinte par défaut de GKE On-Prem a changé:

  * La mémoire minimale requise pour les nœuds de cluster utilisateur est désormais de 8192 millions. 

**CHANGED:**

GKE on-prem exécute désormais la version du minikube **0.28.0** .

**CHANGED:**

GKE Policy Management a été mis à jour vers la version **0.11.1** .

**CHANGED:**

` gkectl ` ne vous invite plus à fournir une configuration proxy par défaut.

**CHANGED:**

Il existe trois nouvelles ressources ConfigMap dans l'espace de noms du
cluster utilisateur: ` cluster-api-etcd-metrics-config ` , ` kube-etcd-
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
administrateur et utilisateur.

**CHANGED:**

` gkectl diagnose snapshot ` peut désormais prendre des instantanés de
fichiers distants sur le nœud, des résultats de commandes à distance sur les
nœuds et des requêtes Prometheus.

**CHANGED:**

` gkectl diagnose snapshot ` peuvent maintenant prendre des instantanés dans
plusieurs threads parallèles.

**CHANGED:**

` gkectl diagnose snapshot ` vous permet désormais de spécifier des mots à
exclure des résultats de l'instantané.

###  Corrections

**FIXED:**

Résolution des problèmes de mise en cache du mini-cube provoquant des appels
réseau inattendus.

**FIXED:**

Résolution du problème lié à l'extraction des identifiants F5 BIG-IP. Les
identifiants sont désormais lus à partir d'un fichier d'identifiants au lieu
d'utiliser des variables d'environnement.

###  Problèmes connus

**ISSUE:**

L'avertissement [ ` govmomi ` ](https://github.com/vmware/govmomi) suivant
peut s'afficher lorsque vous exécutez ` gkectl prepare ` :

` Warning: Line 102: Unable to parse 'enableMPTSupport' for attribute 'key' on
element 'Config' `

**ISSUE:**

Le redimensionnement de clusters utilisateur peut entraîner la suppression ou
la recréation involontaire du nœud.

**ISSUE:**

Impossible de monter les tags PersistentVolumes, ce qui génère l'erreur `
devicePath is empty ` . Pour contourner ce problème, supprimez et recréez la
valeur PersistentVolumeClaim associée.

**ISSUE:**

Le redimensionnement des blocs d'adresses IPAM en cas d'utilisation de
l'allocation d'adresses IP statiques pour les nœuds n'est pas pris en charge
en alpha. Pour contourner ce problème, pensez à allouer plus d'adresses IP que
nécessaire.

**ISSUE:**

Sur les disques lents, la création de la VM peut expirer et entraîner l'échec
des déploiements. Dans ce cas, supprimez toutes les ressources et réessayez.

##  19 décembre 2018

La version 1.0.4 de GKE On-Prem est désormais disponible. Cette version inclut
les modifications suivantes:

###  Corrections

**FIXED:**

La faille provoquée par [ CVE-2018-1002105
](https://github.com/kubernetes/kubernetes/issues/71411) a été corrigée.

##  30 novembre 2018

GKE On-Prem alpha 1.0 est désormais disponible. Les modifications suivantes
sont incluses dans cette version:

###  Modifications

**CHANGED:**

GKE On-Prem alpha 1.0 exécute Kubernetes 1.11.

**CHANGED:**

L'empreinte par défaut de GKE On-Prem a changé:

  * Le plan de contrôle d'administration exécute trois nœuds, qui utilisent 4 processeurs et 16 Go de mémoire. 
  * Le plan de contrôle d'utilisateur exécute un nœud qui utilise 4 processeurs et 16 Go de mémoire. 
  * Les clusters d'utilisateurs exécutent au moins trois nœuds, qui utilisent 4 processeurs et 16 Go de mémoire. 

**CHANGED:**

Prise en charge de la configuration Prometheus haute disponibilité

**CHANGED:**

Compatibilité avec la configuration personnalisée d'Alert Manager.

**CHANGED:**

Prometheus est passé de **2.3.2** à **2.4.3** .

**CHANGED:**

Grafana est passé de **5.0.4** à **5.3.4** .

**CHANGED:**

kube-state-metrics est passé de **1.3.1** à **1.4.0** .

**CHANGED:**

Alert Manager est passé de **1.14.0** à **1.15.2** .

**CHANGED:**

node_exporter est passé de **1.15.2** à **1.16.0** .

###  Corrections

**FIXED:**

La faille de [ CVE-2018-1002103
](https://github.com/kubernetes/minikube/issues/3208) a été corrigée.

###  Problèmes connus

**ISSUE:**

Impossible de monter les tags PersistentVolumes, ce qui génère l'erreur `
devicePath is empty ` . Pour contourner ce problème, supprimez et recréez la
valeur PersistentVolumeClaim associée.

**ISSUE:**

Le redimensionnement des blocs d'adresses IPAM en cas d'utilisation de
l'allocation d'adresses IP statiques pour les nœuds n'est pas pris en charge
en alpha. Pour contourner ce problème, pensez à allouer plus d'adresses IP que
nécessaire.

**ISSUE:**

GKE On-Prem alpha 1.0 ne passe pas encore tous les tests de conformité.

**ISSUE:**

Un seul cluster d'utilisateurs par cluster d'administration peut être créé.
Pour créer des clusters d'utilisateurs supplémentaires, créez un autre cluster
d'administration.

##  31 octobre 2018

GKE On-Prem EAP 2.1 est désormais disponible. Les modifications suivantes sont
incluses dans cette version:

###  Modifications

**CHANGED:**

Lorsque vous créez des clusters administrateur et utilisateur en même temps,
vous pouvez désormais réutiliser les identifiants BIG-IP F5 du cluster
d'administration pour créer le cluster utilisateur. De plus, la CLI exige
désormais que les identifiants BIG-IP soient fournis. cette condition ne peut
pas être ignorée à l'aide de ` --dry-run ` .

**CHANGED:**

Contrôleur F5 BIG-IP mis à niveau pour utiliser la dernière version OSS,
1.7.0.

**CHANGED:**

Pour améliorer la stabilité des machines vSphere lentes, le délai d'expiration
de création de la machine en cluster est désormais de 15 minutes (cinq minutes
auparavant).

##  17 octobre 2018

GKE On-Prem EAP 2.0 est désormais disponible. Les modifications suivantes sont
incluses dans cette version:

###  Modifications

**CHANGED:**

Compatibilité avec GKE Connect

**CHANGED:**

Compatibilité avec Monitoring.

**CHANGED:**

Prise en charge de l'installation à l'aide de répertoires privés.

**CHANGED:**

Prise en charge de l'équilibreur de charge L7 en tant que VIP L4 sur F5 BIG-
IP.

**CHANGED:**

Prise en charge de l'allocation d'adresses IP statiques pour les nœuds lors du
démarrage du cluster.

###  Problèmes connus

**ISSUE:**

Un seul cluster d'utilisateurs par cluster d'administration peut être créé.
Pour créer des clusters d'utilisateurs supplémentaires, créez un autre cluster
d'administration.

**ISSUE:**

Les mises à niveau de cluster ne sont pas compatibles avec EAP 2.0.

**ISSUE:**

Sur les disques lents, la création de la VM peut expirer et entraîner l'échec
des déploiements. Dans ce cas, supprimez toutes les ressources et réessayez.

**ISSUE:**

Dans le cadre du processus d'amorçage de cluster, une instance de minikube
éphémère est exécutée. La version de Minikube utilisée présente une faille de
sécurité [ CVE-2018-1002103
](https://github.com/kubernetes/minikube/issues/3208) .

