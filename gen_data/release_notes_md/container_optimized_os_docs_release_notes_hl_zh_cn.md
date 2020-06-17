#  Container-Optimized OS - 版本说明

##  当前活跃版本

目前， ` cos-cloud ` 映像项目中提供了以下映像：  稳定版  |  测试版  |  开发版  
---|---|---  
      
    
    
    **cos-stable-81-12871-119-0**
    Kernel:         [COS-4.19.112](https://cos.googlesource.com/third_party/kernel/+/fa84f12c6d738af9486e69a006a57df923f9476a%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    

|

    
    
    
    **cos-beta-81-12871-117-0**
    Kernel:         [COS-4.19.112](https://cos.googlesource.com/third_party/kernel/+/fa84f12c6d738af9486e69a006a57df923f9476a%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    

|

    
    
    
    **cos-dev-84-13078-0-0**
    Kernel:         [COS-4.19.119](https://cos.googlesource.com/third_party/kernel/+/cf82bb6a0699ca4452067a6c88483909d1dbc90e%0A)
    Kubernetes:     v1.18.2
    Docker:         v19.03.8
      
  
###  LTS 映像系列

  * [ cos-69-lts ](https://cloud.google.com/container-optimized-os/docs/release-notes/m69?hl=zh-cn)
  * [ cos-73-lts ](https://cloud.google.com/container-optimized-os/docs/release-notes/m73?hl=zh-cn)
  * [ cos-77-lts ](https://cloud.google.com/container-optimized-os/docs/release-notes/m77?hl=zh-cn)

##  发布时间表

实际日期可能会略有不同。

里程碑版  |  下列日期后转为稳定版  
---|---  
82  |  2020 年 5 月 5 日  
81 [LTS]  |  2020 年 3 月 24 日  
80  |  2020 年 2 月 11 日  
77 [LTS]  |  2019 年 9 月 17 日  
73 [LTS]  |  2019 年 3 月 19 日  
69 [LTS]  |  2018 年 9 月 11 日  
  
####  旧版本

里程碑版  |  下列日期后转为稳定版  |  下列日期后弃用  
---|---|---  
79  |  2019 年 12 月 17 日  |  2019 年 2 月 12 日  
78  |  2019 年 10 月 29 日  |  2019 年 12 月 17 日  
76  |  2019 年 8 月 06 日  |  2019 年 9 月 27 日  
75  |  2019 年 6 月 11 日  |  2019 年 8 月 06 日  
74  |  2019 年 4 月 30 日  |  2019 年 6 月 11 日  
72  |  2019 年 2 月 5 日  |  2019 年 5 月 25 日  
71  |  2018 年 12 月 4 日  |  2019 年 2 月 14 日  
70  |  2018 年 10 月 23 日  |  Dec 14, 2018  
68  |  2018 年 7 月 31 日  |  2018 年 10 月 23 日  
67  |  2018 年 6 月 5 日  |  2018 年 9 月 11 日  
66  |  2018 年 4 月 24 日  |  2018 年 7 月 31 日  
65  |  2018 年 3 月 13 日  |  2018 年 6 月 5 日  
64  |  2018 年 1 月 30 日  |  2018 年 4 月 24 日  
63  |  2017 年 12 月 12 日  |  2018 年 3 月 13 日  
62  |  2017 年 10 月 24 日  |  2018 年 1 月 30 日  
61  |  2017 年 9 月 12 日  |  2017 年 11 月 30 日  
60  |  2017 年 8 月 1 日  |  2017 年 10 月 12 日  
59  |  2017 年 6 月 6 日  |  2017 年 8 月 31 日  
58  |  2017 年 4 月 25 日  |  2017 年 7 月 20 日  
57  |  2017 年 3 月 14 日  |  2017 年 5 月 25 日  
56  |  2017 年 1 月 31 日  |  2017 年 4 月 13 日  
  
##  更新日志

###  cos-stable-81-12871-119-0

    
    
    Date:           May 28, 2020
    Kernel:         [COS-4.19.112](https://cos.googlesource.com/third_party/kernel/+/fa84f12c6d738af9486e69a006a57df923f9476a%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    Changelog (vs 81-12871-117-0):
        * Fixed a few OS Login CVEs: CVE-2020-8903, CVE-2020-8907, CVE-2020-8933.
    

###  cos-stable-81-12871-117-0

    
    
    Date:           May 27, 2020
    Kernel:         [COS-4.19.112](https://cos.googlesource.com/third_party/kernel/+/fa84f12c6d738af9486e69a006a57df923f9476a%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    Changelog (vs 81-12871-103-0):
        * Upgraded sys-libs/libseccomp to version 2.4.2-r1 to fix CVE-2019-9893.
    

###  cos-77-12371-274-0

    
    
    Date:           May 26, 2020
    Kernel:         [ChromiumOS-4.19.112](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/5d4ffd91281840f7a118143d77fbefb02e87943c%0A)
    Kubernetes:     v1.15.3
    Docker:         v19.03.1
    Changelog (vs 77-12371-273-0):
        * Fixed a few OS Login CVEs: CVE-2020-8903, CVE-2020-8907, CVE-2020-8933.
    

###  cos-beta-81-12871-117-0

    
    
    Date:           May 26, 2020
    Kernel:         [COS-4.19.112](https://cos.googlesource.com/third_party/kernel/+/fa84f12c6d738af9486e69a006a57df923f9476a%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    Changelog (vs 81-12871-44-0):
        * Added package sys-apps/acl.
        * Backported systemd patch ba0d56f55 to address an issue that resulted in
          leaked mount units.
        * Disabled `accept_ra` on all interfaces by default.
        * Moved kernel repository to https://cos.googlesource.com/third_party/kernel.
        * Removed gve package.
        * Upgraded dev-db/sqlite to version 3.31.1.
        * Upgraded sys-libs/libseccomp to version 2.4.2-r1 to fix CVE-2019-9893.
    

###  cos-77-12371-273-0

    
    
    Date:           May 21, 2020
    Kernel:         [ChromiumOS-4.19.112](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/5d4ffd91281840f7a118143d77fbefb02e87943c%0A)
    Kubernetes:     v1.15.3
    Docker:         v19.03.1
    Changelog (vs 77-12371-251-0):
        * Fixed a Stackdriver Monitoring agent bug where not all mounted disk partitions has their usage reported.
    

###  cos-dev-84-13078-0-0

    
    
    Date:           May 07, 2020
    Kernel:         [COS-4.19.119](https://cos.googlesource.com/third_party/kernel/+/cf82bb6a0699ca4452067a6c88483909d1dbc90e%0A)
    Kubernetes:     v1.18.2
    Docker:         v19.03.8
    Changelog (vs 83-13020-12-0):
        * Updated makedumpfile to 1.6.7.
        * Added package sys-apps/acl.
        * Updated docker to 19.03.8.
        * Upgraded to latest google sdk(287) in cos-toolbox.
        * Disabled `accept_ra` on all interfaces by default.
        * Updated containerd to v1.3.4.
        * Upgraded the Linux kernel to v4.19.119.
        * Updated the built-in kubectl/kubelet to 1.18.2.
        * Updated the Python requests package to v2.22.0 to address CVE-2018-18074.
        * Updated libseccomp to v2.4.2 to address CVE-2019-9893.
    

###  cos-81-12871-103-0

    
    
    Date:           May 07, 2020
    Kernel:         [COS-4.19.112](https://cos.googlesource.com/third_party/kernel/+/fa84f12c6d738af9486e69a006a57df923f9476a%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    Changelog (vs 81-12871-96-0):
        * Added package sys-apps/acl.
    

###  cos-73-11647-534-0

    
    
    Date:           May 07, 2020
    Kernel:         [ChromiumOS-4.14.174](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/657018fc00e3c2be2a7abb3ec149f9bca42b9ab0%0A)
    Kubernetes:     v1.13.3
    Docker:         v18.09.7
    Changelog (vs 73-11647-510-0):
        * Image rebuild to address an infrastructure issue. No image changes.
    

###  cos-81-12871-96-0

    
    
    Date:           Apr 29, 2020
    Kernel:         [COS-4.19.112](https://cos.googlesource.com/third_party/kernel/+/fa84f12c6d738af9486e69a006a57df923f9476a%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    Changelog (vs 81-12871-76-0):
        * Fixed a kernel bug where eBPF programs can cause softlockups.
    

###  cos-77-12371-251-0

    
    
    Date:           Apr 29, 2020
    Kernel:         [ChromiumOS-4.19.112](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/5d4ffd91281840f7a118143d77fbefb02e87943c%0A)
    Kubernetes:     v1.15.3
    Docker:         v19.03.1
    Changelog (vs 77-12371-233-0):
        * Fixed a kernel bug where eBPF programs can cause softlockups.
    lockups
    

###  cos-81-12871-76-0

    
    
    Date:           Apr 29, 2020
    Kernel:         [COS-4.19.112](https://cos.googlesource.com/third_party/kernel/+/7e8a5293f4a62df1dc717093ce6c22cc97b7f1ae%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    Changelog (vs 81-12871-69-0):
        * Disabled `accept_ra` on all interfaces by default.
    

###  cos-77-12371-233-0

    
    
    Date:           Apr 29, 2020
    Kernel:         [ChromiumOS-4.19.112](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/44db6154b00a43d87634fd0d35292aec1d0c14c7%0A)
    Kubernetes:     v1.15.3
    Docker:         v19.03.1
    Changelog (vs 77-12371-227-0):
        * Disabled `accept_ra` on all interfaces by default.
    

###  cos-dev-83-13020-12-0

    
    
    Date:           Apr 13, 2020
    Kernel:         [COS-4.19.114](https://cos.googlesource.com/third_party/kernel/+/a8c47ac5afe9c1a9f569b2caaa93b803a6c4d94b%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    Changelog (vs 83-12998-0-0):
        * Backported systemd patch ba0d56f55 to address an issue that resulted in
          leaked mount units.
        * Moved kernel repository to https://cos.googlesource.com/third_party/kernel.
        * Upgraded the Linux kernel to v4.19.112.
        * Backported necessary ext4 patches and made dioread_nolock default.
    

###  cos-stable-73-11647-510-0

    
    
    Date:           Apr 13, 2020
    Kernel:         [ChromiumOS-4.14.174](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/657018fc00e3c2be2a7abb3ec149f9bca42b9ab0%0A)
    Kubernetes:     v1.13.3
    Docker:         v18.09.7
    Changelog (vs 73-11647-501-0):
        * Disabled `accept_ra` on all interfaces by default.
        * Upgraded OpenSSH to 7.9_p1 to fix CVE-2018-15473.
        

###  cos-stable-81-12871-69-0

    
    
    Date:           Apr 05, 2020
    Kernel:         [COS-4.19.112](https://cos.googlesource.com/third_party/kernel/+/7e8a5293f4a62df1dc717093ce6c22cc97b7f1ae%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    Changelog (vs 81-12871-44-0):
        * Upgraded the Linux kernel to v4.19.112.
        * Backported systemd patch ba0d56f55 to address an issue that resulted in
          leaked mount units.
        * Upgraded dev-db/sqlite to 3.31.1.
        * Moved kernel repository to cos.googlesource.com/third_party/kernel.
        * Backported necessary ext4 patches and made dioread_nolock default.
    

###  cos-stable-77-12371-227-0

    
    
    Date:           Apr 05, 2020
    Kernel:         [ChromiumOS-4.19.112](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/44db6154b00a43d87634fd0d35292aec1d0c14c7%0A)
    Kubernetes:     v1.15.3
    Docker:         v19.03.1
    Changelog (vs 77-12371-208-0):
        * Upgraded the Linux kernel to v4.19.112.
        * Backported systemd patch ba0d56f55 to address an issue that resulted in
          leaked mount units.
    

###  cos-stable-73-11647-501-0

    
    
    Date:           Apr 05, 2020
    Kernel:         [ChromiumOS-4.14.174](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/657018fc00e3c2be2a7abb3ec149f9bca42b9ab0%0A)
    Kubernetes:     v1.13.3
    Docker:         v18.09.7
    Changelog (vs 73-11647-459-0):
        * Upgraded the Linux kernel to v4.14.174.
        * Backported systemd patch ba0d56f55 to address an issue that resulted in
          leaked mount units.
    

###  cos-dev-83-12998-0-0

    
    
    Date:           Mar 27, 2020
    Kernel:         [ChromiumOS-4.19.108](https://chromium.googlesource.com/chromiumos/third_party/lakitu-kernel/+/8bd983177d60daba1e1df7e90bf02cfd0294e9b9%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    Changelog (vs 82-12962-0-0):
        * Upgraded cloud-init to v19.4.
        * Upgraded the Linux kernel to v4.19.108.
        * Removed size limit on /etc/ to fix cluster creation failure because of large number of addons.
        * Upgraded node problem detector to v0.8.1.
    

###  cos-stable-81-12871-59-0

    
    
    Date:           Mar 27, 2020
    Kernel:         [ChromiumOS-4.19.112](https://chromium.googlesource.com/chromiumos/third_party/lakitu-kernel/+/7e8a5293f4a62df1dc717093ce6c22cc97b7f1ae%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    Changelog (vs 81-12871-44-0):
        * Upgraded the Linux kernel to v4.19.112.
    

###  cos-beta-81-12871-44-0

    
    
    Date:           Mar 17, 2020
    Kernel:         [ChromiumOS-4.19.108](https://chromium.googlesource.com/chromiumos/third_party/lakitu-kernel/+/4d594cea40affe77720d76a1f70b5039aa488e52%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    Changelog (vs 81-12871-38-0):
        * Upgraded the Linux kernel to v4.19.108.
        * Removed size limit on /etc/ to fix cluster creation failure because of large number of addons.
    

###  cos-stable-80-12739-104-0

    
    
    Date:           Mar 17, 2020
    Kernel:         [ChromiumOS-4.19.87](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/709837de20828e09bbb42e2f6f2839efedded5a0%0A)
    Kubernetes:     v1.16.6
    Docker:         v19.03.5
    Changelog (vs 80-12739-91-0):
        * Removed size limit on /etc/ to fix cluster creation failure because of large number of addons.
    

###  cos-stable-77-12371-208-0

    
    
    Date:           Mar 17, 2020
    Kernel:         [ChromiumOS-4.19.109](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/9e1168898f7dfad439286058801d5e6135b89ae3%0A)
    Kubernetes:     v1.15.3
    Docker:         v19.03.1
    Changelog (vs 77-12371-183-0):
        * Enabled NETFILTER_XT_MATCH_SOCKET.
        * Fixed a bug where DHCP is not started after link flaps.
        * Removed size limit on /etc/ to fix cluster creation failure because of large number of addons.
        * Upgraded the Linux kernel to v4.19.109
    

###  cos-dev-82-12962-0-0

    
    
    Date:           Mar 09, 2020
    Kernel:         [ChromiumOS-4.19.107](https://chromium.googlesource.com/chromiumos/third_party/lakitu-kernel/+/d778e15bed1da70ccbcafe8c4a76d32139c291ce%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    Changelog (vs 82-12941-0-0):
        * Enabled kernel config NETFILTER_XT_MATCH_SOCKET.
        * Upgraded the Linux kernel to v4.19.107.
        * Fixed ssh hostkey verification error.
        * Backported two trace_uprobe patches from upstream to make USDT work.
    

###  cos-beta-81-12871-38-0

    
    
    Date:           Mar 09, 2020
    Kernel:         [ChromiumOS-4.19.107](https://chromium.googlesource.com/chromiumos/third_party/lakitu-kernel/+/966e554f2db06013e1e4a556255e8d1c8c1de0a7%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    Changelog (vs 81-12871-31-0):
        * Enabled kernel config NETFILTER_XT_MATCH_SOCKET.
        * Upgraded the Linux kernel to v4.19.107.
        * Fixed ssh hostkey verification error.
        * Backported two trace_uprobe patches from upstream to make USDT work.
    

###  cos-dev-82-12941-0-0

    
    
    Date:           Mar 03, 2020
    Kernel:         [ChromiumOS-4.19.105](https://chromium.googlesource.com/chromiumos/third_party/lakitu-kernel/+/cea96c38af5017f6b13bfdc13c50bdde55d7c380%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    Changelog (vs 82-12919-0-0):
        * Upgraded the Linux kernel to v4.19.105.
    

###  cos-beta-81-12871-31-0

    
    
    Date:           Mar 03, 2020
    Kernel:         [ChromiumOS-4.19.105](https://chromium.googlesource.com/chromiumos/third_party/lakitu-kernel/+/37dc923bdc535ccd64fa3d0ad45f64b7763ff8f3%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    Changelog (vs 81-12871-17-0):
        * Upgraded the Linux kernel to v4.19.105.
        * Fixed a bug where DHCP is not started after link flaps.
    

###  cos-stable-80-12739-91-0

    
    
    Date:           Mar 03, 2020
    Kernel:         [ChromiumOS-4.19.87](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/709837de20828e09bbb42e2f6f2839efedded5a0%0A)
    Kubernetes:     v1.16.6
    Docker:         v19.03.5
    Changelog (vs 80-12739-78-0):
        * Minor changes.
    

###  cos-dev-82-12919-0-0

    
    
    Date:           Feb 21, 2020
    Kernel:         [ChromiumOS-4.19.104](https://chromium.googlesource.com/chromiumos/third_party/lakitu-kernel/+/230a8e9a1c1e9acf75f6783b047711b357f746cd%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    Changelog (vs 82-12894-0-0):
        * Fixed a bug where DHCP is not started after link flaps.
        * Upgraded the Linux kernel to v4.19.104.
        * Updated the built-in kubectl/kubelet to 1.17.3.
        * Made Python3 the default Python interpreter.
        * Updated Docker to release v19.03.6.
        * Bring back 99-virtio.network to fix DHCPv6 issue.
        * Fixed TCP empty skb at the tail of the write queue bug in kernel.
    

###  cos-beta-81-12871-17-0

    
    
    Date:           Feb 21, 2020
    Kernel:         [ChromiumOS-4.19.104](https://chromium.googlesource.com/chromiumos/third_party/lakitu-kernel/+/810a37b78aab7edf1898a0f10b6d33f12999dd10%0A)
    Kubernetes:     v1.17.3
    Docker:         v19.03.6
    Changelog (vs 81-12871-7-0):
        * Upgraded the Linux kernel to v4.19.104.
        * Updated the built-in kubectl/kubelet to 1.17.3.
        * Upgraded runc to 1.0.0-rc10. This resolves CVE-2019-19921.
        * Updated Docker to release v19.03.6.
        * Bring back 99-virtio.network to fix DHCPv6 issue.
        * Fixed TCP empty skb at the tail of the write queue bug in kernel.
    

###  cos-stable-80-12739-78-0

    
    
    Date:           Feb 21, 2020
    Kernel:         [ChromiumOS-4.19.87](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/709837de20828e09bbb42e2f6f2839efedded5a0%0A)
    Kubernetes:     v1.16.6
    Docker:         v19.03.5
    Changelog (vs 80-12739-68-0):
        * Bring back 99-virtio.network to fix DHCPv6 issue.
        * Fixed TCP empty skb at the tail of the write queue bug in kernel.
    

###  cos-77-12371-183-0

    
    
    Date:           Feb 21, 2020
    Kernel:         [ChromiumOS-4.19.104](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/0c94af8a1221168be9c750ad378d494e969fa425%0A)
    Kubernetes:     v1.15.3
    Docker:         v19.03.1
    Changelog (vs 77-12371-175-0):
        * Upgraded the Linux kernel to v4.19.104
        * Fixed TCP empty skb at the tail of the write queue bug in kernel.
    

###  cos-73-11647-459-0

    
    
    Date:           Feb 21, 2020
    Kernel:         [ChromiumOS-4.14.171](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/c88d15e74e7bedba260a8ef7ee6920e02182477a%0A)
    Kubernetes:     v1.13.3
    Docker:         v18.09.7
    Changelog (vs 73-11647-449-0):
        * Upgraded the Linux kernel to v4.14.171.
        * Fixed TCP empty skb at the tail of the write queue bug in kernel.
    

###  cos-dev-82-12894-0-0

    
    
    Date:           Feb 12, 2020
    Kernel:         [ChromiumOS-4.19.102](https://chromium.googlesource.com/chromiumos/third_party/lakitu-kernel/+/dc18f11110004b0f87b205188af793af02f434e0%0A)
    Kubernetes:     v1.17.2
    Docker:         v19.03.5
    Changelog (vs 82-12892-0-0):
        * Upgraded the Linux kernel to v4.19.102.
    

###  cos-beta-81-12871-7-0

    
    
    Date:           Feb 12, 2020
    Kernel:         [ChromiumOS-4.19.102](https://chromium.googlesource.com/chromiumos/third_party/lakitu-kernel/+/12060777ae0d5294a935e285df3e4a043915c371%0A)
    Kubernetes:     v1.17.2
    Docker:         v19.03.5
    Changelog (vs 81-12871-6-0):
        * Upgraded the Linux kernel to v4.19.102.
    

###  cos-stable-80-12739-68-0

    
    
    Date:           Feb 12, 2020
    Kernel:         [ChromiumOS-4.19.87](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2cfbd87eae7ca138d457c2085de8621b43ddf08e%0A)
    Kubernetes:     v1.16.6
    Docker:         v19.03.5
    Changelog (vs 80-12739-66-0):
        * Upgraded runc to 1.0.0-rc10. This resolves CVE-2019-19921.
    

###  cos-77-12371-175-0

    
    
    Date:           Feb 12, 2020
    Kernel:         [ChromiumOS-4.19.102](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/1be45a63ab45e4483c7f5aa32a0d0390e8b5a9b9%0A)
    Kubernetes:     v1.15.3
    Docker:         v19.03.1
    Changelog (vs 77-12371-141-0):
        * Enabled some QoS and Fair Queuing options in the Linux kernel.
        * Upgraded the Linux kernel to v4.19.102.
        * Upgraded runc to 1.0.0-rc10. This resolves CVE-2019-19921.
    

###  cos-73-11647-449-0

    
    
    Date:           Feb 12, 2020
    Kernel:         [ChromiumOS-4.14.170](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2df639a0b50d8dbe6419a383afd3994810cd3760%0A)
    Kubernetes:     v1.13.3
    Docker:         v18.09.7
    Changelog (vs 73-11647-415-0):
        * Upgraded runc to 1.0.0-rc10. This resolves CVE-2019-19921.
        * Upgraded the Linux kernel to v4.14.170.
    

###  cos-dev-82-12892-0-0

    
    
    Date:           Feb 10, 2020
    Kernel:         [ChromiumOS-4.19.101](https://chromium.googlesource.com/chromiumos/third_party/lakitu-kernel/+/e97023266391178de3ef1b067f7019d1f959f57a%0A)
    Kubernetes:     v1.17.2
    Docker:         v19.03.5
    Changelog (vs 81-12854-0-0):
        * Upgraded runc to 1.0.0-rc10. This resolves CVE-2019-19921.
        * Upgraded cloud-init to v18.5.
        * Upgraded the built-in kubelet to 1.17.2.
        * Upgraded the Linux kernel to v4.19.101.
        * Upgraded iptables to 1.6.2.
        * Enabled some QoS and Fair Queuing options.
    
    

###  cos-beta-81-12871-6-0

    
    
    Date:           Feb 10, 2020
    Kernel:         [ChromiumOS-4.19.101](https://chromium.googlesource.com/chromiumos/third_party/lakitu-kernel/+/0351c63f06a9e79d3111e82dfc15bb315f7aa13b%0A)
    Kubernetes:     v1.17.2
    Docker:         v19.03.5
    Changelog (vs 81-12854-0-0):
        * Promoted to beta channel.
        * Upgraded the built-in kubelet to 1.17.2.
        * Upgraded the Linux kernel to v4.19.101.
        * Enabled some QoS and Fair Queuing options.
    

###  cos-stable-80-12739-66-0

    
    
    Date:           Feb 10, 2020
    Kernel:         [ChromiumOS-4.19.87](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2cfbd87eae7ca138d457c2085de8621b43ddf08e%0A)
    Kubernetes:     v1.16.6
    Docker:         v19.03.5
    Changelog (vs 80-12739-48-0):
        * Promoted to stable channel.
        * Updated the built-in kubelet to 1.16.6.
    

###  cos-dev-81-12854-0-0

    
    
    Date:           Jan 27, 2020
    Kernel:         [ChromiumOS-4.19.97](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/10ff2a7f44835c3e68ff7de148d91ccc744c102e)
    Kubernetes:     v1.17.1
    Docker:         v19.03.5
    Changelog (vs 81-12834-0-0):
        * Upgraded the Linux kernel to v4.19.97.
        * Updated the built-in kubelet to 1.17.1.
        * Upgraded iptables to v1.6.2.
        * Upgraded openssl to 1.0.2u.
    

###  cos-beta-80-12739-48-0

    
    
    Date:           Jan 27, 2020
    Kernel:         [ChromiumOS-4.19.87](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2cfbd87eae7ca138d457c2085de8621b43ddf08e)
    Kubernetes:     v1.16.5
    Docker:         v19.03.5
    Changelog (vs 80-12739-37-0):
        * Updated the built-in kubelet to 1.16.5.
    

###  cos-dev-81-12834-0-0

    
    
    Date:           Jan 16, 2020
    Kernel:         [ChromiumOS-4.19.94](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/c7ad6ff415b5a1e87f8333e2a63c7209e6efc1b2)
    Kubernetes:     v1.17.0
    Docker:         v19.03.5
    Changelog (vs 81-12813-0-0):
        * Updated the Linux kernel to v4.19.94.
        * Updated gve driver to v1.0.1.
        * Updated docker-credential-gcr to 2.0.0.
        * Updated docker-credential-helpers to 0.6.3.
        * Updated the built-in kubelet to 1.17.0.
    

###  cos-beta-80-12739-37-0

    
    
    Date:           Jan 16, 2020
    Kernel:         [ChromiumOS-4.19.87](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2cfbd87eae7ca138d457c2085de8621b43ddf08e)
    Kubernetes:     v1.16.4
    Docker:         v19.03.5
    Changelog (vs 80-12739-29-0):
        * Minor changes.
    

###  cos-dev-81-12813-0-0

    
    
    Date:           Jan 07, 2020
    Kernel:         [ChromiumOS-4.19.91](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2bbed2a31d4b7517fc6e78d3e2f2c1208bf7d6fc)
    Kubernetes:     v1.16.4
    Docker:         v19.03.5
    Changelog (vs 80-12688-0-0):
        * Fixed vulnerability in glibc (CVE-2019-19126).
        * Upgraded sqlite to 3.30.1 to fix CVE-2019-16168.
        * Upgraded sudo to 1.8.28_p1 to fix CVE-2019-14287.
        * Fixed CFS quota throttling issue.
        * Updated the built-in kubelet to 1.16.4.
        * Upgraded oslogin package to v20190315.
        * Upgraded the Linux kernel to v4.19.91.
        * Upgraded cos-toolbox to 20191218-00.
        * Upgrade containerd to v1.3.2.
        * Added chrony as an alternative NTP client.
        * Added GVNIC driver kernel module.
        * Added tcm_loop kernel module.
        * Disable multicast protocol LLMNR and MDNS by default.
    

###  cos-beta-80-12739-29-0

    
    
    Date:           Jan 07, 2020
    Kernel:         [ChromiumOS-4.19.87](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2cfbd87eae7ca138d457c2085de8621b43ddf08e)
    Kubernetes:     v1.16.4
    Docker:         v19.03.5
    Changelog (vs 80-12688-0-0):
        * Upgraded sudo to 1.8.28_p1 to fix CVE-2019-14287.
        * Backported fix for Linux kernel CVE-2019-19072.
        * Upgraded the Linux kernel to v4.19.87.
        * Updated the built-in kubelet to 1.16.4.
        * Upgraded oslogin package to v20190315.
        * Added GVNIC driver kernel module.
        * Removed alsa/midi/audio kernel features.
    

###  cos-stable-79-12607-80-0

    
    
    Date:           Jan 07, 2020
    Kernel:         [ChromiumOS-4.19.79](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ec6ae0f965353eec4d901d8ed96da0a6608c46a6)
    Kubernetes:     v1.16.3
    Docker:         v19.03.5
    Changelog (vs 79-12607-60-0):
        * Backported fix for Linux kernel CVE-2019-19072.
    

###  cos-stable-77-12371-141-0

    
    
    Date:           Jan 07, 2020
    Kernel:         [ChromiumOS-4.19.91](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2babf80b7a108e07d90f2a29153fed03f10e20ac)
    Kubernetes:     v1.15.3
    Docker:         v19.03.1
    Changelog (vs 77-12371-114-0):
        * Backported fix for Linux kernel CVE-2019-19072.
        * Fixed CFS quota throttling issue.
        * Upgraded the Linux kernel to v4.19.91.
    

###  cos-stable-73-11647-415-0

    
    
    Date:           Jan 07, 2020
    Kernel:         [ChromiumOS-4.14.160](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/71925fffd6c2e882d804e50e30d60ae29a42b756)
    Kubernetes:     v1.13.3
    Docker:         v18.09.7
    Changelog (vs 73-11647-348-0):
        * Fixed CFS quota throttling issue.
        * Increase sysctl net.ipv4.tcp_limit_output_bytes to 1048576.
        * Upgraded the Linux kernel to v4.14.160.
    

###  cos-beta-79-12607-60-0

    
    
    Date:           Dec 16, 2019
    Kernel:         [ChromiumOS-4.19.79](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/9d829ec3dd30b690d894a90de6d44b823fd28083)
    Kubernetes:     v1.16.3
    Docker:         v19.03.5
    Changelog (vs 79-12607-46-0):
        * Fixed CFS quota throttling issue.
    

###  cos-stable-78-12499-89-0

    
    
    Date:           Dec 16, 2019
    Kernel:         [ChromiumOS-4.19.72](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ea60a56f3289516c66deae2fd37cd1a690bdadf4)
    Kubernetes:     v1.15.4
    Docker:         v19.03.3
    Changelog (vs 78-12499-59-0):
        * Fixed CFS quota throttling issue.
    

###  cos-beta-79-12607-46-0

    
    
    Date:           Dec 04, 2019
    Kernel:         [ChromiumOS-4.19.79](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/710aef41c4a1d16c649e4c0d5801c8d803b37f42)
    Kubernetes:     v1.16.3
    Docker:         v19.03.5
    Changelog (vs 79-12607-32-0):
        * Updated Docker to v19.03.5.
        * Updated the built-in kubelet to 1.16.3.
    

###  cos-dev-80-12688-0-0

    
    
    Date:           Nov 18, 2019
    Kernel:         [ChromiumOS-4.19.83](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/5d8615d1e135275cbfdf9522517a3b198e7199ee)
    Kubernetes:     v1.16.3
    Docker:         v19.03.5
    Changelog (vs 80-12657-0-0):
        * Fixed the problem of spawning 8 runc state process for every exec
          on containerd. This was leading to high cpu utilization.
        * Upgraded to docker v19.03.5.
        * Changed the MTU of the default docker network to 1460.
        * Updated the built-in kubelet to 1.16.3.
        * Upgraded the Linux kernel to v4.19.83.
        * Upgraded sys-libs/libapparmor to version 2.13.3.
    

###  cos-beta-79-12607-32-0

    
    
    Date:           Nov 18, 2019
    Kernel:         [ChromiumOS-4.19.79](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/710aef41c4a1d16c649e4c0d5801c8d803b37f42)
    Kubernetes:     v1.16.0
    Docker:         v19.03.3
    Changelog (vs 79-12607-22-0):
        * Minor changes.
    

###  cos-dev-80-12657-0-0

    
    
    Date:           Nov 11, 2019
    Kernel:         [ChromiumOS-4.19.81](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f9b86b7ceb22ed6ea3afb792a083176b1fd4a6f8)
    Kubernetes:     v1.15.3
    Docker:         v19.03.4
    Changelog (vs 79-12607-7-0):
        * Increase sysctl net.ipv4.tcp_limit_output_bytes to 1048576.
        * Fixed the unnecessary creation of two separate test slices
          (resulting in 4 systemd log messages total + runtime overhead) for every
          runc execution.
        * Enabled AMD_MEM_ENCRYPT in COS kernel config.
        * Fixed a Stackdriver Monitoring agent bug where not all mounted disk
          partitions has their usage reported.
        * Upgraded node problem detector to v0.8.0.
        * Upgraded Docker to v19.03.4.
        * Fixed the problem of spawning 8 runc state process for every exec on
          containerd. This was leading to high cpu utilization.
        * Revert kubernetes to v1.15.3.
        * Revert containerd to v1.2.9.
        * Upgraded jsonpatch to v1.23.
        * Upgraded jsonpointer to v2.0.
        * Upgraded configobj to v5.0.6.
        * Fixed a performance regression in completely fair scheduler (CFS).
    

###  cos-beta-79-12607-22-0

    
    
    Date:           Nov 11, 2019
    Kernel:         [ChromiumOS-4.19.79](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/710aef41c4a1d16c649e4c0d5801c8d803b37f42)
    Kubernetes:     v1.16.0
    Docker:         v19.03.3
    Changelog (vs 79-12607-7-0):
        * Increase sysctl net.ipv4.tcp_limit_output_bytes to 1048576.
        * Fixed the unnecessary creation of two separate test slices
          (resulting in 4 systemd log messages total + runtime overhead) for every
          runc execution.
        * Fixed a Stackdriver Monitoring agent bug where not all mounted disk
          partitions has their usage reported.
        * Fixed the problem of spawning 8 runc state process for every exec on
          containerd. This was leading to high cpu utilization.
        * Revert containerd to v1.2.9.
    

###  cos-stable-78-12499-59-0

    
    
    Date:           Nov 08, 2019
    Kernel:         [ChromiumOS-4.19.72](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/344151c2af0e8adc051d3ff8b6cef22126af60f7)
    Kubernetes:     v1.15.4
    Docker:         v19.03.3
    Changelog (vs 78-12499-46-0):
        * Increase sysctl net.ipv4.tcp_limit_output_bytes to 1048576.
        * Fixed the unnecessary creation of two separate test slices
          (resulting in 4 systemd log messages total + runtime overhead) for every
          runc execution.
        * Fixed the problem of spawning 8 runc state process for every exec on
          containerd. This was leading to high cpu utilization.
    

###  cos-stable-77-12371-114-0

    
    
    Date:           Oct 31, 2019
    Kernel:         [ChromiumOS-4.19.80](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f919efb6be4c75660b1215fa0a68fb09bb80cc2b)
    Kubernetes:     v1.15.3
    Docker:         v19.03.1
    Changelog (vs 77-12371-89-0):
        * Increased sysctl net.ipv4.tcp_limit_output_bytes to 1048576.
        * Fixed the problem of spawning 8 runc state process for every exec on
          containerd. This was leading to high cpu utilization.
        * Fixed the unnecessary creation of two separate test slices (resulting
          in 4 systemd log messages total + runtime overhead) for every runc
          execution.
        * Fixed an issue in runc that resulted in unnecessary CPU consumption.
        * Upgraded the Linux kernel to v4.19.80.
        * Fixed a performance regression in completely fair scheduler (CFS).
    
    

###  cos-dev-79-12607-7-0

    
    
    Date:           Oct 28, 2019
    Kernel:         [ChromiumOS-4.19.79](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/710aef41c4a1d16c649e4c0d5801c8d803b37f42)
    Kubernetes:     v1.16.0
    Docker:         v19.03.3
    Changelog (vs 79-12605-0-0):
        * Upgraded Docker to v19.03.3.
        * Fixed a performance regression in completely fair scheduler (CFS).
    

###  cos-beta-78-12499-46-0

    
    
    Date:           Oct 28, 2019
    Kernel:         [ChromiumOS-4.19.72](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/344151c2af0e8adc051d3ff8b6cef22126af60f7)
    Kubernetes:     v1.15.4
    Docker:         v19.03.3
    Changelog (vs 78-12499-38-0):
        * Fixed an issue in runc that resulted in unnecessary CPU consumption.
        * Fixed a performance regression in completely fair scheduler (CFS).
    

###  cos-73-11647-348-0

    
    
    Date:           Oct 28, 2019
    Kernel:         [ChromiumOS-4.14.150](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/41e9e2e85e50dadce3887070595b89c017e37a2c)
    Kubernetes:     v1.13.3
    Docker:         v18.09.7
    Changelog (vs 73-11647-338-0):
        * Fixed the unnecessary creation of two separate test slices (resulting in 4
          systemd log messages total + runtime overhead) for every runc execution.
        * Fixed a performance regression in completely fair scheduler (CFS).
        * Upgraded the Linux kernel to v4.14.150.
    
    

###  cos-dev-79-12605-0-0

    
    
    Date:           Oct 21, 2019
    Kernel:         [ChromiumOS-4.19.79](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/96bfeffb29ca01693d3b444c4e01eefaf5514055)
    Kubernetes:     v1.16.0
    Docker:         v19.03.2
    Changelog (vs 79-12577-0-0):
        * Upgraded containerd to v1.3.0.
        * Upgraded the built-in kubelet to 1.16.0.
        * Upgraded openssl to version 1.0.2t.
    

###  cos-beta-78-12499-38-0

    
    
    Date:           Oct 21, 2019
    Kernel:         [ChromiumOS-4.19.72](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/1e4d47c802bf1644c426bd9a0c4cb3a3f0baa616)
    Kubernetes:     v1.15.4
    Docker:         v19.03.3
    Changelog (vs 78-12499-32-0):
        * Upgraded the built-in kubelet to 1.15.4.
        * Upgraded Docker to v19.03.3
    

###  cos-73-11647-338-0

    
    
    Date:           Oct 21, 2019
    Kernel:         [ChromiumOS-4.14.147](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/59db8e278c187cfe7879152389dd90b4c5bcc776)
    Kubernetes:     v1.13.3
    Docker:         v18.09.7
    Changelog (vs 73-11647-329-0):
        * Fixed an issue in systemd that resulted in unnecessary CPU consumption.
        * Fixed an issue in runc that resulted in unnecessary CPU consumption.
    

###  cos-dev-79-12577-0-0

    
    
    Date:           Oct 14, 2019
    Kernel:         [ChromiumOS-4.19.76](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/8a670a01fc9a69fddb208fbf410929f9462f489d)
    Kubernetes:     v1.15.3
    Docker:         v19.03.2
    Changelog (vs 79-12575-0-0):
        * Minor changes.
    

###  cos-beta-78-12499-32-0

    
    
    Date:           Oct 14, 2019
    Kernel:         [ChromiumOS-4.19.72](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/1e4d47c802bf1644c426bd9a0c4cb3a3f0baa616)
    Kubernetes:     v1.15.3
    Docker:         v19.03.2
    Changelog (vs 78-12499-26-0):
        * Updated openssl to 1.0.2t. This resolves CVE-2019-1563.
        * Backported a kernel patch to fix performance regression in wbt
          scale_up/scale_down
    

###  cos-stable-77-12371-89-0

    
    
    Date:           Oct 09, 2019
    Kernel:         [ChromiumOS-4.19.76](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/33b407437b03b80bb02ce71ae6a9caa3a4b2cdf3)
    Kubernetes:     v1.15.3
    Docker:         v19.03.1
    Changelog (vs 77-12371-76-0):
        * Upgraded the Linux kernel to 4.19.76
        * Backported a kernel patch to ensure the cfs cgroup quota/period ratio
          always stays the same. This addresses a Kubernetes issue where the pod
          cgroup could be changed into an inconsistent state
        * Backported a kernel patch to fix performance regression in wbt
          scale_up/scale_down
    

###  cos-dev-79-12575-0-0

    
    
    Date:           Oct 08, 2019
    Kernel:         [ChromiumOS-4.19.76](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/8a670a01fc9a69fddb208fbf410929f9462f489d)
    Kubernetes:     v1.15.3
    Docker:         v19.03.2
    Changelog (vs 79-12544-0-0):
        * Upgraded the Linux kernel to 4.19.76
        * Enabled FORTIFY_SOURCE, SLAB_FREELIST_RANDOM and SLAB_FREELIST_HARDENED
        * Backported a kernel patch to ensure the cfs cgroup quota/period ratio
          always stays the same. This addresses a Kubernetes issue where the pod
          cgroup could be changed into an inconsistent state
    

###  cos-beta-78-12499-26-0

    
    
    Date:           Oct 08, 2019
    Kernel:         [ChromiumOS-4.19.72](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/0b85c3e37bc602063af41552485495d764875f1c)
    Kubernetes:     v1.15.3
    Docker:         v19.03.2
    Changelog (vs 78-12499-16-0):
        * Backported a kernel patch to ensure the cfs cgroup quota/period ratio
          always stays the same. This addresses a Kubernetes issue where the pod
          cgroup could be changed into an inconsistent state
    

###  cos-stable-73-11647-329-0

    
    
    Date:           Oct 08, 2019
    Kernel:         [ChromiumOS-4.14.145](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/7b985cdebfc76a6427f51cdd4b39ccadc6dc677e)
    Kubernetes:     v1.13.3
    Docker:         v18.09.7
    Changelog (vs 73-11647-293-0):
        * Upgraded the Linux kernel to 4.14.145
        * Backported a kernel patch to ensure the cfs cgroup quota/period ratio
          always stays the same. This addresses a Kubernetes issue where the pod
          cgroup could be changed into an inconsistent state
    

###  cos-stable-69-10895-385-0

    
    
    Date:           Oct 08, 2019
    Kernel:         [ChromiumOS-4.14.145](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/8549f18963962124c0f0d73667e59dbfc17c5218)
    Kubernetes:     v1.11.8
    Docker:         v17.03.2
    Changelog (vs 69-10895-348-0):
        * Upgraded the Linux kernel to 4.14.145.
        * Backported a kernel patch to ensure the cfs cgroup quota/period ratio
          always stays the same. This addresses a Kubernetes issue where the pod
          cgroup could be changed into an inconsistent state
    

###  cos-dev-79-12544-0-0

    
    
    Date:           Sep 27, 2019
    Kernel:         [ChromiumOS-4.19.72](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2d26b9df3f90536fc6a275fcad13edfb5871ad65)
    Kubernetes:     v1.15.3
    Docker:         v19.03.2
    Changelog (vs 78-12493-0-0):
        * New milestone: M79.
        * Enabled dm-snapshot.
        * Cherry-picked https://github.com/containerd/cri/pull/1084 to containerd.
        * Upgraded containerd to v1.2.9.
    

###  cos-beta-78-12499-16-0

    
    
    Date:           Sep 27, 2019
    Kernel:         [ChromiumOS-4.19.72](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/bd33a1d7ffa2770b5fa3f7b08125e81acf56f171)
    Kubernetes:     v1.15.3
    Docker:         v19.03.2
    Changelog (vs 78-12493-0-0):
        * Promoted to beta.
        * Cherry-picked https://github.com/containerd/cri/pull/1084 to containerd.
    

###  cos-stable-77-12371-76-0

    
    
    Date:           Sep 27, 2019
    Kernel:         [ChromiumOS-4.19.72](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/a33dffa8e5c47b877e4daece938a81e3cc810b90)
    Kubernetes:     v1.15.3
    Docker:         v19.03.1
    Changelog (vs 77-12371-57-0):
        * Promoted to stable.
        * Cherry-picked https://github.com/containerd/cri/pull/1084 to containerd.
    

###  cos-dev-78-12493-0-0

    
    
    Date:           Sep 12, 2019
    Kernel:         [ChromiumOS-4.19.69](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/4dfeaae5a306348c8ece2c5f9a552d1111fce2b3)
    Kubernetes:     v1.15.3
    Docker:         v19.03.2
    Changelog (vs 78-12477-0-0):
        * Upgraded Docker to version 19.03.2
        * Upgraded compute-image-packages to 20190801
    

###  cos-beta-77-12371-57-0

    
    
    Date:           Sep 12, 2019
    Kernel:         [ChromiumOS-4.19.60](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/6e0fef1b46bb91c196be56365d9af72e52bb4675)
    Kubernetes:     v1.15.3
    Docker:         v19.03.1
    Changelog (vs 77-12371-44-0):
        * Minor changes.
    

###  cos-dev-78-12477-0-0

    
    
    Date:           Sep 04, 2019
    Kernel:         [ChromiumOS-4.19.69](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/c0cabec97571ed28ae3e62b0fb17ddb547a25dd3)
    Kubernetes:     v1.15.3
    Docker:         v19.03.1
    Changelog (vs 78-12466-0-0):
        * Minor changes.
    

###  cos-beta-77-12371-44-0

    
    
    Date:           Sep 04, 2019
    Kernel:         [ChromiumOS-4.19.60](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/74fab24be8994bb5bb8d1aa8828f50e16bb38346)
    Kubernetes:     v1.15.3
    Docker:         v19.03.1
    Changelog (vs 77-12371-37-0):
        * Upgraded containerd to v1.2.8.
    

###  cos-73-11647-293-0

    
    
    Date:           Sep 04, 2019
    Kernel:         [ChromiumOS-4.14.138](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ed61fe8747ee554d56511964d50289d4bf547083)
    Kubernetes:     v1.13.3
    Docker:         v18.09.7
    Changelog (vs 73-11647-267-0):
        * Upgraded containerd to v1.2.8.
        * Upgraded the Linux kernel to version 4.14.138.
        * Backported upstream writeback patches to fix a softlockup issue.
    

###  cos-dev-78-12466-0-0

    
    
    Date:           Aug 30, 2019
    Kernel:         [ChromiumOS-4.19.68](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f5e279214b82689015b55ba9e21d28ec3e4f6994)
    Kubernetes:     v1.15.3
    Docker:         v19.03.1
    Changelog (vs 78-12447-0-0):
        * Upgraded containerd to v1.2.8.
    

###  cos-beta-77-12371-37-0

    
    
    Date:           Aug 30, 2019
    Kernel:         [ChromiumOS-4.19.60](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/de9362443dedfb962b650233ab4e4f6e40fea193)
    Kubernetes:     v1.15.3
    Docker:         v19.03.1
    Changelog (vs 77-12371-34-0):
        * Minor changes.
    

###  cos-69-10895-348-0

    
    
    Date:           Aug 30, 2019
    Kernel:         [ChromiumOS-4.14.138](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f2a646b776532b7dda331faf8c66b0dbfa7c28b5)
    Kubernetes:     v1.11.8
    Docker:         v17.03.2
    Changelog (vs 69-10895-329-0):
        * Backported upstream writeback patches to fix a softlockup issue.
    

###  cos-dev-78-12427-0-0

    
    
    Date:           Aug 16, 2019
    Kernel:         [ChromiumOS-4.19.66](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/3a9dc431f6a4f9d3a999fee42771bdb518eb0c37)
    Kubernetes:     v1.15.2
    Docker:         v19.03.1
    Changelog (vs 77-12366-0-0):
        * Changed kernel compiler from gcc to clang.
        * Included app-admin/node-problem-detector in COS.
        * Upgraded Docker to version 19.03.1.
        * Updated the built-in kubelet to 1.15.2.
        * Upgraded to Linux Kernel version 4.19.66; this resolves CVE-2019-1125.
    

###  cos-beta-77-12371-24-0

    
    
    Date:           Aug 16, 2019
    Kernel:         [ChromiumOS-4.19.60](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/54aa50936831712642447e73fa5de04a9ee02af4)
    Kubernetes:     v1.15.2
    Docker:         v19.03.1
    Changelog (vs 77-12366-0-0):
        * Changed kernel compiler from gcc to clang.
        * Included app-admin/node-problem-detector in COS
        * Upgraded Docker to version 19.03.1.
        * Updated the built-in kubelet to 1.15.2.
    

###  cos-stable-76-12239-60-0

    
    
    Date:           Aug 16, 2019
    Kernel:         [ChromiumOS-4.19.44](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/87b14d7f1f3f979ecdff38f6ca989c2553f6dd4b)
    Kubernetes:     v1.14.4
    Docker:         v18.09.8
    Changelog (vs 76-12239-60-0):
        * Promoted to stable channel.
    

###  cos-73-11647-267-0

    
    
    Date:           Aug 08, 2019
    Kernel:         [ChromiumOS-4.14.137](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e56f40f300f7a8e1e11933a942c71b768713356a)
    Kubernetes:     v1.13.3
    Docker:         v18.09.7
    Changelog (vs 73-11647-239-0):
        * Upgraded the Linux kernel to v4.14.137. This resolves CVE-2019-1125.
    

###  cos-69-10895-329-0

    
    
    Date:           Aug 08, 2019
    Kernel:         [ChromiumOS-4.14.137](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/b7219ae04b25ef09f0116bcf95abcaff571c16c8)
    Kubernetes:     v1.11.8
    Docker:         v17.03.2
    Changelog (vs 69-10895-299-0):
        * Upgraded the Linux kernel to v4.14.137. This resolves CVE-2019-1125.
    

###  cos-dev-77-12366-0-0

    
    
    Date:           Aug 02, 2019
    Kernel:         [ChromiumOS-4.19.60](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e0affeade47acb27f7d3ffe2f2c435e162286d7e)
    Kubernetes:     v1.15.1
    Docker:         v18.09.8
    Changelog (vs 77-12318-0-0):
        * Added a package sys-fs/xfsprogs.
        * Upgraded Docker to version 18.09.8. This resolves CVE-2018-15664.
        * Upgraded runc to version 1.0.0_rc8.
        * Upgraded docker-proxy to version 0.8.0_p20190513.
        * Upgraded the built-in kubelet to 1.15.1.
    

###  cos-beta-76-12239-60-0

    
    
    Date:           Aug 02, 2019
    Kernel:         [ChromiumOS-4.19.44](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/87b14d7f1f3f979ecdff38f6ca989c2553f6dd4b)
    Kubernetes:     v1.14.4
    Docker:         v18.09.8
    Changelog (vs 76-12239-39-0):
        * Upgraded Docker to version 18.09.8.
    

###  cos-dev-77-12318-0-0

    
    
    Date:           Jul 12, 2019
    Kernel:         [ChromiumOS-4.19.47](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/bac374ea9668979cff35bb47423cbcfd382d89a4)
    Kubernetes:     v1.15.0
    Docker:         v18.09.6
    Changelog (vs 77-12314-0-0):
        * Minor changes.
    

###  cos-beta-76-12239-39-0

    
    
    Date:           Jul 12, 2019
    Kernel:         [ChromiumOS-4.19.44](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/0fb17cd4e23f158fd031e90d4e22354e05928663)
    Kubernetes:     v1.14.4
    Docker:         v18.09.7
    Changelog (vs 76-12239-29-0):
        * Upgraded Docker to version 18.09.7. This resolves CVE-2018-15664.
        * Upgraded runc to version 1.0.0_rc8.
        * Updated the built-in kubelet to 1.14.4.
        * Upgraded docker-proxy to version 0.8.0_p20190513.
        * Upgraded containerd to v1.2.7.
    

###  cos-stable-75-12105-97-0

    
    
    Date:           Jul 12, 2019
    Kernel:         [ChromiumOS-4.14.111](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/bb60ed8b3d7e1babfa843ea4fd291528f1d79268)
    Kubernetes:     v1.13.6
    Docker:         v18.09.7
    Changelog (vs 75-12105-88-0):
        * Upgraded Docker to version 18.09.7. This resolves CVE-2018-15664.
        * Upgraded runc to version 1.0.0_rc8.
        * Upgraded docker-proxy to version 0.8.0_p20190513.
        * Fixed an issue introduced by NFLX-2019-001 fixes.
    
    

###  cos-stable-73-11647-239-0

    
    
    Date:           Jul 12, 2019
    Kernel:         [ChromiumOS-4.14.131](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f75c79ad0a4814bd82f2bd875c5e5ede534f9004)
    Kubernetes:     v1.13.3
    Docker:         v18.09.7
    Changelog (vs 73-11647-231-0):
        * Upgraded Docker to version 18.09.7. This resolves CVE-2018-15664.
        * Upgraded runc to version 1.0.0_rc8.
        * Upgraded docker-proxy to version 0.8.0_p20190513.
    

###  cos-stable-69-10895-299-0

    
    
    Date:           Jul 12, 2019
    Kernel:         [ChromiumOS-4.14.132](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/d2ac2ef5e566ddec6309611d85ef384b4284d60d)
    Kubernetes:     v1.11.8
    Docker:         v17.03.2
    Changelog (vs 69-10895-277-0):
        * Fixed vulnerability in app-arch/bzip2 (CVE-2019-12900).
        * Updated kernel to version v4.14.132.
        * Fixed an issue introduced by NFLX-2019-001 fixes.
    
    

###  cos-dev-77-12314-0-0

    
    
    Date:           Jul 02, 2019
    Kernel:         [ChromiumOS-4.19.56](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/7d1ef39e3a7482d0c6002393dfd7e2a2eeed0c64)
    Kubernetes:     v1.15.0
    Docker:         v18.09.6
    Changelog (vs 77-12293-0-0):
        * Upgraded containerd to v1.2.7.
    

###  cos-beta-76-12239-29-0

    
    
    Date:           Jul 02, 2019
    Kernel:         [ChromiumOS-4.19.44](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/d5fd52801a7f5a949cdf3a97ddda1200bbae9277)
    Kubernetes:     v1.14.2
    Docker:         v18.09.5
    Changelog (vs 76-12239-21-0):
        * Fixed an issue introduced by NFLX-2019-001 fixes.
    

###  cos-stable-75-12105-88-0

    
    
    Date:           Jul 02, 2019
    Kernel:         [ChromiumOS-4.14.119](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/c1c7b3347f217eab8c557c213d2f809cb35033b9)
    Kubernetes:     v1.13.6
    Docker:         v18.09.3
    Changelog (vs 75-12105-77-0):
        * Upgraded containerd to v1.2.7.
    

###  cos-73-11647-231-0

    
    
    Date:           Jul 02, 2019
    Kernel:         [ChromiumOS-4.14.131](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f75c79ad0a4814bd82f2bd875c5e5ede534f9004)
    Kubernetes:     v1.13.3
    Docker:         v18.09.3
    Changelog (vs 73-11647-217-0):
        * Upgraded containerd to v1.2.7.
        * Updated kernel to version v4.14.131.
        * Fixed vulnerability in app-arch/bzip2 (CVE-2019-12900).
        * Fixed an issue introduced by NFLX-2019-001 fixes.
    

###  cos-dev-77-12293-0-0

    
    
    Date:           Jun 24, 2019
    Kernel:         [ChromiumOS-4.19.53](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/337e5a1ca410d2b7ab6e53a87e51b60fddab0869)
    Kubernetes:     v1.15.0
    Docker:         v18.09.6
    Changelog (vs 76-12239-14-0):
        * Upgraded to Linux kernel version 4.19.
        * Fixed the NFLX-2019-001 TCP SACK vulnerabilities in the Linux kernel.
        * Updated the built-in kubelet to 1.15.0.
        * Enabled virtio_balloon driver.
        * Added the conntrack command line utility.
        * Enabled cgroup-v2 hybrid mode.
        * Upgraded Docker to v18.09.6.
        * Upgraded sys-apps/lm_sensors to version 3.5.0.
        * Fixed a vulnerability in vim (CVE-2019-12735) that allows remote attackers to execute arbitrary OS commands.
    

###  cos-beta-76-12239-21-0

    
    
    Date:           Jun 24, 2019
    Kernel:         [ChromiumOS-4.19.44](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/842b4918f5073d373ad833415aa8885e9ec85062)
    Kubernetes:     v1.14.2
    Docker:         v18.09.5
    Changelog (vs 76-12239-14-0):
        * Fixed the NFLX-2019-001 TCP SACK vulnerabilities in the Linux kernel.
    

###  cos-stable-75-12105-77-0

    
    
    Date:           Jun 24, 2019
    Kernel:         [ChromiumOS-4.14.119](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/c1c7b3347f217eab8c557c213d2f809cb35033b9)
    Kubernetes:     v1.13.6
    Docker:         v18.09.3
    Changelog (vs 75-12105-71-0):
        * Fixed the NFLX-2019-001 TCP SACK vulnerabilities in the Linux kernel.
    

###  cos-73-11647-217-0

    
    
    Date:           Jun 19, 2019
    Kernel:         [ChromiumOS-4.14.127](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f2e94ae3029403e49b4ecec8dcecbba5ae4dac51)
    Kubernetes:     v1.13.3
    Docker:         v18.09.3
    Changelog (vs 73-11647-214-0):
        * Updated the Linux kernel to version 4.14.127 to resolve the NFLX-2019-001
          TCP SACK vulnerabilities.
    

###  cos-69-10895-277-0

    
    
    Date:           Jun 19, 2019
    Kernel:         [ChromiumOS-4.14.127](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/6b10a0b5b1910970dc3b62c14c011b39343a5279)
    Kubernetes:     v1.11.8
    Docker:         v17.03.2
    Changelog (vs 69-10895-273-0):
        * Updated the Linux kernel to version 4.14.127 to resolve the NFLX-2019-001
          TCP SACK vulnerabilities.
    

###  cos-dev-76-12239-14-0

    
    
    Date:           Jun 17, 2019
    Kernel:         [ChromiumOS-4.19.44](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/1a775b33a80e6765af3d26d1800f1aaf7bde1eff)
    Kubernetes:     v1.14.2
    Docker:         v18.09.5
    Changelog (vs 76-12238-0-0):
        * Upgraded to Linux kernel version 4.19.
        * Enabled cgroup-v2 hybrid mode in systemd
    

###  cos-beta-75-12105-71-0

    
    
    Date:           Jun 17, 2019
    Kernel:         [ChromiumOS-4.14.119](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/9ac4430f4a9cfd1b3e53d8dea1bc33a5156dc23d)
    Kubernetes:     v1.13.6
    Docker:         v18.09.3
    Changelog (vs 75-12105-54-0):
        * Minor changes.
    

###  cos-73-11647-214-0

    
    
    Date:           Jun 17, 2019
    Kernel:         [ChromiumOS-4.14.124](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/9acdbf036ba70ee01ee1d4f9be3b85f6584f4e91)
    Kubernetes:     v1.13.3
    Docker:         v18.09.3
    Changelog (vs 73-11647-192-0):
        * Updated kernel to version v4.14.124.
        * Backported affinity change-set for napi-tx.
    

###  cos-69-10895-273-0

    
    
    Date:           Jun 17, 2019
    Kernel:         [ChromiumOS-4.14.124](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2e924a33d0f11e02efc3b09679fb79dff122fbb3)
    Kubernetes:     v1.11.8
    Docker:         v17.03.2
    Changelog (vs 69-10895-255-0):
        * Updated kernel to version v4.14.124.
    

###  cos-dev-76-12238-0-0

    
    
    Date:           May 31, 2019
    Kernel:         [ChromiumOS-4.14.120](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ac488ef22a3b01a5bcf060f8a9745a2b7d082da3)
    Kubernetes:     v1.14.2
    Docker:         v18.09.5
    Changelog (vs 76-12232-0-0):
        * Updated kernel to version 4.14.120.
    

###  cos-beta-75-12105-54-0

    
    
    Date:           May 31, 2019
    Kernel:         [ChromiumOS-4.14.119](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ad225858742ac629a9f18157937087fbfbc47e75)
    Kubernetes:     v1.13.6
    Docker:         v18.09.3
    Changelog (vs 75-12105-52-0):
        * Minor changes.
    

###  cos-dev-76-12232-0-0

    
    
    Date:           May 28, 2019
    Kernel:         [ChromiumOS-4.14.119](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/691c0c01178b92cafe3413dd446753559039b865)
    Kubernetes:     v1.14.2
    Docker:         v18.09.5
    Changelog (vs 76-12206-0-0):
        * Merged Linux Stable Kernel 'v4.14.119' for resolving Microarchitectural
          Data Sampling (MDS) vulnerabilities (CVE-2018-12126, CVE-2018-12127,
          CVE-2018-12130, CVE-2019-11091).
        * Upgrade systemd to v239
        * Updated the built-in kubelet to 1.14.2.
        * Upgraded cos-toolbox to version 20190523-00.
        * Set OOM score to -999 for docker.service and containerd.service to enhance
          the reliability of core system daemons.
        * Add restart policy in containerd.service, and corrected docker.service's
          dependency on containerd.service to allow containerd to recover from crashes.
        * Cherry-picked upstream patch https://patchwork.kernel.org/patch/10951403/ in kernel to fix
          a bug in lockd introduced by commit 01b79d20008d "lockd: Show pid of lockd for remote locks"
          in Linux kernel v4.14.105.
        * Rotated keys used by UEFI Secure Boot for signing and verifying the UEFI boot path.
    

###  cos-beta-75-12105-52-0

    
    
    Date:           May 28, 2019
    Kernel:         [ChromiumOS-4.14.119](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ad225858742ac629a9f18157937087fbfbc47e75)
    Kubernetes:     v1.13.6
    Docker:         v18.09.3
    Changelog (vs 75-12105-40-0):
        * Merged Linux Stable Kernel 'v4.14.119' for resolving Microarchitectural
          Data Sampling (MDS) vulnerabilities (CVE-2018-12126, CVE-2018-12127,
          CVE-2018-12130, CVE-2019-11091).
        * Set OOM score to -999 for docker.service and containerd.service to enhance
          the reliability of core system daemons.
        * Add restart policy in containerd.service, and corrected docker.service's
          dependency on containerd.service to allow containerd to recover from crashes.
        * Cherry-picked upstream patch https://patchwork.kernel.org/patch/10951403/ in kernel to fix
          a bug in lockd introduced by commit 01b79d20008d "lockd: Show pid of lockd for remote locks"
          in Linux kernel v4.14.105.
        * Rotated keys used by UEFI Secure Boot for signing and verifying the UEFI boot path.
    

###  cos-stable-74-11895-125-0

    
    
    Date:           May 28, 2019
    Kernel:         [ChromiumOS-4.14.119](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/a93b288ad6dbf9a7749a59e31780554f5b7fd7e8)
    Kubernetes:     v1.13.5
    Docker:         v18.09.3
    Changelog (vs 74-11895-86-0):
        * Merged Linux Stable Kernel 'v4.14.119' for resolving Microarchitectural
          Data Sampling (MDS) vulnerabilities (CVE-2018-12126, CVE-2018-12127,
          CVE-2018-12130, CVE-2019-11091).
        * Upgraded curl to 7.64.1 to fix CVE-2018-16890.
        * Upgraded containerd to version 1.2.6.
        * Set OOM score to -999 for docker.service and containerd.service to enhance
          the reliability of core system daemons.
        * Add restart policy in containerd.service, and corrected docker.service's
          dependency on containerd.service to allow containerd to recover from crashes.
        * Cherry-picked upstream patch https://patchwork.kernel.org/patch/10951403/ in kernel to fix
          a bug in lockd introduced by commit 01b79d20008d "lockd: Show pid of lockd for remote locks"
          in Linux kernel v4.14.105.
        * Rotated keys used by UEFI Secure Boot for signing and verifying the UEFI boot path.
    

###  cos-73-11647-192-0

    
    
    Date:           May 28, 2019
    Kernel:         [ChromiumOS-4.14.119+](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/3c1eaaebd851a2de9dc7ec1be4ddf32dc7de6d41)
    Kubernetes:     v1.13.3
    Docker:         v18.09.3
    Changelog (vs 73-11647-182-0):
        * Upgraded curl to 7.64.1 to fix CVE-2018-16890.
        * Upgraded containerd to version 1.2.6.
        * Set OOM score to -999 for docker.service and containerd.service to enhance
          the reliability of core system daemons.
        * Add restart policy in containerd.service, and corrected docker.service's
          dependency on containerd.service to allow containerd to recover from crashes.
        * Backported affinity changes to support napi-tx in COS.
        * Cherry-picked upstream patch https://patchwork.kernel.org/patch/10951403/ in kernel to fix
          a bug in lockd introduced by commit 01b79d20008d "lockd: Show pid of lockd for remote locks"
          in Linux kernel v4.14.105.
        * Rotated keys used by UEFI Secure Boot for signing and verifying the UEFI boot path.
    

###  cos-69-10895-255-0

    
    
    Date:           May 28, 2019
    Kernel:         [ChromiumOS-4.14.119+](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/584b9a03100a25a35e5e0e7e9067f9957396f638)
    Kubernetes:     v1.11.8
    Docker:         v17.03.2
    Changelog (vs 69-10895-242-0):
        * Upgraded curl to 7.64.1 to fix CVE-2018-16890.
        * Cherry-picked upstream patch https://patchwork.kernel.org/patch/10951403/ in kernel to fix
          a bug in lockd introduced by commit 01b79d20008d "lockd: Show pid of lockd for remote locks"
          in Linux kernel v4.14.105.
        * Rotated keys used by UEFI Secure Boot for signing and verifying the UEFI boot path.
    

###  cos-dev-76-12206-0-0

    
    
    Date:           May 16, 2019
    Kernel:         [ChromiumOS-4.14.118](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/9a7ab8d8a037b99be47c6f32d3fc28df262c8012)
    Kubernetes:     v1.14.1
    Docker:         v18.09.5
    Changelog (vs 76-12163-0-0):
        * Upgraded the built-in kubelet to 1.14.1.
        * Upgraded containerd to version 1.2.6.
        * Upgraded sqlite to 3.25.3 to fix CVE-2018-20346.
        * Mitigated a mount hang issue in the Linux kernel.
    

###  cos-beta-75-12105-40-0

    
    
    Date:           May 16, 2019
    Kernel:         [ChromiumOS-4.14.111](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/994bc24c5ff4a586ac2b00872678cb266dad4c01)
    Kubernetes:     v1.13.6
    Docker:         v18.09.3
    Changelog (vs 75-12105-24-0):
        * Upgraded containerd to version 1.2.6.
        * Upgraded the built-in kubelet to 1.13.6.
        * Upgraded sqlite to 3.25.3 to fix CVE-2018-20346.
        * Upgraded tar to 1.32 to fix CVE-2019-9923.
        * Upgraded curl to 7.64.1 to fix CVE-2018-16890.
    

###  cos-73-11647-182-0

    
    
    Date:           May 16, 2019
    Kernel:         [ChromiumOS-4.14.119](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/9e5137a84a421d65264c86f7ea0f29ceaeb04771)
    Kubernetes:     v1.13.3
    Docker:         v18.09.3
    Changelog (vs 73-11647-163-0):
        * Merged Linux Stable Kernel 'v4.14.119' for resolving Microarchitectural
          Data Sampling (MDS) vulnerabilities (CVE-2018-12126, CVE-2018-12127,
          CVE-2018-12130, CVE-2019-11091).
        * Mitigated a mount hang issue in the Linux kernel.
    

###  cos-69-10895-242-0

    
    
    Date:           May 15, 2019
    Kernel:         [ChromiumOS-4.14.119](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/cb3a5bc72ef93f5026c43e9190f9127be9c46ead)
    Kubernetes:     v1.11.8
    Docker:         v17.03.2
    Changelog (vs 69-10895-211-0):
        *  Merged Linux Stable Kernel 'v4.14.119' for resolving Microarchitectural
           Data Sampling (MDS) vulnerabilities (CVE-2018-12126, CVE-2018-12127,
           CVE-2018-12130, CVE-2019-11091).
        *  Mitigated a mount hang issue in the Linux kernel.
    

###  cos-dev-76-12163-0-0

    
    
    Date:           May 02, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f98df700614d71fb0edf8f8bccf7eb94d7dc551c)
    Kubernetes:     v1.13.4
    Docker:         v18.09.5
    Changelog (vs 76-12128-0-0):
        * Updated curl to 7.64.1. This resolves CVE-2018-16890, CVE-2019-3822 and CVE-2019-3823.
        * Updated tar to 1.32. This resolves CVE-2019-9923.
    

###  cos-beta-75-12105-24-0

    
    
    Date:           May 02, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/0c986c1fc3a1fd447645c96681d802689fac8868)
    Kubernetes:     v1.13.4
    Docker:         v18.09.3
    Changelog (vs 75-12105-10-0):
        * Backported fix for Linux kernel CVE-2019-7308.
        * Backported affinity changes to support napi-tx in COS.
    

###  cos-dev-76-12128-0-0

    
    
    Date:           Apr 25, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/d5f0fa0a2e49e1ed38fdf0bd93255ab953484f05)
    Kubernetes:     v1.13.4
    Docker:         v18.09.5
    Changelog (vs 75-12103-0-0):
        * Upgraded Docker to v18.09.5
        * Backported affinity changes to support napi-tx in COS.
    

###  cos-beta-75-12105-10-0

    
    
    Date:           Apr 25, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2eec8799ba26fe5581d294cb14430e95801e87ef)
    Kubernetes:     v1.13.4
    Docker:         v18.09.3
    Changelog (vs 75-12103-0-0):
        * Promoted to beta channel.
        * Minor changes.
    

###  cos-stable-74-11895-86-0

    
    
    Date:           Apr 25, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/6bc44776c10dfc4c2c456de6be9782e7877a74ca)
    Kubernetes:     v1.13.5
    Docker:         v18.09.3
    Changelog (vs 74-11895-76-0):
        * Promoted to stable channel.
        * Minor changes.
    

###  cos-dev-75-12103-0-0

    
    
    Date:           Apr 19, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2eec8799ba26fe5581d294cb14430e95801e87ef)
    Kubernetes:     v1.13.4
    Docker:         v18.09.3
    Changelog (vs 75-12062-0-0):
        * Set LimitNOFILE to 1048576 in containerd.service to fix an issue
          where the file descriptor limit was not being properly applied to
          containerd.
    

###  cos-beta-74-11895-76-0

    
    
    Date:           Apr 19, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/6bc44776c10dfc4c2c456de6be9782e7877a74ca)
    Kubernetes:     v1.13.5
    Docker:         v18.09.3
    Changelog (vs 74-11895-56-0):
        * Set LimitNOFILE to 1048576 in containerd.service to fix an issue
          where the file descriptor limit was not being properly applied to
          containerd.
    

###  cos-stable-73-11647-163-0

    
    
    Date:           Apr 19, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/d6114dbb2c01eae755f357b8c68f24300965be28)
    Kubernetes:     v1.13.3
    Docker:         v18.09.3
    Changelog (vs 73-11647-121-0):
        * Set LimitNOFILE to 1048576 in containerd.service to fix an issue
          where the file descriptor limit was not being properly applied to
          containerd.
    

###  cos-dev-75-12062-0-0

    
    
    Date:           Apr 11, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/0ddcf7d6aaab7ac9bafee3751a871fd2420a3022)
    Kubernetes:     v1.13.4
    Docker:         v18.09.3
    Changelog (vs 75-12001-0-0):
        * Included 'perf' tool in the image.
        * Fixed an issue where Docker did not preserve the UIDs/GIDs of the init
          process on exec.
        * Fixed slow access to /sys/fs/cgroup/memory/memory.stat. This resolves
          kubelet performance degradation.
    

###  cos-beta-74-11895-56-0

    
    
    Date:           Apr 11, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/6bc44776c10dfc4c2c456de6be9782e7877a74ca)
    Kubernetes:     v1.13.5
    Docker:         v18.09.3
    Changelog (vs 74-11895-38-0):
        * Minor changes.
    

###  cos-69-10895-211-0

    
    
    Date:           Apr 11, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ad21843351160840c0a88d8243a18aaa24f4fb11)
    Kubernetes:     v1.11.8
    Docker:         v17.03.2
    Changelog (vs 69-10895-201-0):
        * Fixed slow access to /sys/fs/cgroup/memory/memory.stat. This resolves
          kubelet performance degradation.
    

###  cos-dev-75-12001-0-0

    
    
    Date:           Apr 01, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/d341d49520c2a62c2f94c7215299b89ff7ccb3f7)
    Kubernetes:     v1.13.4
    Docker:         v18.09.3
    Changelog (vs 75-11981-0-0):
        * Updated compute-image-package and oslogin package to v20190304.
        * Added cos-kernel tool to toolbox.
    

###  cos-beta-74-11895-38-0

    
    
    Date:           Apr 01, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/0e3fab864a5fd885ef57a77059bc7c045967ddb7)
    Kubernetes:     v1.13.5
    Docker:         v18.09.3
    Changelog (vs 74-11895-32-0):
        * Included perf tool in the image.
        * Fixed a bug that dockerd may start containerd even if containerd.service exists.
        * Fixed an issue where Docker did not preserve the UIDs/GIDs of the init process on exec.
        * Updated the built-in kubelet to 1.13.5.
    

###  cos-stable-73-11647-121-0

    
    
    Date:           Apr 01, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/c04a4afa67584baf4601090471d7d308d13932b9)
    Kubernetes:     v1.13.3
    Docker:         v18.09.3
    Changelog (vs 73-11647-112-0):
        * Included perf tool in the image.
        * Fixed a bug that dockerd may start containerd even if containerd.service exists.
        * Fixed an issue where Docker did not preserve the UIDs/GIDs of the init process on exec.
    

###  cos-69-10895-201-0

    
    
    Date:           Apr 01, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e622209aebcc779c3340bc6c3610cfbec86ed112)
    Kubernetes:     v1.11.8
    Docker:         v17.03.2
    Changelog (vs 69-10895-172-0):
        * Included perf tool in the image.
        * Included sosreport in the image.
        * Updated the built-in kubelet to 1.11.8.
        * Fixed an issue where Shielded VM integrity measurements weren't being logged properly.
        * Merged Linux Stable Kernel 'v4.14.106'.
    

###  cos-dev-75-11981-0-0

    
    
    Date:           Mar 25, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/509908a9db196d8314b1dbf3eadb4e4bbd57a89e)
    Kubernetes:     v1.13.4
    Docker:         v18.09.3
    Changelog (vs 74-11892-0-0):
        * New milestone: M75
        * Updated the built-in kubelet to 1.13.4.
        * Fixed an issue where a race condition between Docker and containerd
          resulted in a Docker live restore failure.
        * Upgraded Docker to v18.09.3.
        * Upgraded containerd to v1.2.5.
    

###  cos-beta-74-11895-32-0

    
    
    Date:           Mar 25, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/8540d51e9075c9b47e03132732b1f960cb60ab96)
    Kubernetes:     v1.13.3
    Docker:         v18.09.3
    Changelog (vs 74-11892-0-0):
        * Promoted to beta channel.
        * Upgraded Docker to v18.09.3.
        * Upgraded containerd to v1.2.5.
    

###  cos-stable-73-11647-112-0

    
    
    Date:           Mar 25, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/1eb10e59948394bae265bef1b18f166337a03a73)
    Kubernetes:     v1.13.3
    Docker:         v18.09.3
    Changelog (vs 73-11647-97-0):
        * Promoted to stable channel.
    

###  cos-beta-73-11647-97-0

    
    
    Date:           Mar 18, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/266a6db12c996f4000abb93619e5b5429a4abe9b)
    Kubernetes:     v1.13.3
    Docker:         v18.09.3
    Changelog (vs 73-11647-90-0):
        * Upgraded Docker to v18.09.3.
        * Upgraded containerd to v1.2.5.
    

###  cos-dev-74-11892-0-0

    
    
    Date:           Mar 15, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/479f3ad5abb7fe6c95aee87a07fc2536ea6039ee)
    Kubernetes:     v1.13.3
    Docker:         v18.09.1
    Changelog (vs 74-11888-0-0):
        * Enabled Shielded VMs. Instances created from this image will use UEFI
        firmware and measure boot components into a vTPM by default. Click
        [here](https://cloud.google.com/shielded-vm/?hl=zh-cn) to learn more about Shielded VMs.
    

###  cos-beta-73-11647-90-0

    
    
    Date:           Mar 15, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/9c0725ca524a89b3854cefdfbd5c147efd4f5154)
    Kubernetes:     v1.13.3
    Docker:         v18.09.1
    Changelog (vs 73-11647-75-0):
        * Minor changes.
    

###  cos-stable-72-11316-171-0

    
    
    Date:           Mar 15, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/66ab05738a89be545af257dbea63970a127565b3)
    Kubernetes:     v1.12.4
    Docker:         v18.06.1
    Changelog (vs 72-11316-136-0):
        * Fixed an issue where setting the "cos-update-strategy"
    metadata key to "update_disabled" had no impact on the system's auto
    update policy.
    

###  cos-dev-74-11888-0-0

    
    
    Date:           Mar 07, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/479f3ad5abb7fe6c95aee87a07fc2536ea6039ee)
    Kubernetes:     v1.13.3
    Docker:         v18.09.1
    Changelog (vs 74-11836-0-0):
        * Fixed a bug that caused crash-reporter to abort early.
    

###  cos-beta-73-11647-75-0

    
    
    Date:           Mar 07, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/8a0b9c570d83e725c7a83feaeac7acc02784463a)
    Kubernetes:     v1.13.3
    Docker:         v18.09.1
    Changelog (vs 73-11647-64-0):
        * Fixed a bug that caused crash-reporter to abort early.
    

###  cos-dev-74-11836-0-0

    
    
    Date:           Feb 28, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f99ad93f0cae4dba4afe59b1d3a3fc75161fd3fd)
    Kubernetes:     v1.13.3
    Docker:         v18.09.1
    Changelog (vs 74-11800-0-0):
        * Fixed an issue where setting the "cos-update-strategy"
    metadata key to "update_disabled" had no impact on the system's auto
    update policy.
    
    

###  cos-beta-73-11647-64-0

    
    
    Date:           Feb 28, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/eb49a8f827edb6d8b5926b3ea48c6bc086d7a704)
    Kubernetes:     v1.13.3
    Docker:         v18.09.1
    Changelog (vs 73-11647-46-0):
        * Fixed an issue where setting the "cos-update-strategy"
    metadata key to "update_disabled" had no impact on the system's auto
    update policy.
    
    

###  cos-69-10895-172-0

    
    
    Date:           Feb 28, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/edb81c460eee7a4a35e2a95ebf6450df0963398e)
    Kubernetes:     v1.11.1
    Docker:         v17.03.2
    Changelog (vs 69-10895-138-0):
        * Enabled kernel.softlockup_all_cpu_backtrace. This was
    previously disabled to mitigate a kernel deadlock issue, which is now
    resolved.
        * Configured docker.service by setting RestartSecs=10 to
          always restart Docker after 10 seconds.
    

###  cos-dev-74-11800-0-0

    
    
    Date:           Feb 22, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/8325a284b1fc1efff248b113d8e8a2626955d5b7)
    Kubernetes:     v1.13.3
    Docker:         v18.09.1
    Changelog (vs 74-11758-0-0):
        * Configured docker.service by setting RestartSecs=10 to
          always restart Docker after 10 seconds.
    

###  cos-beta-73-11647-46-0

    
    
    Date:           Feb 22, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/6e13e703ed11e78d111f660331b6eda42f224c00)
    Kubernetes:     v1.13.3
    Docker:         v18.09.1
    Changelog (vs 73-11647-35-0):
        * Configured docker.service by setting RestartSecs=10 to
          always restart Docker after 10 seconds.
    

