#  Release notes

This page documents production updates to Istio on GKE. You can periodically
check this page for announcements about new or updated features, bug fixes,
known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/istio-release-notes.xml `

##  August 20, 2020

1.4.x

**FIXED:**

**Istio 1.4.10-gke.5**

Fixes an issue with protocol detection connection timeouts.

##  August 05, 2020

1.4.x

**FEATURE:**

Starting with version 1.6, the Istio on GKE add-on uses the Istio Operator for
installation and configuration. When you upgrade your cluster to
1.17.7-gke.8+, 1.17.8-gke.6+, or higher, the Istio 1.6 Operator and control
plane are installed alongside the existing 1.4.x Istio control plane. The
upgrade requires user action and follows the [ dual control plane upgrade
](https://istio.io/latest/blog/2020/multiple-control-planes/) process
(referred to as canary upgrades in the Istio documentation). With a dual
control plane upgrade, you can migrate to the 1.6 version by setting a label
on your workloads to point to the new control plane and performing a rolling
restart. To learn more, see [ Upgrading to Istio 1.6 with Operator
](https://cloud.google.com/istio/docs/istio-on-gke/upgrade-with-operator) .

##  July 21, 2020

1.4.x

**FIXED:**

**Istio 1.4.10-gke.4**

Fixes known security issues with the same fixes as [ OSS Istio 1.4.10
](https://istio.io/news/releases/1.4.x/announcing-1.4.10/)

##  March 27, 2020

1.4.x

**FEATURE:**

**Istio 1.4.6-gke.0** \- This is the initial release of Istio 1.4 to Istio on
GKE

##  March 13, 2020

1.2.x

**FIXED:**

**Istio 1.2.10-gke.3** \- Fixes known security issues with the same fixes as [
OSS Istio 1.4.6 ](https://istio.io/news/releases/1.4.x/announcing-1.4.6/) :

  * CVE-2020-8659, CVE-2020-8661, CVE-2020-8664, CVE-2020-8660: [ ISTIO-SECURITY-2020-003 ](https://istio.io/news/security/istio-security-2020-003/)

##  February 19, 2020

1.2.x

**FIXED:**

**Istio 1.2.10-gke.1** \- Fixes the following known security issues:

  * CVE-2020-8595: [ ISTIO-SECURITY-2020-001 ](https://istio.io/news/security/istio-security-2020-001/)
  * CVE-2020-8843: [ ISTIO-SECURITY-2020-002 ](https://istio.io/news/security/istio-security-2020-002/)

##  December 13, 2019

1.2.x

**ISSUE:**

**Istio 1.2.7-gke.0** \- This release has a [ known security issue
](https://istio.io/news/security/istio-security-2019-007/) that can leave
clusters vulnerable. We recommend upgrading to a version of GKE that will
install Istio 1.2.10.

**FIXED:**

**Istio 1.2.10-gke.0** \- Fixes a [ known security issue
](https://istio.io/news/security/istio-security-2019-007/) with the same fixes
as OSS Istio 1.2.10, as well as improvements and fixes from OSS [ Istio 1.2.8
](https://istio.io/news/releases/1.2.x/announcing-1.2.8/) and [ Istio 1.2.9
](https://istio.io/news/releases/1.2.x/announcing-1.2.9/) .

1.1.x

**ISSUE:**

**Istio 1.1.16-gke.0** \- This release has a [ known security issue
](https://istio.io/news/security/istio-security-2019-007/) that can leave
clusters vulnerable. We recommend upgrading to a version of GKE that will
install Istio 1.1.17.

**FIXED:**

**Istio 1.1.17-gke.0** \- Fixes a [ known security issue
](https://istio.io/news/security/istio-security-2019-007/) .

##  November 12, 2019

1.2.x & 1.0.x & 1.1.x

**ISSUE:**

For the following versions:

  * **Istio 1.0.3-gke.0**
  * **Istio 1.0.3-gke.3a**
  * **Istio 1.0.3-gke.3b**
  * **Istio 1.0.6-gke.1**
  * **Istio 1.0.6-gke.3**
  * **Istio 1.0.9-gke.0**
  * **Istio 1.1.7-gke.0**
  * **Istio 1.1.10-gke.0**
  * **Istio 1.1.13-gke.0**
  * **Istio 1.1.16-gke.0**
  * **Istio 1.1.3-gke.0**

Depending on when the cluster was first created, may have a root certificate
that will expire soon. Please follow the [ instructions
](https://istio.io/docs/ops/security/root-transition/) to check the expiration
date and, optionally, extend the life of your root certificate.

1.1.x

**ISSUE:**

**Istio 1.1.13-gke.0** \- Has the known issues addressed in these releases: [
https://istio.io/about/notes/1.1.8/ ](https://istio.io/about/notes/1.1.8/) , [
https://istio.io/about/notes/1.1.9/ ](https://istio.io/about/notes/1.1.9/) , [
https://istio.io/about/notes/1.1.10/ ](https://istio.io/about/notes/1.1.10/)

##  October 10, 2019

1.2.x

**FIXED:**

**Istio 1.2.7-gke.0** \- Fixes a [ known security issue
](https://istio.io/news/2019/istio-security-2019-005/) with the same fixes as
OSS Istio 1.2.7, as well as [ bug fixes
](https://istio.io/news/2019/announcing-1.2.6/#bug-fixes) from OSS Istio
1.2.6.

1.1.x

**FIXED:**

**Istio 1.1.16-gke.0** \- Fixes a [ known security issue
](https://istio.io/news/2019/istio-security-2019-005/) with the same fixes as
OSS Istio 1.1.16, as well as [ security updates from OSS Istio 1.1.14
](https://istio.io/news/2019/announcing-1.1.14/#security-update) , and an [
Envoy crash bug fix from OSS Istio 1.1.15
](https://istio.io/news/2019/announcing-1.1.15/#bug-fixes)

##  August 13, 2019

1.1.x

**FIXED:**

**Istio 1.1.13-gke-0** \- Fixes a [ known security issue
](https://istio.io/blog/2019/istio-security-003-004/) with the same fixes as
OSS Istio version 1.1.13.

##  July 11, 2019

1.0.x

**FIXED:**

**Istio 1.0.9-gke.0** \- Fixes known issues ( [
https://istio.io/about/notes/1.0.7/ ](https://istio.io/about/notes/1.0.7/) , [
https://istio.io/about/notes/1.0.8/ ](https://istio.io/about/notes/1.0.8/) , [
https://istio.io/about/notes/1.0.9/ ](https://istio.io/about/notes/1.0.9/) )
from version 1.0.6-gke.3.

**ISSUE:**

**Istio 1.0.6-gke.3** \- Has the known issues addressed in these releases: [
https://istio.io/about/notes/1.0.7/ ](https://istio.io/about/notes/1.0.7/) , [
https://istio.io/about/notes/1.0.8/ ](https://istio.io/about/notes/1.0.8/) , [
https://istio.io/about/notes/1.0.9/ ](https://istio.io/about/notes/1.0.9/)

1.1.x

**ISSUE:**

**Istio 1.1.7-gke.0** \- Has the known issues addressed in these releases: [
https://istio.io/about/notes/1.1.8/ ](https://istio.io/about/notes/1.1.8/) , [
https://istio.io/about/notes/1.1.9/ ](https://istio.io/about/notes/1.1.9/) , [
https://istio.io/about/notes/1.1.10/ ](https://istio.io/about/notes/1.1.10/)

**FIXED:**

**Istio 1.1.7-gke.0** \- Fixes known issues ( [
https://istio.io/about/notes/1.1.8/ ](https://istio.io/about/notes/1.1.8/) , [
https://istio.io/about/notes/1.1.9/ ](https://istio.io/about/notes/1.1.9/) , [
https://istio.io/about/notes/1.1.10/ ](https://istio.io/about/notes/1.1.10/) )
from version 1.1.7-gke.0.

##  June 27, 2019

1.1.x

**FEATURE:**

**Istio 1.1.7-gke.0** \- This version does not have a [ pod disruption budget
](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-
disruption-budgets-work) . See notes on [ upgrading from Istio 1.1.3
](https://cloud.google.com/istio/docs/istio-on-
gke/upgrading#upgrading_from_istio_113) .

**FEATURE:**

**Istio 1.1.7-gke.0** \- Google Cloud's operations suite tracing is disabled
by default.

**FIXED:**

**Istio 1.1.7-gke.0** \- Fixes a [ known security issue
](https://istio.io/blog/2019/cve-2019-12243/) from version 1.1.3-gke.0.

##  May 16, 2019

1.1.x

**FEATURE:**

**Istio 1.1.3-gke.0** \- Upgrades Istio to [ version 1.1.3
](https://istio.io/about/notes/1.1/) . See notes on [ upgrading from 1.0
versions of Istio. ](https://cloud.google.com/istio/docs/istio-on-
gke/upgrading#upgrading_to_istio_11)

##  April 05, 2019

1.0.x

**FIXED:**

**Istio 1.0.6-gke.3** \- Fixes a [ known security issue
](https://istio.io/blog/2019/announcing-1.1.2) with the same fixes as OSS
Istio version ` 1.0.7 ` . New clusters will use this version by default when
announced on the [ GKE security bulletins page
](https://cloud.google.com/kubernetes-engine/docs/security-bulletins) ,
expected mid April 2019. If you create a new cluster with Istio on GKE before
then, **make sure to select[ a recommended GKE version
](https://cloud.google.com/istio/docs/istio-on-
gke/installing#supported_gke_cluster_versions) ** to get this version of the
add-on. Existing users should upgrade to the latest patched version of GKE as
soon as possible.

Find out more in this [ security bulletin
](https://cloud.google.com/kubernetes-engine/docs/security-
bulletins#april-05-2019) .

##  March 20, 2019

1.0.x

**FIXED:**

**Istio 1.0.3-gke.3b** \- Fixes to all known issues in 1.0.3-gke.3a.

**FIXED:**

**Istio 1.0.6-gke.1** \- Fixes to all known issues in 1.0.3-gke.3a.

**FEATURE:**

**Istio 1.0.6-gke.1** \- Upgrades Istio to version 1.0.6. See the [ Istio
1.0.6 release notes ](https://istio.io/about/notes/1.0.6/) for more
information.

##  January 28, 2019

1.0.x

**FIXED:**

**Istio 1.0.3-gke.3a** \- Fixes to all known issues in 1.0.3-gke.0.

**FEATURE:**

**Istio 1.0.3-gke.3a** \- All ConfigMaps are now read-only, since these may
change during upgrade.

**FEATURE:**

**Istio 1.0.3-gke.3a** \- Google Cloud's operations suite logging and tracing
are [ enabled by default ](https://cloud.google.com/istio/docs/istio-on-
gke/overview#stackdriver_support) . However, please see the release issue
below for current memory issues with tracing.

**FEATURE:**

**Istio 1.0.3-gke.3a** \- Istio on GKE's internal ` prometheus ` (used for
internal metrics) is renamed to ` promsd ` to avoid confusion.

**ISSUE:**

**Istio 1.0.3-gke.3a** \- Google Cloud's operations suite tracing can consume
too much memory in telemetry pods and should be [ disabled
](https://cloud.google.com/istio/docs/istio-on-
gke/installing#disabling_tracing_and_logging) for now.

##  December 11, 2018

1.0.x

**ISSUE:**

**Istio 1.0.3-gke.0** \- Depending on when the cluster was first created, may
have a root certificate that will expire soon. Please follow the [
instructions ](https://istio.io/docs/ops/security/root-transition/) to check
the expiration date and, optionally, extend the life of your root certificate.

**ISSUE:**

**Istio 1.0.3-gke.0** \- Updating an existing cluster Istio config between `
MTLS_STRICT ` and ` PERMISSIVE ` doesn't work.

**ISSUE:**

**Istio 1.0.3-gke.0** \- Setting the ` --enable-stackdriver-kubernetes ` flag
prevents the Istio Google Cloud's operations suite adapter from being
installed, leading to no Google Cloud's operations suite metrics being
published.

**ISSUE:**

**Istio 1.0.3-gke.0** \- Mixer outputs logs to the local machine via the [ `
stdio ` adapter ](https://istio.io/docs/reference/config/policy-and-
telemetry/adapters/stdio/) by default, which can consume large amounts of CPU.

**ISSUE:**

**Istio 1.0.3-gke.0** \- If you are using Google Cloud's operations suite with
Istio 1.0.3 (the version used in this release of Istio on GKE for initial
Istio installation), you can only use a single instance of Istio-Telemetry in
your control plane. If you use multiple instances, telemetry data can be lost.
To make sure your Google Cloud's operations suite support continues to work
smoothly, do the following:

  * Ensure only one instance of Istio-Telemetry is running by setting the ` Istio-Telemetry HorizontalPodAutoscaler maxReplicas ` value to ` 1 ` . 

` kubectl edit -n istio-system HorizontalPodAutoscalers/istio-telemetry `

  * Make sure that your Istio-Telemetry resources are sufficient for one instance to handle the load from the entire cluster 

` kubectl edit -n istio-system Deployments/istio-telemetry `

