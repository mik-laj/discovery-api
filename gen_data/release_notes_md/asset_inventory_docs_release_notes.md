#  Release Notes

This page documents production updates to Cloud Asset Inventory. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.

**Current version: release**

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/asset-release-notes.xml `

##  August 03, 2020

**DEPRECATED:**

k8s.io/Node fields deprecation

The following two fields for assets of ` k8s.io/Node ` are now deprecated in
the exported output of Cloud Storage and BigQuery.

  * ` metadata.resourceVersion `
  * ` status.conditions.lastHeartbeatTime `

##  April 03, 2020

**FEATURE:**

BigQuery export for org policies and access policies

You can now export org policies and access policies to BigQuery tables. See [
Exporting assets to BigQuery ](https://cloud.google.com/asset-
inventory/docs/exporting-to-bigquery) for more information.

**FEATURE:**

Real-time asset monitoring for org policies and access policies

You can now subscribe to real-time notifications for changes to org policies
and access policies. See [ Monitoring asset changes
](https://cloud.google.com/asset-inventory/docs/monitoring-asset-changes) for
more information.

##  February 27, 2020

**FEATURE:**

Resource and policy search beta release

You can now [ search resource metadata ](https://cloud.google.com/asset-
inventory/docs/searching-resources) and [ Cloud IAM policies
](https://cloud.google.com/asset-inventory/docs/searching-iam-policies) in
your project, folder or organization.

##  January 16, 2020

**FEATURE:**

Real-time notifications GA

The ability to receive real-time notifications for asset changes is now
generally available. You can [ monitor asset changes
](https://cloud.google.com/asset-inventory/docs/monitoring-asset-changes) on a
project by creating an activity feed, and then subscribe to the feed to
receive real-time notifications about the changes.

##  November 15, 2019

**FEATURE:**

Export to BigQuery GA

The ability to export asset metadata to BigQuery is now generally available.
See the [ Exporting to BigQuery ](https://cloud.google.com/asset-
inventory/docs/exporting-to-bigquery) topic to learn more.

##  October 10, 2019

**FEATURE:**

Real-time notifications for asset configuration changes Beta release

Beta release of the [ real-time notification ](https://cloud.google.com/asset-
inventory/docs/monitoring-asset-changes) feature for continuous asset
monitoring.

##  March 05, 2019

**FEATURE:**

Cloud Asset Inventory General Availability

Launched the new [ V1 ](https://cloud.google.com/asset-
inventory/docs/reference/rest/#rest-resource-v1) version of the Cloud Asset
API.

##  October 03, 2018

**FEATURE:**

Cloud Asset Inventory Beta release

[ Cloud Asset Inventory ](https://cloud.google.com/asset-
inventory/docs/overview) is a storage service that keeps a five week history
of Google Cloud Platform (GCP) asset metadata. It allows you to export all
asset metadata at a certain timestamp or timeframe.

