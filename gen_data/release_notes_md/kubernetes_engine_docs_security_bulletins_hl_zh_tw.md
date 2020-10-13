#  安全性公告

本主題會說明所有的 Google Kubernetes Engine (GKE) 安全性公告。

發現安全漏洞之後，我們通常會保密，直到相關單位能夠將安全漏洞解決為止。在這種情況下，只要保密規定尚未撤銷，GKE 的 [ 版本資訊
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=zh_tw)
都只會將漏洞稱為「安全性更新」。保密規定撤銷後，我們就會更新版本資訊，向使用者說明修補程式所解決的安全漏洞。

**注意事項：** 如果您會在 GKE 中處理多用戶群工作負載，請特別留意這類公告，因為這些安全漏洞較有可能對多用戶群工作負載造成影響。如需 GKE
的安全性界限技術說明，或是想瞭解安全性界限對工作負載的影響，請參閱 [ 在 Kubernetes 堆疊的各層間提供隔離機制
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) 一文。

如要收到最新的安全性公告消息，請將本頁面的網址加入您的 [ 動態消息閱讀器
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ，或直接新增以下動態消息網址： `
https://cloud.google.com/feeds/kubernetes-engine-security-bulletins.xml `

##  GCP-2020-007

**發布日期：** 2020-06-01  
說明  |  嚴重性  |  附註  
---|---|---  
  
最近在 Kubernetes 中發現伺服器端偽造要求 (SSRF) 安全漏洞 [ CVE-2020-8555
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555)
。這項漏洞會讓某些授權使用者將機密資訊 (最多 500 個位元組) 從控制層主機網路外流出去。由於 Google Kubernetes Engine
(GKE) 控制層使用 Kubernetes 中的控制器，因此會受到這個安全漏洞影響。建議您按照下列步驟操作，將控制層 [ 升級
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=zh_tw) 至最新修補程式版本。節點則無須升級。  

####  該如何解決這個問題？

大多數的客戶無須採取進一步行動，大多數的叢集早已執行修補版本。以下 GKE 版本或更高版本均包含這個安全漏洞的修正措施：

  * 1.14.7-gke.39 
  * 1.14.8-gke.32 
  * 1.14.9-gke.17 
  * 1.14.10-gke.12 
  * 1.15.7-gke.17 
  * 1.16.4-gke.21 
  * 1.17.0-gke.0 

使用 [ 發布版本 ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-
channels?hl=zh_tw) 的叢集都已執行具有因應措施的控制層版本。

####  這個修補程式修正了什麼安全漏洞？

這些修補程式可降低安全漏洞 CVE-2020-8555 的風險。這個安全漏洞對於 GKE 的嚴重性為「中」，因為有各種控制層強化措施，所以不易進行漏洞攻擊。

攻擊者若取得相關權限而獲准建立具有特定內建磁碟區類型 (GlusterFS、Quobyte、StorageFS, ScaleIO) 的 pod 或
StorageClass，即便「沒有」 __ 控制要求主體，也可以透過主要執行個體的主機網路促使 ` kube-controller-manager `
發出 ` GET ` 要求或 ` POST ` 要求。這些磁碟區類型很少在 GKE
上使用，所以如果發現陌生使用者使用這些磁碟區類型，可以視為有用的偵測訊號。

如果這類攻擊手段配合可將 ` GET/POST `
的結果洩漏給攻擊者的途徑，例如透過記錄檔，就可能導致機密資訊外洩。因此，我們更新了相關的儲存空間驅動程式，以防止這類資料外洩的可能性。

|

中

|

[ CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555)  
  
##  GCP-2020-006

**發布日期：** 2020-06-01  
說明  |  嚴重性  |  附註  
---|---|---  
  
Kubernetes 已揭露一項 [ 安全漏洞
](https://github.com/kubernetes/kubernetes/issues/91507)
。這項漏洞會讓有權限的容器將節點流量重新導向至另一個容器。這類攻擊無法讀取或修改雙向 TLS/SSH 流量 (例如在 kubelet 和 API
伺服器之間) 或來自採用 mTLS 的應用程式的流量。所有的 Google Kubernetes Engine (GKE)
節點都會受到這個安全漏洞的影響，建議您按照下列步驟操作， [ 升級 ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=zh_tw) 至最新的修補程式版本。

####  該如何解決這個問題？

為了降低這個安全漏洞的風險，請 [ 升級 ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=zh_tw)
您的控制層，接著將節點升級至下列修補版本之一。使用發布版本的叢集已在控制層和節點上執行修補版本：

  * 1.14.10-gke.36 
  * 1.15.11-gke.15 
  * 1.16.8-gke.15 

一般來說，極少容器需要使用 ` CAP_NET_RAW ` 。依據預設，系統應該會透過 [ PodSecurityPolicy
](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-
policies?hl=zh_tw) 或 [ Anthos Policy Controller
](https://cloud.google.com/anthos-config-management/docs/concepts/policy-
controller?hl=zh_tw) 封鎖這項功能及其他強大的功能：

  * 如要從容器捨棄 ` CAP_NET_RAW ` 功能，方法如下： 
    * 使用以下指令碼透過 [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=zh_tw) 強制執行： 
        
                
        # Require dropping CAP_NET_RAW with a PSP
        apiversion: extensions/v1beta1
        kind: PodSecurityPolicy
        metadata:
          name: no-cap-net-raw
        spec:
          requiredDropCapabilities:
            -NET_RAW
             ...
             # Unrelated fields omitted
        

    * 或者，使用 Anthos Policy Controller/Gatekeeper 搭配這個 [ 限制範本 ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) ，然後套用，例如： 
        
                
        # Dropping CAP_NET_RAW with Gatekeeper
        # (requires the K8sPSPCapabilities template)
        apiversion: constraints.gatekeeper.sh/v1beta1
        kind:  K8sPSPCapabilities
        metadata:
          name: forbid-cap-net-raw
        spec:
          match:
            kinds:
              - apiGroups: [""]
              kinds: ["Pod"]
            namespaces:
              #List of namespaces to enforce this constraint on
              - default
            # If running gatekeeper >= v3.1.0-beta.5,
            # you can exclude namespaces rather than including them above.
            excludedNamespaces:
              - kube-system
          parameters:
            requiredDropCapabilities:
              - "NET_RAW"
        

    * 或者，更新您的 pod 規格： 
        
                
        # Dropping CAP_NET_RAW from a Pod:
        apiVersion: v1
        kind: Pod
        metadata:
          name: no-cap-net-raw
        spec:
          containers:
            -name: may-container
             ...
            securityContext:
              capabilities:
                drop:
                  -NET_RAW
        

####  這個修補程式修正了什麼安全漏洞？

這個修補程式可有效降低下列安全漏洞的風險：

[ Kubernetes 問題 91507 ](https://github.com/kubernetes/kubernetes/issues/91507)
` CAP_NET_RAW ` 功能 (其包含在預設容器功能集) 中所述的安全漏洞，會在節點上惡意設定 IPv6
堆疊，並將節點流量重新導向至攻擊者控制的容器，讓攻擊者可攔截/修改來自節點的流量或預定送至節點的流量。這類攻擊無法讀取或修改雙向 TLS/SSH 流量
(例如在 kubelet 和 API 伺服器之間) 或來自採用 mTLS 的應用程式的流量。

|

中

|

[ Kubernetes 問題 91507 ](https://github.com/kubernetes/kubernetes/issues/91507)  
  
  
##  GCP-2020-005

**發布日期：** 2020-05-07  
**更新日期：** 2020-05-07  說明  |  嚴重性  |  附註  
---|---|---  
  
最近在 Linux 核心發現一個安全漏洞 (請參考 [ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) 中的說明)。這項漏洞會允許濫用容器逃逸，並獲得主機節點上的 Root 權限。

執行 GKE 1.16 或 1.17 的 Google Kubernetes Engine (GKE) Ubuntu
節點會受到這個安全漏洞的影響，建議您參考以下詳細說明，盡快升級至最新的修補程式版本。

執行 Container-Optimized OS 的節點不受影響，在 GKE On-Prem 上運作的節點也不受影響。

####  該如何解決這個問題？

**大多數的客戶無須採取進一步行動，只有在 GKE 版本 1.16 或 1.17 中執行 Ubuntu 的節點受到影響。**

如要升級節點，您必須先將主要執行個體升級至最新版本。Kubernetes 1.16.8-gke.12、1.17.4-gke.10
及更高版本均包含了這個修補程式。您可以從 [ 版本資訊 ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=zh_tw) 中得知該版本是否提供這些修補程式。

####  這個修補程式修正了什麼安全漏洞？

這個修補程式可有效降低下列安全漏洞的風險：

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) 說明 Linux 核心版本 5.5.0
及更高版本中存在一個安全漏洞。這項漏洞會將使用者以 exec
形式操作的機率降至最低，允許惡意容器讀取和寫入核心記憶體，藉此在主機節點上執行根層級程式碼。這個安全漏洞的嚴重性為「高」。

|

高

|

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835)  
  
  
##  GCP-2020-003

**發布日期：** 2020-03-31  
**更新日期：** 2020-03-31  說明  |  嚴重性  |  附註  
---|---|---  
  
最近在 Kubernetes 中發現一個安全漏洞 (請參考 [ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) 中的說明)。這項漏洞會允許任何經授權可進行 POST 要求的使用者在
Kubernetes API 伺服器上執行遠端阻斷服務攻擊。您可以在 [ 這裡
](https://groups.google.com/forum/?hl=zh_tw#!topic/kubernetes-security-
announce/wuwEwZigXBc) 找到 Kubernetes Product Security Committee (PSC)
發布的相關安全漏洞資訊。

無論是使用 [ 主要授權網路 ](https://cloud.google.com/kubernetes-engine/docs/how-
to/authorized-networks?hl=zh_tw) 的 GKE 叢集或是 [ 無公開端點的私人叢集
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=zh_tw#private_master) ，都可以有效降低這個安全漏洞的風險。

####  該如何解決這個問題？

建議您將叢集升級至包含這個安全漏洞修正措施的修補程式版本。

下列為包含修正措施的修補程式版本：

  * 1.13.12-gke.29 
  * 1.14.9-gke.27 
  * 1.14.10-gke.24 
  * 1.15.9-gke.20 
  * 1.16.6-gke.1 

####  這個修補程式修正了哪些安全漏洞？

它可修正下列阻斷服務 (DoS) 安全漏洞：

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) 。

|

中

|

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  GCP-2020-002

**發布日期：** 2020-03-23  
**更新日期：** 2020-03-23  說明  |  嚴重性  |  附註  
---|---|---  
  
Kubernetes 已揭露 [ 兩個阻斷服務安全漏洞
](https://groups.google.com/forum/?hl=zh_tw#!topic/kubernetes-security-
announce/2UOlsba2g0s) ，其中一個會影響 API 伺服器，另一個會影響 Kubelet。詳情請參閱 Kubernetes 問題： [
89377 ](https://github.com/kubernetes/kubernetes/issues/89377) 和 [ 89378
](https://github.com/kubernetes/kubernetes/issues/89378) 。

####  該如何解決這個問題？

所有 GKE 使用者都不會受到 CVE-2020-8551 的影響，除非未受信任的使用者可以在叢集內部網路傳送要求。使用 [ 主要授權網路
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=zh_tw) 也能有效降低 CVE-2020-8552 的安全風險。

####  這些安全漏洞何時可以得到修補？

要修補 CVE-2020-8551 安全漏洞，您必須進行節點升級。以下是包含因應措施的修補程式版本：

  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

注意：1.14.x 以下版本不會受到這個安全漏洞的影響，因此不需要修補程式。

要修補 CVE-2020-8552 安全漏洞，您必須進行主要執行個體升級。以下是包含因應措施的修補程式版本：

  * 1.14.10-gke.32 
  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

|

中

|

[ CVE-2020-8551 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8551)  
[ CVE-2020-8552 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8552)  
  
##  2020 年 1 月 21 日；上次更新日期：2020 年 1 月 24 日

**發布日期：** 2020-01-21  
**更新日期：** 2020-01-24  說明  |  嚴重性  |  附註  
---|---|---  
  
**2020 年 1 月 24 日更新：** 提供可用修補版本的程序正在制訂中，預計在 2020 年 1 月 25 日完成。

* * *

Microsoft 已揭露 Windows Crypto API 及其橢圓曲線簽章的驗證機制存在安全漏洞。詳情請參閱 [ Microsoft 公告事項
](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) 。

**該如何解決這個問題？**

**大多數的客戶無須採取進一步行動，只有執行 Windows Server 的節點受到影響。**

使用 Windows Server 節點的客戶，不論是節點本身，或是這些節點所處理的容器化工作負載，都必須更新到已修補的版本，才能降低這項安全漏洞的風險。

**如何更新容器：**

使用 Microsoft 最新的基本容器映像檔 (選擇上次更新時間為 2020 年 1 月 14 日或之後的 [ servercore
](https://hub.docker.com/_/microsoft-windows-servercore) 或 [ nanoserver
](https://hub.docker.com/_/microsoft-windows-nanoserver) 標記)，來重建容器。

**如何更新節點：**

提供可用修補版本的程序正在制訂中，預計在 2020 年 1 月 24 日完成。

您可以選擇屆時再將節點升級為修補 GKE 版本，也可以隨時使用 Windows Update 手動部署最新的 Windows 修補程式。

下列修補程式版本將包含因應措施：

  * 1.14.7-gke.40 
  * 1.14.8-gke.33 
  * 1.14.9-gke.23 
  * 1.14.10-gke.17 
  * 1.15.7-gke.23 
  * 1.16.4-gke.22 

**這個修補程式修正了哪些安全漏洞？**

這個修補程式可有效降低下列安全漏洞的風險：

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601) \- 這項安全漏洞也稱為 [ Windows Crypto API 假冒安全漏洞
](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) ，可能被利用來製作看起來可信的惡意執行檔，或讓攻擊者進行中間人攻擊，並透過與受影響軟體的
TLS 連線破解機密資訊。

|

NVD 基礎分數：8.1 (高)

|

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601)  
  
  
##  2019 年 11 月 14 日

**發布日期：** 2019-11-14  
**更新日期：** 2019-11-14  說明  |  嚴重性  |  附註  
---|---|---  
  
Kubernetes 已揭露 kubernetes-csi 補充元件 [ ` external-provisioner `
](https://github.com/kubernetes-csi/external-provisioner) 、 [ ` external-
snapshotter ` ](https://github.com/kubernetes-csi/external-snapshotter) 及 [ `
external-resizer ` ](https://github.com/kubernetes-csi/external-resizer)
中的一項安全性問題，這個問題會影響 [ Container Storage Interface (CSI) 驅動程式
](https://kubernetes-csi.github.io/docs/drivers.html) 中隨附補充元件的大多數版本。詳情請參閱 [
Kubernetes 公告事項 ](https://github.com/kubernetes/kubernetes/issues/85233) 。

**該如何解決這個問題？**  
**這個安全漏洞不影響任何代管的 GKE 元件** 。如果您在執行 GKE 1.12 以上版本的 [ GKE Alpha 版叢集
](https://cloud.google.com/kubernetes-engine/docs/concepts/alpha-
clusters?hl=zh_tw) 中，是自行管理本身的 CSI 驅動程式，那就可能會受到影響。如果您屬於上述情況，請洽詢您的 CSI
驅動程式供應商以取得升級操作說明。

**這個修補程式修正了哪些安全漏洞？**  
[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255) ：這項 CVE 在 ` kubernetes-csi ` 補充元件 [ `
external-provisioner ` ](https://github.com/kubernetes-csi/external-
provisioner) 、 [ ` external-snapshotter ` ](https://github.com/kubernetes-
csi/external-snapshotter) 及 [ ` external-resizer `
](https://github.com/kubernetes-csi/external-resizer)
中是安全漏洞，可能會允許未經授權的磁碟區資料存取或變更。這會影響 [ CSI 驅動程式 ](https://kubernetes-
csi.github.io/docs/drivers.html) 隨附補充元件的大多數版本。

|

中

|

[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255)  
  
  
##  2019 年 11 月 12 日

**發布日期：** 2019-11-12  
**更新日期：** 2019-11-12  說明  |  嚴重性  |  附註  
---|---|---  
  
Intel 已揭露了多個 CVE，顯示可能允許推測性執行功能和微架構狀態經過交互作用後，公開資料。詳情請參閱 [ Intel 公告事項
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) 。

**執行 Kubernetes Engine 的主機基礎架構會隔離各個客戶的工作負載。除非您在自己的多用戶群 GKE 叢集內執行不受信任的程式碼， _並且_
使用 N2、M2 或 C2 節點，否則不必採取進一步行動。 ** 針對 N1 節點上的 GKE 執行個體，不必採取新的行動。

如果您目前執行的是 Anthos GKE On-Prem，資料公開程度則因硬體而異。請將您的基礎架構與 [ Intel 公告事項
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) 相互比對。

####  該如何解決這個問題？

**只有當您使用 N2、M2 或 C2 節點的節點集區， _並且_ 這些節點在您自己的多用戶群 GKE
叢集中執行不受信任的程式碼，才會受到影響，也才需要採取行動。 **

**重新啟動節點會套用修補程式** 。在您的節點集區中重新啟動所有節點的最簡單方法，是使用 [ 升級
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=zh_tw#upgrade_nodes) 作業強制所有受影響的節點集區重新啟動。  

附註：您不需要在升級時變更版本。您可以透過 ` cluster-version ` 旗標，啟動相同節點版本的升級。

####  這個修補程式修正了哪些安全漏洞？

這個修補程式可有效降低下列安全漏洞的風險：

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)
：這項 CVE 又稱為 TSX 非同步取消 (TAA)。TAA 所提供的另一種資料竊取途徑，是利用與 [ 微架構資料取樣 (MDS)
](https://cloud.google.com/kubernetes-engine/docs/security-
bulletins?hl=zh_tw#may-14-2019) 所使用的同一種微架構資料結構。

[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)
：這是阻斷服務 (DoS) 安全漏洞，會讓虛擬機器主機允許惡意客體侵襲未受保護的主機，並引發當機。這項 CVE
又稱為「頁面大小變更的機器檢查錯誤」。這不會影響 GKE。

|

中

|

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)  
[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)  
  
##  2019 年 10 月 22 日

**發布日期：** 2019-10-22  
**更新日期：** 2019-10-22  說明  |  嚴重性  |  附註  
---|---|---  
  
最近在 Go 程式設計語言中發現一個安全漏洞，請參考 [ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276) 中的說明。這項安全漏洞可能會影響使用驗證 Proxy 的 Kubernetes
設定。詳情請參閱 [ Kubernetes 公告事項
](https://groups.google.com/forum/?hl=zh_tw#!topic/kubernetes-security-
announce/PtsUCqFi4h4) 。

Kubernetes Engine 不允許驗證 Proxy 的設定，因此不受這項安全漏洞的影響。

|

無

|

[ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276)  
  
  
##  2019 年 10 月 16 日

**發布日期：** 2019-10-16  
**更新日期：** 2019-10-24  說明  |  嚴重性  |  附註  
---|---|---  
  
**2019 年 10 月 24 日更新：** 修補完成的版本現在已可供所有區域使用。

* * *

最近在 Kubernetes 中發現一個安全漏洞 (請參考 [ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) 中的說明)，允許任何經授權可進行 POST 要求的使用者在 Kubernetes
API 伺服器上執行遠端阻斷服務攻擊。您可以在 [ 這裡
](https://groups.google.com/forum/?hl=zh_tw#!topic/kubernetes-security-
announce/jk8polzSUxs) 找到 Kubernetes Product Security Committee (PSC)
發布的相關安全漏洞資訊。

無論是使用 [ 主要授權網路 ](https://cloud.google.com/kubernetes-engine/docs/how-
to/authorized-networks?hl=zh_tw) 的 GKE 叢集或是 [ 無公開端點的私人叢集
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=zh_tw#private_master) ，都可以有效降低這個安全漏洞的風險。

######  該如何解決這個問題？

含有相關修正的修補程式版本發布後，建議您盡快升級叢集。排定於 10 月 14 日當週發布的 GKE 版本，預期將隨附這類修補程式版本，所有區域皆可使用。

下列修補程式版本將包含因應措施：

  * 1.12.10-gke.15 
  * 1.13.11-gke.5 
  * 1.14.7-gke.10 
  * 1.15.4-gke.15 

######  這個修補程式修正了哪些安全漏洞？

這個修補程式可有效降低下列安全漏洞的風險：

CVE-2019-11253 是阻斷服務 (DoS) 安全漏洞。

|

高

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
  
##  2019 年 9 月 16 日

**發布日期：** 2019-09-16  
**更新日期：** 2019-10-16  說明  |  嚴重性  |  附註  
---|---|---  
  
這則公告自最初發布後已經過更新。

最近在 Go 程式設計語言中發現新的安全漏洞 [ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) 和 [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) ，這兩個是阻斷服務
(DoS) 安全漏洞。在 GKE 中，這可能會允許使用者編寫惡意要求，過度耗用 Kubernetes API 伺服器中的
CPU，降低叢集控制層的可用性。詳情請參閱 [ Go 程式設計語言公告事項
](https://groups.google.com/forum/?hl=zh_tw#!topic/golang-
announce/65QixT3tcmg) 。

######  該如何解決這個問題？

一旦發布了最新修補程式版本，能有效降低此安全漏洞的風險之後，建議您盡快升級叢集。根據 [ 發布時間表
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=zh_tw#september_16_2019) ，我們預計這類修補程式會在下次推出 GKE 時於所有區域提供。

下列修補程式版本將包含因應措施：

  * **2019 年 10 月 16 日更新：** 1.12.10-gke.15 
  * 1.13.10-gke.0 
  * 1.14.6-gke.1 

######  這個修補程式修正了什麼安全漏洞？

這個修補程式可有效降低下列安全漏洞的風險：

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) 和 [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) 為阻斷服務 (DoS)
安全漏洞。

|

高

|

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512)  
[ CVE-2019-9514 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9514)  
  
  
##  2019 年 9 月 5 日

**發布日期：** 2019-09-05  
**更新日期：** 2019-09-05

在  2019 年 5 月 31 日  公告中記錄的安全漏洞修正公告已更新。

##  2019 年 8 月 22 日

**發布日期：** 2019-08-22  
**更新日期：** 2019-08-22

2019 年 8 月 5 日  的公告已更新。之前公告記錄的安全漏洞修正已 [ 推出
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=zh_tw#august_22_2019) 。

##  2019 年 8 月 8 日

**發布日期：** 2019-08-08  
**更新日期：** 2019-08-08

2019 年 8 月 5 日  的公告已更新。我們預計該公告中記錄的安全漏洞修正會在下個 GKE 版本中提供。

##  2019 年 8 月 5 日

**發布日期：** 2019-08-05  
**更新日期：** 2019-08-09  說明  |  嚴重性  |  附註  
---|---|---  
  
這則公告自最初發布後已經過更新。

我們最近在 Kubernetes 中發現一個安全漏洞 [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) ，允許叢集範圍內的 [ 自訂資源
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) 執行個體，當做所有命名空間中存在的命名空間物件處理。這表示，只具有命名空間層級 RBAC
權限的使用者和服務帳戶，可與叢集範圍內的自訂資源互動。攻擊者如要利用這項安全漏洞，必須要能存取任何命名空間中的資源。

######  該如何解決這個問題？

一旦發布了最新修補程式版本，能有效降低此安全漏洞的風險之後，建議您盡快 [ 升級
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=zh_tw) 叢集。我們預計這類修補程式會在下次推出 GKE 時於所有區域提供。下列修補程式版本將包含因應措施：

  * 1.11.10-gke.6 
  * 1.12.9-gke.13 
  * 1.13.7-gke.19 
  * 1.14.3-gke.10 ( [ 快速版 ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels?hl=zh_tw) ) 

######  這個修補程式修正了什麼安全漏洞？

這個修補程式可有效降低下列安全漏洞的風險： [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) 。

|

中

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)  
  
##  2019 年 7 月 3 日

**發布日期：** 2019-07-03  
**更新日期：** 2019-07-03  說明  |  嚴重性  |  附註  
---|---|---  
  
可解決 CVE-2019-11246 的 ` kubectl ` 修補版本現已隨附 [ ` gcloud ` 253.0.0
](https://cloud.google.com/sdk/docs/release-notes?hl=zh_tw#kubernetes_engine)
提供。詳情請參閱  2019 年 6 月 25 日安全性公告  。

**注意：** ` kubectl ` 1.11.10 中未提供修補程式。

|

高

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  2019 年 7 月 3 日

**發布日期：** 2019-06-25  
**更新日期：** 2019-07-03  說明  |  嚴重性  |  附註  
---|---|---  
  
######  2019 年 7 月 3 日更新

我們上次更新時，1.11.9 和 1.11.10 版本尚未提供修補程式。現在我們已針對這兩個 1.11 版本發布升級程式 1.11.10-gke.5。

目前 GKE 主要執行個體已修補完畢，而執行 Kubernetes Engine 的 Google 基礎架構已經過修補且不會受到這個安全漏洞的影響。

1.11 主要執行個體即將淘汰，並排定在 2019 年 7 月 8 日當週自動升級至 1.12。您可以選擇任何下列建議動作，促使節點使用修補的版本：

  * 在 2019 年 7 月 8 日前將節點升級至 1.11.10-gke.5。在這天之後，1.11 版本會開始從可用升級目標清單中移除。 
  * 在 1.11 節點上啟用 [ 自動升級 ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades?hl=zh_tw) ，並且在主要執行個體升級至 1.12 時允許節點升級。 
  * [ 手動升級 ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=zh_tw) 主要執行個體和節點到修正的 1.12 版本。 

2019 年 6 月 24 日的原始公告如下：

* * *

######  2019 年 6 月 24 日更新

我們在世界標準時間 2019 年 6 月 22 日 21:40 提供下列修補過的Kubernetes 版本。Kubernetes 1.11.0 和
1.13.6 版本間的主要執行個體會自動更新至修補的版本。如果您執行的版本與此修補程式不相容，請在升級節點前先升級至相容的主要執行個體版本 (如下所列)。

**由於這些安全漏洞比較嚴重，無論是否已啟用節點自動升級功能，建議您還是盡快[ 手動升級
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=zh_tw) 節點和主要執行個體至以下其中一個版本。 **

修補過的版本：

  * 1.11.8-gke.10 
  * 1.12.7-gke.24 
  * 1.12.8-gke.10 
  * 1.13.6-gke.13 

2019 年 6 月 18 日的原始公告如下：

* * *

Netflix 最近揭露了 Linux 核心的三個 TCP 安全漏洞：

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

上述 CVE 統稱為 [ NFLX-2019-001 ](https://github.com/Netflix/security-
bulletins/blob/master/advisories/third-party/2019-001.md) 。

未經修補的 Linux 核心可能會受到遠端觸發的阻斷服務攻擊。 **Google Kubernetes Engine
節點傳送或接收不受信任的網路流量時，會受到這個安全漏洞影響。我們建議您依循以下這些因應步驟來保護自己的工作負載。**

######  Kubernetes 主要執行個體

  * Kubernetes 主要執行個體如果使用 [ 授權網路 ](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks?hl=zh_tw) ，將流量限制在只使用受信任網路，不會受到影響。 

  * 由 Google 代管的 GKE 叢集主要執行個體，在未來幾天內會自動進行修補，客戶不必採取任何行動。 

######  Kubernetes 節點

流量限縮在受信任網路的節點並不會受到影響。這樣處理的叢集具有下列特性：

  * 節點以防火牆隔離不受信任的網路，或沒有公開 IP ( [ 私人叢集 ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters?hl=zh_tw) ) 
  * 叢集沒有公開的 LoadBalancer 服務 

為了有效降低這些安全漏洞的風險，Google
正在研議永久性的對策，準備推出全新的節點版本。永久性修正方案就緒後，我們就會更新這項公告，並傳送電子郵件通知所有 GKE 客戶。

我們另外準備了 Kubernetes DaemonSet，在永久性修正方案尚未出爐前，使用者也可以修改主機的 ` iptables `
設定，做為降低漏洞風險的因應措施。

#####  該如何解決這個問題？

執行下列指令，將 Kubernetes DaemonSet 套用到叢集中的所有節點。這會將 ` iptables ` 規則新增至節點上現有的 `
iptables ` 規則，以降低這個安全漏洞的風險。 **請為每個 Google Cloud 專案的每個叢集執行指令一次。**

    
    
    
    kubectl apply -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

因為 GKE 不支援 Ipv6,，因此不需要 ip6tables 規則。

一旦修補的節點版本準備就緒，而所有可能受影響的節點也都升級了，您就可以使用下列指令移除 DaemonSet。 **請為每個 Google Cloud
專案的每個叢集執行指令一次。**

    
    
    
    kubectl delete -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

|  高  
中  
中  
|  [ CVE-2019-11477 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11477)  
[ CVE-2019-11478 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11478)  
[ CVE-2019-11479 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11479)  
  
  
##  2019 年 6 月 25 日

說明  |  嚴重性  |  附註  
---|---|---  
  
**2019 年 7 月 3 日更新：** 在 ` gcloud ` 253.0.0， ` kubectl ` 1.12.9、1.13.6、1.14.2
及以上版本均含有這個修補程式。

**注意：** 1.11.10 中不提供這個修補程式。

* * *

我們最近在 Kubernetes 中發現一個安全漏洞 [ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) ，允許有權執行容器內 ` kubectl cp `
作業和程式碼的攻擊者修改主機上的檔案。攻擊者可能藉此在主機檔案系統中取代或建立檔案。詳情請參閱 [ Kubernetes 公告事項
](https://groups.google.com/forum/?hl=zh_tw#!topic/kubernetes-security-
announce/NLs2TGbfPdo) 。

**所有 Google Kubernetes Engine (GKE)` gcloud ` 版本都會受到此安全漏洞的影響，我們建議您在最新的 `
gcloud ` 修補程式版本發布時進行升級。 ** 即將提供的修補程式版本會包含此安全漏洞的因應措施。

######  該如何解決這個問題？

下一版的 ` gcloud ` 將會提供 ` kubectl ` 的修補版本。您也可以自己 [ 直接升級 ` kubectl `
](https://kubernetes.io/docs/tasks/tools/install-kubectl/) 。

您可以在 [ ` gcloud ` 版本資訊 ](https://cloud.google.com/sdk/docs/release-
notes?hl=zh_tw) 中得知是否提供這個修補程式。

######  這個修補程式修正了什麼安全漏洞？

安全漏洞 [ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) 允許有權執行容器內 ` kubectl cp `
作業和程式碼的攻擊者修改主機上的檔案。攻擊者可能藉此在主機檔案系統中取代或建立檔案

|

高

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  2019 年 6 月 18 日

說明  |  嚴重性  |  附註  
---|---|---  
  
我們最近在 Docker 中發現一個安全漏洞 [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) ，允許可在容器內執行程式碼的攻擊者，控制外部啟動的 ` docker cp `
作業。攻擊者可能藉此將檔案寫入的位置，變更到主機檔案系統的任何地方。

**所有執行 Docker 的 Google Kubernetes Engine (GKE)
節點都會受到此安全漏洞的影響，建議您在最新修補程式版本發布後立即升級。即將提供的修補程式版本會包含此安全漏洞的因應措施。**

**所有 Google Kubernetes Engine (GKE) 主要執行個體在 1.12.7 版本之前，都是執行
Docker，因此都會受到這個安全漏洞的影響。** 在 GKE，使用者無法存取主要執行個體上的 ` docker cp ` ，因此這個安全漏洞對 GKE
主要執行個體，其實只會造成有限度的影響。

#####  該如何解決這個問題？

只有執行 Docker 的節點會受到影響，且只有在發出可能遭到把持的 ` docker cp ` (或 API 相等) 指令時，才會出現問題。在
Kubernetes 環境中，這是相當不尋常的情況。 執行 [ 含 Containerd 的 COS
](https://cloud.google.com/kubernetes-engine/docs/concepts/using-
containerd?hl=zh_tw) 節點不會受到影響。

要將節點升級，您必須先 [ 升級主要執行個體 ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=zh_tw#upgrading_the_cluster)
到修補的版本。修補程式釋出後，您可以啟動主要執行個體升級，或等待 Google 自動升級主要執行個體。這個修補程式會包含在下一個 GKE 修補程式隨附的
Docker 18.09.7 中。 **這個修補程式只針對 GKE 1.13 以上版本提供。**

我們會依一般升級節奏，自動將叢集主要執行個體升級至修補的版本。您也可以在修補版本發布後，自行啟動主要執行個體升級。

我們會在含有修補程式的版本發布後立即更新此公告。您可以從 [ 版本資訊 ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=zh_tw) 中得知該版本是否提供這些修補程式。

#####  這個修補程式修正了什麼安全漏洞？

這個修補程式可有效降低下列安全漏洞的風險：

安全漏洞 [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) 允許可在容器內執行程式碼的攻擊者，控制外部啟動的 ` docker cp `
作業。攻擊者可能藉此將檔案寫入的位置，變更到主機檔案系統的任何地方。

|  高  |  
  
##  2019 年 5 月 31 日

說明  |  嚴重性  |  附註  
---|---|---  
  
這則公告自最初發布後已經過更新。

######  2019 年 8 月 2 日更新

初始發布公告時，只有 1.13.6-gke.0 至 1.13.6-gke.5 受到影響。在迴歸處理後，現在所有 1.13.6.x
版本都受到影響。如果您執行的是 1.13.6，請盡快升級至 1.13.7。

Kubernetes 專案已揭露 kubelet v1.13.6 和 v1.14.2 中的 [ CVE-2019-11245
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11245) ，這可能造成容器以 UID 0
的身分 (通常對應到 ` root ` 使用者) 執行，即使容器映象檔案指定了不同的使用者。 **如果容器以非 root
使用者的身分執行，且您執行的節點版本為 1.13.6-gke.0 至 1.13.6-gke.6，建議您為容器不應以 UID 0 身分執行的叢集中的所有
Pod 設定` RunAsUser ` 。 **

如果指定非 root ` USER ` 值 (例如在 Dockerfile 中設定 ` USER `
的值)，就會出現非預期的行為。當容器在節點上第一次執行時，會正確套用指定的 UID。不過因為有這個問題，在第二次 (及後續的) 執行時，容器會以 UID 0
的身分執行，而不使用指定的 UID。這通常是不必要的權限提升，可能會導致非預期的應用程式行為。

#####  我如何判斷自己執行的是受影響的版本？

執行以下指令即可列出所有節點及其 kubelet 版本：

    
    
    
    kubectl get nodes -o=jsonpath='{range .items[*]}'\
    '{.status.nodeInfo.machineID}'\
    '{"\t"}{.status.nodeInfo.kubeletVersion}{"\n"}{end}'

如果輸出有下列 kubelet 版本，您的節點即受到影響：

  * v1.13.6 
  * v1.14.2 

#####  如何知道自己的特定設定受到影響？

如果您的容器以非 root 使用者身分執行，且執行的節點版本為 1.13.6-gke.0 至 1.13.6-gke.6，就會受到影響，但下列情形除外：

  * Pod 如果針對 ` runAsUser ` PodSecurityContext 指定有效的非 root 值，不會受到影響，而且持續運作如常。 
  * 強制執行 ` runAsUser ` 設定的 PodSecurityPolicies 也不受影響，且會繼續運作如常。 
  * 指定 ` mustRunAsNonRoot:true ` 的 Pod 不會以 UID 0 的身分啟動，但受到這個問題影響時會無法啟動。 

#####  該如何解決這個問題？

為叢集中不應以 UID 0 身分執行的所有 Pod，設定 [ RunAsUser 安全情境
](https://kubernetes.io/docs/tasks/configure-pod-container/security-
context/#set-the-security-context-for-a-pod) 。您可以使用 [ PodSecurityPolicy
](https://kubernetes.io/docs/concepts/policy/pod-security-policy/) 套用這項設定。

|  中  |  [ CVE-2019-11245 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2019-11245)  
  
##  2019 年 5 月 14 日

說明  |  嚴重性  |  附註  
---|---|---  
  
**2019 年 6 月 11 日更新：** 2019 年 5 月 28 日當週發行的
1.11.10-gke.4、1.12.8-gke.6、1.13.6-gke.5 及以上版本均含有這個修補程式。

Intel 已揭露下列 CVE：

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

上述 CVE 統稱為「微架構資料取樣」(MDS)。當系統利用微架構狀態來進行推測執行的互動時，這些安全漏洞會使資料有曝光風險。詳情請參閱 [ Intel
公告事項 ](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) 。

**執行 Kubernetes Engine 的主機基礎架構會讓各個客戶工作負載之間彼此隔離。除非您在自己的多用戶群 GKE
叢集中執行不受信任的程式碼，否則就不會受到影響。**

**如果客戶在 Kubernetes Engine 內自己的多用戶群服務中執行不受信任的程式碼，這就會變成特別嚴重的安全漏洞。** 如要在
Kubernetes Engine 中降低這個問題的影響程度，請在您的節點停用超執行緒功能。只有使用多個 CPU 的 Google Kubernetes
Engine (GKE) 節點會受到這些安全漏洞的影響。請注意，n1-standard-1 (GKE 預設值)、g1-small 及 f1-micro VM
僅對訪客環境公開 1 個 vCPU，因此不需要停用超執行緒功能。

下一個 [ 修補程式版本 ](https://cloud.google.com/kubernetes-engine/release-
notes?hl=zh_tw)
會納入啟用清除功能的其他防護機制。我們會透過自動升級功能，依一般升級節奏，在未來幾週內自動將主要執行個體和節點升級至修補的版本。
**然而，僅靠修補程式不足以降低此安全漏洞的風險。請參閱以下的建議做法。**

如果您執行 GKE on prem，依使用的硬體而定，可能會受影響。請參閱 [ Intel 公告事項
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) 。

####  該如何解決這個問題？

**除非您在自己的多用戶群 GKE 叢集內執行不受信任的程式碼，否則您不受影響。**

**針對 Kubernetes Engine 中的節點，建立新節點集區且停用超執行緒功能，並且將您的工作負載重新安排到新的節點。**

請注意，n1-standard-1、g1-small 及 f1-micro VM 只對訪客環境公開 1 個 vCPU，因此不需要停用超執行緒功能。

**警告：**

  * 停用超執行緒功能可能會嚴重影響您的叢集和應用程式效能。在將上述停用設定部署至實際工作環境叢集前，請先確認效能影響是可接受的。 
  * 部署 DaemonSet 即可在 GKE 節點集區層級停用超執行緒功能。不過，部署此 DaemonSet 會導致節點集區中的所有節點同時重新啟動。因此，建議您在叢集中建立新節點集區，部署 DaemonSet 以停用該節點集區的超執行緒功能，然後將工作負載遷移至新的節點集區。 

如要建立停用超執行緒功能的新節點集區：

  1. 在叢集中使用節點標籤 ` cloud.google.com/gke-smt-disabled=true ` 建立一個新的節點集區： 
    
        
    gcloud container node-pools create smt-disabled --cluster=[CLUSTER_NAME] \
        --node-labels=cloud.google.com/gke-smt-disabled=true

  2. 將 DaemonSet 部署到此新節點集區。DaemonSet 只會在具有 ` cloud.google.com/gke-smt-disabled=true ` 標籤的節點上執行。如此會停用超執行緒功能，然後重新啟動節點。 
    
        
    kubectl create -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform/\
    k8s-node-tools/master/disable-smt/gke/disable-smt.yaml

  3. 確認 DaemonSet pod 處於執行狀態。 
    
        
    kubectl get pods --selector=name=disable-smt -n kube-system

您應該會得到類似以下的回覆：

    
        
    NAME                READY     STATUS    RESTARTS   AGE
    
    disable-smt-2xnnc   1/1       Running   0          6m

  4. 請檢查 pod 中的記錄檔是否顯示「SMT has been disabled」(SMT 已停用)。 
    
        
    kubectl logs disable-smt-2xnnc disable-smt -n kube-system

附註：如果節點已啟用 [ 安全啟動 ](https://cloud.google.com/kubernetes-engine/docs/how-
to/shielded-gke-nodes?hl=zh_tw#secure_boot) 功能，則無法修改開機選項。如果安全啟動功能已啟用，則必須先將該功能
[ 停用 ](https://cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-
nodes?hl=zh_tw#disabling) ，才能建立 DaemonSet。

您必須讓 DaemonSet
在節點集區中持續運作，如此在集區建立新節點時才會自動套用變更。而節點自動修復、手動或自動升級，以及自動調整資源配置等事件，都可能導致集區內建立節點。

如要重新啟用超執行緒功能，您必須重新建立節點集區，但不去部署現有的 DaemonSet，並將工作負載遷移至新的節點集區。

另外建議您在修補程式發布後立即手動升級節點。如要進行升級，您必須先 [ 將主要執行個體升級
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=zh_tw#upgrading_the_cluster) 至最新版本。GKE 主要執行個體會依一般升級節奏自動升級。

我們會在含修補程式的版本發布後立即更新此公告。

####  這個修補程式修正了什麼安全漏洞？

這個修補程式可有效降低下列安全漏洞的風險：

[ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
、 [ CVE-2018-12127 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2018-12127) 、 [ CVE-2018-12130
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130) 、 [
CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)
：這些安全漏洞會濫用推測性執行功能。上述 CVE 統稱為「微架構資料取樣」。當系統利用微架構狀態來進行推測執行的互動時，這些安全漏洞會使資料有曝光風險。
|  中  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  2019 年 4 月 5 日

說明  |  嚴重性  |  附註  
---|---|---  
  
最近安全漏洞 [ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) 和 [ CVE-2019-9901
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) 在 [ Envoy
](https://www.envoyproxy.io/) 中被發現。

[ Istio ](https://istio.io/) 嵌入 Envoy，且這些安全漏洞允許在某些情況下略過 Istio 政策。

如果您啟用 Google Kubernetes Engine (GKE) 上的 Istio，可能會受這些安全漏洞的影響。
**建議您盡快將受影響的叢集升級至最新的修補程式版本，並升級 Istio 補充元件 (操作說明如下)。**

####  該如何解決這個問題？

**由於這些安全漏洞較為嚴重，無論您是否已啟用節點自動升級功能，我們都建議您：**

  1. **在修補程式發布後盡快[ 手動升級 ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=zh_tw) 叢集。 **
  2. **依照[ 補充元件升級說明文件 ](https://istio.io/docs/setup/kubernetes/upgrade/steps/#sidecar-upgrade) 為您的補充元件升級。 **

太平洋夏令時間今天下午 7:00 前會針對所有 GKE 專案發布修補版本。

這個修補程式會在以下 GKE 版本中提供。修補版本發布在 GKE 安全性公告頁面上 (預計是 2019 年 4 月 15 日)
後，根據預設新叢集會使用此修補版本；如果您在這之前建立了新的叢集，則必須為其指定使用此修補版本。已啟用 [ 節點自動升級功能
](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-
upgrades?hl=zh_tw) 及未手動升級的 GKE 客戶，他們的節點會在下一週自動升級至修補版本。

修補版本：

  * 1.10.12-gke.14 
  * 1.11.6-gke.16 
  * 1.11.7-gke.18 
  * 1.11.8-gke.6 
  * 1.12.6-gke.10 
  * 1.13.4-gke.10 

####  這個修補程式修正了什麼安全漏洞？

這個修補程式可有效降低下列安全漏洞的風險：

[ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) 和 [ CVE-2019-9901。
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) 相關詳細資料請參閱 [
Istio 網誌 ](https://istio.io/blog/2019/announcing-1.1.2) 。

|  高  |

  * [ CVE-2019-9900 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900)
  * [ CVE-2019-9901 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)

  
  
##  2019 年 3 月 1 日

說明  |  嚴重性  |  附註  
---|---|---  
  
**2019 年 3 月 22 日更新：** Kubernetes 1.11.8-gke.4、1.13.4-gke.1
及以上版本均含有這個修補程式。1.12 版中尚未提供這個修補程式。您可以從 [ 版本資訊
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=zh_tw#march_19_2019) 中得知該版本是否提供這些修補程式。

我們最近在 Kubernetes 中發現新的阻斷服務安全漏洞 [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) ，允許授權可進行修補要求的使用者編寫惡意的「json-
patch」要求，以過度耗用 Kubernetes API 伺服器中的 CPU 和記憶體，可能降低叢集控制層的可用性。詳情請參閱 [ Kubernetes
公告事項 ](https://groups.google.com/forum/?hl=zh_tw#!topic/kubernetes-
announce/vmUUNkYfG9g) 。 **所有 Google Kubernetes Engine (GKE)
主要執行個體都受到這些安全漏洞的影響。即將提供的修補程式版本會包含此安全漏洞的因應措施。我們會依一般升級節奏，在未來幾週內自動將叢集主要執行個體升級至修補的版本。**

####  該如何解決這個問題？

**您不需要採取任何動作。GKE 主要執行個體會依一般升級節奏自動升級。** 如果您希望更快升級主要執行個體，可以 [ 手動啟動主要執行個體升級
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=zh_tw#upgrading_the_cluster) 。

我們會在含有修補程式的版本發布後立即更新此公告。請注意，只有 1.11 以上版本提供了這個修補程式，1.10 版並未納入。

####  這個修補程式修正了什麼安全漏洞？

這個修補程式可有效降低下列安全漏洞的風險：

安全漏洞 [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) 允許使用者特別編寫「json-
patch」類型的修補程式，這種類型的程式會過度耗用 Kubernetes API 伺服器中的 CPU 資源，這有可能導致叢集控制層的可用性降低。

|  中  |  [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100)  
  
##  2019 年 2 月 11 日 (runc)

說明  |  嚴重性  |  附註  
---|---|---  
  
Open Containers Initiative (OCI) [ 最近發現
](https://groups.google.com/a/opencontainers.org/forum/m/?hl=zh_tw#!topic/dev/Tc1ELm-8oDI)
在 runc 中有新的安全漏洞 [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) ，允許濫用容器逃逸漏洞以獲得主機節點上的 Root 權限。

**您的 Google Kubernetes Engine (GKE) Ubuntu 節點受到這些安全漏洞的影響，建議您參考以下詳細說明，盡快[ 升級
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=zh_tw) 至最新的修補程式版本。 **

####  該如何解決這個問題？

為了將節點升級，您必須先將主要執行個體升級至最新版本。Kubernetes 1.10.12-gke.7、1.11.6-gke.11、1.11.7-gke.4
及 1.12.5-gke.5 以上版本包含了這個修補程式。您可以從 [ 版本資訊
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=zh_tw#february-11-2019) 中得知該版本是否提供這些修補程式。

請注意，只有 GKE 中的 Ubuntu 節點受到影響。執行 COS 的節點不受影響。

請注意，runc 的新版本已增加記憶體用量，如果您設定低記憶體限制 (< 16 MB)，可能需要更新分配給容器的記憶體。

####  這個修補程式修正了什麼安全漏洞？

這個修補程式可有效降低下列安全漏洞的風險：

[ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) 說明 runc 中的安全漏洞，這個安全漏洞將使用者以 exec
形式操作的機率降至最低，允許惡意容器覆寫主機 runc 二進位檔，以藉此在主機節點上執行根層級程式碼。未以 root
執行的容器不受影響。這個安全漏洞的嚴重性為「高」。

|  高  |  [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736)  
  
##  2019 年 2 月 11 日 (Go)

說明  |  嚴重性  |  附註  
---|---|---  
  
**2019 年 2 月 25 日更新：** 如先前的通知內容所述，1.11.7-gke.4 並未提供這個修補程式。如果您現在的版本是
1.11.7，可以考慮：降級至 1.11.6、升級至 1.12，或等待 2019 年 3 月 4 日當週發布的後續 1.11.7 修補程式。

Go 程式設計語言最近發現新的安全漏洞 [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486) ，這是 P-521 和 P-384 橢圓曲線的密碼編譯/橢圓實作中的阻斷服務
(DoS) 安全漏洞。在 Google Kubernetes Engine (GKE) 中，這可能會允許使用者編寫惡意要求，過度耗用 Kubernetes
API 伺服器中的 CPU，而這可能降低叢集控制層的可用性。詳情請參閱 [ Go 程式設計語言公告事項
](https://groups.google.com/forum/?hl=zh_tw#!topic/golang-
announce/mVeX35iXuSw) 。

**所有 Google Kubernetes Engine (GKE) 主要執行個體都受到這些安全漏洞的影響。[ 最新的修補程式版本
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=zh_tw#february-11-2019)
含有此安全漏洞的因應措施。我們會依一般升級節奏，在未來幾週內自動將叢集主要執行個體升級至修補的版本。 **

####  該如何解決這個問題？

**您不需要採取任何動作。GKE 主要執行個體會依一般升級節奏自動升級。** 如果您希望更快升級主要執行個體，可以 [ 手動啟動主要執行個體升級
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=zh_tw#upgrading_the_cluster) 。

GKE 1.10.12-gke.7、1.11.6-gke.11、1.11.7-gke.4 及 1.12.5-gke.5 以上版本包含了這個修補程式。

####  這個修補程式修正了什麼安全漏洞？

這個修補程式可有效降低下列安全漏洞的風險：

CVE-2019-6486 是 P-521 和 P-384 橢圓曲線的密碼編譯/橢圓實作中的安全漏洞。可允許使用者編寫過度耗用 CPU 的輸入內容。

|  高  |  [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486)  
  
##  2018 年 12 月 3 日

說明  |  嚴重性  |  附註  
---|---|---  
  
Kubernetes 最近發現新的安全性漏洞 [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105) ，讓權限相對較低的使用者能略過 Kubelet API
授權，針對叢集中任何節點的 Pod 恣意操作。詳情請參閱 [ Kubernetes 公告事項
](https://groups.google.com/forum/?hl=zh_tw#!topic/kubernetes-
announce/GVllWCg6L88) 。 **這些安全漏洞影響了所有的 Google Kubernetes Engine (GKE)
主要執行個體，我們已將叢集升級到[ 最新的修補程式版本 ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=zh_tw#november-12-2018) 。您不需要採取任何動作。 **

####  該如何解決這個問題？

**您不需要採取任何動作。GKE 主要執行個體已升級。**

GKE 1.9.7-gke.11、1.10.6-gke.11、1.10.7-gke.11、1.10.9-gke.5、1.11.2-gke.18
以上版本包含了這個修補程式。

####  這個修補程式修正了什麼安全漏洞？

這個修補程式可有效降低下列安全漏洞的風險：

安全漏洞 CVE-2018-1002105 讓權限相對較低的使用者能略過 Kubelet API 的授權，這讓使用者有權發出可升級的權限提升要求，並對
Kubelet API 進行任意呼叫。這個安全漏洞在 Kubernetes 中的嚴重性為「重大」。而 GKE
因為實作上某些細項能防堵未經驗證的權限提升路徑，所以這個安全漏洞的嚴重性僅列為「高」。

|  高  |  [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105)  
  
##  2018 年 11 月 13 日

說明  
---  
  
**2018 年 11 月 16 日更新：** 我們已為所有可能受到影響的憑證完成撤銷與輪替作業，因此您無須採取任何進一步行動。

Google 最近在 Calico Container Network Interface (CNI)
外掛程式中發現一個問題。在特定設定中，這個外掛程式會記錄機密資訊。這個問題已列入 Tigera Technical Advisory 的追蹤清單，編號為 [
TTA-2018-001 ](https://www.projectcalico.org/security-bulletins/) 。

  * 執行偵錯層級的記錄工作時，Calico CNI 外掛程式會將 Kubernetes API 的用戶端設定寫入記錄檔。 
  * 如果 CNI 網路設定中已設定「k8s_auth_token」欄位，Calico CNI 會一併將 Kubernetes API 憑證寫入資訊層級的記錄檔。 
  * 另外，系統在執行偵錯層級的記錄工作時，如果服務帳戶憑證已明確設定 (無論是在 Calico 讀取的 Calico 設定檔或 Calico 使用的環境變數中)，Calico 元件 (calico/node、felix、CNI) 都會將這項資訊寫入記錄檔。 

這些憑證具備下列權限：  
      
    
    
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
  
如果 Google Kubernetes Engine 叢集已啟用叢集網路政策和 Stackdriver Logging，就會將 Calico
服務帳戶憑證記錄至 Stackdriver，未啟用網路政策的叢集則不受影響。

我們已部署可遷移 Calico CNI 外掛程式的修正內容，使其僅會記錄警告層級的資訊，並改用新的服務帳戶。我們會在日後推出的版本中部署經過修補的
Calico 程式碼。

在接下來的一週當中，我們會陸續撤銷所有可能受到影響的憑證。撤銷作業完成後，這則公告也會隨之更新， **因此您無須採取任何進一步行動** (相關輪替作業已於
2018 年 11 月 16 日完成)。

如果想要立即輪替這類憑證，請執行以下指令，系統會在幾秒內自動為服務帳戶重新建立新的 Secret：  
  
kubectl get sa --namespace kube-system calico -o template --template '{{(index
.secrets 0).name}}' | xargs kubectl delete secret --namespace kube-system  
---  
  
####  偵測

GKE 會記錄所有對 API 伺服器的存取。如要確認是否有人在 Google Cloud 已知的 IP 範圍外使用 Calico 憑證，請執行以下
Stackdriver 查詢。請注意，這項作業只會傳回從 GCP 網路以外位置發出的呼叫相關記錄，請根據您使用的環境自訂這項查詢。  
  
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
  
##  2018 年 8 月 14 日

說明  |  嚴重性  |  附註  
---|---|---  
  
[ Intel 已揭露 ](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) 下列 CVE：

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) (發生於 [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (發生於作業系統和 [ SMT ](https://en.wikipedia.org/wiki/Hyper-threading) ) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (發生於虛擬化作業) 

上述 CVE 統稱為「L1 終端機錯誤」(L1TF)。

這些 L1TF 安全漏洞會攻擊處理器層級的資料結構設定，藉此濫用推測性執行功能。 「L1」是指 1 級資料快取
(L1D)，這是一種用於加快記憶體存取速度的小型核心資源。

歡迎參閱 [ Google Cloud 網誌文章
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=zh_tw) ，進一步瞭解這些安全漏洞和 Compute Engine 的因應措施。

####  對 Google Kubernetes Engine 的影響

用於執行 Kubernetes Engine 及隔離各個客戶叢集與節點的基礎架構具備充分的防護機制，因此未受到已知攻擊的影響。

使用 Google Container-Optimized OS 映像檔的 Kubernetes Engine 節點集區如果已啟用 [ 自動升級
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=zh_tw) 功能，就會自動更新至修補的 COS 映像檔版本 (2018 年 8 月 20 日當週發布)。

針對未啟用 [ 自動升級 ](https://cloud.google.com/kubernetes-engine/docs/concepts/node-
auto-upgrades?hl=zh_tw) 功能的 Kubernetes Engine 節點集區，您必須等到修補的 COS 映像檔版本發布後再進行 [
手動升級 ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=zh_tw) 。

|  高  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  2018 年 8 月 6 日；最後更新時間：2018 年 9 月 5 日

說明  |  嚴重性  |  附註  
---|---|---  
  
####  2018 年 9 月 5 日更新

我們最近揭露了 [ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ，這個安全漏洞與 [ CVE-2018-5390
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
均屬於核心層級的網路安全漏洞，在針對不安全系統發動阻斷服務 (DoS) 攻擊時，破壞力更強。兩者的主要差異在於不肖人士可以透過 IP 連線利用
CVE-2018-5391。我們已更新這則公告，以補充這兩個安全漏洞的相關資訊。

####  說明

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) (或稱為「SegmentSmack」) 屬於核心層級的網路安全漏洞，透過 TCP
連線對不安全系統發動阻斷服務 (DoS) 攻擊時，可以造成更大的殺傷力。

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) (或稱為「FragmentSmack」) 屬於核心層級的網路安全漏洞，透過 IP
連線對不安全系統進行阻斷服務 (DoS) 攻擊時，破壞力更強。

####  對 Google Kubernetes Engine 的影響

截至 2018 年 8 月 11 日，所有 Kubernetes Engine
主要執行個體皆已採用最新的防護機制，因此未受到這兩個安全漏洞的影響。另外，已啟用自動升級功能的 Kubernetes Engine
叢集也未受到這兩個安全漏洞的影響。如果您的 Kubernetes Engine 節點集區未啟用 [ 自動升級
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=zh_tw) 功能，且上次手動升級時間早於 2018 年 8 月 11 日，則會受到這兩個安全漏洞的影響。

####  修補版本

由於這個安全漏洞較為嚴重，建議您在修補程式發布後立即 [ 手動升級 ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=zh_tw#upgrading-nodes) 節點。

|  高  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  2018 年 5 月 30 日

說明  |  嚴重性  |  附註  
---|---|---  
  
我們最近在 Git 中發現一個安全漏洞。如果您允許未經授權的使用者透過 gitRepo 磁碟區建立 Pod，這個安全漏洞可能會允許升級 Kubernetes
權限。我們已發現這個 CVE，其標記為 [ CVE-2018-11235 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-11235) 。

####  我會受到影響嗎？

如果您符合以下所有條件，這個安全漏洞就會對您造成影響：

  * 未受信任的使用者可以建立 Pod (或觸發 Pod 建立作業)。 
  * 在防範主機的根存取要求方面，未受信任使用者建立的 Pod 會受到限制 (例如透過 [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=zh_tw) 加以限制)。 
  * 未受信任使用者建立的 Pod 可以使用 gitRepo 磁碟區類型。 

所有 Kubernetes Engine 節點均會受到這個安全漏洞的影響。

####  該如何解決這個問題？

禁止使用 gitRepo 磁碟區類型。如要透過 PodSecurityPolicy 禁止任何人使用 gitRepo 磁碟區，請在
PodSecurityPolicy 的 ` volumes ` 許可清單中省略 ` gitRepo ` 。

如果想將禁止使用 gitRepo 磁碟區的行為套用至其他存放區，您可以透過 initContainer 將 Git 存放區複製到 EmptyDir
磁碟區中：

    
    
    
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

####  解決這個安全漏洞的修補程式為何？

我們會在即將推出的 Kubernetes Engine 版本中發布修補程式。如需相關詳情，日後請持續鎖定這個頁面。

|  中  |

  * [ CVE-2018-11235 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11235)

  
  
##  2018 年 5 月 21 日

說明  |  嚴重性  |  附註  
---|---|---  
  
我們最近在 Linux 核心中發現多個安全漏洞，這些安全漏洞可能會允許以未經授權程序升級權限，或是觸發核心當機而阻斷服務。我們已知悉這些
CVE，其標記分別為 [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) 、 [ CVE-2018-8897
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897) 及 [
CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)
。 所有 Kubernetes Engine 節點均會受到這些安全漏洞的影響，建議您按照下列步驟操作，以 [ 升級
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=zh_tw) 至最新修補程式版本。

####  該如何解決這個問題？

如要進行升級，您必須先將主要執行個體升級至最新版本。這個修補程式將會在 Kubernetes Engine 1.8.12-gke.1、Kubernetes
Engine 1.9.7-gke.1 和 Kubernetes Engine 1.10.2-gke.1 中發布，以上版本均含有適用於 Container-
Optimized OS 和 Ubuntu 映像檔的修補程式。

如果您在修補程式發布前即已建立新的叢集，請務必指定叢集要使用的修補版本。如果是已啟用 [ 節點自動升級
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=zh_tw) 功能，且並沒有進行手動升級的客戶，其節點會在未來幾週內升級至修補版本。

####  這個修補程式修正了哪些安全漏洞？

這個修補程式可有效降低下列安全漏洞的風險：

[ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) ：這個安全漏洞會影響 Linux
核心，允許未經授權的使用者或程序觸發系統核心當機，進而招致 DoS 攻擊或造成權限升級。這個安全漏洞的嚴重性為「高」，CVSS 為 7.8。

[ CVE-2018-8897 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-8897) ：這個安全漏洞會影響 Linux
核心，允許未經授權的使用者或程序觸發系統核心當機，進而招致 DoS 攻擊。這個安全漏洞的嚴重性為「中」，CVSS 為 6.5。

[ CVE-2018-1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) ：這個安全漏洞會影響 Linux 核心的 KVM
管理程序，允許未經授權的程序觸發訪客核心當機，甚至還可能授予權限。Kubernetes Engine 的執行基礎架構已修補了這個安全漏洞，因此
Kubernetes Engine 未受影響。這個安全漏洞的嚴重性為「高」，CVSS 為 8.0。

|  高  |

  * [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199)
  * [ CVE-2018-8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
  * [ CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)

  
  
##  2018 年 3 月 12 日

說明  |  嚴重性  |  附註  
---|---|---  
  
Kubernetes 專案 [ 最近揭露
](https://groups.google.com/forum/?hl=zh_tw#!topic/kubernetes-security-
announce/P7lBjbjDKd8) 了新的安全漏洞，標記分別為 [ CVE-2017-1002101
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101) 和 [
CVE-2017-1002102 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2017-1002102) 。這兩個安全漏洞會允許容器存取位於該容器以外的檔案。所有 Kubernetes
Engine 節點均會受到這些安全漏洞的影響，建議您盡快按照下列步驟操作，以升級至最新修補程式版本。

####  該如何解決這個問題？

由於這些安全漏洞較為嚴重，無論您是否已啟用節點自動升級功能，我們都建議您在修補程式發布後立即 [ 手動升級
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=zh_tw) 節點。我們會在 3 月 16
日之前向所有客戶推出修補程式，但視您的叢集所在區域而定，實際發布時間可能較早。詳情請參閱 [ 發布時間表
](https://cloud.google.com/kubernetes-engine/docs/release-
notes?hl=zh_tw#march-12-2018) 。

如要進行升級，您必須先將主要執行個體升級至最新版本。Kubernetes 1.9.4-gke.1、Kubernetes 1.8.9-gke.1 和
Kubernetes 1.7.14-gke.1 版本均包含了這個修補程式。在 3 月 30
日，新的叢集將依預設使用修補的版本。如果您在此之前即已建立新的叢集，則必須指定叢集要使用的修補版本。

如果您是已啟用 [ 節點自動升級 ](https://cloud.google.com/kubernetes-
engine/docs/concepts/node-auto-upgrades?hl=zh_tw) 功能，以及尚未進行手動升級的 Kubernetes
Engine 客戶，系統會在 4 月 23 日統一將節點升級至修補版本。不過考量到這些安全漏洞的性質，建議您還是在修補程式發布後，立即 [ 手動升級
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=zh_tw) 節點。

####  這個修補程式修正了哪些安全漏洞？

這個修補程式可有效降低下列兩個安全漏洞的風險：

CVE-2017-1002101：這個安全漏洞會允許容器透過 [ 子路徑
](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath)
磁碟區掛接項目，存取位於該磁碟區以外的檔案。也就是說，如果您是透過 PodSecurityPolicy 禁止容器存取主機路徑的磁碟區，可更新或建立 pod
的攻擊者就能透過其他磁碟區類型掛接任何主機路徑。

CVE-2017-1002102：這個安全漏洞會允許使用特定磁碟區類型 (包括 Secret、Config Map、Projected 磁碟區或
Downward API 磁碟區) 的容器刪除位於該磁碟區以外的檔案。也就是說，如果使用前述任一磁碟區類型的容器遭到入侵，或是您允許未受信任的使用者建立
pod，攻擊者就能利用該容器來刪除主機上的任何檔案。

如要進一步瞭解解決方式，請參閱 [ Kubernetes 網誌文章
](https://kubernetes.io/blog/2018/04/04/fixing-subpath-volume-vulnerability/)
。

|  高  |

  * [ CVE-2017-1002101 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101)
  * [ CVE-2017-1002102 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102)

