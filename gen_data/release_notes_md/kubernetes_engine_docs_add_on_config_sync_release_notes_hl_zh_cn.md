#  版本说明

本页面记录 Config Sync 的正式版更新。您可以查看此页面，了解有关新增功能、功能更新、Bug 修复、已知问题和弃用功能的公告。

您可以在 [ Google Cloud 版本说明 ](https://cloud.google.com/release-notes?hl=zh_cn)
页面上查看 Google Cloud 所有产品的最新产品动态。

如需接收最新产品动态，请将本页面的网址添加到您的 [ Feed 阅读器
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ，或直接添加 Feed 网址： `
https://cloud.google.com/feeds/kubernetes-engine-add-on-config-sync-release-
notes.xml `

##  1.2.0

Config Sync v1.2.0 现已正式推出，适用于生产环境。这是该产品的第一个版本。

###  已知问题

**ISSUE:**

向存储库添加 [ APIService ](https://kubernetes.io/docs/concepts/extend-
kubernetes/api-extension) 会导致 Config Sync
进入错误状态，并显示错误消息“[KNV2002](/kubernetes-engine/docs/add-on/config-
sync/reference/errors#knv2002): failed to get server resources: unable to
retrieve the complete list of server
APIs”。此问题会影响通过此存储库同步的新集群和现有集群。如需纠正此问题，请按如下所述操作：

* 使用 ` kubectl get pods -n config-management-system ` 查找 ` git-importer ` 和 ` syncer ` Pod 的名称 
* 复制这些名称，然后使用 ` kubectl delete -n config-management-system pods git-importer-xxxx-xxxx syncer-xxxx-xxxx ` 重新 pod 
* 您必须对每个集群都执行一次这些步骤。 
重新启动集群的 Pod 后，同步将恢复正常。

**ISSUE:**

` nomos view ` 可能无法解析存在于存储库的本地克隆中但尚未同步到集群的 CRD（自定义资源定义）。

如需解决此问题，请使用 [ ` nomos hydrate ` ](https://cloud.google.com/kubernetes-
engine/docs/add-on/config-sync/how-to/nomos-command?hl=zh_cn#hydrate) 代替 `
nomos view ` 。

