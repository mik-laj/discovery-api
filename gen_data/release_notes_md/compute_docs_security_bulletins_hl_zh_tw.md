#  安全性公告

我們會不定期發布與 Compute Engine 相關的安全性公告，您可以在這裡找到所有 Compute Engine 安全性公告的相關說明。

[ 訂閱 Compute Engine 安全性公告。 ![訂閱](https://cloud.google.com/images/feed-
icon.png?hl=zh_tw) ](https://cloud.google.com/feeds/compute-engine-security-
bulletins.xml?hl=zh_tw)

##  發布日期：2019 年 6 月 18 日

**上次更新時間：太平洋標準時間 2019 年 6 月 25 日 6:30**

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

Netflix 最近揭露了 Linux 核心的 3 個 TCP 安全漏洞：

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

上述 CVE 統稱為 [ NFLX-2019-001 ](https://github.com/Netflix/security-
bulletins/blob/master/advisories/third-party/2019-001.md) 。

####  對 Compute Engine 的影響

託管 Compute Engine 的基礎架構具備防護機制，因此不會受到這個安全漏洞的影響。

如果 Compute Engine VM 執行未經修補的 Linux 作業系統，且該作業系統會傳送/接收不受信任的網路流量，這個 VM 就可能會受到這類
DoS 攻擊。因此，我們建議您在該作業系統的修補程式推出時，立即更新這些 VM 執行個體。

我們已針對這個安全漏洞修補會終止 TCP 連線的負載平衡器。如果 Compute Engine
執行個體只透過這些負載平衡器接收不受信任流量，則沒有安全漏洞。這些負載平衡器包括 HTTP 負載平衡器、安全資料傳輸層 (SSL) Proxy
負載平衡器，以及 TCP Proxy 負載平衡器。

網路負載平衡器和內部負載平衡器不會終止 TCP 連線。如果是未經修補的 Compute Engine
執行個體，且會透過這些負載平衡器接收不受信任流量，則有安全漏洞。

####  修補完成的映像檔與廠商資源

當每個作業系統廠商發布修補程式資訊時，我們就會在這裡提供相關連結，包括每個 CVE
的狀態。這些公開映像檔的較舊版本並未包含這些修補程式，因此無法緩解潛在的攻擊活動：

  * ` debian-cloud ` 專案： 
    * ` debian-9-stretch-v20190618 `
  * ` centos-cloud ` 專案： 
    * ` centos-6-v20190619 `
    * ` centos-7-v20190619 `
  * ` cos-cloud ` 專案： 
    * ` cos-dev-77-12293-0-0 `
    * ` cos-beta-76-12239-21-0 `
    * ` cos-stable-75-12105-77-0 `
    * ` cos-73-11647-217-0 `
    * ` cos-69-10895-277-0 `
  * ` coreos-cloud ` 專案： 
    * ` coreos-alpha-2163-2-1-v20190617 `
    * ` coreos-beta-2135-3-1-v20190617 `
    * ` coreos-stable-2079-6-0-v20190617 `
  * ` rhel-cloud ` 專案： 
    * ` rhel-6-v20190618 `
    * ` rhel-7-v20190618 `
    * ` rhel-8-v20190618 `
  * ` rhel-sap-cloud ` 專案： 
    * ` rhel-7-4-sap-v20190618 `
    * ` rhel-7-6-sap-v20190618 `
  * ` suse-cloud ` 專案： 
    * ` sles-12-sp4-v20190617 `
    * ` sles-15-v20190617 `
  * ` suse-sap-cloud ` 專案： 
    * ` sles-12-sp1-sap-v20190617 `
    * ` sles-12-sp2-sap-v20190617 `
    * ` sles-12-sp3-sap-v20190617 `
    * ` sles-12-sp4-sap-v20190617 `
    * ` sles-15-sap-v20190617 `
  * ` ubuntu-cloud ` 專案： 
    * ` ubuntu-1604-xenial-v20190617 `
    * ` ubuntu-1804-bionic-v20190617 `
    * ` ubuntu-1810-cosmic-v20190618 `
    * ` ubuntu-1904-disco-v20190619 `
    * ` ubuntu-minimal-1604-xenial-v20190618 `
    * ` ubuntu-minimal-1804-bionic-v20190617 `
    * ` ubuntu-minimal-1810-cosmic-v20190618 `
    * ` ubuntu-minimal-1904-disco-v20190618 `

|  中  |

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

  
  
##  發布日期：2019 年 5 月 14 日

**上次更新時間：太平洋標準時間 2019 年 5 月 20 日 17:00**

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

Intel 已揭露下列 CVE：

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

上述 CVE 統稱為「微架構資料取樣」(MDS)。當系統利用微架構狀態來進行推測執行的互動時，這些安全漏洞會使資料有曝光風險。

####  對 Compute Engine 的影響

**執行 Compute Engine 的主機基礎架構會讓各個客戶工作負載之間彼此隔離。除非您在 VM
中執行不受信任的程式碼，否則就不必採取進一步的行動。**

如果客戶在 Compute Engine 虛擬機器中自己的多用戶群服務上執行不受信任的程式碼，請參考您客體 OS 廠商建議的緩解方法，其中可能包含使用
Intel 的微碼緩解功能。我們已經為新的清除功能部署訪客傳遞存取權。以下概述適用於一般訪客映像檔的緩解步驟。

####  修補完成的映像檔與廠商資源