###  cos-dev-74-11758-0-0

    
    
    Date:           Feb 14, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/b8a64fd875c87eb930cd7e86ded917e4ecc1da38)
    Kubernetes:     v1.13.3
    Docker:         v18.09.1
    Changelog (vs 73-11647-29-0):
        * New milestone: M74.
        * Updated containerd to 1.2.3.
        * Enabled RAID0 related kernel config.
        * Updated openssl to 1.0.2q. This resolves CVE-2018-0734.
    

###  cos-beta-73-11647-35-0

    
    
    Date:           Feb 14, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/6e13e703ed11e78d111f660331b6eda42f224c00)
    Kubernetes:     v1.13.3
    Docker:         v18.09.1
    Changelog (vs 73-11647-29-0):
        * Promoted to beta channel.
        * Updated containerd to 1.2.3.
        * Updated openssl to 1.0.2q. This resolves CVE-2018-0734.
    

###  cos-stable-72-11316-136-0

    
    
    Date:           Feb 14, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/66ab05738a89be545af257dbea63970a127565b3)
    Kubernetes:     v1.12.4
    Docker:         v18.06.1
    Changelog (vs 72-11316-134-0):
        * Promoted to stable channel.
    

###  cos-dev-73-11647-29-0

    
    
    Date:           Feb 11, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/6deda81c69d428eaf5624b7f77ac3a9ba885a6a3)
    Kubernetes:     v1.13.3
    Docker:         v18.09.1
    Changelog (vs 73-11647-18-0):
        * Enabled kernel crash dump Alpha feature in COS.
        * Updated the built-in kubelet to 1.13.3.
        * Enabled auto update when using Shielded VMs that have never booted in Secure Boot mode. Shielded VMs that have booted in Secure Boot mode at least once will still have auto update disabled. This change does not impact images in cos-cloud.
    

