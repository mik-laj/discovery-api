#  安全公告

我们可能会不时发布与 Compute Engine 相关的安全公告。所有与 Compute Engine 有关的安全公告都会在这里加以说明。

[ 订阅 Compute Engine 安全公告。 ![订阅](https://cloud.google.com/images/feed-
icon.png?hl=zh_cn) ](https://cloud.google.com/feeds/compute-engine-security-
bulletins.xml?hl=zh_cn)

##  发布日期：2019-06-18

**上次更新时间：2019-06-25 太平洋标准时间 (PST) 6:30**

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

Netflix 近来披露了 Linux 内核中的三个 TCP 漏洞：

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

这些 CVE 统称为 [ NFLX-2019-001 ](https://github.com/Netflix/security-
bulletins/blob/master/advisories/third-party/2019-001.md) 。

####  对 Compute Engine 的影响

托管 Compute Engine 的基础架构可抵御此漏洞。

如果 Compute Engine 虚拟机运行的是未修补的 Linux 操作系统，而且在发送/接收不受信任的网络流量，那么就容易遭受这一 DoS
攻击。我们建议在虚拟机实例的操作系统推出补丁程序后，立即更新相应实例。

作为 TCP 连接终端的负载平衡器已针对此漏洞进行了修补。仅通过这些负载平衡器接收不受信任流量的 Compute Engine 实例不受此漏洞的影响。这包括
HTTP 负载平衡器、SSL 代理负载平衡器和 TCP 代理负载平衡器。

网络负载平衡器和内部负载平衡器不作为 TCP 连接终端。未经过修补、通过这些负载平衡器接收不受信任流量的 Compute Engine 实例会受此漏洞影响。

####  修补后的映像和供应商资源

在各操作系统供应商提供补丁程序信息（包括上述各 CVE
的状态）的链接后，我们将在此页面公布。这些公共映像的更早版本不包含相关的补丁程序，因此无法缓解潜在攻击：

  * 项目 ` debian-cloud ` ： 
    * ` debian-9-stretch-v20190618 `
  * 项目 ` centos-cloud ` ： 
    * ` centos-6-v20190619 `
    * ` centos-7-v20190619 `
  * 项目 ` cos-cloud ` ： 
    * ` cos-dev-77-12293-0-0 `
    * ` cos-beta-76-12239-21-0 `
    * ` cos-stable-75-12105-77-0 `
    * ` cos-73-11647-217-0 `
    * ` cos-69-10895-277-0 `
  * 项目 ` coreos-cloud ` ： 
    * ` coreos-alpha-2163-2-1-v20190617 `
    * ` coreos-beta-2135-3-1-v20190617 `
    * ` coreos-stable-2079-6-0-v20190617 `
  * 项目 ` rhel-cloud ` ： 
    * ` rhel-6-v20190618 `
    * ` rhel-7-v20190618 `
    * ` rhel-8-v20190618 `
  * 项目 ` rhel-sap-cloud ` ： 
    * ` rhel-7-4-sap-v20190618 `
    * ` rhel-7-6-sap-v20190618 `
  * 项目 ` suse-cloud ` ： 
    * ` sles-12-sp4-v20190617 `
    * ` sles-15-v20190617 `
  * 项目 ` suse-sap-cloud ` ： 
    * ` sles-12-sp1-sap-v20190617 `
    * ` sles-12-sp2-sap-v20190617 `
    * ` sles-12-sp3-sap-v20190617 `
    * ` sles-12-sp4-sap-v20190617 `
    * ` sles-15-sap-v20190617 `
  * 项目 ` ubuntu-cloud ` ： 
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

  
  
##  发布日期：2019-05-14

**上次更新时间：2019-05-20 太平洋标准时间 (PST) 17:00**

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

Intel 披露了以下 CVE：

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

这些 CVE 统称为微架构数据抽样 (MDS)。这些漏洞可用于通过推测性执行技术与微架构状态交互，从而造成数据泄露风险。

####  对 Compute Engine 的影响

**运行 Compute Engine 的主机基础架构将客户的工作负载彼此隔离。除非您在虚拟机内部运行不受信任的代码，否则无需执行其他操作。**

如果客户在 Compute Engine 虚拟机内自己的多租户服务中运行不受信任的代码，请参阅相应客机操作系统供应商推荐的迁移方案，其中可能包括使用
Intel 的微代码缓解功能。我们已经部署了对新的强制刷新 (flush) 功能的客户直通访问。下面汇总了常用客机映像的可用缓解步骤。

####  修补后的映像和供应商资源

