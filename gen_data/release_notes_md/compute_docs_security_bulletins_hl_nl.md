#  Beveiligingsbulletins

Af en toe publiceren we beveiligingsbulletins over Compute Engine. Alle
beveiligingsbulletins voor Compute Engine worden hier beschreven.

[ Abonneren op de beveiligingsbulletins van Compute Engine.
![Abonneren](https://cloud.google.com/images/feed-icon.png?hl=nl)
](https://cloud.google.com/feeds/compute-engine-security-bulletins.xml?hl=nl)

##  Publicatiedatum: 18-06-2019

**Laatste update: 25-06-2019 om 06:30 uur PST**

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

Netflix heeft onlangs drie TCP-kwetsbaarheden in Linux-kernels bekendgemaakt:

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

Deze CVE's worden gezamenlijk [ NFLX-2019-001
](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-
party/2019-001.md) genoemd.

####  Impact op Compute Engine

De infrastructuur waarop Compute Engine wordt gehost, is beschermd tegen deze
kwetsbaarheid.

Compute Engine-VM's die ongepatchte Linux-besturingssystemen uitvoeren die
niet-vertrouwd netwerkverkeer verzenden/ontvangen, zijn gevoelig voor deze
DoS-aanval. We raden u aan deze VM-instanties te updaten zodra er patches
beschikbaar zijn voor de bijbehorende besturingssystemen.

Load balancers die TCP-verbindingen beëindigen, zijn gepatcht tegen deze
kwetsbaarheid. Compute Engine-instanties die via deze load balancers alleen
niet-vertrouwd verkeer ontvangen, zijn niet kwetsbaar. Voorbeelden zijn HTTP-
load balancers, SSL Proxy-load balancers en TCP Proxy-load balancers.

Load balancers in het netwerk en interne load balancers beëindigen geen TCP-
verbindingen. Niet-gepatchte Compute Engine-instanties die via deze load
balancers niet-vertrouwd verkeer ontvangen, zijn kwetsbaar.

####  Gepatchte images en resources van leveranciers

We bieden hier links naar patchinformatie van elke leverancier van
besturingssystemen zodra deze links beschikbaar zijn. Ook vermelden we de
status van iedere CVE. Eerdere versies van deze openbare images bevatten deze
patches niet en beperken het risico op aanvallen niet:

  * Project ` debian-cloud ` : 
    * ` debian-9-stretch-v20190618 `
  * Project ` centos-cloud ` : 
    * ` centos-6-v20190619 `
    * ` centos-7-v20190619 `
  * Project ` cos-cloud ` : 
    * ` cos-dev-77-12293-0-0 `
    * ` cos-beta-76-12239-21-0 `
    * ` cos-stable-75-12105-77-0 `
    * ` cos-73-11647-217-0 `
    * ` cos-69-10895-277-0 `
  * Project ` coreos-cloud ` : 
    * ` coreos-alpha-2163-2-1-v20190617 `
    * ` coreos-beta-2135-3-1-v20190617 `
    * ` coreos-stable-2079-6-0-v20190617 `
  * Project ` rhel-cloud ` : 
    * ` rhel-6-v20190618 `
    * ` rhel-7-v20190618 `
    * ` rhel-8-v20190618 `
  * Project ` rhel-sap-cloud ` : 
    * ` rhel-7-4-sap-v20190618 `
    * ` rhel-7-6-sap-v20190618 `
  * Project ` suse-cloud ` : 
    * ` sles-12-sp4-v20190617 `
    * ` sles-15-v20190617 `
  * Project ` suse-sap-cloud ` : 
    * ` sles-12-sp1-sap-v20190617 `
    * ` sles-12-sp2-sap-v20190617 `
    * ` sles-12-sp3-sap-v20190617 `
    * ` sles-12-sp4-sap-v20190617 `
    * ` sles-15-sap-v20190617 `
  * Project ` ubuntu-cloud ` : 
    * ` ubuntu-1604-xenial-v20190617 `
    * ` ubuntu-1804-bionic-v20190617 `
    * ` ubuntu-1810-cosmic-v20190618 `
    * ` ubuntu-1904-disco-v20190619 `
    * ` ubuntu-minimal-1604-xenial-v20190618 `
    * ` ubuntu-minimal-1804-bionic-v20190617 `
    * ` ubuntu-minimal-1810-cosmic-v20190618 `
    * ` ubuntu-minimal-1904-disco-v20190618 `

|  Gemiddeld  |

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

  
  
##  Publicatiedatum: 14-05-2019

**Laatste update: 20-05-2019 om 17:00 uur PST**

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

De volgende CVE's zijn door Intel bekendgemaakt:

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

Deze CVE's worden gezamenlijk 'Microarchitectural Data Sampling (MDS)'
genoemd. Via deze kwetsbaarheden kunnen gegevens worden blootgelegd via
interactie tussen speculatieve uitvoering en de microarchitecturale staat.

####  Impact op Compute Engine

**De hostinfrastructuur waarop Compute Engine wordt uitgevoerd, scheidt
productietaken van klanten van elkaar. U hoeft geen actie te ondernemen,
tenzij u niet-vertrouwde code binnen uw VM's uitvoert.**

Klanten die niet-vertrouwde code uitvoeren in hun eigen services met meerdere
tenants binnen virtuele machines van Compute Engine, raadplegen de aanbevolen
risicobeperking van de leverancier van hun gast-OS. Dit omvat mogelijk
functies voor risicobeperking voor microcode van Intel. We hebben passthrough-
toegang voor gasten geïmplementeerd in de nieuwe flush-functionaliteit.
Hieronder volgt een overzicht van de risicobeperkende maatregelen voor
veelvoorkomende gastimages.

####  Gepatchte images en resources van leveranciers

We bieden hier links naar patchinformatie van elke leverancier van
besturingssystemen zodra deze links beschikbaar zijn. Ook vermelden we de
status van iedere CVE. Gebruik deze images om VM-instanties opnieuw te maken.
Eerdere versies van deze openbare images bevatten deze patches niet en
beperken het risico op aanvallen niet:

  * Project ` centos-cloud ` : [ CESA-2019:1169 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023309.html) , [ CESA-2019:1168 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023314.html)
    * ` centos-6-v20190515 `
    * ` centos-7-v20190515 `
  * Project ` coreos-cloud ` : [ MDS-oplossingen voor CoreOS Container Linux ](https://coreos.com/os/docs/latest/disabling-smt.html)
    * ` coreos-stable-2079-4-0-v20190515 `
    * ` coreos-beta-2107-3-0-v20190515 `
    * ` coreos-alpha-2135-1-0-v20190515 `
  * Project ` cos-cloud `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
  * Project ` debian-cloud ` : [ DSA-4444 ](https://www.debian.org/security/2019/dsa-4444)
    * ` debian-9-stretch-v20190514 `
  * Project ` rhel-cloud ` : [ Red Hat MDS-informatieartikel ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-6-v20190515 `
    * ` rhel-7-v20190517 `
    * ` rhel-8-v20190515 `
  * Project ` rhel-sap-cloud ` : [ Red Hat MDS-informatieartikel ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-7-4-sap-v20190515 `
    * ` rhel-7-6-sap-v20190517 `
  * Project ` suse-cloud ` : [ SUSE MDS KB ](https://www.suse.com/support/kb/doc/?id=7023736)
    * ` sles-12-sp4-v20190520 `
    * ` sles-15-v20190520 `
  * Project ` suse-sap-cloud `
    * ` sles-12-sp4-sap-v20190520 `
    * ` sles-15-sap-v20190520 `
  * Project ` ubuntu-os-cloud ` : [ Ubuntu MDS Wiki ](https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/MDS)
    * ` ubuntu-1404-trusty-v20190514 `
    * ` ubuntu-1604-xenial-v20190514 `
    * ` ubuntu-1804-bionic-v20190514 `
    * ` ubuntu-1810-cosmic-v20190514 `
    * ` ubuntu-1904-disco-v20190514 `
    * ` ubuntu-minimal-1604-xenial-v20190514 `
    * ` ubuntu-minimal-1804-bionic-v20190514 `
    * ` ubuntu-minimal-1810-cosmic-v20190514 `
    * ` ubuntu-minimal-1904-disco-v20190514 `
  * Projecten ` windows-cloud ` en ` windows-sql-cloud ` : [ Microsoft ADV190013 ](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/ADV190013)
    * Alle openbare images van Windows Server en SQL Server met versienummer ` v20190514 ` . 
  * Project ` gce-uefi-images `
    * ` centos-7-v20190515 `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
    * ` rhel-7-v20190517 `
    * ` ubuntu-1804-bionic-v20190514 `
    * Alle openbare images van Windows Server met versienummer ` v20190514 ` . 

####  Container-Optimized OS

Als u Container-Optimized OS (COS, voor containers geoptimaliseerd
besturingssysteem) als uw gast-OS gebruikt en niet-vertrouwde productietaken
met meerdere tenants uitvoert in uw virtuele machine, raden we u aan het
volgende te doen:

  1. Schakel hyperthreading uit door ` nosmt ` in te stellen in de opdrachtregel van de kernel.   

Voor bestaande COS-VM's kunt u de ` grub.cfg ` als volgt aanpassen om de optie
` nosmt ` in te stellen en het systeem daarna opnieuw op te starten:

    
        
    # Run as root:
    dir="$(mktemp -d)"
    mount /dev/sda12 "${dir}"
    sed -i -e "s|cros_efi|cros_efi nosmt|g" "${dir}/efi/boot/grub.cfg"
    umount "${dir}"
    rmdir "${dir}"
    
    reboot

Voor het gemak kunt u het onderstaande script uitvoeren om dezelfde resultaten
te bereiken als met de bovenstaande opdrachten. We raden u aan dit script
onderdeel te maken van uw cloudconfiguraties, opstartscripts of
instantietemplates. Zo bent u er zeker van dat nieuwe VM's deze nieuwe
parameter gebruiken. Hieronder vindt u een voorbeeld van een cloudconfiguratie
die dit script uitvoert.

**Waarschuwing:** Wanneer deze opdracht voor het eerst wordt uitgevoerd, wordt
de instantie onmiddellijk opnieuw opgestart. Als u de opdracht daarna uitvoert
voor instanties waarvoor hyperthreading al uitgeschakeld is, heeft dit geen
gevolgen.

    
        
    # Run as root
    /bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)
    

U kunt dit als volgt opnemen in uw cloudconfiguratie:

    
        
    #cloud-config
    
    bootcmd:
    - /bin/bash -c "/bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)"
    

Als u wilt controleren of hyperthreading uitgeschakeld is voor uw instantie,
bekijkt u de uitvoer van ` /sys/devices/system/cpu/smt/active ` \- en `
/sys/devices/system/cpu/smt/control ` -bestanden. Hyperthreading is
uitgeschakeld als er ` 0 ` voor ` active ` en ` off ` voor ` control ` wordt
geretourneerd.

    
        
    cat /sys/devices/system/cpu/smt/active
    cat /sys/devices/system/cpu/smt/control
    

**Opmerking:** Als u UEFI Secure Boot voor uw instantie heeft ingeschakeld,
moet u uw instantie opnieuw maken terwijl UEFI Secure Boot uitgeschakeld is.
Vervolgens voert u de bovenstaande opdracht uit terwijl UEFI Secure Boot
uitgeschakeld is. Daarna schakelt u UEFI Secure Boot in voor uw nieuwe
instantie.

  2. Gebruik een nieuwe versie van de COS-image.   

Voor volledige bescherming tegen de kwetsbaarheid moet u niet alleen
hyperthreading uitschakelen zoals hierboven beschreven, maar ook [ uw
instanties opnieuw maken
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=nl#publicimage) met de geüpdatete images die hierboven worden
vermeld of nieuwere versies (indien beschikbaar) van Container-Optimized OS-
images.

|  Gemiddeld  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  Publicatiedatum: 14-08-2018

**Laatste update: 20-08-2018 om 17:00 uur PST**

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

De volgende CVE's zijn [ door Intel bekendgemaakt
](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) :

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) (voor [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (voor besturingssystemen en [ SMT ](https://en.wikipedia.org/wiki/Hyper-Threading) ) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (voor virtualisatie) 

Deze CVE's worden gezamenlijk 'L1 Terminal Fault (L1TF)' genoemd.

Deze L1TF-kwetsbaarheden maken misbruik van speculatieve uitvoering door de
configuratie van datastructuren op processorniveau aan te vallen. 'L1'
verwijst naar het Level-1 Data-cachegeheugen (L1D), een kleine resource in de
kern die wordt gebruikt om geheugentoegang te versnellen.

Lees de [ post op de Google Cloud-blog
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=nl) voor meer informatie over deze
kwetsbaarheden en de risicobeperkende maatregelen van Compute Engine.

####  Impact op Compute Engine

De hostinfrastructuur waarop Compute Engine wordt uitgevoerd en waarbinnen
productietaken van klanten van elkaar worden gescheiden, is beveiligd tegen
bekende aanvallen.

We raden Compute Engine-klanten aan hun images te updaten om indirect misbruik
binnen hun gastomgevingen te voorkomen. Dit is met name belangrijk voor
klanten die hun eigen services met meerdere tenants uitvoeren op virtuele
machines van Compute Engine.

Google Compute Engine-klanten kunnen de gastbesturingssystemen van hun
instanties op de volgende manieren updaten:

  * U kunt gepatchte openbare images gebruiken om [ bestaande VM-instanties opnieuw te maken ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=nl#publicimage) . 
  * Voor bestaande instanties kunt u patches installeren die beschikbaar zijn gesteld door de leverancier van het besturingssysteem. Vervolgens kunt u de gepatchte instanties opnieuw opstarten. 

####  Gepatchte images en resources van leveranciers

We bieden hier links naar patchinformatie van elke leverancier van
besturingssystemen zodra deze links beschikbaar zijn. Ook vermelden we de
status van CVE's. Gebruik deze images om VM-instanties opnieuw te maken.
Eerdere versies van deze openbare images bevatten deze patches niet en
beperken het risico op aanvallen niet:

  * Project ` centos-cloud ` : 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * Project ` coreos-cloud ` : 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * Project ` cos-cloud ` : 
    * ` cos-stable-66-10452-110-0 `
    * ` cos-stable-67-10575-66-0 `
    * ` cos-beta-68-10718-81-0 `
    * ` cos-dev-69-10895-23-0 `
  * Project ` debian-cloud ` : 
    * ` debian-9-stretch-v20180820 `
  * Project ` rhel-cloud ` : 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * Project ` rhel-sap-cloud ` : 
    * ` rhel-7-sap-apps-v20180814 `
    * ` rhel-7-sap-hana-v20180814 `
  * Project ` suse-cloud ` : 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
    * ` sles-11-sp4-v20180816 `
  * Project ` suse-sap-cloud ` : 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * Project ` ubuntu-os-cloud ` : 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `
  * Projecten ` windows-cloud ` ` gce-uefi-images ` en ` windows-sql-cloud ` : 
    * Alle [ openbare images ](https://cloud.google.com/compute/docs/images?hl=nl#os-compute-support) van Windows Server en SQL Server met versienummer ` -v201800814 ` en hoger bevatten patches. 

|  Hoog  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  Publicatiedatum: 06-08-2018

**Laatste update: 05-09-2018 om 17:00 uur PST**

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Update op 05-09-2018

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) is op 14-08-2018 bekendgemaakt door US-
CERT. Net als [ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) is dit een netwerkkwetsbaarheid op kernel-
niveau die de effectiviteit verhoogt van DoS-aanvallen (denial of service) op
kwetsbare systemen. Het belangrijkste verschil is dat er van CVE-2018-5391
misbruik kan worden gemaakt via IP-verbindingen. We hebben dit bulletin
geüpdatet en beide kwetsbaarheden erin opgenomen.

####  Beschrijving

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ('SegmentSmack') beschrijft een
netwerkkwetsbaarheid op kernel-niveau die de effectiviteit verhoogt van DoS-
aanvallen (denial of service) via TCP-verbindingen op kwetsbare systemen.

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ('FragmentSmack') beschrijft een
netwerkkwetsbaarheid op kernel-niveau die de effectiviteit verhoogt van DoS-
aanvallen (denial of service) via IP-verbindingen op kwetsbare systemen.

####  Impact op Compute Engine

De hostinfrastructuur waarop Compute Engine-VM's worden uitgevoerd, loopt geen
gevaar. De netwerkinfrastructuur waarop het verkeer van en naar Compute Engine
wordt uitgevoerd, is beschermd tegen deze kwetsbaarheid. Compute Engine-VM's
die alleen niet-vertrouwd netwerkverkeer verzenden/ontvangen via [ HTTP(S)
](https://cloud.google.com/load-balancing/docs/https/?hl=nl) , [ SSL
](https://cloud.google.com/load-balancing/docs/ssl/?hl=nl) of [ load balancers
met TCP ](https://cloud.google.com/load-balancing/docs/tcp/?hl=nl) , zijn
beschermd tegen deze kwetsbaarheid.

Compute Engine-VM's die ongepatchte besturingssystemen uitvoeren die
rechtstreeks niet-vertrouwd netwerkverkeer verzenden/ontvangen of die dit via
[ load balancers in het netwerk ](https://cloud.google.com/load-
balancing/docs/network/?hl=nl) doen, zijn gevoelig voor deze DoS-aanval.

We raden u aan uw VM-instanties te updaten zodra er patches beschikbaar zijn
voor de bijbehorende besturingssystemen.

Compute Engine-klanten kunnen de gastbesturingssystemen van hun instanties op
de volgende manieren updaten:

  * U kunt gepatchte openbare images gebruiken om [ bestaande VM-instanties opnieuw te maken ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=nl#publicimage) . Bekijk de lijst met gepatchte openbare images hieronder. 
  * Voor bestaande instanties kunt u patches installeren die beschikbaar zijn gesteld door de leverancier van het besturingssysteem. Vervolgens kunt u de gepatchte instanties opnieuw opstarten. 

####  Gepatchte images en resources van leveranciers

We bieden hier links naar patchinformatie van elke leverancier van
besturingssystemen zodra deze links beschikbaar zijn.

  * Project ` centos-cloud ` (alleen CVE-2018-5390): 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * Project ` coreos-cloud ` (CVE-2018-5390 en CVE-2018-5391): 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * Project ` cos-cloud ` (CVE-2018-5390 en CVE-2018-5391): 
    * ` cos-stable-65-10323-98-0 `
    * ` cos-stable-66-10452-109-0 `
    * ` cos-stable-67-10575-65-0 `
    * ` cos-beta-68-10718-76-0 `
    * ` cos-dev-69-10895-16-0 `
  * Project ` debian-cloud ` (CVE-2018-5390 en CVE-2018-5391): 
    * ` debian-9-stretch-v20180814 `
  * Project ` rhel-cloud ` (alleen CVE-2018-5390): 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * Project ` suse-cloud ` (CVE-2018-5390 en CVE-2018-5391): 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
  * Project ` suse-sap-cloud ` (CVE-2018-5390 en CVE-2018-5391): 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * Project ` ubuntu-os-cloud ` (CVE-2018-5390 en CVE-2018-5391): 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `

|  Hoog  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  Publicatiedatum: 03-01-2018

**Laatste update: 21-05-2018 om 15:00 uur PST**

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Update op 21-05-2018

[ CVE-2018-3640 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-3640) en [ CVE-2018-3639
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639) ,
respectievelijk varianten 3a en 4, zijn [ bekendgemaakt door Intel
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00115.html) . Net als bij de eerste drie varianten van Spectre en Meltdown
zijn er geen risico's voor de infrastructuur waarop VM-instanties van Compute
Engine worden uitgevoerd, worden VM-instanties van klanten van elkaar
gescheiden en blijven ze beschermd. Daarnaast zijn we van plan voor Compute
Engine de microcode-patches van Intel te implementeren in onze eigen
infrastructuur. Zo kunnen klanten die binnen één VM-instantie productietaken
met meerdere tenants of niet-vertrouwde productietaken uitvoeren, aanvullende
risicobeperkende maatregelen binnen VM's inschakelen wanneer deze beschikbaar
worden gesteld door leveranciers van besturingssystemen. Compute Engine
implementeert de microcode-patches nadat Intel deze heeft gecertificeerd en
nadat Compute Engine de patches heeft getest en goedgekeurd voor onze
productieomgeving. Op deze pagina bieden we uitgebreidere tijdlijnen en
updates zodra deze beschikbaar zijn.

####  Beschrijving

Deze CVE's zijn varianten van een nieuwe aanvalsklasse waarbij misbruik wordt
gemaakt van de speculatieve uitvoeringstechnologie waar veel processoren over
beschikken. Met deze aanvalsklasse kan er in bepaalde omstandigheden
ongeautoriseerde alleen-lezen toegang worden verkregen tot gegevens in het
geheugen.

Compute Engine heeft technologie voor live migratie van VM's gebruikt om het
hostsysteem en de hypervisor te updaten zonder gevolgen voor gebruikers,
zonder verplichte onderhoudsperioden en zonder VM's massaal opnieuw op te
starten. Alle gastbesturingssystemen en versies daarvan moeten worden gepatcht
om ze te beschermen tegen deze nieuwe aanvalsklasse, ongeacht waar deze
systemen worden uitgevoerd.

Lees de [ blogpost van Project Zero
](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-
with-side.html) voor alle technische informatie over deze aanvalsmethode. Lees
de post op de [ Google Security Blog
](https://security.googleblog.com/2018/01/todays-cpu-vulnerability-what-you-
need.html) voor alle informatie over de risicobeperkende maatregelen van
Google, inclusief alle productspecifieke informatie.

####  Impact op Compute Engine

De infrastructuur waarop Compute Engine wordt uitgevoerd en waarbinnen VM-
instanties van klanten van elkaar worden gescheiden, is beveiligd tegen
bekende aanvallen. Onze risicobeperkende maatregelen voorkomen
ongeautoriseerde toegang tot onze hostsystemen via apps die binnen VM-
instanties worden uitgevoerd. Deze risicobeperkende maatregelen voorkomen ook
ongeautoriseerde toegang tussen VM-instanties die op hetzelfde hostsysteem
worden uitgevoerd.

Als u ongeautoriseerde toegang binnen uw VM-instanties wilt voorkomen, moet u
de gastbesturingssystemen van deze instanties updaten op een van de volgende
manieren:

  * U kunt gepatchte openbare images gebruiken [ om uw bestaande VM-instanties opnieuw te maken ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=nl#publicimage) . Bekijk de lijst met gepatchte openbare images hieronder. 
  * Voor bestaande instanties kunt u patches installeren die ter distributie beschikbaar zijn gesteld door de leverancier van het besturingssysteem. Vervolgens kunt u de gepatchte instanties opnieuw opstarten. Hieronder vindt u links naar patchinformatie van elke leverancier van besturingssystemen. 

####  Gepatchte images en resources van leveranciers

**Opmerking:** Gepatchte images bevatten mogelijk geen fixes voor alle CVE's
die in dit beveiligingsbulletin worden vermeld. Daarnaast kunnen er voor
verschillende images verschillende methoden zijn om deze aanvalstypen te
voorkomen. Controleer bij de leverancier van uw besturingssysteem welke CVE's
zijn aangepakt in patches en welke preventiemethoden worden gebruikt.

  * Project ` cos-cloud ` : bevat patches die aanvallen van variant 2 ( [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715) ) en variant 3 [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754) ) voorkomen. Google heeft [ Retpoline ](https://support.google.com/faqs/answer/7625886?hl=nl) gebruikt in deze images om de risico's op aanvallen van variant 2 te beperken. 
    * ` cos-stable-63-10032-71-0 ` of imagereeks ` cos-stable `
  * Project ` centos-cloud ` : [ CentOS-patchinformatie ](https://lwn.net/Alerts/CentOS/)
    * ` centos-7-v20180104 ` of imagereeks ` centos-7 `
    * ` centos-6-v20180104 ` of imagereeks ` centos-6 `
  * Project ` coreos-cloud ` : [ CoreOS-patchinformatie ](https://coreos.com/blog/container-linux-meltdown-patch)
    * ` coreos-stable-1576-5-0-v20180105 ` of imagereeks ` coreos-stable `
    * ` coreos-beta-1632-1-0-v20180105 ` of imagereeks ` coreos-beta `
    * ` coreos-alpha-1649-0-0-v20180105 ` of imagereeks ` coreos-alpha `
  * Project ` debian-cloud ` : [ Debian-patchinformatie ](https://www.debian.org/security/#DSAS)
    * ` debian-9-stretch-v20180105 ` of imagereeks ` debian-9 `
    * ` debian-8-jessie-v20180109 ` of imagereeks ` debian-8 `
  * Project ` rhel-cloud ` : [ RHEL-patchinformatie ](https://access.redhat.com/security/vulnerabilities/speculativeexecution)
    * ` rhel-7-v20180104 ` of imagereeks ` rhel-7 `
    * ` rhel-6-v20180104 ` of imagereeks ` rhel-6 `
  * Project ` suse-cloud ` : [ SUSE-patchinformatie ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-v20180104 ` of imagereeks ` sles-12 `
    * ` sles-11-sp4-v20180104 ` of imagereeks ` sles-11 `
  * Project ` suse-sap-cloud ` : [ SUSE-patchinformatie ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-sap-v20180104 ` of imagereeks ` sles-12-sp3-sap `
    * ` sles-12-sp2-sap-v20180104 ` of imagereeks ` sles-12-sp2-sap `
  * Project ` ubuntu-os-cloud ` : [ Ubuntu-patchinformatie ](https://insights.ubuntu.com/2018/01/04/ubuntu-updates-for-the-meltdown-spectre-vulnerabilities/)
    * ` ubuntu-1710-artful-v20180109 ` of imagereeks ` ubuntu-1710 `
    * ` ubuntu-1604-xenial-v20180109 ` of imagereeks ` ubuntu-1604-lts `
    * ` ubuntu-1404-trusty-v20180110 ` of imagereeks ` ubuntu-1404-lts `
  * Projecten ` windows-cloud ` en ` windows-sql-cloud ` : 
    * Alle [ openbare images ](https://cloud.google.com/compute/docs/images?hl=nl#os-compute-support) van Windows Server en SQL Server met versienummer ` -v20180109 ` en hoger bevatten patches. U moet wel de aanbevolen acties uitvoeren die Microsoft beschrijft in het supportbulletin met [ Windows Server-richtlijnen ](https://support.microsoft.com/en-gb/help/4072698/windows-server-guidance-to-protect-against-the-speculative-execution) . Zo kunt u deze risicobeperkende maatregelen inschakelen en verifiëren op uw bestaande machines en op nieuwe machines die u maakt. 

Gebruik deze images om [ uw VM-instanties opnieuw te maken
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=nl#publicimage) . Eerdere versies van deze openbare images
bevatten deze patches niet en beperken het risico op aanvallen niet.

####  Patches van hardwareleveranciers

NVIDIA biedt gepatchte stuurprogramma's om het risico te beperken op aanvallen
tegen systemen waarop NVIDIA®-stuurprogrammasoftware is geïnstalleerd. In het
NVIDIA-beveiligingsbulletin met [ beveiligingsupdates voor de NVIDIA GPU
Display Driver ](http://nvidia.custhelp.com/app/answers/detail/a_id/4611)
leest u welke stuurprogrammaversies zijn gepatcht.

####  Revisiegeschiedenis:

  * 21-05-2018 14:00 uur PST: informatie toegevoegd over twee nieuwe varianten die op 21 mei 2018 zijn bekendgemaakt. 
  * 10-01-2018 15:00 uur PST: informatie toegevoegd over gepatchte openbare images van Windows Server en SQL Server. 
  * 10-01-2018 10:15 uur PST: meerdere Ubuntu-images toegevoegd aan de lijst met gepatchte openbare images. 
  * 10-01-2018 09:50 uur PST: advies toegevoegd voor patches van hardwareleveranciers. 
  * 03-01-2018 t/m 09-01-2018: meerdere revisies uitgevoerd in de lijst met gepatchte openbare images. 

|  Hoog  |

  * [ CVE-2017-5753 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5753)
  * [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715)
  * [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754)
  * [ CVE-2018-3640 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3640)
  * [ CVE-2018-3639 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639)

  
  
##  Publicatiedatum: 02-10-2017

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

[ Dnsmasq ](http://www.thekelleys.org.uk/dnsmasq/doc.html) biedt
functionaliteit voor het aanbieden van DNS, DHCP, routeradvertenties en
netwerk opstarten. Deze software wordt in verschillende systemen
geïnstalleerd, zoals Linux-desktopdistributies (zoals Ubuntu), routers voor
thuisgebruik en IoT-apparaten. Dnsmasq wordt veel gebruikt, zowel op het open
internet als intern in privénetwerken.

Tijdens onze reguliere interne veiligheidsbeoordelingen ontdekte Google zeven
afzonderlijke problemen. Nadat we de ernst van deze problemen hadden
vastgesteld, hebben we de gevolgen en de mogelijkheden tot misbruik ervan
onderzocht en vervolgens voor elk probleem een interne proof of concept
geproduceerd. We hebben ook met de beheerder van Dnsmasq, Simon Kelly,
samengewerkt om de juiste patches te maken en het probleem te verhelpen.

Tijdens onze beoordeling ontdekte het team drie mogelijke externe code-
uitvoeringen, één informatielek en drie denial-of-service-kwetsbaarheden met
gevolgen voor de nieuwste versie op de project git-server vanaf 5 september
2017.

Deze patches worden geladen en toegewezen aan de [ Git-opslagplaats van het
project ](http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=summary) .

####  Impact op Compute Engine

Standaard wordt Dnsmasq alleen geïnstalleerd in images die [ NetworkManager
](https://wikipedia.org/wiki/NetworkManager) gebruiken en is de software niet
actief. Dnsmasq is geïnstalleerd voor de volgende openbare Compute Engine-
images:

  * Ubuntu 16.04, 16.10, 17.04 
  * CentOS 7 
  * RHEL 7 

In andere images kan Dnsmasq zijn geïnstalleerd als een afhankelijkheid voor
andere pakketten. We raden u aan om uw Debian-, Ubuntu-, CentOS-, RHEL-, SLES-
en OpenSUSE-instanties bij te werken zodat de nieuwste besturingssysteemimages
worden gebruikt. CoreOS en Container-Optimized OS worden niet beïnvloed.
Windows-images worden ook niet beïnvloed.

Voor instanties met Debian en Ubuntu kunt u een update uitvoeren door de
volgende opdrachten in uw instantie uit te voeren:

    
    
    
    sudo apt-get -y update
    
    
    
    sudo apt-get -y dist-upgrade

Voor Red Hat Enterprise Linux- en CentOS-instanties voert u het volgende uit:

    
    
    
    sudo yum -y upgrade

Voor SLES- en OpenSUSE-images voert u het volgende uit:

    
    
    
    sudo zypper up

Als alternatief voor het uitvoeren van de handmatige updateopdrachten kunt u [
VM-instanties opnieuw maken met behulp van de imagereeksen
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=nl#publicimage) van het betreffende besturingssysteem.

|  Hoog  |

  * [ CVE-2017-14491 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14491)
  * [ CVE-2017-14492 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14492)
  * [ CVE-2017-14493 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14493)
  * [ CVE-2017-14494 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14494)
  * [ CVE-2017-14495 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14495)
  * [ CVE-2017-14496 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14496)
  * [ CVE-2017-13704 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-13704)

  
  
##  Publicatiedatum: 26-10-2016

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

CVE-2016-5195 is een race condition voor de manier waarop het
geheugensubsysteem van de Linux-kernel de breuk van de alleen-lezen COW-
situatie voor privétoewijzingen bij schrijftoegang heeft afgehandeld.

Een onbevoegde lokale gebruiker kan deze fout gebruiken om schrijftoegang te
krijgen tot geheugentoewijzingen die anders alleen-lezen zijn en zo zijn
rechten op het systeem te vergroten.

Zie de [ Veelgestelde vragen over Dirty COW
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails)
voor meer informatie.

####  Impact op Compute Engine

Alle Linux-distributies en -versies op Compute Engine worden beïnvloed. De
meeste instanties zullen automatisch een nieuwere kernel downloaden en
installeren. Er is wel een herstart vereist om uw actieve systeem te patchen.

Bij nieuwe of opnieuw gemaakte instanties die op de volgende Compute Engine-
images zijn gebaseerd, zijn al gepatchte kernels geïnstalleerd.

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

|  Hoog  |  [ CVE-2016-5195
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails)  
  
##  Publicatiedatum: 16-02-2016

**Laatste update: 22-02-2016**

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

CVE-2015-7547 is een kwetsbaarheid waarbij de glibc DNS-client-side-resolver
software kwetsbaar maakt voor een stack-gebaseerde bufferoverloop bij gebruik
van de bibliotheekfunctie ` getaddrinfo() ` . Een aanvaller kan gebruikmaken
van software die de functie gebruikt om deze kwetsbaarheid te misbruiken met
door aanvallers bestuurde domeinnamen, door aanvallers bestuurde DNS-servers
of door een Man-in-the-Middle-aanval.

Zie voor meer informatie de [ Google Security Blog over online beveiliging
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html) of de database [ Common Vulnerabilities and Exposures
(CVE) ](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-7547) .

####  Impact op Compute Engine

**Update (22-02-2016):**

U kunt nu uw instanties opnieuw maken met behulp van de volgende CoreOS-,
SLES- en OpenSUSE-images:

  * ` coreos-alpha-962-0-0-v20160218 `
  * ` coreos-beta-899-7-0-v20160218 `
  * ` coreos-stable-835-13-0-v20160218 `
  * ` opensuse-13-2-v20160222 `
  * ` opensuse-leap-42-1-v20160222 `
  * ` sles-11-sp4-v20160222 `
  * ` sles-12-sp1-v20160222 `

**Update (17-02-2016):**

U kunt nu een update uitvoeren op Ubuntu 12.04 LTS-, Ubuntu 14.04 LTS- en
Ubuntu 15.10-instanties door de volgende opdrachten uit te voeren:

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Als alternatief voor het uitvoeren van de handmatige updateopdrachten, kunt u
nu de betreffende instanties opnieuw maken met de volgende nieuwe images:

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

We kennen geen methoden die deze kwetsbaarheid kunnen misbruiken via DNS-
resolvers van Compute Engine met de standaard glibc-configuratie. U moet wel
uw virtuele machine-instanties nog steeds zo snel mogelijk patchen, aangezien,
zoals bij elke nieuwe kwetsbaarheid, nieuwe misbruikmethoden in de loop van de
tijd ontdekt kunnen worden. Als u edns0 heeft ingeschakeld (standaard
uitgeschakeld), moet u dit uitschakelen totdat uw instanties zijn gepatcht.

**Oorspronkelijk bulletin:**

Uw Linux-distributie is mogelijk kwetsbaar. Klanten van Compute Engine moeten
de OS-images van hun instanties updaten om deze kwetsbaarheid te voorkomen als
ze een Linux OS gebruiken.

Voor instanties met Debian kunt u een update uitvoeren met behulp van de
volgende opdrachten in uw instantie:

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

We raden ook aan om [ UnattendedUpgrades
](https://wiki.debian.org/UnattendedUpgrades) voor uw Debian-instanties te
installeren.

Voor Red Hat Enterprise Linux-instanties:

  * ` user@my-instance:~$ sudo yum -y upgrade `
  * ` user@my-instance:~$ sudo reboot `

We zullen dit bulletin blijven updaten zolang beheerders van andere
besturingssystemen patches voor deze kwetsbaarheid publiceren en Compute
Engine geüpdatete OS-images publiceert.

|  Hoog  |  [ CVE-2015-7547
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html)  
  
##  Publicatiedatum: 19-03-2015

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

CVE-2015-1427 is een kwetsbaarheid waarbij de Groovy scripting engine in [
Elasticsearch ](https://www.elastic.co/products/elasticsearch) van vóór versie
1.3.8 en 1.4.x-versies van vóór 1.4.3 externe aanvallers toestaat om het
sandbox-beveiligingsmechanisme te omzeilen en willekeurige shell-opdrachten
uit te voeren.

Zie de [ National Vulnerability Database (NVD)
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427) of de
database [ Common Vulnerabilities and Exposures (CVE)
](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-1427) voor meer
informatie.

####  Impact op Compute Engine

Als u Elasticsearch uitvoert op uw Compute Engine-instanties, moet u uw
Elasticsearch-versie upgraden naar 1.4.3 of hoger. Als u uw Elasticsearch-
software al heeft geüpgraded, bent u beschermd tegen deze kwetsbaarheid.

Als u Elasticsearch 1.4.3 of hoger niet heeft geüpgraded, kunt u [ een
doorlopende upgrade uitvoeren
](http://www.elastic.co/guide/en/elasticsearch/reference/current/rolling-
upgrades.html) .

Als u Elasticsearch heeft geïmplementeerd met [ klik om te implementeren
](https://cloud.google.com/solutions/elasticsearch/click-to-deploy?hl=nl) in
de [ Google Cloud Platform Console ](https://console.cloud.google.com/?hl=nl)
, kunt u [ de implementatie verwijderen
](https://console.cloud.google.com/projectselector/deployments?hl=nl) om
instanties met Elasticsearch te verwijderen.

Het Google Cloud Platform-team werkt aan een oplossing om een geüpdatete
versie van Elasticsearch te implementeren. De oplossing is echter nog niet
beschikbaar voor de functie 'Klik om te implementeren' in de [ GCP-console
](https://console.cloud.google.com/?hl=nl) .

|  Hoog  |  [ CVE-2015-1427
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427)  
  
##  Publicatiedatum: 29-01-2015

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

[ CVE-2015-0235 (Ghost)
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235) is een
kwetsbaarheid in de glibc-bibliotheek.

App Engine-, Cloud Storage-, BigQuery- en Cloud SQL-klanten hoeven geen actie
te ondernemen. De servers van Google zijn geüpdatet en beschermd tegen deze
kwetsbaarheid.

Klanten van Compute Engine moeten mogelijk hun OS-images updaten.

####  Impact op Compute Engine

Uw Linux-distributie is mogelijk kwetsbaar. Compute Engine-klanten moeten de
OS-images van hun instanties updaten om deze kwetsbaarheid weg te nemen als ze
Debian 7, Debian 7 backports, Ubuntu 12.04 LTS, Red Hat Enterprise Linux,
CentOS of SUSE Linux Enterprise Server 11 SP3 gebruiken.

Deze kwetsbaarheid heeft geen invloed op Ubuntu 14.04 LTS, Ubuntu 14.10 of
SUSE Linux Enterprise Server 12.

We raden u aan uw Linux-distributies te upgraden. Voor instanties met Debian
7, Debian 7 backports of Ubuntu 12.04 LTS kunt u een update uitvoeren met de
volgende opdrachten in uw instantie:

  1. ` user@my-instance:~$ sudo apt-get update `
  2. ` user@my-instance:~$ sudo apt-get -y upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Voor Red Hat Enterprise Linux- of CentOS-instanties:

  1. ` user@my-instance:~$ sudo yum -y upgrade `
  2. ` user@my-instance:~$ sudo reboot `

Voor SUSE Linux Enterprise Server 11 SP3-instanties:

  1. ` user@my-instance:~$ sudo zypper --non-interactive up `
  2. ` user@my-instance:~$ sudo reboot `

Als alternatief voor het uitvoeren van de bovenstaande handmatige
updateopdrachten, kunnen gebruikers nu hun instanties opnieuw maken met de
volgende nieuwe images:

  * ` debian-7-wheezy-v20150127 `
  * ` backports-debian-7-wheezy-v20150127 `
  * ` centos-6-v20150127 `
  * ` centos-7-v20150127 `
  * ` rhel-6-v20150127 `
  * ` rhel-7-v20150127 `
  * ` sles-11-sp3-v20150127 `
  * ` ubuntu-1204-precise-v20150127 `

####  Gevolgen voor via Google beheerde VM's

Gebruikers van beheerde VM's die ` gcloud preview app deploy ` gebruiken,
moeten hun basisdockercontainers updaten met ` gcloud preview app setup-
managed-vms ` en al hun actieve apps opnieuw implementeren met behulp van `
gcloud preview app deploy ` . Gebruikers die met ` appcfg ` implementeren,
hoeven niets te doen en worden automatisch geüpgraded.

|  Hoog  |  [ CVE-2015-0235
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235)  
  
##  Publicatiedatum: 15-10-2014

**Laatste update: 17-10-2014**

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

CVE-2014-3566 (ook bekend als POODLE) is een kwetsbaarheid in het ontwerp van
SSL-versie 3.0. Met deze kwetsbaarheid kan de niet-versleutelde tekst van
beveiligde verbindingen worden berekend door een netwerkaanvaller. Zie onze [
blogpost ](http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-
exploiting-ssl-30.html) over deze kwetsbaarheid voor meer informatie.

App Engine-, Cloud Storage-, BigQuery- en Cloud SQL-klanten hoeven geen actie
te ondernemen. De servers van Google zijn geüpdatet en beschermd tegen deze
kwetsbaarheid. Klanten van Compute Engine moeten hun OS-images updaten.

####  Impact op Compute Engine

**Geüpdatet (17-10-2014):**

U kunt kwetsbaar zijn als u SSLv3 gebruikt. Compute Engine-klanten moeten de
OS-images van hun instanties updaten om deze kwetsbaarheid te verhelpen.

We raden u aan uw Linux-distributies te upgraden. Voor instanties met Debian
kunt u een update uitvoeren met behulp van de volgende opdrachten in uw
instantie:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

Voor CentOS-instanties:

    
    
    
    user@my-instance:~$ sudo yum -y upgrade
    user@my-instance:~$ sudo reboot

Als alternatief voor het uitvoeren van de bovenstaande handmatige
updateopdrachten kunnen gebruikers nu hun instanties opnieuw maken met de
volgende nieuwe images:

  * ` centos-6-v20141016 `
  * ` centos-7-v20141016 `
  * ` debian-7-wheezy-v20141017 `
  * ` backports-debian-7-wheezy-v20141017 `

We zullen het bulletin updaten voor RHEL- en SLES-images zodra we de images
hebben. In de tussentijd kunnen RHEL-gebruikers meer informatie vinden op de
site van [ Red Hat ](https://access.redhat.com/articles/1232123) .

**Oorspronkelijk bulletin:**

Compute Engine-klanten moeten de OS-images van hun instanties updaten om deze
kwetsbaarheid te verhelpen. We zullen dit beveiligingsbulletin updaten met
instructies zodra er nieuwe OS-images beschikbaar zijn.

|  Gemiddeld  |  [ CVE-2014-3566
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-3566)  
  
##  Publicatiedatum: 24-09-2014

**Laatste update: 29-09-2014**

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

Er zit een bug in Bash (CVE-2014-6271) waarmee externe code kan worden
uitgevoerd op basis van parsering van door aanvallers gecontroleerde
omgevingsvariabelen. De meest waarschijnlijke vorm van misbruik is via
kwaadwillige HTTP-verzoeken die worden gedaan aan CGI-scripts die op een
webserver worden weergegeven. Bekijk de [ bugbeschrijving
](http://seclists.org/oss-sec/2014/q3/650) voor meer informatie.

De Bash-bugs zijn verholpen voor Google Cloud Platform-producten, behalve voor
Compute Engine gast-OS-images die dateren van vóór 26-09-2014. Zie hieronder
voor stappen om de bugs voor uw Compute Engine-images op te lossen.

####  Impact op Compute Engine

Deze bug kan effect hebben op vrijwel alle websites die CGI-scripts gebruiken.
Bovendien zal die waarschijnlijk effect hebben op websites die afhankelijk
zijn van PHP, Perl, Python, SSI, Java, C++ en soortgelijke servlets die shell-
opdrachten zullen oproepen via aanroepen zoals ` popen ` , ` system ` , `
shell_exec ` of vergelijkbare API's. De bug kan ook effect hebben op systemen
die proberen gecontroleerde inlogtoegang te verlenen aan beperkte gebruikers
via mechanismen zoals SSH-opdrachtbeperking of de Bash-beperkte shell.

**Update (29-09-2014):**

Als alternatief voor het uitvoeren van de handmatige updateopdrachten
hieronder, kunnen gebruikers nu hun instanties opnieuw maken met images die
extra kwetsbaarheden in verband met de Bash-beveiligingsbug verminderen,
waaronder [ CVE-2014-7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) , [
CVE-2014-6277 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277)
, [ CVE-2014-6278
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278) , [
CVE-2014-7186 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186)
en [ CVE-2014-7187
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187) . Gebruik de
volgende nieuwe images om uw instanties opnieuw te maken:

  * ` centos-6-v20140926 `
  * ` centos-7-v20140926 `
  * ` debian-7-wheezy-v20140926 `
  * ` backports-debian-7-wheezy-v20140926 `
  * ` rhel-6-v20140926 `

**Update (25-09-2014):**

Gebruikers kunnen nu kiezen om hun instanties opnieuw te maken in plaats van
een handmatige update uit te voeren. Als u uw instanties opnieuw wilt maken,
gebruikt u de volgende nieuwe images die oplossingen voor deze beveiligingsbug
bevatten:

  * ` backports-debian-7-wheezy-v20140924 `
  * ` debian-7-wheezy-v20140924 `
  * ` rhel-6-v20140924 `
  * ` centos-6-v20140924 `
  * ` centos-7-v20140924 `

Voor RHEL- en SUSE-images kunt u ook handmatig updates uitvoeren met behulp
van de volgende opdrachten in uw instanties:

    
    
    
    # RHEL instances
    user@my-instance:~$ sudo yum -y upgrade
    
    # SUSE instances
    user@my-instance:~$ sudo zypper --non-interactive up

**Oorspronkelijk bulletin:**

We raden u aan uw Linux-distributies te upgraden. Voor instanties met Debian
kunt u een update uitvoeren met behulp van de volgende opdrachten in uw
instantie:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    

Voor CentOS-instanties:

    
    
    
    user@my-instance:~$ sudo yum -y upgrade

Zie de aankondiging voor de betreffende Linux-distributie voor meer
informatie:

  * Originele patches: [ http://ftp.gnu.org/gnu/bash/ ](http://ftp.gnu.org/gnu/bash/) (zie het laatste item in *-patches voor de juiste versie) 
  * Debian: [ [SECURITY] [DSA 3032-1] bash-beveiligingsupdate ](https://lists.debian.org/debian-security-announce/2014/msg00220.html)
  * RHEL: 
    * [ RHSA-2014: 1293-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00048.html)
    * [ RHSA-2014: 1294-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00049.html)
  * CentOS 5: [ [CentOS-announce] CESA-2014: 1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020582.html)
  * CentOS 6: [ [CentOS-announce] CESA-2014: 1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020585.html)
  * CentOS 7: [ [CentOS-announce] CESA-2014: 1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020583.html)

|  Hoog  |  [ CVE-2014-7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) , [
CVE-2014-6271 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6271)
, [ CVE-2014-6277
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277) , [
CVE-2014-6278 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278)
[ CVE-2014-7186
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186) , [
CVE-2014-7187 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)  
  
##  Publicatiedatum: 25-07-2014

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

[ Elasticsearch Logstash ](http://www.elasticsearch.org/overview/logstash/) is
kwetsbaar voor OS-opdrachtinjectie die ongeoorloofde wijziging en
openbaarmaking van gegevens mogelijk maakt. Een aanvaller kan bewerkte
gebeurtenissen verzenden naar alle gegevensbronnen van Logstash, waardoor de
aanvaller opdrachten kan uitvoeren met de rechten van het Logstash-proces.

####  Impact op Compute Engine

Deze kwetsbaarheid treft alle Compute Engine-instanties met versies van
Elasticsearch Logstash van vóór 1.4.2 waarbij uitvoer met zabbix of
nagios_nsca is ingeschakeld. Om een aanval te voorkomen, kunt u:

  * upgraden naar Logstash 1.4.2, 
  * de patch voor versies 1.3.x toepassen, 
  * de uitvoer van ` zabbix ` en ` nagios_nsca ` uitschakelen. 

Lees meer op de [ Logstash-blog
](http://www.elasticsearch.org/blog/logstash-1-4-2/) .

Elasticsearch adviseert ook [ een firewall te gebruiken
](http://www.elasticsearch.org/blog/scripting-security/) om externe toegang
door niet-vertrouwde IP's te voorkomen.

|  Hoog  |  [ CVE-2014-4326
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-4326)  
  
##  Publicatiedatum: 18-06-2014

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

We willen graag reageren op mogelijke zorgen van klanten over de beveiliging
van Docker-containers als die worden uitgevoerd op Google Cloud Platform. Dit
geldt voor klanten die onze Google App Engine-extensies gebruiken die Docker-
containers, voor containers geoptimaliseerde virtuele machines of de planner
van Open Source Kubernetes ondersteunen.

Docker heeft het probleem uitstekend afgehandeld; u kunt de de reactie van
Docker [ op hun blog ](http://blog.docker.com/2014/06/docker-container-
breakout-proof-of-concept-exploit/) bekijken. Zoals Docker aangeeft in deze
reactie, is het ontdekte probleem alleen van toepassing op Docker 0.11, een
oudere preproductieversie.

Nu iedereen nadenkt over de beveiliging van containers, willen we er graag op
wijzen dat containeroplossingen in Linux-apps (met name Docker-containers) in
Cloud Platform worden uitgevoerd op volledig virtuele machines (Compute
Engine). Hoewel we de inspanningen van de Docker-community waarderen om de
containerstack in Linux-apps te versterken, erkennen we dat de technologie
nieuw is en er nog veel moet gebeuren. We zijn ervan overtuigd dat volledige
hypervisors (virtuele machines) op dit moment een compacter en beter
verdedigbaar oppervlak bieden. Virtuele machines werden vanaf het begin
ontworpen om kwaadwillende productietaken te isoleren en de waarschijnlijkheid
en impact van een codebug te minimaliseren.

Onze klanten kunnen erop vertrouwen dat er een volledige hypervisor-grens
bestaat tussen hen en mogelijk schadelijke code van derden. Mochten we een
punt bereiken waarop we de stack Linux-app-containers robuust genoeg achten om
productietaken met meerdere tenants te ondersteunen, dan laten we de community
dit weten. Voorlopig is de Linux-app-container geen vervanging voor de
virtuele machine. Het is een manier om er veel meer uit te halen.

|  Laag  |  [ Blogpost van Docker ](http://blog.docker.com/2014/06/docker-
container-breakout-proof-of-concept-exploit/)  
  
##  Publicatiedatum: 05-06-2014

**Laatste update: 09-06-2014**

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

Er is een probleem met OpenSSL waarbij de ` ChangeCipherSpec ` -berichten niet
juist aan de machine met handshakestatus worden verbonden. Hierdoor kunnen ze
vroeg in de handshake worden geïnjecteerd. Een aanvaller die een zorgvuldig
gemaakte handshake gebruikt, kan het gebruik van zwak sleutelmateriaal in
OpenSSL SSL/TLS-clients en -servers forceren. Dit kan worden misbruikt door
een Man-in-the-Middle (MITM)-aanval waarbij de aanvaller het verkeer van de
aangevallen client en server kan ontsleutelen en wijzigen.

Dit probleem wordt geïdentificeerd als [ CVE-2014-0224
](https://www.openssl.org/news/secadv/20140605.txt) . Het OpenSSL-team heeft
het probleem verholpen en de OpenSSL-community gevraagd om OpenSSL te updaten.

####  Impact op Compute Engine

Deze kwetsbaarheid treft alle Compute Engine-instanties die OpenSSL gebruiken,
inclusief Debian, CentOS, Red Hat Enterprise Linux en SUSE Linux Enterprise
Server. U kunt uw instanties updaten door ze opnieuw te maken met nieuwe
images of door pakketten in uw instanties handmatig te updaten.

**Update (09-06-2014):** Als u uw instanties met SUSE Linux Enterprise Server
wilt updaten met nieuwe images, maakt u uw instanties opnieuw met behulp van
de volgende imageversies of hoger:

  * ` sles-11-sp3-v20140609 `

**Oorspronkelijk bericht:**

Als u Debian- en CentOS-instanties wilt updaten met nieuwe images, maakt u uw
instanties opnieuw met een van de volgende imageversies of hoger:

  * ` debian-7-wheezy-v20140605 `
  * ` backports-debian-7-wheezy-v20140605 `
  * ` centos-6-v20140605 `
  * ` rhel-6-v20140605 `

Als u OpenSSL handmatig bij uw instanties wilt updaten, voert u de volgende
opdrachten uit om de betreffende pakketten te updaten. Voor instanties die
CentOS en RHEL uitvoeren, kunt u OpenSSL updaten door deze opdrachten in uw
instantie uit te voeren:

    
    
    
    user@my-instance:~$ sudo yum -y update
    user@my-instance:~$ sudo reboot

Voor instanties met Debian kunt u OpenSSL updaten door de volgende opdrachten
in uw instantie uit te voeren:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

Voor instanties met SUSE Linux Enterprise Server kunt u ervoor zorgen dat
OpenSSL up-to-date is door deze opdrachten in de instantie uit te voeren:

    
    
    
    user@my-instance:~$ sudo zypper --non-interactive up
    user@my-instance:~$ sudo reboot

|  Gemiddeld  |  [ CVE-2014-0224
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0224)  
  
##  Publicatiedatum: 08-04-2014

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

De (1) TLS- en (2) DTLS-implementaties in OpenSSL 1.0.1 vóór 1.0.1g voeren
Heartbeat Extension-pakketten niet goed uit, waardoor aanvallers op afstand
gevoelige informatie uit het procesgeheugen kunnen verkrijgen via zelfgemaakte
pakketten die een bufferoverschrijding activeren, zoals aangetoond door het
lezen van privésleutels, gerelateerd aan ` d1_both.c ` en ` t1_lib.c ` . Dit
staat ook bekend als de Heartbleed-bug.

####  Impact op Compute Engine

Deze kwetsbaarheid heeft invloed op alle Compute Engine Debian-, RHEL- en
CentOS-instanties die niet de meest recente versie van OpenSSL hebben. U kunt
uw instanties updaten door ze opnieuw te maken met nieuwe images of door
pakketten in uw instanties handmatig te updaten.

Als u uw instanties wilt updaten met nieuwe images, maakt u uw instanties
opnieuw met een van de volgende imageversies of hoger:

  * ` debian-7-wheezy-v20140408 `
  * ` backports-debian-7-wheezy-v20140408 `
  * ` centos-6-v20140408 `
  * ` rhel-6-v20140408 `

Als u OpenSSL handmatig in uw instanties wilt updaten, voert u de volgende
opdrachten uit om de betreffende pakketten te updaten. Voor instanties die
CentOS en RHEL uitvoeren, kunt u ervoor zorgen dat OpenSSL up-to-date is door
deze opdrachten in de instantie uit te voeren:

    
    
    
    user@my-instance:~$ sudo yum update
    user@my-instance:~$ sudo reboot

Voor instanties met Debian kunt u OpenSSL updaten door de volgende opdrachten
in uw instantie uit te voeren:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get upgrade
    user@my-instance:~$ sudo reboot

De bug heeft geen invloed op SUSE Linux-instanties.

**Update van 14 april 2014:** Naar aanleiding van nieuw onderzoek naar het
extraheren van sleutels met behulp van de Heartbleed-bug, raadt Compute Engine
klanten van Compute Engine aan nieuwe sleutels voor getroffen SSL-services te
maken.

|  Gemiddeld  |  [ CVE-2014-0160
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0160)  
  
##  Publicatiedatum: 07-06-2013

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

**Opmerking:** Deze kwetsbaarheid is alleen van toepassing op kernels die zijn
beëindigd en verwijderd sinds API-versie v1.

Format string-kwetsbaarheid in de ` b43_request_firmware ` -functie in `
drivers/net/wireless/b43/main.c ` in het draadloze stuurprogramma Broadcom B43
in de Linux-kernel tot en met 3.9.4 biedt lokale gebruikers de mogelijkheid
privileges te verkrijgen door gebruik te maken van root-toegang en format
string-specificatoren op te nemen in een ` fwpostfix ` modprobe-parameter, wat
tot onjuiste constructie van een foutmelding leidt.

####  Impact op Compute Engine

Deze kwetsbaarheid heeft invloed op alle Compute Engine-kernels eerder dan `
gcg-3.3.8-201305291443 ` . Als reactie hierop heeft Compute Engine alle
eerdere kernels beëindigd en aanbevolen dat gebruikers hun instanties en
images updaten en de Compute Engine-kernel ` gce-v20130603 ` gebruiken. `
gce-v20130603 ` bevat kernel ` gcg-3.3.8-201305291443 ` met de patch voor deze
kwetsbaarheid.

Achterhalen welke kernel-versie uw instantie gebruikt:

  1. ssh in uw instantie 
  2. Voer ` uname -r ` uit 

|  Gemiddeld  |  [ CVE-2013-2852
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2852)  
  
##  Publicatiedatum: 07-06-2013

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

**Opmerking:** Deze kwetsbaarheid is alleen van toepassing op kernels die zijn
beëindigd en verwijderd sinds API-versie v1.

Format string-kwetsbaarheid in de register_disk-functie in ` block/genhd.c `
in de Linux-kernel tot en met 3.9.4 biedt lokale gebruikers de mogelijkheid om
privileges te verkrijgen door gebruik te maken van root-toegang en format
string-specificatoren naar ` /sys/module/md_mod/parameters/new_array ` te
schrijven om een bewerkte ` /dev/md ` -apparaatnaam te maken.

####  Impact op Compute Engine

Deze kwetsbaarheid heeft invloed op alle Compute Engine-kernels eerder dan `
gcg-3.3.8-201305291443 ` . Als reactie hierop heeft Compute Engine alle
eerdere kernels beëindigd en aanbevolen dat gebruikers hun instanties en
images updaten en de Compute Engine-kernel ` gce-v20130603 ` gebruiken. `
gce-v20130603 ` bevat kernel ` gcg-3.3.8-201305291443 ` met de patch voor deze
kwetsbaarheid.

Achterhalen welke kernel-versie uw instantie gebruikt:

  1. ssh in uw instantie 
  2. Voer ` uname -r ` uit 

|  Gemiddeld  |  [ CVE-2013-2851
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2851)  
  
##  Publicatiedatum: 14-05-2013

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

**Opmerking:** Deze kwetsbaarheid is alleen van toepassing op kernels die zijn
beëindigd en verwijderd sinds API-versie v1.

De perf_swevent_init-functie in ` kernel/events/core.c ` in de Linux-kernel
vóór 3.8.9 gebruikt een onjuist ` integer ` -gegevenstype, waarmee lokale
gebruikers privileges kunnen verkrijgen via een bewerkte ` perf_event_open `
-systeemaanroep.

####  Impact op Compute Engine

Deze kwetsbaarheid heeft invloed op alle Compute Engine-kernels eerder dan `
gcg-3.3.8-201305211623 ` . Als reactie hierop heeft Compute Engine alle
eerdere kernels beëindigd en aanbevolen dat gebruikers hun instanties en
images updaten en de Compute Engine-kernel ` gce-v20130521 ` gebruiken. `
gce-v20130521 ` bevat kernel ` gcg-3.3.8-201305211623 ` met de patch voor deze
kwetsbaarheid.

Achterhalen welke kernel-versie uw instantie gebruikt:

  1. ssh in uw instantie 
  2. Voer ` uname -r ` uit 

|  Hoog  |  [ CVE-2013-2094
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2094)  
  
##  Publicatiedatum: 18-02-2013

Beschrijving  |  Ernst  |  Opmerkingen  
---|---|---  
  
####  Beschrijving

**Opmerking:** Deze kwetsbaarheid is alleen van toepassing op kernels die zijn
beëindigd en verwijderd sinds API-versie v1.

Race condition in de ptrace-functionaliteit in de Linux-kernel vóór 3.7.5
biedt lokale gebruikers de mogelijkheid privileges te verkrijgen via een `
PTRACE_SETREGS ptrace ` -systeemaanroep in een bewerkte app.

####  Impact op Compute Engine

Deze kwetsbaarheid heeft invloed op Compute Engine-kernels ` 2.6.x-gcg- _
<date> _ ` . Als reactie hierop heeft Compute Engine de 2.6.x-kernels
beëindigd en wordt aanbevolen dat gebruikers hun instanties en images updaten
en de Compute Engine-kernel ` gce-v20130225 ` gebruiken. ` gce-v20130225 `
bevat kernel ` 3.3.8-gcg-201302081521 ` met de patch voor deze kwetsbaarheid.

Achterhalen welke kernel-versie uw instantie gebruikt:

  1. ssh in uw instantie 
  2. Voer ` uname -r ` uit 

|  Gemiddeld  |  [ CVE-2013-0871
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-0871)

