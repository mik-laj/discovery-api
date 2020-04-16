#  Güvenlik Bültenleri

Zaman zaman Compute Engine ile ilgili güvenlik bültenleri yayınlanabilir.
Compute Engine ile ilgili tüm güvenlik bültenleri burada yer almaktadır.

[ Compute Engine güvenlik bültenlerine abone olun. ![Abone
ol](https://cloud.google.com/images/feed-icon.png?hl=tr)
](https://cloud.google.com/feeds/compute-engine-security-bulletins.xml?hl=tr)

##  Yayınlanma tarihi: 18.06.2019

**son güncelleme tarihi: 25.06.2019 Saat 06:30 PST**

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

Linux çekirdeklerindeki üç TCP güvenlik açığı yakın zamanda Netflix tarafından
açıklanmıştır:

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

Bu CVE'lerin tamamına [ NFLX-2019-001 ](https://github.com/Netflix/security-
bulletins/blob/master/advisories/third-party/2019-001.md) adı verilir.

####  Compute Engine'e etkisi

Compute Engine'i barındıran altyapı bu güvenlik açığına karşı korunmaktadır.

Güvenilmeyen ağ trafiği alan/gönderen yama uygulanmamış Linux işletim
sistemleri çalıştıran Compute Engine sanal makineleri, bu DoS saldırısına
karşı savunmasızdır. İşletim sistemleri için yamalar kullanılabilir olur olmaz
bu sanal makine örneklerini güncellemenizi öneririz.

TCP bağlantılarını sonlandıran yük dengeleyiciler, bu güvenlik açığına karşı
korunmak için yamalanmıştır. Bu yük dengeleyicilerden yalnızca güvenilmeyen
trafik alan Compute Engine örnekleri savunmasız değildir. HTTP Yük
Dengeleyicileri, SSL Proxy Yük Dengeleyicileri ve TCP Proxy Yük
Dengeleyicileri de bu kapsamdadır.

Ağ yükü dengeleyicileri ve dahili yük dengeleyicileri, TCP bağlantılarını
sonlandırmaz. Bu yük dengeleyicilerden güvenilmeyen trafik alan, yama
uygulanmamış Compute Engine örnekleri savunmasızdır.

####  Yama uygulanmış görüntüler ve tedarikçi kaynakları

Kullanılabilir olduğunda, iki CVE'nin durumu da dahil, her bir işletim sistemi
tedarikçisinden gelen yama bilgileri için bağlantılar sağlayacağız. Bu genel
görüntülerin erken sürümleri bu yamaları içermez ve potansiyel saldırıları
hafifletmez:

  * ` debian-cloud ` projesi: 
    * ` debian-9-stretch-v20190618 `
  * ` centos-cloud ` projesi: 
    * ` centos-6-v20190619 `
    * ` centos-7-v20190619 `
  * ` cos-cloud ` projesi: 
    * ` cos-dev-77-12293-0-0 `
    * ` cos-beta-76-12239-21-0 `
    * ` cos-stable-75-12105-77-0 `
    * ` cos-73-11647-217-0 `
    * ` cos-69-10895-277-0 `
  * ` coreos-cloud ` projesi: 
    * ` coreos-alpha-2163-2-1-v20190617 `
    * ` coreos-beta-2135-3-1-v20190617 `
    * ` coreos-stable-2079-6-0-v20190617 `
  * ` rhel-cloud ` projesi: 
    * ` rhel-6-v20190618 `
    * ` rhel-7-v20190618 `
    * ` rhel-8-v20190618 `
  * ` rhel-sap-cloud ` projesi: 
    * ` rhel-7-4-sap-v20190618 `
    * ` rhel-7-6-sap-v20190618 `
  * ` suse-cloud ` projesi: 
    * ` sles-12-sp4-v20190617 `
    * ` sles-15-v20190617 `
  * ` suse-sap-cloud ` projesi: 
    * ` sles-12-sp1-sap-v20190617 `
    * ` sles-12-sp2-sap-v20190617 `
    * ` sles-12-sp3-sap-v20190617 `
    * ` sles-12-sp4-sap-v20190617 `
    * ` sles-15-sap-v20190617 `
  * ` ubuntu-cloud ` projesi: 
    * ` ubuntu-1604-xenial-v20190617 `
    * ` ubuntu-1804-bionic-v20190617 `
    * ` ubuntu-1810-cosmic-v20190618 `
    * ` ubuntu-1904-disco-v20190619 `
    * ` ubuntu-minimal-1604-xenial-v20190618 `
    * ` ubuntu-minimal-1804-bionic-v20190617 `
    * ` ubuntu-minimal-1810-cosmic-v20190618 `
    * ` ubuntu-minimal-1904-disco-v20190618 `

|  Orta  |

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

  
  
##  Yayınlanma tarihi: 14.05.2019

**son güncelleme tarihi: 20.05.2019 Saat 17:00 PST**

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

Aşağıdaki CVE'ler Intel tarafından açıklanmıştır:

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

Bu CVE'lerin tamamına Mikromimari Veri Örnekleme (MDS) adı verilir. Bu
güvenlik açıkları, mikromimari durumu ile kurgusal yürütme etkileşimi
üzerinden verilerin savunmasız hale gelmesine neden olabilir.

####  Compute Engine'e etkisi

**Compute Engine'i çalıştıran ana makine altyapısı, müşteri iş yüklerini
birbirinden ayırır. Sanal makinelerinizde güvenilmeyen kod çalıştırmadığınız
takdirde başka bir işlem yapmanız gerekmez.**

Compute Engine sanal makineleri içinde kendi çok kiracılı hizmetlerinde
güvenilmeyen kod çalıştıran müşteriler, konuk işletim sistemi sağlayıcısının
önerdiği etki azaltma bilgilerine başvurmalıdır. Bu bilgiler, Intel'in
mikrokod etki azaltma özelliklerini içerebilir. Konuklar için yeni boşaltma
işlevine doğrudan geçiş erişimi dağıttık. Aşağıda, sık kullanılan konuk
görüntüleri için kullanılabilecek etki azaltma adımlarının bir özeti
verilmiştir.

####  Yama uygulanmış görüntüler ve tedarikçi kaynakları

Kullanılabilir olduğunda, iki CVE'nin durumu da dahil, her bir işletim sistemi
tedarikçisinden gelen yama bilgileri için bağlantılar sağlayacağız. Sanal
makine örneklerini yeniden oluşturmak için bu görüntüleri kullanın. Bu genel
görüntülerin erken sürümleri bu yamaları içermez ve potansiyel saldırıları
hafifletmez:

  * ` centos-cloud ` projesi: [ CESA-2019:1169 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023309.html) , [ CESA-2019:1168 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023314.html)
    * ` centos-6-v20190515 `
    * ` centos-7-v20190515 `
  * ` coreos-cloud ` projesi: [ CoreOS Container Linux için MDS hafifletme işlemleri ](https://coreos.com/os/docs/latest/disabling-smt.html)
    * ` coreos-stable-2079-4-0-v20190515 `
    * ` coreos-beta-2107-3-0-v20190515 `
    * ` coreos-alpha-2135-1-0-v20190515 `
  * ` cos-cloud ` projesi 
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
  * ` debian-cloud ` projesi: [ DSA-4444 ](https://www.debian.org/security/2019/dsa-4444)
    * ` debian-9-stretch-v20190514 `
  * ` rhel-cloud ` projesi: [ Red Hat MDS Bilgi Makalesi ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-6-v20190515 `
    * ` rhel-7-v20190517 `
    * ` rhel-8-v20190515 `
  * ` rhel-sap-cloud ` projesi: [ Red Hat MDS Bilgi Makalesi ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-7-4-sap-v20190515 `
    * ` rhel-7-6-sap-v20190517 `
  * ` suse-cloud ` projesi: [ SUSE MDS Bilgi Tabanı ](https://www.suse.com/support/kb/doc/?id=7023736)
    * ` sles-12-sp4-v20190520 `
    * ` sles-15-v20190520 `
  * ` suse-sap-cloud ` projesi 
    * ` sles-12-sp4-sap-v20190520 `
    * ` sles-15-sap-v20190520 `
  * ` ubuntu-os-cloud ` projesi: [ Ubuntu MDS Wiki ](https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/MDS)
    * ` ubuntu-1404-trusty-v20190514 `
    * ` ubuntu-1604-xenial-v20190514 `
    * ` ubuntu-1804-bionic-v20190514 `
    * ` ubuntu-1810-cosmic-v20190514 `
    * ` ubuntu-1904-disco-v20190514 `
    * ` ubuntu-minimal-1604-xenial-v20190514 `
    * ` ubuntu-minimal-1804-bionic-v20190514 `
    * ` ubuntu-minimal-1810-cosmic-v20190514 `
    * ` ubuntu-minimal-1904-disco-v20190514 `
  * ` windows-cloud ` ve ` windows-sql-cloud ` projesi: [ Microsoft ADV190013 ](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/ADV190013)
    * Sürüm numarası ` v20190514 ` olan tüm Windows Server ve SQL Server genel görüntüleri. 
  * ` gce-uefi-images ` projesi 
    * ` centos-7-v20190515 `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
    * ` rhel-7-v20190517 `
    * ` ubuntu-1804-bionic-v20190514 `
    * Sürüm numarası ` v20190514 ` olan tüm Windows Server genel görüntüleri. 

####  Container İçin Optimize Edilmiş İşletim Sistemi

Konuk işletim sisteminiz olarak Container için Optimize Edilmiş İşletim
Sistemi (COS) kullanıyor ve sanal makinenizde güvenilmeyen, çok kiracılı iş
yükleri çalıştırıyorsanız şunları yapmanızı öneririz:

  1. Çekirdek komut satırında ` nosmt ` ifadesini ayarlayarak Hyper-Threading'i devre dışı bırakın.   

Mevcut COS sanal makinelerde ` nosmt ` seçeneğini ayarlamak için aşağıdaki
işlemleri yaparak ` grub.cfg ` ifadesini değiştirebilir, ardından sistemi
yeniden başlatabilirsiniz:

    
        
    # Run as root:
    dir="$(mktemp -d)"
    mount /dev/sda12 "${dir}"
    sed -i -e "s|cros_efi|cros_efi nosmt|g" "${dir}/efi/boot/grub.cfg"
    umount "${dir}"
    rmdir "${dir}"
    
    reboot

İşlemi daha kolay gerçekleştirmek amacıyla yukarıdaki komutları
çalıştırdığınızda elde edeceğiniz aynı sonuca ulaşmak için aşağıdaki komut
dosyasını çalıştırabilirsiniz. Yeni sanal makinelerin bu yeni parametreyi
kullandığından emin olmak için bu komut dosyasını; bulut yapılandırmanızın,
başlangıç komut dosyalarınızın veya örnek şablonlarınızın bir parçası haline
getirmenizi öneririz. Bu komut dosyasını çalıştıran bir bulut yapılandırması
örneği aşağıda verilmiştir.

**Uyarı:** Bu komut, ilk kez çalıştırıldığında örneğin anında yeninden
başlatılmasını sağlar. Hyper-Threading'in zaten devre dışı bırakıldığı bir
örnekte bu komut daha sonra çalıştırıldığında herhangi bir etkisi
olmayacaktır.

    
        
    # Run as root
    /bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)
    

Bu komut dosyasını bulut yapılandırmanızın bir parçası olarak eklemek için:

    
        
    #cloud-config
    
    bootcmd:
    - /bin/bash -c "/bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)"
    

Örneğinizde Hyper-Threading'in devre dışı olduğunu doğrulamak için `
/sys/devices/system/cpu/smt/active ` ve ` /sys/devices/system/cpu/smt/control
` dosyalarının çıktısını inceleyin. ` active ` için ` 0 ` sonucunu, ` control
` için ` off ` sonucunu döndürüyorsa Hyper-Threading devre dışıdır:

    
        
    cat /sys/devices/system/cpu/smt/active
    cat /sys/devices/system/cpu/smt/control
    

**Not:** Örneğinizde UEFI Güvenli Başlatma'yı etkinleştirdiyseniz örneğinizi
UEFI Güvenli Başlatma devre dışı bırakılmış şekilde yeniden oluşturmanız
gerekecektir. UEFI Güvenli Başlatma devre dışı haldeyken yukarıdaki komutu
çalıştırın, ardından yeni örneğinizde UEFI Güvenli Başlatma'yı etkinleştirin.

  2. COS görüntüsünün yeni sürümünü kullanma   

Hyper-Threading'i yukarıda açıklanan şekilde devre dışı bırakmanın yanı sıra
güvenlik açığından tamamen korunmak için yukarıda belirtilen güncellenmiş
görüntülerle veya Container için Optimize Edilmiş İşletim Sistemi
görüntüleriyle [ örneklerinizi yeniden oluşturmanız
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=tr#publicimage) da gerekir.

|  Orta  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  Yayınlanma tarihi: 14.08.2018

**son güncelleme tarihi: 20.08.2018 Saat 17:00 PST**

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

Aşağıdaki CVE'ler [ Intel tarafından açıklanmıştır
](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) :

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) ( [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) için) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (işletim sistemleri ve [ SMT ](https://en.wikipedia.org/wiki/Hyper-Threading) için) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (sanallaştırma için) 

Bu CVE'lerin tamamına "L1 Terminal Fault (L1TF)" adı verilir.

Bu L1TF güvenlik açıkları, işlemci düzeyinde veri yapılarının yapılandırmasına
saldırarak kurgusal yürütmeyi kötüye kullanır. "L1", bellek erişimini
hızlandırmak için kullanılan küçük bir çekirdek içi kaynak olan 1. Düzey Veri
önbelleğini (L1D) temsil eder.

Bu güvenlik açıkları ve Compute Engine'in çözümleri ile ilgili daha fazla
ayrıntı için [ Google Cloud blog yayınını
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=tr) okuyun.

####  Compute Engine'e etkisi

Compute Engine'i çalıştıran ve müşteri iş yüklerini birbirinden ayıran ana
makine altyapısı, bilinen saldırılara karşı korunur.

Compute Engine müşterileri, konuk ortamı içinde dolaylı kötüye kullanım
olasılığını ortadan kaldırmak için görüntülerini güncellemeye teşvik edilir.
Bu özellikle kendi çok kiracılı hizmetlerini Compute Engine sanal
makinelerinde çalıştıran müşteriler için önemlidir.

Google Compute Engine müşterileri, örnekleri üzerindeki konuk işletim
sistemlerini aşağıdaki seçeneklerden birini kullanarak güncelleyebilir:

  * [ Mevcut sanal makine örneklerini yeniden oluşturmak ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=tr#publicimage) için yama uygulanmış genel görüntüler kullanma. 
  * Mevcut örnekler üzerinde, işletim sistemi tedarikçisi tarafından sağlanan yamalar uygulama ve yama uygulanmış örnekleri yeniden başlatma. 

####  Yama uygulanmış görüntüler ve tedarikçi kaynakları

Kullanılabilir olduğunda, her iki CVE için durum da dahil, her bir işletim
sistemi tedarikçisinden gelen yama bilgileri için bağlantılar sağlayacağız.
Sanal makine örneklerini yeniden oluşturmak için bu görüntüleri kullanın. Bu
genel görüntülerin erken sürümleri bu yamaları içermez ve potansiyel
saldırıları hafifletmez.

  * ` centos-cloud ` projesi: 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * ` coreos-cloud ` projesi: 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * ` cos-cloud ` projesi: 
    * ` cos-stable-66-10452-110-0 `
    * ` cos-stable-67-10575-66-0 `
    * ` cos-beta-68-10718-81-0 `
    * ` cos-dev-69-10895-23-0 `
  * ` debian-cloud ` projesi: 
    * ` debian-9-stretch-v20180820 `
  * ` rhel-cloud ` projesi: 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * ` rhel-sap-cloud ` projesi: 
    * ` rhel-7-sap-apps-v20180814 `
    * ` rhel-7-sap-hana-v20180814 `
  * ` suse-cloud ` projesi: 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
    * ` sles-11-sp4-v20180816 `
  * ` suse-sap-cloud ` projesi: 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * ` ubuntu-os-cloud ` projesi: 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `
  * ` windows-cloud ` ` gce-uefi-images ` ve ` windows-sql-cloud ` projeleri: 
    * Sürüm numarası ` -v201800814 ` ve üzeri olan tüm Windows Server ve SQL Server [ herkese açık görüntüleri ](https://cloud.google.com/compute/docs/images?hl=tr#os-compute-support) yama içerir. 

|  Yüksek  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  Yayınlanma tarihi: 06.08.2018

**son güncelleme tarihi: 05.09.2018 Saat 17:00 PST**

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  05.09.2018 Tarihli Güncelleme

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) , 14/08/2018 tarihinde US-CERT tarafından
yayınlanmıştır. Tıpkı [ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) gibi savunmasız sistemlerde hizmet reddi
(DoS) saldırılarının etkisini artıran çekirdek düzeyinde bir ağ iletişimi
güvenlik açığıdır. Aralarındaki temel fark, CVE-2018-5391 açığının IP
bağlantıları üzerinde kötüye kullanılma riski olmasıdır. Bu bülteni, bu
güvenlik açıklarının her ikisini de kapsayacak şekilde güncelledik.

####  Açıklama

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ("SegmentSmack"), TCP bağlantıları
üzerindeki savunmasız sistemlerde hizmet reddi (DoS) saldırılarının etkisini
artıran çekirdek düzeyinde bir ağ iletişimi güvenlik açığını tanımlar.

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ("FragmentSmack"), IP bağlantıları
üzerindeki savunmasız sistemlerde hizmet reddi (DoS) saldırılarının etkisini
artıran çekirdek düzeyinde bir ağ iletişimi güvenlik açığını tanımlar.

####  Compute Engine'e etkisi

Compute Engine sanal makinelerini çalıştıran ana makine altyapısı risk altında
değildir. Compute Engine sanal makineleri giriş ve çıkış trafiğini yöneten ağ
altyapısı, bu güvenlik açığına karşı korumalıdır. Yalnızca [ HTTP(S)
](https://cloud.google.com/load-balancing/docs/https/?hl=tr) , [ SSL
](https://cloud.google.com/load-balancing/docs/ssl/?hl=tr) veya [ TCP Yük
Dengeleyicileri ](https://cloud.google.com/load-balancing/docs/tcp/?hl=tr)
üzerinden güvenilmeyen ağ trafiği alan/gönderen Compute Engine sanal
makineleri bu güvenlik açığına karşı korumalıdır.

Güvenilmeyen ağ trafiğini doğrudan veya [ Ağ Yük Dengeleyicileri
](https://cloud.google.com/load-balancing/docs/network/?hl=tr) üzerinden
alan/gönderen yama uygulanmamış işletim sistemleri çalıştıran Compute Engine
sanal makineleri bu DoS saldırısına karşı savunmasızdır.

İşletim sistemleri için yamalar kullanılabilir olur olmaz sanal makine
örneklerinizi güncellemenizi öneririz.

Compute Engine müşterileri, örnekleri üzerindeki konuk işletim sistemlerini
aşağıdaki seçeneklerden birini kullanarak güncelleyebilir:

  * [ Mevcut sanal makine örneklerini yeniden oluşturmak ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=tr#publicimage) için yama uygulanmış genel görüntüler kullanma. Aşağıdan, yama uygulanmış genel görüntüler listesine bakın. 
  * Mevcut örnekler üzerinde, işletim sistemi tedarikçisi tarafından sağlanan yamalar uygulama ve yama uygulanmış örnekleri yeniden başlatma. 

####  Yama uygulanmış görüntüler ve tedarikçi kaynakları

Kullanılabilir olduğunda, her bir işletim sistemi tedarikçisinden gelen yama
bilgileri için bağlantılar sağlayacağız.

  * ` centos-cloud ` projesi (yalnızca CVE-2018-5390): 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * ` coreos-cloud ` projesi (CVE-2018-5390 ve CVE-2018-5391): 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * ` cos-cloud ` projesi (CVE-2018-5390 ve CVE-2018-5391): 
    * ` cos-stable-65-10323-98-0 `
    * ` cos-stable-66-10452-109-0 `
    * ` cos-stable-67-10575-65-0 `
    * ` cos-beta-68-10718-76-0 `
    * ` cos-dev-69-10895-16-0 `
  * ` debian-cloud ` projesi (CVE-2018-5390 ve CVE-2018-5391): 
    * ` debian-9-stretch-v20180814 `
  * ` rhel-cloud ` projesi (yalnızca CVE-2018-5390): 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * ` suse-cloud ` projesi (CVE-2018-5390 ve CVE-2018-5391): 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
  * ` suse-sap-cloud ` projesi (CVE-2018-5390 ve CVE-2018-5391): 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * ` ubuntu-os-cloud ` projesi (CVE-2018-5390 ve CVE-2018-5391): 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `

|  Yüksek  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  Yayınlanma tarihi: 03.01.2018

**son güncelleme tarihi: 21.05.2018 Saat 15:00 PST**

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  21.05.2018 Güncellemesi

[ CVE-2018-3640 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-3640) ve [ CVE-2018-3639
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639) , yani
sırasıyla Değişken 3a ve 4, [ Intel tarafından açıklanmıştır
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00115.html) . Spectre ve Meltdown'ın ilk üç varyantında, Compute Engine
sanal makine örneklerini çalıştıran altyapı korunmaktadır ve müşteri sanal
makine örnekleri izoledir ve birbirinden korunur. Ek olarak Compute Engine,
Intel'in mikrokod yamalarını altyapımıza dağıtmayı planlamaktadır. Bu sayede,
tek bir sanal makine örneği içinde güvenilmeyen veya çok kiracılı iş yükleri
çalıştıran müşteriler, işletim sistemi tedarikçileri ve sağlayıcıları
tarafından sunulduğunda sanal makineler arası ek hafifletmeleri
etkinleştirebilecektir. Compute Engine, mikrokod yamaları Intel tarafından
onaylandıktan ve üretim ortamımız için yamaları test edip onayladıktan sonra
yamaları dağıtacaktır. Kullanıma sunulduğunda bu sayfada daha ayrıntılı zaman
çizelgeleri ve güncellemeler sunacağız.

####  Açıklama

Bu CVE'ler, birçok işlemcide mevcut olan kurgusal yürütme teknolojisini kötüye
kullanan yeni bir tür saldırı sınıfı varyantlarıdır. Bu saldırı sınıfı,
çeşitli koşullar altında bellek verilerine yetkisiz salt okuma erişimi
sağlayabilir.

Compute Engine; kullanıcılara etkisi olmadan, zorunlu bakım dönemleri olmadan
ve toplu yeniden başlatma gerekmeden ana makine sistemi ve hipervizör
güncellemeleri yürütmek için Sanal Makine Canlı Geçiş teknolojisini
kullanmıştır. Ancak tüm konuk işletim sistemleri ve sürümlerine, bu
sistemlerin nerede çalıştığından bağımsız şekilde bu yeni saldırı sınıfına
karşı yama uygulanmalıdır.

Bu saldırı yöntemi ile ilgili tüm teknik ayrıntılar için [ Project Zero blog
yayınını ](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-
memory-with-side.html) okuyun. Tüm ürüne özel bilgiler dahil olmak üzere
Google'ın hafifletmelerine dair tüm ayrıntılar için [ Google Güvenlik blogu
yayınını ](https://security.googleblog.com/2018/01/todays-cpu-vulnerability-
what-you-need.html) okuyun.

####  Compute Engine'e etkisi

Compute Engine'i çalıştıran ve müşteri sanal makine örneklerini birbirinden
ayıran altyapı, bilinen saldırılara karşı korunur. Hafifletmelerimiz, ana
makine sistemlerimize sanal makine örnekleri içinde çalışan uygulamalardan
yetkisiz erişimi önlemektedir. Bu hafifletmeler, aynı ana makine sistemi
üzerinde çalışan sanal makine örnekleri arasındaki yetkisiz erişimi de önler.

Sanal makine örnekleriniz içinde yetkisiz erişimi önlemek için bu örnekler
üzerindeki konuk işletim sistemlerini aşağıdaki seçeneklerden birini
kullanarak güncellemeniz gerekir:

  * [ Mevcut sanal makine örneklerinizi yeniden oluşturmak ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=tr#publicimage) için yama uygulanmış genel görüntüler kullanma. Aşağıdan, yama uygulanmış genel görüntüler listesine bakın. 
  * Mevcut örnekleriniz üzerinde, dağıtımınız için işletim sistemi tedarikçisi tarafından sağlanan yamalar uygulama ve yama uygulanmış örnekleri yeniden başlatma. Her bir işletim sistemi tedarikçisinden gelen yama bilgileri için bağlantıları aşağıda görebilirsiniz. 

####  Yama uygulanmış görüntüler ve tedarikçi kaynakları

**Not:** Yama uygulanan görüntüler, bu güvenlik bülteninde listelenen tüm
CVE'ler için çözümler içermeyebilir. Ayrıca, farklı görüntüler bu tür
saldırıları önlemek için farklı yöntemler içerebilir. İşletim sistemi
tedarikçinizle görüşerek yamalarında ele aldıkları CVE'leri ve kullandıkları
önleme yöntemlerini doğrulayın.

  * ` cos-cloud ` projesi: Değişken 2 ( [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715) ) ve Değişken 3 ( [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754) ) saldırılarını önleyen yamalar içerir. Google, Varyant 2 saldırılarını hafifletmek için bu görüntülerde [ Retpoline ](https://support.google.com/faqs/answer/7625886?hl=tr) kullandı. 
    * ` cos-stable-63-10032-71-0 ` veya görüntü ailesi ` cos-stable `
  * ` centos-cloud ` projesi: [ CentOS yama bilgileri ](https://lwn.net/Alerts/CentOS/)
    * ` centos-7-v20180104 ` veya görüntü ailesi ` centos-7 `
    * ` centos-6-v20180104 ` veya görüntü ailesi ` centos-6 `
  * ` coreos-cloud ` projesi: [ CoreOS yama bilgileri ](https://coreos.com/blog/container-linux-meltdown-patch)
    * ` coreos-stable-1576-5-0-v20180105 ` veya görüntü ailesi ` coreos-stable `
    * ` coreos-beta-1632-1-0-v20180105 ` veya görüntü ailesi ` coreos-beta `
    * ` coreos-alpha-1649-0-0-v20180105 ` veya görüntü ailesi ` coreos-alpha `
  * ` debian-cloud ` projesi: [ Debian yama bilgileri ](https://www.debian.org/security/#DSAS)
    * ` debian-9-stretch-v20180105 ` veya görüntü ailesi ` debian-9 `
    * ` debian-8-jessie-v20180109 ` veya görüntü ailesi ` debian-8 `
  * ` rhel-cloud ` projesi: [ RHEL yama bilgileri ](https://access.redhat.com/security/vulnerabilities/speculativeexecution)
    * ` rhel-7-v20180104 ` veya görüntü ailesi ` rhel-7 `
    * ` rhel-6-v20180104 ` veya görüntü ailesi ` rhel-6 `
  * ` suse-cloud ` projesi: [ SUSE yama bilgileri ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-v20180104 ` veya görüntü ailesi ` sles-12 `
    * ` sles-11-sp4-v20180104 ` veya görüntü ailesi ` sles-11 `
  * ` suse-sap-cloud ` projesi: [ SUSE yama bilgileri ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-sap-v20180104 ` veya görüntü ailesi ` sles-12-sp3-sap `
    * ` sles-12-sp2-sap-v20180104 ` veya görüntü ailesi ` sles-12-sp2-sap `
  * ` ubuntu-os-cloud ` projesi: [ Ubuntu yama bilgileri ](https://insights.ubuntu.com/2018/01/04/ubuntu-updates-for-the-meltdown-spectre-vulnerabilities/)
    * ` ubuntu-1710-artful-v20180109 ` veya görüntü ailesi ` ubuntu-1710 `
    * ` ubuntu-1604-xenial-v20180109 ` veya görüntü ailesi ` ubuntu-1604-lts `
    * ` ubuntu-1404-trusty-v20180110 ` veya görüntü ailesi ` ubuntu-1404-lts `
  * ` windows-cloud ` ve ` windows-sql-cloud ` projeleri: 
    * Sürüm numarası ` -v20180109 ` ve üzeri olan tüm Windows Server ve SQL Server [ herkese açık görüntüleri ](https://cloud.google.com/compute/docs/images?hl=tr#os-compute-support) yama içerir. Ancak hem mevcut örneklerinizde hem de yeni oluşturulan örneklerde bu hafifletmeleri etkinleştirmek ve doğrulamak için Microsoft tarafından [ Windows Server ](https://support.microsoft.com/en-gb/help/4072698/windows-server-guidance-to-protect-against-the-speculative-execution) destek bülteni ile sağlanan önerilen işlemleri izlemeniz gerekir. 

[ Sanal makine örneklerinizi yeniden oluşturmak
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=tr#publicimage) için bu görüntüleri kullanın. Bu genel
görüntülerin erken sürümleri bu yamaları içermez ve potansiyel saldırıları
hafifletmez.

####  Donanım tedarikçilerinin yamaları

NVIDIA, NVIDIA® sürücü yazılımı yüklü olan sistemlere karşı potansiyel
saldırıları hafifletmek için yama uygulanmış sürücüler sağlamaktadır. Hangi
sürücü versiyonlarına yama uygulandığını öğrenmek için [ NVIDIA GPU Görüntü
Birimi Sürücüsü Güvenlik Güncellemeleri
](http://nvidia.custhelp.com/app/answers/detail/a_id/4611) güvenlik bültenini
okuyun.

####  Düzeltme geçmişi:

  * 21.05.2018, 14:00 PST: 21 Mayıs 2018'de açıklanan iki yeni varyant ile ilgili bilgi eklendi. 
  * 10.01.2018, 15:00 PST: Yama uygulanmış Windows Server ve SQL Server genel görüntüleri ile ilgili bilgi eklendi. 
  * 10.01.2018, 10:15 PST: Yama uygulanmış genel görüntüler listesine bazı Ubuntu görüntüleri eklendi. 
  * 10.01.2018, 09:50 PST: Donanım tedarikçilerine ait yamalar için talimatlar eklendi. 
  * 03.01.2018-09.01.2018: Yama uygulanmış genel görüntüler listesinde bazı düzeltmeler yapıldı. 

|  Yüksek  |

  * [ CVE-2017-5753 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5753)
  * [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715)
  * [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754)
  * [ CVE-2018-3640 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3640)
  * [ CVE-2018-3639 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639)

  
  
##  Yayınlanma tarihi: 02.10.2017

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

[ Dnsmasq ](http://www.thekelleys.org.uk/dnsmasq/doc.html) ; DNS, DHCP,
yönlendirici reklamları ve ağ önyüklemesi sunma işlevine sahiptir. Bu yazılım,
genellikle masaüstü Linux dağıtımları (ör. Ubuntu), evde kullanılan
yönlendiriciler ve IoT cihazları gibi çeşitli sistemlerde kuruludur. Dnsmasq
hem açık internette hem de özel ağlarda dahili olarak yaygın biçimde
kullanılmaktadır.

Düzenli dahili güvenlik değerlendirmeleri sırasında Google, yedi farklı sorun
keşfetmiştir. Sorunların ciddiyetini belirlemenin ardından, etkileri ve kötüye
kullanım potansiyelini saptamak amacıyla çalışmalar yürütülmüştür. Ardından,
şirket dahilinde bu sorunların her birinden kaynaklanabilecek sonuçlar
gösterilmiştir. Dnsmasq'ın geliştiricisi Simon Kelly ile uygun yamalar üretmek
ve sorundan doğacak zararları hafifletmek için bazı çalışmalar da yapılmıştır.

İnceleme sırasında ekip, 5 Eylül 2017 itibarıyla projenin git sunucusunun son
sürümünü etkileyen üç adet potansiyel uzaktan kod yürütme, bir bilgi sızıntısı
ve üç hizmet reddi güvenlik açığı saptamıştır.

Bu yamalar yukarı akışlı olup [ projenin Git kod deposuna
](http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=summary) bağlıdır.

####  Compute Engine'e etkisi

Varsayılan olarak Dnsmasq, yalnızca [ NetworkManager
](https://wikipedia.org/wiki/NetworkManager) kullanan ve etkin olmayan
(varsayılan olarak) görüntülere yüklenir. Aşağıdaki herkese açık Compute
Engine görüntülerine Dnsmasq yüklüdür:

  * Ubuntu 16.04, 16.10, 17.04 
  * CentOS 7 
  * RHEL 7 

Ancak diğer görüntülerde, diğer paketlere bağımlılık özelliğiyle Dnsmasq
yüklenmiş olabilir. En yeni işletim sistemi görüntüsünü kullanmak için Debian,
Ubuntu, CentOS, RHEL, SLES ve OpenSuse örneklerini güncellemenizi öneririz.
CoreOS ve Container İçin Optimize Edilmiş İşletim Sistemi, durumdan
etkilenmemektedir. Windows görüntüleri de durumdan etkilenmemektedir.

Debian ve Ubuntu'yu çalıştıran örnekler için, örneğinizde aşağıdaki komutları
çalıştırarak güncelleme yapabilirsiniz:

    
    
    
    sudo apt-get -y update
    
    
    
    sudo apt-get -y dist-upgrade

Red Hat Enterprise Linux ve CentOS örneklerinde şu kodu çalıştırın:

    
    
    
    sudo yum -y upgrade

SLES ve OpenSUSE görüntülerinde aşağıdaki komutu çalıştırın:

    
    
    
    sudo zypper up

Manuel güncelleme komutlarının çalıştırılmasına alternatif olarak, ilgili
işletim sisteminin [ görüntü ailelerini kullanarak sanal makine örneklerini
yeniden oluşturabilirsiniz
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=tr#publicimage) .

|  Yüksek  |

  * [ CVE-2017-14491 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14491)
  * [ CVE-2017-14492 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14492)
  * [ CVE-2017-14493 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14493)
  * [ CVE-2017-14494 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14494)
  * [ CVE-2017-14495 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14495)
  * [ CVE-2017-14496 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14496)
  * [ CVE-2017-13704 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-13704)

  
  
##  Yayınlanma tarihi: 26.10.2016

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

CVE-2016-5195; Linux çekirdeğinin bellek alt sistemi tarafından, yazma erişimi
üzerindeki salt okunur özel eşleme COW durumunun kesilmesi şeklindeki yarış
durumunu temsil eder.

Ayrıcalığı olmayan yerel kullanıcılar, bu açığı normalde salt okunur olan
bellek eşlemelerine yazma erişimi elde etmek ve bu sayede sistem üzerindeki
ayrıcalıklarını artırmak için kullanabilir.

Daha fazla bilgi edinmek için [ Dirty COW Hakkında SSS
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails)
bölümünü inceleyin.

####  Compute Engine'e etkisi

Compute Engine'deki tüm Linux dağıtımları ve sürümleri, bu sorundan etkilenir.
Örneklerin çoğu, yeni çekirdeği otomatik olarak indirir ve yükler. Ancak
çalışan sisteminize yama uygulamak için sistemi yeniden başlatmanız gerekir.

Aşağıdaki Compute Engine görüntülerini temel alan yeni veya yeniden
oluşturulan örneklerde zaten yama uygulanmış çekirdekler bulunmaktadır.

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

|  Yüksek  |  [ CVE-2016-5195
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails)  
  
##  Yayınlanma tarihi: 16.02.2016

**Son güncelleme tarihi: 22.02.2016**

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

CVE-2015-7547; glibc DNS istemci tarafı çözümleyicisinin, ` getaddrinfo() `
kitaplık işlevini kullanırken yazılımı yığın tabanlı arabellek taşmasına karşı
savunmasız hale getirdiği bir güvenlik açığıdır. Saldırganlar; bu güvenlik
açığını istismar etmek amacıyla saldırgan denetimindeki alan adları, saldırgan
tarafından denetlenen DNS sunucuları veya bağlantıyı izinsiz izleme
saldırısıyla bu işlevi kullanarak yazılımdan faydalanabilir.

Daha fazla bilgi edinmek için [ Google Dijital Güvenlik Blogu
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html) veya [ Common Vulnerabilities and Exposures (CVE)
](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-7547) veritabanını
inceleyin.

####  Compute Engine'e etkisi

**Güncelleme (22/02/2016):**

Artık aşağıdaki CoreOS, SLES ve OpenSUSE görüntülerini kullanarak
örneklerinizi yeniden oluşturabilirsiniz:

  * ` coreos-alpha-962-0-0-v20160218 `
  * ` coreos-beta-899-7-0-v20160218 `
  * ` coreos-stable-835-13-0-v20160218 `
  * ` opensuse-13-2-v20160222 `
  * ` opensuse-leap-42-1-v20160222 `
  * ` sles-11-sp4-v20160222 `
  * ` sles-12-sp1-v20160222 `

**Güncelleme (17.02.2016):**

Artık aşağıdaki komutları çalıştırarak Ubuntu 12.04 LTS, Ubuntu 14.04 LTS ve
Ubuntu 15.10 örneklerinde güncelleme yapabilirsiniz:

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Manuel güncelleme komutlarını çalıştırmaya alternatif olarak, artık örnekleri
aşağıdaki yeni görüntülerle yeniden oluşturabilirsiniz:

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

Bilgimiz dahilinde, varsayılan glibc yapılandırmasıyla Compute Engine'in DNS
çözümleyicilerini kullanarak bu güvenlik açığını kötüye kullanabilecek
herhangi bir yöntem bulunmamaktadır. Ancak zaman içinde, tüm yeni güvenlik
açıkları için yeni istismar yöntemleri keşfedilebilir. Bu nedenle yamaları
sanal makine örneklerine olabildiğince çabuk uygulamanız gerekir. edns0'ı
etkinleştirdiyseniz (varsayılan olarak devre dışıdır) örneklerinize yama
uygulanana kadar devre dışı bırakmanız gerekir.

**Orijinal bülten:**

Linux dağıtımınızda güvenlik açığı olabilir. Linux OS çalıştıran Compute
Engine müşterilerinin, bu güvenlik açığından etkilenmemek için örneklerinin
işletim sistemi görüntülerini güncellemesi gerekir.

Debian'ı çalıştıran örneklerde, güncellemeyi örneğinizde aşağıdaki komutları
çalıştırarak yapabilirsiniz:

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Ayrıca Debian örnekleriniz için [ UnattendedUpgrades
](https://wiki.debian.org/UnattendedUpgrades) 'i yüklemenizi öneririz.

Red Hat Enterprise Linux örnekleri için:

  * ` user@my-instance:~$ sudo yum -y upgrade `
  * ` user@my-instance:~$ sudo reboot `

Bu bülten, diğer işletim sistemi geliştiricileri bu güvenlik açığı için
yamalar yayınlandığı ve Compute Engine güncellenmiş işletim sistemi
görüntülerini kullanıma sunduğu sürece güncellenmeye devam edecektir.

|  Yüksek  |  [ CVE-2015-7547
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html)  
  
##  Yayınlanma tarihi: 19.03.2015

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

CVE-2015-1427; [ Elasticsearch
](https://www.elastic.co/products/elasticsearch) 'ün 1.3.8'den önceki
sürümlerinde ve 1.4.3'ten önceki herhangi bir 1.4.x sürümünde Groovy komut
dosyası motorunun, uzaktaki saldırganların korumalı alan mekanizmasını aşarak
rastgele kabuk komutları yürütebildiği bir güvenlik açığıdır.

Daha fazla bilgi için [ National Vulnerability Database (NVD)
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427) veya [
Common Vulnerabilities and Exposures (CVE) ](http://www.cve.mitre.org/cgi-
bin/cvename.cgi?name=2015-1427) veritabanını inceleyin.

####  Compute Engine'e etkisi

Compute Engine örneklerinde Elasticsearch kullanıyorsanız Elasticsearch'ü
1.4.3 veya daha yeni bir sürüme yükseltmeniz gerekir. Elasticsearch
yazılımınızın sürümünü zaten yükselttiyseniz bu güvenlik açığından
korunmaktasınız.

Elasticsearch'ü 1.4.3 veya daha yeni bir sürüme yükseltmediyseniz [ sıralı
yükseltme yapabilirsiniz
](http://www.elastic.co/guide/en/elasticsearch/reference/current/rolling-
upgrades.html) .

Elasticsearch'ü [ Google Cloud Platform Console
](https://console.cloud.google.com/?hl=tr) 'da [ Click-to-deploy
](https://cloud.google.com/solutions/elasticsearch/click-to-deploy?hl=tr)
işlemini kullanarak dağıttıysanız Elasticsearch'ü çalıştıran örnekleri
kaldırmak için [ dağıtımı silebilirsiniz
](https://console.cloud.google.com/projectselector/deployments?hl=tr) .

Google Cloud Platform ekibi, Elasticsearch'ün güncellenmiş sürümünün
dağıtılabilmesini sağlayacak bir düzeltme üzerinde çalışmaktadır. Ancak
düzeltme, [ GCP Console ](https://console.cloud.google.com/?hl=tr) 'daki
Click-to-deploy özelliğinde henüz kullanılamamaktadır.

|  Yüksek  |  [ CVE-2015-1427
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427)  
  
##  Yayınlanma tarihi: 29.01.2015

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

[ CVE-2015-0235 (Hayalet)
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235) , glibc
kitaplığındaki bir güvenlik açığıdır.

App Engine, Cloud Storage, BigQuery ve CloudSQL müşterilerinin herhangi bir
işlem yapması gerekmez. Google sunucuları güncellenmiştir ve bu güvenlik
açığına karşı korunmaktadır.

Compute Engine müşterilerinin işletim sistemi görüntülerini güncellemesi
gerekebilir.

####  Compute Engine'e etkisi

Linux dağıtımınızda güvenlik açığı olabilir. Debian 7, Debian 7 backport'ları,
Ubuntu 12.04 LTS, Red Hat Enterprise Linux, CentOS veya SUSE Linux Enterprise
Server 11 SP3 çalıştıran Compute Engine müşterilerinin, bu güvenlik açığından
etkilenmemek için örneklerinin işletim sistemi görüntülerini güncellemesi
gerekir.

Bu güvenlik açığı Ubuntu 14.04 LTS, Ubuntu 14.10 veya SUSE Linux Enterprise
Server 12'yi etkilemez.

Linux dağıtımlarınızı yükseltmenizi öneririz. Debian 7, Debian 7 backport'ları
veya Ubuntu 12.04 LTS'yi çalıştıran örneklerde aşağıdaki komutları kullanarak
güncelleme yapabilirsiniz:

  1. ` user@my-instance:~$ sudo apt-get update `
  2. ` user@my-instance:~$ sudo apt-get -y upgrade `
  3. ` user@my-instance:~$ sudo reboot `

Red Hat Enterprise Linux veya CentOS örnekleri için:

  1. ` user@my-instance:~$ sudo yum -y upgrade `
  2. ` user@my-instance:~$ sudo reboot `

SUSE Linux Enterprise Server 11 SP3 örnekleri için:

  1. ` user@my-instance:~$ sudo zypper --non-interactive up `
  2. ` user@my-instance:~$ sudo reboot `

Yukarıda belirtilen manuel güncelleme komutlarını çalıştırmaya alternatif
olarak, kullanıcılar artık örnekleri aşağıdaki yeni görüntülerle yeniden
oluşturabilir:

  * ` debian-7-wheezy-v20150127 `
  * ` backports-debian-7-wheezy-v20150127 `
  * ` centos-6-v20150127 `
  * ` centos-7-v20150127 `
  * ` rhel-6-v20150127 `
  * ` rhel-7-v20150127 `
  * ` sles-11-sp3-v20150127 `
  * ` ubuntu-1204-precise-v20150127 `

####  Google Tarafından Yönetilen Sanal Makinelere etkisi

` gcloud preview app deploy ` kullanan, yönetilen sanal makine
kullanıcılarının; temel docker container'larını, ` gcloud preview app setup-
managed-vms ` ile güncellemesi ve çalışan uygulamalarından her birini, `
gcloud preview app deploy ` ile yeniden dağıtması gerekir. ` appcfg ` ile
dağıtım yapan kullanıcıların herhangi bir işlem yapması gerekmez ve bu
kullanıcılar, otomatik olarak yeni sürüme geçirilir.

|  Yüksek  |  [ CVE-2015-0235
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235)  
  
##  Yayınlanma tarihi: 15.10.2014

**Son güncelleme tarihi: 17.10.2014**

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

CVE-2014-3566 (diğer adıyla POODLE), SSL 3.0 sürümü tasarımındaki bir güvenlik
açığıdır. Bu güvenlik açığı, ağ saldırganlarının güvenli bağlantılardaki düz
metinleri hesaplayabilmesini sağlar. Ayrıntılı bilgi için güvenlik açıkları
hakkında yayınlanan [ blog yayınlarımızı
](http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-
exploiting-ssl-30.html) inceleyin.

App Engine, Cloud Storage, BigQuery ve CloudSQL müşterilerinin herhangi bir
işlem yapması gerekmez. Google sunucuları güncellenmiştir ve bu güvenlik
açığına karşı korunmaktadır. Compute Engine müşterilerinin, işletim sistemi
görüntülerini güncellemesi gerekir.

####  Compute Engine'e etkisi

**Güncelleme (17/10/2014):**

SSLv3 kullanıyorsanız güvenlik açığından etkilenebilirsiniz. Compute Engine
müşterilerinin, bu güvenlik açığından etkilenmemek için örneklerinin işletim
sistemi görüntülerini güncellemesi gerekir.

Linux dağıtımlarınızı yükseltmenizi öneririz. Debian'ı çalıştıran
örneklerinizde aşağıdaki komutları kullanarak güncelleme yapabilirsiniz:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

CentOS örnekleri için:

    
    
    
    user@my-instance:~$ sudo yum -y upgrade
    user@my-instance:~$ sudo reboot

Yukarıda belirtilen manuel güncelleme komutlarını çalıştırmaya alternatif
olarak, kullanıcılar artık örnekleri aşağıdaki yeni görüntülerle yeniden
oluşturabilir:

  * ` centos-6-v20141016 `
  * ` centos-7-v20141016 `
  * ` debian-7-wheezy-v20141017 `
  * ` backports-debian-7-wheezy-v20141017 `

Görüntüler elde edildikten sonra RHEL ve SLES görüntüleriyle ilgili bültenler
güncellenecektir. Bu sırada RHEL kullanıcıları, daha fazla bilgi için [
doğrudan Red Hat ](https://access.redhat.com/articles/1232123) 'e danışabilir.

**Orijinal bülten:**

Compute Engine müşterilerinin, bu güvenlik açığından etkilenmemek için
örneklerinin işletim sistemi görüntülerini güncellemesi gerekir. Yeni işletim
sistemi görüntüleri elde edildikten sonra bu güvenlik bülteni, talimatlarla
güncellenecektir.

|  Orta  |  [ CVE-2014-3566
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-3566)  
  
##  Yayınlanma tarihi: 24.09.2014

**son güncelleme tarihi: 29.09.2014**

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

Bash'te (CVE-2014-6271) saldırgan tarafından kontrol edilen herhangi bir ortam
değişkeni ayrıştırmasına dayalı olarak kodun uzaktan yürütülmesine izin veren
bir hata bulunmaktadır. En sık karşılaşılan istismar vektörü, web sunucusunda
sunulan CGI komut dosyalarına yapılan kötü amaçlı HTTP istekleri yoluyla
gerçekleştirilir. Daha fazla bilgi için [ hata açıklaması
](http://seclists.org/oss-sec/2014/q3/650) bölümünü inceleyin.

26.09.2014 tarihinden önceki Compute Engine konuk işletim sistemi görüntüleri
haricindeki bash hatalarının taşıdığı risk oranı, Google Cloud Platform
Ürünleri için azaltılmıştır. Compute Engine görüntülerinizdeki hata riskini
azaltmak için gerekli olan adımlara aşağıdan ulaşabilirsiniz.

####  Compute Engine'e etkisi

Bu hata, CGI komut dosyalarının kullanıldığı neredeyse tüm web sitelerini
etkileyebilir. Ayrıca PHP, Perl, Python, SSI, Java, C++ ve benzeri servlet'ler
üzerinden çalışan ve ` popen ` , ` system ` , ` shell_exec ` veya benzeri
API'ler gibi çağrılar aracılığıyla kabuk komutlarını çağıran web sitelerini de
etkileyebilir. Bu durum, erişimi sınırlı olan kullanıcılara SSH komut
sınırlaması veya bash sınırlı kabuk gibi mekanizmalar yoluyla kontrollü oturum
açma erişimine izin vermeye çalışan sistemleri de etkileyebilir.

**Güncelleme (29.09.2014):**

Aşağıda belirtilen manuel güncelleme komutlarını çalıştırmaya alternatif
olarak kullanıcılar, artık örneklerini bash güvenlik hatalarıyla ( [
CVE-2014-7169 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169)
, [ CVE-2014-6277
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277) , [
CVE-2014-6278 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278)
, [ CVE-2014-7186
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186) ve [
CVE-2014-7187 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)
dahil) alakalı ek güvenlik açığı riskini azaltan görüntülerle yeniden
oluşturabilir. Örneklerinizi tekrar oluşturmak için aşağıdaki yeni görüntüleri
kullanın:

  * ` centos-6-v20140926 `
  * ` centos-7-v20140926 `
  * ` debian-7-wheezy-v20140926 `
  * ` backports-debian-7-wheezy-v20140926 `
  * ` rhel-6-v20140926 `

**Güncelleme (25.09.2014):**

Kullanıcılar artık manuel güncelleme yapmak yerine örneklerini yeniden
oluşturabilir. Örneklerinizi yeniden oluşturmak için bu güvenlik hatasına
yönelik düzeltmeleri içeren aşağıdaki yeni görüntüleri kullanın:

  * ` backports-debian-7-wheezy-v20140924 `
  * ` debian-7-wheezy-v20140924 `
  * ` rhel-6-v20140924 `
  * ` centos-6-v20140924 `
  * ` centos-7-v20140924 `

RHEL ve SUSE görüntüleri için, örnekleriniz üzerinde aşağıdaki komutları
çalıştırıp güncellemeleri manuel olarak yapabilirsiniz:

    
    
    
    # RHEL instances
    user@my-instance:~$ sudo yum -y upgrade
    
    # SUSE instances
    user@my-instance:~$ sudo zypper --non-interactive up

**Orijinal bülten:**

Linux dağıtımlarınızı yükseltmenizi öneririz. Debian'ı çalıştıran
örneklerinizde aşağıdaki komutları çalıştırarak güncelleme yapabilirsiniz:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    

CentOS örnekleri için:

    
    
    
    user@my-instance:~$ sudo yum -y upgrade

Ayrıntılı bilgi için ilgili Linux dağıtımıyla alakalı duyuruyu inceleyin:

  * Orijinal yamalar: [ http://ftp.gnu.org/gnu/bash/ ](http://ftp.gnu.org/gnu/bash/) (kullandığınız sürüm için *-patches dosyalarındaki son girişi inceleyin) 
  * Debian: [ [SECURITY] [DSA 3032-1] bash security update ](https://lists.debian.org/debian-security-announce/2014/msg00220.html)
  * RHEL: 
    * [ RHSA-2014:1293-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00048.html)
    * [ RHSA-2014:1294-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00049.html)
  * CentOS 5: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020582.html)
  * CentOS 6: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020585.html)
  * CentOS 7: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020583.html)

|  Yüksek  |  [ CVE-2014-7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) , [
CVE-2014-6271 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6271)
, [ CVE-2014-6277
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277) , [
CVE-2014-6278 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278)
[ CVE-2014-7186
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186) , [
CVE-2014-7187 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)  
  
##  Yayınlanma tarihi: 25.07.2014

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

[ Elasticsearch Logstash ](http://www.elasticsearch.org/overview/logstash/) ,
verilerin yetkisiz olarak değiştirilmesi ve ifşa edilmesine izin verebilen
işletim sistemi komutlarının eklenmesine karşı savunmasızdır. Saldırgan,
hazırlanan olayları Logstash'in herhangi bir veri kaynağına gönderebilir.
Böylece Logstash işleminin iznini alarak komutları yürütebilir.

####  Compute Engine'e etkisi

Bu güvenlik açığı, zabbix veya nagios_nsca çıkışlarının etkinleştirildiği ve
Elasticsearch Logstash'in 1.4.2'den önceki sürümlerini çalıştıran tüm Compute
Engine örneklerini etkiler. Saldırıyı önlemek için aşağıdakilerden birini
yapabilirsiniz:

  * Logstash 1.4.2 sürümüne geçme 
  * 1.3.x sürümleri için yamayı uygulama 
  * ` zabbix ` ve ` nagios_nsca ` çıkışlarını devre dışı bırakma. 

[ Logstash blogundan ](http://www.elasticsearch.org/blog/logstash-1-4-2/) daha
fazla bilgi edinebilirsiniz.

Ayrıca Elasticsearch, güvenilir olmayan IP'lerin uzaktan erişimini önlemek
için [ güvenlik duvarı kullanmanızı
](http://www.elasticsearch.org/blog/scripting-security/) önerir.

|  Yüksek  |  [ CVE-2014-4326
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-4326)  
  
##  Yayınlanma tarihi: 18.06.2014

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

Müşterilerin, Google Cloud Platform'da çalışırken Docker container'larının
güvenliği hakkında doğabilecek endişelerine değinmek istiyoruz. Bu durum,
Docker Container'larını, container için optimize edilmiş sanal makineleri veya
Açık Kaynaklı Kubernetes zamanlayıcısını destekleyen Google App Engine
uzantılarını kullanan müşterileri ilgilendirmektedir.

Docker, konuyu ustaca ele almıştır. İlgili blog yazısına [ buradan
](http://blog.docker.com/2014/06/docker-container-breakout-proof-of-concept-
exploit/) ulaşabilirsiniz. Yazılarında da belirtildiği gibi, açıklanan sorunun
yalnızca daha eski, üretim öncesi bir sürüm olan Docker 0.11 için geçerli
olduğunu hatırlatmak isteriz.

Container güvenliği tüm dünyada üzerine düşünülen bir konu. Google Cloud
Platform'da, Linux uygulama container'ına dayalı çözümlerin (özellikle Docker
container'ları) tamamen sanal makinelerde (Compute Engine) çalıştığını
belirtmek isteriz. Docker topluluğunun Linux uygulama container yığınını daha
güvenli hale getirme çabalarına destek vermekteyiz. Ancak teknolojinin yeni,
yüzey alanının ise geniş olduğunun farkındayız. Şimdilik, tam hipervizörlerin
(sanal makineler) daha kompakt ve savunulabilir bir yüzey alanına sahip olduğu
kanaatindeyiz. Sanal makineler, kötü amaçlı iş yüklerini ayırmak ve kod
hatalarının görülme ihtimaliyle etkisini en aza indirmek için baştan
tasarlanmıştır.

Müşterilerimiz, üçüncü taraf kötü amaçlı olabilecek kodlarla kendileri
arasında tam hipervizörlerin yer aldığından emin olabilir. Linux uygulama
container yığınının, çok kiracılı iş yüklerini destekleyecek kadar sağlam
olduğuna karar verilirse topluluk, bu durumdan haberdar edilecektir. Şimdilik
Linux uygulama container'ı, sanal makinenin yerini alamamaktadır. Container,
sanal makineden daha fazla yararlanabilmenizi sağlar.

|  Düşük  |  [ Docker blog yayını ](http://blog.docker.com/2014/06/docker-
container-breakout-proof-of-concept-exploit/)  
  
##  Yayınlanma tarihi: 05.06.2014

**Son güncelleme tarihi: 09.06.2014**

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

OpenSSL'de, ` ChangeCipherSpec ` mesajlarının el sıkışma durumu makinesine
doğru şekilde bağlanmama sorunu görülmektedir. Bu hata, mesajların el
sıkışmaya erkenden eklenmesine neden olur. Dikkatlice hazırlanmış bir el
sıkışma kullanan saldırganlar, OpenSSL SSL/TLS istemci ve sunucularında zorla
zayıf anahtarlama malzemesi kullanılmasına neden olabilir. Bu durum,
saldırganın saldırıya uğrayan istemci ve sunucu trafiğini çözüp değiştirdiği,
bağlantıyı izinsiz izleme (MITM) saldırısı tarafından istismar edilebilir.

Bu sorun [ CVE-2014-0224 ](https://www.openssl.org/news/secadv/20140605.txt)
koduyla tanımlanmıştır. OpenSSL ekibi sorunu çözmüş, OpenSSL topluluğunu
OpenSSL'yi güncelleme konusunda uyarmıştır.

####  Compute Engine'e etkisi

Bu güvenlik açığı; Debian, CentOS, Red Hat Enterprise Linux ve SUSE Linux
Enterprise Server da dahil olmak üzere OpenSSL kullanan tüm Compute Engine
örneklerini etkiler. Örneklerinizi yeni görüntülerle yeniden oluşturarak
güncelleyebilirsiniz. Örneklerinizdeki paketleri manuel olarak güncelleme
yönteminden de yararlanabilirsiniz.

**Güncelleme (09.06.2014):** SUSE Linux Enterprise Server çalıştıran
örneklerinizi yeni görüntülerle güncellemek için aşağıdaki görüntü sürümlerini
veya daha yenilerini kullanarak örneklerinizi yeniden oluşturun:

  * ` sles-11-sp3-v20140609 `

**Orijinal yayın:**

Yeni görüntüler kullanarak Debian ve CentOS örneklerini güncellemek için
aşağıdaki görüntü sürümlerini veya daha yenilerini kullanarak örneklerinizi
yeniden oluşturun:

  * ` debian-7-wheezy-v20140605 `
  * ` backports-debian-7-wheezy-v20140605 `
  * ` centos-6-v20140605 `
  * ` rhel-6-v20140605 `

Örneklerinizde OpenSSL'yi manuel olarak güncellemek için aşağıdaki komutları
çalıştırarak uygun paketleri güncelleyin. CentOS ve RHEL'yi çalıştıran
örneklerde, bu komutları kendi örneğinizde çalıştırarak OpenSSL'yi
güncelleyebilirsiniz:

    
    
    
    user@my-instance:~$ sudo yum -y update
    user@my-instance:~$ sudo reboot

Debian'ı çalıştıran örneklerinizde aşağıdaki komutları çalıştırarak OpenSSL'yi
güncelleyebilirsiniz:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

SUSE Linux Enterprise Server'ı çalıştıran örneklerinizde aşağıdaki komutları
çalıştırarak OpenSSL'nin güncel olmasını sağlayabilirsiniz:

    
    
    
    user@my-instance:~$ sudo zypper --non-interactive up
    user@my-instance:~$ sudo reboot

|  Orta  |  [ CVE-2014-0224
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0224)  
  
##  Yayınlanma tarihi: 08.04.2014

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

1.0.1g'den önceki OpenSSL 1.0.1'de bulunan (1) TLS ve (2) DTLS uygulamaları,
Heartbeat Uzantı paketlerini düzgün bir şekilde çalıştıramamaktadır. Bu,
uzaktaki saldırganların, arabelleğin fazla okunmasını tetikleyen hazırlanmış
paketler yoluyla hassas bilgiler edinmesine yol açar. Bu durum, Heartbleed
hatası olarak da bilinen ` d1_both.c ` ve ` t1_lib.c ` ile ilgili gizli
anahtarların okunmasıyla da gösterilmiştir.

####  Compute Engine'e etkisi

Bu güvenlik açığı, OpenSSL'nin en güncel sürüme sahip olmayan Compute Engine
Debian, RHEL ve CentOS örneklerini etkiler. Örneklerinizi yeni görüntülerle
yeniden oluşturarak güncelleyebilirsiniz. Örneklerinizdeki paketleri manuel
olarak güncelleme yönteminden de yararlanabilirsiniz.

Yeni görüntüler kullanarak örneklerinizi güncellemek için aşağıdaki görüntü
sürümlerini veya daha yenilerini kullanarak örneklerinizi yeniden oluşturun:

  * ` debian-7-wheezy-v20140408 `
  * ` backports-debian-7-wheezy-v20140408 `
  * ` centos-6-v20140408 `
  * ` rhel-6-v20140408 `

Örneklerinizde OpenSSL'yi manuel olarak güncellemek için aşağıdaki komutları
çalıştırarak uygun paketleri güncelleyin. CentOS ve RHEL'yi çalıştıran
örneklerde, bu komutları kendi örneğinizde çalıştırarak OpenSSL'nin güncel
olmasını sağlayabilirsiniz:

    
    
    
    user@my-instance:~$ sudo yum update
    user@my-instance:~$ sudo reboot

Debian'ı çalıştıran örneklerinizde aşağıdaki komutları çalıştırarak OpenSSL'yi
güncelleyebilirsiniz:

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get upgrade
    user@my-instance:~$ sudo reboot

SUSE Linux çalıştıran örnekler, bu durumdan etkilenmez.

**14 Nisan 2014 tarihli güncelleme:** Compute Engine; Heartbleed hatalarını
kullanarak anahtarları ayıklama üzerine yapılan yeni araştırmaların sonucunda,
Compute Engine müşterilerinin etkilenen tüm SSL hizmetleri için yeni
anahtarlar oluşturmasını önermektedir.

|  Orta  |  [ CVE-2014-0160
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0160)  
  
##  Yayınlanma tarihi: 07.06.2013

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

**Not:** Bu güvenlik açığı, yalnızca API v1 sürümünden itibaren silinen ve
kullanımdan kaldırılan çekirdekler için geçerlidir.

3.9.4 ve öncesi sürümlere sahip olan Linux çekirdeğindeki Broadcom B43
kablosuz sürücüsünün ` drivers/net/wireless/b43/main.c ` üzerindeki `
b43_request_firmware ` işlevinde yer alan biçim dizesi güvenlik açığı, yerel
kullanıcıların kök erişiminden yararlanarak ve ` fwpostfix ` modprobe
parametresindeki biçim dizesi belirteçlerini dahil ederek ayrıcalık
kazanmasına yol açar. Bu da, hata mesajının yanlış biçimde oluşturulmasına
neden olur.

####  Compute Engine'e etkisi

Bu güvenlik açığı, ` gcg-3.3.8-201305291443 ` ve daha eski tüm Compute Engine
çekirdeklerini etkiler. Compute Engine, çözüm olarak önceki tüm çekirdekleri
kullanımdan kaldırmış ve kullanıcılarına, örnek ve görüntülerini Compute
Engine ` gce-v20130603 ` çekirdeğini kullanacak şekilde güncellemelerini
önermiştir. ` gce-v20130603 ` , bu güvenlik açığı için yamaya sahip `
gcg-3.3.8-201305291443 ` çekirdeğini içerir.

Örneğinizin hangi çekirdek sürümünü kullandığını öğrenmek için:

  1. Örneğinize ssh uygulayın 
  2. ` uname -r ` komutunu çalıştırın 

|  Orta  |  [ CVE-2013-2852
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2852)  
  
##  Yayınlanma tarihi: 07.06.2013

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

**Not:** Bu güvenlik açığı, yalnızca API v1 sürümünden itibaren silinen ve
kullanımdan kaldırılan çekirdekler için geçerlidir.

3.9.4 ve öncesi sürümlere sahip olan Linux çekirdeğinde, ` block/genhd.c `
üzerindeki register_disk işlevinde yer alan biçim dizesi güvenlik açığı, yerel
kullanıcıların hazırlanmış ` /dev/md ` cihaz adı oluşturmak için kök
erişiminden yararlanmalarına ve ` /sys/module/md_mod/parameters/new_array `
için biçim dizesi tanımlayıcılarını yazmalarına izin verir.

####  Compute Engine'e etkisi

Bu güvenlik açığı, ` gcg-3.3.8-201305291443 ` ve daha eski tüm Compute Engine
çekirdeklerini etkiler. Compute Engine, çözüm olarak önceki tüm çekirdekleri
kullanımdan kaldırmış ve kullanıcılarına, örnek ve görüntülerini Compute
Engine ` gce-v20130603 ` çekirdeğini kullanacak şekilde güncellemelerini
önermiştir. ` gce-v20130603 ` , bu güvenlik açığı için yamaya sahip `
gcg-3.3.8-201305291443 ` çekirdeğini içerir.

Örneğinizin hangi çekirdek sürümünü kullandığını öğrenmek için:

  1. Örneğinize ssh uygulayın 
  2. ` uname -r ` komutunu çalıştırın 

|  Orta  |  [ CVE-2013-2851
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2851)  
  
##  Yayınlanma tarihi: 14.05.2013

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

**Not:** Bu güvenlik açığı, yalnızca API v1 sürümünden itibaren silinen ve
kullanımdan kaldırılan çekirdekler için geçerlidir.

3.8.9 öncesi sürümlere sahip Linux çekirdeğinde yer alan `
kernel/events/core.c ` üzerindeki perf_swevent_init işlevi, yanlış ` integer `
veri türünü kullanır. Bu da, yerel kullanıcıların hazırlanmış bir `
perf_event_open ` sistem çağrısı üzerinden ayrıcalık kazanabilmesine neden
olur.

####  Compute Engine'e etkisi

Bu güvenlik açığı, ` gcg-3.3.8-201305211623 ` ve daha eski tüm Compute Engine
çekirdeklerini etkiler. Compute Engine, çözüm olarak önceki tüm çekirdekleri
kullanımdan kaldırmış ve kullanıcılarına, örnek ve görüntülerini Compute
Engine ` gce-v20130521 ` çekirdeğini kullanacak şekilde güncellemelerini
önermiştir. ` gce-v20130521 ` , bu güvenlik açığı için yamaya sahip `
gcg-3.3.8-201305211623 ` çekirdeğini içerir.

Örneğinizin hangi çekirdek sürümünü kullandığını öğrenmek için:

  1. Örneğinize ssh uygulayın 
  2. ` uname -r ` komutunu çalıştırın 

|  Yüksek  |  [ CVE-2013-2094
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2094)  
  
##  Yayınlanma tarihi: 18.02.2013

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  Açıklama

**Not:** Bu güvenlik açığı, yalnızca API v1 sürümünden itibaren silinen ve
kullanımdan kaldırılan çekirdekler için geçerlidir.

3.7.5 öncesi sürümlere sahip olan Linux çekirdeğinin ptrace işlevindeki yarış
durumu, yerel kullanıcıların hazırlanmış bir uygulamadaki ` PTRACE_SETREGS
ptrace ` sistem çağrısı yoluyla ayrıcalık kazanabilmesine neden olur.

####  Compute Engine'e etkisi

Bu güvenlik açığı, Compute Engine'in ` 2.6.x-gcg- _ <date> _ ` çekirdeklerini
etkiler. Compute Engine, çözüm olarak 2.6.x sürümüne sahip çekirdekleri
kullanımdan kaldırmış ve kullanıcılarına, örnek ve görüntülerini Compute
Engine ` gce-v20130225 ` çekirdeğini kullanacak şekilde güncellemelerini
önermiştir. ` gce-v20130225 ` , bu güvenlik açığı için yamaya sahip `
3.3.8-gcg-201302081521 ` çekirdeğini içerir.

Örneğinizin hangi çekirdek sürümünü kullandığını öğrenmek için:

  1. Örneğinize ssh uygulayın 
  2. ` uname -r ` komutunu çalıştırın 

|  Orta  |  [ CVE-2013-0871
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-0871)