###  cos-beta-72-11316-134-0

    
    
    Date:           Feb 11, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/66ab05738a89be545af257dbea63970a127565b3)
    Kubernetes:     v1.12.4
    Docker:         v18.06.1
    Changelog (vs 72-11316-115-0):
        * Backported fix for Linux kernel CVE-2018-16884.
    

###  cos-dev-73-11647-18-0

    
    
    Date:           Feb 04, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/9434875af1a814d02f77d4f9f3e52b74465fd73a)
    Kubernetes:     v1.13.2
    Docker:         v18.09.1
    Changelog (vs 73-11636-0-0):
        * Updated docker to v18.09.1.
        * Updated containerd to v1.2.2.
        * Logs additional debug info on serial console during boot.
    

###  cos-beta-72-11316-115-0

    
    
    Date:           Feb 04, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/93d39103381d75eef0fad1d9acd4666c2320ea71)
    Kubernetes:     v1.12.4
    Docker:         v18.06.1
    Changelog (vs 72-11316-99-0):
        * Minor changes.
    

###  cos-dev-73-11636-0-0

    
    
    Date:           Jan 24, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/0e222308f1ecd2c1c612d0d8aad71f8a34ad0e58)
    Kubernetes:     v1.13.2
    Docker:         v18.09.0
    Changelog (vs 73-11553-0-0):
        * Made containerd run as a standalone systemd service.
        * Updated the built-in kubelet to 1.13.2.
        * Reenabled kernel.softlockup_all_cpu_backtrace sysctl.
        * Disabled the CONFIG_DEVMEM configuration option in the kernel.
        * Enabled kernel module signing.
        * Installed a new package keyutils.
        * Updated mdadm to 4.1.
    

