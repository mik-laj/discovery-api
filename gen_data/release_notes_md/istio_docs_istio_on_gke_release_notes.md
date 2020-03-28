#  Release notes

This page documents production updates to Istio on GKE. You can periodically
check this page for announcements about new or updated features, bug fixes,
known issues, and deprecated functionality.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/istio-on-gke-release-notes.xml
`

##  Istio 1.4.6-gke.0

**FEATURE:**

This is the initial release of Istio 1.4 to Istio on GKE

##  Istio 1.2.10-gke.3

**FIXED:**

Fixes known security issues with the same fixes as [ OSS Istio 1.4.6
](https://istio.io/news/releases/1.4.x/announcing-1.4.6/) :

  * CVE-2020-8659, CVE-2020-8661, CVE-2020-8664, CVE-2020-8660: [ ISTIO-SECURITY-2020-003 ](https://istio.io/news/security/istio-security-2020-003/)

##  Istio 1.2.10-gke.1

**FIXED:**

Fixes the following known security issues:

  * CVE-2020-8595: [ ISTIO-SECURITY-2020-001 ](https://istio.io/news/security/istio-security-2020-001/)
  * CVE-2020-8843: [ ISTIO-SECURITY-2020-002 ](https://istio.io/news/security/istio-security-2020-002/)

##  Istio 1.2.10-gke.0

**FIXED:**

Fixes a [ known security issue ](https://istio.io/news/security/istio-
security-2019-007/) with the same fixes as OSS Istio 1.2.10, as well as
improvements and fixes from OSS [ Istio 1.2.8
](https://istio.io/news/releases/1.2.x/announcing-1.2.8/) and [ Istio 1.2.9
](https://istio.io/news/releases/1.2.x/announcing-1.2.9/) .

##  Istio 1.1.17-gke.0

**FIXED:**

Fixes a [ known security issue ](https://istio.io/news/security/istio-
security-2019-007/) .

##  Istio 1.2.7-gke.0

**ISSUE:**

This release has a [ known security issue
](https://istio.io/news/security/istio-security-2019-007/) that can leave
clusters vulnerable. We recommend upgrading to a version of GKE that will
install Istio 1.2.10.

**FIXED:**

Fixes a [ known security issue ](https://istio.io/news/2019/istio-
security-2019-005/) with the same fixes as OSS Istio 1.2.7, as well as [ bug
fixes ](https://istio.io/news/2019/announcing-1.2.6/#bug-fixes) from OSS Istio
1.2.6.

##  Istio 1.1.16-gke.0

**ISSUE:**

This release has a [ known security issue
](https://istio.io/news/security/istio-security-2019-007/) that can leave
clusters vulnerable. We recommend upgrading to a version of GKE that will
install Istio 1.1.17.

**ISSUE:**

Depending on when the cluster was first created, may have a root certificate
that will expire soon. Please follow the [ instructions
](https://istio.io/docs/ops/security/root-transition/) to check the expiration
date and, optionally, extend the life of your root certificate.

**FIXED:**

Fixes a [ known security issue ](https://istio.io/news/2019/istio-
security-2019-005/) with the same fixes as OSS Istio 1.1.16, as well as [
security updates from OSS Istio 1.1.14
](https://istio.io/news/2019/announcing-1.1.14/#security-update) , and an [
Envoy crash bug fix from OSS Istio 1.1.15
](https://istio.io/news/2019/announcing-1.1.15/#bug-fixes)

##  Istio 1.1.13-gke.0

**ISSUE:**

Depending on when the cluster was first created, may have a root certificate
that will expire soon. Please follow the [ instructions
](https://istio.io/docs/ops/security/root-transition/) to check the expiration
date and, optionally, extend the life of your root certificate.

**ISSUE:**

Has the known issues addressed in these releases: [
https://istio.io/about/notes/1.1.8/ ](https://istio.io/about/notes/1.1.8/) , [
https://istio.io/about/notes/1.1.9/ ](https://istio.io/about/notes/1.1.9/) , [
https://istio.io/about/notes/1.1.10/ ](https://istio.io/about/notes/1.1.10/)

Depending on when the cluster was first created, may have a root certificate
that will expire soon. Please follow the [ instructions
](https://istio.io/docs/ops/security/root-transition/) to check the expiration
date and, optionally, extend the life of your root certificate.

**FIXED:**

Fixes a [ known security issue ](https://istio.io/blog/2019/istio-
security-003-004/) with the same fixes as OSS Istio version 1.1.13.

##  Istio 1.0.9-gke.0

**ISSUE:**

Depending on when the cluster was first created, may have a root certificate
that will expire soon. Please follow the [ instructions
](https://istio.io/docs/ops/security/root-transition/) to check the expiration
date and, optionally, extend the life of your root certificate.

**FIXED:**

Fixes known issues ( [ https://istio.io/about/notes/1.0.7/
](https://istio.io/about/notes/1.0.7/) , [ https://istio.io/about/notes/1.0.8/
](https://istio.io/about/notes/1.0.8/) , [ https://istio.io/about/notes/1.0.9/
](https://istio.io/about/notes/1.0.9/) ) from version 1.0.6-gke.3.

##  Istio 1.1.10-gke.0

**ISSUE:**

Depending on when the cluster was first created, may have a root certificate
that will expire soon. Please follow the [ instructions
](https://istio.io/docs/ops/security/root-transition/) to check the expiration
date and, optionally, extend the life of your root certificate.

**FIXED:**

Fixes known issues ( [ https://istio.io/about/notes/1.1.8/
](https://istio.io/about/notes/1.1.8/) , [ https://istio.io/about/notes/1.1.9/
](https://istio.io/about/notes/1.1.9/) , [
https://istio.io/about/notes/1.1.10/ ](https://istio.io/about/notes/1.1.10/) )
from version 1.1.7-gke.0.

##  Istio 1.1.7-gke.0

**ISSUE:**

Depending on when the cluster was first created, may have a root certificate
that will expire soon. Please follow the [ instructions
](https://istio.io/docs/ops/security/root-transition/) to check the expiration
date and, optionally, extend the life of your root certificate.

**ISSUE:**

Has the known issues addressed in these releases: [
https://istio.io/about/notes/1.1.8/ ](https://istio.io/about/notes/1.1.8/) , [
https://istio.io/about/notes/1.1.9/ ](https://istio.io/about/notes/1.1.9/) , [
https://istio.io/about/notes/1.1.10/ ](https://istio.io/about/notes/1.1.10/)

**FIXED:**

Fixes a [ known security issue ](https://istio.io/blog/2019/cve-2019-12243/)
from version 1.1.3-gke.0.

**FEATURE:**

Google Cloud's operations suite tracing is disabled by default.

**FEATURE:**

This version does not have a [ pod disruption budget
](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-
disruption-budgets-work) . See notes on [ upgrading from Istio 1.1.3
](/istio/docs/istio-on-gke/upgrading#upgrading_from_istio_113) .

##  Istio 1.1.3-gke.0

**ISSUE:**

Depending on when the cluster was first created, may have a root certificate
that will expire soon. Please follow the [ instructions
](https://istio.io/docs/ops/security/root-transition/) to check the expiration
date and, optionally, extend the life of your root certificate.

**FEATURE:**

Upgrades Istio to [ version 1.1.3 ](https://istio.io/about/notes/1.1/) . See
notes on [ upgrading from 1.0 versions of Istio. ](/istio/docs/istio-on-
gke/upgrading#upgrading_to_istio_11)

##  Istio 1.0.6-gke.3

**ISSUE:**

Depending on when the cluster was first created, may have a root certificate
that will expire soon. Please follow the [ instructions
](https://istio.io/docs/ops/security/root-transition/) to check the expiration
date and, optionally, extend the life of your root certificate.

**ISSUE:**

Has the known issues addressed in these releases: [
https://istio.io/about/notes/1.0.7/ ](https://istio.io/about/notes/1.0.7/) , [
https://istio.io/about/notes/1.0.8/ ](https://istio.io/about/notes/1.0.8/) , [
https://istio.io/about/notes/1.0.9/ ](https://istio.io/about/notes/1.0.9/)

**FIXED:**

Fixes a [ known security issue ](https://istio.io/blog/2019/announcing-1.1.2)
with the same fixes as OSS Istio version ` 1.0.7 ` . New clusters will use
this version by default when announced on the [ GKE security bulletins page
](https://cloud.google.com/kubernetes-engine/docs/security-bulletins) ,
expected mid April 2019. If you create a new cluster with Istio on GKE before
then, **make sure to select[ a recommended GKE version ](/istio/docs/istio-on-
gke/installing#supported_gke_cluster_versions) ** to get this version of the
add-on. Existing users should upgrade to the latest patched version of GKE as
soon as possible.

Find out more in this [ security bulletin
](https://cloud.google.com/kubernetes-engine/docs/security-
bulletins#april-05-2019) .

