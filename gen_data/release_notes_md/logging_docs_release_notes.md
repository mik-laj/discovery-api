#  Release notes

This page documents production updates to Logging. You can periodically check
this page for announcements about new or updated features, bug fixes, known
issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/stackdriver-release-notes.xml `

##  August 17, 2020

**FEATURE:**

To help you explore your logs more efficiently, Cloud Logging now provides
suggested queries based on the context of your Google Cloud project. For more
information, go to [ Suggested queries
](https://cloud.google.com/logging/docs/view/building-
queries#suggested_queries) .

##  August 11, 2020

**CHANGED:**

Users now manage logs exclusions through logs sinks. As a result, custom roles
that have the ` logging.sinks.* ` permissions can now control the volume of
logs ingested into Cloud Logging through logs sinks.

We recommend that you review any custom roles with the ` logging.sinks.* `
permissions so that you can make adjustments as needed.

**FEATURE:**

Beta release: You can now use Logs Buckets to centralize or divide your logs
based on your needs. For information about this feature, refer to the [
Managing logs buckets ](https://cloud.google.com/logging/docs/buckets) guide.

##  August 03, 2020

**FEATURE:**

Alpha release: You can now use Logs Buckets to centralize or divide your logs
based on your needs. For information about this feature, refer to the [
Managing logs buckets ](https://cloud.google.com/logging/docs/buckets) guide.
To participate in the alpha or to get notified when Logs Buckets goes beta,
fill out the [ sign up form
](https://docs.google.com/forms/d/e/1FAIpQLSeBVpNBivnTAAd4G3rdait9t94uG9TWc07oGwNRGcE071TeCA/viewform)
.

##  July 30, 2020

**CHANGED:**

The Logs field explorer panel is now generally available (GA). To learn more,
see the [ Logs field explorer section on Logs Viewer (Preview) interface page
](https://cloud.google.com/logging/docs/view/logs-viewer-interface#logs-field-
panel) .

##  June 30, 2020

**FEATURE:**

Cloud Logging now contains a Logs Dashboard page that provides a high-level
overview into the health of your systems running within a project. To learn
more, see [ Logs Dashboard
](https://cloud.google.com/logging/docs/view/dashboard) .

##  June 05, 2020

**CHANGED:**

Custom retention is now generally available (GA). In order to have time to
explore this feature, you won't be charged for extended retention of logs
until March 31, 2021. To learn more, see the [ Logging pricing section on the
Pricing for Google Cloud's operations suite page
](https://cloud.google.com/stackdriver/pricing#logging-costs) .

##  June 03, 2020

**FEATURE:**

In the Logs Viewer (Preview), you can now save your queries, which can then be
viewed and run from the **Saved** queries tab. For more information, see the [
Saved queries section on the Building queries page
](https://cloud.google.com/logging/docs/view/building-queries#saved-queries) .

##  May 18, 2020

**FEATURE:**

**Logs Viewer** now contains the **Logs field explorer** panel, which lets you
view aggregation-based results for your project's log fields and makes it more
efficient to refine queries. To learn more, go to the [ Logs Viewer (Preview)
page ](https://cloud.google.com/logging/docs/view/logs-viewer-interface) .

##  May 11, 2020

**FEATURE:**

You can now use regular expressions to query your logs data and create
filters. For more information, go to [ Using regular expressions
](https://cloud.google.com/logging/docs/view/logging-query-language#regular-
expressions) .

##  April 27, 2020

**CHANGED:**

The Logs Viewer (Preview) is now GA. To learn more, go to the [ Logs Viewer
(Preview) Overview page ](https://cloud.google.com/logging/docs/view/logs-
viewer-preview) .

##  March 17, 2020

**CHANGED:**

Incoming log entries must have timestamps that don't exceed the [ logs
retention periods
](https://cloud.google.com/logging/quotas#logs_retention_periods) in the past,
and that don't exceed 24 hours in the future. Log entries outside those time
boundaries aren't ingested by Cloud Logging.

##  March 12, 2020

**CHANGED:**

Cloud Logging Agent for Windows version 1-11 is now available. This version
upgrades ` fluentd ` from 1.4.2 to 1.7.4. Go to [ Installing the Cloud Logging
agent ](https://cloud.google.com/logging/docs/agent/installation) for
information on installing this version of the agent.

##  March 10, 2020

**FEATURE:**

Logs Viewer (Preview) now contains a histogram panel. The histogram panel lets
you visualize your logs data to more easily spot patterns and troubleshoot
issues. For more information, see [ Using Logs Viewer (Preview)
](https://cloud.google.com/logging/docs/view/logs-viewer-interface) .

##  February 24, 2020

**FEATURE:**

Beta release: You can now use the new Logs Viewer (Preview) to view, parse and
analyze log data, and refine your query parameters. Go to [ Logs Viewer
interface (Preview) ](https://cloud.google.com/logging/docs/view/logs-viewer-
interface) for more information.

##  February 17, 2020

**CHANGED:**

BETA: You can now configure the retention periods of your logs data. For more
information, go to [ Storing logs
](https://cloud.google.com/logging/docs/storage) .

##  January 17, 2020

**FEATURE:**

Customer-managed encryption keys (CMEK) for the Logs Router are now Generally
Available (GA). CMEK lets you create, control, and manage encryption keys to
meet your data compliance needs. For details, go to [ Enabling customer-
managed encryption keys for Logs Router
](https://cloud.google.com/logging/docs/routing/managed-encryption) .

##  December 16, 2019

**FEATURE:**

GA release: You can now use partitioned tables for logs exports to BigQuery.
For details, go to [ Partitioned tables
](https://cloud.google.com/logging/docs/export/bigquery#partition-tables) .

##  December 13, 2019

**CHANGED:**

Google Kubernetes Engine (GKE) version 1.15, which is now generally available,
drops support for GKE versions 1.12 and earlier. As a result, the beta version
of Stackdriver Kubernetes Engine Monitoring is no longer supported. If your
GKE clusters are running version 1.12 or earlier, then you must upgrade them
as soon as possible.

##  December 11, 2019

**DEPRECATED:**

Legacy Stackdriver support for Google Kubernetes Engine (GKE) is deprecated.
If you're using Legacy Stackdriver, then you must [ migrate to Stackdriver
Kubernetes Engine Monitoring ](https://cloud.google.com/monitoring/kubernetes-
engine/migration) before Legacy Stackdriver is decommissioned. For more
information, see [ Legacy Stackdriver support for GKE deprecation
](https://cloud.google.com/stackdriver/docs/deprecations/legacy) .

##  November 18, 2019

**FEATURE:**

Customer-managed encryption keys (CMEK) for the Logs Router are now available
in Beta. CMEK lets you create, control, and manage encryption keys to meet
your data compliance needs. For details, go to [ Enabling customer-managed
encryption keys for Logs Router
](https://cloud.google.com/logging/docs/routing/managed-encryption) .

##  September 20, 2019

**FEATURE:**

Beta release: Stackdriver Logging now offers partitioned tables for exports to
BigQuery. For details, go to [ Partitioned tables
](https://cloud.google.com/logging/docs/export/bigquery#partition-tables) .

##  September 10, 2019

**FEATURE:**

Stackdriver Logging now lets you save your advanced log queries to a Saved
Searches library, where they can be managed and shared. Go to [ Saved searches
](http://cloud.google.com/logging/docs/view/overview#saved-searches) for
details.

**CHANGED:**

When creating a new Google Kubernetes Engine (GKE) cluster, Stackdriver
Kubernetes Engine Monitoring is now the default Stackdriver support option.
This is a change from prior versions where Stackdriver Logging and Stackdriver
Monitoring were the default Stackdriver support option. For more information,
see [ Overview of Stackdriver support for GKE
](https://cloud.google.com/monitoring/kubernetes-engine/) .

##  May 21, 2019

**FEATURE:**

[ Stackdriver Kubernetes Engine Monitoring
](https://cloud.google.com/monitoring/kubernetes-engine/) is now generally
available. Users of the legacy Stackdriver support for [ monitoring
](https://cloud.google.com/monitoring/kubernetes-engine/legacy-
stackdriver/monitoring) and [ logging
](https://cloud.google.com/monitoring/kubernetes-engine/legacy-
stackdriver/logging) for Google Kubernetes Engine are encouraged to [ migrate
to Stackdriver Kubernetes Engine Monitoring
](https://cloud.google.com/monitoring/kubernetes-engine/migration) as soon as
possible.

##  April 23, 2019

**CHANGED:**

The maximum size of a log entry has been increased to 256 KB from 100 KB. For
details on logging usage limits, go to [ Quotas and limits
](https://cloud.google.com/logging/quotas) .

##  April 15, 2019

**FEATURE:**

A new Windows version (v1-9) of the Stackdriver Logging agent is now
available. The new version saves the agent service logs on disk for easier
troubleshooting and supports the ` config.d ` configuration extension
directory.

##  March 15, 2019

**CHANGED:**

Stackdriver agents are subject to an updated [ deprecation policy
](https://cloud.google.com/stackdriver/docs/agent-deprecation-policy) . As
part of this transition, the next major version of the Stackdriver Monitoring
and Stackdriver Logging agents will stop supporting operating systems that are
at the end of their lifecycle, as well as some [ third-party agent plugins
](https://cloud.google.com//monitoring/agent/plugins/) .

##  February 22, 2019

**CHANGED:**

You now have two choices for the access control model when creating a Cloud
Storage bucket: bucket-only (new) and object-level. Select **Set object-level
and bucket-level permissions** as the access control model during bucket
creation if you intend to use the bucket as a sink destination. See [ Errors
exporting to Cloud Storage
](https://cloud.google.com/logging/docs/export/configure_export_v2#errors_exporting_to_cloud_storage)
for details.

##  January 22, 2019

**CHANGED:**

In the Stackdriver Logging API, log sinks, metrics, and exclusions have two
new output-only fields: create time and last update time. See [ LogSink
](https://cloud.google.com/logging/docs/reference/v2/rest/v2/sinks) for an
example. If this information isn't available for older resources, these fields
aren't present.

##  December 03, 2018

**FEATURE:**

The Logs Viewer has a new option to display a log entry in its resource
context. It can also pin a log entry while allowing you to change the display
context. See [ Viewing Logs
](https://cloud.google.com/logging/docs/view/overview) for details.

##  November 01, 2018

**FEATURE:**

You can now view error and success metrics for your log sinks using [ export
system metrics ](https://cloud.google.com/logging/docs/logs-based-
metrics#system_logs-based_metrics) .

##  October 19, 2018

**FEATURE:**

You can now link from certain App Engine request logs to a detailed trace that
explains the request's latency. You can also filter log entries according to
their latencies, and if they contain detailed trace data viewable by
Stackdriver Trace. See [ Viewing latency in Trace
](http://cloud.google.com/logging/docs/view/overview#show-latency) for
details.

##  October 01, 2018

**FEATURE:**

The Logs Viewer can now download up to 300 log entries in JSON or CSV format.
See [ Viewing Logs ](https://cloud.google.com/logging/docs/view/overview) for
details.

##  September 14, 2018

**FEATURE:**

The format of service account names for older log [ sinks
](https://cloud.google.com/logging/docs/export/#sink-terms) is being changed
so that all log sinks will have consistent service account names. This naming
format has already been applied to project-level sinks on BigQuery, Cloud
Pub/Sub, and Cloud Storage permission pages. In the coming weeks, this naming
format will be applied to organization-level sinks and folder-level sinks, and
to sinks listed on the **Logs Exports** page in the Logs Viewer. There are no
associated changes to functionality or granted permissions.

##  September 05, 2018

**FEATURE:**

**Access Transparency** logging is now Generally Available. See [ Overview of
Access Transparency ](https://cloud.google.com/logging/docs/audit/access-
transparency-overview) for details.

##  July 25, 2018

**CHANGED:**

Audit logs exports to BigQuery now feature a compact format. On March 1, 2019,
the older extended format will be removed.

##  June 29, 2018

**CHANGED:**

On July 1, 2018 at 00:00 PDT, Stackdriver switches to consumption-based
pricing. For more information, see [ Stackdriver Pricing
](https://cloud.google.com/stackdriver/pricing_v2) .

##  June 26, 2018

**FEATURE:**

You can now immediately disable all logs ingestion. For instructions, see [
Stopping all logs ingestion
](https://cloud.google.com/logging/docs/exclusions#stop-logs) .

##  June 19, 2018

**FEATURE:**

Google Cloud Storage logs streaming time has been reduced from 12 hours to 3
hours. For details, see [ Using Exported Logs
](https://cloud.google.com/logging/docs/export/using_exported_logs#gcs-
availability) .

##  June 18, 2018

**CHANGED:**

**Between June 18, 2018 at 06:00 PDT and July 1, 2018 at 00:00 PDT, your use
of Stackdriver is free** . The service tiers have been removed, and you can
experience all features without incurring costs. Thereafter, Stackdriver
switches to consumption-based pricing. For more information, see [ Upcoming
Pricing ](https://cloud.google.com/stackdriver/pricing_v2) .

##  June 12, 2018

**FEATURE:**

You can now enable and configure your Data Access audit logs using the GCP
console. For details, see [ Configuring Data Access logs
](https://cloud.google.com/logging/docs/audit/configure-data-access) .

##  May 17, 2018

**FEATURE:**

You can now see your Logging usage and estimate your bill according to the new
Stackdriver pricing and in advance of billing enforcement. See [ Estimating
your bills ](https://cloud.google.com/stackdriver/estimating-bills) for
details.

##  May 08, 2018

**FEATURE:**

You can now specify custom fields in your Logs Viewer log-entry summary lines.
See [ Add custom fields
](https://cloud.google.com/logging/docs/view/overview#custom-fields) for
details.

##  May 02, 2018

**FEATURE:**

[ Stackdriver Kubernetes Monitoring
](https://cloud.google.com/monitoring/kubernetes-engine) is released in Beta
for Kubernetes 1.10 clusters running in [ Kubernetes Engine
](https://cloud.google.com/kubernetes-engine/docs/) . The previous Stackdriver
support is still available for those who do not opt into this Beta release.
This release affects Logging by introducing new [ monitored resource types
](https://cloud.google.com/logging/docs/api/v2/resource-list#tag_k8s_cluster)
and new [ Kubernetes metrics
](https://cloud.google.com/monitoring/api/metrics_kubernetes) .

##  April 10, 2018

**FEATURE:**

You can now specify that the Stackdriver Logging agent converts your payloads
to JSON format for certain log inputs. For details on enabling this feature,
see [ Structured Logging ](https://cloud.google.com/logging/docs/structured-
logging) .

##  March 12, 2018

**CHANGED:**

Beginning on June 30, 2018, Stackdriver is switching to consumption-based
pricing, including revised quotas. For more information, see [ Stackdriver
Upcoming Pricing ](https://cloud.google.com/stackdriver/pricing_v2) .

**FEATURE:**

Logging data retention has been increased to 30 days for all projects.

##  February 01, 2018

**FEATURE:**

The Logging agent now supports partial success for logs ingestion. Any invalid
log entries in a full set will be dropped, and the valid log entries now will
be successfully ingested into the Stackdriver Logging API; previously, the
full set would have been dropped if it contained any invalid log entries. To
enable partial success, upgrade your Logging agent to [ google-fluentd v1.5.27
](https://github.com/GoogleCloudPlatform/google-fluentd/releases/tag/v1.5.27)
.

##  December 13, 2017

**FEATURE:**

Filtering logs by **time range** is now available in the Logs Viewer. For more
information, see [ Scroll to a time
](https://cloud.google.com/logging/docs/view/overview#scroll-to-time) .

##  December 04, 2017

**CHANGED:**

**Logging agent recommendation** : VM instances should have at least 1 GB of
memory to run the Logging agent.

**FEATURE:**

**Google Cloud Platform HTTP(S) load balancing logging** now includes logs for
**rejected requests** , such as those due to invalid or expired URL
signatures, and aligns **httpRequest.requestSize** with metrics from the [
Stackdriver Monitoring API
](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-loadbalancing) . For
more information, see [ HTTP(S) Load Balancing Logging
](https://cloud.google.com/compute/docs/load-balancing/http/#logging) .

##  November 29, 2017

**FEATURE:**

**Logs-based metrics** are now Generally Available. For more information, see
[ Overview of Logs-based Metrics ](https://cloud.google.com/logging/docs/logs-
based-metrics) .

**CHANGED:**

**Logging agent installation instructions** : The checksum validation step for
the installation script has been removed. You can see the new instructions on
the [ logging agent installation
](https://cloud.google.com/logging/docs/agent/installation) page.

**FIXED:**

**Logs Viewer** update: Fixes a problem related to the daylight saving time
transition in the U.K. If you see your logs displaying in the wrong time zone,
you can set your default time zone by using the **Jump to date** drop-down
menu to select a different time zone. For more information, see [ Logs Viewer
user interfaces
](https://cloud.google.com/logging/docs/view/overview#the_user_interfaces) .

##  November 01, 2017

**CHANGED:**

**Pricing changes** : Billing for logs overages will begin **March 31, 2018**
. This date extends the one that was previously communicated to give
Stackdriver customers more time to apply the [ exclusion filters
](https://cloud.google.com/logging/docs/exclusions) feature to control which
logs are stored in Logging. Billing for custom and user-defined logs-based
metrics is still postponed. For more information, see [ Stackdriver Pricing
](https://cloud.google.com/stackdriver/pricing) .

##  October 30, 2017

**FEATURE:**

**Exclusion filters** are now Generally Available. For more information, see [
Excluding Logs ](https://cloud.google.com/logging/docs/exclusions) , and the
**Resource Usage** page in the Logs Viewer.

##  October 24, 2017

**CHANGED:**

The **` gcloud logging ` command group ** is now generally available. ` gcloud
beta logging ` will be removed at the end of December 2017. For more
information, see [ gcloud logging
](https://cloud.google.com/sdk/gcloud/reference/logging/) .

##  September 12, 2017

**FEATURE:**

**Admin Activity audit logs** retention has been extended to 400 days for both
the Stackdriver Basic and Premium service tiers. For more information, see [
Audit log retention
](https://cloud.google.com/logging/docs/audit/#audit_log_retention) .

**FEATURE:**

**Logging agent update** to 1.5.18-1. Allows enabling JSON detection via
configuration, fixes a problem with string-valued timestamps, and allows
setting the following [ ` LogEntry `
](https://cloud.google.com//logging/docs/api/reference/rest/v2/LogEntry)
fields: ` trace ` , ` sourceLocation ` , and ` operation ` .

##  August 31, 2017

**FEATURE:**

**Logs-based metrics** now support extracting values from log entries to
create distribution metrics and to populate user-defined metric labels. This
lets you create multiple time series in a single logs-based metric. Also, the
latency of logs-based metrics has dropped from approximately 5 minutes to 1
minute, so you can respond more quickly to the metrics. For more information,
see [ Overview of Logs-based metrics
](https://cloud.google.com/logging/docs/logs-based-metrics/) .

**FEATURE:**

**Exclusion filters** let you control which logs are kept in Stackdriver
Logging. The **Resource Usage** page in the Logs Viewer breaks down log volume
by resource type. For more information, see [ Excluding Logs
](https://cloud.google.com/logging/docs/exclusions) .

**CHANGED:**

**Logging agent** : The Stackdriver Logging agent package has been updated to
version 1.5.17. The agent will now send smaller requests, improving log
delivery latency and increasing queries per second, which may affect users
with high log volumes. Also, the package's bundled Ruby has been updated to
version 2.2.7. If you have configuration snippets or extra gems that depend on
older Ruby features, you may have to update them.

**CHANGED:**

**Pricing changes** : The free per-project allotment of logs is being
increased from 5 GB to 50 GB. Beginning December 1, 2017, we will enforce the
new limits and begin charging for logs kept in Stackdriver Logging above the
limits. For more information, see [ Stackdriver Pricing
](https://cloud.google.com/stackdriver/pricing) .

##  August 23, 2017

**FEATURE:**

**Aggregated Exports** : Organizations and folders can now export selected log
entries from all of their projects with a single sink created in the
organization or folder. For more information, see [ Aggregated Exports
](https://cloud.google.com/logging/docs/export/aggregated_exports) .

**CHANGED:**

**Timestamp handling** . The following changes to log entry timestamps have
been made or are planned. 1\. Logging does not modify the user-provided `
timestamp ` field, except to set it to the current time if it is omitted. A
second field, ` receivedTimestamp ` , is set to the time Logging receives the
entry. 2\. The ` timestamp ` field is used to compute the age of log entries
and to enforce the [ log retention period
](https://cloud.google.com/logging/quotas) . Prior to the change, the `
receivedTimestamp ` field is used for that purpose. 3\. Logging discards log
entries whose timestamps are more than 24 hours in the future or are further
in the past than the log entry's retention period. Prior to the change, future
timestamps and very old timestamps are handled in an unpredictable fashion.
For more information, see [ ` LogEntry `
](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) and [ `
entries.write `
](https://cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write) .

##  July 10, 2017

**FEATURE:**

**IAM support** for Logging now includes custom roles. For more information,
see Logging [ Access Control ](https://cloud.google.com/logging/docs/access-
control) .

**CHANGED:**

**API Migration** . Information about the deprecated v1 API is being removed
from general documentation. Note: Obsolete link to migration information
removed on December 13, 2017. For updated information, see [ APIs & Reference
](https://cloud.google.com/logging/docs/apis) .

##  June 05, 2017

**ISSUE:**

**Exported audit logs in BigQuery** : The BigQuery schema for exported audit
log entries changed on June 5, 2017. The following audit log components now
have shortened field names when they are exported to BigQuery: ` protoPayload
` , ` protoPayload.serviceData ` , ` protoPayload.request ` , and `
protoPayload.response ` . This is a breaking change for queries involving
these fields. For more information see [ Audit log field changes
](https://cloud.google.com/logging/docs/export/using_exported_logs#bigquery-
overview) .

**FEATURE:**

**Apps Script** : You can access your Apps Script logs in Logging.

**FEATURE:**

**Logs Viewer** : You can more easily expand all fields in a log entry.

##  May 01, 2017

**FEATURE:**

Data access logs are now available and are user-configurable. See [
Configuring Data Access Logs
](https://cloud.google.com/logging/docs/audit/configure-data-access) .

**FEATURE:**

**Aggregated exports of logs** : You can now create log sinks in
organizations, billing accounts, and folders. Those sinks can export log
entries from all included projects. See [ Aggregated Exports
](https://cloud.google.com/logging/docs/export/aggregated_exports) .

**DEPRECATED:**

**v1 API turndown: writeLogEntries** : As a final step in the v1 API turndown,
the v1 ` WriteLogEntries ` method will be shut down on October 1, 2017. You
must migrate any applications that write log entries using the v1 API. You
must also upgrade any manually-installed Logging agents in your VM instances.
Note: Obsolete link to migration information removed on December 13, 2017. For
updated information, see [ APIs & Reference
](https://cloud.google.com/logging/docs/apis) .

**DEPRECATED:**

**v1 API turndown: sinks and logs-based metrics** : Migrate your remaining v1
export sinks and v1 logs-based metrics. If you do not, Logging will migrate
them by mid-July, 2017. Note: Obsolete link to migration information removed
on December 13, 2017. For updated information, see [ APIs & Reference
](https://cloud.google.com/logging/docs/apis) .

##  April 01, 2017

**FEATURE:**

**Resource types** : Several new resource types are added, including types for
Cloud Bigtable, Cloud Dataflow, and Cloud Container Engine.

##  March 31, 2017

**CHANGED:**

**V1 API turndown** : The date of the v1 API turndown has changed. See the
release note for May 2017.

**CHANGED:**

**Logging agent for Windows** : If you install the Logging agent on VM
instances running Microsoft Windows, be aware that there are restrictions on
the folders used for the installer and the installed agent. For details, [
Installing on Linux and Windows
](https://cloud.google.com/logging/docs/agent/installation#joint-install) .

##  February 06, 2017

**FEATURE:**

**Exporting logs from organizations, folders, and billing accounts** : The [ `
gcloud logging `
](https://cloud.google.com/logging/docs/reference/tools/gcloud-logging)
command-line tool now supports creating log sinks to export audit logs from
organizations, folders, and billing accounts. This feature also supported in
the API.

**FEATURE:**

**Viewing multiple logs** : Previously in the Logs Viewer, you could view a
single log or "all logs" from a single resource type. Now you can select any
number of logs within a resource type to view, using the log name dropdown
menu.

For example, when viewing App Engine applications, the default is now to
display log entries from any of these logs: ` ngnix.request ` , ` stdout ` , `
request log ` , and ` stderr ` .

**FEATURE:**

**Resuming log streaming** : The Logs Viewer now automatically resumes
streaming logs when its browser window or tab is selected. You no longer have
to restart streaming when returning to the page.

**FEATURE:**

**App Engine Flexible Environment** : For App Engine Flexible Environment, the
Logs Viewer can now display application log entries ("log lines") inside the
log entry for the associated service request. This is similar to the
functionality in the App Engine Standard Environment.

**CHANGED:**

**Deleting logs-based metrics in alerting policies** : Attempting to delete a
[ logs-based metric
](https://cloud.google.com/logging/docs/view/logs_based_metrics) that is used
in one or more Stackdriver Monitoring alerting policies now fails with the
status ` FAILED_PRECONDITION ` . You must remove the metric from the alerting
policies or delete the alerting policies prior to deleting the logs-based
metric.

**CHANGED:**

**Remove daily API quotas** : The Logging API no longer includes daily API
quotas. The API still enforces short-term (per 100s) quotas on API calls, as
displayed in the Stackdriver Logging API dashboard.

**ISSUE:**

**Logs retention and source restriction** : With the implementation of the
Basic and Premium service tiers in December 2016, Stackdriver Logging began
enforcing retention and log source restrictions for projects that are in the
Stackdriver Basic tier or are not associated with a Stackdriver account. In
the Basic tier, log entries are visible for 7 days after they are received,
and logs from non-GCP sources, including Amazon Web Services, are rejected.

##  December 12, 2016

**CHANGED:**

**Logs Viewer v2** : The Logs Viewer has been migrated to the Stackdriver
Logging API v2. For the full documentation, [ Viewing Logs (v2)
](https://cloud.google.com/logging/docs/view/overview) . Note: Obsolete link
to migration information removed on December 13, 2017. For updated
information, see [ APIs & Reference
](https://cloud.google.com/logging/docs/apis) .

**FEATURE:**

**List logs** : the Stackdriver Logging API now has "list logs" methods: [ `
organizations.logs.list `
](https://cloud.google.com/logging/docs/api/reference/rest/v2/organizations.logs/list)
and [ ` projects.logs.list `
](https://cloud.google.com/logging/docs/api/reference/rest/v2/projects.logs/list)
.

**FEATURE:**

**New LogEntry fields** : Fields ` trace ` and ` sourceLocation ` were added
to [ ` LogEntry `
](https://cloud.google.com/logging/docs/api/reference/rest/v2/LogEntry) .

##  November 21, 2016

**FEATURE:**

**Organizations** : The Stackdriver Logging API now allows both projects and
organizations to own logs. A log belonging to an organization is named `
"organizations/[ORGANIZATION_ID]/logs/[LOG_ID]" ` . See [ `
organizations.logs.delete `
](https://cloud.google.com/logging/docs/api/reference/rest/v2/organizations.logs/delete)
.

**FEATURE:**

**Sinks** : The Stackdriver Logging API now allows both projects and
organizations to own sinks. In addition, sinks can now export log entries to
destinations in other projects. See [ ` LogSink `
](https://cloud.google.com/logging/docs/api/reference/rest/v2/organizations.sinks)
.

##  October 20, 2016

**FEATURE:**

Logging is generally available to Google Cloud Platform customers. Individual
features that are in Alpha or Beta release are marked as such in the
documentation.

**CHANGED:**

**Pricing** : Stackdriver is now available in Basic and Premium service tiers.
All existing and new Stackdriver accounts are entered into a 30-day free trial
of the Premium Tier. At the end of the trial period, you could lose some
functionality you had during the Beta release unless you upgrade to the
Premium Tier. For more details, see [ Pricing
](https://cloud.google.com/stackdriver/pricing) .

**FEATURE:**

**API v2** : The Stackdriver Logging API v2 is generally available, providing
a simplified log format. During a transition period, you can use the same API
at either of these two endpoints: ` https://logging.googleapis.com/v2beta1/...
` or ` https://logging.googleapis.com/v2/... ` .

