#  Bollettini sulla sicurezza

Potremmo pubblicare periodicamente dei bollettini sulla sicurezza relativi a
Compute Engine. Di seguito vengono descritti tutti i bollettini di sicurezza
per Compute Engine.

[ Iscriviti ai bollettini di sicurezza per Compute Engine.
![Iscriviti](https://cloud.google.com/images/feed-icon.png?hl=it)
](https://cloud.google.com/feeds/compute-engine-security-bulletins.xml?hl=it)

##  Data di pubblicazione: 18-06-2019

**Ultimo aggiornamento: 25-06-2019 alle ore 6:30 PST**

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

Netflix ha recentemente divulgato tre vulnerabilità TCP nei kernel Linux:

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

Questi CVE vengono denominati collettivamente [ NFLX-2019-001
](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-
party/2019-001.md) .

####  Impatto di Compute Engine

L'infrastruttura che ospita Compute Engine è protetta da questa vulnerabilità.

Le VM di Compute Engine che eseguono sistemi operativi Linux privi di patch e
inviano/ricevono traffico di rete non attendibile sono vulnerabili a questo
attacco DoS. Consigliamo di aggiornare le istanze VM appena saranno
disponibili le patch per i sistemi operativi corrispondenti.

Ai bilanciatori del carico che terminano le connessioni TCP sono state
applicate patch contro questa vulnerabilità. Le istanze di Compute Engine che
ricevono traffico non attendibile solo attraverso questi bilanciatori del
carico non sono vulnerabili. Ciò include i bilanciatori del carico HTTP, del
proxy SSL e del proxy TCP.

I bilanciatori del carico di rete e i bilanciatori del carico interni non
terminano le connessioni TCP. Le istanze di Compute Engine prive di patch che
ricevono traffico non attendibile attraverso questi bilanciatori del carico
sono vulnerabili.

####  Immagini con patch e risorse del fornitore

Forniremo qui i link alle informazioni sulle patch di ciascun fornitore del
sistema operativo appena saranno disponibili, incluso lo stato dei singoli
CVE. Le versioni precedenti di queste immagini pubbliche non contengono queste
patch e non sono in grado di mitigare i potenziali attacchi:

  * Progetto ` debian-cloud ` : 
    * ` debian-9-stretch-v20190618 `
  * Progetto ` centos-cloud ` : 
    * ` centos-6-v20190619 `
    * ` centos-7-v20190619 `
  * Progetto ` cos-cloud ` : 
    * ` cos-dev-77-12293-0-0 `
    * ` cos-beta-76-12239-21-0 `
    * ` cos-stable-75-12105-77-0 `
    * ` cos-73-11647-217-0 `
    * ` cos-69-10895-277-0 `
  * Progetto ` coreos-cloud ` : 
    * ` coreos-alpha-2163-2-1-v20190617 `
    * ` coreos-beta-2135-3-1-v20190617 `
    * ` coreos-stable-2079-6-0-v20190617 `
  * Progetto ` rhel-cloud ` : 
    * ` rhel-6-v20190618 `
    * ` rhel-7-v20190618 `
    * ` rhel-8-v20190618 `
  * Progetto ` rhel-sap-cloud ` : 
    * ` rhel-7-4-sap-v20190618 `
    * ` rhel-7-6-sap-v20190618 `
  * Progetto ` suse-cloud ` : 
    * ` sles-12-sp4-v20190617 `
    * ` sles-15-v20190617 `
  * Progetto ` suse-sap-cloud ` : 
    * ` sles-12-sp1-sap-v20190617 `
    * ` sles-12-sp2-sap-v20190617 `
    * ` sles-12-sp3-sap-v20190617 `
    * ` sles-12-sp4-sap-v20190617 `
    * ` sles-15-sap-v20190617 `
  * Progetto ` ubuntu-cloud ` : 
    * ` ubuntu-1604-xenial-v20190617 `
    * ` ubuntu-1804-bionic-v20190617 `
    * ` ubuntu-1810-cosmic-v20190618 `
    * ` ubuntu-1904-disco-v20190619 `
    * ` ubuntu-minimal-1604-xenial-v20190618 `
    * ` ubuntu-minimal-1804-bionic-v20190617 `
    * ` ubuntu-minimal-1810-cosmic-v20190618 `
    * ` ubuntu-minimal-1904-disco-v20190618 `

|  Media  |

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

  
  
##  Data di pubblicazione: 14-05-2019

**Ultimo aggiornamento: 20-05-2019 alle ore 17.00 PST**

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

Intel ha divulgato i seguenti CVE:

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

Questi CVE vengono denominati collettivamente Microarchitectural Data Sampling
(MDS). Queste vulnerabilità possono determinare un'esposizione dei dati
attraverso l'interazione dell'esecuzione speculativa con lo stato della
microarchitettura.

####  Impatto di Compute Engine

**L'infrastruttura host che esegue Compute Engine isola i carichi di lavoro
dei clienti l'uno dall'altro. A meno che tu non esegua codice non attendibile
all'interno delle VM, non sono necessarie altre azioni.**

I clienti che eseguono codice non attendibile nei propri servizi multi-tenant
all'interno delle macchine virtuali Compute Engine possono fare riferimento
alla mitigazione consigliata dal fornitore del sistema operativo guest, che
potrebbe includere l'utilizzo delle funzionalità di mitigazione del
microcodice Intel. Abbiamo eseguito il deployment dell'accesso pass-through
guest alla nuova funzionalità di svuotamento. Di seguito è riportato un
riepilogo delle procedure di mitigazione per le immagini guest più comuni.

####  Immagini con patch e risorse del fornitore

Forniremo qui i link alle informazioni sulle patch fornite dal fornitore di
ciascun sistema operativo non appena saranno disponibili, con lo stato di
ciascun CVE. Tali immagini possono essere utilizzate per ricreare le istanze
VM. Le versioni precedenti di queste immagini pubbliche non contengono queste
patch e non sono in grado di mitigare i potenziali attacchi:

  * Progetto ` centos-cloud ` : [ CESA-2019:1169 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023309.html) , [ CESA-2019:1168 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023314.html)
    * ` centos-6-v20190515 `
    * ` centos-7-v20190515 `
  * Progetto ` coreos-cloud ` : [ mitigazioni di MDS per CoreOS Container Linux ](https://coreos.com/os/docs/latest/disabling-smt.html)
    * ` coreos-stable-2079-4-0-v20190515 `
    * ` coreos-beta-2107-3-0-v20190515 `
    * ` coreos-alpha-2135-1-0-v20190515 `
  * Progetto ` cos-cloud `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
  * Progetto ` debian-cloud ` : [ DSA-4444 ](https://www.debian.org/security/2019/dsa-4444)
    * ` debian-9-stretch-v20190514 `
  * Progetto ` rhel-cloud ` : [ Articolo informativo su MDS per Red Hat ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-6-v20190515 `
    * ` rhel-7-v20190517 `
    * ` rhel-8-v20190515 `
  * Progetto ` rhel-sap-cloud ` : [ Articolo informativo su MDS per Red Hat ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-7-4-sap-v20190515 `
    * ` rhel-7-6-sap-v20190517 `
  * Progetto ` suse-cloud ` : [ Knowledge base su MDS per SUSE ](https://www.suse.com/support/kb/doc/?id=7023736)
    * ` sles-12-sp4-v20190520 `
    * ` sles-15-v20190520 `
  * Progetto ` suse-sap-cloud `
    * ` sles-12-sp4-sap-v20190520 `
    * ` sles-15-sap-v20190520 `
  * Progetto ` ubuntu-os-cloud ` : [ Wiki su MDS per Ubuntu ](https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/MDS)
    * ` ubuntu-1404-trusty-v20190514 `
    * ` ubuntu-1604-xenial-v20190514 `
    * ` ubuntu-1804-bionic-v20190514 `
    * ` ubuntu-1810-cosmic-v20190514 `
    * ` ubuntu-1904-disco-v20190514 `
    * ` ubuntu-minimal-1604-xenial-v20190514 `
    * ` ubuntu-minimal-1804-bionic-v20190514 `
    * ` ubuntu-minimal-1810-cosmic-v20190514 `
    * ` ubuntu-minimal-1904-disco-v20190514 `
  * Progetti ` windows-cloud ` e ` windows-sql-cloud ` : [ Microsoft ADV190013 ](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/ADV190013)
    * Tutte le immagini pubbliche di Windows Server e SQL Server con numero di versione ` v20190514 ` . 
  * Progetto ` gce-uefi-images `
    * ` centos-7-v20190515 `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
    * ` rhel-7-v20190517 `
    * ` ubuntu-1804-bionic-v20190514 `
    * Tutte le immagini pubbliche di Windows Server con numero di versione ` v20190514 ` . 

####  Container-Optimized OS

Se utilizzi Container Optimized OS (COS) come sistema operativo guest ed
esegui carichi di lavoro multi-tenant non attendibili nella tua macchina
virtuale, ti consigliamo di:

  1. Disabilitare Hyper-Threading impostando ` nosmt ` sulla riga di comando del kernel.   

Sulle VM di COS esistenti, puoi modificare ` grub.cfg ` come segue per
impostare l'opzione ` nosmt ` e quindi riavviare il sistema:

    
        
    # Run as root:
    dir="$(mktemp -d)"
    mount /dev/sda12 "${dir}"
    sed -i -e "s|cros_efi|cros_efi nosmt|g" "${dir}/efi/boot/grub.cfg"
    umount "${dir}"
    rmdir "${dir}"
    
    reboot

Per comodità, puoi ottenere lo stesso effetto dei comandi sopra anche
eseguendo lo script riportato di seguito. Ti consigliamo di includere tale
script in cloud-config, negli script di avvio o nei modelli di istanza, per
assicurarti che le nuove VM utilizzino il nuovo parametro. Di seguito è
riportato un esempio di cloud-config che esegue tale script.

**Avviso:** questo comando determina il riavvio immediato dell'istanza, quando
viene utilizzato per la prima volta. Le esecuzioni successive del comando su
un'istanza con Hyper-Threading già disabilitato non hanno alcun effetto.

    
        
    # Run as root
    /bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)
    

Per includere lo script in cloud-config:

    
        
    #cloud-config
    
    bootcmd:
    - /bin/bash -c "/bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)"
    

Per verificare che l'Hyper-Threading sia disabilitato nella tua istanza,
osserva l'output dei file ` /sys/devices/system/cpu/smt/active ` e `
/sys/devices/system/cpu/smt/control ` . Se viene restituito ` 0 ` per ` active
` e ` off ` per ` control ` , l'Hyper-Threading è disabilitato:

    
        
    cat /sys/devices/system/cpu/smt/active
    cat /sys/devices/system/cpu/smt/control
    

**Nota:** se hai abilitato la funzionalità Avvio protetto UEFI nella tua
istanza, dovrai ricreare l'istanza con tale funzionalità disabilitata,
eseguire il comando precedente con tale funzionalità disabilitata e quindi
abilitare Avvio protetto UEFI nella nuova istanza.

  2. Utilizzare una nuova versione dell'immagine COS   

Oltre a disabilitare l'Hyper-Threading come spiegato in precedenza, devi anche
[ ricreare le tue istanze
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=it#publicimage) con le immagini aggiornate elencate sopra o con
versioni più recenti (se disponibili) delle immagini di Container-Optimized
OS, per ottenere una protezione completa dalla vulnerabilità.

|  Media  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  Data di pubblicazione: 14-08-2018

**Ultimo aggiornamento: 20-08-2018 alle ore 17.00 PST**

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

[ Intel ha divulgato ](https://www.intel.com/content/www/us/en/architecture-
and-technology/l1tf.html) i seguenti CVE:

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) (per [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (per sistemi operativi e [ SMT, Simultaneous Multi-Threading ](https://en.wikipedia.org/wiki/Hyper-Threading) ) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (per la virtualizzazione) 

Questi CVE vengono denominati collettivamente "L1 Terminal Fault (L1TF)".

Queste vulnerabilità L1TF sfruttano l'esecuzione speculativa attaccando la
configurazione delle strutture di dati a livello di processore. "L1" si
riferisce alla cache dei dati di livello 1 (L1D), una piccola risorsa on-core
utilizzata per accelerare l'accesso alla memoria.

Leggi il [ post del blog di Google Cloud
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=it) per ulteriori dettagli su queste
vulnerabilità e sulle mitigazioni di Compute Engine.

####  Impatto di Compute Engine

L'infrastruttura host che esegue Compute Engine e isola i carichi di lavoro
dei clienti l'uno dall'altro è protetta dagli attacchi noti.

I clienti di Compute Engine sono incoraggiati ad aggiornare le loro immagini
per evitare il possibile sfruttamento indiretto di questa vulnerabilità
all'interno dei loro ambienti guest. Ciò è particolarmente importante per i
clienti che eseguono i propri servizi multi-tenant su macchine virtuali
Compute Engine.

Per aggiornare i sistemi operativi guest sulle loro istanze, i clienti di
Google Compute Engine possono:

  * Utilizzare immagini pubbliche con patch per [ ricreare le istanze VM esistenti ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=it#publicimage) . 
  * Installare sulle istanze esistenti le patch messe a disposizione dal fornitore del sistema operativo e riavviare le istanze dopo l'applicazione delle patch. 

####  Immagini con patch e risorse del fornitore

Forniremo qui i link alle informazioni sulle patch di ciascun fornitore del
sistema operativo non appena saranno disponibili, con lo stato di entrambi i
CVE. Utilizza queste immagini per ricreare le istanze VM. Le versioni
precedenti di queste immagini pubbliche non contengono queste patch e non
mitigano i potenziali attacchi:

  * Progetto ` centos-cloud ` : 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * Progetto ` coreos-cloud ` : 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * Progetto ` cos-cloud ` : 
    * ` cos-stable-66-10452-110-0 `
    * ` cos-stable-67-10575-66-0 `
    * ` cos-beta-68-10718-81-0 `
    * ` cos-dev-69-10895-23-0 `
  * Progetto ` debian-cloud ` : 
    * ` debian-9-stretch-v20180820 `
  * Progetto ` rhel-cloud ` : 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * Progetto ` rhel-sap-cloud ` : 
    * ` rhel-7-sap-apps-v20180814 `
    * ` rhel-7-sap-hana-v20180814 `
  * Progetto ` suse-cloud ` : 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
    * ` sles-11-sp4-v20180816 `
  * Progetto ` suse-sap-cloud ` : 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * Progetto ` ubuntu-os-cloud ` : 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `
  * Progetti ` windows-cloud ` ` gce-uefi-images ` e ` windows-sql-cloud ` : 
    * Tutte le [ immagini pubbliche ](https://cloud.google.com/compute/docs/images?hl=it#os-compute-support) di Windows Server e SQL Server con numero di versione ` -v201800814 ` e successivi includono le patch. 

|  Alta  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  Data di pubblicazione: 06-08-2018

**Ultimo aggiornamento: 05-09-2018 alle ore 17.00 PST**

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Aggiornamento 05-09-2018

Il [ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) è stato divulgato il 14-08-2018 da US-
CERT. Come per il [ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) , si tratta di una vulnerabilità di rete a
livello di kernel che aumenta l'efficacia degli attacchi DoS (Denial of
Service) contro i sistemi vulnerabili. La principale differenza è che il
CVE-2018-5391 è sfruttabile sulle connessioni IP. Abbiamo aggiornato questo
bollettino per coprire entrambe le vulnerabilità.

####  Descrizione

Il [ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ("SegmentSmack") descrive una
vulnerabilità di rete a livello di kernel che aumenta l'efficacia degli
attacchi DoS (Denial of Service) contro i sistemi vulnerabili tramite le
connessioni TCP.

Il [ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ("FragmentSmack") descrive una
vulnerabilità di rete a livello di kernel che aumenta l'efficacia degli
attacchi DoS (Denial of Service) contro i sistemi vulnerabili tramite le
connessioni IP.

####  Impatto di Compute Engine

L'infrastruttura host che esegue le VM di Compute Engine non è a rischio.
L'infrastruttura di rete che gestisce il traffico verso e dalle VM di Compute
Engine è protetta da questa vulnerabilità. Le VM di Compute Engine che
inviano/ricevono traffico di rete non attendibile solo tramite bilanciatori
del carico [ HTTP(S) ](https://cloud.google.com/load-
balancing/docs/https/?hl=it) , [ SSL ](https://cloud.google.com/load-
balancing/docs/ssl/?hl=it) o [ TCP ](https://cloud.google.com/load-
balancing/docs/tcp/?hl=it) sono protette da questa vulnerabilità.

Le VM di Compute Engine che eseguono sistemi operativi privi di patch che
inviano/ricevono traffico di rete non attendibile direttamente o tramite [
bilanciatori del carico di rete ](https://cloud.google.com/load-
balancing/docs/network/?hl=it) sono vulnerabili a questo attacco DoS.

Valuta la possibilità di aggiornare le istanze VM non appena sono disponibili
patch per i rispettivi sistemi operativi.

Per aggiornare i sistemi operativi guest sulle loro istanze, i clienti di
Compute Engine possono:

  * Utilizzare immagini pubbliche con patch per [ ricreare le istanze VM esistenti ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=it#publicimage) . L'elenco delle immagini pubbliche con patch è riportato di seguito. 
  * Installare sulle istanze esistenti le patch messe a disposizione dal fornitore del sistema operativo e riavviare le istanze dopo l'applicazione delle patch. 

####  Immagini con patch e risorse del fornitore

Forniremo qui i link alle informazioni relative alle patch di ciascun
fornitore del sistema operativo non appena saranno disponibili.

  * Progetto ` centos-cloud ` (solo CVE-2018-5390): 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * Progetto ` coreos-cloud ` (CVE-2018-5390 e CVE-2018-5391): 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * Progetto ` cos-cloud ` (CVE-2018-5390 e CVE-2018-5391): 
    * ` cos-stable-65-10323-98-0 `
    * ` cos-stable-66-10452-109-0 `
    * ` cos-stable-67-10575-65-0 `
    * ` cos-beta-68-10718-76-0 `
    * ` cos-dev-69-10895-16-0 `
  * Progetto ` debian-cloud ` (CVE-2018-5390 e CVE-2018-5391): 
    * ` debian-9-stretch-v20180814 `
  * Progetto ` rhel-cloud ` (solo CVE-2018-5390): 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * Progetto ` suse-cloud ` (CVE-2018-5390 e CVE-2018-5391): 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
  * Progetto ` suse-sap-cloud ` (CVE-2018-5390 e CVE-2018-5391): 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * Progetto ` ubuntu-os-cloud ` (CVE-2018-5390 e CVE-2018-5391): 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `

|  Alta  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  Data di pubblicazione: 03-01-2018

**Ultimo aggiornamento: 21-05-2018 alle ore 15.00 PST**

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Aggiornamento 21-05-2018

Il [ CVE-2018-3640 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-3640) e il [ CVE-2018-3639
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639) ,
rispettivamente varianti 3a e 4, sono stati [ divulgati da Intel
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00115.html) . Come per le prime tre varianti di Spectre e Meltdown,
l'infrastruttura che esegue le istanze VM di Compute Engine è protetta e le
istanze VM dei clienti sono isolate e protette l'una dall'altra. Inoltre,
Compute Engine prevede il deployment delle patch di microcodice Intel nella
nostra infrastruttura, che consentirà ai clienti che eseguono carichi di
lavoro multi-tenant o non attendibili all'interno di una singola istanza VM di
attivare ulteriori mitigazioni interne alla VM quando fornite dai provider e
dai fornitori di sistemi operativi. Compute Engine eseguirà il deployment
delle patch di microcodice dopo che Intel le avrà certificate e dopo che
Compute Engine avrà verificato e qualificato le patch per il nostro ambiente
di produzione. Forniremo tempistiche e aggiornamenti più dettagliati su questa
pagina non appena saranno disponibili.

####  Descrizione

Questi CVE sono varianti di una nuova classe di attacchi che sfruttano la
tecnologia di esecuzione speculativa disponibile in molti processori. Questa
classe di attacchi può consentire l'accesso non autorizzato in sola lettura ai
dati in memoria in varie circostanze.

Compute Engine ha utilizzato la tecnologia di migrazione live delle VM per
eseguire aggiornamenti del sistema host e dell'hypervisor senza impatto
sull'utente, senza finestre di manutenzione forzata e senza riavvii di massa.
Tuttavia, a tutti i sistemi operativi guest e a tutte le versioni devono
essere applicate patch di protezione da questa nuova classe di attacchi,
indipendentemente dalla posizione di esecuzione di questi sistemi.

Per i dettagli tecnici completi su questo metodo di attacco, leggi il [ post
del blog di Project Zero
](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-
with-side.html) . Per i dettagli completi sulle misure di mitigazione di
Google, incluse tutte le informazioni specifiche del prodotto, leggi il [ post
del blog di Google Security ](https://security.googleblog.com/2018/01/todays-
cpu-vulnerability-what-you-need.html) .

####  Impatto di Compute Engine

L'infrastruttura che esegue Compute Engine e isola le istanze VM dei clienti
l'una dall'altra è protetta dagli attacchi noti. Le nostre mitigazioni
impediscono l'accesso non autorizzato ai nostri sistemi host da applicazioni
eseguite all'interno di istanze VM. Queste mitigazioni impediscono anche
l'accesso non autorizzato tra istanze VM in esecuzione sullo stesso sistema
host.

Per impedire l'accesso non autorizzato all'interno delle istanze di macchine
virtuali, devi aggiornare i sistemi operativi guest in tali istanze
utilizzando una delle seguenti opzioni:

  * Utilizza immagini pubbliche con patch per [ ricreare le istanze VM esistenti ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=it#publicimage) . L'elenco delle immagini pubbliche con patch è riportato di seguito. 
  * Installa sulle istanze esistenti le patch messe a disposizione dal fornitore del sistema operativo per la tua distribuzione e riavvia le istanze dopo l'applicazione delle patch. I link alle informazioni sulle patch di ciascun fornitore del sistema operativo sono riportati di seguito. 

####  Immagini con patch e risorse del fornitore

**Nota:** le immagini con patch potrebbero non includere le correzioni per
tutti i CVE elencati in questo bollettino sulla sicurezza. Inoltre, immagini
diverse potrebbero includere metodi diversi per impedire questi tipi di
attacchi. Rivolgiti al fornitore del sistema operativo per verificare quali
CVE vengono risolti dalle sue patch e quali metodi di prevenzione vengono
utilizzati.

  * Progetto ` cos-cloud ` : include patch per impedire gli attacchi inclusi nella variante 2 ( [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715) ) e nella variante 3 ( [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754) ). Google ha utilizzato [ Retpoline ](https://support.google.com/faqs/answer/7625886?hl=it) in queste immagini per mitigare gli attacchi inclusi nella variante 2. 
    * ` cos-stable-63-10032-71-0 ` o famiglia di immagini ` cos-stable `
  * Progetto ` centos-cloud ` : [ informazioni sulle patch per CentOS ](https://lwn.net/Alerts/CentOS/)
    * ` centos-7-v20180104 ` o famiglia di immagini ` centos-7 `
    * ` centos-6-v20180104 ` o famiglia di immagini ` centos-6 `
  * Progetto ` coreos-cloud ` : [ informazioni sulle patch per CoreOS ](https://coreos.com/blog/container-linux-meltdown-patch)
    * ` coreos-stable-1576-5-0-v20180105 ` o famiglia di immagini ` coreos-stable `
    * ` coreos-beta-1632-1-0-v20180105 ` o famiglia di immagini ` coreos-beta `
    * ` coreos-alpha-1649-0-0-v20180105 ` o famiglia di immagini ` coreos-alpha `
  * Progetto ` debian-cloud ` : [ informazioni sulle patch per Debian ](https://www.debian.org/security/#DSAS)
    * ` debian-9-stretch-v20180105 ` o famiglia di immagini ` debian-9 `
    * ` debian-8-jessie-v20180109 ` o famiglia di immagini ` debian-8 `
  * Progetto ` rhel-cloud ` : [ informazioni sulle patch per RHEL ](https://access.redhat.com/security/vulnerabilities/speculativeexecution)
    * ` rhel-7-v20180104 ` o famiglia di immagini ` rhel-7 `
    * ` rhel-6-v20180104 ` o famiglia di immagini ` rhel-6 `
  * Progetto ` suse-cloud ` : [ informazioni sulle patch per SUSE ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-v20180104 ` o famiglia di immagini ` sles-12 `
    * ` sles-11-sp4-v20180104 ` o famiglia di immagini ` sles-11 `
  * Progetto ` suse-sap-cloud ` : [ informazioni sulle patch per SUSE ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-sap-v20180104 ` o famiglia di immagini ` sles-12-sp3-sap `
    * ` sles-12-sp2-sap-v20180104 ` o famiglia di immagini ` sles-12-sp2-sap `
  * Progetto ` ubuntu-os-cloud ` : [ informazioni sulle patch per Ubuntu ](https://insights.ubuntu.com/2018/01/04/ubuntu-updates-for-the-meltdown-spectre-vulnerabilities/)
    * ` ubuntu-1710-artful-v20180109 ` o famiglia di immagini ` ubuntu-1710 `
    * ` ubuntu-1604-xenial-v20180109 ` o famiglia di immagini ` ubuntu-1604-lts `
    * ` ubuntu-1404-trusty-v20180110 ` o famiglia di immagini ` ubuntu-1404-lts `
  * Progetti ` windows-cloud ` e ` windows-sql-cloud ` : 
    * Tutte le [ immagini pubbliche ](https://cloud.google.com/compute/docs/images?hl=it#os-compute-support) di Windows Server e SQL Server con numero di versione ` -v20180109 ` e successivi includono le patch. Tuttavia, dovrai eseguire le azioni consigliate da Microsoft nel bollettino di assistenza relativo alle [ linee guida per Windows Server ](https://support.microsoft.com/en-gb/help/4072698/windows-server-guidance-to-protect-against-the-speculative-execution) per attivare e verificare queste mitigazioni sia sulle istanze esistenti, sia sulle istanze appena create. 

Utilizza queste immagini per [ ricreare le istanze VM
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=it#publicimage) . Le versioni precedenti di queste immagini
pubbliche non contengono queste patch e non mitigano i potenziali attacchi.

####  Patch dei fornitori di hardware

NVIDIA fornisce driver con patch per mitigare i potenziali attacchi contro i
sistemi su cui è installato il software dei driver NVIDIA®. Per sapere a quali
versioni dei driver sono state applicate le patch, leggi il bollettino sulla
sicurezza di NVIDIA relativo agli [ aggiornamenti di sicurezza per i driver
video delle GPU NVIDIA
](http://nvidia.custhelp.com/app/answers/detail/a_id/4611) .

####  Cronologia delle revisioni:

  * 21-05-2018 ore 14:00 PST: aggiunte informazioni sulle due nuove varianti divulgate il 21 maggio 2018. 
  * 10-01-2018 ore 15:00 PST: aggiunte informazioni sulle immagini pubbliche di Windows Server e SQL Server con patch. 
  * 10-01-2018 ore 10:15 PST: aggiunte diverse immagini Ubuntu all'elenco delle immagini pubbliche con patch. 
  * 10-01-2018 ore 09:50 PST: aggiunte linee guida per le patch messe a disposizione dai fornitori di hardware. 
  * 03-01-2018 - 09-01-2018: apportate diverse modifiche all'elenco delle immagini pubbliche con patch. 

|  Alta  |

  * [ CVE-2017-5753 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5753)
  * [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715)
  * [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754)
  * [ CVE-2018-3640 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3640)
  * [ CVE-2018-3639 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639)

  
  
##  Data di pubblicazione: 02-10-2017

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

[ Dnsmasq ](http://www.thekelleys.org.uk/dnsmasq/doc.html) fornisce la
funzionalità per gestire DNS, DHCP, annunci di router e avvio di rete. Questo
software è installato comunemente in sistemi di vario tipo, tra cui
distribuzioni desktop Linux (come Ubuntu), router domestici e dispositivi IoT.
Dnsmasq è ampiamente utilizzato sia sull'Internet pubblico sia internamente
nelle reti private.

Google ha rilevato sette problemi diversi nel corso delle normali valutazioni
della propria sicurezza interna. Dopo aver stabilito la gravità di questi
problemi, abbiamo cercato di analizzarne l'impatto e la sfruttabilità, per poi
generare una serie di proof of concept interni per ciascuno di essi. Abbiamo
inoltre lavorato con il gestore di Dnsmasq, Simon Kelly, per produrre le patch
adeguate e limitare l'impatto del problema.

Durante la revisione, il nostro team ha riscontrato tre possibili esecuzioni
di codice remoto, una perdita di informazioni e tre vulnerabilità di tipo
Denial of Service che interessano la versione più recente nel server Git di
progetto al 5 settembre 2017.

Queste patch sono propagate a monte e sono confermate nel [ repository Git del
progetto ](http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=summary) .

####  Impatto di Compute Engine

Per impostazione predefinita, Dnsmasq è installato solo nelle immagini che
utilizzano [ NetworkManager ](https://wikipedia.org/wiki/NetworkManager) e non
è attivo. Dnsmasq è installato nelle seguenti immagini pubbliche di Compute
Engine:

  * Ubuntu 16.04, 16.10, 17.04 
  * CentOS 7 
  * RHEL 7 

Tuttavia, Dnsmasq potrebbe essere installato su altre immagini come dipendenza
per altri pacchetti. Ti consigliamo di aggiornare le istanze Debian, Ubuntu,
CentOS, RHEL, SLES e OpenSuse in modo da utilizzare l'immagine più recente del
sistema operativo. CoreOS e Container-Optimized OS non sono interessati, così
come le immagini Windows.

Per le istanze che utilizzano Debian e Ubuntu puoi effettuare un aggiornamento
eseguendo nell'istanza i seguenti comandi:

    
    
    
    sudo apt-get -y update
    
    
    
    sudo apt-get -y dist-upgrade

Esegui il comando seguente per le istanze Red Hat Enterprise Linux e CentOS:

    
    
    
    sudo yum -y upgrade

Esegui il comando seguente per le immagini SLES e OpenSUSE:

    
    
    
    sudo zypper up

In alternativa all'esecuzione dei comandi di aggiornamento manuale, puoi [
ricreare le istanze VM utilizzando le famiglie di immagini
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=it#publicimage) del rispettivo sistema operativo.

|  Alta  |

  * [ CVE-2017-14491 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14491)
  * [ CVE-2017-14492 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14492)
  * [ CVE-2017-14493 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14493)
  * [ CVE-2017-14494 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14494)
  * [ CVE-2017-14495 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14495)
  * [ CVE-2017-14496 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14496)
  * [ CVE-2017-13704 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-13704)

  
  
##  Data di pubblicazione: 26-10-2016

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

La vulnerabilità CVE-2016-5195 è legata a una race condition relativa alla
modalità con cui il sottosistema della memoria del kernel Linux ha gestito la
violazione da parte di utenti non autorizzati dei mapping privati di sola
lettura sfruttando il meccanismo di copy-on-write (COW) al momento
dell'accesso in scrittura.

Un utente locale non privilegiato potrebbe sfruttare questa falla per accedere
in scrittura a mapping di memoria di sola lettura, con conseguente aumento dei
propri privilegi sul sistema.

Per ulteriori informazioni, consulta le [ domande frequenti sulla
vulnerabilità Dirty COW
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails) .

####  Impatto di Compute Engine

Sono interessate tutte le distribuzioni e le versioni di Linux su Compute
Engine. La maggior parte delle istanze scarica e installa automaticamente un
kernel più recente. Tuttavia, è necessario riavviare il sistema per potervi
applicare una patch.

Nelle istanze nuove o ricreate che si basano sulle seguenti immagini Compute
Engine sono già installati i kernel con patch applicata.

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

|  Alta  |  [ CVE-2016-5195
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails)  
  
##  Data di pubblicazione: 16-02-2016

**Ultimo aggiornamento: 22-02-2016**

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

La vulnerabilità CVE-2015-7547 riguarda il resolver lato client del DNS glibc,
che rende il software vulnerabile al sovraccarico del buffer basato su stack
quando si utilizza la funzione di libreria ` getaddrinfo() ` . Un utente
malintenzionato potrebbe prendere il controllo del software che utilizza
questa funzione per sfruttare questa vulnerabilità con nomi di dominio e
server DNS opportunamente predisposti o mediante attacchi di tipo man-in-the-
middle.

Per ulteriori dettagli, consulta il [ blog sulla sicurezza online di Google
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html) o il database delle [ vulnerabilità ed esposizioni
comuni (CVE) ](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-7547) .

####  Impatto di Compute Engine

**Aggiornamento (22-02-2016):**

Adesso puoi ricreare le istanze utilizzando le seguenti immagini CoreOS, SLES
e OpenSUSE:

  * ` coreos-alpha-962-0-0-v20160218 `
  * ` coreos-beta-899-7-0-v20160218 `
  * ` coreos-stable-835-13-0-v20160218 `
  * ` opensuse-13-2-v20160222 `
  * ` opensuse-leap-42-1-v20160222 `
  * ` sles-11-sp4-v20160222 `
  * ` sles-12-sp1-v20160222 `

**Aggiornamento (17-02-2016):**

Adesso puoi aggiornare le istanze Ubuntu 12.04 LTS, Ubuntu 14.04 LTS e Ubuntu
15.10 eseguendo i seguenti comandi:

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

In alternativa all'esecuzione dei comandi di aggiornamento manuale, adesso
puoi ricreare le istanze con le nuove immagini seguenti:

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

Non conosciamo metodi che possono sfruttare questa vulnerabilità attraverso i
resolver DNS di Compute Engine con la configurazione glibc predefinita.
Conviene tuttavia applicare il prima possibile una patch alle istanze di
macchine virtuali poiché, come accade con qualsiasi nuova vulnerabilità, nel
corso del tempo potrebbero essere scoperti nuovi metodi di attacco. Se hai
abilitato edns0 (che è disabilitato per impostazione predefinita), devi
disabilitarlo finché alle istanze non viene applicata la patch.

**Bollettino originale:**

La distribuzione Linux potrebbe essere vulnerabile. Per eliminare questa
vulnerabilità, i clienti di Compute Engine dovranno aggiornare le immagini di
sistema operativo delle proprie istanze se utilizzano un sistema operativo
Linux.

Per le istanze che utilizzano Debian puoi effettuare un aggiornamento
eseguendo nell'istanza i seguenti comandi:

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Ti consigliamo anche di installare [ UnattendedUpgrades
](https://wiki.debian.org/UnattendedUpgrades) per le istanze Debian.

Per le istanze Red Hat Enterprise Linux:

  * ` user@my-instance:~$ sudo yum -y upgrade `
  * ` user@my-instance:~$ sudo reboot `

Continueremo ad aggiornare questo bollettino man mano che altri gestori di
sistema operativo pubblicano le patch per questa vulnerabilità e Compute
Engine rilascia immagini aggiornate di sistema operativo.

|  Alta  |  [ CVE-2015-7547
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html)  
  
##  Data di pubblicazione: 19-03-2015

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

La vulnerabilità CVE-2015-1427 riguarda il motore di script Groovy in [
Elasticsearch ](https://www.elastic.co/products/elasticsearch) (prima della
versione 1.3.8 e qualsiasi versione 1.4.x prima della 1.4.3), che consente a
utenti malintenzionati remoti di aggirare il meccanismo di protezione sandbox
ed eseguire comandi di shell arbitrari.

Per ulteriori dettagli, consulta il [ National Vulnerability Database (NVD)
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427) o il
database delle [ vulnerabilità ed esposizioni comuni (CVE)
](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-1427) .

####  Impatto di Compute Engine

Se esegui Elasticsearch sulle istanze Compute Engine, ti conviene eseguire
l'upgrade a Elasticsearch versione 1.4.3 o successiva. Se hai già eseguito
l'upgrade del software Elasticsearch, il tuo sistema è protetto da questa
vulnerabilità.

Se non hai effettuato l'upgrade a Elasticsearch 1.4.3 o versioni successive,
puoi [ eseguire un upgrade in sequenza
](http://www.elastic.co/guide/en/elasticsearch/reference/current/rolling-
upgrades.html) .

Se hai eseguito il deployment di Elasticsearch mediante la funzionalità [
Click-to-deploy ](https://cloud.google.com/solutions/elasticsearch/click-to-
deploy?hl=it) della [ console di Google Cloud Platform
](https://console.cloud.google.com/?hl=it) , puoi [ eliminare il deployment
](https://console.cloud.google.com/projectselector/deployments?hl=it) per
rimuovere le istanze che eseguono Elasticsearch.

Il team di Google Cloud Platform sta cercando una soluzione per eseguire il
deployment di una versione aggiornata di Elasticsearch. Tuttavia, non è ancora
disponibile una soluzione per la funzionalità Click-to-deploy della [ console
di GCP ](https://console.cloud.google.com/?hl=it) .

|  Alta  |  [ CVE-2015-1427
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427)  
  
##  Data di pubblicazione: 29-01-2015

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

La vulnerabilità [ CVE-2015-0235 (Ghost)
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235) riguarda la
libreria glibc.

I clienti di App Engine, Cloud Storage, BigQuery e CloudSQL non devono
effettuare alcuna azione. I server di Google sono stati aggiornati e sono
protetti da questa vulnerabilità.

I clienti di Compute Engine potrebbero dover aggiornare le proprie immagini di
sistema operativo.

####  Impatto di Compute Engine

La distribuzione Linux potrebbe essere vulnerabile. Per eliminare questa
vulnerabilità, i clienti di Compute Engine dovranno aggiornare le immagini di
sistema operativo delle proprie istanze se eseguono Debian 7, backport di
Debian 7, Ubuntu 12.04 LTS, Red Hat Enterprise Linux, CentOS o SUSE Linux
Enterprise Server 11 SP3.

Questa vulnerabilità non interessa Ubuntu 14.04 LTS, Ubuntu 14.10 o SUSE Linux
Enterprise Server 12.

Ti consigliamo di eseguire l'upgrade delle tue distribuzioni Linux. Per le
istanze che utilizzano Debian 7, backport di Debian 7 o Ubuntu 12.04 LTS, puoi
effettuare un aggiornamento eseguendo nell'istanza i seguenti comandi:

  1. ` user@my-instance:~$ sudo apt-get update `
  2. ` user@my-instance:~$ sudo apt-get -y upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Per le istanze Red Hat Enterprise Linux o CentOS:

  1. ` user@my-instance:~$ sudo yum -y upgrade `
  2. ` user@my-instance:~$ sudo reboot `

Per le istanze SUSE Linux Enterprise Server 11 SP3:

  1. ` user@my-instance:~$ sudo zypper --non-interactive up `
  2. ` user@my-instance:~$ sudo reboot `

In alternativa all'esecuzione dei comandi di aggiornamento manuale riportati
in precedenza, adesso gli utenti possono ricreare le istanze con le nuove
immagini seguenti:

  * ` debian-7-wheezy-v20150127 `
  * ` backports-debian-7-wheezy-v20150127 `
  * ` centos-6-v20150127 `
  * ` centos-7-v20150127 `
  * ` rhel-6-v20150127 `
  * ` rhel-7-v20150127 `
  * ` sles-11-sp3-v20150127 `
  * ` ubuntu-1204-precise-v20150127 `

####  Impatto sulle VM gestite di Google

Gli utenti delle VM gestite che utilizzano ` gcloud preview app deploy `
devono aggiornare i propri container docker di base con ` gcloud preview app
deploy ` ed eseguire nuovamente il deployment di ogni applicazione in
esecuzione utilizzando ` gcloud preview app setup-managed-vms ` . Gli utenti
che eseguono il deployment con ` appcfg ` non devono fare nulla e l'upgrade
verrà eseguito automaticamente.

|  Alta  |  [ CVE-2015-0235
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235)  
  
##  Data di pubblicazione: 15-10-2014

**Ultimo aggiornamento: 17-10-2014**

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

La vulnerabilità CVE-2014-3566 (detta anche POODLE) riguarda la progettazione
di SSL versione 3.0. Questa vulnerabilità consente a un utente malintenzionato
che opera in rete di calcolare il testo non crittografato delle connessioni
sicure. Per i dettagli, consulta il nostro [ post del blog
](http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-
exploiting-ssl-30.html) sulla vulnerabilità.

I clienti di App Engine, Cloud Storage, BigQuery e CloudSQL non devono
effettuare alcuna azione. I server di Google sono stati aggiornati e sono
protetti da questa vulnerabilità. I clienti di Compute Engine devono
aggiornare le proprie immagini di sistema operativo.

####  Impatto di Compute Engine

**Aggiornamento (17-10-2014):**

La vulnerabilità potrebbe riguardarti se utilizzi SSLv3. Per eliminare questa
vulnerabilità, i clienti di Compute Engine dovranno aggiornare le immagini di
sistema operativo delle proprie istanze.

Ti consigliamo di eseguire l'upgrade delle tue distribuzioni Linux. Per le
istanze che utilizzano Debian puoi effettuare un aggiornamento eseguendo
nell'istanza i seguenti comandi:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

Per le istanze CentOS:

    
    
    
    user@my-instance:~$ sudo yum -y upgrade
    user@my-instance:~$ sudo reboot

In alternativa all'esecuzione dei comandi di aggiornamento manuale in alto,
adesso gli utenti possono ricreare le istanze con le nuove immagini seguenti:

  * ` centos-6-v20141016 `
  * ` centos-7-v20141016 `
  * ` debian-7-wheezy-v20141017 `
  * ` backports-debian-7-wheezy-v20141017 `

Aggiorneremo il bollettino per le immagini RHEL e SLES quando avremo a
disposizione le immagini. Nel frattempo, gli utenti RHEL possono contattare [
direttamente Red Hat ](https://access.redhat.com/articles/1232123) per
ulteriori informazioni.

**Bollettino originale:**

Per eliminare questa vulnerabilità, i clienti di Compute Engine dovranno
aggiornare le immagini di sistema operativo delle proprie istanze.
Aggiorneremo questo bollettino di sicurezza con le istruzioni non appena
saranno disponibili nuove immagini di sistema operativo.

|  Media  |  [ CVE-2014-3566
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-3566)  
  
##  Data di pubblicazione: 24-09-2014

**Ultimo aggiornamento: 29-09-2014**

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

In Bash esiste un bug (CVE-2014-6271) che consente l'esecuzione di codice
remoto sulla base dell'analisi di qualsiasi variabile di ambiente controllata
da un utente malintenzionato. Il vettore più probabile di sfruttamento di
questa vulnerabilità è rappresentato da richieste HTTP dannose inviate a
script CGI esposti su un server web. Per ulteriori informazioni, consulta la [
descrizione del bug ](http://seclists.org/oss-sec/2014/q3/650) .

I bug di Bash sono stati limitati per i prodotti Google Cloud Platform, ad
eccezione delle immagini di sistema operativo guest Compute Engine precedenti
al 26-09-2014. Di seguito sono riportati i passaggi per limitare i bug delle
immagini di Compute Engine.

####  Impatto di Compute Engine

Questo bug potrebbe interessare praticamente tutti i siti web che utilizzano
script CGI. Inoltre, è probabile che interessi quelli che utilizzano PHP,
Perl, Python, SSI, Java, C++ e servlet simili che non eseguono mai comandi di
shell tramite chiamate come ` popen ` , ` system ` , ` shell_exec ` o API di
questo tipo. Potrebbe interessare anche i sistemi che tentano di consentire
l'accesso controllato a utenti con restrizioni mediante meccanismi come la
limitazione dei comandi SSH o la shell con restrizione Bash.

**Aggiornamento (29-09-2014):**

In alternativa all'esecuzione dei comandi di aggiornamento manuale riportati
di seguito, gli utenti adesso possono ricreare le proprie istanze con immagini
che mitigano l'impatto di altre vulnerabilità relative al bug sulla sicurezza
di Bash, tra cui: [ CVE-2014-7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) , [
CVE-2014-6277 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277)
, [ CVE-2014-6278
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278) , [
CVE-2014-7186 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186)
e [ CVE-2014-7187
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187) . Utilizza le
nuove immagini seguenti per ricreare le istanze:

  * ` centos-6-v20140926 `
  * ` centos-7-v20140926 `
  * ` debian-7-wheezy-v20140926 `
  * ` backports-debian-7-wheezy-v20140926 `
  * ` rhel-6-v20140926 `

**Aggiornamento (25-09-2014):**

Adesso gli utenti possono scegliere di ricreare le proprie istanze invece di
eseguire un aggiornamento manuale. Per ricreare le istanze, utilizza le nuove
immagini seguenti che contengono le correzioni per questo bug sulla sicurezza:

  * ` backports-debian-7-wheezy-v20140924 `
  * ` debian-7-wheezy-v20140924 `
  * ` rhel-6-v20140924 `
  * ` centos-6-v20140924 `
  * ` centos-7-v20140924 `

Per le immagini RHEL e SUSE puoi anche effettuare manualmente gli
aggiornamenti eseguendo sulle istanze i comandi seguenti:

    
    
    
    # RHEL instances
    user@my-instance:~$ sudo yum -y upgrade
    
    # SUSE instances
    user@my-instance:~$ sudo zypper --non-interactive up

**Bollettino originale:**

Ti consigliamo di eseguire l'upgrade delle tue distribuzioni Linux. Per le
istanze che utilizzano Debian puoi effettuare un aggiornamento eseguendo
nell'istanza i comandi seguenti:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    

Per le istanze CentOS:

    
    
    
    user@my-instance:~$ sudo yum -y upgrade

Per informazioni dettagliate, consulta l'annuncio per la rispettiva
distribuzione Linux:

  * Patch originali: [ http://ftp.gnu.org/gnu/bash/ ](http://ftp.gnu.org/gnu/bash/) (controlla l'ultima voce in *-patches per la versione appropriata) 
  * Debian: [ [SECURITY] [DSA 3032-1] aggiornamento sulla sicurezza Bash ](https://lists.debian.org/debian-security-announce/2014/msg00220.html)
  * RHEL: 
    * [ RHSA-2014:1293-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00048.html)
    * [ RHSA-2014:1294-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00049.html)
  * CentOS 5: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020582.html)
  * CentOS 6: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020585.html)
  * CentOS 7: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020583.html)

|  Alta  |  [ CVE-2014-7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) , [
CVE-2014-6271 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6271)
, [ CVE-2014-6277
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277) , [
CVE-2014-6278 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278)
[ CVE-2014-7186
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186) , [
CVE-2014-7187 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)  
  
##  Data di pubblicazione: 25-07-2014

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

[ Elasticsearch Logstash ](http://www.elasticsearch.org/overview/logstash/) è
vulnerabile ad attacchi di tipo command injection sul sistema operativo che
possono causare modifiche non autorizzate e divulgazione dei dati. Un utente
malintenzionato può inviare eventi generati appositamente a qualsiasi origine
dati di Logstash in modo da eseguire comandi con le autorizzazioni del
processo Logstash.

####  Impatto di Compute Engine

Questa vulnerabilità influisce su tutte le istanze Compute Engine che eseguono
versioni di Elasticsearch Logstash precedenti alla 1.4.2 in cui sono abilitati
gli output zabbix o nagios_nsca. Per impedire gli attacchi, puoi:

  * Eseguire l'upgrade a Logstash 1.4.2 
  * Applicare la patch per le versioni 1.3.x 
  * Disabilitare gli output ` zabbix ` e ` nagios_nsca ` . 

Consulta il [ blog di Logstash
](http://www.elasticsearch.org/blog/logstash-1-4-2/) per ulteriori
informazioni.

Elasticsearch consiglia anche di [ utilizzare un firewall
](http://www.elasticsearch.org/blog/scripting-security/) per impedire
l'accesso remoto da IP non attendibili.

|  Alta  |  [ CVE-2014-4326
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-4326)  
  
##  Data di pubblicazione: 18-06-2014

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

Vogliamo dedicare qualche minuto alla risposta a eventuali dubbi da parte dei
clienti circa la sicurezza dei container Docker eseguiti su Google Cloud
Platform. Sono inclusi i clienti che utilizzano le nostre estensioni Google
App Engine a supporto di container Docker, macchine virtuali ottimizzate per i
container o scheduler di Kubernetes open source.

Docker ha lavorato egregiamente per risolvere il problema e puoi leggere [ qui
](http://blog.docker.com/2014/06/docker-container-breakout-proof-of-concept-
exploit/) la risposta nel suo blog. Tieni presente che, come viene detto nella
risposta, il problema interessa solo Docker 0.11 e una versione precedente di
pre-produzione.

Mentre il mondo sta pensando alla sicurezza dei container, vorremmo
sottolineare che in Google Cloud Platform, le soluzioni basate su container di
applicazioni Linux (in particolare i container Docker) funzionano su macchine
virtuali complete (Compute Engine). Pur supportando gli sforzi della community
Docker per rafforzare la protezione dello stack di container per applicazioni
Linux, ci rendiamo conto che si tratta di una tecnologia nuova con una
superficie di attacco molto ampia. Siamo convinti che, per ora, gli hypervisor
completi (macchine virtuali) hanno una superficie di attacco più compatta e
difendibile. Le macchine virtuali sono state progettate sin dall'inizio per
isolare i carichi di lavoro dannosi e ridurre al minimo la probabilità e
l'impatto di un bug del codice.

I nostri clienti possono essere sicuri che esiste la "barriera" tra di un
hypervisor completo tra loro e il codice potenzialmente dannoso di terze
parti. Se dovessimo giungere alla conclusione che lo stack di container per
applicazioni Linux è abbastanza solido da supportare carichi di lavoro multi-
tenant, lo faremo sapere alla community. Per ora, i container per applicazioni
Linux non sostituiscono le macchine virtuali. È un modo per ottenere molto di
più.

|  Bassa  |  [ Post del blog di Docker
](http://blog.docker.com/2014/06/docker-container-breakout-proof-of-concept-
exploit/)  
  
##  Data di pubblicazione: 05-06-2014

**Ultimo aggiornamento: 09-06-2014**

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

OpenSSL ha un problema per il quale i messaggi ` ChangeCipherSpec ` non
vengono associati correttamente alla macchina per lo stato dell'handshake. Ciò
ne consente l'inserimento anticipato nell'handshake. Un utente malintenzionato
potrebbe sfruttare un handshake generato appositamente per forzare l'uso di
materiale per le chiavi vulnerabile nei client e nei server SSL/TLS OpenSSL.
Ciò potrebbe esporre il sistema ad attacchi di tipo man-in-the-middle (MITM)
in cui un utente malintenzionato può decriptare e modificare il traffico
proveniente dal client e dal server attaccati.

Questo problema è identificato come [ CVE-2014-0224
](https://www.openssl.org/news/secadv/20140605.txt) . Il team OpenSSL ha
risolto il problema e ha avvisato la community OpenSSL di aggiornare OpenSSL.

####  Impatto di Compute Engine

Questa vulnerabilità interessa tutte le istanze di Compute Engine che
utilizzano OpenSSL, inclusi Debian, CentOS, Red Hat Enterprise Linux e SUSE
Linux Enterprise Server. Puoi aggiornare le istanze ricreandole con nuove
immagini oppure aggiornando manualmente i pacchetti nelle istanze.

**Aggiornamento (09-06-2014):** per aggiornare con nuove immagini le istanze
che eseguono SUSE Linux Enterprise Server, ricreale utilizzando le immagini
con le versioni indicate di seguito o successive:

  * ` sles-11-sp3-v20140609 `

**Post originale:**

Per aggiornare le istanze Debian e CentOS mediante nuove immagini, ricreale
utilizzando le immagini con le versioni indicate di seguito o successive:

  * ` debian-7-wheezy-v20140605 `
  * ` backports-debian-7-wheezy-v20140605 `
  * ` centos-6-v20140605 `
  * ` rhel-6-v20140605 `

Per aggiornare manualmente OpenSSL sulle istanze, esegui i comandi riportati
di seguito per aggiornare i pacchetti appropriati. Per le istanze che
utilizzano CentOS e RHEL, puoi aggiornare OpenSSL eseguendo nell'istanza i
comandi seguenti:

    
    
    
    user@my-instance:~$ sudo yum -y update
    user@my-instance:~$ sudo reboot

Per le istanze che utilizzano Debian, puoi aggiornare OpenSSL eseguendo
nell'istanza i comandi seguenti:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

Per le istanze che utilizzano SUSE Linux Enterprise Server, puoi assicurarti
che OpenSSL sia aggiornato eseguendo nell'istanza i comandi seguenti:

    
    
    
    user@my-instance:~$ sudo zypper --non-interactive up
    user@my-instance:~$ sudo reboot

|  Media  |  [ CVE-2014-0224
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0224)  
  
##  Data di pubblicazione: 08-04-2014

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

Le implementazioni (1) TLS e (2) DTLS in OpenSSL 1.0.1 prima di 1.0.1g non
gestiscono correttamente i pacchetti Heartbeat Extension, il che consente a un
utente malintenzionato di ottenere in remoto informazioni sensibili dalla
memoria del processo mediante pacchetti creati appositamente che attivano una
sovralettura del buffer, come dimostrato dalla lettura delle chiavi private,
relativamente a ` d1_both.c ` e ` t1_lib.c ` (detto anche bug Heartbleed).

####  Impatto di Compute Engine

Questa vulnerabilità interessa tutte le istanze Compute Engine Debian, RHEL e
CentOS in cui non è installata la versione più aggiornata di OpenSSL. Puoi
aggiornare le istanze ricreandole con nuove immagini oppure aggiornando
manualmente i pacchetti nelle istanze.

Per aggiornare le istanze mediante nuove immagini, ricreale utilizzando le
immagini con le versioni indicate di seguito o successive:

  * ` debian-7-wheezy-v20140408 `
  * ` backports-debian-7-wheezy-v20140408 `
  * ` centos-6-v20140408 `
  * ` rhel-6-v20140408 `

Per aggiornare manualmente OpenSSL sulle istanze, esegui i comandi riportati
di seguito per aggiornare i pacchetti appropriati. Per le istanze che
utilizzano CentOS e RHEL, puoi assicurarti che OpenSSL sia aggiornato
eseguendo nell'istanza i comandi seguenti:

    
    
    
    user@my-instance:~$ sudo yum update
    user@my-instance:~$ sudo reboot

Per le istanze che utilizzano Debian, puoi aggiornare OpenSSL eseguendo
nell'istanza i comandi seguenti:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get upgrade
    user@my-instance:~$ sudo reboot

Le istanze che utilizzano SUSE Linux non sono interessate.

**Aggiornamento del 14 aprile 2014:** alla luce di un nuovo studio
sull'estrazione delle chiavi mediante il bug Heartbleed, ai clienti di Compute
Engine viene consigliato di creare nuove chiavi per tutti i servizi SSL
interessati.

|  Media  |  [ CVE-2014-0160
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0160)  
  
##  Data di pubblicazione: 07-06-2013

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

**Nota:** questa vulnerabilità riguarda solo i kernel, che sono stati resi
obsoleti e sono stati rimossi a partire dalla versione v1 dell'API.

La vulnerabilità di stringa di formato nella funzione ` b43_request_firmware `
in ` drivers/net/wireless/b43/main.c ` nel driver wireless Broadcom B43 del
kernel Linux fino alla versione 3.9.4 consente agli utenti locali di ottenere
privilegi sfruttando l'accesso root e includendo specificatori di stringa di
formato in un parametro modprobe ` fwpostfix ` , il che causa la generazione
impropria di un messaggio di errore.

####  Impatto di Compute Engine

Questa vulnerabilità riguarda tutti i kernel Compute Engine precedenti alla
versione ` gcg-3.3.8-201305291443 ` . In risposta a questa vulnerabilità,
Compute Engine ha reso obsoleti tutti i kernel precedenti e consiglia agli
utenti di aggiornare le proprie istanze e immagini in modo da utilizzare il
kernel ` gce-v20130603 ` di Compute Engine. ` gce-v20130603 ` contiene il
kernel ` gcg-3.3.8-201305291443 ` , al quale è applicata la patch per questa
vulnerabilità.

Per sapere quale versione kernel è utilizzata dall'istanza:

  1. Utilizza SSH per accedere all'istanza 
  2. Esegui ` uname -r `

|  Media  |  [ CVE-2013-2852
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2852)  
  
##  Data di pubblicazione: 07-06-2013

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

**Nota:** questa vulnerabilità riguarda solo i kernel, che sono stati resi
obsoleti e sono stati rimossi a partire dalla versione v1 dell'API.

La vulnerabilità di stringa di formato nella funzione register_disk in `
block/genhd.c ` del kernel Linux fino alla versione 3.9.4 consente agli utenti
locali di ottenere privilegi sfruttando l'accesso root e scrivendo
specificatori di stringa di formato in `
/sys/module/md_mod/parameters/new_array ` per creare un nome di dispositivo `
/dev/md ` generato appositamente.

####  Impatto di Compute Engine

Questa vulnerabilità riguarda tutti i kernel Compute Engine precedenti alla
versione ` gcg-3.3.8-201305291443 ` . In risposta a questa vulnerabilità,
Compute Engine ha reso obsoleti tutti i kernel precedenti e consiglia agli
utenti di aggiornare le proprie istanze e immagini in modo da utilizzare il
kernel ` gce-v20130603 ` di Compute Engine. ` gce-v20130603 ` contiene il
kernel ` gcg-3.3.8-201305291443 ` , al quale è applicata la patch per questa
vulnerabilità.

Per sapere quale versione kernel è utilizzata dall'istanza:

  1. Utilizza SSH per accedere all'istanza 
  2. Esegui ` uname -r `

|  Media  |  [ CVE-2013-2851
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2851)  
  
##  Data di pubblicazione: 14-05-2013

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

**Nota:** questa vulnerabilità riguarda solo i kernel, che sono stati resi
obsoleti e sono stati rimossi a partire dalla versione v1 dell'API.

La funzione perf_swevent_init in ` kernel/events/core.c ` del kernel Linux
prima della versione 3.8.9 utilizza un tipo di dati ` integer ` errato, il che
consente agli utenti locali di ottenere privilegi mediante una chiamata di
sistema ` perf_event_open ` creata appositamente.

####  Impatto di Compute Engine

Questa vulnerabilità riguarda tutti i kernel Compute Engine precedenti alla
versione ` gcg-3.3.8-201305211623 ` . In risposta a questa vulnerabilità,
Compute Engine ha reso obsoleti tutti i kernel precedenti e consiglia agli
utenti di aggiornare le proprie istanze e immagini in modo da utilizzare il
kernel ` gce-v20130521 ` di Compute Engine. ` gce-v20130521 ` contiene il
kernel ` gcg-3.3.8-201305211623 ` , al quale è applicata la patch per questa
vulnerabilità.

Per sapere quale versione kernel è utilizzata dall'istanza:

  1. Utilizza SSH per accedere all'istanza 
  2. Esegui ` uname -r `

|  Alta  |  [ CVE-2013-2094
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2094)  
  
##  Data di pubblicazione: 18-02-2013

Descrizione  |  Gravità  |  Note  
---|---|---  
  
####  Descrizione

**Nota:** questa vulnerabilità riguarda solo i kernel, che sono stati resi
obsoleti e sono stati rimossi a partire dalla versione v1 dell'API.

La race condition nella funzionalità ptrace del kernel Linux prima della
versione 3.7.5 consente agli utenti locali di ottenere privilegi mediante una
chiamata di sistema ` PTRACE_SETREGS ptrace ` in un'applicazione creata
appositamente.

####  Impatto di Compute Engine

Questa vulnerabilità riguarda tutti i kernel Compute Engine ` 2.6.x-gcg- _
<date> _ ` . In risposta a questa vulnerabilità, Compute Engine ha reso
obsoleti tutti i kernel 2.6.x e consiglia agli utenti di aggiornare le proprie
istanze e immagini in modo da utilizzare il kernel ` gce-v20130225 ` di
Compute Engine. ` gce-v20130225 ` contiene il kernel ` 3.3.8-gcg-201302081521
` , al quale è applicata la patch per questa vulnerabilità.

Per sapere quale versione kernel è utilizzata dall'istanza:

  1. Utilizza SSH per accedere all'istanza 
  2. Esegui ` uname -r `

|  Media  |  [ CVE-2013-0871
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-0871)

