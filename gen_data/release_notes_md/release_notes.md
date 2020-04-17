#  Google Cloud release notes

The following release notes cover the most recent changes over the last 30
days. For a comprehensive list, see the [ individual product release note
pages ](/release-notes/all) .

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/gcp-release-notes.xml `

##  April 15, 2020

**Cloud CDN**

**FEATURE:**

[ Signed Cookies ](https://cloud.google.com/cdn/docs/using-signed-cookies) are
available in **General Availability** . Signed Cookies complement our existing
[ Signed URLs ](https://cloud.google.com/cdn/docs/using-signed-urls)
functionality by allowing you to sign a URL prefix and issue a cookie to a
client, avoiding the need to sign content on a per-URL basis when protecting
media or other content cached by Cloud CDN. Support for authorizing a URL
prefix is extended to Signed URLs as an alternative signing scheme.

**Cloud Deployment Manager**

**FEATURE:**

Added support for [ Cloud Scheduler ](https://cloud.google.com/scheduler)
through ` gcp-types/cloudscheduler-v1:projects.locations.jobs ` .

**CHANGED:**

You can now apply granular [ IAM Permissions
](https://cloud.google.com/iam/docs/permissions-reference) to the [ Google
APIs service account used by Deployment Manager
](https://cloud.google.com/deployment-manager/docs/access-
control#access_control_for) , as we've removed the requirement for `
roles/editor ` being assigned to the service account.

**CHANGED:**

Updates on [ Cloud Functions ](https://cloud.google.com/functions) resources
using ` gcp-types/cloudfunctions-v1 ` now retry on 429 errors.

**CHANGED:**

GKE clusters and node pools will wait for maintenance to complete before
attempting to apply any updates. Affected collections:

  * ` gcp-types/container-v1:projects.zones.clusters `
  * ` gcp-types/container-v1:projects.locations.clusters `
  * ` gcp-types/container-v1:projects.zones.clusters.nodePools `
  * ` gcp-types/container-v1:projects.locations.clusters.nodePools `
  * ` gcp-types/container-v1beta1:projects.zones.clusters `
  * ` gcp-types/container-v1beta1:projects.locations.clusters `
  * ` gcp-types/container-v1beta1:projects.zones.clusters.nodePools `
  * ` gcp-types/container-v1beta1:projects.locations.clusters.nodePools `

**FIXED:**

Deployment Manager now acquires existing GKE cluster resources of type ` gcp-
types/container-v1:projects.locations.clusters ` .

**CHANGED:**

Added support for updating the following properties on ` gcp-
types/container-v1:projects.zones.clusters ` and ` gcp-
types/container-v1:projects.locations.clusters ` :

  * binaryAuthorization 
  * databaseEncryption 
  * masterAuthorizedNetworksConfig 
  * autoscaling 
  * resourceUsageExportConfig 
  * verticalPodAutoscaling 

Additionally, for ` gcp-types/container-v1beta1:projects.zones.clusters ` and
` gcp-types/container-v1beta1:projects.locations.clusters ` the following
fields can also be updated:

  * podSecurityPolicyConfig 
  * privateClusterConfig 
  * shieldedNodes 
  * workloadIdentityConfig 

**FIXED:**

Deployment Manager now correctly updates autoscaling properties for resources
of type ` gcp-types/container-v1:projects.locations.clusters.nodePools ` and `
gcp-types/container-v1beta1:projects.locations.clusters.nodePools ` .

**FIXED:**

Deployment Manager now correctly acquires [ Access Context Manager
](https://cloud.google.com/access-context-manager/docs) resources of type `
gcp-types/accesscontextmanager-v1:accessPolicies.accessLevels ` and ` gcp-
types/accesscontextmanager-v1beta:accessPolicies.accessLevels ` if the
resources already exist.

**CHANGED:**

Added support for updating [ Cloud Pub/Sub ](https://cloud.google.com/pubsub)
subscriptions using ` gcp-types/pubsub-v1:projects.subscriptions ` .

**FIXED:**

Deployment Manager now correctly deletes [ Compute Engine
](https://cloud.google.com/compute/docs) forwarding rules of type `
compute.v1.forwardingRule ` , ` compute.beta.forwardingRule ` , ` gcp-
types/compute-v1:forwardingRules ` and ` gcp-types/compute-
beta:forwardingRules ` when the resource name does not match the forwarding
rule name.

**CHANGED:**

Performance improvements when handling large Swagger / OpenAPI specs when [
adding an API as a type provider ](https://cloud.google.com/deployment-
manager/docs/configuration/type-providers/creating-type-provider) .

**Cloud Key Management Service**

**FEATURE:**

[ Cloud External Key Manager (Cloud EKM)
](https://cloud.google.com/kms/docs/ekm) is generally available.

**Dataflow**

**FEATURE:**

[ Cloud Dataflow SQL
](https://cloud.google.com/dataflow/docs/guides/sql/dataflow-sql-intro) is now
generally available. You can now run parameterized queries from the Dataflow
SQL UI.

**Dataproc**

**FEATURE:**

**Image 1.5**

[ Jupyter on Dataproc
](https://cloud.google.com/dataproc/docs/concepts/components/jupyter) now
supports exporting notebooks as PDFs.

**FEATURE:**

**Image 1.5**

[ Presto ](https://cloud.google.com/dataproc/docs/concepts/components/presto)
now includes two default connectors: * ` bigquery ` pointing to the datasets
of the cluster's project * ` bigquery_public_data ` pointing to the public
datasets

**FEATURE:**

**Image 1.3, 1.4 and 1.5**

Added [ Component Gateway
](https://cloud.google.com/dataproc/docs/concepts/accessing/dataproc-gateways)
support for Datarpoc clusters secured with Kerberos.

**CHANGED:**

New [ sub-minor
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions#supported_cloud_dataproc_versions) versions of Dataproc images:
1.2.95-debian9, 1.3.55-debian9, 1.4.26-debian9, 1.3.55-debian10,
1.4.26-debian10, 1.5.1-debian10, 1.3.55-ubuntu18, 1.4.26-ubuntu18,
1.5.1-ubuntu18.

**CHANGED:**

**Image 1.5**

Updated Presto to [ version 331
](https://prestosql.io/docs/current/release/release-331.html) .

**CHANGED:**

Created ` cloud-sql-proxy ` log file for the Cloud SQL Proxy initialization
action and for Dataproc clusters with Ranger that use Cloud SQL Proxy.

**CHANGED:**

**Image 1.3 and 1.4**

Debian 10 images will become default images for 1.3 and 1.4 image tracks and
Debian 9 images will not be released for these tracks anymore after June 30,
2020.

**FIXED:**

**Images 1.4 and 1.5**

[ SPARK-29080 ](https://issues.apache.org/jira/browse/SPARK-29080) : Support R
file extension case-insensitively when submitting Spark R jobs.

**FIXED:**

**Image 1.3, 1.4 and 1.5**

Fixed a bug where Jupyter was unable to read and write notebooks stored in
Cloud Storage buckets with CMEK enabled.

**FIXED:**

**Image 1.3, 1.4 and 1.5**

[ HIVE-17275 ](https://issues.apache.org/jira/browse/HIVE-17275) : Auto-merge
fails on writes of ` UNION ALL ` output to ORC file with dynamic partitioning.

**Traffic Director**

**CHANGED:**

A new document, [ Traffic Director features
](https://cloud.google.com/traffic-director/docs/features) , is published.

##  April 14, 2020

**BigQuery Data Transfer Service**

**FEATURE:**

BigQuery Data Transfer Service now supports [ Google Merchant Center data
transfers for best sellers data
](https://cloud.google.com/bigquery/docs/merchant-center-
transfer#supported_reports) .

**Cloud Load Balancing**

**FEATURE:**

External HTTP(S) load balancers now support [ URL rewrites and redirects
](https://cloud.google.com/load-balancing/docs/https/traffic-management) .

URL rewrites allow you to decouple the URLs that your external users use from
those that your services use.

With URL redirects, you can redirect client requests from one URL to another
URL.

These features are available in **General Availability** .

**Config Connector**

**CHANGED:**

Added readiness probes to Config Connector pods

**Document AI**

**FEATURE:**

**Document AI Beta released**

The following beta features are available in API version **v1beta2** :

  * **Document processing** : You can use the API to [ parse forms ](https://cloud.google.com/solutions/document-ai/docs/process-forms) or [ tables ](https://cloud.google.com/solutions/document-ai/docs/process-tables) from PDF, TIFF, or GIF documents. 
  * **Regional support** : The API now offers multi-regional support ( ` us ` and ` eu ` ) for all features. [ Using a multi-region endpoint ](https://cloud.google.com/solutions/document-ai/docs/regions) enables you to configure the API to store and process your data in the United States or European Union. 

**FEATURE:**

**Invoice processing Beta**

  * Invoice processing is now available as a restricted feature. See [ Parsing invoices ](https://cloud.google.com/solutions/document-ai/docs/process-invoices) for more information. 

**Network Intelligence Center**

**FEATURE:**

[ Firewall Insights ](https://cloud.google.com/network-intelligence-
center/docs/firewall-insights/concepts/overview) is now in Beta.

##  April 13, 2020

**AI Platform Prediction**

**CHANGED:**

The pricing of Compute Engine (N1) machine types for online prediction in the
us-central1 region has changed. vCPU resources now cost $0.031613 per vCPU
hour and RAM now costs $0.004242 per GB hour.

[ Read more details about pricing. ](https://cloud.google.com/ai-
platform/prediction/pricing)

**App Engine flexible environment .NET**

**CHANGED:**

Quotas for sockets have been removed. There is no longer a limit on the number
of socket connections or the amount of data you can send and receive through a
socket.

**App Engine flexible environment Go**

**CHANGED:**

Quotas for sockets have been removed. There is no longer a limit on the number
of socket connections or the amount of data you can send and receive through a
socket.

**App Engine flexible environment Java**

**CHANGED:**

Quotas for sockets have been removed. There is no longer a limit on the number
of socket connections or the amount of data you can send and receive through a
socket.

**App Engine flexible environment Node.js**

**CHANGED:**

Quotas for sockets have been removed. There is no longer a limit on the number
of socket connections or the amount of data you can send and receive through a
socket.

**App Engine flexible environment Ruby**

**CHANGED:**

Quotas for sockets have been removed. There is no longer a limit on the number
of socket connections or the amount of data you can send and receive through a
socket.

**App Engine flexible environment custom runtimes**

**CHANGED:**

Quotas for sockets have been removed. There is no longer a limit on the number
of socket connections or the amount of data you can send and receive through a
socket.

**App Engine standard environment Java**

**CHANGED:**

Quotas for sockets have been removed. There is no longer a limit on the number
of socket connections or the amount of data your Java 8 app can send and
receive through a socket.

**App Engine standard environment PHP**

**CHANGED:**

Quotas for sockets have been removed. There is no longer a limit on the number
of socket connections or the amount of data your PHP 5 app can send and
receive through a socket.

**App Engine standard environment Python**

**CHANGED:**

Quotas for sockets have been removed. There is no longer a limit on the number
of socket connections or the amount of data your Python 2 app can send and
receive through a socket.

**Cloud Data Loss Prevention**

**FEATURE:**

Added additional [ infoType detectors
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * IRELAND_PPSN 
  * IRELAND_PASSPORT 

**Event Threat Detection**

**FEATURE:**

Event Threat Detection is now in general availability.

  * Learn [ how Event Threat Detection works ](https://cloud.google.com/event-threat-detection/docs/concepts-overview) . 
  * [ Get started using Event Threat Detection ](https://cloud.google.com/event-threat-detection/docs/quickstart-etd-console) . 

**Google Cloud Armor**

**CHANGED:**

Update to rules language syntax. Adds support for the CEL 'has' macro so that
Google Cloud Armor check for absence of a header in the 'request.headers' map.

##  April 11, 2020

**Cloud Vision**

**FEATURE:**

**CMEK compliance**

Vision API is now compliant with customer-managed encryption keys (CMEK). To
learn more, vist the [ CMEK compliance page
](https://cloud.google.com/vision/docs/cmek) . Please note that [ Product
Search ](https://cloud.google.com/vision/product-search/docs/) is _not_ CMEK
compliant at this time.

##  April 10, 2020

**Cloud Composer**

**FEATURE:**

[ Private IP Composer environments
](https://cloud.google.com/composer/docs/concepts/private-ip) are now
generally available (GA). See [ Configuring private IP
](https://cloud.google.com/composer/docs/how-to/managing/configuring-private-
ip) to learn how to use this feature.

**FEATURE:**

Support for [ Shared VPC networks
](https://cloud.google.com/composer/docs/how-to/managing/configuring-shared-
vpc) is now generally available (GA).

**Cloud Load Balancing**

**CHANGED:**

[ Backend services documentation ](https://cloud.google.com/load-
balancing/docs/backend-service) is updated through the Cloud Load Balancing
doc set.

**Config Connector**

**FEATURE:**

Add the CloudBuildTrigger resource

Add the SourceRepoRepository resource

**CHANGED:**

miscellaneous bug fixes and improvements

**Resource Manager**

**FEATURE:**

The Organization Policy Service resource locations constraint has launched for
general availability. This constraint allows you to define the location where
your resources are created, providing important data location compliance
tools. For more information, see the [ Restricting Resource Locations
](https://cloud.google.com/resource-manager/docs/organization-policy/defining-
locations) .

**Security Command Center**

**FEATURE:**

Security Health Analytics is now in general availability.

  * Learn about the [ vulnerability findings ](https://cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings) provided by Security Health Analytics. 
  * [ Get started with Security Health Analytics ](https://cloud.google.com/security-command-center/docs/quickstart-security-health-analytics) . 

##  April 09, 2020

**AI Platform Prediction**

**FIXED:**

If you deploy a model version for online prediction that uses [ runtime
version 2.1 ](https://cloud.google.com/ai-platform/prediction/docs/runtime-
version-list) with a [ GPU ](https://cloud.google.com/ai-
platform/prediction/docs/machine-types-online-prediction#gpus) , AI Platform
Prediction now correctly uses TensorFlow 2.1.0 to serve predictions.
Previously, AI Platform Prediction used TensorFlow 2.0.0 to serve predictions
in this situation.

**AI Platform Training**

**FEATURE:**

You can now specify virtual machine instances with the evaluator task type as
part of your training cluster for distributed training jobs. Read more about [
evaluators in TensorFlow distributed training ](https://cloud.google.com/ai-
platform/training/docs/distributed-training-details) , see [ how to configure
machine types for evaluators ](https://cloud.google.com/ai-
platform/training/docs/machine-types) , and learn about [ using evaluators
with custom containers ](https://cloud.google.com/ai-
platform/training/docs/distributed-training-containers) .

**CHANGED:**

The maximum running time for training jobs now defaults to seven days. If a
training job is still running after this duration, AI Platform Training
cancels the job.

[ Learn how to adjust the maximum running time for a job.
](https://cloud.google.com/ai-platform/training/docs/training-
jobs#configuring_the_job)

**BigQuery**

**FEATURE:**

Scheduling queries no longer requires the ` bigquery.transfers.update `
permission. The ` bigquery.jobs.create ` permission can now be used to
schedule queries. See [ Scheduling queries
](https://cloud.google.com/bigquery/docs/scheduling-
queries#required_permissions) for details.

**Cloud CDN**

**FEATURE:**

TLS v1.3 is now enabled by default for all external HTTPS load balancers, SSL
proxy load balancers, and Cloud CDN. Note that this change doesn't apply to
internal HTTPS load balancers or Traffic Director.

TLS v1.3 supports modern ciphers with forward-secrecy as a baseline and,
critically, reduces the number of round trips required to establish a TLS
session, which directly improves performance seen by your end-users.

Clients that support TLS v1.3 include Chrome, Chromium-based browsers, and
Android. These clients automatically negotiate TLS v1.3 without requiring any
changes. Clients that do not support TLS v1.3 are unaffected.

**Cloud Load Balancing**

**FEATURE:**

TLS v1.3 is now enabled by default for all external HTTPS load balancers, SSL
proxy load balancers, and Cloud CDN. Note that this change doesn't apply to
internal HTTPS load balancers or Traffic Director.

TLS v1.3 supports modern ciphers with forward-secrecy as a baseline and,
critically, reduces the number of round trips required to establish a TLS
session, which directly improves performance seen by your end-users.

Clients that support TLS v1.3 include Chrome, Chromium-based browsers, and
Android. These clients automatically negotiate TLS v1.3 without requiring any
changes. Clients that do not support TLS v1.3 are unaffected.

**Dataflow**

**FEATURE:**

Dataflow now provides beta support for [ Flex Templates
](https://cloud.google.com/dataflow/docs/guides/templates/using-flex-
templates) .

**FEATURE:**

Dataflow now provides beta support for [ Interactive Notebooks
](https://cloud.google.com/dataflow/docs/guides/interactive-pipeline-
development) .

**VPC Service Controls**

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

##  April 08, 2020

**AI Platform Optimizer**

**FEATURE:**

AI Platform Optimizer is now available in [ beta
](https://cloud.google.com/products#product-launch-stages) .

AI Platform Optimizer is a black-box optimization service that helps you tune
hyperparameters in complex machine learning models.

Visit the [ AI Platform Optimizer overview ](https://cloud.google.com/ai-
platform/optimizer/docs/overview) to learn more about how it works. To get
started, try using AI Platform Optimizer to [ optimize a machine learning
model ](https://cloud.google.com/ai-platform/optimizer/docs/optimizing-ml-
model) or to [ optimize two functions at once ](https://cloud.google.com/ai-
platform/optimizer/docs/optimizing-multiple-objectives) .

**App Engine standard environment Python**

**CHANGED:**

Updated Python SDK to version 1.9.90

**BigQuery**

**FEATURE:**

BigQuery materialized views are now available as a [ beta
](https://cloud.google.com/products#product-launch-stages) release. For more
information, see [ Introduction to materialized views
](https://cloud.google.com/bigquery/docs/materialized-views-intro) .

**Cloud Data Loss Prevention**

**FEATURE:**

Added additional infoType detectors:

  * ` AZURE_AUTH_TOKEN `
  * ` GCP_API_KEY `

##  April 07, 2020

**Dataflow**

**FEATURE:**

Dataflow now [ supports
](https://cloud.google.com/dataflow/pricing#pricing_details) Dataflow Shuffle,
Streaming Engine, FlexRS, and the following [ regional endpoints
](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) in GA:

  * ` us-east4 ` (Northern Virginia) 
  * ` europe-west2 ` (London) 
  * ` europe-west3 ` (Frankfurt) 

##  April 06, 2020

**AI Platform Training**

**FIXED:**

[ Runtime version 2.1 ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list) now includes scikit-learn 0.22.1
instead of scikit-learn 0.22.

**Cloud Bigtable**

**FEATURE:**

Key Visualizer for Cloud Bigtable is now integrated into the [ Google Cloud
Console ](https://console.cloud.google.com) . The following enhancements have
been added:

  * Eligibility has been simplified to a minimum of 30 GB of data per table. 
  * You can now specify the start and end time for a scan. 
  * Performance data is now more recent. 
  * Your performance data is retained for 14 days. 

##  April 05, 2020

**Cloud Composer**

**FEATURE:**

Cloud Composer is now available in Salt Lake City ( ` us-west3 ` ).

##  April 03, 2020

**AI Platform Training**

**FEATURE:**

You can now use customer-managed encryption keys (CMEK) to protect data in
your AI Platform Training jobs. This feature is available in beta.

To learn about the benefits and limitations of using CMEK, and to walk through
configuring CMEK for a training job, read the [ guide to using CMEK with AI
Platform Training ](https://cloud.google.com/ai-platform/training/docs/cmek) .

**Access Context Manager**

**FEATURE:**

Beta release of the Access Context Manager Bulk API.

The Access Context Manager Bulk API can be used for operations such as
replacing all of your organization's access levels. For more information, see
[ Making bulk changes to access levels ](https://cloud.google.com/access-
context-manager/docs/bulk-operations) .

**AutoML Natural Language**

**CHANGED:**

Integration with [ VPC Service Controls ](https://cloud.google.com/vpc-
service-controls/docs/overview) is now in [ beta stage
](https://cloud.google.com/products/#product-launch-stages) .

**AutoML Tables**

**CHANGED:**

Integration with [ VPC Service Controls ](https://cloud.google.com/vpc-
service-controls/docs/overview) is now in [ beta stage
](https://cloud.google.com/products/#product-launch-stages) .

**AutoML Translation**

**CHANGED:**

Integration with [ VPC Service Controls ](https://cloud.google.com/vpc-
service-controls/docs/overview) is now in [ beta stage
](https://cloud.google.com/products/#product-launch-stages) .

**AutoML Vision Image Classification (ICN)**

**CHANGED:**

Integration with [ VPC Service Controls ](https://cloud.google.com/vpc-
service-controls/docs/overview) is now in [ beta stage
](https://cloud.google.com/products/#product-launch-stages) .

**AutoML Vision Object Detection**

**CHANGED:**

Integration with [ VPC Service Controls ](https://cloud.google.com/vpc-
service-controls/docs/overview) is now in [ beta stage
](https://cloud.google.com/products/#product-launch-stages) .

**Cloud Talent Solution Job Search**

**DEPRECATED:**

As of this date, Cloud Talent Solution Job Search v2 is no longer available.
Calls to v2 will result in error. The deprecation of v2 was first communicated
in August 2018.

**Dataproc**

**FEATURE:**

Added Presto and SparkR job type support to [ Dataproc Workflows
](https://cloud.google.com/dataproc/docs/concepts/workflows/overview) .

**FIXED:**

Fixed an [ Auto Zone Placement
](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-
zone) bug that incorrectly returned ` INVALID_ARGUMENT ` errors as ` INTERNAL
` errors, and didn't propagate these error messages to the user.

**VPC Service Controls**

**FEATURE:**

Beta support for bulk changes to service perimeters.

Using the beta release of Access Context Manager's Bulk API, you can perform
operations such as replacing all of your organization's service perimeters.
For more information, see [ Making bulk changes to service perimeters
](https://cloud.google.com/vpc-service-controls/docs/bulk-operations) .

##  April 02, 2020

**Anthos GKE deployed on AWS**

**FEATURE:**

Initial beta release of Anthos GKE on AWS

**CHANGED:**

The release improves upon earlier releases with:

  * **Improved reliability** : User clusters are now deployed in a high availability (HA) fashion, where both control plane instances as well as node pools can be placed across multiple availability zones. AWS Auto Scaling groups are also now used for resiliency. 

  * **Improved security** : Control plane instances for different user clusters are now isolated in separate security groups. Instance Metadata Service Version 2 (IMDSv2) is enabled to protect against SSRF attacks, and sensitive fields in EC2 metadata are now encrypted. 

  * **Easier to deploy** : The installation process for the management layer has been simplified and performs additional validation checks. It uses Terraform modules for flexible integration into different AWS environments, and customers can now leverage existing security groups and IAM resources to secure clusters. Documentation has been improved and expanded. 

  * **Future-proof storage stack** : We're now using the [ EBS CSI driver ](https://github.com/kubernetes-sigs/aws-ebs-csi-driver) to manage all AWS EBS volumes. The legacy, in-tree Kubernetes EBS driver has been removed entirely, and all upcoming storage features, such as snapshots, will be provided using CSI. 

  * **Updated Kubernetes version** : User clusters are now based on Kubernetes 1.15 and have passed open-source Kubernetes conformance tests. 

**BigQuery**

**FEATURE:**

[ BigQuery Reservations ](https://cloud.google.com/bigquery/docs/reservations-
intro) is now available in all [ BigQuery regions
](https://cloud.google.com/bigquery/docs/locations) .

**Config Connector**

**FIXED:**

Fixed the [ ComputeInstance idempotency issue
](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/103)

##  April 01, 2020

**Anthos GKE on-prem**

**ISSUE:**

When upgrading from version 1.2.2 to 1.3.0 by using the Bundle download in the
[ alternate upgrade method ](https://cloud.google.com/anthos/gke/docs/on-
prem/how-to/upgrading#alternate_upgrade_scenario) , a timeout might occur that
will cause your user cluster upgrade to fail. To avoid this issue, you must
perform the [ full upgrade process
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading) that
includes upgrading your admin workstation with the OVA file.

**Anthos Service Mesh**

**FIXED:**

1.4.7-asm.0

Contains the same fixes as OSS Istio 1.4.7. See [ Announcing Istio 1.4.7
](https://istio.io/news/releases/1.4.x/announcing-1.4.7/) for more
information.

**Cloud Identity and Access Management**

**FEATURE:**

When you [ use a service account key to access Google Cloud
](https://cloud.google.com/iam/docs/audit-logging/examples-service-
accounts#auth-service-account-key) , your audit logs now identify the key that
was used.

**Cloud Spanner**

**FEATURE:**

A [ beta ](https://cloud.google.com/products/#product-launch-stages) version
of the Cloud Spanner emulator is now available, enabling you to develop and
test Cloud Spanner applications locally. For more information, see [ Using the
Cloud Spanner Emulator ](https://cloud.google.com/spanner/docs/emulator) .

**Dataproc**

**FEATURE:**

Announcing the [ General Availability (GA)
](https://cloud.google.com/terms/launch-stages#launch-stages) release of [
Dataproc Presto job type
](https://cloud.google.com/dataproc/docs/reference/rest/v1/PrestoJob) , which
can be submitted to a cluster using the [ ` gcloud dataproc jobs submit presto
` ](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/presto)
command. Note: The [ Dataproc Presto Optional Component
](https://cloud.google.com/dataproc/docs/concepts/components/presto) must be
enabled when the cluster is created to submit a Presto job to the cluster.

**Google Cloud Marketplace Partners**

**FEATURE:**

If you sell Kubernetes apps on Google Cloud Marketplace, you can now configure
your app to target clusters where at least one node has a GPU. When users
deploy the app, only clusters with GPUs are shown as valid deployment targets.

[ Learn about modifying your app's ` schema.md ` to check for GPUs
](https://github.com/GoogleCloudPlatform/marketplace-k8s-app-
tools/blob/master/docs/schema.md#gpus) .

[ Read the overview of selling Kubernetes apps on Google Cloud Marketplace
](https://cloud.google.com/marketplace/docs/partners/kubernetes-solutions/) .

**VPC Service Controls**

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following integrations:

  * [ Container Analysis ](https://cloud.google.com/container-registry/docs/container-analysis)

##  March 31, 2020

**AI Platform Notebooks**

**FEATURE:**

AI Platform Notebooks is now [ Generally Available
](https://cloud.google.com/products#product-launch-stages) . Some integrations
with and specific features of AI Platform Notebooks are still in beta, such as
[ Virtual Private Cloud Service Controls ](https://cloud.google.com/ai-
platform/notebooks/docs/service-perimeter) , [ Cloud Identity and Access
Management (Cloud IAM) ](https://cloud.google.com/ai-
platform/notebooks/docs/iam) roles, and [ AI Platform Notebooks API
](https://cloud.google.com/ai-platform/notebooks/docs/reference/rest) .

**BigQuery**

**FEATURE:**

` INFORMATION_SCHEMA ` views for [ BigQuery reservations
](https://cloud.google.com/bigquery/docs/information-schema-reservations) are
now in public [ alpha ](https://cloud.google.com/products/?hl=EN#product-
launch-stages) .

**Cloud Composer**

**FEATURE:**

The new [ Composer monitoring dashboard
](https://cloud.google.com/composer/docs/monitoring-dashboard) is now in beta.

**Cloud Functions**

**CHANGED:**

Cloud Functions now supports [ Connecting to Cloud SQL
](https://cloud.google.com/sql/docs/mysql/connect-functions) at the [ General
Availability release level ](https://cloud.google.com/products/#product-
launch-stages) .

  * The Beta release introduced improved security when accessing Cloud SQL from functions via the ` /cloudsql ` filesystem path. Most functions have been automatically upgraded. In some cases, you may see warning messages in Stackdriver logging to help you complete the required upgrade steps. 

**Dialogflow**

**CHANGED:**

When using fulfillment, the ` WebhookResponse.payload ` field can now only be
used for two cases:

  * Custom data sent from your webhook service to a Dialogflow API caller. 
  * Google Assitant integration custom payload rich response messages. 

For all other [ custom payload rich response messages
](https://cloud.google.com/dialogflow/docs/intents-rich-messages#custom) , you
should use the ` WebhookResponse.fulfillment_mesages[].payload ` field.

**Google Cloud Armor**

**FEATURE:**

[ Google Cloud Armor ](https://cloud.google.com/armor) [ integration with
Cloud Security Command Center ](https://cloud.google.com/armor/docs/cscc-
findings) is generally available.

**Storage Transfer Service**

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
integration with [ VPC Service Controls ](https://cloud.google.com/vpc-
service-controls/docs/overview)

**FEATURE:**

Transfer service on-premises: [ Beta stage
](https://cloud.google.com/products/#product-launch-stages) integration with [
VPC Service Controls ](https://cloud.google.com/vpc-service-
controls/docs/overview)

**VPC Service Controls**

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following integrations:

  * [ AutoML Natural Language ](https://cloud.google.com/natural-language/automl/docs)
  * [ AutoML Tables ](https://cloud.google.com/automl-tables/docs)
  * [ AutoML Translation ](https://cloud.google.com/translate/automl/docs)
  * [ AutoML Video Intelligence ](https://cloud.google.com/video-intelligence/automl/docs)
  * [ AutoML Vision ](https://cloud.google.com/vision/automl/docs)
  * [ Artifact Registry ](https://cloud.google.com/artifacts/docs)

**Video Intelligence API**

**FEATURE:**

The following GA feature is available in the Video Intelligence API version
v1:

**Logo recognition** : Detect, track, and recognize the presence of over
100,000 brands and logos in video content. [ Learn more
](https://cloud.google.com/video-intelligence/docs/logo-recognition)

##  March 30, 2020

**BigQuery**

**FEATURE:**

[ Scripting ](https://cloud.google.com/bigquery/docs/reference/standard-
sql/scripting) and [ stored procedures
](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-
definition-language#create_procedure) are now [ Generally Available
](https://cloud.google.com/products/#product-launch-stages) .

**Cloud Deployment Manager**

**CHANGED:**

If your Python templates use features that are only for Python 2.x, your
templates will now continue to work until **June 2020** .

Learn about [ migrating your templates to Python 3
](https://cloud.google.com/deployment-manager/docs/migrate-to-python3) .

**Cloud Monitoring**

**FEATURE:**

You can now write time-series data for custom and Prometheus metrics at the
rate of 1 data point every 10 seconds. This was previously limited to 1 point
every minute.

**CHANGED:**

Data for custom and Prometheus metrics is now retained for 24 months.
Previously, the retention period was 6 weeks.

**Cloud NAT**

**FEATURE:**

[ Cloud NAT monitoring
](https://cloud.google.com/nat/docs/monitoring#monitoring) is available in
**General Availability** .

**Cloud Run**

**FEATURE:**

The Cloud Run revision details panel now surfaces build information if the [
Container Analysis API ](https://cloud.google.com/container-
registry/docs/container-analysis) has been enabled and the container has been
built with [ Cloud Build ](https://cloud.google.com/cloud-build) , as well as
source repository information if the container has been built by a [ Cloud
Build Trigger ](https://cloud.google.com/cloud-build/docs/running-
builds/create-manage-triggers) .

**Cloud Trace**

**FEATURE:**

You can now use [ OpenTelemetry ](https://opentelemetry.io/) with [ Go
](https://cloud.google.com/trace/docs/setup/go-ot) and [ Node.js
](https://cloud.google.com/trace/docs/setup/nodejs-ot) to instrument your
applications running on GKE and Compute Engine.

**Google Cloud Armor**

**CHANGED:**

[ Google Cloud Armor ](https://cloud.google.com/armor/sla) [ Service Level
Agreement ](https://cloud.google.com/armor/sla) is released.

**Migrate for Anthos**

**FEATURE:**

New ` migctl ` CLI for deploying Migrate for Anthos, creating and operating
migrations using a structured workflow and a migration processing cluster.

**FEATURE:**

Introducing a unified migration workflow across all supported VM sources --
VMware, AWS EC2, Azure VMs and Compute Engine VMs.

**FEATURE:**

Migrations are defined and operated using a Kubernetes CRD.

**FEATURE:**

Automated generation of a suggested migration plan (specified in a CRD), CI/CD
artifacts and deployment specs. The migration process now results in
extracting and generating container and deployment artifacts, including a
container image and a Dockerfile, extracted data in a persistent volume,
deployment/statefulSet, PVC and PV specs in an auto-generated YAML file for
easy workload deployment.

**FEATURE:**

The Migrate for Anthos software runtime layer now offers a compatibility
feature for older Java versions that are not container aware by reflecting the
correct resource allocations in the container's ` /proc ` file system.

**FEATURE:**

Migrate for Anthos v1.0 Marketplace deployment is now removed. Migrate for
Anthos v1.3 allows installation in v1.0 compatibility mode where needed.

**FEATURE:**

Preview features -- contact your Google Sales representative to enroll.

  * Migrating Windows VMs with IIS ASP.NET web applications to Windows 2019 containers on GKE. 
  * Processing migrations in Anthos on-prem. 

**ISSUE:**

**151505531, 150052607:** In some cases, migration can be stuck with no
progress. When running ` migctl migration status migration-name --verbose ` ,
you might see an event such as this:

    
    
    could not find attached GCE PD
    

**Workaround:** Delete the migration using ` migctl migration delete ` and re-
create it.

**ISSUE:**

**147211918:** In some cases, migration from AWS or Azure as a source can be
stuck with no progress. If this happens, run ` kubectl describe storageclass `
to view related events. You can also check the status of the matching Cloud
Details in Migrate for Compute Engine.

**ISSUE:**

**146699220:** When the source VM has a systemd service with a ` NICE ` config
property, the service might not start when running in a container.

**Workaround:** Remove the ` NICE ` property in the source VM before the
migration.

**ISSUE:**

**144896313:** Migration of Security-Enhanced Linux (SELinux) is not
supported.

**ISSUE:**

**149900626:** Some file systems not listed in [ Compatible VM operating
systems ](/release-notes/compatible-os-versions) may fail to migrate. When
running ` migctl migration logs migration-name ` , the logs in Cloud Logging
may show a message such as:

    
    
    failed to mount - exit status 32 - mount: /tmp/bootdir: unknown filesystem type 'LVM2\_member'.
    

**ISSUE:**

**152194161:** Your migrated workload container fails when running a cluster
with GKE nodes of type "COS". When you run the command ` kubectl logs
[podname] ` , you might see the following:

    
    
    apparmor.go:385] Couldn't set label to lxc-container-default - write /proc/1/attr/current: no such file or directory
    

This is an indication that the required AppArmor profiles are not installed on
the GKE nodes. To solve this, run ` migctl setup install --cos-runtime ` .

**ISSUE:**

**148334068:** When Migrating a physical VM from on-premises connected via
Migrate for Compute Engine, Migrate for Anthos attempts to optimize network
utilization and discards (rather than stream) blocks that are not in use on
the source VM file system. In some cases, this might cause VMware storage
sessions to time out. For assistance, please contact support.

**ISSUE:**

**GKE on-prem preview:** If a source was created with ` migctl source create `
using the wrong credentials, migrations will fail. Attempts to delete the
migration with ` migctl migration delete ` may hang in a "Terminating" state,
as in the following example:

    
    
    ubuntu@gke-on-prem-admin-appliance-1:~/$ ./migctl migration list
    NAME       PROCESS              STATE                   STATUS        PROGRESS   AGE
    my-vm-01   generate-artifacts   createSourceSnapshots   TERMINATING   [2/13]     
    

**Recommender**

**FEATURE:**

Insights is now available in beta. See the [ documentation
](https://cloud.google.com/recommender/docs/insights/using-insights) for
details.

**Service Directory**

**FEATURE:**

[ Service Directory ](https://cloud.google.com/service-directory/docs/) is
available in **Beta** .

##  March 29, 2020

**Network Intelligence Center**

**FEATURE:**

[ Performance Dashboard ](https://cloud.google.com/network-intelligence-
center/docs/performance-dashboard/concepts/overview) is now available in
**Beta** .

##  March 27, 2020

**AI Platform Prediction**

**FEATURE:**

[ AI Explanations ](https://cloud.google.com/ai-platform/prediction/docs/ai-
explanations/overview) now supports [ XRAI ](https://arxiv.org/abs/1906.02825)
, a new feature attribution method for image data.

The [ image tutorial
](https://colab.sandbox.google.com/github/GoogleCloudPlatform/ml-on-
gcp/blob/master/tutorials/explanations/ai-explanations-image.ipynb) has been
updated to include XRAI. In the tutorial, you can deploy an image
classification model using both integrated gradients and XRAI, and compare the
results.

**FEATURE:**

[ AI Explanations ](https://cloud.google.com/ai-platform/prediction/docs/ai-
explanations/overview) provides an [ approximation error
](https://cloud.google.com/ai-platform/prediction/docs/ai-explanations/using-
feature-attributions#using-approx-error) with your explanations results.

Learn more about the [ approximation error ](https://cloud.google.com/ai-
platform/prediction/docs/ai-explanations/using-feature-attributions#using-
approx-error) and how to improve your explanations results.

**FEATURE:**

AI Platform Prediction now supports the following regions for [ batch
prediction ](https://cloud.google.com/ai-platform/prediction/docs/batch-
predict) , in addition to those that were already supported:

  * ` us-west3 ` (Salt Lake City) 
  * ` europe-west2 ` (London) 
  * ` europe-west3 ` (Frankfurt) 
  * ` europe-west6 ` (Zurich) 
  * ` asia-south1 ` (Mumbai) 
  * ` asia-east2 ` (Hong Kong) 
  * ` asia-northeast1 ` (Tokyo) 
  * ` asia-northeast2 ` (Osaka) 
  * ` asia-northeast3 ` (Seoul) 

Note that ` asia-northeast1 ` was already available for online prediction.

See the [ full list of available regions ](https://cloud.google.com/ai-
platform/prediction/docs/regions) and read about [ pricing for each region
](https://cloud.google.com/ai-platform/prediction/pricing) .

**AI Platform Training**

**FEATURE:**

AI Platform Training now supports the following regions, in addition to those
that were already supported:

  * ` us-west3 ` (Salt Lake City) 
  * ` europe-west2 ` (London) 
  * ` europe-west3 ` (Frankfurt) 
  * ` europe-west6 ` (Zurich) 
  * ` asia-south1 ` (Mumbai) 
  * ` asia-east2 ` (Hong Kong) 
  * ` asia-northeast1 ` (Tokyo) 
  * ` asia-northeast2 ` (Osaka) 
  * ` asia-northeast3 ` (Seoul) 

Out of these regions, the following support [ training with NVIDIA Tesla T4
GPUs ](https://cloud.google.com/ai-platform/training/docs/using-gpus) :

  * ` europe-west2 `
  * ` asia-south1 `
  * ` aisa-northeast1 `
  * ` asia-northeast3 `

See the [ full list of available regions ](https://cloud.google.com/ai-
platform/training/docs/regions) and read about [ pricing for each region
](https://cloud.google.com/ai-platform/training/pricing) .

**BigQuery**

**FEATURE:**

BigQuery Column-level security is now available as a [ beta
](https://cloud.google.com/products#product-launch-stages) release. For more
information, see [ Introduction to BigQuery Column-level security
](https://cloud.google.com/bigquery/docs/column-level-security-intro) .

**Cloud SQL for PostgreSQL**

**FEATURE:**

PostgreSQL version 12 is now Beta. To start using PostgreSQL 12, see [
Creating instances ](https://cloud.google.com/sql/docs/postgres/create-
instance) .

**FEATURE:**

PostgreSQL version 10 is now generally available. To start using PostgreSQL
10, see [ Creating instances
](https://cloud.google.com/sql/docs/postgres/create-instance) .

**Dialogflow**

**CHANGED:**

The shutdown of the V1 API [ announced in November
](https://cloud.google.com/dialogflow/docs/release-notes#November_14_2019) has
been extended to May 31, 2020,

##  March 26, 2020

**Memorystore for Memcached**

**FEATURE:**

Beta release of Memorystore for Memcached.

##  March 25, 2020

**App Engine standard environment Python**

**CHANGED:**

Updated Python SDK to version 1.9.89.

**Cloud CDN**

**FEATURE:**

Cloud CDN [ custom origins ](https://cloud.google.com/cdn/docs/custom-origins-
overview) is available in **General Availability** . You can now use Cloud
CDN's distributed edge caching infrastructure to connect to an origin hosted
outside of GCP, such as on-premises or in another cloud.

**Config Connector**

**FEATURE:**

Add "Deletion Defender" workload -- a pod whose job is to ensure that only
resources meant to trigger a delete on the underlying API do so. If this
workload goes down for whatever reason, the controller is prevented from
performing deletions, thus protecting against accidental deletions in the case
of cascading deletions prompted by uninstalling CRDs.

**FEATURE:**

Add support for structured metadata list for ComputeInstance and
ComputeInstanceTemplate in the form of a spec.metadata field.

**Dataproc**

**FEATURE:**

Added pagination support to Clusters List methods to provide functionality to
the ` pageSize ` parameter, which is a part of the API. This feature allows
users to specify a page size to receive paginated data in the response. The
default page size is 200 and the max page size is 1000.

**FEATURE:**

Added alphabetical sort order to Workflow Templates List methods.

**FEATURE:**

Dataproc clusters can now be created on the GKE platform by setting the [ `
GkeClusterConfig `
](https://cloud.google.com/dataproc/docs/reference/rest/v1beta2/ClusterConfig#GkeClusterConfig)
instead of the [ ` GceClusterConfig `
](https://cloud.google.com/dataproc/docs/reference/rest/v1beta2/ClusterConfig#GceClusterConfig)
via the Beta API. This feature allows jobs to be submitted that will run on
the Kubernetes cluster.

**FEATURE:**

Announcing the [ Beta ](https://cloud.google.com/terms/launch-stages#launch-
stages) release of [ Dataproc - Ranger Top-Level Component
](https://cloud.google.com/dataproc/docs/concepts/components/ranger) and [
Dataproc - Solr Top-Level Component
](https://cloud.google.com/dataproc/docs/concepts/components/solr) .

**FEATURE:**

Announcing the [ General Availability (GA)
](https://cloud.google.com/terms/launch-stages#launch-stages) release of [
Dataproc - Presto Top-Level Component
](https://cloud.google.com/dataproc/docs/concepts/components/presto) .

**FEATURE:**

Announcing the [ General Availability (GA)
](https://cloud.google.com/terms/launch-stages#launch-stages) release of
Dataproc [ 1.5 images
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions#supported_cloud_dataproc_versions) .

**CHANGED:**

New [ sub-minor versions
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions#supported_cloud_dataproc_versions) of Dataproc images:
1.2.94-debian9, 1.3.54-debian9, 1.4.25-debian9, 1.5.0-debian10,
1.3.54-ubuntu18, 1.4.25-ubuntu18, and 1.5.0-ubuntu18

**CHANGED:**

**Image 1.5**  
Upgraded the Cloud Storage connector to version [ 2.1.1
](https://github.com/GoogleCloudDataproc/hadoop-
connectors/releases/tag/v2.1.1) .

**CHANGED:**

**Images 1.2 and 1.4**

Dataproc 1.4 will be the default image version after April 31, 2020.

Dataproc 1.2 will have no further releases after June 30, 2020.

**FIXED:**

**Images 1.3, 1.4, and 1.5**  
Fixed HDFS UI in the [ Component Gateway
](https://cloud.google.com/dataproc/docs/concepts/accessing/dataproc-gateways)
on HA clusters

**FIXED:**

Fixed issue where [ Jupyter
](https://cloud.google.com/dataproc/docs/concepts/components/jupyter) hangs
when loading a directory containing many large files. This also improves
responsiveness when listing directories.

**Dialogflow**

**CHANGED:**

The shutdown of 7 integrations [ announced in January
](https://cloud.google.com/dialogflow/docs/release-notes#January_06_2020) is
now extended to May 6th, 2020.

##  March 24, 2020

**Anthos Config Management**

**CHANGED:**

Anthos Policy Controller is now Generally Available

**CHANGED:**

Anthos Config Management now includes the generally-available version of
Config Connector.

**CHANGED:**

Anthos Config Management now supports the use of a [ Personal Access Tokens
](https://help.github.com/en/github/authenticating-to-github/creating-a-
personal-access-token-for-the-command-line) for authentication against
supported Git providers. More information can be found in [ Installing Anthos
Config Management ](https://cloud.google.com/anthos-config-
management/docs/how-to/installing) .

**CHANGED:**

Anthos Config Management now supports the use of an HTTP or HTTPS proxy to
connect with your Git host. More information can be found at [ Installing
Anthos Config Management ](https://cloud.google.com/anthos-config-
management/docs/how-to/installing) .

**BigQuery Data Transfer Service**

**CHANGED:**

BigQuery Data Transfer Service is now available in the [ Northern Virginia
(us-east4) region and the Salt Lake City (us-west3) region
](https://cloud.google.com/bigquery-transfer/docs/locations#locations) .

**Cloud Functions**

**CHANGED:**

Cloud Functions now supports [ network settings
](https://cloud.google.com/functions/docs/networking/network-settings) at the
[ General Availability release level
](https://cloud.google.com/products/#product-launch-stages) .

**CHANGED:**

Cloud Functions now supports [ VPC Service Controls
](https://cloud.google.com/functions/docs/securing/using-vpc-service-controls)
at the [ General Availability release level
](https://cloud.google.com/products/#product-launch-stages) .

**Cloud Profiler**

**CHANGED:**

Integration of Stackdriver Profiler with Virtual Private Cloud Service
Controls is now Generally Available. For more information, see [ VPC Service
Controls documentation ](https://cloud.google.com/vpc-service-controls/docs/)
.

**Cloud SQL for MySQL**

**FEATURE:**

Cloud SQL now supports 96-core machine types for MySQL, Postgres, and SQL
Server instances. For pricing-related information, see the [ Pricing page
](https://cloud.google.com/sql/pricing) .

**Cloud SQL for PostgreSQL**

**FEATURE:**

Cloud SQL now supports 96-core machine types for MySQL, Postgres, and SQL
Server instances. For pricing-related information, see the [ Pricing page
](https://cloud.google.com/sql/pricing) .

**Cloud SQL for SQL Server**

**FEATURE:**

Cloud SQL now supports 96-core machine types for MySQL, Postgres, and SQL
Server instances. For pricing-related information, see the [ Pricing page
](https://cloud.google.com/sql/pricing) .

**Memorystore for Redis**

**FEATURE:**

Released support for Redis version 5.0 (beta) on Memorystore for Redis. For
more details, see [ Supported versions
](https://cloud.google.com/memorystore/docs/redis/supported-versions) .

**VPC Service Controls**

**FEATURE:**

General availability for the following integration:

  * [ Cloud Functions ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_functions)

##  March 23, 2020

**Anthos**

**FEATURE:**

[ Anthos ](https://cloud.google.com/anthos) 1.3.0 is now available.

**Updated components:**

  * [ Anthos GKE on-prem release notes ](https://cloud.google.com/anthos/gke/docs/on-prem/release-notes)
  * [ Anthos Config Management release notes ](https://cloud.google.com/anthos-config-management/docs/release-notes)

**Anthos GKE on-prem**

**FEATURE:**

Anthos GKE on-prem 1.3.0-gke.16 is now available. To upgrade, see [ Upgrading
GKE on-prem ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/upgrading) .

GKE on-prem 1.3.0-gke.16 clusters run on Kubernetes 1.15.7-gke.32.

**FEATURE:**

A new installer helps you [ create and prepare the admin workstation
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/admin-workstation) .

**FEATURE:**

Support for [ vSAN ](https://docs.vmware.com/en/VMware-vSAN/index.html)
datastore on your admin and user clusters.

**FEATURE:**

In bundled load balancing mode, GKE on-prem provides and manages the [ Seesaw
load balancer ](https://github.com/google/seesaw) .

**FEATURE:**

The [ Authentication Plugin for Anthos
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/oidc) has been
integrated into and replaced with the Google Cloud command-line interface,
which improves the authentication process and provides the user consent flow
through ` gcloud ` commands.

**FEATURE:**

Added support for up to [ 100 nodes per user cluster
](https://cloud.google.com/anthos/gke/docs/on-prem/quotas) .

**FEATURE:**

The Cluster CA now signs the TLS certificates that the Kubelet API serves, and
the TLS certificates are auto-rotated.

**FEATURE:**

vSphere credential rotation is enabled. Users can now use Solution User
Certificates to authenticate to GKE deployed on-prem.

**FEATURE:**

` gkectl ` automatically uses the proxy URL from ` config.yaml ` to configure
the proxy on the admin workstation.

**FEATURE:**

Preview Feature: Introducing User cluster Nodepools. A _node pool_ is a group
of nodes within a cluster that all have the same configuration. In GKE on-prem
1.3.0, node pools are a preview feature in the user clusters. This feature
lets users create multiple node pools in a cluster, and update them as needed.

**CHANGED:**

The metric ` kubelet_containers_per_pod_count ` is changed to a [ histogram
metric ](https://prometheus.io/docs/concepts/metric_types/#histogram) .

**FIXED:**

Fixed an issue in the vSphere storage plugin that prevented vSphere storage
policies from working. [ This is an example
](https://github.com/kubernetes/examples/blob/master/staging/volumes/vsphere/vsphere-
volume-spbm-policy.yaml) of how you might use this feature.

**ISSUE:**

Prometheus + Grafana: two graphs on the **Machine** dashboard don't work
because of missing metrics: **Disk Usage** and **Disk Available** .

**ISSUE:**

All OOM events for containers trigger a SystemOOM event, even if they are
container/pod OOM events. To check whether an OOM is actually a SystemOOM,
check the kernel log for a message ` oom-kill:… ` . If ` oom_memcg=/ `
(instead of ` oom_memcg=/kubepods/… ` ), then it's a SystemOOM. If it's not a
SystemOOM, it's safe to ignore.

**ISSUE:**

**Affected versions: 1.3.0-gke.16**

If you configured a proxy in the ` config.yaml ` and also used a bundle other
than the full bundle ( [ static IP
](http://cloud.google.com/anthos/gke/docs/on-prem/how-to/install-static-
ips#bundlepath) | [ DHCP ](http://cloud.google.com/anthos/gke/docs/on-
prem/how-to/install-dhcp#bundlepath) ), you must append the ` --fast ` flag to
run ` gkectl check-config ` . For example: ` gkectl check-config --config
config.yaml --fast ` .

**ISSUE:**

Running the 1.3 version of the [ ` gkectl diagnose `
](http://cloud.google.com/anthos/gke/docs/on-prem/reference/gkectl/diagnose)
command might fail if your clusters:

  * Are older than Anthos GKE on-prem version 1.3. 
  * Include manually installed add-ons in the ` kube-system ` namespace. 

**BigQuery Data Transfer Service**

**FEATURE:**

BigQuery Data Transfer Service now supports [ Google Merchant Center data
transfers for pricing competitiveness
](https://cloud.google.com/bigquery/docs/merchant-center-
transfer#supported_reports) .

**Cloud Billing**

**FEATURE:**

**Billing health checks** is now available on your **Cloud Billing** account
**Overview** page in the **Cloud Console** . This feature automatically
analyzes the health of your **Cloud Billing** account, then displays the
results in a Billing health checks informational card, helping you avoid
common billing-related issues and to adopt our [ best-practice recommendations
](https://cloud.google.com/billing/docs/onboarding-checklist#checklist_3) . In
the info card, click **_View all health checks_ ** to view a page with
detailed recommendations, explanations, and action items to remedy issues that
could jeopardize the safety or condition of your Cloud Billing account.

To see the **Billing health checks** card, go to the [ Manage billing accounts
page ](https://console.cloud.google.com/billing) in the Cloud Console and sign
in, then select the name of the billing account you want to view. The Billing
Overview page is displayed with the **BILLING ACCOUNT OVERVIEW** tab selected.
Look for the card titled **Billing health checks** .

**Cloud Composer**

**FEATURE:**

Cloud Composer is now available in Sao Paulo ( ` southamerica-east1 ` ).

**Cloud Run**

**FIXED:**

You can now restrict which regions are available to deploy Cloud Run (fully
managed) services using an organization policy with a [ resource locations
constraint ](https://cloud.google.com/resource-manager/docs/organization-
policy/defining-locations) .

**Cloud Translation**

**CHANGED:**

The Cloud Translation Advanced API is migrating to a [ new quota system
](https://cloud.google.com/translate/quotas) that eliminates the distinction
between default and maximum limits.

This change will roll out gradually, starting on **March 30, 2020 and
continuing through April 30, 2020** . Since quotas define the usage limits for
a project or a user, the change could impact your billing.

**Config Connector**

**FIXED:**

Fixed label update issue on ContainerCluster
(https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/110)

**CHANGED:**

Bumped memory request and limit for the manager pod as resource usage has gone
up and the original limit of 256 Mi was found to not be sufficient for large
customers

**CHANGED:**

Changed admission webhooks to return non-200 error codes when denying
admission

**Game Servers**

**FEATURE:**

**Public beta release** Game Servers provides a fully managed offering of the
open source Agones project that runs on Kubernetes.

**Managed Service for Microsoft Active Directory**

**CHANGED:**

**GA pricing now in effect**

New pricing for Managed Microsoft AD is now in effect. Learn more about
standard [ Managed AD pricing ](https://cloud.google.com/managed-microsoft-
ad/pricing) and view [ pricing examples ](https://cloud.google.com/managed-
microsoft-ad/pricing#pricing_examples) .

**Security Command Center**

**FEATURE:**

The Notifications API is now in general availability. [ Get started with the
notifications API ](https://cloud.google.com/security-command-center/docs/how-
to-notifications) .

**CHANGED:**

The ` eventType ` field was removed from `
organizations.notificationConfigs.create ` in the v1 API. Learn more about [
creating a ` NotificationConfig ` ](https://cloud.google.com/security-command-
center/docs/how-to-api-manage-notifications#create-config) .

**Storage Transfer Service**

**FEATURE:**

Transfer Service for on-premises data is now generally available. For more
information, see [ Transfer Service for on-premises data Overview
](https://cloud.google.com/storage-transfer/docs/on-prem-overview) .

**FEATURE:**

Storage Transfer Service now offers Beta support for transfers from Microsoft
Azure Blob Storage.

##  March 20, 2020

**App Engine standard environment Java**

**CHANGED:**

  * Updated Java SDK to version 1.9.79. 
  * Updated Jetty to version 9.4.27. 

**AutoML Natural Language**

**CHANGED:**

AutoML Natural Language now supports TIFF files as training data and input for
predictions.

**CHANGED:**

AutoML Natural Language now supports classification and sentiment analysis in
[ 20 languages ](https://cloud.google.com/natural-
language/automl/docs/languages#classification) .

**Cloud Composer**

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.10.0-airflow-1.10.2 ` , ` composer-1.10.0-airflow-1.10.3 ` and ` composer-1.10.0-airflow-1.10.6 ` . The default is ` composer-1.10.0-airflow-1.10.2 ` . Upgrade your Cloud SDK to use features in this release. 

