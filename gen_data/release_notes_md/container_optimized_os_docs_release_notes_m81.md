#  Release Notes: Milestone 81

##  Current Status

Image Family  |  cos-81-lts  
---|---  
Deprecated After  |  Jun 24, 2021  
Kernel  |  [ 4.19.112
](https://cos.googlesource.com/third_party/kernel/+/1d5bc45f886bc0308010614cdcdf658f5fb44a25)  
Kubernetes  |  v1.17.6  
Docker  |  v19.03.6  
  
##  Changelog

###  cos-81-12871-148-0

_Date: June 17, 2020_

  * Made dioread_nolock non-default. 

###  cos-81-12871-146-0

_Date: June 16, 2020_

  * Updated toolbox base container image to include security patches. 

###  cos-81-12871-130-0

_Date: June 16, 2020_

  * Updated the built-in kubectl/kubelet to v1.17.6 to fix a bug that could result in the inability to start a cluster. 

###  cos-81-12871-119-0

_Date: May 28, 2020_

  * Fixed a few OS Login CVEs: CVE-2020-8903, CVE-2020-8907, CVE-2020-8933. 

###  cos-81-12871-117-0

_Date: May 27, 2020_

  * Upgraded sys-libs/libseccomp to version 2.4.2-r1 to fix CVE-2019-9893. 

###  cos-81-12871-103-0

_Date: May 07, 2020_

  * Added package sys-apps/acl. 

###  cos-81-12871-96-0

_Date: Apr 29, 2020_

  * Fixed a kernel bug where eBPF programs can cause softlockups. 

###  cos-81-12871-76-0

_Date: Apr 29, 2020_

  * Disabled `accept_ra` on all interfaces by default. 

###  cos-81-12871-69-0

_Date: Apr 05, 2020_

  * Upgraded the Linux kernel to v4.19.112. 
  * Backported systemd patch ba0d56f55 to address an issue that resulted in leaked mount units. 
  * Upgraded dev-db/sqlite to 3.31.1. 
  * Moved kernel repository to cos.googlesource.com/third_party/kernel. 
  * Backported necessary ext4 patches and made dioread_nolock default. 

###  cos-81-12871-59-0 (vs Milestone 77)

_Date: Mar 27, 2020_

####  New features

  * Added support for new Google Compute Engine virtual network interface (GVNIC). 
  * Added support for AMD's Secure Encrypted Virtualization. 
  * Added support to implement SCSI devices in user space. 
  * Added support for snapshotting any block device without massive copying. 
  * Enhanced security by reducing the predictability of the kernel slab allocator against heap overflows and providing a lightweight support for detecting buffer overflow. 
  * Added chrony package for time synchronization. 
  * Disabled multicast protocol LLMNR and MDNS by default. 

####  Package updates

  * Upgraded docker to v19.03.6. 
  * Upgraded containerd to v1.3.2. 
  * Upgraded runc to v1.0.0. 
  * Upgraded docker-credential-gcr to v2.0.0. 
  * Upgraded the built-in kubectl/kubelet to v1.17.3. 
  * Upgraded node-problem-detector to v0.8.0. 
  * Upgraded cos-toolbox to 20191218-00. 
  * Upgraded openssl to 1.0.2u. 
  * Upgraded oslogin to v20190315. 
  * Upgraded compute-image-packages to v20190801. 

####  Bug fixes

  * Changed the MTU of the default docker network to 1460 to make it consistent with Google Compute Engine's default MTU value. 
  * Fixed a regression that blocks user-level statically defined tracking probes (requires a semaphore) to work. 
  * Fixed vulnerability in glibc (CVE-2019-19126). 