###  cos-beta-72-11316-99-0

    
    
    Date:           Jan 24, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/04f032bcba5d37a03ec09386c53ccf890a957bb6)
    Kubernetes:     v1.12.4
    Docker:         v18.06.1
    Changelog (vs 72-11316-72-0):
        * Updated the built-in kubelet to 1.12.4.
    

###  cos-69-10895-138-0

    
    
    Date:           Jan 24, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/edb81c460eee7a4a35e2a95ebf6450df0963398e)
    Kubernetes:     v1.11.1
    Docker:         v17.03.2
    Changelog (vs 69-10895-123-0):
        * Backported the fix for a deadlock issue in kernel panic.
        * Merged Linux Stable Kernel 'v4.14.91'.
    

###  cos-dev-73-11553-0-0

    
    
    Date:           Jan 10, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f3657621d66b1875da1098fe545e666f037797da)
    Kubernetes:     v1.13.0
    Docker:         v18.09.0
    Changelog (vs 73-11517-0-0):
        * Upgraded docker to v18.09.0.
        * Cherry-pick Ext4 commits that address FS inconsistencies caused by
          disruptions during NFS CREATE operation under certain conditions.
    

###  cos-beta-72-11316-72-0

    
    
    Date:           Jan 10, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/d48fd11cb831cd6dd20a0f9174944eaf127322df)
    Kubernetes:     v1.12.3
    Docker:         v18.06.1
    Changelog (vs 72-11316-56-0):
        * Set CONFIG_BLK_WBT_MQ=y to improve performance isolation on
          persistent disks. This fixes a bug where writes on a SSD persistent
          disk can affect performance on the Standard persistent boot disk.
    

###  cos-69-10895-123-0

    
    
    Date:           Jan 10, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/a766b4df211de407187de69d671882e50177c0e4)
    Kubernetes:     v1.11.1
    Docker:         v17.03.2
    Changelog (vs 69-10895-102-0):
        * Set CONFIG_BLK_WBT_MQ=y to improve performance isolation on
          persistent disks. This fixes a bug where writes on a SSD persistent
          disk can affect performance on the Standard persistent boot disk.
        * Cherry-pick Ext4 commits that address FS inconsistencies caused by
          disruptions during NFS CREATE operation under certain conditions.
        * Merge Linux Stable Kernel 'v4.14.89'
    

###  cos-dev-73-11517-0-0

    
    
    Date:           Jan 03, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/78cf9a607b2636aad660628021f8a4035cf486a6)
    Kubernetes:     v1.13.0
    Docker:         v18.06.1
    Changelog (vs 73-11438-0-0):
        * Set CONFIG_BLK_WBT_MQ=y to improve performance isolation on
          persistent disks. This fixes a bug where writes on a SSD persistent
          disk can affect performance on the Standard persistent boot disk.
        * Merged Linux stable version v4.14.89 into the kernel.
    

###  cos-beta-72-11316-56-0

    
    
    Date:           Jan 03, 2019
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2560ace36cc1a4ff381e1d71b4c8376661233466)
    Kubernetes:     v1.12.3
    Docker:         v18.06.1
    Changelog (vs 72-11316-34-0):
        * Minor changes.
    

###  cos-dev-73-11438-0-0

    
    
    Date:           Dec 20, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/83371f57ccb49a1bdcd2a5498d57a183f94c11dd)
    Kubernetes:     v1.13.0
    Docker:         v18.06.1
    Changelog (vs 73-11391-0-0):
        * Upgraded runc to version 1.0.0-rc6. Fixes an issue observed in
          Kubernetes liveness probes (https://github.com/opencontainers/runc/issues/1884).
    

###  cos-beta-72-11316-34-0

    
    
    Date:           Dec 20, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2f253930244182796dcfd3fa0cb217ade7f6a854)
    Kubernetes:     v1.12.3
    Docker:         v18.06.1
    Changelog (vs 72-11316-21-0):
        * Enabled the "metadata_csum" ext4 feature on the stateful partition. This
          also improves performance of boot-disk resize operation.
    

###  cos-stable-71-11151-71-0

    
    
    Date:           Dec 20, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/79a7b53abf2adb1a79eb0cdde2fbe3ff4734c33d)
    Kubernetes:     v1.11.5
    Docker:         v18.06.1
    Changelog (vs 71-11151-60-0):
        * Enabled the "metadata_csum" ext4 feature on the stateful partition. This
          also improves performance of boot-disk resize operation.
        * Apply IMA Policy only when cloud-audit-setup.service is explicitly run.
    

###  cos-69-10895-102-0

    
    
    Date:           Dec 20, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/11f991ff52a03cdd8ac6f2adf6c46979bba48724)
    Kubernetes:     v1.11.1
    Docker:         v17.03.2
    Changelog (vs 69-10895-93-0):
        * Disabled auto update on shielded images. Images in cos-cloud are
    not impacted by this change.
        * Enabled the "metadata_csum" ext4 feature on the stateful partition. This
          also improves performance of boot-disk resize operation.
        * Apply IMA Policy only when cloud-audit-setup.service is explicitly run.
    

###  cos-dev-73-11391-0-0

    
    
    Date:           Dec 14, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ce30e4931524ab8f30f7d753f7d39cebb1bf4ac1)
    Kubernetes:     v1.13.0
    Docker:         v18.06.1
    Changelog (vs 72-11316-6-0):
        * New milestone: M73.
        * Increase default fs.inotify.max_user_instances to 1024.
        * Enabled the "metadata_csum" ext4 feature on the stateful partition.
        * Updated built-in kubelet to 1.13.0.
        * Apply IMA Policy only when cloud-audit-setup.service is explicitly run.
    

###  cos-beta-72-11316-21-0

    
    
    Date:           Dec 14, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/d41f0b47d0996bbfc98e2e11fa4453ab5058f168)
    Kubernetes:     v1.12.3
    Docker:         v18.06.1
    Changelog (vs 72-11316-6-0):
        * Promoted to beta channel.
        * Apply IMA Policy only when cloud-audit-setup.service is explicitly run.
    

###  cos-stable-71-11151-60-0

    
    
    Date:           Dec 14, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/79a7b53abf2adb1a79eb0cdde2fbe3ff4734c33d)
    Kubernetes:     v1.11.5
    Docker:         v18.06.1
    Changelog (vs 71-11151-53-0):
        * Promoted to stable channel.
        * Updated built-in Kubelet to 1.11.5.
        * Disabled auto update on Shielded VM enabled images. Images in 'cos-cloud' project are not impacted by this change.
    

###  cos-dev-72-11316-6-0

    
    
    Date:           Dec 06, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/263de8111e236b02249b82e7196e41a2504d7ecd)
    Kubernetes:     v1.12.3
    Docker:         v18.06.1
    Changelog (vs 72-11315-0-0):
        * Minor changes.
    

###  cos-beta-71-11151-53-0

    
    
    Date:           Dec 06, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ac52e5f750c85eb4a85d669c1beea698a00cfb46)
    Kubernetes:     v1.11.4
    Docker:         v18.06.1
    Changelog (vs 71-11151-47-0):
        * Minor changes.
    

###  cos-stable-70-11021-99-0

    
    
    Date:           Dec 06, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/df6e456fb4311de49825eed9f7478683e51eda47)
    Kubernetes:     v1.11.3
    Docker:         v18.06.1
    Changelog (vs 70-11021-67-0):
        * Backported fix for Linux kernel CVE-2018-17182.
        * Backported fix for Linux kernel CVE-2018-18281.
    

###  cos-dev-72-11315-0-0

    
    
    Date:           Nov 30, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/45b849da0f10d19f873a9b75d087dc70bde7e77d)
    Kubernetes:     v1.12.3
    Docker:         v18.06.1
    Changelog (vs 72-11264-0-0):
        * Disabled auto update on Shielded VM enabled images. Images in 'cos-cloud' project are not impacted by this change.
        * Updated Kubernetes to v1.12.3.
    

###  cos-beta-71-11151-47-0

    
    
    Date:           Nov 30, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/3b81c3f28831b9f4366ed70987341837ee2e1033)
    Kubernetes:     v1.11.4
    Docker:         v18.06.1
    Changelog (vs 71-11151-32-0):
        * Minor changes.
    

###  cos-69-10895-93-0

    
    
    Date:           Nov 16, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/8ababd756bfbf24f7a0d7a8ae3af7fe85d320a25)
    Kubernetes:     v1.11.1
    Docker:         v17.03.2
    Changelog (vs 69-10895-91-0):
        * Updated kernel to v4.14.79.
        * Fixed the bug that cloud-init can't write gzipped files.
    

###  cos-dev-72-11264-0-0

    
    
    Date:           Nov 15, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/3505998f279389131f5a830057cce3c4220a5d70)
    Kubernetes:     v1.11.4
    Docker:         v18.06.1
    Changelog (vs 72-11229-0-0):
        * Set CONFIG_SCSI_MQ_DEFAULT=y to enable support for multiqueue SCSI for Local SSD devices.
        * Enable a few kernel configs for IPv6.
        * Upgraded built-in kubelet to v1.11.4
        * Switching back to using gcc to compile the kernel from using clang.
    

###  cos-beta-71-11151-32-0

    
    
    Date:           Nov 15, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/4fee3299be69b42dfa1949fbf49d5c2641e6952a)
    Kubernetes:     v1.11.4
    Docker:         v18.06.1
    Changelog (vs 71-11151-21-0):
        * Upgraded built-in kubelet to v1.11.4
    

###  cos-dev-72-11229-0-0

    
    
    Date:           Nov 06, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/fd7ac64fb42476dc4e365b5b0aa42149f1e70272)
    Kubernetes:     v1.11.3
    Docker:         v18.06.1
    Changelog (vs 72-11190-0-0):
        * Upgrade glibc version to v2.27.
        * Use clang compiler to build the Linux kernel.
    

###  cos-beta-71-11151-21-0

    
    
    Date:           Nov 06, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/1597eb7c5f89bc094d4be74f26f7e3bf98b564f7)
    Kubernetes:     v1.11.3
    Docker:         v18.06.1
    Changelog (vs 71-11151-16-0):
        * Minor changes.
    

###  cos-stable-70-11021-67-0

    
    
    Date:           Nov 06, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/20eb4c4bcab0f7ce05051ed5b81ee33229e63565)
    Kubernetes:     v1.11.3
    Docker:         v18.06.1
    Changelog (vs 70-11021-62-0):
        * Minor changes.
    

###  cos-dev-72-11190-0-0

    
    
    Date:           Oct 29, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/6623310fff8b446e65c9a8ca86172a4dfe6822ba)
    Kubernetes:     v1.11.3
    Docker:         v18.06.1
    Changelog (vs 72-11172-0-0):
        * Minor changes.
    

###  cos-beta-71-11151-16-0

    
    
    Date:           Oct 29, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f7bd8f4bca18c968b8d66762b5a9e029ac703076)
    Kubernetes:     v1.11.3
    Docker:         v18.06.1
    Changelog (vs 71-11151-5-0):
        * Fixed an issue where an interaction between IMA and NFS could cause deadlock.
    

###  cos-stable-70-11021-62-0

    
    
    Date:           Oct 29, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/20eb4c4bcab0f7ce05051ed5b81ee33229e63565)
    Kubernetes:     v1.11.3
    Docker:         v18.06.1
    Changelog (vs 70-11021-51-0):
        * Fixed an issue where an interaction between IMA and NFS could cause deadlock.
    

###  cos-69-10895-91-0

    
    
    Date:           Oct 29, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ff03fe06c0fc35868c5ada1306e9471a48bec9c3)
    Kubernetes:     v1.11.1
    Docker:         v17.03.2
    Changelog (vs 69-10895-85-0):
        * Fixed an issue where an interaction between IMA and NFS could cause deadlock.
        * Fixed a `stackdriver-logging.service` issue observed in Containers on Compute Engine.
        * PCID is now enabled by default when supported by the CPU platform.
    

###  cos-dev-72-11172-0-0

    
    
    Date:           Oct 19, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e6257ccf82e571f6fb995cbcb19abc6eee7423de)
    Kubernetes:     v1.11.3
    Docker:         v18.06.1
    Changelog (vs 71-11147-0-0):
        * New milestone: 72.
        * Fixed an issue where an interaction between IMA and NFS could cause deadlock.
        * PCID is now enabled by default when supported by the CPU platform.
        * Fixed a `stackdriver-logging.service` issue observed in Containers on Compute Engine.
    

###  cos-beta-71-11151-5-0

    
    
    Date:           Oct 19, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/8ed20bc17dd09bc21c934b1cdf1f7ab84ed0a3c8)
    Kubernetes:     v1.11.3
    Docker:         v18.06.1
    Changelog (vs 71-11147-0-0):
        * Promoted to beta channel.
        * PCID is now enabled by default when supported by the CPU platform.
        * Fixed a `stackdriver-logging.service` issue observed in Containers on Compute Engine.
    

###  cos-stable-70-11021-51-0

    
    
    Date:           Oct 19, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f33f40cdd15d5fd1a81f514c66a1272bb11c88ee)
    Kubernetes:     v1.11.3
    Docker:         v18.06.1
    Changelog (vs 70-11021-45-0):
        * Fixed the bug that cloud-init can't write gzipped files.
        * PCID is now enabled by default when supported by the CPU platform.
        * Fixed a `stackdriver-logging.service` issue observed in Containers on Compute Engine.
    

###  cos-dev-71-11147-0-0

    
    
    Date:           Oct 11, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/01b831de9ca23821e1519f1ad1ae89143cc5329d)
    Kubernetes:     v1.11.3
    Docker:         v18.06.1
    Changelog (vs 71-11128-0-0):
        * Fixed bug preventing cloud-init from writing gzipped files.
        * Enabled CONFIG_NET_ACT_MIRRED and CONFIG_NET_ACT_PEDIT.
    

###  cos-beta-70-11021-45-0

    
    
    Date:           Oct 11, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f33f40cdd15d5fd1a81f514c66a1272bb11c88ee)
    Kubernetes:     v1.11.3
    Docker:         v18.06.1
    Changelog (vs 70-11021-39-0):
        * Reset softlockup_all_cpu_backtrace to '0' to avoid kernel deadlock on high
          CPU machines under certain circumstances.
    

###  cos-stable-69-10895-85-0

    
    
    Date:           Oct 11, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/96d6d803ccae172c7a1e9b0f1fee8bcff8894756)
    Kubernetes:     v1.11.1
    Docker:         v17.03.2
    Changelog (vs 69-10895-71-0):
        * Reset softlockup_all_cpu_backtrace to '0' to avoid kernel deadlock on high
          CPU machines under certain circumstances.
    

###  cos-dev-71-11128-0-0

    
    
    Date:           Oct 05, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f7f5708161ab9ec64de9932cb9c82a481e5ac093)
    Kubernetes:     v1.11.3
    Docker:         v18.06.1
    Changelog (vs 71-11104-0-0):
        * Reset softlockup_all_cpu_backtrace to '0' to avoid kernel deadlock on
          high-CPU machines under certain circumstances.
    

###  cos-beta-70-11021-39-0

    
    
    Date:           Oct 05, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f33f40cdd15d5fd1a81f514c66a1272bb11c88ee)
    Kubernetes:     v1.11.3
    Docker:         v18.06.1
    Changelog (vs 70-11021-29-0):
        * Minor changes.
    

###  cos-dev-71-11104-0-0

    
    
    Date:           Sep 27, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/022708b4bb18325353d45733ed9e48850a410b40)
    Kubernetes:     v1.11.3
    Docker:         v18.06.1
    Changelog (vs 71-11074-0-0):
        * Updated toolbox docker container tag '20180918-00'
        * Installed pigz for faster docker image downloads.
        * Update Kubernetes to v1.11.3
    

###  cos-beta-70-11021-29-0

    
    
    Date:           Sep 27, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f33f40cdd15d5fd1a81f514c66a1272bb11c88ee)
    Kubernetes:     v1.11.3
    Docker:         v18.06.1
    Changelog (vs 70-11021-18-0):
        * Updated toolbox docker container tag '20180918-00'
        * Update Kubernetes to v1.11.3
    

###  cos-stable-69-10895-71-0

    
    
    Date:           Sep 27, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/96d6d803ccae172c7a1e9b0f1fee8bcff8894756)
    Kubernetes:     v1.11.1
    Docker:         v17.03.2
    Changelog (vs 69-10895-62-0):
        * Removed userspace headers from kernel header artifact.
    

###  cos-stable-69-10895-62-0

    
    
    Date:           Sep 18, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/96d6d803ccae172c7a1e9b0f1fee8bcff8894756)
    Kubernetes:     v1.11.1
    Docker:         v17.03.2
    Changelog (vs 69-10895-52-0):
        * Minor changes.
    

###  cos-dev-71-11074-0-0

    
    
    Date:           Sep 17, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/a61e41ac7421e1bde52aaf743ca97042423caddb)
    Kubernetes:     v1.11.1
    Docker:         v18.06.1
    Changelog (vs 70-11021-11-0):
        * Minor changes.
    

###  cos-beta-70-11021-18-0

    
    
    Date:           Sep 17, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/79eadab82441a401c52a71497d5f5cf4f001048a)
    Kubernetes:     v1.11.1
    Docker:         v18.06.1
    Changelog (vs 70-11021-11-0):
        * Minor changes.
        * Promoted to beta channel.
    

###  cos-stable-69-10895-52-0

    
    
    Date:           Sep 17, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/96d6d803ccae172c7a1e9b0f1fee8bcff8894756)
    Kubernetes:     v1.11.1
    Docker:         v17.03.2
    Changelog (vs 69-10895-52-0):
        * Promoted to stable channel.
    

###  cos-stable-68-10718-106-0

    
    
    Date:           Sep 13, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e828a46e7038ae7593462e965328bee7ec2570bd)
    Kubernetes:     v1.10.5
    Docker:         v17.03.2
    Changelog (vs 68-10718-102-0):
        * Backported a fix to ensure that scsi contributes to randomness when running
          rotational device (https://chromium-review.googlesource.com/1212547).
          This addresses an issue where docker is slow to start because of
          low entropy on standard PDs since v4.14.63 merge.
    

###  cos-dev-70-11021-11-0

    
    
    Date:           Sep 10, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/c116f2c8c400aea79ed1a11aaf3bf3869d04eb05)
    Kubernetes:     v1.11.1
    Docker:         v18.06.1
    Changelog (vs 70-11021-0-0):
        * Backported a fix to ensure that scsi contributes to randomness when running
          rotational device (https://chromium-review.googlesource.com/1212545).
          This addresses an issue where docker is slow to start because of
          low entropy on standard PDs since v4.14.63 merge.
    

###  cos-beta-69-10895-52-0

    
    
    Date:           Sep 10, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/96d6d803ccae172c7a1e9b0f1fee8bcff8894756)
    Kubernetes:     v1.11.1
    Docker:         v17.03.2
    Changelog (vs 69-10895-42-0):
        * Backported a fix to ensure that scsi contributes to randomness when running
          rotational device (https://chromium-review.googlesource.com/1212546).
          This addresses an issue where docker is slow to start because of
          low entropy on standard PDs since v4.14.63 merge.
    

###  cos-stable-65-10323-104-0

    
    
    Date:           Sep 10, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/71fc76c0715d05a20eb22abfd26d92efc03cc63f)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-99-0):
        * Merge Linux stable kernel 'v4.4.153'.
    

###  cos-dev-70-11021-0-0

    
    
    Date:           Aug 31, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/52c742d7395c35e2bb295f20b3e4390293c67214)
    Kubernetes:     v1.11.1
    Docker:         v18.06.1
    Changelog (vs 69-10895-27-0):
        * Turn on virtio_net.napi_tx.
        * Enabled CONFIG_RANDOM_TRUST_CPU to address entropy starvation on PD-SSD boot disks.
        * Upgraded docker to 18.06.1
        * Upgraded OpenSSL to 1.0.2p
        * Upgraded the ca-certificates package to version 20180409.3.37
    

###  cos-beta-69-10895-42-0

    
    
    Date:           Aug 31, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/6f2926628697156acb33aeca513a9a99b93e0f28)
    Kubernetes:     v1.11.1
    Docker:         v17.03.2
    Changelog (vs 69-10895-27-0):
        * Enabled CONFIG_RANDOM_TRUST_CPU to address entropy starvation on PD-SSD boot disks.
        * Upgraded OpenSSL to 1.0.2p
        * Merged Linux stable version v4.14.65 into the kernel.
    

###  cos-stable-68-10718-102-0

    
    
    Date:           Aug 31, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f5aaf89463119a94471444e29ce12dd49b4d654e)
    Kubernetes:     v1.10.5
    Docker:         v17.03.2
    Changelog (vs 68-10718-86-0):
        * Fixed a softlockup issue that occurred on single VCPU VMs when using FUSE filesystems.
        * Enabled CONFIG_RANDOM_TRUST_CPU to address entropy starvation on PD-SSD boot disks.
        * Merged Linux stable version v4.14.65 into the kernel.
    

###  cos-stable-67-10575-67-0

    
    
    Date:           Aug 24, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/45440158aa19d315ed6aea42f8d12929effdbf49)
    Kubernetes:     v1.10.0
    Docker:         v17.03.2
    Changelog (vs 67-10575-66-0):
        * Backported the fix for a cloud-init bug that write_files can't deal with non-asci content (https://bugs.launchpad.net/bugs/1487877).
    

###  cos-dev-69-10895-27-0

    
    
    Date:           Aug 17, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e7d0ede66eb4efd21bf8935391cc2797f480c15f)
    Kubernetes:     v1.11.1
    Docker:         v17.03.2
    Changelog (vs 69-10895-23-0):
        * Backported the fix for a cloud-init bug that write_files can't deal with non-asci content (https://bugs.launchpad.net/bugs/1487877).
    

###  cos-beta-69-10895-27-0

    
    
    Date:           Aug 17, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e7d0ede66eb4efd21bf8935391cc2797f480c15f)
    Kubernetes:     v1.11.1
    Docker:         v17.03.2
    Changelog (vs 69-10895-23-0):
        * Promoted to beta channel.
        * Backported the fix for a cloud-init bug that write_files can't deal with non-asci content (https://bugs.launchpad.net/bugs/1487877).
    

