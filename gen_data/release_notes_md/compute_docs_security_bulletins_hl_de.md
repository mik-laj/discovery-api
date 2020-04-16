#  Sicherheitsbulletins

Von Zeit zu Zeit veröffentlichen wir Sicherheitsbulletins im Zusammenhang mit
Compute Engine. Sämtliche Sicherheitsbulletins zu Compute Engine sind hier
beschrieben.

[ Compute Engine-Sicherheitsbulletins abonnieren
![Abonnieren](https://cloud.google.com/images/feed-icon.png?hl=de)
](https://cloud.google.com/feeds/compute-engine-security-bulletins.xml?hl=de)

##  Veröffentlichungsdatum: 18.06.2019

**Zuletzt aktualisiert: 25.06.2019, 6:30 Uhr (UTC -8)**

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

Netflix hat vor Kurzem drei TCP-Sicherheitslücken in Linux-Kernels
offengelegt:

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

Diese CVEs (Common Vulnerabilities and Exposures) werden zusammen als [
NFLX-2019-001 ](https://github.com/Netflix/security-
bulletins/blob/master/advisories/third-party/2019-001.md) bezeichnet.

####  Auswirkungen auf Compute Engine

Die Infrastruktur, auf der Compute Engine gehostet wird, ist vor dieser
Sicherheitslücke geschützt.

Compute Engine-VMs sind für diesen DoS-Angriff nur dann anfällig, wenn auf
ihnen nicht gepatchte Linux-Betriebssysteme ausgeführt werden und sie nicht
vertrauenswürdigen Netzwerktraffic senden oder empfangen. Aktualisieren Sie
diese VM-Instanzen so bald wie möglich, wenn Patches für die Betriebssysteme
dieser Instanzen verfügbar sind.

Auf Load-Balancern, die TCP-Verbindungen beenden, wurde diese Sicherheitslücke
geschlossen. Compute Engine-Instanzen, die über diese Load-Balancer
ausschließlich nicht vertrauenswürdigen Traffic empfangen, sind nicht
anfällig. Dazu zählen HTTP-Load-Balancer, SSL-Proxy-Load-Balancer und TCP-
Proxy-Load-Balancer.

Netzwerk-Load-Balancer und interne Load-Balancer beenden TCP-Verbindungen
nicht. Nicht gepatchte Compute Engine-Instanzen, die nicht vertrauenswürdigen
Traffic über diese Load-Balancer empfangen, sind anfällig.

####  Gepatchte Images und Anbieterressourcen

Sobald die jeweiligen Betriebssystemanbieter Patchinformationen zur Verfügung
gestellt haben, finden Sie auf dieser Seite entsprechende Links sowie den
aktuellen Status zu diesen CVEs. Frühere Versionen dieser öffentlichen Images
enthalten diese Patches nicht und können die Wirkung potenzieller Angriffe
nicht abschwächen.

  * Projekt ` debian-cloud ` : 
    * ` debian-9-stretch-v20190618 `
  * Projekt ` centos-cloud ` : 
    * ` centos-6-v20190619 `
    * ` centos-7-v20190619 `
  * Projekt ` cos-cloud ` : 
    * ` cos-dev-77-12293-0-0 `
    * ` cos-beta-76-12239-21-0 `
    * ` cos-stable-75-12105-77-0 `
    * ` cos-73-11647-217-0 `
    * ` cos-69-10895-277-0 `
  * Projekt ` coreos-cloud ` : 
    * ` coreos-alpha-2163-2-1-v20190617 `
    * ` coreos-beta-2135-3-1-v20190617 `
    * ` coreos-stable-2079-6-0-v20190617 `
  * Projekt ` rhel-cloud ` : 
    * ` rhel-6-v20190618 `
    * ` rhel-7-v20190618 `
    * ` rhel-8-v20190618 `
  * Projekt ` rhel-sap-cloud ` : 
    * ` rhel-7-4-sap-v20190618 `
    * ` rhel-7-6-sap-v20190618 `
  * Projekt ` suse-cloud ` : 
    * ` sles-12-sp4-v20190617 `
    * ` sles-15-v20190617 `
  * Projekt ` suse-sap-cloud ` : 
    * ` sles-12-sp1-sap-v20190617 `
    * ` sles-12-sp2-sap-v20190617 `
    * ` sles-12-sp3-sap-v20190617 `
    * ` sles-12-sp4-sap-v20190617 `
    * ` sles-15-sap-v20190617 `
  * Projekt ` ubuntu-cloud ` : 
    * ` ubuntu-1604-xenial-v20190617 `
    * ` ubuntu-1804-bionic-v20190617 `
    * ` ubuntu-1810-cosmic-v20190618 `
    * ` ubuntu-1904-disco-v20190619 `
    * ` ubuntu-minimal-1604-xenial-v20190618 `
    * ` ubuntu-minimal-1804-bionic-v20190617 `
    * ` ubuntu-minimal-1810-cosmic-v20190618 `
    * ` ubuntu-minimal-1904-disco-v20190618 `

|  Mittel  |

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

  
  
##  Veröffentlichungsdatum: 14.05.2019

**Zuletzt aktualisiert: 20.05.2019, 17:00 Uhr (UTC -8)**

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

Die folgenden CVEs (Common Vulnerabilities and Exposures) wurden von Intel
offengelegt:

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

Diese CVEs werden zusammen als Microarchitectural Data Sampling (MDS)
bezeichnet. Diese Sicherheitslücken bringen das Risiko mit sich, dass Daten
Angriffen ausgesetzt sind, die durch Interaktion einer spekulativen Ausführung
mit dem mikroarchitektonischen Status erfolgen.

####  Auswirkungen auf Compute Engine

**Die Hostinfrastruktur, auf der Compute Engine ausgeführt wird, dient dazu,
Arbeitslasten von Kunden voneinander zu isolieren. Sofern Sie keinen nicht
vertrauenswürdigen Code auf den VMs ausführen, sind keine weiteren
Gegenmaßnahmen erforderlich.**

Kunden, die auf virtuellen Maschinen von Compute Engine für ihre eigenen
Dienste mit mehreren Mandanten nicht vertrauenswürdigen Code ausführen,
sollten sich an die empfohlenen Maßnahmen zur Risikominderung halten, die der
Anbieter ihres Gastbetriebssystems vorsieht. Diese Gegenmaßnahmen umfassen
unter Umständen den Einsatz von Microcode-Funktionen von Intel. Für die neue
Flush-Funktionalität haben wir einen Zugang für Gäste eingerichtet. Im
Folgenden finden Sie eine Zusammenfassung der Schritte, die als Abhilfe für
übliche Gäste-Images zur Verfügung stehen.

####  Gepatchte Images und Anbieterressourcen

Sobald die jeweiligen Betriebssystemanbieter Patchinformationen zur Verfügung
gestellt haben, finden Sie auf dieser Seite entsprechende Links sowie den
aktuellen Status zu diesen CVEs. Diese Images dienen dazu, VM-Instanzen erneut
zu erstellen. Frühere Versionen dieser öffentlichen Images enthalten diese
Patches nicht und können die Wirkung potenzieller Angriffe nicht abschwächen.

  * Projekt ` centos-cloud ` : [ CESA-2019:1169 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023309.html) , [ CESA-2019:1168 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023314.html)
    * ` centos-6-v20190515 `
    * ` centos-7-v20190515 `
  * Projekt ` coreos-cloud ` : [ MDS-Strategien zur Risikominderung für CoreOS Container Linux ](https://coreos.com/os/docs/latest/disabling-smt.html)
    * ` coreos-stable-2079-4-0-v20190515 `
    * ` coreos-beta-2107-3-0-v20190515 `
    * ` coreos-alpha-2135-1-0-v20190515 `
  * Projekt ` cos-cloud `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
  * Projekt ` debian-cloud ` : [ DSA-4444 ](https://www.debian.org/security/2019/dsa-4444)
    * ` debian-9-stretch-v20190514 `
  * Projekt ` rhel-cloud ` : [ Informationsartikel zu Red Hat MDS ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-6-v20190515 `
    * ` rhel-7-v20190517 `
    * ` rhel-8-v20190515 `
  * Projekt ` rhel-sap-cloud ` : [ Informationsartikel zu Red Hat MDS ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-7-4-sap-v20190515 `
    * ` rhel-7-6-sap-v20190517 `
  * Projekt ` suse-cloud ` : [ SUSE MDS KB ](https://www.suse.com/support/kb/doc/?id=7023736)
    * ` sles-12-sp4-v20190520 `
    * ` sles-15-v20190520 `
  * Projekt ` suse-sap-cloud `
    * ` sles-12-sp4-sap-v20190520 `
    * ` sles-15-sap-v20190520 `
  * Projekt ` ubuntu-os-cloud ` : [ Wiki zu Ubuntu MDS ](https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/MDS)
    * ` ubuntu-1404-trusty-v20190514 `
    * ` ubuntu-1604-xenial-v20190514 `
    * ` ubuntu-1804-bionic-v20190514 `
    * ` ubuntu-1810-cosmic-v20190514 `
    * ` ubuntu-1904-disco-v20190514 `
    * ` ubuntu-minimal-1604-xenial-v20190514 `
    * ` ubuntu-minimal-1804-bionic-v20190514 `
    * ` ubuntu-minimal-1810-cosmic-v20190514 `
    * ` ubuntu-minimal-1904-disco-v20190514 `
  * Projekte ` windows-cloud ` und ` windows-sql-cloud ` : [ Microsoft ADV190013 ](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/ADV190013)
    * Alle öffentlichen Images von Windows Server und SQL Server mit der Versionsnummer ` v20190514 ` . 
  * Projekt ` gce-uefi-images `
    * ` centos-7-v20190515 `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
    * ` rhel-7-v20190517 `
    * ` ubuntu-1804-bionic-v20190514 `
    * Alle öffentlichen Images von Windows Server mit der Versionsnummer ` v20190514 ` . 

####  Container-Optimized OS

Wenn Sie als Gästebetriebssystem Container-Optimized OS nutzen und auf den
virtuellen Maschinen nicht vertrauenswürdige Arbeitslasten mit mehreren
Mandanten ausführen, empfehlen wir folgendes Vorgehen:

  1. Deaktivieren Sie das Hyper-Threading, indem Sie in der Kernel-Befehlszeile ` nosmt ` festlegen.   

Bei bestehenden COS-VMs können Sie ` grub.cfg ` wie folgt modifizieren, um die
Option ` nosmt ` festzulegen und das System anschließend neu zu starten:

    
        
    # Run as root:
    dir="$(mktemp -d)"
    mount /dev/sda12 "${dir}"
    sed -i -e "s|cros_efi|cros_efi nosmt|g" "${dir}/efi/boot/grub.cfg"
    umount "${dir}"
    rmdir "${dir}"
    
    reboot

Zur Vereinfachung können Sie das folgende Skript ausführen, um dasselbe
Ergebnis zu erzielen wie mit den oben aufgeführten Befehlen. Wir empfehlen,
dieses Skript in Ihre Cloud-Konfiguration, Startskripts oder Instanzvorlagen
aufzunehmen, damit diese neuen Parameter für neue VMs verwendet werden. Unten
ist ein Beispiel für eine Cloud-Konfiguration aufgeführt, die dieses Skript
ausführt.

**Warnung:** Dieser Befehl führt beim erstmaligen Ausführen dazu, dass die
Instanz sofort neu gestartet wird. Wird der Befehl anschließend mit einer
Instanz wiederholt, bei der das Hyper-Threading bereits deaktiviert ist, hat
dies keine Auswirkungen.

    
        
    # Run as root
    /bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)
    

Als Bestandteil der Cloud-Konfiguration sieht dies so aus:

    
        
    #cloud-config
    
    bootcmd:
    - /bin/bash -c "/bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)"
    

Sehen Sie sich die Ausgabe der Dateien ` /sys/devices/system/cpu/smt/active `
und ` /sys/devices/system/cpu/smt/control ` an, um zu überprüfen, ob das
Hyper-Threading deaktiviert ist. Wird ` 0 ` für ` active ` und ` off ` für `
control ` zurückgegeben, ist das Hyper-Threading deaktiviert:

    
        
    cat /sys/devices/system/cpu/smt/active
    cat /sys/devices/system/cpu/smt/control
    

**Hinweis** : Falls Sie auf Ihrer Instanz UEFI Secure Boot aktiviert haben,
müssen Sie die Instanz noch einmal mit deaktiviertem UEFI Secure Boot
erstellen, den oben aufgeführten Befehl bei deaktiviertem UEFI Secure Boot
ausführen und dann UEFI Secure Boot auf der neuen Instanz aktivieren.

  2. Verwenden Sie die neue Version des COS-Images   

Zusätzlich zum Deaktivieren des Hyper-Threading wie oben beschrieben sollten
Sie auch die [ Instanzen neu erstellen
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=de#publicimage) , und zwar mit den oben aufgeführten
aktualisierten Images oder neueren Versionen der Images mit Container-
Optimized OS (sofern verfügbar), damit dort, wo die Sicherheitslücke besteht,
ein vollständiger Schutz hergestellt wird.

|  Mittel  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  Veröffentlichungsdatum: 14.08.2018

**Zuletzt aktualisiert: 20.08.2018, 17:00 Uhr (UTC -8)**

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

Die folgenden CVEs (Common Vulnerabilities and Exposures) wurden [ von Intel
offengelegt ](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) :

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) (für [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (für Betriebssysteme und [ SMT ](https://en.wikipedia.org/wiki/Hyper-Threading) ) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (für Virtualisierung) 

Diese CVEs werden zusammenfassend als "L1 Terminal Fault (L1TF)" bezeichnet.

Durch diese L1TF-Sicherheitslücken wird die spekulative Ausführung des
Prozessors dazu genutzt, Angriffe auf die Konfiguration von Datenstrukturen
auf Prozessorebene durchzuführen. "L1" bezeichnet den Level-1-Datencache
(L1D), eine kleine On-Core-Ressource, die zur Beschleunigung des
Speicherzugriffs verwendet wird.

Weitere Informationen zu diesen Sicherheitslücken und den entsprechenden
Gegenmaßnahmen in Compute Engine erhalten Sie im [ Google Cloud-Blogpost
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=de) .

####  Auswirkungen auf Compute Engine

Die Hostinfrastruktur, auf der Compute Engine ausgeführt wird, und die die
Arbeitslasten von Kunden voneinander isoliert, ist vor bekannten Angriffen
geschützt.

Kunden von Compute Engine wird empfohlen, ihre Images zu aktualisieren, um
mögliche indirekte Angriffe auf ihre Gastumgebungen zu verhindern. Dies ist
insbesondere für Kunden wichtig, die ihre eigenen mandantenfähigen Dienste auf
virtuellen Maschinen in Compute Engine ausführen.

Kunden von Google Compute Engine können die Gastbetriebssysteme auf ihren
Instanzen über eine der folgenden Optionen aktualisieren:

  * Verwenden Sie gepatchte öffentliche Images, [ um vorhandene VM-Instanzen neu zu erstellen ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=de#publicimage) . 
  * Installieren Sie auf vorhandenen Instanzen vom Betriebssystemanbieter bereitgestellte Patches und starten Sie die gepatchten Instanzen neu. 

####  Gepatchte Images und Anbieterressourcen

Sobald die jeweiligen Betriebssystemanbieter Patchinformationen zur Verfügung
gestellt haben, finden Sie auf dieser Seite entsprechende Links sowie den
aktuellen Status zu den beiden CVEs. Verwenden Sie diese Images, um Ihre VM-
Instanzen neu zu erstellen. Frühere Versionen dieser öffentlichen Images
enthalten diese Patches nicht und können die Wirkung potenzieller Angriffe
nicht abschwächen.

  * Projekt ` centos-cloud ` : 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * Projekt ` coreos-cloud ` : 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * Projekt ` cos-cloud ` : 
    * ` cos-stable-66-10452-110-0 `
    * ` cos-stable-67-10575-66-0 `
    * ` cos-beta-68-10718-81-0 `
    * ` cos-dev-69-10895-23-0 `
  * Projekt ` debian-cloud ` : 
    * ` debian-9-stretch-v20180820 `
  * Projekt ` rhel-cloud ` : 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * Projekt ` rhel-sap-cloud ` : 
    * ` rhel-7-sap-apps-v20180814 `
    * ` rhel-7-sap-hana-v20180814 `
  * Projekt ` suse-cloud ` : 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
    * ` sles-11-sp4-v20180816 `
  * Projekt ` suse-sap-cloud ` : 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * Projekt ` ubuntu-os-cloud ` : 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `
  * Projekte ` windows-cloud ` ` gce-uefi-images ` und ` windows-sql-cloud ` : 
    * Alle [ öffentlichen Images ](https://cloud.google.com/compute/docs/images?hl=de#os-compute-support) von Windows Server und SQL Server mit der Versionsnummer ` -v201800814 ` und höher enthalten Patches. 

|  Hoch  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  Veröffentlichungsdatum: 06.08.2018

**Zuletzt aktualisiert: 05.09.2018, 17:00 Uhr (UTC -8)**

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Aktualisierung vom 05.09.2018

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) wurde am 14.08.2018 von US-CERT
offengelegt. Wie bei [ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) handelt es sich um eine
Netzwerksicherheitslücke auf Kernelebene, durch die die Effektivität von DoS-
Angriffen (Denial of Service) auf anfällige Systeme erhöht wird. Der
Hauptunterschied besteht darin, dass CVE-2018-5391 über IP-Verbindungen
ausgenutzt werden kann. Wir haben dieses Bulletin so aktualisiert, dass beide
Sicherheitslücken angesprochen werden.

####  Beschreibung

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ("SegmentSmack") beschreibt eine Netzwerk-
Sicherheitslücke auf Kernelebene, durch die die Effektivität von DoS-Angriffen
(Denial of Service) über TCP-Verbindungen auf anfällige Systeme erhöht wird.

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ("FragmentSmack") beschreibt eine
Netzwerk-Sicherheitslücke auf Kernelebene, durch die die Effektivität von DoS-
Angriffen (Denial of Service) über IP-Verbindungen auf anfällige Systeme
erhöht wird.

####  Auswirkungen auf Compute Engine

Für die Hostinfrastruktur, auf der Compute Engine-VMs ausgeführt werden,
besteht kein Risiko. Die Netzwerkinfrastruktur, die den Traffic von und zu
Compute Engine-VMs handhabt, ist gegen diese Sicherheitslücke geschützt.
Compute Engine-VMs, die nicht vertrauenswürdigen Traffic ausschließlich über [
HTTP(S) ](https://cloud.google.com/load-balancing/docs/https/?hl=de) -, [ SSL
](https://cloud.google.com/load-balancing/docs/ssl/?hl=de) \- oder [ TCP-Load-
Balancer ](https://cloud.google.com/load-balancing/docs/tcp/?hl=de)
senden/empfangen, sind gegen diese Sicherheitslücke geschützt.

Compute Engine-VMs sind für diesen DoS-Angriff nur dann anfällig, wenn auf
ihnen nicht gepatchte Betriebssysteme ausgeführt werden und sie nicht
vertrauenswürdigen Netzwerktraffic direkt oder über [ Netzwerk-Load-Balancer
](https://cloud.google.com/load-balancing/docs/network/?hl=de)
senden/empfangen.

Aktualisieren Sie Ihre VM-Instanzen so bald wie möglich, wenn Patches für ihre
Betriebssysteme verfügbar sind.

Kunden von Compute Engine können die Gastbetriebssysteme auf ihren Instanzen
über eine der folgenden Optionen aktualisieren:

  * Verwenden Sie gepatchte öffentliche Images, [ um vorhandene VM-Instanzen neu zu erstellen ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=de#publicimage) . Unten finden Sie eine Liste der gepatchten öffentlichen Images. 
  * Installieren Sie auf vorhandenen Instanzen vom Betriebssystemanbieter bereitgestellte Patches und starten Sie die gepatchten Instanzen neu. 

####  Gepatchte Images und Anbieterressourcen

Sobald die jeweiligen Betriebssystemanbieter Patchinformationen zur Verfügung
gestellt haben, finden Sie auf dieser Seite entsprechende Links.

  * Projekt ` centos-cloud ` (nur CVE-2018-5390): 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * Projekt ` coreos-cloud ` (CVE-2018-5390 und CVE-2018-5391): 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * Projekt ` cos-cloud ` (CVE-2018-5390 und CVE-2018-5391): 
    * ` cos-stable-65-10323-98-0 `
    * ` cos-stable-66-10452-109-0 `
    * ` cos-stable-67-10575-65-0 `
    * ` cos-beta-68-10718-76-0 `
    * ` cos-dev-69-10895-16-0 `
  * Projekt ` debian-cloud ` (CVE-2018-5390 und CVE-2018-5391): 
    * ` debian-9-stretch-v20180814 `
  * Projekt ` rhel-cloud ` (nur CVE-2018-5390): 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * Projekt ` suse-cloud ` (CVE-2018-5390 und CVE-2018-5391): 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
  * Projekt ` suse-sap-cloud ` (CVE-2018-5390 und CVE-2018-5391): 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * Projekt ` ubuntu-os-cloud ` (CVE-2018-5390 und CVE-2018-5391): 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `

|  Hoch  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  Veröffentlichungsdatum: 03.01.2018

**Zuletzt aktualisiert: 21.05.2018, 15:00 Uhr (UTC -8)**

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Aktualisierung vom 21.05.2018

Die Sicherheitslücken [ CVE-2018-3640 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-3640) und [ CVE-2018-3639
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639) , Varianten 3a
bzw. 4, wurden [ von Intel offengelegt
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00115.html) . Wie bei den ersten drei Varianten von Spectre und Meltdown
ist die Infrastruktur geschützt, auf der Compute Engine-VM-Instanzen
ausgeführt werden, und VM-Instanzen von Kunden sind isoliert und voreinander
geschützt. Darüber hinaus plant das Team von Compute Engine, Microcode-Patches
von Intel in unserer Infrastruktur zu implementieren. Kunden, die
mandantenfähige oder nicht vertrauenswürdige Arbeitslasten in einer einzelnen
VM-Instanz ausführen, können dadurch innerhalb der VM zusätzliche
Gegenmaßnahmen ergreifen, wenn die Betriebssystemanbieter solche Maßnahmen
anbieten. Das Team von Compute Engine wird die Microcode-Patches
implementieren, sobald sie von Intel zertifiziert und von Compute Engine für
unsere Produktionsumgebung getestet und qualifiziert wurden. Auf dieser Seite
finden Sie genaue Zeitpläne und Neuigkeiten, sobald diese vorliegen.

####  Beschreibung

Diese CVEs sind Varianten einer neuen Angriffsklasse, die die in vielen
Prozessoren verfügbare Technologie der spekulativen Ausführung ausnutzen. Bei
dieser Klasse von Angriffen kann es unter verschiedenen Umständen zu einem
unberechtigten Lesezugriff auf Speicherdaten kommen.

Compute Engine nutzte die Live-Migrationstechnologie für virtuelle Maschinen,
um Hostsystem- und Hypervisor-Updates ohne Beteiligung der Nutzer, ohne
erzwungene Wartungsfenster und ohne erforderliche Massenneustarts
durchzuführen. Als Schutz vor dieser neuen Angriffsklasse müssen jedoch alle
Gastbetriebssysteme und -versionen gepatcht werden, unabhängig davon, wo diese
Systeme ausgeführt werden.

Der [ Project Zero-Blogpost
](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-
with-side.html) enthält umfassende technische Details zu dieser
Angriffsmethode. Im [ Google Security-Blogpost
](https://security.googleblog.com/2018/01/todays-cpu-vulnerability-what-you-
need.html) finden Sie ausführliche Informationen zu den Gegenmaßnahmen von
Google einschließlich aller produktspezifischen Angaben.

####  Auswirkungen auf Compute Engine

Die Infrastruktur, auf der Compute Engine läuft und die die VM-Instanzen von
Kunden voneinander isoliert, ist vor bekannten Angriffen geschützt. Unsere
Gegenmaßnahmen verhindern den unbefugten Zugriff auf unsere Hostsysteme durch
Anwendungen, die innerhalb von VM-Instanzen ausgeführt werden. Außerdem
verhindern sie den nicht autorisierten Zugriff von VM-Instanzen auf andere VM-
Instanzen, die auf demselben Hostsystem ausgeführt werden.

Um den nicht autorisierten Zugriff innerhalb Ihrer VM-Instanzen zu verhindern,
müssen Sie die Gastbetriebssysteme dieser Instanzen über eine der folgenden
Optionen aktualisieren:

  * Verwenden Sie gepatchte öffentliche Images, [ um Ihre vorhandenen VM-Instanzen neu zu erstellen ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=de#publicimage) . Unten finden Sie eine Liste der gepatchten öffentlichen Images. 
  * Installieren Sie in Ihren vorhandenen Instanzen Patches, die vom Betriebssystemanbieter für Ihre Distribution zur Verfügung gestellt werden, und starten Sie die gepatchten Instanzen neu. Unten finden Sie Links zu den Patchinformationen der einzelnen Betriebssystemanbieter. 

####  Gepatchte Images und Anbieterressourcen

**Hinweis** : Gepatchte Images enthalten möglicherweise nicht für alle CVEs,
die in diesem Sicherheitsbulletin aufgeführt sind, Fehlerkorrekturen. Darüber
hinaus können verschiedene Images unterschiedliche Methoden zum Verhindern
dieser Angriffsarten enthalten. Erkundigen Sie sich bei Ihrem
Betriebssystemanbieter, welche CVEs in den jeweiligen Patches behoben und
welche Präventionsmethoden verwendet werden.

  * Projekt ` cos-cloud ` : Enthält Patches, die Angriffe der Variante 2 ( [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715) ) und der Variante 3 ( [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754) ) verhindern. Google hat in diesen Images [ Retpoline ](https://support.google.com/faqs/answer/7625886?hl=de) verwendet, um Angriffe der Variante 2 abzuschwächen. 
    * ` cos-stable-63-10032-71-0 ` oder Image-Familie ` cos-stable `
  * Projekt ` centos-cloud ` : [ CentOS-Patchinformationen ](https://lwn.net/Alerts/CentOS/)
    * ` centos-7-v20180104 ` oder Image-Familie ` centos-7 `
    * ` centos-6-v20180104 ` oder Image-Familie ` centos-6 `
  * Projekt ` coreos-cloud ` : [ CoreOS-Patchinformationen ](https://coreos.com/blog/container-linux-meltdown-patch)
    * ` coreos-stable-1576-5-0-v20180105 ` oder Image-Familie ` coreos-stable `
    * ` coreos-beta-1632-1-0-v20180105 ` oder Image-Familie ` coreos-beta `
    * ` coreos-alpha-1649-0-0-v20180105 ` oder Image-Familie ` coreos-alpha `
  * Projekt ` debian-cloud ` : [ Debian-Patchinformationen ](https://www.debian.org/security/#DSAS)
    * ` debian-9-stretch-v20180105 ` oder Image-Familie ` debian-9 `
    * ` debian-8-jessie-v20180109 ` oder Image-Familie ` debian-8 `
  * Projekt ` rhel-cloud ` : [ RHEL-Patchinformationen ](https://access.redhat.com/security/vulnerabilities/speculativeexecution)
    * ` rhel-7-v20180104 ` oder Image-Familie ` rhel-7 `
    * ` rhel-6-v20180104 ` oder Image-Familie ` rhel-6 `
  * Projekt ` suse-cloud ` : [ SUSE-Patchinformationen ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-v20180104 ` oder Image-Familie ` sles-12 `
    * ` sles-11-sp4-v20180104 ` oder Image-Familie ` sles-11 `
  * Projekt ` suse-sap-cloud ` : [ SUSE-Patchinformationen ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-sap-v20180104 ` oder Image-Familie ` sles-12-sp3-sap `
    * ` sles-12-sp2-sap-v20180104 ` oder Image-Familie ` sles-12-sp2-sap `
  * Projekt ` ubuntu-os-cloud ` : [ Ubuntu-Patchinformationen ](https://insights.ubuntu.com/2018/01/04/ubuntu-updates-for-the-meltdown-spectre-vulnerabilities/)
    * ` ubuntu-1710-artful-v20180109 ` oder Image-Familie ` ubuntu-1710 `
    * ` ubuntu-1604-xenial-v20180109 ` oder Image-Familie ` ubuntu-1604-lts `
    * ` ubuntu-1404-trusty-v20180110 ` oder Image-Familie ` ubuntu-1404-lts `
  * Projekte ` windows-cloud ` und ` windows-sql-cloud ` : 
    * Alle [ öffentlichen Images ](https://cloud.google.com/compute/docs/images?hl=de#os-compute-support) von Windows Server und SQL Server mit der Versionsnummer ` -v20180109 ` und höher enthalten Patches. Sie müssen jedoch die von Microsoft im [ Windows Server-Leitfaden ](https://support.microsoft.com/en-gb/help/4072698/windows-server-guidance-to-protect-against-the-speculative-execution) gegebenen Empfehlungen befolgen, um diese Gegenmaßnahmen sowohl für vorhandene als auch für neu erstellte Instanzen zu aktivieren und zu überprüfen. 

Verwenden Sie diese Images, [ um Ihre VM-Instanzen neu zu erstellen
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=de#publicimage) . Frühere Versionen dieser öffentlichen Images
enthalten diese Patches nicht und können die Wirkung potenzieller Angriffe
nicht abschwächen.

####  Patches von Hardwareanbietern

NVIDIA bietet gepatchte Treiber zur Minimierung von möglichen Angriffen auf
Systeme mit installierter NVIDIA®-Treibersoftware. Welche Treiberversionen
gepatcht wurden, entnehmen Sie dem Sicherheitsbulletin zu [ Grafiktreiber-
Sicherheitsupdates für NVIDIA-GPUs
](http://nvidia.custhelp.com/app/answers/detail/a_id/4611) von NVIDIA.

####  Überarbeitungsverlauf:

  * 21.05.2018, 14:00 Uhr (UTC -8): Informationen zu zwei neuen Varianten hinzugefügt, die am 21. Mai 2018 offengelegt wurden. 
  * 11.01.2018, 15:00 Uhr (UTC -8): Informationen zu gepatchten öffentlichen Windows Server- und SQL Server-Images hinzugefügt. 
  * 10.01.2018, 10:15 Uhr (UTC -8): Mehrere Ubuntu-Images zur Liste der gepatchten öffentlichen Images hinzugefügt. 
  * 10.01.2018, 09:50 Uhr (UTC -8): Anleitung für Patches von Hardwareanbietern hinzugefügt. 
  * 03.01.2018 bis 09.01.2018: Liste der gepatchten öffentlichen Images mehrfach überarbeitet. 

|  Hoch  |

  * [ CVE-2017-5753 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5753)
  * [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715)
  * [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754)
  * [ CVE-2018-3640 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3640)
  * [ CVE-2018-3639 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639)

  
  
##  Veröffentlichungsdatum: 02.10.2017

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

[ Dnsmasq ](http://www.thekelleys.org.uk/dnsmasq/doc.html) bietet Funktionen
für DNS-, DHCP- und Router-Anzeigen sowie Netzwerkstarts. Diese Software ist
üblicherweise auf Systemen mit Desktop-Linux-Distributionen (z. B. Ubuntu),
Heimroutern und IoT-Geräten installiert. Dnsmasq wird sowohl im offenen
Internet als auch intern für private Netzwerke eingesetzt.

Google hat bei regelmäßigen internen Sicherheitsanalysen sieben verschiedene
Probleme entdeckt. Wir haben den Schweregrad dieser Probleme ermittelt und
anschließend untersucht, wie sie sich auswirken und wie sie ausgenutzt werden
können. Für jede einzelne Schwachstelle haben wir dann einen internen Proof of
Concept erarbeitet. Zusätzlich haben wir gemeinsam mit Simon Kelly, der
Dnsmasq betreut, entsprechende Patches entwickelt, um das Problem zu
entschärfen.

Während der Überprüfung fand unser Team drei Möglichkeiten zur
Remotecodeausführung, ein Datenleck und drei Denial-of-Service-Schwachstellen.
Diese betreffen die neueste Version vom 5. September 2017, die auf dem Git-
Server des Projekts liegt.

Die Patches wurden in das [ Git-Repository des Projekts
](http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=summary) eingepflegt.

####  Auswirkungen auf Compute Engine

Standardmäßig ist Dnsmasq nur in Images installiert, die [ NetworkManager
](https://wikipedia.org/wiki/NetworkManager) verwenden, und inaktiv. In den
folgenden öffentlichen Compute Engine-Images ist Dnsmasq installiert:

  * Ubuntu 16.04, 16.10, 17.04 
  * CentOS 7 
  * RHEL 7 

Bei anderen Images ist Dnsmasq jedoch möglicherweise als Abhängigkeit für
andere Pakete installiert. Wir empfehlen Ihnen, Ihre Debian-, Ubuntu-,
CentOS-, RHEL-, SLES- und OpenSuse-Instanzen auf die neuesten Betriebssystem-
Images zu aktualisieren. CoreOS und Container-Optimized OS sind nicht
betroffen. Windows-Images sind ebenfalls nicht betroffen.

Instanzen, auf denen Debian oder Ubuntu ausgeführt wird, können durch
Ausführung der folgenden Befehle auf der Instanz aktualisiert werden:

    
    
    
    sudo apt-get -y update
    
    
    
    sudo apt-get -y dist-upgrade

Für Red Hat Enterprise Linux- und CentOS-Instanzen führen Sie folgenden Befehl
aus:

    
    
    
    sudo yum -y upgrade

Für SLES- und OpenSUSE-Images führen Sie folgenden Befehl aus:

    
    
    
    sudo zypper up

Alternativ zur Ausführung der manuellen Aktualisierungsbefehle können Sie auch
[ VM-Instanzen mithilfe der Image-Familien des jeweiligen Betriebssystems neu
erstellen ](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=de#publicimage) .

|  Hoch  |

  * [ CVE-2017-14491 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14491)
  * [ CVE-2017-14492 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14492)
  * [ CVE-2017-14493 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14493)
  * [ CVE-2017-14494 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14494)
  * [ CVE-2017-14495 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14495)
  * [ CVE-2017-14496 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14496)
  * [ CVE-2017-13704 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-13704)

  
  
##  Veröffentlichungsdatum: 26.10.2016

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

CVE-2016-5195 bezieht sich auf eine Race-Bedingung bei der Handhabung von
schreibgeschützten privaten Speicherbereichen durch das Speichersubsystem des
Linux-Kernels bei Schreibzugriffen.

Ein nicht authentifizierter lokaler Nutzer könnte diese Schwachstelle nutzen,
um Schreibzugriff auf ansonsten schreibgeschützte Speicherbereiche zu
erhalten, und so seine Rechte auf dem System ausweiten.

Weitere Informationen finden Sie in der [ FAQ zu Dirty COW
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails) .

####  Auswirkungen auf Compute Engine

Alle Linux-Distributionen und ‑Versionen auf Compute Engine sind betroffen.
Von den meisten Instanzen wird automatisch ein neuerer Kernel heruntergeladen
und installiert. Zum Patchen laufender Systeme ist jedoch ein Neustart
erforderlich.

In den neuen oder neu erstellten Instanzen, die auf den folgenden Compute
Engine-Images basieren, sind bereits gepatchte Kernels installiert:

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

|  Hoch  |  [ CVE-2016-5195
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails)  
  
##  Veröffentlichungsdatum: 16.02.2016

**Zuletzt aktualisiert: 22.02.2016**

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

CVE-2015-7547 ist eine Sicherheitslücke, die dazu führt, dass der glibc-
basierte DNS-Resolver auf Clientseite Software für Pufferüberläufe auf dem
Stack anfällig macht, wenn die Bibliotheksfunktion ` getaddrinfo() ` verwendet
wird. Ein Angreifer kann Software kapern, indem er diese Funktion verwendet,
um die Sicherheitslücke mit von ihm kontrollierten Domainnamen oder DNS-
Servern bzw. über eine Man-in-the-Middle-Attacke auszunutzen.

Weitere Informationen finden Sie im [ Google-Blog zur Onlinesicherheit
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html) und in der Datenbank [ Common Vulnerabilities and
Exposures (CVE) ](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-7547)
.

####  Auswirkungen auf Compute Engine

**Aktualisierung (22.02.2016):**

Sie können Ihre Instanzen nun mit den folgenden CoreOS-, SLES- und OpenSUSE-
Images erstellen:

  * ` coreos-alpha-962-0-0-v20160218 `
  * ` coreos-beta-899-7-0-v20160218 `
  * ` coreos-stable-835-13-0-v20160218 `
  * ` opensuse-13-2-v20160222 `
  * ` opensuse-leap-42-1-v20160222 `
  * ` sles-11-sp4-v20160222 `
  * ` sles-12-sp1-v20160222 `

**Aktualisierung (17.02.2016):**

Sie können jetzt durch Ausführung der folgenden Befehle eine Aktualisierung
auf Ubuntu 12.04 LTS-, Ubuntu 14.04 LTS- und Ubuntu 15.10-Instanzen vornehmen:

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Als Alternative zur Ausführung der manuellen Aktualisierungsbefehle können Sie
jetzt mit folgenden neuen Images die Instanzen neu erstellen:

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

Uns sind keine Methoden bekannt, mit denen diese Schwachstelle über den DNS-
Resolver von Compute Engine in der Standardkonfiguration von glibc ausgenutzt
werden kann. Da wie bei allen Schwachstellen auch hier im Laufe der Zeit neue
Ausnutzungsmethoden entdeckt werden können, sollten Sie Ihre VM-Instanzen
trotzdem so schnell wie möglich patchen. Falls aktiviert, deaktivieren Sie
edns0 (standardmäßig deaktiviert), bis die Instanzen gepatcht sind.

**Ursprüngliches Bulletin:**

Ihre Linux-Distribution könnte anfällig sein. Compute Engine-Kunden, auf deren
Instanzen ein Linux-Betriebssystem ausgeführt wird, müssen zum Schließen
dieser Sicherheitslücke die Betriebssystem-Images ihrer Instanzen
aktualisieren.

Instanzen, auf denen Debian ausgeführt wird, können durch Ausführung der
folgenden Befehle auf der Instanz aktualisiert werden:

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Wir empfehlen außerdem die Installation von [ UnattendedUpgrades
](https://wiki.debian.org/UnattendedUpgrades) für Debian-Instanzen.

Für Red Hat Enterprise Linux-Instanzen:

  * ` user@my-instance:~$ sudo yum -y upgrade `
  * ` user@my-instance:~$ sudo reboot `

Sobald andere Betriebssystem-Maintainer Patches für diese Schwachstelle
veröffentlichen und aktualisierte Betriebssystem-Images von Compute Engine
bereitgestellt werden, bringen wir dieses Bulletin auf den neuesten Stand.

|  Hoch  |  [ CVE-2015-7547
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html)  
  
##  Veröffentlichungsdatum: 19.03.2015

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

CVE-2015-1427 ist eine Sicherheitslücke, die es Remote-Angreifern über die
Groovy Skript-Engine in [ Elasticsearch
](https://www.elastic.co/products/elasticsearch) vor Version 1.3.8 und in
allen 1.4.x-Versionen vor 1.4.3 ermöglicht, den Sandbox-Schutzmechanismus zu
umgehen und beliebige Shell-Befehle auszuführen.

Ausführliche Informationen finden Sie in der [ National Vulnerability Database
(NVD) ](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427) und in
der Datenbank [ Common Vulnerabilities and Exposures (CVE)
](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-1427) .

####  Auswirkungen auf Compute Engine

Wenn Sie Elasticsearch auf Ihren Compute Engine-Instanzen ausführen, sollten
Sie die Elasticsearch-Version auf 1.4.3 oder höher aktualisieren. Wenn Sie
bereits ein Upgrade Ihrer Elasticsearch-Software durchgeführt haben, sind Sie
vor dieser Schwachstelle geschützt.

Wenn Sie kein Upgrade auf Elasticsearch 1.4.3 oder höher durchgeführt haben,
können Sie ein [ Rolling Upgrade durchführen
](http://www.elastic.co/guide/en/elasticsearch/reference/current/rolling-
upgrades.html) .

Wenn Elasticsearch per [ Click-to-Deploy
](https://cloud.google.com/solutions/elasticsearch/click-to-deploy?hl=de) in
der [ Google Cloud Platform Console ](https://console.cloud.google.com/?hl=de)
bereitgestellt wurde, können Sie die [ Bereitstellung löschen
](https://console.cloud.google.com/projectselector/deployments?hl=de) und
damit Instanzen entfernen, auf denen Elasticsearch ausgeführt wird.

Das Google Cloud Platform-Team arbeitet an einer Lösung, um eine aktualisierte
Version von Elasticsearch bereitzustellen. Diese Lösung ist jedoch noch nicht
für die Click-to-Deploy-Funktion in der [ GCP Console
](https://console.cloud.google.com/?hl=de) verfügbar.

|  Hoch  |  [ CVE-2015-1427
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427)  
  
##  Veröffentlichungsdatum: 29.01.2015

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

[ CVE-2015-0235 (Ghost)
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235) ist eine
Sicherheitslücke in der glibc-Bibliothek.

Für App Engine-, Cloud Storage-, BigQuery- und CloudSQL-Kunden sind keine
Maßnahmen erforderlich. Die Google-Server wurden aktualisiert und sind vor
dieser Schwachstelle geschützt.

Kunden von Compute Engine müssen unter Umständen ihre Betriebssystem-Images
aktualisieren.

####  Auswirkungen auf Compute Engine

Ihre Linux-Distribution könnte anfällig sein. Compute Engine-Kunden, die
Debian 7, Debian 7 Backports, Ubuntu 12.04 LTS, Red Hat Enterprise Linux,
CentOS oder SUSE Linux Enterprise Server 11 SP3 ausführen, müssen zum
Schließen dieser Sicherheitslücke das Betriebssystem-Image ihrer Instanzen
aktualisieren.

Diese Schwachstelle betrifft weder Ubuntu 14.04 LTS noch Ubuntu 14.10 oder
SUSE Linux Enterprise Server 12.

Wir empfehlen ein Upgrade Ihrer Linux-Distributionen. Instanzen, auf denen
Debian 7, Debian 7 Backports oder Ubuntu 12.04 LTS ausgeführt wird, können
durch Ausführung der folgenden Befehle auf der Instanz aktualisiert werden:

  1. ` user@my-instance:~$ sudo apt-get update `
  2. ` user@my-instance:~$ sudo apt-get -y upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Für Red Hat Enterprise Linux- oder CentOS-Instanzen:

  1. ` user@my-instance:~$ sudo yum -y upgrade `
  2. ` user@my-instance:~$ sudo reboot `

Für SUSE Linux Enterprise Server 11 SP3-Instanzen:

  1. ` user@my-instance:~$ sudo zypper --non-interactive up `
  2. ` user@my-instance:~$ sudo reboot `

Als Alternative zur Ausführung der manuellen Aktualisierungsbefehle können Sie
jetzt mit folgenden neuen Images Ihre Instanzen neu erstellen:

  * ` debian-7-wheezy-v20150127 `
  * ` backports-debian-7-wheezy-v20150127 `
  * ` centos-6-v20150127 `
  * ` centos-7-v20150127 `
  * ` rhel-6-v20150127 `
  * ` rhel-7-v20150127 `
  * ` sles-11-sp3-v20150127 `
  * ` ubuntu-1204-precise-v20150127 `

####  Auswirkungen auf von Google verwaltete VMs

Nutzer verwalteter VMs, die ` gcloud preview app deploy ` verwenden, müssen
ihre Basis-Docker-Container mit ` gcloud preview app setup-managed-vms `
aktualisieren und alle laufenden Anwendungen mit ` gcloud preview app deploy `
neu bereitstellen. Nutzer, die mit ` appcfg ` arbeiten, müssen nichts tun. Das
Upgrade erfolgt in diesem Fall automatisch.

|  Hoch  |  [ CVE-2015-0235
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235)  
  
##  Veröffentlichungsdatum: 15.10.2014

**Zuletzt aktualisiert: 17.10.2014**

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

CVE-2014-3566 (genannt POODLE) ist eine Schwachstelle im Design der SSL-
Version 3.0. Durch diese Sicherheitslücke kann der Klartext gesicherter
Verbindungen von einem Netzwerkangreifer berechnet werden. Weitere
Informationen zu dieser Sicherheitslücke finden Sie in unserem [ Blogpost
](http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-
exploiting-ssl-30.html) .

Für App Engine-, Cloud Storage-, BigQuery- und CloudSQL-Kunden sind keine
Maßnahmen erforderlich. Die Google-Server wurden aktualisiert und sind vor
dieser Schwachstelle geschützt. Kunden von Compute Engine müssen ihre
Betriebssystem-Images aktualisieren.

####  Auswirkungen auf Compute Engine

**Aktualisiert (17.10.2014):**

Bei Verwendung von SSLv3 können Sie von dieser Schwachstelle betroffen sein.
Compute Engine-Kunden müssen zum Schließen dieser Sicherheitslücke das
Betriebssystem-Image ihrer Instanzen aktualisieren.

Wir empfehlen ein Upgrade Ihrer Linux-Distributionen. Instanzen, auf denen
Debian ausgeführt wird, können durch Ausführung der folgenden Befehle auf der
Instanz aktualisiert werden:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

Für CentOS-Instanzen:

    
    
    
    user@my-instance:~$ sudo yum -y upgrade
    user@my-instance:~$ sudo reboot

Als Alternative zur Ausführung der obigen manuellen Aktualisierungsbefehle
können Sie jetzt mit folgenden neuen Images Ihre Instanzen neu erstellen:

  * ` centos-6-v20141016 `
  * ` centos-7-v20141016 `
  * ` debian-7-wheezy-v20141017 `
  * ` backports-debian-7-wheezy-v20141017 `

Sobald uns die entsprechenden Images vorliegen, werden wir das Bulletin in
Bezug auf RHEL- und SLES-Images aktualisieren. In der Zwischenzeit können
RHEL-Nutzer weitere Informationen [ direkt von Red Hat
](https://access.redhat.com/articles/1232123) beziehen.

**Ursprüngliches Bulletin:**

Compute Engine-Kunden müssen zum Schließen dieser Sicherheitslücke das
Betriebssystem-Image ihrer Instanzen aktualisieren. Sobald neue
Betriebssystem-Images verfügbar sind, werden wir dieses Sicherheitsbulletin um
weitere Anweisungen aktualisieren.

|  Mittel  |  [ CVE-2014-3566
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-3566)  
  
##  Veröffentlichungsdatum: 24.09.2014

**Zuletzt aktualisiert: 29.09.2014**

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

Ein Fehler in Bash (CVE-2014-6271) erlaubt die Codeausführung per Fernzugriff
durch die Auswertung beliebiger vom Angreifer kontrollierter
Umgebungsvariablen. Der wahrscheinlichste Angriffsvektor besteht in
böswilligen HTTP-Anforderungen an CGI-Skripts, die ungeschützt auf einem
Webserver liegen. Weitere Informationen entnehmen Sie der [ Fehlerbeschreibung
](http://seclists.org/oss-sec/2014/q3/650) .

Die Bash-Fehler wurden für alle Google Cloud Platform-Produkte so weit wie
möglich behoben. Davon ausgenommen sind Gastbetriebssystem-Images für Compute
Engine, die vor dem 26.09.2014 erstellt wurden. Durch Ausführen der
nachfolgend beschriebenen Schritte können Sie die Auswirkungen der
Programmfehler auf Ihre Compute Engine-Images einschränken.

####  Auswirkungen auf Compute Engine

Dieser Fehler kann sich auf praktisch alle Websites auswirken, die CGI-Skripts
verwenden. Darüber hinaus betrifft er wahrscheinlich auch Websites, die auf
PHP-, Perl-, Python-, SSI-, Java-, C++ und ähnliche Servlets angewiesen sind,
die Shell-Befehle über ` popen ` , ` system ` , ` shell_exec ` oder ähnliche
APIs aufrufen. Er kann sich auch auf Systeme auswirken, die versuchen, Nutzern
mit beschränkten Rechten über Mechanismen wie etwa SSH-Befehlsbeschränkung
oder die eingeschränkte Bash-Shell einen kontrollierten Anmeldezugriff zu
erlauben.

**Aktualisierung (29.09.2014)**

Alternativ zur Ausführung der nachfolgenden manuellen Aktualisierungsbefehle
können Nutzer jetzt ihre Instanzen mit solchen Images neu erstellen, die die
Risiken aufgrund der folgenden weiteren Sicherheitslücken im Zusammenhang mit
der Bash-Sicherheitslücke verringern. Hierzu gehören [ CVE-2014-7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) , [
CVE-2014-6277 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277)
, [ CVE-2014-6278
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278) , [
CVE-2014-7186 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186)
und [ CVE-2014-7187
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187) . Verwenden
Sie zur Neu-Erstellung Ihrer Instanzen die folgenden neuen Images:

  * ` centos-6-v20140926 `
  * ` centos-7-v20140926 `
  * ` debian-7-wheezy-v20140926 `
  * ` backports-debian-7-wheezy-v20140926 `
  * ` rhel-6-v20140926 `

**Aktualisierung (25.09.2014):**

Nutzer haben nun die Möglichkeit, ihre Instanzen neu zu erstellen, anstatt
eine manuelle Aktualisierung durchzuführen. Verwenden Sie die folgenden neuen
Images mit Korrekturen für diese Sicherheitslücke, um Ihre Instanzen neu zu
erstellen:

  * ` backports-debian-7-wheezy-v20140924 `
  * ` debian-7-wheezy-v20140924 `
  * ` rhel-6-v20140924 `
  * ` centos-6-v20140924 `
  * ` centos-7-v20140924 `

Bei RHEL- und SUSE-Images können Sie auch manuelle Aktualisierungen vornehmen,
indem Sie die folgenden Befehle auf den Instanzen ausführen:

    
    
    
    # RHEL instances
    user@my-instance:~$ sudo yum -y upgrade
    
    # SUSE instances
    user@my-instance:~$ sudo zypper --non-interactive up

**Ursprüngliches Bulletin:**

Wir empfehlen ein Upgrade Ihrer Linux-Distributionen. Instanzen, auf denen
Debian ausgeführt wird, können durch Ausführung der folgenden Befehle auf der
Instanz aktualisiert werden:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    

Für CentOS-Instanzen:

    
    
    
    user@my-instance:~$ sudo yum -y upgrade

Ausführliche Informationen finden Sie in der Ankündigung der entsprechenden
Linux-Distribution:

  * Ursprüngliche Patches: [ http://ftp.gnu.org/gnu/bash/ ](http://ftp.gnu.org/gnu/bash/) (siehe letzten Eintrag in *-patches für die entsprechende Version) 
  * Debian: [ [SECURITY] [DSA 3032-1] Bash-Sicherheitsupdate ](https://lists.debian.org/debian-security-announce/2014/msg00220.html)
  * RHEL: 
    * [ RHSA-2014:1293-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00048.html)
    * [ RHSA-2014:1294-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00049.html)
  * CentOS 5: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020582.html)
  * CentOS 6: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020585.html)
  * CentOS 7: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020583.html)

|  Hoch  |  [ CVE-2014-7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) , [
CVE-2014-6271 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6271)
, [ CVE-2014-6277
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277) , [
CVE-2014-6278 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278)
, [ CVE-2014-7186
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186) , [
CVE-2014-7187 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)  
  
##  Veröffentlichungsdatum: 25.07.2014

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

[ Elasticsearch Logstash ](http://www.elasticsearch.org/overview/logstash/)
ist anfällig für Befehlsinjektionen in das Betriebssystem, die unter Umständen
eine nicht autorisierte Änderung und Weitergabe von Daten ermöglichen. Ein
Angreifer kann gefälschte Ereignisse an eine beliebige Datenquelle von
Logstash senden und somit Befehle mit den Rechten des Logstash-Prozesses
ausführen.

####  Auswirkungen auf Compute Engine

Diese Schwachstelle betrifft alle Compute Engine-Instanzen, auf denen
Versionen von Elasticsearch Logstash vor 1.4.2 mit aktivierten zabbix- oder
nagios_nsca-Ausgaben ausgeführt werden. Zum Schutz vor Angriffen haben Sie
folgende Optionen:

  * Upgrade auf Logstash 1.4.2 vornehmen 
  * Patch für die Versionen 1.3.x anwenden 
  * ` zabbix ` \- und ` nagios_nsca ` -Ausgaben deaktivieren 

Weitere Informationen finden Sie im [ Logstash-Blog
](http://www.elasticsearch.org/blog/logstash-1-4-2/) .

Elasticsearch empfiehlt auch [ die Verwendung einer Firewall
](http://www.elasticsearch.org/blog/scripting-security/) , um den
Remotezugriff durch nicht vertrauenswürdige IP-Adressen zu vermeiden.

|  Hoch  |  [ CVE-2014-4326
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-4326)  
  
##  Veröffentlichungsdatum: 18.06.2014

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

Wir möchten kurz auf mögliche Bedenken eingehen, die Kunden in Bezug auf die
Sicherheit von Docker-Containern bei Ausführung auf der Google Cloud Platform
haben können. Dazu gehören Kunden, die unsere Google App Engine-Erweiterungen
verwenden, von denen Docker-Container, für Container optimierte VMs oder der
Open-Source-Scheduler Kubernetes unterstützt werden.

Docker hat vorbildlich auf das Problem reagiert. [ Die entsprechende
Blogantwort finden Sie hier. ](http://blog.docker.com/2014/06/docker-
container-breakout-proof-of-concept-exploit/) Wie in der Antwort betont, gilt
das entdeckte Problem nur für Docker 0.11, eine ältere Vorproduktionsversion.

Während alle Welt über Containersicherheit nachdenkt, möchten wir darauf
aufmerksam machen, dass auf Linux-Anwendungscontainern beruhende Lösungen
(insbesondere Docker-Container) in der Google Cloud Platform in vollständigen
VMs (Compute Engine) ausgeführt werden. Wir unterstützen zwar die Bemühungen
der Docker-Community, den Linux-Anwendungscontainer-Stack zu stärken, halten
aber den Hinweis für wichtig, dass es sich um eine neue Technologie handelt,
die eine große Oberfläche und damit auch Angriffsfläche bietet. Wir glauben,
dass vollständige Hypervisoren (VMs) bislang eine kompaktere und leichter zu
verteidigende Oberfläche bieten. VMs wurden von Anfang an mit dem Ziel
entwickelt, schädliche Arbeitslasten zu isolieren und die Wahrscheinlichkeit
des Auftretens sowie die Auswirkungen von möglichen Programmfehlern zu
minimieren.

Unsere Kunden können sich auf eine vollständige Hypervisor-Grenze zwischen
ihnen und potenziellem Schadcode Dritter verlassen. Wenn wir den Linux-
Anwendungscontainer-Stack als robust genug für mandantenfähige Arbeitslasten
befinden, werden wir die Community darüber in Kenntnis setzen. Derzeit ist der
Linux-Anwendungscontainer kein Ersatz für die VM. Er ermöglicht jedoch eine
wesentlich bessere Ausschöpfung ihrer Möglichkeiten.

|  Niedrig  |  [ Docker-Blogpost ](http://blog.docker.com/2014/06/docker-
container-breakout-proof-of-concept-exploit/)  
  
##  Veröffentlichungsdatum: 05.06.2014

**Zuletzt aktualisiert: 09.06.2014**

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

Ein Problem in OpenSSL besteht darin, dass die ` ChangeCipherSpec ` -Meldungen
nicht richtig in die Zustandsmaschine für den Handshake eingebunden werden.
Dadurch können sie vorzeitig in den Handshake injiziert werden. Angreifer
können mit einem sorgfältig gefälschten Handshake die Verwendung von schwachem
Verschlüsselungsmaterial auf OpenSSL SSL/TLS-Clients und -Servern erzwingen.
Dies kann durch einen Man-in-the-Middle-Angriff ausgenutzt werden, indem der
Angreifer den Datenverkehr vom angegriffenen Client und Server entschlüsselt
und ändert.

Dieses Problem läuft unter der Kennung [ CVE-2014-0224
](https://www.openssl.org/news/secadv/20140605.txt) . Das OpenSSL-Team hat das
Problem behoben und die OpenSSL-Community aufgefordert, OpenSSL zu
aktualisieren.

####  Auswirkungen auf Compute Engine

Diese Schwachstelle betrifft alle Compute Engine-Instanzen, die OpenSSL
nutzen, einschließlich Debian, CentOS, Red Hat Enterprise Linux und SUSE Linux
Enterprise Server. Sie können Ihre Instanzen aktualisieren, indem Sie diese
mit den neuen Images erneut erstellen oder die Pakete auf den Instanzen
manuell aktualisieren.

**Aktualisierung (09.06.2014)** : Wenn Sie Ihre Instanzen, auf denen SUSE
Linux Enterprise Server ausgeführt wird, mit neuen Images aktualisieren
möchten, erstellen Sie die Instanzen mithilfe der folgenden oder höheren
Image-Versionen neu:

  * ` sles-11-sp3-v20140609 `

**Ursprünglicher Post:**

Zum Aktualisieren von Debian- und CentOS-Instanzen mit neuen Images erstellen
Sie die Instanzen mithilfe der folgenden oder höheren Image-Versionen neu:

  * ` debian-7-wheezy-v20140605 `
  * ` backports-debian-7-wheezy-v20140605 `
  * ` centos-6-v20140605 `
  * ` rhel-6-v20140605 `

Wenn Sie OpenSSL auf Ihren Instanzen manuell aktualisieren möchten, führen Sie
die folgenden Befehle zur Aktualisierung der entsprechenden Pakete aus. Bei
Instanzen, auf denen CentOS und RHEL ausgeführt wird, können Sie OpenSSL durch
Ausführen dieser Befehle auf der Instanz aktualisieren:

    
    
    
    user@my-instance:~$ sudo yum -y update
    user@my-instance:~$ sudo reboot

Zum Aktualisieren von OpenSSL auf Instanzen, auf denen Debian läuft, können
Sie die folgenden Befehle auf den Instanzen ausführen:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

Bei Instanzen, auf denen SUSE Linux Enterprise Server ausgeführt wird, können
Sie sich durch Ausführen der folgenden Befehle auf der Instanz überprüfen, ob
OpenSSL auf dem neuesten Stand ist:

    
    
    
    user@my-instance:~$ sudo zypper --non-interactive up
    user@my-instance:~$ sudo reboot

|  Mittel  |  [ CVE-2014-0224
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0224)  
  
##  Veröffentlichungsdatum: 08.04.2014

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

Die (1) TLS- und (2) DTLS-Implementierungen in OpenSSL 1.0.1 vor 1.0.1g
behandeln Heartbeat Extension-Pakete nicht richtig. Dadurch können entfernte
Angreifer mithilfe von gefälschten Datenpaketen, die lesend über die Grenzen
des Datenpuffers hinaus zugreifen, vertrauliche Informationen aus den
Prozessspeichern auslesen. Dies wurde durch das Auslesen privater Schlüssel im
Zusammenhang mit ` d1_both.c ` und ` t1_lib.c ` , dem Heartbleed-
Programmfehler, veranschaulicht.

####  Auswirkungen auf Compute Engine

Diese Schwachstelle betrifft alle Compute Engine-Instanzen unter Debian, RHEL
und CentOS, deren OpenSSL-Version nicht auf dem neuesten Stand ist. Sie können
die Instanzen aktualisieren, indem Sie sie mit neuen Images neu erstellen oder
die Pakete manuell auf den Instanzen aktualisieren.

Zum Aktualisieren Ihrer Instanzen mit neuen Images erstellen Sie die Instanzen
mithilfe der folgenden oder höheren Image-Versionen neu:

  * ` debian-7-wheezy-v20140408 `
  * ` backports-debian-7-wheezy-v20140408 `
  * ` centos-6-v20140408 `
  * ` rhel-6-v20140408 `

Wenn Sie OpenSSL auf Ihren Instanzen manuell aktualisieren möchten, führen Sie
die folgenden Befehle zur Aktualisierung der entsprechenden Pakete aus. Bei
Instanzen, auf denen CentOS und RHEL ausgeführt werden, können Sie sich durch
Ausführen dieser Befehle auf der Instanz darüber vergewissern, dass OpenSSL
auf dem neuesten Stand ist:

    
    
    
    user@my-instance:~$ sudo yum update
    user@my-instance:~$ sudo reboot

Zum Aktualisieren von OpenSSL auf Instanzen, auf denen Debian läuft, können
Sie die folgenden Befehle auf den Instanzen ausführen:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get upgrade
    user@my-instance:~$ sudo reboot

Instanzen, auf denen SUSE Linux läuft, sind nicht betroffen.

**Aktualisierung (14.04.2014)** : Angesichts neuer Erkenntnisse über das
Auslesen von Schlüsseln mithilfe des Heartbleed-Programmfehlers wird Kunden
von Compute Engine empfohlen, neue Schlüssel für eventuell betroffene SSL-
Dienste zu erstellen.

|  Mittel  |  [ CVE-2014-0160
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0160)  
  
##  Veröffentlichungsdatum: 07.06.2013

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

**Hinweis** : Diese Sicherheitslücke betrifft nur die Kernels, die ab API-
Version v1 verworfen und entfernt wurden.

Eine Formatstring-Sicherheitslücke in der Funktion ` b43_request_firmware ` in
der Datei ` drivers/net/wireless/b43/main.c ` des Broadcom B43 Wireless-
Treibers im Linux-Kernel bis 3.9.4 ermöglicht lokalen Nutzern Folgendes:
Erweiterung ihrer Rechte, indem sie Root-Zugriff erlangen und Formatstring-
Bezeichner in einen ` fwpostfix ` -Modprobe-Parameter einbinden, die zu einer
falschen Konstruktion einer Fehlermeldung führen.

####  Auswirkungen auf Compute Engine

Diese Sicherheitslücke betrifft alle Compute Engine-Kernels vor `
gcg-3.3.8-201305291443 ` . Als Reaktion darauf hat Compute Engine alle
früheren Kernels verworfen. Nutzern wird empfohlen, ihre Instanzen und Images
auf den Stand des Compute Engine-Kernels ` gce-v20130603 ` zu bringen. `
gce-v20130603 ` enthält den Kernel ` gcg-3.3.8-201305291443 ` mit dem Patch
für diese Sicherheitslücke.

So finden Sie heraus, welche Kernelversion von einer Instanz verwendet wird:

  1. Erstellen Sie eine SSH-Verbindung zur Instanz. 
  2. Führen Sie ` uname -r ` aus. 

|  Mittel  |  [ CVE-2013-2852
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2852)  
  
##  Veröffentlichungsdatum: 07.06.2013

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

**Hinweis** : Diese Sicherheitslücke betrifft nur diejenigen Kernels, die ab
API-Version v1 verworfen und entfernt wurden.

Eine Formatstring-Schwachstelle in der Funktion register_disk in der Datei `
block/genhd.c ` des Linux-Kernels bis 3.9.4 ermöglicht lokalen Nutzern
Folgendes: Erweiterung ihrer Rechte, indem sie Root-Zugriff erlangen und
Formatstring-Bezeichner in ` /sys/module/md_mod/parameters/new_array `
schreiben, um einen gefälschten ` /dev/md ` -Gerätenamen zu erstellen.

####  Auswirkungen auf Compute Engine

Diese Sicherheitslücke betrifft alle Compute Engine-Kernels vor `
gcg-3.3.8-201305291443 ` . Als Reaktion darauf hat Compute Engine alle
früheren Kernels verworfen. Nutzern wird empfohlen, ihre Instanzen und Images
auf den Stand des Compute Engine-Kernels ` gce-v20130603 ` zu bringen. `
gce-v20130603 ` enthält den Kernel ` gcg-3.3.8-201305291443 ` mit dem Patch
für diese Sicherheitslücke.

So finden Sie heraus, welche Kernelversion von einer Instanz verwendet wird:

  1. Erstellen Sie eine SSH-Verbindung zur Instanz. 
  2. Führen Sie ` uname -r ` aus. 

|  Mittel  |  [ CVE-2013-2851
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2851)  
  
##  Veröffentlichungsdatum: 14.05.2013

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

**Hinweis** : Diese Sicherheitslücke betrifft nur die Kernels, die ab API-
Version v1 verworfen und entfernt wurden.

Die Funktion perf_swevent_init in der Datei ` kernel/events/core.c ` im Linux-
Kernel vor 3.8.9 verwendet einen falschen ` integer ` -Datentyp, der es
lokalen Nutzern ermöglicht, über einen gefälschten ` perf_event_open `
-Systemaufruf ihre Rechte zu erweitern.

####  Auswirkungen auf Compute Engine

Diese Sicherheitslücke betrifft alle Compute Engine-Kernels vor `
gcg-3.3.8-201305211623 ` . Als Reaktion darauf hat Compute Engine alle
früheren Kernels verworfen. Nutzern wird empfohlen, ihre Instanzen und Images
auf den Stand des Compute Engine-Kernels ` gce-v20130521 ` zu bringen. `
gce-v20130521 ` enthält den Kernel ` gcg-3.3.8-201305211623 ` mit dem Patch
für diese Sicherheitslücke.

So finden Sie heraus, welche Kernelversion von einer Instanz verwendet wird:

  1. Erstellen Sie eine SSH-Verbindung zur Instanz. 
  2. Führen Sie ` uname -r ` aus. 

|  Hoch  |  [ CVE-2013-2094
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2094)  
  
##  Veröffentlichungsdatum: 18.02.2013

Beschreibung  |  Schweregrad  |  Hinweise  
---|---|---  
  
####  Beschreibung

**Hinweis** : Diese Sicherheitslücke betrifft nur die Kernels, die ab API-
Version v1 verworfen und entfernt wurden.

Eine Race-Bedingung in der ptrace-Funktion im Linux-Kernel vor 3.7.5
ermöglicht lokalen Nutzern, über einen ` PTRACE_SETREGS ptrace ` -Systemaufruf
in einer gefälschten Anwendung ihre Rechte zu erweitern.

####  Auswirkungen auf Compute Engine

Diese Sicherheitslücke betrifft die Compute Engine-Kernels ` 2.6.x-gcg- _
<date> _ ` . Als Reaktion darauf hat Compute Engine die 2.6.x-Kernels
verworfen. Nutzern wird empfohlen, ihre Instanzen und Images auf den Stand des
Compute Engine-Kernels ` gce-v20130225 ` zu bringen. ` gce-v20130225 ` enthält
den Kernel ` 3.3.8-gcg-201302081521 ` mit dem Patch für diese
Sicherheitslücke.

So finden Sie heraus, welche Kernelversion von einer Instanz verwendet wird:

  1. Erstellen Sie eine SSH-Verbindung zur Instanz. 
  2. Führen Sie ` uname -r ` aus. 

|  Mittel  |  [ CVE-2013-0871
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-0871)

