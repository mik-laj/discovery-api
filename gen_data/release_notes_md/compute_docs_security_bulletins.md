#  Security bulletins

From time to time, we might release security bulletins related to Compute
Engine. All security bulletins for Compute Engine are described here.

[ Subscribe to Compute Engine security bulletins. ![Subscribe](/images/feed-
icon.png) ](https://cloud.google.com/feeds/compute-engine-security-
bulletins.xml)

##  Date published: 2020-06-19

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

VMs that have OS Login enabled might be susceptible to privilege escalation
vulnerabilities. These vulnerabilities gives users that are granted OS Login
permissions (but not given admin access) the ability to escalate to root
access in the VM.

####  Vulnerabilities

The following three vulnerabilities, which are due to overly permissive
default group memberships, were identified for Compute Engine images:

  * [ CVE-2020-8903 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8903) : by using the ` adm ` user, it is possible to leverage the DHCP XID to obtain administrative privileges. 
  * [ CVE-2020-8907 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8907) : by using the ` docker ` user, it is possible to mount and modify the host OS filesystem to obtain administrative privileges. 
  * [ CVE-2020-8933 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8933) : by using the ` lxd ` user, it is possible to attach host OS file systems and obtain administrative privileges. 

####  Patched images and fixes

All Compute Engine public images created after ` v20200506 ` are patched.

If you need to fix this issue without updating to a later version of your
image, you can edit the ` /etc/security/group.conf ` file and remove the ` adm
` , ` lxd ` and ` docker ` users from the default OS Login entry.

|  High  |

  * [ CVE-2020-8903 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8903)
  * [ CVE-2020-8907 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8907)
  * [ CVE-2020-8933 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8933)

  
  
##  Date published: 2020-01-21

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

Microsoft disclosed the following vulnerability:

  * [ CVE-2020-0601 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-0601) — This vulnerability is also known as the Windows Crypto API Spoofing Vulnerability and could be exploited to make malicious executables appear trusted or allow the attacker to conduct man-in-the-middle attacks and decrypt confidential information on user connections to the affected software. 

####  Compute Engine impact

The underlying infrastructure that runs Compute Engine is not impacted by this
vulnerability. Unless you are running Windows Server in your Compute Engine
virtual machine, no further action is required. Customers using Compute Engine
VMs running Windows Server should ensure their instances have the latest
Windows patch.

####  Patched images and vendor resources

Earlier versions of the public Windows images do not contain the following
patches and do not mitigate potential attacks:

  * Projects ` windows-cloud ` and ` windows-sql-cloud `
    * All Windows Server and SQL Server public images starting from v20200114 

|  Medium  |

  * [ CVE-2020-0601 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-0601)

  
  
##  Date published: 2019-11-12

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

Intel has disclosed the following CVEs:

  * [ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135) — This CVE is also known as TSX Async Abort (TAA). TAA provides another avenue for data exfiltration using the same microarchitectural data structures that were exploited by Microarchitectural Data Sampling (MDS). 
  * [ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207) — This CVE is also known as "Machine Check Error on Page Size Change." This is a Denial of Service (DoS) vulnerability affecting virtual machine hosts allowing a malicious guest to crash an unprotected host. 

####  Compute Engine impact

#####  CVE-2019-1135

The host infrastructure that runs Compute Engine isolates customer workloads.
Unless you are running untrusted code inside N2, C2, or M2 VMs, no further
action is required.