###  cos-stable-68-10718-86-0

    
    
    Date:           Aug 17, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e73eb2215343df75d060a2cc4b290ebd030b218e)
    Kubernetes:     v1.10.5
    Docker:         v17.03.2
    Changelog (vs 68-10718-81-0):
        * Promoted to stable channel.
        * Backported the fix for a cloud-init bug that write_files can't deal with non-asci content (https://bugs.launchpad.net/bugs/1487877).
    

###  cos-stable-65-10323-99-0

    
    
    Date:           Aug 14, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/9f2ecb7c9cd4b2886853e2feba31f539dde25a4d)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-98-0):
        * Fix for Linux Kernel CVE-2018-12232
        * Backported fixes for L1 Terminal Fault (L1TF) issue (CVE-2018-3615, CVE-2018-3620, and CVE-2018-3646).
    

###  cos-dev-69-10895-23-0

    
    
    Date:           Aug 14, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e7d0ede66eb4efd21bf8935391cc2797f480c15f)
    Kubernetes:     v1.11.1
    Docker:         v17.03.2
    Changelog (vs 69-10895-16-0):
        * Backported fix for a kernel warning "WARNING: fs/overlayfs/readdir.c:393 ovl_iterate+0x25c/0x260 WARN_ON(!cache->refcount)"
        * Fix for Linux Kernel CVE-2018-12232
        * Backported fixes for L1 Terminal Fault (L1TF) issue (CVE-2018-3615, CVE-2018-3620, and CVE-2018-3646).
    

###  cos-beta-68-10718-81-0

    
    
    Date:           Aug 14, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e73eb2215343df75d060a2cc4b290ebd030b218e)
    Kubernetes:     v1.10.5
    Docker:         v17.03.2
    Changelog (vs 68-10718-76-0):
        * Fix for Linux Kernel CVE-2018-12232
        * Backported fixes for L1 Terminal Fault (L1TF) issue (CVE-2018-3615, CVE-2018-3620, and CVE-2018-3646).
    

###  cos-stable-67-10575-66-0

    
    
    Date:           Aug 14, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/45440158aa19d315ed6aea42f8d12929effdbf49)
    Kubernetes:     v1.10.0
    Docker:         v17.03.2
    Changelog (vs 67-10575-65-0):
        * Fix for Linux Kernel CVE-2018-12232
        * Backported fixes for L1 Terminal Fault (L1TF) issue (CVE-2018-3615, CVE-2018-3620, and CVE-2018-3646).
    

###  cos-stable-66-10452-110-0

    
    
    Date:           Aug 14, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/9e8d00792d96e8c0e64845951643889f1a66583b)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10452-109-0):
        * Fix for Linux Kernel CVE-2018-12232
        * Backported fixes for L1 Terminal Fault (L1TF) issue (CVE-2018-3615, CVE-2018-3620, and CVE-2018-3646).
    

###  cos-dev-69-10895-16-0

    
    
    Date:           Aug 07, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/5b91f0bf318cb7c4bbb7ba35d2023119150183c6)
    Kubernetes:     v1.11.1
    Docker:         v17.03.2
    Changelog (vs 69-10895-10-0):
        * Fixes for CVE-2018-5391.
        * Fixed a softlockup issue that occurred on single VCPU VMs when using FUSE filesystems.
        * Updated Kubernetes to v1.11.1
    

###  cos-beta-68-10718-76-0

    
    
    Date:           Aug 07, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2bf666456691e3fa3660ce371b38b3509030a338)
    Kubernetes:     v1.10.5
    Docker:         v17.03.2
    Changelog (vs 68-10718-70-0):
        * Fixes for CVE-2018-5391.
    

###  cos-stable-67-10575-65-0

    
    
    Date:           Aug 07, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/bbe3394dcd24530dd05b2059e7ab7263a07a34c6)
    Kubernetes:     v1.10.0
    Docker:         v17.03.2
    Changelog (vs 67-10575-64-0):
        * Fixes for CVE-2018-5391.
    

###  cos-stable-66-10452-109-0

    
    
    Date:           Aug 07, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/a64d42388743f77dc01fef398d96ffdda96b321b)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10452-108-0):
        * Fixes for CVE-2018-5391.
    

###  cos-stable-65-10323-98-0

    
    
    Date:           Aug 04, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/4df76b6fb22548e5c3c9e646ac3c1cffdaa72740)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-97-0):
        * Fixes for CVE-2018-5391.
    

###  cos-dev-69-10895-10-0

    
    
    Date:           Jul 31, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/3a561f7f69468b6d416dbbc08cef65850b1506ea)
    Kubernetes:     v1.11.0
    Docker:         v17.03.2
    Changelog (vs 69-10895-0-0):
        * Fixes for CVE-2018-5390.
    

###  cos-beta-68-10718-70-0

    
    
    Date:           Jul 31, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/92748bdc35bae574a3b905ca2d58ff86d8b5750f)
    Kubernetes:     v1.10.5
    Docker:         v17.03.2
    Changelog (vs 68-10718-63-0):
        * Fixes for CVE-2018-5390.
    

###  cos-stable-67-10575-64-0

    
    
    Date:           Jul 31, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/dd929865b8ccf9253f743b0a72bfeb9febdf5c54)
    Kubernetes:     v1.10.0
    Docker:         v17.03.2
    Changelog (vs 67-10575-62-0):
        * Fixes for CVE-2018-5390.
    

###  cos-stable-66-10452-108-0

    
    
    Date:           Jul 31, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/88dc785f46183b6e1bc59f6f79a073b824b37013)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10452-107-0):
        * Fixes for CVE-2018-5390.
    

###  cos-stable-65-10323-97-0

    
    
    Date:           Jul 31, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/29e0394967c240a4da6f45459dc71fde02b5328c)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-94-0):
        * Fixes for CVE-2018-5390.
    

###  cos-dev-69-10895-0-0

    
    
    Date:           Jul 25, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/5b9b9e14a8dc9af066375c343ad1a91981462ae2)
    Kubernetes:     v1.11.0
    Docker:         v17.03.2
    Changelog (vs 69-10884-0-0):
        * Minor changes.
    

###  cos-beta-68-10718-63-0

    
    
    Date:           Jul 25, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/52a84cab3bb49e459a20306dd35707a880d7a1bc)
    Kubernetes:     v1.10.5
    Docker:         v17.03.2
    Changelog (vs 68-10718-59-0):
        * Minor changes.
    

###  cos-dev-69-10884-0-0

    
    
    Date:           Jul 20, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/add1502b136ef79c24d15a77918703ecca103a2f)
    Kubernetes:     v1.11.0
    Docker:         v17.03.2
    Changelog (vs 69-10873-0-0):
        * Increase default kernel.pid_max to 2^22.
    

###  cos-beta-68-10718-59-0

    
    
    Date:           Jul 20, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/52a84cab3bb49e459a20306dd35707a880d7a1bc)
    Kubernetes:     v1.10.5
    Docker:         v17.03.2
    Changelog (vs 68-10718-52-0):
        * Minor changes.
    

###  cos-dev-69-10873-0-0

    
    
    Date:           Jul 13, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f9b96ddab2325e0c598edffb2efaadc485c6a3b4)
    Kubernetes:     v1.11.0
    Docker:         v17.03.2
    Changelog (vs 69-10850-0-0):
        * Rebased Kernel to 4.14.54.
    

###  cos-beta-68-10718-52-0

    
    
    Date:           Jul 13, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/52a84cab3bb49e459a20306dd35707a880d7a1bc)
    Kubernetes:     v1.10.5
    Docker:         v17.03.2
    Changelog (vs 68-10718-41-0):
        * Removed SCSI CD-ROM support. This resolves CVE-2018-11506.
        * Updated curl to 7.60.0. This resolves CVE-2018-1000300 and CVE-2018-1000301.
    

###  cos-stable-67-10575-62-0

    
    
    Date:           Jul 16, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/29df4015ccafea31852d4c5f9641804b94b87747)
    Kubernetes:     v1.10.0
    Docker:         v17.03.2
    Changelog (vs 67-10575-57-0):
        * Removed SCSI CD-ROM support. This resolves CVE-2018-11506.
        * Updated curl to 7.60.0. This resolves CVE-2018-1000300 and CVE-2018-1000301.
    

###  cos-stable-66-10452-107-0

    
    
    Date:           Jul 13, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/0e35e889986f5c894db31275ad389ea56171faec)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10452-104-0):
        * Removed SCSI CD-ROM support. This resolves CVE-2018-11506.
        * Updated curl to 7.60.0. This resolves CVE-2018-1000300 and CVE-2018-1000301.
    

###  cos-stable-65-10323-94-0

    
    
    Date:           Jul 13, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/d58a9a62296e94669227df3362396c7f86e550c7)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-91-0):
        * Removed SCSI CD-ROM support. This resolves CVE-2018-11506.
        * Updated curl to 7.60.0. This resolves CVE-2018-1000300 and CVE-2018-1000301.
    

###  cos-dev-69-10850-0-0

    
    
    Date:           Jul 06, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/01d1d6e2a1a74b9b8acba7d5eed67fe83e914aa1)
    Kubernetes:     v1.11.0
    Docker:         v17.03.2
    Changelog (vs 69-10824-0-0):
        * Removed SCSI CD-ROM support. This resolves CVE-2018-11506.
        * Upgraded built-in kubelet to v1.11.0
    

###  cos-beta-68-10718-41-0

    
    
    Date:           Jul 06, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/52a84cab3bb49e459a20306dd35707a880d7a1bc)
    Kubernetes:     v1.10.5
    Docker:         v17.03.2
    Changelog (vs 68-10718-36-0):
        * Upgraded built-in kubelet to v1.10.5
    

###  cos-dev-69-10824-0-0

    
    
    Date:           Jun 28, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/3f04517ba55a44a1477193bdf2d49b6a3a5b5b58)
    Kubernetes:     v1.10.4
    Docker:         v17.03.2
    Changelog (vs 69-10803-0-0):
        * Updated docker-credential-gcr to 1.5.0
    

###  cos-beta-68-10718-36-0

    
    
    Date:           Jun 28, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/74adceb3566ba8187cd4e42144ac8201b5825aab)
    Kubernetes:     v1.10.2
    Docker:         v17.03.2
    Changelog (vs 68-10718-29-0):
        * Minor changes.
    

###  cos-dev-69-10803-0-0

    
    
    Date:           Jun 22, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/dbe258521c5b269bf5c57993c0cb16b5b7434cde)
    Kubernetes:     v1.10.4
    Docker:         v17.03.2
    Changelog (vs 69-10783-0-0):
        * Updated BUG_REPORT_URL in /etc/os-release.
        * Enabled NFS debug configs in the kernel.
        * Enabled tcp_bbr kernel module for TCP congestion control.
        * Upgraded Git to version 2.16.4 to fix CVE 2018-11235.
    

###  cos-beta-68-10718-29-0

    
    
    Date:           Jun 22, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/74adceb3566ba8187cd4e42144ac8201b5825aab)
    Kubernetes:     v1.10.2
    Docker:         v17.03.2
    Changelog (vs 68-10718-23-0):
        * Upgraded Git to version 2.16.4 to fix CVE 2018-11235.
    

###  cos-stable-67-10575-57-0

    
    
    Date:           Jun 22, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/29df4015ccafea31852d4c5f9641804b94b87747)
    Kubernetes:     v1.10.0
    Docker:         v17.03.2
    Changelog (vs 67-10575-55-0):
        * Upgraded Git to version 2.16.4 to fix CVE 2018-11235.
    

###  cos-stable-66-10452-104-0

    
    
    Date:           Jun 22, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/0e35e889986f5c894db31275ad389ea56171faec)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10452-101-0):
        * Upgraded Git to version 2.16.4 to fix CVE 2018-11235.
    

###  cos-stable-65-10323-91-0

    
    
    Date:           Jun 22, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/d58a9a62296e94669227df3362396c7f86e550c7)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-85-0):
        * Upgraded Git to version 2.16.4 to fix CVE 2018-11235.
    

###  cos-dev-69-10783-0-0

    
    
    Date:           Jun 15, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/a32b5bcfd3fe8281a4a42c313c5956b466b51c7c)
    Kubernetes:     v1.10.4
    Docker:         v17.03.2
    Changelog (vs 68-10718-15-0):
        * Set '--disable-legacy-registry' Docker config to true by default.
        * Updated Kubernetes to 1.10.4.
        * Updated sshd_config to drop cbc based Ciphers.
        * Updated root CA certificates to match Mozilla NSS 3.36.1.
        * Updated OpenSSL to 1.0.2o.
    

###  cos-beta-68-10718-23-0

    
    
    Date:           Jun 15, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/0ad8a7d2f842fb181a5730c3a5f50324e9640bec)
    Kubernetes:     v1.10.2
    Docker:         v17.03.2
    Changelog (vs 68-10718-15-0):
        * Promoted to beta channel.
    

###  cos-stable-67-10575-55-0

    
    
    Date:           Jun 15, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/29df4015ccafea31852d4c5f9641804b94b87747)
    Kubernetes:     v1.10.0
    Docker:         v17.03.2
    Changelog (vs 67-10575-54-0):
        * Promoted to stable channel.
    

###  cos-dev-68-10718-15-0

    
    
    Date:           Jun 07, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/dde7de068bf5d70e0aaf6004aefa6fb3731c5541)
    Kubernetes:     v1.10.2
    Docker:         v17.03.2
    Changelog (vs 68-10718-6-0):
        * Minor changes.
    

###  cos-beta-67-10575-54-0

    
    
    Date:           Jun 07, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/29df4015ccafea31852d4c5f9641804b94b87747)
    Kubernetes:     v1.10.0
    Docker:         v17.03.2
    Changelog (vs 67-10575-50-0):
        * Minor changes.
    

###  cos-dev-68-10718-6-0

    
    
    Date:           Jun 01, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/dde7de068bf5d70e0aaf6004aefa6fb3731c5541)
    Kubernetes:     v1.10.2
    Docker:         v17.03.2
    Changelog (vs 68-10714-0-0):
        * Minor changes.
    

###  cos-beta-67-10575-50-0

    
    
    Date:           Jun 01, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/29df4015ccafea31852d4c5f9641804b94b87747)
    Kubernetes:     v1.10.0
    Docker:         v17.03.2
    Changelog (vs 67-10575-45-0):
        * Minor changes.
    

###  cos-stable-66-10452-101-0

    
    
    Date:           Jun 01, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/0e35e889986f5c894db31275ad389ea56171faec)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10452-89-0):
        * Fixed an issue where invoking the `getsockopt` system call would sometimes
        cause the kernel to deadlock.
    

###  cos-dev-68-10714-0-0

    
    
    Date:           May 25, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/421bb018fc1212b132d4b65d5ed3639ab2cd6ce1)
    Kubernetes:     v1.10.2
    Docker:         v17.03.2
    Changelog (vs 68-10690-0-0):
        * Resolved CVE-2017-18258 by upgrading the libxml2 package.
    

###  cos-beta-67-10575-45-0

    
    
    Date:           May 25, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/29df4015ccafea31852d4c5f9641804b94b87747)
    Kubernetes:     v1.10.0
    Docker:         v17.03.2
    Changelog (vs 67-10575-41-0):
        * Resolved CVE-2017-18258 by upgrading the libxml2 package.
    

###  cos-dev-68-10690-0-0

    
    
    Date:           May 18, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/a93f89293f77fff4d0b6e4efdcfd4a972d6ee839)
    Kubernetes:     v1.10.2
    Docker:         v17.03.2
    Changelog (vs 68-10658-0-0):
        * Fixed a go-1.10 incompatibility issue in Docker by backporting https://github.com/moby/moby/commit/a422774.
        * Upgraded Kubernetes to v1.10.2.
    

###  cos-beta-67-10575-41-0

    
    
    Date:           May 18, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/29df4015ccafea31852d4c5f9641804b94b87747)
    Kubernetes:     v1.10.0
    Docker:         v17.03.2
    Changelog (vs 67-10575-32-0):
        * Fixed a go-1.10 incompatibility issue in Docker by backporting https://github.com/moby/moby/commit/a422774.
    

###  cos-dev-68-10658-0-0

    
    
    Date:           May 10, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/1bfb9428ece3c59e591e5c86e965d4af759c0761)
    Kubernetes:     v1.10.1
    Docker:         v17.03.2
    Changelog (vs 68-10644-0-0):
        * Enabled EFI Variable filesystem.
        * Minor fixes.
    

###  cos-beta-67-10575-32-0

    
    
    Date:           May 10, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/29df4015ccafea31852d4c5f9641804b94b87747)
    Kubernetes:     v1.10.0
    Docker:         v17.03.2
    Changelog (vs 67-10575-27-0):
        * Fixes for CVE-2018-1092,CVE-2018-1093,CVE-2018-1094,CVE-2018-1095.
        * Minor changes.
    

###  cos-stable-66-10452-89-0

    
    
    Date:           May 11, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e2e439017d740b3fbe0f4f1a2bc63af84facf535)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10452-81-0):
        * Fixes for CVE-2018-1092,CVE-2018-1093,CVE-2018-1094,CVE-2018-1095.
        * Minor changes.
    

###  cos-stable-65-10323-85-0

    
    
    Date:           May 10, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/d58a9a62296e94669227df3362396c7f86e550c7)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-83-0):
        * Disabled kernel memory accounting.
        * Backported fixes for CVE-2018-1092,CVE-2018-1093,CVE-2018-1094.
    

###  cos-dev-68-10644-0-0

    
    
    Date:           May 04, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/7f86c373d98046cff03f06b6866bc60aaf64a712)
    Kubernetes:     v1.10.1
    Docker:         v17.03.2
    Changelog (vs 68-10615-0-0):
        * Fixes to grub to remove unnecessary modules
        * Minor changes.
    

###  cos-beta-67-10575-27-0

    
    
    Date:           May 04, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e65c4da58924c79671a50757cf6dd741e7a76e4a)
    Kubernetes:     v1.10.0
    Docker:         v17.03.2
    Changelog (vs 67-10575-13-0):
        * Minor changes.
    

###  cos-stable-66-10452-81-0

    
    
    Date:           May 01, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/c2d3cc36e8e7b67bc90f463c8f2d5cf3f33f5d84)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10452-74-0):
        * Backported a fix for Linux kernel CVE-2018-1000199.
    

###  cos-stable-65-10323-83-0

    
    
    Date:           May 01, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/8de740b7f495a1ce5a7ce216055a5a915ac3c248)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-75-0):
        * Backported a fix for Linux kernel CVE-2018-1000199.
    

###  cos-dev-68-10615-0-0

    
    
    Date:           Apr 25, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/585b872fc447017c51c0c09e3701e501fd1d3149)
    Kubernetes:     v1.10.1
    Docker:         v17.03.2
    Changelog (vs 67-10575-8-0):
        * Updated Kubernetes to v1.10.1.
        * Backported a fix for a Linux kernel race condition that was causing kernel
          panics.
    

###  cos-beta-67-10575-13-0

    
    
    Date:           Apr 25, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/349f1dd378f4409d2c280e175228cd988d2a5099)
    Kubernetes:     v1.10.0
    Docker:         v17.03.2
    Changelog (vs 67-10575-8-0):
        * Promoted to beta channel.
        * Backported a fix for a Linux kernel race condition that was causing kernel
          panics.
    

###  cos-stable-66-10452-74-0

    
    
    Date:           Apr 25, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/1dcd0f0a0f4b0e1d6fee6199832de76bc58482b7)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10452-68-0):
        * Promoted to stable channel.
        * Backported a fix for a Linux kernel race condition that was causing kernel
          panics.
    

###  cos-dev-67-10575-8-0

    
    
    Date:           Apr 20, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/28345a67600476de6f43979ffd2bc0f3e6212dbe)
    Kubernetes:     v1.10.0
    Docker:         v17.03.2
    Changelog (vs 67-10574-0-0):
        * Minor changes.
    

###  cos-beta-66-10452-68-0

    
    
    Date:           Apr 20, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/649c0edc37773a0f5dcb099de52cfac35e11f652)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10452-53-0):
        * Backported a fix for Linux kernel CVE-2018-1068.
    

###  cos-stable-65-10323-75-0

    
    
    Date:           Apr 20, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/58f1195f1c24ee272ffc7b913c268b781483fff1)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-69-0):
        * Backported a fix for Linux kernel CVE-2018-1068.
    

###  cos-dev-67-10574-0-0

    
    
    Date:           Apr 13, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f7e8023df9a7ba3b2028c7a2bbba08a7530761e8)
    Kubernetes:     v1.10.0
    Docker:         v17.03.2
    Changelog (vs 67-10550-0-0):
        * Updated kubernetes to v1.10.0
    

###  cos-beta-66-10452-53-0

    
    
    Date:           Apr 13, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/425ead889365ca91a79ceac96f4270efa926c00b)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10452-45-0):
        * Enabled the fix for a bug in containerd (https://github.com/containerd/containerd/pull/872 - Killing a container's shim process while having an exec attached to it will result in panic error).
    

###  cos-dev-67-10550-0-0

    
    
    Date:           Apr 06, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/6dc6045daa653ab5aa45bb571c21c8f254cb0902)
    Kubernetes:     v1.9.6
    Docker:         v17.03.2
    Changelog (vs 67-10527-0-0):
        * Minor changes.
    

###  cos-beta-66-10452-45-0

    
    
    Date:           Apr 06, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/425ead889365ca91a79ceac96f4270efa926c00b)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10452-28-0):
        * Backported a fix for a bug in containerd that killing a container's shim process while having an exec attached to it will result in panic error (https://github.com/containerd/containerd/pull/872).
    

###  cos-stable-65-10323-69-0

    
    
    Date:           Apr 06, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/94bdaa2af49562e7aba0168cae050911d105f5cb)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-64-0):
        * Backported a fix for a bug in containerd that killing a container's shim process while having an exec attached to it will result in panic error (https://github.com/containerd/containerd/pull/872).
    

###  cos-dev-67-10527-0-0

    
    
    Date:           Mar 29, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/0e6f8e69810b260e8b91dd04d744c174f54b0a7b)
    Kubernetes:     v1.9.6
    Docker:         v17.03.2
    Changelog (vs 67-10505-0-0):
        * Updated kubernetes to v1.9.6.
        * Backported a fix for a bug in containerd that killing a container's shim process while having an exec attached to it will result in panic error (https://github.com/containerd/containerd/pull/872).
        * Updated e2fsprogs to 1.44.0.
    

###  cos-beta-66-10452-28-0

    
    
    Date:           Mar 29, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e61aa5e572c62933c1b0ee9090bae138ce80f149)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10452-21-0):
        * Minor changes.
    

###  cos-stable-65-10323-64-0

    
    
    Date:           Mar 29, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/94bdaa2af49562e7aba0168cae050911d105f5cb)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-62-0):
        * Backported fix for Linux kernel CVE-2018-1065.
    

###  cos-dev-67-10505-0-0

    
    
    Date:           Mar 22, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/c4a03cfbfe50b427b0218d39967efb9a77eeaebc)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10452-13-0):
        * New milestone in dev channel.
        * Updated docker-credential-gcr to v1.4.3.
        * Enabled BPF JIT.
    

###  cos-beta-66-10452-21-0

    
    
    Date:           Mar 22, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/b0902253773310f5a084b731edb9f085f67c50ad)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10452-13-0):
        * Promoted to beta channel.
    

###  cos-stable-65-10323-62-0

    
    
    Date:           Mar 22, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/3574f116f40f1c5a8d959c82231f8ddfbf2ca2a3)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-55-0):
        * Promoted to stable channel.
    

###  cos-dev-66-10452-13-0

    
    
    Date:           Mar 16, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/b0902253773310f5a084b731edb9f085f67c50ad)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10452-8-0):
        * Updated Toolbox container tag to '20180309-00'
    

###  cos-beta-65-10323-55-0

    
    
    Date:           Mar 16, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/703d0b8b228d422c78aee8dc740f69dbffbd2e0f)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-51-0):
        * Minor bugfixes
    

###  cos-dev-66-10452-8-0

    
    
    Date:           Mar 12, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/b0902253773310f5a084b731edb9f085f67c50ad)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10428-0-0):
        * Enable BPF JIT.
        * Minor changes.
    

###  cos-beta-65-10323-51-0

    
    
    Date:           Mar 08, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/d9ab1636c319dd56be1cfef454bf72b9b1aaeed3)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-47-0):
        * Minor changes.
    

###  cos-beta-65-10323-47-0

    
    
    Date:           Mar 01, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/11b313e2b636f7c570636a0eb5807b37f6684b6f)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-39-0):
        * Minor changes.
    

###  cos-dev-66-10428-0-0

    
    
    Date:           Feb 23, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/cc9cec492660a4cbcd202fd6c448f316d006ab63)
    Kubernetes:     v1.9.3
    Docker:         v17.03.2
    Changelog (vs 66-10408-0-0):
        * Enabled IP Virtual Server support in kernel (CONFIG_IP_VS)
        * Updated Kubernetes to v1.9.3.
        * Avoid flooding console with iptables log messages
        * Upgraded bash to version 4.3_p48-r1, which includes a fix for CVE-2016-9401
    

###  cos-beta-65-10323-39-0

    
    
    Date:           Feb 23, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/b0e65df3af6f7d47e782514ea7d4c7f9d00a885b)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-33-0):
        * Avoid flooding console with iptables log messages
        * Upgraded curl to version 7.58.0, which includes a fix for CVE-2018-1000007
    

###  cos-dev-66-10408-0-0

    
    
    Date:           Feb 16, 2018
    Kernel:         [ChromiumOS-4.14](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/608b37ebb1b1b1d110d0b99e6490cbf01417af6d)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 66-10385-0-0):
        * Enable OS Login Guest Environment for Google Compute Engine
        * Updated Linux Kernel to 4.14.
    

###  cos-beta-65-10323-33-0

    
    
    Date:           Feb 15, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ba5e18130468dfd172dd68fee39a56a5f4a5fcad)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-23-0):
        * Minor changes.
    

###  cos-dev-66-10385-0-0

    
    
    Date:           Feb 08, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ec22bec75d68e4bad3328e4155752a45059f7630)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 66-10367-0-0):
        * Updated compute-image-packages to v20180129
    

