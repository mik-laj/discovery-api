#  Release Notes

This page documents production updates to VPC Service Controls. You can
periodically check this page for announcements about new or updated features,
bug fixes, known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/vpc-sc-release-notes.xml `

##  June 26, 2020

**CHANGED:**

[ Beta stage support ](https://cloud.google.com/products/#product-launch-
stages) for the following integration:

  * [ Binary Authorization ](https://cloud.google.com/binary-authorization/docs/securing-with-vpcsc)

##  June 11, 2020

**FEATURE:**

General availability for bulk changes to service perimeters.

Using Access Context Manager's Bulk API, you can replace all of your
organization's service perimeters in one operation. For more information, see
[ Making bulk changes to service perimeters ](https://cloud.google.com/vpc-
service-controls/docs/bulk-operations) .

##  June 04, 2020

**FEATURE:**

The VPC accessible services feature is now generally available. Use VPC
accessible services to limit the access of network endpoints and VMs in a
perimeter to only services protected by that perimeter.

For more information about the feature, see [ VPC accessible services
](https://cloud.google.com/docs/vpc-service-controls/docs/vpc-accessible-
services) .

##  May 21, 2020

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following integration:

  * [ Service Directory ](https://cloud.google.com/service-directory/docs/securing-with-vpc-sc)

##  May 13, 2020

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following integration:

  * [ Memorystore for Redis ](https://cloud.google.com/memorystore/docs/redis)

##  April 09, 2020

**FEATURE:**

The beta version of the VPC accessible services feature is now available.

The [ VPC accessible services ](https://cloud.google.com/vpc-service-
controls/docs/vpc-accessible-services) feature introduces the ability to limit
the access of network endpoints inside your service perimeter to an explicit
set of services.

To learn how to configure VPC accessible services for your perimeter, read
about [ limiting access to services inside a perimeter
](https://cloud.google.com/vpc-service-controls/docs/manage-service-
perimeters#accessible-services) .

**FEATURE:**

The beta version of dry run mode for service perimeters is now available.

This release introduces a new method of configuring service perimeters: dry
run mode. For more information, [ read about dry run mode
](https://cloud.google.com/vpc-service-controls/docs/dry-run-mode) .

##  April 03, 2020

**FEATURE:**

Beta support for bulk changes to service perimeters.

Using the beta release of Access Context Manager's Bulk API, you can perform
operations such as replacing all of your organization's service perimeters.
For more information, see [ Making bulk changes to service perimeters
](https://cloud.google.com/vpc-service-controls/docs/bulk-operations) .

##  April 01, 2020

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following integrations:

  * [ Container Analysis ](https://cloud.google.com/container-registry/docs/container-analysis)

##  March 31, 2020

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following integrations:

  * [ AutoML Natural Language ](https://cloud.google.com/natural-language/automl/docs)
  * [ AutoML Tables ](https://cloud.google.com/automl-tables/docs)
  * [ AutoML Translation ](https://cloud.google.com/translate/automl/docs)
  * [ AutoML Video Intelligence ](https://cloud.google.com/video-intelligence/automl/docs)
  * [ AutoML Vision ](https://cloud.google.com/vision/automl/docs)
  * [ Artifact Registry ](https://cloud.google.com/artifacts/docs)

##  March 24, 2020

**FEATURE:**

General availability for the following integration:

  * [ Cloud Functions ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_functions)

##  March 10, 2020

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for:

  * [ Managed Service for Microsoft Active Directory ](https://cloud.google.com/managed-microsoft-ad/docs)

##  February 06, 2020

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following integrations:

  * [ Cloud Translation ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_translate)

##  January 31, 2020

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following integrations:

  * [ Cloud Functions ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_functions)
  * [ Cloud Data Fusion ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_data_fusion)

##  December 20, 2019

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following integration:

  * [ AI Platform Training ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_aip-training)

##  December 18, 2019

**FEATURE:**

[ Beta stage support ](https://cloud.google.com/products/#product-launch-
stages) for the following integrations:

  * [ Cloud Asset Inventory ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_cloud_asset_api)

##  December 17, 2019

**FEATURE:**

General availability support for:

  * [ Cloud SQL ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_cloud_sql_admin_api)

##  December 16, 2019

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following integrations:

  * [ Trace API ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_trace)

##  December 10, 2019

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following integrations:

  * [ Profiler API ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_profiler)

##  December 02, 2019

**FEATURE:**

Unique identifier for VPC Service Controls access errors.

When a request for resources in a perimeter is denied (a 403 error), a unique
identifier is generated that you can use to identify the corresponding log
entry using Stackdriver Logging.

For more information, see:

  * [ Unique Identifier helps troubleshooting VPC Service Controls perimeter ](https://cloud.google.com/blog/products/identity-security/unique-identifier-helps-troubleshooting-vpc-service-controls-perimeter)
  * [ VPC Service Controls troubleshooting documentation ](https://cloud.google.com/vpc-service-controls/docs/troubleshooting#using_the_errors_unique_id)

##  October 30, 2019

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following integrations:

  * [ Natural Language API ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_natural_language_api)

##  August 22, 2019

**CHANGED:**

The [ limits ](https://cloud.google.com/vpc-service-controls/quotas) for VPC
Service Controls have been increased:

  * Previously, only 50 perimeters per policy were allowed. That limit has been increased to 100. 
  * Previously, only 2500 projects total were allowed across all perimeters for one policy. That limit has been increased to 4000. 

##  August 09, 2019

**FEATURE:**

[ General availability ](https://cloud.google.com/products/#product-launch-
stages) for the following integrations:

  * [ Cloud Dataflow ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_dataflow)

##  May 24, 2019

**FEATURE:**

[ General availability ](https://cloud.google.com/products/#product-launch-
stages) for the following integrations:

  * [ Cloud Key Management Service ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_kms)
  * [ Cloud Spanner ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_spanner)
  * [ Container Registry ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_registry)
  * [ Google Kubernetes Engine ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_gke)

##  April 01, 2019

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following:

  * Cloud Dataflow 

##  March 29, 2019

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following:

  * Cloud Key Management Service 
  * Cloud Spanner 

##  March 08, 2019

**FEATURE:**

General availability of VPC Service Controls.

##  February 28, 2019

**FEATURE:**

[ Alpha stage ](https://cloud.google.com/terms/launch-stages) support for the
Google Kubernetes Engine API.

[ Beta stage ](https://cloud.google.com/terms/launch-stages) support for
Google Kubernetes Engine private clusters.

As of this release, GKE private clusters can be protected by VPC Service
Controls service perimeters.

For more information, refer to the [ VPC Service Controls page
](https://cloud.google.com/vpc-service-controls) and the [ documentation
](https://cloud.google.com/vpc-service-controls/docs) .

##  December 20, 2018

**FEATURE:**

Public beta release of VPC Service Controls.

As of this release, VPC Service Controls supports the following services:

  * Cloud Bigtable 
  * Cloud Storage 
  * BigQuery 
  * Cloud Pub/Sub 
  * Cloud Dataproc 
  * Stackdriver Logging 

VPC Service Controls also has Alpha stage support for the following services:

**Note:** We recommend you protect these services for testing purposes only.

  * Container Registry 
  * Cloud Key Management Service 
  * Cloud Spanner 

**ISSUE:**

App Engine is not supported by VPC Service Controls. However, you can use
Access Context Manager to allow App Engine apps outside a service perimeter to
access resources protected by VPC Service Controls by adding the App Engine
service account to an access level for that perimeter.

For more information, read about [ App Engine limitations
](https://cloud.google.com/vpc-service-controls/docs/supported-
products#appengine) .

**ISSUE:**

The BigQuery Data Transfer Service is not supported. Additionally, there are
known limitations with the legacy BigQuery interface, the third-party ODBC
driver for BigQuery, and BigQuery audit logs.

For more information, read about [ BigQuery limitations
](https://cloud.google.com/vpc-service-controls/docs/supported-
products#bigquery) .

**ISSUE:**

The Java and Python client libraries for all supported services are fully
supported for access using the VPC Service Controls restricted VIP. Support
for others language is at Alpha stage and should be used for testing purposes
only. Client libraries updated since November 1, 2018 must be used.

Service account keys and OAuth2 client metadata used to authenticate must be
updated as of November 1, 2018.

For more information, read about [ client library limitations
](https://cloud.google.com/vpc-service-controls/docs/supported-
products#clientlibraries) .

**ISSUE:**

To configure Cloud Billing exporting inside a service perimeter, the user
performing the configuration must be added to an access level for that
perimeter.

For more information, read about [ Cloud Billing limitations
](https://cloud.google.com/vpc-service-controls/docs/supported-
products#billing) .

**ISSUE:**

Cloud Dataproc requires additional steps to set up a functional cluster inside
a service perimeter.

For more information, read about [ Cloud Dataproc limitations
](https://cloud.google.com/vpc-service-controls/docs/supported-
products#dataproc) .

**ISSUE:**

Cloud Functions is not supported by VPC Service Controls. However, you can use
Access Context Manager to allow functions outside a service perimeter to
access resources protected by VPC Service Controls by adding the Cloud
Functions service account to an access level for that perimeter.

For more information, read about [ Cloud Functions limitations
](https://cloud.google.com/vpc-service-controls/docs/supported-
products#functions) .

**ISSUE:**

VPC Service Controls policy only applies to new Cloud Pub/Sub push
subscriptions. Push subscriptions that exist before a service perimeter is
created will not be blocked by that perimeter.

For more information, read about [ Cloud Pub/Sub limitations
](https://cloud.google.com/vpc-service-controls/docs/supported-
products#pubsub) .

**ISSUE:**

Cloud Shell is not supported. It is treated as outside of service perimeters
and denied access to data protected by VPC Service Controls.

**ISSUE:**

Legacy Cloud Storage buckets can in certain cases be written to out of a
service perimeter even when access is denied.

Additionally, Cloud Storage audit logs do not always report VPC Service
Controls errors correctly.

For more information, read about [ Cloud Storage limitations
](https://cloud.google.com/vpc-service-controls/docs/supported-
products#storage) .

**ISSUE:**

To create Compute Engine images from Cloud Storage inside a service perimeter,
the user performing the configuration must be added to an access level for
that perimeter.

For more information, read about [ Compute Engine limitations
](https://cloud.google.com/vpc-service-controls/docs/supported-
products#computeengine) .

**ISSUE:**

A Cloud DNS private zone or BIND must be used to map Container Registry to the
restricted VIP.

The following Google-managed repositories are available to all projects
regardless of service perimeters:

  * dataflow.gcr.io 
  * gcr.io/cloud-airflow-releaser 
  * gcr.io/cloudsql-docker 
  * gcr.io/gke-node-images 
  * gcr.io/kubeflow-images-public 
  * gcr.io/kubernetes-helm 
  * gcr.io/project-calico 
  * gcr.io/stackdriver-agents 
  * gke.gcr.io 
  * k8s.gcr.io 
  * mirror.gcr.io 

For more information, read about [ Container Registry limitations
](https://cloud.google.com/vpc-service-controls/docs/supported-
products#registry) .

**ISSUE:**

To use the Google Cloud Platform Console with services protected by a service
perimeter, the user accessing the services must be added to an access level
for that perimeter.

**ISSUE:**

Because VPC Service Controls does not currently support folder and
organization resources, log exports of folder-level and organization-level
logs (including aggregate logs) do not support service perimeters.

Aggregated Stackdriver Logging logs can access data protected by a service
perimeter. Cloud IAM should be used to control access to that data.

For more information, read about [ Logging limitations
](https://cloud.google.com/vpc-service-controls/docs/supported-
products#logging) .

