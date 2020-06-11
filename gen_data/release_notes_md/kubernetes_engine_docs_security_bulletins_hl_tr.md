#  Güvenlik bültenleri

Google Kubernetes Engine (GKE) ile ilgili tüm güvenlik bültenleri bu belgede
açıklanmaktadır.

Güvenlik açıkları, etkilenen taraflar bunları ele alma imkanı bulana kadar
genellikle ambargolu şekilde gizli tutulur. Bu durumlarda, ambargo
kaldırılıncaya kadar GKE'nin [ Sürüm Notları
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=tr) 'nda
"güvenlik güncellemelerinden" bahsedilir. Bu noktada, sürüm notları yamanın
ele aldığı güvenlik açığını yansıtacak şekilde güncellenir.

**Not:** GKE üzerinde çok kiracılı iş yükleri çalıştırıyorsanız lütfen bu
bültenlere özellikle dikkat edin. Bu güvenlik açıklarının çok kiracılı iş
yüklerini etkilemesi daha olasıdır. GKE'deki güvenlik sınırları ve bunların iş
yüklerini nasıl etkilediğiyle ilgili teknik açıklamalar için [ Kubernetes
yığınının farklı katmanlarında yalıtım
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) bölümüne bakın.

En son yayınlanan bültenleri almak istiyorsanız bu sayfanın URL'sini [ feed
okuyucunuza ](https://wikipedia.org/wiki/Comparison_of_feed_aggregators)
ekleyin veya feed URL'sini doğrudan ekleyin: `
https://cloud.google.com/feeds/kubernetes-engine-security-bulletins.xml `

##  GCP-2020-005

**Yayınlanma tarihi:** 07.05.2020  
**Güncellenme tarihi:** 07.05.2020  Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
Yakın zamanda Linux çekirdeğinde, [ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) ile açıklanan bir güvenlik açığı tespit
edildi. Bu güvenlik açığı, container'ın kod dışına alınmasıyla ana makine
düğümünde kök ayrıcalıkları edinmesine izin verir.

GKE'nin 1.16 veya 1.17 sürümlerini çalıştıran Google Kubernetes Engine (GKE)
Ubuntu düğümleri bu güvenlik açığından etkilenmektedir. Aşağıda ayrıntılarıyla
açıkladığımız şekilde, en kısa süre içinde son yama sürümüne yükseltmenizi
öneririz.

Container-Optimized OS çalıştıran düğümler bu güvenlik açığından etkilenmez.
GKE On-Prem çalıştıran düğümler etkilenmez.

####  Ne yapmalıyım?

**Çoğu müşterinin herhangi bir işlem yapması gerekmez. Yalnızca GKE'nin 1.16
veya 1.17 sürümünde Ubuntu çalıştıran düğümler etkilenmektedir.**

Düğümlerinizi yükseltmek için öncelikle ana düğümünüzü en yeni sürüme
yükseltmeniz gerekir. Bu yama, Kubernetes 1.16.8-gke.12, 1.17.4-gke.10 ve daha
yeni sürümlerde kullanılabilecektir. Bu yamaların kullanıma sunulma durumunu [
sürüm notlarından ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=tr) takip edebilirsiniz.

####  Bu yama hangi güvenlik açığına yönelik?

Yama, aşağıdaki güvenlik açığı riskini azaltır:

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) , Linux'un 5.5.0 ve üzeri çekirdek
sürümlerindeki bir güvenlik açığını tanımlar. Bu güvenlik açığı, kötü amaçlı
bir container'ın (yürütme açısından minimum kullanıcı etkileşimi bulunan)
çekirdek belleğini okuyup yazmasına ve böylece ana makine düğümünde kök
düzeyinde kod yürütme yetkisi elde etmesine olanak tanır. Bu güvenlik açığı,
"Yüksek" önem düzeyli güvenlik açığı olarak derecelendirilmiştir.

|

Yüksek

|

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835)  
  
  
##  GCP-2020-003

**Yayınlanma tarihi:** 31.03.2020  
**Güncellenme tarihi:** 31.03.2020  Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
Yakın zamanda Kubernetes'te [ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) ile açıklanan bir güvenlik açığı tespit
edildi. Güvenlik açığı, POST isteği yapma yetkisi olan tüm kullanıcılara, bir
Kubernetes API sunucusuna uzaktan Hizmet Reddi saldırısı yürütme izni verir.
Kubernetes Ürün Güvenliği Komitesi'nin (PSC) bu güvenlik açığıyla ilgili
yayınladığı ek bilgilere [ buradan
](https://groups.google.com/forum/?hl=tr#!topic/kubernetes-security-
announce/wuwEwZigXBc) ulaşabilirsiniz.

[ Ana Yetkili Ağları ](https://cloud.google.com/kubernetes-engine/docs/how-
to/authorized-networks?hl=tr) ve [ Herkese açık uç noktası olmayan özel
kümeleri ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=tr#private_master) kullanan GKE Kümeleri, bu güvenlik açığının
risklerini azaltır.

####  Ne yapmalıyım?

Kümenizi, bu güvenlik açığının çözümünü içeren bir yama sürümüne yükseltmenizi
öneririz.

Çözümün yer aldığı yama sürümlerinin listesi aşağıda verilmiştir:

  * 1.13.12-gke.29 
  * 1.14.9-gke.27 
  * 1.14.10-gke.24 
  * 1.15.9-gke.20 
  * 1.16.6-gke.1 

####  Bu yama hangi güvenlik açıklarına yönelik?

Yama ile aşağıdaki Hizmet Reddi (DoS) güvenlik açıkları düzeltilir:

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) .

|

Orta

|

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  GCP-2020-002

**Yayınlanma tarihi:** 23.03.2020  
**Güncellenme tarihi:** 23.03.2020  Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
Kubernetes tarafından biri API sunucusunu ve diğeri Kubelet'leri etkileyen [
iki hizmet reddi güvenlik açığı
](https://groups.google.com/forum/?hl=tr#!topic/kubernetes-security-
announce/2UOlsba2g0s) açıklanmıştır. Daha fazla bilgi için [ 89377
](https://github.com/kubernetes/kubernetes/issues/89377) ve [ 89378
](https://github.com/kubernetes/kubernetes/issues/89378) numaralı Kubernetes
sorunlarını inceleyin.

####  Ne yapmalıyım?

Güvenilmeyen kullanıcılar kümenin dahili ağında istek gönderemediği sürece tüm
GKE kullanıcıları CVE-2020-8551 güvenlik açığına karşı korumaya alınmıştır. Ek
olarak [ ana sistem yetkili ağların ](https://cloud.google.com/kubernetes-
engine/docs/how-to/authorized-networks?hl=tr) kullanılması CVE-2020-8552
riskini azaltır.

####  Bunlar için ne zaman yama uygulanacak?

CVE-2020-8551 yamaları için düğümlerin yeni sürüme geçirilmesi gerekir.
Çözümün yer alacağı yama sürümlerinin listesi aşağıda verilmiştir:

  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

Not: 1.14.x ve önceki sürümler bu güvenlik açığından etkilenmez ve dolayısıyla
bunlar için yama gerekmez.

CVE-2020-8552 yamaları için ana sistemin yeni sürüme geçirilmesi gerekir.
Çözümün yer alacağı yama sürümlerinin listesi aşağıda verilmiştir:

  * 1.14.10-gke.32 
  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

|

Orta

|

[ CVE-2020-8551 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8551)  
[ CVE-2020-8552 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8552)  
  
##  21 Ocak 2020; son güncelleme 24 Ocak 2020

**Yayınlanma tarihi:** 21.01.2020  
**Güncellenme tarihi:** 24.01.2020  Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
**24.01.2020 Tarihli Güncelleme:** Yama uygulanmış sürümlerin kullanıma
sunulması üzerinde çalışılmaktadır ve süreç 25 Ocak 2020'de tamamlanacaktır.

* * *

Microsoft, Windows Crypto API'de ve eliptik eğri algoritmalı imzaları
doğrulama işlevinde bir güvenlik açığı bulunduğunu açıkladı. Daha fazla bilgi
için lütfen [ Microsoft'un açıklamasına
](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) bakın.

**Ne yapmalıyım?**

**Çoğu müşterinin herhangi bir işlem yapması gerekmez. Yalnızca üzerinde
Windows Server çalışan düğümler etkilenir.**

Windows Server düğümleri kullanan müşteriler, bu güvenlik açığının riskini
hafifletmek için hem düğümleri hem de bu düğümler üzerinde çalışan container
mimarisine alınmış iş yüklerini yama uygulanmış sürümlerle güncellemelidir.

**Container'ları güncellemek için:**

Son güncelleme tarihi 14.01.2020 veya daha yeni olan bir [ servercore
](https://hub.docker.com/_/microsoft-windows-servercore) veya [ nanoserver
](https://hub.docker.com/_/microsoft-windows-nanoserver) etiketi seçerek
Microsoft'un en yeni temel container görüntülerini kullanın ve
container'larınızı yeniden oluşturun.

**Düğümleri güncellemek için:**

Yama uygulanmış sürümlerin kullanıma sunulması üzerinde çalışılmaktadır ve
süreç 24 Ocak 2020'de tamamlanacaktır.

Bu tarihe kadar bekleyerek düğümlerinizi yama uygulanmış bir GKE sürümüne
yükseltebilir veya en yeni Windows yamasını istediğiniz bir zamanda manuel
olarak dağıtmak için Windows Update'i kullanabilirsiniz.

Çözümün yer alacağı yama sürümlerinin listesi aşağıda verilmiştir:

  * 1.14.7-gke.40 
  * 1.14.8-gke.33 
  * 1.14.9-gke.23 
  * 1.14.10-gke.17 
  * 1.15.7-gke.23 
  * 1.16.4-gke.22 

**Bu yama hangi güvenlik açıklarını ele alıyor?**

Yama, aşağıdaki güvenlik açıklarının riskini azaltır:

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601) \- Bu güvenlik açığı, [ Windows Crypto API
Adres Sahteciliği Güvenlik Açığı ](https://portal.msrc.microsoft.com/en-
US/security-guidance/advisory/CVE-2020-0601) olarak da bilinir ve kötü amaçlı
yürütülebilir dosyaların güvenli gibi gösterilmesini veya saldırganların
"ortadaki adam" saldırıları yürüterek etkilenen yazılıma giden TLS
bağlantılarındaki gizli bilgilerin şifresini çözmesini mümkün kılacak şekilde
kötüye kullanılabilir.

|

NVD Baz Puanı: 8.1 (Yüksek)

|

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601)  
  
  
##  14 Kasım 2019

