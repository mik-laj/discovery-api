#  版本说明

本页面记录 Migrate for Compute Engine 的正式版更新。您可以定期查看本页面，以了解有关新功能或更新功能、Bug
修复、已知问题和已弃用功能的公告。

您可以在 [ Google Cloud 版本说明 ](https://cloud.google.com/release-notes?hl=zh-cn)
页面上查看 Google Cloud 所有产品的最新产品动态。

要接收最新产品动态，请将本页面的网址添加到您的 [ Feed 阅读器
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) ，或直接添加 Feed 网址： `
https://cloud.google.com/feeds/migrate-for-compute-engine-release-notes.xml `

如需查看此版本及其他版本的构建列表，请参阅 [ 构建记录 ](https://cloud.google.com/migrate/compute-
engine/docs/build-history?hl=zh-cn) 。

##  要求和操作系统支持

请参阅 [ 要求 ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/concepts/requirements?hl=zh-cn) 和 [ 支持的操作系统
](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/supported-os-versions?hl=zh-cn) 。

##  4.10 新增功能

###  Cloud Console 集成

**FEATURE:**

V4.10 与 [ GCP Console ](https://cloud.google.com/cloud-console/?hl=zh-cn)
集成，可实现无缝部署迁移管理器以及创建必需的服务帐号。

###  部署到专用访问环境

**FEATURE:**

V4.10 支持部署到启用 API 专用访问权限的环境。在这些环境中，系统将在没有公共 IP 的情况下部署系统，并依赖于专用访问权限来访问云 API。请参阅
[ 配置迁移管理器 ](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-
to/configure-manager/configuring-migration-manager?hl=zh-cn) 。

###  vCenter 插件的可选部署

**FEATURE:**

V4.10 引入在部署或未部署 vCenter 插件时部署到本地来源 vCenter 环境的选项。通过部署而不使用 vCenter 插件，您可以将多个
Migrate 系统连接到同一 vCenter 环境。请参阅 [ 注册 VMware vCenter 环境
](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-to/configure-
manager/configuring-vms-vm?hl=zh-cn#register_the_vmware_vcenter_environment) 。

###  支持在将 Windows 2008 升级到 2012 之前/之后的自定义脚本

**FEATURE:**

V4.10 支持在使用 Windows 升级之前/之后运行自定义脚本。您可以向虚拟机添加自定义脚本。如需了解详情，请参阅 [ 升级 Windows
Server 虚拟机 ](https://cloud.google.com/migrate/compute-engine/docs/4.10/how-
to/upgrading-vms/upgrading-windows-vms?hl=zh-cn) 。

###  支持将 Azure Gen2 实例迁移到 Compute Engine

**FEATURE:**

V4.10 支持从 [ Azure Gen2 ](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/supported-os-versions?hl=zh-cn) 实例迁移到具有 UFI 支持的
Compute Engine 实例。

###  自动 O/S 发现和许可分配

**FEATURE:**

V4.10 引入自动识别已迁移操作系统的功能，默认情况下，系统会为已迁移的虚拟机分配正确的许可。如果您希望使用 Windows BYOL 许可或 Linux
高级许可迁移虚拟机，则需要在 Runbook 中以输入形式提供这些内容。请参阅文档中的 [ 许可部分
](https://cloud.google.com/migrate/compute-
engine/docs/4.10/reference/runbooks?hl=zh-cn) 。

##  修正的问题

**FIXED:**

修复了 AWS ena 驱动程序导致迁移后 Windows 映像崩溃的问题。

##  已知问题

**ISSUE:**

**＃149004085** ：本地 Ubuntu 14 可能无法启动网络发布分离。

**解决方法** ：通过串行控制台连接，并使用 DHCP 手动添加网络接口。

**ISSUE:**

**＃145086776** ：在极少数情况下，较低版本的 RHEL7 可能会在流式传输期间挂起或出现内核崩溃。此问题已在更高版本的 RHEL7
中得到解决。

**解决方法** ：在迁移之前运行 ` sudo yum update ` 以更新系统。

**ISSUE:**

**#145644737** ：通过使用 cloud-init 的 Linux 分发实例在 Azure 或 AWS 上创建克隆后，在安装 Linux
准备软件包后可能会遇到启动问题。

**解决方法** ：在克隆之前卸载软件包，并在准备迁移时重新安装。

**ISSUE:**

**#143313211** ：迁移 RHEL 6.8 虚拟机的客户可能会在云目标中遇到启动问题。

使用内核版本 2.6.32-xxx 以及使用 LVM 的 RHEL 6.x 系统可能会在迁移期间在 Compute Engine 中启动时发生内核崩溃。

**解决方法** ：在迁移之前，应将内核升级到 2.6.32-754 版或更高版本。

**ISSUE:**

**#143262721** ：当数据磁盘大于 4 TB 时，从 Azure 迁移虚拟机失败。

目前，Migrate for Compute Engine 不支持迁移数据磁盘大于 4TB 的 Azure 虚拟机。

**解决方法** ：确保虚拟机具有小于 4TB 的数据磁盘。

**ISSUE:**

**＃131532690** ：如果安装 Symantec Endpoint Protection (SEP)，则 Windows Server 2016
工作负载的云端运行和迁移操作可能会失败。当 SEP 似乎已停用时，也可能发生这种情况。

**解决方法** ：修改工作负载网络接口绑定以移除 SEP 选项。

  1. 下载 [ Microsoft Network VSP Bind (nvspbind) ](https://gallery.technet.microsoft.com/Hyper-V-Network-VSP-Bind-cf937850)
  2. 将 Microsoft_Nvspbind_package.EXE 安装到 c:\temp。 
  3. 以管理员身份打开命令提示符，然后运行以下命令： 
    
        nvspbind.exe /d * symc_teefer2

**ISSUE:**

**#131614405** ：当 SUSE Linux Enterprise Server 11 上安装 Velostrata Prep RPM
时，除了现有的静态 IP 配置之外，虚拟机还会获取 DHCP IP 地址。如果虚拟机在使用 DHCP 服务启用的子网中本地启动，则会出现此问题。

注意：如果子网没有 DHCP 服务，则不会出现此问题。与原始静态 IP 地址的通信没有连接影响。

**ISSUE:**

**#131637800** ：注册 Velostrata 插件后，运行 Cloud Extensions
扩展向导可能会在“完成”时生成错误“XXXXXXXXXX”。

**解决方法** ：取消注册 Velostrata 插件并重启 vSphere Web 客户端服务，然后重新注册该插件。如果问题仍然存在，请与支持团队联系。

**ISSUE:**

**#131548730** ：在某些情况下，将虚拟机移到“云端运行”，而第三方虚拟机级备份解决方案保留临时快照时，Migrate for Compute
Engine 定期写回操作不会完成，即使在备份解决方案删除临时快照之后也是如此。虚拟机上未提交的写入计数器将显示增大的大小，并且不会在本地创建一致性检查点。

**解决方法**
：为虚拟机选择“本地运行”操作，并等待任务完成，这将提交所有待处理的写入。然后，再次选择“云端运行”操作。请注意，提交许多待处理的写入可能需要一段时间。请勿使用“强制”选项，因为这会导致未提交的写入丢失。

**ISSUE:**

**#131605387** ：vCenter 重新启动会导致 vCenter 中的 Velostrata 任务从界面中消失。这是 vCenter 限制。

**解决方法** ：使用 Velostrata PowerShell 模块监控当前正在运行的 Velostrata 托管虚拟机或 Cloud
Extensions 任务。

**ISSUE:**

**＃131638716** ：如果 ESXi 主机处于维护模式，则将虚拟机移到云端时，操作将失败并在回滚阶段卡住。

**解决方法** ：手动取消“云端运行”任务，将虚拟机迁移到集群中的另一个 ESXi 主机，然后重试“云端运行”操作。

**ISSUE:**

**#131638455** ：云端运行操作失败，并显示错误“无法创建虚拟机快照。无法在当前状态（关机）下执行所尝试的操作”。

**解决方法** ：VMware 虚拟机快照文件可能指向不存在的快照。请联系支持团队来纠正问题。

**ISSUE:**

**#131534862** ：在极少数情况下，在本地重新运行工作负载 后，工作负载 VMDK 会被锁定。在某些情况下，这是因为 Velostrata
管理设备与运行工作负载的 ESXi 主机之间出现网络中断。

注意：问题会在 1-2 小时后自行解决。

**ISSUE:**

**＃131550214** ：在分离期间，操作可能会失败，并显示以下错误消息：“操作已取消”。

**解决方法** ：重试分离操作。

**ISSUE:**

**#131650367** ：在取消分离操作后执行分离时，操作可能会失败。

**解决方法** ：重试操作。

**ISSUE:**

**#131649978** ：如果出现特定系统故障，Velostrata 组件会断开与 vCenter
的连接。在这种情况下，系统可能不会发送事件，导致警报未正确设置或未正确清除。

**解决方法** ：在 vCenter 中手动清除警报。

**ISSUE:**

**#131532549** ：对于使用零售许可的 Windows 机器的工作负载，当从云端返回时，该许可不存在。

**解决方法** ：重新安装许可。

**ISSUE:**

**＃131555885** ：当云端的虚拟机在缓存模式下运行时，即可使用 vCenter“导出 OVA”操作，但此操作会导致 OVA 损坏。

**解决方法** ：仅在分离后创建 OVA。

**ISSUE:**

**#131647857** ：在极少数情况下，如果创建云组件实例且系统在标记之前失败，则该实例将保持未标记状态。这不允许完全清理或修复 CE。

**解决方法** ：手动标记实例，然后运行“修复”。

**ISSUE:**

**＃131537125** ：Cloud Extensions 高可用性不适用于运行具有 LVM 配置的 Ubuntu 操作系统的工作负载。

**解决方法** ：将内核更新到 3.13.0-161 或更高版本。

**ISSUE:**

**＃131560126** Suse12：由于 SUSE 内核低于 4.2 版本的错误，不支持包括含子卷的 BTRFS 装载的配置。

**解决方法** ：升级到内核 >=4.2 (SP2) 的 SUSE 版本。

**ISSUE:**

**＃131533480** ：使用“创建 Cloud Extensions”向导时，使用非法 HTTP 代理地址不会生成警告消息。

**解决方法** ：删除 CE，然后使用有效的 HTTP 代理地址创建 CE。

**ISSUE:**

**#131647654** ：本地运行操作成功，但将状态标记为失败，并显示错误“无法整合快照”

**解决方法** ：通过 vCenter 整合快照，并手动清除错误。

**ISSUE:**

**#131558198** ：在 PowerShell 3.0 上运行时，云端到云端 Runbook 的 PowerShell 客户端报告错误

**解决方法** ：升级到 PowerShell 4.0

**ISSUE:**

**#131533056** ：将 RHEL 7.4 从 AWS 迁移到 Google Cloud 时，不会自动安装 Google Cloud 代理。

**解决方法** ：手动移除 AWS 代理并安装 Google Cloud 代理

**ISSUE:**

**＃131532713** ：在 Windows 2003R2 的离线迁移之后，如果手动删除 NIC，则可能无法自动检测并自动重新安装它。

解决方法：可以将虚拟机存储附加到其他虚拟机，可以使用类似的虚拟机作为参考，手动导入 NIC 注册表项。请与支持团队联系以寻求帮助。

**ISSUE:**

**#131532666** ：使用内核版本 2.6.32 运行的 Linux 版本可能会在出现临时存储访问故障时遇到内核崩溃；当通过 iSCSI
进行流式传输时，发生这些情况的可能性更高。

解决方法：升级内核。分离后，发生该问题的可能性也会降低。

**ISSUE:**

**#131532846** ：某些防火墙和防病毒内容可能会在阻止 iSCSI 流量迁移到云端时导致 Windows 虚拟机失败。

解决方法：在迁移时停用受影响的服务，并在分离后重新安装。

**ISSUE:**

**＃131532882** ：在某些情况下，在 Windows 更新期间启动“云端运行”可能会导致更新突然终止并导致无法在云端启动。

解决方法：允许系统在迁移前完成 Windows 更新和/或暂停 Windows 更新。

**ISSUE:**

**＃135664281** ：在完成或取消 Azure 到 Google Cloud 的迁移时，如果 Velostrata Management
无法启动导入程序，则 Velostrata 创建的资源可能会保留在原始实例的资源组中。

**ISSUE:**

**＃133137658** 情景：迁移管理器和 VSphere 之间没有网络连接

客户影响：RunInCloud 任务将因 VSphere 上的 getReadSessions 调用失败而失败。

**解决方法** ：修复网络连接。如果不是，请取消该任务并重试。

**ISSUE:**

**#135573857** 情景：使用“强制”标志将虚拟机移回本地时，整合快照失败会导致虚拟机保持由 Velostrata
管理。在同一虚拟机上执行云端运行可能会失败，因为托管虚拟机上不允许。

**解决方法** ：等待几分钟，然后重试。

**ISSUE:**

**＃137082702** ：在极少数情况下，“取消分离”操作会成功，但虚拟机实例将无法启动。

**解决方法** ：将实例移回并再次将其移到云端。

