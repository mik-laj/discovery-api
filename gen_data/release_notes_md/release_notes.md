#  Google Cloud release notes

The following release notes cover the most recent changes over the last 30
days. For a comprehensive list, see the [ individual product release note
pages ](/release-notes/all) .

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/gcp-release-notes.xml `

##  July 21, 2020

**AutoML Video Intelligence Object Tracking**

**CHANGED:**

In April 2020, a model upgrade for the AutoML Video Object Tracking feature
was released. This release is for non-downloadable models only. Models trained
after April 2020 may show improvements in the evaluation results.

**Compute Engine**

**FEATURE:**

You can now create _balanced persistent disks_ , in addition to standard and
SSD persistent disks. Balanced persistent disks are an alternative to SSD
persistent disks that balance performance and cost. For more information, see
[ Persistent disk types
](https://cloud.google.com/compute/docs/disks/index#disk-types) .

**Istio on Google Kubernetes Engine**

**FIXED:**

**Istio 1.4.10-gke.4**

Fixes known security issues with the same fixes as [ OSS Istio 1.4.10
](https://istio.io/news/releases/1.4.x/announcing-1.4.10/)

**Traffic Director**

**FEATURE:**

Traffic Director supports proxyless gRPC applications in General Availability.
In this deployment model, gRPC applications can participate in a service mesh
without needing a sidecar proxy.

##  July 20, 2020

**AI Platform Training**

**FEATURE:**

[ Customer-managed encryption keys (CMEK) for AI Platform Training
](https://cloud.google.com/ai-platform/training/docs/cmek) is now generally
available.

**FEATURE:**

The [ VPC Service Controls integration with AI Platform Training
](https://cloud.google.com/ai-platform/training/docs/vpc-service-controls) is
now generally available.

**FEATURE:**

You can now train a PyTorch model on AI Platform Training by [ using a pre-
built PyTorch container ](https://cloud.google.com/ai-
platform/training/docs/getting-started-pytorch) . Pre-built PyTorch containers
are available in beta.

**Cloud Storage**

**FEATURE:**

[ Detailed audit logging mode ](https://cloud.google.com/storage/docs/org-
policy-constraints#audit-logging) launched.

**Identity and Access Management**

**CHANGED:**

We are delaying the upcoming changes for [ deleted members that are bound to a
role ](https://cloud.google.com/iam/docs/release-notes#July_01_2020) . These
changes will take effect starting on August 31, 2020.

**Secret Manager**

**FEATURE:**

Secret Manager adds support for the following curated Cloud IAM roles:

  * Secret Manager Secret Version Adder ( ` roles/secretmanager.secretVersionAdder ` ) 
  * Secret Manager Secret Version Manager ( ` roles/secretmanager.secretVersionManager ` ) 

To learn more, see [ IAM and access control ](https://cloud.google.com/secret-
manager/docs/access-control) .

**VPC Service Controls**

**FEATURE:**

General availability for the following integration:

  * [ AI Platform Training ](https://cloud.google.com/ai-platform/training/docs/vpc-service-controls)

##  July 17, 2020

**App Engine standard environment Java**

**CHANGED:**

  * Updated Java SDK to version 1.9.81 

**AutoML Translation**

**FEATURE:**

For test data, added support for the ` .tmx ` file type when evaluating
existing models. For more information, see [ Evaluating models
](https://cloud.google.com/translate/automl/docs/evaluate#evaluate_and_compare_models_using_a_new_test_set)
.

**Compute Engine**

**FEATURE:**

The Organization Policy for [ restricting protocol forwarding creation
](https://cloud.google.com/compute/docs/protocol-
forwarding#enforcing_protocol_forwarding_settings_across_a_project_folder_or_organization)
has launched into **Beta** .

**Dataproc**

**FEATURE:**

Dataproc now uses [ Shielded VMs ](https://cloud.google.com/security/shielded-
cloud/shielded-vm) for Debian 10 and Ubuntu 18.04 clusters by default.

**FEATURE:**

The ` Proxy-Authorization ` header is accepted in place of ` Authorization `
to authenticate to Component Gateway to the backend for programmatic API
calls. If ` Proxy-Authorization ` is set to a bearer token, Component Gateway
will forward the ` Authorization ` header if it does not contain a bearer
token.

For example, this allows setting both ` Proxy-Authorization: Bearer <google-
access-token> ` as well as setting ` Authorization: Basic ... ` to
authenticate to HiveServer2 with HTTP basic auth.

**FEATURE:**

Added support for Zeppelin Spark and shell interpreters in [ Kerberized
clusters ](https://cloud.google.com/dataproc/docs/concepts/configuring-
clusters/security) by default.

**CHANGED:**

New [ sub-minor versions
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions#supported_dataproc_versions) of Dataproc images: 1.3.63-debian10,
1.3.63-ubuntu18, 1.4.34-debian10, 1.4.34-ubuntu18, 1.5.9-debian10,
1.5.9-ubuntu18, 2.0.0-RC5-debian10, and 2.0.0-RC5-ubuntu18.

**CHANGED:**

Image 2.0 preview:

  * Updated Pig ` 0.18.0-SNAPHOT ` to [ 0b2066a revision ](https://github.com/apache/pig/commit/0b2066a6fd9e2907210c5dff1c480f017889425b) to fix Hive 3.1 compatibility ( [ PIG-4764 ](https://issues.apache.org/jira/browse/PIG-4764) ). 

**FIXED:**

If a project's regional Dataproc [ staging bucket
](https://cloud.google.com/dataproc/docs/concepts/configuring-
clusters/staging-bucket) is manually deleted, it will be recreated
automatically when a cluster is subsequently created in that region.

##  July 16, 2020

**BigQuery**

**FEATURE:**

BigQuery GIS now supports two new functions, ` ST_CONVEXHULL ` and ` ST_DUMP `
:

  * ` ST_CONVEXHULL ` returns the smallest convex ` GEOGRAPHY ` that covers the input. 
  * ` ST_DUMP ` returns an ` ARRAY ` of simple ` GEOGRAPHY ` s where each element is a component of the input ` GEOGRAPHY ` . 

For more information, see the [ ` ST_CONVEXHULL `
](https://cloud.google.com/bigquery/docs/reference/standard-
sql/geography_functions#st_convexhull) and [ ` ST_DUMP `
](https://cloud.google.com/bigquery/docs/reference/standard-
sql/geography_functions#st_dump) reference pages.

**Cloud Data Fusion**

**FEATURE:**

Cloud Data Fusion version 6.1.3 is now available. This version includes
performance improvements and minor bug fixes.

  * Improved performance of Joiner plugins, aggregators, program startup, and previews. 
  * Added support for custom images. You can select a custom Dataproc image by specifying the image URI. 
  * Added support for rendering large schemas (>1000 fields) in the pipelines UI. 
  * Added payload compression support to the messaging service. 

**Cloud Load Balancing**

**FEATURE:**

The Organization Policy for [ restricting load balancer creation
](https://cloud.google.com/load-balancing/docs/org-policy-constraints) has
launched into **Beta** .

**Compute Engine**

**CHANGED:**

SSD persistent disks on certain machine types now have a maximum write
throughput of 1,200 MB/s. To learn more about the requirements to reach these
limits, see [ Block storage performance
](https://cloud.google.com/compute/docs/disks/performance#size_price_performance)
.

**FEATURE:**

You can now [ suspend and resume
](https://cloud.google.com/compute/docs/instances/suspend-resume-instance)
your VM instances. This feature is available in **Beta** .

**Config Connector**

**FEATURE:**

Add support for allowing fields not specified by the user to be externally-
managed (i.e. changeable outside of Config Connector). This feature can be
enabled for a resource by enabling K8s server-side apply for the resource,
which will be the default for all K8s resources starting in K8s 1.18. More
detailed docs about the feature coming soon.

**FEATURE:**

Operator improvement: add support for cluster-mode set-ups, which allows users
to use one Google Service Account for all namespaces in their cluster. This is
very similar to the traditional "Workload Identity" installation set-up.

**FIXED:**

Fix ` ContainerCluster ` validation issue ( [ Issue #242
](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/242) ).

**FIXED:**

Fix OOM issue for the ` cnrm-resource-stats-recorder ` pod ( [ Issue #239
](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/239) ).

**FEATURE:**

Add support for ` projectViewer ` prefix for members in ` IAMPolicy ` and `
IAMPolicyMember ` ( [ Issue #234
](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/234) ).

**CHANGED:**

Reduce ` spec.revisionHistoryLimit ` for the ` cnrm-stats-recorder ` and `
cnrm-webhook-manager ` Deployments from 10 (the default) to 1.

##  July 15, 2020

**AutoML Vision Image Classification (ICN)**

**CHANGED:**

**TFLite Edge model update**

TFLite edge models are now enhanced with metadata. Models trained in the next
6 months will be backwards compatible as separate metadata and label files are
included. TFLite models trained after this time may not be backwards
compatible.

For more information see:

  * [ Metadata information and how to add metadata to a TFLite model ](https://www.tensorflow.org/lite/convert/metadata)
  * [ Integrate models with metadata ](https://www.tensorflow.org/lite/guide/codegen)
  * [ Process input and output data with the TensorFlow Lite Support Library ](https://www.tensorflow.org/lite/guide/lite_support)

**BigQuery ML**

**FEATURE:**

Data split and validation options are now available for [ AutoML Table model
training ](https://cloud.google.com/bigquery-ml/docs/reference/standard-
sql/bigqueryml-syntax-create-automl) .

**Cloud Data Loss Prevention**

**CHANGED:**

Added [ infoType detector ](https://cloud.google.com/dlp/docs/infotypes-
reference) :

  * ISRAEL_IDENTITY_CARD_NUMBER 

**Cloud Functions**

**FEATURE:**

Cloud Functions has added support for a new runtime, [ Node 12
](https://cloud.google.com/functions/docs/concepts/nodejs-runtime) , in Beta.

Cloud Functions has added support for a new runtime, [ Python 3.8
](https://cloud.google.com/functions/docs/concepts/python-runtime) , in Beta.

**Cloud Spanner**

**FEATURE:**

You can now run SQL queries to retrieve [ read statistics
](https://cloud.google.com/spanner/docs/introspection/read-statistics) for
your database over recent one-minute, 10-minute, and one-hour time periods.

##  July 14, 2020

**AI Platform Prediction**

**FEATURE:**

[ VPC Service Controls ](https://cloud.google.com/vpc-service-
controls/docs/overview) now supports AI Platform Prediction. Learn [ how to
use a service perimeter to protect online prediction
](https://cloud.google.com/ai-platform/prediction/docs/vpc-service-controls) .
This functionality is in beta.

**Artifact Registry**

**FEATURE:**

You can now use Customer-Managed Encryption Keys (CMEK) to protect repository
data in Artifact Registry. For more information, see [ Enabling customer-
managed encryption keys ](https://cloud.google.com/artifact-
registry/docs/cmek) .

**Cloud Key Management Service**

**FEATURE:**

Cloud HSM resources are available in the ` us-west4 ` and ` asia-southeast2 `
regions. Cloud KMS resources were already available in these regions.

For information about which [ Cloud Locations
](https://cloud.google.com/about/locations/) are supported by Cloud KMS, Cloud
HSM, and Cloud EKM, see the [ Cloud KMS regional locations
](https://cloud.google.com/kms/docs/locations#regional) .

**VPC Service Controls**

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following integration:

  * [ AI Platform Prediction ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_aip-prediction)

##  July 13, 2020

**AI Platform Training**

**FEATURE:**

You can now configure a training job to run using a [ custom service account
](https://cloud.google.com/ai-platform/training/docs/custom-service-account) .
Using a custom service account can help you customize which Google Cloud
resources your training code can access.

This feature is available in beta.

**BigQuery**

**FEATURE:**

The Standard SQL statement [ ` ASSERT `
](https://cloud.google.com/bigquery/docs/reference/standard-sql/debugging-
statements) is now supported. You can use [ ` ASSERT `
](https://cloud.google.com/bigquery/docs/reference/standard-sql/debugging-
statements) to validate that data matches specified expectations.

**Cloud Bigtable**

**CHANGED:**

The default data points used for CPU utilization charts on the [ Cloud
Bigtable Monitoring ](https://cloud.google.com/bigtable/docs/monitoring-
instance) page have changed. Previously, data points on the charts reflected
the mean for a displayed alignment period. Now the data points reflect the
maximum for the alignment period. This change ensures that charts clearly show
the peaks that are important for monitoring the health of a Cloud Bigtable
instance.

**Cloud CDN**

**CHANGED:**

Added a new [ setup guide ](https://cloud.google.com/cdn/docs/setting-up-cdn-
with-external-origin) for custom (external) origins with Cloud CDN and
external HTTP(S) Load Balancing.

**Cloud Load Balancing**

**FEATURE:**

Internal TCP/UDP load balancers now support [ regional health checks
](https://cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks)
. To configure, see [ Health checks for backend services
](https://cloud.google.com/load-balancing/docs/health-checks#hc-to-bes) . This
feature is supported in **General Availability** .

**Cloud Run**

**FEATURE:**

The Cloud Run user interface now allows you to easily [ set up Continuous
Deployment from Git using Cloud Build
](https://cloud.google.com/run/docs/continuous-deployment-with-cloud-build)

**Dataprep by Trifacta**

**FEATURE:**

**Introducing Cloud Dataprep Premium by TRIFACTA INC. and Cloud Dataprep
Standard by TRIFACTA INC.:** You can now upgrade your existing Cloud Dataprep
by TRIFACTA INC. projects to unlock advanced features, such as broader API
access and relational connectivity. To see the full set of new capabilities
and use cases, see [ Google Cloud Dataprep by Trifacta Pricing
](https://www.trifacta.com/products/pricing/cloud-dataprep/) .

  * These two product tiers are available through the [ Google Cloud Platform Marketplace ](https://console.cloud.google.com/marketplace/product/endpoints/cloud-dataprep-editions-v2) . 
    * Cloud Dataprep Premium by TRIFACTA INC. enables Fine Grained Data Access Control, which requires additional permissions within the project. For more information on these permissions, see [ Required User Permissions ](https://cloud.google.com/dataprep/docs/html/Required-User-Permissions_158400598.html) . 
    * For more information, see [ Getting Started with Cloud Dataprep ](https://cloud.google.com/dataprep/docs/html/Getting-Started-with-Cloud-Dataprep_158401056.html) . 
  * **Important:** All existing Cloud Dataprep by TRIFACTA INC. projects are unchanged. You can upgrade individual projects through the GCP Marketplace to unlock the new functionality. 

**FEATURE:**

**Relational connectivity:** Connect to relational sources to import data and,
where supported, write results.

  * **Feature Availability:** This feature is available in Cloud Dataprep Premium by TRIFACTA INC. 
  * The following relational connections are supported: 
    * [ Create Oracle Connections ](https://cloud.google.com/dataprep/docs/html/Create-Oracle-Connections_158401064.html)
    * [ Create PostgreSQL Connections ](https://cloud.google.com/dataprep/docs/html/Create-PostgreSQL-Connections_158401065.html)
    * [ Create SQL Server Connections ](https://cloud.google.com/dataprep/docs/html/Create-SQL-Server-Connections_158401066.html)
    * [ Create Salesforce Connections ](https://cloud.google.com/dataprep/docs/html/Create-Salesforce-Connections_158401069.html)
  * For more information, see [ Connect ](https://cloud.google.com/dataprep/docs/html/Connect_158401062.html) . 

**FEATURE:**

**Advanced Cloud Dataflow execution options:** Specify additional job
execution options at the project level or for individual jobs.

  * **Feature Availability:** This feature is available in Cloud Dataprep Premium by TRIFACTA® INC. 
  * Assign scaling algorithms for managing Google Compute Engine instances or define minimum and maximum workers to use. 
  * Specify the service account and any billing labels to apply to your jobs. 
  * For more information: 
    * Project-level settings: see [ Project Settings Page ](https://cloud.google.com/dataprep/docs/html/Project-Settings-Page_136161418.html) . 
    * Individual job executions: see [ Dataflow Execution Settings ](https://cloud.google.com/dataprep/docs/html/Dataflow-Execution-Settings_154091521.html) . 

**FEATURE:**

**Introducing plans:** A plan is a sequence of tasks on one or more flows that
can be scheduled.

  * **Feature Availability:** This feature is available in Cloud Dataprep Premium by TRIFACTA INC. 
  * **NOTE:** In this release, the only type of task that is supported is Run Flow. 
  * For more information on plans, see [ Plans Page ](https://cloud.google.com/dataprep/docs/html/Plans-Page_158401272.html) . 

  * For more information on orchestration in general, see [ Overview of Operationalization ](https://cloud.google.com/dataprep/docs/html/Overview-of-Operationalization_151992519.html) . 

**FEATURE:**

* **_Dataflow execution in non-local VPC:_ ** * You can now execute your Cloud Dataflow jobs on a non-local or shared virtual private network (VPC). 

  * **NOTE:** To accommodate a wider range of shared VPCs configuration, subnetworks must be specified by full URL. See Changes below. 
  * Project owners can set these execution options for the entire project. See [ Project Settings Page ](https://cloud.google.com/dataprep/docs/html/Project-Settings-Page_136161418.html) . 

**CHANGED:**

**Subnetwork specified by URL:** When you are specifying the subnetwork where
to execute your Cloud Dataflow jobs, you must now specify the subnetwork using
a URL.

  * **Tip:** This feature can be used when Cloud Dataprep by TRIFACTA INC. is configured to execute Cloud Dataflow jobs to run within a shared VPC hosted in a project other than the current project. 
  * Previously, you could specify the subnetwork by name. However, non-local subnetwork values could not be specified in this manner. 
  * For more information, see [ Dataflow Execution Settings ](https://cloud.google.com/dataprep/docs/html/Dataflow-Execution-Settings_154091521.html) . 

**Google Cloud Marketplace**

**CHANGED:**

The IAM permissions required for purchasing the following solutions from
Google Cloud Marketplace have changed:

  * Apache Kafka® on Confluent Cloud™ 
  * DataStax Astra for Apache Cassandra 
  * Elasticsearch Service on Elastic Cloud 
  * NetApp Cloud Volumes Service 
  * Redis Enterprise Cloud 

If you use [ custom roles ](https://cloud.google.com/iam/docs/understanding-
custom-roles) to purchase these solutions, you must update the custom roles to
include the permissions described in [ Access Control for Google Cloud
Marketplace ](https://cloud.google.com/marketplace/docs/access-control) .

Specifically, if your custom role includes the ` billing.subscriptions.create
` permission, you must update it to include the `
consumerprocurement.orders.place ` and the `
consumerprocurement.accounts.create ` permissions.

If you use the [ Billing Administrator
](https://cloud.google.com/iam/docs/understanding-roles#billing-roles) role to
purchase these solutions, you don't need to take any action.

**Secret Manager**

**FEATURE:**

Secret Manager resources can now be stored in the ` australia-southeast1 `
region. To learn more, see [ Locations ](https://cloud.google.com/secret-
manager/docs/locations/) .

##  July 10, 2020

**Anthos Service Mesh**

**FIXED:**

**1.6.5-asm.1, 1.5.8-asm.0, and 1.4.10-asm.4**

Fixes the security issue, [ ISTIO-SECURITY-2020-008
](https://istio.io/latest/news/security/istio-security-2020-008) , with the
same fixes as Istio 1.6.5 and Istio 1.5.8. These fixes were backported to
1.4.10-asm.4. For more information, see the Istio release notes:

  * [ Istio 1.6.5 ](https://istio.io/latest/news/releases/1.6.x/announcing-1.6.5/)

  * [ Istio 1.5.8 ](https://istio.io/latest/news/releases/1.5.x/announcing-1.5.8/)

**Cloud Billing**

**FEATURE:**

The [ Cost Table report ](https://cloud.google.com/billing/docs/how-to/cost-
table) functionality has been updated to add a **Table configuration**
interface that replaces the previous _Group by_ and _Label_ selectors. Use the
new **Table configuration** dialog to choose a **Label key** and select your
**Group by** options. Additionally, the available **Group by** options have
been enhanced to include a new **Custom grouping** option. Use custom grouping
to view a [ nested cost table ](https://cloud.google.com/billing/docs/how-
to/cost-table#nested_table_view) with your costs grouped by up to three
dimensions that you choose, including label values. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/cost-table) for more details.

**Cloud Functions**

**FEATURE:**

Cloud Functions is now available in the following regions:

  * ` us-west2 ` (Los Angeles) 
  * ` us-west4 `
  * ` southamerica-east1 ` (Sao Paulo) 
  * ` asia-northeast2 ` (Osaka) 

See [ Cloud Functions Locations
](https://cloud.google.com/functions/docs/locations) for details.

**Cloud Monitoring**

**FEATURE:**

SLO monitoring for microservices is now Generally Available in the Cloud
Console. This feature lets you create service-level objectives (SLOs) and set
up alerting policies to monitor their performance using auto-generated
dashboards with metrics, logs, and alerts in a single place. For more
information, see [ SLO monitoring
](https://cloud.google.com/stackdriver/docs/solutions/slo-monitoring) .

**Dataproc**

**FEATURE:**

Added ` --temp-bucket ` flag to ` gcloud dataproc clusters create ` and `
gcloud dataproc workflow-templates set-managed-cluster ` to allow users to
configure a Cloud Storage bucket that stores ephemeral cluster and jobs data,
such as Spark and MapReduce history files.

**FEATURE:**

Extended Jupyter to support notebooks stored on VM persistent disk. This
change modifies the Jupyter contents manager to create two virtual top-level
directories, named ` GCS ` , and ` Local Disk ` . The ` GCS ` directory points
to the Cloud Storage location used by previous versions, and the ` Local Disk
` directory points to the persistent disk of the VM running Jupyter.

**FEATURE:**

Dataproc images now include the [ oauth2l ](https://github.com/google/oauth2l)
command line tool. The tool is installed in ` /usr/local/bin ` , which is
available to all users in the VM.

**CHANGED:**

New [ sub-minor versions
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions#supported_dataproc_versions) of Dataproc images: 1.2.102-debian9,
1.3.62-debian9, 1.4.33-debian9, 1.3.62-debian10, 1.4.33-debian10,
1.5.8-debian10, 1.3.62-ubuntu18, 1.4.33-ubuntu18, 1.5.8-ubuntu18,
2.0.0-RC4-debian10, 2.0.0-RC4-ubuntu18

**FIXED:**

  * Images 1.3 - 1.5: 

    * Fixed [ HIVE-11920 ](https://issues.apache.org/jira/browse/HIVE-11920) : ADD JAR failing with URL schemes other than file/ivy/hdfs. 
  * Images 1.3 - 2.0 preview: 

    * Fixed [ TEZ-4108 ](https://issues.apache.org/jira/browse/TEZ-4108) : NullPointerException during speculative execution race condition. 

**FIXED:**

Fixed a race condition that could nondeterministically cause Hive-WebHCat to
fail at startup when HBase is not enabled.

##  July 09, 2020

**Cloud SQL for PostgreSQL**

**FEATURE:**

Cloud SQL now supports [ point-in-time recovery (PITR) for PostgreSQL
](https://cloud.google.com/sql/docs/postgres/backup-recovery/pitr) . Point-in-
time recovery helps you recover an instance to a specific point in time. For
example, if an error causes a loss of data, you can recover a database to its
state before the error occurred.

**Config Connector**

**FEATURE:**

Added support for ` SecretManagerSecret `

**Managed Service for Microsoft Active Directory**

**FEATURE:**

The [ Managed Microsoft AD SLA ](https://cloud.google.com/managed-microsoft-
ad/sla) has been published.

##  July 08, 2020

**App Engine flexible environment .NET**

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs) . Notably, this feature allows
you to use [ Cloud CDN ](https://cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

**App Engine flexible environment Go**

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs) . Notably, this feature allows
you to use [ Cloud CDN ](https://cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

**App Engine flexible environment Java**

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs) . Notably, this feature allows
you to use [ Cloud CDN ](https://cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

**App Engine flexible environment Node.js**

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs) . Notably, this feature allows
you to use [ Cloud CDN ](https://cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

**App Engine flexible environment PHP**

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs) . Notably, this feature allows
you to use [ Cloud CDN ](https://cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

**App Engine flexible environment Ruby**

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs) . Notably, this feature allows
you to use [ Cloud CDN ](https://cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

**App Engine flexible environment custom runtimes**

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs) . Notably, this feature allows
you to use [ Cloud CDN ](https://cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

**App Engine standard environment Go**

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs) . Notably, this feature allows
you to use [ Cloud CDN ](https://cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs) . Notably, this feature allows
you to use [ Cloud CDN ](https://cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

**App Engine standard environment Java**

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs) . Notably, this feature allows
you to use [ Cloud CDN ](https://cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs) . Notably, this feature allows
you to use [ Cloud CDN ](https://cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

**App Engine standard environment Node.js**

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs) . Notably, this feature allows
you to use [ Cloud CDN ](https://cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

**App Engine standard environment PHP**

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs) . Notably, this feature allows
you to use [ Cloud CDN ](https://cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs) . Notably, this feature allows
you to use [ Cloud CDN ](https://cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

**App Engine standard environment Python**

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs) . Notably, this feature allows
you to use [ Cloud CDN ](https://cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs) . Notably, this feature allows
you to use [ Cloud CDN ](https://cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

**App Engine standard environment Ruby**

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine via [
Serverless network endpoint groups ](https://cloud.google.com//load-
balancing/docs/negs/setting-up-serverless-negs) . Notably, this feature allows
you to use [ Cloud CDN ](https://cloud.google.com/cdn) with App Engine.  
This feature is available in Beta.

##  July 07, 2020

**Cloud Composer**

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.10.6-airflow-1.10.2 ` , ` composer-1.10.6-airflow-1.10.3 ` and ` composer-1.10.6-airflow-1.10.6 ` . The default is ` composer-1.10.6-airflow-1.10.3 ` . Upgrade your Cloud SDK to use features in this release. 

  * **For Airflow 1.10.6 and later:** The Airflow config property ` [celery] pool ` is now blocked. 

  * The ` [core]sql_alchemy_pool_recycle ` Airflow setting has been modified to improve SQL connection reliability. 

