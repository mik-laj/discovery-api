#  Notes de version : Jalon 69

##  État actuel

Famille d'images  |  cos-69-lts  
---|---  
Obsolète à partir du  |  11 déc. 2019  
Noyau  |  [ 4.14.91+
](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/edb81c460eee7a4a35e2a95ebf6450df0963398e)  
Kubernetes  |  v1.11.1  
Docker  |  v17.03.2  
  
##  Journal des modifications (depuis le jalon 68)

###  cos-69-10895-172-0

_Date : 28 février 2019_

  * Activation de kernel.softlockup_all_cpu_backtrace, qui était précédemment désactivé afin d'atténuer un problème, maintenant résolu, de blocage du noyau. 
  * Configuration de docker.service en définissant RestartSecs=10 pour systématiquement redémarrer Docker au bout de 10 secondes. 

###  cos-69-10895-138-0

_Date : 24 janvier 2019_

  * Rétroportage du correctif résolvant un problème de blocage lors d'une panique du noyau. 
  * Intégration du noyau stable Linux v4.14.91. 

###  cos-69-10895-123-0

_Date : 10 janvier 2019_

  * Définition de CONFIG_BLK_WBT_MQ=y pour améliorer l'isolation des performances sur les disques persistants. Cette modification corrige un bug à cause duquel les écritures sur un disque persistant SSD peuvent affecter les performances sur le disque de démarrage persistant standard. 
  * Sélection de commits Ext4 qui corrigent des incohérences au niveau du système de fichiers, dues à des perturbations lors de l'opération NFS CREATE dans certaines conditions. 
  * Intégration du noyau stable Linux v4.14.89. 

###  cos-69-10895-102-0

_Date : 20 décembre 2018_

  * Désactivation de la mise à jour automatique sur les images protégées. Les images dans cos-cloud ne sont pas affectées par ce changement. 
  * Activation de la fonctionnalité ext4 "metadata_csum" sur la partition avec état. Cette modification améliore également les performances du redimensionnement du disque de démarrage. 
  * Application de la stratégie IMA uniquement lorsque cloud-audit-setup.service est explicitement exécuté. 

###  cos-69-10895-93-0

_Date : 16 novembre 2018_

  * Mise à jour du noyau vers la version v4.14.79. 
  * Correction du bug empêchant cloud-init d'écrire des fichiers compressés avec gzip. 

###  cos-69-10895-91-0

_Date : 29 octobre 2018_

  * Résolution du problème de blocage pouvant survenir lors d'une interaction entre IMA et NFS. 
  * Correction d'un problème stackdriver-logging.service observé dans les conteneurs sur Compute Engine. 
  * PCID est désormais activé par défaut lorsqu'il est compatible avec la plate-forme du processeur. 

###  cos-69-10895-85-0

_Date : 11 octobre 2018_

  * Réinitialisation de softlockup_all_cpu_backtrace sur la valeur 0 pour éviter le blocage du noyau, dans certaines circonstances, sur les machines à haute capacité de processeur. 

###  cos-69-10895-71-0

_Date : 1er octobre 2018_

  * Suppression des en-têtes d'utilisateur dans l'artefact d'en-tête du noyau. 

###  cos-69-10895-62-0

_Date : 18 septembre 2018_

  * Promotion en version stable. 
  * Rétroportage d'un correctif pour s'assurer que scsi contribue au caractère aléatoire lorsqu'il exécute un appareil rotationnel  . Cette modification résout un problème de ralentissement au démarrage de docker en raison d'une entropie faible sur les disques persistants standards depuis l'intégration de la version 4.14.63. 
  * Activation de CONFIG_RANDOM_TRUST_CPU pour résoudre le problème de manque d'entropie sur les disques de démarrage SSD persistants. 
  * Mise à niveau d'OpenSSL vers la version 1.0.2p. 
  * Intégration de la version stable Linux v4.14.65. 
  * Rétroportage du correctif pour le bug cloud-init empêchant write_files de traiter du contenu non-asci  . 
  * Rétroportage d'un correctif pour l'avertissement du noyau "WARNING: fs/overlayfs/readdir.c:393 ovl_iterate+0x25c/0x260 WARN_ON(!cache->refcount)" 
  * Correctif pour le noyau Linux CVE-2018-12232. 
  * Rétroportage de correctifs pour le problème L1 Terminal Fault (L1TF) (CVE-2018-3615, CVE-2018-3620 et CVE-2018-3646). 
  * Correctifs pour CVE-2018-5391. 
  * Correction d'un problème de blocage logiciel survenant sur les VM à processeur virtuel unique lors de l'utilisation de systèmes de fichiers FUSE. 
  * Mise à jour de Kubernetes vers la version v1.11.1. 
  * Correctifs pour CVE-2018-5390. 
  * Augmentation de la valeur kernel.pid_max par défaut à 2^22. 
  * Intégration de la version stable Linux v4.14.54 dans le noyau. 
  * Suppression de la compatibilité avec les CD-ROM SCSI. Cette modification corrige CVE-2018-11506. 
  * Mise à niveau de Kubelet intégré vers la version v1.11.0. 
  * Mise à niveau de docker-credential-gcr vers la version 1.5.0. 
  * Mise à niveau de BUG_REPORT_URL dans /etc/os-release. 
  * Activation des configurations de débogage NFS dans le noyau. 
  * Activation du module de noyau tcp_bbr pour le contrôle de la congestion TCP. 
  * Mise à niveau de Git vers la version 2.16.4 pour corriger CVE 2018-11235. 
  * Définition de l'option de configuration Docker "--disable-legacy-registry" sur la valeur "true" par défaut. 
  * Mise à niveau de Kubernetes vers la version 1.10.4. 
  * Mise à niveau de sshd_config pour supprimer les chiffrements basés sur cbc. 
  * Mise à jour des certificats CA racine pour correspondre à Mozilla NSS 3.36.1. 
  * Mise à niveau de OpenSSL vers la version 1.0.2o. 

