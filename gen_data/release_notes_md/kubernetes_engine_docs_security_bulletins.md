#  Security bulletins

All security bulletins for Google Kubernetes Engine (GKE) are described in
this topic.

Vulnerabilities are often kept secret under embargos until affected parties
have had a chance to address them. In these cases, GKE's [ Release Notes
](/kubernetes-engine/docs/release-notes) will refer to "security updates"
until the embargo has been lifted. At that point the notes will be updated to
reflect the vulnerability the patch addressed.

**Note:** If you run multi-tenant workloads on GKE, please pay particular
attention to these bulletins. These vulnerabilities are more likely to impact
multi-tenant workloads. For a technical description of security boundaries in
GKE and how these impact workloads, see [ Isolation at different layers of the
Kubernetes stack ](https://cloudplatform.googleblog.com/2018/05/Exploring-
container-security-Isolation-at-different-layers-of-the-Kubernetes-stack.html)
.

To get the latest security bulletins delivered to you, add the URL of this
page to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/kubernetes-engine-security-
bulletins.xml `

##  GCP-2020-007

**Published:** 2020-06-01  
Description  |  Severity  |  Notes  
---|---|---  
  
Server Side Request Forgery (SSRF) vulnerability, [ CVE-2020-8555
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555) , was recently
discovered in Kubernetes, allowing certain authorized users to leak up to 500
bytes of sensitive information from the control plane host network. The Google
Kubernetes Engine (GKE) control plane uses controllers from Kubernetes and is
thus affected by this vulnerability. We recommend that you [ upgrade
](/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) the control
plane to the latest patch version, as we detail below. A node upgrade is not
required.  

####  What should I do?

For most customers, no further action is required. The vast majority of
clusters are already running a patched version. The following GKE versions or
newer contain the fix for this vulnerability:

  * 1.14.7-gke.39 
  * 1.14.8-gke.32 
  * 1.14.9-gke.17 
  * 1.14.10-gke.12 
  * 1.15.7-gke.17 
  * 1.16.4-gke.21 
  * 1.17.0-gke.0 

Clusters using [ release channels ](/kubernetes-engine/docs/concepts/release-
channels) are already on control plane versions with the mitigation.

####  What vulnerability is addressed by this patch?

These patches mitigate vulnerability CVE-2020-8555. This is rated as a Medium
vulnerability for GKE as it was difficult to exploit due to various control
plane hardening measures.

An attacker with permissions to create a Pod with certain built-in Volume
types (GlusterFS, Quobyte, StorageFS, ScaleIO) or permissions to create a
StorageClass can cause ` kube-controller-manager ` to make ` GET ` requests or
` POST ` requests _without_ an attacker controlled request body from the
master's host network. These volume types are rarely used on GKE, so new use
of these volume types may be a useful detection signal.

Combined with a means to leak the results of the ` GET/POST ` back to the
attacker, such as through logs, this can lead to disclosure of sensitive
information. We have updated the storage drivers in question to remove the
potential for such leaks.

|

Medium

|

[ CVE-2020-8555 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8555)  
  
##  GCP-2020-006

**Published:** 2020-06-01  
Description  |  Severity  |  Notes  
---|---|---  
  
Kubernetes has disclosed a [ vulnerability
](https://github.com/kubernetes/kubernetes/issues/91507) that allows a
privileged container to redirect node traffic to another container. Mutual
TLS/SSH traffic, such as between the kubelet and API server or traffic from
applications using mTLS cannot be read or modified by this attack. All Google
Kubernetes Engine (GKE) nodes are affected by this vulnerability, and we
recommend that you [ upgrade ](/kubernetes-engine/docs/how-to/upgrading-a-
cluster) to the latest patch version, as we detail below.

####  What should I do?

To mitigate this vulnerability, [ upgrade ](/kubernetes-engine/docs/how-
to/upgrading-a-cluster) your control plane, and then your nodes to one of the
patched versions listed below. Clusters on release channels are already
running a patched version on both control plane and nodes:

  * 1.14.10-gke.36 
  * 1.15.11-gke.15 
  * 1.16.8-gke.15 

Very few containers typically require ` CAP_NET_RAW ` . This and other
powerful capabilities should be blocked by default through [ PodSecurityPolicy
](/kubernetes-engine/docs/how-to/pod-security-policies) or [ Anthos Policy
Controller ](/anthos-config-management/docs/concepts/policy-controller) :

  * Drop the ` CAP_NET_RAW ` capability from containers: 
    * By enforcing it through [ PodSecurityPolicy ](/kubernetes-engine/docs/how-to/pod-security-policies) using: 
        
                # Require dropping CAP_NET_RAW with a PSP
        apiversion: extensions/v1beta1
        kind: PodSecurityPolicy
        metadata:
          name: no-cap-net-raw
        spec:
          requiredDropCapabilities:
            -NET_RAW
             ...
             # Unrelated fields omitted
        

    * Or by using Anthos Policy Controller/Gatekeeper with this [ constraint template ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) and applying it, for example: 
        
                # Dropping CAP_NET_RAW with Gatekeeper
        # (requires the K8sPSPCapabilities template)
        apiversion: constraints.gatekeeper.sh/v1beta1
        kind:  K8sPSPCapabilities
        metadata:
          name: forbid-cap-net-raw
        spec:
          match:
            kinds:
              - apiGroups: [""]
              kinds: ["Pod"]
            namespaces:
              #List of namespaces to enforce this constraint on
              - default
            # If running gatekeeper >= v3.1.0-beta.5,
            # you can exclude namespaces rather than including them above.
            excludedNamespaces:
              - kube-system
          parameters:
            requiredDropCapabilities:
              - "NET_RAW"
        

    * Or by updating your Pod specs: 
        
                # Dropping CAP_NET_RAW from a Pod:
        apiVersion: v1
        kind: Pod
        metadata:
          name: no-cap-net-raw
        spec:
          containers:
            -name: may-container
             ...
            securityContext:
              capabilities:
                drop:
                  -NET_RAW
        

####  What vulnerability is addressed by this patch?

The patch mitigate the following vulnerability:

The vulnerability described in [ Kubernetes issue 91507
](https://github.com/kubernetes/kubernetes/issues/91507) ` CAP_NET_RAW `
capability (which is included in the default container capability set) to
maliciously configure the IPv6 stack on the node and redirect node traffic to
the attacker controlled container. This will allow the attacker to
intercept/modify traffic originating from or destined for the node. Mutual
TLS/SSH traffic, such as between the kubelet and API server or traffic from
applications using mTLS cannot be read or modified by this attack.

|

Medium

|

[ Kubernetes issue 91507
](https://github.com/kubernetes/kubernetes/issues/91507)  
  
  
##  GCP-2020-005

**Published:** 2020-05-07  
**Updated:** 2020-05-07  Description  |  Severity  |  Notes  
---|---|---  
  
A vulnerability was recently discovered in the Linux kernel, described in [
CVE-2020-8835 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8835)
, allowing container escape to obtain root privileges on the host node.

Google Kubernetes Engine (GKE) Ubuntu nodes running GKE 1.16 or 1.17 are
affected by this vulnerability, and we recommend that you upgrade to the
latest patch version as soon as possible, as we detail below.

Nodes running Container-Optimized OS are not affected. Nodes running on GKE
on-prem are not affected.

####  What should I do?

**For most customers, no further action is required. Only nodes running Ubuntu
in GKE version 1.16 or 1.17 are affected.**

In order to upgrade your nodes, you must first upgrade your master to the
newest version. This patch will be available in Kubernetes 1.16.8-gke.12,
1.17.4-gke.10, and newer releases. Track the availability of these patches in
the [ release notes ](/kubernetes-engine/docs/release-notes) .

####  What vulnerability is addressed by this patch?

The patch mitigates the following vulnerability:

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835) describes a vulnerability in the Linux
kernel version 5.5.0 and newer that allows a malicious container to (with
minimal user interaction in the form of an exec) read and write kernel memory
and thus gain root-level code execution on the host node. This is rated as a
'High' severity vulnerability.

|

High

|

[ CVE-2020-8835 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8835)  
  
  
##  GCP-2020-003

**Published:** 2020-03-31  
**Updated:** 2020-03-31  Description  |  Severity  |  Notes  
---|---|---  
  
A vulnerability was recently discovered in Kubernetes, described in [
CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) , which allows any user authorized to
make POST requests to execute a remote Denial-of-Service attack on a
Kubernetes API server. The Kubernetes Product Security Committee (PSC)
released additional information on this vulnerability which can be found [
here ](https://groups.google.com/forum/#!topic/kubernetes-security-
announce/wuwEwZigXBc) .

GKE Clusters that use [ Master Authorized Networks ](/kubernetes-
engine/docs/how-to/authorized-networks) and [ Private clusters with no public
endpoint ](/kubernetes-engine/docs/how-to/private-clusters#private_master)
mitigate this vulnerability.

####  What should I do?

We recommend that you upgrade your cluster to a patch version containing the
fix for this vulnerability.

The patch versions which contain the fix are listed below:

  * 1.13.12-gke.29 
  * 1.14.9-gke.27 
  * 1.14.10-gke.24 
  * 1.15.9-gke.20 
  * 1.16.6-gke.1 

####  What vulnerabilities are addressed by this patch?

The patch fixes the following Denial-of-Service (DoS) vulnerability:

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) .

|

Medium

|

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  GCP-2020-002

**Published:** 2020-03-23  
**Updated:** 2020-03-23  Description  |  Severity  |  Notes  
---|---|---  
  
Kubernetes has disclosed [ two denial of service vulnerabilities
](https://groups.google.com/forum/#!topic/kubernetes-security-
announce/2UOlsba2g0s) , one impacting the API server, and the other impacting
Kubelets. For more details, see the Kubernetes issues: [ 89377
](https://github.com/kubernetes/kubernetes/issues/89377) and [ 89378
](https://github.com/kubernetes/kubernetes/issues/89378) .

####  What should I do?

All GKE users are protected from CVE-2020-8551 unless untrusted users can send
requests within the cluster's internal network. Use of [ master authorized
networks ](/kubernetes-engine/docs/how-to/authorized-networks) additionally
mitigates against CVE-2020-8552.

####  When will these be patched?

Patches for CVE-2020-8551 require a node upgrade. The patch versions which
will contain the mitigation are listed below:

  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

Note: Versions 1.14.x and earlier are unaffected by this vulnerability so no
patches are required.

Patches for CVE-2020-8552 require a master upgrade. The patch versions which
will contain the mitigation are listed below:

  * 1.14.10-gke.32 
  * 1.15.10-gke.* 
  * 1.16.7-gke.* 

|

Medium

|

[ CVE-2020-8551 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8551)  
[ CVE-2020-8552 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8552)  
  
##  January 21, 2020; last updated January 24, 2020

**Published:** 2020-01-21  
**Updated:** 2020-01-24  Description  |  Severity  |  Notes  
---|---|---  
  
**2020-01-24 Update:** The process of making patched versions available is
already underway and will be completed by January 25, 2020.

* * *

Microsoft has disclosed a vulnerability in the Windows Crypto API and its
validation of elliptic curve signatures. For more information please see [
Microsoft's disclosure. ](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601)

**What should I do?**

**For most customers, no further action is required. Only nodes running
Windows Server are impacted.**

For customers who are using Windows Server nodes, both the nodes and the
containerized workloads that run on those nodes must be updated to patched
versions to mitigate this vulnerability.

**To update the containers:**

Rebuild your containers using Microsoft's latest base container images,
selecting a [ servercore ](https://hub.docker.com/_/microsoft-windows-
servercore) or [ nanoserver ](https://hub.docker.com/_/microsoft-windows-
nanoserver) tag with a LastUpdated Time of 1/14/2020 or later.

**To update the nodes:**

The process of making patched versions available is already underway and will
be completed by January 24, 2020.

You may either wait until that time and perform a node upgrade to a patched
GKE version or you may use Windows Update to deploy the latest Windows patch
manually at any time.

The patch versions which will contain the mitigation are listed below:

  * 1.14.7-gke.40 
  * 1.14.8-gke.33 
  * 1.14.9-gke.23 
  * 1.14.10-gke.17 
  * 1.15.7-gke.23 
  * 1.16.4-gke.22 

**What vulnerabilities are addressed by this patch?**

The patch mitigates the following vulnerabilities:

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601) \- This vulnerability is also known as the
[ Windows Crypto API Spoofing Vulnerability
](https://portal.msrc.microsoft.com/en-US/security-
guidance/advisory/CVE-2020-0601) and could be exploited to make malicious
executables appear trusted or allow the attacker to conduct man-in-the-middle
attacks and decrypt confidential information on TLS connections to the
affected software.

|

NVD Base Score: 8.1 (High)

|

[ CVE-2020-0601 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-0601)  
  
  
##  November 14, 2019

**Published:** 2019-11-14  
**Updated:** 2019-11-14  Description  |  Severity  |  Notes  
---|---|---  
  
Kubernetes has disclosed a security issue in the kubernetes-csi [ ` external-
provisioner ` ](https://github.com/kubernetes-csi/external-provisioner) , [ `
external-snapshotter ` ](https://github.com/kubernetes-csi/external-
snapshotter) , and [ ` external-resizer ` ](https://github.com/kubernetes-
csi/external-resizer) sidecars that impacts most versions of the sidecars
bundled in [ Container Storage Interface (CSI) drivers ](https://kubernetes-
csi.github.io/docs/drivers.html) . For further details, see the [ Kubernetes
disclosure ](https://github.com/kubernetes/kubernetes/issues/85233) .

**What should I do?**  
**This vulnerability does not affect any managed GKE components** . You may be
affected if you manage your own CSI drivers in [ GKE Alpha clusters
](https://cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters)
running GKE version 1.12 or higher. If you are affected, check with your CSI
driver vendor for upgrade instructions.

**What vulnerabilities are addressed by this patch?**  
[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255) : This CVE is a vulnerability in the `
kubernetes-csi ` [ ` external-provisioner ` ](https://github.com/kubernetes-
csi/external-provisioner) , [ ` external-snapshotter `
](https://github.com/kubernetes-csi/external-snapshotter) , and [ ` external-
resizer ` ](https://github.com/kubernetes-csi/external-resizer) sidecars which
can allow unauthorized volume data access or mutation. This impacts most
versions of the sidecars bundled in [ CSI drivers ](https://kubernetes-
csi.github.io/docs/drivers.html) .

|

Medium

|

[ CVE-2019-11255 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11255)  
  
  
##  November 12, 2019

**Published:** 2019-11-12  
**Updated:** 2019-11-12  Description  |  Severity  |  Notes  
---|---|---  
  
Intel has disclosed CVEs that potentially allow interactions between
speculative execution and microarchitectural state to expose data. For further
details, see the [ Intel disclosure
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) .

**The host infrastructure that runs Kubernetes Engine isolates customer
workloads. Unless you are running untrusted code inside your own multi-tenant
GKE clusters _and_ using N2, M2 or C2 nodes, no further action is required. **
For GKE instances on N1 nodes, no new action is required.

If you are running Anthos GKE on-prem, exposure is hardware dependent. Please
compare your infrastructure with the [ Intel disclosure
](https://blogs.intel.com/technology/2019/11/ipas-november-2019-intel-
platform-update-ipu/) .

####  What should I do?

**You are only impacted if you are using node pools with N2, M2, or C2 nodes
_and_ those nodes run untrusted code inside your own multi-tenant GKE
clusters. **

**Restarting your nodes applies the patch.** The easiest way to restart all
nodes in your node pool is to use the [ upgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster#upgrade_nodes) operation to force a restart across all of the affected
node pool.  

Note: You do not need to change versions during an upgrade. You can start an
upgrade to the same node version with the ` cluster-version ` flag.

####  What vulnerabilities are addressed by this patch?

The patch mitigates the following vulnerabilities:

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)
: This CVE is also known as TSX Async Abort (TAA). TAA provides another avenue
for data exfiltration using the same microarchitectural data structures that
were exploited by [ Microarchitectural Data Sampling (MDS)
](https://cloud.google.com/kubernetes-engine/docs/security-
bulletins#may-14-2019) .

[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)
This is a Denial of Service (DoS) vulnerability affecting virtual machine
hosts allowing a malicious guest to crash an unprotected host. This CVE is
also known as "Machine Check Error on Page Size Change." This does not affect
GKE.

|

Medium

|

[ CVE-2019-11135 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11135)  
[ CVE-2018-12207 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12207)  
  
##  October 22, 2019

**Published:** 2019-10-22  
**Updated:** 2019-10-22  Description  |  Severity  |  Notes  
---|---|---  
  
A vulnerability was recently discovered in the Go programming language,
described in [ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276) . This vulnerability potentially impacts
Kubernetes configurations using an Authenticating Proxy. For further details,
see the [ Kubernetes disclosure
](https://groups.google.com/forum/#!topic/kubernetes-security-
announce/PtsUCqFi4h4) .

Kubernetes Engine does not allow configuration of an Authenticating Proxy, so
is not affected by this vulnerability.

|

None

|

[ CVE-2019-16276 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-16276)  
  
  
##  October 16, 2019

**Published:** 2019-10-16  
**Updated:** 2019-10-24  Description  |  Severity  |  Notes  
---|---|---  
  
**2019-10-24 Update:** Patched versions are now available in all zones.

* * *

A vulnerability was recently discovered in Kubernetes, described in [
CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) , which allows any user authorized to
make POST requests to execute a remote Denial-of-Service attack on a
Kubernetes API server. The Kubernetes Product Security Committee (PSC)
released additional information on this vulnerability which can be found [
here ](https://groups.google.com/forum/#!topic/kubernetes-security-
announce/jk8polzSUxs) .

GKE Clusters that use [ Master Authorized Networks ](/kubernetes-
engine/docs/how-to/authorized-networks) and [ Private clusters with no public
endpoint ](/kubernetes-engine/docs/how-to/private-clusters#private_master)
mitigate this vulnerability.

######  What should I do?

We recommend that you upgrade your cluster to a patch version containing the
fix as soon as they are available. We expect them to be available in all zones
with the GKE release planned for the week of October 14th.

The patch versions which will contain the mitigation are listed below:

  * 1.12.10-gke.15 
  * 1.13.11-gke.5 
  * 1.14.7-gke.10 
  * 1.15.4-gke.15 

######  What vulnerabilities are addressed by this patch?

The patch mitigates the following vulnerabilities:

CVE-2019-11253 is a Denial-of-Service (DoS) vulnerability.

|

High

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
  
##  September 16, 2019

**Published:** 2019-09-16  
**Updated:** 2019-10-16  Description  |  Severity  |  Notes  
---|---|---  
  
This bulletin has been updated since its original publication.

The Go programming language recently discovered new security vulnerabilities [
CVE-2019-9512 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9512)
and [ CVE-2019-9514 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9514) , which are Denial of Service (DoS)
vulnerabilities. In GKE, this could allow a user to craft malicious requests
that consume excessive amounts of CPU in the Kubernetes API server,
potentially reducing the availability of the cluster control plane. For
further details, see the [ Go programming language disclosure
](https://groups.google.com/forum/#!topic/golang-announce/65QixT3tcmg) .

######  What should I do?

We recommend that you upgrade your cluster to the latest patch version, which
contains the mitigation to this vulnerability, as soon as they are available.
We expect them to be available in all zones with the next GKE release,
according to the [ release schedule ](/kubernetes-engine/docs/release-notes-
archive#september_16_2019) .

The patch versions which will contain the mitigation are listed below:

  * **October 16, 2019 Update:** 1.12.10-gke.15 
  * 1.13.10-gke.0 
  * 1.14.6-gke.1 

######  What vulnerability is addressed by this patch?

The patch mitigates the following vulnerabilities:

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512) and [ CVE-2019-9514
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9514) are Denial of
Service (DoS) vulnerabilities.

|

High

|

[ CVE-2019-9512 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9512)  
[ CVE-2019-9514 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9514)  
  
  
##  September 5, 2019

**Published:** 2019-09-05  
**Updated:** 2019-09-05

The bulletin for the fix for the vulnerability documented in the bulletin of
May 31, 2019  is updated.

##  August 22, 2019

**Published:** 2019-08-22  
**Updated:** 2019-08-22

The bulletin for  August 5, 2019  has been updated. The fix for the
vulnerability documented in the earlier bulletin is [ available ](/kubernetes-
engine/docs/release-notes-archive#august_22_2019) .

##  August 8, 2019

**Published:** 2019-08-08  
**Updated:** 2019-08-08

The bulletin for  August 5, 2019  has been updated. We expect the fix for the
vulnerability documented in that bulletin to be available in the next release
of GKE.

##  August 5, 2019

**Published:** 2019-08-05  
**Updated:** 2019-08-09  Description  |  Severity  |  Notes  
---|---|---  
  
This bulletin has been updated since its original publication.

Kubernetes recently discovered a vulnerability, [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) , which
allows cluster-scoped [ custom resource
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) instances to be acted on as if they were namespaced objects
existing in all Namespaces. This means user and service accounts with only
namespace-level RBAC permissions can interact with cluster-scoped custom
resources. Exploiting this vulnerability requires the attacker to have
privileges to access the resource in any namespace.

######  What should I do?

We recommend that you [ upgrade ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-cluster) your cluster to the latest patch
version, which contains the mitigation to this vulnerability, as soon as they
are available. We expect them to be available in all zones with the next GKE
release. The patch versions which will contain the mitigation are listed
below:

  * 1.11.10-gke.6 
  * 1.12.9-gke.13 
  * 1.13.7-gke.19 
  * 1.14.3-gke.10 ( [ Rapid Channel ](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels) ) 

######  What vulnerability is addressed by this patch?

The patch mitigates the following vulnerability: [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Medium

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)  
  
##  July 3, 2019

**Published:** 2019-07-03  
**Updated:** 2019-07-03  Description  |  Severity  |  Notes  
---|---|---  
  
A patched version of ` kubectl ` to address CVE-2019-11246 is now available
with [ ` gcloud ` 253.0.0 ](https://cloud.google.com/sdk/docs/release-
notes#kubernetes_engine) . See the  June 25, 2019 security bulletin  for more
information.

**Note:** The patch is not available in ` kubectl ` 1.11.10.

|

High

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  July 3, 2019

**Published:** 2019-06-25  
**Updated:** 2019-07-03  Description  |  Severity  |  Notes  
---|---|---  
  
######  July 3, 2019 Update

At the time of our last update, patches for versions 1.11.9 and 1.11.10 were
not yet available. We have now released 1.11.10-gke.5 as an upgrade target for
both 1.11 versions.

At this time, GKE masters have been patched, and the Google infrastructure
that runs Kubernetes Engine has been patched and is protected from this
vulnerability.

1.11 masters will soon be deprecated and are scheduled to automatically
upgrade to 1.12 the week of July 8, 2019. You may choose any of the following
suggested actions to get nodes onto a patched version:

  * Perform the node upgrade to 1.11.10-gke.5 by Jul 8, 2019. After this date, 1.11 versions will begin to be removed from the available list of upgrade targets. 
  * Enable [ auto upgrades ](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) on 1.11 nodes and allow them to be upgraded when the masters are upgraded to 1.12. 
  * [ Manually upgrade ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) both masters and nodes to a fixed 1.12 version. 

The original bulletin from June 24, 2019 follows:

* * *

######  June 24, 2019 Update

As of 2019-06-22 21:40 UTC we have made the following patched Kubernetes
versions available. Masters between Kubernetes versions 1.11.0 and 1.13.6 will
be automatically updated to a patched version. If you are not running a
version compatible with this patch, upgrade to a compatible master version
(listed below) before upgrading your nodes.

**Due to the severity of these vulnerabilities, whether you have node auto-
upgrade enabled or not, we recommend that you[ manually upgrade ](/kubernetes-
engine/docs/how-to/upgrading-a-container-cluster) both your nodes and masters
to one of these versions as soon as possible. **

The patched verions:

  * 1.11.8-gke.10 
  * 1.12.7-gke.24 
  * 1.12.8-gke.10 
  * 1.13.6-gke.13 

The original bulletin from June 18, 2019 follows:

* * *

Netflix has recently disclosed three TCP vulnerabilities in Linux kernels:

  * [ CVE-2019-11477 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11477)
  * [ CVE-2019-11478 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11478)
  * [ CVE-2019-11479 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11479)

These CVEs are collectively referred to as [ NFLX-2019-001
](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-
party/2019-001.md) .

Unpatched Linux kernels may be vulnerable to a remotely triggered denial of
service attack. **Google Kubernetes Engine nodes that send or receive
untrusted network traffic are affected, and we recommend that you follow these
mitigation steps below to protect your workloads.**

######  Kubernetes masters

  * Kubernetes masters using [ Authorized Networks ](/kubernetes-engine/docs/how-to/authorized-networks) to limit traffic to trusted networks are unaffected. 

  * Masters for GKE clusters, which are managed by Google, will be patched automatically in the coming days. No customer action is required. 

######  Kubernetes nodes

Nodes that limit traffic to trusted networks are unaffected. This would be a
cluster with the following:

  * Nodes firewalled from untrusted networks or with no public IPs ( [ Private clusters ](/kubernetes-engine/docs/how-to/private-clusters) ) 
  * Clusters without public LoadBalancer Services 

Google is preparing a permanent mitigation for these vulnerabilities that will
be made available as a new node version. We will update this bulletin and send
an email to all GKE customers when the permanent fix is made available.

Until the permanent fix is available, we've created a Kubernetes DaemonSet
that implements mitigations by modifying the host ` iptables ` configuration.

#####  What should I do?

Apply the Kubernetes DaemonSet to all nodes in your cluster by running the
following command. This adds an ` iptables ` rule to the existing ` iptables `
rules on the node to mitigate the vulnerability. **Run the command once per
cluster per Google Cloud project.**

    
    
    kubectl apply -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

Because Ipv6 is not supported on GKE, no ip6tables rule is required.

Once a patched node version is available and you have upgraded all
potentially-affected nodes, you can remove the DaemonSet using the following
command. **Run the command once per cluster per Google Cloud project.**

    
    
    kubectl delete -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform\
    /k8s-node-tools/master/drop-small-mss/drop-small-mss.yaml
          

|  High  
Medium  
Medium  
|  [ CVE-2019-11477 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11477)  
[ CVE-2019-11478 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11478)  
[ CVE-2019-11479 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11479)  
  
  
##  June 25, 2019

Description  |  Severity  |  Notes  
---|---|---  
  
**2019-07-03 Update:** This patch is available in ` gcloud ` 253.0.0, for `
kubectl ` versions 1.12.9, 1.13.6, 1.14.2 and newer releases.

**Note:** The patch is not available in 1.11.10.

* * *

Kubernetes recently discovered a vulnerability, [ CVE-2019-11246
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11246) , which
allows an attacker with access to a ` kubectl cp ` operation and code
execution inside a container to modify files on the host. This exploit
potentially allows an attacker to replace or create a file in the host file
system. For further details, see the [ Kubernetes disclosure
](https://groups.google.com/forum/#!topic/kubernetes-security-
announce/NLs2TGbfPdo) .

**All Google Kubernetes Engine (GKE)` gcloud ` versions are affected by this
vulnerability, and we recommend that you upgrade to the latest patch version
of ` gcloud ` when it becomes available. ** An upcoming patch version will
include a mitigation for this vulnerability.

######  What should I do?

A patched version of ` kubectl ` will be available in an upcoming ` gcloud `
release. You can also [ upgrade ` kubectl ` directly
](https://kubernetes.io/docs/tasks/tools/install-kubectl/) yourself.

Track the availability of this patch in the [ ` gcloud ` release notes
](/sdk/docs/release-notes) .

######  What vulnerability is addressed by this patch?

The vulnerability [ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11246) allows an attacker with access to a `
kubectl cp ` operation and code execution inside a container to modify files
on the host. This exploit potentially allows an attacker to replace or create
a file in the host file system

|

High

|

[ CVE-2019-11246 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664)  
  
##  June 18, 2019

Description  |  Severity  |  Notes  
---|---|---  
  
Docker recently discovered a vulnerability, [ CVE-2018-15664
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-15664) , that allows
an attacker that can execute code inside a container to hijack an externally-
initiated ` docker cp ` operation. This exploit potentially allows an attacker
to change where a file is being written, to an arbitrary location in the host
file system.

**All Google Kubernetes Engine (GKE) nodes running Docker are affected by this
vulnerability, and we recommend that you upgrade to the latest patch version
once available. An upcoming patch version will include a mitigation for this
vulnerability.**

**All Google Kubernetes Engine (GKE) masters older than version 1.12.7 are
running Docker and are affected by this vulnerability.** On GKE, users do not
have access to ` docker cp ` on the master and so the risk of this
vulnerability is limited for GKE masters.

#####  What should I do?

Only nodes running Docker are affected, and only when a ` docker cp ` (or API
equivalent) command that can be hijacked is issued. This is expected to be
fairly unusual in a Kubernetes environment. Nodes running [ COS with
containerd ](/kubernetes-engine/docs/concepts/using-containerd) are not
affected.

In order to upgrade your nodes, you must first [ upgrade your master
](/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading_the_cluster) to
the patched version. When the patch is available, you can either initiate a
master upgrade or wait for Google to auto-upgrade the master. The patch will
be available in Docker 18.09.7, included in an upcoming GKE patch. **This
patch will only be available for GKE versions 1.13 and above.**

We will upgrade cluster masters to the patched version automatically, at the
regular upgrade cadence. You can also initiate a master upgrade yourself after
the patched version becomes available.

We will update this bulletin with the versions containing a patch once
available. Track the availability of these patches in the [ release notes
](/kubernetes-engine/docs/release-notes) .

#####  What vulnerability is addressed by this patch?

The patch mitigates the following vulnerability:

The vulnerability [ CVE-2018-15664 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-15664) allows an attacker that can execute code
inside a container to hijack an externally-initiated ` docker cp ` operation.
This exploit potentially allows an attacker to change where a file is being
written, to an arbitrary location in the host file system.

|  High  |  
  
##  May 31, 2019

Description  |  Severity  |  Notes  
---|---|---  
  
This bulletin has been updated since its original publication.

######  August 2, 2019 Update

At the time of the initial bulletin, only 1.13.6-gke.0 through 1.13.6-gke.5
were impacted. Due to a regression all 1.13.6.x versions are now affected. If
you are runnuing 1.13.6 upgrade to 1.13.7 as soon as possible.

The Kubernetes project has disclosed [ CVE-2019-11245
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11245) in kubelet
v1.13.6 and v1.14.2, which can cause containers to run as UID 0 (typically
maps to the ` root ` user), even if a different user is specified in the
container image. **If your containers run as a non-root user and you are
running node version 1.13.6-gke.0 through 1.13.6-gke.6, we recommend you set`
RunAsUser ` on all Pods in the cluster whose containers should not run as UID
0. **

If a non-root ` USER ` value is specified (for example, by setting the value
of ` USER ` in a Dockerfile), unexpected behavior occurs. When a container
runs for the first time on a node, it correctly respects the specified UID.
However, due to this defect, on the second run (and subsequent runs) the
container runs as UID 0 regardless of the specified UID. This is usually an
undesired escalated privilege, and can lead to unexpected application
behavior.

#####  How do I know if I'm running an impacted version?

Run the following command to list all nodes and their kubelet version:

    
    
    kubectl get nodes -o=jsonpath='{range .items[*]}'\
    '{.status.nodeInfo.machineID}'\
    '{"\t"}{.status.nodeInfo.kubeletVersion}{"\n"}{end}'

If the output lists kubelet versions listed below, your nodes are impacted:

  * v1.13.6 
  * v1.14.2 

#####  How do I know if my specific configuration is affected?

If your containers run as a non-root user, and you are running node version
1.13.6-gke.0 through 1.13.6-gke.6 you are impacted except in the following
cases:

  * Pods that specify a valid non-root value for the ` runAsUser ` PodSecurityContext are unaffected and continue to work as expected. 
  * PodSecurityPolicies that enforce a ` runAsUser ` setting are also unaffected and continue to work as expected. 
  * Pods that specify ` mustRunAsNonRoot:true ` will not start as UID 0, but will fail to start when impacted by this issue. 

#####  What should I do?

Set the [ RunAsUser Security Context
](https://kubernetes.io/docs/tasks/configure-pod-container/security-
context/#set-the-security-context-for-a-pod) on all Pods in the cluster that
should not run as UID 0. You can apply this configuration using a [
PodSecurityPolicy ](https://kubernetes.io/docs/concepts/policy/pod-security-
policy/) .

|  Medium  |  [ CVE-2019-11245 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2019-11245)  
  
##  May 14, 2019

Description  |  Severity  |  Notes  
---|---|---  
  
**2019-06-11 Update:** The patch is available in 1.11.10-gke.4, 1.12.8-gke.6,
and 1.13.6-gke.5 released the week of 2019-05-28, and newer releases.

Intel has disclosed the following CVEs:

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130)
  * [ CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091)

These CVEs are collectively referred to as Microarchitectural Data Sampling
(MDS). These vulnerabilities potentially allow data to be exposed via the
interaction of speculative execution with microarchitectural state. For
further details, see the [ Intel disclosure
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) .

**The host infrastructure that runs Kubernetes Engine isolates customer
workloads from each other. Unless you are running untrusted code inside your
own multi-tenant GKE clusters, you are not impacted.**

**For customers running untrusted code in their own multi-tenant services
within Kubernetes Engine, this is a particularly severe vulnerability.** To
mitigate it in Kubernetes Engine, disable Hyper-Threading in your nodes. Only
Google Kubernetes Engine (GKE) nodes using multiple CPUs are affected by these
vulnerabilities. Note that n1-standard-1 (the GKE default), g1-small and
f1-micro VMs only expose 1 vCPU to the guest environment so there is no need
to disable Hyper-Threading.

Additional protections to enable flush functionality will be included in an
upcoming [ patch version ](/kubernetes-engine/release-notes) . We will upgrade
masters and nodes with auto-upgrade to the patched version automatically in
the coming weeks, at the regular upgrade cadence. **The patch alone is not
sufficient to mitigate exposure to this vulnerability. See below for
recommended actions.**

If you are running GKE on prem, you may be affected depending on the hardware
you are using. Please refer to the [ Intel disclosure
](https://www.intel.com/content/www/us/en/security-center/advisory/intel-
sa-00233.html) .

####  What should I do?

**Unless you are running untrusted code inside your own multi-tenant GKE
clusters, you are not impacted.**

**For nodes in Kubernetes Engine, create new node pools with Hyper-Threading
disabled and reschedule your workloads onto the new nodes.**

Note that n1-standard-1, g1-small, and f1-micro VMs only expose 1 vCPU to the
guest environment so there is no need to disable Hyper-Threading.

**Warning:**

  * Disabling Hyper-Threading might have severe performance impact on your clusters and application. Please ensure that this is acceptable before deploying this to your production clusters. 
  * Hyper-threading can be disabled at the GKE node pool level by deploying a DaemonSet. However, deploying this DaemonSet will result in all of your nodes in the node pool rebooting at the same time. Therefore, it is recommended to create a new node pool in your cluster, deploy the DaemonSet to disable Hyper-Threading in that node pool, and then migrate your workloads to the new node pool. 

To create a new node pool with Hyper-Threading disabled:

  1. Create a new node pool in your cluster with the node label ` cloud.google.com/gke-smt-disabled=true ` : 
    
        gcloud container node-pools create smt-disabled --cluster=[CLUSTER_NAME] \
        --node-labels=cloud.google.com/gke-smt-disabled=true

  2. Deploy the DaemonSet to this new node pool. The DaemonSet will only run on nodes with the ` cloud.google.com/gke-smt-disabled=true ` label. It will disable Hyper-Threading and then reboot the node. 
    
        kubectl create -f \
    https://raw.githubusercontent.com/GoogleCloudPlatform/\
    k8s-node-tools/master/disable-smt/gke/disable-smt.yaml

  3. Ensure that the DaemonSet pods are in running state. 
    
        kubectl get pods --selector=name=disable-smt -n kube-system

You should get a response similar to:

    
        NAME                READY     STATUS    RESTARTS   AGE
    
    disable-smt-2xnnc   1/1       Running   0          6m

  4. Check that “SMT has been disabled” appears in the logs of the pods. 
    
        kubectl logs disable-smt-2xnnc disable-smt -n kube-system

Note: Boot options cannot be modified if the node has [ Secure Boot
](/kubernetes-engine/docs/how-to/shielded-gke-nodes#secure_boot) feature
enabled. If Secure Boot is enabled, it needs to be [ disabled ](/kubernetes-
engine/docs/how-to/shielded-gke-nodes#disabling) before the DaemonSet is
created.

You must keep the DaemonSet running on the nodepools so that new nodes created
in the pool will have the changes applied automatically. Node creations can be
triggered by node auto repair, manual or auto upgrade, and auto-scaling.

To re-enable Hyper-Threading, you will need to recreate the node pool without
deploying the provided DaemonSet, and migrate your workloads to the new node
pool.

We also recommend that you manually upgrade your nodes once the patch becomes
available. In order to upgrade, you must first [ upgrade your master
](/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading_the_cluster) to
the newest version. GKE masters will automatically be upgraded at the regular
upgrade cadence.

We will update this bulletin with the versions containing a patch once
available.

####  What vulnerability is addressed by this patch?

The patch mitigates the following vulnerabilities:

[ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12126)
, [ CVE-2018-12127 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2018-12127) , [ CVE-2018-12130
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2018-12130) , [
CVE-2019-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-11091) :
These vulnerabilities exploit speculative execution. These CVEs are
collectively referred to as Microarchitectural Data Sampling. These
vulnerabilities potentially allow data to be exposed via the interaction of
speculative execution with microarchitectural state.  |  Medium  |

  * [ CVE-2018-12126 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12126)
  * [ CVE-2018-12127 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12127)
  * [ CVE-2018-12130 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-12130)
  * [ CVE-2018-11091 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11091)

  
  
##  April 5, 2019

Description  |  Severity  |  Notes  
---|---|---  
  
Recently, the security vulnerabilities [ CVE-2019-9900
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900) and [
CVE-2019-9901. ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)
were discovered in [ Envoy ](https://www.envoyproxy.io/) .

[ Istio ](https://istio.io/) embeds Envoy, and these vulnerabilities allow
Istio policy to be bypassed in some cases.

If you have enabled Istio on Google Kubernetes Engine (GKE), you may be
affected by these vulnerabilities. **We recommend upgrading your affected
clusters to the latest patch version as soon as possible, and upgrading your
Istio sidecars (instructions below).**

####  What should I do?

**Due to the severity of these vulnerabilities, whether you have node auto-
upgrades enabled or not, we recommend that you:

  1. [ Manually upgrade ](/kubernetes-engine/docs/how-to/upgrading-a-cluster) your cluster as soon as the patch becomes available. 
  2. Upgrade your sidecars by following the [ sidecar upgrade documentation ](https://archive.istio.io/v1.5/docs/setup/upgrade/cni-helm-upgrade/#control-plane-upgrade) . 

**

The patched versions will be made available for all GKE projects before 7:00
PM PDT today.

This patch will be available in the below GKE versions. New clusters will use
the patched version by default when announced on the GKE security bulletins
page, expected on April 15th, 2019; if you create a new cluster before then,
you must specify the patched version for it to use. GKE customers who have [
node auto-upgrades ](/kubernetes-engine/docs/how-to/node-auto-upgrades)
enabled, and who do not manually upgrade, will have their nodes auto-upgraded
to patched versions in the following week.

Patched Versions:

  * 1.10.12-gke.14 
  * 1.11.6-gke.16 
  * 1.11.7-gke.18 
  * 1.11.8-gke.6 
  * 1.12.6-gke.10 
  * 1.13.4-gke.10 

####  What vulnerability is addressed by this patch?

The patch mitigates the following vulnerabilities:

[ CVE-2019-9900 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9900) and [ CVE-2019-9901.
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901) You can read
more about them on the [ Istio blog.
](https://istio.io/blog/2019/announcing-1.1.2)

|  High  |

  * [ CVE-2019-9900 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900)
  * [ CVE-2019-9901. ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9901)

  
  
##  March 1, 2019

Description  |  Severity  |  Notes  
---|---|---  
  
**2019-03-22 Update:** This patch is available in Kubernetes 1.11.8-gke.4,
1.13.4-gke.1, and newer releases. The patch is not yet available in 1.12.
Track the availability of these patches in the [ release notes ](/kubernetes-
engine/docs/release-notes-archive#march_19_2019) .

Kubernetes recently discovered a new denial of service vulnerability [
CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) , allowing a user authorized to make
patch requests to craft a malicious "json-patch" request that consumes
excessive amounts of CPU and memory in the Kubernetes API server, potentially
reducing the availability of the cluster control plane. For further details,
see the [ Kubernetes disclosure
](https://groups.google.com/forum/#!topic/kubernetes-announce/vmUUNkYfG9g) .
**All Google Kubernetes Engine (GKE) masters are affected by these
vulnerabilities. An upcoming patch version will include a mitigation for this
vulnerability. We will upgrade cluster masters to the patched version
automatically in the coming weeks, at the regular upgrade cadence.**

####  What should I do?

**No action is required. GKE masters will automatically be upgraded at the
regular upgrade cadence.** If you wish to upgrade your master sooner, you can
[ manually initiate a master upgrade ](/kubernetes-engine/docs/how-
to/upgrading-a-cluster#upgrading_the_cluster) .

We will update this bulletin with the versions containing a patch. Note that
the patch will only be available in versions 1.11+, not also in 1.10.

####  What vulnerability is addressed by this patch?

The patch mitigates the following vulnerability:

The vulnerability [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100) allows a user to specially craft a
patch of type "json-patch" that consumes excessive amounts of CPU in the
Kubernetes API server, potentially reducing the availability of the cluster
control plane.

|  Medium  |  [ CVE-2019-1002100 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-1002100)  
  
##  February 11, 2019 (runc)

Description  |  Severity  |  Notes  
---|---|---  
  
The Open Containers Initiative (OCI) [ recently discovered
](https://groups.google.com/a/opencontainers.org/forum/m/#!topic/dev/Tc1ELm-8oDI)
a new security vulnerability [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) in runc, allowing container escape to
obtain root privileges on the host node.

**Your Google Kubernetes Engine (GKE) Ubuntu nodes are affected by these
vulnerabilities, and we recommend that you[ upgrade ](/kubernetes-
engine/docs/how-to/upgrading-a-cluster) to the latest patch version as soon as
possible, as we detail below. **

####  What should I do?

In order to upgrade your nodes, you must first upgrade your master to the
newest version. This patch is available in Kubernetes 1.10.12-gke.7,
1.11.6-gke.11, 1.11.7-gke.4, 1.12.5-gke.5 and newer releases. Track the
availability of these patches in the [ release notes ](/kubernetes-
engine/docs/release-notes-archive#february-11-2019) .

Note that only Ubuntu nodes in GKE are affected. Nodes running COS are not
affected.

Note that the new version of runc has increased memory usage and may require
updating memory allocated to containers if you have set low memory limits (<
16MB).

####  What vulnerability is addressed by this patch?

The patch mitigates the following vulnerability:

[ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736) describes a vulnerability in runc that
allows a malicious container to (with minimal user interaction in the form of
an exec) overwrite the host runc binary and thus gain root-level code
execution on the host node. Containers not running as root are unaffected.
This is rated as a 'High' severity vulnerability.

|  High  |  [ CVE-2019-5736 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-5736)  
  
##  February 11, 2019 (Go)

Description  |  Severity  |  Notes  
---|---|---  
  
**2019-02-25 Update:** The patch is not available in 1.11.7-gke.4 as
previously communicated. If you are running 1.11.7, you can: downgrade to
1.11.6, upgrade to 1.12, or wait until the next 1.11.7 patch available the
week of 2019-03-04.

The Go programming language recently discovered a new security vulnerability [
CVE-2019-6486 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-6486)
, which is a Denial of Service (DoS) vulnerability in the crypto/elliptic
implementations of the P-521 and P-384 elliptic curves. In Google Kubernetes
Engine (GKE), this could allow a user to craft malicious requests that consume
excessive amounts of CPU in the Kubernetes API server, potentially reducing
the availability of the cluster control plane. For further details, see the [
Go programming language disclosure
](https://groups.google.com/forum/#!topic/golang-announce/mVeX35iXuSw) .

**All Google Kubernetes Engine (GKE) masters are affected by these
Vulnerabilities. The[ latest patch version ](/kubernetes-engine/docs/release-
notes#february-11-2019) Includes a mitigation for this vulnerability. We will
upgrade cluster masters to the patched version automatically in the coming
weeks, at the regular upgrade cadence. **

####  What should I do?

**No action is required. GKE masters will automatically be upgraded at the
regular upgrade cadence.** If you wish to upgrade your master sooner, you can
[ manually initiate a master upgrade ](/kubernetes-engine/docs/how-
to/upgrading-a-cluster#upgrading_the_cluster) .

This patch is available in GKE 1.10.12-gke.7, 1.11.6-gke.11, 1.11.7-gke.4,
1.12.5-gke.5, and newer releases.

####  What vulnerability is addressed by this patch?

The patch mitigates the following vulnerability:

CVE-2019-6486 is a vulnerability in the crypto/elliptic implementations of the
P-521 and P-384 elliptic curves. This allows a user to craft inputs that
consume excessive amounts of CPU.

|  High  |  [ CVE-2019-6486 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-6486)  
  
##  December 3, 2018

Description  |  Severity  |  Notes  
---|---|---  
  
Kubernetes recently discovered a new security vulnerability [ CVE-2018-1002105
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1002105) , allowing
a user with relatively low privileges to bypass authorization to the kubelet's
APIs, giving the ability to execute arbitrary operations for any Pod on any
node in the cluster. For further details, see the [ Kubernetes disclosure
](https://groups.google.com/forum/#!topic/kubernetes-announce/GVllWCg6L88) .
**All Google Kubernetes Engine (GKE) masters were affected by these
vulnerabilities, and we have already upgraded clusters to the[ latest patch
versions ](/kubernetes-engine/docs/release-notes-archive#november-12-2018) .
No action is required. **

####  What should I do?

**No action is required. GKE masters have already been upgraded.**

This patch is available in GKE 1.9.7-gke.11, 1.10.6-gke.11, 1.10.7-gke.11,
1.10.9-gke.5, and 1.11.2-gke.18 and newer releases.

####  What vulnerability is addressed by this patch?

The patch mitigates the following vulnerability:

The vulnerability CVE-2018-1002105 allows a user with relatively low
privileges to bypass authorization to the kubelet's APIs. This gives a user
authorized to make upgradable requests to escalate and make arbitrary calls to
the kubelet's API. This is rated as a Critical vulnerability in Kubernetes.
Given some details in GKE's implementation that prevented the unauthenticated
escalation path, this is rated as a High vulnerability.

|  High  |  [ CVE-2018-1002105 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1002105)  
  
##  November 13, 2018

Description  
---  
  
**2018-11-16 Update:** The revocation and rotation of all potentially impacted
tokens is complete. No further action is required.

Google recently discovered an issue in the Calico Container Network Interface
(CNI) plugin which can, in certain configurations, log sensitive information.
This issue is tracked under Tigera Technical Advisory [ TTA-2018-001
](https://www.projectcalico.org/security-bulletins/) .

  * When running with debug-level logging, the Calico CNI plugin will write Kubernetes API client configuration into the logs. 
  * The Calico CNI will also write the Kubernetes API token to the logs at the info level if the "k8s_auth_token" field is set on the CNI network configuration. 
  * Additionally, when running with debug-level logging, if the service account token is explicitly set, either in the Calico configuration file read by Calico, or as environment variables used by Calico, then Calico components (calico/node, felix, CNI) will write this information to the log files. 

These tokens have the following permissions:  
      
    
    bgpconfigurations.crd.projectcalico.org     [create get list update watch]
    bgppeers.crd.projectcalico.org              [create get list update watch]
    clusterinformations.crd.projectcalico.org   [create get list update watch]
    felixconfigurations.crd.projectcalico.org   [create get list update watch]
    globalbgpconfigs.crd.projectcalico.org      [create get list update watch]
    globalfelixconfigs.crd.projectcalico.org    [create get list update watch]
    globalnetworkpolicies.crd.projectcalico.org [create get list update watch]
    globalnetworksets.crd.projectcalico.org     [create get list update watch]
    hostendpoints.crd.projectcalico.org         [create get list update watch]
    ippools.crd.projectcalico.org               [create get list update watch]
    networkpolicies.crd.projectcalico.org       [create get list update watch]
    nodes                                       [get list update watch]
    pods                                        [get list watch patch]
    namespaces                                  [get list watch]
    networkpolicies.extensions                  [get list watch]
    endpoints                                   [get]
    services                                    [get]
    pods/status                                 [update]
    networkpolicies.networking.k8s.io           [watch list]
            
  
---  
  
Google Kubernetes Engine Clusters with a Cluster Network Policy and
Stackdriver Logging enabled, logged Calico service account tokens to
Stackdriver. Clusters without Network Policy enabled are unaffected.

We have deployed a fix that migrates the Calico CNI plugin to only log at the
warning level, and use a new service account. The patched calico code will be
deployed in a later release.

Over the course of the next week, we will perform a rolling revocation of any
potentially impacted tokens. This bulletin will be updated when the revocation
is complete. **No further action on your part is required.** (This rotation
was completed on 2018-11-16)

If you wish to rotate these tokens immediately you can run the following
command, the new secret for the service account should be re-created
automatically within a few seconds:  
  
kubectl get sa --namespace kube-system calico -o template --template '{{(index
.secrets 0).name}}' | xargs kubectl delete secret --namespace kube-system  
---  
  
####  Detection

GKE logs all access to the API server. To determine if a Calico token was used
from outside Google Cloud's expected IP range, you can run the following
Stackdriver query. Please note this will only return records for calls made
from outside GCP's network. You should customize it as needed for your
specific environment.  
  
---  
      
    
    resource.type="k8s_cluster"
    protoPayload.authenticationInfo.principalEmail="system:serviceaccount:kube-system:calico"
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.34.208.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.35.192.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "8.35.200.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.59.80.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.192.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.208.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.216.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.220.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "108.170.222.0/24")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.224.0.0/13")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "162.216.148.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "162.222.176.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "173.255.112.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "192.158.28.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.192.112.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.223.232.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "199.223.236.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "23.236.48.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "23.251.128.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.204.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.208.0.0/13")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "107.167.160.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "107.178.192.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.2.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.4.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.8.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.16.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.32.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "146.148.64.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.192.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.240.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.8.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.16.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.32.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.64.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.128.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "104.154.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "104.196.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "208.68.108.0/23")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.184.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.188.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.202.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.192.0/19")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.224.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.192.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.196.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.198.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.199.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.199.128.0/18")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.200.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "2600:1900::/35")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.190.224.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.232.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.234.0.0/16")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.0.0/17")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.235.192.0/20")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.236.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.240.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.203.232.0/21")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "130.211.4.0/22")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.220.0.0/14")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.242.0.0/15")
    NOT ip_in_net(protoPayload.requestMetadata.callerIp, "35.244.0.0/14")
            
  
---  
  
##  August 14, 2018

Description  |  Severity  |  Notes  
---|---|---  
  
[ Intel has disclosed ](https://www.intel.com/content/www/us/en/architecture-
and-technology/l1tf.html) the following CVEs:

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615) (for [ SGX ](https://en.wikipedia.org/wiki/Software_Guard_Extensions) ) 
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620) (for operating systems and [ SMT ](https://en.wikipedia.org/wiki/Hyper-threading) ) 
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646) (for virtualization) 

These CVEs are collectively referred to as "L1 Terminal Fault (L1TF)".

These L1TF vulnerabilities exploit speculative execution by attacking the
configuration of processor-level data structures. "L1" refers to the Level-1
Data cache (L1D), a small on-core resource used to accelerate memory access.

Read the [ Google Cloud blog post
](https://cloud.google.com/blog/products/gcp/protecting-against-the-new-l1tf-
speculative-vulnerabilities) for more details on these vulnerabilities and
Compute Engine's mitigations.

####  Google Kubernetes Engine impact

The infrastructure that runs Kubernetes Engine and isolates customer Clusters
and Nodes from each other is protected against known attacks.

Kubernetes Engine node pools that use Google's Container-Optimized OS image,
and who have [ auto-upgrade ](https://cloud.google.com/kubernetes-
engine/docs/concepts/node-auto-upgrades) enabled, will be automatically
updated to patched versions of our COS image as they become available starting
the week of 2018-08-20.

Kubernetes Engine node pools that do not have [ auto-upgrade
](https://cloud.google.com/kubernetes-engine/docs/concepts/node-auto-upgrades)
enabled must [ manually upgrade ](https://cloud.google.com/kubernetes-
engine/docs/how-to/upgrading-a-container-cluster) as patched versions of our
COS image become available.

|  High  |

  * [ CVE-2018-3615 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3615)
  * [ CVE-2018-3620 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3620)
  * [ CVE-2018-3646 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-3646)

  
  
##  August 6, 2018; last updated: September 5th, 2018

Description  |  Severity  |  Notes  
---|---|---  
  
####  2018-09-05 Update

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) was recently disclosed. As with [
CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
, this is a kernel-level networking vulnerability that increases the
effectiveness of denial of service (DoS) attacks against vulnerable systems.
The main difference is that CVE-2018-5391 is exploitable over IP connections.
We updated this bulletin to cover both of these vulnerabilities.

####  Description

[ CVE-2018-5390 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5390) ("SegmentSmack") describes a kernel-level
networking vulnerability that increases the effectiveness of denial of service
(DoS) attacks against vulnerable systems over TCP connections.

[ CVE-2018-5391 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-5391) ("FragmentSmack") describes a kernel-level
networkingvulnerability that increases the effectiveness of denial of service
(DoS) attacks against vulnerable systems over IP connections.

####  Google Kubernetes Engine impact

As of 2018-08-11, all Kubernetes Engine masters are protected against both
vulnerabilities. Also, all Kubernetes Engine clusters that are configured to
automatically upgrade are also protected against both vulnerabilities.
Kubernetes Engine node pools that are not configured to [ automatically
upgrade ](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster) , and were last manually upgraded before 2018-08-11, are affected by
both vulnerabilities.

####  Patched versions

Due to the severity of this vulnerability, we recommend you [ manually upgrade
](https://cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-
cluster#upgrading-nodes) your nodes as soon as the patch becomes available.

|  High  |

  * [ CVE-2018-5390 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5390)
  * [ CVE-2018-5391 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5391)

  
  
##  May 30, 2018

Description  |  Severity  |  Notes  
---|---|---  
  
A vulnerability was recently discovered in Git which may allow escalation of
privileges in Kubernetes if unprivileged users are allowed to create Pods with
gitRepo volumes. The CVE is identified with the tag [ CVE-2018-11235
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11235) .

####  Am I affected?

This vulnerability affects you if all of the following are true:

  * Untrusted users can create Pods (or trigger Pod creation). 
  * Pods created by untrusted users have restrictions preventing host root access (for example, via [ PodSecurityPolicy ](/kubernetes-engine/docs/how-to/pod-security-policies) ). 
  * Pods created by untrusted users are allowed to use the gitRepo volume type. 

All Kubernetes Engine nodes are vulnerable.

####  What should I do?

Forbid the use of the gitRepo volume type. To forbid gitRepo volumes with
PodSecurityPolicy, omit ` gitRepo ` from the ` volumes ` whitelist in your
PodSecurityPolicy.

Equivalent gitRepo volume behavior can be achieved by cloning a git repository
into an EmptyDir volume from an initContainer:

    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: git-repo-example
    spec:
      initContainers:
        # This container clones the desired git repo to the EmptyDir volume.
        - name: git-clone
          image: alpine/git # Any image with git will do
          args:
            - clone
            - --single-branch
            - --
            - https://github.com/kubernetes/kubernetes # Your repo
            - /repo # Put it in the volume
          securityContext:
            runAsUser: 1 # Any non-root user will do. Match to the workload.
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
          volumeMounts:
            - name: git-repo
              mountPath: /repo
      containers:
        ...
      volumes:
        - name: git-repo
          emptyDir: {}

####  What patch addresses this vulnerability?

A patch will be included in an upcoming Kubernetes Engine release. Please
check back here for details.

|  Medium  |

  * [ CVE-2018-11235 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11235)

  
  
##  May 21, 2018

Description  |  Severity  |  Notes  
---|---|---  
  
Several vulnerabilities were recently discovered in the Linux kernel which may
allow escalation of privileges or denial of service (via kernel crash) from an
unprivileged process. These CVEs are identified with tags [ CVE-2018-1000199
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199) , [
CVE-2018-8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
, and [ CVE-2018-1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) . All Kubernetes Engine nodes are affected
by these vulnerabilities, and we recommend that you [ upgrade ](/kubernetes-
engine/docs/how-to/upgrading-a-container-cluster) to the latest patch version,
as detailed below.

####  What should I do?

In order to upgrade, you must first upgrade your master to the newest version.
This patch is available in Kubernetes Engine 1.8.12-gke.1, Kubernetes Engine
1.9.7-gke.1, and Kubernetes Engine 1.10.2-gke.1. These releases include
patches for both Container-Optimized OS and Ubuntu images.

If you create a new cluster before then, you must specify the patched version
for it to be used. Customers who have [ node auto-upgrades ](/kubernetes-
engine/docs/concepts/node-auto-upgrades) enabled and who do not manually
upgrade will have their nodes upgraded to patched versions in the coming
weeks.

####  What vulnerabilities are addressed by this patch?

The patch mitigates the following vulnerabilities:

[ CVE-2018-1000199 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1000199) : This vulnerability affects the Linux
kernel. It allows an unprivileged user or process to crash the system kernel,
leading to a DoS attack or privilege escalation. This is rated as a High
vulnerability, with a CVSS of 7.8.

[ CVE-2018-8897 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-8897) : This vulnerability affects the Linux
kernel. It allows an unprivileged user or process to crash the system kernel,
leading to a DoS attack. This is rated as a Medium vulnerability, with a CVSS
of 6.5.

[ CVE-2018-1087 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2018-1087) : This vulnerability affects Linux
kernel's KVM hypervisor. This allows an unprivileged process to crash the
guest kernel or potentially gain privileges. This vulnerability is patched in
the infrastructure that Kubernetes Engine runs on, so Kubernetes Engine is
unaffected. This is rated as a High vulnerability, with a CVSS score of 8.0.

|  High  |

  * [ CVE-2018-1000199 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1000199)
  * [ CVE-2018-8897 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-8897)
  * [ CVE-2018-1087 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1087)

  
  
##  March 12, 2018

Description  |  Severity  |  Notes  
---|---|---  
  
The Kubernetes project [ recently disclosed
](https://groups.google.com/forum/#!topic/kubernetes-security-
announce/P7lBjbjDKd8) new security vulnerabilities, [ CVE-2017-1002101
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101) and [
CVE-2017-1002102 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=2017-1002102) , allowing containers to access files
outside the container. All Kubernetes Engine nodes are affected by these
vulnerabilities, and we recommend that you upgrade to the latest patch version
as soon as possible, as we detail below.

####  What should I do?

Due to the severity of these vulnerabilities, whether you have node auto-
upgrades enabled or not, we recommend that you [ manually upgrade
](/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your nodes as
soon as the patch becomes available. The patch will be available for all
customers by March 16th, but it may be available for you sooner based on the
zone your cluster is in, according to the [ release schedule ](/kubernetes-
engine/docs/release-notes-archive#march-12-2018) .

In order to upgrade, you must first upgrade your master to the newest version.
This patch will be available in Kubernetes 1.9.4-gke.1, Kubernetes
1.8.9-gke.1, and Kubernetes 1.7.14-gke.1. New clusters will use the patched
version by default by March 30; if you create a new cluster before then, you
must specify the patched version for it to be used.

Kubernetes Engine customers who have [ node auto-upgrades ](/kubernetes-
engine/docs/concepts/node-auto-upgrades) enabled and who do not manually
upgrade will have their nodes upgraded to patched versions by April 23rd.
However, due to the nature of the vulnerability, we recommend you [ manually
upgrade ](/kubernetes-engine/docs/how-to/upgrading-a-container-cluster) your
nodes as soon as the patch is available to you.

####  What vulnerabilities are addressed by this patch?

The patch mitigates the following two vulnerabilities:

The vulnerability CVE-2017-1002101 allows containers using [ subpath
](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath) volume
mounts to access files outside of the volume. This means that if you are
blocking container access to hostpath volumes with PodSecurityPolicy, an
attacker with the ability to update or create pods can mount any hostpath
using any other volume type.

The vulnerability CVE-2017-1002102 allows containers using certain volume
types - including secrets, config maps, projected volumes, or downward API
volumes - to delete files outside of the volume. This means that if a
container using one of these volume types is compromised, or if you allow
untrusted users to create pods, an attacker could use that container to delete
arbitrary files on the host.

To learn more about the fix, read the [ Kubernetes blog post
](https://kubernetes.io/blog/2018/04/04/fixing-subpath-volume-vulnerability/)
.

|  High  |

  * [ CVE-2017-1002101 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002101)
  * [ CVE-2017-1002102 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2017-1002102)

