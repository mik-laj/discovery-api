#  Release Notes: Milestone 69

##  Current Status

Image Family  |  cos-69-lts  
---|---  
Deprecated After  |  Dec 11, 2019  
Kernel  |  [ 4.14.145
](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/8549f18963962124c0f0d73667e59dbfc17c5218)  
Kubernetes  |  v1.11.8  
Docker  |  v17.03.2  
  
##  Changelog (vs Milestone 68)

###  cos-69-10895-385-0

_Date: Oct 08, 2019_

  * Upgraded the Linux kernel to 4.14.145. 
  * Backported a kernel patch to ensure the cfs cgroup quota/period ratio always stays the same. This addresses a Kubernetes issue where the pod cgroup could be changed into an inconsistent state. 

###  cos-69-10895-348-0

_Date: Aug 30, 2019_

  * Backported upstream writeback patches to fix a Docker hung issue. 

###  cos-69-10895-329-0

_Date: Aug 08, 2019_

  * Upgraded the Linux kernel to v4.14.137. This resolves CVE-2019-1125. 

###  cos-69-10895-299-0

_Date: Jul 12, 2019_

  * Fixed vulnerability in app-arch/bzip2 (CVE-2019-12900). 
  * Updated kernel to version v4.14.132. 
  * Fixed an issue introduced by NFLX-2019-001 fixes. 

###  cos-69-10895-277-0

_Date: Jun 19, 2019_

  * Updated the Linux kernel to version 4.14.127 to resolve the NFLX-2019-001 TCP SACK vulnerabilities. 

###  cos-69-10895-273-0

_Date: Jun 17, 2019_

  * Updated kernel to version v4.14.124. 

###  cos-69-10895-255-0

_Date: May 28, 2019_

  * Upgraded curl to v7.64.1 to fix CVE-2018-16890. 
  * Cherry-picked upstream patch https://patchwork.kernel.org/patch/10951403/ in kernel to fix a bug in lockd introduced by commit 01b79d20008d "lockd: Show pid of lockd for remote locks" in Linux kernel v4.14.105. 
  * Rotated keys used by UEFI Secure Boot for signing and verifying the UEFI boot path. 

###  cos-69-10895-242-0

_Date: May 15, 2019_

  * Merged Linux Stable Kernel 'v4.14.119' for resolving Microarchitectural Data Sampling (MDS) vulnerabilities (CVE-2018-12126, CVE-2018-12127, CVE-2018-12130, CVE-2019-11091). 
  * Mitigated a mount hang issue in the Linux kernel. 

###  cos-69-10895-211-0

_Date: Apr 11, 2019_

  * Fixed slow access to /sys/fs/cgroup/memory/memory.stat. This resolves kubelet performance degradation. 

###  cos-69-10895-201-0

_Date: Apr 01, 2019_

  * Included perf tool in the image. 
  * Included sosreport in the image. 
  * Updated the built-in kubelet to 1.11.8. 
  * Fixed an issue where Shielded VM integrity measurements weren't being logged properly. 
  * Merged Linux Stable Kernel 'v4.14.106'. 

###  cos-69-10895-172-0

_Date: Feb 28, 2019_

  * Enabled kernel.softlockup_all_cpu_backtrace. This was previously disabled to mitigate a kernel deadlock issue, which is now resolved. 
  * Configured docker.service by setting RestartSecs=10 to always restart Docker after 10 seconds. 

###  cos-69-10895-138-0

_Date: Jan 24, 2019_

  * Backported the fix for a deadlock issue in kernel panic. 
  * Merged Linux Stable Kernel 'v4.14.91'. 

###  cos-69-10895-123-0

_Date: Jan 10, 2019_

  * Set CONFIG_BLK_WBT_MQ=y to improve performance isolation on persistent disks. This fixes a bug where writes on a SSD persistent disk can affect performance on the Standard persistent boot disk. 
  * Cherry-picked Ext4 commits that address FS inconsistencies caused by disruptions during NFS CREATE operation under certain conditions. 
  * Merged Linux Stable Kernel 'v4.14.89'. 

###  cos-69-10895-102-0

_Date: Dec 20, 2018_

  * Disabled auto update on shielded images. Images in cos-cloud are not impacted by this change. 
  * Enabled the "metadata_csum" ext4 feature on the stateful partition. This also improves performance of boot-disk resize operation. 
  * Apply IMA Policy only when cloud-audit-setup.service is explicitly run. 

###  cos-69-10895-93-0

_Date: Nov 16, 2018_

  * Updated kernel to v4.14.79. 
  * Fixed the bug that cloud-init can't write gzipped files. 

###  cos-69-10895-91-0

_Date: Oct 29, 2018_

  * Fixed an issue where an interaction between IMA and NFS could cause deadlock. 
  * Fixed a stackdriver-logging.service issue observed in Containers on Compute Engine. 
  * PCID is now enabled by default when supported by the CPU platform. 

###  cos-69-10895-85-0

_Date: Oct 11, 2018_

  * Reset softlockup_all_cpu_backtrace to '0' to avoid kernel deadlock on high CPU machines under certain circumstances. 

###  cos-69-10895-71-0

_Date: Oct 1, 2018_

  * Removed userspace headers from kernel header artifact. 

###  cos-69-10895-62-0

_Date: Sept 18, 2018_

  * Promoted to Stable channel. 
  * Backport a fix to ensure that scsi contributes to randomness when running rotational device  . This addresses an issue where docker is slow to start because of low entropy on standard PDs since v4.14.63 merge. 
  * Enabled CONFIG_RANDOM_TRUST_CPU to address entropy starvation on PD-SSD boot disks. 
  * Upgraded OpenSSL to 1.0.2p 
  * Merged Linux stable version v4.14.65 
  * Backported the fix for a cloud-init bug that write_files can't deal with non-asci content  . 
  * Backport fix for a kernel warning "WARNING: fs/overlayfs/readdir.c:393 ovl_iterate+0x25c/0x260 WARN_ON(!cache->refcount)" 
  * Fix for Linux Kernel CVE-2018-12232 
  * Backport fixes for L1 Terminal Fault (L1TF) issue (CVE-2018-3615, CVE-2018-3620 and CVE-2018-3646). 
  * Fixes for CVE-2018-5391. 
  * Fixed a softlockup issue that occurred on single VCPU VMs when using FUSE filesystems. 
  * Updated Kubernetes to v1.11.1 
  * Fixes for CVE-2018-5390. 
  * Increase default kernel.pid_max to 2^22. 
  * Merged Linux stable version v4.14.54 into the kernel. 
  * Removed SCSI CD-ROM support. This resolves CVE-2018-11506. 
  * Upgraded built-in kubelet to v1.11.0 
  * Updated docker-credential-gcr to 1.5.0 
  * Updated BUG_REPORT_URL in /etc/os-release. 
  * Enabled NFS debug configs in the kernel. 
  * Enabled tcp_bbr kernel module for TCP congestion control. 
  * Upgraded Git to version 2.16.4 to fix CVE 2018-11235. 
  * Set '--disable-legacy-registry' Docker config to true by default. 
  * Updated Kubernetes to 1.10.4. 
  * Updated sshd_config to drop cbc based Ciphers. 
  * Updated root CA certificates to match Mozilla NSS 3.36.1. 
  * Updated OpenSSL to 1.0.2o. 

Send feedback

