#  Bulletins de sécurité

Nous publions occasionnellement des bulletins de sécurité relatifs à Compute
Engine. Tous sont décrits sur cette page.

[ S'abonner aux bulletins de sécurité Compute Engine
![S'abonner](https://cloud.google.com/images/feed-icon.png?hl=fr)
](https://cloud.google.com/feeds/compute-engine-security-bulletins.xml?hl=fr)

##  Date de publication : 18-06-2019

**Dernière mise à jour : 25-06-2019 6:30 PST**

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

Récemment, Netflix a révélé trois failles TCP dans les noyaux Linux :

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

Ces failles CVE sont collectivement désignées sous le nom de [ NFLX-2019-001
](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-
party/2019-001.md) .

####  Impact sur Compute Engine

L'infrastructure qui héberge Compute Engine est protégée contre cette faille.

Les VM Compute Engine exécutant des systèmes d'exploitation Linux non corrigés
qui envoient/reçoivent du trafic réseau non approuvé sont vulnérables à cette
attaque par déni de service (DoS). Pensez à mettre à jour ces instances de VM
dès que des correctifs sont disponibles pour leur système d'exploitation.

Les équilibreurs de charge qui interrompent les connexions TCP ont été
corrigés. Les instances Compute Engine qui ne reçoivent que du trafic non
approuvé via ces équilibreurs de charge ne sont pas vulnérables. Sont inclus
les équilibreurs de charge HTTP, ainsi que les équilibreurs de charge proxy
SSL et TCP.

Les équilibreurs de charge réseau et internes n'interrompent pas les
connexions TCP. Les instances Compute Engine non corrigées qui reçoivent du
trafic non approuvé via ces équilibreurs de charge sont vulnérables.

####  Images corrigées et ressources des fournisseurs

Vous trouverez ici des liens vers les informations sur les correctifs de
chaque fournisseur de système d'exploitation dès qu'elles seront disponibles,
y compris l'état de chaque faille CVE. Les versions antérieures de ces images
publiques n'incluent pas ces correctifs et ne protègent pas contre les
attaques potentielles :

  * Projet ` debian-cloud ` : 
    * ` debian-9-stretch-v20190618 `
  * Projet ` centos-cloud ` : 
    * ` centos-6-v20190619 `
    * ` centos-7-v20190619 `
  * Projet ` cos-cloud ` : 
    * ` cos-dev-77-12293-0-0 `
    * ` cos-beta-76-12239-21-0 `
    * ` cos-stable-75-12105-77-0 `
    * ` cos-73-11647-217-0 `
    * ` cos-69-10895-277-0 `
  * Projet ` coreos-cloud ` : 
    * ` coreos-alpha-2163-2-1-v20190617 `
    * ` coreos-beta-2135-3-1-v20190617 `
    * ` coreos-stable-2079-6-0-v20190617 `
  * Projet ` rhel-cloud ` : 
    * ` rhel-6-v20190618 `
    * ` rhel-7-v20190618 `
    * ` rhel-8-v20190618 `
  * Projet ` rhel-sap-cloud ` : 
    * ` rhel-7-4-sap-v20190618 `
    * ` rhel-7-6-sap-v20190618 `
  * Projet ` suse-cloud ` : 
    * ` sles-12-sp4-v20190617 `
    * ` sles-15-v20190617 `
  * Projet ` suse-sap-cloud ` : 
    * ` sles-12-sp1-sap-v20190617 `
    * ` sles-12-sp2-sap-v20190617 `
    * ` sles-12-sp3-sap-v20190617 `
    * ` sles-12-sp4-sap-v20190617 `
    * ` sles-15-sap-v20190617 `
  * Projet ` ubuntu-cloud ` : 
    * ` ubuntu-1604-xenial-v20190617 `
    * ` ubuntu-1804-bionic-v20190617 `
    * ` ubuntu-1810-cosmic-v20190618 `
    * ` ubuntu-1904-disco-v20190619 `
    * ` ubuntu-minimal-1604-xenial-v20190618 `
    * ` ubuntu-minimal-1804-bionic-v20190617 `
    * ` ubuntu-minimal-1810-cosmic-v20190618 `
    * ` ubuntu-minimal-1904-disco-v20190618 `

|  Moyen  |

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

  
  
##  Date de publication : 14-05-2019

**Dernière mise à jour : 20-05-2019 17:00 PST**

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

Intel a divulgué les failles CVE suivantes :

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

Ces failles CVE sont collectivement désignées sous le nom de
"Microarchitectural Data Sampling (MDS)". En raison de l'interaction entre
l'exécution spéculative et l'état microarchitectural, elles comportent un
risque d'exposition des données.

####  Impact sur Compute Engine

**L'infrastructure hôte qui exécute Compute Engine isole les charges de
travail des clients les unes des autres. À moins que vous n'exécutiez du code
non approuvé dans vos VM, aucune autre action n'est requise.**

Pour les clients exécutant du code non approuvé dans leurs propres services
mutualisés sur des machines virtuelles Compute Engine, reportez-vous aux
recommandations d'atténuation de votre fournisseur d'OS invité, qui peuvent
inclure l'utilisation des fonctionnalités Intel d'atténuation du microcode.
Nous avons déployé un accès invité direct à la nouvelle fonctionnalité de
vidage. Vous trouverez ci-dessous un résumé de la procédure d'atténuation
disponible pour les images courantes d'invités.

####  Images corrigées et ressources des fournisseurs

Vous trouverez ici des liens vers les informations sur les correctifs de
chaque fournisseur de système d'exploitation dès qu'elles seront disponibles,
y compris l'état de chaque faille CVE. Utilisez ces images pour recréer des
instances de VM. Les versions antérieures de ces images publiques n'incluent
pas ces correctifs et n'offrent aucune protection contre des attaques
potentielles :

  * Projet ` centos-cloud ` : [ CESA-2019:1169 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023309.html) , [ CESA-2019:1168 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023314.html)
    * ` centos-6-v20190515 `
    * ` centos-7-v20190515 `
  * Projet ` coreos-cloud ` : [ atténuations MDS pour CoreOS Container Linux ](https://coreos.com/os/docs/latest/disabling-smt.html)
    * ` coreos-stable-2079-4-0-v20190515 `
    * ` coreos-beta-2107-3-0-v20190515 `
    * ` coreos-alpha-2135-1-0-v20190515 `
  * Projet ` cos-cloud `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
  * Projet ` debian-cloud ` : [ DSA-4444 ](https://www.debian.org/security/2019/dsa-4444)
    * ` debian-9-stretch-v20190514 `
  * Projet ` rhel-cloud ` : [ article sur MDS de la base de connaissances Red Hat ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-6-v20190515 `
    * ` rhel-7-v20190517 `
    * ` rhel-8-v20190515 `
  * Projet ` rhel-sap-cloud ` : [ article sur MDS de la base de connaissances Red Hat ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-7-4-sap-v20190515 `
    * ` rhel-7-6-sap-v20190517 `
  * Projet ` suse-cloud ` : [ article sur MDS de la base de connaissances SUSE ](https://www.suse.com/support/kb/doc/?id=7023736)
    * ` sles-12-sp4-v20190520 `
    * ` sles-15-v20190520 `
  * Projet ` suse-sap-cloud `
    * ` sles-12-sp4-sap-v20190520 `
    * ` sles-15-sap-v20190520 `
  * Projet ` ubuntu-os-cloud ` : [ wiki d'Ubuntu sur MDS ](https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/MDS)
    * ` ubuntu-1404-trusty-v20190514 `
    * ` ubuntu-1604-xenial-v20190514 `
    * ` ubuntu-1804-bionic-v20190514 `
    * ` ubuntu-1810-cosmic-v20190514 `
    * ` ubuntu-1904-disco-v20190514 `
    * ` ubuntu-minimal-1604-xenial-v20190514 `
    * ` ubuntu-minimal-1804-bionic-v20190514 `
    * ` ubuntu-minimal-1810-cosmic-v20190514 `
    * ` ubuntu-minimal-1904-disco-v20190514 `
  * Projets ` windows-cloud ` et ` windows-sql-cloud ` : [ avis de sécurité ADV190013 de Microsoft ](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/ADV190013)
    * Toutes les images publiques Windows Server et SQL Server comportant le numéro de version ` v20190514 ` . 
  * Projet ` gce-uefi-images `
    * ` centos-7-v20190515 `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
    * ` rhel-7-v20190517 `
    * ` ubuntu-1804-bionic-v20190514 `
    * Toutes les images publiques Windows Server comportant le numéro de version ` v20190514 ` . 

####  Container-Optimized OS

Si vous utilisez Container-Optimized OS (COS) en tant que système
d'exploitation invité, et que vous exécutez des charges de travail mutualisées
non approuvées dans votre machine virtuelle, nous vous recommandons de
procéder comme suit :

  1. Désactivez la technologie Hyper-Threading en définissant ` nosmt ` sur la ligne de commande du noyau.   

Sur les VM COS existantes, vous pouvez modifier le paramètre ` grub.cfg `
comme illustré ci-dessous afin de définir l'option ` nosmt ` , puis redémarrer
le système :

    
        
    # Run as root:
    dir="$(mktemp -d)"
    mount /dev/sda12 "${dir}"
    sed -i -e "s|cros_efi|cros_efi nosmt|g" "${dir}/efi/boot/grub.cfg"
    umount "${dir}"
    rmdir "${dir}"
    
    reboot

Pour plus de simplicité, vous pouvez exécuter le script ci-dessous. Vous
obtiendrez le même résultat que si vous aviez exécuté les commandes décrites
précédemment. Afin de garantir que les nouvelles VM utiliseront ce paramètre,
nous vous recommandons d'intégrer ce code dans vos scripts cloud-config de
démarrage ou dans vos modèles d'instance. Vous trouverez ci-après un exemple
de script cloud-config exécutant ce code.

**Avertissement** : À sa première exécution, cette commande entraînera un
redémarrage immédiat de l'instance. Les exécutions successives de cette
commande sur les instances où la technologie Hyper-Threading est déjà
désactivée n'auront aucun effet.

    
        
    # Run as root
    /bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)
    

Pour inclure ce code dans le script cloud-config :

    
        
    #cloud-config
    
    bootcmd:
    - /bin/bash -c "/bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)"
    

Pour vérifier si la technologie Hyper-Threading est désactivée sur votre
instance, vérifiez le résultat des fichiers `
/sys/devices/system/cpu/smt/active ` et ` /sys/devices/system/cpu/smt/control
` . Si les résultats sont ` 0 ` pour ` active ` et ` off ` pour ` control ` ,
l'Hyper-Threading est désactivé :

    
        
    cat /sys/devices/system/cpu/smt/active
    cat /sys/devices/system/cpu/smt/control
    

**Remarque** : Si vous avez activé le démarrage sécurisé UEFI sur l'instance,
vous devrez recréer l'instance en désactivant cette fonction, exécuter la
commande ci-dessus (le démarrage sécurisé UEFI étant désactivé), puis activer
le démarrage sécurisé UEFI sur la nouvelle instance.

  2. Utilisez la nouvelle version de l'image COS.   

En plus de désactiver la technologie Hyper-Threading selon la procédure
décrite précédemment, vous devez également [ recréer vos instances
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=fr#publicimage) avec les images à jour répertoriées ci-dessus ou
avec une version plus récente (si disponible) des images Container-Optimized
OS, afin de bénéficier d'une protection complète contre les failles.

|  Moyen  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  Date de publication : 14-08-2018

**Dernière mise à jour : 20-08-2018 17:00 PST**

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

[ Intel a divulgué ](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) les failles CVE suivantes :

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) (pour [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (pour les systèmes d'exploitation et [ SMT ](https://en.wikipedia.org/wiki/Hyper-Threading) ) 
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

####  Impact sur Compute Engine

L'infrastructure hôte qui exécute Compute Engine et qui isole les charges de
travail client les unes des autres est protégée contre les attaques connues.

Les clients de Compute Engine sont invités à mettre à jour leurs images pour
éviter toute possibilité d'exploitation indirecte au sein de leurs
environnements invités. Cette mise à jour est particulièrement importante pour
les utilisateurs qui exécutent leurs propres services mutualisés sur des
machines virtuelles Compute Engine.

Pour mettre à jour les systèmes d'exploitation invités sur leurs instances,
les clients de Google Compute Engine peuvent procéder de l'une des façons
suivantes :

  * Utiliser des images publiques corrigées pour [ recréer des instances de VM existantes ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=fr#publicimage)
  * Sur les instances existantes, installer les correctifs procurés par le fournisseur du système d'exploitation et redémarrer les instances corrigées 

####  Images corrigées et ressources des fournisseurs

Vous trouverez ici des liens vers les informations sur les correctifs de
chaque fournisseur de système d'exploitation dès qu'elles seront disponibles,
y compris l'état de chaque faille CVE. Utilisez ces images pour recréer des
instances de VM. Les versions antérieures de ces images publiques n'incluent
pas ces correctifs et n'offrent aucune protection contre des attaques
potentielles :

  * Projet ` centos-cloud ` : 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * Projet ` coreos-cloud ` : 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * Projet ` cos-cloud ` : 
    * ` cos-stable-66-10452-110-0 `
    * ` cos-stable-67-10575-66-0 `
    * ` cos-beta-68-10718-81-0 `
    * ` cos-dev-69-10895-23-0 `
  * Projet ` debian-cloud ` : 
    * ` debian-9-stretch-v20180820 `
  * Projet ` rhel-cloud ` : 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * Projet ` rhel-sap-cloud ` : 
    * ` rhel-7-sap-apps-v20180814 `
    * ` rhel-7-sap-hana-v20180814 `
  * Projet ` suse-cloud ` : 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
    * ` sles-11-sp4-v20180816 `
  * Projet ` suse-sap-cloud ` : 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * Projet ` ubuntu-os-cloud ` : 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `
  * Projets ` windows-cloud ` ` gce-uefi-images ` et ` windows-sql-cloud ` : 
    * Toutes les [ images publiques ](https://cloud.google.com/compute/docs/images?hl=fr#os-compute-support) Windows Server et SQL Server à partir du numéro de version ` -v201800814 ` incluent les correctifs. 

|  Élevé  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  Date de publication : 06-08-2018

**Dernière mise à jour : 05-09-2018 17:00 PST**

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Mise à jour du 05/09/2018

La faille [ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) a été divulguée le 14/08/2018 par US-CERT.
Tout comme [ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) , il s'agit d'une faille réseau au niveau
du noyau, qui rend les attaques de déni de service (DoS) plus efficaces dans
les systèmes vulnérables. La principale différence réside dans le fait que la
faille CVE-2018-5391 est exploitable sur les connexions IP. Nous avons mis à
jour ce bulletin afin de traiter ces deux failles.

####  Description

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ("SegmentSmack") fait référence à une
faille réseau au niveau du noyau. Celle-ci rend les attaques de déni de
service (DoS) plus efficaces dans les systèmes vulnérables, via les connexions
TCP.

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ("FragmentSmack") fait référence à une
faille réseau au niveau du noyau. Celle-ci rend les attaques de déni de
service (DoS) plus efficaces dans les systèmes vulnérables, via les connexions
IP.

####  Impact sur Compute Engine

L'infrastructure hôte qui exécute les VM Compute Engine ne court aucun risque.
L'infrastructure réseau qui gère le trafic vers et depuis les VM Compute
Engine est protégée contre cette faille. Les VM Compute Engine qui ne font
qu'envoyer/recevoir du trafic réseau non approuvé via [ HTTP(S)
](https://cloud.google.com/load-balancing/docs/https/?hl=fr) , [ SSL
](https://cloud.google.com/load-balancing/docs/ssl/?hl=fr) ou les [
équilibreurs de charge TCP ](https://cloud.google.com/load-
balancing/docs/tcp/?hl=fr) sont protégées contre cette faille.

Les VM Compute Engine exécutant des systèmes d'exploitation non corrigés qui
envoient/reçoivent du trafic réseau non approuvé directement ou via les [
équilibreurs de charge réseau ](https://cloud.google.com/load-
balancing/docs/network/?hl=fr) sont vulnérables à cette attaque par déni de
service (DoS).

Pensez à mettre à jour vos instances de VM dès que des correctifs sont
disponibles pour leurs systèmes d'exploitation.

Les clients Compute Engine peuvent mettre à jour les systèmes d'exploitation
invités sur leurs instances en suivant l'une de ces méthodes :

  * Utiliser des images publiques corrigées pour [ recréer des instances de VM existantes ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=fr#publicimage) (voir la liste des images publiques corrigées ci-dessous) 
  * Sur les instances existantes, installer les correctifs procurés par le fournisseur du système d'exploitation et redémarrer les instances corrigées 

####  Images corrigées et ressources des fournisseurs

Vous trouverez ici des liens vers les informations sur les correctifs de
chaque fournisseur de système d'exploitation dès qu'elles seront disponibles.

  * Projet ` centos-cloud ` (CVE-2018-5390 uniquement) : 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * Projet ` coreos-cloud ` (CVE-2018-5390 et CVE-2018-5391) : 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * Projet ` cos-cloud ` (CVE-2018-5390 et CVE-2018-5391) : 
    * ` cos-stable-65-10323-98-0 `
    * ` cos-stable-66-10452-109-0 `
    * ` cos-stable-67-10575-65-0 `
    * ` cos-beta-68-10718-76-0 `
    * ` cos-dev-69-10895-16-0 `
  * Projet ` debian-cloud ` (CVE-2018-5390 et CVE-2018-5391) : 
    * ` debian-9-stretch-v20180814 `
  * Projet ` rhel-cloud ` (CVE-2018-5390 uniquement) : 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * Projet ` suse-cloud ` (CVE-2018-5390 et CVE-2018-5391) : 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
  * Projet ` suse-sap-cloud ` (CVE-2018-5390 et CVE-2018-5391) : 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * Project ` ubuntu-os-cloud ` (CVE-2018-5390 et CVE-2018-5391) : 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `

|  Élevé  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  Date de publication : 03-01-2018

**Dernière mise à jour : 21-05-2018 15:00 PST**

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Mise à jour du 21/05/2018

Les failles [ CVE-2018-3640 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-3640) et [ CVE-2018-3639
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639) , et leurs
variantes respectives 3a et 4, ont été [ divulguées par Intel
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00115.html) . Comme avec les trois premières variantes de Spectre et
Meltdown, l'infrastructure qui exécute les instances de VM Compute Engine est
protégée et les instances de VM client sont isolées et protégées les unes des
autres. De plus, Compute Engine prévoit de déployer les correctifs du
microcode d'Intel sur notre infrastructure, ce qui permettra aux clients
exécutant des charges de travail non approuvées ou mutualisées au sein d'une
même instance de VM d'appliquer d'autres protections au sein des VM dès
qu'elles seront mises à disposition par les fournisseurs du système
d'exploitation. Compute Engine déploiera les correctifs du microcode une fois
qu'Intel les aura certifiés et après que Compute Engine aura testé et validé
les correctifs pour notre environnement de production. Nous publierons un
calendrier plus précis et les mises à jour sur cette page dès qu'ils seront
disponibles.

####  Description

Ces failles CVE sont des variantes d'une nouvelle catégorie d'attaque
exploitant la technologie d'exécution spéculative disponible dans de nombreux
processeurs. Cette catégorie d'attaque peut fournir un accès non autorisé en
lecture seule aux données de la mémoire dans plusieurs cas.

Compute Engine a fait appel à la technologie de migration à chaud des VM pour
mettre à jour le système hôte et l'hyperviseur sans impact sur l'utilisateur,
sans intervalle de maintenance forcée et sans redémarrage en masse. Cependant,
tous les systèmes d'exploitation invités et toutes les versions doivent être
corrigés pour les protéger contre cette nouvelle catégorie d'attaque, quel que
soit l'emplacement d'exécution de ces systèmes.

Lisez [ cet article du blog Project Zero
](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-
with-side.html) pour obtenir des informations techniques complètes sur ce mode
d'attaque. Lisez [ cet article du blog Google sur la sécurité
](https://security.googleblog.com/2018/01/todays-cpu-vulnerability-what-you-
need.html) pour en savoir plus sur les protections de Google et connaître
toutes les informations spécifiques au produit.

####  Impact sur Compute Engine

L'infrastructure hôte qui exécute Compute Engine et qui isole les instances de
VM client les unes des autres est protégée contre les attaques connues. Nos
protections empêchent l'accès non autorisé à nos systèmes hôtes à partir
d'applications exécutées dans les instances de VM. Elles empêchent également
l'accès non autorisé entre les instances de VM exécutées sur le même système
hôte.

Pour empêcher tout accès non autorisé au sein de vos instances de VM, vous
devez mettre à jour les systèmes d'exploitation invités sur ces instances en
procédant de l'une des façons suivantes :

  * Utiliser des images publiques corrigées pour [ recréer vos instances de VM existantes ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=fr#publicimage) (voir la liste des images publiques corrigées ci-dessous) 
  * Sur les instances existantes, installer les correctifs procurés par le fournisseur du système d'exploitation et redémarrer les instances corrigées (consulter les liens vers les informations sur les correctifs de chaque fournisseur de système d'exploitation ci-dessous) 

####  Images corrigées et ressources des fournisseurs

**Remarque** : Les images corrigées peuvent ne pas inclure les correctifs pour
toutes les failles CVE répertoriées dans ce bulletin de sécurité. De plus,
différentes images peuvent inclure différentes méthodes de protection contre
ces types d'attaque. Renseignez-vous auprès du fournisseur de votre système
d'exploitation pour connaître les failles CVE traitées dans ses correctifs et
les méthodes de protection qu'il utilise.

  * Projet ` cos-cloud ` : inclut des correctifs contre les attaques Variante 2 ( [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715) ) et Variante 3 ( [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754) ). Google utilise [ Retpoline ](https://support.google.com/faqs/answer/7625886?hl=fr) dans ces images pour contrer les attaques Variante 2. 
    * ` cos-stable-63-10032-71-0 ` ou famille d'images ` cos-stable `
  * Projet ` centos-cloud ` : [ informations sur le correctif CentOS ](https://lwn.net/Alerts/CentOS/)
    * ` centos-7-v20180104 ` ou famille d'images ` centos-7 `
    * ` centos-6-v20180104 ` ou famille d'images ` centos-6 `
  * Projet ` coreos-cloud ` : [ informations sur le correctif CoreOS ](https://coreos.com/blog/container-linux-meltdown-patch)
    * ` coreos-stable-1576-5-0-v20180105 ` ou famille d'images ` coreos-stable `
    * ` coreos-beta-1632-1-0-v20180105 ` ou famille d'images ` coreos-beta `
    * ` coreos-alpha-1649-0-0-v20180105 ` ou famille d'images ` coreos-alpha `
  * Projet ` debian-cloud ` : [ informations sur le correctif Debian ](https://www.debian.org/security/#DSAS)
    * ` debian-9-stretch-v20180105 ` ou famille d'images ` debian-9 `
    * ` debian-8-jessie-v20180109 ` ou famille d'images ` debian-8 `
  * Projet ` rhel-cloud ` : [ informations sur le correctif RHEL ](https://access.redhat.com/security/vulnerabilities/speculativeexecution)
    * ` rhel-7-v20180104 ` ou famille d'images ` rhel-7 `
    * ` rhel-6-v20180104 ` ou famille d'images ` rhel-6 `
  * Projet ` suse-cloud ` : [ informations sur le correctif SUSE ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-v20180104 ` ou famille d'images ` sles-12 `
    * ` sles-11-sp4-v20180104 ` ou famille d'images ` sles-11 `
  * Projet ` suse-sap-cloud ` : [ informations sur le correctif SUSE ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-sap-v20180104 ` ou famille d'images ` sles-12-sp3-sap `
    * ` sles-12-sp2-sap-v20180104 ` ou famille d'images ` sles-12-sp2-sap `
  * Projet ` ubuntu-os-cloud ` : [ informations sur le correctif Ubuntu ](https://insights.ubuntu.com/2018/01/04/ubuntu-updates-for-the-meltdown-spectre-vulnerabilities/)
    * ` ubuntu-1710-artful-v20180109 ` ou famille d'images ` ubuntu-1710 `
    * ` ubuntu-1604-xenial-v20180109 ` ou famille d'images ` ubuntu-1604-lts `
    * ` ubuntu-1404-trusty-v20180110 ` ou famille d'images ` ubuntu-1404-lts `
  * Projets ` windows-cloud ` et ` windows-sql-cloud ` : 
    * Toutes les [ images publiques ](https://cloud.google.com/compute/docs/images?hl=fr#os-compute-support) Windows Server et SQL Server à partir du numéro de version ` -v20180109 ` incluent les correctifs. Toutefois, vous devez suivre les recommandations de Microsoft fournies dans le bulletin d'assistance [ Instructions Windows Server ](https://support.microsoft.com/en-gb/help/4072698/windows-server-guidance-to-protect-against-the-speculative-execution) pour activer et vérifier ces protections sur vos instances existantes et celles créées récemment. 

Utilisez ces images pour [ recréer vos instances de VM
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=fr#publicimage) . Les versions antérieures de ces images publiques
n'incluent pas ces correctifs et ne protègent pas contre les attaques
potentielles.

####  Correctifs des fournisseurs de matériel

NVIDIA fournit des pilotes corrigés pour protéger des attaques potentielles
les systèmes sur lesquels un logiciel pilote NVIDIA® est installé. Pour
connaître les versions de pilote corrigées, lisez le bulletin de sécurité sur
les [ mises à jour de sécurité pour les pilotes d'affichage des GPU NVIDIA
](http://nvidia.custhelp.com/app/answers/detail/a_id/4611) publié par NVIDIA.

####  Historique des révisions :

  * 21/05/2018 14h00 (PST) : ajout d'informations sur les deux nouvelles variantes divulguées le 21 mai 2018 
  * 10/01/2018 15h00 (PST) : ajout d'informations sur les images publiques corrigées Windows Server et SQL Server 
  * 10/01/2018 10h15 (PST) : ajout de plusieurs images Ubuntu à la liste des images publiques corrigées 
  * 10/01/2018 9h50 (PST) : ajout d'instructions sur les correctifs des fournisseurs de matériel 
  * Entre le 03/01/2018 et le 09/01/2018 : ajout de plusieurs révisions à la liste des images publiques corrigées 

|  Élevé  |

  * [ CVE-2017-5753 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5753)
  * [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715)
  * [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754)
  * [ CVE-2018-3640 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3640)
  * [ CVE-2018-3639 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639)

  
  
##  Date de publication : 02-10-2017

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

Les fonctionnalités de [ Dnsmasq
](http://www.thekelleys.org.uk/dnsmasq/doc.html) permettent de fournir des
services DNS et DHCP, de diffuser des annonces de routeurs et de démarrer le
réseau. Ce logiciel est généralement installé sur des systèmes aussi variés
que des distributions Linux pour ordinateur (comme Ubuntu), des routeurs
domestiques et des appareils IoT. Dnsmasq est couramment utilisé sur
l'Internet ouvert et en interne sur les réseaux privés.

Nous avons identifié sept problèmes distincts au cours de nos contrôles
internes réguliers de la sécurité. Après avoir déterminé la gravité de ces
problèmes, nous avons étudié leur impact et leur exploitabilité, puis nous
avons réalisé des démonstrations de faisabilité internes pour chacun d'entre
eux. Nous avons également travaillé avec le responsable de Dnsmasq, Simon
Kelly, au développement de correctifs appropriés et à l'atténuation des
problèmes.

Notre examen nous a permis de détecter trois exécutions potentielles de code à
distance, une fuite d'informations et trois failles de déni de service
affectant la dernière version sur le serveur Git du projet (en date du 5
septembre 2017).

Ces correctifs ont été appliqués en amont et ont été validés dans le [ dépôt
Git du projet ](http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=summary) .

####  Impact sur Compute Engine

Par défaut, Dnsmasq n'est installé que sur les images qui utilisent [
NetworkManager ](https://wikipedia.org/wiki/NetworkManager) et est désactivé.
Les images publiques Compute Engine suivantes disposent de Dnsmasq :

  * Ubuntu 16.04, 16.10 et 17.04 
  * CentOS 7 
  * RHEL 7 

Toutefois, Dnsmasq peut être installé sur d'autres images en tant que
dépendance pour d'autres packages. Nous vous recommandons de mettre à jour vos
instances Debian, Ubuntu, CentOS, RHEL, SLES et OpenSuse de manière à utiliser
la dernière image du système d'exploitation. CoreOS et Container-Optimized OS
ne sont pas affectés. Les images Windows ne sont pas concernées non plus.

Pour les instances fonctionnant sous Debian et Ubuntu, vous pouvez effectuer
une mise à jour en exécutant les commandes suivantes :

    
    
    
    sudo apt-get -y update
    
    
    
    sudo apt-get -y dist-upgrade

Pour les instances Red Hat Enterprise Linux et CentOS, exécutez la commande
suivante :

    
    
    
    sudo yum -y upgrade

Pour les images SLES et OpenSUSE, exécutez la commande suivante :

    
    
    
    sudo zypper up

Au lieu d'exécuter manuellement des commandes de mise à jour, vous pouvez [
recréer des instances de VM à l'aide des familles d'images
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=fr#publicimage) du système d'exploitation correspondant.

|  Élevé  |

  * [ CVE-2017-14491 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14491)
  * [ CVE-2017-14492 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14492)
  * [ CVE-2017-14493 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14493)
  * [ CVE-2017-14494 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14494)
  * [ CVE-2017-14495 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14495)
  * [ CVE-2017-14496 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14496)
  * [ CVE-2017-13704 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-13704)

  
  
##  Date de publication : 26-10-2016

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

La faille CVE-2016-5195 correspond à une condition de concurrence détectée
dans la manière dont le sous-système de mémoire du noyau Linux gère la faille
COW des mappages privés en lecture seule sur l'accès en écriture.

Un utilisateur local ne disposant pas de droits d'accès peut exploiter cette
faille pour obtenir un accès en écriture à des mappages de mémoire qui ne sont
autrement accessibles qu'en lecture seule, et ainsi s'accorder d'autres
autorisations sur le système.

Pour en savoir plus, consultez les [ questions fréquentes relatives à la
faille Dirty COW
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails) .

####  Impact sur Compute Engine

Toutes les distributions et versions de Linux sur Compute Engine sont
concernées. La plupart des instances téléchargent et installent
automatiquement un noyau plus récent. Cependant, un redémarrage est nécessaire
pour appliquer un correctif à votre système en cours d'exécution.

Les noyaux corrigés ont déjà été appliqués aux instances nouvelles ou recréées
basées sur les images Compute Engine suivantes.

  * ` centos-6-v20161026 `
  * ` centos-7-v20161025 `
  * ` coreos-alpha-1192-2-0-v20161021 `
  * ` coreos-beta-1185-2-0-v20161021 `
  * ` coreos-stable-1122-3-0-v20161021 `
  * ` debian-8-jessie-v20161020 `
  * ` rhel-6-v20161026 `
  * ` rhel-7-v20161024 `
  * ` sles-11-sp4-v20161021 `
  * ` sles-12-sp1-v20161021 `
  * ` ubuntu-1204-precise-v20161020 `
  * ` ubuntu-1404-trusty-v20161020 `
  * ` ubuntu-1604-xenial-v20161020 `
  * ` ubuntu-1610-yakkety-v20161020 `

|  Élevé  |  [ CVE-2016-5195
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails)  
  
##  Date de publication : 16-02-2016

**Dernière mise à jour : 22-02-2016**

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

La faille CVE-2015-7547 concerne l'outil de résolution DNS glibc côté client
qui rend le logiciel vulnérable à un dépassement de mémoire tampon basé sur
une pile lors de l'utilisation de la fonction ` getaddrinfo() ` de la
bibliothèque. Un pirate peut tirer parti d'un logiciel utilisant cette
fonction pour exploiter cette faille via des noms de domaines ou des serveurs
DNS qu'ils contrôlent, ou via une attaque de type "homme du milieu".

Pour en savoir plus, consultez notre [ blog sur la sécurité en ligne
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html) ou la base de données [ Common Vulnerabilities and
Exposures (CVE) ](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-7547)
.

####  Impact sur Compute Engine

**Mise à jour (22-02-2016) :**

Vous pouvez désormais recréer vos instances à l'aide des images CoreOS, SLES
et OpenSUSE suivantes :

  * ` coreos-alpha-962-0-0-v20160218 `
  * ` coreos-beta-899-7-0-v20160218 `
  * ` coreos-stable-835-13-0-v20160218 `
  * ` opensuse-13-2-v20160222 `
  * ` opensuse-leap-42-1-v20160222 `
  * ` sles-11-sp4-v20160222 `
  * ` sles-12-sp1-v20160222 `

**Mise à jour (17-02-2016) :**

Vous pouvez désormais effectuer une mise à jour sur les instances Ubuntu 12.04
LTS, Ubuntu 14.04 LTS et Ubuntu 15.10 en exécutant les commandes suivantes :

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Au lieu d'exécuter manuellement des commandes de mise à jour, vous pouvez
désormais recréer vos instances à l'aide des nouvelles images suivantes :

  * ` backports-debian-7-wheezy-v20160216 `
  * ` centos-6-v20160216 `
  * ` centos-7-v20160216 `
  * ` debian-7-wheezy-v20160216 `
  * ` debian-8-jessie-v20160216 `
  * ` rhel-6-v20160216 `
  * ` rhel-7-v20160216 `
  * ` ubuntu-1204-precise-v20160217a `
  * ` ubuntu-1404-trusty-v20160217a `
  * ` ubuntu-1510-wily-v20160217 `

Nous ne connaissons aucune méthode permettant d'exploiter cette faille via les
outils de résolution DNS de Compute Engine avec la configuration par défaut de
la bibliothèque glibc. Vous devez toutefois appliquer le correctif à vos
instances de machines virtuelles dès que possible. En effet, comme pour toute
nouvelle faille, les pirates peuvent découvrir de nouvelles méthodes
d'exploitation au fil du temps. Si vous avez activé EDNS0 (désactivé par
défaut), vous devez le désactiver jusqu'à ce que vous appliquiez le correctif
à vos instances.

**Bulletin initial :**

Votre distribution Linux est susceptible d'être vulnérable. Les clients
Compute Engine doivent mettre à jour les images d'OS de leurs instances pour
éliminer tout risque de faille si elles exécutent un système d'exploitation
Linux.

Pour les instances utilisant Debian, vous pouvez effectuer une mise à jour en
exécutant les commandes suivantes :

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Nous vous recommandons également d'installer le package [ UnattendedUpgrades
](https://wiki.debian.org/UnattendedUpgrades) pour vos instances Debian.

Pour les instances Red Hat Enterprise Linux :

  * ` user@my-instance:~$ sudo yum -y upgrade `
  * ` user@my-instance:~$ sudo reboot `

Nous mettrons à jour ce bulletin lorsque d'autres correctifs seront développés
pour cette faille par des mainteneurs de systèmes d'exploitation et lorsque
Compute Engine publiera des images d'OS mises à jour.

|  Élevé  |  [ CVE-2015-7547
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html)  
  
##  Date de publication : 19-03-2015

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

La faille CVE-2015-1427 concerne le moteur de script Groovy d' [ Elasticsearch
](https://www.elastic.co/products/elasticsearch) , avant la version 1.3.8 et
toutes les versions 1.4.x antérieures à la version 1.4.3. Elle permet aux
pirates distants de contourner le mécanisme de protection du bac à sable et
d'exécuter des commandes d'interface système arbitraires.

Pour en savoir plus, consultez le site [ National Vulnerability Database (NVD)
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427) ou la base
de données [ Common Vulnerabilities and Exposures (CVE)
](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-1427) .

####  Impact sur Compute Engine

Si vous exécutez Elasticsearch sur vos instances Compute Engine, vous devez
passer à Elasticsearch version 1.4.3 ou ultérieure. Si vous avez déjà mis à
jour votre logiciel Elasticsearch, vous êtes protégé contre cette faille.

Si vous n'avez pas installé Elasticsearch version 1.4.3 ou ultérieure, vous
pouvez [ effectuer une mise à niveau progressive
](http://www.elastic.co/guide/en/elasticsearch/reference/current/rolling-
upgrades.html) .

Si vous avez utilisé le [ déploiement par clic
](https://cloud.google.com/solutions/elasticsearch/click-to-deploy?hl=fr) pour
Elasticsearch dans la [ console Google Cloud Platform
](https://console.cloud.google.com/?hl=fr) , vous pouvez [ supprimer le
déploiement
](https://console.cloud.google.com/projectselector/deployments?hl=fr) pour
supprimer les instances exécutant Elasticsearch.

L'équipe Google Cloud Platform développe actuellement un correctif afin de
déployer une version mise à jour d'Elasticsearch. Toutefois, il n'est pas
encore disponible pour la fonctionnalité de déploiement par clic dans la [
console GCP ](https://console.cloud.google.com/?hl=fr) .

|  Élevé  |  [ CVE-2015-1427
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427)  
  
##  Date de publication : 29-01-2015

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

La faille [ CVE-2015-0235 (Ghost)
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235) concerne la
bibliothèque glibc.

Aucune action n'est requise de la part des clients App Engine, Cloud Storage,
BigQuery et Cloud SQL. Les serveurs de Google ont été mis à jour et sont
protégés contre cette faille.

Les clients Compute Engine peuvent avoir besoin de mettre à jour leurs images
d'OS.

####  Impact sur Compute Engine

Votre distribution Linux est susceptible d'être vulnérable. Les clients
Compute Engine doivent mettre à jour les images d'OS de leurs instances pour
éliminer cette faille si elles exécutent Debian 7, des rétroportages Debian 7,
Ubuntu 12.04 LTS, Red Hat Enterprise Linux, CentOS ou SUSE Linux Enterprise
Server 11 SP3.

Cette faille n'affecte pas Ubuntu 14.04 LTS, Ubuntu 14.10 ni SUSE Linux
Enterprise Server 12.

Nous vous recommandons de mettre à jour vos distributions Linux. Pour les
instances Debian 7, de rétroportages Debian 7 ou Ubuntu 12.04 LTS, vous pouvez
effectuer une mise à jour en exécutant les commandes suivantes :

  1. ` user@my-instance:~$ sudo apt-get update `
  2. ` user@my-instance:~$ sudo apt-get -y upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Pour les instances Red Hat Enterprise Linux ou CentOS :

  1. ` user@my-instance:~$ sudo yum -y upgrade `
  2. ` user@my-instance:~$ sudo reboot `

Pour les instances de SUSE Linux Enterprise Server 11 SP3 :

  1. ` user@my-instance:~$ sudo zypper --non-interactive up `
  2. ` user@my-instance:~$ sudo reboot `

Au lieu d'exécuter manuellement les commandes de mise à jour ci-dessus, les
utilisateurs peuvent désormais recréer leurs instances à l'aide des nouvelles
images suivantes :

  * ` debian-7-wheezy-v20150127 `
  * ` backports-debian-7-wheezy-v20150127 `
  * ` centos-6-v20150127 `
  * ` centos-7-v20150127 `
  * ` rhel-6-v20150127 `
  * ` rhel-7-v20150127 `
  * ` sles-11-sp3-v20150127 `
  * ` ubuntu-1204-precise-v20150127 `

####  Impact sur les VM gérées de Google

Les utilisateurs de VM gérées qui effectuent leur déploiement avec la commande
` gcloud preview app deploy ` doivent mettre à jour leurs conteneurs Docker de
base à l'aide de ` gcloud preview app setup-managed-vms ` et redéployer
chacune de leurs applications actives à l'aide de la commande ` gcloud preview
app deploy ` . Pour les utilisateurs qui effectuent leur déploiement à l'aide
de la commande ` appcfg ` , aucune action n'est requise, car la mise à jour
sera automatique.

|  Élevé  |  [ CVE-2015-0235
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235)  
  
##  Date de publication : 15-10-2014

**Dernière mise à jour : 17-10-2014**

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

La faille CVE-2014-3566 (ou POODLE) correspond à un problème dans la
conception de SSL version 3.0. Cette vulnérabilité permet à un pirate réseau
de calculer le texte brut des connexions sécurisées. Pour en savoir plus,
consultez notre [ article de blog
](http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-
exploiting-ssl-30.html) sur cette faille.

Aucune action n'est requise de la part des clients App Engine, Cloud Storage,
BigQuery et Cloud SQL. Les serveurs de Google ont été mis à jour et sont
protégés contre cette faille. Les clients Compute Engine doivent mettre à jour
leurs images d'OS.

####  Impact sur Compute Engine

**Mise à jour (17-10-2014) :**

Vous pouvez être vulnérable si vous utilisez SSLv3. Les clients Compute Engine
doivent mettre à jour les images d'OS de leurs instances pour éliminer tout
risque de faille.

Nous vous recommandons de mettre à jour vos distributions Linux. Pour les
instances utilisant Debian, vous pouvez effectuer une mise à jour en exécutant
les commandes suivantes :

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

Pour les instances CentOS :

    
    
    
    user@my-instance:~$ sudo yum -y upgrade
    user@my-instance:~$ sudo reboot

Au lieu d'exécuter manuellement les commandes de mise à jour ci-dessus, les
utilisateurs peuvent désormais recréer leurs instances à l'aide des nouvelles
images suivantes :

  * ` centos-6-v20141016 `
  * ` centos-7-v20141016 `
  * ` debian-7-wheezy-v20141017 `
  * ` backports-debian-7-wheezy-v20141017 `

Nous mettrons à jour le bulletin pour les images RHEL et SLES une fois que
nous disposerons de ces dernières. En attendant, les utilisateurs de RHEL
peuvent consulter directement le site de [ Red Hat
](https://access.redhat.com/articles/1232123) pour en savoir plus.

**Bulletin initial :**

Les clients Compute Engine doivent mettre à jour les images d'OS de leurs
instances pour éliminer tout risque de faille. Nous mettrons à jour ce
bulletin de sécurité en y ajoutant des instructions une fois que les nouvelles
images d'OS seront disponibles.

|  Moyen  |  [ CVE-2014-3566
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-3566)  
  
##  Date de publication : 24-09-2014

**Dernière mise à jour : 29-09-2014**

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

Le bug (CVE-2014-6271) dans l'interface système bash permet l'exécution de
code à distance basée sur l'analyse de toutes les variables d'environnement
contrôlées par le pirate. L'exploitation la plus probable de cette faille
s'effectue via des requêtes HTTP malveillantes adressées à des scripts CGI
exposés sur un serveur Web. Pour en savoir plus, consultez la [ description du
bug ](http://seclists.org/oss-sec/2014/q3/650) .

Les risques de bugs bash ont été limités dans les produits Google Cloud
Platform, à l'exception des images d'OS invités Compute Engine antérieures au
26/09/2014. Veuillez suivre les instructions ci-dessous pour limiter les
risques de bugs pour vos images Compute Engine.

####  Impact sur Compute Engine

Ce bug peut affecter pratiquement tous les sites Web utilisant des scripts
CGI. En outre, il est également susceptible de concerner les sites Web qui
reposent sur PHP, Perl, Python, SSI, Java, C ++, et des servlets similaires
qui invoquent des commandes d'interface système via des appels tels que `
popen ` , ` system ` , ` shell_exec ` ou des API semblables. Ce bug peut
également affecter les systèmes qui tentent d'accorder un accès contrôlé aux
utilisateurs restreints via des mécanismes tels que la limitation de commandes
SSH ou l'interface système bash limitée.

**Mise à jour (29-09-2014) :**

Au lieu d'exécuter manuellement les commandes de mise à jour ci-dessous, les
utilisateurs peuvent désormais recréer leurs instances à l'aide d'images qui
limitent les risques de failles liées au bug de sécurité bash, y compris [
CVE-2014-7169 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169)
, [ CVE-2014-6277
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277) , [
CVE-2014-6278 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278)
, [ CVE-2014-7186
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186) et [
CVE-2014-7187 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)
. Utilisez les nouvelles images suivantes pour recréer vos instances :

  * ` centos-6-v20140926 `
  * ` centos-7-v20140926 `
  * ` debian-7-wheezy-v20140926 `
  * ` backports-debian-7-wheezy-v20140926 `
  * ` rhel-6-v20140926 `

**Mise à jour (25-09-2014) :**

Les utilisateurs peuvent désormais choisir de recréer leurs instances au lieu
d'effectuer une mise à jour manuelle. Pour cela, utilisez les nouvelles images
suivantes qui contiennent des correctifs pour ce bug de sécurité :

  * ` backports-debian-7-wheezy-v20140924 `
  * ` debian-7-wheezy-v20140924 `
  * ` rhel-6-v20140924 `
  * ` centos-6-v20140924 `
  * ` centos-7-v20140924 `

Pour les images RHEL et SUSE, vous pouvez également effectuer des mises à jour
manuellement en exécutant les commandes suivantes sur vos instances :

    
    
    
    # RHEL instances
    user@my-instance:~$ sudo yum -y upgrade
    
    # SUSE instances
    user@my-instance:~$ sudo zypper --non-interactive up

**Bulletin initial :**

Nous vous recommandons de mettre à jour vos distributions Linux. Pour les
instances utilisant Debian, vous pouvez effectuer une mise à jour en exécutant
les commandes suivantes :

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    

Pour les instances CentOS :

    
    
    
    user@my-instance:~$ sudo yum -y upgrade

Pour obtenir des informations détaillées, consultez l'annonce relative à la
distribution Linux correspondante :

  * Correctifs d'origine : [ http://ftp.gnu.org/gnu/bash/ ](http://ftp.gnu.org/gnu/bash/) (voir la dernière entrée dans *-patches pour connaître la version appropriée) 
  * Debian : [ [SECURITY] [DSA 3032-1] bash security update ](https://lists.debian.org/debian-security-announce/2014/msg00220.html)
  * RHEL : 
    * [ RHSA-2014:1293-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00048.html)
    * [ RHSA-2014:1294-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00049.html)
  * CentOS 5 : [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020582.html)
  * CentOS 6 : [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020585.html)
  * CentOS 7 : [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020583.html)

|  Élevé  |  [ CVE-2014-7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) , [
CVE-2014-6271 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6271)
, [ CVE-2014-6277
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277) , [
CVE-2014-6278 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278)
, [ CVE-2014-7186
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186) , [
CVE-2014-7187 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)  
  
##  Date de publication : 25-07-2014

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

[ Elasticsearch Logstash ](http://www.elasticsearch.org/overview/logstash/)
est vulnérable à l'injection de commandes du système d'exploitation qui
peuvent permettre la modification et la divulgation non autorisées des
données. Un pirate peut envoyer des événements spécialement conçus à n'importe
quelle source de données Logstash, ce qui lui permet d'exécuter des commandes
avec les autorisations du processus Logstash.

####  Impact sur Compute Engine

Cette faille affecte toutes les instances Compute Engine exécutant des
versions d'Elasticsearch Logstash antérieures à la version 1.4.2 avec les
sorties zabbix ou nagios_nsca activées. Pour empêcher une attaque, vous pouvez
effectuer l'une des opérations suivantes :

  * Installer Logstash version 1.4.2 
  * Appliquer le correctif aux versions 1.3.x 
  * Désactiver les sorties ` zabbix ` et ` nagios_nsca `

Pour en savoir plus, consultez le [ blog de Logstash
](http://www.elasticsearch.org/blog/logstash-1-4-2/) .

Elasticsearch recommande également d' [ utiliser un pare-feu
](http://www.elasticsearch.org/blog/scripting-security/) pour empêcher l'accès
à distance d'adresses IP non fiables.

|  Élevé  |  [ CVE-2014-4326
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-4326)  
  
##  Date de publication : 18-06-2014

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

Nous souhaitons prendre un moment pour répondre aux éventuelles inquiétudes
des clients concernant la sécurité des conteneurs Docker lors de leur
exécution sur Google Cloud Platform. Cela inclut les clients qui utilisent nos
extensions Google App Engine compatibles avec les conteneurs Docker, les
machines virtuelles optimisées pour les conteneurs ou le programmeur Open
Source Kubernetes.

L'équipe Docker s'est efforcée avec succès de répondre au problème, et vous
pouvez consulter la solution proposée sur son blog en [ cliquant ici
](http://blog.docker.com/2014/06/docker-container-breakout-proof-of-concept-
exploit/) . Notez que, comme indiqué dans l'article du blog, le problème
identifié ne concerne que Docker 0.11, une ancienne version de préproduction.

Alors que nous pensons tous à la sécurité des conteneurs, nous souhaitons
souligner que, dans Google Cloud Platform, les solutions basées sur des
conteneurs d'applications Linux (en particulier les conteneurs Docker)
fonctionnent sur des VM complètes (Compute Engine). Bien que nous soutenions
les efforts de la communauté Docker pour renforcer la pile de conteneurs
d'applications Linux, nous reconnaissons que la technologie est encore
nouvelle et que la surface d'exposition est vaste. Nous pensons que, pour le
moment, les hyperviseurs complets (machines virtuelles) offrent une surface
d'exposition plus compacte et plus défendable. Les machines virtuelles ont été
conçues dès le départ pour isoler les charges de travail malveillantes, et
limiter les risques et l'impact d'un bug de code.

Nos clients peuvent se rassurer : la barrière de sécurité des hyperviseurs
complets les protège de tout code tiers potentiellement malveillant. Si nous
déterminons par la suite que la pile de conteneurs d'applications Linux est
suffisamment fiable pour traiter des charges de travail mutualisées, nous en
informerons la communauté. Pour l'instant, le conteneur d'applications Linux
ne remplace pas la machine virtuelle. Il s'agit d'un moyen de l'exploiter
davantage.

|  Faible  |  [ Article du blog de Docker
](http://blog.docker.com/2014/06/docker-container-breakout-proof-of-concept-
exploit/)  
  
##  Date de publication : 05-06-2014

**Dernière mise à jour : 09-06-2014**

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

Le problème OpenSSL concerne les messages ` ChangeCipherSpec ` qui ne sont pas
correctement associés à la machine en état handshake. Cela leur permet d'être
injectés tôt dans le cadre du handshake. Un pirate utilisant un handshake
spécialement conçu peut forcer l'utilisation de matériel de chiffrement
vulnérable sur les clients et les serveurs OpenSSL SSL/TLS. Cette faille peut
être exploitée par une attaque de type "homme du milieu" permettant au pirate
de déchiffrer et de modifier le trafic du client et du serveur attaqués.

Ce problème a été identifié par le code [ CVE-2014-0224
](https://www.openssl.org/news/secadv/20140605.txt) . L'équipe OpenSSL a
résolu le problème et a averti sa communauté de la nécessité de mettre à jour
OpenSSL.

####  Impact sur Compute Engine

Cette faille affecte toutes les instances Compute Engine qui utilisent
OpenSSL, y compris Debian, CentOS, Red Hat Enterprise Linux et SUSE Linux
Enterprise Server. Vous pouvez mettre à jour vos instances en les recréant
avec de nouvelles images ou en mettant à jour les packages manuellement.

**Mise à jour (09-06-2014)** : Pour mettre à jour vos instances exécutant SUSE
Linux Enterprise Server à l'aide de nouvelles images, recréez vos instances en
utilisant la version d'image suivante ou une version ultérieure :

  * ` sles-11-sp3-v20140609 `

**Post d'origine :**

Pour mettre à jour les instances Debian et CentOS à l'aide de nouvelles
images, recréez vos instances en utilisant l'une des versions d'images
suivantes ou une version ultérieure :

  * ` debian-7-wheezy-v20140605 `
  * ` backports-debian-7-wheezy-v20140605 `
  * ` centos-6-v20140605 `
  * ` rhel-6-v20140605 `

Pour mettre à jour manuellement OpenSSL sur vos instances, exécutez les
commandes suivantes pour mettre à jour les packages appropriés. Pour les
instances utilisant CentOS et RHEL, vous pouvez mettre à jour OpenSSL en
exécutant les commandes ci-dessous :

    
    
    
    user@my-instance:~$ sudo yum -y update
    user@my-instance:~$ sudo reboot

Pour les instances utilisant Debian, vous pouvez mettre à jour OpenSSL en
exécutant les commandes suivantes :

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

Pour les instances utilisant SUSE Linux Enterprise Server, vous pouvez vous
assurer qu'OpenSSL est à jour en exécutant les commandes suivantes :

    
    
    
    user@my-instance:~$ sudo zypper --non-interactive up
    user@my-instance:~$ sudo reboot

|  Moyen  |  [ CVE-2014-0224
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0224)  
  
##  Date de publication : 08-04-2014

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

Les mises en œuvre (1) TLS et (2) DTLS dans OpenSSL 1.0.1, avant la version
1.0.1g, ne gèrent pas correctement les paquets Heartbeat Extension. Cela
permet aux pirates distants d'obtenir des informations sensibles à partir de
la mémoire de processus via des paquets spécialement conçus qui déclenchent un
"buffer over-read" (ou bug Heartbleed) par la lecture des clés privées
associées à ` d1_both.c ` et ` t1_lib.c ` .

####  Impact sur Compute Engine

Cette faille affecte toutes les instances Debian, RHEL et CentOS de Compute
Engine qui ne disposent pas de la version la plus récente d'OpenSSL. Vous
pouvez mettre à jour vos instances en les recréant avec de nouvelles images ou
en mettant à jour les packages manuellement.

Pour mettre à jour vos instances à l'aide de nouvelles images, recréez vos
instances en utilisant l'une des versions d'images suivantes ou une version
ultérieure :

  * ` debian-7-wheezy-v20140408 `
  * ` backports-debian-7-wheezy-v20140408 `
  * ` centos-6-v20140408 `
  * ` rhel-6-v20140408 `

Pour mettre à jour manuellement OpenSSL sur vos instances, exécutez les
commandes suivantes pour mettre à jour les packages appropriés. Pour les
instances utilisant CentOS et RHEL, vous pouvez vous assurer qu'OpenSSL est à
jour en exécutant les commandes suivantes :

    
    
    
    user@my-instance:~$ sudo yum update
    user@my-instance:~$ sudo reboot

Pour les instances utilisant Debian, vous pouvez mettre à jour OpenSSL en
exécutant les commandes suivantes :

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get upgrade
    user@my-instance:~$ sudo reboot

Les instances utilisant SUSE Linux ne sont pas affectées.

**Mise à jour le 14 avril 2014** : Au vu de nouvelles recherches sur
l'extraction de clés à l'aide du bug Heartbleed, Compute Engine recommande à
ses clients de créer de nouvelles clés pour tous les services SSL concernés.

|  Moyen  |  [ CVE-2014-0160
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0160)  
  
##  Date de publication : 06-07-2013

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

**Remarque** : Cette faille concerne uniquement les noyaux qui sont devenus
obsolètes et ont été supprimés depuis la version v1 de l'API.

La faille associée au format de chaîne de la fonction ` b43_request_firmware `
du fichier ` drivers/net/wireless/b43/main.c ` du pilote de réseau sans fil
Broadcom B43 dans le noyau Linux, jusqu'à la version 3.9.4, permet aux
utilisateurs locaux d'obtenir des autorisations en exploitant l'accès root et
en incluant des indicateurs de chaîne de format dans un paramètre modprobe `
fwpostfix ` , ce qui entraîne la construction incorrecte d'un message
d'erreur.

####  Impact sur Compute Engine

Cette faille affecte tous les noyaux Compute Engine antérieurs à `
gcg-3.3.8-201305291443 ` . L'équipe Compute Engine a rendu obsolètes tous les
noyaux antérieurs, et vous recommande de mettre à jour vos instances et images
de manière à utiliser le noyau Compute Engine ` gce-v20130603 ` . La version `
gce-v20130603 ` contient le noyau ` gcg-3.3.8-201305291443 ` , qui intègre le
correctif pour cette faille.

Pour connaître la version de noyau utilisée par votre instance, procédez comme
suit :

  1. Connectez-vous en SSH à votre instance. 
  2. Exécutez la commande ` uname -r ` . 

|  Moyen  |  [ CVE-2013-2852
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2852)  
  
##  Date de publication : 06-07-2013

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

**Remarque** : Cette faille concerne uniquement les noyaux qui sont devenus
obsolètes et ont été supprimés depuis la version v1 de l'API.

La faille associée au format de chaîne de la fonction register_disk du fichier
` block/genhd.c ` dans le noyau Linux, jusqu'à la version 3.9.4, permet aux
utilisateurs locaux d'obtenir des autorisations en exploitant l'accès root et
en écrivant des indicateurs de chaînes de format dans `
/sys/module/md_mod/parameters/new_array ` afin de créer un nom d'appareil `
/dev/md ` spécial.

####  Impact sur Compute Engine

Cette faille affecte tous les noyaux Compute Engine antérieurs à `
gcg-3.3.8-201305291443 ` . L'équipe Compute Engine a rendu obsolètes tous les
noyaux antérieurs, et vous recommande de mettre à jour vos instances et images
de manière à utiliser le noyau Compute Engine ` gce-v20130603 ` . La version `
gce-v20130603 ` contient le noyau ` gcg-3.3.8-201305291443 ` , qui intègre le
correctif pour cette faille.

Pour connaître la version de noyau utilisée par votre instance, procédez comme
suit :

  1. Connectez-vous en SSH à votre instance. 
  2. Exécutez la commande ` uname -r ` . 

|  Moyen  |  [ CVE-2013-2851
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2851)  
  
##  Date de publication : 14-05-2014

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

**Remarque** : Cette faille concerne uniquement les noyaux qui sont devenus
obsolètes et ont été supprimés depuis la version v1 de l'API.

La fonction perf_swevent_init du fichier ` kernel/events/core.c ` dans le
noyau Linux, avant la version 3.8.9, utilise un type de données ` integer `
incorrect, ce qui permet aux utilisateurs locaux d'obtenir des autorisations
via un appel système ` perf_event_open ` spécial.

####  Impact sur Compute Engine

Cette faille affecte tous les noyaux Compute Engine antérieurs à `
gcg-3.3.8-201305211623 ` . L'équipe Compute Engine a rendu obsolètes tous les
noyaux antérieurs, et vous recommande de mettre à jour vos instances et images
de manière à utiliser le noyau Compute Engine ` gce-v20130521 ` . La version `
gce-v20130521 ` contient le noyau ` gcg-3.3.8-201305211623 ` , qui intègre le
correctif pour cette faille.

Pour connaître la version de noyau utilisée par votre instance, procédez comme
suit :

  1. Connectez-vous en SSH à votre instance. 
  2. Exécutez la commande ` uname -r ` . 

|  Élevé  |  [ CVE-2013-2094
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2094)  
  
##  Date de publication : 18-02-2013

Description  |  Niveau de gravité  |  Remarques  
---|---|---  
  
####  Description

**Remarque** : Cette faille concerne uniquement les noyaux qui sont devenus
obsolètes et ont été supprimés depuis la version v1 de l'API.

La condition de concurrence détectée dans la fonction ptrace des versions de
noyau Linux antérieures à la version 3.7.5 permet aux utilisateurs locaux
d'obtenir des autorisations via un appel système ` PTRACE_SETREGS ptrace `
dans une application spéciale.

####  Impact sur Compute Engine

Cette faille affecte les noyaux Compute Engine ` 2.6.x-gcg- _ <date> _ ` .
L'équipe Compute Engine a rendu obsolètes les noyaux 2.6.x, et vous recommande
de mettre à jour vos instances et images de manière à utiliser le noyau
Compute Engine ` gce-v20130225 ` . Cette version ` gce-v20130225 ` contient le
noyau ` 3.3.8-gcg-201302081521 ` , qui intègre le correctif pour cette faille.

Pour connaître la version de noyau utilisée par votre instance, procédez comme
suit :

  1. Connectez-vous en SSH à votre instance. 
  2. Exécutez la commande ` uname -r ` . 

|  Moyen  |  [ CVE-2013-0871
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-0871)

