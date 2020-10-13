#  安全公告

本主题介绍了 Google Kubernetes Engine (GKE) 的所有安全公告。

漏洞通常有一段时间的保密期，以便给让影响的各方有机会解决这些问题。在这种情况下，GKE 的 [ 版本说明
](https://cloud.google.com/kubernetes-engine/docs/release-notes?hl=zh_cn)
会在保密期结束前使用“安全更新”来泛指这些漏洞。保密期结束后，我们会更新版本说明，以阐明补丁程序所解决的漏洞。

**注意** ：如果您在 GKE 上运行多租户工作负载，请特别注意这些公告。这些漏洞更有可能影响到多租户工作负载。有关 GKE
中安全边界的技术说明以及这些安全边界对工作负载的影响，请参阅 [ Kubernetes 栈中不同层的隔离
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) 。

如需接收最新安全公告，请将本页面的网址添加到您的 [ Feed 阅读器
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ，或直接添加 Feed 网址： `
https://cloud.google.com/feeds/kubernetes-engine-security-bulletins.xml `

##  GCP-2020-011

**发布日期** ：2020-07-24  
说明  |  严重级别  |  备注  
---|---|---  
  
最近在 Kubernetes 中发现了一个网络漏洞 [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) 。服务有时会使用本地环回接口
(127.0.0.1) 与同一 pod 中运行的其他应用通信。利用此漏洞，有权访问集群网络的攻击者能够将流量发送到相邻 Pod
和节点的环回接口。如果服务依赖于无法在其 Pod 之外访问的环回接口，则攻击者可以利用这些服务。

要在 GKE 集群上利用此漏洞，攻击者需要拥有托管集群 VPC 的 Google Cloud
的网络管理员权限。此漏洞本身并不会授予攻击者网络管理员权限。因此，对于 GKE，此漏洞的严重级别分配为低。

####  该怎么做？

要修复此漏洞，请将集群的节点池 [ 升级 ](https://cloud.google.com/kubernetes-
engine/docs/concepts/cluster-upgrades?hl=zh_cn) 到以下 GKE 版本（及更高版本）：

  * 1.17.7-gke.0 
  * 1.16.11-gke.0 
  * 1.16.10-gke.11 
  * 1.16.9-gke.14 

####  该补丁程序解决了哪一漏洞？

这些补丁程序修复了以下漏洞： [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) 。

|

低

|

[ CVE-2020-8558 ](https://github.com/kubernetes/kubernetes/issues/92315)  
  
##  GCP-2020-009

**发布日期** ：2020-07-15  说明  |  严重级别  |  备注  
---|---|---  
  
最近在 Kubernetes 中发现了一个提权漏洞 [ CVE-2020-8559 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8559) 。利用此漏洞，已破解节点的攻击者能够在集群中的任何 Pod
中执行命令。因此，攻击者可以使用已被破解的节点来破解其他节点并且可能读取信息，或者导致破坏性操作。

请注意，集群中的某个节点必须已被破解，攻击者才能利用此漏洞。此漏洞本身不会破解集群中的任何节点。

####  该怎么做？

将集群 [ 升级 ](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-
upgrades?hl=zh_cn) 到修补后的版本。集群将在接下来的几周内自动升级，修补后的版本将在 2020 年 7 月 19
日之前提供，以提高手动升级计划速度。以下 GKE 控制层面版本或更新版本包含针对此漏洞的修复：

  * v1.14.10-gke.46 
  * v1.15.12-gke.8 
  * v1.16.9-gke.11 
  * v1.16.10-gke.9 
  * v1.16.11-gke.3+ 
  * v1.17.7-gke.6+ 

####  该补丁程序解决了哪一漏洞？

这些补丁程序解决了漏洞 CVE-2020-8559。此漏洞被评为 GKE
的中危漏洞，因为除了现有已遭破解的节点之外，攻击者还需要拥有集群、节点和工作负载的第一手信息，才能有效利用此攻击。此漏洞本身不会为攻击者提供已遭破解的节点。

|

中

|

[ CVE-2020-8559 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8559)  
  
##  GCP-2020-007

**发布日期：** 2020-06-01  
说明  |  严重级别  |  备注  
---|---|---  
  
近期在 Kubernetes 中发现了一个服务器端请求伪造 (SSRF) 漏洞 ( [ CVE-2020-8555
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555)
)，该漏洞会导致某些已获授权的用户从控制平面主机网络中泄露多达 500 字节的敏感信息。Google Kubernetes Engine (GKE)
控制平面使用的是 Kubernetes 的控制器，所有 Kubernetes Engine 节点都会受到此漏洞的影响，我们建议您将控制平面 [ 升级
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=zh_cn) 到最新的补丁程序版本，具体说明如下所述。不需要升级节点。  

####  该怎么做？

大多数客户无需执行任何额外操作。绝大多数集群已在运行修补版本。 以下 GKE 版本或更高版本包含针对此漏洞的修补程序：

  * 1.14.7-gke.39 
  * 1.14.8-gke.32 
  * 1.14.9-gke.17 
  * 1.14.10-gke.12 
  * 1.15.7-gke.17 
  * 1.16.4-gke.21 
  * 1.17.0-gke.0 

使用 [ 发布渠道 ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-
channels?hl=zh_cn) 的集群已在采取了缓解措施的控制平面版本上运行。

####  该补丁程序解决了哪一漏洞？

这些补丁程序解决了漏洞 CVE-2020-8555。此漏洞被评为 GKE 的中危漏洞，由于各种控制平面安全强化措施的实施而很难被利用。

有权创建内置了卷类型（GlusterFS、Quobyte、StorageFS、ScaleIO）的 Pod 的攻击者或有权创建 StorageClass
的攻击者可以使 ` kube-controller-manager ` 发出 ` GET ` 请求或 ` POST `
请求，而无需通过主实例的主机网络控制请求正文 __ 。这些卷类型在 GKE 上很少使用，因此重新使用这些卷类型可能是一个有用的检测信号。

如果与重新向攻击者泄露 ` GET/POST `
结果的方法结合使用（例如通过日志），则可能会导致敏感信息被披露。我们更新了相关的存储驱动程序，以消除发生此类泄露的可能性。

|

中

|

[ CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555)  
  
##  GCP-2020-006

**发布日期：** 2020-06-01  
说明  |  严重级别  |  备注  
---|---|---  
  
Kubernetes 披露了一个 [ 漏洞 ](https://github.com/kubernetes/kubernetes/issues/91507)
，该漏洞允许特权容器将节点流量重定向至其他容器。此攻击无法读取或修改双向 TLS/SSH 流量（例如 kubelet 与 API
服务器之间的流量）或来自使用 mTLS 的应用的流量。所有 Google Kubernetes Engine (GKE)
节点都会受到此漏洞的影响，我们建议您 [ 升级 ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=zh_cn) 到最新的补丁程序版本，具体说明如下所述。

####  该怎么做？

要解决此漏洞，请 [ 升级 ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=zh_cn)
您的控制平面，然后将您的节点升级为下面列出的一个修补版本。使用发布渠道的集群已同时在控制平面和节点上运行修补版本：

  * 1.14.10-gke.36 
  * 1.15.11-gke.15 
  * 1.16.8-gke.15 

通常，很少有容器需要 ` CAP_NET_RAW ` 。默认情况下，应该通过 [ PodSecurityPolicy
](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-
policies?hl=zh_cn) 或 [ Anthos 政策控制器 ](https://cloud.google.com/anthos-config-
management/docs/concepts/policy-controller?hl=zh_cn) 阻止此功能和其他强大的功能：

  * 从容器中删除 ` CAP_NET_RAW ` 功能： 
    * 使用以下命令，通过 [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=zh_cn) 强制执行此操作： 
        
                
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
        

    * 或者将 Anthos 政策控制器/Gatekeeper 与此 [ 限制条件模板 ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) 结合使用，并加以应用，例如： 
        
                
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
        

    * 或者更新您的 Pod 规范： 
        
                
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
        

####  该补丁程序解决了哪一漏洞？

该补丁程序解决了以下漏洞：

[ Kubernetes 问题 91507 ](https://github.com/kubernetes/kubernetes/issues/91507)
中所述的漏洞 ` CAP_NET_RAW ` 功能（包含在默认容器功能集中）会在节点上恶意配置 IPv6
堆栈，并将节点流量重定向至攻击者控制的容器。这样一来，攻击者就可以拦截/修改源自或发送至该节点的流量。此攻击无法读取或修改双向 TLS/SSH 流量（例如
kubelet 与 API 服务器之间）或来自使用 mTLS 的应用的流量。

|

中

|

[ Kubernetes 问题 91507 ](https://github.com/kubernetes/kubernetes/issues/91507)  
  
  
##  GCP-2020-005

**发布日期** ：2020 年 5 月 7 日  
**更新日期** ：2020 年 5 月 7 日  说明  |  严重级别  |  备注  
---|---|---  
  
近期在 Linux 内核中发现了一个漏洞（如 [ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) 中所述），该漏洞允许容器逃逸，从而获得主机节点上的 root 权限。

运行 GKE 1.16 或 1.17 版本的 Google Kubernetes Engine (GKE) Ubuntu
节点均受此漏洞影响，我们建议您按照下文详述的方法，尽快升级到最新补丁程序版本。

运行 Container-Optimized OS 的节点不受影响。在 GKE On-Prem 上运行的节点不受影响。

####  该怎么做？

**大多数客户无需执行任何额外操作。只有使用 GKE 1.16 或 1.17 版本且运行 Ubuntu 的节点会受到影响。**

若要升级节点，您必须先将主实例升级到最新版本。Kubernetes 1.16.8-gke.12、1.17.4-gke.10
及更新的版本中提供了该补丁程序。在 [ 版本说明 ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=zh_cn) 中可以跟踪这些补丁程序的提供情况。

####  该补丁程序解决了哪一漏洞？

该补丁程序解决了以下漏洞：

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) 描述了 Linux 内核 5.5.0
版本及更新版本中的一个漏洞，该漏洞允许恶意容器（只需极少的用户互动，执行一次 exec 即可触发）读写内核内存，从而获得主机节点上的 root
级代码执行权限。此漏洞的严重级别分级为“高”。

|

高

|

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835)  
  
  
##  GCP-2020-003

**发布日期** ：2020 年 3 月 31 日  
**更新日期** ：2020 年 3 月 31 日  说明  |  严重级别  |  备注  
---|---|---  
  
近期在 Kubernetes 中发现了一个漏洞（如 [ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) 中所述），该漏洞导致任何有权发出 POST 请求的用户都可以对
Kubernetes API 服务器执行远程拒绝服务攻击。Kubernetes 产品安全委员会 (PSC) 已经发布了有关此漏洞的更多信息，详见 [ 此处
](https://groups.google.com/forum/?hl=zh_cn#!topic/kubernetes-security-
announce/wuwEwZigXBc) 。

使用 [ 主授权网络 ](https://cloud.google.com/kubernetes-engine/docs/how-
to/authorized-networks?hl=zh_cn) 的 GKE 集群和 [ 无公共端点的专用集群
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=zh_cn#private_master) 可缓解此漏洞。

####  该怎么做？

建议您将集群升级为包含针对此漏洞的修补程序的版本。

包含此修补程序的版本如下所示：

  * 1.13.12-gke.29 
  * 1.14.9-gke.27 
  * 1.14.10-gke.24 
  * 1.15.9-gke.20 
  * 1.16.6-gke.1 

####  该补丁程序解决了哪些漏洞？

该补丁程序修复了以下拒绝服务攻击 (DoS) 漏洞：

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) 。

|

中

|

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  GCP-2020-002

**发布日期** ：2020 年 3 月 23 日  
**更新日期** ：2020 年 3 月 23 日  说明  |  严重级别  |  备注  
---|---|---  
  
Kubernetes 披露了 [ 两个拒绝服务攻击漏洞
](https://groups.google.com/forum/?hl=zh_cn#!topic/kubernetes-security-
announce/2UOlsba2g0s) ，一个影响 API 服务器，另一个影响 Kubelet。如需了解详情，请参见 Kubernetes 问题 [
89377 ](https://github.com/kubernetes/kubernetes/issues/89377) 和 [ 89378
](https://github.com/kubernetes/kubernetes/issues/89378) 。

####  该怎么做？

所有 GKE 用户均已受到针对 CVE-2020-8551 的保护，唯一有风险的情况就是不受信任的用户能从集群的内部网络中发送请求。使用 [ 主授权网络
](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-
networks?hl=zh_cn) 可针对 CVE-2020-8552 提供额外的缓解措施。

####  何时会推出针对这些漏洞的补丁程序？

针对 CVE-2020-8551 的补丁程序要求进行节点升级。下面列出了将包含缓解措施的补丁程序版本：

  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

注意：版本 1.14.x 和更早的版本不受此漏洞的影响，因此无需补丁程序。

针对 CVE-2020-8552 的补丁程序需要进行主节点升级。下面列出了将包含缓解措施的补丁程序版本：

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
  
##  2020 年 1 月 21 日；上次更新时间：2020 年 1 月 24 日

**发布日期** ：2020 年 1 月 21 日  
**更新日期** ：2020 年 1 月 24 日  说明  |  严重级别  |  备注  
---|---|---  
  
**2020 年 1 月 24 日更新** ：我们正在推出修补版本，此过程将在 2020 年 1 月 25 日完成。

* * *

Microsoft 披露了 Windows Crypto API 及其对椭圆曲线签名的验证中的一个漏洞。如需了解详情，请参阅 [ Microsoft
披露信息 ](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) 。

**该怎么做？**

**大多数客户无需执行任何额外操作。只有运行 Windows Server 的节点会受影响。**

对使用 Windows Server 节点的客户而言，节点以及在这些节点上运行的容器化工作负载都必须更新到修补版本以缓解此漏洞。

**如需更新容器，请执行以下操作：**

使用 Microsoft 的最新基础容器映像重新构建容器，请选择上次更新时间为 2020 年 1 月 14 日或更晚日期的 [ servercore
](https://hub.docker.com/_/microsoft-windows-servercore) 或 [ nanoserver
](https://hub.docker.com/_/microsoft-windows-nanoserver) 标记。

**如需更新节点，请执行以下操作：**

我们正在推出修补版本，此过程将在 2020 年 1 月 24 日完成。

届时，您可以将节点升级为 GKE 修补版本，也可以随时使用 Windows 更新手动部署最新的 Windows 补丁程序。

下面列出了将包含缓解措施的补丁程序版本：

  * 1.14.7-gke.40 
  * 1.14.8-gke.33 
  * 1.14.9-gke.23 
  * 1.14.10-gke.17 
  * 1.15.7-gke.23 
  * 1.16.4-gke.22 

**该补丁程序解决了哪些漏洞？**

该补丁程序缓解了以下漏洞：

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601) \- 此漏洞又称为 [ Windows Crypto API 仿冒漏洞
](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601)
，攻击者可以利用此漏洞将恶意可执行文件伪装成受信任的程序，或者发动中间人攻击并解密与受影响软件的 TLS 连接相关的机密信息。

|

NVD 基本得分：8.1（高）

|

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601)  
  
  
##  2019 年 11 月 14 日

**发布日期** ：2019 年 11 月 14 日  
**更新日期** ：2019 年 11 月 14 日  说明  |  严重级别  |  备注  
---|---|---  
  
Kubernetes 披露了 kubernetes-csi [ ` external-provisioner `
](https://github.com/kubernetes-csi/external-provisioner) 、 [ ` external-
snapshotter ` ](https://github.com/kubernetes-csi/external-snapshotter) 和 [ `
external-resizer ` ](https://github.com/kubernetes-csi/external-resizer)
Sidecar 中存在的一个安全问题，此问题会影响到 [ 容器存储接口 (CSI) 驱动程序 ](https://kubernetes-
csi.github.io/docs/drivers.html) 中捆绑的 Sidecar 的大多数版本。如需了解详情，请参阅 [ Kubernetes
披露信息 ](https://github.com/kubernetes/kubernetes/issues/85233) 。

**该怎么做？**  
**此漏洞不会影响任何代管 GKE 组件** 。 如果您在运行 GKE 1.12 版或更高版本的 [ GKE Alpha 版集群
](https://cloud.google.com/kubernetes-engine/docs/concepts/alpha-
clusters?hl=zh_cn) 中管理自己的 CSI 驱动程序，则可能会受此漏洞影响。如果您受到影响，请联系您的 CSI
驱动程序供应商，以获得升级说明。

**该补丁程序解决了哪些漏洞？**  
[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255) ：此 CVE 是 ` kubernetes-csi ` [ ` external-
provisioner ` ](https://github.com/kubernetes-csi/external-provisioner) 、 [ `
external-snapshotter ` ](https://github.com/kubernetes-csi/external-
snapshotter) 和 [ ` external-resizer ` ](https://github.com/kubernetes-
csi/external-resizer) Sidecar 中的一个漏洞，可能允许未经授权的卷数据访问或突变。这会影响到 [ CSI 驱动程序
](https://kubernetes-csi.github.io/docs/drivers.html) 内捆绑的 Sidecar 的大多数版本。

|

中

|

[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255)  
  
  
##  2019 年 11 月 12 日

**发布日期** ：2019 年 11 月 12 日  
**更新日期** ：2019 年 11 月 12 日  说明  |  严重级别  |  备注  
---|---|---  
  
Intel 披露了多个可能允许在推测性执行与微架构状态之间进行交互，从而导致数据泄露的 CVE。如需了解详情，请参阅 [ Intel 披露信息
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) 。

**运行 Kubernetes Engine 的主机基础架构会将客户工作负载彼此隔离。除非您在自己的多租户 GKE 集群内运行不受信任的代码，并且 __
在使用 N2、M2 或 C2 节点，否则无需执行进一步操作。 ** N1 节点上的 GKE 实例无需采取新的操作。

如果您运行的是 Anthos GKE On-Prem，则数据泄露的可能性取决于所用的硬件。请将您的基础架构与 [ Intel 披露信息
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) 对照比较。

####  该怎么做？

**只有在您使用包含 N2、M2 或 C2 节点的节点池并且 __ 这些节点在您自己的多租户 GKE 集群内运行不受信任的代码时，您才会受到影响。 **

**重启您的节点以应用补丁程序。** 如需重启节点池中的所有节点，最简单的方法就是使用 [ 升级
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=zh_cn#upgrade_nodes) 操作，强制所有受影响的节点池中的节点重启。  

注意：在升级过程中，您不需要更改版本。您可以使用 ` cluster-version ` 标志，启动到相同节点版本的升级。

####  该补丁程序解决了哪些漏洞？

该补丁程序缓解了以下漏洞：

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)
：此 CVE 也称为 TSX 异步中止 (TAA)。TAA 提供了使用与 [ 微架构数据抽样 (MDS)
](https://cloud.google.com/kubernetes-engine/docs/security-
bulletins?hl=zh_cn#may-14-2019) 相同的微架构数据结构实现数据渗漏的另一种途径。

[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)
这是一种影响虚拟机主机的拒绝服务攻击 (DoS) 漏洞，允许恶意客机导致未受保护的主机崩溃。此 CVE 也称为“页面大小更改时机器检查错误”。此问题不会影响
GKE。

|

中

|

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)  
[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)  
  
##  2019 年 10 月 22 日

**发布日期** ：2019 年 10 月 22 日  
**更新日期** ：2019 年 10 月 22 日  说明  |  严重级别  |  备注  
---|---|---  
  
[ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276) 描述了近期在 Go 编程语言中发现的一个漏洞。此漏洞可能会影响使用身份验证代理的
Kubernetes 配置。如需了解详情，请参阅 [ Kubernetes 披露信息
](https://groups.google.com/forum/?hl=zh_cn#!topic/kubernetes-security-
announce/PtsUCqFi4h4) 。

Kubernetes Engine 不允许配置身份验证代理，因此不会受到此漏洞的影响。

|

无

|

[ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276)  
  
  
##  2019 年 10 月 16 日

**发布日期** ：2019 年 10 月 16 日  
**更新日期** ：2019 年 10 月 24 日  说明  |  严重级别  |  备注  
---|---|---  
  
**2019 年 10 月 24 日更新** ：经过修补的版本现已在所有区域推出。

* * *

近期在 Kubernetes 中发现了一个漏洞（如 [ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) 中所述），该漏洞导致任何有权发出 POST 请求的用户都可以在
Kubernetes API 服务器上执行远程拒绝服务攻击。Kubernetes 产品安全委员会 (PSC) 已经发布了有关此漏洞的更多信息，详见 [ 此处
](https://groups.google.com/forum/?hl=zh_cn#!topic/kubernetes-security-
announce/jk8polzSUxs) 。

GKE 集群可使用 [ 主授权网络 ](https://cloud.google.com/kubernetes-engine/docs/how-
to/authorized-networks?hl=zh_cn) 和 [ 无公共端点的专用集群
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters?hl=zh_cn#private_master) 缓解此漏洞。

######  该怎么做？

我们建议您在包含修复方案的补丁程序版本发布后，尽快将集群升级到相应补丁程序版本。我们预计，它们将在 10 月 14 日那一周按计划发布的 GKE
版本中推出，届时将可供所有区域使用。

下面列出了将包含缓解措施的补丁程序版本：

  * 1.12.10-gke.15 
  * 1.13.11-gke.5 
  * 1.14.7-gke.10 
  * 1.15.4-gke.15 

######  该补丁程序解决了哪些漏洞？

该补丁程序缓解了以下漏洞：

CVE-2019-11253 是一种拒绝服务攻击 (DoS) 漏洞。

|

高

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
  
##  2019 年 9 月 16 日

**发布日期** ：2019 年 9 月 16 日  
**更新日期** ：2019 年 10 月 16 日  说明  |  严重级别  |  备注  
---|---|---  
  
此公告在原始发布版本的基础上进行了更新。

Go 编程语言近期被发现存在新的安全漏洞 [ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) 和 [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) ，两者均属于拒绝服务攻击
(DoS) 漏洞。在 GKE 中，这些漏洞可能允许用户编写恶意请求，占用 Kubernetes API 服务器的大量 CPU
资源，有可能降低集群控制平面的可用性。如需了解详情，请参阅 [ Go 编程语言披露信息
](https://groups.google.com/forum/?hl=zh_cn#!topic/golang-
announce/65QixT3tcmg) 。

######  该怎么做？

在包含针对此漏洞的缓解措施的最新补丁程序版本发布后，我们建议您尽快将集群升级到相应的补丁程序版本。根据 [ 发布时间表
](https://cloud.google.com/kubernetes-engine/docs/release-notes-
archive?hl=zh_cn#september_16_2019) ，我们预计这些补丁程序版本将随下个 GKE 版本一起在所有区域推出。

下面列出了将包含缓解措施的补丁程序版本：

  * **2019 年 10 月 16 日更新** ：1.12.10-gke.15 
  * 1.13.10-gke.0 
  * 1.14.6-gke.1 

######  该补丁程序解决了哪一漏洞？

该补丁程序缓解了以下漏洞：

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) 和 [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) 属于拒绝服务攻击 (DoS)
漏洞。

|

高

|

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512)  
[ CVE-2019-9514 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9514)  
  
  
##  2019 年 9 月 5 日

**发布日期** ：2019 年 9 月 5 日  
**更新日期** ：2019 年 9 月 5 日

修复  2019 年 5 月 31 日  的安全公告内记录的漏洞的公告已更新。

##  2019 年 8 月 22 日

**发布日期** ：2019 年 8 月 22 日  
**更新日期** ：2019 年 8 月 22 日

2019 年 8 月 5 日  的公告已更新。 先前发布的一则公告中记录的漏洞的修复已 [ 发布
](https://cloud.google.com/kubernetes-engine/docs/release-notes-
archive?hl=zh_cn#august_22_2019) 。

##  2019 年 8 月 8 日

**发布日期** ：2019 年 8 月 8 日  
**更新日期** ：2019 年 8 月 8 日

2019 年 8 月 5 日  的公告已更新。 我们预计，该公告中记录的漏洞的修复将在下个版本的 GKE 中提供。

##  2019 年 8 月 5 日

**发布日期** ：2019 年 8 月 5 日  
**更新日期** ：2019 年 8 月 9 日  说明  |  严重级别  |  备注  
---|---|---  
  
此公告在原始发布版本的基础上进行了更新。

Kubernetes 最近发现了一个漏洞 ( [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) )，该漏洞允许集群级的 [ 自定义资源
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) 实例像存在于所有命名空间内的有命名空间对象一样得到处理。这意味着仅有命名空间级 RBAC
权限的用户和服务帐号可以与集群级自定义资源交互。利用此漏洞要求攻击者具有访问任意命名空间内资源的权限。

######  该怎么做？

在包含此漏洞缓解措施的最新补丁程序版本发布后，建议您尽快将集群 [ 升级 ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=zh_cn) 到该补丁程序版本。我们预计，它们将随下个 GKE
版本在所有区域提供。下面列出了将包含缓解措施的补丁程序版本：

  * 1.11.10-gke.6 
  * 1.12.9-gke.13 
  * 1.13.7-gke.19 
  * 1.14.3-gke.10（ [ 快速版 ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels?hl=zh_cn) ） 

######  该补丁程序解决了哪一漏洞？

该补丁程序缓解了以下漏洞： [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) 。

|

中

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)  
  
##  2019 年 7 月 3 日

**发布日期** ：2019 年 7 月 3 日  
**更新日期** ：2019 年 7 月 3 日  说明  |  严重级别  |  备注  
---|---|---  
  
解决 CVE-2019-11246 的 ` kubectl ` 修补版本将随 [ ` gcloud ` 253.0.0
](https://cloud.google.com/sdk/docs/release-notes?hl=zh_cn#kubernetes_engine)
一起提供。 如需了解详情，请参阅  2019 年 6 月 25 日的安全公告  。

**注意** ：该补丁程序在 ` kubectl ` 1.11.10 中不可用。

|

高

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  2019 年 7 月 3 日

**发布日期** ：2019 年 6 月 25 日  
**更新日期** ：2019 年 7 月 3 日  说明  |  严重级别  |  备注  
---|---|---  
  
######  2019 年 7 月 3 日更新

在我们上次更新此公告时，1.11.9 版和 1.11.10 版的补丁程序尚不可用。现在，我们已经发布了 1.11.10-gke.5，作为这两个 1.11
版本的升级目标。

目前，GKE 主实例已得到修补，运行 Kubernetes Engine 的 Google 基础架构已得到修补，提供了抵御此漏洞的保护机制。

1.11 主实例将很快弃用，并计划于 2019 年 7 月 8 日这一周自动升级到 1.12 版本。您可以选择以下任意推荐操作，将节点升级到经过修补的版本。

  * 在 2019 年 7 月 8 日之前，将节点升级到 1.11.10-gke.5。在此日期之后，我们会开始将 1.11 版本从可用升级目标列表中移除。 
  * 在 1.11 节点上启用 [ 自动升级 ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades?hl=zh_cn) ，允许主实例升级到 1.12 时升级这些节点。 
  * 执行 [ 手动升级 ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=zh_cn) ，将主实例和这些节点升级到已修复的 1.12 版本。 

2019 年 6 月 24 日发布的原始公告如下：

* * *

######  2019 年 6 月 24 日更新

截至 2019 年 6 月 22 日 21:40（世界协调时间 (UTC)），我们提供了以下经过修补的 Kubernetes 版本。版本介于
Kubernetes 1.11.0 与 1.13.6
之间的主实例将自动更新到修补后的版本。如果您运行的版本不兼容此补丁程序，请先将主实例升级到兼容的版本（参见下方列表），然后再升级节点。

**由于这些漏洞的严重性，无论您是否启用了节点自动升级，我们都建议您尽快执行[ 手动升级
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=zh_cn) ，将您的节点和主实例升级到下列版本之一。 **

已修补的版本：

  * 1.11.8-gke.10 
  * 1.12.7-gke.24 
  * 1.12.8-gke.10 
  * 1.13.6-gke.13 

2019 年 6 月 18 日发布的原始公告如下：

* * *

Netflix 近来披露了 Linux 内核中的三个 TCP 漏洞：

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

这些 CVE 统称为 [ NFLX-2019-001 ](https://github.com/Netflix/security-
bulletins/blob/master/advisories/third-party/2019-001.md) 。

未经修补的 Linux 内核可能很容易受到远程触发的拒绝服务攻击。 **发送或接收不受信任的网络流量的 Google Kubernetes Engine
节点会受到影响，我们建议您按照下方的缓解步骤保护您的工作负载。**

######  Kubernetes 主实例

  * 使用 [ 授权网络 ](https://cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks?hl=zh_cn) ，将流量限制为与受信任网络之间的流量的 Kubernetes 主实例不受影响。 

  * 由 Google 管理的 GKE 集群主实例将在未来几天内自动得到修补。客户无需采取任何行动。 

######  Kubernetes 节点

将流量限制为与受信任网络之间的流量的节点不受影响。符合以下条件的集群属于这种情形：

  * 通过防火墙禁止与不受信任的网络之间通信的节点，或者没有公共 IP 地址的节点（ [ 私有集群 ](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters?hl=zh_cn) ） 
  * 没有公共 LoadBalancer 服务的集群 

Google 正在准备这些漏洞的永久性缓解措施，并将作为新节点版本推出。在永久性修复措施可用后，我们将更新本公告，也会向所有 GKE 客户发送一封电子邮件。

在永久性修复措施推出之前，我们创建了一个 Kubernetes DaemonSet，通过修改主机 ` iptables ` 配置实施缓解措施。

#####  该怎么做？

请运行以下命令，在您的集群的所有节点上应用 Kubernetes DaemonSet。这会向节点上的现有 ` iptables ` 规则中添加一条 `
iptables ` 规则，缓解该漏洞。 **为每个 Google Cloud 项目的每个集群运行一次该命令。**

    
    
    
    kubectl apply -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

由于 GKE 不支持 Ipv6，无需 ip6tables 规则。

在经过修补的节点版本可用，并且您升级了所有可能受影响的节点之后，即可使用如下命令移除 DaemonSet。 **为每个 Google Cloud
项目的每个集群运行一次该命令。**

    
    
    
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

说明  |  严重级别  |  备注  
---|---|---  
  
**2019 年 7 月 3 日更新** ：此补丁程序在 ` gcloud ` 253.0.0 中可用，适用于 ` kubectl `
1.12.9、1.13.6、1.14.2 和更新版本。

**注意** ：该补丁程序在 1.11.10 中不可用。

* * *

Kubernetes 近期发现了一个漏洞 ( [ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) )，它允许具有容器内的 ` kubectl cp `
操作和代码执行访问权限的攻击者修改主机上的文件。此漏洞可能允许攻击者在主机文件系统中替换或创建文件。如需了解详情，请参阅 [ Kubernetes 披露信息
](https://groups.google.com/forum/?hl=zh_cn#!topic/kubernetes-security-
announce/NLs2TGbfPdo) 。

**所有 Google Kubernetes Engine (GKE)` gcloud ` 版本都会受到此漏洞的影响，我们建议您在 ` gcloud `
的最新补丁程序版本推出后升级到该补丁程序版本。 ** 即将推出的补丁程序版本将包含针对此漏洞的缓解措施。

######  该怎么做？

在即将推出的 ` gcloud ` 版本中将提供经过修补的 ` kubectl ` 版本。您还可以自行 [ 直接升级 ` kubectl `
](https://kubernetes.io/docs/tasks/tools/install-kubectl/) 。

在 [ ` gcloud ` 版本说明 ](https://cloud.google.com/sdk/docs/release-
notes?hl=zh_cn) 中可以跟踪此补丁程序的可用情况。

######  该补丁程序解决了哪一漏洞？

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) 漏洞允许具有容器内的 ` kubectl cp `
操作和代码执行访问权限的攻击者修改主机上的文件。此漏洞可能允许攻击者在主机文件系统中替换或创建文件

|

高

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  2019 年 6 月 18 日

说明  |  严重级别  |  备注  
---|---|---  
  
Docker 近期发现存在一个漏洞 ( [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) )，它允许能够在容器内执行代码的攻击者劫持外部发起的 ` docker cp `
操作。此漏洞可能允许攻击者将文件写入位置更改为主机文件系统中的任意位置。

**运行 Docker 的所有 Google Kubernetes Engine (GKE)
节点均受此漏洞影响，我们建议您在最新补丁程序版本推出后升级到该补丁程序版本。即将推出的补丁程序版本将包含针对此漏洞的缓解措施。**

**版本早于 1.12.7 的所有 Google Kubernetes Engine (GKE) 主实例都在运行 Docker，会受到此漏洞的影响。** 在
GKE 上，用户不具备主实例上 ` docker cp ` 的访问权限，因此该漏洞给 GKE 主实例造成的风险有限。

#####  该怎么做？

只有在节点运行 Docker 并且发出有可能被劫持的 ` docker cp ` （或 API 等效）命令时，此类节点才会受到影响。
我们预计，Kubernetes 环境满足这些条件的情况非常少见。 运行 [ 带有 containerd 的 COS
](https://cloud.google.com/kubernetes-engine/docs/concepts/using-
containerd?hl=zh_cn) 的节点不受影响。

如需升级节点，您必须首先 [ 将主实例升级 ](https://cloud.google.com/kubernetes-engine/docs/how-
to/upgrading-a-cluster?hl=zh_cn#upgrading_the_cluster)
为经过修补的版本。在补丁程序可用时，您可以发起主实例升级，也可以等待 Google 自动升级主实例。该补丁程序将在 Docker 18.09.7
中提供，并且会包含在即将发布的 GKE 补丁程序中。 **此补丁程序仅适用于 GKE 1.13 及更高版本。**

我们将按照常规升级节奏，自动将集群主实例升级到经过修补的版本。在经过修补的版本可用后，您也可以自行发起主实例升级。.

在包含补丁程序的版本可用后，我们将更新此公告。在 [ 版本说明 ](https://cloud.google.com/kubernetes-
engine/docs/release-notes?hl=zh_cn) 中可以跟踪这些补丁程序的可用情况。

#####  该补丁程序解决了哪一漏洞？

该补丁程序解决了以下漏洞：

漏洞 [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) 允许能够在容器内执行代码的攻击者劫持外部发起的 ` docker cp `
操作。此漏洞可能允许攻击者将文件写入位置更改为主机文件系统中的任意位置。

|  高  |  
  
##  2019 年 5 月 31 日

说明  |  严重级别  |  备注  
---|---|---  
  
此公告在原始发布版本的基础上进行了更新。

######  2019 年 8 月 2 日更新

在初始公告发布时，仅有 1.13.6-gke.0 到 1.13.6-gke.5 受影响。由于回归，目前所有 1.13.6.x 版本均受影响。如果您目前在运行
1.13.6 版本，请尽快升级到 1.13.7。

Kubernetes 项目披露，kubelet v1.13.6 和 v1.14.2 中存在漏洞 [ CVE-2019-11245
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11245) ，这可能导致容器以 UID
0（通常映射到 ` root ` 用户）的身份运行，即便容器映像中指定了不同用户也是如此。 **如果您以非根用户的身份运行容器，而且您运行的节点版本是
1.13.6-gke.0 至 1.13.6-gke.6，我们建议您在不应以 UID 0 的身份运行容器的集群的所有 Pod 上设置` RunAsUser `
。 **

如果指定了非根用户 ` USER ` 值（例如，通过在 Dockerfile 中设置 ` USER `
值），则可能发生意外行为。容器首次在一个节点上运行时会正确采用指定 UID。但由于此缺陷的存在，在第二次（及后续）运行的时候，无论指定 UID
如何，该容器都会以 UID 0 的身份运行。这通常属于不希望发生的权限升级，可能导致意外的应用行为。

#####  如何判断我运行的版本是否受影响？

请运行以下命令，列出所有节点及其 kubelet 版本：

    
    
    
    kubectl get nodes -o=jsonpath='{range .items[*]}'\
    '{.status.nodeInfo.machineID}'\
    '{"\t"}{.status.nodeInfo.kubeletVersion}{"\n"}{end}'

如果输出列出了如下 kubelet 版本，则您的节点受此问题影响：

  * v1.13.6 
  * v1.14.2 

#####  如何判断我的特定配置是否受影响？

如果您以非根用户的身份运行容器，而且您运行的节点版本是 1.13.6-gke.0 至 1.13.6-gke.6，则除以下情况外，您都会受到影响：

  * 为 ` runAsUser ` PodSecurityContext 指定有效非根用户值的 Pod 不受影响，并且能继续按预期运行。 
  * 强制实施 ` runAsUser ` 设置的 PodSecurityPolicy 也不受影响，能够继续按预期运行。 
  * 指定了 ` mustRunAsNonRoot:true ` 的 Pod 不会以 UID 0 的身份启动，但在受此问题影响时无法正常启动。 

#####  该怎么做？

在集群中不应以 UID 0 身份运行的所有 Pod 上设置 [ RunAsUser 安全上下文
](https://kubernetes.io/docs/tasks/configure-pod-container/security-
context/#set-the-security-context-for-a-pod) 。您可以使用 [ PodSecurityPolicy
](https://kubernetes.io/docs/concepts/policy/pod-security-policy/) 应用此配置。

|  中  |  [ CVE-2019-11245 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2019-11245)  
  
##  2019 年 5 月 14 日

说明  |  严重级别  |  备注  
---|---|---  
  
**2019 年 6 月 11 日更新** ：2019 年 5 月 28 日那一周中发布的 1.11.10-gke.4、1.12.8-gke.6 和
1.13.6-gke.5 及更新的版本中提供了该补丁程序。

Intel 披露了以下 CVE：

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

这些 CVE 统称为微架构数据抽样 (MDS)。这些漏洞可用于通过推测性执行技术与微架构状态交互，从而造成数据泄露风险。如需了解详情，请参阅 [ Intel
披露信息 ](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) 。

**运行 Kubernetes Engine 的主机基础架构将客户的工作负载彼此隔离。除非您在自己的多租户 GKE
集群内部运行不受信任的代码，否则不会受此问题影响。**

**如果用户在 Kubernetes Engine 内部其自己的多租户服务中运行不受信任的代码，则该漏洞可能产生极为严重的影响。** 如需在
Kubernetes Engine 内缓解此漏洞，请在您的节点内禁用超线程。这些漏洞仅影响使用多个 CPU 的 Google Kubernetes
Engine (GKE) 节点。 请注意，n1-standard-1（GKE 默认设置）、g1-small 和 f1-micro 虚拟机仅会向客机环境公开
1 个 vCPU，因此无需禁用超线程。

即将发布的 [ 补丁程序版本 ](https://cloud.google.com/kubernetes-engine/release-
notes?hl=zh_cn) 中将包含启用强制刷新功能的附加保护机制。
我们将在未来几周内按常规升级节奏将启用自动升级的主实例和节点自动升级到修补后的版本。
**不过仅凭补丁程序本身不足以缓解此漏洞的风险。请参见下文了解推荐措施。**

如果您在运行 GKE On-Prem，则根据所用硬件，您可能会受此漏洞影响。请参阅 [ Intel 披露信息
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) 。

####  该怎么做？

**除非您在自己的多租户 GKE 集群内运行不受信任的代码，否则不会受到影响。**

**对于 Kubernetes Engine 内的节点，请创建停用了超线程的新节点池，并重新将您的工作负载安排到新节点上。**

请注意，n1-standard-1、g1-small 和 f1-micro 虚拟机仅向客机环境公开 1 个 vCPU，因此不需要停用超线程。

**警告** ：

  * 停用超线程可能会对您的集群和应用产生严重性能影响。请在将此项举措部署到您的生产集群之前，确保可以接受这种影响。 
  * 可以通过部署 DaemonSet 在 GKE 节点池级别上停用超线程。但部署此 DaemonSet 将导致您在该节点池中的所有节点同时重新启动。 因此，建议在您的集群内创建新节点池，部署 DaemonSet 以在该节点池内停用超线程，随后将工作负载迁移到新节点池。 

创建停用了超线程的新节点池的方法如下：

  1. 在集群中使用节点标签 ` cloud.google.com/gke-smt-disabled=true ` 创建一个新的节点池： 
    
        
    gcloud container node-pools create smt-disabled --cluster=[CLUSTER_NAME] \
        --node-labels=cloud.google.com/gke-smt-disabled=true

  2. 将 DaemonSet 部署到这个新节点池。DaemonSet 只会在带有 ` cloud.google.com/gke-smt-disabled=true ` 标签的节点上运行。它将停用超线程，然后重新启动节点。 
    
        
    kubectl create -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform/\
    k8s-node-tools/master/disable-smt/gke/disable-smt.yaml

  3. 确保 DaemonSet Pod 处于运行状态。 
    
        
    kubectl get pods --selector=name=disable-smt -n kube-system

您应该会收到类似如下的响应：

    
        
    NAME                READY     STATUS    RESTARTS   AGE
    
    disable-smt-2xnnc   1/1       Running   0          6m

  4. 检查 Pod 的日志中是否出现“SMT 已停用”(SMT has been disabled)。 
    
        
    kubectl logs disable-smt-2xnnc disable-smt -n kube-system

注意：如果节点启用了 [ 安全启动 ](https://cloud.google.com/kubernetes-engine/docs/how-
to/shielded-gke-nodes?hl=zh_cn#secure_boot) 功能，则启动选项无法修改。如果安全启动功能已经启用，需要首先将其 [
停用 ](https://cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-
nodes?hl=zh_cn#disabling) ，然后才能创建 DaemonSet。

您必须让 DaemonSet 在节点池上保持运行，从而使得池中创建的新节点可以自动应用更改。节点创建可由节点自动修复、手动升级或自动升级和自动扩缩触发。

如需再次启用超线程，您需要重新创建节点池，但不要在其中部署所提供的 DaemonSet，然后将工作负载迁移到新节点池。

我们还建议您在补丁程序可用后手动升级节点。若要升级，您必须先 [ 将主实例升级 ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=zh_cn#upgrading_the_cluster)
到最新版本。GKE 主实例会按照常规升级节奏自动升级。

在包含补丁程序的版本发布后，我们将更新此公告。

####  该补丁程序解决了哪一漏洞？

该补丁程序缓解了以下漏洞：

[ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
、 [ CVE-2018-12127 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2018-12127) 、 [ CVE-2018-12130
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130) 、 [
CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)
：这些漏洞会利用推测性执行技术发起攻击。这些 CVE 统称为微架构数据抽样。这些漏洞可用于通过推测性执行技术与微架构状态交互，从而造成数据泄露风险。  |
中  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  2019 年 4 月 5 日

说明  |  严重级别  |  备注  
---|---|---  
  
近期发现了 [ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) 和 [ CVE-2019-9901
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) 这两个 [ Envoy
](https://www.envoyproxy.io/) 漏洞。

Envoy 嵌入在 [ Istio ](https://istio.io/) 之中，这些漏洞允许用户在某些情况下绕过 Istio 政策。

如果您在 Google Kubernetes Engine (GKE) 上启用了 Istio，那么就可能会受到这些漏洞的影响。
**在最新补丁程序版本发布后，我们建议您尽快将受影响的集群升级到这些补丁程序版本，并且升级您的 Istio 的 Sidecar（请参见下方说明）。**

####  该怎么做？

**鉴于这些漏洞的严重级别，无论您是否启用了节点自动升级，我们都建议您采取以下措施：**

  1. **在补丁程序可用时立即[ 手动升级 ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster?hl=zh_cn) 您的集群。 **
  2. **按照[ Sidecar 升级文档 ](https://archive.istio.io/v1.5/docs/setup/upgrade/cni-helm-upgrade/#control-plane-upgrade) 升级您的 Sidecar。 **

修补后的版本将在今日下午 7:00（美国太平洋夏令时间）之前推出，可供所有 GKE 项目使用。

此补丁程序将在如下 GKE 版本中可用。在 GKE 安全公告页面上发布相应信息之后（预计在 2019 年 4 月 15
日发布），新集群将默认使用修补后的版本，如果您在此之前创建了新集群，则必须为您的集群指定使用修补后的版本。启用了 [ 节点自动升级
](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-
upgrades?hl=zh_cn) 的 GKE 客户以及未手动升级的 GKE 客户的节点会在此后的一周内自动升级到修补后的版本。

修补后的版本：

  * 1.10.12-gke.14 
  * 1.11.6-gke.16 
  * 1.11.7-gke.18 
  * 1.11.8-gke.6 
  * 1.12.6-gke.10 
  * 1.13.4-gke.10 

####  该补丁程序解决了哪一漏洞？

该补丁程序缓解了以下漏洞：

[ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) 和 [ CVE-2019-9901
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) 。 您可以访问 [
Istio 博客 ](https://istio.io/blog/2019/announcing-1.1.2) 详细了解相关信息。

|  高  |

  * [ CVE-2019-9900 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900)
  * [ CVE-2019-9901 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) 。 

  
  
##  2019 年 3 月 1 日

说明  |  严重级别  |  备注  
---|---|---  
  
**2019 年 3 月 22 日更新** ：此补丁程序将在 Kubernetes 1.11.8-gke.4、1.13.4-gke.1
和更新版本中可用。此补丁程序在 1.12 版本中尚不可用。在 [ 版本说明 ](https://cloud.google.com/kubernetes-
engine/docs/release-notes-archive?hl=zh_cn#march_19_2019) 中可以跟踪这些补丁程序的可用情况。

Kubernetes 近来发现了一个新的拒绝服务攻击漏洞 [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) ，该漏洞允许获得发布补丁程序请求授权的用户编写恶意的 "json-patch"
请求，占用 Kubernetes API 服务器的大量 CPU 和内存资源，有可能降低集群控制平面的可用性。如需了解详情，请参阅 [ Kubernetes
披露信息 ](https://groups.google.com/forum/?hl=zh_cn#!topic/kubernetes-
announce/vmUUNkYfG9g) 。 **所有 Google Kubernetes Engine (GKE)
主实例都会受到这些漏洞的影响。即将推出的补丁程序版本将包含针对此漏洞的缓解措施。我们将在未来几周内按常规升级节奏将集群主实例自动升级到修补后的版本。**

####  该怎么做？

**您无需采取任何操作。GKE 主实例会按照常规升级节奏自动升级。** 如果您想尽快升级主实例，可以 [ 手动启动主实例升级
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=zh_cn#upgrading_the_cluster) 。

我们将更新本公告，列举包含补丁程序的版本。请注意，补丁程序仅可用于 1.11 及以上版本，不可用于 1.10 版本。

####  该补丁程序解决了哪一漏洞？

该补丁程序解决了以下漏洞：

[ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) 漏洞允许用户编写 "json-patch" 类型的补丁程序，占用
Kubernetes API 服务器的大量 CPU 资源，有可能降低集群控制平面的可用性。

|  中  |  [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100)  
  
##  2019 年 2 月 11 日 (runc)

说明  |  严重级别  |  备注  
---|---|---  
  
Open Containers Initiative (OCI) [ 近期发现
](https://groups.google.com/a/opencontainers.org/forum/m/?hl=zh_cn#!topic/dev/Tc1ELm-8oDI)
了 runc 中的一个新安全漏洞 [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) ，该漏洞允许容器逃逸，从而获得主机节点上的 root 权限。

**您的 Google Kubernetes Engine (GKE) Ubuntu 节点会受到这些漏洞的影响，我们建议您尽快[ 升级
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=zh_cn) 到最新的补丁程序版本，具体说明如下所述。 **

####  该怎么做？

若要升级节点，您必须先将主节点升级到最新版本。Kubernetes
1.10.12-gke.7、1.11.6-gke.11、1.11.7-gke.4、1.12.5-gke.5 及更新的版本中提供了该补丁程序。在 [ 版本说明
](https://cloud.google.com/kubernetes-engine/docs/release-notes-
archive?hl=zh_cn#february-11-2019) 中可以跟踪这些补丁程序的可用情况。

请注意，仅有 GKE 中的 Ubuntu 节点会受此影响。运行 COS 的节点不受影响。

请注意，新版本的 runc 内存使用量更高，如果您先前设置了较低的内存限制 (< 16MB)，则可能需要更新分配给容器的内存量。

####  该补丁程序解决了哪一漏洞？

该补丁程序解决了以下漏洞：

[ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) 描述了 runc 中的一个漏洞，该漏洞允许恶意容器（只需极少的用户互动，执行一次
exec 即可触发）覆盖主机 runc 二进制文件，从而获得主机节点上的 root 级代码执行权限。 未以 root
权限运行的容器不受影响。此漏洞的严重级别分级为“高”。

|  高  |  [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736)  
  
##  2019 年 2 月 11 日 (Go)

说明  |  严重级别  |  备注  
---|---|---  
  
**2019 年 2 月 25 日更新** ：与之前所宣布的一样，该补丁程序在 1.11.7-gke.4 中不可用。如果您运行的是
1.11.7，则可以采取这样的做法：降级到 1.11.6，再升级到 1.12，或者等到 2019 年 3 月 4 日那一周发布的下一个 1.11.7
补丁程序。

Go 编程语言近期被发现存在一个新的安全漏洞 [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486) ，这是 P-521 和 P-384 椭圆曲线的加密/椭圆实现中存在的一个拒绝服务攻击
(DoS) 漏洞。在 Google Kubernetes Engine (GKE) 中，该漏洞可能允许用户编写恶意请求，占用 Kubernetes API
服务器的大量 CPU 资源，有可能降低集群控制平面的可用性。 如需了解详情，请参阅 [ Go 编程语言披露信息
](https://groups.google.com/forum/?hl=zh_cn#!topic/golang-
announce/mVeX35iXuSw) 。

**所有 Google Kubernetes Engine (GKE) 主实例都会受到这些漏洞的影响。[ 最新版本的补丁程序
](https://cloud.google.com/kubernetes-engine/docs/release-notes-
archive?hl=zh_cn#february-11-2019)
包含针对此漏洞的缓解措施。我们将在未来几周内按常规升级节奏将集群主实例自动升级到修补后的版本。 **

####  该怎么做？

**您无需采取任何操作。GKE 主实例会按照常规升级节奏自动升级。** 如果您想尽快升级主实例，可以 [ 手动启动主实例升级
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=zh_cn#upgrading_the_cluster) 。

GKE 1.10.12-gke.7、1.11.6-gke.11、1.11.7-gke.4、1.12.5-gke.5 及更新的版本中提供了此补丁程序。

####  该补丁程序解决了哪一漏洞？

该补丁程序解决了以下漏洞：

CVE-2019-6486 是 P-521 和 P-384 椭圆曲线的加密/椭圆实现中存在的一个漏洞。用户可以利用该漏洞编写输入，耗用大量 CPU 资源。

|  高  |  [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486)  
  
##  2018 年 12 月 3 日

说明  |  严重级别  |  备注  
---|---|---  
  
Kubernetes 最近发现了 [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105) 这个新的安全漏洞，该漏洞能让权限相对较低的用户绕过对 kubelet 的
API 的授权，使其能对集群中任何节点上的任何 Pod 执行任意操作。如需了解详情，请参阅 [ Kubernetes 披露信息
](https://groups.google.com/forum/?hl=zh_cn#!topic/kubernetes-
announce/GVllWCg6L88) 。 **所有 Google Kubernetes Engine (GKE)
主实例都会受到这些漏洞的影响，我们已经将集群升级到了[ 最新补丁版本 ](https://cloud.google.com/kubernetes-
engine/docs/release-notes-archive?hl=zh_cn#november-12-2018) 。您无需采取任何操作。 **

####  该怎么做？

**您无需采取任何操作。GKE 主实例已升级。**

GKE 1.9.7-gke.11、1.10.6-gke.11、1.10.7-gke.11、1.10.9-gke.5 和 1.11.2-gke.18
及更新的版本中提供了该补丁程序。

####  该补丁程序解决了哪一漏洞？

该补丁程序解决了以下漏洞：

CVE-2018-1002105 漏洞能让权限相对较低的用户绕过对 kubelet 的 API
的授权。这使得用户可以获得授权，提出可升级的请求，从而实现提权并任意调用 kubelet 的 API。此漏洞在 Kubernetes
中的严重程度为“严重”。考虑到 GKE 实现中的一些细节会阻止未通过身份验证的提权路径，此漏洞在 GKE 中的严重程度为“高”。

|  高  |  [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105)  
  
##  2018 年 11 月 13 日

说明  
---  
  
**2018 年 11 月 16 日更新** ：已完成所有可能受影响的令牌的吊销和轮替。您无需采取进一步行动。

Google 最近在 Calico Container Network Interface (CNI)
插件中发现了一个问题，该插件在某些配置下可以记录敏感信息。此问题由 Tigera 技术公告 [ TTA-2018-001
](https://www.projectcalico.org/security-bulletins/) 追踪记录。

  * 如果在运行时使用调试级日志记录选项，Calico CNI 插件会将 Kubernetes API 客户端配置写入日志。 
  * 如果在 CNI 网络配置中设置了“k8s_auth_token”字段，Calico CNI 还会将 Kubernetes API 令牌写入信息级日志。 
  * 此外，在使用调试级日志记录选项来运行该插件时，如果明确设置了服务帐号令牌（无论是在 Calico 读取的 Calico 配置文件中设置，还是设置为 Calico 使用的环境变量），Calico 组件（calico/节点、felix、CNI）均会将此信息写入日志文件。 

这些令牌拥有以下权限：  
      
    
    
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
  
启用了集群网络政策和 Stackdriver Logging 的 Google Kubernetes Engine 集群会将 Calico
服务帐号令牌记录到 Stackdriver 中。未启用网络政策的集群不受影响。

我们已部署一个修复程序，将 Calico CNI 插件改为仅记录警告级日志并使用新的服务帐号。Calico 的修补代码将在之后的版本中部署。

下周，我们将对任何可能受到影响的令牌进行滚动吊销。吊销完成后，我们会更新此公告。 **您无需采取任何进一步行动。** （此轮替已于 2018 年 11 月
16 日完成）

如果您希望立即轮替这些令牌，则可运行以下命令，系统将在几秒钟内自动重新创建服务帐号的新密钥：  
  
kubectl get sa --namespace kube-system calico -o template --template '{{(index
.secrets 0).name}}' | xargs kubectl delete secret --namespace kube-system  
---  
  
####  检测

GKE 会记录所有访问 API 服务器的行为。如要确定是否有人在 Google Cloud 的预期 IP 范围之外使用了 Calico 令牌，您可以运行以下
Stackdriver 查询。请注意，这只会返回从 GCP 网络之外进行的调用的记录。您应该根据您的具体环境，按需要对查询进行自定义。  
  
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

说明  |  严重级别  |  备注  
---|---|---  
  
[ Intel 披露了 ](https://www.intel.com/content/www/us/en/architecture-and-
technology/l1tf.html) 以下 CVE：

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) （针对 [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ） 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) （针对操作系统和 [ SMT ](https://en.wikipedia.org/wiki/Hyper-threading) ） 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) （针对虚拟化） 

这些 CVE 统称为“L1 终端故障 (L1TF)”。

这些 L1TF 漏洞通过攻击处理器层的数据结构配置来利用推测性执行技术。 “L1”是指 1 级数据缓存
(L1D)，这是一种用于加快内存访问速度的小型芯片上资源。

如需详细了解这些漏洞和 Compute Engine 的缓解措施，请参阅 [ Google Cloud 博文
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities?hl=zh_cn) 。

####  对 Google Kubernetes Engine 的影响

运行 Kubernetes Engine 并将客户的集群和节点彼此隔离的基础架构可以抵御已知攻击。

使用 Google 的 Container-Optimized OS 映像且启用了 [ 自动升级
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=zh_cn) 的 Kubernetes Engine 节点池将在 COS 映像的修复版本可用时自动进行更新（修复版本自 2018 年
8 月 20 日那周起可用）。

未启用 [ 自动升级 ](https://cloud.google.com/kubernetes-engine/docs/concepts/node-
auto-upgrades?hl=zh_cn) 的 Kubernetes Engine 节点池必须在 COS 映像的修补版本可用时 [ 手动进行更新
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=zh_cn) 。

|  高  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  2018 年 8 月 6 日；最后更新时间：2018 年 9 月 5 日

说明  |  严重级别  |  备注  
---|---|---  
  
####  2018 年 9 月 5 日更新

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) 已于最近披露。与 [ CVE-2018-5390
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
一样，这也是一个内核级的网络漏洞，可提高拒绝服务攻击 (DoS) 对存在该漏洞的系统的破坏效力。两者的主要区别在于 CVE-2018-5391 可通过 IP
连接加以利用。为涵盖这两个漏洞，我们更新了此公告。

####  说明

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) （“SegmentSmack”）描述了一个内核级的网络漏洞，它可提高经由 TCP
连接的 DoS（拒绝服务）攻击对存在该漏洞的系统的破坏效力。

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) （“FragmentSmack”）描述了一个内核级的网络漏洞，它可提高经由 IP
连接的 DoS（拒绝服务）攻击对存在该漏洞的系统的破坏效力。

####  对 Google Kubernetes Engine 的影响

截至 2018 年 8 月 11 日，所有 Kubernetes Engine 主节点都可以抵御对这两个漏洞的攻击。此外，所有配置为自动升级的
Kubernetes Engine 集群也可以抵御这类攻击。 未配置为 [ 自动升级
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster?hl=zh_cn) 且最后一次手动升级是在 2018 年 8 月 11 日之前的 Kubernetes Engine
节点池会受到这两个漏洞的影响。

####  修补版本

鉴于此漏洞的严重级别，我们建议您在补丁程序可用时立即 [ 手动升级 ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster?hl=zh_cn#upgrading-nodes) 您的节点。

|  高  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  2018 年 5 月 30 日

说明  |  严重级别  |  备注  
---|---|---  
  
最近在 Git 中发现了一个漏洞。如果允许无特权的用户创建使用 gitRepo 卷的 Pod，则可能会允许 Kubernetes 中的权限提升。此 CVE
标识为 [ CVE-2018-11235 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-11235) 。

####  我会受到影响吗？

如果满足以下所有条件，则此漏洞会影响到您：

  * 不受信任的用户可以创建 Pod（或触发 Pod 的创建）。 
  * 由不受信任的用户创建的 Pod 被限制访问主机根目录（例如，通过 [ PodSecurityPolicy ](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies?hl=zh_cn) ）。 
  * 由不受信任的用户创建的 Pod 被允许使用 gitRepo 卷类型。 

所有 Kubernetes Engine 节点都受此漏洞的影响。

####  该怎么做？

禁止使用 gitRepo 卷类型。如需通过 PodSecurityPolicy 禁止 gitRepo 卷，请从 PodSecurityPolicy 的 `
volumes ` 白名单中删掉 ` gitRepo ` 。

通过从 initContainer 将 git 代码库克隆到 EmptyDir 卷中，可以实现等效的 gitRepo 卷行为：

    
    
    
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

####  哪个补丁程序可解决这个漏洞？

即将发布的 Kubernetes Engine 版本中将包含一个补丁程序。 请稍后查看此处了解详情。

|  中  |

  * [ CVE-2018-11235 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11235)

  
  
##  2018 年 5 月 21 日

说明  |  严重级别  |  备注  
---|---|---  
  
最近在 Linux 内核中发现了多个漏洞，这些漏洞可能会允许无特权的进程提升其权限或开展拒绝服务攻击（通过内核崩溃）。这些 CVE 标识为 [
CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) 、 [ CVE-2018-8897
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897) 和 [
CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)
。 所有 Kubernetes Engine 节点都会受到这些漏洞的影响，我们建议您 [ 升级
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=zh_cn) 到最新的补丁程序版本，具体说明如下所述。

####  该怎么做？

若要升级，您必须先将主节点升级到最新版本。Kubernetes Engine 1.8.12-gke.1、Kubernetes Engine
1.9.7-gke.1 和 Kubernetes Engine 1.10.2-gke.1 中提供了相应补丁程序。 这些版本包含 Container-
Optimized OS 和 Ubuntu 映像的补丁程序。

如果在此之前创建新集群，您必须指定修补后的版本，才能获得相应补丁程序。对于已启用 [ 节点自动升级
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-
upgrades?hl=zh_cn) 且未进行手动升级的客户，其节点将会在未来几周内升级到修补后的版本。

####  该补丁程序解决了哪些漏洞？

该补丁程序缓解了以下漏洞：

[ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) ：此漏洞影响到 Linux
内核。它允许无特权的用户或进程引发系统内核崩溃，继而导致 DoS 攻击或权限提升。此漏洞被评为高危漏洞且 CVSS 的评分为 7.8。

[ CVE-2018-8897 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-8897) ：此漏洞影响到 Linux 内核。它允许无特权的用户或进程引发系统内核崩溃，继而导致
DoS 攻击。 此漏洞被评为中危漏洞且 CVSS 的评分为 6.5。

[ CVE-2018-1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) ：此漏洞影响到 Linux 内核的 KVM
管理程序。它允许无特权的进程引发客机内核崩溃或有可能获得特权。运行 Kubernetes Engine 的基础架构已修补此漏洞，因此 Kubernetes
Engine 不会受到影响。此漏洞被评为高危漏洞且 CVSS 的评分为 8.0。

|  高  |

  * [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199)
  * [ CVE-2018-8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
  * [ CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)

  
  
##  2018 年 3 月 12 日

说明  |  严重级别  |  备注  
---|---|---  
  
Kubernetes 项目 [ 最近披露了
](https://groups.google.com/forum/?hl=zh_cn#!topic/kubernetes-security-
announce/P7lBjbjDKd8) 新的安全漏洞 [ CVE-2017-1002101 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2017-1002101) 和 [ CVE-2017-1002102
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102)
，这些漏洞允许容器访问该容器之外的文件。所有 Kubernetes Engine
节点都会受到这些漏洞的影响，我们建议您尽快升级到最新的补丁程序版本，具体说明如下所述。

####  该怎么做？

鉴于这些漏洞的严重级别，无论您是否启用了节点自动升级，我们都建议您在补丁程序可用时立即 [ 手动升级
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=zh_cn) 您的节点。该补丁程序将于 3 月 16
日之前提供给所有客户，但根据您的集群所在的区域，您也可能会更早获得该补丁程序，具体请参照 [ 发布计划
](https://cloud.google.com/kubernetes-engine/docs/release-notes-
archive?hl=zh_cn#march-12-2018) 。

若要升级，您必须先将主节点升级到最新版本。Kubernetes 1.9.4-gke.1、Kubernetes 1.8.9-gke.1 和
Kubernetes 1.7.14-gke.1 中提供了相应补丁程序。默认情况下，新集群将在 3 月 30
日使用修补后的版本；如果在此之前创建新集群，则必须指定修补后的版本，才能获得相应补丁程序。

对于已启用 [ 节点自动升级 ](https://cloud.google.com/kubernetes-
engine/docs/concepts/node-auto-upgrades?hl=zh_cn) 且不进行手动升级的客户，其节点将会在 4 月 23
日之前升级到修补后的版本。不过，鉴于此漏洞的性质，我们建议您在补丁程序可用时立即 [ 手动升级
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
container-cluster?hl=zh_cn) 您的节点。

####  该补丁程序解决了哪些漏洞？

该补丁程序缓解了以下两个漏洞：

漏洞 CVE-2017-1002101 允许使用 [ 子路径
](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath)
卷装载功能的容器访问卷外部的文件。这意味着，如果您使用 PodSecurityPolicy 来阻止容器访问主机路径卷，则可更新或创建 Pod
的攻击者将能够使用任何其他卷类型来装载任何主机路径。

漏洞 CVE-2017-1002102 允许使用某些卷类型（包括 Secret 卷、ConfigMap 卷、映射卷或 Downward API
卷）的容器删除该卷外部的文件。这意味着，如果使用其中一种卷类型的容器遭到破解，或者您允许不受信任的用户创建
Pod，则攻击者可以使用该容器删除主机上的任意文件。

如需详细了解此修复程序，请参阅 [ Kubernetes 博文
](https://kubernetes.io/blog/2018/04/04/fixing-subpath-volume-vulnerability/)
。

|  高  |

  * [ CVE-2017-1002101 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101)
  * [ CVE-2017-1002102 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102)