**DEPRECATED:**

**API v1** : The Stackdriver Logging API v1 (v1beta3) is deprecated. Users of
this API should migrate to the v2 API. The v1 API will be removed from service
on March 30, 2017. Note: Obsolete link to migration information removed on
December 13, 2017. For updated information, see [ APIs & Reference
](https://cloud.google.com/logging/docs/apis) .

##  September 09, 2016

**CHANGED:**

The Google Cloud Logging API is now known as the Stackdriver Logging API. This
change does not affect any code.

##  June 15, 2016

**CHANGED:**

A change to the v2beta1 API might affect some existing code. In the following
methods, the parameter ` projectName ` has been changed to ` parent ` : `
sinks.create ` , ` sinks.list ` , ` metrics.list ` , ` metrics.create ` .

**CHANGED:**

The Google Logging API v2beta1 reference documentation now includes code
snippets for each method. For example, see [ ` entries.list `
](https://cloud.google.com/logging/docs/api/ref_v2beta1/rest/v2beta1/entries/list)
.

##  April 27, 2016

**CHANGED:**

The user documentation has been reorganized. The [ documentation landing page
](https://cloud.google.com/logging/docs) and the left-side navigation entries
have changed. Existing URLs to individual documentation pages will be
redirected if necessary.

##  March 23, 2016

**CHANGED:**

Google Cloud Logging is now **Stackdriver Logging** , part of the [ Google
Stackdriver ](https://cloud.google.com/stackdriver) suite of products. You can
now manage logs from Amazon EC2 virtual machine instances alongside your
Google Cloud Platform (GCP) projects. See [ Logging agent
](https://cloud.google.com/logging/docs/agent) for more details.

##  February 18, 2016

**CHANGED:**

The [ logging agent authorization
](https://cloud.google.com/logging/docs/agent/authorization) instructions now
recommend storing private-key credentials as `
/etc/google/auth/application_default_credentials.json ` . You do not have to
move your existing file at `
/root/.config/gcloud/application_default_credentials.json ` .

##  January 29, 2016

**CHANGED:**

The [ Logs Viewer ](https://cloud.google.com/logging/docs/view/logs_viewer)
now lets you [ view the structure
](https://cloud.google.com/logging/docs/view/logs_viewer#expanding) of log
entries. You can also [ show or hide
](https://cloud.google.com/logging/docs/view/logs_viewer#similar) log entries
with similar field values.

##  December 10, 2015

**CHANGED:**

Version 2 of the [ Cloud Logging API
](https://cloud.google.com/logging/docs/apis) is now available. Among other
changes, the V2 API lets you retrieve log entries from Logging using the [ `
entries.list `
](https://cloud.google.com/logging/docs/api/ref_v2beta1/rest/v2beta1/entries/list)
method.

##  October 22, 2015

**CHANGED:**

The [ Logs Viewer ](https://cloud.google.com/logging/docs/view/logs_viewer)
now has cascading menus for selecting log entries from Google App Engine and
Google Compute Engine.

##  October 13, 2015

**CHANGED:**

See [ logs-based-metrics
](https://cloud.google.com/logging/docs/view/logs_based_metrics) to learn how
to create Google Cloud Monitoring metrics using logs filters.

**CHANGED:**

The list of [ log types
](https://cloud.google.com/logging/docs/view/logs_index) has been expanded.

##  September 15, 2015

**CHANGED:**

Added [ Java examples ](https://cloud.google.com/logging/docs/api/tasks/) of
Logging API usage. Simplified the [ authorization code
](https://cloud.google.com/logging/docs/api/tasks/authorization) for Java and
Python, and the same code now runs on App Engine, Compute Engine, and your
development workstation.

##  September 09, 2015

**CHANGED:**

The [ command-line interface
](https://cloud.google.com/logging/docs/api/gcloud-logging) in the Google
Cloud SDK is now named ` gcloud beta logging ` .

##  August 12, 2015

**FEATURE:**

The [ Cloud Logging API ](https://cloud.google.com/logging/docs/reference/api-
overview) and [ command-line interface
](https://cloud.google.com/logging/docs/api/gcloud-logging) now support
project sinks. A project sink can export log entries from any combination of
logs, based on [ advanced logs filters
](https://cloud.google.com/logging/docs/view/advanced-queries) .

##  August 03, 2015

**FEATURE:**

Cloud Logging now has advanced logs filters that let you specify arbitrary
Boolean expressions that match on log entries. See [ Using advanced logs
filters ](https://cloud.google.com/logging/docs/view/advanced-queries) in the
Logs Viewer, and the [ Advanced Logs Filters guide
](https://cloud.google.com/logging/docs/view/advanced-queries) .

##  June 15, 2015

**CHANGED:**

The logging agent has new, simpler [ installation instructions
](https://cloud.google.com/logging/docs/agent/installation) You no longer have
to edit the agent's configuration file to install [ private-key authorization
](https://cloud.google.com/logging/docs/agent/authorization) .

**CHANGED:**

The Logging documentation has been reorganized. The [ table of contents
](https://cloud.google.com/logging/docs) now groups all information about the
logging agent, viewing logs, and exporting logs in individual sections.

##  May 21, 2015

**CHANGED:**

A new GCP Console UI panel for the [ logs export feature
](https://cloud.google.com/logging/docs/export/configure_export) was released.
The UI lets you export a subset of your logs from a logs service. For example,
you could export ` syslog ` from Google Compute Engine without exporting `
activity_log ` .

##  April 28, 2015

**FEATURE:**

You can now stream logs from Cloud Logging to [ Google Cloud Pub/Sub
](https://cloud.google.com/pubsub/docs) and from there to your own endpoints.
This involves changes to [ logs export
](https://cloud.google.com/logging/docs/export/using_exported_logs#pubsub-
overview) . For example, use Cloud Pub/Sub to route logs through [ Google
Cloud Dataflow ](https://cloud.google.com/dataflow/docs) and into tools like [
Google BigQuery ](https://cloud.google.com/bigquery/docs) .

##  March 19, 2015

**FEATURE:**

The [ Google Cloud Logging API ](https://cloud.google.com/logging/docs/api) is
now available in Beta release. The API lets you write logs, create logs, and
control the export of logs. Client libraries make it easy to use the API in
your favorite programming language.

**FEATURE:**

The [ ` glcoud logging ` ](https://cloud.google.com/logging/docs/api/gcloud-
logging) command-line interface, which uses the API, is now available in Beta
release. The commands provide an easy way to perform administrative tasks such
configuring logs export.

**FEATURE:**

Cloud Logging is now available in Beta release, allowing you to configure,
visualize, analyze and export your Google Compute Engine and Google App Engine
logs.

**FEATURE:**

The ` google-fluentd ` logging agent runs with [ additional operating systems
](https://cloud.google.com/logging/docs/agent/installation) , including
Debian, Ubuntu, Red Hat, and CentOS. A single script installs the agent on any
supported operating system.

**FEATURE:**

The ` google-fluentd ` logging agent supports [ two dozen third-party logs
](https://cloud.google.com/logging/docs/view/logs_index) .

**CHANGED:**

The [ Logs Viewer refresh
](https://cloud.google.com/logging/docs/view/logs_viewer) brings more search
options and quicker access to [ logs export configurations
](https://cloud.google.com/logging/docs/export/configure_export) . Regex-
search has been removed as part of this refresh.

**CHANGED:**

The Cloud Logging documentation has been improved with more set-up options, [
simpler procedures ](https://cloud.google.com/logging/docs/agent/installation)
and [ more examples
](https://cloud.google.com/logging/docs/export/using_exported_logs) .

##  January 15, 2015

**FEATURE:**

Beta release: App Engine logs can be exported to Cloud Storage and BigQuery.