**FEATURE:**

  * Improved Composer logs: Composer Agent adds more detailed logs in Cloud Monitoring to describe the current stage of environment creation and provide better error messages if an operation fails. 
  * MySQL passwords are now stored in Kubernetes Secrets instead of the config map. 
  * You can now set the ` core.store_serialized_dags ` property to ` False ` after setting it to ` True ` . (Previously it was not possible to switch back.) 
  * Composer now uses Pip version 19.0.2 for both Python 2 and Python 3 Airflow environments. 
  * Added the Airflow property ` core.store_dag_code ` , which lets you see DAG code in the web UI while VPC-SC is enabled. 
  * New metrics have been added to the monitoring API. [ See the full list here ](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-composer) . 

**FIXED:**

  * Fixed an issue where Airflow database connection errors did not propagate correctly. 
  * Logs from the Composer Agent will now show the correct severity level in Cloud Monitoring. 
  * Fixed an issue where network tags added to environments did not propagate to the node pools created during the in-cluster image building. 
  * The Composer Agent will now wait for ` env_vars ` to be sent before starting the web server. 
  * Backported a fix for SQL proxy, which improves the stability of SQL connections inside workers. 
  * Added new scripts to handle synchronization of files from Customer Project buckets with tenant project buckets in DRS mode, so that DAG synchronization is not affected by long-running logs synchronization. 
  * Fixed an issue that prevented the creation of environments in the same VPC but different regions. 
  * Fixed an issue with updating the node count for Composer environments running versions 1.6.0 to 1.8.2. 
  * Installing PyPI packages from private repositories in the public Internet (specified in the pip.conf file) now works in private IP Composer environments without having to configure Cloud NAT. 

