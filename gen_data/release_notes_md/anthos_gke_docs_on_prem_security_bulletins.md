#  Security bulletins

All security bulletins for Anthos GKE on-prem (GKE on-prem) are described in
this topic.

Vulnerabilities are often kept secret under embargos until affected parties
have had a chance to address them. In these cases, GKE on-prem's [ Release
notes ](/anthos/gke/docs/on-prem/release-notes) will refer to "security
updates" until the embargo has been lifted. At that point the notes will be
updated to reflect the vulnerability the patch addressed.

**Note:** If you run multi-tenant workloads on GKE on-prem, please pay
particular attention to these bulletins. These vulnerabilities are more likely
to impact multi-tenant workloads. For a technical description of security
boundaries in GKE on-prem and how these impact workloads, see [ Isolation at
different layers of the Kubernetes stack
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) .

To get the latest security bulletins delivered to you, add the URL of this
page to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) .

##  GCP-2020-009

**Published:** 2020-07-15  Description  |  Severity  |  Notes  
---|---|---  
  
A privilege escalation vulnerability, [ CVE-2020-8559
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8559) , was recently
discovered in Kubernetes. This vulnerability allows an attacker that has
already compromised a node to execute a command in any Pod in the cluster. The
attacker can thereby use the already compromised node to compromise other
nodes and potentially read information, or cause destructive actions.

Note that for an attacker to exploit this vulnerability, a node in your
cluster must have already been compromised. This vulnerability, by itself,
will not compromise any nodes in your cluster.

####  What should I do?

[ Upgrade ](/anthos/gke/docs/on-prem/how-to/upgrading) your cluster to a
patched version. The following upcoming GKE on-prem versions or newer contain
the fix for this vulnerability:

  * Anthos 1.3.3 
  * Anthos 1.4.1 

####  What vulnerability is addressed by this patch?

These patches mitigate vulnerability CVE-2020-8559. This is rated as a Medium
vulnerability for GKE, as it requires the attacker to have first hand
information about the cluster, nodes, and workloads to effectively leverage
this attack in addition to an existing compromised node. This vulnerability by
itself will not provide an attacker with a compromised node.

|

Medium

|

[ CVE-2020-8559 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-8559)  
  
##  GCP-2020-007

**Published:** 2020-06-01  
Description  |  Severity  |  Notes  
---|---|---  
  
Server Side Request Forgery (SSRF) vulnerability, [ CVE-2020-8555
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555) , was recently
discovered in Kubernetes, allowing certain authorized users to leak up to 500
bytes of sensitive information from the control plane host network. The Google
Kubernetes Engine (GKE) control plane uses controllers from Kubernetes and is
thus affected by this vulnerability. We recommend that you upgrade the control
plane to the latest patch version, as we detail below. A node upgrade is not
required.  

####  What should I do?

The following Anthos GKE on-prem (GKE on-prem) versions or newer contain the
fix for this vulnerability:

  * Anthos 1.3.0 

If you are using a previous version, [ upgrade your existing cluster
](/anthos/gke/docs/on-prem/how-to/upgrading) to a version containing the fix.

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
recommend that you upgrade to the latest patch version, as we detail below.

####  What should I do?

To mitigate this vulnerability for Anthos GKE on-prem (GKE on-prem), [ upgrade
your clusters ](/anthos/gke/docs/on-prem/how-to/upgrading) to the following
version or newer:

  * Anthos 1.3.2 

Very few containers typically require ` CAP_NET_RAW ` . This and other
powerful capabilities should be blocked by default through [ Anthos Policy
Controller ](/anthos-config-management/docs/concepts/policy-controller) or by
updating your Pod specs:

  * Drop the ` CAP_NET_RAW ` capability from containers: 
    * By using Anthos Policy Controller/Gatekeeper with this [ constraint template ](https://github.com/open-policy-agent/gatekeeper/blob/master/library/pod-security-policy/capabilities/template.yaml) and applying it, for example: 
        
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
        

    * By updating your Pod specs: 
        
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
  
  
##  GCP-2020-004

Description  |  Severity  |  Notes  
---|---|---  
  
A vulnerability was recently discovered in Kubernetes, described in [
CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) , which allows any user authorized to
make POST requests to execute a remote Denial-of-Service attack on a
Kubernetes API server. The Kubernetes Product Security Committee (PSC)
released additional information on this vulnerability which can be found [
here ](https://groups.google.com/g/kubernetes-security-announce/c/wuwEwZigXBc)
.

You can mitigate this vulnerability by limiting which clients have network
access to your Kubernetes API servers.

####  What should I do?

We recommend that you upgrade your clusters to patch versions containing the
fix for this vulnerability as soon as they are available.

The patch versions which contain the fix are listed below:

  * Anthos 1.3.0, which runs Kubernetes version 1.15.7-gke.32 

####  What vulnerabilities are addressed by this patch?

The patch fixes the following Denial-of-Service (DoS) vulnerability:

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254) .

|

Medium

|

[ CVE-2019-11254 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11254)  
  
##  October 16, 2019

Description  |  Severity  |  Notes  
---|---|---  
  
A vulnerability was recently discovered in Kubernetes, described in [
CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) , which allows any user authorized to
make POST requests to execute a remote Denial-of-Service attack on a
Kubernetes API server. The Kubernetes Product Security Committee (PSC)
released additional information on this vulnerability which can be found [
here ](https://groups.google.com/forum/#!topic/kubernetes-security-
announce/jk8polzSUxs) .

You can mitigate this vulnerability by limiting which clients have network
access to your Kubernetes API servers.

######  What should I do?

We recommend that you [ upgrade your clusters ](/anthos/gke/docs/on-prem/how-
to/upgrading#clusters) to a patch version containing the fix as soon as they
are available.

The patch versions which will contain the fix are listed below:

  * Anthos 1.1.1, which runs Kubernetes version 1.13.7-gke.30 

######  What vulnerability is addressed by this patch?

The patch mitigates the following vulnerability: [ CVE-2019-11253
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253) .

|

High

|

[ CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253)  
  
##  August 23, 2019

Description  |  Severity  |  Notes  
---|---|---  
  
We recently discovered and mitigated a vulnerability where the RBAC proxy used
for securing monitoring endpoints did not correctly authorize users. As a
result, metrics from certain components are available to unauthorized users
from within the internal cluster network. The following components were
affected:

  * ` etcd `
  * ` etcd-events `
  * ` kube-apiserver `
  * ` kube-controller-manager `
  * ` kube-scheduler `
  * ` node-exporter `
  * ` kube-state-metrics `
  * ` prometheus `
  * ` alertmanager `

######  What should I do?

We recommend that you [ upgrade ](/anthos/gke/docs/on-prem/how-
to/upgrading#clusters) your clusters to version [ 1.0.2-gke.3
](/anthos/gke/docs/on-prem/downloads#gkectl_latest) , which includes the patch
for this vulnerability, as soon as possible.

|

Medium

|

[ Anthos GKE on-prem releases ](/anthos/gke/docs/on-
prem/downloads#gkectl_latest)  
  
##  August 22, 2019

Description  |  Severity  |  Notes  
---|---|---  
  
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

We recommend that you [ upgrade ](/anthos/gke/docs/on-prem/how-to/upgrading-
clusters) your clusters to version [ 1.0.2-gke.3 ](/anthos/gke/docs/on-
prem/downloads#gkectl_latest) , which includes the patch for this
vulnerability, as soon as possible.

######  What vulnerability is addressed by this patch?

The patch mitigates the following vulnerability: [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Medium

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

