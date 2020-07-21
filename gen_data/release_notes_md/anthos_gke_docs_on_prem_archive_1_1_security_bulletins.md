You are viewing documentation for a previous version of GKE On-Prem. [ View
the latest documentation ](/anthos/gke/docs/on-prem) .

#  Security bulletins

All security bulletins for GKE On-Prem are described in this topic.

Vulnerabilities are often kept secret under embargos until affected parties
have had a chance to address them. In these cases, GKE On-Prem's [ Release
Notes ](/anthos/gke/docs/on-prem/archive/1.1/release-notes) will refer to
"security updates" until the embargo has been lifted. At that point the notes
will be updated to reflect the vulnerability the patch addressed.

**Note:** If you run multi-tenant workloads on GKE On-Prem, please pay
particular attention to these bulletins. These vulnerabilities are more likely
to impact multi-tenant workloads. For a technical description of security
boundaries in GKE On-Prem and how these impact workloads, see [ Isolation at
different layers of the Kubernetes stack
](https://cloudplatform.googleblog.com/2018/05/Exploring-container-security-
Isolation-at-different-layers-of-the-Kubernetes-stack.html) .

To get the latest security bulletins delivered to you, add the URL of this
page to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) .

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

We recommend that you [ upgrade your clusters ](/anthos/gke/docs/on-
prem/archive/1.1/how-to/administration/upgrading-clusters) to a patch version
containing the fix as soon as they are available.

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

We recommend that you [ upgrade ](/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/upgrading-clusters) your clusters to version [ 1.0.2-gke.3
](/anthos/gke/docs/on-prem/archive/1.1/downloads#gkectl_latest) , which
includes the patch for this vulnerability, as soon as possible.

|

Medium

|

[ GKE On-Prem releases ](/anthos/gke/docs/on-
prem/archive/1.1/downloads#gkectl_latest)  
  
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

We recommend that you [ upgrade ](/anthos/gke/docs/on-prem/archive/1.1/how-
to/administration/upgrading-clusters) your clusters to version [ 1.0.2-gke.3
](/anthos/gke/docs/on-prem/archive/1.1/downloads#gkectl_latest) , which
includes the patch for this vulnerability, as soon as possible.

######  What vulnerability is addressed by this patch?

The patch mitigates the following vulnerability: [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) .

|

Medium

|

[ CVE-2019-11247 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11247)

