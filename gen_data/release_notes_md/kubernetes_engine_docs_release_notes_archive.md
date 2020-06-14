#  Release notes archive

This page contains a historical archive of all release notes for Google
Kubernetes Engine prior to 2020. To view more recent release notes, see the [
Release notes ](/kubernetes-engine/docs/release-notes) .

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/kubernetes-engine-release-
notes.xml `

##  December 23, 2019

###  Rapid channel  
(1.16.x)

**FEATURE:**

[ Global access ](/kubernetes-engine/docs/how-to/internal-load-
balancing#global_access) for internal TCP/UDP load balancing Services is now
Beta. Global access allows internal load balancing IP addresses to be accessed
from any region within a VPC.

##  December 13, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  No Channel

#####  v.1.12.x

######  1.12.10-gke.22

#####  v.1.15.x

######  1.15.4-gke.22

**FEATURE:**

GKE 1.15 is generally available for new clusters.

######  Upgrading

Before creating GKE v1.15 clusters, you **must** review the [ known issues
](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#known-
issues) and [ urgent upgrade notes
](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md#urgent-
upgrade-notes) .

###  New features

**FEATURE:**

By default, firewall rules restrict your cluster master to only initiate TCP
connections to your nodes on ports 443 (HTTPS) and 10250 (kubelet). For some
Kubernetes features, you might need to add firewall rules to allow access on
additional ports. For example, in Kubernetes 1.9 and older, kubectl top
accesses heapster, which needs a firewall rule to allow TCP connections on
port 8080. To grant such access, you can add firewall rules.

**FEATURE:**

Node-local DNS caching is now available in beta. This does create a single
point of failure. If the node-cache goes down DNS for all Pods on that node
will be broken until the cache is up.

###  Known Issues

**ISSUE:**

There is a low risk that consumers of the published OpenAPI document that made
assumptions about the **absence** of schema info for a given type (for
example, "no schema info means a resource is a custom resource") could have
those assumptions broken once custom resources start publishing schema
definitions.

###  Stable channel  
and 1.13.x

#####  Stable channel

There are no changes to the Stable channel this week.

#####  No channel

  * 1.13.11-gke.15 
  * 1.13.12-gke.16 

###  Regular channel  
and 1.14.x

#####  Regular channel

There are no changes to the Regular channel, but 1.15 will be available in
this channel in January 2020.

**Note:** Relevant content is also available separately in the [ Regular
channel release notes ](/kubernetes-engine/docs/release-notes-regular) .

#####  No channel

  * 1.14.7-gke.25 
  * 1.14.8-gke.21 
  * 1.14.9-gke.2 

###  Rapid channel  
(1.16.x)

#####  Rapid channel

######  1.16.0-gke.20

**Note:** Relevant content is also available separately in the [ Rapid channel
release notes ](/kubernetes-engine/docs/release-notes-rapid) .

GKE 1.16.0-gke.20 (alpha) is now available for testing and validation in the
Rapid [ release channel ](/kubernetes-engine/docs/concepts/release-channels) .

**Important:** Existing clusters enrolled in the Rapid release channel will be
auto-upgraded to this version.

###  Retired APIs

**DEPRECATED:**

extensions/v1beta1, apps/v1beta1, and apps/v1beta2 won't be served by default.

  * All resources under ` apps/v1beta1 ` and ` apps/v1beta2 ` \- use ` apps/v1 ` instead. 
  * ` daemonsets ` , ` deployments ` , ` replicasets ` resources under ` extensions/v1beta1 ` \- use ` apps/v1 ` instead. 
  * ` networkpolicies ` resources under ` extensions/v1beta1 ` \- use ` networking.k8s.io/v1 ` instead. 
  * ` podsecuritypolicies ` resources under ` extensions/v1beta1 ` \- use ` policy/v1beta1 ` instead. 

###  Changes

**CHANGED:**

New clusters have the ` cos-metrics-enabled ` flag enabled by default. This
change allows kernel crash logs to be collected. You can disable by adding `
--metadata cos-metrics-enabled=false ` when you create clusters.

###  Fixed

**FIXED:**

All of the versions made available include a fix for the issue where newly
created node pools are created successfully but are incorrectly shown as
PROVISIONING, as reported on  December 6th, 2019  .

###  New features

**FEATURE:**

[ Maintenance windows and exclusions ](/kubernetes-
engine/docs/concepts/maintenance-windows-and-exclusions) , which was
previously available in beta, is now generally available.

###  Changes

**CHANGED:**

The beta version of Stackdriver Kubernetes Engine Monitoring is no longer
supported.

**DEPRECATED:**

Legacy Stackdriver support for Google Kubernetes Engine (GKE) is deprecated.
If you're using Legacy Stackdriver for logging or monitoring, you must [
migrate to Stackdriver Kubernetes Engine Monitoring ](/monitoring/kubernetes-
engine/migration) before Legacy Stackdriver is decommissioned. For more
information, see [ Legacy Stackdriver support for GKE deprecation.
](/stackdriver/docs/deprecations/legacy)

##  December 6, 2019

**ISSUE:**

The  December 4, 2019 rollout  is paused. Versions that were made available
for upgrades and new clusters in that release will no longer be available.
This is to address an issue where newly created node pools are created
successfully but are incorrectly shown as PROVISIONING.

##  December 4, 2019

###  Fixed

We have fixed an issue with cluster upgrade from a version earlier than
1.14.2-gke.10 when gVisor is enabled in the cluster. It's now safe to upgrade
to any version greater than 1.14.7-gke.17. This issue was originally noted in
the  release notes for October 30, 2019  .

###  Version updates

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  v1.12.x

No new v1.12.x versions this week.

###  Stable channel  
and 1.13.x

#####  Stable channel

There are no changes to the Stable channel this week.

**Note:** Relevant content is also available separately in the [ Stable
channel release notes ](/kubernetes-engine/docs/release-notes-stable) .

#####  No channel

######  1.13.12-gke.14

**Note:** 1.13.12-gke.14 is not yet available in the Stable channel. It is
available to clusters that do not use a release channel.

**CHANGED:**

This version updates COS to [ cos-stable-73-11647-348-0 ](/container-
optimized-os/docs/release-notes/m73#cos-73-11647-348-0) .

###  Regular channel  
and 1.14.x

#####  Regular channel

There are no changes to the Regular channel this week.

**Note:** Relevant content is also available separately in the [ Regular
channel release notes ](/kubernetes-engine/docs/release-notes-regular) .

#####  No channel

######  1.14.8-gke.18

**Note:** 1.14.8-gke.18 is not yet available in the Stable channel. It is
available to clusters that do not use a release channel.

**CHANGED:**

This version updates COS to [ cos-stable-73-11647-348-0 ](/container-
optimized-os/docs/release-notes/m73#cos-73-11647-348-0) .

###  Rapid channel  
(1.15.x)

#####  Rapid channel

There are no changes to the Rapid channel this week.

##  November 22, 2019

###  Fixed

**FIXED:**

The known issue in the COS kernel that may cause kernel panic, previously
reported on  November 5th, 2019  , is resolved. The versions available in this
release use updated versions of COS. GKE 1.12 uses [ ` cos-69-10895-348-0 `
](/container-optimized-os/docs/release-notes/m69#cos-69-10895-348-0) and
versions 1.13 and 1.14 use [ cos-stable-73-11647-348-0 ](/container-optimized-
os/docs/release-notes/m73#cos-73-11647-348-0) .

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version  |  Upgrade version  
---|---  
1.12.10-gke.15  |  1.12.10-gke.17  
  
####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  v1.12.x

#####  1.12.10-gke.20

**FIXED:**

This version uses [ ` cos-69-10895-348-0 ` ](/container-optimized-
os/docs/release-notes/m69#cos-69-10895-348-0) which fixes the known issue that
may cause kernel panics, previously reported on  November 5th, 2019  .

###  Stable channel  
and 1.13.x

#####  Stable channel

There are no changes to the Stable channel this week.

#####  No channel

######  1.13.12-gke.13

**FIXED:**

This version uses [ ` cos-stable-73-11647-348-0 ` ](/container-optimized-
os/docs/release-notes/m73#cos-73-11647-348-0) which fixes the known issue that
may cause kernel panics, previously reported on  November 5th, 2019  .

###  Regular channel  
and 1.14.x

#####  Regular channel

There are no changes to the Regular channel this week.

#####  No channel

######  1.14.8-gke.17

**FIXED:**

This version uses [ ` cos-stable-73-11647-348-0 ` ](/container-optimized-
os/docs/release-notes/m73#cos-73-11647-348-0) which fixes the known issue that
may cause kernel panics, previously reported on  November 5th, 2019  .

###  Rapid channel  
(1.15.x)

#####  Rapid channel

There are no changes to the Rapid channel this week.

####  Versions no longer available

The following versions are no longer available for new clusters or upgrades.

  * 1.12.10-gke.15 
  * 1.13.11-gke.5 
  * 1.13.11-gke.9 
  * 1.13.11-gke.11 
  * 1.13.12-gke.2 
  * 1.14.7-gke.10 
  * 1.14.7-gke.14 
  * 1.14.7-gke.17 
  * 1.14.8-gke.2 

##  November 18, 2019

###  Fixed

**FIXED:**

The known issue in the COS kernel that may cause nodes to crash, previously
reported on  November 5th, 2019  , is resolved. This release downgrades COS to
[ cos-73-11647-293-0 ](/container-optimized-os/docs/release-
notes#cos-73-11647-293-0) .

####  Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version  |  Upgrade version  
---|---  
1.13.0-gke.0 to 1.13.11-gke.13  |  1.13.11-gke.14 (Stable channel)  
1.13.12-gke.0 to 1.13.12-gke.7  |  1.13.12-gke.8  
1.14.0-gke.0 to 1.14.7-gke.22  |  1.14.7-gke.23  
1.14.8-gke.0 to 1.14.8-gke.11  |  1.14.8-gke.12 (Regular channel)  
**Note:** 1.15 was unaffected by this issue.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  v1.12.x

#####  1.12.10-gke.17

No new v1.12.x versions this week.

###  Stable channel  
and 1.13.x

#####  Stable channel

######  1.13.11-gke.14

**FIXED:**

This version includes a fix for a known issue in the COS kernel that may have
caused nodes to crash.

**Note:** Relevant content is also available separately in the [ Stable
channel release notes ](/kubernetes-engine/docs/release-notes-stable) .

#####  No channel

######  1.13.12-gke.8

**Note:** 1.13.12-gke.8 is not yet available in the Stable channel. It is
available to clusters that do not use a release channel.

**FIXED:**

This version includes a fix for a known issue in the COS kernel that may have
caused nodes to crash.

###  Regular channel  
and 1.14.x

#####  Regular channel

######  1.14.8-gke.12

**FIXED:**

This version includes a fix for a known issue in the COS kernel that may have
caused nodes to crash.

**Note:** Relevant content is also available separately in the [ Regular
channel release notes ](/kubernetes-engine/docs/release-notes-regular) .

#####  No channel

######  1.14.7-gke.23

**FIXED:**

This version includes a fix for a known issue in the COS kernel that may have
caused nodes to crash.

###  Rapid channel  
(1.15.x)

#####  1.15.4-gke.15

No new v1.15.x versions this week.

##  November 11, 2019

###  Changes

**CHANGED:**

After November 11, 2019, new clusters and node pools created with ` gcloud `
have [ node auto-upgrade ](/kubernetes-engine/docs/how-to/node-auto-upgrades)
enabled by default.

##  November 05, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version  |  Upgrade version  
---|---  
v1.12.x  |  1.12.10-gke.15  
v1.13.x  |  1.13.11-gke.5  
v1.14.x  |  1.14.7-gke.10  
**Note:** Clusters using [ release channels ](/kubernetes-
engine/docs/concepts/release-channels) are auto-upgraded when new versions are
available in their channel as noted in the following sections.

Rollouts are phased across multiple weeks, to ensure cluster and fleet
stability.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  v1.12.x

#####  v1.12.10-gke.17

**FIXED:**

This release includes a patch for the golang vulnerability CVE-2019-17596,
fixed in go-boringcrypto 1.13.1 and 1.12.11.

**CHANGED:**

Updated containerd to [ 1.2.10
](https://github.com/containerd/containerd/releases/tag/v1.2.10)

###  Stable channel  
(1.13.x)

**Note:** Relevant content is also available separately in the [ Regular
channel release notes ](/kubernetes-engine/docs/release-notes-regular) .

#####  v1.13.11-gke.11

**Note:** This version is available to clusters that do not use a release
channel.

**FIXED:**

This release includes a patch for the golang vulnerability CVE-2019-17596,
fixed in go-boringcrypto 1.13.1 and 1.12.11.

**CHANGED:**

Updated containerd to [ 1.2.10
](https://github.com/containerd/containerd/releases/tag/v1.2.10)

#####  v1.13.12-gke.2

**Note:** This version is available to clusters that do not use a release
channel.

**FIXED:**

This release includes a patch for the golang vulnerability CVE-2019-17596,
fixed in go-boringcrypto 1.13.1 and 1.12.11.

**CHANGED:**

Updated containerd to [ 1.2.10
](https://github.com/containerd/containerd/releases/tag/v1.2.10)

###  Regular channel  
(1.14.x)

#####  v1.14.7-gke.17

**FIXED:**

This release includes a patch for the golang vulnerability CVE-2019-17596,
fixed in go-boringcrypto 1.13.1 and 1.12.11.

#####  v1.14.8-gke.2

**FIXED:**

This release includes a patch for the golang vulnerability CVE-2019-17596,
fixed in go-boringcrypto 1.13.1 and 1.12.11.

###  Rapid channel  
(1.15.x)

#####  v1.15.4-gke.18

**Note:** Relevant content is also available separately in the [ Rapid channel
release notes ](/kubernetes-engine/docs/release-notes-rapid) .

GKE 1.15.4-gke.18 (alpha) is now available for testing and validation in the
Rapid [ release channel ](/kubernetes-engine/docs/concepts/release-channels) .
For more details, refer to the [ release notes for Kubernetes v1.15
](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md)
.

**FIXED:**

This release includes a patch for the golang vulnerability CVE-2019-17596,
fixed in go-boringcrypto 1.13.1 and 1.12.11.

###  Known issues

**ISSUE:**

We have found an issue in COS that might cause kernel panics on nodes.

This impacts node versions:

  * 1.13.11-gke.9 
  * 1.13.11-gke.11 
  * 1.13.11-gke.12 
  * 1.13.12-gke.1 
  * 1.13.12-gke.2 
  * 1.13.12-gke.3 
  * 1.13.12-gke.4 
  * 1.14.7-gke.14 
  * 1.14.7-gke.17 
  * 1.14.8-gke.1 
  * 1.14.8-gke.2 
  * 1.14.8-gke.6 
  * 1.14.8-gke.7 

A patch is being tested and will rollout soon, but we recommend customers
avoid these node versions or downgrade to previous, unaffected patches.

###  New features

**FEATURE:**

[ Surge upgrades ](/kubernetes-engine/docs/concepts/cluster-upgrades#surge)
are now in beta. Surge upgrades allow you to configure speed and disruption of
node upgrades

###  Changes

**CHANGED:**

[ Node auto-provisioning ](/kubernetes-engine/docs/how-to/node-auto-
provisioning) has reached General Availability. Node auto-provisioning creates
or deletes node pools from your cluster based upon resource requests.

##  October 30, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  New default version

The default version for new clusters is now v1.13.11-gke.9 (previously
v1.13.10-gke.0). Clusters enrolled in the stable [ release channel
](/kubernetes-engine/docs/concepts/release-channels) will be auto-upgraded to
this version.

####  Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version  |  Upgrade version  
---|---  
1.12.x versions  |  1.12.10-gke.17  
1.13.x versions  |  1.13.11-gke.5  
1.14.x versions  |  1.14.7-gke.10  
**Note:** Clusters using [ release channels ](/kubernetes-
engine/docs/concepts/release-channels) are auto-upgraded when new versions are
available in the relevant release channels, as noted in the following
sections.

Rollouts are phased across multiple weeks, to ensure cluster and fleet
stability.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  v1.12.x

No new v1.12.x versions this week.

###  Stable channel  
and 1.13.x

#####  Stable channel

**Note:** Relevant content is also available separately in the [ Stable
channel release notes ](/kubernetes-engine/docs/release-notes-stable) .

######  1.13.11-gke.9

**CHANGED:**

Update containerd to 1.2.10.

**CHANGED:**

Update COS to cos-u-73-11647-329-0.

**FIXED:**

This release includes a patch for [ CVE-2019-11253
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253) . For more
information, see the [ security bulletin for October 16, 2019 ](/kubernetes-
engine/docs/security-bulletins#october_16_2019) .

###  Regular channel  
and 1.14.x

#####  Regular channel

**Note:** Relevant content is also available separately in the [ Regular
channel release notes ](/kubernetes-engine/docs/release-notes-regular) .

######  1.14.7-gke.10

This version was generally available on [ October 18, 2019 ](/kubernetes-
engine/docs/release-notes#october_18_2019) and is now available in the Regular
[ release channel ](/kubernetes-engine/docs/concepts/release-channels) .

**FIXED:**

This release includes a patch for [ CVE-2019-11253
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253) . For more
information, see the [ security bulletin for October 16, 2019 ](/kubernetes-
engine/docs/security-bulletins#october_16_2019) .

#####  No channel

######  1.14.7-gke.14

**Note:** 1.14.7-gke.14 is not yet available in the Regular channel. It is
available to clusters that do not use a release channel.

**CHANGED:**

Update COS to cos-u-73-11647-329-0.

###  Rapid channel  
(1.15.x)

#####  1.15.4-gke.17

**Note:** Relevant content is also available separately in the [ Rapid channel
release notes ](/kubernetes-engine/docs/release-notes-rapid) .

GKE 1.15.4-gke.17 (alpha) is now available for testing and validation in the
Rapid [ release channel ](/kubernetes-engine/docs/concepts/release-channels) .

**Important:** Existing clusters enrolled in the Rapid release channel will be
auto-upgraded to this version.

**FIXED:**

Fixes a known issue reported on [ October 11, 2019 ](/kubernetes-
engine/docs/release-notes-rapid#october_11_2019) regarding fdatasync
performance regression on COS/Ubuntu. Node image for Container-Optimized OS
updated to [ cos-77-12371-89-0 ](http://cloud.google.com/container-optimized-
os/docs/release-notes#cos-stable-77-12371-89-0) . Node image for Ubuntu
updated to [ ubuntu-gke-1804-d1903-0-v20191011a
](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-
gke-1804-d1903-0-v20191011a.manifest)

####  Versions no longer available

The following versions are no longer available for new clusters or upgrades.

  * 1.12.10-gke.15 
  * 1.13.7-gke.24 
  * 1.13.9-gke.3 
  * 1.13.9-gke.11 
  * 1.13.10-gke.0 
  * 1.13.10-gke.7 
  * 1.14.6-gke.1 
  * 1.14.6-gke.2 
  * 1.14.6-gke.13 

###  Known Issues

**ISSUE:**

If you use Sandbox Pods in your GKE cluster and plan to upgrade from a version
less than 1.14.2-gke.10 to a version greater than 1.14.2-gke.10, you need to
manually run ` kubectl delete mutatingwebhookconfiguration gvisor-admission-
webhook-config ` after the upgrade.

##  October 18, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version  |  Upgrade version  
---|---  
1.12.x versions  |  1.13.7-gke.24  
1.14.x versions 1.14.6-gke.0 and older  |  1.14.6-gke.1  
**Note:** Clusters using [ release channels ](/kubernetes-
engine/docs/concepts/release-channels) are auto-upgraded when new versions are
available in the relevant release channels, as noted in the following
sections.

Rollouts are phased across multiple weeks, to ensure cluster and fleet
stability.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  v1.12.x

#####  1.12.10-gke.15

**FIXED:**

This release includes a patch for [ CVE-2019-11253
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253) . For more
information, see the [ security bulletin for October 16, 2019 ](/kubernetes-
engine/docs/security-bulletins#october_16_2019) .

###  Stable channel  
and 1.13.x

#####  Stable channel

There are no changes to the Stable channel this week.

**Note:** Relevant content is also available separately in the [ Stable
channel release notes ](/kubernetes-engine/docs/release-notes-stable) .

#####  No channel

######  1.13.11-gke.5

**Note:** 1.13.11-gke.5 is not yet available in the Stable channel. It is
available to clusters that do not use a release channel.

**FIXED:**

This release includes a patch for [ CVE-2019-11253
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253) . For more
information, see the [ security bulletin for October 16, 2019 ](/kubernetes-
engine/docs/security-bulletins#october_16_2019) .

###  Regular channel  
and 1.14.x

#####  Regular channel

There are no changes to the Regular channel this week.

**Note:** Relevant content is also available separately in the [ Regular
channel release notes ](/kubernetes-engine/docs/release-notes-regular) .

#####  No channel

######  1.14.7-gke.10

**Note:** 1.14.7-gke.10 is not yet available in the Regular channel. It is
available to clusters that do not use a release channel.

**FIXED:**

This release includes a patch for [ CVE-2019-11253
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253) . For more
information, see the [ security bulletin for October 16, 2019 ](/kubernetes-
engine/docs/security-bulletins#october_16_2019) .

###  Rapid channel  
(1.15.x)

#####  1.15.4-gke.15

**Note:** Relevant content is also available separately in the [ Rapid channel
release notes ](/kubernetes-engine/docs/release-notes-rapid) .

GKE 1.15.4-gke.15 (alpha) is now available for testing and validation in the
Rapid [ release channel ](/kubernetes-engine/docs/concepts/release-channels) .

**Important:** Existing clusters enrolled in the Rapid release channel will be
auto-upgraded to this version.

**FIXED:**

This release includes a patch for [ CVE-2019-11253
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11253) . For more
information, see the [ security bulletin for October 16, 2019
](https://cloud.google.com/kubernetes-engine/docs/security-
bulletins#october_16_2019) .

####  Versions no longer available

The following versions are no longer available for new clusters or upgrades.

  * 1.12.9-gke.15 
  * 1.12.9-gke.16 
  * 1.12.10-gke.5 
  * 1.12.10-gke.11 

###  Security bulletin

**ISSUE:**

A vulnerability was recently discovered in Kubernetes, described in [
CVE-2019-11253 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-11253) , which allows any user authorized to
make POST requests to execute a remote Denial-of-Service attack on a
Kubernetes API server. For more information, see the [ security bulletin
](/kubernetes-engine/docs/security-bulletins#october_16_2019) .

##  October 11, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  New default version

The default version for new clusters is now v1.13.10-gke.0 (previously
v1.13.7-gke.24). Clusters enrolled in the stable [ release channel
](/kubernetes-engine/docs/concepts/release-channels) will be auto-upgraded to
this version.

####  Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version  |  Upgrade version  
---|---  
versions older than 1.12.9-gke.13  |  1.12.9-gke.15  
1.13.x versions older than 1.13.7-gke.19  |  1.13.7-gke.24  
1.14.x versions older than 1.14.6-gke.0  |  1.14.6-gke.1  
**Note:** Clusters using [ release channels ](/kubernetes-
engine/docs/concepts/release-channels) are auto-upgraded when new versions are
available in the relevant release channels, as noted in the following
sections.

Rollouts are phased across multiple weeks, to ensure cluster and fleet
stability.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  v1.12.x

#####  1.12.10-gke.11

**CHANGED:**

Upgrade containerd to [ 1.2.9
](https://github.com/containerd/containerd/releases/tag/v1.2.9)

**CHANGED:**

Node image for Container-Optimized OS updated to [ cos-69-10895-348-0
](/container-optimized-os/docs/release-notes#cos-69-10895-348-0) .

**CHANGED:**

Node image for Ubuntu updated to [ ubuntu-gke-1804-d1703-0-v20190917
](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-
gke-1804-d1703-0-v20190917.manifest) ).

###  Stable channel  
(1.13.x)

#####  Stable channel

**Note:** Relevant content is also available separately in the [ Stable
channel release notes ](/kubernetes-engine/docs/release-notes-stable) .

######  1.13.10-gke.0

This version was generally available on [ September 16, 2019 ](/kubernetes-
engine/docs/release-notes#september_16_2019) and is now available in the
Stable [ release channel ](/kubernetes-engine/docs/concepts/release-channels)
.

**FIXED:**

This release includes a patch for CVE-2019-9512 and CVE-2019-9514. For more
information, see the [ security bulletin for September 16, 2019 ](/kubernetes-
engine/docs/security-bulletins#september_16_2019) .

#####  No channel

######  1.13.10-gke.7

**Note:** 1.13.10-gke.7 is not yet available in the Stable channel. It is
available to clusters that do not use a release channel.

**CHANGED:**

Upgrade containerd to [ 1.2.9
](https://github.com/containerd/containerd/releases/tag/v1.2.9)

**CHANGED:**

Node image for Container-Optimized OS updated to [ cos-u-73-11647-293-0
](/container-optimized-os/docs/release-notes#cos-73-11647-293-0) .

**CHANGED:**

Node image for Ubuntu updated to [ ubuntu-gke-1804-d1809-0-v20190918
](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-
gke-1804-d1809-0-v20190918.manifest) . Upgrades Nvidia GPU driver to 418
driver, adds Vulkan ICD for graphical workloads, and fixes nvidia-uvm
installation order.

###  Regular channel  
(1.14.x)

#####  Regular channel

**Note:** Relevant content is also available separately in the [ Regular
channel release notes ](/kubernetes-engine/docs/release-notes-regular) .

######  1.14.6-gke.1

This version was generally available on [ September 9, 2019 ](/kubernetes-
engine/docs/release-notes#september_9_2019) and is now available in the
Regular [ release channel ](/kubernetes-engine/docs/concepts/release-channels)
.

#####  No channel

######  1.14.6-gke.13

**Note:** 1.14.6-gke.13 is not yet available in the Regular channel. It is
available to clusters that do not use a release channel.

**FEATURE:**

Enable SecureBoot on master VMs.

**CHANGED:**

Node image for Container-Optimized OS updated to [ cos-u-73-11647-293-0
](/container-optimized-os/docs/release-notes#cos-73-11647-293-0) .

**CHANGED:**

Node image for Ubuntu updated to [ ubuntu-gke-1804-d1809-0-v20190918
](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-
gke-1804-d1809-0-v20190918.manifest) . Upgrades Nvidia GPU driver to 418
driver, adds Vulkan ICD for graphical workloads, and fixes nvidia-uvm
installation order.

**CHANGED:**

Upgrades GPU device plugin to the latest version with Vulkan support.

**ISSUE:**

**Do not upgrade to this version if you use** [ Workload Identity
](/kubernetes-engine/docs/how-to/workload-identity) . There is a known issue
where the gke-metadata-server Pods crashloop if you create or uprade a cluster
to 1.14.6-gke.13.

**FIXED:**

Fixes an issue where cronjobs cannot be scheduled when the total number of
existing jobs exceeds 500.

###  Rapid channel  
(1.15.x)

#####  1.15.3-gke.18

**Note:** Relevant content is also available separately in the [ Rapid channel
release notes ](/kubernetes-engine/docs/release-notes-rapid) .

GKE 1.15.3-gke.18 (alpha) is now available for testing and validation in the
Rapid [ release channel ](/kubernetes-engine/docs/concepts/release-channels) .

**Important:** Existing clusters enrolled in the Rapid release channel will be
auto-upgraded to this version.

**CHANGED:**

Upgraded Istio to 1.2.5.

**CHANGED:**

Improvements to gVisor.

**CHANGED:**

Node image for Container-Optimized OS updated to cos-rc-77-12371-44-0. This
update includes upgrading the kernel to 4.19 from 4.14 and upgrading Docker to
19.03 from 18.09.

**CHANGED:**

Node image for Ubuntu updated to ubuntu-gke-1804-d1903-0-v20190917a. This
update includes upgrading the kernel to 5 from 4.15 and upgrading Docker to
19.03 from 18.09.

**ISSUE:**

**Do not update to this version if you have clusters with hundreds of nodes
per cluster or with I/O intensive workloads.** Clusters with these
characteristics may be impacted by a known issue in versions 4.19 and 5.0 of
the Linux kernel that introduces performance regressions in the ` fdatasync `
system call.

####  Versions no longer available

v1.14.3-gke.11 is no longer available for new clusters or upgrades.

###  Features

**FEATURE:**

[ Node auto-provisioning ](/kubernetes-engine/docs/how-to/node-auto-
provisioning) is now generally available.

**FEATURE:**

[ Vertical Pod Autoscaler ](/kubernetes-
engine/docs/concepts/verticalpodautoscaler) is now generally available.

###  Changes

**CHANGED:**

Upgrade [ Cloud Run on GKE ](/run/docs/gke/release-notes) to 0.9.0.

###  Fixed issues

**FIXED:**

Fixed a bug with fluentd that would prevent new nodes from starting on large
clusters with over 1000 nodes on v1.12.6.

##  October 2, 2019

**FEATURE:**

[ Maintenance windows and exclusions ](/kubernetes-
engine/docs/concepts/maintenance-windows-and-exclusions) now give you granular
control over when automatic maintenance occurs on your clusters. You can
specify the start time, duration, and recurrence of a cluster's maintenance
window. You can also designate specific periods of time when non-essential
automatic maintenance should not occur.

##  September 26, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  New default version

The default version for new clusters is now v1.13.7-gke.24 (previously
v1.13.7-gke.8). Clusters enrolled in the stable [ release channel
](/kubernetes-engine/docs/concepts/release-channels) will be auto-upgraded to
this version.

####  Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version  |  Upgrade version  
---|---  
versions older than 1.12.9-gke.13  |  1.12.9-gke.15  
1.13.x versions older than 1.13.7-gke.19  |  1.13.7-gke.24  
**Note:** Clusters using [ release channels ](/kubernetes-
engine/docs/concepts/release-channels) are auto-upgraded when new versions are
available in the relevant release channels, as noted in the following
sections.

Auto-upgrades are currently occurring two days behind the [ rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) . Some 1.11
clusters will be upgraded to 1.12 in the week of October 7th.

Rollouts are phased across multiple weeks, to ensure cluster and fleet
stability.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  1.12.x

No new v1.12.x versions this week.

###  Stable channel  
(1.13.x)

No new v1.13.x versions this week.

**CHANGED:**

v1.13.7-gke.24 is now available in the Stable release channel.

###  Regular channel  
(1.14.x)

There are no changes to the Regular channel in this release.

**Note:** 1.14.6-gke.2 is not yet available in the Regular channel. It is
available to clusters that do not use a release channel.  **Note:** This
version was previously available in the Rapid channel.

#####  1.14.6-gke.2

**FIXED:**

This release includes a patch for CVE-2019-9512 and CVE-2019-9514.

**CHANGED:**

Reduces startup time for GPU nodes running [ Container-Optimized OS
](/kubernetes-engine/docs/concepts/node-images#container-optimized_os) .

###  Rapid channel  
(1.15.x)

GKE 1.15.3-gke.1 (alpha) is now available for testing and validation in the
Rapid [ release channel ](/kubernetes-engine/docs/concepts/release-channels) .

**Important:** Existing clusters enrolled in the Rapid release channel will be
auto-upgraded to this version.

For more details, refer to the [ release notes for Kubernetes v1.15
](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.15.md)
.

**CHANGED:**

Starting with GKE v1.15, the open source [ Kubernetes Dashboard
](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-
dashboard/) is no longer natively supported in GKE as a managed add-on. To
deploy it manually, follow the [ deployment instructions
](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-
dashboard/#deploying-the-dashboard-ui) in the Kubernetes Dashboard
documentation.

**CHANGED:**

Resizing PersistentVolumes is now a beta feature. As part of this change,
resizing a PersisntentVolume no longer requires you to restart the Pod.

####  Versions no longer available

The following versions are no longer available for new clusters or upgrades.

  * 1.12.7-gke.25 
  * 1.12.7-gke.26 
  * 1.12.8-gke.10 
  * 1.12.8-gke.12 
  * 1.12.9-gke.7 
  * 1.12.9-gke.13 
  * 1.13.6-gke.13 
  * 1.13.7-gke.8 
  * 1.13.7-gke.19 

##  September 20, 2019

**FEATURE:**

[ Ingress Controller ](/kubernetes-engine/docs/concepts/ingress) v1.6, which
was previously available in beta, is generally available for clusters running
v1.13.7-gke.5 and higher.

Along with Ingress Controller, the following are also generally available:

  * [ Configuring load balancing through Ingress ](/kubernetes-engine/docs/how-to/load-balance-ingress)
  * [ Using multiple SSL certificates in HTTP(s) load balancing ](/kubernetes-engine/docs/how-to/ingress-multi-ssl)
  * [ HTTP/2 for load balancing ](/kubernetes-engine/docs/how-to/ingress-http2)

This note has been corrected. [ Using Google-managed SSL certificates
](/kubernetes-engine/docs/how-to/managed-certs) is currently in Beta.

##  September 16, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

The release notes for  September 16, 2019  were incorrectly published early,
on September 9. The incorrect release notes included an announcement of the
availability of a security patch that was not actually made available on that
date. For more information about the security patch, see the [ security
bulletin for September 16, 2019 ](/kubernetes-engine/docs/security-
bulletins#september_16_2019) .

####  Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version  |  Upgrade version  
---|---  
v1.11  |  v1.12  
  
Rollouts are phased across multiple weeks, to ensure cluster and fleet
stability.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  v1.12.x

#####  v1.12.10-gke.5

**FIXED:**

Fixes an issue where Vertical Pod Autoscaler would reject valid Pod patches.

###  Stable channel  
(1.13.x)

**Note:** Relevant content is also available separately in the [ Stable
channel release notes ](/kubernetes-engine/docs/release-notes-stable) .

#####  1.13.10-gke.0

**Note:** This version is not yet available in the Stable channel. It is
available to clusters that do not use a release channel.

**FIXED:**

This release includes a patch for CVE-2019-9512 and CVE-2019-9514. For more
information, see the [ security bulletin for September 16, 2019 ](/kubernetes-
engine/docs/security-bulletins#september_16_2019) .

**CHANGED:**

Reduces startup time for GPU nodes running [ Container-Optimized OS
](/kubernetes-engine/docs/concepts/node-images#container-optimized_os) .

#####  v1.13.7-gke.8

This version was generally available on [ June 27, 2019 ](/kubernetes-
engine/docs/release-notes#june_27_2019) and is now available in the Stable [
release channel ](/kubernetes-engine/docs/concepts/release-channels) .

###  Regular channel  
(1.14.x)

**Note:** Relevant content is also available separately in the [ Regular
channel release notes ](/kubernetes-engine/docs/release-notes-regular) .

#####  v1.14.6-gke.1

**Note:** This version is not yet available in the Regular channel. It is
available to clusters that do not use a release channel.

**FIXED:**

This release includes a patch for CVE-2019-9512 and CVE-2019-9514. For more
information, see the [ security bulletin for September 16, 2019 ](/kubernetes-
engine/docs/security-bulletins#september_16_2019) .

**CHANGED:**

Reduces startup time for GPU nodes running [ Container-Optimized OS
](/kubernetes-engine/docs/concepts/node-images#container-optimized_os) .

#####  v1.14.3-gke.11

This version was generally available on [ September 5, 2019 ](/kubernetes-
engine/docs/release-notes#september_5_2019) and is now available in the
Regular [ release channel ](/kubernetes-engine/docs/concepts/release-channels)
.

###  Rapid channel  
(1.14.x)

#####  v1.14.6-gke.1

**Note:** Relevant content is also available separately in the [ Rapid channel
release notes ](/kubernetes-engine/docs/release-notes-rapid) .

GKE v1.14.6-gke.1 (alpha) is now available for testing and validation in the
Rapid [ release channel ](/kubernetes-engine/docs/concepts/release-channels) .
For more details, refer to the [ release notes for Kubernetes v1.14.6
](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#v1146)
.

**FIXED:**

This release includes a patch for CVE-2019-9512 and CVE-2019-9514. For more
information, see the [ security bulletin for September 16, 2019 ](/kubernetes-
engine/docs/security-bulletins#september_16_2019) .

**CHANGED:**

Reduces startup time for GPU nodes running [ Container-Optimized OS
](/kubernetes-engine/docs/concepts/node-images#container-optimized_os) .

###  New features

**FEATURE:**

**Correction:** This note was incorrectly published early. Ingress Controller
v1.6 became generally available on  September 20, 2019  .

Ingress Controller v1.6, which was previously available in beta, is generally
available for clusters running v1.13.7-gke.5 and higher.

**FEATURE:**

[ Network Endpoint Groups ](/kubernetes-engine/docs/how-to/container-native-
load-balancing) , which allow HTTP(S) load balancers to target Pods directly,
are now generally available.

**FEATURE:**

[ Release channels ](/kubernetes-engine/docs/concepts/release-channels) ,
which provide more control over which automatic upgrades your cluster
receives, are generally available. In addition to the Rapid channel, you can
now enroll your clusters in the Regular or Stable channel.

##  September 9, 2019

###  Correction

The release notes for  September 16, 2019  were incorrectly published early,
on September 9. The incorrect release notes included an announcement of the
availability of a security patch that was not actually made available until
the week of September 16, 2019. For more information avbout the patch, see the
[ security bulletin for September 16, 2019 ](/kubernetes-engine/docs/security-
bulletins#september_16_2019) .

No GKE releases occurred the week of September 9, 2019.

##  September 5, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  New default version

The default version for new clusters is now 1.13.7-gke.8 (previously
1.12.8-gke.10).

####  Scheduled automatic upgrades

Auto-upgrades are no longer paused.

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version  |  upgrade version  
---|---  
1.11.x  |  1.12.7-gke.25  
  
Rollouts are phased across multiple weeks, to ensure cluster and fleet
stability.

####  Versions no longer available

The following versions are no longer available for new clusters or cluster
upgrades:

  * 1.11.10-gke.6 

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  v1.12.x

#####  1.12.9-gke.16

Minor bug fixes and performance improvements.

###  v1.13.x

#####  1.13.9-gke.3

Bug fixes and performance improvements.

###  v1.14.x

#####  1.14.3-gke.11

**FEATURE:**

GKE 1.14 is generally available.

**Note:** If you created a v1.14.x cluster using the Rapid channel, you cannot
currently modify the cluster to use a non-Rapid version. To keep the cluster
running v1.14.x, re-create the cluster without enrolling it in the Rapid
channel.

######  Upgrading

Before [ upgrading clusters to GKE v1.14 ](/kubernetes-engine/docs/how-
to/upgrading-a-cluster) , you **must** review the [ known issues
](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#known-
issues) and [ urgent upgrade notes
](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#urgent-
upgrade-notes) .

For example, the default RBAC policy no longer grants access to discovery and
permission-checking APIs, and you must take specific action to preserve the
old behavior for newly-created cluster users.

######  Differences between GKE v1.14.x and Kubernetes 1.14

GKE v1.14.x has the following differences from [ Kubernetes 1.14.x
](https://kubernetes.io/blog/2019/03/25/kubernetes-1-14-release-announcement/)
:

  * Storage Migrator is not supported on GKE v1.14.x. 

  * CSI Inline Volumes (Alpha) are not supported on GKE v1.14.x. 

  * Huge Pages is not supported on GKE 1.14.x. If you are interested in support for Huge Pages, [ register your interest ](https://docs.google.com/forms/d/e/1FAIpQLScxvLni5-6_2m0oUpD1i5ekyiZj7aW30JULLwoQnPy00x5B5Q/viewform?usp=sf_link) . 

######  New features

**FEATURE:**

[ Pod Ready++
](https://github.com/kubernetes/enhancements/blob/master/keps/sig-
network/0007-pod-ready%2B%2B.md) is generally available and supported on GKE
v1.14.x.

**FEATURE:**

[ Pod priority and preemption
](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/)
is generally available and supported on GKE v1.14.x.

**FEATURE:**

The [ RunAsGroup ](https://kubernetes.io/docs/tasks/configure-pod-
container/security-context/) feature has been promoted to beta and enabled by
default. PodSpec and PodSecurityPolicy objects can be used to control the
primary GID of containers on Docker and containerd runtimes.

**FEATURE:**

Early-access to test Windows containers is now available. If you are
interested in testing Windows containers, fill out [ this form
](http://j.mp/gke-windows) .

######  Other changes

**CHANGED:**

The ` node.k8s.io ` API group and ` runtimeclasses.node.k8s.io ` resource have
been migrated to a built-in API. If you were using RuntimeClasses, you must
recreate each of them after upgrading, and also delete the `
runtimeclasses.node.k8s.io ` CRD. RuntimeClasses can no longer be created
without a defined handler.

**CHANGED:**

When creating a new GKE cluster, Stackdriver Kubernetes Engine Monitoring is
now the default Stackdriver support option. This is a change from prior
versions where Stackdriver Logging and Stackdriver Monitoring were the default
Stackdriver support option. For more information, see [ Overview of
Stackdriver support for GKE ](/monitoring/kubernetes-engine) .

**DEPRECATED:**

OS and Arch information is now recorded in ` kubernetes.io/os ` and `
kubernetes.io/arch ` labels on Node objects. The previous labels ( `
beta.kubernetes.io/os ` and ` beta.kubernetes.io/arch ` ) are still recorded,
but are deprecated and targeted for removal in Kubernetes 1.18.

######  Known Issues

**ISSUE:**

Users with the Quobyte Volume plugin are advised not to upgrade between GKE
1.13.x and 1.14.x due to an issue with Kubernetes 1.14. This will be fixed in
an upcoming release.

Bug fixes and performance improvements.

###  Rapid

The following versions are available to clusters enrolled in the Rapid [
release channel ](/kubernetes-engine/docs/concepts/release-channels) .

**Note:** This content is also available separately in the [ Rapid channel
release notes ](/kubernetes-engine/docs/release-notes-rapid) .

#####  1.14.5-gke.5

GKE 1.14.5-gke.5 is now available in the Rapid release channel. It includes
bug fixes and performance improvements. For more details, refer to the [
release notes for Kubernetes v1.14
](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md#changelog-
since-v1144) .

###  New features

**FEATURE:**

[ Intranode visibility ](/kubernetes-engine/docs/how-to/intranode-visibility)
is generally available.

**FEATURE:**

You can now use [ Customer-managed encryption keys (beta) ](/kubernetes-
engine/docs/how-to/dynamic-provisioning-cmek) to control the encryption used
for attached persistent disks in your clusters. This is available as a
dynamically provisioned PersistentVolume.

**FEATURE:**

Both [ containerd on Container-Optimized OS (cos_containerd) ](/kubernetes-
engine/docs/concepts/node-images#cos-containerd) and [ containerd on Ubuntu
(ubuntu_containerd) ](/kubernetes-engine/docs/concepts/node-images#ubuntu-
containerd) node images are generally available.

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

##  August 22, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  Scheduled automatic upgrades

Auto-upgrades are currently paused.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  v1.11.x

#####  1.11.10-gke.6

**FIXED:**

This version was previously released and is available again. It mitigates
against the vulnerability described in the [ security bulletin published on
August 5, 2019 ](/kubernetes-engine/docs/security-bulletins#august-05-2019) .

###  v1.12.x

Multiple v1.12.x versions are available this week:

#####  1.12.9-gke.13

**FIXED:**

This version mitigates against the vulnerability described in the [ security
bulletin published on August 5, 2019 ](/kubernetes-engine/docs/security-
bulletins#august-05-2019) .

#####  1.12.9-gke.15

**FIXED:**

Fixes an issue that can cause Horizontal Pod Autoscaler to increase the
replica count to the maximum, regardless of other autoscaling factors.

**FIXED:**

Upgrade Istio to 1.1.13, to address address [ two vulnerabilities
](https://istio.io/blog/2019/istio-security-003-004/) announced by the Istio
project. These vulnerabilities can be used to mount a Denial of Service (DoS)
attack against services using Istio.

**CHANGED:**

The node image for Container-Optimized OS (COS) is now [ cos-69-10895-329-0
](/container-optimized-os/docs/release-notes/m69) .

###  v1.13.x

Multiple v1.13.x versions are available this week:

#####  1.13.7-gke.19

**FIXED:**

This version mitigates against the vulnerability described in the [ security
bulletin published on August 5, 2019 ](/kubernetes-engine/docs/security-
bulletins#august-05-2019) .

#####  1.13.7-gke.24

**FIXED:**

Fixes an issue that can cause Horizontal Pod Autoscaler to increase the
replica count to the maximum during a rolling update, regardless of other
autoscaling factors.

**FIXED:**

Upgrade Istio to 1.1.13, to address address [ two vulnerabilities
](https://istio.io/blog/2019/istio-security-003-004/) announced by the Istio
project. These vulnerabilities can be used to mount a Denial of Service (DoS)
attack against services using Istio.

**CHANGED:**

The node image for Container-Optimized OS (COS) is now [ cos-73-11647-267-0
](/container-optimized-os/docs/release-notes/m73) .

###  Rapid channel

#####  1.14.3-gke.11

**Note:** This content is also available separately in the [ Rapid channel
release notes ](/kubernetes-engine/docs/release-notes-rapid) .

GKE 1.14.3-gke.11 (alpha) is now available for testing and validation in the
Rapid [ release channel ](/kubernetes-engine/docs/concepts/release-channels) .
For more details, refer to the [ release notes for Kubernetes v1.14
](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md)
.

**FIXED:**

This version mitigates against the vulnerability described in the [ security
bulletin published on August 5, 2019 ](/kubernetes-engine/docs/security-
bulletins#august-05-2019) .

**FIXED:**

Upgrade Istio to 1.1.13, to address address [ two vulnerabilities
](https://istio.io/blog/2019/istio-security-003-004/) announced by the Istio
project. These vulnerabilities can be used to mount a Denial of Service (DoS)
attack against services using Istio.

**CHANGED:**

The node image for Container-Optimized OS (COS) is now [ cos-73-11647-267-0
](/container-optimized-os/docs/release-notes/m73) .

###  New features

**FEATURE:**

[ Config Connector ](/config-connector) is a Kubernetes addon that allows you
to manage your Google Cloud resources through Kubernetes configuration.

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

##  August 12, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  Important information about v1.10.x nodes

In addition to GKE's [ version policy ](/kubernetes-engine/versioning-and-
upgrades) , Kubernetes has a [ version skew policy
](https://kubernetes.io/docs/setup/version-skew-policy/) of supporting only
the three newest minor versions. Older versions are not guaranteed to receive
bug fixes or security updates, and the control plane may become incompatible
with nodes running unsupported versions.

Specifically, the Kubernetes v1.13.x control plane is not compatible with
nodes running v1.10.x. Clusters in such a configuration could become
unreachable or fail to run your workloads correctly. Additionally, ** security
patches  are not applied to v1.10.x and below. **

We previously published a notice that Google would enable node auto-upgrade to
node pools running v1.10.x or lower, to bring those clusters into a supported
configuration and mitigate the incompatibility risk described above. To allow
for sufficient time for customers to complete the upgrade themselves, Google
postponed upgrading cluster control planes to 1.13 until mid-September 2019.
Please plan your manual node upgrade to keep your clusters healthy and up to
date.

####  Scheduled automatic upgrades

Auto-upgrades are currently paused.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  v1.11.x

#####  1.11.10-gke.6

**FIXED:**

Fixes the vulnerability announced in the [ security bulletin for August 5,
2019 ](/kubernetes-engine/docs/security-bulletins#august-05-2019) .

**FIXED:**

Fixes a problem where Cluster Autoscaler can create too many nodes when
scaling up.

###  v1.12.x

Multiple v1.12.x versions are available this week:

#####  1.12.9-gke.13

**Note:** This version contains all the changes in 1.12.9-gke.10, as well as
those listed here.

**FIXED:**

Fixes the vulnerability announced in the [ security bulletin for August 5,
2019 ](/kubernetes-engine/docs/security-bulletins#august-05-2019) .

**FIXED:**

Fixes a problem where Cluster Autoscaler can create too many nodes when
scaling up.

#####  1.12.9-gke.10

**FIXED:**

Fixes a problem where Vertical Pod Autoscaler would reject valid patches to
Pods.

**FIXED:**

Improvements to Cluster Autoscaler.

**FIXED:**

Updates Istio to v1.0.9-gke.0.

#####  v1.12.8-gke.12

**FIXED:**

Updates Istio to v1.0.9-gke.0.

#####  1.12.7-gke.2

**FIXED:**

Updates Istio to v1.0.9-gke.0.

**FIXED:**

Fixes a [ problem ](https://github.com/kubernetes/kubernetes/pull/79451) where
the kubelet could fail to start a Pod for the first time if the node was not
completely configured and the Pod's restart policy was ` NEVER ` .

###  v1.13.x

Multiple v1.13.x versions are available this week:

#####  1.13.7-gke.19

**Note:** This version contains all the changes in 1.13.7-gke.15, as well as
those listed here.

**FIXED:**

Fixes the vulnerability announced in the [ security bulletin for August 5,
2019 ](/kubernetes-engine/docs/security-bulletins#august-05-2019) .

**FIXED:**

Fixes a problem where Cluster Autoscaler can create too many nodes when
scaling up.

#####  1.13.7-gke.15

**FIXED:**

Fixes a problem where Vertical Pod Autoscaler would reject valid patches to
Pods.

**FIXED:**

Improvements to Cluster Autoscaler.

**FEATURE:**

You can now use [ Vulkan ](https://www.khronos.org/vulkan/) with GPUs to
process graphics workloads. The Vulkan configuration directorhy is mounted on
` /etc/vulkan/icd.d ` in the container.

**FIXED:**

Updates Istio to v1.1.10-gke.0.

**FIXED:**

Fixes a [ problem ](https://github.com/kubernetes/kubernetes/pull/79451) where
the kubelet could fail to start a Pod for the first time if the node was not
completely configured and the Pod's restart policy was ` NEVER ` .

###  Rapid (v1.14.x)

#####  1.14.3-gke.10

**Note:** This content is also available separately in the [ Rapid channel
release notes ](/kubernetes-engine/docs/release-notes-rapid) .

GKE 1.14.3-gke.10 (alpha) is now available for testing and validation in the
Rapid [ release channel ](/kubernetes-engine/docs/concepts/release-channels) .
For more details, refer to the [ release notes for Kubernetes v1.14
](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md)
.

**FIXED:**

Fixes the vulnerability announced in the [ security bulletin for August 5,
2019 ](/kubernetes-engine/docs/security-bulletins#august-05-2019) .

**FIXED:**

Fixes a problem where Cluster Autoscaler can create too many nodes when
scaling up.

**CHANGED:**

In v1.14.3-gke.10 and higher, [ GKE Sandbox ](/kubernetes-engine/docs/how-
to/sandbox-pods) uses the ` gvisor.config.common-webhooks.networking.gke.io `
webhook, which is created when the cluster starts and makes sandboxed nodes
available faster.

###  Security bulletin

**ISSUE:**

Kubernetes recently discovered a vulnerability, [ CVE-2019-11247
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11247) , which
allows cluster-scoped custom resource instances to be acted on as if they were
namespaced objects existing in all Namespaces. This vulnerability is fixed in
GKE versions also announced today. For more information, see the [ security
bulletin ](/kubernetes-engine/docs/security-bulletins#august-05-2019) .

###  New features

**FEATURE:**

Clusters running v1.13.6-gke.0 or higher can use [ Shielded GKE Nodes (beta)
](/kubernetes-engine/docs/how-to/shielded-gke-nodes) , which provide strong,
verifiable node identity and integrity to increase the security of your nodes.

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

##  August 1, 2019

**Note:** Auto-upgrades for masters and nodes are currently paused.

###  New versions available for upgrades and new clusters

During the week of July 8, 2019, a release resulted in a partial rollout.
Release notes were not published at that time. Changes discussed in the rest
of this entry were applied **only to the following zones** :

  * ` europe-west2-a `
  * ` us-east1 `
  * ` us-east1-d `

In those zones only, the following new versions are available:

  * 1.13.7-gke.15 
  * 1.12.9-gke.10 
  * 1.12.7-gke.26 
  * 1.12.8-gke.12 

In those zones only, the following versions are no longer available for new
clusters or nodes:

  * 1.11.10-gke.5 

In those zones only, clusters running v1.11.x with auto-upgrade enabled were
upgraded to v1.12.7-gke.25.

###  Security bulletin

**FIXED:**

GKE v1.13.7.x includes patches that mitigate multiple vulnerabilities that are
present in v1.13.6. Clusters running any v1.13.6.x version should upgrade to
1.13.7.x, to mitigate against these vulnerabilities, which are described in
the following security bulletins:

  * [ June 25, 2019 ](/kubernetes-engine/docs/security-bulletins#june-25-2019)
  * [ May 31, 2019 ](/kubernetes-engine/docs/security-bulletins#may-31-2019)

###  New features

**FEATURE:**

GKE usage metering (Beta) now supports tracking actual consumption, in
addition to resource requests, for clusters running v1.12.8-gke.8 and higher,
v1.13.6-gke.7 and higher, or 1.14.2-gke.8 and higher. A new BigQuery table, `
gke_cluster_resource_consumption ` , is created automatically in the BigQuery
dataset. For more information about this and other improvements to Usage
Metering, see [ Usage metering (Beta) ](/kubernetes-engine/docs/how-
to/cluster-usage-metering) .

**FEATURE:**

[ Node auto-provisioning ](/kubernetes-engine/docs/how-to/node-auto-
provisioning) is supported on regional clusters running v1.12.x or higher.

##  July 29, 2019

**CHANGED:**

VPC-native is **no longer** the default cluster network mode for new clusters
created using ` gcloud ` v256.0.0 or higher. Instead, the routes-based cluster
network mode is used by default. We recommend manually enabling [ VPC-native
](/kubernetes-engine/docs/how-to/alias-ips) , to avoid exhausting routes
quota.

VPC-native clusters are created by default when you use Google Cloud Console
or ` gcloud ` versions 251.0.0 through 255.0.0. Routes-based clusters are
created by default when using the REST API.

##  June 27, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  Important changes to clusters running unsupported versions

In addition to GKE's [ version policy ](/kubernetes-engine/versioning-and-
upgrades) , Kubernetes has a [ version skew policy
](https://kubernetes.io/docs/setup/version-skew-policy/) of supporting only
the three newest minor versions. Older versions are not guaranteed to receive
bug fixes or security updates, and the control plane may become incompatible
with nodes running unsupported versions.

For example, the Kubernetes v1.13.x control plane is not compatible with nodes
running v1.10.x. Clusters in such a configuration could become unreachable or
fail to run your workloads correctly. Additionally,  security patches  are not
applied to v1.10.x and below.

To keep your clusters operational and to protect Google's infrastructure, we
strongly recommend that you upgrade existing nodes to v1.11.x or higher before
the end of June 2019. At that time, Google will enable node auto-upgrade on
node pools older than v1.11.x, and these nodes will be updated to v1.11.x so
that the control plane can be upgraded to v1.13.x and remain compatible with
existing node pools.

We strongly recommend leaving node auto-upgrade enabled.

NOTE: As of 1.12 all kubelets are issued certificates from the cluster CA and
verification of kubelet certificates is enabled automatically if all nodepools
are 1.12+. We have observed that introducing older (pre 1.12) nodepools after
certificate verification has started may cause connection problems for kubectl
logs/exec/attach/portforward commands, and should be avoided.

####  Versions no longer available for upgrades and new clusters

The following versions are no longer available for new clusters or cluster
upgrades:

  * 1.11.8-gke.10 
  * 1.11.10-gke.4 
  * 1.12.7-gke.10 
  * 1.12.7-gke.21 
  * 1.12.7-gke.22 
  * 1.12.8-gke.6 
  * 1.12.8-gke.7 
  * 1.12.9-gke.3 
  * 1.13.6-gke.5 
  * 1.13.6-gke.6 
  * 1.13.7-gke.0 

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  v1.11.x

#####  1.11.10-gke.5

**FIXED:**

This version contains a patch for recently discovered TCP vulnerabilities in
the Linux kernel. See the associated [ security bulletin ](/kubernetes-
engine/docs/security-bulletins#june-25-2019) for more information.

###  v1.12.x

#####  1.12.7-gke.25

**FIXED:**

This version contains a patch for recently discovered TCP vulnerabilities in
the Linux kernel. See the associated [ security bulletin ](/kubernetes-
engine/docs/security-bulletins#june-25-2019) for more information.

#####  1.12.8-gke.10

**FIXED:**

This version contains a patch for recently discovered TCP vulnerabilities in
the Linux kernel. See the associated [ security bulletin ](/kubernetes-
engine/docs/security-bulletins#june-25-2019) for more information.

#####  1.12.9-gke.7

**FIXED:**

This version contains a patch for recently discovered TCP vulnerabilities in
the Linux kernel. See the associated [ security bulletin ](/kubernetes-
engine/docs/security-bulletins#june-25-2019) for more information.

###  v1.13.x

#####  1.13.6-gke.13

**FIXED:**

This version contains a patch for recently discovered TCP vulnerabilities in
the Linux kernel. See the associated [ security bulletin ](/kubernetes-
engine/docs/security-bulletins#june-25-2019) for more information.

#####  1.13.7-gke.8

**FIXED:**

This version contains a patch for recently discovered TCP vulnerabilities in
the Linux kernel. See the associated [ security bulletin ](/kubernetes-
engine/docs/security-bulletins#june-25-2019) for more information.

###  Rapid channel

#####  1.14.3-gke.9

**FIXED:**

This version contains a patch for recently discovered TCP vulnerabilities in
the Linux kernel. See the associated [ security bulletin ](/kubernetes-
engine/docs/security-bulletins#june-25-2019) for more information.

**Note:** This content is also available separately in the [ Rapid channel
release notes ](/kubernetes-engine/docs/release-notes-rapid) .

###  Security bulletins

**FIXED:**

Patched versions are now available to address TCP vulnerabilities in the Linux
Kernel. For more information, see the [ security bulletin ](/kubernetes-
engine/docs/security-bulletins#june-25-2019) In accordance with the documented
support policy, patches will not be applied to GKE version 1.10 and older.

**ISSUE:**

Kubernetes recently discovered a vulnerability in ` kubectl ` ,
CVE-2019-11246. For more information, see the [ security bulletin
](/kubernetes-engine/docs/security-bulletins#june-25-2019) .

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * Early access to test Windows Containers 
  * [ Usage metering ](/kubernetes-engine/docs/how-to/cluster-usage-metering) will become generally available 

##  June 4, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version  |  Upgrade version  
---|---  
1.11.9  |  1.12.7-gke.10  
  
Rollouts are phased across multiple weeks, to ensure cluster and fleet
stability.

####  Versions no longer available

The following versions are no longer available for new clusters or cluster
upgrades:

  * 1.11.8-gke.6 
  * 1.11.9-gke.8 
  * 1.11.9-gke.13 
  * 1.14.2-gke.1 [Preview] 

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  v1.11.x

No v1.11.x versions this week.

###  v1.12.x

v1.12.8-gke.7 includes the following changes:

**CHANGED:**

Improved Node Auto-Provisioning support for multi-zonal clusters with GPUs.

Cloud Run 0.6

###  v1.13.x

v1.13.6-gke.6 includes the following changes:

**CHANGED:**

Improved Node Auto-Provisioning support for multi-zonal clusters with GPUs.

Cloud Run 0.6

COS images now use the Nvidia GPU 418.67 driver. Nvidia drivers on COS are now
pre-compiled, greatly reducing driver installation time.

**ISSUE:**

GKE nodes running Kubernetes v1.13.6 are affected by CVE-2019-11245.
Information about the impact and mitigation of this vulnerability is available
in this [ Kubernetes issue report
](https://github.com/kubernetes/kubernetes/issues/78308) . In addition to
security concerns, this bug can cause Pods that must run as a specific UID to
fail.

###  Rapid channel

**CHANGED:**

v1.14.1-gke.5 is the default for new Rapid channel clusters. This version
includes patched node images that address [ CVE-2019-11245 ](/kubernetes-
engine/docs/security-bulletins#may-31-2019) .

**ISSUE:**

GKE nodes running Kubernetes v1.14.2 are affected by CVE-2019-11245.
Information about the impact and mitigation of this vulnerability is available
in this [ Kubernetes issue report
](https://github.com/kubernetes/kubernetes/issues/78308) . In addition to
security concerns, this bug can cause Pods that must run as a specific UID to
fail.

###  Security bulletin

**ISSUE:**

GKE nodes running Kubernetes v1.13.6 and v1.14.2 are affected by
CVE-2019-11245. Information about the impact and mitigation of this
vulnerability is available in this [ Kubernetes issue report
](https://github.com/kubernetes/kubernetes/issues/78308) . In addition to
security concerns, this bug can cause Pods that must run as a specific UID to
fail.

###  Changes

**CHANGED:**

Currently, [ VPC-native ](/kubernetes-engine/docs/how-to/alias-ips) is the
default for new clusters created with ` gcloud ` or the Google Cloud Console.
However, VPC-native is not the default for new clusters created with the REST
API.

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * Early access to test Windows Containers 
  * [ Usage metering ](/kubernetes-engine/docs/how-to/cluster-usage-metering) will become generally available 
  * New clusters will begin to default to [ VPC-native ](/kubernetes-engine/docs/how-to/alias-ips)

##  June 3, 2019

###  Corrections

**CHANGED:**

Basic authentication and client certificate issuance are disabled by default
for clusters created with GKE 1.12 and higher. We recommend switching your
clusters to use OpenID instead. However, you can still enable basic
authentication and client certificate issuance manually.

To learn more about cluster security, see [ Hardening your cluster
](/kubernetes-engine/docs/how-to/hardening-your-cluster) .

This information was inadvertently omitted from the  February 27, 2019 release
note  . However, the documentation about cluster routing was updated.

**CHANGED:**

The rollout dates for the  May 28, 2019  releases are incorrect. Day 2 spanned
May 29-30, day 3 is May 31, and day 4 is June 3.

##  May 28, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  Important changes to clusters running unsupported versions

In addition to GKE's [ version policy ](/kubernetes-engine/versioning-and-
upgrades) , Kubernetes has a [ version skew policy
](https://kubernetes.io/docs/setup/version-skew-policy/) of supporting only
the three newest minor versions. Older versions are not guaranteed to receive
bug fixes or security updates, and the control plane may become incompatible
with nodes running unsupported versions.

For example, the Kubernetes v1.13.x control plane is not compatible with nodes
running v1.10.x. Clusters in such a configuration could become unreachable or
fail to run your workloads correctly.

To keep your clusters operational and to protect Google's infrastructure, we
strongly recommend that you upgrade existing nodes to v1.11.x or higher before
the end of June 2019. At that time, Google will enable node auto-upgrade on
node pools older than v1.11.x, and these nodes will be updated to v1.11.x so
that the control plane can be upgraded to v1.13.x and remain compatible with
existing node pools.

We strongly recommend leaving node auto-upgrade enabled.

####  Scheduled automatic upgrades

No new automatic upgrades this week; previously-announced automatic upgrades
may still be ongoing.

Rollouts are phased across multiple weeks, to ensure cluster and fleet
stability.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  v1.11.x

v1.11.10-gke.4 includes the following changes:

**FIXED:**

The node image for Container-Optimized OS (COS) is now [ cos-69-10895-242-0
](/container-optimized-os/docs/release-notes/m69) .

The node image for Ubuntu is now [ ubuntu-gke-1804-d1703-0-v20190517
](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-
gke-1804-d1703-0-v20190517.manifest) .

Node images have been updated to fix Microarchitectural Data Sampling (MDS)
vulnerabilities announced by Intel. For more information, see the [ security
bulletin ](/kubernetes-engine/docs/security-bulletins#may-14-2019) .

The patch alone is not sufficient to mitigate exposure to this vulnerability.
For more information, see the [ security bulletin ](/kubernetes-
engine/docs/security-bulletins#may-14-2019) .

###  v1.12.x

v1.12.8-gke.6 includes the following changes:

**FIXED:**

The node image for Container-Optimized OS (COS) is now [ cos-69-10895-242-0
](/container-optimized-os/docs/release-notes/m69) .

The node image for Ubuntu is now [ ubuntu-gke-1804-d1703-0-v20190517
](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-
gke-1804-d1703-0-v20190517.manifest) .

Node images have been updated to fix Microarchitectural Data Sampling (MDS)
vulnerabilities announced by Intel.

The patch alone is not sufficient to mitigate exposure to this vulnerability.
For more information, see the [ security bulletin ](/kubernetes-
engine/docs/security-bulletins#may-14-2019) .

###  v1.13.x

v1.13.6-gke.5 includes the following changes:

**FIXED:**

The node image for Container-Optimized OS (COS) is now [ cos-u-73-11647-182-0
](/container-optimized-os/docs/release-notes/m73) .

The node image for Ubuntu is now [ ubuntu-gke-1804-d1809-0-v20190517
](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-
gke-1804-d1809-0-v20190517.manifest) .

Node images have been updated to fix Microarchitectural Data Sampling (MDS)
vulnerabilities announced by Intel. For more information, see the [ security
bulletin ](/kubernetes-engine/docs/security-bulletins#may-14-2019) .

The patch alone is not sufficient to mitigate exposure to this vulnerability.
For more information, see the [ security bulletin ](/kubernetes-
engine/docs/security-bulletins#may-14-2019) .

###  Rapid channel

v1.14.2-gke.2 is the default for new Rapid channel clusters, and includes the
following changes:

**FEATURE:**

GKE Sandbox is supported on v1.14.x clusters running v1.14.2-gke.2 or higher.

**FIXED:**

The node image for Container-Optimized OS (COS) is now [ cos-u-73-11647-182-0
](/container-optimized-os/docs/release-notes/m73) .

The node image for Ubuntu is now [ ubuntu-gke-1804-d1809-0-v20190517
](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-
gke-1804-d1809-0-v20190517.manifest) .

  * Node images have been updated to fix Microarchitectural Data Sampling (MDS) vulnerabilities announced by Intel. For more information, see the [ security bulletin ](/kubernetes-engine/docs/security-bulletins#may-14-2019) . 

The patch alone is not sufficient to mitigate exposure to this vulnerability.
For more information, see the [ security bulletin ](/kubernetes-
engine/docs/security-bulletins#may-14-2019) .

  * Nodes using these images are now [ shielded VMs ](/shielded-vm) with the following properties: 

    * [ UEFI ](http://www.uefi.org/sites/default/files/resources/UEFI_Secure_Boot_in_Modern_Computer_Security_Solutions_2013.pdf) boot is enabled. 
    * [ SecureBoot ](/security/shielded-cloud/shielded-vm#secure-boot) is disabled. 
    * [ vTPM ](/security/shielded-cloud/shielded-vm#vtpm) is enabled. 
    * [ Integrity Monitoring ](/security/shielded-cloud/shielded-vm#integrity-monitoring) is enabled. 

**CHANGED:**

The following IP ranges have been added to default non-IP-masq ` iptables `
rules:

  * ` 100.64.0.0/10 `
  * ` 192.0.0.0/24 `
  * ` 192.0.2.0/24 `
  * ` 192.88.99.0/24 `
  * ` 198.18.0.0/15 `
  * ` 198.51.100.0/24 `
  * ` 203.0.113.0/24 `
  * ` 240.0.0.0/4 `

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * Cloud Run will be upgraded 
  * Istio will be upgraded for v1.13.x clusters 
  * Early access to test Windows Containers, expected in early June 
  * New clusters will begin to default to [ VPC-native ](/kubernetes-engine/docs/how-to/alias-ips)

##  May 20, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  Important changes to clusters running unsupported versions

In addition to GKE's [ version policy ](/kubernetes-engine/versioning-and-
upgrades) , Kubernetes has a [ version skew policy
](https://kubernetes.io/docs/setup/version-skew-policy/) of supporting only
the three newest minor versions. Older versions are not guaranteed to receive
bug fixes or security updates, and the control plane may become incompatible
with nodes running unsupported versions.

For example, the Kubernetes v1.13.x control plane is not compatible with nodes
running v1.10.x. Clusters in such a configuration could become unreachable or
fail to run your workloads correctly.

To keep your clusters operational and to protect Google's infrastructure, we
strongly recommend that you upgrade existing nodes to v1.11.x or higher before
the end of June 2019. At that time, Google will enable node auto-upgrade on
node pools older than v1.11.x, and these nodes will be updated to v1.11.x so
that the control plane can be upgraded to v1.13.x and remain compatible with
existing node pools.

We strongly recommend leaving node auto-upgrade enabled.

####  Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version  |  Upgrade version  
---|---  
1.10.x (nodes only, completing)  |  1.11.8-gke.6  
1.12.6-gke.10  |  1.12.6-gke.11  
1.14.1-gke.4 and older 1.14.x (Alpha)  |  1.14.1-gke.5 (Alpha)  
  
Rollouts are phased across multiple weeks, to ensure cluster and fleet
stability.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  v1.11.x

No v1.11.x versions this week.

###  v1.12.x

No v1.12.x versions this week.

**CHANGED:**

**Correction:** Istio was not upgraded to 1.1.3 in v1.12.7-gke.17. The [
release note for May 13, 2019 ](/kubernetes-engine/docs/release-
notes#may_13_2019) has been corrected.

###  v1.13.x

v1.13.6-gke.0 is available.

**FEATURE:**

This version includes support for [ GKE Sandbox ](/kubernetes-engine/docs/how-
to/sandbox-pods) .

**CHANGED:**

Update Istio to v1.1.3.

**CHANGED:**

Node images have been updated as follows:

  * The Node image for Container-Optimized OS nodes is now [ cos-u-73-11647-182-0 ](/container-optimized-os/docs/release-notes/m73) . 
  * The Node image for Ubuntu nodes is now [ ubuntu-gke-1804-d1809-0-v20190506 ](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1809-0-v20190506.manifest) . 

Nodes using these images are now [ shielded VMs ](/shielded-vm) with the
following properties:

  * [ UEFI ](http://www.uefi.org/sites/default/files/resources/UEFI_Secure_Boot_in_Modern_Computer_Security_Solutions_2013.pdf) boot is enabled. 
  * [ SecureBoot ](/security/shielded-cloud/shielded-vm#secure-boot) is disabled. 
  * [ vTPM ](/security/shielded-cloud/shielded-vm#vtpm) is enabled. 
  * [ Integrity Monitoring ](/security/shielded-cloud/shielded-vm#integrity-monitoring) is enabled. 

###  Rapid channel

No v1.14.x versions this week.

####  Versions no longer available

The following versions are no longer available for new clusters or cluster
upgrades:

  * 1.12.6-gke.10 

###  New features

**FEATURE:**

[ Google Cloud's operations suite Kubernetes Engine Monitoring
](/monitoring/kubernetes-engine) is now generally available for clusters using
the following GKE versions:

  * 1.12.x clusters v1.12.7-gke.17 and newer 
  * 1.13.x clusters v1.13.5-gke.10 and newer 
  * 1.14.x (Alpha) clusters v1.14.1-gke.5 and newer 

Users of the legacy Google Cloud's operations suite support are encouraged to
[ migrate to Google Cloud's operations suite Kubernetes Engine Monitoring
](/monitoring/kubernetes-engine/migration) before support for legacy Google
Cloud's operations suite is removed.

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * [ GKE Sandbox ](/kubernetes-engine/docs/how-to/sandbox-pods) support for v1.14.x (Alpha) clusters 
  * v1.14.x nodes will be [ shielded VMs ](/shielded-vm)
  * Early access to test Windows Containers, expected in early June 

##  May 13, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  Important changes to clusters running unsupported versions

In addition to GKE's [ version policy ](/kubernetes-engine/versioning-and-
upgrades) , Kubernetes has a [ version skew policy
](https://kubernetes.io/docs/setup/version-skew-policy/) of supporting only
the three newest minor versions. Older versions are not guaranteed to receive
bug fixes or security updates, and the control plane may become incompatible
with nodes running unsupported versions.

For example, the Kubernetes v1.13.x control plane is not compatible with nodes
running v1.10.x. Clusters in such a configuration could become unreachable or
fail to run your workloads correctly.

To keep your clusters operational and to protect Google's infrastructure, we
strongly recommend that you upgrade existing nodes to v1.11.x or higher before
the end of June 2019. At that time, Google will enable node auto-upgrade on
node pools older than v1.11.x, and these nodes will be updated to v1.11.x so
that the control plane can be upgraded to v1.13.x and remain compatible with
existing node pools.

We strongly recommend leaving node auto-upgrade enabled.

####  New default version

The default version for new clusters is now 1.12.7-gke.10 (previously
1.11.8-gke.6). If your cluster is using v1.12.6-gke.10, upgrade to this
version to avoid a potential issue that causes [ auto-repairing nodes
](/kubernetes-engine/docs/how-to/node-auto-repair) to fail.

####  Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

**Note:** Node auto-upgrade is no longer paused.  Current version  |  Upgrade
version  
---|---  
**All 1.10.x versions** , including v1.10.12-gke.14 (continuing after
unpausing node auto-upgrade)  |  v1.11.8-gke.6  
v1.11.x versions older than v1.11.8-gke.6  |  v1.11.8-gke.6  
  
Rollouts are phased across multiple weeks, to ensure cluster and fleet
stability.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

###  v1.11.x

#####  v1.11.9-gke.13

  * Improvements to Vertical Pod Autoscaler 
  * Improvements to Cluster Autoscaler 
  * Cloud Run for GKE now uses the default Istio sidecar injection behavior 
  * Fix an issue that prevented the kubelet from seeing all GPUs available to nodes using the Ubuntu node image. 

###  v1.12.x

#####  v1.12.7-gke.17

  * Upgrade Ingress controller to [ 1.5.2 ](https://github.com/kubernetes/ingress-gce/releases/tag/v1.5.2)
  * Improvements to Vertical Pod Autoscaler 
  * Improvements to Cluster Autoscaler 
  * Fix an issue that prevented the kubelet from seeing all GPUs available to nodes using the Ubuntu node image 
  * Fix an issue that sets the dynamic maximum volume count to 16 if your nodes use a custom machine type. The value is now set to 128. 

###  v1.13.x

#####  v1.13.5-gke.10

######  Upgrading to GKE v1.13.x

To prepare to upgrade your clusters, read the [ Kubernetes 1.13 release notes
](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.13.md#kubernetes-113-release-
notes) and the following information. You may need to modify your cluster
before upgrading.

**DEPRECATED:**

` scheduler.alpha.kubernetes.io/critical-pod ` is deprecated. To mark Pods as
critical, use [ Pod priority and preemption
](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/)
.

**DEPRECATED:**

` node.status.volumes.attached.devicePath ` is deprecated for Container
Storage Interface (CSI) volumes and will not be enabled in future releases.

**DEPRECATED:**

The built-in ` system:csi-external-provisioner ` and ` system:csi-external-
attacher ` Roles are no longer automatically created You can create your own
Roles and modify your Deployments to use them.

**DEPRECATED:**

Support for CSI drivers using 0.3 and older versions of the CSI API is
deprecated. Users should upgrade CSI drivers to use the 1.0 API during the
deprecation period.

**ISSUE:**

Kubernetes cannot distinguish between manually-provisioned zonal and regional
persistent disks with the same name. Ensure that persistent disks have unique
names across the Google Cloud project. This issue does not occur when using
dynamically provisioned persistent disks.

**ISSUE:**

If kubelet fails to register a CSI driver, it does not make a second attempt.
To work around this issue, restart the CSI driver Pod.

**ISSUE:**

After resizing a PersistentVolumeClaim (PVC), the PVC is sometimes left with a
spurious ` RESIZING ` condition when expansion has already completed. The
condition is spurious as long as the PVC's reported size is correct. If the
value of ` pvc.spec.capacity['storage'] ` matches `
pvc.status.capacity['storage'] ` , the condition is spurious and you can
delete or ignore it.

**ISSUE:**

The CSI ` driver-registrar external ` sidecar container v1.0.0 has a known
issue where it takes up to a minute to restart.

**CHANGED:**

DaemonSets now use scheduling features that require kubelet version 1.11 or
higher. Google will update kubelet to 1.11 before upgrading clusters to
v1.13.x.

**CHANGED:**

kubelet can no longer delete their Node API objects.

**CHANGED:**

Use of the ` --node-labels ` flag to set labels under the ` kubernetes.io/ `
and ` k8s.io/ ` prefix will be subject to restriction by the NodeRestriction
admission plugin in future releases. See the [ admission plugin documentation
](https://kubernetes.io/docs/reference/access-authn-authz/admission-
controllers/#noderestriction) for the list of allowed labels.

###  Rapid channel

#####  1.14.1-gke.5

**Note:** This content is also available separately in the [ Rapid channel
release notes ](/kubernetes-engine/docs/release-notes-rapid) .

GKE v1.14.1-gke.5 (alpha) is now available for testing and validation in the
Rapid [ release channel ](/kubernetes-engine/docs/concepts/release-channels) .
For more details, refer to the [ release notes for Kubernetes v1.14
](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.14.md)
.

**CHANGED:**

GKE v1.14.x has the following differences from Kubernetes 1.14.x.

  * GKE v1.14.x uses ` kube-dns ` rather than ` core-dns ` . 
  * GKE v1.14.x does not support [ Dramatically Simplify Kubernetes Cluster Creation ](https://github.com/kubernetes/enhancements/issues/11) , a sub-feature of ` kubeadm ` . 
  * GKE v1.14.x does not support [ taint-based eviction ](https://github.com/kubernetes/kubernetes/issues/69533) . 

**ISSUE:**

You cannot yet create an alpha cluster running GKE v1.14.x. If you attempt to
use the ` --enable-kubernetes-alpha ` flag, cluster creation fails.

###  Security bulletin

**ISSUE:**

If you run untrusted code in your own multi-tenant services within Google
Kubernetes Engine, we recommend that you disable Hyper-Threading to mitigate
Microarchitectural Data Sampling (MDS) vulnerabilities announced by Intel. For
more information, see the [ security bulletin ](/kubernetes-
engine/docs/security-bulletins#may-14-2019) .

###  New features

**FEATURE:**

With GKE 1.13.5-gke.10, GKE 1.13 is now generally available for use in
production. You can upgrade clusters running older v1.13.x versions manually.

GKE v1.13.x has the following differences from Kubernetes 1.13:

  * GKE v1.13.x uses ` kube-dns ` rather than ` core-dns ` . 
  * GKE v1.13.x does not support [ Dramatically Simplify Kubernetes Cluster Creation ](https://github.com/kubernetes/enhancements/issues/11) , a sub-feature of ` kubeadm ` . 
  * GKE v1.13.x does not support [ taint-based eviction ](https://github.com/kubernetes/kubernetes/issues/69533) . 

For information about upgrading from v1.12.x, see **Upgrading to GKE v1.13.x**
in  New versions available for upgrades and new clusters  .

**FEATURE:**

We are introducing [ Release channels ](/kubernetes-
engine/docs/concepts/release-channels) , a new way to keep your GKE clusters
up to date. The Rapid release channel is available, and includes v1.14.1-gke.5
(alpha). You can [ sign up ](https://forms.gle/93EGYaLx6kn9rPEh9) to try
release channels and preview GKE v1.14.x.

**FEATURE:**

[ GKE Sandbox (Beta) ](/kubernetes-engine/docs/how-to/sandbox-pods) is now
available for clusters running v1.12.7-gke.17 and higher and v1.13.5-gke.15
and higher. You can use GKE Sandbox to isolate untrusted workloads in a
sandbox to protect your nodes, other workloads, and cluster metadata from
defective or malicious code.

###  Changes

**CHANGED:**

For clusters running v1.12.x or higher and using nodes with less than 1 GB of
memory, GKE reserves 255 MiB of memory. This is not a new change, but it was
not previously noted. For more details about node resources, see [ Allocatable
memory and CPU resources ](/kubernetes-engine/docs/concepts/cluster-
architecture#memory_cpu) .

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * [ GKE Sandbox ](/kubernetes-engine/docs/how-to/sandbox-pods) will be supported on v1.13.x clusters 

##  April 29, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  Scheduled automatic upgrades

**Masters only** with auto-upgrade enabled will be upgraded as follows:

Current version  |  Upgrade version  
---|---  
**All 1.10.x versions** , including v1.10.12-gke.14 (continuing)  |
1.11.8-gke.6  
1.13.4-gke.x  |  1.13.5-gke.10  
**Note:** Node auto-upgrade is currently disabled. You can continue to upgrade
node pools manually. Node auto-upgrade will be re-enabled in the coming weeks.

Rollouts are phased across multiple weeks, to ensure cluster and fleet
stability.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

  * 1.12.6-gke.11 
    * Nodes continue to use Docker as the default runtime. 
    * Fix a performance regression introduced in 1.12.6-gke.10. This regression caused delays when the kubelet reads the ` /sys/fs/cgroup/memory/memory.stat ` file to determine a node's memory usage. 

The following versions are no longer available for new clusters or cluster
upgrades:

  * 1.11.9-gke.5 
  * 1.12.7-gke.7 
  * 1.13.4-gke.10 
  * 1.13.5-gke.7 

###  Fixed issues

**FIXED:**

A problem was fixed in the Stackdriver Kubernetes Monitoring (Beta) Metadata
agent. This problem caused the agent to generate unnecessary log messages.

###  Changes

**CHANGED:**

[ Alpha clusters ](/kubernetes-engine/docs/concepts/alpha-clusters) running
Kubernetes 1.13 and higher created with the ` gcloud ` command-line tool
version 242.0.0 and higher have auto-upgrade and auto-repair disabled.
Previously, you were required to disable these feature manually.

###  Known issues

**ISSUE:**

Under certain circumstances, Google-managed SSL certificates (Beta) are not
being provisioned in regional clusters. If this happens, you are unable to
create or update managed certificates. If you are experiencing this issue, [
contact Google Cloud support ](/support) .

**ISSUE:**

Node auto-upgrade is currently disabled. You can still upgrade node pools
manually.

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * Node auto-upgrade will be re-enabled 
  * etcd will be upgraded 
  * Improvements to Vertical Pod Autoscaler 
  * Improvements to Cluster Autoscaler 
  * Improvements to Managed Certificates 

##  April 26, 2019

Due to delays during the [ April 22 GKE release rollout ](/kubernetes-
engine/docs/release-notes#april_22_2019) , the release will not complete by
April 26, 2019 as originally planned. Rollout is expected to complete by April
29, 2019 GMT.

##  April 25, 2019

###  Changes

**CHANGED:**

**Google Cloud's operations suite Kubernetes Monitoring users:** Google
Cloud's operations suite Kubernetes Monitoring logging label fields change
when you upgrade your GKE clusters to GKE v1.12.6 or higher. The following
changes were effective the week of March 26, 2019:

  * Kubernetes Pod labels, currently located in the ` metadata.userLabels ` field, are moved to the ` labels ` field in the LogEntry and the label keys have a prefix prefix of ` k8s-pod/ ` . The filter expressions in your [ sinks ](/logging/docs/export) , [ logs-based metrics ](/logging/docs/logs-based-metrics) , [ log exclusions ](/logging/docs/exclusions) , or queries might need to change. 
  * Google Cloud's operations suite system labels that are in the ` metadata.systemLabels ` field are no longer available. 

For detailed information about what changed, see the [ release guide
](/monitoring/kubernetes-engine/release-guide) for Google Cloud's operations
suite Beta Monitoring and Logging, also known as Google Cloud's operations
suite Kubernetes Monitoring (Beta).

##  April 22, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version  |  Upgrade version  
---|---  
**All 1.10.x versions** , including v1.10.12-gke.14  |  1.11.8-gke.6  
  
This roll-out will be phased across multiple weeks.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

  * 1.11.9-gke.8 

    * Node image for Container-Optimized OS updated to [ cos-69-10895-211-0 ](/container-optimized-os/docs/release-notes/m69)
      * Fix a performance regression introduced in v1.11.x node images older than 1.11.9-gke.8. This regression caused delays when the kubelet reads the ` /sys/fs/cgroup/memory/memory.stat ` file to determine a node's memory usage. 
    * Upgrade Node Problem Detector to [ 0.6.3 ](https://github.com/kubernetes/kubernetes/pull/76284)
  * 1.12.7-gke.10 

    * Node image for Container-Optimized OS updated to [ cos-69-10895-211-0 ](/container-optimized-os/docs/release-notes/m69)
      * Fix a performance regression introduced in v1.12.x node images older than v1.12.6-gke.10. This regression caused delays when the kubelet reads the ` /sys/fs/cgroup/memory/memory.stat ` file to determine a node's memory usage. 
    * Upgrade Node Problem Detector to [ 0.6.3 ](https://github.com/kubernetes/kubernetes/pull/76285)
  * 1.13.5-gke.10 (Preview) 

    * To create a cluster, use the following command, replacing `  my-alpha-cluster  with the name of your cluster: 
        
                gcloud container clusters create my-alpha-cluster \
          --cluster-version=1.13.5-gke.10 \
          --enable-kubernetes-alpha \
          --no-enable-autorepair
        

    * Upgrade Node Problem Detector to [ 0.6.3 ](https://github.com/kubernetes/kubernetes/pull/76286)

The following versions are no longer available for new clusters or cluster
upgrades:

  * **All 1.10.x versions** , including v1.10.12-gke.14 

###  Fixed issues

**FIXED:**

A known issue in v1.12.6-gke.10 and older has been fixed in 1.12.7-gke.10.
This issue causes node auto-repair to fail. Upgrading is recommended.

**FIXED:**

A known issue in 1.12.7-gke.7 and older has been fixed in 1.12.7-gke.10. The `
currentMetrics ` field now reports the correct value. The problem only
affected reporting and did not impact the functionality of Horizontal Pod
Autoscaler.

###  Deprecations

GKE v1.10.x has been deprecated, and is no longer available for new clusters,
master upgrades, or node upgrades.

The ` Cluster.FIELDS.initial_node_count ` field has been deprecated in favor
of ` nodePool.initial_node_count ` in the ` v1 ` and ` v1beta1 ` GKE APIs.

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * etcd will be upgraded 
  * Improvements to Vertical Pod Autoscaler 
  * Improvements to Cluster Autoscaler 
  * Improvements to Managed Certificates 

##  April 19, 2019

**CHANGED:**

You can now use [ Usage metering ](/kubernetes-engine/docs/how-to/cluster-
usage-metering) with GKE 1.12.x and 1.13.x clusters.

##  April 18, 2019

**FEATURE:**

You can now run GKE clusters in region ` asia-northeast2 ` (Osaka, Japan) with
zones ` asia-northeast2-a ` , ` asia-northeast2-b ` , and ` asia-northeast2-c
` .

The new region and zones will be included in future rollout schedules.

##  April 15, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  New default version

The default version for new clusters has been updated to 1.11.8-gke.6
(previously 1.11.7-gke.12).

####  Scheduled automatic upgrades

Masters and nodes with auto-upgrade enabled will be upgraded:

Current version  |  Upgrade version  
---|---  
1.10.x versions 1.10.12-gke.13 and older  |  1.10.12-gke.14  
1.11.x versions 1.11.8-gke.5 and older  |  1.11.8-gke.6  
1.12.x versions 1.12.6-gke.9 and older  |  1.12.6-gke.10  
1.13.x versions 1.13.4-gke.9 and older  |  1.13.4-gke.10 (Preview)  
  
####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

  * 1.11.9-gke.5 
    * Node image for Container-Optimized OS updated to [ cos-69-10895-201-0 ](/container-optimized-os/docs/release-notes/m69)
      * This release note previously stated, in error, that Docker was upgraded. However, the Docker version is still 17.03 in this image. 
      * Apply a restart policy to the Docker daemon, so that it attempts to restart every 10 seconds if it is not running, with no maximum number of retries. 
      * Apply security update for [ CVE-2019-8912 ](https://people.canonical.com/%7Eubuntu-security/cve/2019/CVE-2019-8912.html)
    * Node image for Ubuntu updated to [ ubuntu-gke-1804-d1703-0-v20190409 ](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1809-0-v20190409.manifest)
      * This release note previously stated, in error, that Docker was upgraded. However, the Docker version is still 17.03 in this image. 
      * Apply a restart policy to the Docker daemon, so that it attempts to restart every 10 seconds if it is not running, with no maximum number of retries. 
      * Apply security update for [ CVE-2019-8912 ](https://people.canonical.com/%7Eubuntu-security/cve/2019/CVE-2019-8912.html)
    * Upgrade [ Cloud Run on GKE ](/run/docs/gke/release-notes) to 0.5.0 
    * Upgrade containerd to [ 1.1.7 ](https://github.com/containerd/containerd/releases/tag/v1.1.7)
  * 1.12.7-gke.7 
    * Node image for Container-Optimized OS updated to [ cos-69-10895-201-0 ](/container-optimized-os/docs/release-notes/m69)
      * This release note previously stated, in error, that Docker was upgraded. However, the Docker version is still 17.03 in this image. 
      * Apply a restart policy to the Docker daemon, so that it attempts to restart every 10 seconds if it is not running, with no maximum number of retries. 
      * Apply security update for [ CVE-2019-8912 ](https://people.canonical.com/%7Eubuntu-security/cve/2019/CVE-2019-8912.html)
    * Node image for Ubuntu updated to [ ubuntu-gke-1804-d1703-0-v20190409 ](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1809-0-v20190409.manifest)
      * This release note previously stated, in error, that Docker was upgraded. However, the Docker version is still 17.03 in this image. 
      * Apply a restart policy to the Docker daemon, so that it attempts to restart every 10 seconds if it is not running, with no maximum number of retries. 
      * Apply security update for [ CVE-2019-8912 ](https://people.canonical.com/%7Eubuntu-security/cve/2019/CVE-2019-8912.html)
    * Upgrade [ Cloud Run on GKE ](/run/docs/gke/release-notes) to 0.5.0 
    * Upgrade containerd to [ 1.2.6 ](https://github.com/containerd/containerd/releases/tag/v1.1.7)
  * 1.13.5-gke.7 (Preview) 

    * To create a cluster, use the following command, replacing `  my-alpha-cluster  with the name of your cluster: 
        
                gcloud container clusters create my-alpha-cluster \
          --cluster-version=1.13.5-gke.7 \
          --enable-kubernetes-alpha \
          --no-enable-autorepair
        

    * Node image for Container-Optimized OS updated to [ cos-u-73-11647-121-0 ](/container-optimized-os/docs/release-notes/m73)

      * Upgrade Docker from 17.03 to 18.09 
      * Apply a restart policy to the Docker daemon, so that it attempts to restart every 10 seconds if it is not running, with no maximum number of retries. 
      * Apply security update for [ CVE-2019-8912 ](https://people.canonical.com/%7Eubuntu-security/cve/2019/CVE-2019-8912.html)
    * Node image for Ubuntu updated to [ ubuntu-gke-1804-d1809-0-v20190402a ](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1809-0-v20190402a.manifest)

      * Upgrade Docker from 17.03 to 18.09 
      * Apply a restart policy to the Docker daemon, so that it attempts to restart every 10 seconds if it is not running, with no maximum number of retries. 
      * Apply security update for [ CVE-2019-8912 ](https://people.canonical.com/%7Eubuntu-security/cve/2019/CVE-2019-8912.html)
    * Upgrade [ Cloud Run on GKE ](/run/docs/gke/release-notes) to 0.5.0 

    * Upgrade containerd to [ 1.2.6 ](https://github.com/containerd/containerd/releases/tag/v1.1.7)

    * Improvements to volume operation metrics 

    * Cluster Autoscaler is now supported for GKE 1.13 clusters 

    * Fix a problem that caused the ` currentMetrics ` field for Horizontal Pod Autoscaler with 'AverageValue' target to always report ` unknown ` . The problem only affected reporting and did not impact the functionality of Horizontal Pod Autoscaler. 

The following versions are no longer available for new clusters or cluster
upgrades:

  * 1.10.12-gke.7 
  * 1.10.12-gke.9 
  * 1.11.6-gke.11 
  * 1.11.6-gke.16 
  * 1.11.7-gke.12 
  * 1.11.7-gke.18 
  * 1.11.8-gke.2 
  * 1.11.8-gke.4 
  * 1.11.8-gke.5 
  * 1.12.5-gke.5 
  * 1.12.6-gke.7 
  * 1.13.4-gke.1 
  * 1.13.4-gke.5 

###  Changes

**CHANGED:**

Improvements have been made to the automated rules for the [ add-on resizer
](/kubernetes-engine/docs/how-to/small-cluster-tuning) . It now uses 5 nodes
as the inflection point.

###  Known issues

**ISSUE:**

GKE 1.12.7-gke.7 and older, and 1.13.4-gke.10 and older have a known issue
where the ` currentMetrics ` field for Horizontal Pod Autoscaler with `
AverageValue ` target always reports ` unknown ` . The problem only affects
reporting and does not impact the functionality of Horizontal Pod Autoscaler.

This issue has already been fixed in GKE 1.13.5-gke.7.

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * Version 1.10.x will soon be unvailable for new clusters. 
  * The known issue published this week about Horizontal Pod Autoscaler metrics will be fixed in GKE 1.12.x as well. 
  * etcd will be upgraded. 

##  April 2, 2019

**FIXED:**

The following GKE releases contain a security update that addresses [
CVE-2019-9900 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900)
and [ CVE-2019-9901. ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2019-9901) For more information, see the [ security
bulletin ](/kubernetes-engine/docs/security-bulletins#april-05-2019) .

This release note was expanded with more information after an embargo about
the vulnerabilities was lifted.

  * 1.10.12-gke.14 
  * 1.11.6-gke.16 
  * 1.11.7-gke.18 
  * 1.11.8-gke.6 
  * 1.12.6-gke.10 
  * 1.13.4-gke.10 (Public preview) 
    * To create a cluster, use the following command, replacing ` my-alpha-cluster  ` with the name of your cluster: 
        
                gcloud container clusters create my-alpha-cluster \
          --cluster-version=1.13.4-gke.10 \
          --enable-kubernetes-alpha \
          --no-enable-autorepair
            

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

##  March 26, 2019

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

  * 1.11.8-gke.5 
    * Improvements to Cluster Autoscaler 
    * Improvements to gVisor 
  * 1.12.6-gke.7 
    * Improvements to Cluster Autoscaler 
    * Update Ingress controller to [ 1.5.1 ](https://github.com/kubernetes/ingress-gce/releases/tag/v1.5.1)
    * Update containerd to [ 1.2.5 ](https://github.com/containerd/containerd/releases/tag/v1.2.5)
  * 1.13.4-gke.5 (public preview) 

    * To create a cluster, use the following command, replacing ` my-alpha-cluster  ` with the name of your cluster: 
        
                gcloud container clusters create my-alpha-cluster \
        --cluster-version=1.13.4-gke.5 \
        --enable-kubernetes-alpha \
        --no-enable-autorepair
        

    * Improvements to Vertical Pod Autoscaler 
    * Improvements to gVisor 
    * Update Ingress controller to [ 1.5.1 ](https://github.com/kubernetes/ingress-gce/releases/tag/v1.5.1)

    * Update containerd to [ 1.2.5 ](https://github.com/containerd/containerd/releases/tag/v1.2.5)

    * Cluster Autoscaler is not operational in this GKE version. 

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

##  March 19, 2019

###  GKE 1.13 public preview

GKE 1.13.4-gke.1 is available for [ alpha clusters ](/kubernetes-
engine/docs/concepts/alpha-clusters) as a public preview. The preview period
helps Google Cloud to improve the quality of the final GA release, and allows
you to test the new version earlier.

To create a cluster using this version, use the following command, replacing `
my-alpha-cluster  ` with the name of your cluster. Use the exact cluster
version provided in the command. You can add other configuration options, but
do not change any of the ones below.

    
    
    gcloud container clusters create my-alpha-cluster \
      --cluster-version=1.13.4-gke.1 \
      --enable-kubernetes-alpha \
      --no-enable-autorepair
    

**Note:** Preview versions of GKE are not listed in the available cluster
versions in Google Cloud Platform Console.

Alpha clusters become unavailable after 30 days.

####  Changes

  * The preview uses ` kube-dns ` rather than ` core-dns ` . 
  * The preview does not support [ Dramatically Simplify Kubernetes Cluster Creation ](https://github.com/kubernetes/enhancements/issues/11) , a sub-feature of ` kubeadm ` . 
  * The preview does not support [ taint-based eviction ](https://github.com/kubernetes/kubernetes/issues/69533) . 

###  Version updates

GKE cluster versions have been updated.

Note: Your clusters might not have these versions available. Rollouts begin on
the day of the note and take four or more business days to be completed across
all Google Cloud zones. For more information, see the [ Rollout schedule
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades and node upgrades for existing clusters. See [ these
instructions ](/kubernetes-engine/versioning-and-upgrades#available_versions)
for more information on the Kubernetes versioning scheme.

  * 1.11.8-gke.4 
    * New Ubuntu node image [ ubuntu-gke-1804-d1703-0-v20190307b ](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-gke-1804-d1703-0-v20190307b.manifest)
      * Update Nvidia GPU driver to 410 
      * Fix [ USN-3887-1: snapd vulnerability ](https://usn.ubuntu.com/3887-1/)
    * Update Istio to 1.0.6 
    * Improvements to Vertical Pod Autoscaler 
    * Fix CVE-2019-1002100. For more information, see the [ security bulletin ](/kubernetes-engine/docs/security-bulletins#march-01-2019) . 
  * 1.13.4-gke.1 (see  GKE 1.13 public preview  for limitations and more information) 
    * Includes the fix for CVE-2019-1002100. For more information, see the [ security bulletin ](/kubernetes-engine/docs/security-bulletins#march-01-2019) . 
    * Known issues 
      * GKE 1.13.4-gke.1 clusters may experience a  previously-published known issue  related to elevated master error rates, if Namespaces exist with names longer than 44 characters. To work around the issue, use shorter Namespace names. 
      * Cluster autoscaler is not operational in this GKE version. 

The following versions are no longer available for new clusters or cluster
upgrades:

  * 1.11.5-gke.5 
  * 1.11.6-gke.2 
  * 1.11.6-gke.3 
  * 1.11.6-gke.6 
  * 1.11.6-gke.8 
  * 1.11.7-gke.4 
  * 1.11.7-gke.6 

**DEPRECATED:**

GKE 1.12.5-gke.10 is no longer available for new clusters, master upgrades, or
node upgrades.

Last week, we began to make GKE 1.12.5-gke.10 unavailable for new clusters or
upgrades, due to increased error rates. That process completes this week.

If you have already upgraded to 1.12.5-gke.10 and are experiencing elevated
error rates, you can [ contact support ](https://cloud.google.com/support-
hub/) .

####  Automated master and node upgrades

The following versions will be updated for masters and nodes with auto-upgrade
enabled. Automated upgrades are rolled out over multiple weeks to ensure
cluster stability.

  * 1.11.6 Masters and nodes with auto-upgrade enabled which are using versions 1.11.6-gke.10 or earlier will begin to be upgraded to 1.11.7-gke.12. 
  * 1.11.7 Masters and nodes with auto-upgrade enabled which are using version 1.11.7-gke.11 or earlier will begin to be upgraded to 1.11.7-gke.12. 

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * Nodes with auto-upgrade enabled and masters running 1.11.x will be upgraded to 1.11.7-gke.12 
  * GKE 1.12.x masters will begin using the containerd runtime with an upcoming release. 

##  March 14, 2019

**DEPRECATED:**

GKE 1.12.5-gke.10 is no longer available for new clusters or master upgrades.

We have received reports of master nodes experiencing elevated error rates
when upgrading to version 1.12.5-gke.10 in all regions. Therefore, we have
begun the process of making it unavailable for new clusters or upgrades.

If you have already upgraded to 1.12.5-gke.10 and are experiencing elevated
error rates, you can [ contact support ](https://cloud.google.com/support-
hub/) .

##  March 11, 2019

**FEATURE:**

You can now run GKE clusters in region ` europe-west6 ` (Zürich, Switzerland)
with zones ` europe-west6-a ` , ` europe-west6-b ` , and ` europe-west6-c ` .

The new region and zones will be included in future rollout schedules.

##  March 5, 2019

###  Version updates

GKE cluster versions have been updated.  Note: Your clusters might not have
these versions available. Rollouts begin on the day of the note and take four
or more business days to be completed across all Google Cloud zones. For more
information, see the [ Rollout schedule ](/kubernetes-engine/versioning-and-
upgrades#rollout_schedule) .

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades for existing clusters:

  * 1.10.12-gke.7 - This version is being made available again after being previously removed. 
  * 1.10.12-gke.9 
  * 1.11.7-gke.12 
  * 1.12.5-gke.10 

####  Node image updates

**CHANGED:**

#####  Container-Optimized OS with containerd image for GKE 1.11 clusters

The Container-Optimized OS with containerd node image has been upgraded from `
cos-69-10895-138-0-c115 ` to ` cos-69-10895-138-0-c116 ` for clusters running
**Kubernetes 1.11+** .

See [ COS image release notes ](/container-optimized-os/docs/release-notes)
and the [ containerd v1.1.5 to v1.1.6 changelog
](https://github.com/containerd/containerd/compare/v1.1.5...v1.1.6) for more
information.

#####  Container-Optimized OS with containerd image for GKE 1.12 clusters

The Container-Optimized OS with containerd node image has been upgraded from `
cos-69-10895-138-0-c123 ` to ` cos-69-10895-138-0-c124 ` for clusters running
**Kubernetes 1.12.5-gke.10+** and alpha clusters running **Kubernetes 1.13+**
.

` cos-69-10895-138-0-c124 ` upgrades Docker to v18.09.0.

See [ COS image release notes ](/container-optimized-os/docs/release-notes)
and the [ containerd v1.2.3 to v1.2.4 changelog
](https://github.com/containerd/containerd/compare/v1.2.3...v1.2.4) for more
information.

###  Other Updates

  * GKE Ingress has been upgraded from v1.4.3 to v1.5.0 for clusters running 1.12.5-gke.10+. For details, see the detailed [ changelog ](https://github.com/kubernetes/ingress-gce/blob/master/CHANGELOG.md) and [ release notes ](https://github.com/kubernetes/ingress-gce/releases) . 

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * Nodes with auto-upgrade enabled and masters running 1.11.x will be upgraded to 1.11.7-gke.12 

##  February 27, 2019

GKE 1.12.5-gke.5 is generally available and includes Kubernetes 1.12.
Kubernetes 1.12 provides faster auto-scaling, faster affinity scheduling,
topology-aware dynamic provisioning of storage, and advanced audit logging.
For more information, see [ Digging into Kubernetes 1.12
](https://cloud.google.com/blog/products/containers-kubernetes/digging-into-
kubernetes-1-12) on the GCP blog.

###  Version updates

GKE cluster versions have been updated.  Note: Your clusters might not have
these versions available. Rollouts begin on the day of the note and take four
or more business days to be completed across all Google Cloud zones. For more
information, see the [ Rollout schedule ](/kubernetes-engine/versioning-and-
upgrades#rollout_schedule) .

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades for existing clusters:

  * 1.12.5-gke.5 

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  Known issues

**ISSUE:** A known issue in GKE 1.12.5-gke.5 and all 1.11.x versions below
1.11.6 can cause significant delays when the cluster autoscaler adds new nodes
to the cluster, if the cluster has hundreds of unschedulable Pods due to
resource starvation. It may require a few minutes before all Pods are
scheduled, depending on the number of unschedulable Pods and the size of the
cluster. The workaround is to add an adequate number of nodes manually. If
adding nodes does not resolve the issue, [ contact support
](https://cloud.google.com/support-hub/) .

**ISSUE:** A known issue in GKE 1.12.5-gke.5 can cause unbounded memory usage.
This is caused by a memory leak in ReflectorMetricsProvider. See [ this issue
](https://github.com/kubernetes/kubernetes/issues/73587) for further details.
This will be fixed in an upcoming patch.

**ISSUE:** A known issue in GKE 1.12.5-gke.5 slows down or stops Pod
scheduling in clusters with large numbers of terminated Pods. See [ this issue
](https://github.com/kubernetes/kubernetes/issues/74412) for further details.
This will be fixed in an upcoming patch.

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * Nodes with auto-upgrade enabled and masters running 1.10 will begin to be upgraded to 1.11 

##  February 18, 2019

###  Version updates

GKE cluster versions have been updated.  Note: Your clusters might not have
these versions available. Rollouts begin on the day of the note and take four
or more business days to be completed across all Google Cloud zones. For more
information, see the [ Rollout schedule ](/kubernetes-engine/versioning-and-
upgrades#rollout_schedule) .

####  New default version for new clusters

Kubernetes version 1.11.7-gke.4 is the default version for new clusters,
available according to this week's rollout schedule.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades for existing clusters:

  * 1.11.7-gke.6 

####  Versions no longer available

The following versions are no longer available for new clusters or cluster
upgrades:

  * 1.10.x 

####  Node image updates

**CHANGED:**

The Container-Optimized OS node image has been upgraded from `
cos-69-10895-123-0 ` to ` cos-69-10895-138-0 ` . See COS image [ release notes
](/container-optimized-os/docs/release-notes) for more information.

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  New Features

**FEATURE:** GKE Ingress has been upgraded from v1.4.2 to v1.4.3 for clusters
running 1.11.7-gke.6+. For details, see the [ detailed changelog
](https://github.com/kubernetes/ingress-gce/blob/master/CHANGELOG.md) and [
release notes ](https://github.com/kubernetes/ingress-gce/releases/tag/v1.4.3)
.

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * GKE 1.12 will be made generally available. 
  * Nodes with auto-upgrade enabled and masters running 1.10 will begin to be upgraded to 1.11.7-gke.4. 

##  February 11, 2019

###  Version updates

GKE cluster versions have been updated.  Note: Your clusters might not have
these versions available. Rollouts begin on the day of the note and take four
or more business days to be completed across all Google Cloud zones. For more
information, see the [ Rollout schedule ](/kubernetes-engine/versioning-and-
upgrades#rollout_schedule) .

####  New versions available for upgrades and new clusters

The following Kubernetes versions will be available for new clusters and for
opt-in master upgrades of existing clusters this week according to the rollout
schedule:

  * 1.11.6-gke.11 
  * 1.11.7-gke.4 
  * 1.10.12-gke.7 

####  Versions no longer available

The following versions are no longer available for new clusters or cluster
upgrades:

  * 1.11.6-gke.0 

####  Node image updates

**CHANGED:**

The Ubuntu node image has been upgraded to [ ` ubuntu-
gke-1604-d1703-0-v20190124 ` ](https://storage.googleapis.com/ubuntu-os-gke-
cloud/ubuntu-gke-1604-d1703-0-v20190124.manifest) for clusters running
**1.10.12-gke.7** .

The Ubuntu node image has been upgraded to [ ` ubuntu-
gke-1804-d1703-0-v20190124 ` ](https://storage.googleapis.com/ubuntu-os-gke-
cloud/ubuntu-gke-1804-d1703-0-v20190124.manifest) for clusters running
**1.11.6-gke.11** , **1.11.7-gke.4** and **1.12.5-gke.5 (EAP)** .

**Changes:**

  * This image contains security patch for [ USN-3863-1: APT vulnerability ](https://usn.ubuntu.com/3863-1) . 
  * This image contains security patch for [ CVE-2019-5736. ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5736)

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  New Features

  * [ Node auto-repair ](/kubernetes-engine/docs/how-to/node-auto-repair) and [ node auto-upgrade ](/kubernetes-engine/docs/how-to/node-auto-upgrades) are supported on Ubuntu nodes with GKE version 1.11.4-gke.8 and above. 
  * [ Node auto-provisioning ](/kubernetes-engine/docs/how-to/node-auto-provisioning) is now available in regional clusters with GKE 1.11.7 and above. 

##  January 28, 2019

###  Version updates

Kubernetes Engine cluster versions have been updated as detailed in the
following sections. See [ these instructions ](/kubernetes-engine/versioning-
and-upgrades#available_versions) to get a full list of the Kubernetes versions
you can run on your Kubernetes Engine masters and nodes.

For information about changes expected in the coming weeks, see  Coming soon
.

####  New default version for new clusters

GKE version 1.11.6-gke.2 is the default version for new clusters, available
according to this week's rollout schedule.

####  New versions available for upgrades and new clusters

The following Kubernetes Engine versions are available, according to this
week's rollout schedule, for new clusters and for opt-in master upgrades for
existing clusters:

  * 1.11.6-gke.6 

####  GKE Ingress controller update

**CHANGED:**

GKE Ingress has been upgraded from v1.4.1 to v1.4.2 for clusters running
1.11.6-gke.6+. For details, see the [ change log
](https://github.com/kubernetes/ingress-gce/blob/master/CHANGELOG.md) and the
[ release notes ](https://github.com/kubernetes/ingress-
gce/releases/tag/v1.4.2) .

###  Fixed Issues

**FIXED:**

A bug in version 1.10.x and 1.11.x may lead to periodic persistent disk commit
latency spikes exceeding one second. This may trigger master re-elections of
GKE components and cause short (a few seconds) periods of unavailability in
the cluster control plane. The issue is fixed in version 1.11.6-gke.6.

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * 25% of the upgrades from 1.10 to 1.11.6-gke.2 will be complete. 
  * Version 1.11.6-gke.8 will be made available. 
  * Version 1.10 will be made unavailable. 

##  January 21, 2019

###  Version updates

Kubernetes Engine cluster versions have been updated as detailed in the
following sections. See [ these instructions ](/kubernetes-engine/versioning-
and-upgrades#available_versions) to get a full list of the Kubernetes versions
you can run on your Kubernetes Engine masters and nodes.

For information about changes expected in the coming weeks, see  Coming soon
.

####  New default version for new clusters

Kubernetes version 1.10.11-gke.1 is the default version for new clusters,
available according to this week's rollout schedule.

####  New versions available for upgrades and new clusters

The following Kubernetes Engine versions are now available for new clusters
and for opt-in master upgrades for existing clusters:

  * 1.10.12-gke.1 
  * 1.11.6-gke.3 

The following versions are no longer available for new clusters or cluster
upgrades:

  * 1.10.6-gke.13 
  * 1.10.7-gke.11 
  * 1.10.7-gke.13 
  * 1.10.9-gke.5 
  * 1.10.9-gke.7 
  * 1.11.2-gke.26 
  * 1.11.3-gke.24 
  * 1.11.4-gke.13 

####  Scheduled master auto-upgrades

  * Cluster masters running 1.10.x will be upgraded to 1.10.11-gke.1. 
  * Cluster masters running 1.11.2 through 1.11.4 will be upgraded to 1.11.5-gke.5. 

####  Scheduled node auto-upgrades

Cluster nodes with auto-upgrade enabled will be upgraded:

  * 1.10.x nodes with auto-upgrade enabled will be upgraded to 1.10.11-gke.1. 
  * 1.11.2 through 1.11.4 nodes with auto-upgrade enabled will be upgraded to 1.11.5-gke.5. 

###  Changes

**CHANGED:**

GKE will not set ` --max-nodes-total ` , because ` --max-nodes-total ` is
inaccurate when the cluster uses [ Flexible Pod CIDR ranges ](/kubernetes-
engine/docs/how-to/flexible-pod-cidr) . This will be gated in 1.11.7+.

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * GKE 1.11.6-gke.6 will be available. 
  * A new COS image will be available. 

##  January 14, 2019

###  Version updates

Kubernetes Engine cluster versions have been updated as detailed in the
following sections. See [ these instructions ](/kubernetes-engine/versioning-
and-upgrades#available_versions) to get a full list of the Kubernetes versions
you can run on your Kubernetes Engine masters and nodes.

For information about changes expected in the coming weeks, see  Coming soon
.

####  New versions available for upgrades and new clusters

The following Kubernetes Engine versions are now available for new clusters
and for opt-in master upgrades for existing clusters:

  * 1.10.12-gke.0 
  * 1.11.6-gke.0 
  * 1.11.6-gke.2 

The following versions are no longer available for new clusters or cluster
upgrades:

  * 1.11.2-gke.25 
  * 1.11.3-gke.23 
  * 1.11.4-gke.12 
  * 1.11.5-gke.4 

####  Scheduled master auto-upgrades

  * Cluster masters running 1.9.x will be upgraded to 1.10.9-gke.5. 
  * Cluster masters running 1.11.2-gke.25 will be upgraded to 1.11.2-gke.26. 
  * Cluster masters running 1.11.3-gke.23 will be upgraded to 1.11.3-gke.24. 
  * Cluster masters running 1.11.4-gke.12 will be upgraded to 1.11.4-gke.13. 
  * Cluster masters running 1.11.5-gke.4 will be upgraded to 1.11.5-gke.5. 

####  Scheduled node auto-upgrades

Cluster nodes with auto-upgrade enabled will be upgraded:

  * 1.9.x nodes with auto-upgrade enabled will be upgraded to 1.10.9-gke.5. 
  * 1.11.2-gke.25 nodes with auto-upgrade enabled will be upgraded to 1.11.2-gke.26. 
  * 1.11.3-gke.23 nodes with auto-upgrade enabled will be upgraded to 1.11.3-gke.24. 
  * 1.11.4-gke.12 nodes with auto-upgrade enabled will be upgraded to 1.11.4-gke.13. 
  * 1.11.5-gke.4 nodes with auto-upgrade enabled will be upgraded to 1.11.5-gke.5. 

####  GKE Ingress controller update

The GKE Ingress controller has been upgraded from v1.4.0 to v1.4.1 for
clusters running 1.11.6-gke.2+. For details, see the [ change log
](https://github.com/kubernetes/ingress-gce/blob/master/CHANGELOG.md) and the
[ release notes ](https://github.com/kubernetes/ingress-
gce/releases/tag/v1.4.1) .

###  Fixed Issues

**FIXED:**

If you use Stackdriver Kubernetes Monitoring Beta with structured JSON
logging, an issue with the parsing of structured JSON log entries was
introduced in GKE v1.11.4-gke.12. See [ release guide for Stackdriver
Kubernetes Monitoring ](/monitoring/kubernetes-engine/release-guide) . This is
fixed by upgrading your cluster:

  * 1.11.6-gke.2 

**FIXED:**

Users of GKE 1.11.2.x, 1.11.3-gke.18, 1.11.4-gke.8, or 1.11.5-gke.2 on
clusters that use Calico network policies may experience failures due to a
problem recreating the ` BGPConfigurations.crd.projectcalico.org ` resource.
This is fixed by the automatic upgrades to masters and nodes that have auto-
upgrade enabled.

**FIXED:**

A problem in Endpoints API object validation could prevent updates during an
upgrade, leading to stale network information for Services. Symptoms of the
problem include failed healthchecks with a ` 502 ` status code or a message
such as ` Forbidden: Cannot change NodeName ` . This is fixed by the automatic
upgrades to masters and nodes that have auto-upgrade enabled.

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * All GKE 1.10.x masters will be upgraded to the latest 1.10 version. 
  * All GKE 1.11.0 through 1.11.4 masters will be upgraded to the latest 1.11.5 version. 

##  January 8, 2019

The rollout beginning January 8, 2019 has been paused after two days. This is
being done as a caution, so that we can investigate an issue that will be
fixed in next week's rollout. This is not a bug in any GKE version currently
available or planned to be made available.

##  December 17, 2018

###  Version updates

GKE cluster versions have been updated.  Note: Your clusters might not have
these versions available. Rollouts begin on the day of the note and take four
or more business days to be completed across all Google Cloud zones. For more
information, see the [ Rollout schedule ](/kubernetes-engine/versioning-and-
upgrades#rollout_schedule) .

For information about changes expected in the coming weeks, see  Coming soon
.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades for existing clusters:

  * 1.11.2-gke.26 
  * 1.11.3-gke.24 
  * 1.11.4-gke.13 
  * 1.11.5-gke.5 

The following versions are no longer available for new clusters or cluster
upgrades:

  * 1.11.2-gke.18 
  * 1.11.2-gke.20 
  * 1.11.3-gke.18 
  * 1.11.4-gke.8 

####  Scheduled master auto-upgrades

Remaining cluster masters running GKE 1.9.x will be upgraded to GKE
1.10.9-gke.5 in January 2019.

####  Scheduled node auto-upgrades

Cluster nodes with auto-upgrade enabled will be upgraded:

  * 1.11.2-gke.x nodes with auto-upgrade enabled will be upgraded to 1.11.2-gke.25 
  * 1.11.3-gke.x nodes with auto-upgrade enabled will be upgraded to 1.11.3-gke.23 
  * 1.11.4-gke.x nodes with auto-upgrade enabled will be upgraded to 1.11.4-gke.12 
  * 1.11.5-gke.x nodes with auto-upgrade enabled will be upgraded to 1.11.5-gke.4 

###  Fixed Issues

**FIXED:**

Users upgrading to GKE 1.11.2.x, 1.11.3-gke.18, 1.11.4-gke.8, or 1.11.5-gke.2
on clusters that use Calico network policies may experience failures due to a
problem recreating the ` BGPConfigurations.crd.projectcalico.org ` resource.
This problem does not affect newly-created clusters. This is fixed by
upgrading your to one of the following versions:

  * 1.11.2-gke.25 
  * 1.11.3-gke.23 
  * 1.11.4-gke.12 
  * 1.11.5-gke.4 

**FIXED:**

A problem in Endpoints API object validation could prevent updates during an
upgrade, leading to stale network information for Services. Symptoms of the
problem include failed healthchecks with a ` 502 ` status code or a message
such as ` Forbidden: Cannot change NodeName ` . If you encounter this problem,
upgrade your cluster to one of the following versions:

  * 1.11.2-gke.26 
  * 1.11.3-gke.24 
  * 1.11.4-gke.13 
  * 1.11.5-gke.5 

This problem can also affect earlier versions of GKE, but the fix is not yet
available for those versions. If you are running an earlier version and
encounter this issue, [ contact support ](/support-hub) .

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * Remaining GKE 1.9.x masters are expected to be upgraded in January 2019. 

##  December 10, 2018

###  Version updates

GKE cluster versions have been updated.  Note: Your clusters might not have
these versions available. Rollouts begin on the day of the note and take four
or more business days to be completed across all Google Cloud zones. For more
information, see the [ Rollout schedule ](/kubernetes-engine/versioning-and-
upgrades#rollout_schedule) .

For information about changes expected in the coming weeks, see  Coming soon
.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades for existing clusters:

  * 1.10.11-gke.1 
  * 1.11.2-gke.25 
  * 1.11.3-gke.23 
  * 1.11.4-gke.12 
  * 1.11.5-gke.4 

The following versions are no longer available for new clusters or cluster
upgrades:

  * 1.9.x 
  * 1.10.6-gke.11 

####  Scheduled master auto-upgrades

We will begin upgrading cluster masters running GKE 1.9.x to GKE 1.10.9-gke.5.
The upgrade will be completed in January 2019.

####  Scheduled node auto-upgrades

Cluster nodes with auto-upgrade enabled will be upgraded:

  * 1.11.2-gke.x nodes with auto-upgrade enabled will be upgraded to 1.11.2-gke.25 
  * 1.11.3-gke.x nodes with auto-upgrade enabled will be upgraded to 1.11.3-gke.23 
  * 1.11.4-gke.x nodes with auto-upgrade enabled will be upgraded to 1.11.4-gke.12 
  * 1.11.5-gke.x nodes with auto-upgrade enabled will be upgraded to 1.11.5-gke.4 

####  Node image updates

**CHANGED:**

Container-Optimized OS node image has been upgraded to ` cos-
stable-69-10895-91-0 ` for clusters running **Kubernetes 1.11.2** ,
**Kubernetes 1.11.3** , **Kubernetes 1.11.4** , and **Kubernetes 1.11.5** ..

**Changes:**

  * containerd has been upgraded from 1.1.2 to 1.1.5. Refer to the COS image [ release notes ](/container-optimized-os/docs/release-notes) and the [ containerd changelog ](https://www.google.com/url?q=https://github.com/containerd/containerd/compare/v1.1.2...v1.1.5&sa=D&ust=1544664090277000&usg=AFQjCNH11OOTWA13hVz45R8LUwfE_ohH1g) for details. 

###  Fixed Issues

**FIXED:**

Users upgrading to GKE 1.11.3 on clusters that use Calico network policies may
experience failures due to a problem recreating the `
BGPConfigurations.crd.projectcalico.org ` resource. This problem does not
affect newly-created clusters. This is fixed by upgrading your GKE 1.11.3
clusters to 1.11.3-gke.23.

**FIXED:**

Users modifying or upgrading existing GKE 1.11.x clusters that use Alias IP
may experience network failures due to a mismatch between the new IP range
assigned the Pods and the alias IP address range for the nodes. This is fixed
by upgrading your GKE 1.11.x clusters to one of the following versions:

  * 1.11.2-gke.25 
  * 1.11.3-gke.23 
  * 1.11.4-gke.12 
  * 1.11.5-gke.4 

###  Changes

**CHANGED:**

Node Problem Detector (NPD) has been upgraded from 0.5.0 to 0.6.0 for clusters
running GKE 1.10.11-gke.1+ and 1.11.5-gke.1+. For details, see the [ upstream
pull request ](https://github.com/kubernetes/kubernetes/pull/71522) .

###  Known Issues

**ISSUE:**

In GKE v1.11.4-gke.12 and later, if you use Stackdriver Kubernetes Monitoring
Beta with structured JSON logging, there is an issue with the parsing of
structured JSON log entries. As a workaround, you can downgrade to GKE 1.11.3.
For more information, see the [ release guide for Stackdriver Kubernetes
Monitoring ](/monitoring/kubernetes-engine/release-guide#beta_release_1102) .

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * All GKE 1.9.x masters will be upgraded to 1.10.9-gke.5. 

##  December 4, 2018

###  Version updates

GKE cluster versions have been updated.  Note: Your clusters might not have
these versions available. Rollouts begin on the day of the note and take four
or more business days to be completed across all Google Cloud zones. For more
information, see the [ Rollout schedule ](/kubernetes-engine/versioning-and-
upgrades#rollout_schedule) .

For information about changes expected in the coming weeks, see  Coming soon
.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades for existing clusters:

  * 1.11.4-gke.8 

####  Node image updates

**CHANGED:**

Ubuntu node image has been upgraded to [ ` ubuntu-
gke-1804-d1703-0-v20181113.manifest ` ](https://storage.googleapis.com/ubuntu-
os-gke-cloud/ubuntu-gke-1804-d1703-0-v20181113.manifest) for clusters running
**Kubernetes 1.11.4-gke.8** .

**Changes:**

  * The following warning is now displayed to SSH clients that connect to Nodes using SSH or to run remote commands on Nodes over an SSH connection: 
    
        WARNING: Any changes on the boot disk of the node must be made via
    DaemonSet in order to preserve them across node (re)creations.
    Node will be (re)created during manual-upgrade, auto-upgrade,
    auto-repair or auto-scaling.

###  New features

**FEATURE:**

  * [ GKE Usage metering (beta) ](/kubernetes-engine/docs/how-to/cluster-usage-metering) is now available. 

###  Changes

**CHANGED:**

  * You can now drain node pools and delete Nodes in parallel. 
  * GKE data in Cloud Asset Inventory and Search is now available in near-real-time. Previously, data was dumped at 6-hour intervals. 

###  Fixed Issues

**FIXED:**

When upgrading to GKE 1.11.x versions prior to GKE 1.11.4-gke.8, a problem
with provisioning the ExternalIP on one or more Nodes causes the ` kubectl `
command to fail. The following error is logged in the ` kube-apiserver ` log:

    
    
    Failed to getAddresses: no preferred addresses found; known addresses

This issue is fixed in GKE 1.11.4-gke.8. If you can't upgrade to that version,
you can work around this issue by following these steps:

  1. Determine which Nodes have no ExternalIP set: 
    
        kubectl get nodes -o wide

Look for entries where the last column is ` <none> ` .

  2. Restart affected nodes. 

###  Known Issues

**ISSUE:**

Users upgrading to GKE 1.11.3 on clusters that use Calico network policies may
experience failures due to a problem recreating the `
BGPConfigurations.crd.projectcalico.org ` resource. This problem does not
affect newly-created clusters. This is expected to be fixed in the coming
weeks.

To work around this problem, you can create the `
BGPConfigurations.crd.projectcalico.org ` resource manually:

  1. Copy the following script into a file named ` bgp.yaml ` : 
    
        apiVersion: apiextensions.k8s.io/v1beta1
    kind: CustomResourceDefinition
    metadata:
      name: bgpconfigurations.crd.projectcalico.org
      labels:
        kubernetes.io/cluster-service: "true"
        addonmanager.kubernetes.io/mode: Reconcile
    spec:
      scope: Cluster
      group: crd.projectcalico.org
      version: v1
      names:
        kind: BGPConfiguration
        plural: bgpconfigurations
        singular: bgpconfiguration
        

  2. Apply the change to the affected cluster using the following command: 
    
        kubectl apply -f bgp.yaml

**ISSUE:**

Users modifying or upgrading existing GKE 1.11.x clusters that use Alias IP
may experience network failures due to a mismatch between the new IP range
assigned the Pods and the alias IP address range for the nodes. This is
expected to be fixed in the coming weeks.

To work around this problem, follow these steps. Use the name of your node in
place of  [NODE_NAME]  , and use your cluster's zone in place of  [ZONE]  .

  1. Cordon node that has been affected: 
    
        kubectl cordon [NODE_NAME]

  2. Drain node of all workloads: 
    
        kubectl drain [NODE_NAME]

  3. Delete the Node object from Kubernetes 
    
        kubectl delete nodes [NODE_NAME]

  4. Reboot the Node. This is not optional. 
    
        gcloud compute instances reset --zone [ZONE] [NODE_NAME]

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  Coming soon

We expect the following changes in the coming weeks. This information is not a
guarantee, but is provided to help you plan for upcoming changes.

  * We expect to begin upgrading cluster masters running GKE 1.9.x to 1.10.9-gke.5. 
  * An updated Container-Optimized OS node image, including [ containerd 1.1.5 ](https://github.com/containerd/containerd/releases/tag/v1.1.5)
  * Support for enabling Node auto-upgrade and auto-repair when creating or modifying node pools for GKE 1.11 clusters running Ubuntu node images 

##  November 26, 2018

###  Version updates

GKE cluster versions have been updated.  Note: Your clusters might not have
these versions available. Rollouts begin on the day of the note and take four
or more business days to be completed across all Google Cloud zones. For more
information, see the [ Rollout schedule ](/kubernetes-engine/versioning-and-
upgrades#rollout_schedule) .

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades for existing clusters:

  * 1.10.6-gke.13 
  * 1.10.7-gke.13 
  * 1.10.9-gke.7 
  * 1.11.2-gke.20 
  * 1.11.3-gke.18 

####  Node image updates

**CHANGED:**

Container-Optimized OS node image has been upgraded to ` cos-
stable-69-10895-91-0 ` for clusters running **Kubernetes 1.10.9** and
**Kubernetes 1.11.3** .

**Changes:**

  * Bug fix for pod hanging when executing a file in NFS path 

See COS image [ release notes ](/container-optimized-os/docs/release-notes)
for more information.

**CHANGED:**

Ubuntu node image has been upgraded to [ ` ubuntu-gke-1804-bionic-20180921 `
](https://storage.googleapis.com/ubuntu-os-gke-cloud/ubuntu-
gke-1804-bionic-20180921.manifest) for clusters running **Kubernetes 1.11.3**
.

**Changes:**

  * Add GPU support on Ubuntu 

###  Known Issues

**ISSUE:**

When upgrading to GKE 1.11.x versions prior to GKE 1.11.4-gke.8, a problem
with provisioning the ExternalIP on one or more Nodes causes some ` kubectl `
command to fail. The following error is logged in the ` kube-apiserver ` log:

    
    
    Failed to getAddresses: no preferred addresses found; known addresses

You can work around this issue by following these steps:

  1. Determine which Nodes have no ExternalIP set: 
    
        kubectl get nodes -o wide

Look for entries where the last column is ` <none> ` .

  2. Restart affected nodes. 

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

###  New Features

**FEATURE:** Vertical Pod Autoscaler (beta) is now available on 1.11.3-gke.11
and higher.

##  November 12, 2018

###  Version updates

GKE cluster versions have been updated.  Note: Your clusters might not have
these versions available. Rollouts begin on the day of the note and take four
or more business days to be completed across all Google Cloud zones. For more
information, see the [ Rollout schedule ](/kubernetes-engine/versioning-and-
upgrades#rollout_schedule) .

####  New default version for new clusters

Kubernetes version 1.9.7-gke.11 is the default version for new clusters,
available according to this week's rollout schedule.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades for existing clusters:

  * 1.9.7-gke.11 
  * 1.10.6-gke.11 
  * 1.10.7-gke.11 
  * 1.10.9-gke.5 
  * 1.11.2-gke.18 

####  Scheduled master auto-upgrades

Cluster masters will be auto-upgraded as described below:

  * All clusters running 1.9.7 will be upgraded to 1.9.7-gke.11 
  * All clusters running 1.10.6 will be upgraded to 1.10.6-gke.11 
  * All clusters running 1.10.7 will be upgraded to 1.10.7-gke.11 
  * All clusters running 1.10.9 will be upgraded to 1.10.9-gke.5 
  * All clusters running 1.11.2 will be upgraded to 1.11.2-gke.18 

####  Versions no longer available

The following versions are no longer available for new clusters or cluster
upgrades:

  * 1.9.7-gke.7 
  * 1.10.6-gke.9 
  * 1.10.7-gke.9 
  * 1.10.9-gke.3 
  * 1.11.2-gke.15 

###  Known Issues

**ISSUE:**

When upgrading to GKE 1.11.x versions prior to GKE 1.11.4-gke.8, a problem
with provisioning the ExternalIP on one or more Nodes causes some ` kubectl `
command to fail. The following error is logged in the ` kube-apiserver ` log:

    
    
    Failed to getAddresses: no preferred addresses found; known addresses

You can work around this issue by following these steps:

  1. Determine which Nodes have no ExternalIP set: 
    
        kubectl get nodes -o wide

Look for entries where the last column is

    
        <none>

.

  2. Restart affected nodes. 

###  Other Updates

**CHANGED:**

Patch 2 for Tigera Technical Advisory TTA-2018-001. See the [ security
bulletin ](https://cloud.google.com/kubernetes-engine/docs/security-
bulletins#november-13-2018) for further details.

**CHANGED:**

Patch for Kubernetes vulnerability [ CVE-2018-1002105
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1002105) . See the [
security bulletin ](/kubernetes-engine/docs/security-
bulletins#december-3-2018) for more details.

##  November 5, 2018

###  Version updates

GKE cluster versions have been updated.  Note: Your clusters might not have
these versions available. Rollouts begin on the day of the note and take four
or more business days to be completed across all Google Cloud zones. For more
information, see the [ Rollout schedule ](/kubernetes-engine/versioning-and-
upgrades#rollout_schedule) .

####  New default version for new clusters

Kubernetes version 1.9.7-gke.7 is the default version for new clusters,
available according to this week's rollout schedule.

####  New versions available for upgrades and new clusters

The following Kubernetes versions are now available for new clusters and for
opt-in master upgrades for existing clusters:

  * 1.9.7-gke.7 
  * 1.10.6-gke.9 
  * 1.10.7-gke.9 
  * 1.10.9-gke.3 
  * 1.11.2-gke.15 

####  Scheduled master auto-upgrades

Cluster masters running will be auto-upgraded as described below:

  * All clusters running 1.9.x will be upgraded to 1.9.7-gke.7 
  * All clusters running 1.10.6 will be upgraded to 1.10.6-gke.9 
  * All clusters running 1.10.7 will be upgraded to 1.10.7-gke.9 
  * All clusters running 1.10.9 will be upgraded to 1.10.9-gke.3 
  * All clusters running 1.11.2 will be upgraded to 1.11.2-gke.15 

####  Versions no longer available

The following versions are no longer available for new clusters or cluster
upgrades:

  * 1.9.7-gke.6 
  * 1.10.6-gke.6 
  * 1.10.7-gke.6 
  * 1.10.9-gke.0 
  * 1.11.2-gke.9 

###  Other Updates

**CHANGED:** Patch 1 for Tigera Technical Advisory TTA-2018-001. See the [
security bulletin ](https://cloud.google.com/kubernetes-engine/docs/security-
bulletins#november-13-2018) for further details. The November 12th release
contains additional fixes that address TTA-2018-001 and we recommend customers
upgrade to that release.

###  Rollout schedule

The rollout schedule is now included in [ Versioning and upgrades
](/kubernetes-engine/versioning-and-upgrades#rollout_schedule) .

##  November 1, 2018

###  New Features

**FEATURE:**

[ Node auto-provisioning ](/kubernetes-engine/docs/how-to/node-auto-
provisioning) is now available in beta.

##  October 30, 2018

###  Version updates

GKE cluster versions have been updated as detailed in the following sections.
See [ supported versions ](/kubernetes-engine/supported-versions) for a full
list of the Kubernetes versions you can run on your GKE masters and nodes.

####  New versions available for upgrades and new clusters

GKE 1.11.2-gke.9 is now generally available.

  * You can now select Container-Optimized OS with ` containerd ` images when creating, modifying, or upgrading a cluster to GKE v1.11. Visit [ Using Container-Optimized OS with containerd ](/kubernetes-engine/docs/concepts/using-containerd) for details. 

  * The CustomResourceDefinition API supports a ` versions ` list field (and deprecates the previous singular ` version ` field) that you can use to support multiple versions of custom resources you have developed, to indicate the stability of a given custom resource. All versions must currently use the same schema, so if you need to add a field, you must add it to all versions. Currently, versions only indicate the stability of your custom resource, and do not allow for any difference in functionality among versions. For more information, visit [ Versions of CustomResourceDefinitions ](https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definition-versioning/) . 

  * Kubernetes 1.11 introduces beta support for increasing the size of an existing PersistentVolume. To increase the size of a PersistentVolume, edit the PersistentVolumeClaim (PVC) object. Kubernetes expands the file system automatically. 

Kubernetes 1.11 also includes alpha support for expanding an online
PersistentVolume (one which is in use by a running deployment). To test this
feature, use an [ alpha cluster ](/kubernetes-engine/docs/how-to/creating-an-
alpha-cluster) .

Shrinking persistent volumes is not supported. For more details, visit [
Resizing a volume containing a file system
](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#resizing-a-
volume-containing-a-file-system) .

  * Subresources allow you to add capabilities to custom resources. You can enable ` /status ` and ` /scale ` REST endpoints for a given custom resource. You can access these endpoints to view or modify the behavior of the custom resource, using ` PUT ` , ` POST ` , or ` PATCH ` requests. Visit [ Subresources ](https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/#subresources) for details. 

Also, 1.10.9-gke.0 is available.

###  Scheduled master auto-upgrades

  * Cluster masters running GKE 1.10.6 will be upgraded to 1.10.6-gke.6. 
  * Cluster masters running GKE 1.10.7 will be upgraded to 1.10.7-gke.6. 

###  Fixed Issues

**FIXED:**

GKE 1.10.7-gke.6 and 1.11.2-gke.9 fix an issue that is present in GKE
1.10.6-gke.2 and higher and 1.11.2-gke.4 and higher, where master component
logs are missing from Stackdriver Logging.

###  Other Updates

Container-Optimized OS node image has been upgraded to `cos-
beta-69-10895-52-0` for clusters running Kubernetes 1.11.2-gke.9,
1.10.9-gke.0, or 1.10.7-gke.6. See [ COS image release notes ](/container-
optimized-os/docs/release-notes) for more information.

###  Rollout schedule

