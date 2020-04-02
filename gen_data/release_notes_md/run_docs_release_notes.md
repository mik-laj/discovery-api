#  Cloud Run (fully managed) release notes

This page documents production updates to Cloud Run (fully managed). You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/run-release-notes.xml `

##  March 30, 2020

**FEATURE:**

The Cloud Run revision details panel now surfaces build information if the [
Container Analysis API ](https://cloud.google.com/container-
registry/docs/container-analysis) has been enabled and the container has been
built with [ Cloud Build ](https://cloud.google.com/cloud-build) , as well as
source repository information if the container has been built by a [ Cloud
Build Trigger ](https://cloud.google.com/cloud-build/docs/running-
builds/create-manage-triggers) .

##  March 23, 2020

**FIXED:**

You can now restrict which regions are available to deploy Cloud Run (fully
managed) services using an organization policy with a [ resource locations
constraint ](https://cloud.google.com/resource-manager/docs/organization-
policy/defining-locations) .

##  March 16, 2020

**FEATURE:**

Cloud Run (fully managed) now supports deploying container images from [ Cloud
Artifact Registry ](https://cloud.google.com/artifacts/docs/overview)

##  February 12, 2020

**FEATURE:**

Cloud Run (fully managed) now supports [ rollbacks, gradual rollouts
(blue/green deployments), and other traffic migration manipulations
](https://cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration)
between revisions.

##  January 30, 2020

**FEATURE:**

Cloud Run is now available in the following regions:

  * asia-east1 (Taiwan) 
  * europe-north1 (Finland) 
  * europe-west4 (Netherlands) 
  * us-east4 (Northern Virginia) 
  * us-west1 (Oregon) 

##  January 24, 2020

**FEATURE:**

You can now [ allocate 2 vCPUs
](https://cloud.google.com/run/docs/configuring/cpu) to Cloud Run (fully
managed) services.

##  January 07, 2020

**FEATURE:**

You can now [ customize the container port
](https://cloud.google.com/run/docs/configuring/containers#configure-port) on
which requests are sent. We still recommend listening on ` $PORT ` for better
container portability.

**FEATURE:**

Deploy Cloud Run services from a local configuration file with ` gcloud beta
run services replace service.yaml ` .

**FEATURE:**

[ Specify custom command and arguments
](https://cloud.google.com/run/docs/configuring/containers#configure-
entrypoint) for your deployed containers.

**FEATURE:**

Use custom revision names with the ` --revision-suffix ` command line flag.

##  December 23, 2019

**CHANGED:**

Cloud Run (fully managed) [ Service Level Agreement (SLA)
](https://cloud.google.com/run/sla) has been updated to a Monthly Uptime
Percentage of at least 99.95%

##  November 14, 2019

**FEATURE:**

Cloud Run (fully managed) is now Generally Available (GA).

##  October 25, 2019

**BREAKING:**

Legacy versions of the [ container instance metadata server
](https://cloud.google.com/run/docs/reference/container-contract#metadata-
server) have been removed.

##  October 22, 2019

**CHANGED:**

Cloud Run (fully managed) free tier is now applied as a spending based
discount.

##  October 21, 2019

**FEATURE:**

Cloud Run is now covered by [ HIPAA Compliance
](https://cloud.google.com/security/compliance/hipaa/) .

##  October 01, 2019

**FEATURE:**

The [ max instances setting
](https://cloud.google.com/run/docs/configuring/max-instances) feature allows
you to set a limit to the total number of container instances that are started
up to handle traffic.

##  September 26, 2019

**FEATURE:**

The "Metrics" tab on the [ service detail page
](https://cloud.google.com/run/docs/managing/services#details) now includes a
" [ Billable container instance time
](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-run) " chart,
allowing you to better understand how many instances are actively serving
traffic for this service.

**FEATURE:**

The "Metrics" tab on the [ service detail page
](https://cloud.google.com/run/docs/managing/services#details) now includes an
[ "Error Reporting" ](https://cloud.google.com/run/docs/error-reporting) table
that displays the top application errors for this service.

##  September 25, 2019

**FEATURE:**

Cloud Run (fully managed) now supports [ unary gRPC
](https://grpc.io/docs/guides/concepts/) .

##  September 19, 2019

**FEATURE:**

[ Cloud Run (fully managed) v1 API
](https://cloud.google.com/run/docs/reference/rest/) is now available.

##  September 10, 2019

**FEATURE:**

You can set [ labels ](https://cloud.google.com/run/docs/configuring/labels)
on Cloud Run services and revisions.

##  August 19, 2019

**CHANGED:**

Cloud Run (fully managed) services are now only accessible via HTTPS. Any HTTP
requests to Cloud Run services now receives a 302 "Moved Temporarily" status
code that redirects to the HTTPS location. Web browsers follow this
redirection.

##  July 10, 2019

**FEATURE:**

The following new regions are now available: ` asia-northeast1 ` , ` europe-
west1 ` , and ` us-east1 ` .

##  July 08, 2019

**FEATURE:**

New YAML tab on the service details page.

##  June 18, 2019

**CHANGED:**

New ` --platform ` flag added to [ Cloud Run gcloud command line
](https://cloud.google.com/sdk/gcloud/reference/beta/run/) . This argument is
optional but will be required in a future release of the tool.

##  June 07, 2019

**FEATURE:**

[ Per-service identity ](https://cloud.google.com/run/docs/securing/service-
identity#per-service-identity) .

##  May 20, 2019

**FEATURE:**

New "Metrics" tab in the Cloud Run service detail view, displaying a list of
curated [ monitoring metrics ](https://cloud.google.com/run/docs/monitoring) .

##  May 17, 2019

**FEATURE:**

Cloud Run (fully managed) has been added to the [ Google Cloud Platform
Pricing Calculator ](https://cloud.google.com/products/calculator/) .

##  May 07, 2019

**FEATURE:**

[ Cloud SQL is now supported
](https://cloud.google.com/run/docs/configuring/connect-cloudsql) .

##  April 09, 2019

**FEATURE:**

Cloud Run (fully managed) Beta release.

##  August 15, 2018

**FEATURE:**

Cloud Run (fully managed) Alpha release.

