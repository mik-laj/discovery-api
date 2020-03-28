#  Release Notes

This page documents production updates to Security Command Center. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/scc-release-notes.xml `

##  March 23, 2020

**FEATURE:**

The Notifications API is now in general availability. [ Get started with the
notifications API ](https://cloud.google.com/security-command-center/docs/how-
to-notifications) .

**CHANGED:**

The ` eventType ` field was removed from `
organizations.notificationConfigs.create ` in the v1 API. Learn more about [
creating a ` NotificationConfig ` ](https://cloud.google.com/security-command-
center/docs/how-to-api-manage-notifications#create-config) .

##  February 14, 2020

**CHANGED:**

Security Command Center roles inherit Web Security Scanner roles as follows:

  * The ` securitycenter.adminViewer ` role inherits the permissions of the ` cloudsecurityscanner.viewer ` role. 
  * The ` securitycenter.adminEditor ` role inherits the permissions of the ` cloudsecurityscanner.editor ` role. 

For information about how to view all of the permissions that are associated
with a role, see the Cloud IAM documentation about [ Getting the role metadata
](https://cloud.google.com/iam/docs/creating-custom-
roles#getting_the_role_metadata) .

##  February 13, 2020

**FEATURE:**

The notifications API is now in beta:

  * Send new findings and updated findings notifications to a Pub/Sub topic. 
  * Filter notifications by provider source, finding type, category or any other finding fields, properties or security marks. 

[ Get started with the notifications API ](https://cloud.google.com/security-
command-center/docs/how-to-notifications) .

**CHANGED:**

[ Security Command Center tools ](https://cloud.google.com/security-command-
center/docs/how-to-cloud-scc-tools) will become obsolete in future Security
Command Center releases, when their functionalities are added as built-in
features. Support is offered on best-effort basis only for all Security
Command Center tools.

##  November 11, 2019

**CHANGED:**

Cloud SCC now supports full JSON with arrays and JSON objects as potential
property types. This includes support for sorting on JSON object sub-fields,
and filtering on:

  * Array elements 
  * Full JSON objects with partial string match 
  * JSON object sub-fields 

Learn more about [ Filtering and sorting findings
](https://cloud.google.com/security-command-center/docs/how-to-api-list-
findings#filtering_findings) .

##  October 14, 2019

**FEATURE:**

Security Health Analytics is now in beta and can now be enabled in the Sources
Management page of Cloud SCC.

**FEATURE:**

A new Vulnerabilities tab in Cloud SCC displays a dashboard that summarizes
Security Health Analytics findings. This dashboard includes information about
CIS benchmarks and recommended remediations.

**CHANGED:**

Security Health Analytics no longer requires separate service account setup or
permissions. Instead, it uses the Cloud SCC service account that's created for
you during signup.

##  August 20, 2019

**CHANGED:**

The following Security Health Analytics finding type names have changed:

Old Name  |  New Name  
---|---  
` LOGGING_DISABLED ` |  ` CLUSTER_LOGGING_DISABLED `  
` MONITORING_DISABLED ` |  ` CLUSTER_MONITORING_DISABLED `  
` NO_ROOT_PASSWORD ` |  ` SQL_NO_ROOT_PASSWORD `  
` WEAK_ROOT_PASSWORD ` |  ` SQL_WEAK_ROOT_PASSWORD `  
  
##  May 10, 2019

**ISSUE:**

Using VPC Service Controls currently blocks Cloud SCC asset discovery inside
VPC Service perimeters for the following asset types:

  * Compute Engine 
    * Addresses 
    * Routes 
    * VPN Tunnels 
  * Cloud Storage Buckets 
  * GKE Clusters 

This is expected to be fixed in a future release.

For information about troubleshooting access issues, see [ VPC Service
Controls Troubleshooting ](https://cloud.google.com/vpc-service-
controls/docs/troubleshooting) . To work around the access to these assets,
see [ Granting access from the internet with access levels
](https://cloud.google.com/vpc-service-controls/docs/use-access-levels) .

##  April 10, 2019

**FEATURE:**

Cloud SCC is now in general availability (GA). These release notes include
updated items from beta and new items for GA.

**CHANGED:**

` ListAssetResult ` has changed.

  * [ Beta ](https://cloud.google.com/security-command-center/docs/reference/rest/v1beta1/organizations.assets/list#ListAssetsResult)
  * [ v1 ](https://cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.assets/list#ListAssetsResult)

**CHANGED:**

[ GroupFindingsResponse ](https://cloud.google.com/security-command-
center/docs/reference/rest/v1/organizations.sources.findings/group) now
includes ` totalSize ` .

**FIXED:**

` gcloud ` command-line tool support for Cloud SCC is now available.

**FIXED:**

There are now client libraries available for C#, Go, Java, Node.JS, PHP,
Python, and Ruby.

**FIXED:**

Previously only active state findings were shown in the UI. You can now also
choose to show inactive state findings.

**FEATURE:**

` ListFindings ` and ` GroupFindings ` now supports comparison between two
points in time. For more information, see the [ ` compareDuration ` parameter
](https://cloud.google.com/security-command-
center/docs/reference/rest/v1/organizations.sources.findings/list) .

**FEATURE:**

Assets now include Cloud IAM information for organizations, projects, Compute
Engine, Cloud Storage, and others where applicable. [ Cloud IAM Policy
information ](https://cloud.google.com/security-command-
center/docs/reference/rest/v1/organizations.assets/list#IamPolicy) can be
searched, filtered, and joined with all other Asset information and Security
Marks.

**FEATURE:**

Native integration with [ Security Health Analytics
](https://cloud.google.com/security-command-center/docs/how-to-enable-
security-health-analytics) for native managed vulnerability scanning.

**FEATURE:**

Native integration with [ Event Threat Detection
](https://cloud.google.com/security-command-center/docs/how-to-view-
vulnerabilities-threats#etd) for log-based threat detection.

**FEATURE:**

Native integrations with [ Phishing Protection
](https://cloud.google.com/security-command-center/docs/how-to-view-
vulnerabilities-threats#phishing-protection) .

**FEATURE:**

The Cloud SCC dashboard now enables you to select whether just active state
findings are displayed or both active and inactive.

**FEATURE:**

The Cloud SCC dashboard now enables you to set active or inactive state for
each finding.

**FEATURE:**

The Cloud SCC dashboard now enables you to perform a time-diff query for a
fixed set of time periods.

**FEATURE:**

You can now [ export Cloud SCC data ](https://cloud.google.com/security-
command-center/docs/how-to-export-data) as filtered Asset or Findings data to
the Cloud Storage bucket and project you select.

**FEATURE:**

[ Hello World example app ](https://cloud.google.com/security-command-
center/docs/how-to-cloud-scc-tools) is expanded to include Cloud Functions
functions for: removing bucket ACLs, deleting firewall rules, and creating a
VM snapshot.

**FEATURE:**

New example apps are available for:

  * Integrations with Access Transparency Logs, Audit Logging, and Binary Authorization. 
  * Connecting to Splunk. 

For more information, see [ Installing Cloud SCC tools
](https://cloud.google.com/security-command-center/docs/how-to-cloud-scc-
tools) .

**FEATURE:**

Additional security partner integrations through
[Marketplace](https://console.cloud.google.com/marketplace/details/google-
cloud-platform/cloud-security-command-center.

**ISSUE:**

Sorting on Asset ID column on the asset page doesn't work as expected.

**ISSUE:**

Sorting on the following findings page columns doesn't work as expected:

  * ` eventTime `
  * ` source property `
  * ` security mark `
  * ` id `
  * ` externalUri `

**ISSUE:**

Sorting isn't supported for source properties and security marks on the
findings changed page.

**ISSUE:**

After you've created a new asset, the new asset won't appear in Cloud SCC
until it's re-scanned. To see current asset state before the daily re-scan,
trigger an on-demand re-scan and then wait at least 5 minutes to see the new
asset appear in Cloud SCC.

**ISSUE:**

After you've made a Cloud IAM policy change on an asset, the updated policy
won't appear in Cloud SCC until it's re-scanned. To see current Cloud IAM
policy before the daily re-scan, trigger an on-demand re-scan and then wait at
least 10 minutes to see the updated Cloud IAM policies in Cloud SCC.

**ISSUE:**

Code examples are still in progress for C#, Node.js, PHP, and Ruby.

Send feedback

