#  Cloud Run for Anthos Release Notes

This page documents production updates to Cloud Run for Anthos. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/runanthos-release-notes.xml `

##  July 13, 2020

**CHANGED:**

Cloud Run for Anthos on Google Cloud version [ 0.15.0-gke.3
](https://github.com/knative/serving/releases/tag/v0.15.0) is now available
for the following versions (and greater)

  * 1.17.7-gke.15 

And it now supports [ Managed TLS GA
](https://cloud.google.com/run/docs/gke/managed-tls) .

##  July 07, 2020

**CHANGED:**

Cloud Run for Anthos on Google Cloud version 0.14.0-gke.10 is now available
for following cluster versions (and greater):

  * 1.15.12-gke.6 
  * 1.16.10-gke.8 
  * 1.17.6-gke.11 

Fixes CVE-2020-11080 affecting [ HTTP2 library used by Envoy in Istio
](https://istio.io/latest/news/security/istio-security-2020-006/) .

##  June 19, 2020

**FEATURE:**

Cloud Run for Anthos on Google Cloud version [ 0.14.0-gke.5
](https://github.com/knative/serving/releases/tag/v0.14.0) is now available
for the 1.17.6-gke.4+ cluster version.

##  April 27, 2020

**FEATURE:**

Cloud Run for Anthos on Google Cloud version [ 0.13.2-gke.3
](https://github.com/knative/serving/releases/tag/v0.13.2) is now available
for following cluster versions (and greater):

  * 1.15.11-gke.9 
  * 1.16.5-gke.2 
  * 1.16.6-gke.11 
  * 1.16.8-gke.7 

##  April 22, 2020

**FEATURE:**

Cloud Run for Anthos now support [ Private Clusters
](https://cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-
concept) for following cluster versions (and greater):

  * 1.15.11-gke.9 
  * 1.16.5-gke.2 
  * 1.16.6-gke.11 
  * 1.16.8-gke.7 

##  March 13, 2020

**FEATURE:**

Cloud Run for Anthos on Google Cloud version [ 0.11.0-gke.9
](https://github.com/knative/serving/releases/tag/v0.11.1) is now available
for following cluster versions (and greater):

  * 1.14.10-gke.27 
  * 1.15.9-gke.17 
  * 1.15.11-gke.1 
  * 1.16.6-gke.11 
  * 1.16.8-gke.3 

##  February 05, 2020

**FEATURE:**

[ Automatic TLS certificates ](https://cloud.google.com/run/docs/gke/auto-tls)
can now be enabled for the following cluster versions (and greater):

  * 1.15.7-gke.23 
  * 1.14.10-gke.17 
  * 1.14.9-gke.23 
  * 1.14.8-gke.33 

##  November 14, 2019

**CHANGED:**

Cloud Run for Anthos on GCP is now Generally Available (GA).

##  October 21, 2019

**FEATURE:**

Cloud Run is now covered by [ HIPAA Compliance
](https://cloud.google.com/security/compliance/hipaa/) .

##  October 10, 2019

**FEATURE:**

Cloud Run for Anthos on Google Cloud version 0.8.1-gke.0 is now available on
GKE master versions 1.14.6-gke.13, 1.13.10-gke.7.

##  October 01, 2019

**FEATURE:**

The [ max instances setting
](https://cloud.google.com/run/docs/configuring/max-instances) feature allows
you to set a limit to the total number of container instances that are started
up to handle traffic.

##  September 23, 2019

**FEATURE:**

Cloud Run for Anthos on Google Cloud version 0.8.0-gke.0 is now available on
GKE master versions 1.13.10-gke.0.

##  September 19, 2019

**FEATURE:**

Cloud Run for Anthos deployed on VMware Beta release.

##  September 10, 2019

**FEATURE:**

You can set [ labels ](https://cloud.google.com/run/docs/configuring/labels)
on Cloud Run services and revisions.

##  June 18, 2019

**CHANGED:**

New ` --platform ` flag added to [ Cloud Run ` gcloud ` command line
](https://cloud.google.com/sdk/gcloud/reference/beta/run/) . This argument is
optional but will be required in a future release of the tool.

##  June 05, 2019

**FEATURE:**

Cloud Run for Anthos on Google Cloud version ` 0.6.0-gke.1 ` is now available
on GKE master versions ` 1.13.6-gke.6 ` and ` 1.12.8-gke.7 ` .

**ISSUE:**

When upgrading to this version, previously deployed services will return an
error ` no healthy upstream ` until a new revision is deployed.

**FEATURE:**

Improved reliability when scaling from zero.

##  May 16, 2019

**FEATURE:**

Cloud Run for Anthos on Google Cloud version ` 0.5.2-gke.1 ` is now available
on GKE master versions ` 1.13.5-gke.10 ` , ` 1.12.7-gke.17 ` and `
1.11.9-gke.13 ` .

**CHANGED:**

Cloud Run for Anthos on Google Cloud no longer injects Istio sidecars by
default in the versions ` 1.12.7-gke.17 ` and ` 1.11.9-gke.13 ` .

**CHANGED:**

Cloud Run for Anthos on Google Cloud no longer blocks network egress from the
cluster by default in the versions ` 1.12.7-gke.17 ` and ` 1.11.9-gke.13 ` .

##  April 22, 2019

**FEATURE:**

Cloud Run for Anthos on Google Cloud version ` 0.5.0-gke.1 ` is now available
on GKE master versions ` 1.12.7-gke.7 ` and ` 1.11.9-gke.5 ` .

**CHANGED:**

Knative serving has been updated to ` 0.5.0 ` . See the [ Knative serving `
0.5.0 ` release notes
](https://github.com/knative/serving/releases/tag/v0.5.0) for more
information.

##  April 09, 2019

**FEATURE:**

Cloud Run for Anthos on Google Cloud Beta release.

##  March 24, 2019

**FEATURE:**

Cloud Run for Anthos on Google Cloud version ` 0.4.0-gke.2 ` is now available
on GKE master versions ` 1.12.6-gke.0 ` , ` 1.11.8-gke.4 ` , and `
1.11.7-gke.15 ` .

**FEATURE:**

Knative serving has been updated to ` 0.4.0 ` . See the [ Knative serving `
0.4.0 ` release notes
](https://github.com/knative/serving/releases/tag/v0.4.0) for more
information.

**ISSUE:**

Request logs are not displayed in the logs panel in this release.

**ISSUE:**

Cloud Run for Anthos on Google Cloud is incompatible with GKE versions `
1.10.12-gke.7 ` , ` 1.11.6-gke.11 ` , ` 1.12.5-gke.5 ` . If you are using one
of these GKE versions with the add-on enabled, you must upgrade to a newer
version of GKE.

