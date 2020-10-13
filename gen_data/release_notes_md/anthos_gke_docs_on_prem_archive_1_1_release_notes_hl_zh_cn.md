#  版本说明

本页面记录了 Anthos GKE On-Prem 的正式版更新。您可以定期查看本页面，以了解有关新增功能、功能更新、功能弃用、错误修复和已知问题的公告。

另请参阅：

  * [ 下载 ](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=zh-cn)
  * [ 版本控制和升级 ](https://cloud.google.com/anthos/gke/docs/on-prem/versioning-and-upgrades?hl=zh-cn)
  * [ 升级 GKE On-Prem ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=zh-cn)

您可以在 [ Google Cloud 版本说明 ](https://cloud.google.com/release-notes?hl=zh-cn)
页面上查看 Google Cloud 所有产品的最新产品动态。

要接收最新产品动态，请将本页面的网址添加到您的 [ Feed 阅读器
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ，或直接添加 Feed 网址： `
https://cloud.google.com/feeds/gkeonprem-release-notes.xml `

##  2019 年 11 月 19 日

GKE On-Prem 1.1.2-gke.0 版本现已发布。要下载 1.1.2-gke.0 版本的 OVA、 ` gkectl ` 和升级软件包，请参阅
[ 下载 ](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=zh-
cn#latest) 。然后，请参阅 [ 升级管理员工作站 ](https://cloud.google.com/anthos/gke/docs/on-
prem/how-to/upgrading?hl=zh-cn) 和 [ 升级集群
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=zh-cn)
。

此补丁程序版本包含以下更改：

###  新增功能

**FEATURE:**

发布了 [ 强化集群的安全性 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/security/hardening-your-cluster?hl=zh-cn) 。

**FEATURE:**

发布了 [ 管理集群 ](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/managing-clusters?hl=zh-cn) 。

###  修复

**FIXED:**

修复了  11 月 5 日  的已知问题。

**FIXED:**

修复了  11 月 8 日  的已知问题。

###  已知问题

**ISSUE:**

如果您在 vSphere 中运行多个数据中心，则运行 ` gkectl diagnose cluster ` 可能会返回以下错误，您可以放心忽略该错误：

    
    
    Checking storage...FAIL
    path '*' resolves to multiple datacenters

**ISSUE:**

如果您运行的是 vSAN 数据存储区，运行 ` gkectl diagnose cluster ` 可能会返回以下错误，您可以放心忽略该错误：

    
    
    PersistentVolume [NAME]: virtual disk "[[DATASTORE_NAME]]
    [PVC]" IS NOT attached to machine "[MACHINE_NAME]" but IS listed in the Node.Status

##  2019 年 11 月 8 日

**ISSUE:**

在 GKE on-prem 1.1.1-gke.2 版本中，已知问题会阻止创建配置为使用 Docker 注册表的集群。您可以通过填充 GKE On-Prem
配置文件的 ` privateregistryconfig ` 字段来配置 Docker 注册表。集群创建失败，并显示错误，例如 ` Failed to
create root cluster: could not create external client: could not create
external control plane: docker run error: exit status 125 `

针对版本 1.1.2 进行了修正。与此同时，如果要创建配置为使用 Docker 注册表的集群，请将 ` --skip-validation-docker `
标志传递给 ` gkectl create cluster ` 。

##  2019 年 11 月 5 日

**ISSUE:**

GKE On-Prem 的配置文件有一个字段 ` vcenter.datadisk ` ，用于查找虚拟机磁盘（VMDK）文件的路径。在安装期间，您需要为
VMDK 选择一个名称。默认情况下，GKE On-Prem 会创建一个 VMDK 并将其保存到 vSphere 数据存储区的根目录中。

如果您使用的是 vSAN 数据存储区，则需要在数据存储区中创建用于保存 VMDK 的文件夹。您可以提供该字段的完整路径（例如 ` datadisk:
anthos/gke/docs/on-prem/datadisk.vmdk ` ），并且 GKE On-Prem 会将 VMDK 保存在该文件夹中。

创建文件夹时，vSphere 会为文件夹分配一个通用唯一标识符（UUID）。虽然您提供了 GKE On-Prem 配置的文件夹路径，但是 vSphere
API 会查找文件夹的 UUID。目前，这种不匹配可能会导致集群创建和升级失败。

针对版本 1.1.2 进行了修正。与此同时，您需要提供文件夹的 UUID，而不是文件夹的路径。按照 [ 升级集群
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/upgrading-clusters?hl=zh-cn#admin_datadisk_folder)
和安装主题中当前提供的解决方法说明进行操作。

##  2019 年 10 月 25 日

GKE On-Prem 1.1.1-gke.2 版本现已发布。要下载 1.1.1-gke.2 版本的 OVA、 ` gkectl ` 和升级软件包，请参阅
[ 下载 ](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=zh-
cn#latest) 。然后，请参阅 [ 升级管理员工作站 ](https://cloud.google.com/anthos/gke/docs/on-
prem/how-to/upgrading?hl=zh-cn) 和 [ 升级集群
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading?hl=zh-cn)
。

此补丁程序版本包含以下更改：

###  新增功能

**FEATURE:**

**所需操作** ：此版本将管理员工作站上的最低 ` gcloud ` 版本升级到 256.0.0。您应该 [ 升级管理员工作站
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/upgrading-admin-workstation?hl=zh-cn) 。然后，您应该 [ 升级集群
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/upgrading-clusters?hl=zh-cn) 。

**FEATURE:**

开源 [ CoreOS 工具箱 ](https://github.com/coreos/toolbox) 现已包含在所有 GKE On-Prem
集群节点中。这套工具对于排查节点问题非常有用。请参阅 [ 使用工具箱调试节点问题
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/support/toolbox?hl=zh-cn) 。

###  修复

**FIXED:**

修复了导致配置 OIDC 的集群无法升级的问题。

**FIXED:**

修复了 [ 安全公告 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/security-bulletins?hl=zh-cn#october-16-2019) 中描述的 [
CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) 。

**FIXED:**

修复了由于与 Google Cloud 的连接中断而导致集群指标丢失的问题。当 GKE On-Prem 集群与 Google Cloud
之间的连接断开一段时间后，该集群的指标现在会完全恢复。

**FIXED:**

修复了导致提取管理员集群指标比提取用户集群指标慢的问题。

###  已知问题

**ISSUE:**

对于使用静态 IP
且使用与管理员集群不同的网络的用户集群：如果您覆盖用户集群的网络配置，则用户控制平面可能无法启动。这是因为它使用的是用户集群的网络，但从管理员集群分配 IP
地址和网关。

要解决此问题，您可以更新每个用户控制平面的 MachineDeployment 规范以使用正确的网络。然后，删除每个用户控制平面 Machine，使
MachineDeployment 创建新的 Machines：

  1.     # List MachineDeployments in the admin cluster
        kubectl get machinedeployments --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

  2.     # Update a user control plane MachineDeployment from your shell
        kubectl edit machinedeployment --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] [MACHINEDEPLOYMENT_NAME]

  3.     # List Machines in the admin cluster
        kubectl get machines --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

  4.     # Delete user control plane Machines in the admin cluster
        kubectl delete machines --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] [MACHINE_NAME]

##  2019 年 9 月 26 日

GKE On-Prem 1.1.0-gke.6 版本现已发布。要下载 1.1.0-gke.6 版本的 OVA、 ` gkectl ` 和升级软件包，请参阅
[ 下载 ](https://cloud.google.com/anthos/gke/docs/on-prem/downloads?hl=zh-
cn#latest) 。然后，请参阅 [ 升级集群 ](https://cloud.google.com/anthos/gke/docs/on-
prem/how-to/upgrading?hl=zh-cn) 。

此次要版本包含以下更改：

###  新增功能

**FEATURE:**

集群节点的默认 Kubernetes 版本现在是版本 1.13.7-gke.20（以前是版本 1.12.7-gke.19）。

**FEATURE:**

**所需操作** ：从版本 1.1.0-gke.6 开始，GKE On-Prem 现在为您的用户集群节点创建 vSphere [ Distributed
Resource Scheduler（DRS） ](https://www.vmware.com/products/vsphere/drs-
dpm.html) 规则，使它们分布在数据中心的至少三个物理主机上。

**默认情况下，系统会为运行版本 1.1.0-gke.6 的所有新用户和现有用户集群启用此功能。**

要使用此功能，您的 vSphere 环境需要满足以下条件：

  * 必须启用 VMware DRS。VMware DRS 需要 vSphere Enterprise Plus 许可版本。如需了解如何启用 DRS，请参阅 [ 在集群中启用 VMware DRS ](https://kb.vmware.com/s/article/1034280) 。 
  * GKE On-Prem 配置文件的 ` vcenter ` 字段中提供的 vSphere 用户帐号必须具有 ` Host.Inventory.EditCluster ` 权限。 
  * 至少有三个物理主机可用。 

如果您 _不_ 想要为现有用户集群启用此功能（例如，如果您没有足够的主机来容纳该功能），请在升级用户集群 _之前_ 执行以下步骤：

  1. 打开现有的 GKE On-Prem 配置文件。 
  2. 在 ` usercluster ` 规范下，按照 [ ` antiaffinitygroups ` 文档 ](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-to/installation/install?hl=zh-cn#antiaffinitygroups) 中所述添加 ` antiaffinitygroups ` 字段： 
    
        usercluster:
          ...
          antiaffinitygroups:
            enabled: false
    

  3. 保存文件。 
  4. 使用配置文件进行升级。您的集群已升级，但该功能未启用。 

**FEATURE:**

您现在可以为集群设置 [ 默认存储类别 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/default-storage-class?hl=zh-cn) 。

**FEATURE:**

您现在可以将 [ 容器存储接口（CSI）1.0 ](https://github.com/container-storage-interface/spec)
用作集群的存储类别。

**FEATURE:**

您现在可以使用 ` gkectl delete cluster --force ` [ 删除已损坏或运行状况不佳的用户集群
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/deleting-a-user-cluster?hl=zh-cn#delete_unhealthy_cluster)

**FEATURE:**

您现在可以使用 ` debug-toolbox ` 容器映像 [ 诊断节点问题
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/support/debug-
toolbox?hl=zh-cn) 。

**FEATURE:**

您现在可以通过运行 ` gkectl ` 命令 [ 跳过验证 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/installation/install?hl=zh-cn#skip_validate) 。

**FEATURE:**

默认情况下， ` gkectl diagnose snapshot ` 创建的 tar 压缩包现在包含命令输出的日志。

**FEATURE:**

添加 ` gkectl diagnose snapshot ` 标志 ` --seed-config ` 。当您传递标志时，它会在由 ` snapshot
` 生成的压缩包中包含集群的 GKE On-Prem 配置文件。

###  更改

**CHANGED:**

已从 GKE On-Prem 配置文件中删除 ` gkeplatformversion ` 字段。要指定集群的版本，请将版本的集合提供给 `
bundlepath ` 字段。

**CHANGED:**

在使用 [ ` antiaffinitygroups ` ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/installation/install?hl=zh-cn#antiaffinitygroups)
之前，您需要先添加 vSphere 权限 ` Host.Inventory.EditCluster ` 。

**CHANGED:**

现在，您可以通过传递 ` --snapshot-config ` （以前为 ` --config ` ）在 ` gkectl diagnose
snapshot ` 中指定配置文件。请参阅 [ 诊断集群问题 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/support/diagnose?hl=zh-cn#diagnose_snapshot) 。

**CHANGED:**

现在，您可以通过传递 ` --snapshot-config ` （以前为 ` --config ` ）使用 ` gkectl diagnose
snapshot ` 捕获集群的配置文件。请参阅 [ 诊断集群问题
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/support/diagnose?hl=zh-cn#diagnose_snapshot) 。

**CHANGED:**

如果您提供用户集群的 kubeconfig 而不是管理员集群的 kubeconfig，则 ` gkectl diagnose ` 命令现在会返回错误。

**CHANGED:**

Cloud Console 现在会在注册用户集群的升级可用时通知您。

###  已知问题

**ISSUE:**

已知问题会阻止使用 OIDC 的 1.0.11 版、1.0.1-gke.5 版和 1.0.2-gke.3 版集群升级至版本 1.1。针对版本 1.1.1
进行了修正。如果您配置了带有 OIDC 的版本 1.0.11、1.0.1-gke.5 或 1.0.2-gke.3 集群，则无法对其进行升级。按照 [ 安装
GKE On-Prem ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/install?hl=zh-cn) 创建版本 1.1 集群。

##  2019 年 8 月 22 日

GKE On-Prem 1.0.2-gke.3 版本现已发布。此补丁程序版本包含以下更改：

###  新增功能

**FEATURE:**

Seesaw 现在支持手动负载平衡。

**FEATURE:**

现在可以为管理员集群和用户集群指定不同的 vSphere 网络。

**FEATURE:**

您现在可以使用 ` gkectl ` 删除用户集群。请参阅 [ 删除用户集群
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/deleting-a-user-cluster?hl=zh-cn) 。

###  更改

**CHANGED:** ` gkectl diagnose snapshot ` 现在从用户集群控制平面获取日志。

**CHANGED:**

GKE On-Prem OIDC 规范已更新，新增了几个字段： ` kubectlredirecturl ` 、 ` scopes ` 、 `
extraparams ` 和 ` usehttpproxy ` 。

**CHANGED:**

Calico 已更新至 3.7.4 版本。

**CHANGED:**

Cloud Monitoring 的系统指标前缀已从 ` external.googleapis.com/prometheus/ ` 更改为 `
kubernetes.io/anthos/ ` 。如果您要跟踪指标或提醒，请使用下一个前缀更新您的信息中心。

###  修复

**FIXED:**

[ 修复了 CVE-2019-11247 中的漏洞 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/security-bulletins?hl=zh-cn#august-22-2019) 。

**FIXED:**

[ 修复了 RBAC 代理中的漏洞 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/security-bulletins?hl=zh-cn#august-23-2019) 。

##  2019 年 7 月 30 日

GKE On-Prem 1.0.1-gke.5 版本现已发布。此补丁程序版本包含以下更改：

###  新增功能

**FEATURE:**

已发布 [ GKE On-Prem 备忘单 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/reference/cheatsheet?hl=zh-cn) 。

###  更改

**CHANGED:**

如果您使用的是静态 IP， ` gkectl check-config ` 现在还会检查节点 IP 是否可用。

**CHANGED:**

在尝试上传虚拟机的 OVA 映像之前， ` gkectl prepare ` 现在会检查虚拟机是否存在并在 vSphere 中被标记为模板。

**CHANGED:**

添加了对指定 vCenter 集群以及该集群中资源池的支持。

**CHANGED:**

将 F5 BIG-IP 控制器升级到 1.9.0 版。

**CHANGED:**

将 Istio Ingress 控制器升级到 1.2.2 版。

###  修复

**FIXED:**

修复了管理员工作站的 Docker 注册表中的注册表数据永久性问题。

**FIXED:**

修复了检查用户集群名称是否已在使用的验证。

##  2019 年 7 月 25 日

GKE On-Prem 1.0.11 版现已推出。

##  2019 年 6 月 17 日

GKE On-Prem 现已全面推出。1.0.10 版包含以下更改：

###  从 beta-1.4 版升级到 1.0.10 版

在将您的 Beta 版集群升级至首个通用版本之前，请执行 [ 从 GKE On-Prem Beta 版升级到通用版
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/upgrading/from-beta?hl=zh-cn) 中所述步骤，并注意以下几点：

  * 如果您运行的是 beta-1.4 之前的 Beta 版，请务必先升级到 beta-1.4 版本。 

  * 如果您的 Beta 版集群运行自己的 L4 负载平衡器（不是默认的 F5 BIG-IP），您需要删除并重新创建集群，以运行最新的 GKE On-Prem 版本。 

  * 如果您的集群已从 beta-1.3 升级到 beta-1.4，请在升级之前 _对每个用户集群_ 运行以下命令： 
    
        kubectl delete crd networkpolicies.crd.projectcalico.org

  * 现在需要验证 vCenter 证书。（已不再支持“ ` vsphereinsecure ` ”。）如果您要将 Beta 版 1.4 集群升级到 1.0.10，则需要在升级配置文件中提供受 vCenter 信任的根 CA 公共证书。 

  * 您需要升级 _所有_ 正在运行的集群。要使此升级成功，您的集群不能以混合版本状态运行。 

  * 您需要先将管理员集群升级到最新版本，然后再升级您的用户集群。 

###  新增功能

**FEATURE:**

您现在可以启用 [ 手动负载平衡模式 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/installation/manual-lb?hl=zh-cn) 来配置 L4
负载平衡器。您仍然可以选择使用默认负载平衡器 F5 BIG-IP。

**FEATURE:**

已更新 GKE On-Prem 的配置驱动安装过程。您现在可以使用单个 [ 配置文件
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/overview?hl=zh-
cn#config) 进行声明式安装。

**FEATURE:**

添加 ` gkectl create-config ` ，可生成用于安装 GKE On-
Prem、升级现有集群以及在现有安装中创建其他用户集群的配置文件。这将取代安装向导和先前版本中的 ` create-config.yaml ` 。请参阅有关
[ 安装 GKE On-Prem ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/installation/install?hl=zh-cn#generate_config) 的更新文档。

**FEATURE:**

添加 ` gkectl check-config ` ，用于验证 GKE on-prem 配置文件。请参阅有关 [ 安装 GKE On-Prem
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/install?hl=zh-cn#validate_config) 的更新文档。

**FEATURE:**

向 ` gkectl prepare ` 添加可选的 ` --validate-attestations `
标志。此标志用于验证您的管理员工作区中包含的容器映像是否由 Google 构建并签名，并已准备好部署。请参阅有关 [ 安装 GKE On-Prem
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/install?hl=zh-cn#prepare) 的更新文档。

###  更改

**CHANGED:**

将 Kubernetes 版本升级到 1.12.7-gke.19。您现在可以 [ 将集群升级
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/upgrading-clusters?hl=zh-cn) 到此版本。您无法再创建运行 Kubernetes 版本
1.11.2-gke.19 的集群。

我们建议您先升级管理员集群，然后再升级用户集群。

**CHANGED:**

将 Istio Ingress 控制器升级到 1.1.7 版本。

**CHANGED:**

现在需要验证 vCenter 证书。已不再支持“ ` vsphereinsecure ` ”）。您可以在 GKE On-Prem 配置文件的 `
cacertpath ` 字段中提供证书。

当客户端调用 vCenter 服务器时，vCenter
服务器必须通过出示证书来向客户端证明其身份。该证书必须由证书授权机构（CA）签署。证书不能是自签名证书。

如果要将 Beta 1.4 集群升级到 1.0.10，则需要在升级配置文件中提供受 vCenter 信任的根 CA 公共证书。

###  已知问题

**ISSUE:**

[ 升级集群 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/upgrading-clusters?hl=zh-cn) 可能会导致使用 [ PodDisruptionBudgets
](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-
disruption-budgets-work) （PDBs）的工作负载中断或停机。

**ISSUE:**

您可能无法将使用 [ 手动负载平衡模式 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/installation/manual-lb?hl=zh-cn) 的 Beta 版集群升级到 GKE On-
Prem 版本 1.0.10。要对这些集群进行升级并继续使用您自己的负载平衡器，您需要重新创建集群。

##  2019 年 5 月 24 日

GKE On-Prem Beta 版 1.4.7 现已发布。此版本包括以下更改：

###  新增功能

**FEATURE:**

在 [ ` gkectl diagnose snapshot `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.4/how-
to/administration/diagnose?hl=zh-cn#capture_admin) 命令中， ` --admin-ssh-key-path
` 参数现在是可选的。

###  更改

**CHANGED:**

我们于 2019 年 5 月 8 日对 Connect 进行了一项更改，该服务可让您使用 Cloud Console 与 GKE On-Prem
集群进行交互。要使用新的 Connect Agent，您必须向 Cloud Console 重新注册集群，或者必须升级到 Anthos GKE On-
Prem Beta 版 1.4。

您的 GKE On-Prem 集群及其上运行的工作负载将继续不间断运行。但是，在您重新注册集群或升级到 beta-1.4 之前，集群在 Cloud
Console 中将不可见。

在重新注册或升级之前，请确保您的服务帐号具有 ` gkehub.connect ` 角色。此外，如果您的服务帐号具有旧的
clusterregistry.connect 角色，则最好移除该角色。

为您的服务帐号授予 gkehub.connect 角色：

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

如果您的服务帐号具有旧的 ` clusterregistry.connect ` 角色，请移除旧角色：

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/clusterregistry.connect"

重新注册您的集群，或升级到 Anthos GKE On-Prem beta-1.4。

要 [ 重新注册集群 ](https://cloud.google.com/kubernetes-engine/connect/updating-
agent?hl=zh-cn) ，请执行以下操作：

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \
          --context=[USER_CLUSTER_CONTEXT] \
          --service-account-key-file=[LOCAL_KEY_PATH] \
          --kubeconfig-file=[KUBECONFIG_PATH] \
          --project=[PROJECT_ID]
          

要 [ 升级到 Anthos GKE on-prem beta-1.4
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.4/how-
to/administration/upgrading-a-cluster?hl=zh-cn) ，请执行以下操作：

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  已知问题

**ISSUE:**

有一个问题会导致 Connect Agent 在升级期间无法更新到新版本。要解决此问题，请在升级集群后运行以下命令：

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  2019 年 5 月 13 日

###  已知问题

**ISSUE:**

从版本 beta-1.2 升级到 beta-1.3
的集群可能会受到已知问题的影响，该问题会损坏集群的配置文件并阻止集群日后升级。此问题会影响所有将来的集群升级。

您可以通过删除并重新创建从 beta-1.2 升级到 beta-1.3 的集群来解决此问题。

要在不删除和重新创建集群的情况下解决此问题，您需要重新编码并应用每个集群的 Secret。执行以下步骤：

  1. 获取管理员集群中存储的 ` create-config ` Secrets 的内容。必须针对 kube-system 命名空间中的 ` create-config ` Secret 和每个用户集群命名空间中的 ` create-config ` Secrets 执行此操作： 
    
        kubectl get secret create-config -n kube-system -o jsonpath={.data.cfg} | base64 -d > kube-system_create_secret.yaml
    
        kubectl get secret create-config -n [USER_CLUSTER_NAME] -o jsonpath={.data.cfg} | base64 -d > [USER_CLUSTER_NAME]_create_secret.yaml

  2. 对于每个用户集群，在编辑器中打开 ` [USER_CLUSTER_NAME]  _create_secret.yaml ` 文件。如果 ` registerserviceaccountkey ` 和 ` connectserviceaccountkey ` 的值不是 ` REDACTED ` ，则无需采取进一步操作：Secret 不需要重新编码并写入集群。 
  3. 在其他编辑器中打开原始 ` create_config.yaml ` 文件。 
  4. 在 ` [USER_CLUSTER_NAME]  _create_secret.yaml ` 中，将 ` registerserviceaccountkey ` 和 ` connectserviceaccountkey ` 的值替换为原始值 ` create_config.yaml ` 文件中的值。保存更改后的文件。 
  5. 对每个 ` [USER_CLUSTER_NAME]  _create_secret.yaml ` 以及 ` kube-system_create_secret.yaml ` 文件，请重复执行第 3 至 5 步。 
  6. Base64 对每个 ` [USER_CLUSTER_NAME]  _create_secret.yaml ` 文件和 ` kube-system_create_secret.yaml ` 文件进行编码： 
    
        cat [USER_CLUSTER_NAME]_create_secret.yaml | base64 > [USER_CLUSTER_NAME]_create_secret_create_secret.b64
    
        cat kube-system-cluster_create_secret.yaml | base64 >kube-system-cluster_create_secret.b64

  7. 将集群中每个 Secret 中的 ` data[cfg] ` 字段替换为相应文件的内容： 
    
        kubectl edit secret create-config -n [USER_CLUSTER_NAME]
    
      # kubectl edit opens the file in the shell's default text editor
      # Open `first-user-cluster_create_secret.b64` in another editor, and replace
      # the `cfg` value with the copied value
      # Make sure the copied string has no newlines in it!

  8. 为每个 ` [USER_CLUSTER_NAME]  _create_secret.yaml ` Secret 和 ` kube-system_create_secret.yaml ` Secret 重复步骤 8。 
  9. 要确保更新成功，请重复步骤 1。 

##  2019 年 5 月 7 日

GKE On-Prem Beta 版 1.4.1 现已发布。此版本包括以下更改：

###  新增功能

**FEATURE:**

在 [ ` gkectl diagnose snapshot `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.4/how-
to/administration/diagnose?hl=zh-cn#capture_admin) 命令中， ` --admin-ssh-key-path
` 参数现在是可选的。

###  更改

**CHANGED:**

我们于 2019 年 5 月 8 日对 Connect 进行了一项更改，该服务可让您使用 Cloud Console 与 GKE On-Prem
集群进行交互。要使用新的 Connect Agent，您必须向 Cloud Console 重新注册集群，或者必须升级到 Anthos GKE On-
Prem Beta 版 1.4。

您的 GKE On-Prem 集群及其上运行的工作负载将继续不间断运行。但是，在您重新注册集群或升级到 beta-1.4 之前，集群在 Cloud
Console 中将不可见。

在重新注册或升级之前，请确保您的服务帐号具有 gkehub.connect 角色。此外，如果您的服务帐号具有旧的
clusterregistry.connect 角色，则最好移除该角色。

为您的服务帐号授予 gkehub.connect 角色：

    
    
    gcloud projects add-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/gkehub.connect"

如果您的服务帐号具有旧的 clusterregistry.connect 角色，请移除旧角色：

    
    
    gcloud projects remove-iam-policy-binding [PROJECT_ID] \
          --member="serviceAccount:[SERVICE_ACCOUNT_NAME]@[PROJECT_ID].iam.gserviceaccount.com" \
          --role="roles/clusterregistry.connect"

重新注册您的集群，或升级到 Anthos GKE On-Prem beta-1.4。

要 [ 重新注册集群 ](https://cloud.google.com/kubernetes-engine/connect/updating-
agent?hl=zh-cn) ，请执行以下操作：

    
    
    gcloud alpha container hub register-cluster [CLUSTER_NAME] \
          --context=[USER_CLUSTER_CONTEXT] \
          --service-account-key-file=[LOCAL_KEY_PATH] \
          --kubeconfig-file=[KUBECONFIG_PATH] \
          --project=[PROJECT_ID]
          

要 [ 升级到 Anthos GKE on-prem beta-1.4
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.4/how-
to/administration/upgrading-a-cluster?hl=zh-cn) ，请执行以下操作：

    
    
    gkectl upgrade --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]

###  已知问题

**ISSUE:**

有一个问题会导致 Connect Agent 在升级期间无法更新到新版本。要解决此问题，请在升级集群后运行以下命令：

    
    
    kubectl delete pod gke-connect-agent-install -n gke-connect

##  2019 年 4 月 25 日

GKE On-Prem Beta 版 1.3.1 现已发布。此版本包括以下更改：

###  新增功能

**FEATURE:**

` gkectl diagnose snapshot ` 命令现在有一个 [ ` --dry-run `
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.3/how-
to/administration/diagnose?hl=zh-cn#performing_a_dry_run_for_a_snapshot) 标志。

**FEATURE:**

` gkectl diagnose snapshot ` 命令现在支持四种 [ 场景
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.3/how-
to/administration/diagnose?hl=zh-cn#snapshot_scenarios) 。

**FEATURE:**

` gkectl diagnose snapshot ` 命令现在支持用于指定命名空间的正则表达式。

###  更改

**CHANGED:**

Istio 1.1 现在是默认的 [ 入站流量控制器 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/beta-1.3/how-to/administration/upgrading-a-cluster?hl=zh-
cn#upgrading_the_ingress_controller) 。入站流量控制器在管理员集群和用户集群的 ` gke-system `
命名空间中运行。这样可以让入站流量的传输层安全协议(TLS)管理更加轻松。要启用 Ingress 或在升级后重新启用 Ingress，请按照 [ 启用
Ingress ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/beta-1.3/how-to/installation/install?hl=zh-
cn#enabling_ingress) 下的说明操作。

**CHANGED:**

` gkectl ` 工具不再使用 Minikube 和 KVM 进行引导。这意味着您无需在管理员工作站虚拟机上启用嵌套虚拟化。

###  已知问题

**ISSUE:**

GKE on-prem 的入站流量控制器使用 Istio 1.1，具有自动 Secret 发现功能。但是，用于 Secret 发现的节点代理可能无法在
Secret 删除后获取 Secret 更新。因此，请避免删除 Secret。如果必须删除 Secret 且 Ingress TLS 之后失败，请在 GKE
系统命名空间中手动重启 Ingress Pod。

##  2019 年 4 月 11 日

GKE On-Prem Beta 版 1.2.1 现已发布。此版本包括以下更改：

###  新增功能

**FEATURE:**

GKE On-Prem 集群现在自动使用 [ Connect ](https://cloud.google.com/kubernetes-
engine/connect?hl=zh-cn) 连接回 Google。

**FEATURE:**

现在，每个用户集群最多可以运行 3 个控制平面。

###  更改

**CHANGED:**

` gkectl ` 现在验证 vSphere 和 F5 BIG-IP 凭据创建集群。

###  已知问题

**ISSUE:**

回归会导致 ` gkectl diagnose snapshot ` 命令使用错误的 SSH
密钥，从而导致命令无法从用户集群中收集信息。作为支持案例的解决方法，您可能需要通过 SSH 连接到个人用户集群节点并手动收集数据。

##  2019 年 4 月 2 日

GKE On-Prem Beta 版 1.1.1 现已发布。此版本包括以下更改：

###  新增功能

**FEATURE:**

您现在可以使用 [ 开放虚拟设备（OVA） ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/beta-1.1/how-to/installation/getting-started?hl=zh-
cn#download_ova) 安装 GKE On-
Prem，这是一个包含多个命令行界面工具的预配置虚拟机映像。此更改使安装变得更轻松，并且移除了一个虚拟化层。您不再需要在 Docker 容器内运行 `
gkectl ` 。

如果您在 beta-1.1.1 之前安装了 GKE On-Prem 版本，则应按照文档中的说明创建一个新的管理员工作站。安装新的管理员工作站之后，将任何
SSH 密钥、配置文件、kubeconfigs 和其他任何需要的文件从以前的工作站复制到新工作站。

**FEATURE:**

添加有关 [ 备份和恢复集群 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/beta-1.1/how-to/administration/backing-up?hl=zh-cn) 的文档。

**FEATURE:**

您现在可以使用 OIDC 和 ADFS 为集群配置身份验证。如需了解详情，请参阅 [ 使用 OIDC 和 ADFS 进行身份验证
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/beta-1.1/how-
to/security/oidc-adfs?hl=zh-cn) 和 [ 身份验证
](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/concepts/authentication?hl=zh-cn) 。

###  更改

**CHANGED:**

您现在必须使用管理员集群的私钥才能运行 ` gkectl diagnose snapshot ` 。

**CHANGED:**

在安装过程中添加了一个配置选项，用于部署多主实例用户集群。

**CHANGED:**

[ Connect 文档 ](https://cloud.google.com/kubernetes-engine/connect?hl=zh-cn)
已迁移。

###  修复

**FIXED:**

修复了在意外移除节点时集群网络可能中断的问题。

###  已知问题

**ISSUE:**

GKE On-Prem 的配置管理器已从 0.11 版升级到 0.13 版。系统的多个组件已重命名。您需要采取一些步骤来清理之前版本的资源并安装新实例。

如果您拥有配置管理器的有效实例：

  1. 卸载实例： 
    
        kubectl -n=nomos-system delete nomos --all

  2. 确保实例的命名空间没有资源： 
    
        kubectl -n nomos-system get all

  3. 删除命名空间： 
    
        kubectl delete ns nomos-system

  4. 删除 CRD： 
    
        kubectl delete crd nomos.addons.sigs.k8s.io

  5. 删除该操作的所有 kube-system 资源： 
    
        kubectl -n kube-system delete all -l k8s-app=nomos-operator

如果您没有有效的配置管理器实例，请执行以下操作：

  1. 删除配置管理器命名空间： 
    
        kubectl delete ns nomos-system

  2. 删除 CRD： 
    
        kubectl delete crd nomos.addons.sigs.k8s.io

  3. 删除该操作的所有 kube-system 资源： 
    
        kubectl -n kube-system delete all -l k8s-app=nomos-operator

##  2019 年 3 月 12 日

GKE On-Prem Beta 版 1.0.3 现已发布。此版本包括以下更改：

###  修复

**FIXED:**

修复了导致 Docker 证书保存到错误位置的问题。

##  2019 年 3 月 4 日

GKE On-Prem Beta 版 1.0.2 现已发布。此版本包括以下更改：

###  新增功能

**FEATURE:**

您现在可以运行 ` gkectl version ` 来检查您运行的是 ` gkectl ` 的哪个版本。

**FEATURE:**

您现在可以 [ 将用户集群升级 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/beta-1.0/how-to/administration/upgrading-a-cluster?hl=zh-cn)
到未来的 Beta 版。

**FEATURE:**

[ Anthos Config Management ](https://cloud.google.com/anthos-config-
management/docs?hl=zh-cn) 0.11.6 版现已发布。

**FEATURE:**

现在，每个节点都会启用 Stackdriver Logging。默认情况下，日志记录代理会将日志复制到您的 GCP 项目，仅用于控制平面服务、集群
API、vSphere 控制器、Calico、BIG-IP 控制器、Envoy 代理、Connect、Anthos Config
Management、Prometheus 和 Grafana 服务、Istio 控制平面和 Docker。默认情况下，排除应用容器日志，但可以选择启用。

**FEATURE:**

Stackdriver Prometheus Sidecar 捕获与 Logging 代理相同组件的指标。

**FEATURE:**

现在支持 [ Kubernetes 网络政策 ](https://kubernetes.io/docs/concepts/services-
networking/network-policies/) 。

###  更改

**CHANGED:**

您现在可以更新集群规范中的 IP 地址块，以扩展给定集群的 IP 范围。

**CHANGED:**

如果您在 alpha 版期间安装的集群在 Beta 版之后与 Google 断开连接，则可能需要重新连接。请参阅 [ 手动注册用户集群
](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/registering-a-user-cluster?hl=zh-cn) 。

**CHANGED:**

已更新 [ 使用入门 ](https://cloud.google.com/anthos/gke/docs/on-prem/archive/1.1/how-
to/installation/getting-started?hl=zh-cn) ，其中包括激活服务帐号和运行 ` gkectl prepare `
的步骤。

**CHANGED:**

` gkectl diagnose snapshot ` 现在仅收集配置数据并排除日志。此工具用于在打开支持案例之前捕获环境的详细信息。

**CHANGED:**

支持在集群创建时为 F5 BIG-IP 配置可选的 SNAT 池名称。这可用于在 [ F5 BIG-IP 控制器
](https://clouddocs.f5.com/products/connectors/k8s-bigip-ctlr/v1.8/) 上配置“
--vs-snat-pool-name”值。

**CHANGED:**

现在，您需要为在管理员集群中运行的插件提供 VIP。

###  修复

**FIXED:**

改进了集群大小调整操作，以防止意外删除节点。

##  2019 年 2 月 7 日

GKE On-Prem Alpha 版本 1.3 现已发布。此版本包括以下更改：

###  新增功能

**FEATURE:**

在安装过程中，您现在可以提供具有 ` nodeip ` 块的 YAML 文件来配置静态 IPAM。

###  更改

**CHANGED:**

您现在需要在 vSphere Datastore 中配置一个 100GB 磁盘。GKE On-Prem 使用该磁盘来存储其一些重要数据，例如
etcd。请参阅 [ 系统要求 ](https://cloud.google.com/anthos/gke/docs/on-
prem/requirements?hl=zh-cn) 。

**CHANGED:**

您现在只能为 ` nodeip ` 块提供小写主机名。

**CHANGED:**

GKE On-Prem 现在强制要求用户集群具有唯一名称。

**CHANGED:**

现在，使用 mTLS 和基于角色的访问控制来保护使用 Istio 端点的指标端点和 API。

**CHANGED:**

Grafana 的外部通信已停用。

**CHANGED:**

对 Prometheus 和 Alertmanager 运行状况检查的改进。

**CHANGED:**

Prometheus 现在使用安全端口来获取指标。

**CHANGED:**

对 Grafana 信息中心进行了几项更新。

###  已知问题

**ISSUE:**

如果您的 vCenter 用户帐号使用 ` DOMAIN\USER ` 之类的格式，则可能需要转义反斜杠（ ` DOMAIN\\USER `
）。在安装过程中，当提示输入用户帐户时，请务必执行此操作。

##  2019 年 1 月 23 日

GKE On-Prem Alpha 版本 1.2.1 现已发布。此版本包括以下更改：

###  新增功能

**FEATURE:**

您现在可以使用 ` gkectl ` [ 删除管理员集群 ](https://cloud.google.com/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/deleting-an-admin-cluster?hl=zh-cn) 。

###  更改

**CHANGED:**

` gkectl diagnose snapshot ` 命令现在允许您在捕获远程命令结果和文件的快照时指定节点。

##  2019 年 1 月 14 日

GKE On-Prem Alpha 版 1.1.2 现已发布。此版本包括以下更改：

###  新增功能

**FEATURE:**

您现在可以使用 ` gkectl prepare ` 命令拉取和推送 GKE On-Prem 容器映像，该映像弃用了 `
populate_registry.sh ` 脚本。

**FEATURE:**

现在， ` gkectl prepare ` 会提示您输入有关 vSphere 集群和资源池的信息。

**FEATURE:**

您现在可以使用 ` gkectl create ` 命令创建用户集群并将其添加到现有的管理员控制平面，方法是在创建集群期间出现提示时传入现有
kubeconfig 文件。

**FEATURE:**

现在，您可以在创建集群时为管理员集群和用户集群传入 Ingress TLS Secret。您将看到以下新提示：

` Do you want to use TLS for Admin Control Plane/User Cluster ingress? `

提供 TLS Secret 和证书可让 ` gkectl ` 设置 Ingress TLS。安装 TLS 后，系统不会自动停用 HTTP。

###  更改

**CHANGED:**

GKE On-Prem 现在运行 Kubernetes 版本 **1.11.2-gke.19** 。

**CHANGED:**

GKE On-Prem 的默认足迹已更改：

  * 用户集群节点的最低内存要求现在为 8192M。 

**CHANGED:**

GKE On-Prem 现在运行 Minikube 版本 **0.28.0** 。

**CHANGED:**

GKE 政策管理中心已升级到版本 **0.11.1** 。

**CHANGED:**

默认情况下 ` gkectl ` 不再提示您提供代理配置。

**CHANGED:**

用户集群命名空间中有三个新的 ConfigMap 资源： ` cluster-api-etcd-metrics-config ` 、 ` kube-
etcd-metrics-config ` 和 ` kube-apiserver-config ` 。GKE On-Prem
使用这些文件快速引导指标代理容器。

**CHANGED:**

kube-apiserver 事件现在位于其自己的 etcd 中。您可以在用户集群的命名空间中看到 kube-etcd-events。

**CHANGED:**

集群 API 控制器现在使用领导者选举。

**CHANGED:**

现在从凭据文件中提取 vSphere 凭据。

**CHANGED:**

` gkectl diagnose ` 命令现在可与管理员集群和用户集群配合使用。

**CHANGED:**

` gkectl diagnose snapshot ` 现在可以拍摄节点上远程文件的快照、节点上远程命令的结果和 Prometheus 查询。

**CHANGED:**

` gkectl diagnose snapshot ` 现在可以在多个并行线程中拍摄快照。

**CHANGED:**

` gkectl diagnose snapshot ` 现在允许您指定要从快照结果中排除的字词。

###  修复

**FIXED:**

修复了导致意外网络调用的 minikube 缓存问题。

**FIXED:**

修复了提取 F5 BIG-IP 凭据的问题。现在从凭据文件中读取凭据，而不是使用环境变量。

###  已知问题

**ISSUE:**

运行 ` gkectl prepare ` 时，您可能会遇到以下 [ ` govmomi `
](https://github.com/vmware/govmomi) 警告：

` Warning: Line 102: Unable to parse 'enableMPTSupport' for attribute 'key' on
element 'Config' `

**ISSUE:**

调整用户集群大小可能会导致无意中删除节点或重新创建节点。

**ISSUE:**

PersistentVolume 可能无法装载，从而产生错误 ` devicePath is empty ` 。要解决此问题，请删除并重新创建关联的
PersistentVolumeClaim。

**ISSUE:**

如果 Alpha 版不支持对节点使用静态 IP 分配，则需要调整 IPAM 地址块的大小。如需解决此问题，请考虑分配比当前所需更多的 IP 地址。

**ISSUE:**

在网速较慢的磁盘上，虚拟机创建可能会超时并导致部署失败。如果发生这种情况，请删除所有资源，然后重试。

##  2018 年 12 月 19 日

GKE On-Prem Alpha 版 1.0.4 现已发布。此版本包括以下更改：

###  修复

**FIXED:**

由 [ CVE-2018-1002105 ](https://github.com/kubernetes/kubernetes/issues/71411)
引起的漏洞已修补。

##  2018 年 11 月 30 日

GKE On-Prem Alpha 版 1.0 现已发布。此版本包括以下更改：

###  更改

**CHANGED:**

GKE On-Prem Alpha 版 1.0 运行 Kubernetes 1.11。

**CHANGED:**

GKE On-Prem 的默认足迹已更改：

  * 管理员控制平面运行三个节点，这些节点使用 4 个 CPU 和 16GB 内存。 
  * 用户控制平面运行一个使用 4 个 CPU 16GB 内存的节点。 
  * 用户集群至少运行 3 个节点，这些节点使用 4 个 CPU 和 16GB 内存。 

**CHANGED:**

支持高可用性 Prometheus 设置。

**CHANGED:**

支持自定义提醒 Manager 配置。

**CHANGED:**

Prometheus 已从 **2.3.2** 升级到 **2.4.3** 。

**CHANGED:**

Grafana 从 **5.0.4** 升级到 **5.3.4** 。

**CHANGED:**

kube-state-metrics 从 **1.3.1** 升级到 **1.4.0** 。

**CHANGED:**

Alert Manager 从 **1.14.0** 升级到 **1.15.2** 。

**CHANGED:**

node_exporter 从 **1.15.2** 升级到 **1.16.0** 。

###  修复

**FIXED:**

由 [ CVE-2018-1002103 ](https://github.com/kubernetes/minikube/issues/3208)
引起的漏洞已修补。

###  已知问题

**ISSUE:**

PersistentVolume 可能无法装载，从而产生错误 ` devicePath is empty ` 。要解决此问题，请删除并重新创建关联的
PersistentVolumeClaim。

**ISSUE:**

如果 Alpha 版不支持对节点使用静态 IP 分配，则需要调整 IPAM 地址块的大小。如需解决此问题，请考虑分配比当前所需更多的 IP 地址。

**ISSUE:**

GKE On-Prem Alpha 版 1.0 尚未通过所有一致性测试。

**ISSUE:**

每个管理员集群只能创建一个用户集群。要创建其他用户集群，请创建另一个管理员集群。

##  2018 年 10 月 31 日

GKE On-Prem EAP 2.1 现已发布。此版本包括以下更改：

###  更改

**CHANGED:**

当您同时创建管理员集群和用户集群时，现在可以重新使用管理员集群的 F5 BIG-IP 凭据来创建用户集群。此外，CLI 现在要求提供 BIG-IP
凭据；无法使用 ` --dry-run ` 跳过此要求。

**CHANGED:**

F5 BIG-IP 控制器已升级为使用最新 OSS 版本 1.7.0。

**CHANGED:**

为了提高慢速 vSphere 机器的稳定性，现在集群机器创建超时为 15 分钟（之前为 5 分钟）。

##  2018 年 10 月 17 日

GKE On-Prem EAP 2.0 现已发布。此版本包括以下更改：

###  更改

**CHANGED:**

支持 GKE Connect。

**CHANGED:**

支持 Monitoring。

**CHANGED:**

支持使用 private registries 进行安装。

**CHANGED:**

支持在 F5 BIG-IP 上将 L7 负载平衡器作为 L4 VIP 前端。

**CHANGED:**

支持在集群引导期间为节点分配静态 IP。

###  已知问题

**ISSUE:**

每个管理员集群只能创建一个用户集群。要创建其他用户集群，请创建另一个管理员集群。

**ISSUE:**

EAP 2.0 不支持集群升级。

**ISSUE:**

在网速较慢的磁盘上，虚拟机创建可能会超时并导致部署失败。如果发生这种情况，请删除所有资源，然后重试。

**ISSUE:**

作为集群引导过程的一部分，将运行一个短时效 minikube 实例。使用的 Minikube 版本存在安全漏洞 [ CVE-2018-1002103
](https://github.com/kubernetes/minikube/issues/3208) 。