N2, C2, or M2 customers running untrusted code in their own multi-tenant
services within Compute Engine virtual machines should [ stop and start
](https://cloud.google.com/compute/docs/instances/stop-start-instance) their
VMs in order to ensure they have the latest security mitigations. A reboot,
without a stop/start, is not sufficient. This guidance assumes you have
already applied previously released updates covering the MDS vulnerability. If
not, please [ follow the instructions ](/compute/docs/security-
bulletins#20190514) to apply the appropriate updates.

For customers running N1 machine types, no action is required, as this
vulnerability does not represent new exposure beyond the previously disclosed
MDS vulnerabilities.

#####  CVE-2018-12207

The host infrastructure that runs Compute Engine is protected from this
vulnerability. No further action is required.

|  Medium  |

  * [ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11135)
  * [ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12207)

  
  
##  Date published: 2019-06-18

**last updated: 2019-06-25 T 6:30 PST**

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

Netflix has recently disclosed three TCP vulnerabilities in Linux kernels:

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

These CVEs are collectively referred to as [ NFLX-2019-001
](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-
party/2019-001.md) .

####  Compute Engine impact

The infrastructure that hosts Compute Engine is protected from this
vulnerability.

Compute Engine VMs running unpatched Linux operating systems that send/receive
untrusted network traffic are vulnerable to this DoS attack. Consider updating
these VM instances as soon as patches are available for their operating
systems.

Load balancers that terminate TCP connections have been patched against this
vulnerability. Compute Engine instances that receive only untrusted traffic
through these load balancers are not vulnerable. This includes HTTP Load
Balancers, SSL Proxy Load Balancers, and TCP Proxy Load Balancers.

Network load balancers and internal load balancers do not terminate TCP
connections. Unpatched Compute Engine instances that receive untrusted traffic
through these load balancers are vulnerable.

####  Patched images and vendor resources

We will provide links to patch information from each operating system vendor
here as they become available, including the status for each CVE. Earlier
versions of these public images do not contain these patches and do not
mitigate potential attacks:

  * Project ` debian-cloud ` : 
    * ` debian-9-stretch-v20190618 `
  * Project ` centos-cloud ` : 
    * ` centos-6-v20190619 `
    * ` centos-7-v20190619 `
  * Project ` cos-cloud ` : 
    * ` cos-dev-77-12293-0-0 `
    * ` cos-beta-76-12239-21-0 `
    * ` cos-stable-75-12105-77-0 `
    * ` cos-73-11647-217-0 `
    * ` cos-69-10895-277-0 `
  * Project ` coreos-cloud ` : 
    * ` coreos-alpha-2163-2-1-v20190617 `
    * ` coreos-beta-2135-3-1-v20190617 `
    * ` coreos-stable-2079-6-0-v20190617 `
  * Project ` rhel-cloud ` : 
    * ` rhel-6-v20190618 `
    * ` rhel-7-v20190618 `
    * ` rhel-8-v20190618 `
  * Project ` rhel-sap-cloud ` : 
    * ` rhel-7-4-sap-v20190618 `
    * ` rhel-7-6-sap-v20190618 `
  * Project ` suse-cloud ` : 
    * ` sles-12-sp4-v20190617 `
    * ` sles-15-v20190617 `
  * Project ` suse-sap-cloud ` : 
    * ` sles-12-sp1-sap-v20190617 `
    * ` sles-12-sp2-sap-v20190617 `
    * ` sles-12-sp3-sap-v20190617 `
    * ` sles-12-sp4-sap-v20190617 `
    * ` sles-15-sap-v20190617 `
  * Project ` ubuntu-cloud ` : 
    * ` ubuntu-1604-xenial-v20190617 `
    * ` ubuntu-1804-bionic-v20190617 `
    * ` ubuntu-1810-cosmic-v20190618 `
    * ` ubuntu-1904-disco-v20190619 `
    * ` ubuntu-minimal-1604-xenial-v20190618 `
    * ` ubuntu-minimal-1804-bionic-v20190617 `
    * ` ubuntu-minimal-1810-cosmic-v20190618 `
    * ` ubuntu-minimal-1904-disco-v20190618 `

|  Medium  |

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

  
  
##  Date published: 2019-05-14

**last updated: 2019-05-20 T 17:00 PST**

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

Intel has disclosed the following CVEs:

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

These CVEs are collectively referred to as Microarchitectural Data Sampling
(MDS). These vulnerabilities potentially allow data to be exposed via the
interaction of speculative execution with microarchitectural state.

####  Compute Engine impact

**The host infrastructure that runs Compute Engine isolates customer workloads
from each other. Unless you are running untrusted code inside your VMs, no
further action is required.**

For customers running untrusted code in their own multi-tenant services within
Compute Engine virtual machines, refer to your Guest OS Vendor's recommended
mitigation, which might include using Intel's microcode mitigation features.
We have deployed guest pass-through access to the new flush functionality. The
following is a summary of mitigation steps available for common guest images.

####  Patched images and vendor resources

We will provide links to patch information from each operating system vendor
here as they become available, including status for each CVE. Use these images
to recreate VM instances. Earlier versions of these public images do not
contain these patches and do not mitigate potential attacks:

  * Project ` centos-cloud ` : [ CESA-2019:1169 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023309.html) , [ CESA-2019:1168 ](https://lists.centos.org/pipermail/centos-announce/2019-May/023314.html)
    * ` centos-6-v20190515 `
    * ` centos-7-v20190515 `
  * Project ` coreos-cloud ` : [ MDS mitigations for CoreOS Container Linux ](https://coreos.com/os/docs/latest/disabling-smt.html)
    * ` coreos-stable-2079-4-0-v20190515 `
    * ` coreos-beta-2107-3-0-v20190515 `
    * ` coreos-alpha-2135-1-0-v20190515 `
  * Project ` cos-cloud `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
  * Project ` debian-cloud ` : [ DSA-4444 ](https://www.debian.org/security/2019/dsa-4444)
    * ` debian-9-stretch-v20190514 `
  * Project ` rhel-cloud ` : [ Red Hat MDS Knowledge Article ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-6-v20190515 `
    * ` rhel-7-v20190517 `
    * ` rhel-8-v20190515 `
  * Project ` rhel-sap-cloud ` : [ Red Hat MDS Knowledge Article ](https://access.redhat.com/security/vulnerabilities/mds)
    * ` rhel-7-4-sap-v20190515 `
    * ` rhel-7-6-sap-v20190517 `
  * Project ` suse-cloud ` : [ SUSE MDS KB ](https://www.suse.com/support/kb/doc/?id=7023736)
    * ` sles-12-sp4-v20190520 `
    * ` sles-15-v20190520 `
  * Project ` suse-sap-cloud `
    * ` sles-12-sp4-sap-v20190520 `
    * ` sles-15-sap-v20190520 `
  * Project ` ubuntu-os-cloud ` : [ Ubuntu MDS Wiki ](https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/MDS)
    * ` ubuntu-1404-trusty-v20190514 `
    * ` ubuntu-1604-xenial-v20190514 `
    * ` ubuntu-1804-bionic-v20190514 `
    * ` ubuntu-1810-cosmic-v20190514 `
    * ` ubuntu-1904-disco-v20190514 `
    * ` ubuntu-minimal-1604-xenial-v20190514 `
    * ` ubuntu-minimal-1804-bionic-v20190514 `
    * ` ubuntu-minimal-1810-cosmic-v20190514 `
    * ` ubuntu-minimal-1904-disco-v20190514 `
  * Projects ` windows-cloud ` and ` windows-sql-cloud ` : [ Microsoft ADV190013 ](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/ADV190013)
    * All Windows Server and SQL Server public images with version number ` v20190514 ` . 
  * Project ` gce-uefi-images `
    * ` centos-7-v20190515 `
    * ` cos-69-10895-242-0 `
    * ` cos-73-11647-182-0 `
    * ` rhel-7-v20190517 `
    * ` ubuntu-1804-bionic-v20190514 `
    * All Windows Server public images with version number ` v20190514 ` . 

####  Container-Optimized OS

If you are using Container Optimized OS (COS) as your Guest OS and you are
running untrusted, multi-tenant workloads in your virtual machine, we
recommend that you:

  1. Disable Hyper-Threading by setting ` nosmt ` on the kernel command-line.   

On existing COS VMs, you can modify the ` grub.cfg ` as follows to set the `
nosmt ` option and then reboot the system:

    
        # Run as root:
    dir="$(mktemp -d)"
    mount /dev/sda12 "${dir}"
    sed -i -e "s|cros_efi|cros_efi nosmt|g" "${dir}/efi/boot/grub.cfg"
    umount "${dir}"
    rmdir "${dir}"
    
    reboot

For convenience, you can run the script below to achieve the same result as
running the commands above. We recommend making this script part of your
cloud-config, startup scripts or instance templates, to ensure that new VMs
use this new parameter. An example cloud-config that runs this script is
below.

**Warning:** This command will result in an immediate reboot of the instance
when run for the first time. Subsequent runs of the command on an instance
with Hyper-Threading already disabled will have no effect.

    
        # Run as root
    /bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)
    

To include this as part of your cloud-config:

    
        #cloud-config
    
    bootcmd:
    - /bin/bash -c "/bin/bash <(curl -s https://storage.googleapis.com/cos-tools/scripts/disable_smt.sh)"
    

To confirm if Hyper-Threading is disabled on your instance, look at the output
of ` /sys/devices/system/cpu/smt/active ` and `
/sys/devices/system/cpu/smt/control ` files. If it returns ` 0 ` for ` active
` and ` off ` for ` control ` , Hyper-Threading is disabled:

    
        cat /sys/devices/system/cpu/smt/active
    cat /sys/devices/system/cpu/smt/control
    

**Note:** If you have enabled UEFI Secure Boot on your instance, you will need
to re-create your instance with UEFI Secure Boot disabled, run the above
command with UEFI Secure Boot disabled, and then enable UEFI Secure Boot on
your new instance.

  2. Use new version of COS image   

In addition to disabling Hyper-Threading as described above, you should also [
re-create your instances ](/compute/docs/instances/create-start-
instance#publicimage) with the updated images listed above or newer versions
(when available) of Container-Optimized OS images to get fully protected from
the vulnerability.

|  Medium  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  Date published: 2018-08-14

**last updated: 2018-08-20 T 17:00 PST**

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

[ Intel has disclosed ](https://www.intel.com/content/www/us/en/architecture-
and-technology/l1tf.html) the following CVEs:

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) (for [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (for operating systems and [ SMT ](https://en.wikipedia.org/wiki/Hyper-Threading) ) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (for virtualization) 

These CVEs are collectively referred to as "L1 Terminal Fault (L1TF)".

These L1TF vulnerabilities exploit speculative execution by attacking the
configuration of processor-level data structures. "L1" refers to the Level-1
Data cache (L1D), a small on-core resource used to accelerate memory access.

Read the [ Google Cloud blog post
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities) for more details on these vulnerabilities and
Compute Engine's mitigations.

####  Compute Engine impact

The host infrastructure that runs Compute Engine and isolates customer
workloads from each other is protected against known attacks.

Compute Engine customers are encouraged to update their images to prevent the
possibility of indirect exploitation within their guest environments. This is
particularly important for customers running their own multi-tenant services
on Compute Engine virtual machines.

Compute Engine customers can update the guest operating systems on their
instances using one of the following options:

  * Use patched public images to [ recreate existing VM instances ](https://cloud.google.com/compute/docs/instances/create-start-instance#publicimage) . 
  * On existing instances, install patches provided by the operating system vendor and reboot the patched instances. 

####  Patched images and vendor resources

We will provide links to patch information from each operating system vendor
here as they become available, including status for both CVEs. Use these
images to recreate VM instances. Earlier versions of these public images do
not contain these patches and do not mitigate potential attacks:

  * Project ` centos-cloud ` : 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * Project ` coreos-cloud ` : 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * Project ` cos-cloud ` : 
    * ` cos-stable-66-10452-110-0 `
    * ` cos-stable-67-10575-66-0 `
    * ` cos-beta-68-10718-81-0 `
    * ` cos-dev-69-10895-23-0 `
  * Project ` debian-cloud ` : 
    * ` debian-9-stretch-v20180820 `
  * Project ` rhel-cloud ` : 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * Project ` rhel-sap-cloud ` : 
    * ` rhel-7-sap-apps-v20180814 `
    * ` rhel-7-sap-hana-v20180814 `
  * Project ` suse-cloud ` : 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
    * ` sles-11-sp4-v20180816 `
  * Project ` suse-sap-cloud ` : 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * Project ` ubuntu-os-cloud ` : 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `
  * Projects ` windows-cloud ` ` gce-uefi-images ` and ` windows-sql-cloud ` : 
    * All Windows Server and SQL Server [ public images ](https://cloud.google.com/compute/docs/images#os-compute-support) with version number ` -v201800814 ` and later include patches. 

|  High  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  Date published: 2018-08-06

**last updated: 2018-09-05 T 17:00 PST**

Description  |  Severity  |  Notes  
---|---|---  
  
####  2018-09-05 Update

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) was disclosed on 2018-08-14 by US-CERT. As
with [ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) , this is a kernel-level networking
vulnerability that increases the effectiveness of denial of service (DoS)
attacks against vulnerable systems. The main difference is that CVE-2018-5391
is exploitable over IP connections. We updated this bulletin to cover both
vulnerabilities.

####  Description

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ("SegmentSmack") describes a kernel-level
networking vulnerability that increases the effectiveness of denial of service
(DoS) attacks against vulnerable systems over TCP connections.

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ("FragmentSmack") describes a kernel-level
networking vulnerability that increases the effectiveness of denial of service
(DoS) attacks against vulnerable systems over IP connections.

####  Compute Engine impact

The host infrastructure that runs Compute Engine VMs is not at risk. The
network infrastructure that handles traffic to and from Compute Engine VMs is
protected against this vulnerability. Compute Engine VMs that only
send/receive untrusted network traffic via [ HTTP(S)
](https://cloud.google.com/load-balancing/docs/https/) , [ SSL
](https://cloud.google.com/load-balancing/docs/ssl/) , or [ TCP Load Balancers
](https://cloud.google.com/load-balancing/docs/tcp/) are protected against
this vulnerability.

Compute Engine VMs running unpatched operating systems that send/receive
untrusted network traffic directly, or via [ Network Load Balancers
](https://cloud.google.com/load-balancing/docs/network/) , are vulnerable to
this DoS attack.

Consider updating your VM instances as soon as patches are available for their
operating systems.

Compute Engine customers can update the guest operating systems on their
instances using one of the following options:

  * Use patched public images to [ recreate existing VM instances ](https://cloud.google.com/compute/docs/instances/create-start-instance#publicimage) . See the list of patched public images below. 
  * On existing instances, install patches provided by the operating system vendor and reboot the patched instances. 

####  Patched images and vendor resources

We will provide links to patch information from each operating system vendor
here as they become available.

  * Project ` centos-cloud ` (CVE-2018-5390 only): 
    * ` centos-7-v20180815 `
    * ` centos-6-v20180815 `
  * Project ` coreos-cloud ` (CVE-2018-5390 and CVE-2018-5391): 
    * ` coreos-stable-1800-7-0-v20180816 `
    * ` coreos-beta-1855-2-0-v20180816 `
    * ` coreos-alpha-1871-0-0-v20180816 `
  * Project ` cos-cloud ` (CVE-2018-5390 and CVE-2018-5391): 
    * ` cos-stable-65-10323-98-0 `
    * ` cos-stable-66-10452-109-0 `
    * ` cos-stable-67-10575-65-0 `
    * ` cos-beta-68-10718-76-0 `
    * ` cos-dev-69-10895-16-0 `
  * Project ` debian-cloud ` (CVE-2018-5390 and CVE-2018-5391): 
    * ` debian-9-stretch-v20180814 `
  * Project ` rhel-cloud ` (CVE-2018-5390 only): 
    * ` rhel-7-v20180814 `
    * ` rhel-6-v20180814 `
  * Project ` suse-cloud ` (CVE-2018-5390 and CVE-2018-5391): 
    * ` sles-15-v20180816 `
    * ` sles-12-sp3-v20180814 `
  * Project ` suse-sap-cloud ` (CVE-2018-5390 and CVE-2018-5391): 
    * ` sles-15-sap-v20180816 `
    * ` sles-12-sp3-sap-v20180814 `
    * ` sles-12-sp2-sap-v20180816 `
  * Project ` ubuntu-os-cloud ` (CVE-2018-5390 and CVE-2018-5391): 
    * ` ubuntu-1804-bionic-v20180814 `
    * ` ubuntu-1604-xenial-v20180814 `
    * ` ubuntu-1404-trusty-v20180814 `
    * ` ubuntu-minimal-1804-bionic-v20180814 `
    * ` ubuntu-minimal-1604-xenial-v20180814 `

|  High  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  Date published: 2018-01-03

**last updated: 2018-05-21 T 15:00 PST**

Description  |  Severity  |  Notes  
---|---|---  
  
####  2018-05-21 Update

[ CVE-2018-3640 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-3640) and [ CVE-2018-3639
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639) , Variants 3a
and 4 respectively, were [ disclosed by Intel
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00115.html) . As with the first three variants of Spectre and Meltdown, the
infrastructure that runs Compute Engine VM instances is protected and customer
VM instances are isolated and protected from one another. Additionally,
Compute Engine plans to deploy Intel's microcode patches to our
infrastructure, which will allow customers who run untrusted or multi-tenant
workloads within a single VM instance to enable additional intra-VM
mitigations when those mitigations are provided by operating system vendors
and providers. Compute Engine will deploy the microcode patches once Intel has
certified them and after Compute Engine has tested and qualified the patches
for our production environment. We will provide more detailed timelines and
updates on this page as they become available.

####  Description

These CVEs are variants of a new class of attack that exploit the speculative
execution technology available in many processors. This class of attack can
allow for unauthorized read-only access to memory data under various
circumstances.

Compute Engine used VM Live Migration technology to perform host system and
hypervisor updates with no user impact, no forced maintenance windows, and no
mass reboots required. However, all guest operating systems and versions must
be patched to protect against this new class of attack regardless of where
those systems run.

Read the [ Project Zero blog post
](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-
with-side.html) for complete technical details on this attack method. Read the
[ Google Security blog post ](https://security.googleblog.com/2018/01/todays-
cpu-vulnerability-what-you-need.html) for complete details on Google's
mitigations including all product-specific information.

####  Compute Engine impact

The infrastructure that runs Compute Engine and isolates customer VM instances
from each other is protected against known attacks. Our mitigations prevent
unauthorized access to our host systems from applications running inside VM
instances. These mitigations also prevent unauthorized access between VM
instances running on the same host system.

To prevent unauthorized access within your virtual machine instances, you must
update the guest operating systems on those instances using one of the
following options:

  * Use patched public images to [ recreate your existing VM instances ](https://cloud.google.com/compute/docs/instances/create-start-instance#publicimage) . See the list of patched public images below. 
  * On your existing instances, install patches provided by the operating system vendor for your distribution and reboot the patched instances. See the links to patch information from each operating system vendor below. 

####  Patched images and vendor resources

**Note:** Patched images might not include fixes for all of the CVEs listed in
this security bulletin notice. Additionally, different images might include
different methods for preventing these types of attacks. Check with your
operating system vendor to confirm which CVEs they address in their patches
and what prevention methods they use.

  * Project ` cos-cloud ` : Includes patches that prevent Variant 2 ( [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715) ) and Variant 3 ( [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754) ) attacks. Google used [ Retpoline ](https://support.google.com/faqs/answer/7625886) in these images to mitigate Variant 2 attacks. 
    * ` cos-stable-63-10032-71-0 ` or image family ` cos-stable `
  * Project ` centos-cloud ` : [ CentOS patch information ](https://lwn.net/Alerts/CentOS/)
    * ` centos-7-v20180104 ` or image family ` centos-7 `
    * ` centos-6-v20180104 ` or image family ` centos-6 `
  * Project ` coreos-cloud ` : [ CoreOS patch information ](https://coreos.com/blog/container-linux-meltdown-patch)
    * ` coreos-stable-1576-5-0-v20180105 ` or image family ` coreos-stable `
    * ` coreos-beta-1632-1-0-v20180105 ` or image family ` coreos-beta `
    * ` coreos-alpha-1649-0-0-v20180105 ` or image family ` coreos-alpha `
  * Project ` debian-cloud ` : [ Debian patch information ](https://www.debian.org/security/#DSAS)
    * ` debian-9-stretch-v20180105 ` or image family ` debian-9 `
    * ` debian-8-jessie-v20180109 ` or image family ` debian-8 `
  * Project ` rhel-cloud ` : [ RHEL patch information ](https://access.redhat.com/security/vulnerabilities/speculativeexecution)
    * ` rhel-7-v20180104 ` or image family ` rhel-7 `
    * ` rhel-6-v20180104 ` or image family ` rhel-6 `
  * Project ` suse-cloud ` : [ SUSE patch information ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-v20180104 ` or image family ` sles-12 `
    * ` sles-11-sp4-v20180104 ` or image family ` sles-11 `
  * Project ` suse-sap-cloud ` : [ SUSE patch information ](https://www.suse.com/c/suse-addresses-meltdown-spectre-vulnerabilities/)
    * ` sles-12-sp3-sap-v20180104 ` or image family ` sles-12-sp3-sap `
    * ` sles-12-sp2-sap-v20180104 ` or image family ` sles-12-sp2-sap `
  * Project ` ubuntu-os-cloud ` : [ Ubuntu patch information ](https://insights.ubuntu.com/2018/01/04/ubuntu-updates-for-the-meltdown-spectre-vulnerabilities/)
    * ` ubuntu-1710-artful-v20180109 ` or image family ` ubuntu-1710 `
    * ` ubuntu-1604-xenial-v20180109 ` or image family ` ubuntu-1604-lts `
    * ` ubuntu-1404-trusty-v20180110 ` or image family ` ubuntu-1404-lts `
  * Projects ` windows-cloud ` and ` windows-sql-cloud ` : 
    * All Windows Server and SQL Server [ public images ](https://cloud.google.com/compute/docs/images#os-compute-support) with version number ` -v20180109 ` and later include patches. However, you must follow the recommended actions provided by Microsoft in the [ Windows Server guidance ](https://support.microsoft.com/en-gb/help/4072698/windows-server-guidance-to-protect-against-the-speculative-execution) support bulletin to enable and verify these mitigations on both your existing instances and newly-created instances. 

Use these images to [ recreate your VM instances
](https://cloud.google.com/compute/docs/instances/create-start-
instance#publicimage) . Earlier versions of these public images do not contain
these patches and do not mitigate potential attacks.

####  Patches from hardware vendors

NVIDIA provides patched drivers to mitigate potential attacks against systems
that have NVIDIA® driver software installed. To learn which driver versions
are patched, read the [ NVIDIA GPU Display Driver Security Updates
](http://nvidia.custhelp.com/app/answers/detail/a_id/4611) security bulletin
from NVIDIA.

####  Revision history:

  * 2018-05-21 T 14:00 PST: Added information about 2 new variants disclosed on May 21, 2018. 
  * 2018-01-10 T 15:00 PST: Added information about patched Windows Server and SQL Server public images. 
  * 2018-01-10 T 10:15 PST: Added several Ubuntu images to the list of patched public images. 
  * 2018-01-10 T 09:50 PST: Added guidance for patches from hardware vendors. 
  * 2018-01-03 to 2018-01-09: Made several revisions to the list of patched public images. 

|  High  |

  * [ CVE-2017-5753 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5753)
  * [ CVE-2017-5715 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715)
  * [ CVE-2017-5754 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5754)
  * [ CVE-2018-3640 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3640)
  * [ CVE-2018-3639 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3639)

  
  
##  Date published: 2017-10-02

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

[ Dnsmasq ](http://www.thekelleys.org.uk/dnsmasq/doc.html) provides
functionality for serving DNS, DHCP, router advertisements, and network boot.
This software is commonly installed in systems as varied as desktop Linux
distributions (like Ubuntu), home routers, and IoT devices. Dnsmasq is widely
used both on the open Internet and internally in private networks.

Google discovered seven distinct issues over the course of our regular
internal security assessments. After we determined the severity of these
issues, we worked to investigate their impact and exploitability and then
produced internal proofs of concept for each of them. We also worked with the
maintainer of Dnsmasq, Simon Kelly, to produce appropriate patches and
mitigate the issue.

During our review, the team found three potential remote code executions, one
information leak, and three denial of service vulnerabilities affecting the
latest version at the project git server as of September 5th 2017.

These patches are upstreamed and are committed to the [ project’s Git
repository ](http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=summary) .

####  Compute Engine impact

By default, Dnsmasq is only installed in images that use [ NetworkManager
](https://wikipedia.org/wiki/NetworkManager) and is inactive by default. The
following Compute Engine public images have Dnsmasq installed:

  * Ubuntu 16.04, 16.10, 17.04 
  * CentOS 7 
  * RHEL 7 

However, other images might have Dnsmasq installed as a dependency for other
packages. We recommend that you update your Debian, Ubuntu, CentOS, RHEL,
SLES, and OpenSuse instances to use the latest operating system image. CoreOS
and Container-Optimized OS are not affected. Windows images are also
unaffected.

For instances running Debian and Ubuntu, you can perform an update by running
the following commands in your instance:

    
    
    sudo apt-get -y update
    
    
    sudo apt-get -y dist-upgrade

For Red Hat Enterprise Linux and CentOS instances, run:

    
    
    sudo yum -y upgrade

For SLES and OpenSUSE images, run:

    
    
    sudo zypper up

As an alternative to running the manual update commands, you can [ recreate VM
instances using the image families
](https://cloud.google.com/compute/docs/instances/create-start-
instance#publicimage) of the respective operating system.

|  High  |

  * [ CVE-2017-14491 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14491)
  * [ CVE-2017-14492 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14492)
  * [ CVE-2017-14493 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14493)
  * [ CVE-2017-14494 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14494)
  * [ CVE-2017-14495 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14495)
  * [ CVE-2017-14496 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-14496)
  * [ CVE-2017-13704 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-13704)

  
  
##  Date published: 2016-10-26

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

CVE-2016-5195 is a race condition in the way Linux kernel's memory subsystem
handled breakage of the read only private mappings COW situation on write
access.

An unprivileged local user could use this flaw to gain write access to
otherwise read only memory mappings and thus increase their privileges on the
system.

For more information see the [ Dirty COW FAQ
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails) .

####  Compute Engine impact

All Linux distributions and versions on Compute Engine are affected. Most
instances will automatically download and install a newer kernel. However, a
reboot is required to patch your running system.

New or re-created instances based on the following Compute Engine images have
patched kernels installed already.

  * ` centos-6-v20161026 `
  * ` centos-7-v20161025 `
  * ` coreos-alpha-1192-2-0-v20161021 `
  * ` coreos-beta-1185-2-0-v20161021 `
  * ` coreos-stable-1122-3-0-v20161021 `
  * ` debian-8-jessie-v20161020 `
  * ` rhel-6-v20161026 `
  * ` rhel-7-v20161024 `
  * ` sles-11-sp4-v20161021 `
  * ` sles-12-sp1-v20161021 `
  * ` ubuntu-1204-precise-v20161020 `
  * ` ubuntu-1404-trusty-v20161020 `
  * ` ubuntu-1604-xenial-v20161020 `
  * ` ubuntu-1610-yakkety-v20161020 `

|  High  |  [ CVE-2016-5195
](https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails)  
  
##  Date published: 2016-02-16

**Last updated: 2016-02-22**

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

CVE-2015-7547 is a vulnerability where the glibc DNS client side resolver
makes software vulnerable to a stack-based buffer overflow when using the `
getaddrinfo() ` library function. An attacker can take advantage of software
using the function to exploit this vulnerability with attacker-controlled
domain names, attacker-controlled DNS servers, or through a man-in-the-middle
attack.

For more details, see the [ Google Security blog post
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html) or the [ Common Vulnerabilities and Exposures (CVE)
](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-7547) database.

####  Compute Engine impact

**Update (2016-02-22):**

You can now recreate your instances using the following CoreOS, SLES, and
OpenSUSE images:

  * ` coreos-alpha-962-0-0-v20160218 `
  * ` coreos-beta-899-7-0-v20160218 `
  * ` coreos-stable-835-13-0-v20160218 `
  * ` opensuse-13-2-v20160222 `
  * ` opensuse-leap-42-1-v20160222 `
  * ` sles-11-sp4-v20160222 `
  * ` sles-12-sp1-v20160222 `

**Update (2016-02-17):**

You can now perform an update on Ubuntu 12.04 LTS, Ubuntu 14.04 LTS, and
Ubuntu 15.10 instances by running the following commands:

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

As an alternative to running the manual update commands, you can now recreate
their instances with the following new images:

  * ` backports-debian-7-wheezy-v20160216 `
  * ` centos-6-v20160216 `
  * ` centos-7-v20160216 `
  * ` debian-7-wheezy-v20160216 `
  * ` debian-8-jessie-v20160216 `
  * ` rhel-6-v20160216 `
  * ` rhel-7-v20160216 `
  * ` ubuntu-1204-precise-v20160217a `
  * ` ubuntu-1404-trusty-v20160217a `
  * ` ubuntu-1510-wily-v20160217 `

We are not aware of any methods that can exploit this vulnerability through
Compute Engine's DNS resolvers with the default glibc configuration. You
should still patch your virtual machine instances as soon as possible, since,
as with any new vulnerability, new exploit methods may be discovered over
time. If you have enabled edns0 (disabled by default), you should disable it
until your instances are patched.

**Original bulletin:**

Your Linux distribution might be vulnerable. Compute Engine customers will
need to update the OS images of their instances to eliminate this
vulnerability if they are running a Linux OS.

For instances running Debian, you can perform an update by running the
following commands in your instance:

  1. ` user@my-instance:~$ sudo apt-get -y update `
  2. ` user@my-instance:~$ sudo apt-get -y dist-upgrade `
  3. ` user@my-instance:~$ sudo reboot `

We also recommend installing [ UnattendedUpgrades
](https://wiki.debian.org/UnattendedUpgrades) for your Debian instances.

For Red Hat Enterprise Linux instances:

  * ` user@my-instance:~$ sudo yum -y upgrade `
  * ` user@my-instance:~$ sudo reboot `

We will continue to update this bulletin as other operating system maintainers
publish patches for this vulnerability and as Compute Engine releases updated
OS images.

|  High  |  [ CVE-2015-7547
](https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-
getaddrinfo-stack.html)  
  
##  Date published: 2015-03-19

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

CVE-2015-1427 is a vulnerability where the Groovy scripting engine in [
Elasticsearch ](https://www.elastic.co/products/elasticsearch) before version
1.3.8 and any 1.4.x versions before 1.4.3, allows remote attackers to bypass
the sandbox protection mechanism and execute arbitrary shell commands.

For more details, see the [ National Vulnerability Database (NVD)
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427) or the [
Common Vulnerabilities and Exposures (CVE) ](http://www.cve.mitre.org/cgi-
bin/cvename.cgi?name=2015-1427) database.

####  Compute Engine impact

If you are running Elasticsearch on your Compute Engine instances, you should
upgrade your Elasticsearch version to 1.4.3 or higher. If you have already
upgraded your Elasticsearch software, you are protected from this
vulnerability.

If you have not upgraded Elasticsearch 1.4.3 or higher, you can [ perform a
rolling upgrade
](http://www.elastic.co/guide/en/elasticsearch/reference/current/rolling-
upgrades.html) .

If you deployed Elasticsearch using [ Click-to-deploy
](https://cloud.google.com/solutions/elasticsearch/click-to-deploy) in the [
Google Cloud Console ](https://console.cloud.google.com/) , you can [ delete
the deployment ](https://console.cloud.google.com/projectselector/deployments)
to remove instances running Elasticsearch.

The Google Cloud team is working on a fix in order to deploy an updated
version of Elasticsearch. However, the fix is not yet available for the Click-
to-deploy feature in the [ Cloud Console ](https://console.cloud.google.com/)
.

|  High  |  [ CVE-2015-1427
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-1427)  
  
##  Date published: 2015-01-29

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

[ CVE-2015-0235 (Ghost)
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235) is a
vulnerability in the glibc library.

App Engine, Cloud Storage, BigQuery, and Cloud SQL customers do not need to
take any actions. Google servers have been updated and are protected from this
vulnerability.

Customers of Compute Engine may need to update their OS images.

####  Compute Engine impact

Your Linux distribution may be vulnerable. Compute Engine customers will need
to update the OS images of their instances to eliminate this vulnerability if
they are running Debian 7, Debian 7 backports, Ubuntu 12.04 LTS, Red Hat
Enterprise Linux, CentOS, or SUSE Linux Enterprise Server 11 SP3.

This vulnerability does not affect Ubuntu 14.04 LTS, Ubuntu 14.10, or SUSE
Linux Enterprise Server 12.

We recommend that you upgrade your Linux distributions. For instances running
Debian 7, Debian 7 backports, or Ubuntu 12.04 LTS, you can perform an update
by running the following commands in your instance:

  1. ` user@my-instance:~$ sudo apt-get update `
  2. ` user@my-instance:~$ sudo apt-get -y upgrade `
  3. ` user@my-instance:~$ sudo reboot `

For Red Hat Enterprise Linux or CentOS instances:

  1. ` user@my-instance:~$ sudo yum -y upgrade `
  2. ` user@my-instance:~$ sudo reboot `

For SUSE Linux Enterprise Server 11 SP3 instances:

  1. ` user@my-instance:~$ sudo zypper --non-interactive up `
  2. ` user@my-instance:~$ sudo reboot `

As an alternative to running the manual update commands above, users can now
recreate their instances with the following new images:

  * ` debian-7-wheezy-v20150127 `
  * ` backports-debian-7-wheezy-v20150127 `
  * ` centos-6-v20150127 `
  * ` centos-7-v20150127 `
  * ` rhel-6-v20150127 `
  * ` rhel-7-v20150127 `
  * ` sles-11-sp3-v20150127 `
  * ` ubuntu-1204-precise-v20150127 `

####  Google Managed VM impact

Managed VM users using ` gcloud preview app deploy ` must update their base
docker containers with ` gcloud preview app setup-managed-vms ` and redeploy
each of their running apps using ` gcloud preview app deploy ` . Users that
deploy with ` appcfg ` do not need to do anything and will be upgraded
automatically.

|  High  |  [ CVE-2015-0235
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-0235)  
  
##  Date published: 2014-10-15

**Last updated: 2014-10-17**

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

CVE-2014-3566 (aka POODLE) is a vulnerability in the design of SSL version
3.0. This vulnerability allows the plaintext of secure connections to be
calculated by a network attacker. For details, see our [ blog post
](http://googleonlinesecurity.blogspot.com/2014/10/this-poodle-bites-
exploiting-ssl-30.html) on the vulnerability.

App Engine, Cloud Storage, BigQuery, and Cloud SQL customers do not need to
take any actions. Google servers have been updated and are protected from this
vulnerability. Customers of Compute Engine need to update their OS images.

####  Compute Engine impact

**Updated (2014-10-17):**

You may be vulnerable if you are using SSLv3. Compute Engine customers will
need to update the OS images of their instances to eliminate this
vulnerability.

We recommend that you upgrade your Linux distributions. For instances running
Debian, you can perform an update by running the following commands in your
instance:

    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

For CentOS instances:

    
    
    user@my-instance:~$ sudo yum -y upgrade
    user@my-instance:~$ sudo reboot

As an alternative to running the manual update commands above, users can now
recreate their instances with the following new images to recreate your
instances:

  * ` centos-6-v20141016 `
  * ` centos-7-v20141016 `
  * ` debian-7-wheezy-v20141017 `
  * ` backports-debian-7-wheezy-v20141017 `

We will update the bulletin for RHEL and SLES images after we have the images.
In the meantime, RHEL users can consult [ Red Hat directly
](https://access.redhat.com/articles/1232123) for more information.

**Original bulletin:**

Compute Engine customers will need to update the OS images of their instances
to eliminate this vulnerability. We will update this security bulletin with
instructions once new OS images are available.

|  Medium  |  [ CVE-2014-3566
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-3566)  
  
##  Date published: 2014-09-24

**last updated: 2014-09-29**

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

There is a bug in bash (CVE-2014-6271) that allows remote code execution based
on parsing of any attacker-controlled environment variables. The most likely
vector of exploitation is via malicious HTTP requests made to CGI scripts
exposed on a web server. For more information, see the [ bug description
](http://seclists.org/oss-sec/2014/q3/650) .

The bash bugs have been mitigated for Google Cloud products except for Compute
Engine guest OS images dated before 20140926\. Please see below for steps to
mitigate the bugs for your Compute Engine images.

####  Compute Engine impact

This bug may affect virtually all websites that use CGI scripts. In addition,
it will likely affect web sites that rely on PHP, Perl, Python, SSI, Java,
C++, and similar servlets that will ever invoke shell commands via calls such
as ` popen ` , ` system ` , ` shell_exec ` , or similar APIs. It may also
affect systems that attempt to allow controlled login access to restricted
users via mechanisms such as SSH command limitation or the bash restricted
shell.

**Update (2014-09-29):**

As an alternative to running the manual update commands below, users can now
recreate their instances with images that mitigate additional vulnerabilities
related to the bash security bug, including [ CVE-2014-7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) , [
CVE-2014-6277 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277)
, [ CVE-2014-6278
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278) , [
CVE-2014-7186 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186)
, and [ CVE-2014-7187
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187) . Use the
following new images to recreate your instances:

  * ` centos-6-v20140926 `
  * ` centos-7-v20140926 `
  * ` debian-7-wheezy-v20140926 `
  * ` backports-debian-7-wheezy-v20140926 `
  * ` rhel-6-v20140926 `

**Update (2014-09-25):**

Users can now choose to recreate their instances instead of performing a
manual update. To recreate your instances, use the following new images which
contains fixes to this security bug:

  * ` backports-debian-7-wheezy-v20140924 `
  * ` debian-7-wheezy-v20140924 `
  * ` rhel-6-v20140924 `
  * ` centos-6-v20140924 `
  * ` centos-7-v20140924 `

For RHEL and SUSE images, you can also manually perform updates by running the
following commands on your instances:

    
    
    # RHEL instances
    user@my-instance:~$ sudo yum -y upgrade
    
    # SUSE instances
    user@my-instance:~$ sudo zypper --non-interactive up

**Original bulletin:**

We recommend that you upgrade your Linux distributions. For instances running
Debian, you can perform an update by running the following commands in your
instance:

    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    

For CentOS instances:

    
    
    user@my-instance:~$ sudo yum -y upgrade

For detailed information, review the announcement for the respective Linux
distribution:

  * Original patches: [ http://ftp.gnu.org/gnu/bash/ ](http://ftp.gnu.org/gnu/bash/) (see the last entry in *-patches for the appropriate version) 
  * Debian: [ [SECURITY] [DSA 3032-1] bash security update ](https://lists.debian.org/debian-security-announce/2014/msg00220.html)
  * RHEL: 
    * [ RHSA-2014:1293-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00048.html)
    * [ RHSA-2014:1294-01 ](https://www.redhat.com/archives/rhsa-announce/2014-September/msg00049.html)
  * CentOS 5: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020582.html)
  * CentOS 6: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020585.html)
  * CentOS 7: [ [CentOS-announce] CESA-2014:1293 ](http://lists.centos.org/pipermail/centos-announce/2014-September/020583.html)

|  High  |  [ CVE-2014-7169
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7169) , [
CVE-2014-6271 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6271)
, [ CVE-2014-6277
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6277) , [
CVE-2014-6278 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-6278)
[ CVE-2014-7186
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7186) , [
CVE-2014-7187 ](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-7187)  
  
##  Date published: 2014-07-25

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

[ Elasticsearch Logstash ](http://www.elasticsearch.org/overview/logstash/) is
vulnerable to OS command injection that can allow unauthorized modification
and disclosure of data. An attacker can send crafted events to any of
Logstash’s data sources, allowing the attacker to execute commands with the
permissions of the Logstash process.

####  Compute Engine impact

This vulnerability affects all Compute Engine instances running versions of
Elasticsearch Logstash before 1.4.2 with zabbix or nagios_nsca outputs
enabled. To prevent attack, you can either:

  * Upgrade to Logstash 1.4.2 
  * Apply the patch for versions 1.3.x 
  * Disable the ` zabbix ` and ` nagios_nsca ` outputs. 

Read more on the [ Logstash blog
](http://www.elasticsearch.org/blog/logstash-1-4-2/) .

Elasticsearch also recommends [ using a firewall
](http://www.elasticsearch.org/blog/scripting-security/) to prevent remote
access by untrusted IPs.

|  High  |  [ CVE-2014-4326
](http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-4326)  
  
##  Date published: 2014-06-18

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

We would like to take a moment to respond to any possible concerns that
customers have about the security of Docker containers when running on Google
Cloud. This includes customers using our App Engine extensions that support
Docker Containers, container optimized virtual machines, or the Open Source
Kubernetes scheduler.

Docker has done a great job of responding to the issue and you can see their
blog response [ here ](http://blog.docker.com/2014/06/docker-container-
breakout-proof-of-concept-exploit/) . Note that, as they say in their
response, the issue revealed applies only to Docker 0.11, an older, pre-
production, version.

While the world is thinking about container security, we would like to point
out that in Google Cloud, Linux application container based solutions
(specifically Docker containers) run in full virtual machines (Compute
Engine). While we support the efforts of the Docker community to harden the
Linux application container stack, we recognize that the technology is new,
and the surface area large. It is our belief that, for now, full hypervisors
(virtual machines) provide a more compact and defensible surface area. Virtual
machines were designed from the beginning to isolate malicious workloads and
to minimize the likelihood and impact of a code bug.

Our customers can rest assured that a full hypervisor boundary exists between
them and any third party, potentially malicious code. Should we reach a point
where we consider the Linux application container stack robust enough to
support multi-tenant workloads, we will let the community know. For now, the
Linux application container does not replace the virtual machine. It is a way
to get a lot more out of it.

|  Low  |  [ Docker blog post ](http://blog.docker.com/2014/06/docker-
container-breakout-proof-of-concept-exploit/)  
  
##  Date published: 2014-06-05

**Last updated: 2014-06-09**

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

OpenSSL has an issue where the ` ChangeCipherSpec ` messages are not correctly
bound into the handshake state machine. This allows them to be injected early
into the handshake. An attacker using a carefully crafted handshake can force
the use of weak keying material in OpenSSL SSL/TLS clients and servers. This
can be exploited by a Man-in-the-middle (MITM) attack where the attacker can
decrypt and modify traffic from the attacked client and server.

This issue is identified as [ CVE-2014-0224
](https://www.openssl.org/news/secadv/20140605.txt) . The OpenSSL team has
fixed the issue and alerted the OpenSSL community to update OpenSSL.

####  Compute Engine impact

This vulnerability affects all Compute Engine instances which use OpenSSL,
including Debian, CentOS, Red Hat Enterprise Linux, and SUSE Linux Enterprise
Server. You can update your instances by recreating them with new images, or
by manually updating packages on your instances.

**Update (2014-06-09):** To update your instances running SUSE Linux
Enterprise Server with new images, recreate your instances using the following
image versions or higher:

  * ` sles-11-sp3-v20140609 `

**Original post:**

To update Debian and CentOS instances using new images, recreate your
instances using any of the following image versions or higher:

  * ` debian-7-wheezy-v20140605 `
  * ` backports-debian-7-wheezy-v20140605 `
  * ` centos-6-v20140605 `
  * ` rhel-6-v20140605 `

To manually update OpenSSL on your instances, run the following commands to
update the appropriate packages. For instances running CentOS and RHEL, you
can update OpenSSL by running these commands in your instance:

    
    
    user@my-instance:~$ sudo yum -y update
    user@my-instance:~$ sudo reboot

For instances running Debian, you can update OpenSSL by running the following
commands in your instance:

    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get -y upgrade
    user@my-instance:~$ sudo reboot

For instances running SUSE Linux Enterprise Server, you can ensure OpenSSL is
up to date by running these commands in the instance:

    
    
    user@my-instance:~$ sudo zypper --non-interactive up
    user@my-instance:~$ sudo reboot

|  Medium  |  [ CVE-2014-0224
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0224)  
  
##  Date published: 2014-04-08

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

The (1) TLS and (2) DTLS implementations in OpenSSL 1.0.1 before 1.0.1g do not
properly handle Heartbeat Extension packets, which allows remote attackers to
obtain sensitive information from process memory via crafted packets that
trigger a buffer over-read, as demonstrated by reading private keys, related
to ` d1_both.c ` and ` t1_lib.c ` , aka the Heartbleed bug.

####  Compute Engine impact

This vulnerability affects all Compute Engine Debian, RHEL, and CentOS
instances that do not have the most updated version of OpenSSL. You can update
your instances by recreating them with new images, or by manually updating
packages on your instances.

To update your instances using new images, recreate your instances using any
of the following image versions or higher:

  * ` debian-7-wheezy-v20140408 `
  * ` backports-debian-7-wheezy-v20140408 `
  * ` centos-6-v20140408 `
  * ` rhel-6-v20140408 `

To manually update OpenSSL on your instances, run the following commands to
update the appropriate packages. For instances running CentOS and RHEL, you
can ensure OpenSSL is up to date by running these commands in the instance:

    
    
    user@my-instance:~$ sudo yum update
    user@my-instance:~$ sudo reboot

For instances running Debian, you can update OpenSSL by running the following
commands in your instance:

    
    
    user@my-instance:~$ sudo apt-get update
    user@my-instance:~$ sudo apt-get upgrade
    user@my-instance:~$ sudo reboot

Instances running SUSE Linux are not affected.

**Update on April 14, 2014:** In light of new research on extracting keys
using the Heartbleed bug, Compute Engine is recommending that Compute Engine
customers create new keys for any affected SSL services.

|  Medium  |  [ CVE-2014-0160
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2014-0160)  
  
##  Date published: 2013-06-07

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

**Note:** This vulnerability is only applicable for kernels, which have been
deprecated and removed since API version v1.

Format string vulnerability in the ` b43_request_firmware ` function in `
drivers/net/wireless/b43/main.c ` in the Broadcom B43 wireless driver in the
Linux kernel through 3.9.4 allows local users to gain privileges by leveraging
root access and including format string specifiers in an ` fwpostfix `
modprobe parameter, leading to improper construction of an error message.

####  Compute Engine impact

This vulnerability affects all Compute Engine kernels earlier than `
gcg-3.3.8-201305291443 ` . In response, Compute Engine has deprecated all
earlier kernels and recommends that users update their instances and images to
use Compute Engine kernel ` gce-v20130603 ` . ` gce-v20130603 ` contains
kernel ` gcg-3.3.8-201305291443 ` , which has the patch for this
vulnerability.

To find out what kernel version your instance is using:

  1. ssh into your instance 
  2. Run ` uname -r `

|  Medium  |  [ CVE-2013-2852
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2852)  
  
##  Date published: 2013-06-07

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

**Note:** This vulnerability is only applicable for kernels, which have been
deprecated and removed since API version v1.

Format string vulnerability in the register_disk function in ` block/genhd.c `
in the Linux kernel through 3.9.4 allows local users to gain privileges by
leveraging root access and writing format string specifiers to `
/sys/module/md_mod/parameters/new_array ` in order to create a crafted `
/dev/md ` device name.

####  Compute Engine Impact

This vulnerability affects all Compute Engine kernels earlier than `
gcg-3.3.8-201305291443 ` . In response, Compute Engine has deprecated all
earlier kernels and recommends that users update their instances and images to
use Compute Engine kernel ` gce-v20130603 ` . ` gce-v20130603 ` contains
kernel ` gcg-3.3.8-201305291443 ` , which has the patch for this
vulnerability.

To find out what kernel version your instance is using:

  1. ssh into your instance 
  2. Run ` uname -r `

|  Medium  |  [ CVE-2013-2851
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2851)  
  
##  Date published: 2013-05-14

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

**Note:** This vulnerability is only applicable for kernels, which have been
deprecated and removed since API version v1.

The perf_swevent_init function in ` kernel/events/core.c ` in the Linux kernel
before 3.8.9 uses an incorrect ` integer ` data type, which allows local users
to gain privileges via a crafted ` perf_event_open ` system call.

####  Compute Engine impact

This vulnerability affects all Compute Engine kernels earlier than `
gcg-3.3.8-201305211623 ` . In response, Compute Engine has deprecated all
earlier kernels and recommends that users update their instances and images to
use Compute Engine kernel ` gce-v20130521 ` . ` gce-v20130521 ` contains
kernel ` gcg-3.3.8-201305211623 ` , which has the patch for this
vulnerability.

To find out what kernel version your instance is using:

  1. ssh into your instance 
  2. Run ` uname -r `

|  High  |  [ CVE-2013-2094
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-2094)  
  
##  Date published: 2013-02-18

Description  |  Severity  |  Notes  
---|---|---  
  
####  Description

**Note:** This vulnerability is only applicable for kernels, which have been
deprecated and removed since API version v1.

Race condition in the ptrace functionality in the Linux kernel before 3.7.5
allows local users to gain privileges via a ` PTRACE_SETREGS ptrace ` system
call in a crafted application.

####  Compute Engine impact

This vulnerability affects Compute Engine kernels ` 2.6.x-gcg- _ <date> _ ` .
In response, Compute Engine has deprecated 2.6.x kernels and recommends that
users update their instances and images to use Compute Engine kernel `
gce-v20130225 ` . ` gce-v20130225 ` contains kernel ` 3.3.8-gcg-201302081521 `
, which has the patch for this vulnerability.

To find out what kernel version your instance is using:

  1. ssh into your instance 
  2. Run ` uname -r `

|  Medium  |  [ CVE-2013-0871
](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-0871)