在各操作系统供应商提供补丁程序信息（包括上述各 CVE
的状态）的链接之后，我们将在此页面公布。请使用这些映像重新创建虚拟机实例。这些公共映像的更早版本不包含相关的补丁程序，因此无法缓解潜在攻击：

  * 项目 ` centos-cloud ` ： [ CESA-2019:1169 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023309.html) 、 [ CESA-2019:1168 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023314.html)
    * ` centos-6-v20190515 `
    * ` centos-7-v20190515 `
  * 项目 ` coreos-cloud ` ： [ 适用于 CoreOS Container Linux 的 MDS 缓解措施 ](https://coreos.com/os/docs/latest/disabling-smt.html)
    * ` coreos-stable-2079-4-0-v20190515 `
    * ` coreos-beta-2107-3-0-v20190515 `
    * ` coreos-alpha-2135-1-0-v20190515 `
  * 项目 ` cos-cloud `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
  * 项目 ` debian-cloud ` ： [ DSA-4444 ](https://www.debian.org/security/2019/dsa-4444)
    * ` debian-9-stretch-v20190514 `
  * 项目 ` rhel-cloud ` ： [ Red Hat MDS 知识文章 ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-6-v20190515 `
    * ` rhel-7-v20190517 `
    * ` rhel-8-v20190515 `
  * 项目 ` rhel-sap-cloud ` ： [ Red Hat MDS 知识文章 ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-7-4-sap-v20190515 `
    * ` rhel-7-6-sap-v20190517 `
  * 项目 ` suse-cloud ` ： [ SUSE MDS KB ](https://www.suse.com/support/kb/doc/?id=7023736)
    * ` sles-12-sp4-v20190520 `
    * ` sles-15-v20190520 `
  * 项目 ` suse-sap-cloud `
    * ` sles-12-sp4-sap-v20190520 `
    * ` sles-15-sap-v20190520 `
  * 项目 ` ubuntu-os-cloud ` ： [ Ubuntu MDS Wiki ](https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/MDS)
    * ` ubuntu-1404-trusty-v20190514 `
    * ` ubuntu-1604-xenial-v20190514 `
    * ` ubuntu-1804-bionic-v20190514 `
    * ` ubuntu-1810-cosmic-v20190514 `
    * ` ubuntu-1904-disco-v20190514 `
    * ` ubuntu-minimal-1604-xenial-v20190514 `
    * ` ubuntu-minimal-1804-bionic-v20190514 `
    * ` ubuntu-minimal-1810-cosmic-v20190514 `
    * ` ubuntu-minimal-1904-disco-v20190514 `
  * 项目 ` windows-cloud ` 和 ` windows-sql-cloud ` ： [ Microsoft ADV190013 ](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/ADV190013)
    * 版本号为 ` v20190514 ` 的所有 Windows Server 和 SQL Server 公共映像。 
  * 项目 ` gce-uefi-images `
    * ` centos-7-v20190515 `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
    * ` rhel-7-v20190517 `
    * ` ubuntu-1804-bionic-v20190514 `
    * 版本号为 ` v20190514 ` 的所有 Windows Server 公共映像。 

####  Container-Optimized OS

如果您在使用 Container Optimized OS (COS)
作为客机操作系统，而且在虚拟机中运行不受信任的多租户工作负载，我们建议您采取以下措施：

  1. 在内核命令行中设置 ` nosmt ` 来停用超线程。   

在现有 COS 虚拟机上，您可以按如下方式修改 ` grub.cfg ` ，设置 ` nosmt ` 选项，然后重新启动系统：

    
        
    # Run as root:
    dir="$(mktemp -d)"
    mount /dev/sda12 "${dir}"
    sed -i -e "s|cros_efi|cros_efi nosmt|g" "${dir}/efi/boot/grub.cfg"
    umount "${dir}"
    rmdir "${dir}"
    
    reboot

为便捷起见，您可以运行下面的脚本，效果与运行上方命令相同。建议您将该脚本加入 cloud-config
文件、启动脚本或实例模板中，确保新虚拟机都使用这个新参数。下面还给出了运行此脚本的一个示例 cloud-config 文件。

**警告** ：此命令在初次运行时会导致实例立即重启。在已经停用了超线程的实例上，后续运行此命令不会产生任何效果。

    
        
    # Run as root
    /bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)
    

按如下所示，将这段脚本加入到 cloud-config 文件中：

    
        
    #cloud-config
    
    bootcmd:
    - /bin/bash -c "/bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)"
    

如需确认您的实例已经停用超线程，请查看 ` /sys/devices/system/cpu/smt/active ` 和 `
/sys/devices/system/cpu/smt/control ` 文件的输出。如果针对 ` active ` 返回了 ` 0 ` ，针对 `
control ` 返回了 ` off ` ，则表示超线程已停用：

    
        
    cat /sys/devices/system/cpu/smt/active
    cat /sys/devices/system/cpu/smt/control
    

**注意** ：如果您的实例已启用 UEFI 安全启动，则需要在停用 UEFI 安全启动的情况下重新创建实例。请在停用 UEFI
安全启动的情况下运行上面的命令，然后在新实例上启用 UEFI 安全启动。

  2. 使用新版本的 COS 映像   

除了按上文所述方式停用超线程之外，您还应使用上面列出的经过更新的映像或 Container-Optimized OS 映像的新版本（可用时） [
重新创建实例 ](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=zh_cn#publicimage) ，以便获得充分保护并避免受到这些漏洞影响。

|  中  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  发布日期：2018-08-14

**上次更新时间：2018-08-20 太平洋标准时间 (PST) 17:00**

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

[ Intel 披露了 ](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) 以下 CVE：

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) （针对 [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ） 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) （针对操作系统和 [ SMT ](https://en.wikipedia.org/wiki/Hyper-Threading) ） 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) （针对虚拟化） 

这些 CVE 统称为“L1 终端故障 (L1TF)”。

这些 L1TF 漏洞通过攻击处理器层的数据结构配置来利用推测性执行技术。“L1”是指 1 级数据缓存
(L1D)，这是一种用于加快内存访问速度的小型芯片上资源。

如需详细了解这些漏洞和 Compute Engine 的缓解措施，请参阅 [ Google Cloud 博文
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=zh_cn) 。

####  对 Compute Engine 的影响

运行 Compute Engine 并将客户的工作负载彼此隔离的主机基础架构可以抵御已知攻击。

我们鼓励 Compute Engine 客户更新自己的映像，以防在其客机环境内被间接利用。这对在 Compute Engine
虚拟机上运行其多租户服务的客户尤为重要。

Google Compute Engine 客户可以通过以下任一方式更新其实例上的客机操作系统：

  * 使用修补后的公共映像 [ 重新创建现有虚拟机实例 ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=zh_cn#publicimage) 。 
  * 在现有实例上，安装操作系统供应商提供的补丁程序，然后重新启动修补后的实例。 

####  修补后的映像和供应商资源

在各操作系统供应商提供补丁程序信息（包括上述 CVE
的状态）的链接后，我们将在此页面公布。您可以使用这些映像重新创建虚拟机实例。这些公共映像的更早版本不包含相关的补丁程序，因此无法缓解潜在攻击：

  * 项目 ` centos-cloud ` ： 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * 项目 ` coreos-cloud ` ： 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * 项目 ` cos-cloud ` ： 
    * ` cos-stable-66-10452-110-0 `
    * ` cos-stable-67-10575-66-0 `
    * ` cos-beta-68-10718-81-0 `
    * ` cos-dev-69-10895-23-0 `
  * 项目 ` debian-cloud ` ： 
    * ` debian-9-stretch-v20180820 `
  * 项目 ` rhel-cloud ` ： 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * 项目 ` rhel-sap-cloud ` ： 
    * ` rhel-7-sap-apps-v20180814 `
    * ` rhel-7-sap-hana-v20180814 `
  * 项目 ` suse-cloud ` ： 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
    * ` sles-11-sp4-v20180816 `
  * 项目 ` suse-sap-cloud ` ： 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * 项目 ` ubuntu-os-cloud ` ： 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `
  * 项目 ` windows-cloud ` ` gce-uefi-images ` 和 ` windows-sql-cloud ` ： 
    * 所有 ` -v201800814 ` 及更高版本的 Windows Server 和 SQL Server [ 公共映像 ](https://cloud.google.com/compute/docs/images?hl=zh_cn#os-compute-support) 都包含补丁程序。 

|  高  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  发布日期：2018-08-06

**上次更新时间：2018-09-05 太平洋标准时间 (PST) 17:00**

说明  |  严重级别  |  备注  
---|---|---  
  
####  2018 年 9 月 5 日更新

US-CERT 在 2018 年 8 月 14 日披露了 [ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) 。与 [ CVE-2018-5390
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
一样，这也是一个内核级的网络漏洞，可提高 DoS（拒绝服务）攻击对存在该漏洞的系统的攻击有效性。两者的主要区别是 CVE-2018-5391 可通过 IP
连接加以利用。我们在此更新公告，涵盖这两个漏洞的相关信息。

####  说明

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) （“SegmentSmack”）描述了一个内核级的网络漏洞，利用它可增强经由 TCP
连接的 DoS（拒绝服务）攻击对存在该漏洞的系统的攻击有效性。

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) （“FragmentSmack”）描述了一个内核级的网络漏洞，利用它可增强经由 IP
连接的 DoS（拒绝服务）攻击对存在该漏洞的系统的攻击有效性。

####  对 Compute Engine 的影响

运行 Compute Engine 虚拟机的主机基础架构不会受到影响。处理进出 Compute Engine
虚拟机的流量的网络基础架构可以抵御此漏洞。仅通过 [ HTTP(S) ](https://cloud.google.com/load-
balancing/docs/https/?hl=zh_cn) 、 [ SSL ](https://cloud.google.com/load-
balancing/docs/ssl/?hl=zh_cn) 或 [ TCP 负载平衡器 ](https://cloud.google.com/load-
balancing/docs/tcp/?hl=zh_cn) 发送/接收不受信任的网络流量的 Compute Engine 虚拟机可抵御此漏洞。

运行未修补的操作系统的 Compute Engine 虚拟机在直接或通过 [ 网络负载平衡器
](https://cloud.google.com/load-balancing/docs/network/?hl=zh_cn)
发送/接收不受信任的网络流量时容易遭受这一 DoS（拒绝服务）攻击。

我们建议在虚拟机实例的操作系统推出补丁程序后，立即更新这些实例。

Compute Engine 客户可以通过以下任一方式更新其实例上的客机操作系统：

  * 使用修补后的公共映像 [ 重新创建现有虚拟机实例 ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=zh_cn#publicimage) 。请查看下面的修补后公共映像列表。 
  * 在现有实例上，安装操作系统供应商提供的补丁程序，然后重新启动修补后的实例。 

####  修补后的映像和供应商资源

在各操作系统供应商提供补丁程序信息的链接后，我们将在此页面公布。

  * 项目 ` centos-cloud ` （仅限 CVE-2018-5390）： 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * 项目 ` coreos-cloud ` （CVE-2018-5390 和 CVE-2018-5391）： 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * 项目 ` cos-cloud ` （CVE-2018-5390 和 CVE-2018-5391）： 
    * ` cos-stable-65-10323-98-0 `
    * ` cos-stable-66-10452-109-0 `
    * ` cos-stable-67-10575-65-0 `
    * ` cos-beta-68-10718-76-0 `
    * ` cos-dev-69-10895-16-0 `
  * 项目 ` debian-cloud ` （CVE-2018-5390 和 CVE-2018-5391）： 
    * ` debian-9-stretch-v20180814 `
  * 项目 ` rhel-cloud ` （仅限 CVE-2018-5390）： 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * 项目 ` suse-cloud ` （CVE-2018-5390 和 CVE-2018-5391）： 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
  * 项目 ` suse-sap-cloud ` （CVE-2018-5390 和 CVE-2018-5391）： 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * 项目 ` ubuntu-os-cloud ` （CVE-2018-5390 和 CVE-2018-5391）： 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `

|  高  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  发布日期：2018-01-03

**上次更新时间：2018-05-21 太平洋标准时间 (PST) 15:00**

说明  |  严重级别  |  备注  
---|---|---  
  
####  2018 年 5 月 21 日更新

[ Intel 披露了 ](https://www.intel.com/content/www/us/en/security-
center/advisory/intel-sa-00115.html) [ CVE-2018-3640
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3640) 和 [
CVE-2018-3639 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639)
（分别对应变体 3a 和 4）。与 Spectre 和 Meltdown 的前三个变体一样，运行 Compute Engine
虚拟机实例的基础架构也不会受到影响，而且客户虚拟机实例也会彼此隔离、互不影响。此外，Compute Engine 还计划将 Intel
的微代码补丁程序部署到我们的基础架构中。对于在单个虚拟机实例内运行不受信任或多租户工作负载的客户，这将让他们能够在操作系统供应商和提供商提供了其它的虚拟机内缓解措施时加以启用。Compute
Engine 只会部署符合以下两个条件的微代码补丁程序：已获得 Intel 认证；经 Compute Engine
测试并证实可在我们的生产环境中使用。我们将及时地在此页面公布更详细的时间安排和更新。

####  说明

这些 CVE 是一种新型攻击的变体，它们利用的是许多处理器都提供的推测性执行技术。此类攻击可在多种情况下对内存数据进行未经授权的只读访问。

Compute Engine
使用虚拟机实时迁移技术来执行主机系统和管理程序更新，因此不会因为更新而影响用户，也不需要强制实施维护期和执行大规模重新启动。但为了抵御这种新型攻击，必须对所有客机操作系统和版本进行修补，无论这些系统在何处运行。

如需详细了解有关这种攻击方式的完整技术信息，请阅读 [ Project Zero 博文
](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-
with-side.html) 。如需详细了解有关 Google 提供的缓解措施的完整信息（包括所有产品特有的信息），请阅读 [ Google 安全博文
](https://security.googleblog.com/2018/01/todays-cpu-vulnerability-what-you-
need.html) 。

####  对 Compute Engine 的影响

运行 Compute Engine
并将客户的虚拟机实例彼此隔离的基础架构可以抵御已知攻击。我们的缓解措施可防止在虚拟机实例内部运行的应用对我们的主机系统进行未经授权的访问。这些缓解措施还可以防止在同一主机系统上运行的虚拟机实例之间进行未经授权的访问。

如需防止虚拟机实例内部发生未经授权的访问，您必须使用以下任一方式更新这些实例上的客机操作系统：

  * 使用修补后的公共映像 [ 重新创建现有虚拟机实例 ](https://cloud.google.com/compute/docs/instances/create-start-instance?hl=zh_cn#publicimage) 。请查看下面的修补后公共映像列表。 
  * 在现有实例上，安装操作系统供应商为您的发行版提供的补丁程序，然后重启实例。如需了解来自各操作系统供应商的补丁程序信息，请参阅下面的链接。 

####  修补后的映像和供应商资源

**注意** ：修补后的映像可能不包含针对本安全公告声明中列出的所有 CVE
的修复。另外，不同映像所包含的用于抵御这些类型攻击的方法可能也有所不同。请与您的操作系统供应商联系，以确认其所提供的补丁程序可以解决哪些 CVE
以及采用的是何种防御措施。

  * 项目 ` cos-cloud ` ：所含补丁程序可抵御变体 2 ( [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715) ) 和变体 3 ( [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754) ) 攻击。Google 在这些映像中使用 [ Retpoline ](https://support.google.com/faqs/answer/7625886?hl=zh_cn) 来缓解变体 2 攻击。 
    * ` cos-stable-63-10032-71-0 ` 或映像系列 ` cos-stable `
  * 项目 ` centos-cloud ` ： [ CentOS 补丁程序信息 ](https://lwn.net/Alerts/CentOS/)
    * ` centos-7-v20180104 ` 或映像系列 ` centos-7 `
    * ` centos-6-v20180104 ` 或映像系列 ` centos-6 `
  * 项目 ` coreos-cloud ` ： [ CoreOS 补丁程序信息 ](https://coreos.com/blog/container-linux-meltdown-patch)
    * ` coreos-stable-1576-5-0-v20180105 ` 或映像系列 ` coreos-stable `
    * ` coreos-beta-1632-1-0-v20180105 ` 或映像系列 ` coreos-beta `
    * ` coreos-alpha-1649-0-0-v20180105 ` 或映像系列 ` coreos-alpha `
  * 项目 ` debian-cloud ` ： [ Debian 补丁程序信息 ](https://www.debian.org/security/#DSAS)
    * ` debian-9-stretch-v20180105 ` 或映像系列 ` debian-9 `
    * ` debian-8-jessie-v20180109 ` 或映像系列 ` debian-8 `
  * 项目 ` rhel-cloud ` ： [ RHEL 补丁程序信息 ](https://access.redhat.com/security/vulnerabilities/speculativeexecution)
    * ` rhel-7-v20180104 ` 或映像系列 ` rhel-7 `
    * ` rhel-6-v20180104 ` 或映像系列 ` rhel-6 `
  * 项目 ` suse-cloud ` ： [ SUSE 补丁程序信息 ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-v20180104 ` 或映像系列 ` sles-12 `
    * ` sles-11-sp4-v20180104 ` 或映像系列 ` sles-11 `
  * 项目 ` suse-sap-cloud ` ： [ SUSE 补丁程序信息 ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-sap-v20180104 ` 或映像系列 ` sles-12-sp3-sap `
    * ` sles-12-sp2-sap-v20180104 ` 或映像系列 ` sles-12-sp2-sap `
  * 项目 ` ubuntu-os-cloud ` ： [ Ubuntu 补丁程序信息 ](https://insights.ubuntu.com/2018/01/04/ubuntu-updates-for-the-meltdown-spectre-vulnerabilities/)
    * ` ubuntu-1710-artful-v20180109 ` 或映像系列 ` ubuntu-1710 `
    * ` ubuntu-1604-xenial-v20180109 ` 或映像系列 ` ubuntu-1604-lts `
    * ` ubuntu-1404-trusty-v20180110 ` 或映像系列 ` ubuntu-1404-lts `
  * 项目 ` windows-cloud ` 和 ` windows-sql-cloud ` ： 
    * 所有 ` -v20180109 ` 及更高版本的 Windows Server 和 SQL Server [ 公共映像 ](https://cloud.google.com/compute/docs/images?hl=zh_cn#os-compute-support) 都包含补丁程序。但是，您必须按照 Microsoft 在 [ Windows Server 指南 ](https://support.microsoft.com/en-gb/help/4072698/windows-server-guidance-to-protect-against-the-speculative-execution) 支持公告中建议的操作加以启用，并且需要验证这些缓解措施在现有实例和新创建的实例上的效果。 

您可以使用这些映像 [ 重新创建虚拟机实例
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=zh_cn#publicimage) 。这些公共映像的更早版本不包含相关的补丁程序，因此无法缓解潜在攻击。

####  来自硬件供应商的补丁程序

NVIDIA 提供了经过修补的驱动程序，可缓解对安装了 NVIDIA® 驱动程序软件的系统的潜在攻击。如需了解哪些驱动程序版本已经过修补，请参阅
NVIDIA 的 [ NVIDIA GPU 显示驱动程序安全更新
](http://nvidia.custhelp.com/app/answers/detail/a_id/4611) 安全公告。

####  修订历史记录：

  * 2018-05-21 T 14:00（美国太平洋标准时间）：添加了有关在 2018 年 5 月 21 日披露的 2 个新型变体的信息。 
  * 2018-01-10 T 15:00（美国太平洋标准时间）：添加了有关修补后的 Windows Server 和 SQL Server 公共映像的信息。 
  * 2018-01-10 T 10:15（美国太平洋标准时间）：在修补后的公共映像列表中添加了几个 Ubuntu 映像。 
  * 2018-01-10 T 09:50（美国太平洋标准时间）：添加了有关来自硬件供应商的补丁程序的指南。 
  * 2018-01-03 至 2018-01-09：对修补后的公共映像列表进行了多项修订。 

|  高  |

  * [ CVE-2017-5753 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5753)
  * [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715)
  * [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754)
  * [ CVE-2018-3640 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3640)
  * [ CVE-2018-3639 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639)

  
  
##  发布日期：2017-10-02

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

[ Dnsmasq ](http://www.thekelleys.org.uk/dnsmasq/doc.html) 提供服务
DNS、DHCP、路由器通告和网络启动的功能。该软件普遍安装在桌面 Linux 发行版（如 Ubuntu）、家用路由器和 IoT
设备等多种系统中。Dnsmasq 广泛用于开放互联网和专用网络内部。

Google
在定期内部安全评估过程中发现了七个不同的问题。在确定这些问题的严重性之后，我们研究了它们的影响和被利用的可能性，然后针对每个问题完成了内部概念证明。我们还与
Dnsmasq 的维护者 Simon Kelly 合作编写了适当的补丁程序，以缓解这一问题。

在我们的审查过程中，截至 2017 年 9 月 5 日，团队发现了三个潜在的远程代码执行、一个信息泄露以及三个拒绝服务漏洞，这些漏洞影响项目 git
服务器的最新版本。

这些补丁程序已经上传，并且已经提交到了 [ 项目的 Git 代码库
](http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=summary) 。

####  对 Compute Engine 的影响

默认情况下，Dnsmasq 仅安装在使用 [ NetworkManager
](https://wikipedia.org/wiki/NetworkManager) 的映像中，并且处于非活动状态。以下 Compute Engine
公共映像安装了 Dnsmasq：

  * Ubuntu 16.04、16.10、17.04 
  * CentOS 7 
  * RHEL 7 

但是，其他映像可能已将 Dnsmasq 作为其他软件包的依赖项安装。我们建议您更新 Debian、Ubuntu、CentOS、RHEL、SLES 和
OpenSuse 实例，以使用最新的操作系统映像。CoreOS 和 Container-Optimized OS 不受影响。Windows 映像也不受影响。

对于运行 Debian 和 Ubuntu 的实例，您可以通过在实例中运行以下命令来执行更新：

    
    
    
    sudo apt-get -y update
    
    
    
    sudo apt-get -y dist-upgrade

对于 Red Hat Enterprise Linux 和 CentOS 实例，运行：

    
    
    
    sudo yum -y upgrade

对于 SLES 和 OpenSUSE 映像，运行：

    
    
    
    sudo zypper up

除了运行手动更新命令以外，您可以使用相应操作系统的 [ 映像系列重新创建 VM 实例
](https://cloud.google.com/compute/docs/instances/create-start-
instance?hl=zh_cn#publicimage) 。

|  高  |

  * [ CVE-2017-14491 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14491)
  * [ CVE-2017-14492 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14492)
  * [ CVE-2017-14493 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14493)
  * [ CVE-2017-14494 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14494)
  * [ CVE-2017-14495 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14495)
  * [ CVE-2017-14496 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14496)
  * [ CVE-2017-13704 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-13704)

  
  
##  发布日期：2016-10-26

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

CVE-2016-5195 是 Linux 内核内存子系统处理写访问中只读私有映射 COW 泄漏时，发生争用的情况。

未经授权的本地用户可以利用此漏洞，获取对只读内存映射的写入访问权限，从而提高自身的系统权限。

如需了解更多信息，请参阅 [ Dirty COW 常见问题解答
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails) 。

####  对 Compute Engine 的影响

Compute Engine 上的所有 Linux
发行版和版本都会受到影响。大多数实例会自动下载并安装更新的内核。但是，需要重新启动才能完成对正在运行的系统的修补。

基于以下 Compute Engine 映像的新实例或重新创建的实例已经安装了经过修补的内核。

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
  
##  发布日期：2016-02-16

**上次更新日期：2016-02-22**

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

CVE-2015-7547 是一个漏洞，在使用 ` getaddrinfo() ` 库函数时，glibc DNS
客户端解析器会导致软件容易受到基于堆栈的缓冲区溢出攻击。攻击者可以借助调用此函数的软件，通过由攻击者控制的域名和 DNS
服务器，或者通过中间人攻击来利用这一漏洞。

如需了解详情，请参阅 [ Google 在线安全博客
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html) 或 [ 常见漏洞和披露 (CVE) ](http://www.cve.mitre.org/cgi-
bin/cvename.cgi?name=2015-7547) 数据库。

####  对 Compute Engine 的影响

**更新日期 (2016-02-22)：**

您现在可以使用以下 CoreOS、SLES 和 OpenSUSE 映像重新创建实例：

  * ` coreos-alpha-962-0-0-v20160218 `
  * ` coreos-beta-899-7-0-v20160218 `
  * ` coreos-stable-835-13-0-v20160218 `
  * ` opensuse-13-2-v20160222 `
  * ` opensuse-leap-42-1-v20160222 `
  * ` sles-11-sp4-v20160222 `
  * ` sles-12-sp1-v20160222 `

**更新日期 (2016-02-17)：**

您现在可以通过运行以下命令在 Ubuntu 12.04 LTS、Ubuntu 14.04 LTS 和 Ubuntu 15.10 实例上执行更新：

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

除了运行手动更新命令以外，您现在可以使用以下新映像重新创建其实例：

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

就我们所知，尚无任何方法可通过使用默认 glibc 配置的 Compute Engine DNS
解析器利用此漏洞。不过您仍然应该尽快为自己的虚拟机实例安装补丁程序，因为与任何新漏洞一样，随着时间的推移可能会发现新的利用方法。如果您已经启用了
edns0（默认为禁用），则应该将其禁用，直到为实例安装好补丁程序。

**原始公告：**

您的 Linux 发行版可能存在漏洞。Compute Engine 客户如果在运行 Linux 操作系统，则需要更新其实例的操作系统映像，以消除这个漏洞。

对于运行 Debian 的实例，您可以通过在实例中运行以下命令来执行更新：

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

我们还建议为您的 Debian 实例安装 [ UnattendedUpgrades
](https://wiki.debian.org/UnattendedUpgrades) 。

对于 Red Hat Enterprise Linux 实例，请运行以下命令：

  * ` user@my-instance:~$ sudo yum -y upgrade `
  * ` user@my-instance:~$ sudo reboot `

随着其他操作系统维护者针对此漏洞发布补丁程序，以及 Compute Engine 发布更新后的操作系统映像，我们将不断更新此公告。

|  高  |  [ CVE-2015-7547
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html)  
  
##  发布日期：2015-03-19

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

CVE-2015-1427 是针对 [ Elasticsearch
](https://www.elastic.co/products/elasticsearch) 中 Groovy 脚本引擎在版本 1.3.8
之前的各版本以及 1.4.3 之前的各 1.4.x 版本的漏洞，该漏洞让远程攻击者可绕过沙箱保护机制并执行任意 shell 命令。

如需了解详情，请参阅 [ 美国国家漏洞数据库 (NVD)
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427) 或 [ 常见漏洞和披露
(CVE) ](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-1427) 数据库。

####  对 Compute Engine 的影响

如果您在 Compute Engine 实例上运行 Elasticsearch，应将 Elasticsearch 升级到 1.4.3
或更高版本。如果您已经升级了 Elasticsearch 软件，则可以免受此漏洞的攻击。

如果您尚未升级到 Elasticsearch 1.4.3 或更高版本，可以 [ 执行滚动升级
](http://www.elastic.co/guide/en/elasticsearch/reference/current/rolling-
upgrades.html) 。

如果您在 [ Google Cloud Platform Console
](https://console.cloud.google.com/?hl=zh_cn) 中使用 [ 一键部署
](https://cloud.google.com/solutions/elasticsearch/click-to-deploy?hl=zh_cn)
功能来部署 Elasticsearch，可以 [ 删除部署
](https://console.cloud.google.com/projectselector/deployments?hl=zh_cn) 以移除运行
Elasticsearch 的实例。

Google Cloud Platform 团队正在开发修补程序，以便部署 Elasticsearch 的更新版本。但是，可用于 [ GCP Console
](https://console.cloud.google.com/?hl=zh_cn) 中“一键部署”功能的修补程序尚未完成。

|  高  |  [ CVE-2015-1427
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427)  
  
##  发布日期：2015-01-29

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

[ CVE-2015-0235 (Ghost)
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235) 是 glibc
库中的一个漏洞。

App Engine、Cloud Storage、BigQuery 和 Cloud SQL 客户不需要采取任何行动。Google
服务器已经更新，可抵御此漏洞。

Compute Engine 的客户可能需要更新其操作系统映像。

####  对 Compute Engine 的影响

您的 Linux 发行版可能存在漏洞。如果 Compute Engine 客户运行的是 Debian 7、Debian 7 反向移植、Ubuntu
12.04 LTS、Red Hat Enterprise Linux、CentOS 或 SUSE Linux Enterprise Server 11
SP3，则需要更新其实例的操作系统映像以消除此漏洞。

此漏洞不影响 Ubuntu 14.04 LTS、Ubuntu 14.10 或 SUSE Linux Enterprise Server 12。

我们建议您升级 Linux 发行版。对于运行 Debian 7、Debian 7 反向移植或 Ubuntu 12.04 LTS
的实例，您可以通过在实例中运行以下命令来执行更新：

  1. ` user@my-instance:~$ sudo apt-get update `
  2. ` user@my-instance:~$ sudo apt-get -y upgrade `
  3. ` user@my-instance:~$ sudo reboot `

对于 Red Hat Enterprise Linux 和 CentOS 实例，运行：

  1. ` user@my-instance:~$ sudo yum -y upgrade `
  2. ` user@my-instance:~$ sudo reboot `

对于 SUSE Linux Enterprise Server 11 SP3 实例，运行：

  1. ` user@my-instance:~$ sudo zypper --non-interactive up `
  2. ` user@my-instance:~$ sudo reboot `

除了运行手动更新命令以外，用户现在可以使用以下新映像重新创建其实例：

  * ` debian-7-wheezy-v20150127 `
  * ` backports-debian-7-wheezy-v20150127 `
  * ` centos-6-v20150127 `
  * ` centos-7-v20150127 `
  * ` rhel-6-v20150127 `
  * ` rhel-7-v20150127 `
  * ` sles-11-sp3-v20150127 `
  * ` ubuntu-1204-precise-v20150127 `

####  对由 Google 托管的虚拟机的影响

使用 ` gcloud preview app deploy ` 命令部署的托管虚拟机用户需要执行 ` gcloud preview app setup-
managed-vms ` 命令来更新其基础 Docker 容器，并运行 ` gcloud preview app deploy `
命令重新部署每个正在运行的应用。使用 ` appcfg ` 执行部署的用户不需要采取任何措施，系统将会自动进行升级。

|  高  |  [ CVE-2015-0235
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235)  
  
##  发布日期：2014-10-15

**上次更新日期：2014-10-17**

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

CVE-2014-3566（又称为 POODLE）是 SSL 3.0
版设计中的一个漏洞。利用这个漏洞，网络攻击者能够计算安全连接的明文。有关详细信息，请参阅我们探讨该漏洞的 [ 博文
](http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-
exploiting-ssl-30.html) 。

App Engine、Cloud Storage、BigQuery 和 Cloud SQL 客户不需要采取任何行动。Google
服务器已经更新，可抵御此漏洞。Compute Engine 的客户需要更新其操作系统映像。

####  对 Compute Engine 的影响

**更新日期 (2014-10-17)：**

如果您使用 SSLv3，则可能会受到攻击。Compute Engine 客户需要更新其实例的操作系统映像，以消除这个漏洞。

我们建议您升级 Linux 发行版。对于运行 Debian 的实例，您可以在实例中运行以下命令来执行更新：

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

对于 CentOS 实例，运行：

    
    
    
    user@my-instance:~$ sudo yum -y upgrade
    user@my-instance:~$ sudo reboot

除了运行上述手动更新命令以外，用户现在可以使用以下新映像重新创建其实例：

  * ` centos-6-v20141016 `
  * ` centos-7-v20141016 `
  * ` debian-7-wheezy-v20141017 `
  * ` backports-debian-7-wheezy-v20141017 `

当我们获得 RHEL 和 SLES 的相应映像后，就会更新此公告。同时，RHEL 用户可以 [ 直接咨询 Red Hat
](https://access.redhat.com/articles/1232123) 以获取更多信息。

**原始公告：**

Compute Engine 客户需要更新其实例的操作系统映像，以消除这一漏洞。在获得新的操作系统映像之后，我们将更新此安全公告添加相关说明。

|  中  |  [ CVE-2014-3566
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-3566)  
  
##  发布日期：2014-09-24

**上次更新日期：2014-09-29**

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

bash 中存在一个错误 (CVE-2014-6271)，允许基于对由攻击者控制的任何环境变量的解析来远程执行代码。最有可能的攻击方向是向 Web
服务器上暴露的 CGI 脚本发出恶意 HTTP 请求。如需了解更多信息，请参阅 [ 错误说明 ](http://seclists.org/oss-
sec/2014/q3/650) 。

除了日期为 20140926 之前的 Compute Engine 访客操作系统映像之外，Google Cloud Platform 产品中的 bash
错误问题均已得到缓解。请参阅下面的步骤来缓解 Compute Engine 映像中的这一问题。

####  对 Compute Engine 的影响

这个问题可能会影响所有使用 CGI 脚本的网站。此外，它可能会影响依赖于 PHP、Perl、Python、SSI、Java、C ++ 和类似 servlet
的网站，只要类似的 servlet 将通过诸如 ` popen ` 、 ` system ` 、 ` shell_exec ` 或类似的 API 来调用
shell 命令。它也可能影响那些试图通过诸如 SSH 命令限制或 bash 限制的 shell 等机制，允许受限用户进行受控登录访问的系统。

**更新日期 (2014-09-29)：**

除了运行下列手动更新命令以外，用户现在还可以使用用于缓解与 bash 安全问题相关的其他漏洞的映像重新创建其实例，这些漏洞包括 [
CVE-2014-7169 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169)
、 [ CVE-2014-6277
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277) 、 [
CVE-2014-6278 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278)
、 [ CVE-2014-7186
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186) 和 [
CVE-2014-7187 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)
。使用以下新映像重新创建您的实例：

  * ` centos-6-v20140926 `
  * ` centos-7-v20140926 `
  * ` debian-7-wheezy-v20140926 `
  * ` backports-debian-7-wheezy-v20140926 `
  * ` rhel-6-v20140926 `

**更新日期 (2014-09-25)：**

用户现在可以选择重新创建其实例，而非执行手动更新。如需重新创建实例，请使用以下包含此安全问题修补程序的新映像：

  * ` backports-debian-7-wheezy-v20140924 `
  * ` debian-7-wheezy-v20140924 `
  * ` rhel-6-v20140924 `
  * ` centos-6-v20140924 `
  * ` centos-7-v20140924 `

对于 RHEL 和 SUSE 映像，也可以在实例上运行以下命令来手动执行更新：

    
    
    
    # RHEL instances
    user@my-instance:~$ sudo yum -y upgrade
    
    # SUSE instances
    user@my-instance:~$ sudo zypper --non-interactive up

**原始公告：**

我们建议您升级 Linux 发行版。对于运行 Debian 的实例，可以在实例中运行以下命令来执行更新：

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    

对于 CentOS 实例，运行：

    
    
    
    user@my-instance:~$ sudo yum -y upgrade

如需了解详细信息，请查看相应 Linux 发行版的公告：

  * 原始补丁程序： [ http://ftp.gnu.org/gnu/bash/ ](http://ftp.gnu.org/gnu/bash/) （参见 *-patches 中的最后一个条目以获得适当的版本） 
  * Debian： [ [SECURITY] [DSA 3032-1] bash 安全更新 ](https://lists.debian.org/debian-security-announce/2014/msg00220.html)
  * RHEL： 
    * [ RHSA-2014:1293-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00048.html)
    * [ RHSA-2014:1294-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00049.html)
  * CentOS 5： [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020582.html)
  * CentOS 6： [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020585.html)
  * CentOS 7： [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020583.html)

|  高  |  [ CVE-2014-7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) 、 [
CVE-2014-6271 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6271)
、 [ CVE-2014-6277
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277) 、 [
CVE-2014-6278 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278)
、 [ CVE-2014-7186
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186) 、 [
CVE-2014-7187 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)  
  
##  发布日期：2014-07-25

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

[ Elasticsearch Logstash ](http://www.elasticsearch.org/overview/logstash/)
容易受到操作系统命令注入的攻击，可能允许未经授权地修改和披露数据。攻击者可以将制作好的事件发送到任何 Logstash 的数据源，让攻击者得以使用
Logstash 进程的权限执行命令。

####  对 Compute Engine 的影响

此漏洞会影响所有运行 Elasticsearch Logstash 1.4.2 之前的版本并启用了 zabbix 或 nagios_nsca 输出的
Compute Engine 实例。为了防止攻击，您可以采取以下任一措施：

  * 升级到 Logstash 1.4.2 
  * 应用版本 1.3.x 的补丁程序 
  * 禁用 ` zabbix ` 和 ` nagios_nsca ` 输出。 

在 [ Logstash 博客 ](http://www.elasticsearch.org/blog/logstash-1-4-2/) 中阅读更多信息。

Elasticsearch 还建议 [ 使用防火墙 ](http://www.elasticsearch.org/blog/scripting-
security/) 来防止不受信任的 IP 执行远程访问。

|  高  |  [ CVE-2014-4326
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-4326)  
  
##  发布日期：2014-06-18

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

我们希望用一些时间，回应客户对于在 Google Cloud Platform 上运行 Docker 容器的安全性方面可能存在的一些顾虑。这包括使用我们的
App Engine 扩展程序来支持 Docker 容器、容器优化虚拟机或开源 Kubernetes 调度程序的客户。

Docker 已经很好地回应了这个问题，您可以在 [ 此处 ](http://blog.docker.com/2014/06/docker-
container-breakout-proof-of-concept-exploit/)
看到他们的博客回应。请注意，正如他们在回应中所说的那样，目前发现的问题仅存在于 Docker 0.11，这是一个较早的非正式版本。

虽然全世界都在考虑容器安全性，但我们想指出的是，在 Google Cloud Platform 中，基于 Linux 应用容器（特别是 Docker
容器）的解决方案是在完整的虚拟机 (Compute Engine) 中运行的。尽管我们支持 Docker 社区加强 Linux
应用容器堆栈的努力，但是我们认识到这项技术仍属新生事物，有着较大的受攻击面。就目前而言，我们相信，完整的管理程序（虚拟机）提供了更紧凑、更便于防御的受攻击面。虚拟机设计的初衷，就是为了隔离恶意工作负载，并尽量减少代码错误的可能性和影响。

我们的客户可以放心，他们与任何第三方的潜在恶意代码之间都有着完整的管理程序边界。当我们认为 Linux
应用容器堆栈足够强大可靠，能够支持多租户工作负载时，我们会及时告知社区。目前，Linux 应用容器不会取代虚拟机，而仅仅是一种更充分地利用虚拟机的方法。

|  低  |  [ Docker 博文 ](http://blog.docker.com/2014/06/docker-container-
breakout-proof-of-concept-exploit/)  
  
##  发布日期：2014-06-05

**上次更新日期：2014-06-09**

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

OpenSSL 存在一个问题，导致 ` ChangeCipherSpec `
消息未能正确绑定到握手状态机器。这使得它们可以提前被注入握手。攻击者可以利用精心设计的握手，强制在 OpenSSL SSL/TLS
客户端和服务器中使用弱密钥材料。这可以被中间人 (MITM) 攻击所利用，让攻击者可以解密和修改来自受攻击客户端和服务器的流量。

此问题被标识为 [ CVE-2014-0224 ](https://www.openssl.org/news/secadv/20140605.txt)
。OpenSSL 团队已经解决了这个问题，并提醒 OpenSSL 社区更新 OpenSSL。

####  对 Compute Engine 的影响

此漏洞会影响所有使用 OpenSSL 的Compute Engine 实例，包括 Debian、CentOS、Red Hat Enterprise
Linux 和 SUSE Linux Enterprise Server。您可以通过用新映像重新创建实例进行更新，也可以手动更新实例上的软件包。

**更新日期 (2014-06-09)：** 如需使用新映像更新正在运行 SUSE Linux Enterprise Server
的实例，请使用以下映像版本或更高版本重新创建实例：

  * ` sles-11-sp3-v20140609 `

**原始信息：**

如需使用新映像更新 Debian 和 CentOS 实例，请使用以下任一映像版本或更高版本重新创建实例：

  * ` debian-7-wheezy-v20140605 `
  * ` backports-debian-7-wheezy-v20140605 `
  * ` centos-6-v20140605 `
  * ` rhel-6-v20140605 `

如需在实例上手动更新 OpenSSL，请运行以下命令来更新相应的软件包。对于运行 CentOS 和 RHEL 的实例，可以在实例中运行以下命令来更新
OpenSSL：

    
    
    
    user@my-instance:~$ sudo yum -y update
    user@my-instance:~$ sudo reboot

对于运行 Debian 的实例，可以在实例中运行以下命令来更新 OpenSSL：

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

对于运行 SUSE Linux Enterprise Server 的实例，可以在实例中运行这些命令确保 OpenSSL 升级到最新版本：

    
    
    
    user@my-instance:~$ sudo zypper --non-interactive up
    user@my-instance:~$ sudo reboot

|  中  |  [ CVE-2014-0224
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0224)  
  
##  发布日期：2014-04-08

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

在 OpenSSL 1.0.1g 之前，OpenSSL 1.0.1 中的 (1) TLS 和 (2) DTLS
实现不能正确处理检测信号扩展程序数据包，使得远程攻击者可以通过精心设计的数据包触发缓冲区过度读取，从而从进程内存中获取敏感信息，比如读取与 `
d1_both.c ` 和 ` t1_lib.c ` 相关的私钥，这个问题也称为“心脏出血问题”。

####  对 Compute Engine 的影响

此漏洞会影响所有未安装 OpenSSL 最新版本的 Compute Engine Debian、RHEL 和 CentOS
实例。您可以通过用新映像重新创建实例进行更新，也可以手动更新实例上的软件包。

如需使用新映像更新实例，请使用以下任一映像版本或更高版本重新创建实例：

  * ` debian-7-wheezy-v20140408 `
  * ` backports-debian-7-wheezy-v20140408 `
  * ` centos-6-v20140408 `
  * ` rhel-6-v20140408 `

如需在实例上手动更新 OpenSSL，请运行以下命令来更新相应的软件包。对于运行 CentOS 和 RHEL 的实例，可以在实例中运行以下命令来确保
OpenSSL 为最新版本：

    
    
    
    user@my-instance:~$ sudo yum update
    user@my-instance:~$ sudo reboot

对于运行 Debian 的实例，可以在实例中运行以下命令来更新 OpenSSL：

    
    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get upgrade
    user@my-instance:~$ sudo reboot

运行 SUSE Linux 的实例不受影响。

**2014 年 4 月 14 日更新：** 鉴于针对利用心脏出血错误提取密钥的新研究，Compute Engine 建议其客户为任何受影响的 SSL
服务创建新密钥。

|  中  |  [ CVE-2014-0160
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0160)  
  
##  发布日期：2013-06-07

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

**注意：** 此漏洞仅在自 API v1 版本以来已弃用和移除的内核中出现。

Linux 内核 3.9.4 及以下版本中，Broadcom B43 无线网络驱动程序的 ` drivers/net/wireless/b43/main.c
` 文件内的 ` b43_request_firmware ` 函数存在格式化字符串漏洞，使得本地用户可利用 root 访问权限以及在 `
fwpostfix ` modprobe 参数中包含格式化字符串说明符来获得特权，导致不正确的错误消息构造。

####  对 Compute Engine 的影响

此漏洞会影响 ` gcg-3.3.8-201305291443 ` 之前的所有 Compute Engine 内核。作为回应，Compute Engine
已弃用所有较早的内核，并建议用户更新其实例和映像以使用 Compute Engine 内核 ` gce-v20130603 ` 。 `
gce-v20130603 ` 包含内核 ` gcg-3.3.8-201305291443 ` ，该内核有此漏洞的补丁程序。

如需确定实例正在使用的内核版本，请执行以下操作：

  1. 通过 ssh 连接到实例 
  2. 运行 ` uname -r `

|  中  |  [ CVE-2013-2852
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2852)  
  
##  发布日期：2013-06-07

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

**注意：** 此漏洞仅在自 API v1 版本以来已弃用和移除的内核中出现。

Linux 内核 3.9.4 及以下版本中， ` block/genhd.c ` 文件内的 register_disk
函数存在格式化字符串漏洞，使得本地用户可利用 root 访问权限以及向 ` /sys/module/md_mod/parameters/new_array
` 写入格式化字符串说明符来获得特权，从而创建捏造的 ` /dev/md ` 设备名称。

####  对 Compute Engine 的影响

此漏洞会影响 ` gcg-3.3.8-201305291443 ` 之前的所有 Compute Engine 内核。作为回应，Compute Engine
已弃用所有较早的内核，并建议用户更新其实例和映像以使用 Compute Engine 内核 ` gce-v20130603 ` 。 `
gce-v20130603 ` 包含内核 ` gcg-3.3.8-201305291443 ` ，该内核有此漏洞的补丁程序。

如需确定实例正在使用的内核版本，请执行以下操作：

  1. 通过 ssh 连接到实例 
  2. 运行 ` uname -r `

|  中  |  [ CVE-2013-2851
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2851)  
  
##  发布日期：2013-05-14

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

**注意：** 此漏洞仅在自 API v1 版本以来已弃用和移除的内核中出现。

3.8.9 版本之前的 Linux 内核中， ` kernel/events/core.c ` 文件内的 perf_swevent_init
函数使用不正确的 ` integer ` 数据类型，使得本地用户可通过恶意创建的 ` perf_event_open ` 系统调用来获得特权。

####  对 Compute Engine 的影响

此漏洞会影响 ` gcg-3.3.8-201305211623 ` 之前的所有 Compute Engine 内核。作为回应，Compute Engine
已弃用所有较早的内核，并建议用户更新其实例和映像以使用 Compute Engine 内核 ` gce-v20130521 ` 。 `
gce-v20130521 ` 包含内核 ` gcg-3.3.8-201305211623 ` ，该内核有此漏洞的补丁程序。

如需确定实例正在使用的内核版本，请执行以下操作：

  1. 通过 ssh 连接到实例 
  2. 运行 ` uname -r `

|  高  |  [ CVE-2013-2094
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2094)  
  
##  发布日期：2013-02-18

说明  |  严重级别  |  备注  
---|---|---  
  
####  说明

**注意：** 此漏洞仅在自 API v1 版本以来已弃用和移除的内核中出现。

3.7.5 版本之前的 Linux 内核中的 ptrace 功能存在争用条件，使得本地用户可通过恶意创建的应用程序中的 ` PTRACE_SETREGS
ptrace ` 系统调用来获得特权。

####  对 Compute Engine 的影响

此漏洞会影响 Compute Engine 内核 ` 2.6.x-gcg- _ <date> _ ` 。作为回应，Compute Engine 已弃用
2.6.x 的内核，并建议用户更新其实例和映像以使用 Compute Engine 内核 ` gce-v20130225 ` 。 `
gce-v20130225 ` 包含内核 ` 3.3.8-gcg-201302081521 ` ，该内核有针对此漏洞的补丁程序。

如需确定实例正在使用的内核版本，请执行以下操作：

  1. 通过 ssh 连接到实例 
  2. 运行 ` uname -r `

|  中  |  [ CVE-2013-0871
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-0871)

