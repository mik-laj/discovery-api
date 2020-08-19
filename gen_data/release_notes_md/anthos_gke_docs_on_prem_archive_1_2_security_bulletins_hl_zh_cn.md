您正在查看旧版 GKE On-Prem 的文档。 [ 查看最新文档
](https://cloud.google.com/anthos/gke/docs/on-prem?hl=zh-cn) 。

#  安全公告

本主题介绍了 Anthos GKE On-Prem 的所有安全公告。

漏洞通常有一段时间的保密期，以便给让影响的各方有机会解决这些问题。在这种情况下，GKE On-Prem 的 [ 版本说明
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.2/release-
notes?hl=zh-cn) 会在保密期结束前使用“安全更新”来泛指这些漏洞。保密期结束后，我们会更新版本说明，以阐明补丁程序所解决的漏洞。

**注意** ：如果您在 GKE On-Prem 上运行多租户工作负载，请特别注意这些公告。这些漏洞更有可能影响到多租户工作负载。有关 GKE On-
Prem 中安全边界的技术说明以及这些安全边界对工作负载的影响，请参阅 [ Kubernetes 栈中不同层的隔离
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) 。

如需接收最新安全公告，请将本页面的网址添加到您的 [ Feed 阅读器
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) 。

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
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.2/how-
to/upgrading-clusters?hl=zh-cn) 到相应补丁程序版本。

包含此补丁程序的版本如下所示：

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

我们建议您尽快将集群 [ 升级 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.2/how-to/upgrading-clusters?hl=zh-cn) 到版本 [ 1.0.2-gke.3
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.2/downloads?hl=zh-cn#gkectl_latest) ，其中包含此漏洞的补丁程序。

|

中

|

[ Anthos GKE On-Prem 版本 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.2/downloads?hl=zh-cn#gkectl_latest)  
  
##  2019 年 8 月 22 日

说明  |  严重级别  |  备注  
---|---|---  
  
Kubernetes 最近发现了一个漏洞 ( [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) )，该漏洞允许集群级的 [ 自定义资源
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) 实例像存在于所有命名空间内的有命名空间对象一样得到处理。这意味着仅有命名空间级 RBAC
权限的用户和服务帐号可以与集群级自定义资源交互。利用此漏洞要求攻击者具有访问任意命名空间内资源的权限。

######  该怎么做？

我们建议您尽快将集群 [ 升级 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.2/how-to/upgrading-clusters?hl=zh-cn) 到版本 [ 1.0.2-gke.3
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.2/downloads?hl=zh-cn#gkectl_latest) ，其中包含此漏洞的补丁程序。

######  该补丁程序解决了哪一漏洞？

该补丁程序缓解了以下漏洞： [ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247) 。

|

中

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