###  cos-beta-65-10323-23-0

    
    
    Date:           Feb 08, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ea2e18e2077abfa8c0fab8ec0085d5bada10e506)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-12-0):
        * Backported a bugfix for netcat: https://sourceforge.net/p/nc110/code/25/
    

###  cos-dev-66-10367-0-0

    
    
    Date:           Feb 02, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/5b81d145d3719a2167a0bb2475aafd7730c32167)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-1-0):
        * New milestone in dev channel.
        * Updated Toolbox Docker image
        * Updated Kubernetes to v1.8.7
    

###  cos-beta-65-10323-12-0

    
    
    Date:           Feb 02, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2d7de0bde20ae17f934c2a2e44cb24b6a1471dec)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 65-10323-1-0):
        * Promoted to beta channel.
        * Updated Toolbox Docker image
        * Updated Kubernetes to v1.8.7
    

###  cos-stable-64-10176-62-0

    
    
    Date:           Feb 02, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2cbee1af2bec3f32a3ea1d33822efc2e937c1fd1)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 64-10176-60-0):
        * Promoted to stable channel.
    

###  cos-dev-65-10323-1-0

    
    
    Date:           Jan 24, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/3bb47e2cd0a1b7dc769f46ff0e7ee77b80ec9a3e)
    Kubernetes:     v1.8.6
    Docker:         v17.03.2
    Changelog (vs 65-10312-0-0):
        * Increased default kernel.hung_task_timeout_secs to 300 so that COS is more tolerant to occassional PD slowness.
        * Add retries to cloud-init when connecting to Google Compute Engine metadata server.
    

###  cos-beta-64-10176-60-0

    
    
    Date:           Jan 24, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2cbee1af2bec3f32a3ea1d33822efc2e937c1fd1)
    Kubernetes:     v1.8.7
    Docker:         v17.03.2
    Changelog (vs 64-10176-49-0):
        * Updated Kubernetes to v1.8.7
    

###  cos-stable-63-10032-88-0

    
    
    Date:           Jan 19, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/09b49365a3c4f884c48162ffe7c4c73839c2c611)
    Kubernetes:     v1.7.8
    Docker:         v17.03.2
    Changelog (vs 63-10032-71-0):
        * Backported fixes for Linux kernel CVE-2017-16939
    

###  cos-dev-65-10312-0-0

    
    
    Date:           Jan 16, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/7b2e7cbdee72aa4de79dd1e3922719577e1ae7ca)
    Kubernetes:     v1.8.6
    Docker:         v17.03.2
    Changelog (vs 65-10280-0-0):
        * Updated docker-credential-gcr to v1.4.2
        * Fixed an [issue](https://github.com/systemd/systemd/issues/7798) in systemd that leaked inactive units when creating mounts on specific mountpoints.
    

###  cos-beta-64-10176-49-0

    
    
    Date:           Jan 16, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/6e1618e065fc43c33e6dcbcf764aa5a98ef9411d)
    Kubernetes:     v1.8.2
    Docker:         v17.03.2
    Changelog (vs 64-10176-39-0):
        * Fixed an [issue](https://github.com/systemd/systemd/issues/7798) in systemd that leaked inactive units when creating mounts on specific mountpoints.
    

###  cos-dev-65-10280-0-0

    
    
    Date:           Jan 05, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ade4a1c12bfd03ab9fbf9a77f1933faa1c7824a6)
    Kubernetes:     v1.8.6
    Docker:         v17.03.2
    Changelog (vs 64-10176-7-0):
        * Recompiled kernel with [RETPOLINE](https://support.google.com/faqs/answer/7625886?hl=zh-cn) enabled GCC.
        * Updated Kubernetes to v1.8.6.
        * Updated openssl version to 1.0.2n that contains the fix for CVE-2017-3737.
        * Updated rsync version to 3.1.2-r2 that contains the fixes for CVE-2017-17433 and CVE-2017-17434.
    

###  cos-beta-64-10176-39-0

    
    
    Date:           Jan 05, 2018
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/472fce40cc16aa5fd1e724a19c013a3fd597ed27)
    Kubernetes:     v1.8.2
    Docker:         v17.03.2
    Changelog (vs 64-10176-7-0):
        * Promoted to beta channel.
    

###  cos-stable-62-9901-80-0

    
    
    Date:           Dec 15, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/8c29ef0fdecb75284311088ccb0f88c7abd7197f)
    Kubernetes:     v1.7.7
    Docker:         v17.03.2
    Changelog (vs 62-9901-79-0):
        * Backported fixes for CVE-2017-1000405.
        * Include performance fix for KPTI (previously called KAISER).
    

###  cos-stable-63-10032-71-0

    
    
    Date:           Dec 08, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/c4c6234ae4f384ce00819c41b48ca8f6f1fa3ba8)
    Kubernetes:     v1.7.8
    Docker:         v17.03.2
    Changelog (vs 63-10032-62-0):
        * Backported fixes for CVE-2017-1000405.
    

###  cos-beta-63-10032-71-0

    
    
    Date:           Dec 08, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/c4c6234ae4f384ce00819c41b48ca8f6f1fa3ba8)
    Kubernetes:     v1.7.8
    Docker:         v17.03.2
    Changelog (vs 63-10032-62-0):
        * Backported fixes for CVE-2017-1000405.
    

###  cos-stable-63-10032-62-0

    
    
    Date:           Dec 06, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/a0e470c8b3bbe44bf6027cd08e178b9b873a0f7c)
    Kubernetes:     v1.7.8
    Docker:         v17.03.2
    Changelog (vs 63-10032-60-0):
        * Include performance fix for KPTI (previously called KAISER).
    

###  cos-beta-63-10032-62-0

    
    
    Date:           Dec 06, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/a0e470c8b3bbe44bf6027cd08e178b9b873a0f7c)
    Kubernetes:     v1.7.8
    Docker:         v17.03.2
    Changelog (vs 63-10032-60-0):
        * Include performance fix for KPTI (previously called KAISER).
    

###  cos-dev-64-10176-7-0

    
    
    Date:           Dec 07, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/4711637236755daccc29c8bf495046a193f8992c)
    Kubernetes:     v1.8.2
    Docker:         v17.03.2
    Changelog (vs 64-10173-0-0):
        * Backported fixes for CVE-2017-1000405.
        * Include performance fix for KPTI (previously called KAISER).
    

**注意** ：  由于 GCP 虚拟化堆栈的潜在功能衰退， ` cos-dev-64-10173-0-0 `
已被标记为“OBSOLETE”（已作废）。创建新实例时，此映像版本不再可用，任何使用此映像版本创建实例的尝试都将失败。

###  cos-dev-64-10173-0-0

    
    
    Date:           Nov 30, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/6681fbe05e99608e74cc6d4a10327c250ce0c02d)
    Kubernetes:     v1.8.2
    Docker:         v17.03.2
    Changelog (vs 64-10151-0-0):
        * Backported fixes for CVE-2017-16548 and CVE-2017-16994.
    

###  cos-stable-63-10032-60-0

    
    
    Date:           Nov 30, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/eecf1b79631742d2969abeafac85151a3b5f3759)
    Kubernetes:     v1.7.8
    Docker:         v17.03.2
    Changelog (vs cos-beta-63-10032-60-0):
        * Promoted to stable channel.
    

###  cos-beta-63-10032-60-0

    
    
    Date:           Nov 30, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/eecf1b79631742d2969abeafac85151a3b5f3759)
    Kubernetes:     v1.7.8
    Docker:         v17.03.2
    Changelog (vs 63-10032-50-0):
        * Backported fixes for CVE-2017-16548 and CVE-2017-16994.
    

###  cos-dev-64-10151-0-0

    
    
    Date:           Nov 22, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/4a42e979a5cf9cd7cec7bba4fa3858516388599b)
    Kubernetes:     v1.8.2
    Docker:         v17.03.2
    Changelog (vs 64-10133-0-0):
        * Enabled KPTI (previously called KAISER) security feature in kernel
        * Mounted /tmp with noexec option.
        * Updated Kubernetes to v1.8.2
        * Disabled unprivileged use of ebpf syscall.
    

###  cos-beta-63-10032-50-0

    
    
    Date:           Nov 22, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/1a2b454f20e92792b9df2d31223ca16a6379557a)
    Kubernetes:     v1.7.8
    Docker:         v17.03.2
    Changelog (vs 63-10032-40-0):
        * Enabled KPTI (previously called KAISER) security feature in kernel
        * Disabled unprivileged use of ebpf syscall.
    

###  cos-stable-62-9901-79-0

    
    
    Date:           Nov 22, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/520c957f9807937a4cdc977e23edb9524e2b372a)
    Kubernetes:     v1.7.7
    Docker:         v17.03.2
    Changelog (vs 62-9901-78-0):
        * Enabled KPTI (previously called KAISER) security feature in kernel
    

###  cos-stable-62-9901-78-0

    
    
    Date:           Nov 20, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/35b73d1fb74c40cde3eb4b5f841861b3eb2b0007)
    Kubernetes:     v1.7.7
    Docker:         v17.03.2
    Changelog (vs 62-9901-75-0):
        * Backported fixes for CVE-2017-15951
    

###  cos-dev-64-10133-0-0

    
    
    Date:           Nov 16, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/8e70b51a27e27b18038dc8603298fbb4fc105b4e)
    Kubernetes:     v1.7.8
    Docker:         v17.03.2
    Changelog (vs 64-10112-0-0):
        * Backported fixes for CVE-2017-1000254
        * Move storage-driver option from docker.service to daemon.json
    

###  cos-beta-63-10032-40-0

    
    
    Date:           Nov 09, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/894358a0af93890cf277df74d58b461d1d60b587)
    Kubernetes:     v1.7.8
    Docker:         v17.03.2
    Changelog (vs 63-10032-32-0):
        * Backported fixes for CVE-2017-1000254
        * Move storage-driver option from docker.service to daemon.json
        * Move live-restore docker options form docker.service to /etc/docker/daemon.json
    

###  cos-stable-61-9765-89-0

    
    
    Date:           Nov 10, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/b3813349f32f4d6b2e2bd58c5a8a9abcfa508c49)
    Kubernetes:     v1.6.10
    Docker:         v17.03.2
    Changelog (vs 61-9765-79-0):
        * Backported the fix for https://github.com/systemd/systemd/issues/4747 in systemd
        * Enabled kernel softlockup panic at runtime via sysctl instead of at kernel compile time
        * Backported fixes for Linux kernel CVE-2017-1000111 and CVE-2017-1000112
    

###  cos-dev-64-10112-0-0

    
    
    Date:           Nov 09, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/4a42e979a5cf9cd7cec7bba4fa3858516388599b)
    Kubernetes:     v1.7.8
    Docker:         v17.03.2
    Changelog (vs 64-10083-0-0):
        * Enabled kernel softlockup panic at runtime via sysctl instead of at kernel compile time
        * Backported the fix for https://github.com/systemd/systemd/issues/4747 in systemd
        * Patched shadow to allow user names that match the gnu-regex '[a-zA-Z0-9_.][a-zA-Z0-9_.-]{0,30}[a-zA-Z0-9_.$-]?', except fully numeric ones and pure dots
        * Updated compute-image-packages to v20171006
        * Increased Docker log line max size from 16KB to 100kB
        * Backported fixes for Linux kernel CVE-2017-15299, CVE-2017-12192, and CVE-2017-15537
        * Bugfix for Containers on Compute Engine (Alpha)
    

###  cos-beta-63-10032-32-0

    
    
    Date:           Nov 09, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/8c00dce331d4156650ce51ac5176484f3cb811cf)
    Kubernetes:     v1.7.8
    Docker:         v17.03.2
    Changelog (vs 63-10032-22-0):
        * Backported the fix for https://github.com/systemd/systemd/issues/4747 in systemd
        * Patched shadow to allow user names that match the gnu-regex '[a-zA-Z0-9_.][a-zA-Z0-9_.-]{0,30}[a-zA-Z0-9_.$-]?', except fully numeric ones and pure dots
        * Enabled kernel softlockup panic at runtime via sysctl instead of at kernel compile time
        * Backported fixes for Linux kernel CVE-2017-15299, CVE-2017-12192, and CVE-2017-15537
        * Bugfix for Containers on Compute Engine (Alpha)
    

###  cos-stable-62-9901-75-0

    
    
    Date:           Nov 09, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/957c2ec5c7b906973b8bf5be3dd066524569b1ec)
    Kubernetes:     v1.7.7
    Docker:         v17.03.2
    Changelog (vs 62-9901-59-0):
        * Backported the fix for https://github.com/systemd/systemd/issues/4747 in systemd
        * Enabled kernel softlockup panic at runtime via sysctl instead of at kernel compile time
        * Backported fixes for Linux kernel CVE-2017-1000111 and CVE-2017-1000112
    

###  cos-dev-64-10083-0-0

    
    
    Date:           Oct 31, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/df5e860a0205bd52f1ca3ba2dea2ec35add3e1b4)
    Kubernetes:     v1.7.8
    Docker:         v17.03.2
    Changelog (vs 63-10032-4-0):
        * New milestone in dev channel
        * Reduce VM boot time by setting grub timeout to zero.
        * Upgrade Kubernetes to v1.7.8
        * Move live-restore docker options from docker.service to /etc/docker/daemon.json
    

###  cos-beta-63-10032-22-0

    
    
    Date:           Oct 31, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/72d0ea281b0b44399e79bd24a33692c8872d81c4)
    Kubernetes:     v1.7.8
    Docker:         v17.03.2
    Changelog (vs 63-10032-4-0):
        * Promoted to beta channel.
        * Upgrade Kubernetes to v1.7.8.
    

###  cos-stable-62-9901-59-0

    
    
    Date:           Oct 31, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e987f76b729ae849552e35a29f1ceb0b049725ea)
    Kubernetes:     v1.7.7
    Docker:         v17.03.2
    Changelog (vs 62-9901-50-0):
        * Promoted to stable channel.
        * Upgrade Curl to v7.55.1.
    

###  cos-dev-63-10032-4-0

    
    
    Date:           Oct 19, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/8f0f11eecfddc49d9544ba6417bef9fb0010465a)
    Kubernetes:     v1.7.7
    Docker:         v17.03.2
    Changelog (vs 63-10022-0-0):
        * Minor changes
    

###  cos-beta-62-9901-50-0

    
    
    Date:           Oct 19, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/a278f49b51f7511b8a91a4a2f238182f65b674db)
    Kubernetes:     v1.7.7
    Docker:         v17.03.2
    Changelog (vs 62-9901-45-0):
        * Minor changes
    

###  cos-beta-62-9901-45-0

    
    
    Date:           Oct 12, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/cedb28682000cd98bf9bf0de155ef06c7a9d6e4a)
    Kubernetes:     v1.7.7
    Docker:         v17.03.2
    Changelog (vs 62-9901-37-0):
        * Upgraded Kubernetes to v1.7.7.
    

###  cos-dev-63-10022-0-0

    
    
    Date:           Oct 11, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/b04db86fe9aeac1b9c7dd74bcb31ef8d911e2213)
    Kubernetes:     v1.7.7
    Docker:         v17.03.2
    Changelog (vs 63-10004-0-0):
        * Upgraded e2fsprogs to v1.43.6
    

###  cos-stable-60-9592-100-0

    
    
    Date:           Oct 06, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ffd9a4db8e11e5007d2309dbf14495b4cdb1158e)
    Kubernetes:     v1.6.4
    Docker:         v1.13.1
    Changelog (vs 60-9592-95-0):
        * Fix for Linux Kernel CVE-2017-12146
    

###  cos-stable-61-9765-79-0

    
    
    Date:           Oct 6, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/a99ba8d3e62114115144713be9df5e2b129e61d6)
    Kubernetes:     v1.6.10
    Docker:         v17.03.2
    Changelog (vs 61-9765-66-0):
        * Fix for Linux Kernel CVE-2017-12146
    

###  cos-beta-62-9901-37-0

    
    
    Date:           Oct 5, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/c85eb265363ceeaf3a09a1f27efd14df023b12fd)
    Kubernetes:     v1.7.6
    Docker:         v17.03.2
    Changelog (vs 62-9901-21-0):
        * Minor changes
    

###  cos-dev-63-10004-0-0

    
    
    Date:           Oct 5, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2b6395d9d63488ac2825a67a7178671c936808c4)
    Kubernetes:     v1.7.7
    Docker:         v17.03.2
    Changelog (vs 63-9975-0-0):
        * Upgraded Kubernetes to v1.7.7.
    

###  cos-dev-63-9975-0-0

    
    
    Date:           Sep 28, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/0452e344f3e5b72e69a6499b349a2b770e953699)
    Kubernetes:     v1.7.6
    Docker:         v17.03.2
    Changelog (vs 63-9956-0-0):
        * Fix for Linux Kernel CVE-2017-11600
    

###  cos-dev-63-9956-0-0

    
    
    Date:           Sep 20, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/d12a16ab1aa0bb0cfe440581924e940eb6ab4206)
    Kubernetes:     v1.7.6
    Docker:         v17.03.2
    Changelog (vs 62-9901-8-0):
        * Upgraded Kubernetes package to v1.7.6
        * Enabled CONFIG_IFB as module
        * Enabled support for eBPF syscall
    

###  cos-beta-62-9901-21-0

    
    
    Date:           Sep 20, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/64e357f9622e67c02a8d66d7d3f8f1001ce07571)
    Kubernetes:     v1.7.6
    Docker:         v17.03.2
    Changelog (vs 62-9901-8-0):
        * Promoted to beta channel
        * Upgraded Kubernetes package to v1.7.6
    

###  cos-stable-61-9765-66-0

    
    
    Date:           Sep 18, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/01693b885a081b92a166f9492e4ae712f08ac1a9)
    Kubernetes:     v1.6.10
    Docker:         v17.03.2
    Changelog (vs 61-9765-50-0):
        * Mitigated a [potential performance regression](https://github.com/kubernetes/kubernetes/issues/50703)
          in Kubernetes by adding a temporary experimental flag to docker daemon
          that allows disabling docker healthchecks. This does not affect
          non-Kubernetes use cases.
        * Upgraded dev-vcs/git package to 2.13.5 in order to fix CVE-2017-1000117.
    

###  cos-stable-60-9592-95-0

    
    
    Date:           Sep 18, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/92105e8327f908198e242b5c66cecd30b948b6d7)
    Kubernetes:     v1.6.4
    Docker:         v1.13.1
    Changelog (vs 60-9592-90-0):
        * Upgraded dev-vcs/git package to 2.13.5 in order to fix CVE-2017-1000117.
    

###  cos-beta-61-9765-58-0

    
    
    Date:           Sep 08, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f8849f297fcbacd190de33ef50f68138a289f892)
    Kubernetes:     v1.6.9
    Docker:         v17.03.2
    Changelog (vs 61-9765-50-0):
        * Mitigated a [potential performance regression](https://github.com/kubernetes/kubernetes/issues/50703)
          in Kubernetes by adding a temporary experimental flag to docker daemon
          that allows disabling docker healthchecks. This does not affect
          non-Kubernetes use cases.
    

###  cos-dev-62-9901-8-0

    
    
    Date:           Sep 08, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/de32fb4df33564df567473b2c9989dcc97ad0648)
    Kubernetes:     v1.7.2
    Docker:         v17.03.2
    Changelog (vs 62-9901-0-0):
        * Minor changes
    

###  cos-dev-62-9901-0-0

    
    
    Date:           Sep 01, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f34a195f353849b9b1d3c231e0d571a8cd4cbfe6)
    Kubernetes:     v1.7.2
    Docker:         v17.03.2
    Changelog (vs 62-9874-0-0):
        * Mitigated a [potential performance regression](https://github.com/kubernetes/kubernetes/issues/50703)
          in Kubernetes by adding a temporary experimental flag to docker daemon
          that allows disabling docker healthchecks. This does not affect
          non-Kubernetes use cases.
        * Upgraded dev-python/prettytable to version 0.7.2. This fixes an issue seen
          in cloud-init
    

###  cos-beta-61-9765-50-0

    
    
    Date:           Sep 01, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/b391a00495de043ef9605da3a5cee4578e544ff5)
    Kubernetes:     v1.6.9
    Docker:         v17.03.2
    Changelog (vs 61-9765-31-0):
        * Upgraded kubernetes to 1.6.9
        * Backported https://golang.org/cl/53635 which resolved the incompatibility
          in tar files generated between Go 1.7 and Go 1.8
        * Backported Linux kernel fix https://patchwork.kernel.org/patch/9882431/
    

###  cos-stable-60-9592-90-0

    
    
    Date:           Sep 01, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/c0dda75c2c06905ff4a2e8b41de27d4f2d773856)
    Kubernetes:     v1.6.4
    Docker:         v1.13.1
    Changelog (vs 60-9592-84-0):
        * Fix for Linux Kernel CVE-2017-10661
        * Backported https://golang.org/cl/53635 which resolved the incompatibility
          in tar files generated between Go 1.7 and Go 1.8
    

###  cos-dev-62-9874-0-0

    
    
    Date:           Aug 24, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/797702bdfae89441b69f1e50661b310492268928)
    Kubernetes:     v1.7.2
    Docker:         v17.03.2
    Changelog (vs 62-9851-0-0):
        * Alpha support for Containers on Compute Engine.
    

###  cos-dev-62-9851-0-0

    
    
    Date:           Aug 17, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/432a134c29bc1205c64a65c0e18f8af2fee2acf2)
    Kubernetes:     v1.7.2
    Docker:         v17.03.2
    Changelog (vs 62-9831-0-0):
        * Cherrypicked upstream kernel change https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=6e7bc478c9a006c701c14476ec9d389a484b4864
        * Cherrypicked upstream Go language change https://go.googlesource.com/go/+/01e45c736882754ca785b5a802ec0866a6544f8b
    

###  cos-beta-61-9765-31-0

    
    
    Date:           Aug 17, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f64189f5892631ee7e731426b708445a3f68542f)
    Kubernetes:     v1.6.7
    Docker:         v17.03.2
    Changelog (vs 61-9765-24-0):
        * Fix for Linux Kernel CVE-2017-7533
    

###  cos-stable-60-9592-84-0

    
    
    Date:           Aug 17, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/30321742b4e00c2250c21bb15f64cb23fa443c74)
    Kubernetes:     v1.6.4
    Docker:         v1.13.1
    Changelog (vs 60-9592-82-0):
        * Fix for Linux Kernel CVE-2017-7533
    

###  cos-dev-62-9831-0-0

    
    
    Date:           Aug 11, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/73ed5e4a867572a4da19e5d8f97161fe5b1cd012)
    Kubernetes:     v1.7.2
    Docker:         v17.03.2
    Changelog (vs cos-dev-62-9785-0-0):
        * Disabled HPN support in OpenSSH so that Compute Engine's SSH-from-browser
          feature is compatible with Container-Optimized OS instances.
        * Upgraded Kubernetes to v1.7.2
        * Fixed systemd-resolved CVE-2017-9445
        * Backported kernel fixes for CVE-2017-11473, CVE-2017-11472, CVE-2017-7542,
          and CVE-2017-7533.
    

###  cos-beta-61-9765-24-0

    
    
    Date:           Aug 11, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/90b18e47a6433aac7f67ba26d26dca18774f15fb)
    Kubernetes:     v1.6.7
    Docker:         v17.03.2
    Changelog (vs cos-beta-61-9765-17-0):
        * Disabled HPN support in OpenSSH so that Compute Engine's SSH-from-browser
          feature is compatible with Container-Optimized OS instances.
        * Backported a few systemd-resolved fixes for alloc size calculation (fixes
          CVE-2017-9445)
    

###  cos-stable-60-9592-82-0

    
    
    Date:           Aug 11, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/8abd14de68dda5071b7624c96a86060219a4b272)
    Kubernetes:     v1.6.4
    Docker:         v1.13.1
    Changelog (vs cos-stable-60-9592-76-0):
        * Backported a few systemd-resolved fixes for alloc size calculation (fixes
          CVE-2017-9445)
    

###  cos-dev-62-9785-0-0

    
    
    Date:           Aug 04, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ab2d669e3aa15afd2dd379cd4079584c21f49c70)
    Kubernetes:     v1.6.4
    Docker:         v17.03.2
    Changelog (vs 61-9765-17-0):
        * New milestone in dev channel
        * Minor bugfixes
    

###  cos-beta-61-9765-17-0

    
    
    Date:           Aug 04, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/1339e618dcd8d09ed028b2ee9442355fd3e9d5ca)
    Kubernetes:     v1.6.7
    Docker:         v17.03.2
    Changelog (vs 61-9765-8-0):
        * Promoted to beta
        * Upgraded Kubernetes to v1.6.7
    

###  cos-stable-60-9592-76-0

    
    
    Date:           Aug 04, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/4504f6dcbb0829cd4590a0cbfd1c6ec4a9642b7b)
    Kubernetes:     v1.6.4
    Docker:         v1.13.1
    Changelog (vs 60-9592-70-0):
        * Promoted to stable
        * Minor bugfixes
    

###  cos-dev-61-9765-8-0

    
    
    Date:           Jul 27, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/b20dc626222db5d048cc331d74cbc7691f09e968)
    Kubernetes:     v1.6.4
    Docker:         v17.03.2
    Changelog (vs 61-9759-0-0):
        * Fixed build issues with open source codebase
    

###  cos-beta-60-9592-70-0

    
    
    Date:           Jul 27, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/4504f6dcbb0829cd4590a0cbfd1c6ec4a9642b7b)
    Kubernetes:     v1.6.4
    Docker:         v1.13.1
    Changelog (vs 60-9592-65-0):
        * Updated sys-apps/coreutils to 8.25. Greatly reduced number of syscalls `du` makes and improved kubelet performance
    

###  cos-beta-60-9592-65-0

    
    
    Date:           Jul 20, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/4504f6dcbb0829cd4590a0cbfd1c6ec4a9642b7b)
    Kubernetes:     v1.6.4
    Docker:         v1.13.1
    Changelog (vs 60-9592-52-0):
        * Fix for Linux kernel CVE-2017-11176
        * Fixed a bug in the `ip sets` command: sometimes valid entries in hash:* types of sets were evicted
    

