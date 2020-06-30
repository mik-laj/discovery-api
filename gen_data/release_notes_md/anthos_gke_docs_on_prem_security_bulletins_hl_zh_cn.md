#  安全公告

本主题介绍了 Anthos GKE On-Prem (GKE On-Prem) 的所有安全公告。

漏洞通常有一段时间的保密期，以便给让影响的各方有机会解决这些问题。在这种情况下，GKE On-Prem 的 [ 版本说明
](https://cloud.google.com/anthos/gke/docs/on-prem/release-notes?hl=zh-cn)
会在保密期结束前使用“安全更新”来泛指这些漏洞。保密期结束后，我们会更新版本说明，以阐明补丁程序所解决的漏洞。

**注意** ：如果您在 GKE On-Prem 上运行多租户工作负载，请特别注意这些公告。这些漏洞更有可能影响到多租户工作负载。有关 GKE On-
Prem 中安全边界的技术说明以及这些安全边界对工作负载的影响，请参阅 [ Kubernetes 堆栈中不同层的隔离
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) 。

如需接收最新安全公告，请将本页面的网址添加到您的 [ Feed 阅读器
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 。

##  GCP-2020-007

**发布日期：** 2020-06-01  
说明  |  严重级别  |  备注  
---|---|---  
  
技术人员最近在 Kubernetes 中发现了服务器端请求伪造 (SSRF) 漏洞 [ CVE-2020-8555
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555)
，该漏洞允许某些授权用户从控制层面主机网络泄露高达 500 字节的敏感信息。Google Kubernetes Engine (GKE) 控制层面会使用
Kubernetes 中的控制器，因此会受到此漏洞的影响。我们建议您将控制平面升级到最新的补丁程序版本，具体说明如下所述。节点不需要升级。  

####  该怎么做？

以下 Anthos GKE On-Prem (GKE On-Prem) 版本或更新版本包含针对此漏洞的修补程序：

  * Anthos 1.3.0 

如果您使用的是早期版本，请 [ 将现有集群升级 ](https://cloud.google.com/anthos/gke/docs/on-
prem/how-to/upgrading?hl=zh-cn) 到包含该修补程序的版本。

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

要缓解 Anthos GKE On-Prem (GKE On-Prem) 的此漏洞所带来的影响，请 [ 将集群升级
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=zh-cn)
到以下版本或更新版本：

  * Anthos 1.3.2 

通常，很少有容器需要 ` CAP_NET_RAW ` 。默认情况下，应通过 [ Anthos 政策控制器
](https://cloud.google.com/anthos-config-management/docs/concepts/policy-
controller?hl=zh-cn) 或更新 pod 规范来阻止此功能和其他强大的功能：

  * 从容器中删除 ` CAP_NET_RAW ` 功能： 
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
        

    * 通过更新 pod 规范： 
        
                
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
  
  
##  GCP-2020-004

说明  |  严重级别  |  备注  
---|---|---  
  
近期在 Kubernetes 中发现了一个漏洞（如 [ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) 中所述），该漏洞导致任何有权发出 POST 请求的用户都可以对
Kubernetes API 服务器执行远程拒绝服务攻击。Kubernetes 产品安全委员会 (PSC) 已经发布了有关此漏洞的更多信息，详见 [ 此处
](https://groups.google.com/g/kubernetes-security-
announce/c/wuwEwZigXBc?hl=zh-cn) 。

您可以通过限制哪些客户端可以访问您的 Kubernetes API 服务器来缓解此漏洞。

####  该怎么做？

我们建议您尽快将集群升级为包含此漏洞修复的补丁程序版本。

包含此修补程序的版本如下所示：

  * Anthos 1.3.0（运行 Kubernetes 版本 1.15.7-gke.32） 

####  该补丁程序解决了哪些漏洞？

该补丁程序修复了以下拒绝服务攻击 (DoS) 漏洞：

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) 。

|

中

|

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  2019 年 10 月 16 日

说明  |  严重级别  |  备注  
---|---|---  
  
近期在 Kubernetes 中发现了一个漏洞（如 [ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) 中所述），该漏洞导致任何有权发出 POST 请求的用户都可以对
Kubernetes API 服务器执行远程拒绝服务攻击。Kubernetes 产品安全委员会 (PSC) 已经发布了有关此漏洞的更多信息，详见 [ 此处
](https://groups.google.com/forum/?hl=zh-cn#!topic/kubernetes-security-
announce/jk8polzSUxs) 。

您可以通过限制哪些客户端可以访问您的 Kubernetes API 服务器来缓解此漏洞。

######  该怎么做？

我们建议您在包含修复方案的补丁程序版本发布后，尽快将 [ 集群升级
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading-
clusters?hl=zh-cn) 到相应补丁程序版本。

包含此修复的补丁程序版本如下所示：

  * Anthos 1.1.1（运行 Kubernetes 版本 1.13.7-gke.30） 

######  该补丁程序解决了哪一漏洞？

该补丁程序缓解了以下漏洞： [ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) 。

|

高

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
##  2019 年 8 月 23 日

说明  |  严重级别  |  备注  
---|---|---  
  
我们最近发现并缓解了一个漏洞，在该漏洞中，用于保护监控端点的 RBAC
代理未正确授权用户。因此，内部集群网络中未授权用户可以访问某些组件的指标。以下组件受到了影响：

  * ` etcd `
  * ` etcd-events `
  * ` kube-apiserver `
  * ` kube-controller-manager `
  * ` kube-scheduler `
  * ` node-exporter `
  * ` kube-state-metrics `
  * ` prometheus `
  * ` alertmanager `

######  该怎么做？

我们建议您尽快将集群 [ 升级 ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/upgrading-clusters?hl=zh-cn) 到版本 [ 1.0.2-gke.3
](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=zh-
cn#gkectl_latest) ，其中包含此漏洞的补丁程序。

|

中

|

[ Anthos GKE On-Prem 版本 ](https://cloud.google.com/anthos/gke/docs/on-
prem/downloads?hl=zh-cn#gkectl_latest)  
  
##  2019 年 8 月 22 日

说明  |  严重级别  |  备注  
---|---|---  
  
Kubernetes 最近发现了一个漏洞 ( [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) )，该漏洞允许集群级的 [ 自定义资源
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) 实例像存在于所有命名空间内的有命名空间对象一样得到处理。这意味着仅有命名空间级 RBAC
权限的用户和服务帐号可以与集群级自定义资源交互。利用此漏洞要求攻击者具有访问任意命名空间内资源的权限。

######  该怎么做？

我们建议您尽快将集群 [ 升级 ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/upgrading-clusters?hl=zh-cn) 到版本 [ 1.0.2-gke.3
](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=zh-
cn#gkectl_latest) ，其中包含此漏洞的补丁程序。

######  该补丁程序解决了哪一漏洞？

该补丁程序缓解了以下漏洞： [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) 。

|

中

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

