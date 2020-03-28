#  Release Notes

This page documents production updates to Error Reporting. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/stackdriver-release-notes.xml `

##  December 13, 2019

**CHANGED:**

Error Reporting now infers the service name and version from the ` logEntry `
fields named ` k8s-pod/serving_knative_dev/service ` and `
k8s-pod/serving_knative_dev/revision ` for Knative Serving labels on Cloud Run
on Google Kubernetes Engine. This replaces the current default value of `
gke_instances ` for service name.

##  May 08, 2019

**FEATURE:**

**API**

Error events written as instances of [ ` ReportedErrorEvent `
](https://cloud.google.com/error-
reporting/reference/rest/v1beta1/projects.events/report#ReportedErrorEvent)
generate properly formatted error messages in Stackdriver Logging.

##  January 18, 2019

**FEATURE:**

**Error detection for Python applications** has been improved. You might see
more newly detected error groups or receive more notifications.

##  December 19, 2017

**FEATURE:**

**Resolution Status** features are now Generally Available. You can now assign
a status to your error groups, making it easier to triage errors.

##  June 05, 2017

**FEATURE:**

**IAM roles** : Stackdriver Error Reporting IAM roles are now available. See [
Error Reporting IAM roles ](https://cloud.google.com/error-
reporting/docs/iam#iam_roles) .

##  May 01, 2017

**FEATURE:**

**Error filters** : You can now filter errors by custom text in addition to
filtering by time, service, and version.

##  October 20, 2016

**FEATURE:**

**Cloud Functions** : Cloud Functions automatically reports unhandled
JavaScript exceptions to Stackdriver Error Reporting.

##  September 08, 2016

**FEATURE:**

**C++** and **Ruby** are now supported.

**FIXED:**

**PHP** stack traces are better supported.

##  August 16, 2016

**FEATURE:**

[ **Cloud Console mobile app** ](https://cloud.google.com/console-app) now
supports Error Reporting.

##  July 18, 2016

**FEATURE:**

**App Engine** : Error Reporting is now generally available for Google App
Engine standard environment.

##  July 12, 2016

**FEATURE:**

**API** : The Stackdriver Error Reporting API has a new endpoint to report
errors: [ ` projects.events.report ` ](https://cloud.google.com/error-
reporting/reference/rest/v1beta1/projects.events/report) .

##  June 27, 2016

**FEATURE:**

The **GCP Console** home page now has an Error Reporting card.

##  March 17, 2016

**FEATURE:**

**Beta release** of Stackdriver Error Reporting.

Send feedback

