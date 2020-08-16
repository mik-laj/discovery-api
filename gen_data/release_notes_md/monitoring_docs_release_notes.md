#  Release notes

This page documents production updates to Monitoring. You can periodically
check this page for announcements about new or updated features, bug fixes,
known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/stackdriver-release-notes.xml `

##  August 13, 2020

**FEATURE:**

The new, out-of-the-box **Infrastructure Summary** dashboard for Compute
Engine VMs provides a single-pane-of-glass view into your VM fleet and load
balancers. At a glance, you can see the top 5 VMs across a variety of key
metrics including memory, CPU, sent/received traffic, latency, disk
read/write, and more.

##  August 12, 2020

**FEATURE:**

Enhancements to the pre-configured Compute Engine **VM Instances** dashboard.
The inventory table now includes a **Monitoring Agent Status** column, and the
Monitoring agent can be installed by using a UI workflow from the table. The
**Explore** tab gives an overview of additional metrics being sent (including
agent metrics, custom metrics, and logs-based metrics) as well as a set of
quick links to learn more about each type of metric. You can also use the
**Recommended Alerts** button on the dashboard to configure fleet-wide alerts.

##  July 10, 2020

**FEATURE:**

SLO monitoring for microservices is now Generally Available in the Cloud
Console. This feature lets you create service-level objectives (SLOs) and set
up alerting policies to monitor their performance using auto-generated
dashboards with metrics, logs, and alerts in a single place. For more
information, see [ SLO monitoring
](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring) .

##  July 07, 2020

**CHANGED:**

Monitoring Query Language (MQL) is now Generally Available. MQL is an
expressive, text-based interface to Cloud Monitoring time-series data. With
MQL, you can create charts you can't create any other way. You can access MQL
from both the Cloud Console and the Monitoring API. For more information, see
[ Introduction to Monitoring Query Language
](https://cloud.google.com/monitoring/mql/) .

##  June 15, 2020

**CHANGED:**

The Service Monitoring API is now Generally Available. You can use this
feature to create services, set service-level objectives (SLOs), and create
alerting policies to monitor your SLOs. See [ Service monitoring
](https://cloud.google.com/monitoring/service-monitoring/) for documentation,
and [ ` services ` ](https://cloud.google.com/monitoring/api/v3/#service-
monitoring) for reference material.

##  June 08, 2020

**FEATURE:**

Enhancements to the pre-configured Compute Engine **VM Instances** dashboard.
Compute Engine cross-fleet metrics and detail views specific to CPU, Disk,
Memory, and Network are now available. Use filters to narrow down the set of
VMs being inspected, and use the time selector or in-chart time selection to
change the time window. VMs with the Monitoring agent installed get detailed
memory and disk analysis out of the box.

##  May 20, 2020

**FEATURE:**

Cloud Monitoring introduces an improved experience for viewing and managing
incidents. Improvements include performance optimizations for Workspaces with
large numbers of incidents, summary statics, and the ability to filter by
alerting policy name, metric type, and resource type. For more information,
see [ Incidents and events
](https://cloud.google.com/monitoring/alerts/incidents-events) .

##  May 19, 2020

**CHANGED:**

Alert notifications delivered by email now come from "alerting-
noreply@google.com" instead of "alerts@stackdriver.com".

##  May 14, 2020

**CHANGED:**

Starting in version 6.0.2, the Cloud Monitoring agent is available for the
Ubuntu LTS 20.04 (Focal Fossa) distribution.

##  May 08, 2020

**FEATURE:**

Monitoring Query Language (MQL) is now available in Beta. MQL is an
expressive, text-based interface to Cloud Monitoring time-series data. With
MQL, you can create charts you can't create any other way. You can access MQL
from both the Cloud Console and the Monitoring API. For more information, see
[ Introduction to Monitoring Query Language
](https://cloud.google.com/monitoring/mql/) .

##  April 28, 2020

**DEPRECATED:**

The 5.x version of the Cloud Monitoring agent for Linux is deprecated. Users
are encouraged [ to upgrade their agents
](https://cloud.google.com/monitoring/agent/install-agent#upgrade) as soon as
possible.

**DEPRECATED:**

The ` stack-install.sh ` and the ` install-monitoring-agent.sh ` installation
scripts for the Cloud Monitoring agent for Linux [ are deprecated
](https://cloud.google.com/stackdriver/docs/deprecations/mon-agent-install) .
Refer to the [ Installing the Cloud Monitoring agent
](https://cloud.google.com/monitoring/agent/install-agent#joint-install) guide
for the latest installation procedures.

##  March 30, 2020

**FEATURE:**

You can now write time-series data for custom and Prometheus metrics at the
rate of 1 data point every 10 seconds. This was previously limited to 1 point
every minute.

**CHANGED:**

Data for custom and Prometheus metrics is now retained for 24 months.
Previously, the retention period was 6 weeks.

##  February 24, 2020

**CHANGED:**

Stackdriver Monitoring is available exclusively in the Cloud Console. For more
information, see [ Monitoring in the GCP Console
](https://cloud.google.com/monitoring/docs/monitoring_in_console) .

**FEATURE:**

Stackdriver Monitoring agent version 6.0.0 is now available for the following
distributions:

  * CentOS 7 
  * Ubuntu LTS 16.04 (Xenial Xerus) and Ubuntu LTS 18.04 (Bionic Beaver) 
  * Ubuntu Minimal LTS 16.04 (Xenial Xerus) and Ubuntu Minimal LTS 18.04 (Bionic Beaver) 
  * Amazon Linux AMI (except Amazon Linux 2.0 AMI) 

##  February 19, 2020

**FEATURE:**

Starting in version 6.0.0, the Stackdriver Monitoring agent is available for
the Ubuntu 19.10 (Eoan Ermine) distribution.

##  February 18, 2020

**FEATURE:**

Stackdriver Monitoring agent version 6.0.0 is now available for the Debian 9
distribution.

##  February 14, 2020

**FEATURE:**

You can now send notifications from your alerting policies to Cloud Pub/Sub
topics. For more information, see [ Notification options
](https://cloud.google.com/monitoring/support/notification-options) .

**CHANGED:**

The Stackdriver Monitoring Dashboard API is now Generally Available. You can
use this feature to programmatically manage your dashboards and charts. See [
Managing dashboards by API
](https://cloud.google.com//monitoring/dashboards/api-dashboard) for
documentation, and [ ` Dashboard `
](https://cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards)
for reference material.

##  February 11, 2020

**FEATURE:**

Stackdriver Monitoring agent version 6.0.0 has been released to the CentOS 8
distribution.

##  February 06, 2020

**FEATURE:**

Starting in version 6.0.0, the Stackdriver Monitoring agent is available for
the Debian 10 distribution.

##  January 31, 2020

**FEATURE:**

Stackdriver Monitoring Agent version 6.0.0 is now available, and the release
will gradually roll out to the various Linux distributions. This version is
built on a [ fork of ` collectd ` version 5.8.1
](https://github.com/Stackdriver/collectd) and includes the following changes:

  * drops support for [ various third-party integrations ](https://cloud.google.com/stackdriver/docs/deprecations/third-party-apps) . 
  * changes the file path for configuring an HTTP proxy when [ installing the agent ](https://cloud.google.com/monitoring/agent/install-agent#joint-install) . 

**FEATURE:**

Stackdriver Monitoring agent version 6.0.0 is now available for the SUSE and
SUSE Linux Enterprise Server (SLES) Linux distributions.

##  January 13, 2020

**CHANGED:**

Stackdriver Monitoring in the Cloud Console is Generally Available and is the
default option. For a limited period of time, you also have the option to use
the classic Stackdriver Monitoring Console. Your configuration information,
such as uptime checks and alerting policies, is accessible and changeable,
from the Cloud Console and from the classic Stackdriver Monitoring Console.
For more information, see [ Monitoring in the GCP Console
](https://cloud.google.com/monitoring/docs/monitoring_in_console) .

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

##  December 09, 2019

**FEATURE:**

The Stackdriver Monitoring Dashboard API is now in Beta release. You can use
this feature to programmatically manage your dashboards and charts. See [
Managing dashboards by API
](https://cloud.google.com//monitoring/dashboards/api-dashboard) for
documentation, and [ ` Dashboard `
](https://cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards)
for reference material.

##  December 04, 2019

**FEATURE:**

Stackdriver Monitoring in the Cloud Console is in beta release. Your
configuration information, such as uptime checks and alerting policies, is
accessible and changeable, from the Cloud Console and from the classic
Stackdriver Monitoring Console. For more information about the beta, see [
Monitoring in the GCP Console
](https://cloud.google.com/monitoring/docs/monitoring_in_console) .

##  November 14, 2019

**FEATURE:**

The Service Monitoring API is now in Beta release. You can use this feature to
create services, set service-level objectives (SLOs), and create alerting
policies to monitor your SLOs. See [ Service monitoring
](https://cloud.google.com/monitoring/service-monitoring/) for documentation,
and [ ` services ` ](https://cloud.google.com/monitoring/api/v3/#service-
monitoring) for reference material.

##  September 10, 2019

**CHANGED:**

When creating a new Google Kubernetes Engine (GKE) cluster, Stackdriver
Kubernetes Engine Monitoring is now the default Stackdriver support option.
This is a change from prior versions where Stackdriver Logging and Stackdriver
Monitoring were the default Stackdriver support option. For more information,
see [ Overview of Stackdriver support for GKE
](https://cloud.google.com/monitoring/kubernetes-engine/) .

##  August 08, 2019

**FEATURE:**

[ Stackdriver Monitoring ](https://cloud.google.com/monitoring/uptime-checks)
has two new uptime check features: SSL certificate validation and regex
negation content matching.

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

##  May 02, 2019

**FEATURE:**

Stackdriver Workspace creation is now a one-step operation. For more
information, go to [ Getting a Workspace quickly
](https://cloud.google.com/monitoring/workspaces/manage#single-project-ws) .

##  April 23, 2019

**FEATURE:**

The OpenCensus library is now generally available as the official library for
user-defined metrics in Stackdriver Monitoring. The [ Custom metrics with
OpenCensus ](https://cloud.google.com/monitoring/custom-metrics/open-census)
page includes samples in Go, Java, Node.js, and Python.

##  March 18, 2019

**FEATURE:**

The [ Uptime Configuration API
](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs)
is now complete and GA. The API, part of the [ Stackdriver Monitoring API
](https://cloud.google.com/monitoring/api/ref_v3/rest/) , lets you create,
edit and manage [ uptime checks ](https://cloud.google.com/monitoring/uptime-
checks/) .

##  March 15, 2019

**CHANGED:**

Stackdriver agents are subject to an updated [ deprecation policy
](https://cloud.google.com/stackdriver/docs/agent-deprecation-policy) . As
part of this transition, the next major version of the Stackdriver Monitoring
and Stackdriver Logging agents will stop supporting operating systems that are
at the end of their lifecycle, as well as some [ third-party agent plugins
](https://cloud.google.com/monitoring/agent/plugins/) .

##  February 08, 2019

**FEATURE:**

The Stackdriver Monitoring Agent now supports Ubuntu 18.04 LTS ("Bionic
Beaver").

##  December 06, 2018

**CHANGED:**

A mechanism to collect monitoring data from Prometheus clients, which can be
deployed as a sidecar in the same Kubernetes pod as a working Prometheus
server, is now available. See [ Using Prometheus
](https://cloud.google.com/monitoring/kubernetes-engine/prometheus) for more
information.

##  December 05, 2018

**FEATURE:**

Documentation for using [ OpenCensus ](https://opencensus.io) to capture
custom metrics in Java applications is now available. See [ Custom metrics
with OpenCensus ](https://cloud.google.com/monitoring/custom-metrics/open-
census) for more information.

##  November 16, 2018

**CHANGED:**

The new UI for creating alerting policies is now complete and Generally
Available. This interface, based on Metrics Explorer, offers fine-grained
control over the selection of the metrics used in alerting conditions. See [
Managing Alerting Policies ](https://cloud.google.com/monitoring/alerts/using-
alerting-ui) for more information.

##  October 10, 2018

**FEATURE:**

A new UI for creating alerting policies is available in Beta. This interface,
based on Metrics Explorer, offers fine-grained control over the selection of
the metrics used in alerting conditions. See [ Managing Alerting Policies
](https://cloud.google.com/monitoring/alerts/using-alerting-ui) for more
information.

##  September 19, 2018

**CHANGED:**

[ Stackdriver Kubernetes Monitoring
](https://cloud.google.com/monitoring/kubernetes-engine/) (Beta) for
Kubernetes version 1.10.6 and above, restores the managed support for
Kubernetes Monitoring. You can also [ upgrade your existing clusters
](https://cloud.google.com/monitoring/kubernetes-engine/installing#migrating)
to this release, no matter which (if any) Stackdriver support they had before.
Note the warnings about [ incompatibilities
](https://cloud.google.com/monitoring/kubernetes-engine/migration) between the
old and new Stackdriver support.

##  September 18, 2018

**FEATURE:**

The legends for Stackdriver charts have been significantly improved. Legends
now support more than one labeled column. The legend provides a selected set
of columns as a default, but users can choose the columns they want to see in
the legend. All columns are sortable. The legend detects a configuration of
columns that exceeds the available space, and provides scrollbars. The
resizing of the legends is also improved. For details, see [ Configuring
Legends ](https://cloud.google.com/monitoring/charts/working-with-legends) .

##  September 10, 2018

**CHANGED:**

"Stackdriver accounts" have been renamed "Workspaces" to reflect their use as
a "single pane of glass" through which you view resources from multiple
projects and AWS accounts. There is no change in their functionality, but we
have improved the documentation for them. For more information, see [
Workspaces ](https://cloud.google.com/monitoring/workspaces/) .

##  June 29, 2018

**CHANGED:**

On July 1, 2018 at 00:00 PDT, Stackdriver switches to consumption-based
pricing. For more information, see [ Stackdriver Pricing
](https://cloud.google.com/stackdriver/pricing_v2) .

##  June 19, 2018

**FEATURE:**

If you want to minimize the **AWS permissions** you give to Stackdriver, then
see [ Minimal AWS Permissions
](https://cloud.google.com/monitoring/support/minimal-aws-permissions) .

##  June 18, 2018

**CHANGED:**

**Between June 18, 2018 at 06:00 PDT and July 1, 2018 at 00:00 PDT, your use
of Stackdriver is free** . The service tiers have been removed, and you can
experience all features without incurring costs. Thereafter, Stackdriver
switches to consumption-based pricing. For more information, see [ Upcoming
Pricing ](https://cloud.google.com/stackdriver/pricing_v2) .

##  May 24, 2018

**CHANGED:**

Any Stackdriver free trials created after May 29, 2018 will expire on June 30,
2018. After June 30, 2018, free trials will be replaced with a free monthly
allocation of logs and metrics. For more information about Stackdriver's new
consumption-based pricing, see [ Stackdriver Upcoming Pricing
](https://cloud.google.com/stackdriver/pricing_v2) .

##  May 23, 2018

**CHANGED:**

Custom dashboards and pages for resource groups are now limited to 25 charts.
Any dashboards or groups pages with more than 25 charts will continue to work,
but you will not be able to add additional charts to them.

##  May 22, 2018

**FEATURE:**

You can now see your Monitoring usage metrics and estimate your bill for your
usage of Monitoring, according to the new Stackdriver pricing and in advance
of billing enforcement. See [ Estimating your bills
](https://cloud.google.com/stackdriver/estimating-bills) for details.

##  May 21, 2018

**FEATURE:**

A new UI for creating conditions in alerting policies is available in Beta.
This UI, based on Metrics Explorer, offers fine-grained control over the
selection of the metrics used in alerting conditions. See [ Managing Alerting
Policies ](https://cloud.google.com/monitoring/alerts/using-alerting-ui) for
more information.

##  May 11, 2018

**CHANGED:**

If you are using custom IAM roles, any roles that load Stackdriver Monitoring
dashboards now require additional IAM permissions. The `
monitoring.dashboards.* ` and ` monitoring.publicWidgets.* ` permissions are
now public, and custom roles used to load dashboards must now include them.
See [ Stackdriver Monitoring Access Control
](https://cloud.google.com/monitoring/access-control#roles) for more
information.

##  May 02, 2018

**FEATURE:**

[ Stackdriver Kubernetes Monitoring
](https://cloud.google.com//monitoring/kubernetes-engine) is released in Beta
for Kubernetes 1.10 clusters running in [ Kubernetes Engine
](https://cloud.google.com//kubernetes-engine/docs/) . The previous
Stackdriver support is still available for those who do not opt into this Beta
release. The release introduces new [ monitored resource types
](https://cloud.google.com//monitoring/api/resources#tag_k8s_cluster) and new
[ Kubernetes metrics
](https://cloud.google.com//monitoring/api/metrics_kubernetes#kubernetes) .
The monitoring features are free to customers during the Beta period.

##  April 26, 2018

**CHANGED:**

You can now use variables in the documentation associated with alerting
policies to pull specific details about the alert into notifications, to
create playbook information for responders. See [ Additional documentation
tools ](https://cloud.google.com/monitoring/alerts/doc-variables) for more
information. The Webhooks and Slack notification channels now receive a copy
of this enhanced documentation as part of alert notifications. Additionally,
email notifications from alerting policies now use HTML-formatted messages.

##  April 19, 2018

**FEATURE:**

Boolean metrics can now be queried and charted.

##  April 17, 2018

**CHANGED:**

The [ Using Alerting Policies ](https://cloud.google.com/monitoring/alerts)
documentation has been updated to provide additional guides and links to
sample code for managing alerting policies and notification channels
programmatically. The update also removes some obsolete service-tier
information.

##  March 28, 2018

**CHANGED:**

Stackdriver now loads charts much more quickly, especially when the chart
contains a long time span.

##  March 26, 2018

**CHANGED:**

A new option on the Dashboards menu, **Public Charts** , lets you see a list
of all the shared charts. You can also use this page to remove sharing from a
chart. The on-chart indicator that the chart is shared has been removed.

##  March 12, 2018

**CHANGED:**

Beginning on June 30, 2018, Stackdriver is switching to consumption-based
pricing, including revised quotas. For more information, see [ Stackdriver
Upcoming Pricing ](https://cloud.google.com//stackdriver/pricing_v2) .

##  March 08, 2018

**FEATURE:**

The ` AlertPolicy ` and ` NotificationChannels ` APIs are now in Beta release.
See [ Alerting policies
](https://cloud.google.com/monitoring/api/v3/#alerting-policies) and [
Notification channels
](https://cloud.google.com/monitoring/api/v3/#notification-channels) for more
information.

##  January 29, 2018

**FIXED:**

The Stackdriver email reports that you can configure for your [ Stackdriver
account ](https://cloud.google.com/monitoring/workspaces/manage#single-
project-ws) have been improved. Issues with the content and the delivery of
reports have been fixed, and the _from_ address for the reports has been
changed from ` monitoring-noreply@stackdriver.google.com ` to ` monitoring-
noreply@google.com ` . The Utilization section, present only if the Monitoring
Agent is installed, now lists the 10 groups with the highest utilization, and
a new summary row reports overall utilization for the Stackdriver account.

##  January 17, 2018

**CHANGED:**

The name of the Monitoring agent process on Windows has been updated. It now
shows up in the system process list as ` StackdriverMonitoring ` .

##  January 08, 2018

**CHANGED:**

The performance of the Monitoring dashboards and charts has been improved.
Additionally, a new version of Metrics Explorer is available, and the metric-
selection interface has been greatly improved, allowing arbitrary label
filtering and group-by functionality. This interface is also used for creating
dashboard charts, making the process consistent across the two tasks. See [
Using Charts ](https://cloud.google.com/monitoring/charts) for more
information.

##  December 14, 2017

**CHANGED:**

**Alerting events page** : An updated implementation has required some user
interface changes. The alerting events page ( **Alerting > Events ** ) no
longer shows a heatmap or counts of events in each category.

##  November 08, 2017

**CHANGED:**

The Monitoring agents for Linux and Windows VM instances now report errors for
unrecognized metrics. The errors are written to the agent log on your VM
instance. If the [ Logging agent
](https://cloud.google.com/logging/docs/agent/) is also running on the VM
instance, then the logs are also available in Stackdriver Logging. The error
messages are, "Unsupported collectd plugin/type combination" and "Unsupported
collectd ID." Previously, these metrics were dropped silently. See the agent's
[ Troubleshooting Checklist
](https://cloud.google.com/monitoring/agent/troubleshooting#checklist) for
more information.

##  November 05, 2017

**DEPRECATED:**

Documentation for the deprecated Cloud Monitoring API v2 has been removed. The
API was turned down in August, 2017.

##  October 19, 2017

**FEATURE:**

Beta release: The Monitoring agent can now export collectd and statsd metrics
as Stackdriver [ custom metrics ](https://cloud.google.com/monitoring/custom-
metrics/) . For more information, see [ Custom Metrics from the Agent
](https://cloud.google.com/monitoring/agent/custom-metrics-agent) and the
agent's [ StatsD plugin
](https://cloud.google.com/monitoring/agent/plugins/statsd)

##  October 17, 2017

**FEATURE:**

Beta release: The [ Uptime Configuration API
](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs)
and [ uptime metrics
](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-monitoring) are now
available. The API, part of the [ Stackdriver Monitoring API
](https://cloud.google.com/monitoring/api/ref_v3/rest/) , lets you create and
edit [ uptime checks ](https://cloud.google.com/monitoring/uptime-checks/) .
The status of your checks is recorded in the uptime metrics.

##  October 02, 2017

**FIXED:**

Calls to [ createTimeSeries
](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create)
now fail without writing any data points if the request includes more than one
point in the same time series. Formerly, in some cases, one data point would
be written in each time series and a status of 500 would be returned by the
call.

##  September 13, 2017

**CHANGED:**

**Object Stores Resources** : Google Cloud Storage metrics and Amazon S3
metrics are now separated in the Stackdriver UI into their own service
dashboards. The "Object Stores" dashboard is replaced by "Cloud Storage" or
"S3", depending on which service you are using.

##  September 08, 2017

**FEATURE:**

**HTTPS(S) Load Balancer** metrics are available in Beta release to use in
Monitoring. For details, see the GCP [ ` loadbalancing `
](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-loadbalancing)
metrics and the [ ` https_lb_rule `
](https://cloud.google.com/monitoring/api/resources#tag_https_lb_rule)
monitored resource.

**FEATURE:**

**Cloud Interconnect** custom dashboards and alert monitoring are available in
Beta release. For details, see the GCP [ ` interconnect `
](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-interconnect)
metrics and the [ ` interconnect `
](https://cloud.google.com/monitoring/api/resources#tag_interconnect) and [ `
interconnect_attachment `
](https://cloud.google.com/monitoring/api/resources#tag_interconnect_attachment)
monitored resources.

**FEATURE:**

**HTTPS(S) Load Balancer** metrics are available in Beta release to use in
Monitoring. For details, see the GCP [ ` loadbalancing `
](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-loadbalancing)
metrics and the [ ` https_lb_rule `
](https://cloud.google.com/monitoring/api/resources#tag_https_lb_rule)
monitored resource.

##  August 23, 2017

**FEATURE:**

**Dashboard filtering** : Custom dashboards and resource list pages now
support filtering on groups. Each page that supports filtering now has a
filter bar under the header where you specify the group.

##  July 10, 2017

**FEATURE:**

**Heatmaps for distribution metrics** : Heatmaps are available in dashboard
charts. Select a distribution metric from either the **Custom** or **Logging**
metric groups and specify **Heatmap** .

**FEATURE:**

**IAM for Stackdriver Monitoring** is now complete and GA. New IAM roles
include **Monitoring Editor** and **Monitoring Admin** , and there is full
support for custom roles. For more information, see Monitoring [ Access
Control ](https://cloud.google.com/monitoring/access-control) .

**CHANGED:**

**Agent permissions** in VM instances: The agent no longer needs the **Project
Editor** IAM role; it only needs the **Monitoring Metric Writer** role ( `
roles/monitoring.metricWriter ` ). For more information, see Monitoring [
Access Control ](https://cloud.google.com/monitoring/access-control) .

**FEATURE:**

**Windows process metrics** now include all processes accessible to the
Monitoring agent. See [ Agent process metrics
](https://cloud.google.com/monitoring/api/metrics_agent#agent-processes) .

**FEATURE:**

**Windows Server 2016** is supported by the current Monitoring agent.

**CHANGED:**

**Stacked charts** : The order of data streams in stacked charts has been
reversed, so that the first stream is on the top and the last stream is on the
bottom. This order is consistent with the chart legend and hovercard.

##  June 05, 2017

**FEATURE:**

**Uptime checks** have a new overview and detail dashboards. See [ Uptime
Checks ](https://cloud.google.com/monitoring/alerts/uptime-checks) .

**FEATURE:**

**Singapore region support** : Stackdriver now supports the Singapore region,
` asia-southeast1 ` .

##  May 01, 2017

**FEATURE:**

New metric and resource types: There are new Cloud Platform metric and
resource types, including those for Cloud Bigtable, Cloud Dataflow, Cloud DNS,
Cloud Internet of Things, Cloud Pub/Sub, Cloud Spanner, and Stackdriver
Logging. Microsoft Windows system and application metrics ( ` iis ` , ` mssql
` , ` pagefile ` ) are available as Agent metrics and can be used for charting
and alerting.

##  April 02, 2017

**ISSUE:**

**v2beta2 API turndown** : The deprecated v2beta1 and v2beta2 APIs will be
shut down during August 2017.

##  March 31, 2017

**FEATURE:**

**Time shifting (Beta)** : You can now compare your current metric data with
data from 1 day, 1 week, or 4 weeks ago. See **Compare to past** in the
**Advanced options** for line chart creation.

**FEATURE:**

**Faster chart legends** : Charts involving custom and logs-based metrics now
have faster legends that include instance names with the metric name where
available. You can quickly identify instances and sort the metrics by name.

**FEATURE:**

**Faster user interface** : Initial page load times have been reduced across
the user interface.

**FEATURE:**

**Cloud ML** : [ Cloud Machine Learning Engine metrics
](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-ml) are available
for dashboards and alerting.

**FEATURE:**

**Cloud Spanner** : [ Cloud Spanner metrics
](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-spanner) are
available for dashboards and alerting.

**FEATURE:**

**Cloud Dataflow** : [ Cloud Dataflow
](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-dataflow) is now
integrated with Monitoring. For more details, see the [ Big Data and Machine
Learning Blog ](https://cloud.google.com/blog/big-data/2017/03/monitoring-and-
improving-your-google-cloud-dataflow-pipelines-with-google-stackdriver) .

**CHANGED:**

**Monitoring agent** : Although the statsd plugin is distributed with the
Monitoring agent, there are not yet any instructions for using the plugin with
Monitoring.

##  February 06, 2017

**FIXED:**

**Process owner** : When sending process metrics, the Stackdriver Monitoring
agent now returns a stringified UID if the process owner name is not set.
Previously, the agent would not send process owner information, which was then
treated by the Monitoring API as malformed input and discarded. Available in
stackdriver-agent/5.5.2-359. See [ Determining the agent version
](https://cloud.google.com/monitoring/agent/install-agent#agent-version) .

**FIXED:**

**Lost input from the Monitoring agent** : Malformed data from the Monitoring
agent could cause Stackdriver Monitoring to lose well-formed input bundled in
the same request. Now, only the malformed input is lost. You do not have to
update your agent for this fix.

**FEATURE:**

**Selectable uptime check regions** : Stackdriver Monitoring now lets you
select the geographic region(s) that check your service.

##  January 18, 2017

**FEATURE:**

**New AWS regions** : Monitoring now supports the AWS Canada ( **ca-
central-1** ) and London ( **eu-west-2** ) regions.

##  December 12, 2016

**FEATURE:**

**Account IDs in URLs** : Monitoring has added the Stackdriver account ID to
its URLs. You can now open multiple tabs for different accounts and more
easily share links with coworkers. URLs without the account ID use the most
recently accessed Stackdriver account.

##  December 08, 2016

**FEATURE:**

**Incident pages** (Beta): See **Alerting > Incidents ** . Each open incident
now has a detail page that collects a graph of the incident, links to affected
resources, and the comments made on the incident.

**FEATURE:**

**Metrics Explorer** (Beta): See **Resources > Metric Explorer ** . Select a
monitored resource type and metric. You can aggregate data across your
instances.

##  November 21, 2016

**CHANGED:**

**Time series** : The recommended maximum rate of writing data points to a
single time series is changed from 1/sec to 1/min. See [ Writing metric data
](https://cloud.google.com/monitoring/custom-metrics/creating-metrics#writing-
ts) .

**FEATURE:**

**Chart options** : You can now display data as stacked bar charts and stacked
area charts, using the **Stacked** option under **Chart Types** . Stacked bar
charts are automatically aligned to hour boundaries. Stacked area charts work
best with metrics received at 1-minute intervals.

**FEATURE:**

**New AWS region** : Monitoring now supports the AWS region **us-east-2** .

**FEATURE:**

**Chart snapshots** : You can now download images of charts in PNG format.
Choose **Download Image** from the **More** menu. The chart legend is not
presently rendered.

**FEATURE:**

**Group support for metrics** : When charting custom and logs-based metrics, a
new **Group** filter appears under **Advanced Options** . The effect of the
filter is not shown until after you save the chart.

##  October 20, 2016

**FEATURE:**

**GA** : Monitoring is generally available to Google Cloud Platform customers.
Individual features that are in Alpha or Beta release are marked as such in
the documentation.

**CHANGED:**

**Pricing** : Stackdriver is now available in Basic and Premium service tiers.
All existing and new Stackdriver accounts are entered into a 30-day free trial
of the Premium Tier. At the end of the trial period, you could lose some
functionality you had during the Beta release unless you upgrade to the
Premium Tier. For more details, see [ Pricing
](https://cloud.google.com/stackdriver/pricing) .

**FEATURE:**

**API v3** : The Stackdriver Monitoring API v3 is now generally available.

**FEATURE:**

**Monitoring agent** : A new version of the Stackdriver Monitoring Agent,
v5.5.2-349, is available. Its improvements include an update to collectd
5.5.2, support MongoDB 3.0, [ agent health metrics
](https://cloud.google.com/monitoring/api/metrics_agent#agent-agent) , and
bundled ~~statsd~~ , tail, and network plugins. For more information, see [
Installing the Monitoring Agent
](https://cloud.google.com/monitoring/agent/install-agent) .

**FEATURE:**

**Custom metrics** : Custom metric descriptors are created as needed when you
write time series data. See [ Auto-creation of custom metrics
](https://cloud.google.com/monitoring/custom-metrics/creating-metrics#auto-
creation) .

**FEATURE:**

**Charting** : You can use log scales in your charts, and you can zoom both
the x- and y-axes by clicking-and-dragging.

**FEATURE:**

**New metrics** : New metrics are now available from Cloud Router, BigQuery,
and TaskQueues (pull metrics). See the [ Metrics List
](https://cloud.google.com/monitoring/api/metrics) .

**FEATURE:**

**Creating alerts** : We have introduced a new, more streamlined user
interface for creating and editing alerting policies.

##  September 11, 2016

**CHANGED:**

The Google Monitoring API (v3) is now known as the Stackdriver Monitoring API
(v3). This change does not affect any code.

**DEPRECATED:**

The Monitoring v2 API is now deprecated. It is still named the Google Cloud
Monitoring API in **APIs & services ** .

##  July 26, 2016

**CHANGED:**

Some documentation pages have moved in the table of contents, but their URLs
are the same or have redirections. All agent-related pages are now part of the
How-To section, [ Using the Monitoring Agent
](https://cloud.google.com//monitoring/agent/) . The former "Using Metrics"
page has been reorganized into several pages under [ Using Custom Metrics
](https://cloud.google.com/monitoring/agent/) .

##  June 09, 2016

**CHANGED:**

The documentation for metrics and custom metrics has been reorganized and
extended for the Monitoring API v3. See [ Metrics
](https://cloud.google.com//monitoring/api/v3/metrics) , [ Using Metrics
](https://cloud.google.com//monitoring/api/v3/using-metrics) , and [ Metrics
List ](https://cloud.google.com//monitoring/api/metrics) .

**CHANGED:**

The [ Stackdriver Monitoring API v3 reference documentation
](https://cloud.google.com/monitoring/api/ref_v3/rest/) now includes code
samples for each method. For example, see [ metricDescriptors.list
](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/list)
. [ Sample Code ](https://cloud.google.com/monitoring/docs/tutorials) will
continue to be available on GitHub.

##  June 06, 2016

**CHANGED:**

[ Metrics List ](https://cloud.google.com//monitoring/api/metrics) is now a
comprehensive list of all metrics available in Monitoring, including metrics
gathered by the monitoring agent and metrics from Amazon Web Services.

##  April 27, 2016

**CHANGED:**

The documentation has been reorganized. The [ documentation landing page
](https://cloud.google.com/monitoring/docs/) and the left-side navigation
entries have changed. Existing URLs to individual documentation pages will be
redirected if necessary.

**CHANGED:**

The [ Quickstart ](https://cloud.google.com//monitoring/quickstart-lamp) has
been simplified. It now includes setting up a virtual machine instance and
installing both the monitoring and logging agents.

##  March 23, 2016

**CHANGED:**

Google Cloud Monitoring is now **Stackdriver Monitoring** , part of the [
Google Stackdriver ](https://cloud.google.com/stackdriver) suite of products.

**FEATURE:**

You can now monitor Amazon Web Services (AWS) accounts alongside your Google
Cloud Platform (GCP) projects. Read about [ Stackdriver Accounts
](https://cloud.google.com/monitoring/accounts/) and install the new [
monitoring agent ](https://cloud.google.com/monitoring/agent/) .

**ISSUE:**

When installing the monitoring agent on an Amazon EC2 VM instance running
Microsoft Windows, ignore the following error message if you get it only once
after the service is started: "StackdriverAgent is running on an AWS instance
but project ID is not set."

##  March 17, 2016

**FEATURE:**

The [ Monitoring API v3
](https://cloud.google.com/monitoring/api/ref_v3/rest/) is now available.
Users are encouraged to begin upgrading from the Cloud Monitoring API v2. See
[ What's new ](https://cloud.google.com/monitoring/api/v3/) in the v3 API and
look at the new [ code samples
](https://cloud.google.com/monitoring/docs/tutorials) on GitHub.

##  September 29, 2015

**FEATURE:**

Charts now have a [ View Logs
](https://cloud.google.com/monitoring/quickstart-lamp#charts-to-logs) option
in their settings menu.

##  January 07, 2015

**FEATURE:**

First beta release of [ Google Cloud Monitoring powered by Stackdriver
](https://cloud.google.com/monitoring) .

