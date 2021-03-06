新版 Anthos GKE on AWS 已于 7 月 24 日发布。如需了解重大更改，请参阅 [ 版本说明
](https://cloud.google.com/anthos/gke/docs/aws/release-notes?hl=zh-cn) 。

#  安全公告

了解针对 Anthos GKE on AWS (GKE on AWS) 的安全公告。

##  GCP-2020-011

**发布日期** ：2020-07-24  
说明  |  严重级别  |  备注  
---|---|---  
  
最近在 Kubernetes 中发现了一个网络漏洞 [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) 。服务有时会使用本地环回接口
(127.0.0.1) 与同一 pod 中运行的其他应用通信。利用此漏洞，有权访问集群网络的攻击者能够将流量发送到相邻 Pod
和节点的环回接口。如果服务依赖于无法在其 Pod 之外访问的环回接口，则攻击者可以利用这些服务。

要在 GKE on AWS 集群上利用此漏洞，攻击者需要对集群中的 EC2 实例停用 [ 来源目标检查
](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html)
。这要求攻击者拥有对 EC2 实例上的 ` ModifyInstanceAttribute ` 或 `
ModifyNetworkInterfaceAttribute ` 的 AWS IAM 权限。因此，对于 GKE on AWS，此漏洞的严重级别分配为低。

####  我该怎么做？

如需修复此漏洞，请将您的集群升级到修补后的版本。以下即将推出的 GKE on AWS 版本或更高版本应该会包含针对此漏洞的修补程序：

  * GKE on AWS 1.4.2 

####  该补丁程序解决了哪一漏洞？

此补丁程序修复了以下漏洞： [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) 。

|

低

|

[ CVE-2020-8558 ](https://github.com/kubernetes/kubernetes/issues/92315)  
  
##  GCP-2020-009

**发布日期** ：2020-07-15  说明  |  严重级别  |  备注  
---|---|---  
  
最近在 Kubernetes 中发现了一个提权漏洞 [ CVE-2020-8559 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8559) 。利用此漏洞，已破解节点的攻击者能够在集群中的任何 pod
中执行命令。因此，攻击者可以使用已被破解的节点来破解其他节点并且可能读取信息，或者导致破坏性操作。

请注意，集群中的某个节点必须已被破解，攻击者才能利用此漏洞。此漏洞本身不会破解集群中的任何节点。

####  我该怎么做？

GKE on AWS GA 1.4.1 将于 2020 年 7 月底发布，该版本及更高版本包含针对此漏洞的补丁程序。如果您使用的是以前的版本，请 [
下载新版本的 anthos-gke 命令行工具 ](https://cloud.google.com/anthos/gke/docs/aws/how-
to/prerequisites?hl=zh-cn) ，并重新创建管理和用户集群。

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
  
技术人员最近在 Kubernetes 中发现了服务器端请求伪造 (SSRF) 漏洞 [ CVE-2020-8555
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555)
，该漏洞允许某些授权用户从控制层面主机网络泄露高达 500 字节的敏感信息。Google Kubernetes Engine (GKE) 控制平面使用的是
Kubernetes 的控制器，所有 Kubernetes Engine
节点都会受到此漏洞的影响，我们建议您将控制层面升级到最新的补丁程序版本，具体说明如下所述。节点不需要升级。  

####  我该怎么做？

Anthos GKE on AWS (GKE on AWS) v0.2.0 或更高版本已包含针对此漏洞的补丁程序。如果您使用的是以前的版本，请 [
下载新版本的 anthos-gke 命令行工具 ](https://cloud.google.com/anthos/gke/docs/aws/how-
to/prerequisites?hl=zh-cn) ，并重新创建管理集群和用户集群。

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
  
Kubernetes 披露了一种 [ 漏洞 ](https://github.com/kubernetes/kubernetes/issues/91507)
，该漏洞允许具有特权的容器将节点流量重定向到其他容器。此攻击无法读取或修改双向 TLS/SSH 流量（例如 kubelet 与 API
服务器之间）或来自使用 mTLS 的应用的流量。所有 Google Kubernetes Engine (GKE)
节点都会受到此漏洞的影响，我们建议您升级到最新的补丁程序版本，具体说明如下所述。

####  我该怎么做？

[ 下载以下版本或更高版本的 anthos-gke 命令行工具
](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites?hl=zh-cn)
，然后重新创建管理集群和用户集群：

  * aws-0.2.1-gke.7 

通常，很少有容器需要 ` CAP_NET_RAW ` 。默认情况下，应通过 [ Anthos 政策控制器
](https://cloud.google.com/anthos-config-management/docs/concepts/policy-
controller?hl=zh-cn) 或更新 pod 规范来阻止此功能和其他强大的功能：

从容器中删除 ` CAP_NET_RAW ` 功能：

  * 将 Anthos 政策控制器/Gatekeeper 与此 [ 限制条件模板 ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) 结合使用，并加以应用，例如： 
    
        
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
    

  * 或者更新您的 pod 规范： 
    
        
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