###  cos-dev-61-9759-0-0

    
    
    Date:           Jul 20, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/c79f8d4233c01ec78ae71547548764aa1c623395)
    Kubernetes:     v1.6.4
    Docker:         v17.03.2
    Changelog (vs 61-9733-0-0):
        * Updated sys-apps/coreutils to 8.25. Greatly reduced number of syscalls `du` makes and improved kubelet performance
        * Updated dev-go/dbus to use upstream commit bd29ed602e2c
        * Fix for Linux kernel CVE-2017-11176
    

###  cos-stable-59-9460-73-0

    
    
    Date:           Jul 14, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e6c7193d61d7affc144ad703b74524ddd574d2ee)
    Kubernetes:     v1.6.4
    Docker:         v1.11.2
    Changelog (vs 59-9460-64-0):
        * Fix for Linux kernel CVE-2017-1000364
        * Fix for Linux kernel CVE-2017-1000365
        * Fix for Linux kernel CVE-2017-1000370
        * Fix for Linux kernel CVE-2017-1000371
        * Fix for Linux kernel CVE-2017-1000379
        * Fix for glibc CVE-2017-1000366
    

###  cos-dev-61-9733-0-0

    
    
    Date:           Jul 11, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/28066af425ed7a348bb083933b79ee8e9e5ad80f)
    Kubernetes:     v1.6.4
    Docker:         v17.03.2
    Changelog (vs 61-9715-0-0):
        * Upgraded Docker to v17.03.2
        * Fixed a bug in the `ip sets` command: sometimes valid entries in hash:* types of sets were evicted
        * Fix for Linux kernel CVE-2017-1000364
    

###  cos-beta-60-9592-52-0

    
    
    Date:           Jul 11, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/7f2f4ec356e8eb3d34127bc12c6396fe0f9c9935)
    Kubernetes:     v1.6.4
    Docker:         v1.13.1
    Changelog (vs 60-9592-31-0):
        * Fix for Linux kernel CVE-2017-1000364
        * Fix for Linux kernel CVE-2017-1000365
        * Fix for Linux kernel CVE-2017-1000370
        * Fix for Linux kernel CVE-2017-1000371
        * Fix for Linux kernel CVE-2017-1000379
        * Fix for glibc CVE-2017-1000366
    

###  cos-dev-61-9715-0-0

    
    
    Date:           Jul 05, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/53013b900b5e6e8cc550655e1265160e19223395)
    Kubernetes:     v1.6.4
    Docker:         v17.03.1
    Changelog (vs 61-9696-0-0):
        * Fixed a regression in cos-dev builds starting with 61-9655-0-0 that caused the image size to grow beyond 10GB.
    

###  cos-dev-61-9696-0-0

    
    
    Date:           Jun 29, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/191dca88b1ed808885143b91265a60b72f87654f)
    Kubernetes:     v1.6.4
    Docker:         v17.03.1
    Changelog (vs 61-9678-0-0):
        * Switched to LLVM compiler
        * Fixed a bug that may lead to the kernel freezing with the following error message: "unregister_netdevice: waiting for lo to become free."
    

###  cos-dev-61-9678-0-0

    
    
    Date:           Jun 26, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/fccc397a120b54273388eb4278ed8febef45f499)
    Kubernetes:     v1.6.4
    Docker:         v17.03.1
    Changelog (vs 61-9655-0-0):
        * Upgraded Docker to v17.03.1
        * Enabled live-restore and overlay2 for Docker by default
        * Updated default toolbox image tag to '20170615-00'
        * Fixed ext4 kernel panic caused by memory shortage in memory cgroup
    

###  cos-beta-60-9592-31-0

    
    
    Date:           Jun 26, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/87e57fe3d0c730becf153126668e883e8bdbe552)
    Kubernetes:     v1.6.4
    Docker:         v1.13.1
    Changelog (vs 60-9592-23-0):
        * Fixed ext4 kernel panic caused by memory shortage in memory cgroup
    

###  cos-dev-61-9655-0-0

    
    
    Date:           Jun 16, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e816096d3b75e5007f26cc3bb7a71696ddd9355e)
    Kubernetes:     v1.6.4
    Docker:         v1.13.1
    Changelog (vs 61-9626-0-0):
        * Disabled the default IP Aliases setting in the Google IP
          Forwarding Daemon
        * Upgraded docker-credential-gcr to v1.4.1
        * kernel: remove sysctl vm.disk_based_swap (default behavior is enabled)
        * Fix for Linux kernel CVE-2017-9075
    

###  cos-beta-60-9592-23-0

    
    
    Date:           Jun 16, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e1feb5b2b5ec536c380bfc4d688b9fa8a1ec072c)
    Kubernetes:     v1.6.4
    Docker:         v1.13.1
    Changelog (vs 60-9592-11-0):
        * Disabled the default IP Aliases setting in the Google IP
          Forwarding Daemon
        * Fix for Linux kernel CVE-2017-9077
        * Fix for Linux kernel CVE-2017-9242
    

###  cos-stable-59-9460-64-0

    
    
    Date:           Jun 16, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/efee0d7cfca9bf17817d7b5d796b56fa75c3b217)
    Kubernetes:     v1.6.4
    Docker:         v1.11.2
    Changelog (vs 59-9460-60-0):
        * Disabled the default IP Aliases setting in the Google IP
          Forwarding Daemon
        * Fix for Linux kernel CVE-2017-9077
        * Fix for Linux kernel CVE-2017-9242
    

###  cos-dev-61-9626-0-0

    
    
    Date:           Jun 8, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/49093717589cfbcf552aa147e95b4f17eba4cff8)
    Kubernetes:     v1.6.4
    Docker:         v1.13.1
    Changelog (vs 60-9592-2-0):
        * New milestone in dev channel
        * Fixed /etc/resolv.conf in toolbox container
        * Upgraded Kubernetes to v1.6.4
        * Support multiple network interfaces that are configured through DHCP
        * Updated to compute-image-packages-20170523
        * Fix for Linux kernel CVE-2017-9077
        * Fix for Linux kernel CVE-2017-9242
    

###  cos-beta-60-9592-11-0

    
    
    Date:           Jun 8, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/29b96e742763422c309e0a054e14b487617195a2)
    Kubernetes:     v1.6.4
    Docker:         v1.13.1
    Changelog (vs 60-9592-2-0):
        * Fixed /etc/resolv.conf in toolbox container
        * Upgraded Kubernetes to v1.6.4
        * Promoted to beta channel
    

###  cos-stable-59-9460-60-0

    
    
    Date:           Jun 8, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e4cd28825ca47cac5cf21fc33a16b4067f91fbd6)
    Kubernetes:     v1.6.4
    Docker:         v1.11.2
    Changelog (vs 59-9460-57-0):
        * Upgraded Kubernetes to v1.6.4
        * Promoted to stable channel
    

###  cos-dev-60-9592-2-0

    
    
    Date:           Jun 1, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/89fb96d5c381a9d7e79bdcd2d1d869a0db2340c3)
    Kubernetes:     v1.6.3
    Docker:         v1.13.1
    Changelog (vs 60-9588-0-0):
        * Minor bugfixes
    

###  cos-beta-59-9460-57-0

    
    
    Date:           Jun 1, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/cbf24c865092fa317c84fdbf3a900020096ebbcb)
    Kubernetes:     v1.6.1
    Docker:         v1.11.2
    Changelog (vs 59-9460-51-0):
        * Minor bugfixes
    

###  cos-dev-60-9588-0-0

    
    
    Date:           May 25, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/49ff6bf77a9772d73653bbb9da369ebbb77740f2)
    Kubernetes:     v1.6.3
    Docker:         v1.13.1
    Changelog (vs 60-9565-0-0):
        * Fix for Linux kernel CVE-2017-8890
        * Fix a bug in CPU scheduler that may lead to kernel panic
    

###  cos-beta-59-9460-51-0

    
    
    Date:           May 25, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/56aedbc2e3a1d7b9795caa19b1988ad924453575)
    Kubernetes:     v1.6.1
    Docker:         v1.11.2
    Changelog (vs 59-9460-43-0):
        * Fix for Linux kernel CVE-2017-8890
    

###  cos-stable-58-9334-74-0

    
    
    Date:           May 25, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/279a539fa270cc84d29072b8506103fd23a8a2cb)
    Kubernetes:     v1.5.6
    Docker:         v1.11.2
    Changelog (vs 58-9334-72-0):
        * Fix for Linux kernel CVE-2017-8890
    

###  cos-stable-57-9202-74-0

（ ` google-containers ` 项目中的 gci-stable-57-9202-74-0）

    
    
    Date:           May 22, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2e530edf318f6b1cbe61e25d8ced8968ae76f99d)
    Kubernetes:     v1.5.4
    Docker:         v1.11.2
    Changelog (vs 57-9202-64-0):
        * Fix for Linux kernel CVE-2017-7895
    

###  cos-dev-60-9565-0-0

    
    
    Date:           May 22, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/6e4fafd29935c844357d317c143164a00dcb1912)
    Kubernetes:     v1.6.3
    Docker:         v1.13.1
    Changelog (vs 60-9540-0-0):
        * Fix for Linux kernel CVE-2017-7895
        * Upgraded Docker to v1.13.1
        * Upgraded Kubernetes to v1.6.3
        * /proc/config.gz available by default (without needed 'modprobe configs')
        * Added support for docker-credential-gcr
          (https://github.com/GoogleCloudPlatform/docker-credential-gcr)
        * Minor bugfix in audit subsystem
    

###  cos-stable-58-9334-72-0

    
    
    Date:           May 18, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/24ac2493b8e042c1e27bbbfcbafa0e4074814b91)
    Kubernetes:     v1.5.6
    Docker:         v1.11.2
    Changelog (vs 58-9334-62-0):
        * Fix for Linux kernel CVE-2017-7895
    

###  cos-beta-59-9460-43-0

    
    
    Date:           May 18, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/6b420e93fafedaed9045df6d5e75913a7a466b04)
    Kubernetes:     v1.6.1
    Docker:         v1.11.2
    Changelog (vs 59-9460-20-0):
        * Fix for Linux kernel CVE-2017-7895
    

###  cos-dev-60-9540-0-0

    
    
    Date:           May 11, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/630aaaf48f4ee3803e754d5548256b44545f774e)
    Kubernetes:     v1.6.1
    Docker:         v1.11.2
    Changelog (vs 60-9504-0-0):
        * Enabled kernel's static hugepage support
        * Enabled DM_THIN_PROVISIONING support
        * Enabled kernel address space layout randomization (KASLR)
        * Ensured cloud-init waits for user-data to become accessible
        * Added new gcr-online.target that can be used to launch tasks when Google
          Container Registry (GCR) becomes accessible on boot
        * Added support for DHCP option 119 (Domain Search List) in systemd
    

###  cos-dev-60-9504-0-0

    
    
    Date:           May 3, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/0a8384cee386f5054d0b6e1ff658c090edfe9f6f)
    Kubernetes:     v1.6.1
    Docker:         v1.11.2
    Changelog (vs 59-9460-11-0):
        * Upgraded Kubernetes to version 1.6.1
        * Upgraded systemd to version 232
        * Upgraded D-Bus to version 1.10.12
        * Promoted to dev channel
    

###  cos-beta-59-9460-20-0

    
    
    Date:           May 3, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/26481563cb3788ad254c2bf2126b843c161c7e48)
    Kubernetes:     v1.6.1
    Docker:         v1.11.2
    Changelog (vs 59-9460-11-0):
        * Upgraded Kubernetes to version 1.6.1
        * Promoted to beta channel
    

###  cos-stable-58-9334-62-0

    
    
    Date:           May 3, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/3b524e9879ea6c804aa271c741109402ec963849)
    Kubernetes:     v1.5.6
    Docker:         v1.11.2
    Changelog (vs 58-9334-56-0):
        * No major changes since the last release
        * Promoted to stable channel
    

###  cos-dev-59-9460-11-0

    
    
    Date:           Apr 27, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/af5357e134ae386b9e9b43e2569ecfc6cc66ba57)
    Kubernetes:     v1.5.4
    Docker:         v1.11.2
    Changelog (vs 59-9460-4-0):
        * No major changes since the last release.
    

###  cos-beta-58-9334-56-0

    
    
    Date:           Apr 27, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/66d3efa3532d2d7a4852fa9578c56a0bc48cdddb)
    Kubernetes:     v1.5.6
    Docker:         v1.11.2
    Changelog (vs 58-9334-53-0):
        * Backported upstream kernel patch for error handling in encrypted ext4 filesystem
    

###  cos-beta-58-9334-53-0

    
    
    Date:           Apr 20, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f7928f617825295a9e7634355243b1037bab3354)
    Kubernetes:     v1.5.6
    Docker:         v1.11.2
    Changelog (vs 58-9334-35-0):
        * Upgraded kubernetes to version 1.5.6
    

###  cos-dev-59-9460-4-0

    
    
    Date:           Apr 20, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/40192ddf4a4701186c8ed2f4f23f6bc27180175e)
    Kubernetes:     v1.5.4
    Docker:         v1.11.2
    Changelog (vs 59-9452-0-0):
        * Fixed the incorrect kernel version shown in image description
        * Fixed the bug wherein journald doesn't persist logs across instance reboot
        * Changed compilation of runc, containerd and docker to dynamically-linked
        * Added support for journald as log driver for Docker containers
        * Run fsck for the stateful partition on every boot
        * Use new JSON file format for Docker configuration in dockercfg_update.sh
    

###  cos-dev-59-9452-0-0

    
    
    Date:           Apr 12, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/9414ec0f0e56f9b4dda673f83b6b8ea875c19b1a)
    Kubernetes:     v1.5.4
    Docker:         v1.11.2
    Changelog (vs 59-9436-0-0):
        * Minor internal implementation changes
    

###  cos-dev-59-9436-0-0

    
    
    Date:           Apr 6, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/66ae58eeed73fd4cac1b4323fab31222589de05f)
    Kubernetes:     v1.5.4
    Docker:         v1.11.2
    Changelog (vs 59-9415-0-0):
        * Cherry-picked fixes for 'gcplogs' log-driver in Docker
          (https://github.com/docker/docker/issues/29344)
        * Enabled KPROBES kernel config so kprobes work
    

###  cos-beta-58-9334-35-0

    
    
    Date:           Apr 6, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/d45255c5542ded7ea1588589e32840dc646f6cb9)
    Kubernetes:     v1.5.4
    Docker:         v1.11.2
    Changelog (vs 58-9334-28-0):
        * Cherry-picked fixes for 'gcplogs' log-driver in Docker
          (https://github.com/docker/docker/issues/29344)
    

###  cos-stable-57-9202-64-0

（ ` google-containers ` 项目中的 gci-stable-57-9202-64-0）

    
    
    Date:           Apr 6, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/74bef1248bcac595d8aec0b58a7ccc0a0fc401a1)
    Kubernetes:     v1.5.4
    Docker:         v1.11.2
    Chaneglog (vs 57-9202-56-0):
        * Fixes for CVE-2017-7184, CVE-2017-7308
        * Cherry-picked fixes for 'gcplogs' log-driver in Docker
          (https://github.com/docker/docker/issues/29344)
    

###  cos-stable-56-9000-104-0

（ ` google-containers ` 项目中的 gci-stable-56-9000-104-0）

    
    
    Date:           Apr 6, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ddf7301a8936c8299989d738bb4ea538b0fa8760)
    Kubernetes:     v1.4.9
    Docker:         v1.11.2
    Changelog (vs 56-9000-103-0)
        * Fixes for CVE-2017-7184, CVE-2017-7308
    

###  cos-stable-56-9000-103-0

（ ` google-containers ` 项目中的 gci-stable-56-9000-103-0）

    
    
    Date:           Apr 3, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/7be5a11bd5fbf3184cd9d9b790830adf1644a256)
    Kubernetes:     v1.4.9
    Docker:         v1.11.2
    Changelog (vs 56-9000-84-2)
        * Updated Kubernetes to v1.4.9
    

###  cos-beta-58-9334-28-0

    
    
    Date:           Mar 31, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/77d0a61c8643fdc0f1b798fa1f17db1362da2ee2)
    Kubernetes:     v1.5.4
    Docker:         v1.11.2
    Changelog (vs 58-9334-19-0):
        * Fixes for CVE-2017-7184, CVE-2017-7308
    

###  cos-dev-59-9415-0-0

    
    
    Date:           Mar 31, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/7e02bef7e3154372ec74e232d8936ad9864a90a5)
    Kubernetes:     v1.5.4
    Docker:         v1.11.2
    Changelog (vs 59-9394-0-0):
        * Upgraded libseccomp to version 2.3.1
        * Upgraded sys-kernel/linux-headers to version 4.4
        * Fixes for CVE-2017-7184, CVE-2017-7308
    

###  cos-stable-57-9202-56-0 回滚

（ ` google-containers ` 项目中的 gci-stable-57-9202-56-0 回滚）

    
    
    Date:           Mar 30, 2017
    Rollback Reason:
        * Identified an issue where using the Docker API from inside a Docker
          container breaks in certain cases.
    

###  cos-dev-59-9394-0-0

    
    
    Date:           Mar 24, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/7adb62f0a1fc5f92b6febb408dc8d69f0c6beaeb)
    Kubernetes:     v1.5.4
    Docker:         v1.11.2
    Changelog (vs 58-9334-11-0):
        * Improved metadata polling in device_policy_manager for lower latency
    

###  cos-beta-58-9334-19-0

    
    
    Date:           Mar 24, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f0b97651dc2e2b60f2b68159427825407876f623)
    Kubernetes:     v1.5.4
    Docker:         v1.11.2
    Changelog (vs 58-9334-11-0):
        * Upgraded kubernetes version to v1.5.4
        * Promoted to beta channel
    

###  cos-stable-57-9202-56-0

（ ` google-containers ` 项目中的 gci-stable-57-9202-56-0）

    
    
    Date:           Mar 24, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/0d8baba41415886419efea6655b4be90219ba86c)
    Kubernetes:     v1.5.4
    Docker:         v1.11.2
    Chaneglog (vs 57-9202-51-0):
        * Upgraded kubernetes version to v1.5.4
        * Promoted to stable channel
    

###  cos-beta-57-9202-51-0

（ ` google-containers ` 项目中的 gci-beta-57-9202-51-0）

    
    
    Date:           Mar  15, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/cfee525e555b7134f253bb6b2059fda6b742fab3)
    Kubernetes:     v1.5.2
    Docker:         v1.11.2
    Changelog (vs 57-9202-38-0)
        * Minor changes
    

###  cos-dev-58-9334-11-0

    
    
    Date:           Mar  15, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f0b97651dc2e2b60f2b68159427825407876f623)
    Kubernetes:     v1.5.2
    Docker:         v1.11.2
    Changelog (vs 58-9333-2-0)
        * Minor changes
    

###  cos-dev-58-9334-2-0

    
    
    Date:           Mar  8, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/03fd4eaa9a4fdd071ddaceae608a6412055b6df4)
    Kubernetes:     v1.5.2
    Docker:         v1.11.2
    Changelog (vs 58-9330-0-0)
        * Fixed double-logging of audit messages
        * Updated compute-image-packages to v20170227
    

###  cos-dev-58-9330-0-0

    
    
    Date:           Mar  3, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/b4e479e3de70a7622e55150806f0800a87f15b2b)
    Kubernetes:     v1.5.2
    Docker:         v1.11.2
    Changelog (vs 58-9312-0-0)
        * Includes 3 network and 1 filesystem backports from upstream kernel
    

###  cos-dev-58-9312-0-0

    
    
    Date:           Feb 24, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/027cb5f503cfe46ee430053acee33e7082517114)
    Kubernetes:     v1.5.2
    Docker:         v1.11.2
    Changelog (vs 58-9289-0-0)
        * Fixed CVE-2017-5551, CVE-2017-5967, CVE-2017-5970.
        * Allowed environment variables EDITOR, LANG, LC_ALL, PAGER, and TZ to be set through ssh.
        * Backported a patch for compute-image-packages to fix high cpu usage.
    

###  cos-beta-57-9202-38-0

（ ` google-containers ` 项目中的 gci-beta-57-9202-38-0）

    
    
    Date:           Feb 24, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/93a19af1a69cf6e8134c04514f6e7614cea1498e)
    Kubernetes:     v1.5.2
    Docker:         v1.11.2
    Changelog (vs 57-9202-38-0)
        * Minor changes.
    

###  cos-dev-58-9289-0-0

    
    
    Date:           Feb 17, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/75e725b8739577bd7da269a8ae380647b5b0425d)
    Kubernetes:     v1.5.2
    Docker:         v1.11.2
    Changelog (vs 57-9202-30-0)
        * device_policy_manager now supports full image name as the value for 'cos-update-strategy'.
        * device_policy_manager now performs channel switch when users try to update to a different channel.
        * Expanded bindmount@.service into .mount units.
        * Removed dependency on Upstart so that systemd is now the init process as PID 1.
        * Added a C.UTF-8 locale and made it default.
        * Moved all COS-specific system services under the cgroup slice '/system.slice/system-sysdaemons.slice/'.
        * Backported fixes for issues identified by KASAN.
    

###  cos-stable-56-9000-84-2

（ ` google-containers ` 项目中的 gci-stable-56-9000-84-2）

    
    
    Date:           Fec 17, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2fdf6034a0fae9794d80e4d218e237771224ba8f)
    Kubernetes:     v1.4.8
    Docker:         v1.11.2
    Changelog (vs 56-9000-84-0)
        * Promoted to stable channel.
        * Backported upstream kernel patches to fix iptables-restore performance regression in 4.4 kernel.
        * Fixed a bug in google-accounts-daemon which causes it to misbehave when network/metadata service becomes unavailable.
    

###  cos-beta-57-9202-30-0

（gci-beta-57-9202-30-0 ` google-containers ` 项目）

    
    
    Date:           Feb 16, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/00ab61fbf51ecae3aac66c88e8bb115e1130a56b)
    Kubernetes:     v1.5.2
    Docker:         v1.11.2
    Changelog (vs 57-9202-26-0)
        * Fixed a bug in google-accounts-daemon which causes it to misbehave when network/metadata service becomes unavailable.
        * Improved handling of missing metadata keys in device_policy_manager.
    

###  cos-dev-57-9202-26-0

（gci-dev-57-9202-26-0 ` google-containers ` 项目）

    
    
    Date:           Feb 13, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e9520b5dc2551b7024918b7bc75f4b1b65f3d162)
    Kubernetes:     v1.5.2
    Docker:         v1.11.2
    Changelog (vs 57-9202-20-0)
        * Backported upstream kernel patches to fix iptables-restore performance regression in 4.4 kernel
    

###  cos-dev-57-9202-20-0

（gci-dev-57-9202-20-0 ` google-containers ` 项目）

    
    
    Date:           Feb 09, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/579137351eb28bb2bb417cb61622d919f545f2cc)
    Kubernetes:     v1.5.2
    Docker:         v1.11.2
    Changelog (vs 57-9196-0-0)
        * Backported the get_metadata_value script from compute-image-packages 1.3.3
        * Changeed ID=gci to ID=cos in /etc/os-release
        * Added support metadata keys with 'cos-' prefix
        * Upgraded kubernetes to 1.5.2
        * Fixed CVE-2016-9962 in runc
        * Backported a few upstream kernel patches that fixed xfstest failures for ext4.
    

###  cos-beta-56-9000-84-0

（ ` google-containers ` 项目中的 gci-beta-56-9000-84-0）

    
    
    Date:           Fec 08, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/b96348ccbec508bf24db93c500acd89668b70e54)
    Kubernetes:     v1.4.8
    Docker:         v1.11.2
    Changelog (vs 56-9000-80-0)
        * Changed ID=gci to ID=cos in /etc/os-release
    

###  cos-stable-55-8872-79-0

（ ` google-containers ` 项目中的 gci-stable-55-8872-79-0）

    
    
    Date:           Feb 03, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/87ac4d46e07460371049e76ea6949566a6aaba0e)
    Kubernetes:     v1.4.6
    Docker:         v1.11.2
    Changelog (vs 55-8872-77-0)
        * Added support metadata keys with 'cos-' prefix
        * Changed ID=gci to ID=cos in /etc/os-release
    

###  cos-beta-56-9000-80-0

（ ` google-containers ` 项目中的 gci-beta-56-9000-80-0）

    
    
    Date:           Jan 31, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/b06c29c53e07da0a84042628a099d5f78b1d5b08)
    Kubernetes:     v1.4.8
    Docker:         v1.11.2
    Changelog (vs 56-9000-76-0)
        * Backported get_metadata_value script
        * Added support metadata keys with 'cos-' prefix
    

###  cos-stable-55-8872-77-0

（ ` google-containers ` 项目中的 gci-stable-55-8872-77-0）

    
    
    Date:           Jan 27, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/87ac4d46e07460371049e76ea6949566a6aaba0e)
    Kubernetes:     v1.4.6
    Docker:         v1.11.2
    Changelog (vs 55-8872-76-0)
        * Fixed CVE-2016-9962 in runc component of Docker
    

###  cos-beta-56-9000-76-0

（ ` google-containers ` 项目中的 gci-beta-56-9000-76-0）

    
    
    Date:           Jan 26, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ebf1eb795f24e43de5c8f96998047208ce2c88bb)
    Kubernetes:     v1.4.8
    Docker:         v1.11.2
    Changelog (vs 56-9000-66-0)
        * Updated Kubernetes to v1.4.8
        * Fix issue where net.ipv4.conf.eth0.forwarding and net.ipv4.ip_forward could
          get reset to 0 on systemd-networkd and/or systemd-sysctl service restart
        * Fixed CVE-2016-9962 in runc component of Docker
    

###  cos-dev-57-9196-0-0

（gci-dev-57-9196-0-0 ` google-containers ` 项目）

    
    
    Date:           Jan 18, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/286200cda473a8f55cd41b165ddf64cbbf90ae5c)
    Kubernetes:     v1.4.6
    Docker:         v1.11.2
    Changelog (vs 57-9102-0-0)
        * kernel: Use kernel default of net.ipv4.ip_forwarding
        * kernel: LSM: fix buffer over-read in printable_cmdline
        * kernel: Merge with stable kernel v4.4.35
        * glibc: roll to 2.23
    

