#  Release notes

This page provides a combined list of the release notes for products in Google
Cloud's operations suite. You can periodically check these page for
announcements about new or updated features, bug fixes, known issues, and
deprecated functionality.

You can also see find the release notes for each separate product on the
following pages:

  * [ Cloud Monitoring ](/monitoring/docs/release-notes)
  * [ Cloud Logging ](/logging/docs/release-notes)
  * [ Error Reporting ](/error-reporting/docs/release-notes)
  * [ Cloud Debugger ](/debugger/docs/release-notes)
  * [ Cloud Profiler ](/profiler/docs/release-notes)
  * [ Cloud Trace ](/trace/docs/release-notes)

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/stackdriver-release-notes.xml `

##  August 17, 2020

**Cloud Logging**

**FEATURE:**

To help you explore your logs more efficiently, Cloud Logging now provides
suggested queries based on the context of your Google Cloud project. For more
information, go to [ Suggested queries
](https://cloud.google.com/logging/docs/view/building-
queries#suggested_queries) .

**Cloud Trace**

**FEATURE:**

The Cloud Trace viewer now supports search by the trace ID. For more
information, see [ Viewing Trace Details
](https://cloud.google.com/trace/docs/viewing-details) .

##  August 13, 2020

**Cloud Monitoring**

**FEATURE:**

The new, out-of-the-box **Infrastructure Summary** dashboard for Compute
Engine VMs provides a single-pane-of-glass view into your VM fleet and load
balancers. At a glance, you can see the top 5 VMs across a variety of key
metrics including memory, CPU, sent/received traffic, latency, disk
read/write, and more.

##  August 12, 2020

**Cloud Monitoring**

**FEATURE:**

Enhancements to the pre-configured Compute Engine **VM Instances** dashboard.
The inventory table now includes a **Monitoring Agent Status** column, and the
Monitoring agent can be installed by using a UI workflow from the table. The
**Explore** tab gives an overview of additional metrics being sent (including
agent metrics, custom metrics, and logs-based metrics) as well as a set of
quick links to learn more about each type of metric. You can also use the
**Recommended Alerts** button on the dashboard to configure fleet-wide alerts.

##  August 11, 2020

**Cloud Logging**

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

**Cloud Logging**

**FEATURE:**

Alpha release: You can now use Logs Buckets to centralize or divide your logs
based on your needs. For information about this feature, refer to the [
Managing logs buckets ](https://cloud.google.com/logging/docs/buckets) guide.
To participate in the alpha or to get notified when Logs Buckets goes beta,
fill out the [ sign up form
](https://docs.google.com/forms/d/e/1FAIpQLSeBVpNBivnTAAd4G3rdait9t94uG9TWc07oGwNRGcE071TeCA/viewform)
.

##  July 30, 2020

**Cloud Logging**

**CHANGED:**

The Logs field explorer panel is now generally available (GA). To learn more,
see the [ Logs field explorer section on Logs Viewer (Preview) interface page
](https://cloud.google.com/logging/docs/view/logs-viewer-interface#logs-field-
panel) .

##  July 10, 2020

**Cloud Monitoring**

**FEATURE:**

SLO monitoring for microservices is now Generally Available in the Cloud
Console. This feature lets you create service-level objectives (SLOs) and set
up alerting policies to monitor their performance using auto-generated
dashboards with metrics, logs, and alerts in a single place. For more
information, see [ SLO monitoring
](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring) .

##  July 07, 2020

**Cloud Monitoring**

**CHANGED:**

Monitoring Query Language (MQL) is now Generally Available. MQL is an
expressive, text-based interface to Cloud Monitoring time-series data. With
MQL, you can create charts you can't create any other way. You can access MQL
from both the Cloud Console and the Monitoring API. For more information, see
[ Introduction to Monitoring Query Language
](https://cloud.google.com/monitoring/mql/) .

##  June 30, 2020

**Cloud Logging**

**FEATURE:**

Cloud Logging now contains a Logs Dashboard page that provides a high-level
overview into the health of your systems running within a project. To learn
more, see [ Logs Dashboard
](https://cloud.google.com/logging/docs/view/dashboard) .

##  June 29, 2020

**Cloud Debugger**

**FEATURE:**

Cloud Debugger now lets you canary snapshots and logpoints on your Node.js
applications. To learn more, see the [ Node.js page for setting up Cloud
Debugger ](https://cloud.google.com/debugger/docs/setup/nodejs) .

##  June 17, 2020

**Cloud Debugger**

**FEATURE:**

Cloud Debugger now lets you canary snapshots and logpoints on your Python
applications. To learn more, see the [ Python page for setting up Cloud
Debugger ](https://cloud.google.com/debugger/docs/setup/python) .

##  June 15, 2020

**Cloud Monitoring**

**CHANGED:**

The Service Monitoring API is now Generally Available. You can use this
feature to create services, set service-level objectives (SLOs), and create
alerting policies to monitor your SLOs. See [ Service monitoring
](https://cloud.google.com/monitoring/service-monitoring/) for documentation,
and [ ` services ` ](https://cloud.google.com/monitoring/api/v3/#service-
monitoring) for reference material.

##  June 08, 2020

**Cloud Monitoring**

**FEATURE:**

Enhancements to the pre-configured Compute Engine **VM Instances** dashboard.
Compute Engine cross-fleet metrics and detail views specific to CPU, Disk,
Memory, and Network are now available. Use filters to narrow down the set of
VMs being inspected, and use the time selector or in-chart time selection to
change the time window. VMs with the Monitoring agent installed get detailed
memory and disk analysis out of the box.

##  June 05, 2020

**Cloud Logging**

**CHANGED:**

Custom retention is now generally available (GA). In order to have time to
explore this feature, you won't be charged for extended retention of logs
until March 31, 2021. To learn more, see the [ Logging pricing section on the
Pricing for Google Cloud's operations suite page
](https://cloud.google.com/stackdriver/pricing#logging-costs) .

##  June 03, 2020

**Cloud Logging**

**FEATURE:**

In the Logs Viewer (Preview), you can now save your queries, which can then be
viewed and run from the **Saved** queries tab. For more information, see the [
Saved queries section on the Building queries page
](https://cloud.google.com/logging/docs/view/building-queries#saved-queries) .

##  May 20, 2020

**Cloud Monitoring**

**FEATURE:**

Cloud Monitoring introduces an improved experience for viewing and managing
incidents. Improvements include performance optimizations for Workspaces with
large numbers of incidents, summary statics, and the ability to filter by
alerting policy name, metric type, and resource type. For more information,
see [ Incidents and events
](https://cloud.google.com/monitoring/alerts/incidents-events) .

##  May 19, 2020

**Cloud Debugger**

**FEATURE:**

Cloud Debugger now lets you canary snapshots and logpoints on your Java
applications. To learn more, see the [ Java page for setting up Cloud Debugger
](https://cloud.google.com/debugger/docs/setup/java) .

**Cloud Monitoring**

**CHANGED:**

Alert notifications delivered by email now come from "alerting-
noreply@google.com" instead of "alerts@stackdriver.com".

##  May 18, 2020

**Cloud Logging**

**FEATURE:**

**Logs Viewer** now contains the **Logs field explorer** panel, which lets you
view aggregation-based results for your project's log fields and makes it more
efficient to refine queries. To learn more, go to the [ Logs Viewer (Preview)
page ](https://cloud.google.com/logging/docs/view/logs-viewer-interface) .

##  May 14, 2020

**Cloud Monitoring**

**CHANGED:**

Starting in version 6.0.2, the Cloud Monitoring agent is available for the
Ubuntu LTS 20.04 (Focal Fossa) distribution.

##  May 12, 2020

**Cloud Profiler**

**CHANGED:**

The Cloud Profiler Python agent is now generally available. See [ Profiling
Python applications ](https://cloud.google.com/profiler/docs/profiling-python)
for information on configuring your Python application.

##  May 11, 2020

**Cloud Logging**

**FEATURE:**

You can now use regular expressions to query your logs data and create
filters. For more information, go to [ Using regular expressions
](https://cloud.google.com/logging/docs/view/logging-query-language#regular-
expressions) .

##  May 08, 2020

**Cloud Monitoring**

**FEATURE:**

Monitoring Query Language (MQL) is now available in Beta. MQL is an
expressive, text-based interface to Cloud Monitoring time-series data. With
MQL, you can create charts you can't create any other way. You can access MQL
from both the Cloud Console and the Monitoring API. For more information, see
[ Introduction to Monitoring Query Language
](https://cloud.google.com/monitoring/mql/) .

##  April 28, 2020

**Cloud Monitoring**

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

##  April 27, 2020

**Cloud Logging**

**CHANGED:**

The Logs Viewer (Preview) is now GA. To learn more, go to the [ Logs Viewer
(Preview) Overview page ](https://cloud.google.com/logging/docs/view/logs-
viewer-preview) .

##  April 20, 2020

**Cloud Profiler**

**CHANGED:**

The Cloud Profiler Node.js agent is now generally available. See [ Profiling
Node.js applications ](https://cloud.google.com/profiler/docs/profiling-
nodejs) for information on configuring your Node.js application.

**FEATURE:**

The Cloud Profiler Node.js agent now supports release 12 of Node.js. See [
Profiling Node.js applications
](https://cloud.google.com/profiler/docs/profiling-nodejs) for information on
configuring your Node.js application.

**CHANGED:**

The Cloud Profiler Node.js agent no longer supports release 8 of Node.js.

##  March 30, 2020

**Cloud Monitoring**

**FEATURE:**

You can now write time-series data for custom and Prometheus metrics at the
rate of 1 data point every 10 seconds. This was previously limited to 1 point
every minute.

**CHANGED:**

Data for custom and Prometheus metrics is now retained for 24 months.
Previously, the retention period was 6 weeks.

**Cloud Trace**

**FEATURE:**

You can now use [ OpenTelemetry ](https://opentelemetry.io/) with [ Go
](https://cloud.google.com/trace/docs/setup/go-ot) and [ Node.js
](https://cloud.google.com/trace/docs/setup/nodejs-ot) to instrument your
applications running on GKE and Compute Engine.

##  March 24, 2020

**Cloud Profiler**

**CHANGED:**

Integration of Stackdriver Profiler with Virtual Private Cloud Service
Controls is now Generally Available. For more information, see [ VPC Service
Controls documentation ](https://cloud.google.com/vpc-service-controls/docs/)
.

##  March 17, 2020

**Cloud Logging**

**CHANGED:**

Incoming log entries must have timestamps that don't exceed the [ logs
retention periods
](https://cloud.google.com/logging/quotas#logs_retention_periods) in the past,
and that don't exceed 24 hours in the future. Log entries outside those time
boundaries aren't ingested by Cloud Logging.

##  March 12, 2020

**Cloud Logging**

**CHANGED:**

Cloud Logging Agent for Windows version 1-11 is now available. This version
upgrades ` fluentd ` from 1.4.2 to 1.7.4. Go to [ Installing the Cloud Logging
agent ](https://cloud.google.com/logging/docs/agent/installation) for
information on installing this version of the agent.

##  March 10, 2020

**Cloud Logging**

**FEATURE:**

Logs Viewer (Preview) now contains a histogram panel. The histogram panel lets
you visualize your logs data to more easily spot patterns and troubleshoot
issues. For more information, see [ Using Logs Viewer (Preview)
](https://cloud.google.com/logging/docs/view/logs-viewer-interface) .

##  February 24, 2020

**Cloud Logging**

**FEATURE:**

Beta release: You can now use the new Logs Viewer (Preview) to view, parse and
analyze log data, and refine your query parameters. Go to [ Logs Viewer
interface (Preview) ](https://cloud.google.com/logging/docs/view/logs-viewer-
interface) for more information.

**Cloud Monitoring**

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

##  February 20, 2020

**Cloud Trace**

**CHANGED:**

Integration of Cloud Trace with Virtual Private Cloud Service Controls is now
generally available. For more information, see [ VPC Service Controls
documentation ](https://cloud.google.com/vpc-service-controls/docs/) .

##  February 19, 2020

**Cloud Monitoring**

**FEATURE:**

Starting in version 6.0.0, the Stackdriver Monitoring agent is available for
the Ubuntu 19.10 (Eoan Ermine) distribution.

**Cloud Trace**

**FEATURE:**

[ Beta release ](https://cloud.google.com/products/#product-launch-stages) :
Export of Stackdriver Trace data to BigQuery. For more information, see [
Managing Trace exports ](https://cloud.google.com/trace/docs/trace-export-
overview) .

##  February 18, 2020

**Cloud Monitoring**

**FEATURE:**

Stackdriver Monitoring agent version 6.0.0 is now available for the Debian 9
distribution.

##  February 17, 2020

**Cloud Logging**

**CHANGED:**

BETA: You can now configure the retention periods of your logs data. For more
information, go to [ Storing logs
](https://cloud.google.com/logging/docs/storage) .

##  February 14, 2020

**Cloud Monitoring**

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

**Cloud Monitoring**

**FEATURE:**

Stackdriver Monitoring agent version 6.0.0 has been released to the CentOS 8
distribution.

##  February 06, 2020

**Cloud Monitoring**

**FEATURE:**

Starting in version 6.0.0, the Stackdriver Monitoring agent is available for
the Debian 10 distribution.

**Cloud Trace**

**CHANGED:**

The [ Stackdriver Trace API v2
](https://cloud.google.com/trace/docs/reference) is now Generally Available.

##  January 31, 2020

**Cloud Monitoring**

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

##  January 17, 2020

**Cloud Logging**

**FEATURE:**

Customer-managed encryption keys (CMEK) for the Logs Router are now Generally
Available (GA). CMEK lets you create, control, and manage encryption keys to
meet your data compliance needs. For details, go to [ Enabling customer-
managed encryption keys for Logs Router
](https://cloud.google.com/logging/docs/routing/managed-encryption) .

##  January 13, 2020

**Cloud Monitoring**

**CHANGED:**

Stackdriver Monitoring in the Cloud Console is Generally Available and is the
default option. For a limited period of time, you also have the option to use
the classic Stackdriver Monitoring Console. Your configuration information,
such as uptime checks and alerting policies, is accessible and changeable,
from the Cloud Console and from the classic Stackdriver Monitoring Console.
For more information, see [ Monitoring in the GCP Console
](https://cloud.google.com/monitoring/docs/monitoring_in_console) .

##  December 16, 2019

**Cloud Logging**

**FEATURE:**

GA release: You can now use partitioned tables for logs exports to BigQuery.
For details, go to [ Partitioned tables
](https://cloud.google.com/logging/docs/export/bigquery#partition-tables) .

**Cloud Trace**

**FEATURE:**

Integration of Stackdriver Trace with Virtual Private Cloud Service Controls
is now beta. For more information, see [ VPC Service Controls documentation
](https://cloud.google.com/vpc-service-controls/docs/) .

##  December 13, 2019

**Cloud Logging**

**CHANGED:**

Google Kubernetes Engine (GKE) version 1.15, which is now generally available,
drops support for GKE versions 1.12 and earlier. As a result, the beta version
of Stackdriver Kubernetes Engine Monitoring is no longer supported. If your
GKE clusters are running version 1.12 or earlier, then you must upgrade them
as soon as possible.

**Cloud Monitoring**

**CHANGED:**

Google Kubernetes Engine (GKE) version 1.15, which is now generally available,
drops support for GKE versions 1.12 and earlier. As a result, the beta version
of Stackdriver Kubernetes Engine Monitoring is no longer supported. If your
GKE clusters are running version 1.12 or earlier, then you must upgrade them
as soon as possible.

**Cloud Profiler**

**FEATURE:**

Strackdriver Profiler supports Istio on Google Kubernetes Engine for [ Go
](https://cloud.google.com/profiler/docs/profiling-go) , [ Java
](https://cloud.google.com/profiler/docs/profiling-java) , [ Python
](https://cloud.google.com/profiler/docs/profiling-python) , and [ Node.js
](https://cloud.google.com/profiler/docs/profiling-nodejs) services. This
feature is now in **Beta** .

**Error Reporting**

**CHANGED:**

Error Reporting now infers the service name and version from the ` logEntry `
fields named ` k8s-pod/serving_knative_dev/service ` and `
k8s-pod/serving_knative_dev/revision ` for Knative Serving labels on Cloud Run
on Google Kubernetes Engine. This replaces the current default value of `
gke_instances ` for service name.

##  December 11, 2019

**Cloud Logging**

**DEPRECATED:**

Legacy Stackdriver support for Google Kubernetes Engine (GKE) is deprecated.
If you're using Legacy Stackdriver, then you must [ migrate to Stackdriver
Kubernetes Engine Monitoring ](https://cloud.google.com/monitoring/kubernetes-
engine/migration) before Legacy Stackdriver is decommissioned. For more
information, see [ Legacy Stackdriver support for GKE deprecation
](https://cloud.google.com/stackdriver/docs/deprecations/legacy) .

**Cloud Monitoring**

**DEPRECATED:**

Legacy Stackdriver support for Google Kubernetes Engine (GKE) is deprecated.
If you're using Legacy Stackdriver, then you must [ migrate to Stackdriver
Kubernetes Engine Monitoring ](https://cloud.google.com/monitoring/kubernetes-
engine/migration) before Legacy Stackdriver is decommissioned. For more
information, see [ Legacy Stackdriver support for GKE deprecation
](https://cloud.google.com/stackdriver/docs/deprecations/legacy) .

##  December 10, 2019

**Cloud Profiler**

**FEATURE:**

Integration of Stackdriver Profiler with Virtual Private Cloud Service
Controls is now beta. For more information, see [ VPC Service Controls
documentation ](https://cloud.google.com/vpc-service-controls/docs/) .

##  December 09, 2019

**Cloud Monitoring**

**FEATURE:**

The Stackdriver Monitoring Dashboard API is now in Beta release. You can use
this feature to programmatically manage your dashboards and charts. See [
Managing dashboards by API
](https://cloud.google.com//monitoring/dashboards/api-dashboard) for
documentation, and [ ` Dashboard `
](https://cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards)
for reference material.

##  December 04, 2019

**Cloud Monitoring**

**FEATURE:**

Stackdriver Monitoring in the Cloud Console is in beta release. Your
configuration information, such as uptime checks and alerting policies, is
accessible and changeable, from the Cloud Console and from the classic
Stackdriver Monitoring Console. For more information about the beta, see [
Monitoring in the GCP Console
](https://cloud.google.com/monitoring/docs/monitoring_in_console) .

##  November 20, 2019

**Cloud Trace**

**FEATURE:**

The **Trace list** page has a new menu-driven filtering solution that is in
Beta release testing. For more information, see [ Finding and viewing traces
](https://cloud.google.com/trace/docs/finding-traces) .

##  November 18, 2019

**Cloud Logging**

**FEATURE:**

Customer-managed encryption keys (CMEK) for the Logs Router are now available
in Beta. CMEK lets you create, control, and manage encryption keys to meet
your data compliance needs. For details, go to [ Enabling customer-managed
encryption keys for Logs Router
](https://cloud.google.com/logging/docs/routing/managed-encryption) .

##  November 14, 2019

**Cloud Monitoring**

**FEATURE:**

The Service Monitoring API is now in Beta release. You can use this feature to
create services, set service-level objectives (SLOs), and create alerting
policies to monitor your SLOs. See [ Service monitoring
](https://cloud.google.com/monitoring/service-monitoring/) for documentation,
and [ ` services ` ](https://cloud.google.com/monitoring/api/v3/#service-
monitoring) for reference material.

##  November 12, 2019

**Cloud Debugger**

**FEATURE:**

[ Stackdriver Debugger ](https://cloud.google.com/debugger/docs) has an
updated and expanded quickstart guide showing how to install the agent and
debug an app while it's in production. See the [ Debugger Quickstart guide
](https://cloud.google.com/debugger/docs/quickstart) for more information.

##  September 20, 2019

**Cloud Logging**

**FEATURE:**

Beta release: Stackdriver Logging now offers partitioned tables for exports to
BigQuery. For details, go to [ Partitioned tables
](https://cloud.google.com/logging/docs/export/bigquery#partition-tables) .

##  September 10, 2019

**Cloud Logging**

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

**Cloud Monitoring**

**CHANGED:**

When creating a new Google Kubernetes Engine (GKE) cluster, Stackdriver
Kubernetes Engine Monitoring is now the default Stackdriver support option.
This is a change from prior versions where Stackdriver Logging and Stackdriver
Monitoring were the default Stackdriver support option. For more information,
see [ Overview of Stackdriver support for GKE
](https://cloud.google.com/monitoring/kubernetes-engine/) .

##  August 08, 2019

**Cloud Monitoring**

**FEATURE:**

[ Stackdriver Monitoring ](https://cloud.google.com/monitoring/uptime-checks)
has two new uptime check features: SSL certificate validation and regex
negation content matching.

##  July 31, 2019

**Cloud Debugger**

**FEATURE:**

**Cloud Run** and **Cloud Run on GKE** : Stackdriver Debugger can now be used
to debug applications on Cloud Run and Cloud Run on GKE that are written in [
Node.js ](https://cloud.google.com/debugger/docs/setup/nodejs) , [ Python
](https://cloud.google.com/debugger/docs/setup/python) , and [ Java
](https://cloud.google.com/debugger/docs/setup/java) .

##  May 21, 2019

**Cloud Logging**

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

**Cloud Monitoring**

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

##  May 08, 2019

**Cloud Profiler**

**FEATURE:**

Java 11 is now supported. For more information, see [ Profiling Java
](https://cloud.google.com/profiler/docs/profiling-java) .

**Error Reporting**

**FEATURE:**

**API**

Error events written as instances of [ ` ReportedErrorEvent `
](https://cloud.google.com/error-
reporting/reference/rest/v1beta1/projects.events/report#ReportedErrorEvent)
generate properly formatted error messages in Stackdriver Logging.

##  May 02, 2019

**Cloud Monitoring**

**FEATURE:**

Stackdriver Workspace creation is now a one-step operation. For more
information, go to [ Getting a Workspace quickly
](https://cloud.google.com/monitoring/workspaces/manage#single-project-ws) .

##  April 23, 2019

**Cloud Logging**

**CHANGED:**

The maximum size of a log entry has been increased to 256 KB from 100 KB. For
details on logging usage limits, go to [ Quotas and limits
](https://cloud.google.com/logging/quotas) .

**Cloud Monitoring**

**FEATURE:**

The OpenCensus library is now generally available as the official library for
user-defined metrics in Stackdriver Monitoring. The [ Custom metrics with
OpenCensus ](https://cloud.google.com/monitoring/custom-metrics/open-census)
page includes samples in Go, Java, Node.js, and Python.

##  April 15, 2019

**Cloud Logging**

**FEATURE:**

A new Windows version (v1-9) of the Stackdriver Logging agent is now
available. The new version saves the agent service logs on disk for easier
troubleshooting and supports the ` config.d ` configuration extension
directory.

##  March 26, 2019

**Cloud Profiler**

**FEATURE:**

Stackdriver Profiler is now generally available. Stackdriver Profiler lets you
analyze and understand the performance of your Go, Java, Node.js or Python
applications. For more information, see [ About Stackdriver Profiler
](https://cloud.google.com/profiler/docs/about-profiler) .

##  March 18, 2019

**Cloud Monitoring**

**FEATURE:**

The [ Uptime Configuration API
](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs)
is now complete and GA. The API, part of the [ Stackdriver Monitoring API
](https://cloud.google.com/monitoring/api/ref_v3/rest/) , lets you create,
edit and manage [ uptime checks ](https://cloud.google.com/monitoring/uptime-
checks/) .

##  March 15, 2019

**Cloud Logging**

**CHANGED:**

Stackdriver agents are subject to an updated [ deprecation policy
](https://cloud.google.com/stackdriver/docs/agent-deprecation-policy) . As
part of this transition, the next major version of the Stackdriver Monitoring
and Stackdriver Logging agents will stop supporting operating systems that are
at the end of their lifecycle, as well as some [ third-party agent plugins
](https://cloud.google.com//monitoring/agent/plugins/) .

**Cloud Monitoring**

**CHANGED:**

Stackdriver agents are subject to an updated [ deprecation policy
](https://cloud.google.com/stackdriver/docs/agent-deprecation-policy) . As
part of this transition, the next major version of the Stackdriver Monitoring
and Stackdriver Logging agents will stop supporting operating systems that are
at the end of their lifecycle, as well as some [ third-party agent plugins
](https://cloud.google.com/monitoring/agent/plugins/) .

##  March 12, 2019

**Cloud Profiler**

**FEATURE:**

Python is now supported. For more information, see [ Profiling Python
](https://cloud.google.com/profiler/docs/profiling-python) .

##  February 28, 2019

**Cloud Profiler**

**FEATURE:**

The new **Color mode** filter option lets you color the flame graph frames by
package name, by the metric consumption of the function, or by the metric
consumption of the function and its children. For more information, see [
Color mode ](https://cloud.google.com/profiler/docs/filtering-profiles#color-
filter) .

##  February 22, 2019

**Cloud Logging**

**CHANGED:**

You now have two choices for the access control model when creating a Cloud
Storage bucket: bucket-only (new) and object-level. Select **Set object-level
and bucket-level permissions** as the access control model during bucket
creation if you intend to use the bucket as a sink destination. See [ Errors
exporting to Cloud Storage
](https://cloud.google.com/logging/docs/export/configure_export_v2#errors_exporting_to_cloud_storage)
for details.

##  February 08, 2019

**Cloud Monitoring**

**FEATURE:**

The Stackdriver Monitoring Agent now supports Ubuntu 18.04 LTS ("Bionic
Beaver").

##  January 22, 2019

**Cloud Logging**

**CHANGED:**

In the Stackdriver Logging API, log sinks, metrics, and exclusions have two
new output-only fields: create time and last update time. See [ LogSink
](https://cloud.google.com/logging/docs/reference/v2/rest/v2/sinks) for an
example. If this information isn't available for older resources, these fields
aren't present.

##  January 18, 2019

**Error Reporting**

**FEATURE:**

**Error detection for Python applications** has been improved. You might see
more newly detected error groups or receive more notifications.

##  December 18, 2018

**Cloud Trace**

**CHANGED:**

Trace list now limits HTTP method and HTTP status matches to trace root spans.
See [ Filter traces ](https://cloud.google.com/trace/docs/finding-
traces#filter_traces) for more details.

**FEATURE:**

You can now filter traces for analysis reports by the full URI, by the URI
prefix, or by using trace filter. See [ Create a new analysis report
](https://cloud.google.com/trace/docs/analysis-
reports#create_a_new_analysis_report) for details.

##  December 07, 2018

**Cloud Profiler**

**FEATURE:**

Go 1.11 for App Engine standard environment is now supported. For more
information, see [ Profiling Go
](https://cloud.google.com/profiler/docs/profiling-go) .

##  December 06, 2018

**Cloud Monitoring**

**CHANGED:**

A mechanism to collect monitoring data from Prometheus clients, which can be
deployed as a sidecar in the same Kubernetes pod as a working Prometheus
server, is now available. See [ Using Prometheus
](https://cloud.google.com/monitoring/kubernetes-engine/prometheus) for more
information.

##  December 05, 2018

**Cloud Monitoring**

**FEATURE:**

Documentation for using [ OpenCensus ](https://opencensus.io) to capture
custom metrics in Java applications is now available. See [ Custom metrics
with OpenCensus ](https://cloud.google.com/monitoring/custom-metrics/open-
census) for more information.

##  December 03, 2018

**Cloud Logging**

**FEATURE:**

The Logs Viewer has a new option to display a log entry in its resource
context. It can also pin a log entry while allowing you to change the display
context. See [ Viewing Logs
](https://cloud.google.com/logging/docs/view/overview) for details.

##  November 16, 2018

**Cloud Monitoring**

**CHANGED:**

The new UI for creating alerting policies is now complete and Generally
Available. This interface, based on Metrics Explorer, offers fine-grained
control over the selection of the metrics used in alerting conditions. See [
Managing Alerting Policies ](https://cloud.google.com/monitoring/alerts/using-
alerting-ui) for more information.

##  November 01, 2018

**Cloud Logging**

**FEATURE:**

You can now view error and success metrics for your log sinks using [ export
system metrics ](https://cloud.google.com/logging/docs/logs-based-
metrics#system_logs-based_metrics) .

##  October 31, 2018

**Cloud Trace**

**CHANGED:**

Stackdriver Trace enforces consumption-based pricing as of November 1, 2018 at
00:00 PDT. For more information, see [ Stackdriver Pricing
](https://cloud.google.com/stackdriver/pricing) .

**CHANGED:**

On November 1, 2018, Stackdriver Trace begins enforcing a daily trace spans
ingestion quota. See [ Stackdriver Trace Quotas & Limits
](https://cloud.google.com/trace/docs/quotas) for details.

##  October 19, 2018

**Cloud Logging**

**FEATURE:**

You can now link from certain App Engine request logs to a detailed trace that
explains the request's latency. You can also filter log entries according to
their latencies, and if they contain detailed trace data viewable by
Stackdriver Trace. See [ Viewing latency in Trace
](http://cloud.google.com/logging/docs/view/overview#show-latency) for
details.

##  October 10, 2018

**Cloud Monitoring**

**FEATURE:**

A new UI for creating alerting policies is available in Beta. This interface,
based on Metrics Explorer, offers fine-grained control over the selection of
the metrics used in alerting conditions. See [ Managing Alerting Policies
](https://cloud.google.com/monitoring/alerts/using-alerting-ui) for more
information.

##  October 01, 2018

**Cloud Logging**

**FEATURE:**

The Logs Viewer can now download up to 300 log entries in JSON or CSV format.
See [ Viewing Logs ](https://cloud.google.com/logging/docs/view/overview) for
details.

##  September 19, 2018

**Cloud Monitoring**

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

**Cloud Monitoring**

**FEATURE:**

The legends for Stackdriver charts have been significantly improved. Legends
now support more than one labeled column. The legend provides a selected set
of columns as a default, but users can choose the columns they want to see in
the legend. All columns are sortable. The legend detects a configuration of
columns that exceeds the available space, and provides scrollbars. The
resizing of the legends is also improved. For details, see [ Configuring
Legends ](https://cloud.google.com/monitoring/charts/working-with-legends) .

##  September 14, 2018

**Cloud Logging**

**FEATURE:**

The format of service account names for older log [ sinks
](https://cloud.google.com/logging/docs/export/#sink-terms) is being changed
so that all log sinks will have consistent service account names. This naming
format has already been applied to project-level sinks on BigQuery, Cloud
Pub/Sub, and Cloud Storage permission pages. In the coming weeks, this naming
format will be applied to organization-level sinks and folder-level sinks, and
to sinks listed on the **Logs Exports** page in the Logs Viewer. There are no
associated changes to functionality or granted permissions.

##  September 10, 2018

**Cloud Monitoring**

**CHANGED:**

"Stackdriver accounts" have been renamed "Workspaces" to reflect their use as
a "single pane of glass" through which you view resources from multiple
projects and AWS accounts. There is no change in their functionality, but we
have improved the documentation for them. For more information, see [
Workspaces ](https://cloud.google.com/monitoring/workspaces/) .

##  September 05, 2018

**Cloud Logging**

**FEATURE:**

**Access Transparency** logging is now Generally Available. See [ Overview of
Access Transparency ](https://cloud.google.com/logging/docs/audit/access-
transparency-overview) for details.

**Cloud Trace**

**FEATURE:**

Billing enforcement for Trace has been postponed to November 1, 2018, rather
than the previously announced date of September 30, 2018. You can now estimate
your bill for your usage of Trace, according to the new pricing and in advance
of billing enforcement. See [ Estimating your bills
](https://cloud.google.com/stackdriver/estimating-bills) for details.

##  August 02, 2018

**Cloud Profiler**

**FEATURE:**

The new **Weight** filter lets you select and graph profiles that consume the
most of the profile's measured metric. For more information, see [ Weight
filter ](https://cloud.google.com/profiler/docs/selecting-profiles#weight-
filter) .

##  July 25, 2018

**Cloud Logging**

**CHANGED:**

Audit logs exports to BigQuery now feature a compact format. On March 1, 2019,
the older extended format will be removed.

##  July 24, 2018

**Cloud Profiler**

**FEATURE:**

The new **Compare To** option lets you compare profiles that differ by end
time, zone, or service version. For more information, see [ Comparing profiles
](https://cloud.google.com/profiler/docs/comparing-profiles) .

##  June 29, 2018

**Cloud Logging**

**CHANGED:**

On July 1, 2018 at 00:00 PDT, Stackdriver switches to consumption-based
pricing. For more information, see [ Stackdriver Pricing
](https://cloud.google.com/stackdriver/pricing_v2) .

**Cloud Monitoring**

**CHANGED:**

On July 1, 2018 at 00:00 PDT, Stackdriver switches to consumption-based
pricing. For more information, see [ Stackdriver Pricing
](https://cloud.google.com/stackdriver/pricing_v2) .

##  June 26, 2018

**Cloud Logging**

**FEATURE:**

You can now immediately disable all logs ingestion. For instructions, see [
Stopping all logs ingestion
](https://cloud.google.com/logging/docs/exclusions#stop-logs) .

##  June 19, 2018

**Cloud Logging**

**FEATURE:**

Google Cloud Storage logs streaming time has been reduced from 12 hours to 3
hours. For details, see [ Using Exported Logs
](https://cloud.google.com/logging/docs/export/using_exported_logs#gcs-
availability) .

**Cloud Monitoring**

**FEATURE:**

If you want to minimize the **AWS permissions** you give to Stackdriver, then
see [ Minimal AWS Permissions
](https://cloud.google.com/monitoring/support/minimal-aws-permissions) .

##  June 18, 2018

**Cloud Logging**

**CHANGED:**

**Between June 18, 2018 at 06:00 PDT and July 1, 2018 at 00:00 PDT, your use
of Stackdriver is free** . The service tiers have been removed, and you can
experience all features without incurring costs. Thereafter, Stackdriver
switches to consumption-based pricing. For more information, see [ Upcoming
Pricing ](https://cloud.google.com/stackdriver/pricing_v2) .

**Cloud Monitoring**

**CHANGED:**

**Between June 18, 2018 at 06:00 PDT and July 1, 2018 at 00:00 PDT, your use
of Stackdriver is free** . The service tiers have been removed, and you can
experience all features without incurring costs. Thereafter, Stackdriver
switches to consumption-based pricing. For more information, see [ Upcoming
Pricing ](https://cloud.google.com/stackdriver/pricing_v2) .

##  June 12, 2018

**Cloud Logging**

**FEATURE:**

You can now enable and configure your Data Access audit logs using the GCP
console. For details, see [ Configuring Data Access logs
](https://cloud.google.com/logging/docs/audit/configure-data-access) .

##  May 24, 2018

**Cloud Monitoring**

**CHANGED:**

Any Stackdriver free trials created after May 29, 2018 will expire on June 30,
2018. After June 30, 2018, free trials will be replaced with a free monthly
allocation of logs and metrics. For more information about Stackdriver's new
consumption-based pricing, see [ Stackdriver Upcoming Pricing
](https://cloud.google.com/stackdriver/pricing_v2) .

##  May 23, 2018

**Cloud Monitoring**

**CHANGED:**

Custom dashboards and pages for resource groups are now limited to 25 charts.
Any dashboards or groups pages with more than 25 charts will continue to work,
but you will not be able to add additional charts to them.

##  May 22, 2018

**Cloud Monitoring**

**FEATURE:**

You can now see your Monitoring usage metrics and estimate your bill for your
usage of Monitoring, according to the new Stackdriver pricing and in advance
of billing enforcement. See [ Estimating your bills
](https://cloud.google.com/stackdriver/estimating-bills) for details.

##  May 21, 2018

**Cloud Monitoring**

**FEATURE:**

A new UI for creating conditions in alerting policies is available in Beta.
This UI, based on Metrics Explorer, offers fine-grained control over the
selection of the metrics used in alerting conditions. See [ Managing Alerting
Policies ](https://cloud.google.com/monitoring/alerts/using-alerting-ui) for
more information.

##  May 17, 2018

**Cloud Logging**

**FEATURE:**

You can now see your Logging usage and estimate your bill according to the new
Stackdriver pricing and in advance of billing enforcement. See [ Estimating
your bills ](https://cloud.google.com/stackdriver/estimating-bills) for
details.

##  May 15, 2018

**Cloud Profiler**

**FEATURE:**

The new **Focus** filter lets you analyze the aggregate resource consumption
of a specific function and the proportion of time spent in the function by
different callers. For more information, see [ Using the **Focus** Filter
](https://cloud.google.com/profiler/docs/filtering-profiles#focus-filter) .

##  May 11, 2018

**Cloud Monitoring**

**CHANGED:**

If you are using custom IAM roles, any roles that load Stackdriver Monitoring
dashboards now require additional IAM permissions. The `
monitoring.dashboards.* ` and ` monitoring.publicWidgets.* ` permissions are
now public, and custom roles used to load dashboards must now include them.
See [ Stackdriver Monitoring Access Control
](https://cloud.google.com/monitoring/access-control#roles) for more
information.

##  May 08, 2018

**Cloud Logging**

**FEATURE:**

You can now specify custom fields in your Logs Viewer log-entry summary lines.
See [ Add custom fields
](https://cloud.google.com/logging/docs/view/overview#custom-fields) for
details.

##  May 02, 2018

**Cloud Logging**

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

**Cloud Monitoring**

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

**Cloud Monitoring**

**CHANGED:**

You can now use variables in the documentation associated with alerting
policies to pull specific details about the alert into notifications, to
create playbook information for responders. See [ Additional documentation
tools ](https://cloud.google.com/monitoring/alerts/doc-variables) for more
information. The Webhooks and Slack notification channels now receive a copy
of this enhanced documentation as part of alert notifications. Additionally,
email notifications from alerting policies now use HTML-formatted messages.

##  April 19, 2018

**Cloud Monitoring**

**FEATURE:**

Boolean metrics can now be queried and charted.

##  April 17, 2018

**Cloud Monitoring**

**CHANGED:**

The [ Using Alerting Policies ](https://cloud.google.com/monitoring/alerts)
documentation has been updated to provide additional guides and links to
sample code for managing alerting policies and notification channels
programmatically. The update also removes some obsolete service-tier
information.

##  April 10, 2018

**Cloud Logging**

**FEATURE:**

You can now specify that the Stackdriver Logging agent converts your payloads
to JSON format for certain log inputs. For details on enabling this feature,
see [ Structured Logging ](https://cloud.google.com/logging/docs/structured-
logging) .

##  April 04, 2018

**Cloud Trace**

**FEATURE:**

The Trace Viewer now allows you to view trace spans for related Google Cloud
Platform projects in one view. See [ Viewing traces across projects
](https://cloud.google.com/trace/docs/cross-project-traces) for details.

##  March 28, 2018

**Cloud Monitoring**

**CHANGED:**

Stackdriver now loads charts much more quickly, especially when the chart
contains a long time span.

**Cloud Profiler**

**FEATURE:**

Stackdriver Profiler is released in Beta.

**Cloud Trace**

**FEATURE:**

Stackdriver Trace Data Access audit logs are now Generally Available. See [
Stackdriver Trace Audit Logging ](https://cloud.google.com/trace/docs/audit-
logging) for details.

##  March 26, 2018

**Cloud Monitoring**

**CHANGED:**

A new option on the Dashboards menu, **Public Charts** , lets you see a list
of all the shared charts. You can also use this page to remove sharing from a
chart. The on-chart indicator that the chart is shared has been removed.

##  March 12, 2018

**Cloud Logging**

**CHANGED:**

Beginning on June 30, 2018, Stackdriver is switching to consumption-based
pricing, including revised quotas. For more information, see [ Stackdriver
Upcoming Pricing ](https://cloud.google.com/stackdriver/pricing_v2) .

**FEATURE:**

Logging data retention has been increased to 30 days for all projects.

**Cloud Monitoring**

**CHANGED:**

Beginning on June 30, 2018, Stackdriver is switching to consumption-based
pricing, including revised quotas. For more information, see [ Stackdriver
Upcoming Pricing ](https://cloud.google.com//stackdriver/pricing_v2) .

**Cloud Trace**

**CHANGED:**

Beginning on June 30, 2018, Stackdriver is switching to consumption-based
pricing, including revised quotas. For more information, see [ Stackdriver
Upcoming Pricing ](https://cloud.google.com/stackdriver/pricing_v2) .

##  March 08, 2018

**Cloud Monitoring**

**FEATURE:**

The ` AlertPolicy ` and ` NotificationChannels ` APIs are now in Beta release.
See [ Alerting policies
](https://cloud.google.com/monitoring/api/v3/#alerting-policies) and [
Notification channels
](https://cloud.google.com/monitoring/api/v3/#notification-channels) for more
information.

##  February 27, 2018

**Cloud Trace**

**FEATURE:**

The Trace Viewer now associates logs entries with trace spans when the
LogEntry ` span_id ` field is specified. See [ Integrating with Cloud Logging
](https://cloud.google.com/trace/docs/trace-log-integration) for details.

**FIXED:**

The Trace Viewer now follows your scroll through the span details page, making
it easier to see span details of large traces.

##  February 01, 2018

**Cloud Logging**

**FEATURE:**

The Logging agent now supports partial success for logs ingestion. Any invalid
log entries in a full set will be dropped, and the valid log entries now will
be successfully ingested into the Stackdriver Logging API; previously, the
full set would have been dropped if it contained any invalid log entries. To
enable partial success, upgrade your Logging agent to [ google-fluentd v1.5.27
](https://github.com/GoogleCloudPlatform/google-fluentd/releases/tag/v1.5.27)
.

##  January 29, 2018

**Cloud Monitoring**

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

**Cloud Monitoring**

**CHANGED:**

The name of the Monitoring agent process on Windows has been updated. It now
shows up in the system process list as ` StackdriverMonitoring ` .

##  January 12, 2018

**Cloud Trace**

**FEATURE:**

The Trace viewer now shows sub-millisecond resolution for Trace spans.

##  January 09, 2018

**Cloud Trace**

**FEATURE:**

The Trace viewer now displays span annotations and message events written with
the [ Stackdriver Trace API v2
](https://cloud.google.com/trace/docs/reference/v2/rest/) . See [ Viewing
Trace Details ](https://cloud.google.com/trace/docs/viewing-
details#annotating_spans) for more information.

##  January 08, 2018

**Cloud Monitoring**

**CHANGED:**

The performance of the Monitoring dashboards and charts has been improved.
Additionally, a new version of Metrics Explorer is available, and the metric-
selection interface has been greatly improved, allowing arbitrary label
filtering and group-by functionality. This interface is also used for creating
dashboard charts, making the process consistent across the two tasks. See [
Using Charts ](https://cloud.google.com/monitoring/charts) for more
information.

##  December 19, 2017

**Error Reporting**

**FEATURE:**

**Resolution Status** features are now Generally Available. You can now assign
a status to your error groups, making it easier to triage errors.

##  December 14, 2017

**Cloud Monitoring**

**CHANGED:**

**Alerting events page** : An updated implementation has required some user
interface changes. The alerting events page ( **Alerting > Events ** ) no
longer shows a heatmap or counts of events in each category.

##  December 13, 2017

**Cloud Logging**

**FEATURE:**

Filtering logs by **time range** is now available in the Logs Viewer. For more
information, see [ Scroll to a time
](https://cloud.google.com/logging/docs/view/overview#scroll-to-time) .

##  December 04, 2017

**Cloud Logging**

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

**Cloud Logging**

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

##  November 08, 2017

**Cloud Monitoring**

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

**Cloud Monitoring**

**DEPRECATED:**

Documentation for the deprecated Cloud Monitoring API v2 has been removed. The
API was turned down in August, 2017.

##  November 03, 2017

**Cloud Debugger**

**CHANGED:**

**Compute Engine (Go)** : The support for Go applications on Compute Engine VM
instances is in Beta release. Your Go applications should be compiled without
the default optimizations, or else Stackdriver Debugger might show incorrect
information about your application.

##  November 01, 2017

**Cloud Logging**

**CHANGED:**

**Pricing changes** : Billing for logs overages will begin **March 31, 2018**
. This date extends the one that was previously communicated to give
Stackdriver customers more time to apply the [ exclusion filters
](https://cloud.google.com/logging/docs/exclusions) feature to control which
logs are stored in Logging. Billing for custom and user-defined logs-based
metrics is still postponed. For more information, see [ Stackdriver Pricing
](https://cloud.google.com/stackdriver/pricing) .

##  October 31, 2017

**Cloud Trace**

**FEATURE:**

The [ Stackdriver Trace API v2
](https://cloud.google.com/trace/docs/reference/v2/rest/) is now in Beta
release. For a comparison of the v1 and v2 APIs, see [ Stackdriver Trace API
](https://cloud.google.com/trace/docs/reference) .

##  October 30, 2017

**Cloud Logging**

**FEATURE:**

**Exclusion filters** are now Generally Available. For more information, see [
Excluding Logs ](https://cloud.google.com/logging/docs/exclusions) , and the
**Resource Usage** page in the Logs Viewer.

##  October 24, 2017

**Cloud Logging**

**CHANGED:**

The **` gcloud logging ` command group ** is now generally available. ` gcloud
beta logging ` will be removed at the end of December 2017. For more
information, see [ gcloud logging
](https://cloud.google.com/sdk/gcloud/reference/logging/) .

##  October 19, 2017

**Cloud Monitoring**

**FEATURE:**

Beta release: The Monitoring agent can now export collectd and statsd metrics
as Stackdriver [ custom metrics ](https://cloud.google.com/monitoring/custom-
metrics/) . For more information, see [ Custom Metrics from the Agent
](https://cloud.google.com/monitoring/agent/custom-metrics-agent) and the
agent's [ StatsD plugin
](https://cloud.google.com/monitoring/agent/plugins/statsd)

##  October 17, 2017

**Cloud Monitoring**

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

**Cloud Monitoring**

**FIXED:**

Calls to [ createTimeSeries
](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create)
now fail without writing any data points if the request includes more than one
point in the same time series. Formerly, in some cases, one data point would
be written in each time series and a status of 500 would be returned by the
call.

**Cloud Trace**

**FEATURE:**

The Trace viewer now shows parent-child relationships between trace spans. You
can expand or collapse the parent spans. See [ Viewing Trace Details
](https://cloud.google.com/trace/docs/viewing-details) for more information.

##  September 13, 2017

**Cloud Monitoring**

**CHANGED:**

**Object Stores Resources** : Google Cloud Storage metrics and Amazon S3
metrics are now separated in the Stackdriver UI into their own service
dashboards. The "Object Stores" dashboard is replaced by "Cloud Storage" or
"S3", depending on which service you are using.

##  September 12, 2017

**Cloud Logging**

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

##  September 08, 2017

**Cloud Monitoring**

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

##  August 31, 2017

**Cloud Logging**

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

**Cloud Logging**

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

**Cloud Monitoring**

**FEATURE:**

**Dashboard filtering** : Custom dashboards and resource list pages now
support filtering on groups. Each page that supports filtering now has a
filter bar under the header where you specify the group.

##  August 01, 2017

**Cloud Trace**

**FEATURE:**

The Trace Viewer now allows you to view associated log entries in line with
trace spans and links to VM logs for Google Cloud Load Balancer spans. See the
[ Integrating with Cloud Logging ](https://cloud.google.com/trace/docs/trace-
log-integration) .

##  July 10, 2017

**Cloud Logging**

**FEATURE:**

**IAM support** for Logging now includes custom roles. For more information,
see Logging [ Access Control ](https://cloud.google.com/logging/docs/access-
control) .

**CHANGED:**

**API Migration** . Information about the deprecated v1 API is being removed
from general documentation. Note: Obsolete link to migration information
removed on December 13, 2017. For updated information, see [ APIs & Reference
](https://cloud.google.com/logging/docs/apis) .

**Cloud Monitoring**

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

**Cloud Logging**

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

**Cloud Monitoring**

**FEATURE:**

**Uptime checks** have a new overview and detail dashboards. See [ Uptime
Checks ](https://cloud.google.com/monitoring/alerts/uptime-checks) .

**FEATURE:**

**Singapore region support** : Stackdriver now supports the Singapore region,
` asia-southeast1 ` .

**Cloud Trace**

**FEATURE:**

**Advanced trace filters** : The Trace List page and Trace API now allow
filtering traces by custom labels, latencies, child spans, and methods in
addition to URIs. See [ Trace Filters
](https://cloud.google.com/trace/docs/trace-filters) .

**Error Reporting**

**FEATURE:**

**IAM roles** : Stackdriver Error Reporting IAM roles are now available. See [
Error Reporting IAM roles ](https://cloud.google.com/error-
reporting/docs/iam#iam_roles) .

##  May 01, 2017

**Cloud Logging**

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

**Cloud Monitoring**

**FEATURE:**

New metric and resource types: There are new Cloud Platform metric and
resource types, including those for Cloud Bigtable, Cloud Dataflow, Cloud DNS,
Cloud Internet of Things, Cloud Pub/Sub, Cloud Spanner, and Stackdriver
Logging. Microsoft Windows system and application metrics ( ` iis ` , ` mssql
` , ` pagefile ` ) are available as Agent metrics and can be used for charting
and alerting.

**Error Reporting**

**FEATURE:**

**Error filters** : You can now filter errors by custom text in addition to
filtering by time, service, and version.

##  April 02, 2017

**Cloud Monitoring**

**ISSUE:**

**v2beta2 API turndown** : The deprecated v2beta1 and v2beta2 APIs will be
shut down during August 2017.

##  April 01, 2017

**Cloud Logging**

**FEATURE:**

**Resource types** : Several new resource types are added, including types for
Cloud Bigtable, Cloud Dataflow, and Cloud Container Engine.

##  March 31, 2017

**Cloud Logging**

**CHANGED:**

**V1 API turndown** : The date of the v1 API turndown has changed. See the
release note for May 2017.

**CHANGED:**

**Logging agent for Windows** : If you install the Logging agent on VM
instances running Microsoft Windows, be aware that there are restrictions on
the folders used for the installer and the installed agent. For details, [
Installing on Linux and Windows
](https://cloud.google.com/logging/docs/agent/installation#joint-install) .

**Cloud Monitoring**

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

**Cloud Logging**

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

**Cloud Monitoring**

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

**Cloud Trace**

**FEATURE:**

**Zipkin tracer compatibility** : Stackdriver Trace is now compatible with
Zipkin tracers. For more information, see this [ blog post
](https://cloudplatform.googleblog.com/2016/12/Stackdriver-Trace-Zipkin-
distributed-tracing-and-performance-analysis-for-everyone.html) .

**FEATURE:**

**Scatter plots** : We've added a new scatter-plot selection tool to the
Stackdriver Trace UI. This lets you more quickly identify, view, and compare
interesting traces.

##  January 18, 2017

**Cloud Monitoring**

**FEATURE:**

**New AWS regions** : Monitoring now supports the AWS Canada ( **ca-
central-1** ) and London ( **eu-west-2** ) regions.

##  December 12, 2016

**Cloud Logging**

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

**Cloud Monitoring**

**FEATURE:**

**Account IDs in URLs** : Monitoring has added the Stackdriver account ID to
its URLs. You can now open multiple tabs for different accounts and more
easily share links with coworkers. URLs without the account ID use the most
recently accessed Stackdriver account.

##  December 08, 2016

**Cloud Monitoring**

**FEATURE:**

**Incident pages** (Beta): See **Alerting > Incidents ** . Each open incident
now has a detail page that collects a graph of the incident, links to affected
resources, and the comments made on the incident.

**FEATURE:**

**Metrics Explorer** (Beta): See **Resources > Metric Explorer ** . Select a
monitored resource type and metric. You can aggregate data across your
instances.

##  November 21, 2016

**Cloud Logging**

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

**Cloud Monitoring**

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

**Cloud Debugger**

**CHANGED:**

**Debugger GA & logs integration ** : Debugger is generally available.
Debugger now integrates a log panel into the debug view and will remember the
last selected location. Additionally, you can insert logpoints dynamically
without any rebuilds or restarts. The left and right panels in debug view can
now be collapsed for additional viewing space for source.

**Cloud Logging**

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

**Cloud Monitoring**

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

**Cloud Trace**

**FEATURE:**

**Analysis Reports** : Compare your application's latency profile across time
and versions.

**Error Reporting**

**FEATURE:**

**Cloud Functions** : Cloud Functions automatically reports unhandled
JavaScript exceptions to Stackdriver Error Reporting.

##  September 11, 2016

**Cloud Monitoring**

**CHANGED:**

The Google Monitoring API (v3) is now known as the Stackdriver Monitoring API
(v3). This change does not affect any code.

**DEPRECATED:**

The Monitoring v2 API is now deprecated. It is still named the Google Cloud
Monitoring API in **APIs & services ** .

##  September 09, 2016

**Cloud Logging**

**CHANGED:**

The Google Cloud Logging API is now known as the Stackdriver Logging API. This
change does not affect any code.

##  September 08, 2016

**Error Reporting**

**FEATURE:**

**C++** and **Ruby** are now supported.

**FIXED:**

**PHP** stack traces are better supported.

##  August 16, 2016

**Error Reporting**

**FEATURE:**

[ **Cloud Console mobile app** ](https://cloud.google.com/console-app) now
supports Error Reporting.

##  July 26, 2016

**Cloud Monitoring**

**CHANGED:**

Some documentation pages have moved in the table of contents, but their URLs
are the same or have redirections. All agent-related pages are now part of the
How-To section, [ Using the Monitoring Agent
](https://cloud.google.com//monitoring/agent/) . The former "Using Metrics"
page has been reorganized into several pages under [ Using Custom Metrics
](https://cloud.google.com/monitoring/agent/) .

##  July 18, 2016

**Error Reporting**

**FEATURE:**

**App Engine** : Error Reporting is now generally available for Google App
Engine standard environment.

##  July 12, 2016

**Error Reporting**

**FEATURE:**

**API** : The Stackdriver Error Reporting API has a new endpoint to report
errors: [ ` projects.events.report ` ](https://cloud.google.com/error-
reporting/reference/rest/v1beta1/projects.events/report) .

##  June 27, 2016

**Error Reporting**

**FEATURE:**

The **GCP Console** home page now has an Error Reporting card.

##  June 15, 2016

**Cloud Logging**

**CHANGED:**

A change to the v2beta1 API might affect some existing code. In the following
methods, the parameter ` projectName ` has been changed to ` parent ` : `
sinks.create ` , ` sinks.list ` , ` metrics.list ` , ` metrics.create ` .

**CHANGED:**

The Google Logging API v2beta1 reference documentation now includes code
snippets for each method. For example, see [ ` entries.list `
](https://cloud.google.com/logging/docs/api/ref_v2beta1/rest/v2beta1/entries/list)
.

##  June 09, 2016

**Cloud Monitoring**

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

**Cloud Monitoring**

**CHANGED:**

[ Metrics List ](https://cloud.google.com//monitoring/api/metrics) is now a
comprehensive list of all metrics available in Monitoring, including metrics
gathered by the monitoring agent and metrics from Amazon Web Services.

##  April 27, 2016

**Cloud Logging**

**CHANGED:**

The user documentation has been reorganized. The [ documentation landing page
](https://cloud.google.com/logging/docs) and the left-side navigation entries
have changed. Existing URLs to individual documentation pages will be
redirected if necessary.

**Cloud Monitoring**

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

**Cloud Logging**

**CHANGED:**

Google Cloud Logging is now **Stackdriver Logging** , part of the [ Google
Stackdriver ](https://cloud.google.com/stackdriver) suite of products. You can
now manage logs from Amazon EC2 virtual machine instances alongside your
Google Cloud Platform (GCP) projects. See [ Logging agent
](https://cloud.google.com/logging/docs/agent) for more details.

**Cloud Monitoring**

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

**Cloud Monitoring**

**FEATURE:**

The [ Monitoring API v3
](https://cloud.google.com/monitoring/api/ref_v3/rest/) is now available.
Users are encouraged to begin upgrading from the Cloud Monitoring API v2. See
[ What's new ](https://cloud.google.com/monitoring/api/v3/) in the v3 API and
look at the new [ code samples
](https://cloud.google.com/monitoring/docs/tutorials) on GitHub.

**Error Reporting**

**FEATURE:**

**Beta release** of Stackdriver Error Reporting.

##  February 18, 2016

**Cloud Logging**

**CHANGED:**

The [ logging agent authorization
](https://cloud.google.com/logging/docs/agent/authorization) instructions now
recommend storing private-key credentials as `
/etc/google/auth/application_default_credentials.json ` . You do not have to
move your existing file at `
/root/.config/gcloud/application_default_credentials.json ` .

##  January 29, 2016

**Cloud Logging**

**CHANGED:**

The [ Logs Viewer ](https://cloud.google.com/logging/docs/view/logs_viewer)
now lets you [ view the structure
](https://cloud.google.com/logging/docs/view/logs_viewer#expanding) of log
entries. You can also [ show or hide
](https://cloud.google.com/logging/docs/view/logs_viewer#similar) log entries
with similar field values.

##  December 10, 2015

**Cloud Logging**

**CHANGED:**

Version 2 of the [ Cloud Logging API
](https://cloud.google.com/logging/docs/apis) is now available. Among other
changes, the V2 API lets you retrieve log entries from Logging using the [ `
entries.list `
](https://cloud.google.com/logging/docs/api/ref_v2beta1/rest/v2beta1/entries/list)
method.

##  October 22, 2015

**Cloud Logging**

**CHANGED:**

The [ Logs Viewer ](https://cloud.google.com/logging/docs/view/logs_viewer)
now has cascading menus for selecting log entries from Google App Engine and
Google Compute Engine.

##  October 13, 2015

**Cloud Logging**

**CHANGED:**

See [ logs-based-metrics
](https://cloud.google.com/logging/docs/view/logs_based_metrics) to learn how
to create Google Cloud Monitoring metrics using logs filters.

**CHANGED:**

The list of [ log types
](https://cloud.google.com/logging/docs/view/logs_index) has been expanded.

##  September 29, 2015

**Cloud Monitoring**

**FEATURE:**

Charts now have a [ View Logs
](https://cloud.google.com/monitoring/quickstart-lamp#charts-to-logs) option
in their settings menu.

##  September 15, 2015

**Cloud Logging**

**CHANGED:**

Added [ Java examples ](https://cloud.google.com/logging/docs/api/tasks/) of
Logging API usage. Simplified the [ authorization code
](https://cloud.google.com/logging/docs/api/tasks/authorization) for Java and
Python, and the same code now runs on App Engine, Compute Engine, and your
development workstation.

##  September 09, 2015

**Cloud Logging**

**CHANGED:**

The [ command-line interface
](https://cloud.google.com/logging/docs/api/gcloud-logging) in the Google
Cloud SDK is now named ` gcloud beta logging ` .

##  August 12, 2015

**Cloud Logging**

**FEATURE:**

The [ Cloud Logging API ](https://cloud.google.com/logging/docs/reference/api-
overview) and [ command-line interface
](https://cloud.google.com/logging/docs/api/gcloud-logging) now support
project sinks. A project sink can export log entries from any combination of
logs, based on [ advanced logs filters
](https://cloud.google.com/logging/docs/view/advanced-queries) .

##  August 03, 2015

**Cloud Logging**

**FEATURE:**

Cloud Logging now has advanced logs filters that let you specify arbitrary
Boolean expressions that match on log entries. See [ Using advanced logs
filters ](https://cloud.google.com/logging/docs/view/advanced-queries) in the
Logs Viewer, and the [ Advanced Logs Filters guide
](https://cloud.google.com/logging/docs/view/advanced-queries) .

##  June 15, 2015

**Cloud Logging**

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

**Cloud Logging**

**CHANGED:**

A new GCP Console UI panel for the [ logs export feature
](https://cloud.google.com/logging/docs/export/configure_export) was released.
The UI lets you export a subset of your logs from a logs service. For example,
you could export ` syslog ` from Google Compute Engine without exporting `
activity_log ` .

##  April 28, 2015

**Cloud Logging**

**FEATURE:**

You can now stream logs from Cloud Logging to [ Google Cloud Pub/Sub
](https://cloud.google.com/pubsub/docs) and from there to your own endpoints.
This involves changes to [ logs export
](https://cloud.google.com/logging/docs/export/using_exported_logs#pubsub-
overview) . For example, use Cloud Pub/Sub to route logs through [ Google
Cloud Dataflow ](https://cloud.google.com/dataflow/docs) and into tools like [
Google BigQuery ](https://cloud.google.com/bigquery/docs) .

##  March 19, 2015

**Cloud Logging**

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

**Cloud Logging**

**FEATURE:**

Beta release: App Engine logs can be exported to Cloud Storage and BigQuery.

##  January 07, 2015

**Cloud Monitoring**

**FEATURE:**

First beta release of [ Google Cloud Monitoring powered by Stackdriver
](https://cloud.google.com/monitoring) .