**Cloud Load Balancing**

**CHANGED:**

To help you get started quickly, added two new examples for external HTTP(S)
Load Balancing:

  * [ Setting up a simple external HTTP load balancer ](https://cloud.google.com/load-balancing/docs/https/ext-http-lb-simple)
  * [ Setting up a simple external HTTPS load balancer ](https://cloud.google.com/load-balancing/docs/https/ext-https-lb-simple)

**FEATURE:**

[ Health check logging ](https://cloud.google.com/load-balancing/docs/health-
check-logging) is now available in **Beta** .

**Cloud Natural Language API**

**CHANGED:**

The Natural Language API now supports [ additional languages
](https://cloud.google.com/natural-language/docs/languages#sentiment_analysis)
for sentiment analysis.

**Network Intelligence Center**

**FEATURE:**

[ Connectivity Tests ](https://cloud.google.com/network-intelligence-
center/docs/connectivity-tests/concepts/overview) and the [ Network Management
API ](https://cloud.google.com/network-intelligence-center/docs/connectivity-
tests/apis) are now Generally Available.

**Storage Transfer Service**

**FEATURE:**

Storage Transfer Service supports [ Pub/Sub notifications for transfer jobs
](https://cloud.google.com/storage-transfer/docs/pub-sub-transfer) for
external cloud provider to Cloud Storage transfers.

##  March 19, 2020

**Cloud Bigtable**

**FEATURE:**

You can now create a production [ Cloud Bigtable instance
](https://cloud.google.com/bigtable/docs/creating-instance) that has one or
two nodes per cluster. Prior to this change, production instances had a
minimum of three nodes per cluster, and the only way to create smaller
clusters was in a development instance.

**CHANGED:**

The [ Cloud Bigtable Service Level Agreement (SLA)
](https://cloud.google.com/bigtable/sla) has been updated.

**Cloud Spanner**

**FEATURE:**

The open-source [ C++ client library for Cloud Spanner
](https://github.com/googleapis/google-cloud-cpp-spanner) is now available. To
get started using C++ with Cloud Spanner, [ see this tutorial
](https://cloud.google.com/spanner/docs/getting-started/cpp) .

##  March 18, 2020

**Cloud Key Management Service**

**FEATURE:**

[ Importing keys ](https://cloud.google.com/kms/docs/importing-a-key) into
Cloud KMS software keys is generally available (GA).

**Cloud Load Balancing**

**FEATURE:**

Internal HTTP(S) Load Balancing now supports [ configurable idle timeouts
](https://cloud.google.com/load-
balancing/docs/l7-internal#timeouts_and_retries) .

**FEATURE:**

Cloud IAM Conditions now supports [ forwarding rule attributes
](https://www.cloud.google.com/load-balancing/docs/access-control/iam-
conditions) . You can use these attributes to specify the types of forwarding
rules that a member can create. This feature is available in **General
Availability** .

**Config Connector**

**CHANGED:**

miscellaneous bug fixes and improvements

**Dataproc**

**CHANGED:**

Added the following flag to the ` gcloud dataproc clusters update ` command:

  * ` --num-secondary-workers `

**DEPRECATED:**

The following flag to ` gcloud dataproc clusters update ` has been deprecated:

  * ` --num-preemptible-workers `

See the related change, above, for the new flag to use in place of this
deprecated flag.