當每個作業系統廠商發布修補程式資訊時，我們就會在這裡提供相關連結，包括每個 CVE 的狀態。請使用這些映像檔來重新建立 VM
執行個體。這些公開映像檔的較舊版本並未包含這些修補程式，因此無法緩解潛在的攻擊活動：

  * ` centos-cloud ` 專案： [ CESA-2019:1169 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023309.html) 、 [ CESA-2019:1168 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023314.html)
    * ` centos-6-v20190515 `
    * ` centos-7-v20190515 `
  * ` coreos-cloud ` 專案： [ 適用於 CoreOS Container Linux 的 MDS 緩解方法 ](https://coreos.com/os/docs/latest/disabling-smt.html)
    * ` coreos-stable-2079-4-0-v20190515 `
    * ` coreos-beta-2107-3-0-v20190515 `
    * ` coreos-alpha-2135-1-0-v20190515 `
  * ` cos-cloud ` 專案 
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
  * ` debian-cloud ` 專案： [ DSA-4444 ](https://www.debian.org/security/2019/dsa-4444)
    * ` debian-9-stretch-v20190514 `
  * ` rhel-cloud ` 專案： [ Red Hat MDS 知識庫文章 ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-6-v20190515 `
    * ` rhel-7-v20190517 `
    * ` rhel-8-v20190515 `
  * ` rhel-sap-cloud ` 專案： [ Red Hat MDS 知識庫文章 ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-7-4-sap-v20190515 `
    * ` rhel-7-6-sap-v20190517 `
  * ` suse-cloud ` 專案： [ SUSE MDS 知識庫 ](https://www.suse.com/support/kb/doc/?id=7023736)
    * ` sles-12-sp4-v20190520 `
    * ` sles-15-v20190520 `
  * ` suse-sap-cloud ` 專案 
    * ` sles-12-sp4-sap-v20190520 `
    * ` sles-15-sap-v20190520 `
  * ` ubuntu-os-cloud ` 專案： [ Ubuntu MDS Wiki ](https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/MDS)
    * ` ubuntu-1404-trusty-v20190514 `
    * ` ubuntu-1604-xenial-v20190514 `
    * ` ubuntu-1804-bionic-v20190514 `
    * ` ubuntu-1810-cosmic-v20190514 `
    * ` ubuntu-1904-disco-v20190514 `
    * ` ubuntu-minimal-1604-xenial-v20190514 `
    * ` ubuntu-minimal-1804-bionic-v20190514 `
    * ` ubuntu-minimal-1810-cosmic-v20190514 `
    * ` ubuntu-minimal-1904-disco-v20190514 `
  * ` windows-cloud ` 和 ` windows-sql-cloud ` 專案： [ Microsoft ADV190013 ](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/ADV190013)
    * 所有版本編號為 ` v20190514 ` 的 Windows Server 和 SQL Server 公開映像檔。 
  * ` gce-uefi-images ` 專案 
    * ` centos-7-v20190515 `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
    * ` rhel-7-v20190517 `
    * ` ubuntu-1804-bionic-v20190514 `
    * 所有版本編號為 ` v20190514 ` 的 Windows Server 公開映像檔。 

####  Container-Optimized OS

如果您把 Container Optimized OS (COS) 當做客體 Guest OS
來使用，且您在自己的虛擬機器上執行不受信任的多用戶群工作負載，我們建議您：

  1. 停用超執行緒功能，方法是在核心指令列上設定 ` nosmt ` 。   

請在現有的 COS VM 上，依照以下內容來修改 ` grub.cfg ` ，以便設定 ` nosmt ` 選項並讓系統重新啟動：

    
        
    # Run as root:
    dir="$(mktemp -d)"
    mount /dev/sda12 "${dir}"
    sed -i -e "s|cros_efi|cros_efi nosmt|g" "${dir}/efi/boot/grub.cfg"
    umount "${dir}"
    rmdir "${dir}"
    
    reboot

為方便起見，您只要執行下列指令碼就能達到執行上述指令的效果。我們建議您把該指令碼新增到您的雲端組態、開機指令碼，或執行個體範本中，以確保新的 VM
會使用這個參數。以下是會執行該指令碼的雲端組態範例。

**警告：** 這個指令會讓第一次執行該指令的執行個體立刻重新啟動。之後您在已停用超執行緒功能的執行個體上再次執行該指令時，就不會有任何效果。

    
        
    # Run as root
    /bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)
    

如何將該指令新增到您的雲端組態中：

    
        
    #cloud-config
    
    bootcmd:
    - /bin/bash -c "/bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)"
    

如要確認執行個體的超執行緒功能是否已停用，請查看 ` /sys/devices/system/cpu/smt/active ` 和 `
/sys/devices/system/cpu/smt/control ` 檔案的輸出內容。如果您看到 ` active ` 為 ` 0 ` ，且 `
control ` 為 ` off ` ，即代表超執行緒功能已停用：

    
        
    cat /sys/devices/system/cpu/smt/active
    cat /sys/devices/system/cpu/smt/control
    

**注意：** 如果您已經啟用執行個體上的 UEFI 安全啟動功能，就必須要在 UEFI 安全啟動功能停用的情況下重新建立執行個體、在 UEFI
安全啟動功能停用的情況下執行上述指令，然後啟用新執行個體上的 UEFI 安全啟動功能。

  2. 使用新版本的 COS 映像檔   

除了採用上述方法來停用超執行緒功能之外，您也應該利用上述已更新或較新版本 (如果已推出) 的 Container-Optimized OS 映像檔來 [
重新建立執行個體 ](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=zh_tw#publicimage) ，以便獲得可抵擋該安全漏洞的完整保護。

|  中  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  發布日期：2018 年 8 月 14 日

**上次更新時間：太平洋標準時間 2018 年 8 月 20 日 17:00**

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

[ Intel 已揭露 ](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) 下列 CVE：

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) (發生於 [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (發生於作業系統和 [ SMT ](https://en.wikipedia.org/wiki/Hyper-Threading) ) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (發生於虛擬化作業) 

上述 CVE 統稱為「L1 終端機錯誤」(L1TF)。

這些 L1TF 安全漏洞會攻擊處理器層級資料結構的設定，藉此利用推測執行攻擊。「L1」是指 1 級資料快取
(L1D)，這是一種用於加快記憶體存取速度的小型核心資源。

歡迎參閱 [ Google Cloud 網誌文章
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=zh_tw) ，進一步瞭解這些安全漏洞和 Compute Engine 的解決方法。

####  對 Compute Engine 的影響

用於執行 Compute Engine 及隔離各個客戶工作負載的主機基礎架構具備充分的防護機制，因此未受到已知攻擊的影響。

我們建議 Compute Engine 的客戶更新映像檔，以免訪客環境中出現間接的惡意利用活動。對於在 Compute Engine
虛擬機器上執行多用戶群服務的客戶來說，這一點尤為重要。

Google Compute Engine 的客戶可以透過下列其中一種方法更新執行個體上的訪客作業系統：

  * 使用修補完成的公開映像檔 [ 重新建立現有的 VM 執行個體 ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=zh_tw#publicimage) 。 
  * 在現有的執行個體上安裝由作業系統廠商提供的修補程式，並重新啟動經過修補的執行個體。 

####  修補完成的映像檔與廠商資源

作業系統廠商發布修補程式資訊之後，我們就會在這裡提供相關連結和前述兩個 CVE 的狀態。您可以使用這些映像檔來重新建立 VM
執行個體。這些公開映像檔的舊有版本未包含這些修補程式，因此無法防範潛在的攻擊活動：

  * ` centos-cloud ` 專案： 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * ` coreos-cloud ` 專案： 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * ` cos-cloud ` 專案： 
    * ` cos-stable-66-10452-110-0 `
    * ` cos-stable-67-10575-66-0 `
    * ` cos-beta-68-10718-81-0 `
    * ` cos-dev-69-10895-23-0 `
  * ` debian-cloud ` 專案： 
    * ` debian-9-stretch-v20180820 `
  * ` rhel-cloud ` 專案： 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * ` rhel-sap-cloud ` 專案： 
    * ` rhel-7-sap-apps-v20180814 `
    * ` rhel-7-sap-hana-v20180814 `
  * ` suse-cloud ` 專案： 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
    * ` sles-11-sp4-v20180816 `
  * ` suse-sap-cloud ` 專案： 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * ` ubuntu-os-cloud ` 專案： 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `
  * ` windows-cloud ` ` gce-uefi-images ` 和 ` windows-sql-cloud ` 專案： 
    * 所有版本編號為 ` -v201800814 ` 及較新版本的 Windows Server 和 SQL Server [ 公開映像檔 ](https://cloud.google.com/compute/docs/images?hl=zh_tw#os-compute-support) 都包含修補程式。 

|  高  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  發布日期：2018 年 8 月 6 日

**上次更新時間：太平洋標準時間 2018 年 9 月 5 日 17:00**

說明  |  嚴重性  |  附註  
---|---|---  
  
####  2018 年 9 月 5 日更新

US-CERT 於 2018 年 8 月 14 日揭露 [ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) 。這個安全漏洞與 [ CVE-2018-5390
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
均為核心層級的網路安全漏洞，會提高針對不安全系統進行的阻斷服務 (DoS) 攻擊效率。兩者的主要差異在於不肖人士可以透過 IP 連線利用
CVE-2018-5391。我們已更新這則公告，以補充這兩個安全漏洞的相關資訊。

####  說明

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) (或稱為「SegmentSmack」) 屬於核心層級的網路安全漏洞，可透過 TCP
連線提高針對不安全系統進行的阻斷服務 (DoS) 攻擊效率。

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) (或稱為「FragmentSmack」) 屬於核心層級的網路安全漏洞，可透過 IP
連線提高針對不安全系統進行的阻斷服務 (DoS) 攻擊效率。

####  對 Compute Engine 的影響

執行 Compute Engine VM 的主機基礎架構並未受到影響。處理 Compute Engine VM
傳入與傳出流量的網路基礎架構具備充分的防護機制，因此未受到這個安全漏洞的影響。只會透過 [ HTTP(S)
](https://cloud.google.com/load-balancing/docs/https/?hl=zh_tw) 、 [ SSL
](https://cloud.google.com/load-balancing/docs/ssl/?hl=zh_tw) 或 [ TCP 負載平衡器
](https://cloud.google.com/load-balancing/docs/tcp/?hl=zh_tw) 傳送/接收不受信任網路流量的
Compute Engine VM 已得到保護，不會受到這個安全漏洞的影響。

如果 Compute Engine VM 執行未經修補的作業系統，且該作業系統會直接或透過 [ 網路負載平衡器
](https://cloud.google.com/load-balancing/docs/network/?hl=zh_tw)
傳送/接收不受信任的網路流量，這個 VM 就可能受到這類 DoS 攻擊的影響。

VM 執行個體的作業系統廠商發布修補程式之後，建議您立即進行更新。

Compute Engine 的客戶可以透過下列其中一種方法更新執行個體上的訪客作業系統：

  * 使用修補完成的公開映像檔 [ 重新建立現有的 VM 執行個體 ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=zh_tw#publicimage) 。請參閱下方的已修補公開映像檔清單。 
  * 在現有的執行個體上安裝由作業系統廠商提供的修補程式，並重新啟動經過修補的執行個體。 

####  修補完成的映像檔與廠商資源

當每個作業系統廠商發布修補程式資訊時，我們就會在這裡提供相關連結。

  * ` centos-cloud ` 專案 (僅限 CVE-2018-5390)： 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * ` coreos-cloud ` 專案 (CVE-2018-5390 和 CVE-2018-5391)： 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * ` cos-cloud ` 專案 (CVE-2018-5390 和 CVE-2018-5391)： 
    * ` cos-stable-65-10323-98-0 `
    * ` cos-stable-66-10452-109-0 `
    * ` cos-stable-67-10575-65-0 `
    * ` cos-beta-68-10718-76-0 `
    * ` cos-dev-69-10895-16-0 `
  * ` debian-cloud ` 專案 (CVE-2018-5390 和 CVE-2018-5391)： 
    * ` debian-9-stretch-v20180814 `
  * ` rhel-cloud ` 專案 (僅限 CVE-2018-5390)： 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * ` suse-cloud ` 專案 (CVE-2018-5390 和 CVE-2018-5391)： 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
  * ` suse-sap-cloud ` 專案 (CVE-2018-5390 和 CVE-2018-5391)： 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * ` ubuntu-os-cloud ` 專案 (CVE-2018-5390 和 CVE-2018-5391)： 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `

|  高  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  發布日期：2018 年 1 月 3 日

**上次更新時間：太平洋標準時間 2018 年 5 月 21 日 15:00**

說明  |  嚴重性  |  附註  
---|---|---  
  
####  2018 年 5 月 21 日更新

[ Intel 已經揭露 ](https://www.intel.com/content/www/us/en/security-
center/advisory/intel-sa-00115.html) [ CVE-2018-3640
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3640) 和 [
CVE-2018-3639 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639)
(分別為變種 3a 和變種 4)。與 Spectre 和 Meltdown 前三個變種的情況相同，執行 Compute Engine VM
執行個體的基礎架構具備充分的防護機制，因此未受到這個安全漏洞的影響。由於客戶 VM 執行個體彼此隔離，亦未受影響。另外，Compute Engine 預計將
Intel 的微碼修補程式部署至自有基礎架構。作業系統廠商與供應商提供可於 VM 內部執行的解決方法之後，在單一 VM
執行個體中處理不受信任或多用戶群工作負載的客戶即可啟用這類額外的解決方法。這些微碼修補程式必須通過 Intel 認證，並由 Compute Engine
在實際工作環境中進行測試及驗證後，Compute Engine 才會加以部署。修補程式發布之後，我們會在這個頁面中提供更詳細的時程表與相關最新消息。

####  說明

這些 CVE 屬於新型攻擊的變種，會利用多種處理器中的推測執行技術。發動這類攻擊之後，未獲授權的使用者就能在多種情況下取得記憶體資料的唯讀存取權。

Compute Engine 使用 VM
即時遷移技術來執行主機系統和管理程序更新，因此您無須指派任何人加以管理，也不需要進行強制性維護作業或大規模重新啟動執行個體。不過請注意，無論訪客作業系統是在何種環境中運作，這類作業系統和版本都必須經過修補，否則可能會受到這種新型攻擊的威脅。

如要全面瞭解這種攻擊方法的相關技術資訊，請參閱 [ Project Zero 網誌文章
](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-
with-side.html) 。如想取得 Google 解決方法的完整詳細資訊 (包括所有產品專用資訊)，則請參閱 [ Google 安全性網誌文章
](https://security.googleblog.com/2018/01/todays-cpu-vulnerability-what-you-
need.html) 。

####  對 Compute Engine 的影響

用於執行 Compute Engine 及隔離各個客戶 VM
執行個體的基礎架構具備充分的防護機制，因此未受到已知攻擊的影響。部署我們的解決方法之後，您就能預防不肖人士未經授權即透過 VM
執行個體中運作的應用程式存取主機系統，執行相同主機系統的其他 VM 執行個體也不會遭到未經授權的存取。

如要避免虛擬機器執行個體中發生未經授權的存取活動，您必須透過下列其中一種方法更新這些執行個體上的訪客作業系統：

  * 使用經過修補的公開映像檔 [ 重新建立現有的 VM 執行個體 ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=zh_tw#publicimage) 。請參閱下方的已修補公開映像檔清單。 
  * 在現有的執行個體上安裝由作業系統廠商提供的修補程式，並重新啟動經過修補的執行個體。各家作業系統廠商已提供相關的修補程式資訊，請見下方連結。 

####  修補完成的映像檔與廠商資源

**注意事項：** 這則安全性公告通知列出了多項
CVE，但修補完成的映像檔中可能未含所有安全漏洞的修正內容。另外，不同映像檔中提供的攻擊防護方法可能不同。請與您的作業系統廠商聯絡，確認對方在修補程式中解決的
CVE 為何，並瞭解他們採用何種防護方法。

  * ` cos-cloud ` 專案：包含可防範變種 2 ( [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715) ) 和變種 3 ( [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754) ) 攻擊的修補程式。在這些映像檔中，Google 是採用 [ Retpoline ](https://support.google.com/faqs/answer/7625886?hl=zh_tw) 來防範變種 2 的攻擊活動。 
    * ` cos-stable-63-10032-71-0 ` 或 ` cos-stable ` 映像檔系列 
  * ` centos-cloud ` 專案： [ CentOS 修補程式資訊 ](https://lwn.net/Alerts/CentOS/)
    * ` centos-7-v20180104 ` 或 ` centos-7 ` 映像檔系列 
    * ` centos-6-v20180104 ` 或 ` centos-6 ` 映像檔系列 
  * ` coreos-cloud ` 專案： [ CoreOS 修補程式資訊 ](https://coreos.com/blog/container-linux-meltdown-patch)
    * ` coreos-stable-1576-5-0-v20180105 ` 或 ` coreos-stable ` 映像檔系列 
    * ` coreos-beta-1632-1-0-v20180105 ` 或 ` coreos-beta ` 映像檔系列 
    * ` coreos-alpha-1649-0-0-v20180105 ` 或 ` coreos-alpha ` 映像檔系列 
  * ` debian-cloud ` 專案： [ Debian 修補程式資訊 ](https://www.debian.org/security/#DSAS)
    * ` debian-9-stretch-v20180105 ` 或 ` debian-9 ` 映像檔系列 
    * ` debian-8-jessie-v20180109 ` 或 ` debian-8 ` 映像檔系列 
  * ` rhel-cloud ` 專案： [ RHEL 修補程式資訊 ](https://access.redhat.com/security/vulnerabilities/speculativeexecution)
    * ` rhel-7-v20180104 ` 或 ` rhel-7 ` 映像檔系列 
    * ` rhel-6-v20180104 ` 或 ` rhel-6 ` 映像檔系列 
  * ` suse-cloud ` 專案： [ SUSE 修補程式資訊 ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-v20180104 ` 或 ` sles-12 ` 映像檔系列 
    * ` sles-11-sp4-v20180104 ` 或 ` sles-11 ` 映像檔系列 
  * ` suse-sap-cloud ` 專案： [ SUSE 修補程式資訊 ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-sap-v20180104 ` 或 ` sles-12-sp3-sap ` 映像檔系列 
    * ` sles-12-sp2-sap-v20180104 ` 或 ` sles-12-sp2-sap ` 映像檔系列 
  * ` ubuntu-os-cloud ` 專案： [ Ubuntu 修補程式資訊 ](https://insights.ubuntu.com/2018/01/04/ubuntu-updates-for-the-meltdown-spectre-vulnerabilities/)
    * ` ubuntu-1710-artful-v20180109 ` 或 ` ubuntu-1710 ` 映像檔系列 
    * ` ubuntu-1604-xenial-v20180109 ` 或 ` ubuntu-1604-lts ` 映像檔系列 
    * ` ubuntu-1404-trusty-v20180110 ` 或 ` ubuntu-1404-lts ` 映像檔系列 
  * ` windows-cloud ` 和 ` windows-sql-cloud ` 專案： 
    * 所有版本編號為 ` -v20180109 ` 及較新版本的 Windows Server 和 SQL Server [ 公開映像檔 ](https://cloud.google.com/compute/docs/images?hl=zh_tw#os-compute-support) 都包含修補程式。不過，您必須按照 Microsoft 在 [ Windows Server 指引 ](https://support.microsoft.com/en-gb/help/4072698/windows-server-guidance-to-protect-against-the-speculative-execution) 支援公告中提供的建議步驟，在現有和新建立的執行個體上啟用並驗證這些解決方法。 

您可以使用這些映像檔來 [ 重新建立 VM 執行個體
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=zh_tw#publicimage) 。這些公開映像檔的舊有版本未包含這些修補程式，因此無法防範潛在的攻擊活動。

####  硬體廠商提供的修補程式

NVIDIA 提供經過修補的驅動程式，可防範針對已安裝 NVIDIA® 驅動程式軟體的系統進行的潛在攻擊。如想瞭解哪些驅動程式版本已修補完成，請參閱
NVIDIA 的 [ NVIDIA GPU 顯示器驅動程式安全性更新
](http://nvidia.custhelp.com/app/answers/detail/a_id/4611) 相關公告。

####  修訂版本記錄：

  * 2018 年 5 月 21 日 14:00 (太平洋標準時間)：新增 2018 年 5 月 21 日揭露的 2 個新型變種相關資訊。 
  * 2018 年 1 月 10 日 15:00 (太平洋標準時間)：新增修補完成的 Windows Server 和 SQL Server 公開映像檔相關資訊。 
  * 2018 年 1 月 10 日 10:15 (太平洋標準時間)：將多個 Ubuntu 映像檔新增至已修補公開映像檔清單。 
  * 2018 年 1 月 10 日 09:50 (太平洋標準時間)：新增硬體廠商提供的修補程式相關指南。 
  * 2018 年 1 月 3 日至 2018 年 1 月 9 日：多次修改已修補公開映像檔清單的內容。 

|  高  |

  * [ CVE-2017-5753 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5753)
  * [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715)
  * [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754)
  * [ CVE-2018-3640 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3640)
  * [ CVE-2018-3639 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639)

  
  
##  發布日期：2017 年 10 月 2 日

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

[ Dnsmasq ](http://www.thekelleys.org.uk/dnsmasq/doc.html) 提供
DNS、DHCP、路由器通告和網路開機服務。這個軟體通常安裝在桌機版本的 Linux (如 Ubuntu)、家用路由器和 IoT
裝置等各種系統中，並且廣泛使用於開放式網路和內部私人網絡。

Google
在定期的內部安全評估過程中，發現了七項值得注意的問題。在確定這些問題的嚴重性後，我們研究了它們的影響和可利用性，然後為每個問題建立內部概念驗證。我們還與
Dnsmasq 的維護人員 Simon Kelly 合作，製作了相應的修補程式來減緩問題。

在截至 2017 年 9 月 5 日的審查過程中，我們的團隊發現了三個潛在的遠端執行程式碼問題、一個資訊外洩和三個阻斷服務安全漏洞，這些問題會影響專案在
git 伺服器上的最新版本。

這些修補程式會回溯既往，並提交至 [ 專案的 Git 存放區
](http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=summary) 。

####  對 Compute Engine 的影響

根據預設，Dnsmasq 僅安裝在使用 [ NetworkManager
](https://wikipedia.org/wiki/NetworkManager) 的映像檔中，且預設為停用狀態。下列 Compute Engine
公開映像檔已安裝 Dnsmasq：

  * Ubuntu 16.04、16.10、17.04 
  * CentOS 7 
  * RHEL 7 

但是，其他映像檔可能已安裝 Dnsmasq，做為其他套件的依附元件。我們建議您更新 Debian、Ubuntu、CentOS、RHEL、SLES 和
OpenSuse 執行個體，以使用最新的作業系統映像檔。CoreOS 和 Container-Optimized OS 不會受到影響，Windows
映像檔也不會受影響。

執行 Debian 和 Ubuntu 的執行個體，可於執行個體中使用以下指令來更新：

    
    
    
    sudo apt-get -y update
    
    
    
    sudo apt-get -y dist-upgrade

如果是 Red Hat Enterprise Linux 和 CentOS 執行個體，請執行：

    
    
    
    sudo yum -y upgrade

如果是 SLES 和 OpenSUSE 映像檔，請執行：

    
    
    
    sudo zypper up

除了執行手動更新指令之外，也可以使用個別作業系統的 [ 映像檔系列，重新建立 VM 執行個體
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=zh_tw#publicimage) 。

|  高  |

  * [ CVE-2017-14491 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14491)
  * [ CVE-2017-14492 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14492)
  * [ CVE-2017-14493 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14493)
  * [ CVE-2017-14494 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14494)
  * [ CVE-2017-14495 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14495)
  * [ CVE-2017-14496 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14496)
  * [ CVE-2017-13704 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-13704)

  
  
##  發布日期：2016 年 10 月 26 日

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

CVE-2016-5195 是 Linux 核心的記憶體子系統在處理 COW 時出現競爭狀況，破壞唯讀與寫入權限的專屬對應關係。

未經授權的本機使用者可利用這個安全漏洞取得對應其他唯讀記憶體的編寫存取權，從而提高他們在系統中的權限。

詳情請參閱 [ Dirty COW 常見問題
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails) 。

####  對 Compute Engine 的影響

Compute Engine 上所有的 Linux
發行版和各種版本都受到影響。大多數的執行個體會自動下載並安裝較新的核心。但是，必須重新啟動才能修補正在運作中的系統。

使用下列的 Compute Engine 映像檔新建或重新建立的執行個體已安裝修補過的核心。

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

|  高  |  [ CVE-2016-5195
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails)  
  
##  發布日期：2016 年 2 月 16 日

**上次更新時間：2016 年 2 月 22 日**

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

CVE-2015-7547 是 glibc DNS 用戶端解析器會導致使用 ` getaddrinfo() `
程式庫函式的軟體容易出現堆疊型緩衝區溢位問題的安全漏洞。 攻擊者可以藉由使用此函式的軟體，以攻擊者控制的網域名稱、攻擊者控制的 DNS
伺服器或透過攔截式攻擊來利用這項漏洞。

詳情請參閱 [ Google 線上安全性網誌
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html) 或 [ 常見安全漏洞與資料外洩 ](http://www.cve.mitre.org/cgi-
bin/cvename.cgi?name=2015-7547) (Common Vulnerabilities and Exposures，簡稱 CVE)
資料庫。

####  對 Compute Engine 的影響

**更新 (2016 年 2 月 22 日)：**

現可使用 CoreOS、SLES 和 OpenSUSE 映像檔，重新建立您的執行個體：

  * ` coreos-alpha-962-0-0-v20160218 `
  * ` coreos-beta-899-7-0-v20160218 `
  * ` coreos-stable-835-13-0-v20160218 `
  * ` opensuse-13-2-v20160222 `
  * ` opensuse-leap-42-1-v20160222 `
  * ` sles-11-sp4-v20160222 `
  * ` sles-12-sp1-v20160222 `

**更新 (2016 年 2 月 17 日)：**

現可在 Ubuntu 12.04 LTS、Ubuntu 14.04 LTS 和 Ubuntu 15.10 執行個體上，使用下列指令來更新：

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

除了執行手動更新指令之外，也可以利用下列的新映像檔來重新建立執行個體：

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

我們雖然不知道任何以 glibc 預設配置透過 Compute Engine 的 DNS
解析器來利用這個安全漏洞的方法。但是，您仍應盡速修補您的虛擬機器執行個體，因為每當發現新的漏洞，過一段時間可能就會出現新的攻擊方法。如果已啟用 edns0
(預設為停用)，您應該在完成執行個體的修補前先改為停用。

**原始公告：**

您的 Linux 發行版可能存有安全漏洞。如果您是使用 Linux 作業系統的 Compute Engine
客戶，需更新執行個體的作業系統映像檔，以消除這個漏洞。

執行 Debian 的執行個體，可於執行個體中使用以下指令來更新：

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

另外，我們建議您為 Debian 執行個體安裝 [ UnattendedUpgrades
](https://wiki.debian.org/UnattendedUpgrades) 。

如果是 Red Hat Enterprise Linux 執行個體，指令如下：

  * ` user@my-instance:~$ sudo yum -y upgrade `
  * ` user@my-instance:~$ sudo reboot `

只要有作業系統維護人員針對這個漏洞發布修補程式，或者 Compute Engine 釋出了作業系統映像檔更新，我們都會更新公告。

|  高  |  [ CVE-2015-7547
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html)  
  
##  發布日期：2015 年 3 月 19 日

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

CVE-2015-1427 是 Groovy 指令碼引擎 [ Elasticsearch
](https://www.elastic.co/products/elasticsearch) 在 1.3.8 版以前和 1.4.3 之前任何 1.4.x
版的漏洞，使遠端攻擊者可繞過沙箱保護機制並執行任何的殼層指令。

詳情請參閱 [ 國家安全漏洞資料庫
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427) (National
Vulnerability Database，簡稱 NVD) 或 [ 常見安全漏洞與資料外洩 ](http://www.cve.mitre.org/cgi-
bin/cvename.cgi?name=2015-1427) (Common Vulnerabilities and Exposures，簡稱 CVE)
資料庫。

####  對 Compute Engine 的影響

如果您在 Compute Engine 執行個體上執行 Elasticsearch，應將 Elasticsearch 版本升級至 1.4.3
以上版本。如果您已經升級了 Elasticsearch 軟體，則不會受到這個安全漏洞的影響。

如果您尚未升級至 Elasticsearch 1.4.3 以上版本，可 [ 執行漸進式升級
](http://www.elastic.co/guide/en/elasticsearch/reference/current/rolling-
upgrades.html) 。

如果您是在 [ Google Cloud Platform Console
](https://console.cloud.google.com/?hl=zh_tw) 中使用 [ 點擊部署
](https://cloud.google.com/solutions/elasticsearch/click-to-deploy?hl=zh_tw)
來部署 Elasticsearch，您可以透過 [ 刪除部署項目
](https://console.cloud.google.com/projectselector/deployments?hl=zh_tw) 來移除執行
Elasticsearch 的執行個體。

Google Cloud Platform 團隊正在研究修復方法，以便部署 Elasticsearch 的更新版本。但是 [ GCP 主控台
](https://console.cloud.google.com/?hl=zh_tw) 的點擊部署功能尚不適用這項修正。

|  高  |  [ CVE-2015-1427
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427)  
  
##  發布日期：2015 年 1 月 29 日

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

[ CVE-2015-0235 (Ghost)
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235) 是 glibc
程式庫中的一個安全漏洞。

App Engine、Cloud Storage、BigQuery 和 CloudSQL 客戶無需採取任何行動。Google
的伺服器已經更新，因此不會受到這個漏洞的影響。

Compute Engine 的客戶可能需要更新 OS 映像檔。

####  對 Compute Engine 的影響

您的 Linux 發行版可能有安全漏洞。如果 Compute Engine 客戶使用的是 Debian 7、Debian 7
backports、Ubuntu 12.04 LTS、Red Hat Enterprise Linux、CentOS 或 SUSE Linux
Enterprise Server 11 SP3，則需更新執行個體的作業系統映像檔，以消除這個漏洞。

這個漏洞不影響 Ubuntu 14.04 LTS、Ubuntu 14.10 或 SUSE Linux Enterprise Server 12。

我們建議您升級您的 Linux 發行版。執行 Debian 7、Debian 7 backports 或 Ubuntu 12.04 LTS
的執行個體，可於執行個體中使用以下指令來更新：

  1. ` user@my-instance:~$ sudo apt-get update `
  2. ` user@my-instance:~$ sudo apt-get -y upgrade `
  3. ` user@my-instance:~$ sudo reboot `

如果是 Red Hat Enterprise Linux 或 CentOS 執行個體，指令如下：

  1. ` user@my-instance:~$ sudo yum -y upgrade `
  2. ` user@my-instance:~$ sudo reboot `

如果是 SUSE Linux Enterprise Server 11 SP3 執行個體，指令如下：

  1. ` user@my-instance:~$ sudo zypper --non-interactive up `
  2. ` user@my-instance:~$ sudo reboot `

除了執行手動更新指令之外，使用者也可利用下列的新映像檔重新建立執行個體：

  * ` debian-7-wheezy-v20150127 `
  * ` backports-debian-7-wheezy-v20150127 `
  * ` centos-6-v20150127 `
  * ` centos-7-v20150127 `
  * ` rhel-6-v20150127 `
  * ` rhel-7-v20150127 `
  * ` sles-11-sp3-v20150127 `
  * ` ubuntu-1204-precise-v20150127 `

####  對 Google 代管 VM 的影響

使用 ` gcloud preview app deploy ` 的代管 VM 使用者必須以 ` gcloud preview app setup-
managed-vms ` 更新基本 Docker 容器，並透過 ` gcloud preview app deploy `
重新部署各個運作中的應用程式。利用 ` appcfg ` 進行部署的使用者無需採取任何行動，部署項目就會自動升級。

|  高  |  [ CVE-2015-0235
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235)  
  
##  發布日期：2014 年 10 月 15 日

**上次更新時間：2014 年 10 月 17 日**

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

CVE-2014-3566 (又稱為 POODLE) 是 SSL 3.0
版在設計上的一個安全漏洞。這個漏洞讓網路攻擊者能計算出安全連線中的明文。詳情請參閱我們關於安全漏洞的 [ 網誌文章
](http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-
exploiting-ssl-30.html) 。

App Engine、Cloud Storage、BigQuery 和 CloudSQL 客戶無需採取任何行動。Google
的伺服器已經更新，因此不會受到這個漏洞的影響。Compute Engine 的客戶需要更新 OS 映像檔。

####  對 Compute Engine 的影響

**更新 (2014 年 10 月 17 日)：**

如果您使用 SSLv3，可能會受到攻擊。Compute Engine 客戶需更新執行個體的作業系統映像檔，以消除這個漏洞。

我們建議您升級您的 Linux 發行版。執行 Debian 的執行個體，可於執行個體中使用以下指令來更新：

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

如果是 CentOS 執行個體，指令如下：

    
    
    
    user@my-instance:~$ sudo yum -y upgrade
    user@my-instance:~$ sudo reboot

除了執行手動更新指令之外，使用者也可利用下列的新映像檔重新建立執行個體：

  * ` centos-6-v20141016 `
  * ` centos-7-v20141016 `
  * ` debian-7-wheezy-v20141017 `
  * ` backports-debian-7-wheezy-v20141017 `

我們有映像檔後，將更新 RHEL 和 SLES 映像檔公告。在此期間，RHEL 使用者可以 [ 直接諮詢 Red Hat
](https://access.redhat.com/articles/1232123) ，以獲取更多資訊。

**原始公告：**

Compute Engine 客戶需更新執行個體的作業系統映像檔，以消除這個漏洞。一旦有新的作業系統映像檔可使用時，我們將更新這則安全公告與操作說明。

|  中  |  [ CVE-2014-3566
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-3566)  
  
##  發布日期：2014 年 9 月 24 日

**上次更新時間：2014 年 9 月 29 日**

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

這個 bash 中的錯誤 (CVE-2014-6271)
會根據任何攻擊者控制的環境變數進行剖析，讓攻擊者得以從遠端執行程式碼。最可能的利用手法是透過對暴露於網路伺服器的 CGI 指令碼進行惡意 HTTP
要求。如需詳細資訊，請參閱 [ 錯誤說明 ](http://seclists.org/oss-sec/2014/q3/650) 。

除了 2014 年 9 月 26 日以前的 Compute Engine 客體 OS 映像檔外，Google Cloud Platform 產品上的這個
bash 漏洞都已獲得緩解。請參閱下面的步驟來排除 Compute Engine 映像檔中的錯誤。

####  對 Compute Engine 的影響

這個錯誤可能會影響使用 CGI 指令碼的所有網站。此外，也可能會影響仰賴 PHP、Perl、Python、SSI、JAVA、C++ 和 Servlet
之類的網站，透過呼叫像是 ` popen ` 、 ` system ` 、 ` shell_exec ` 或類似的 API 調用殼層指令。若系統是透過如
SSH 指令限制或 bash 限制殼層等機制，試圖將受控管的登入存取權開放給受限制的使用者，則也可能會受到影響。

**更新 (2014 年 9 月 29 日)：**

除了執行下列的手動更新指令之外，使用者現在也可以選擇利用映像檔重新建立執行個體，以便防範其他的 bash 安全性錯誤相關安全漏洞問題，其中包含 [
CVE-2014-7169 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169)
、 [ CVE-2014-6277
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277) 、 [
CVE-2014-6278 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278)
、 [ CVE-2014-7186
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186) 和 [
CVE-2014-7187 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)
。 使用下列新映像檔來重新建立您的執行個體：

  * ` centos-6-v20140926 `
  * ` centos-7-v20140926 `
  * ` debian-7-wheezy-v20140926 `
  * ` backports-debian-7-wheezy-v20140926 `
  * ` rhel-6-v20140926 `

**更新 (2014 年 9 月 25 日)：**

使用者現可選擇重新建立執行個體，而不必執行手動更新。 如要重新建立您的執行個體，請使用以下已對這個安全漏洞進行修正的新映像檔：

  * ` backports-debian-7-wheezy-v20140924 `
  * ` debian-7-wheezy-v20140924 `
  * ` rhel-6-v20140924 `
  * ` centos-6-v20140924 `
  * ` centos-7-v20140924 `

至於 RHEL 和 SUSE 映像檔，可於執行個體上使用下列指令來手動更新：

    
    
    
    # RHEL instances
    user@my-instance:~$ sudo yum -y upgrade
    
    # SUSE instances
    user@my-instance:~$ sudo zypper --non-interactive up

**原始公告：**

我們建議您升級您的 Linux 發行版。如果是執行 Debian 的執行個體，您可於執行個體中使用以下指令來更新：

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    

如果是 CentOS 執行個體，指令如下：

    
    
    
    user@my-instance:~$ sudo yum -y upgrade

如需詳細信息，請查看個別的 Linux 發行版公告：

  * 原始修補程式： [ http://ftp.gnu.org/gnu/bash/ ](http://ftp.gnu.org/gnu/bash/) (請見結尾為 *-patches 的項目，以找到適當版本) 
  * Debian： [ [SECURITY] [DSA 3032-1] bash 安全性更新 ](https://lists.debian.org/debian-security-announce/2014/msg00220.html)
  * RHEL: 
    * [ RHSA-2014:1293-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00048.html)
    * [ RHSA-2014:1294-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00049.html)
  * CentOS 5： [ [CentOS-通告] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020582.html)
  * CentOS 6： [ [CentOS-通告] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020585.html)
  * CentOS 7： [ [CentOS-通告] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020583.html)

|  高  |  [ CVE-2014-7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) 、 [
CVE-2014-6271 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6271)
、 [ CVE-2014-6277
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277) 、 [
CVE-2014-6278 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278)
、 [ CVE-2014-7186
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186) 、 [
CVE-2014-7187 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)  
  
##  發布日期：2014 年 7 月 25 日

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

[ Elasticsearch Logstash ](http://www.elasticsearch.org/overview/logstash/)
容易受到 OS 指令注入攻擊，這會允許未經授權的修改和資料揭露。攻擊者可以向任何 Logstash 的資料來源傳送蓄意設計的事件，允許攻擊者使用
Logstash 處理程序的權限來執行指令。

####  對 Compute Engine 的影響

這個安全漏洞會影響 Elasticsearch Logstash 版本低於 1.4.2 並啟用 zabbix 或 nagios_nsca 輸出的所有
Compute Engine 執行個體。為了防止攻擊，您可以：

  * 升級到 Logstash 1.4.2 
  * 為 1.3.x 版套用修補程式 
  * 停用 ` zabbix ` 與 ` nagios_nsca ` 輸出。 

深入閱讀 [ Logstash 網誌 ](http://www.elasticsearch.org/blog/logstash-1-4-2/) 的內容。

Elasticsearch 建議 [ 使用防火牆 ](http://www.elasticsearch.org/blog/scripting-
security/) 來防止不受信任的 IP 進行遠端存取。

|  高  |  [ CVE-2014-4326
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-4326)  
  
##  發布日期：2014 年 6 月 18 日

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

我們想花點時間來回應客戶對於 Google Cloud Platform 上執行的 Docker 容器安全性可能會有的任何疑慮。 採用支援 Docker
容器、容器最佳化虛擬機器或開放原始碼 Kubernetes 排程器的 Google App Engine 擴充功能的客戶，可能都會有這些疑慮。

Docker 已針對這個問題提供完善的說明，按 [ 這裡 ](http://blog.docker.com/2014/06/docker-
container-breakout-proof-of-concept-exploit/)
即可瀏覽他們的網誌回應內容。請注意，一如他們在回覆內容中所說，此次發現的問題僅存在於未正式推出的舊有版本 Docker 0.11。

雖然全世界都在思考容器安全性問題，但我們想強調的是，以 Linux 應用程式容器為基礎的解決方案 (尤其是 Docker 容器) 可以完全在 Google
Cloud Platform 的虛擬機器 (Google Compute Engine) 中運作。雖然我們支持 Docker 社群加強在 Linux
應用程式容器堆疊上的努力，但我們認識到這是一項新的技術，而且牽涉範圍廣大。我們相信就目前來說，完整的管理程序（虛擬機器）提供了更精簡和更具防禦性的介面區。虛擬機器從一開始就是為隔離惡意工作負載而設計，並盡量減少程式碼錯誤的可能性和影響。

我們的客戶可以放心，他們和任何可能具有惡意程式碼的第三方之間，存在全面的管理程序防線。如果我們認為 Linux
應用程式容器堆疊的穩健程度，已足以支援多租戶工作負載時，我們將會讓社群知道這一點。就目前來說，Linux
應用程式容器不會取代虛擬機器。這是完成更多工作的方式。

|  低  |  [ Docker 網誌文章 ](http://blog.docker.com/2014/06/docker-container-
breakout-proof-of-concept-exploit/)  
  
##  發布日期：2014 年 6 月 5 日

**上次更新時間：2014 年 6 月 9 日**

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

OpenSSL 在處理 ` ChangeCipherSpec `
訊息上有瑕疵，導致未與握手狀態機器建立正確繫結。因此可在握手處理過程中，將訊息提前注入。如此一來，攻擊者就能蓄意操弄握手作業的漏洞，強行在 OpenSSL
SSL/TLS 用戶端和伺服器中使用安全性低的加密材料。這可以用於攔截式 (MITM) 攻擊手法，讓攻擊者可以解密和修改受攻擊客戶端和伺服器的流量。

這個問題已標識為 [ CVE-2014-0224 ](https://www.openssl.org/news/secadv/20140605.txt)
。OpenSSL 團隊已修正了這個問題，並提醒 OpenSSL 社群更新 OpenSSL。

####  對 Compute Engine 的影響

這個安全漏洞會影響所有使用 OpenSSL 的 Compute Engine 執行個體，包括 Debian、CentOS、Red Hat
Enterprise Linux 和 SUSE Linux Enterprise
Server。您可以透過使用新映像檔重新建立執行個體，也可以手動更新執行個體上的套件。

**更新 (2014 年 6 月 9 日)：** 要利用新映像檔更新執行 SUSE Linux Enterprise Server
的執行個體，請使用下列映像檔版本或更新版本重新建立執行個體：

  * ` sles-11-sp3-v20140609 `

**原始文章：**

要利用新映像檔更新 Debian 和 CentOS 的執行個體，請使用下列任一映像檔版本或更新版本重新建立執行個體：

  * ` debian-7-wheezy-v20140605 `
  * ` backports-debian-7-wheezy-v20140605 `
  * ` centos-6-v20140605 `
  * ` rhel-6-v20140605 `

如要在您的執行個體上手動更新 OpenSSL，請執行以下指令來更新相應的套件。若是執行 CentOS 和 RHEL
的執行個體，可於執行個體中使用這些指令來更新 OpenSSL：

    
    
    
    user@my-instance:~$ sudo yum -y update
    user@my-instance:~$ sudo reboot

若是執行 Debian 的執行個體，可於執行個體中使用以下指令來更新 OpenSSL：

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

若是執行 SUSE Linux Enterprise Server 的執行個體，可於執行個體中使用這些指令來確保 OpenSSL 是最新版本：

    
    
    
    user@my-instance:~$ sudo zypper --non-interactive up
    user@my-instance:~$ sudo reboot

|  中  |  [ CVE-2014-0224
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0224)  
  
##  發布日期：2014 年 4 月 8 日

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

在 OpenSSL 1.0.1 版到 1.0.1g 版本之前的 (1) 傳輸層安全標準 (TLS) 與 (2) DTLS 機制，未適當處理
Heartbeat Extension 封包，讓遠端攻擊者可透過蓄意建構的封包觸發緩衝區過度讀取，進而從記憶體處理程序中獲取機密資訊，例如讀取與 `
d1_both.c ` 和 ` t1_lib.c ` 有關的私密金鑰，也稱為 Heartbleed 漏洞。

####  對 Compute Engine 的影響

這個安全漏洞會影響所有不具有最新 OpenSSL 版本的 Compute Engine Debian、RHEL 和 CentOS
執行個體。您可以透過使用新映像檔重新建立執行個體，也可以手動更新執行個體上的套件。

要使用新映像檔更新執行個體，請利用下列任一映像檔版本或更新版本重新建立執行個體：

  * ` debian-7-wheezy-v20140408 `
  * ` backports-debian-7-wheezy-v20140408 `
  * ` centos-6-v20140408 `
  * ` rhel-6-v20140408 `

如要在您的執行個體上手動更新 OpenSSL，請執行以下指令來更新相應的套件。若是執行 CentOS 和 RHEL
的執行個體，可於執行個體中使用這些指令來確保 OpenSSL 是最新版本：

    
    
    
    user@my-instance:~$ sudo yum update
    user@my-instance:~$ sudo reboot

若是執行 Debian 的執行個體，可於執行個體中使用以下指令來更新 OpenSSL：

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get upgrade
    user@my-instance:~$ sudo reboot

採用 SUSE Linux 的執行個體不受影響。

**2014 年 4 月 14 日更新：** Compute Engine 根據使用 Heartbleed 漏洞來擷取金鑰的新研究，建議 Compute
Engine 客戶為任何受影響的 SSL 服務建立新的金鑰。

|  中  |  [ CVE-2014-0160
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0160)  
  
##  發布日期：2013 年 6 月 7 日

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

**注意：** 這個安全漏洞僅對核心造成影響，且自 API 版本 v1 後的核心已遭淘汰及移除。

在 Linux kernel 3.9.4 之前的版本中，Broadcom B43 無線驅動程式中 `
drivers/net/wireless/b43/main.c ` 的 ` b43_request_firmware `
函式存在格式化字串安全漏洞，本機使用者可利用 root 存取權在 ` fwpostfix ` modprobe
參數中包含格式化字串指定碼，導致錯誤訊息的結構不當，以藉此獲取權限。

####  對 Compute Engine 的影響

這個安全漏洞會影響 ` gcg-3.3.8-201305291443 ` 之前的所有 Compute Engine
核心。為解決這個安全漏洞問題，Compute Engine 已淘汰所有早期核心，同時建議使用者更新執行個體和映像檔，以便使用 Compute Engine
核心 ` gce-v20130603 ` 。 ` gce-v20130603 ` 包含核心 ` gcg-3.3.8-201305291443 `
，其中具有針對這項安全漏洞的修補程式。

如要找出您執行個體使用的核心版本：

  1. 透過 ssh 登入您的執行個體 
  2. 執行 ` uname -r `

|  中  |  [ CVE-2013-2852
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2852)  
  
##  發布日期：2013 年 6 月 7 日

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

**注意：** 這個安全漏洞僅對核心造成影響，且自 API 版本 v1 後的核心已遭淘汰及移除。

在 Linux kernel 3.9.4 之前的版本中， ` block/genhd.c ` 的 register_disk
函式存在格式化字串安全漏洞，本機使用者可利用 root 存取權將格式化字串指定碼寫入 `
/sys/module/md_mod/parameters/new_array ` 來建立蓄意設計的 ` /dev/md ` 裝置名稱，以藉此獲取權限。

####  對 Compute Engine 的影響

這個安全漏洞會影響 ` gcg-3.3.8-201305291443 ` 之前的所有 Compute Engine
核心。為解決這個安全漏洞問題，Compute Engine 已淘汰所有早期核心，同時建議使用者更新執行個體和映像檔，以便使用 Compute Engine
核心 ` gce-v20130603 ` 。 ` gce-v20130603 ` 包含核心 ` gcg-3.3.8-201305291443 `
，其中具有針對這項安全漏洞的修補程式。

如要找出您執行個體使用的核心版本：

  1. 透過 ssh 登入您的執行個體 
  2. 執行 ` uname -r `

|  中  |  [ CVE-2013-2851
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2851)  
  
##  發布日期：2013 年 5 月 14 日

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

**注意：** 這個安全漏洞僅對核心造成影響，且自 API 版本 v1 後的核心已遭淘汰及移除。

在 Linux kernel 3.8.9 之前的版本中， ` kernel/events/core.c ` 的 perf_swevent_init
函式使用不正確的 ` integer ` 資料類型，本機使用者可透過蓄意設計的 ` perf_event_open ` 系統呼叫以獲取權限。

####  對 Compute Engine 的影響

這個安全漏洞會影響 ` gcg-3.3.8-201305211623 ` 之前的所有 Compute Engine
核心。為解決這個安全漏洞問題，Compute Engine 已淘汰所有早期核心，同時建議使用者更新執行個體和映像檔，以便使用 Compute Engine
核心 ` gce-v20130521 ` 。 ` gce-v20130521 ` 包含核心 ` gcg-3.3.8-201305211623 `
，其中具有針對這項安全漏洞的修補程式。

如要找出您執行個體使用的核心版本：

  1. 透過 ssh 登入您的執行個體 
  2. 執行 ` uname -r `

|  高  |  [ CVE-2013-2094
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2094)  
  
##  發布日期：2013 年 2 月 18 日

說明  |  嚴重性  |  附註  
---|---|---  
  
####  說明

**注意：** 這個安全漏洞僅對核心造成影響，且自 API 版本 v1 後的核心已遭淘汰及移除。

在 Linux kernel 3.7.5 之前的版本中，ptrace 存在競爭狀況，本機使用者可在蓄意設計的應用程式中透過 ` PTRACE_SETREGS
ptrace ` 系統呼叫以獲取權限。

####  對 Compute Engine 的影響

這個安全漏洞會影響 Compute Engine 核心 ` 2.6.x-gcg- _ <date> _ ` 。為了解決這個問題，Compute Engine
已淘汰 2.6.x 核心，並建議使用者更新執行個體和映像檔，以便使用 Compute Engine 核心 ` gce-v20130225 ` 。 `
gce-v20130225 ` 包含核心 ` 3.3.8-gcg-201302081521 ` ，後者已經修補了這個安全漏洞。

如要找出您執行個體使用的核心版本：

  1. 透過 ssh 登入您的執行個體 
  2. 執行 ` uname -r `

|  中  |  [ CVE-2013-0871
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-0871)

