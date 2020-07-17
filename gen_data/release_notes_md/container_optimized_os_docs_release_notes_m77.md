#  Release Notes: Milestone 77

##  Current Status

Image Family  |  cos-77-lts  
---|---  
Deprecated After  |  Dec 17, 2020  
Kernel  |  [ 4.19.112
](https://cos.googlesource.com/third_party/kernel/+/5d4ffd91281840f7a118143d77fbefb02e87943c)  
Kubernetes  |  v1.15.3  
Docker  |  v19.03.1  
  
##  Changelog

###  cos-77-12371-326-0

_Date: July 13, 2020_

  * Added rsync back into the image, which was removed in cos-dev-77-12293-0-0. 
  * Mount /var/lib/containerd with exec option. 
  * Moved Kernel source to cos.googlesource.com. 
  * Fixed CVE-2019-9169. 

###  cos-77-12371-296-0

_Date: June 16, 2020_

  * Updated toolbox base container image to include security patches. 

###  cos-77-12371-274-0

_Date: May 26, 2020_

  * Fixed a few OS Login CVEs: CVE-2020-8903, CVE-2020-8907, CVE-2020-8933. 

###  cos-77-12371-273-0

_Date: May 21, 2020_

  * Fixed a Stackdriver Monitoring agent bug where not all mounted disk partitions has their usage reported. 

###  cos-77-12371-251-0

_Date: Apr 29, 2020_

  * Fixed a kernel bug where eBPF programs can cause softlockups. 

###  cos-77-12371-233-0

_Date: Apr 29, 2020_

  * Disabled `accept_ra` on all interfaces by default. 

###  cos-77-12371-227-0

_Date: Apr 05, 2020_

  * Upgraded the Linux kernel to v4.19.112. 
  * Backported systemd patch ba0d56f55 to address an issue that resulted in leaked mount units. 

###  cos-77-12371-208-0

_Date: Mar 17, 2020_

  * Enabled NETFILTER_XT_MATCH_SOCKET. 
  * Fixed a bug where DHCP is not started after link flaps. 
  * Removed size limit on /etc/ to fix cluster creation failure because of large number of addons. 
  * Upgraded the Linux kernel to v4.19.109. 

###  cos-77-12371-183-0

_Date: Feb 21, 2020_

  * Upgraded the Linux kernel to v4.19.104. 
  * Fixed TCP empty skb at the tail of the write queue bug in kernel. 

###  cos-77-12371-175-0

_Date: Feb 12, 2020_

  * Enabled some QoS and Fair Queuing options in the Linux kernel. 
  * Upgraded the Linux kernel to v4.19.102. 
  * Upgraded runc to 1.0.0-rc10. This resolves CVE-2019-19921. 

###  cos-77-12371-141-0

_Date: Jan 07, 2020_

  * Backported fix for Linux kernel CVE-2019-19072. 
  * Fixed CFS quota throttling issue. 
  * Upgraded the Linux kernel to v4.19.91. 

###  cos-77-12371-114-0

_Date: Oct 31, 2019_

  * Increased sysctl net.ipv4.tcp_limit_output_bytes to 1048576. 
  * Fixed the problem of spawning 8 runc state process for every exec on containerd. This was leading to high cpu utilization. 
  * Fixed the unnecessary creation of two separate test slices (resulting in 4 systemd log messages total + runtime overhead) for every runc execution. 
  * Fixed an issue in runc that resulted in unnecessary CPU consumption. Upgraded the Linux kernel to v4.19.80. 
  * Fixed a performance regression in completely fair scheduler (CFS). 

###  cos-77-12371-89-0

_Date: Oct 9, 2019_

  * Upgraded the Linux kernel to 4.19.76. 
  * Backported a kernel patch to ensure the cfs cgroup quota/period ratio always stays the same. This addresses a Kubernetes issue where the pod cgroup could be changed into an inconsistent state. 
  * Backported a kernel patch to fix performance regression in wbt scale_up/scale_down. 

###  cos-77-12371-76-0 (vs Milestone 73)

_Date: Sep 27, 2019_

####  New features

  * Enabled Shielded VM by default. Secure boot is not enabled by default. 
  * Enabled cgroup v2 hybrid mode in systemd. 
  * Added support for the virtio balloon driver. 
  * Added the node-problem-detector package. 
  * Added the conntrack-tools package. 
  * Added the xfsprogs package. 

####  Package updates

  * Upgraded systemd to version 239. 
  * Upgraded the Linux kernel to version 4.19. 
  * Upgraded Docker to version 19.03. 
  * Upgraded Kubelet to version 1.15. 
  * Upgraded the compute-image-packages to version 20190304. 
  * Upgraded openssl to version 1.0.2r. 
  * Upgraded openssh to version 7.9p1. 
  * Changed kernel compiler from gcc to clang. 