###  gci-beta-56-9000-66-0

    
    
    Date:           Jan 18, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ebf1eb795f24e43de5c8f96998047208ce2c88bb)
    Kubernetes:     v1.4.6
    Docker:         v1.11.2
    Changelog (vs 56-9000-36-0)
        * minor changes
    

###  gci-stable-55-8872-76-0

    
    
    Date:           Jan 18, 2017
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/399336437729a064b06e7c1975f3588c515f0669)
    Kubernetes:     v1.4.6
    Docker:         v1.11.2
    Changelog (vs 55-8872-71-0)
        * minor changes
    

###  gci-dev-56-9000-36-0

    
    
    Date:           Dec 22, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/468e32738c8b296add7bdac971854dfe94102a03)
    Kubernetes:     v1.4.6
    Docker:         v1.11.2
    Changelog (vs 56-9000-21-0)
        * Fixed CVE-2016-7039, CVE-2016-8655, CVE-2016-9793
    

###  gci-dev-57-9102-0-0

    
    
    Date:           Dec 19, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/5d9c4a0af7bfe69ffae39d6aa95deec61ebf3f53)
    Kubernetes:     v1.4.6
    Docker:         v1.11.2
    Changelog (vs 56-9000-21-0):
        * default.target now refers to multi-user.target instead of graphical.target in systemd
        * fixes a bug in systemd that could cause toolbox to terminate unexpectedly
        * Fixed CVE-2016-7039, CVE-2016-8655, CVE-2016-9793
        * other bugfixes
    

###  gci-beta-56-9000-21-0

    
    
    Date:           Dec 15, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/b01f26d5bc74ac26701c523a47a525e16f8aadf7)
    Kubernetes:     v1.4.6
    Docker:         v1.11.2
    Changelog:
        * Promoted to beta from #gci-dev-56-9000-21-0
    

###  gci-stable-55-8872-71-0

    
    
    Date:           Dec 14, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/399336437729a064b06e7c1975f3588c515f0669)
    Kubernetes:     v1.4.6
    Docker:         v1.11.2
    Changelog:
        * Promoted to stable from #gci-beta-55-8872-71-0
    

###  gci-beta-55-8872-71-0

    
    
    Date:           Dec 14, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/399336437729a064b06e7c1975f3588c515f0669)
    Kubernetes:     v1.4.6
    Docker:         v1.11.2
    Changelog (vs 55-8872-70-0)
        * Fixed CVE-2016-7039, CVE-2016-8655, CVE-2016-9793
    

###  gci-beta-55-8872-70-0

    
    
    Date:           Dec 09, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/5aca169e30daa35b14195523d6b937e086d0917d)
    Kubernetes:     v1.4.6
    Docker:         v1.11.2
    Changelog (vs 55-8872-55-0)
        * Enabled BLK_DEV_THROTTLING and process stats accounting config options in kernel
        * Fixed CVE-2015-8964, CVE-2016-6828, CVE-2016-7042, CVE-2016-7097, CVE-2016-7917 and CVE-2016-8666
    

###  gci-dev-56-9000-21-0

    
    
    Date:           Dec 09, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/b01f26d5bc74ac26701c523a47a525e16f8aadf7)
    Kubernetes:     v1.4.6
    Docker:         v1.11.2
    Changelog (vs 56-8977-0-0)
        * Updated Kubernetes to v1.4.6
        * Added compute-image-packages (20160930 release)
        * Enabled BLK_DEV_THROTTLING, BLK_DEV_NVME and process stats accounting config options in kernel
        * Fixed Fixed CVE-2015-8964, CVE-2016-6828, CVE-2016-7042, CVE-2016-7097 and CVE-2016-7917
    

###  gci-stable-54-8743-89-0

    
    
    Date:           Dec 06, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/4303355de7ac578f4c090b163f3947dd8af3996f)
    Kubernetes:     v1.3.10
    Docker:         v1.11.2
    Changelog (vs 54-8743-86-0)
        * Enabled BLK_DEV_THROTTLING kernel config
        * Enabled kernel configs related to process stats accounting
        * Fixed CVE-2015-8964, CVE-2016-6828, CVE-2016-7042, CVE-2016-7097, CVE-2016-7917 and CVE-2016-8666
    

###  gci-beta-55-8872-55-0

    
    
    Date:           Nov 17, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/21832f0a28d144d7fd4301f6a9c91ebd5066eb2f)
    Kubernetes:     v1.4.6
    Docker:         v1.11.2
    Changelog (vs 54-8872-47-0)
        * Updated Kubernetes to v1.4.6
        * Change the product name to 'Container-Optimized OS' in /etc/os-release
    

###  gci-stable-54-8743-86-0

    
    
    Date:           Nov 17, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/68e83d20b0213d9030599255a2b2ea9b61d7f8cb)
    Kubernetes:     v1.3.10
    Docker:         v1.11.2
    Changelog (vs 54-8743-76-0)
        * Updated Kubernetes to v1.3.10
        * Change the product name to 'Container-Optimized OS' in /etc/os-release
    

###  gci-stable-53-8530-102-0

    
    
    Date:           Nov 17, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/d3546e625ae97608e16f19458c7cb6d544f06a1a)
    Kubernetes:     v1.3.9
    Docker:         v1.11.2
    Changelog (vs 53-8530-100-0)
        * Change the product name to 'Container-Optimized OS' in /etc/os-release
    

###  gci-beta-55-8872-47-0

    
    
    Date:           Nov 11, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/8dd2a1e58443e9178738b13d238ca6fe8fe1d11f)
    Kubernetes:     v1.4.5
    Docker:         v1.11.2
    Changelog (vs 55-8872-40-0)
        * Cherry-pick runc PR#608: [Eliminate redundant parsing of mountinfo](https://github.com/opencontainers/runc/pull/608)
    

###  gci-dev-56-8977-0-0

    
    
    Date:           Nov 10, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/e301df29a003db6b8d93732ca801e3c547434860)
    Kubernetes:     v1.4.5
    Docker:         v1.11.2
    Changelog (vs 56-8956-0-0)
        * Cherry-pick runc PR#608: [Eliminate redundant parsing of mountinfo](https://github.com/opencontainers/runc/pull/608)
        * Enabled various kernel modules needed for iptables and conntrack functionality to work correctly.
        * Updated Docker image used by `toolbox` and it now comes with several networking tools pre-installed.
        * Fixed CVE-2016-8666
    

###  gci-beta-55-8872-40-0

    
    
    Date:           Nov 04, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/82eb8c21ab8f0477218d68d86a929c524b89b7ef)
    Kubernetes:     v1.4.5
    Docker:         v1.11.2
    Changelog (vs 55-8872-26-0)
        * Updated kubernetes to v1.4.5
    

###  gci-dev-56-8956-0-0

    
    
    Date:           Nov 03, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/45f5a49ecaedd43d738830e18088e52395c437bb)
    Kubernetes:     v1.4.5
    Docker:         v1.11.2
    Changelog (vs 56-8938-0-0)
        * Updated kubernetes to v1.4.5
    

###  gci-dev-56-8938-0-0

    
    
    Date:           Oct 27, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/67a3c2abbff92d91f14964cae7a5826826a3c5d8)
    Kubernetes:     v1.4.4
    Docker:         v1.11.2
    Changelog (vs 55-8872-18-0)
        * Updated kubernetes to v1.4.4
        * Fixed a bug in e2fsprogs that caused mke2fs to take a very long time. Upstream fix: http://git.kernel.org/cgit/fs/ext2/e2fsprogs.git/commit/?h=next&id=d33e690fe7a6cbeb51349d9f2c7fb16a6ebec9c2
    

###  gci-beta-55-8872-26-0

    
    
    Date:           Oct 26, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/17ce94f76a9ae943f1f3a15ffb043b9b6377c6cf)
    Kubernetes:     v1.4.4
    Docker:         v1.11.2
    Changelog (vs 55-8872-18-0)
        * Updated kubernetes to v1.4.4
        * Fixed a bug in e2fsprogs that caused mke2fs to take a very long time. Upstream fix: http://git.kernel.org/cgit/fs/ext2/e2fsprogs.git/commit/?h=next&id=d33e690fe7a6cbeb51349d9f2c7fb16a6ebec9c2
    

###  gci-stable-54-8743-76-0

    
    
    Date:           Oct 26, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/68e83d20b0213d9030599255a2b2ea9b61d7f8cb)
    Kubernetes:     v1.3.9
    Docker:         v1.11.2
    Changelog (vs 54-8743-71-0)
        * Fixed a bug in e2fsprogs that caused mke2fs to take a very long time. Upstream fix: http://git.kernel.org/cgit/fs/ext2/e2fsprogs.git/commit/?h=next&id=d33e690fe7a6cbeb51349d9f2c7fb16a6ebec9c2
    

###  gci-stable-54-8743-71-0

    
    
    Date:           Oct 21, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/68e83d20b0213d9030599255a2b2ea9b61d7f8cb)
    Kubernetes:     v1.3.9
    Docker:         v1.11.2
    Changelog (vs 54-8743-69-0)
        * Fix for Linux Kernel CVE-2016-5195 (Dirty Cow)
        * Updated kubernetes to v1.3.9
        * Disabled timeout in systemd-networkd-wait-online.service to better deal with network bringup latency observed in some cases
    

###  gci-stable-53-8530-100-0

    
    
    Date:           Oct 20, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/d3546e625ae97608e16f19458c7cb6d544f06a1a)
    Kubernetes:     v1.3.9
    Docker:         v1.11.2
    Changelog (vs 53-8530-85-0)
        * Fix for Linux Kernel CVE-2016-5195 (Dirty Cow)
        * Updated kubernetes to v1.3.9
    

###  gci-dev-55-8872-18-0

    
    
    Date:           Oct 20, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/79629b100ec90058c70d2c3d57a37721b6d93c74)
    Kubernetes:     v1.4.1
    Docker:         v1.11.2
    Changelog (vs 55-8872-16-0)
        * Fix for Linux Kernel CVE-2016-5195 (Dirty Cow)
    

###  gci-beta-54-8743-69-0

    
    
    Date:           Oct 19, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/4e199886207a9667aad8cb83eeec05f2f3cc253e)
    Kubernetes:     v1.3.8
    Docker:         v1.11.2
    Changelog (vs 54-8743-54-0)
        * Minor bugfixes
    

###  gci-dev-55-8872-16-0

    
    
    Date:           Oct 19, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/5d8b5c4ff51097112c48f35a8008a79679a94199)
    Kubernetes:     v1.4.1
    Docker:         v1.11.2
    Changelog (vs 55-8866-0-0)
        * Updated kubernetes to v1.4.1
        * Toolbox started using gcr.io/google-containers/toolbox as base image
        * Enabled FSCACHE, CACHEFILES and NFS_FSCACHE kernel configurations for better NFS support
    

###  gci-dev-55-8866-0-0

    
    
    Date:           Oct 5, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/c357ace7d34415c375dcfb2261d0270956821042)
    Kubernetes:     v1.4.0
    Docker:         v1.11.2
    Changelog (vs 55-8820-0-0)
        * Updated kubernetes to v1.4.0
        * Enabled VXLAN and IP_SET config options in kernel to support some networking tools
        * Patched OpenSSL (CVE-2016-2177, CVE-2016-2178, CVE-2016-2179, CVE-2016-2181, CVE-2016-2182, CVE-2016-6302, CVE-2016-6303)
    

###  gci-beta-54-8743-54-0

    
    
    Date:           Oct 4, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/4e199886207a9667aad8cb83eeec05f2f3cc253e)
    Kubernetes:     v1.3.8
    Docker:         v1.11.2
    Changelog (vs 54-8743-42-0):
        * Updated Kubernetes to v1.3.8
        * Backported OverlayFS fixes from v4.4.21 stable kernel
    

###  gci-stable-53-8530-94-0

    
    
    Date:           Sep 28, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/92c4175adf5d1c7c7ca049e2de23d09814a4fb9d)
    Kubernetes:     v1.3.8
    Docker:         v1.11.2
    Changelog (vs 53-8530-85-0):
        * Fixed performance regression in veth device driver in ChromiumOS kernel
        * Updated Kubernetes to v1.3.8
    

###  gci-dev-55-8820-0-0

    
    
    Date:           Sep 20, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/afdeb0befacc4f4abed41ea4e3e7b6937d38268c)
    Kubernetes:     v1.3.7
    Docker:         v1.11.2
    Changelog:
        * Updated kubernetes to v1.3.7
        * Added ebtables and ethtools
        * Changed the binaries runc, containerd and docker to be statically linked
        * Patched systemd to prevent being OOM-killed when running as PID other than 1
        * Fixed performance regression in veth device driver in ChromiumOS kernel
    

###  gci-beta-54-8743-42-0

    
    
    Date:           Sep 27, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f2ae55cf412350cc9ed2deff8f54a774f77acfdf)
    Kubernetes:     v1.3.7
    Docker:         v1.11.2
    Changelog (vs 54-8743-25-0):
        * Updated Kubernetes to v1.3.7
        * Fixed performance regression in veth device driver in ChromiumOS kernel
        * Patched OpenSSL (CVE-2016-2177, CVE-2016-2178, CVE-2016-2179, CVE-2016-2181, CVE-2016-2182, CVE-2016-6302, CVE-2016-6303)
    

###  gci-beta-54-8743-25-0

    
    
    Date:           Sep 13, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/594f4061708851db1846bf5f5910e4b75a550be7)
    Kubernetes:     v1.3.6
    Docker:         v1.11.2
    Changelog:
        * Promoted release milestone 54 to beta
    

###  gci-stable-53-8530-85-0

    
    
    Date:           Sep 14, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2176eccebe32db8b6db0f33a605fc4466a850571)
    Kubernetes:     v1.3.7
    Docker:         v1.11.2
    Changelog (vs 53-8530-81-0):
        * Updated Kubernetes to v1.3.7
        * Enable marketing name injection for model and name
        * CRAS: bt_device - Associate with adapter's object path
    

###  gci-stable-53-8530-81-0

    
    
    Date:           Sep 8, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/2176eccebe32db8b6db0f33a605fc4466a850571)
    Kubernetes:     v1.3.6
    Docker:         v1.11.2
    Changelog (vs 53-8530-71-0):
        * docker: upgrade go-patricia to fix memory leak ([Docker issue#24420](https://github.com/docker/docker/issues/24420))
        * overlayfs corruption fix ([Kernel commit 45d11738969633ec07ca35d75d486bf2d8918df6](https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=45d11738969633ec07ca35d75d486bf2d8918df6))
    

###  gci-dev-54-8743-3-0

    
    
    Date:           Aug 29, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/b6e7e72f4cf33e6dd28a293c13fb8d35ea0d424d)
    Kubernetes:     v1.3.6
    Docker:         v1.11.2
    Changelog (vs 54-8711-0-0):
        * Updated Kubernetes to v1.3.6.
        * Docker: cherry-pick fix for memory leak in go-patricia
          ([Docker commit 3d714b5ed58cfdfd5872ddd3654d171b09bb02d3](https://github.com/docker/docker/commit/3d714b5ed58cfdfd5872ddd3654d171b09bb02d3))
        * Cloud-Init: execute users-groups before write-files
        * Kernel: make SHA256 the default hash for IMA
    

###  gci-beta-53-8530-71-0

    
    
    Date:           Aug 29, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/fff2f33dbeef1de83cb55b8ed78fdde3ca7ae862)
    Kubernetes:     v1.3.6
    Docker:         v1.11.2
    Changelog (vs gci-beta-53-8530-57-0):
        * Updated Kubernetes to v1.3.6.
    

###  gci-stable-52-8350-75-0

    
    
    Date:           August 25, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/0cda144bc0a167ff1965dd2c98a26495a0c20f1b)
    Kubernetes:     v1.2.6
    Docker:         v1.9.1
    Changelog (vs gci-stable-52-8350-60-0):
        * Fix for a ChromiumOS-specific memory leak in fs/namei.c
    

###  gci-dev-54-8711-0-0

    
    
    Date:           Aug 16, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/a1b32ed254270ecc48c1e2de2228b9f05d3e586b)
    Kubernetes:     v1.3.5
    Docker:         v1.11.2
    Changelog (vs 54-8666-0-0):
        * Updated Kubernetes to v1.3.5.
        * Enable apparmor support by default
        * Enable GCR (Container Registry) mirror
        * Enable bcache as a module
    

###  gci-beta-53-8530-57-0

    
    
    Date:           Aug 15, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/cecc00547a0490d8097e2b0c374b269bb8cb14da)
    Kubernetes:     v1.3.5
    Docker:         v1.11.2
    Changelog (vs gci-beta-53-8530-42-0):
        * Updated Kubernetes to v1.3.5.
        * Users creates by Google accounts manager daemon are automatically added to `docker` group
        * Fixed a filesystem-related memory leak in ChromiumOS kernel
    

###  gci-dev-54-8666-0-0

    
    
    Date:           Aug 3, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/d8bd5ee322c8581f630c1a9e66c570516bbec01b)
    Kubernetes:     v1.3.4
    Docker:         v1.11.2
    Changelog (vs gci-dev-53-8530-29-0):
        * Updated Kubernetes to v1.3.4.
        * Kernel: many unused features were disabled
        * Added apparmor support
        * Enabled seccomp support
        * Kernel updated to 4.4.14
        * Updated 'toolbox' image to 'jessie-backports'
    

###  gci-beta-53-8530-42-0

    
    
    Date:           Aug 3, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/4e62b0fbc077665204a0e15448c4418fc68d184e)
    Kubernetes:     v1.3.4
    Docker:         v1.11.2
    Changelog:
        * Updated Kubernetes to v1.3.4.
    

###  gci-beta-53-8530-40-0

    
    
    Date:           Aug 2, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/4e62b0fbc077665204a0e15448c4418fc68d184e)
    Kubernetes:     v1.3.3
    Docker:         v1.11.2
    Changelog:
        * Promoted release milestone 53 to beta (no code changes vs gci-dev-53-8530-29-0)
    

###  gci-stable-52-8350-60-0

    
    
    Date:           July 28, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/08c7aa38b1691d764cbd2989aec3eb7f46c5f34e)
    Kubernetes:     v1.2.6
    Docker:         v1.9.1
    Changelog:
        * Promoted release milestone 52 to stable (no code changes)
    

###  gci-dev-53-8530-29-0

    
    
    Date:           July 25, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/4e62b0fbc077665204a0e15448c4418fc68d184e)
    Kubernetes:     v1.3.3
    Docker:         v1.11.2
    Changelog:
        * Updated Kubernetes to v1.3.3.
        * Minor bugfix in crash/metrics reporting code.
    

###  gci-beta-52-8350-60-0

    
    
    Date:           July 21, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/08c7aa38b1691d764cbd2989aec3eb7f46c5f34e)
    Kubernetes:     v1.2.6
    Docker:         v1.9.1
    Changelog:
        * Updated Kubernetes to v1.2.6.
    

###  gci-dev-53-8530-20-0

    
    
    Date:           July 18, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/08c7aa38b1691d764cbd2989aec3eb7f46c5f34e)
    Kubernetes:     v1.3.2
    Docker:         v1.11.2
    Changelog:
        * Updated Kubernetes to v1.3.2.
    

###  gci-dev-53-8530-14-0

    
    
    Date:           July 14, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/08c7aa38b1691d764cbd2989aec3eb7f46c5f34e)
    Kubernetes:     v1.3.0
    Docker:         v1.11.2
    Changelog:
        * Minor fixes.
    

###  gci-dev-53-8530-6-0

    
    
    Date:           July 07, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/08c7aa38b1691d764cbd2989aec3eb7f46c5f34e)
    Kubernetes:     v1.3.0
    Docker:         v1.11.2
    Changelog:
        * Updated Kubernetes to v1.3.0
        * Fixed a typo in cloud-init's UID assignment code
        * Enabled NFS server and client support in the kernel
        * Enabled crash and metrics collection daemons (requires user opt-in, see
        [Configuring a Container-VM instance](https://cloud.google.com/compute/docs/containers/vm-image?hl=zh-cn#other_metadata_flags))
    

###  gci-beta-52-8350-45-0

    
    
    Date:           June 28, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/cbe8f4d3550b5313599387b0a25f91325a7141ac)
    Kubernetes:     v1.2.5
    Docker:         v1.9.1
    Changelog:
        * Updated Kubernetes to v1.2.5
    

###  gci-dev-53-8490-0-0

    
    
    Date:           June 23, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ca6177fd6ccff1385a471d6c2de6e8f86e3b2285)
    Kubernetes:     v1.3.0-beta2
    Docker:         v1.11.2
    Changelog:
        * Updated Kubernetes to v1.3.0-beta2
        * Added a systemd service `cloud-audit-setup` to log network connections and binary executions (disabled by default)
    

###  gci-beta-52-8350-39-0

    
    
    Date:           June 23, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ee65ea6da5571323faca2c7d8e45c3286efc814e)
    Kubernetes:     v1.2.4
    Docker:         v1.9.1
    Changelog:
        * Promoted release milestone 52 to beta
        * Started to audit every binary execution
    

###  gci-stable-51-8172-47-0

    
    
    Date:           June 9, 2016
    Kernel:         [ChromiumOS-3.18](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f0ea9e40f2fadd4efee9b0bfe888a71942542538)
    Kubernetes:     v.1.2.4
    Docker:         v1.9.1
    Changelog:
        * Promoted release milestone 51 to stable (no code changes since `gci-beta-51-8172-38-0`)
    

###  gci-dev-52-8352-0-0

    
    
    Date:           May 23, 2016
    Kernel:         [ChromiumOS-4.4](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/ee65ea6da5571323faca2c7d8e45c3286efc814e)
    Kubernetes:     v1.2.4
    Docker:         v1.9.1
    Changelog:
        * Kernel upgraded to v4.4
        * cloud-init: add patch to resolve metadata server locally
        * docker: backport fix for [issue#18113](https://github.com/docker/docker/issues/18113)
        * docker: Add error checks in dockercfg_update.sh
    

###  gci-beta-51-8172-38-0

    
    
    Date:           May 18, 2016
    Kernel:         [ChromiumOS-3.18](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f0ea9e40f2fadd4efee9b0bfe888a71942542538)
    Kubernetes:     v1.2.4
    Docker:         v1.9.1
    Changelog:
        * cloud-init: add patch to resolve metadata server locally
        * docker: backport fix for [issue#18113](https://github.com/docker/docker/issues/18113)
        * docker: Add error checks in dockercfg_update.sh
    

###  gci-dev-52-8300-0-0

    
    
    Date:           May 09, 2016
    Kernel:         [ChromiumOS-3.18](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/b4595d8a0def05c00255be3cb088b1ce8d0cf976)
    Kubernetes:     v1.2.4
    Docker:         v1.9.1
    Changelog:
        * Updated Kubernetes to v1.2.4
        * Fixed device policy file corruption
        * Fixed image license
        * Switched to using grub2
        * Fixed manual rollback
        * Added /etc/os-release file
    

###  gci-beta-51-8172-26-0

    
    
    Date:           May 09, 2016
    Kernel:         [ChromiumOS-3.18](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f0ea9e40f2fadd4efee9b0bfe888a71942542538)
    Kubernetes:     v1.2.4
    Docker:         v1.9.1
    Changelog:
        * Updated Kubernetes to v1.2.4
    

###  gci-stable-50-7978-71-0

    
    
    Date:           May 05, 2016
    Kernel:         [ChromiumOS-3.18](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/6ee79dc904805a4224db14359b1980bef4b2e5d5)
    Kubernetes:     v1.1.8
    Docker:         v1.9.1
    Changelog:
        * Fixed image license
        * Internal cleanup changes
    

###  gci-beta-51-8172-23-0

    
    
    Date:           May 04, 2016
    Kernel:         [ChromiumOS-3.18](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f0ea9e40f2fadd4efee9b0bfe888a71942542538)
    Kubernetes:     v1.2.3
    Docker:         v1.9.1
    Changelog:
        * Fixed image license
        * Fixed device-policy file corruption
    

###  gci-stable-50-7978-62-0

    
    
    Date:           Apr 26, 2016
    Kernel:         [ChromiumOS-3.18](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/98ea42d9ff5021e78029d047f807fc67c1bd39e1)
    Kubernetes:     v1.1.8
    Docker:         v1.9.1
    Changelog:
        * Promoted to Stable channel
        * Fix for CVE-2015-8785
    

###  gci-beta-51-8172-12-0

    
    
    Date:           Apr 26, 2016
    Kernel:         [ChromiumOS-3.18](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/f0ea9e40f2fadd4efee9b0bfe888a71942542538)
    Kubernetes:     v1.2.3
    Docker:         v1.9.1
    Changelog:
        * Promoted to Beta channel
        * Updated Kubernetes to 1.2.3
        * Added kubelet systemd service
        * glibc: backport fix for CVE-2013-7423
        * Fix for CVE-2015-8785
    

###  gci-dev-52-8244-0-0

    
    
    Date:           Apr 26, 2016
    Kernel:         [ChromiumOS-3.18](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/af147c2a385fd8be16ee51b9ad836cd02923197c)
    Kubernetes:     v1.2.3
    Docker:         v1.9.1
    Changelog:
        * Updated Kubernetes to 1.2.3
        * Added kubelet systemd service
        * Fixed /etc/localtime symlink
        * Rixed mount options usage in gci_startup
        * Improved error checks in dockercfg_update.sh
        * Send audit messages to journald
        * glibc: backport fix for CVE-2013-7423
        * Fix for CVE-2015-8785
    

###  gci-dev-51-8168-0-0

    
    
    Date:           Apr 21, 2016
    Kernel:         [ChromiumOS-3.18](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/93922b2968c739687b3079b1fc34889df39a2e36)
    Kubernetes:     v1.2.2
    Docker:         v1.9.1
    Changelog:
        * Bug fixes
    

* * *

###  gci-beta-50-7978-52-0

    
    
    Date:           Apr 11, 2016
    Kernel:         [ChromiumOS-3.18](https://chromium.googlesource.com/chromiumos/third_party/kernel/+/3d397b7064410623cfcd26ff5c545595dd21b66d)
    Kubernetes:     v1.1.8
    Docker:         v1.9.1
    Changelog:
        * Promoted to beta channel
    

