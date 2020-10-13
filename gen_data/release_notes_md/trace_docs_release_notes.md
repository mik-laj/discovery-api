#  Release Notes

This page documents production updates to Trace. You can periodically check
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

The Cloud Trace viewer now supports search by the trace ID. For more
information, see [ Viewing Trace Details
](https://cloud.google.com/trace/docs/viewing-details) .

##  March 30, 2020

**FEATURE:**

You can now use [ OpenTelemetry ](https://opentelemetry.io/) with [ Go
](https://cloud.google.com/trace/docs/setup/go-ot) and [ Node.js
](https://cloud.google.com/trace/docs/setup/nodejs-ot) to instrument your
applications running on GKE and Compute Engine.

##  February 20, 2020

**CHANGED:**

Integration of Cloud Trace with Virtual Private Cloud Service Controls is now
generally available. For more information, see [ VPC Service Controls
documentation ](https://cloud.google.com/vpc-service-controls/docs/) .

##  February 19, 2020

**FEATURE:**

[ Beta release ](https://cloud.google.com/products/#product-launch-stages) :
Export of Stackdriver Trace data to BigQuery. For more information, see [
Managing Trace exports ](https://cloud.google.com/trace/docs/trace-export-
overview) .

##  February 06, 2020

**CHANGED:**

The [ Stackdriver Trace API v2
](https://cloud.google.com/trace/docs/reference) is now Generally Available.

##  December 16, 2019

**FEATURE:**

Integration of Stackdriver Trace with Virtual Private Cloud Service Controls
is now beta. For more information, see [ VPC Service Controls documentation
](https://cloud.google.com/vpc-service-controls/docs/) .

##  November 20, 2019

**FEATURE:**

The **Trace list** page has a new menu-driven filtering solution that is in
Beta release testing. For more information, see [ Finding and viewing traces
](https://cloud.google.com/trace/docs/finding-traces) .

##  December 18, 2018

**CHANGED:**

Trace list now limits HTTP method and HTTP status matches to trace root spans.
See [ Filter traces ](https://cloud.google.com/trace/docs/finding-
traces#filter_traces) for more details.

**FEATURE:**

You can now filter traces for analysis reports by the full URI, by the URI
prefix, or by using trace filter. See [ Create a new analysis report
](https://cloud.google.com/trace/docs/analysis-
reports#create_a_new_analysis_report) for details.

##  October 31, 2018

**CHANGED:**

Stackdriver Trace enforces consumption-based pricing as of November 1, 2018 at
00:00 PDT. For more information, see [ Stackdriver Pricing
](https://cloud.google.com/stackdriver/pricing) .

**CHANGED:**

On November 1, 2018, Stackdriver Trace begins enforcing a daily trace spans
ingestion quota. See [ Stackdriver Trace Quotas & Limits
](https://cloud.google.com/trace/docs/quotas) for details.

##  September 05, 2018

**FEATURE:**

Billing enforcement for Trace has been postponed to November 1, 2018, rather
than the previously announced date of September 30, 2018. You can now estimate
your bill for your usage of Trace, according to the new pricing and in advance
of billing enforcement. See [ Estimating your bills
](https://cloud.google.com/stackdriver/estimating-bills) for details.

##  April 04, 2018

**FEATURE:**

The Trace Viewer now allows you to view trace spans for related Google Cloud
Platform projects in one view. See [ Viewing traces across projects
](https://cloud.google.com/trace/docs/cross-project-traces) for details.

##  March 28, 2018

**FEATURE:**

Stackdriver Trace Data Access audit logs are now Generally Available. See [
Stackdriver Trace Audit Logging ](https://cloud.google.com/trace/docs/audit-
logging) for details.

##  March 12, 2018

**CHANGED:**

Beginning on June 30, 2018, Stackdriver is switching to consumption-based
pricing, including revised quotas. For more information, see [ Stackdriver
Upcoming Pricing ](https://cloud.google.com/stackdriver/pricing_v2) .

##  February 27, 2018

**FEATURE:**

The Trace Viewer now associates logs entries with trace spans when the
LogEntry ` span_id ` field is specified. See [ Integrating with Cloud Logging
](https://cloud.google.com/trace/docs/trace-log-integration) for details.

**FIXED:**

The Trace Viewer now follows your scroll through the span details page, making
it easier to see span details of large traces.

##  January 12, 2018

**FEATURE:**

The Trace viewer now shows sub-millisecond resolution for Trace spans.

##  January 09, 2018

**FEATURE:**

The Trace viewer now displays span annotations and message events written with
the [ Stackdriver Trace API v2
](https://cloud.google.com/trace/docs/reference/v2/rest/) . See [ Viewing
Trace Details ](https://cloud.google.com/trace/docs/viewing-
details#annotating_spans) for more information.

##  October 31, 2017

**FEATURE:**

The [ Stackdriver Trace API v2
](https://cloud.google.com/trace/docs/reference/v2/rest/) is now in Beta
release. For a comparison of the v1 and v2 APIs, see [ Stackdriver Trace API
](https://cloud.google.com/trace/docs/reference) .

##  October 02, 2017

**FEATURE:**

The Trace viewer now shows parent-child relationships between trace spans. You
can expand or collapse the parent spans. See [ Viewing Trace Details
](https://cloud.google.com/trace/docs/viewing-details) for more information.

##  August 01, 2017

**FEATURE:**

The Trace Viewer now allows you to view associated log entries in line with
trace spans and links to VM logs for Google Cloud Load Balancer spans. See the
[ Integrating with Cloud Logging ](https://cloud.google.com/trace/docs/trace-
log-integration) .

##  June 05, 2017

**FEATURE:**

**Advanced trace filters** : The Trace List page and Trace API now allow
filtering traces by custom labels, latencies, child spans, and methods in
addition to URIs. See [ Trace Filters
](https://cloud.google.com/trace/docs/trace-filters) .

##  February 06, 2017

**FEATURE:**

**Zipkin tracer compatibility** : Stackdriver Trace is now compatible with
Zipkin tracers. For more information, see this [ blog post
](https://cloudplatform.googleblog.com/2016/12/Stackdriver-Trace-Zipkin-
distributed-tracing-and-performance-analysis-for-everyone.html) .

**FEATURE:**

**Scatter plots** : We've added a new scatter-plot selection tool to the
Stackdriver Trace UI. This lets you more quickly identify, view, and compare
interesting traces.

##  October 20, 2016

**FEATURE:**

**Analysis Reports** : Compare your application's latency profile across time
and versions.

