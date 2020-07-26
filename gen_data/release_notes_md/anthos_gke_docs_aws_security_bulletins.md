A new version of Anthos GKE on AWS was released on July 24. See the [ release
notes ](/anthos/gke/docs/aws/release-notes) for information on breaking
changes.

#  Security bulletins

Learn about security bulletins for Anthos GKE on AWS (GKE on AWS).

##  GCP-2020-011

**Published:** 2020-07-24  
Description  |  Severity  |  Notes  
---|---|---  
  
A networking vulnerability, [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) , was recently
discovered in Kubernetes. Services sometimes communicate with other
applications running inside the same Pod using the local loopback interface
(127.0.0.1). This vulnerability allows an attacker with access to the
cluster's network to send traffic to the loopback interface of adjacent Pods
and nodes. Services that rely on the loopback interface not being accessible
outside their Pod could be exploited.

Exploiting this vulnerability on GKE on AWS clusters requires an attacker to
disable [ source destination checks
](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html) on
the EC2 instances in the cluster. This requires the attacker to have AWS IAM
permissions for ` ModifyInstanceAttribute ` or `
ModifyNetworkInterfaceAttribute ` on the EC2 instances. For this reason, this
vulnerability has been assigned a Low severity for GKE on AWS.

####  What should I do?

To fix this vulnerability, upgrade your cluster to a patched version. The
following upcoming GKE on AWS versions or newer are expected to include the
fix for this vulnerability:

  * GKE on AWS 1.4.2 

####  What vulnerability is addressed by this patch?

This patch fixes the following vulnerability: [ CVE-2020-8558
](https://github.com/kubernetes/kubernetes/issues/92315) .

|

Low

|

[ CVE-2020-8558 ](https://github.com/kubernetes/kubernetes/issues/92315)  
  
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

GKE on AWS GA (1.4.1, available end of July, 2020) or newer includes the patch
for this vulnerability. If you are using a previous version, [ download a new
version of the anthos-gke command line tool ](/anthos/gke/docs/aws/how-
to/prerequisites) and recreate your management and user clusters.

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

Anthos GKE on AWS (GKE on AWS) v0.2.0 or newer already includes the patch for
this vulnerability. If you are using a previous version, [ download a new
version of the anthos-gke command line tool ](/anthos/gke/docs/aws/how-
to/prerequisites) and recreate your management and user clusters.

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

[ Download the anthos-gke command line tool
](https://cloud.google.com/anthos/gke/docs/aws/how-to/prerequisites) with the
following version or newer and recreate your management and user clusters:

  * aws-0.2.1-gke.7 

Very few containers typically require ` CAP_NET_RAW ` . This and other
powerful capabilities should be blocked by default through [ Anthos Policy
Controller ](/anthos-config-management/docs/concepts/policy-controller) or by
updating your Pod specs:

Drop the ` CAP_NET_RAW ` capability from containers:

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