**Yayınlanma tarihi:** 14.11.2019  
**Güncellenme tarihi:** 14.11.2019  Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
Kubernetes, kubernetes-csi [ ` external-provisioner `
](https://github.com/kubernetes-csi/external-provisioner) , [ ` external-
snapshotter ` ](https://github.com/kubernetes-csi/external-snapshotter) ve [ `
external-resizer ` ](https://github.com/kubernetes-csi/external-resizer)
yardımcı dosyalarında bir güvenlik sorunu açıkladı. Bu sorun, [ Container
Depolama Arayüzü (CSI) sürücülerinde ](https://kubernetes-
csi.github.io/docs/drivers.html) paketlenmiş çoğu yardımcı dosya sürümünü
etkilemektedir. Ayrıntılı bilgi için [ Kubernetes açıklamasına
](https://github.com/kubernetes/kubernetes/issues/85233) göz atın.

**Ne yapmalıyım?**  
**Bu güvenlik açığı yönetilen hiçbir GKE bileşenini etkilemez** . Kendi CSI
sürücülerinizi, GKE sürümü 1.12 veya üzerini çalıştıran [ GKE Alfa kümelerinde
](https://cloud.google.com/kubernetes-engine/docs/concepts/alpha-
clusters?hl=tr) yönetiyorsanız etkilenebilirsiniz. Sorun sizi etkilediyse CSI
sürücüsü tedarikçinizle iletişime geçerek yeni sürüme geçme talimatlarını
edinin.

**Bu yama hangi güvenlik açıklarını ele alıyor?**  
[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255) : Bu CVE, birim verilerine dair yetkisiz
erişim veya değişime izin verebilen ` kubernetes-csi ` [ ` external-
provisioner ` ](https://github.com/kubernetes-csi/external-provisioner) , [ `
external-snapshotter ` ](https://github.com/kubernetes-csi/external-
snapshotter) ve [ ` external-resizer ` ](https://github.com/kubernetes-
csi/external-resizer) yardımcı dosyalarında bulunur. [ CSI sürücülerinde
](https://kubernetes-csi.github.io/docs/drivers.html) paket haline getirilmiş
yardımcı dosyaların çoğu sürümünü etkiler.

|

Orta

|

[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255)  
  
  
##  12 Kasım 2019

**Yayınlanma tarihi:** 12.11.2019  
**Güncellenme tarihi:** 12.11.2019  Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
Intel, spekülatif yürütme ile mikromimari durumu arasındaki etkileşimlerin
verileri açığa çıkarmasına izin verebilecek CVE'ler açıkladı. Ayrıntılı bilgi
için [ Intel açıklamasına ](https://blogs.intel.com/technology/2019/11/ipas-
november-2019-intel-platform-update-ipu/) göz atın.

**Kubernetes Engine'i çalıştıran ana makine altyapısı, müşteri iş yüklerini
birbirinden ayırır. Kendinize ait çok kiracılı GKE kümelerinizde güvenilmeyen
kod çalıştırmadığınız _ve_ N2, M2 ya da C2 düğümlerini kullanmadığınız
takdirde başka bir işlem yapmanız gerekmez. ** N1 düğümlerindeki GKE örnekleri
için yeni işlem yapmanız gerekmez.

Anthos GKE On-Prem çalıştırıyorsanız bu durumdan etkilenmeniz donanıma
bağlıdır. Lütfen altyapınızı [ Intel açıklamasına
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) göre karşılaştırın.

####  Ne yapmalıyım?

**Yalnızca N2, M2 veya C2 düğümlerini kullanmanız _ve_ bu düğümlerin kendinize
ait çok kiracılı GKE kümelerinizde güvenilmeyen kod çalıştırması durumunda
etkilenirsiniz. **

**Düğümlerinizi yeniden başlattığınızda yama uygulanır.** Düğüm havuzunuzdaki
tüm düğümleri yeniden başlatmanın en kolay yolu, [ yeni sürüme geçme
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=tr#upgrade_nodes) işlemini kullanarak etkilenen düğüm havuzunun
tamamında zorunlu yeniden başlatma uygulamaktır.  

Not: Yeni sürüme geçme işlemi sırasında sürümleri değiştirmeniz gerekmez. `
cluster-version ` işaretine sahip düğüm sürümünde yükseltme işlemini
başlatabilirsiniz.

####  Bu yama hangi güvenlik açıklarına yönelik?

Yama, aşağıdaki güvenlik açıklarının riskini azaltır:

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)
: Bu CVE, TSX Eş Zamansız İptal (TAA) olarak da bilinir. TAA, [ Mikromimari
Veri Örnekleme (MDS) ](https://cloud.google.com/kubernetes-
engine/docs/security-bulletins?hl=tr#may-14-2019) ile mikromimari veri
yapılarının kötü amaçlı kullanılmasıyla başka bir veri hırsızlığı alanı
oluşturur.

[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)
Sanal ana makineleri etkileyen bu CVE, kötü amaçlı bir konuğun korumasız bir
ana makineyi çökertmesine neden olan bir Hizmet Reddi (DoS) güvenlik açığıdır.
Bu CVE, "Sayfa Boyutu Değişikliğinde Makine Kontrolü Hatası" olarak da
bilinir. Bu CVE GKE'yi etkilemez.

|

Orta

|

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)  
[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)  
  
##  22 Ekim 2019

**Yayınlanma tarihi:** 22.10.2019  
**Güncellenme tarihi:** 22.10.2019  Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
Yakın zamanda Go programlama dilinde, [ CVE-2019-16276
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-16276) 'da açıklanan
güvenlik açığı tespit edildi. Bu güvenlik açığı, Kimlik Doğrulama Proxy'si
kullanarak Kubernetes yapılandırmalarını etkileme potansiyeline sahip.
Ayrıntılı bilgi için [ Kubernetes açıklamasına
](https://groups.google.com/forum/?hl=tr#!topic/kubernetes-security-
announce/PtsUCqFi4h4) göz atın.

Kubernetes Engine, Kimlik Doğrulama Proxy'lerinin yapılandırmalarına izin
vermez ve bu nedenle bu güvenlik açığından etkilenmez.

|

Yok

|

[ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276)  
  
  
##  16 Ekim 2019

**Yayınlanma tarihi:** 16.10.2019  
**Güncellenme tarihi:** 24.10.2019  Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
**24.10.2019 Tarihli Güncelleme:** Yamalı sürümler artık tüm alt bölgelerde
kullanılabilir.

* * *

Yakın zamanda Kubernetes'te [ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) 'te açıklanan güvenlik açığı tespit
edilmiştir. Güvenlik açığı, POST isteği yapma yetkisi olan tüm kullanıcılara
Kubernetes API sunucusuna uzaktan Hizmet Reddi saldırısı yürütme izni verir.
Kubernetes Ürün Güvenliği Komitesi'nin (PSC), bu güvenlik açığıyla ilgili
yayınladığı ek bilgilere [ buradan
](https://groups.google.com/forum/?hl=tr#!topic/kubernetes-security-
announce/jk8polzSUxs) ulaşabilirsiniz.

[ Ana Yetkili Ağları ](https://cloud.google.com/kubernetes-engine/docs/how-
to/authorized-networks?hl=tr) ve [ Herkese açık uç noktası olmayan özel
kümeleri ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=tr#private_master) kullanan GKE Kümeleri, bu güvenlik açığının
zararlarını hafifletir.

######  Ne yapmalıyım?

Kümenizi, çözümü içeren bir yama sürümü yayınlanır yayınlanmaz bu sürüme
yükseltmenizi öneririz. Yamaların 14 Ekim haftası için planlanan GKE sürümüyle
birlikte tüm alt bölgelerde kullanıma sunulacağını tahmin ediyoruz.

Çözümün yer alacağı yama sürümlerinin listesi aşağıda verilmiştir:

  * 1.12.10-gke.15 
  * 1.13.11-gke.5 
  * 1.14.7-gke.10 
  * 1.15.4-gke.15 

######  Bu yama hangi güvenlik açıklarına yönelik?

Yama, aşağıdaki güvenlik açıklarının riskini azaltır:

CVE-2019-11253, Hizmet Reddi (DoS) güvenlik açığıdır.

|

Yüksek

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
  
##  16 Eylül 2019

**Yayınlanma tarihi:** 16.09.2019  
**Güncellenme tarihi:** 16.10.2019  Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
Bu bülten, ilk yayınının ardından güncellenmiştir.

Go programlama dili yakın zamanda, Hizmet Reddi (DoS) güvenlik açığı olan yeni
[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) ve [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) güvenlik
açıklarını tespit etti. GKE'de bu, kullanıcıların Kubernetes API sunucusunda
aşırı CPU miktarı tüketen kötü amaçlı istekler oluşturmasına izin vererek küme
kontrol düzleminin kullanılabilirliğini azaltabilir. Ayrıntılı bilgi için [ Go
programlama dili açıklamasına
](https://groups.google.com/forum/?hl=tr#!topic/golang-announce/65QixT3tcmg)
göz atın.

######  Ne yapmalıyım?

Kümenizi, bu güvenlik açığına yönelik çözümü içeren en son yama sürümü
yayınlanır yayınlanmaz bu sürüme yükseltmenizi öneririz. Bu yamaların, [ yayın
planı ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=tr#september_16_2019) doğrultusunda sonraki GKE sürümüyle birlikte
tüm alt bölgelerde kullanıma sunulacağını tahmin ediyoruz.

Çözümün yer alacağı yama sürümlerinin listesi aşağıda verilmiştir:

  * **16 Ekim 2019 Tarihli Güncelleme:** 1.12.10-gke.15 
  * 1.13.10-gke.0 
  * 1.14.6-gke.1 

######  Bu yama hangi güvenlik açığına yönelik?

Yama, aşağıdaki güvenlik açıklarının riskini azaltır:

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) ve [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) , Hizmet Reddi
(DoS) güvenlik açıklarıdır.

|

Yüksek

|

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512)  
[ CVE-2019-9514 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9514)  
  
  
##  5 Eylül 2019

**Yayınlanma tarihi:** 05.09.2019  
**Güncellenme tarihi:** 05.09.2019

31 Mayıs 2019  tarihli bültende güvenlik açığının çözümü için yayınlanan
bülten güncellenmiştir.

##  22 Ağustos 2019

**Yayınlanma tarihi:** 22.08.2019  
**Güncellenme tarihi:** 22.08.2019

5 Ağustos 2019  tarihli bülten güncellenmiştir. Önceki bültende açıklanan
güvenlik açığının çözümü [ kullanıma sunulmuştur
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=tr#august_22_2019) .

##  8 Ağustos 2019

**Yayınlanma tarihi:** 08.08.2019  
**Güncellenme tarihi:** 08.08.2019

5 Ağustos 2019  tarihli bülten güncellenmiştir. Bu bültende açıklanan güvenlik
açığının çözümünün GKE'nin sonraki sürümünde kullanıma sunulacağını tahmin
ediyoruz.

##  5 Ağustos 2019

**Yayınlanma tarihi:** 05.08.2019  
**Güncellenme tarihi:** 09.08.2019  Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
Bu bülten, ilk yayınının ardından güncellenmiştir.

Kubernetes yakın zamanda küme kapsamındaki [ özel kaynak
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) örneklerinin tüm Ad Alanlarında bulunan ad alanlı nesneler gibi
işleme alınmasına izin veren [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) güvenlik açığını tespit etti. Bu,
yalnızca ad alanı düzeyinde RBAC izinlerine sahip kullanıcı ve hizmet
hesaplarının küme kapsamındaki özel kaynaklarla etkileşim kurabileceği
anlamına gelir. Bu güvenlik açığının kötü amaçlı kullanılması için saldırganın
herhangi bir ad alanındaki kaynağa erişim izinlerine sahip olması gerekir.

######  Ne yapmalıyım?

Kümenizi, bu güvenlik açığına yönelik çözümü içeren en son yama sürümü
yayınlanır yayınlanmaz bu sürüme [ yükseltmenizi
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=tr) öneririz. Yamaların bir sonraki GKE sürümüyle birlikte tüm alt
bölgelerde kullanıma sunulacağını tahmin ediyoruz. Çözümün yer alacağı yama
sürümlerinin listesi aşağıda verilmiştir:

  * 1.11.10-gke.6 
  * 1.12.9-gke.13 
  * 1.13.7-gke.19 
  * 1.14.3-gke.10 ( [ Hızlı Kanal ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels?hl=tr) ) 

######  Bu yama hangi güvenlik açığına yönelik?

Yamada aşağıdaki güvenlik açığının çözümü yer alır: [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Orta

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)  
  
##  3 Temmuz 2019

**Yayınlanma tarihi:** 03.07.2019  
**Güncellenme tarihi:** 03.07.2019  Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
CVE-2019-11246 güvenlik açığına yönelik yayınlanan ` kubectl ` yamalı sürümü [
` gcloud ` 253.0.0 ](https://cloud.google.com/sdk/docs/release-
notes?hl=tr#kubernetes_engine) ile kullanıma sunulmuştur. Daha fazla bilgi
için  25 Haziran 2019 tarihli güvenlik bültenini  inceleyin.

**Not:** Yama, ` kubectl ` 1.11.10 sürümünde mevcut değildir.

|

Yüksek

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  3 Temmuz 2019

**Yayınlanma tarihi:** 25.06.2019  
**Güncellenme tarihi:** 03.07.2019  Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
######  3 Temmuz 2019 Tarihli Güncelleme

Son güncellememiz yayınlandığında, 1.11.9 ve 1.11.10 sürümlerinin yamaları
henüz kullanıma sunulmamıştı. Şimdi, 1.11.10-gke.5 sürümünü, her iki 1.11
sürümünün de yükseltme hedefi olarak yayınlıyoruz.

Bu kez, GKE ana düğümleri ile Kubernetes Engine'i çalıştıran Google
altyapısına yama uygulandı ve bu güvenlik açığına karşı korumaya alındı.

1.11 ana düğümleri yakın zamanda kullanımdan kaldırıldı ve 8 Temmuz 2019
haftasında otomatik olarak 1.12 sürümüne yükseltilecek şekilde planlandı.
Düğümleri yamalı bir sürüme almak için aşağıdaki önerilen adımlardan herhangi
birini seçebilirsiniz:

  * 8 Temmuz 2019 tarihine kadar düğümlerin 1.11.10-gke.5 sürümüne yükseltme işlemini gerçekleştirin. Bu tarihten sonra, 1.11 sürümleri kullanılabilir yükseltme hedefleri listesinden kaldırılmaya başlanacaktır. 
  * 1.11 sürümü düğümlerde [ otomatik yükseltmeleri ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades?hl=tr) etkinleştirerek ana düğümler 1.12 sürümüne yükseltildiğinde bu düğümlerin de yükseltilmesine izin verin. 
  * Hem ana düğümleri hem de düğümleri, sabit bir 1.12 sürümüne [ manuel olarak yükseltin ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=tr) . 

24 Haziran 2019 tarihli bültende şu bilgiler yer almaktadır:

* * *

######  24 Haziran 2019 Tarihli Güncelleme

22.06.2019 21:40 UTC itibarıyla aşağıdaki yama uygulanmış Kubernetes
sürümlerini kullanıma sunduk. Kubernetes sürümleri 1.11.0 ile 1.13.6 arasında
olan ana düğümler otomatik olarak yama uygulanmış sürüme yükseltilecektir.
Çalıştırdığınız sürüm bu yamayla uyumlu değilse düğümlerinizi yükseltmeden
önce uyumlu bir ana sürüme (listesi aşağıda verilmiştir) yükseltme işlemi
gerçekleştirin.

**Bu güvenlik açıklarının ciddiyeti nedeniyle, düğümler için otomatik
yükseltme özelliği etkinleştirilmiş olsun veya olmasın, yamalar kullanıma
sunulur sunulmaz hem düğümlerinizi hem de ana düğümlerinizi bu sürümlerden
birine[ manuel olarak yükseltmenizi ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-container-cluster?hl=tr) öneririz. **

Yama uygulanmış sürümler:

  * 1.11.8-gke.10 
  * 1.12.7-gke.24 
  * 1.12.8-gke.10 
  * 1.13.6-gke.13 

18 Haziran 2019 tarihli bültende şu bilgiler yer almaktadır:

* * *

Linux çekirdeklerindeki üç TCP güvenlik açığı yakın zamanda Netflix tarafından
açıklanmıştır:

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

Bu CVE'lerin tamamına [ NFLX-2019-001 ](https://github.com/Netflix/security-
bulletins/blob/master/advisories/third-party/2019-001.md) adı verilir.

Yama uygulanmamış Linux çekirdekleri, uzaktan tetiklenen bir hizmet reddi
saldırısı güvenlik açığından etkilenebilir. **Güvenilmeyen ağ trafiği gönderen
veya alan Google Kubernetes Engine düğümleri etkilenmektedir. Bu yüzden, iş
yüklerinizi korumak için aşağıdaki çözüm adımlarını uygulamanızı öneririz.**

######  Kubernetes ana düğümleri

  * Güvenilen ağların trafiğini sınırlamak için [ Yetkili Ağlar ](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks?hl=tr) kullanan Kubernetes ana düğümleri etkilenmez. 

  * Google'ın yönettiği GKE kümelerinin ana düğümlerine, önümüzdeki günlerde otomatik olarak yama uygulanacaktır. Müşterilerin hiçbir işlem yapması gerekmez. 

######  Kubernetes düğümleri

Güvenilir ağların trafiğini sınırlayan düğümler etkilenmez. Bu küme aşağıdaki
özelliklere sahiptir:

  * Güvenilmeyen ağlardan güvenlik duvarıyla ayrı tutulan ya da herkese açık IP'si olmayan düğümler ( [ Özel kümeler ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters?hl=tr) ) 
  * Herkese açık LoadBalancer Hizmetleri olmayan kümeler 

Google, bu güvenlik açıklarına yönelik kalıcı bir çözüm hazırlamaktadır.
Çözüm, yeni bir düğüm sürümü olarak sunulacaktır. Kalıcı çözüm kullanıma
sunulduğunda bu bülteni güncelleyip tüm GKE müşterilerini e-posta ile
bilgilendireceğiz.

Kalıcı çözüm kullanıma sunulana kadar faydalanmanız için ana makine ` iptables
` yapılandırmasını değiştirerek çözüm uygulayan bir Kubernetes DaemonSet
oluşturduk.

#####  Ne yapmalıyım?

Aşağıdaki komutu çalıştırarak Kubernetes DaemonSet'i kümenizdeki tüm düğümlere
uygulayın. Bu işlem, güvenlik açığını gidermek için mevcut ` iptables `
kurallarına bir ` iptables ` kuralı ekler. **Komutu, Google Cloud projesi
bazında küme başına bir kez çalıştırın.**

    
    
    
    kubectl apply -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

GKE'de Ipv6 desteklenmediği için ip6tables kuralı gerekli değildir.

Yama uygulanmış düğüm sürümü kullanıma sunulduktan ve etkilenmiş olabilecek
tüm düğümlerinizi yükselttikten sonra aşağıdaki komutu kullanarak DaemonSet'i
kaldırabilirsiniz. **Komutu, Google Cloud projesi bazında küme başına bir kez
çalıştırın.**

    
    
    
    kubectl delete -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

|  Yüksek  
Orta  
Orta  
|  [ CVE-2019-11477 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11477)  
[ CVE-2019-11478 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11478)  
[ CVE-2019-11479 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11479)  
  
  
##  25 Haziran 2019

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
**03.07.2019 Tarihli Güncelleme:** Bu yama, ` gcloud ` 253.0.0 sürümü ile
1.12.9, 1.13.6, 1.14.2 ve daha yeni ` kubectl ` sürümleri için kullanılabilir.

**Not:** Yama, 1.11.10 sürümünde mevcut değildir.

* * *

Kubernetes, yakın zamanda [ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) güvenlik açığını tespit etti. Bu güvenlik
açığı, saldırganların ana makinedeki dosyaları değiştirmeleri için container
içinde ` kubectl cp ` çalışma ve kod yürütme özelliklerine erişmelerini
sağlar. Bu açıklardan yararlanma, saldırganlara ana makinenin dosya sisteminde
dosya oluşturma veya değiştirme izni sağlayabilir. Ayrıntılı bilgi için [
Kubernetes açıklamasına
](https://groups.google.com/forum/?hl=tr#!topic/kubernetes-security-
announce/NLs2TGbfPdo) göz atın.

**Tüm Google Kubernetes Engine (GKE)` gcloud ` sürümleri bu güvenlik açığından
etkilenmektedir. Bu nedenle, ` gcloud ` son yama sürümü kullanıma sunulduğunda
bu sürüme yükseltme yapmanızı öneririz. ** Daha sonra kullanıma sunulacak bir
yama sürümünde bu güvenlik açığı için bir çözüm sunulacaktır.

######  Ne yapmalıyım?

Daha sonra yayınlanacak ` gcloud ` sürümünde ` kubectl ` için yama uygulanmış
bir sürüm yer alacaktır. Dilerseniz [ ` kubectl ` için doğrudan kendiniz
yükseltme yapabilirsiniz ](https://kubernetes.io/docs/tasks/tools/install-
kubectl/) .

Bu yamanın kullanıma sunulma durumunu [ ` gcloud ` sürüm notlarından
](https://cloud.google.com/sdk/docs/release-notes?hl=tr) takip edebilirsiniz.

######  Bu yama hangi güvenlik açığına yönelik?

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) güvenlik açığı, container içinde `
kubectl cp ` çalışma ve kod yürütme özelliklerine erişimi olan bir saldırganın
ana makinedeki dosyaları değiştirebilmesini sağlar. Bu açıklardan yararlanma,
saldırganların ana makinenin dosya sisteminde dosya oluşturmasını veya
değiştirmesini sağlayabilir

|

Yüksek

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  18 Haziran 2019

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
Docker, kısa bir süre önce [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) güvenlik açığını tespit etti. Güvenlik
açığı, container içinde kod yürütebilen saldırganların dışarıdan başlatılan `
docker cp ` işlemini ele geçirmesine izin verebilir. Bu açıklardan yararlanma,
saldırganlara dosyaların yazıldığı konumu ana makine dosya sisteminde rastgele
bir konumla değiştirme olanağı sağlayabilir.

**Docker çalıştıran tüm Google Kubernetes Engine (GKE) düğümleri bu güvenlik
açığından etkilenmektedir. Bu nedenle, son yama sürümü kullanıma sunulduğunda
bu sürüme yükseltme yapmanızı öneririz. Daha sonra kullanıma sunulacak bir
yama sürümünde bu güvenlik açığı için bir çözüm sunulacaktır.**

**1.12.7 sürümünden eski olan tüm Google Kubernetes Engine (GKE) ana düğümleri
Docker çalıştırdığı için bu güvenlik açığından etkilenmektedir.** GKE'de ana
düğüm üzerinde kullanıcıların ` docker cp ` erişimi yoktur ve bu güvenlik
açığının oluşturduğu risk GKE ana düğümleriyle sınırlıdır.

#####  Ne yapmalıyım?

Yalnızca Docker çalıştıran düğümler etkilenmektedir ve bu durum yalnızca ele
geçirilebilen bir ` docker cp ` (veya API eşdeğeri) komutu verildiğinde
gerçekleşmektedir. Bu durumun, Kubernetes ortamlarında oldukça sıra dışı
olması beklenir. [ Containerd ile COS ](https://cloud.google.com/kubernetes-
engine/docs/concepts/using-containerd?hl=tr) çalıştıran düğümler etkilenmez.

Düğümlerinizi yükseltmek için önce [ ana düğümünüzün yama uygulanmış sürüme
yükseltilmesi ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=tr#upgrading_the_cluster) gerekir. Yama kullanıma
sunulduğunda, ana düğüm yükseltme işlemi başlatabilir veya Google'ın ana
düğümü otomatik olarak yükseltmesini bekleyebilirsiniz. Yama, daha sonra
duyurulacak olan bir GKE yamasına dahil edilen Docker 18.09.7 sürümde
kullanıma sunulacaktır. **Bu yama, yalnızca 1.13 ve üzeri GKE sürümleri için
kullanıma sunulacaktır.**

Küme ana sistemlerini düzenli yükseltme sıklığında otomatik olarak yama
uygulanmış sürüme yükselteceğiz. Dilerseniz yama uygulanmış sürüm kullanıma
sunulduktan sonra kendiniz de ana düğüm yükseltme işlemi başlatabilirsiniz.

Yama kullanıma sunulduğunda bu bülten yamayı içeren sürümlerle
güncellenecektir. Bu yamaların kullanıma sunulma durumunu [ sürüm notlarından
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=tr) takip
edebilirsiniz.

#####  Bu yama hangi güvenlik açığına yönelik?

Yama, aşağıdaki güvenlik açığı riskini azaltır:

[ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) güvenlik açığı, container içinde kod
yürütebilen saldırganların dışarıdan başlatılan ` docker cp ` işlemini ele
geçirmesine izin verir. Bu açıklardan yararlanma, saldırganlara dosyaların
yazıldığı konumu ana makine dosya sisteminde rastgele bir konumla değiştirme
olanağı sağlayabilir.

|  Yüksek  |  
  
##  31 Mayıs 2019

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
Bu bülten, ilk yayınının ardından güncellenmiştir.

######  2 Ağustos 2019 Tarihli Güncelleme

Bülten ilk yayınlandığında yalnızca 1.13.6-gke.0 ile 1.13.6-gke.5 arası
sürümler etkilenmişti. Regresyon nedeniyle şu anda tüm 1.13.6.x sürümleri
etkilenmektedir. 1.13.6 sürümünü çalıştırıyorsanız en kısa zamanda 1.13.7
sürümüne yükseltme yapın.

Kubernetes projesi, kubelet v1.13.6 ve v1.14.2'de [ CVE-2019-11245
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11245) güvenlik açığını
açıkladı. Güvenlik açığı, container görüntüsünde farklı bir kullanıcı
belirtilmiş olsa bile container'ların UID 0 (genellikle ` root `
kullanıcısıyla eşleştirilir) olarak çalışmasına yol açmaktadır.
**Container'larınız kök olmayan kullanıcı olarak çalışıyorsa ve 1.13.6-gke.0
ile 1.13.6-gke.6 arası düğüm sürümü çalıştırıyorsanız container'ları UID 0
olarak çalışmaması gereken kümelerdeki tüm Kapsüllerde` RunAsUser ` komutunu
ayarlamanızı öneririz. **

Kök olmayan bir ` USER ` değeri belirtilirse (örneğin, bir Dockerfile'da `
USER ` değerini ayarlayarak) beklenmedik davranışlar ortaya çıkar.
Container'lar bir düğümde ilk kez çalıştırıldığında belirtilen UID'ye uyar.
Ancak bu kusur nedeniyle ikinci çalıştırmada (ve sonraki çalıştırmalarda)
container, belirtilen UID'den bağımsız olarak UID 0 olarak çalışır. Bu durum
genellikle istenmeyen bir ayrıcalık artışıdır ve beklenmedik uygulama
davranışına yol açabilir.

#####  Çalıştırdığım sürümün etkilenmiş olup olmadığını nasıl anlarım?

Aşağıdaki komutu çalıştırarak tüm düğümleri ve kubelet sürümlerini listeleyin:

    
    
    
    kubectl get nodes -o=jsonpath='{range .items[*]}'\
    '{.status.nodeInfo.machineID}'\
    '{"\t"}{.status.nodeInfo.kubeletVersion}{"\n"}{end}'

Çıkış, aşağıdaki kubelet sürümlerini listelerse düğümleriniz etkilenmiş
demektir:

  * v1.13.6 
  * v1.14.2 

#####  Belirli bir yapılandırmamın etkilenmiş olup olmadığını nasıl anlarım?

Container'larınız kök olmayan kullanıcı olarak çalışıyorsa ve 1.13.6-gke.0 ile
1.13.6-gke.6 arası düğüm sürümü çalıştırıyorsanız aşağıdaki durumlar hariç
olmak üzere, düğümleriniz etkilenmiştir:

  * ` runAsUser ` PodSecurityContext için geçerli bir kök olmayan değer belirten kapsüller etkilenmez ve normal şekilde çalışmaya devam eder. 
  * Bir ` runAsUser ` ayarını zorunlu kılan PodSecurityPolicy'ler de etkilenmez ve normal şekilde çalışmaya devam eder. 
  * ` mustRunAsNonRoot:true ` belirten kapsüller UID 0 olarak başlatılmaz ancak bu sorundan etkilendiklerinde başlatılamazlar. 

#####  Ne yapmalıyım?

Kümedeki UID 0 olarak çalışmaması gereken tüm kapsüllerde [ RunAsUser Güvenlik
Bağlamı ](https://kubernetes.io/docs/tasks/configure-pod-container/security-
context/#set-the-security-context-for-a-pod) 'nı ayarlayın. Bu yapılandırmayı
[ PodSecurityPolicy ](https://kubernetes.io/docs/concepts/policy/pod-security-
policy/) kullanarak uygulayabilirsiniz.

|  Orta  |  [ CVE-2019-11245 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2019-11245)  
  
##  14 Mayıs 2019

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
**11.06.2019 Tarihli Güncelleme:** Yama, 28.05.2019 haftası yayınlanan
1.11.10-gke.4, 1.12.8-gke.6 ve 1.13.6-gke.5 sürümlerinde mevcuttur.

Aşağıdaki CVE'ler Intel tarafından açıklanmıştır:

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

Bu CVE'lerin tamamına Mikromimari Veri Örnekleme (MDS) adı verilir. Bu
güvenlik açıkları, mikromimari durumu ile kurgusal yürütme etkileşimi
üzerinden verilerin savunmasız hale gelmesine neden olabilir. Ayrıntılı bilgi
için [ Intel açıklamasına ](https://www.intel.com/content/www/us/en/security-
center/advisory/intel-sa-00233.html) göz atın.

**Kubernetes Engine'i çalıştıran ana makine altyapısı, müşteri iş yüklerini
birbirinden ayırır. Kendinize ait çok kiracılı GKE kümelerinizde güvenilmeyen
kod çalıştırmıyorsanız sorundan etkilenmezsiniz.**

**Kubernetes Engine içinde kendilerine ait çok kiracılı hizmetlerde
güvenilmeyen kod çalıştıran müşteriler için bu durum, özellikle ciddi bir
güvenlik açığıdır.** Sorunu Kubernetes Engine'de düzeltmek için düğümlerinizde
Hyper-Threading'i devre dışı bırakın. Yalnızca birden çok CPU kullanan Google
Kubernetes Engine (GKE) düğümleri bu güvenlik açıklarından etkilenir.
n1-standard-1 (GKE varsayılanı), g1-small ve f1-micro sanal makinelerinin
konuk ortama yalnızca 1 vCPU sunması nedeniyle Hyper-Threading'in devre dışı
bırakılmasına gerek yoktur.

Daha sonra duyurulacak bir [ yama sürümüne
](https://cloud.google.com/kubernetes-engine/release-notes?hl=tr) boşaltma
işlevini etkinleştirecek ek korumalar dahil edilecektir. Önümüzdeki
haftalarda, düzenli yükseltme sıklığında otomatik yükseltme özellikli ana
düğümleri ve düğümleri yama uygulanmış sürüme otomatik olarak yükselteceğiz.
**Bu güvenlik açığından etkilenme riskini ortadan kaldırmak için tek başına
yama yeterli değildir. Önerilen işlemler için aşağıya bakın.**

GKE On-Prem çalıştırıyorsanız kullandığınız donanıma bağlı olarak sorundan
etkilenmiş olabilirsiniz. Lütfen [ Intel açıklamasına
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) göz atın.

####  Ne yapmalıyım?

**Kendinize ait çok kiracılı GKE kümelerinizde güvenilmeyen kod
çalıştırmıyorsanız sorundan etkilenmezsiniz.**

**Kubernetes Engine'deki düğümler için Hyper-Threading devre dışı olacak
şekilde yeni düğüm havuzları oluşturun ve iş yüklerinizi yeni düğümler için
yeniden planlayın.**

n1-standard-1, g1-small ve f1-micro sanal makinelerinin konuk ortama yalnızca
1 vCPU sunması nedeniyle Hyper-Threading'in devre dışı bırakılmasına gerek
yoktur.

**Uyarı:**

  * Hyper-Threading devre dışı bırakıldığında, kümeleriniz ve uygulamanız performans açısından ciddi şekilde etkilenebilir. Bunu üretim kümelerinize dağıtmadan önce işlemin kabul edilebilir olduğundan emin olun. 
  * Hyper-Threading, bir DaemonSet dağıtılarak GKE düğüm havuzu düzeyinde devre dışı bırakılabilir. Ancak bu DaemonSet'in dağıtılması düğüm havuzundaki tüm düğümlerinizin aynı anda yeniden başlatılmasına neden olur. Bu nedenle, kümenizde yeni bir düğüm havuzu oluşturmanız, DaemonSet'i dağıtarak ilgili düğüm havuzunda Hyper-Threading'i devre dışı bırakmanız ve daha sonra iş yüklerinizi yeni düğüm havuzuna taşımanız önerilir. 

Hyper-Threading devre dışıyken yeni düğüm havuzu oluşturmak için:

  1. Kümenizde ` cloud.google.com/gke-smt-disabled=true ` düğüm etiketine sahip yeni bir düğüm havuzu oluşturun: 
    
        
    gcloud container node-pools create smt-disabled --cluster=[CLUSTER_NAME] \
        --node-labels=cloud.google.com/gke-smt-disabled=true

  2. DaemonSet'i bu yeni düğüm havuzuna dağıtın. DaemonSet yalnızca ` cloud.google.com/gke-smt-disabled=true ` etiketine sahip düğümlerde çalışır. Hyper-Threading'i devre dışı bırakır ve düğümü yeniden başlatır. 
    
        
    kubectl create -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform/\
    k8s-node-tools/master/disable-smt/gke/disable-smt.yaml

  3. DaemonSet kapsüllerinin çalışır durumda olduğundan emin olun. 
    
        
    kubectl get pods --selector=name=disable-smt -n kube-system

Şuna benzer bir yanıt alırsınız:

    
        
    NAME                READY     STATUS    RESTARTS   AGE
    
    disable-smt-2xnnc   1/1       Running   0          6m

  4. Kapsüllerin günlüklerinde "SMT devre dışı bırakıldı" ifadesinin yer aldığından emin olun. 
    
        
    kubectl logs disable-smt-2xnnc disable-smt -n kube-system

Not: Düğümde [Güvenli Başlatma](/kubernetes-engine/docs/how-to/shielded-gke-
nodes#secure_boot) özelliği etkinleştirilmişse başlatma seçenekleri
değiştirilemez. Güvenli Başlatma etkinleştirilmişse DaemonSet'in
oluşturulabilmesi için bu özelliğin [devre dışı bırakılması](/kubernetes-
engine/docs/how-to/shielded-gke-nodes#disabling) gerekir.

Düğüm havuzlarında DaemonSet'i çalışır durumda tutmanız gerekir. Bu sayede,
havuzda oluşturulan yeni düğümlere değişiklikler otomatik olarak uygulanır.
Düğüm oluşturma işlemleri, otomatik düğüm onarımı, manuel veya otomatik
yükseltme ve otomatik ölçeklendirme nedeniyle tetiklenebilir.

Hyper-Threading'i yeniden etkinleştirmek için verilen DaemonSet'i dağıtmadan
düğüm havuzunu yeniden oluşturmanız ve iş yüklerinizi yeni düğüm havuzuna
taşımanız gerekir.

Yama kullanıma sunulduğunda düğümlerinizi manuel olarak yükseltmenizi de
öneririz. Yükseltme için öncelikle [ ana düğümünüzü en yeni sürüme
yükseltmeniz ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=tr#upgrading_the_cluster) gerekir. GKE ana
düğümleri, düzenli yükseltme sıklığında otomatik olarak yükseltilir.

Yama kullanıma sunulduğunda bu bülten yamayı içeren sürümlerle
güncellenecektir.

####  Bu yama hangi güvenlik açığına yönelik?

Yama, aşağıdaki güvenlik açıklarının riskini azaltır:

[ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
, [ CVE-2018-12127 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2018-12127) , [ CVE-2018-12130
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130) , [
CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091) :
Bu güvenlik açıkları, kurgusal yürütmeden kötü amaçla yararlanır. Bu CVE'lerin
tamamına Mikromimari Veri Örnekleme adı verilir. Bu güvenlik açıkları,
mikromimari durumu ile kurgusal yürütme etkileşimi üzerinden verilerin
savunmasız hale gelmesine neden olabilir.  |  Orta  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  5 Nisan 2019

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
Kısa bir süre önce [ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) ve [ CVE-2019-9901
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) güvenlik
açıkları [ Envoy ](https://www.envoyproxy.io/) 'da tespit edildi.

Envoy, [ Istio ](https://istio.io/) 'da gömülü olarak bulunur ve bu güvenlik
açıkları, bazı durumlarda Istio politikasının aşılmasına yol açar.

Google Kubernetes Engine (GKE) üzerinde Istio'yu etkinleştirdiyseniz bu
güvenlik açıklarından etkilenebilirsiniz. **Etkilenen kümelerinizi en kısa
sürede en son yama sürümüne yükseltmenizi ve Istio yardımcı dosyalarınızı
yükseltmenizi (talimatları aşağıda verilmiştir) öneririz.**

####  Ne yapmalıyım?

**Bu güvenlik açıklarının ciddiyeti nedeniyle, düğümler için otomatik
yükseltme özelliği etkinleştirilmiş olsun veya olmasın, aşağıdaki adımlar
önerilir:**

  1. **Yama kullanıma sunulur sunulmaz kümenizi[ manuel olarak yükseltin ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=tr) . **
  2. **[ Yardımcı dosya yükseltme belgelerine ](https://istio.io/docs/setup/kubernetes/upgrade/steps/#sidecar-upgrade) uygun şekilde yardımcı dosyalarınızı yükseltin. **

Yama uygulanmış sürümler bugün saat 19:00'dan (PDT) önce tüm GKE projeleri
için kullanıma sunulacaktır.

Bu yama aşağıdaki GKE sürümlerinde kullanıma sunulacaktır. Yama uygulanmış
sürüm GKE güvenlik bültenleri sayfasında duyurulduğunda (15 Nisan 2019'da
beklenmektedir) yeni kümeler varsayılan olarak yama uygulanmış sürümü
kullanacaktır. Bu tarihten önce küme oluşturursanız kullanacağı yama
uygulanmış sürümü belirtmeniz gerekir. [ Otomatik düğüm yükseltme
](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-
upgrades?hl=tr) özelliğini etkinleştirmiş olan ve manuel olarak yükseltme
işlemi yapmayan GKE müşterilerinin düğümleri, önümüzdeki hafta yama uygulanmış
sürüme otomatik olarak yükseltilecektir.

Yama Uygulanmış Sürümler:

  * 1.10.12-gke.14 
  * 1.11.6-gke.16 
  * 1.11.7-gke.18 
  * 1.11.8-gke.6 
  * 1.12.6-gke.10 
  * 1.13.4-gke.10 

####  Bu yama hangi güvenlik açığına yönelik?

Yama, aşağıdaki güvenlik açıklarının riskini azaltır:

[ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) ve [ CVE-2019-9901.
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) [ Istio
blogunda ](https://istio.io/blog/2019/announcing-1.1.2) bunlarla ilgili daha
fazla bilgi edinebilirsiniz.

|  Yüksek  |

  * [ CVE-2019-9900 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900)
  * [ CVE-2019-9901. ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)

  
  
##  1 Mart 2019

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
**22.03.2019 Tarihli Güncelleme:** Bu yama Kubernetes 1.11.8-gke.4,
1.13.4-gke.1 ve daha yeni sürümlerde mevcuttur. Yama henüz 1.12 sürümünde
kullanıma sunulmamıştır. Bu yamaların kullanıma sunulma durumunu [ sürüm
notlarından ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=tr#march_19_2019) takip edebilirsiniz.

Kubernetes, kısa bir süre önce, [ CVE-2019-1002100
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-1002100) kodlu yeni
hizmet reddi güvenlik açığını tespit etti. Bu güvenlik açığı, yama isteği
yapma yetkisi olan kullanıcının Kubernetes API sunucusunda aşırı miktarda CPU
ve bellek kullanılmasına yol açan "json-patch" isteği oluşturmasına izin
verir. Bu durumda, küme kontrol düzleminin kullanılabilirliğini azaltabilir.
Ayrıntılı bilgi için [ Kubernetes açıklamasına
](https://groups.google.com/forum/?hl=tr#!topic/kubernetes-
announce/vmUUNkYfG9g) göz atın. **Bu güvenlik açıklarından tüm Google
Kubernetes Engine (GKE) ana düğümleri etkilenir. Daha sonra kullanıma
sunulacak bir yama sürümünde bu güvenlik açığı için bir çözüm sunulacaktır.
Küme ana sistemleri, önümüzdeki haftalarda, düzenli yükseltme sıklığında yama
uygulanmış sürüme otomatik olarak yükseltilecektir.**

####  Ne yapmalıyım?

**Bu konuyla ilgili herhangi bir işlem yapmanıza gerek yoktur. GKE ana
düğümleri, düzenli yükseltme sıklığında otomatik olarak yükseltilecektir.**
Ana düğümünüzü daha erken yükseltmek isterseniz [ ana düğümü yükseltme
işlemini manuel olarak başlatın ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=tr#upgrading_the_cluster) .

Bu bülten, yama içeren sürümlerle güncellenecektir. Yamanın yalnızca 1.11
üzeri sürümlerde kullanıma sunulacağını, 1.10 sürümlerinde sunulmayacağını
unutmayın.

####  Bu yama hangi güvenlik açığına yönelik?

Yama, aşağıdaki güvenlik açığı riskini azaltır:

Güvenlik açığı [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) , kullanıcının Kubernetes API
sunucusunda aşırı miktarda CPU kullanılmasına yol açan "json-patch" isteği
oluşturmasına izin verir. Bu durumda, küme kontrol düzleminin
kullanılabilirliğini azalabilir.

|  Orta  |  [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100)  
  
##  11 Şubat 2019 (runc)

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
Open Containers Initiative (OCI), runc içindeki [ CVE-2019-5736
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5736) kodlu yeni
güvenlik açığını [ kısa bir süre önce tespit etti
](https://groups.google.com/a/opencontainers.org/forum/m/?hl=tr#!topic/dev/Tc1ELm-8oDI)
. Bu güvenlik açığı, container'ın kod dışına alınmasıyla ana makine düğümünde
kök ayrıcalıkları edinmesine izin verir.

**Bu güvenlik açığından Google Kubernetes Engine (GKE) Ubuntu düğümleriniz
etkilenir. Bu nedenle, aşağıda açıklandığı gibi en kısa zamanda düğümlerinizi
en son yama sürümüne[ yükseltmenizi ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=tr) öneririz. **

####  Ne yapmalıyım?

Düğümlerinizi yükseltmek için öncelikle ana düğümünüzü en yeni sürüme
yükseltmeniz gerekir. Bu yama Kubernetes 1.10.12-gke.7, 1.11.6-gke.11,
1.11.7-gke.4, 1.12.5-gke.5 ve daha yeni sürümlerde kullanılabilir. Bu
yamaların kullanıma sunulma durumunu [ ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=tr#february-11-2019) sürüm notlarından takip
edebilirsiniz.

Yalnızca GKE'deki Ubuntu düğümlerinin etkilendiğini unutmayın. COS çalıştıran
düğümler etkilenmez.

Yeni runc sürümünün bellek kullanımını artırdığını ve düşük bellek sınırları
(< 16 MB) belirlediyseniz ayrılan belleğin güncellenmesi gerekebileceğini
unutmayın.

####  Bu yama hangi güvenlik açığına yönelik?

Yama, aşağıdaki güvenlik açığı riskini azaltır:

[ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) , runc içindeki bir güvenlik açığını
tanımlar. Bu güvenlik açığı, kötü amaçlı bir container'ın ana makine runc
ikili programının üzerine yazmasına ve böylece ana makine düğümünde kök
düzeyinde kod yürütme yetkisi elde etmesine olanak verir. Kök olarak
çalışmayan container'lar etkilenmez. Bu güvenlik açığı, "Yüksek" önem düzeyli
güvenlik açığı olarak derecelendirilmiştir.

|  Yüksek  |  [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736)  
  
##  11 Şubat 2019 (Go)

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
**25.02.2019 Tarihli Güncelleme:** Daha önce bildirildiği gibi 1.11.7-gke.4
için yama mevcut değildir. 1.11.7 sürümünü çalıştırıyorsanız şunları
yapabilirsiniz: eski 1.11.6 sürümüne geçebilirsiniz, 1.12 yeni sürümüne
geçebilirsiniz veya 04.03.2019 haftasında kullanıma sunulacak 1.11.7 yama
sürümünü bekleyebilirsiniz.

Go programlama dili yeni bir güvenlik açığı olan [ CVE-2019-6486
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-6486) 'yı tespit
etti. Bu, P-521 ve P-384 elips biçimli eğrilerinin şifreleme/elips biçimli
uygulamalarını hedef alan bir Hizmet Reddi (DoS) güvenlik açığıdır. Bu
güvenlik açığı, Google Kubernetes Engine (GKE) üzerinde kullanıcının
Kubernetes API sunucusunda aşırı miktarda CPU ve bellek kullanılmasına yol
açan "json-patch" isteği oluşturmasına izin verir. Bu durumda, küme kontrol
düzleminin kullanılabilirliğini azaltabilir. Ayrıntılı bilgi için [ Go
programlama dili açıklamasına
](https://groups.google.com/forum/?hl=tr#!topic/golang-announce/mVeX35iXuSw)
göz atın.

**Bu güvenlik açıklarından tüm Google Kubernetes Engine (GKE) ana düğümleri
etkilenir.[ En son yama sürümünde ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=tr#february-11-2019) bu güvenlik açığına yönelik
bir çözüm bulunur. Küme ana sistemleri, önümüzdeki haftalarda, düzenli
yükseltme sıklığında yama uygulanmış sürüme otomatik olarak yükseltilecektir.
**

####  Ne yapmalıyım?

**Bu konuyla ilgili herhangi bir işlem yapmanıza gerek yoktur. GKE ana
düğümleri, düzenli yükseltme sıklığında otomatik olarak yükseltilecektir.**
Ana düğümünüzü daha erken yükseltmek isterseniz [ ana düğümü yükseltme
işlemini manuel olarak başlatın ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=tr#upgrading_the_cluster) .

Bu yama GKE 1.10.12-gke.7, 1.11.6-gke.11, 1.11.7-gke.4, 1.12.5-gke.5 ve daha
yeni sürümlerde kullanılabilir.

####  Bu yama hangi güvenlik açığına yönelik?

Yama, aşağıdaki güvenlik açığı riskini azaltır:

CVE-2019-6486, P-521 ve P-384 elips biçimli eğrilerinin şifreleme/elips
biçimli uygulamalarını hedef alan bir güvenlik açığıdır. Kullanıcının, aşırı
miktarda CPU kullanımına yol açan girişler oluşturmasına olanak verir.

|  Yüksek  |  [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486)  
  
##  3 Aralık 2018

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
Kubernetes kısa süre önce, çok düşük ayrıcalıklara sahip bir kullanıcının
kubelet API'leri yetkilendirmesini atlayarak kümedeki herhangi bir düğümde yer
alan herhangi bir Kapsülde rastgele işlemler yapmasına imkan tanıyan yeni
güvenlik açığı [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105) 'i keşfetti. Ayrıntılı bilgi için [
Kubernetes açıklamasına
](https://groups.google.com/forum/?hl=tr#!topic/kubernetes-
announce/GVllWCg6L88) göz atın. **Tüm Google Kubernetes Engine (GKE) ana
düğümleri bu güvenlik açıklarından etkilendi ve kümeleri[ en yeni yama
sürümlerine ](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=tr#november-12-2018) yükselttik. Bu konuyla ilgili herhangi bir işlem
yapmanıza gerek yoktur. **

####  Ne yapmalıyım?

**Bu konuyla ilgili herhangi bir işlem yapmanıza gerek yoktur. GKE ana
düğümleri daha önce yükseltilmiştir.**

Bu yama GKE 1.9.7-gke.11, 1.10.6-gke.11, 1.10.7-gke.11, 1.10.9-gke.5 ve
1.11.2-gke.18 ve daha yeni sürümler için kullanılabilir.

####  Bu yama hangi güvenlik açığına yönelik?

Yama, aşağıdaki güvenlik açığı riskini azaltır:

CVE-2018-1002105 güvenlik açığı, nispeten düşük düzeyde ayrıcalıklara sahip
kullanıcının, kubelet API'lerine erişim yetkilendirmesini atlamasına imkan
verir. Bu durumda, kullanıcının, derecesini yükselterek kubelet API'sine
rastgele çağrılar yapması için yükseltilebilir istekler yapmaya yetkili hale
gelmesini sağlar. Bu güvenlik açığı Kubernetes'te Kritik önem düzeyli güvenlik
açığı olarak derecelendirilmiştir. GKE uygulamasında kimliği doğrulanamayan
ayrıcalık artırmayı önleyen bazı ayrıntılar ışığında, Yüksek güvenlik açığı
olarak derecelendirilmiştir.

|  Yüksek  |  [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105)  
  
##  13 Kasım 2018

Açıklama  
---  
  
**16/11/2018 Tarihli Güncelleme:** Potansiyel olarak etkilenen jetonların
iptali ve dönüşümü tamamlanmıştır. Başka bir işlem yapılmasına gerek yoktur.

Google kısa süre önce Calico Container Network Interface (CNI) eklentisinde,
belirli yapılandırmalarda hassas bilgilerin günlüğe kaydedilmesine neden olan
bir sorun keşfetmiştir. Bu sorun, Tigera Technical Advisory [ TTA-2018-001
](https://www.projectcalico.org/security-bulletins/) altında izlenmektedir.

  * Calico CNI eklentisi, hata ayıklama düzeyinde günlük kaydıyla çalışırken günlük kayıtlarına Kubernetes API istemci yapılandırmasını yazar. 
  * Calico CNI ayrıca CNI ağ yapılandırmasında "k8s_auth_token" alanı ayarlanmışsa bilgi düzeyinde günlük kayıtlarına Kubernetes API jetonunu yazar. 
  * Ek olarak, hata ayıklama düzeyinde günlük kaydıyla çalışırken, hizmet hesabı jetonu Calico tarafından okunan Calico yapılandırma dosyasında veya Calico tarafından kullanılan ortam değişkenleri olarak açık şekilde belirtilmişse Calico bileşenleri (calico/node, felix, CNI) günlük dosyalarına bu bilgiyi yazar. 

Bu jetonlar aşağıdaki izinlere sahiptir:  
      
    
    
    bgpconfigurations.crd.projectcalico.org     [create get list update watch]
    bgppeers.crd.projectcalico.org              [create get list update watch]
    clusterinformations.crd.projectcalico.org   [create get list update watch]
    felixconfigurations.crd.projectcalico.org   [create get list update watch]
    globalbgpconfigs.crd.projectcalico.org      [create get list update watch]
    globalfelixconfigs.crd.projectcalico.org    [create get list update watch]
    globalnetworkpolicies.crd.projectcalico.org [create get list update watch]
    globalnetworksets.crd.projectcalico.org     [create get list update watch]
    hostendpoints.crd.projectcalico.org         [create get list update watch]
    ippools.crd.projectcalico.org               [create get list update watch]
    networkpolicies.crd.projectcalico.org       [create get list update watch]
    nodes                                       [get list update watch]
    pods                                        [get list watch patch]
    namespaces                                  [get list watch]
    networkpolicies.extensions                  [get list watch]
    endpoints                                   [get]
    services                                    [get]
    pods/status                                 [update]
    networkpolicies.networking.k8s.io           [watch list]
            
  
---  
  
Küme Ağ Politikasına sahip ve Stackdriver Logging'in etkinleştirildiği, Calico
hizmet hesabı jetonlarını Stackdriver Logging'e kaydeden Google Kubernetes
Engine Kümeleri bu durumdan etkilenmiştir. Ağ Politikası etkinleştirilmemiş
kümeler etkilenmemiştir.

Calico CNI eklentisini yalnızca uyarı düzeyinde günlüğe kaydedecek ve yeni bir
hizmet hesabı kullanacak şekilde taşıyan bir düzeltmeyi dağıttık. Yama
uygulanan Calico kodu, sonraki bir sürümde dağıtılacaktır.

Önümüzdeki hafta içinde, potansiyel olarak etkilenen jetonların iptalini
gerçekleştireceğiz. İptal işlemi tamamlandığında bu bülten güncellenecektir.
**Başka bir işlem yapmanıza gerek yoktur.** (Bu dönüşüm 16/11/2018 tarihinde
tamamlanmıştır)

Bu jetonları derhal dönüştürmek isterseniz aşağıdaki komutu
çalıştırabilirsiniz. Hizmet hesabı için yeni gizli anahtar birkaç saniye
içinde otomatik olarak yeniden oluşturulacaktır:  
      
    
    
    kubectl get sa --namespace kube-system calico -o template --template '{{(index .secrets 0).name}}' | xargs kubectl delete secret --namespace kube-system
            
  
---  
  
####  Algılama

GKE, API sunucusuna yapılan tüm erişimleri günlüğe kaydeder. Google Cloud'un
beklenen IP aralığı dışından bir Calico jetonunun kullanılıp kullanılmadığını
belirlemek için aşağıdaki Stackdriver sorgusunu çalıştırabilirsiniz. Bunun
yalnızca GCP ağı dışından yapılan çağrı kaydı sonuçlarını döndüreceğini
unutmayın. Sorguyu özel ortamınızın ihtiyaçlarına göre kişiselleştirmelisiniz.  
  
---  
      
    
    
    resource.type="k8s_cluster"
    protoPayload.authenticationInfo.principalEmail="system:serviceaccount:kube-system:calico"
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.34.208.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.35.192.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.35.200.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.59.80.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.192.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.208.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.216.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.220.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.222.0/24")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.224.0.0/13")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "162.216.148.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "162.222.176.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "173.255.112.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "192.158.28.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.192.112.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.223.232.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.223.236.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "23.236.48.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "23.251.128.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.204.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.208.0.0/13")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "107.167.160.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "107.178.192.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.2.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.4.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.8.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.16.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.32.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.64.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.192.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.240.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.8.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.16.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.32.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.64.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.128.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "104.154.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "104.196.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "208.68.108.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.184.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.188.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.202.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.192.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.224.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.192.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.196.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.198.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.199.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.199.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.200.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "2600:1900::/35")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.224.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.232.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.234.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.192.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.236.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.240.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.232.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.4.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.220.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.242.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.244.0.0/14")
            
  
---  
  
##  14 Ağustos 2018

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
Aşağıdaki CVE'ler [ Intel tarafından açıklanmıştır
](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) :

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) ( [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) için) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (işletim sistemleri ve [ SMT ](https://en.wikipedia.org/wiki/Hyper-threading) için) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (sanallaştırma için) 

Bu CVE'lerin tamamına "L1 Terminal Fault (L1TF)" adı verilir.

Bu L1TF güvenlik açıkları, işlemci düzeyinde veri yapılarının yapılandırmasına
saldırarak kurgusal yürütmeyi kötüye kullanır. "L1", bellek erişimini
hızlandırmak için kullanılan küçük bir çekirdek içi kaynak olan 1. Düzey veri
önbelleğini temsil eder.

Bu güvenlik açıklarına ve Compute Engine'in çözümlerine dair daha fazla
ayrıntı için [ Google Cloud blog yayınını
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=tr) okuyun.

####  Google Kubernetes Engine etkisi

Kubernetes Engine'i çalıştıran ve müşteri Kümelerini ve Düğümlerini
birbirinden ayıran altyapı, bilinen saldırılara karşı korunur.

Google'ın Kapsayıcı İçin Optimize Edilmiş İşletim Sistemi görüntüsünü kullanan
ve [ otomatik yükseltmenin ](https://cloud.google.com/kubernetes-
engine/docs/concepts/node-auto-upgrades?hl=tr) etkinleştirilmiş olduğu
Kubernetes Engine düğüm havuzları, 20/08/2018 haftasından başlayacak şekilde
kullanılabilir olduğunda COS görüntümüzün yama uygulanmış sürümlerine otomatik
olarak yükseltilecektir.

[ Otomatik yükseltmenin ](https://cloud.google.com/kubernetes-
engine/docs/concepts/node-auto-upgrades?hl=tr) etkinleştirilmemiş olduğu
Kubernetes Engine düğüm havuzlarının, COS görüntümüzün yama uygulanmış sürümü
kullanılabilir olduğunda [ manuel yükseltme
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=tr) işlemi yapması gerekir.

|  Yüksek  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  6 Ağustos 2018; Son güncelleme: 5 Eylül 2018

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
####  05.09.2018 Tarihli Güncelleme

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) kısa süre önce duyurulmuştur. [
CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
gibi bu da savunmasız sistemlerde hizmet reddi (DoS) saldırılarının etkisini
artıran çekirdek düzeyinde bir ağ iletişimi güvenlik açığıdır. Aralarındaki
temel fark, CVE-2018-5391 açığının IP bağlantıları üzerinde kötüye kullanılma
riski olmasıdır. Bu bülteni, bu güvenlik açıklarının her ikisini de kapsayacak
şekilde güncelledik.

####  Açıklama

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ("SegmentSmack") TCP bağlantıları
üzerindeki savunmasız sistemlerde hizmet reddi (DoS) saldırılarının etkisini
artıran çekirdek düzeyinde bir ağ iletişimi güvenlik açığını tanımlar.

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ("FragmentSmack") IP bağlantıları
üzerindeki savunmasız sistemlerde hizmet reddi (DoS) saldırılarının etkisini
artıran çekirdek düzeyinde bir ağ iletişimi güvenlik açığını tanımlar.

####  Google Kubernetes Engine etkisi

11/08/2018 itibarıyla tüm Kubernetes Engine ana düğümleri her iki güvenlik
açığına karşı korunmaktadır. Otomatik yükseltme yapılandırması olan tüm
Kubernetes Engine kümeleri de her iki güvenlik açığına karşı korunur. [
Otomatik yükseltmenin ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=tr) yapılandırılmamış olduğu ve en son 11/08/2018
tarihinden önce manuel olarak yükseltilmiş olan Kubernetes Engine düğüm
havuzları her iki güvenlik açığından da etkilenmektedir.

####  Yama uygulanan sürümler

Bu güvenlik açığının ciddiyeti nedeniyle, yama kullanıma sunulur sunulmaz
düğümlerinizi [ manuel olarak yükseltmenizi
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=tr#upgrading-nodes) öneririz.

|  Yüksek  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  30 Mayıs 2018

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
Kısa süre önce Git üzerinde, ayrıcalığı bulunmayan kullanıcıların gitRepo
hacimleriyle Kapsüller oluşturmasına izin verildiğinde Kubernetes'te ayrıcalık
artırmaya imkan tanıyabilecek bir güvenlik açığı keşfedilmiştir. Bu CVE, [
CVE-2018-11235 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-11235) etiketiyle tanımlanmaktadır.

####  Güvenlik açıklarından etkilendim mi?

Aşağıdaki koşulların tamamı geçerliyse güvenlik açığı sizi etkilemiştir:

  * Güvenilmeyen kullanıcılar Kapsül oluşturabiliyordur (veya Kapsül oluşturma işlemi tetikleyebiliyordur). 
  * Güvenilmeyen kullanıcılar tarafından oluşturulan Kapsüllerde ana makine kök erişimini önleyen kısıtlamalar vardır (ör. [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=tr) ile). 
  * Güvenilmeyen kullanıcılar tarafından oluşturulan Kapsüllerin gitRepo birim türünü kullanmasına izin veriliyordur. 

Tüm Kubernetes Engine düğümleri savunmasızdır.

####  Ne yapmalıyım?

GitRepo birim türünün kullanımını yasaklayın. GitRepo birimlerini
PodSecurityPolicy ile yasaklamak için ` gitRepo ` birim türünü
PodSecurityPolicy'nizdeki ` volumes ` beyaz listesinden çıkarın.

Eşdeğer gitRepo birim davranışı, bir initContainer'dan bir EmptyDir birimine
git kod deposu klonlanarak sağlanabilir:

    
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: git-repo-example
    spec:
      initContainers:
        # This container clones the desired git repo to the EmptyDir volume.
        - name: git-clone
          image: alpine/git # Any image with git will do
          args:
            - clone
            - --single-branch
            - --
            - https://github.com/kubernetes/kubernetes # Your repo
            - /repo # Put it in the volume
          securityContext:
            runAsUser: 1 # Any non-root user will do. Match to the workload.
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
          volumeMounts:
            - name: git-repo
              mountPath: /repo
      containers:
        ...
      volumes:
        - name: git-repo
          emptyDir: {}

####  Hangi yama bu güvenlik açığını ele alıyor?

Sonraki Kubernetes Engine sürümüne bir yama dahil edilecektir. Ayrıntılı bilgi
için lütfen bu bölümü tekrar kontrol edin.

|  Orta  |

  * [ CVE-2018-11235 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11235)

  
  
##  21 Mayıs 2018

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
Kısa süre önce Linux çekirdeğinde ayrıcalık artırmaya veya ayrıcalığı
bulunmayan bir işlemden hizmet reddi (çekirdek kilitlenmesiyle) saldırılarına
imkan tanıyan bazı güvenlik açıkları keşfedilmiştir. Bu CVE'ler [
CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) , [ CVE-2018-8897
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897) ve [
CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)
etiketleriyle tanımlanmaktadır. Tüm Kubernetes Engine düğümleri bu güvenlik
açıklarından etkilenmiştir. Aşağıda ayrıntılarıyla açıklandığı şekilde en son
yama sürümüne [ yükseltme ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-container-cluster?hl=tr) işlemi yapmanızı
öneririz.

####  Ne yapmalıyım?

Yükseltme için öncelikle ana düğümünüzü en yeni sürüme yükseltmeniz gerekir.
Bu yama Kubernetes Engine 1.8.12-gke.1, Kubernetes Engine 1.9.7-gke.1 ve
Kubernetes Engine 1.10.2-gke.1 için kullanılabilir. Bu sürümler, hem Container
İçin Optimize Edilmiş İşletim Sistemi hem de Ubuntu görüntüleri için yamalar
içerir.

Daha önce yeni bir küme oluşturduysanız bu kümenin kullanılabilmesi için yama
uygulanmış sürümü belirtmeniz gerekir. [ Otomatik düğüm yükseltme
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=tr) özelliğini etkinleştirilmiş olan ve manuel yükseltme yapmayan
müşterilerin düğümleri, önümüzdeki haftalarda yama uygulanmış sürümlere
yükseltilecektir.

####  Bu yama hangi güvenlik açıklarına yönelik?

Yama, aşağıdaki güvenlik açıklarının riskini azaltır:

[ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) : Bu güvenlik açığı, Linux çekirdeğini
etkiler. Ayrıcalığa sahip olmayan bir kullanıcı veya işlemin sistem
çekirdeğini kilitleyerek DoS saldırısı veya ayrıcalık artırmaya yol
açabilmesine imkan tanır. Bu güvenlik açığı 7,8 CVSS puanı ile Yüksek önem
düzeyli güvenlik açığı olarak derecelendirilmiştir.

[ CVE-2018-8897 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-8897) : Bu güvenlik açığı, Linux çekirdeğini
etkiler. Ayrıcalığa sahip olmayan bir kullanıcı veya işlemin sistem
çekirdeğini kilitleyerek DoS saldırısına yol açabilmesine imkan tanır. Bu
güvenlik açığı 6,5 CVSS puanı ile Orta önem düzeyli güvenlik açığı olarak
derecelendirilmiştir.

[ CVE-2018-1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) : Bu güvenlik açığı, Linux çekirdeği KVM
hipervizörünü etkiler. Ayrıcalığa sahip olmayan bir işlemin konuk çekirdeğini
kilitlemesine veya potansiyel ayrıcalıklar kazanmasına imkan tanır. Bu
güvenlik açığına Kubernetes Engine'in çalıştığı altyapıda yama uygulanmıştır,
böylece Kubernetes Engine etkilenmemiştir. Bu güvenlik açığı 8,0 CVSS puanı
ile Yüksek önem düzeyli güvenlik açığı olarak derecelendirilmiştir.

|  Yüksek  |

  * [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199)
  * [ CVE-2018-8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
  * [ CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)

  
  
##  12 Mart 2018

Açıklama  |  Önem Düzeyi  |  Notlar  
---|---|---  
  
Kubernetes projesinin [ kısa süre önce duyurduğu
](https://groups.google.com/forum/?hl=tr#!topic/kubernetes-security-
announce/P7lBjbjDKd8) yeni güvenlik açıkları [ CVE-2017-1002101
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101) ve [
CVE-2017-1002102 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2017-1002102) , container'ların container dışındaki
dosyalara erişebilmesine imkan tanımaktadır. Tüm Kubernetes Engine düğümleri
bu güvenlik açıklarından etkilenmiştir. Aşağıda ayrıntılarıyla açıklandığı
şekilde en kısa sürede en yeni yama sürümüne yükseltme yapmanızı öneririz.

####  Ne yapmalıyım?

Bu güvenlik açıklarının ciddiyeti nedeniyle, düğümler için otomatik yükseltme
özelliği etkinleştirilmiş olsun veya olmasın, yama kullanıma sunulur sunulmaz
düğümlerinizi [ manuel olarak yükseltmenizi
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=tr) öneririz. Yama 16 Mart'ta tüm müşteriler için
kullanılabilir olacaktır. Ancak [ sürüm programına
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=tr#march-12-2018) göre, kümenizin bulunduğu alt bölgeye bağlı olarak
sizin için daha önce kullanıma sunulabilir.

Yükseltme için öncelikle ana düğümünüzü en yeni sürüme yükseltmeniz gerekir.
Bu yama Kubernetes 1.9.4-gke.1, Kubernetes 1.8.9-gke.1 ve Kubernetes
1.7.14-gke.1 için kullanılabilecektir. Yeni kümeler 30 Mart'tan itibaren
varsayılan olarak yama uygulanmış sürümü kullanacaktır. Daha önce yeni bir
küme oluşturursanız bu kümenin kullanılabilmesi için yama uygulanmış sürümü
belirtmeniz gerekir.

[ Otomatik düğüm yükseltme ](https://cloud.google.com/kubernetes-
engine/docs/concepts/node-auto-upgrades?hl=tr) özelliği etkinleştirilmiş olan
ve manuel yükseltme yapmayan müşterilerin düğümleri, 23 Nisan'da yama
uygulanmış sürümlere yükseltilecektir. Ancak güvenlik açığının özelliği
nedeniyle, yama kullanıma sunulur sunulmaz düğümlerinizi [ manuel olarak
yükseltmenizi ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-container-cluster?hl=tr) öneririz.

####  Bu yama hangi güvenlik açıklarına yönelik?

Yama, aşağıdaki iki güvenlik açığının riskini azaltır:

Container'ların [ alt yol
](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath) birim
bağlantılarını kullanarak birim dışındaki dosyalara erişebilmesine imkan
tanıyan CVE-2017-1002101 güvenlik açığı. Bu, şu anlama gelir:
PodSecurityPolicy ile hostpath birimlerine container erişimini engelliyorsanız
kapsülleri güncelleme veya oluşturma becerisi olan bir saldırgan, diğer
herhangi bir birim türünü kullanarak bir hostpath bağlantısı kurabilir.

Container'ların belirli birim türlerini (gizli anahtarlar, config map'ler,
öngörülen birimler, Downward API birimleri) kullanarak birim dışındaki
dosyaları silmesine imkan tanıyan CVE-2017-1002102 güvenlik açığı. Bu, şu
anlama gelir: Bu birim türlerinden birini kullanan bir container'ın güvenliği
ihlal edilirse veya güvenilmeyen kullanıcıların kapsül oluşturmasına izin
verirseniz bir saldırgan, bu container'ı kullanarak ana makine üzerindeki
dosyaları rastgele silebilir.

Bu düzeltme hakkında daha fazla bilgi için [ Kubernetes blog yayınını
](https://kubernetes.io/blog/2018/04/04/fixing-subpath-volume-vulnerability/)
okuyun.

|  Yüksek  |

  * [ CVE-2017-1002101 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101)
  * [ CVE-2017-1002102 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102)

