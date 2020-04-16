#  版本说明：里程碑 69

##  当前状态

映像系列  |  cos-69-lts  
---|---  
已在此日期之后弃用  |  2019 年 12 月 11 日  
内核  |  [ 4.14.65+
](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/96d6d803ccae172c7a1e9b0f1fee8bcff8894756)  
Kubernetes  |  v1.11.1  
Docker  |  v17.03.2  
  
##  更新日志（与里程碑 68 相比）

###  cos-69-10895-91-0

_日期：2018 年 10 月 29 日_

  * 修复了 IMA 与 NFS 之间的交互可能导致死锁的问题。 
  * 修复了 Compute Engine 上的容器中观察到的“stackdriver-logging.service”问题。 
  * 现在，如果 CPU 平台具有相应支持，PCID 会默认启用。 

###  cos-69-10895-85-0

_日期：2018 年 10 月 11 日_

  * 将 softlockup_all_cpu_backtrace 重置为“0”，以避免在某些条件下高 CPU 机器类型上出现内核死锁。 

###  cos-69-10895-71-0

_日期：2018 年 10 月 1 日_

  * 从内核标头软件工件中删除了用户空间标头。 

###  cos-69-10895-62-0

_日期：2018 年 9 月 18 日_

  * 升级至稳定版。 
  * 反向移植了一项修复，以确保在运行旋转设备时 scsi 有助于保证随机性  。这解决了自 v4.14.63 合并以来，标准 PD 上的低熵导致 Docker 启动缓慢的问题。 
  * 启用 CONFIG_RANDOM_TRUST_CPU 以解决 PD-SSD 启动磁盘上的熵饥饿问题。 
  * 将 OpenSSL 升级到 1.0.2p 
  * 合并了 Linux 稳定版 v4.14.65 
  * 反向移植了一项解决 cloud-init 错误的修复，即 write_files 无法处理非 asci 内容  。 
  * 反向移植了内核警告“WARNING: fs/overlayfs/readdir.c:393 ovl_iterate+0x25c/0x260 WARN_ON(!cache->refcount)”的修复 
  * 修复 Linux 内核 CVE-2018-12232 
  * 反向移植了 L1 终端故障 (L1TF) 问题（CVE-2018-3615、CVE-2018-3620 和 CVE-2018-3646）的修复。 
  * 修复了 CVE-2018-5391。 
  * 修复了使用 FUSE 文件系统时在单 VCPU 虚拟机上发生的 softlockup 问题。 
  * 将 Kubernetes 更新为 v1.11.1 
  * 修复了 CVE-2018-5390。 
  * 将默认 kernel.pid_max 增加到 2^22。 
  * 将 Linux 稳定版 v4.14.54 合并到内核中。 
  * 移除了 SCSI CD-ROM 支持。这解决了 CVE-2018-11506。 
  * 将内置 kubelet 升级到 v1.11.0 
  * 将 docker-credential-gcr 更新为 1.5.0 
  * 更新了 /etc/os-release 中的 BUG_REPORT_URL。 
  * 在内核中启用了 NFS 调试配置。 
  * 启用了 tcp_bbr 内核模块以实现 TCP 拥塞控制。 
  * 将 Git 升级到版本 2.16.4 以修复 CVE 2018-11235。 
  * 默认将“--disable-legacy-registry”Docker 配置设置为 true。 
  * 将 Kubernetes 更新为 1.10.4。 
  * 更新了 sshd_config 以删除基于 cbc 的加密。 
  * 更新了根 CA 证书以匹配 Mozilla NSS 3.36.1。 
  * 将 OpenSSL 更新为 1.0.2o。 