**FIXED:**

  * Fixed an issue with Airflow 1.10.6 environments where task logs were not visible in the UI when DAG serialization was enabled. 
  * It is now possible to upgrade from Composer versions 1.1.1, 1.2.0, 1.3.0, 1.4.0, 1.4.1, 1.4.2, 1.5.0, and 1.5.2 to the newest version. 

**Cloud Functions**

**FEATURE:**

External HTTP(S) Load Balancing is now supported for Google Cloud Functions
via [ Serverless network endpoint groups ](https://cloud.google.com/load-
balancing/docs/negs/setting-up-serverless-negs) .

Notably, this feature allows you to use [ Cloud CDN
](https://cloud.google.com/cdn) and [ Cloud Armor
](https://cloud.google.com/armor) with Google Cloud Functions.

This feature is available in Beta.

**Cloud Load Balancing**

**FEATURE:**

External HTTP(S) Load Balancing is now supported for App Engine, Cloud
Functions, and Cloud Run services. To configure this, you will need to use a
new type of network endpoint group (NEG) called a [ Serverless NEG
](https://cloud.google.com/load-balancing/docs/negs/setting-up-serverless-
negs) .

This feature is available in Beta.

**Cloud Monitoring**

**CHANGED:**

Monitoring Query Language (MQL) is now Generally Available. MQL is an
expressive, text-based interface to Cloud Monitoring time-series data. With
MQL, you can create charts you can't create any other way. You can access MQL
from both the Cloud Console and the Monitoring API. For more information, see
[ Introduction to Monitoring Query Language
](https://cloud.google.com/monitoring/mql/) .

**Cloud Run**

**FEATURE:**

External HTTP(S) Load Balancing is now supported for Cloud Run services via [
Serverless network endpoint groups ](https://cloud.google.com/load-
balancing/docs/negs/setting-up-serverless-negs) .  
Notably, this feature allows you to use [ Cloud CDN
](https://cloud.google.com/cdn) and multi-region load balancing.  
This feature is available in Beta.

**Dataproc**

**FEATURE:**

Announcing the [ General Availability (GA)
](https://cloud.google.com/products#product-launch-stages) release of [
Dataproc Component Gateway
](https://cloud.google.com/dataproc/docs/concepts/accessing/dataproc-gateways)
, which provides secure access to web endpoints for Dataproc default and
optional components.

**Traffic Director**

**FEATURE:**

Traffic Director now provides the option of automated Envoy deployment.

**FEATURE:**

Traffic Director now supports automated Envoy deployments for Google Compute
Engine VMs in Beta.

##  July 06, 2020

**App Engine standard environment Node.js**

**FEATURE:**

The [ Node.js 12 runtime
](https://cloud.google.com/appengine/docs/standard/nodejs/runtime) for the App
Engine standard environment is now generally available.

**App Engine standard environment Python**

**FEATURE:**

The [ Python 3.8 runtime
](https://cloud.google.com/appengine/docs/standard/python3/runtime) for the
App Engine standard environment is now generally available.

**App Engine standard environment Ruby**

**FEATURE:**

The [ Ruby 2.6 and 2.7 runtime Betas
](https://cloud.google.com/appengine/docs/standard/ruby/runtime) for the App
Engine standard environment are now available.

**BigQuery**

**CHANGED:**

Updated version of [ Magnitude Simba ODBC
](https://cloud.google.com/bigquery/providers/simba-drivers) driver. This
version includes some performance improvements and bug fixes, and it catches
up with the JDBC driver by adding support for user defined functions and
variable time zones using the connection string.

**Compute Engine**

**FEATURE:**

E2 machine types now offer up to 32 vCPUs. See [ E2 machine types
](https://cloud.google.com/compute/docs/machine-types#e2_machine_types) for
more information.

**Dialogflow**

**FEATURE:**

The Dialogflow Console has been upgraded with an improved [ Analytics page
](https://cloud.google.com/dialogflow/docs/analytics) (Beta) that provides new
metrics and data views.

##  July 04, 2020

**Document AI**

**CHANGED:**

**Invoice Parsing Beta model upgrade**

The Invoice Parsing Beta model has been upgraded. This model upgrade results
in higher quality results for the [ entities
](https://cloud.google.com/document-
ai/docs/reference/rest/v1beta2/Document#Entity) and [ entityRelations
](https://cloud.google.com/document-
ai/docs/reference/rest/v1beta2/Document#EntityRelation) . There is no API
change.

See the [ product documentation ](https://cloud.google.com/solutions/document-
ai/docs/process-invoices) for more information.

##  July 01, 2020

**BigQuery ML**

**FEATURE:**

BigQuery ML now supports time series models as a [ beta
](https://cloud.google.com/products#product-launch-stages) release. For more
information, see [ CREATE MODEL statement for time series models
](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-
syntax-create-time-series) .

**Config Connector**

**FEATURE:**

Config Connector now supports [ ` --server-dry-run `
](https://kubernetes.io/blog/2019/01/14/apiserver-dry-run-and-kubectl-diff/)
for resource CRDs.

**FIXED:**

Fix a bug for the BigtableInstance resource that causes constant
reconciliation.

**CHANGED:**

Deprecate BigtableInstance's spec.deletionProtection field.

**Identity and Access Management**

**CHANGED:**

The organization policy constraint to [ prevent automatic role grants to Cloud
IAM service accounts ](https://cloud.google.com/resource-
manager/docs/organization-policy/restricting-service-
accounts#disable_service_account_default_grants) is now [ generally available
](https://cloud.google.com/products/#product-launch-stages) . To improve
security, we strongly recommend that you enable this constraint.

**CHANGED:**

Starting on July 27, 2020, IAM policies will identify deleted members that are
bound to a role. Deleted members have the prefix ` deleted: ` and the suffix `
?uid=  numeric-id  ` .

For example, if you delete the account for the user ` tamika@example.com ` ,
and a policy binds that user to a role, the policy shows an identifier similar
to ` deleted:user:tamika@example.com?uid=123456789012345678901 ` .

For ` SetIamPolicy ` requests, you can use this new syntax starting on July
27. For ` GetIamPolicy ` and ` SetIamPolicy ` responses, you might see the new
prefix and suffix in some, but not all, responses until we finish rolling out
the change. We expect to complete the rollout by July 31, 2020.

See the documentation for a [ detailed example
](https://cloud.google.com/iam/docs/policies#example-deleted-member) , as well
as guidance on [ updating policies that contain deleted members
](https://cloud.google.com/iam/docs/policies#handle-deleted-members) .

**ISSUE:**

Starting on July 27, 2020, if a binding in a policy refers to a deleted member
(for example, ` deleted:user:tamika@example.com?uid=123456789012345678901 ` ),
you cannot add a binding for a newly created member with the same name (in
this case, ` user:tamika@example.com ` ). If you try to add a binding for the
newly created member, IAM will apply the binding to the deleted member
instead.

To resolve this issue, see our guidance on [ updating policies that contain
deleted members ](https://cloud.google.com/iam/docs/policies#handle-deleted-
members) .

**Network Intelligence Center**

**FEATURE:**

Connectivity Tests now supports [ running tests
](https://cloud.google.com/network-intelligence-center/docs/connectivity-
tests/how-to/running-connectivity-tests) from the **Network interface details
screen** of a Compute Engine VM instance in the Google Cloud Console.

**Resource Manager**

**FEATURE:**

The Organization Policy for [ restricting automatic IAM permission grants to
new service accounts ](https://cloud.google.com/resource-
manager/docs/organization-policy/restricting-service-
accounts#disable_service_account_default_grants) has launched into general
availability.

##  June 30, 2020

**Anthos Service Mesh**

**FEATURE:**

1.6.4-asm.9 is now available.

**FEATURE:**

ASM 1.6 is compatible with and has the feature set of Istio 1.6 (see [ Istio
release notes ](https://istio.io/latest/news/releases/1.6.x/announcing-1.6/)
), subject to the list of [ ASM Supported Features
](https://cloud.google.com/service-mesh/docs/supported-features) .

**FIXED:**

1.5.7-asm.0 and 1.4.10-asm.3

Fixes the security issue, [ ISTIO-SECURITY-2020-007
](https://istio.io/latest/news/security/istio-security-2020-007/) , with the
same fixes as Istio 1.6.4. For information, see the [ Istio release notes
](https://istio.io/latest/news/releases/1.6.x/announcing-1.6.4/) .

**Description**

The vulnerability affects Anthos Service Mesh (ASM) versions 1.4.0 to 1.4.10,
1.5.0 to 1.5.5, and 1.6.4 whether running in Anthos GKE on-prem or on GKE,
potentially exposing your application to Denial of Service (DOS) attacks. This
vulnerability is referenced in these publicly disclosed Istio security
bulletins:

  * [ ISTIO-SECURITY-2020-007 ](https://istio.io/news/security/istio-security-2020-007/) : 
    * CVE-2020-12603 (CVSS score 7.0, High): Envoy through 1.14.1 may consume excessive amounts of memory when proxying HTTP/2 requests or responses with many small (e.g., 1 byte) data frames. 
    * CVE-2020-12605 (CVSS score 7.0, High): Envoy through 1.14.1 may consume excessive amounts of memory when processing HTTP/1.1 headers with long field names or requests with long URLs. 
    * CVE-2020-8663 (CVSS score 7.0, High): Envoy version 1.14.1 or earlier may exhaust file descriptors and/or memory when accepting too many connections. 
    * CVE-2020-12604 (CVSS score 7.0, High): Envoy through 1.14.1 is susceptible to increased memory usage in the case where an HTTP/2 client requests a large payload but does not send enough window updates to consume the entire stream and does not reset the stream. The attacker can cause data associated with many streams to be buffered forever. 

**Mitigation**

If you use ASM 1.6.4: * Apply the additional configuration changes specified
in [ ISTIO-SECURITY-2020-007 ](https://istio.io/latest/news/security/istio-
security-2020-007/) to prevent Denial of Service (DOS) attacks on your mesh.

If you use ASM 1.4.0 to 1.4.10 or 1.5.0 to 1.5.5: * Upgrade your clusters to
ASM 1.4.10-asm.3 or ASM 1.5.7-asm.0 as soon as possible and apply the
additional configuration changes specified in [ ISTIO-SECURITY-2020-007
](https://istio.io/latest/news/security/istio-security-2020-007/) to prevent
Denial of Service (DOS) attacks on your mesh.

  * See the following documentation for how to upgrade your Anthos Service Mesh. 

    * ASM 1.5 for GKE and on-premises, respectively: 
    * [ Upgrading Anthos Service Mesh on GKE ](https://cloud.google.com/service-mesh/docs/upgrading-gke)
    * [ Upgrading Anthos Service Mesh on-prem ](https://cloud.google.com/service-mesh/docs/gke-on-prem-upgrading)

    * ASM 1.4 for GKE and on-premises, respectively: 

    * [ Upgrading Anthos Service Mesh on GKE ](https://cloud.google.com/service-mesh/docs/archive/1.4/docs/upgrading-gke-1-4)

    * [ Upgrading Anthos Service Mesh on-prem ](https://cloud.google.com/service-mesh/docs/archive/1.4/docs/gke-on-prem-upgrading-1-4)

**FEATURE:**

Anthos Service Mesh now supports multi-cluster meshes (beta) when running on
GKE on Google Cloud.

**FEATURE:**

Users that configure multiple clusters in their mesh can now see unified,
multi-cluster views of their services in the Anthos Service Mesh pages in the
Cloud Console. Note that multi-cluster support is in Beta and not all UI
features are supported in multi-cluster mode.

**FEATURE:**

ASM 1.6 is supported in a single cluster configuration in Anthos Attached
Clusters in the following environments: Amazon Elastic Kubernetes Service
(EKS) and Microsoft Azure Kubernetes Service (AKS).

**CHANGED:**

The profile to install ASM in GKE has been renamed from ` asm ` to ` asm-gcp `
, see [ Upgrading Anthos Service Mesh on GKE
](https://cloud.google.com/service-mesh/docs/upgrading-gke) . The profile to
install ASM in GKE on-premise clusters has been renamed from ` asm-onprem ` to
` asm-multicloud ` , see [ Upgrading Anthos Service Mesh on premises
](https://cloud.google.com/service-mesh/docs/gke-on-prem-upgrading) .

**FEATURE:**

In the ` asm-multicloud ` profile, ASM now installs a complete observability
stack (Prometheus, Grafana and Kiali).

**FEATURE:**

Support for cross-cluster load balancing (beta) for your [ multi-cluster mesh
](https://cloud.google.com/service-mesh/docs/gke-install-multi-cluster) for
GKE on Google Cloud.

**FEATURE:**

New installation guides: [ Installing Anthos Service Mesh on attached clusters
](https://cloud.google.com/service-mesh/docs/attached-clusters-install) and [
Adding clusters to an Anthos Service Mesh ](https://cloud.google.com/service-
mesh/docs/gke-install-multi-cluster) .

**FEATURE:**

Anthos Service Mesh now supports cross-cluster security policies (beta) for
your [ multi-cluster mesh ](https://cloud.google.com/service-mesh/docs/gke-
install-multi-cluster) when running on GKE on Google Cloud.

**FEATURE:**

Upgrade from ASM 1.5 to ASM 1.6 without downtime using a [ dual control plane
upgrade ](https://istio.io/latest/blog/2020/multiple-control-planes/) .

**BREAKING:**

Known Issue: If you upgrade from Istio to ASM 1.6 and have set SLOs on your
service metrics, those SLOs might be lost and need to be recreated after the
upgrade.

**Cloud Build**

**FEATURE:**

Cloud Build now provides open-source notifiers for [ Slack
](https://cloud.google.com/cloud-build/docs/configuring-
notifications/configure-slack) and [ SMTP ](https://cloud.google.com/cloud-
build/docs/configuring-notifications/configure-smtp) . These notifiers can be
configured to securely alert users about build status.

**Cloud Composer**

**FEATURE:**

Cloud Composer support for [ VPC Service Controls
](https://cloud.google.com/composer/docs/configuring-vpc-sc) is now in Beta.

**Cloud Logging**

**FEATURE:**

Cloud Logging now contains a Logs Dashboard page that provides a high-level
overview into the health of your systems running within a project. To learn
more, see [ Logs Dashboard
](https://cloud.google.com/logging/docs/view/dashboard) .

**Cloud Run**

**CHANGED:**

Cloud Run (fully managed) support for [ connecting to a VPC network
](https://cloud.google.com/run/docs/configuring/connecting-vpc) with [
Serverless VPC Access ](https://cloud.google.com/vpc/docs/configure-
serverless-vpc-access) is now at general availability (GA).

**Google Cloud VMware Engine**

**FEATURE:**

[ Google Cloud VMware Engine ](https://cloud.google.com/vmware-engine/) is
**generally available** . This service delivers a fully managed VMware
platform stack—VMware ESXi, vCenter, vSAN, NSX-T, and HCX—in a dedicated
environment on Google Cloud's infrastructure to support your enterprise
production workloads. Using VMware Engine, you can bring your on-premises
workloads to Google Cloud by connecting to a dedicated VMware environment.

You can run the service in the ` us-east4 ` (Ashburn, Northern Virginia) and `
us-west2 ` (Los Angeles, California) regions.

For more information, read the [ VMware Engine documentation
](https://cloud.google.com/vmware-engine/docs/) .

**VPC Service Controls**

**FEATURE:**

General availability of dry run mode for service perimeters.

This release introduces dry run configurations for your service perimeters,
allowing you to test changes to perimeters before enforcing the changes. For
more information, [ read about dry run mode ](https://cloud.google.com/vpc-
service-controls/docs/dry-run-mode) .

**FEATURE:**

Beta release of the VPC Service Controls Troubleshooter.

The VPC Service Controls Troubleshooter allows you to use the unique
identifiers generated by VPC Service Controls errors to understand and resolve
common denials to services in your perimeters.

During the beta period, the following error types are supported:

  * ` NO_MATCHING_ACCESS_LEVEL `
  * ` NETWORK_NOT_IN_SAME_SERVICE_PERIMETER `
  * ` NO_MATCHING_ACCESS_LEVEL `

For more information, read about [ the VPC Service Controls Troubleshooter
](https://cloud.google.com/vpc-service-controls/docs/troubleshooter) .

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following integrations:

  * [ Cloud Composer ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_composer)
  * [ Cloud Healthcare API ](https://cloud.google.com/vpc-service-controls/docs/supported-products#table_healthcare)

##  June 29, 2020

**BigQuery**

**FEATURE:**

[ Flex slots ](https://cloud.google.com/bigquery/docs/reservations-
concepts#commitment_plans) are now [ generally available (GA)
](https://cloud.google.com/products/?hl=EN#product-launch-stages) .

**CHANGED:**

The [ BigQuery SLA ](https://cloud.google.com/bigquery/sla) has been updated
to >= 99.99% Monthly Uptime Percentage for all users.

**Cloud Debugger**

**FEATURE:**

Cloud Debugger now lets you canary snapshots and logpoints on your Node.js
applications. To learn more, see the [ Node.js page for setting up Cloud
Debugger ](https://cloud.google.com/debugger/docs/setup/nodejs) .

**Cloud Load Balancing**

**FEATURE:**

You can now [ create an internal HTTP(S) load balancer in a Shared VPC
_service_ project ](https://cloud.google.com/load-
balancing/docs/l7-internal#shared_vpc) .

This feature is available in **Alpha** . Please contact your Google account
team to get access to this feature.

**Cloud Run**

**FEATURE:**

Cloud Run is now available in the following regions:

  * ` asia-northeast2 ` (Osaka) 
  * ` australia-southeast1 ` (Sydney) 
  * ` northamerica-northeast1 ` (Montréal) 

**Dialogflow**

**DEPRECATED:**

The V1 API is in the process of a gradual shutdown. See the [ November 14,
2019 release note ](https://cloud.google.com/dialogflow/docs/release-
notes#November_14_2019) for details.

##  June 26, 2020

**App Engine standard environment Go**

**FEATURE:**

The [ Go 1.14 runtime Beta
](https://cloud.google.com/appengine/docs/standard/go/runtime) for the App
Engine standard environment is now available.

**BigQuery**

**FEATURE:**

[ Region qualified ` INFORMATION_SCHEMA ` views
](https://cloud.google.com/bigquery/docs/information-schema-intro#syntax) are
now in [ beta ](https://cloud.google.com/products/#product-launch-stages) .

**CHANGED:**

Starting in mid-July, unqualified ` INFORMATION_SCHEMA ` queries for `
SCHEMATA ` and ` SCHEMATA_OPTIONS ` views will default to returning metadata
from the ` US ` multi-region. For information about how to specify a region,
see [ region qualifier syntax
](https://cloud.google.com/bigquery/docs/information-schema-
intro#region_qualifier) .

**Compute Engine**

**FEATURE:**

To support a wide variety of BYOL scenarios, you can now [ configure VMs to
live migrate within a sole-tenant node group during host maintenance events
](https://cloud.google.com/compute/docs/nodes/bringing-your-own-licenses) .
This is **Generally Available** .

**VPC Service Controls**

**CHANGED:**

[ Beta stage support ](https://cloud.google.com/products/#product-launch-
stages) for the following integration:

  * [ Binary Authorization ](https://cloud.google.com/binary-authorization/docs/securing-with-vpcsc)

##  June 25, 2020

**Anthos**

**FEATURE:**

[ Anthos ](https://cloud.google.com/anthos) 1.4.0 is now available.

**Updated components:**

  * [ Anthos GKE on-prem release notes ](https://cloud.google.com/anthos/gke/docs/on-prem/release-notes)
  * [ Anthos Config Management release notes ](https://cloud.google.com/anthos-config-management/docs/release-notes)
  * See component and multi-cloud [ version and upgrade support ](https://cloud.google.com/anthos/docs/version-and-upgrade-support)

**Anthos Config Management**

**FEATURE:**

Anthos Config Management is now Generally Available on AKS (Kubernetes v1.16
or higher) and EKS (Kubernetes v1.16 or higher).

**ISSUE:**

Config Connector is not currently supported on EKS or AKS, as it is unable to
run on these providers.

**CHANGED:**

The following Policy Controller constraint templates have been added to the
Default Template Library:

  * allowedserviceportname 
  * destinationruletlsenabled 
  * disallowedauthzprefix 
  * policystrictonly 
  * sourcenotallauthz 

The following constraint templates have been updated:

  * k8sblockprocessnamespacesharing 
  * k8sdisallowedrolebindingsubjects 
  * k8semptydirhassizelimit 
  * k8slocalstoragerequiresafetoevict 
  * k8smemoryrequestequalslimit 
  * k8snoexternalservices 
  * k8spspallowedusers 
  * k8spspallowprivilegeescalationcontainer 
  * k8spspapparmor 
  * k8spspcapabilities 
  * k8spspflexvolumes 
  * k8spspforbiddensysctls 
  * k8spspfsgroup 
  * k8spsphostfilesystem 
  * k8spsphostnamespace 
  * k8spsphostnetworkingports 
  * k8spspprivilegedcontainer 
  * k8spspprocmount 
  * k8spspreadonlyrootfilesystem 
  * k8spspseccomp 
  * k8spspselinux 
  * k8spspvolumetypes 

See the [ Default Template Library documentation
](https://cloud.google.com/anthos-config-management/docs/reference/constraint-
template-library) for more information.

**CHANGED:**

Anthos Policy Controller has been updated to include a more recent build of
OPA Gatekeeper (hash: [ 25ca799 ](https://github.com/open-policy-
agent/gatekeeper/tree/25ca7993efb26079156e24d4c9bc8b8a2e83c3ef) ).

This new build of OPA Gatekeeper includes a number of bug fixes and
performance improvements, and adds three new monitoring metrics:

  * gatekeeper_sync 
  * gatekeeper_sync_duration_seconds 
  * gatekeeper_sync_last_run_time 

**FIXED:**

The ` nomos ` CLI tool now supports the ` KUBECONFIG ` environment variable in
a way that matches the [ ` kubectl ` behavior
](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-
kubeconfig/#the-kubeconfig-environment-variable) with multiple delimited
configuration files.

**FIXED:**

Anthos Config Management no longer gets into a continuous ` PATCH ` loop when
encountering unmanaged resources with config-management annotations and a
missing ` last-applied-configuration ` annotation.

**ISSUE:**

Anthos Config Management is not issuing errors when it encounters certain
types of malformed configurations in a resource definition. This may result in
the Kubernetes API Server ignoring the malformed fields and applying the
default value for the field instead.

**ISSUE:**

Policy Controller may fail to start successfully when synced resources are
marked for deletion.

This issue will be addressed in the upstream OPA Gatekeeper project in a
future release. For more information see the [ relevant issue
](https://github.com/open-policy-agent/gatekeeper/issues/660) in the
Gatekeeper project.

**CHANGED:**

This release includes several logging and performance improvements.

**Anthos GKE on-prem**

**FEATURE:**

Anthos GKE on-prem 1.4.0-gke.13 is now available. To upgrade, see [ Upgrading
GKE on-prem ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/upgrading) . GKE on-prem 1.4.0-gke.13 clusters run on Kubernetes
1.16.8-gke.6.

**FEATURE:**

**Updated to Kubernetes 1.16:**

  * Please note that Kubernetes 1.16 has deprecated some of its APIs. For more information, see [ Kubernetes 1.16 deprecated APIs ](https://cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-16) . 

**FEATURE:**

**Simplified upgrade:**

  * This release provides a simplified upgrade experience via the following changes: 

    * Automatically migrate information from the previous version of admin workstation using ` gkeadm ` . 
    * Extend preflight checks to better prepare for upgrades. 
    * Support skip version upgrade to enable users to upgrade the cluster from any patch release of a minor release to any patch release of the next minor release. For more information about the detailed upgrade procedure and limitations, see [ upgrading GKE on-prem ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading) . 
    * The [ alternate upgrade scenario for Common Vulnerabilities and Exposures ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/upgrading) has been deprecated. All upgrades starting with version 1.3.2 need to upgrade the entire admin workstation. 
    * The bundled load balancer is now automatically upgraded during cluster upgrade. 

**FEATURE:**

**Improved installation and cluster configuration:**

  * The user cluster [ node pools ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/user-cluster-basic#nodepoolsname) feature is now generally available. 
  * This release improves the installation experience via the following changes: 

    * Supports ` gkeadm ` for Windows OS. 
    * Introduces a standalone command for creating admin clusters. 
  * Introduce a new version of configuration files to separate admin and user cluster configurations and commands. This is designed to provide a consistent user experience and better configuration management. 

**FEATURE:**

**Improved disaster recovery capabilities:**

  * This release provides enhanced disaster recovery functionality to [ support backup and restore ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/backing-up#user_cluster_backups) HA user cluster with etcd. 
  * This release also provides a manual process to recover a single etcd replica failure in a HA cluster without any data loss. 

**FEATURE:**

**Enhanced monitoring with Cloud Monitoring (formerly Stackdriver):**

  * This release provides better product monitoring and resource usage management via the following changes: 

    * Introduces a [ default monitoring dashboard ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/logging-and-monitoring#dashboards) . 
    * Enables vSphere resource metrics collection by default. 
  * Ubuntu Image now conforms with PCI DSS, NIST Baseline High, and DoD SRG IL2 compliance configurations. 

**CHANGED:**

**Functionality changes:**

  * Enabled Horizontal Pod Autoscaler (HPA) for the Istio ingress gateway. 
  * Removed ingress controller from admin cluster. 
  * Consolidated sysctl configs with Google Kubernetes Engine. 
  * Added etcd defrag pod in admin cluster and user cluster, which will be responsible for monitoring etcd's database size and defragmenting it as needed. This helps reclaim etcd database size and recover etcd when its disk space is exceeded. 

**CHANGED:**

**Support for a vSphere folder (Preview):**

  * This release allows customers to install GKE on-prem in a vSphere folder, reducing the scope of the permission required for the vSphere user. 

**CHANGED:**

**Improved scale:**

  * This release improves the cluster scalability by supporting [ a maximum of 10 instead of 5 user clusters for each admin cluster ](https://cloud.google.com/anthos/gke/docs/on-prem/quotas) . 

**FIXED:**

**Fixes:**

  * Fixed the issue of the user cluster's Kubernetes API server not being able to connect to kube-etcd after admin nodes and user cluster master reboot. In previous versions, kube-dns in admin clusters was configured through kubeadm. In 1.4, this configuration is moved from kubeadm to bundle, which enables deploying two kube-dns replicas on two admin nodes. As a result, a single admin node reboot/failure won't disrupt user cluster API access. 
  * Fixed the issue that controllers such as calico-typha can't be scheduled on an admin cluster master node, when the admin cluster master node is under disk pressure. 
  * Resolved pods failure with MatchNodeSelector on admin cluster master after node reboot or kubelet restart. 
  * Tuned etcd quota limit settings based on the etcd data disk size and the settings in GKE Classic. 

**ISSUE:**

**Known issues:**

  * If a user cluster is created without any node pool named the same as the cluster, managing the node pools using ` gkectl update cluster ` would fail. To avoid this issue, when creating a user cluster, you need to name one node pool the same as the cluster. 
  * The ` gkectl ` command might exit with panic when converting config from "/path/to/config.yaml" to v1 config files. When that occurs, you can resolve the issue by removing the unused bundled load balancer section ("loadbalancerconfig") in the config file. 
  * When using gkeadm to upgrade an admin workstation on Windows, the info file filled out from this template needs to have the line endings converted to use Unix line endings (LF) instead of Windows line endings (CRLF). You can use Notepad++ to convert the line endings. 
  * After upgrading an admin workstation with a static IP using gkeadm, you need to run ` ssh-keygen -R <admin-workstation-ip> ` to remove the IP from the known hosts, because the host identification changed after VM re-creation. 
  * We have added Horizontal Pod Autoscaler for istio-ingress and istio-pilot deployments. HPA can scale up unnecessarily for istio-ingress and istio-pilot deployments during cluster upgrades. This happens because the metrics server is not able to report usage of some pods (newly created and terminating; for more information, see [ this Kubernetes issue ](https://github.com/kubernetes/kubernetes/issues/72775) ). No actions are needed; scale down will happen five minutes after the upgrade finishes. 
  * When running a preflight check for ` config.yaml ` that contains both ` admincluster ` and ` usercluster ` sections, the "data disk" check in the "user cluster vCenter" category might fail with the message: ` [FAILURE] Data Disk: Data disk is not in a folder. Use a data disk in a folder when using vSAN datastore. ` User clusters don't use data disks, and it's safe to ignore the failure. 
  * When upgrading the admin cluster, the preflight check for the user cluster OS image validation will fail. The user cluster OS image is not used in this case, and it's safe to ignore the "User Cluster OS Image Exists" failure in this case. 
  * A Calico-node pod might be stuck in an unready state after node IP changes. To resolve this issue, you need to delete any unready Calico-node pods. 
  * The BIG-IP controller might fail to update F5 VIP after any admin cluster master IP changes. To resolve this, you need to use the admin cluster master node IP in kubeconfig and delete the bigip-controller pod from the admin master. 
  * The stackdriver-prometheus-k8s pod could enter a crashloop after host failure. To resolve this, you need to remove any corrupted PersistentVolumes that the stackdriver-prometheus-k8s pod uses. 
  * After node IP change, pods running with hostNetwork don't get podIP corrected until Kubelet restarts. To resolve this, you need to restart Kubelet or delete those pods using previous IPs. 
  * An admin cluster fails after any admin cluster master node IP address changes. To avoid this, you should avoid changing the admin master IP address if possible by using a static IP or a non-expired DHCP lease instead. If you encounter this issue and need further assistance, please contact Google Support. 
  * User cluster upgrade might be stuck with the error: ` Failed to update machine status: no matches for kind "Machine" in version "cluster.k8s.io/v1alpha1". ` To resolve this, you need to delete the clusterapi pod in the user cluster namespace in the admin cluster. 

**ISSUE:**

If your vSphere environment has fewer than three hosts, user cluster upgrade
might fail. To resolve this, you need to disable ` antiAffinityGroups ` in the
cluster config before upgrading the user cluster. For v1 config, please set `
antiAffinityGroups.enabled = false ` ; for v0 config, please set `
usercluster.antiaffinitygroups.enabled = false ` .

**Note:** Disabling ` antiAffinityGroups ` in the cluster config during
upgrade is only allowed for the 1.3.2 to 1.4. _x_ upgrade to resolve the
upgrade issue; the support might be removed in the future.

**Cloud Load Balancing**

**CHANGED:**

The introductory period during which you can use Internal HTTP(S) Load
Balancing without charge is coming to an end. Starting on July 25, 2020, your
usage of Internal HTTP(S) Load Balancing will be [ billed to your project
](https://cloud.google.com/compute/network-pricing#internal-https-lb) .

**Config Connector**

**FEATURE:**

Add an option, iam-format, to config-connector to control IAM output, options
are policy, policymember, or none.

**FEATURE:**

ComputeForwardingRule's target field now supports referencing a
ComputeTargetSSLProxy and ComputeTargetTCPProxy.

**CHANGED:**

DataFlowJob's serviceAccountEmail, network, subnetwork, machineType, and
ipConfiguration fields now support updates.

**FIXED:**

Fix an issue where config-connector would error on a Project resource.

##  June 24, 2020

**Cloud Composer**

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.10.5-airflow-1.10.2 ` , ` composer-1.10.5-airflow-1.10.3 ` and ` composer-1.10.5-airflow-1.10.6 ` . The default is ` composer-1.10.5-airflow-1.10.3 ` . Upgrade your Cloud SDK to use features in this release. 

**FEATURE:**

  * Composer now uses the Kubernetes v1 API, and is compatible with GKE 1.16 
  * An updated haproxy configuration for Composer increases the maximum number of connections to 2000, and changes load balancing to be based on the number of connections. These settings can be configured with environment variables. 

**FIXED:**

  * Error messages for ` TP_APP_ENGINE_CREATING ` timeout and RPC delivery issues have been expanded. 
  * Airflow Providers can now be installed inside Cloud Composer. 
  * Error handling for rendering templates in the Airflow web server UI has been improved. 
  * Fixed an issue with rendering task instance details (logs, task instance template, params) in the Airflow web server UI when DAG serialization is enabled. 
  * Fixed an issue with ` DataFlowJavaOperator ` , so it can now be used with Apache Beam 2.20. 
  * Improved error reporting for failing operations. 
  * Memory consumption of the ` gcs-syncd ` container is now constrained to prevent system instability. 

**Dataproc**

**CHANGED:**

New [ subminor image versions
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions#supported_cloud_dataproc_versions) : 1.2.100-debian9, 1.3.60-debian9,
1.4.31-debian9, 1.3.60-debian10, 1.4.31-debian10, 1.5.6-debian10,
1.3.60-ubuntu18, 1.4.31-ubuntu18, 1.5.6-ubuntu18, preview 2.0.0-RC2-debian10,
and preview 2.0.0-RC2-ubuntu18.

**CHANGED:**

  * **Image 2.0 preview** : 

    * [ SPARK-22404 ](https://issues.apache.org/jira/browse/SPARK-22404) : set ` spark.yarn.unmanagedAM.enabled ` property to ` true ` on clusters where Kerberos is not enabled to run Spark Application Master in driver (not managed in YARN) to improve job execution time. 
    * Updated R version to 3.6 

    * Updated Spark to [ 3.0.0 version ](https://spark.apache.org/releases/spark-release-3-0-0.html)

  * **Image 1.5**

    * Updated R version to 3.6 

**FIXED:**

Fixed a quota validation bug where accelerator counts were squared before
validation -- for example, previously if you requested 8 GPUs, Dataproc
validated whether your project had quota for ` 8^2=64 ` GPUs.

##  June 23, 2020

**AI Platform Deep Learning VM Image**

**FIXED:**

**M50 release**

Miscellaneous bug fixes.

**Cloud Billing**

**FEATURE:**

Committed use discounts (CUDs) are now available to purchase for Cloud SQL.
CUDs provide discounted prices in exchange for your commitment to use a
minimum level of resources for a specified term. With spend-based committed
use discounts for Cloud SQL, you can earn a deep discount off your cost of use
in exchange for committing to continuously use database instances in a
particular region for a 1- or 3-year term. See the [ blog
](https://cloud.google.com/blog/products/databases/cloud-sql-database-
instances-now-discounted) and [ documentation
](https://cloud.google.com/docs/cuds) for more details.

**Cloud SQL for MySQL**

**FEATURE:**

Committed use discounts (CUDs) are now available to purchase for Cloud SQL.
CUDs provide discounted prices in exchange for your commitment to use a
minimum level of resources for a specified term. With committed use discounts
for Cloud SQL, you can earn a deep discount off your cost of use in exchange
for committing to continuously use database instances in a particular region
for a 1- or 3-year term. See the [ documentation
](https://cloud.google.com/sql/docs/mysql/cud) for more details.

**Cloud SQL for PostgreSQL**

**FEATURE:**

Committed use discounts (CUDs) are now available to purchase for Cloud SQL.
CUDs provide discounted prices in exchange for your commitment to use a
minimum level of resources for a specified term. With committed use discounts
for Cloud SQL, you can earn a deep discount off your cost of use in exchange
for committing to continuously use database instances in a particular region
for a 1- or 3-year term. See the [ documentation
](https://cloud.google.com/sql/docs/mysql/cud) for more details.

**Cloud SQL for SQL Server**

**FEATURE:**

Committed use discounts (CUDs) are now available to purchase for Cloud SQL.
CUDs provide discounted prices in exchange for your commitment to use a
minimum level of resources for a specified term. With committed use discounts
for Cloud SQL, you can earn a deep discount off your cost of use in exchange
for committing to continuously use database instances in a particular region
for a 1- or 3-year term. See the [ documentation
](https://cloud.google.com/sql/docs/mysql/cud) for more details.

**Google Cloud Armor**

**CHANGED:**

[ Promotional pricing ](https://cloud.google.com/armor/pricing) for Google
Cloud Armor is extended to July 31, 2020.

