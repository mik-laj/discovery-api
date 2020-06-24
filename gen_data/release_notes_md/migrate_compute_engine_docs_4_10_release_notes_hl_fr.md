#  Notes de version

Cette page répertorie les mises à jour en production de Migrate for Compute
Engine. Consultez-la régulièrement pour obtenir des informations sur les
fonctionnalités nouvelles ou mises à jour, les corrections de bugs, les
problèmes connus et les fonctionnalités obsolètes.

Vous pouvez consulter les dernières mises à jour de produits pour l'ensemble
de Google Cloud sur la page [ Notes de version de Google Cloud
](https://cloud.google.com/release-notes?hl=fr) .

Pour recevoir les dernières mises à jour concernant ce produit, ajoutez l'URL
de cette page à votre [ lecteur de flux
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ou ajoutez l'URL
du flux directement : ` https://cloud.google.com/feeds/migrate-for-compute-
engine-release-notes.xml `

Pour obtenir la liste des compilations de cette version et d'autres versions,
consultez l' [ historique de compilation
](https://cloud.google.com/migrate/compute-engine/docs/build-history?hl=fr) .

##  Conditions requises et systèmes d'exploitation compatibles

Consultez les sections [ Conditions requises
](https://cloud.google.com/migrate/compute-
engine/docs/4.10/concepts/requirements?hl=fr) et [ Systèmes d'exploitation
compatibles ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/supported-os-versions?hl=fr) .

##  4.10 – Nouvelles fonctionnalités

###  Intégration de Cloud Console

**FEATURE:**

La version 4.10 s'intègre à la [ console GCP ](https://cloud.google.com/cloud-
console/?hl=fr) pour faciliter le déploiement du gestionnaire de migration et
la création des comptes de service requis.

###  Déploiement dans un environnement d'accès privé

**FEATURE:**

La version 4.10 accepte le déploiement dans des environnements avec l'accès
privé à l'API activé. Dans ces environnements, le système est déployé sans
adresse IP publique et utilise un accès privé pour accéder aux API Cloud.
Consultez la section [ Configurer le gestionnaire de migration
](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-to/configure-
manager/configuring-migration-manager?hl=fr) .

###  Déploiement facultatif du plug-in vCenter

**FEATURE:**

La version 4.10 présente l'option de déploiement dans un environnement vCenter
source sur site avec ou sans déploiement de plug-in vCenter. Le déploiement
sans plug-in vCenter vous permet de connecter plusieurs systèmes Migrate au
même environnement vCenter. Consultez la section [ Enregistrer l'environnement
VMware vCenter ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/how-to/configure-manager/configuring-vms-
vm?hl=fr#register_the_vmware_vcenter_environment) .

###  Compatibilité avec le script personnalisé de prétraitement/post-
traitement lors de la mise à niveau de Windows 2008 vers 2012

**FEATURE:**

La version 4.10 accepte l'exécution de scripts personnalisés de
prétraitement/post-traitement lors de l'utilisation de la mise à niveau
Windows. Vous pouvez ajouter des scripts personnalisés à la VM. Consultez [
Mettre à niveau des VM Windows Server
](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-to/upgrading-
vms/upgrading-windows-vms?hl=fr) pour plus d'informations.

###  Compatibilité avec la migration des instances Azure Gen2 vers Compute
Engine

**FEATURE:**

La version 4.10 prend en charge la migration des instances [ Azure Gen2
](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/supported-os-versions?hl=fr) vers les instances
Compute Engine avec compatibilité UEFI.

###  Détection automatique des systèmes d'exploitation et attribution des
licences

**FEATURE:**

La version 4.10 introduit automatiquement l'identification du système
d'exploitation migré qui attribuera par défaut la licence appropriée à la VM
migrée. Dans les cas où vous souhaitez migrer des VM à l'aide de la licence
Windows BYOL ou de la licence premium Linux, vous devez les fournir sous forme
d'entrées dans le runbook. Veuillez consulter la [ section relative aux
licences ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/runbooks?hl=fr) de la documentation.

##  Problèmes résolus

**FIXED:**

Correction d'un problème lié aux pilotes AWS ena qui entraînait le plantage
des images Windows après la migration.

##  Problèmes connus

**ISSUE:**

**149004085** : Ubuntu 14 depuis l'environnement sur site peut échouer à
démarrer la dissociation d'un réseau.

**Solution** : connectez-vous via la console série et ajoutez manuellement
l'interface réseau avec DHCP.

**ISSUE:**

**145086776** : dans de rares cas, les anciennes versions de RHEL7 peuvent se
bloquer lors de la diffusion ou atteindre une panique du noyau. Ce problème a
été résolu dans les versions ultérieures de RHEL7.

**Solution** : exécutez ` sudo yum update ` avant la migration pour mettre à
jour le système.

**ISSUE:**

**145644737** : les clones créés sur Azure ou AWS à partir d'instances de
distribution Linux utilisant cloud-init peuvent rencontrer des problèmes de
démarrage après l'installation du package de préparation Linux.

**Solution** : désinstallez le package avant de le cloner, puis réinstallez-le
lors de la préparation de la migration.

**ISSUE:**

**143313211** : les clients qui migrent la VM RHEL 6.8 peuvent rencontrer des
problèmes de démarrage dans la destination cloud.

Les systèmes RHEL 6.x utilisant des versions de noyau 2.6.32-xxx et utilisant
LVM peuvent rencontrer une panique du noyau lors du démarrage dans Compute
Engine lors de la migration.

**Solution** : le noyau doit être mis à niveau vers la version 2.6.32-754 ou
ultérieure avant la migration.

**ISSUE:**

**143262721** : la migration de VM depuis Azure échoue lorsque le disque de
données est supérieur à 4 téraoctets.

À l'heure actuelle, Migrate for Compute Engine n'est pas compatible avec la
migration de VM Azure avec des disques de données supérieurs à 4 To.

**Solution** : assurez-vous que la VM dispose d'un disque de données inférieur
à 4 To.

**ISSUE:**

**131532690** : les opérations run-in-cloud et de migration peuvent échouer
pour la charge de travail Windows Server 2016 lorsque Symantec Endpoint
Protection (SEP) est installé. Cela peut également se produire lorsque SEP
semble être désactivé.

**Solution** : modifiez les liaisons de l'interface réseau de la charge de
travail pour supprimer l'option SEP.

  1. Téléchargez [ Microsoft Network VSP Bind (nvspbind) ](https://gallery.technet.microsoft.com/Hyper-V-Network-VSP-Bind-cf937850) . 
  2. Installez Microsoft_Nvspbind_package.EXE dans c:\temp. 
  3. Ouvrez une invite de commande en tant qu'administrateur et exécutez la commande suivante : 
    
        nvspbind.exe /d * symc_teefer2

**ISSUE:**

**131637800** : lorsque le package RPM velostrata-prep est installé sur SUSE
Linux Enterprise Server 11, la VM obtient une adresse IP DHCP en plus d'une
configuration IP statique existante. Ce problème survient lorsque la VM est
démarrée sur site dans un sous-réseau activé avec les services DHCP.

Remarque : Le problème ne se produit pas lorsque le sous-réseau ne dispose
d'aucun service DNS. Il n'y a aucun impact sur la connectivité des
communications avec l'adresse IP statique d'origine.

**ISSUE:**

**131637800** : une fois que le plug-in Velostrata est enregistré, l'exécution
de l'assistant d'extension cloud peut générer une erreur "XXXXXXXXXX" lorsque
l'opération est terminée.

**Solution** : annulez l'enregistrement du plug-in Velostrata et redémarrez le
service client Web vSphere, puis réenregistrez le plug-in. Contactez
l'assistance si le problème persiste.

**ISSUE:**

**131548730** : dans certains cas, lorsqu'une VM est déplacée lors de
l'opération run-in-cloud alors qu'une solution de sauvegarde tierce contient
un instantané temporaire, les opérations d'écriture périodiques Migrate for
Compute Engine ne se terminent pas même après la suppression de l'instantané
temporaire. Le compteur d'écritures non validées sur la VM affichera une
taille croissante et aucun point de contrôle de cohérence ne sera créé sur
site.

**Solution** : sélectionnez l'action "Exécuter sur site" pour la VM et
attendez que la tâche soit terminée, ce qui validera toutes les écritures en
attente. Sélectionnez ensuite à nouveau l'action "Run-in-cloud". Notez que la
validation de nombreuses écritures en attente peut prendre un certain temps.
N'utilisez pas l'option "Forcer", car cela entraînerait la perte des écritures
non validées.

**ISSUE:**

**131605387** : le redémarrage de vCenter entraîne la disparition des tâches
Velostrata dans vCenter de l'interface utilisateur. Il s'agit d'une limitation
de vCenter.

**Solution** : utilisez le module Velostrata PowerShell pour surveiller les VM
gérées Velostrata ou les tâches d'extensions cloud en cours d'exécution.

**ISSUE:**

**131638716** : avec un hôte ESXi en mode de maintenance, si une VM est
déplacée vers le cloud, l'opération échoue et est bloquée pendant la phase de
rollback.

**Solution** : annulez manuellement la tâche "Run-in-cloud", migrez la VM vers
un autre hôte ESXi dans le cluster et relancez l'opération "Run-in-cloud".

**ISSUE:**

**131638455** : une opération "Run-in-cloud" échoue avec le message d'erreur
"Échec de la création de l'instantané de machine virtuelle. L'opération tentée
ne peut pas être effectuée dans l'état actuel (Hors tension)".

**Solution** : il se peut que le fichier d'instantané de la VM VMware pointe
vers un instantané inexistant. Contactez l'assistance pour résoudre le
problème.

**ISSUE:**

**131534862** : dans de rares cas, après l'exécution d'une charge de travail
sur site, les disques VMDK de la charge de travail sont verrouillés. Dans
certains cas, cela est dû à des interruptions du réseau entre le dispositif de
gestion Velostrata et l'hôte ESXi sur lequel la charge de travail est
exécutée.

Remarque : Le problème sera résolu au bout d'une à deux heures.

**ISSUE:**

**131550214** : lors de la dissociation, l'opération peut échouer avec le
message d'erreur suivant : "L'opération a été annulée".

**Solution** : relancez l'opération de dissociation.

**ISSUE:**

**131650367** : lors d'une opération de dissociation après une annulation de
dissociation, l'action peut échouer.

**Solution** : relancez l'opération.

**ISSUE:**

**131649978** : en cas de défaillance du système, les composants Velostrata se
déconnectent de vCenter. Dans ce cas, il est possible qu'un événement ne soit
pas envoyé et que l'alarme ne soit pas correctement définie ou ne soit pas
effacée correctement.

**Solution** : effacez l'alarme manuellement dans vCenter.

**ISSUE:**

**131532549** : pour les charges de travail avec une machine Windows utilisant
une licence de commerce, la licence n'existe pas lorsque vous revenez du
cloud.

**Solution** : réinstallez la licence.

**ISSUE:**

**131555885** : l'opération "Exporter OVA" de vCenter est disponible lorsque
la VM dans le cloud s'exécute en mode cache, mais cette opération entraîne un
fichier OVA corrompu.

**Solution** : ne créez le fichier OVA qu'après la dissociation.

**ISSUE:**

**131647857** : dans de rares cas, lorsqu'une instance de composant cloud est
créée et que le système échoue avant l'ajout de tags, l'instance reste sans
tag. Cela empêchera le nettoyage complet et la réparation de l'extension
cloud.

**Solution** : ajoutez manuellement un tag à l'instance, puis exécutez la
commande "Réparer".

**ISSUE:**

**131537125** : la haute disponibilité de l'extension cloud ne fonctionne pas
pour les charges de travail exécutant le système d'exploitation Ubuntu avec la
configuration LVM.

**Solution** : mettez à jour le noyau vers la version 3.13.0-161 ou
ultérieure.

**ISSUE:**

**131560126** – Suse12 : en raison d'un bug du noyau SUSE antérieur à la
version 4.2, les configurations incluant des montages BTRFS avec des sous-
volumes ne sont pas compatibles.

**Solution** : effectuez une mise à niveau vers SUSE avec le noyau >=4.2
(SP2).

**ISSUE:**

**131533480** : lorsque vous utilisez l'assistant de création d'extension
cloud, l'utilisation d'une adresse de proxy HTTP illégal ne génère pas de
message d'avertissement.

**Solution** : supprimez l'extension cloud, puis créez-la avec une adresse de
proxy HTTP valide.

**ISSUE:**

**131647654** : l'exécution de l'opération sur site a réussi, mais l'état est
marqué comme ayant échoué avec l'erreur "Impossible de regrouper les
instantanés".

**Solution** : regroupez les instantanés via vCenter et effacez l'erreur
manuellement.

**ISSUE:**

**131558198** : le client PowerShell pour le runbook cloud à cloud signale des
erreurs lors de l'exécution sur PowerShell 3.0.

**Solution** : passez à PowerShell 4.0.

**ISSUE:**

**131533056** : lors de la migration de RHEL 7.4 de AWS vers Google Cloud,
l'agent Google Cloud n'est pas installé automatiquement.

**Solution** : supprimez manuellement l'agent AWS et installez l'agent Google
Cloud.

**ISSUE:**

**131532713** : après la migration hors connexion de Windows 2003R2, si une
carte d'interface réseau est supprimée manuellement, il peut être impossible
de la détecter et de la réinstaller automatiquement.

Solution : le stockage de VM peut être associé à une autre VM et l'entrée de
registre de la carte d'interface réseau peut être importée manuellement en
utilisant une VM similaire comme référence. Contactez l'assistance pour
obtenir de l'aide.

**ISSUE:**

**131532666** : les versions Linux exécutées avec la version du noyau 2.6.32
peuvent subir une panique du noyau en cas d'échec de l'accès au stockage
éphémère. Ces erreurs sont plus susceptibles de se produire lors de la
diffusion en continu sur iSCSI.

Solution : mettez à jour votre noyau. Le problème sera également réduit après
la dissociation.

**ISSUE:**

**131532846** : certains pare-feu et antivirus peuvent entraîner l'échec des
VM Windows lors du transfert vers le cloud en bloquant le trafic iSCSI.

Solution : désactivez le service concerné lors de la migration et réinstallez-
le après la dissociation.

**ISSUE:**

**131532882** : dans certains cas, l'exécution de l'opération "Run-in-cloud"
lors d'une mise à jour de Windows peut entraîner l'arrêt brutal de la mise à
jour et un échec du démarrage dans le cloud.

Solution : autorisez le système à terminer la mise à jour Windows et/ou à
suspendre les mises à jour Windows avant la migration.

**ISSUE:**

**135664281** : lorsque vous effectuez ou annulez la migration d'Azure vers
Google Cloud, si Velostrata Management ne parvient pas à démarrer
l'importateur, les ressources créées par Velostrata peuvent rester dans le
groupe de ressources de l'instance d'origine.

**ISSUE:**

**133137658** – Scénario : aucune connexion réseau entre le gestionnaire de
migration et VSphere.

Impact sur le client : la tâche "Run-in-cloud" reste bloquée en raison d'un
échec de l'appel de getReadSessions sur VSphere.

**Solution** : corrigez la connexion réseau. Vous pouvez également annuler la
tâche et réessayer.

**ISSUE:**

**135573857** – Scénario : lors du déplacement d'une VM sur site avec
l'indicateur "force", l'échec du regroupement de l'instantané entraîne la
gestion de Velostrata par la VM. L'opération "Run-in-cloud" sur la même VM
peut échouer, car elle n'est pas autorisée sur les VM gérées.

**Solution** : attendez quelques minutes, puis réessayez.

**ISSUE:**

**137082702** : dans de rares cas, l'opération d'annulation de la dissociation
réussit, mais l'instance de VM ne démarre pas.

**Solution** : replacez l'instance dans son emplacement d'origine et déplacez-
la vers le cloud.

