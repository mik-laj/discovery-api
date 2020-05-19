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

##  May 18, 2020

**Cloud Bigtable**

**CHANGED:**

The [ Cloud Bigtable Monitoring
](https://cloud.google.com/bigtable/docs/monitoring-instance) page in the
Cloud Console has been redesigned. Changes to the visual experience include
the following: * Views that are now split into separate tabs * A new time
range picker * Updated styling on the graphs

**Cloud Billing**

**FEATURE:**

**Cloud Billing budgets emails** : ensure your budget alert emails are seen by
the right people using Cloud Monitoring notifications on your Cloud Billing
budgets. By default, alert emails are sent to Billing Account Administrators.
With the _Monitoring notifications_ feature, you can customize your budget to
send alerts to up to five additional email recipients you specify. See the [
documentation ](https://cloud.google.com/billing/docs/how-to/budgets-
notification-recipients) for more details.

**FEATURE:**

New information is now available on your **Cloud Billing** account
**Overview** page in the **Cloud Console** , featuring at-a-glance summaries
of the top five spending projects and top five spending products over the last
12 months.

To see the updated Billing Account Overview page, go to the [ Manage billing
accounts page ](https://console.cloud.google.com/billing) in the Cloud Console
and sign in, then select the name of the Cloud Billing account you want to
view. The Billing Overview page is displayed with the **BILLING ACCOUNT
OVERVIEW** tab selected. You might need to scroll the page to see all the
features.

**Cloud DNS**

**FEATURE:**

[ DNS forwarding to a non-RFC 1918 address
](https://cloud.google.com/dns/zones/#creating-forwarding-zones) is available
in **General Availability** .

**Cloud Functions**

**CHANGED:**

Cloud Functions now supports [ Node.js 10
](https://cloud.google.com/functions/docs/concepts/nodejs-10-runtime) at the [
General Availability release level
](https://cloud.google.com/products/#product-launch-stages) .

**Cloud Identity and Access Management**

**CHANGED:**

Recommendations from the [ Cloud IAM recommender
](https://cloud.google.com/iam/docs/recommender-overview) can now include [
suggestions to create custom roles
](https://cloud.google.com/iam/docs/recommender-overview#custom-roles) .

**Cloud Logging**

**FEATURE:**

**Logs Viewer** now contains the **Logs field explorer** panel, which lets you
view aggregation-based results for your project's log fields and makes it more
efficient to refine queries. To learn more, go to the [ Logs Viewer (Preview)
page ](https://cloud.google.com/logging/docs/view/logs-viewer-interface) .

**Cloud SQL for MySQL**

**FEATURE:**

MySQL 5.6 minor version is upgraded to 5.6.42. MySQL 5.7 minor version is
upgraded to 5.7.25.

**Cloud Spanner**

**FEATURE:**

You can now run SQL queries to retrieve [ transaction statistics
](https://cloud.google.com/spanner/docs/transaction-stats-tables) for your
database over recent one-minute, 10-minute, and one-hour time periods.

**Cloud Storage**

**CHANGED:**

The V4 signing process is now in GA.

  * The V4 signing process is an improved method for creating [ signatures ](https://cloud.google.com/storage/docs/authentication/signatures) using RSA or HMAC keys. 

**Virtual Private Cloud**

**FEATURE:**

Subnets in VPC networks now support IP addresses other than RFC 1918
addresses. For more information, see [ Subnet ranges
](https://cloud.google.com/vpc/docs/vpc#manually_created_subnet_ip_ranges) .

##  May 17, 2020

**Dialogflow**

**CHANGED:**

Old Node.js client library require statements must be updated. Your require
statements should look like this:

` const dialogflow = require('@google-cloud/dialogflow').v2; `

or this:

` const dialogflow = require('@google-cloud/dialogflow').v2beta1; `

Old syntax that does not include ` @google-cloud ` is now deprecated. The old
syntax will continue to work, but you will not receive updates.

##  May 16, 2020

**Cloud Data Loss Prevention**

**FEATURE:**

Added [ infoType detectors ](https://cloud.google.com/dlp/docs/infotypes-
reference) :

AWS_CREDENTIALS

##  May 15, 2020

**Cloud Composer**

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.10.3-airflow-1.10.2 ` , ` composer-1.10.3-airflow-1.10.3 ` and ` composer-1.10.3-airflow-1.10.6 ` . The default is ` composer-1.10.3-airflow-1.10.3 ` . Upgrade your Cloud SDK to use features in this release. 

**FEATURE:**

  * Resource quota limits have been updated, allowing environment administrators to set quotas with more granularity. The default quotas for read and write operations have also changed; see [ Cloud Composer resource quotas ](https://cloud.google.com/composer/quotas) for details. The old limits are deprecated, but will not be removed from the Cloud Console Quotas page until a future release. 

**CHANGED:**

  * The machine type of the Airflow web server will now be preserved during Composer environment updates, including cases like new PyPi module installations, or adding new environment variables. 
  * Synchronization of log files between the Airflow scheduler, web server and workers has been improved. 
  * More useful error messages have been added for Composer environment upgrade failures. 
  * _Future change:_ Airflow 1.10.6 will become the default Airflow version for Composer environments in an upcoming release. 

**DEPRECATED:**

  * Composer version 1.6.1 has been deprecated. 

**Cloud SQL for PostgreSQL**

**FEATURE:**

PostgreSQL 9.6 minor version is upgraded to 9.6.16. PostgreSQL 10 minor
version is upgraded to 10.11. PostgreSQL 11 minor version is upgraded to 11.6.
PostgreSQL 12 minor version is upgraded to 12.1.

**Cloud Vision**

**CHANGED:**

**OCR model upgrades**

The ` text_detection ` and ` document_text_detection ` models have been
upgraded to newer versions. The API interface and client library will be the
same as previous version. The API follows the same [ Service Level Agreement
](https://cloud.google.com/vision/sla) .

The legacy models can still be accessed until June 30, 2020. Specify
"builtin/legacy_20190601" in the [ ` model `
](https://cloud.google.com/vision/docs/reference/rest/v1/Feature) field of a `
Feature ` object to get the old model results. After June 30, 2020 the old
models will not longer be offered.

For more information, see the [ product documentation
](https://cloud.google.com/vision/docs/ocr) .

**Config Connector**

**FIXED:**

fix ContainerNodePool version upgrade scenario

**CHANGED:**

increase the cpu/memory request for webhook and recorder

**CHANGED:**

Miscellaneous bug fixes and improvement

##  May 14, 2020

**App Engine flexible environment PHP**

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/flexible/php/labeling-resources) .

**App Engine flexible environment Ruby**

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/flexible/ruby/labeling-resources) .

**Cloud Monitoring**

**CHANGED:**

Starting in version 6.0.2, the Cloud Monitoring agent is available for the
Ubuntu LTS 20.04 (Focal Fossa) distribution.

##  May 13, 2020

**AI Platform Prediction**

**FEATURE:**

AI Platform Prediction now supports the following regions for batch
prediction, in addition to those that were already supported:

  * ` northamerica-northeast1 ` (Montréal) 
  * ` southamerica-east1 ` (São Paulo) 
  * ` australia-southeast1 ` (Sydney) 

See the [ full list of available regions ](https://cloud.google.com/ai-
platform/prediction/docs/regions) .

` northamerica-northeast1 ` and ` southamerica-east1 ` have the same pricing
as other Americas regions, and ` australia-southeast1 ` has the same pricing
as other Asia Pacific regions. Learn about [ pricing for each region
](https://cloud.google.com/ai-platform/prediction/pricing) .

**AI Platform Training**

**FEATURE:**

AI Platform Training now supports the following regions, in addition to those
that were already supported:

  * ` northamerica-northeast1 ` (Montréal) 
  * ` southamerica-east1 ` (São Paulo) 
  * ` australia-southeast1 ` (Sydney) 

GPUs are available for training in each of the new regions:

  * NVIDIA Tesla P4 GPUs are available in ` northamerica-northeast1 ` . 
  * NVIDIA Tesla T4 GPUs are available in ` southamerica-east1 ` . 
  * NVIDIA Tesla P4 GPUs and NVIDIA Tesla P100 GPUs are available in ` australia-southeast1 ` . 

See the [ full list of available regions ](https://cloud.google.com/ai-
platform/training/docs/regions) and the [ guide to training with GPUs
](https://cloud.google.com/ai-platform/training/docs/using-gpus) .

` northamerica-northeast1 ` and ` southamerica-east1 ` have the same pricing
as other Americas regions, and ` australia-southeast1 ` has the same pricing
as other Asia Pacific regions. Learn about [ pricing for each region
](https://cloud.google.com/ai-platform/training/pricing) .

**BigQuery**

**CHANGED:**

Updated versions of [ Magnitude Simba JDBC
](https://cloud.google.com/bigquery/providers/simba-drivers/) drivers have
been released.

**Cloud Run**

**FEATURE:**

Cloud Run (fully managed) now supports [ connecting to a VPC network
](https://cloud.google.com/run/docs/configuring/connecting-vpc) with [
Serverless VPC Access ](https://cloud.google.com/vpc/docs/configure-
serverless-vpc-access) , in beta.

**Memorystore for Redis**

**FEATURE:**

Released support for [ VPC Service Controls
](https://cloud.google.com/memorystore/docs/redis/using-vpc-service-controls)
for Memorystore for Redis.

**VPC Service Controls**

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following integration:

  * [ Memorystore for Redis ](https://cloud.google.com/memorystore/docs/redis)

##  May 12, 2020

**AI Platform Deep Learning VM Image**

**FIXED:**

**M47 release**

Fixed an OS login issue under single user mode for a user external to an
organization.

Fixed a git extensions plugin issue in TensorFlow 2 images.

**Anthos Service Mesh**

**FIXED:**

1.4.9-asm.1

Fixes the security issue, CVE-2020-10739, with the same fixes as [ OSS Istio
1.4.9 ](https://istio.io/news/releases/1.4.x/announcing-1.4.9/) . See [ ISTIO-
SECURITY-2020-005 ](https://istio.io/news/security/istio-security-2020-005)
for more information.

**BigQuery**

**CHANGED:**

Updated versions of [ Magnitude Simba ODBC
](https://cloud.google.com/bigquery/providers/simba-drivers/) drivers have
been released.

**Cloud Profiler**

**CHANGED:**

The Cloud Profiler Python agent is now generally available. See [ Profiling
Python applications ](https://cloud.google.com/profiler/docs/profiling-python)
for information on configuring your Python application.

**Cloud TPU**

**CHANGED:**

Cloud TPU currently supports TensorFlow version 1.15.2. See the [ Release
Notes ](https://github.com/tensorflow/tensorflow/releases/tag/v1.15.2) .

TensorFlow 1.15 supported Python 2, but that support has been discontinued
with TensorFlow 1.15.2.

**Compute Engine**

**FEATURE:**

Automatically manage the size of sole-tenant node groups with the [ sole-
tenant node group autoscaler
](https://cloud.google.com/compute/docs/nodes/node-group-autoscaler) . This is
**Generally Available** .

**Security Command Center**

**FEATURE:**

Security Command Center Premium and Standard tiers are now available.

**FEATURE:**

The Security Command Center Premium tier includes:

  * Security Health Analytics 
  * Web Security Scanner managed scans 
  * Event Threat Detection 
  * Container Threat Detection 

Learn more about the [ Security Command Center Premium tier
](https://cloud.google.com/security-command-center/docs/concepts-security-
command-center-overview) .

**DEPRECATED:**

The Event Threat Detection API will be deprecated in the coming months.
Similar functionality is available in the Security Command Center API settings
feature.

**FEATURE:**

Container Threat Detection currently supports the following Kubernetes Engine
versions on the Regular and Rapid [ channels
](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels) :

  * >= 1.15.9-gke.12 
  * >= 1.16.5-gke.2 
  * >= 1.17 

In a future update, Container Threat Detection will support version 1.14 and
the Stable channel.

##  May 11, 2020

**App Engine standard environment Python**

**CHANGED:**

Updated Python SDK to version 1.9.91.

**Cloud Logging**

**FEATURE:**

You can now use regular expressions to query your logs data and create
filters. For more information, go to [ Using regular expressions
](https://cloud.google.com/logging/docs/view/logging-query-language#regular-
expressions) .

**Cloud SQL for PostgreSQL**

**FEATURE:**

Cloud SQL has expanded support for PostgreSQL extensions. Eight additional
PostgreSQL extensions are now available:

  * pageinspect 
  * pgfincore 
  * pg_freespacemap 
  * pg_repack 
  * pg_visibility 
  * PL/Proxy 
  * postgres_fdw 
  * postgresql-hll 

For information about these newly-added extensions, see [ PostgreSQL
extensions ](https://cloud.google.com/sql/docs/postgres/extensions) .

**Compute Engine**

**FEATURE:**

You can identify idle persistent disk resources by using [ idle persistent
disk recommendations ](https://cloud.google.com/compute/docs/disks/viewing-
and-applying-idle-pd-recommendations) . Following these recommendations will
help reduce unused resources and reduce your compute bill. This feature is
**Generally available** .

##  May 08, 2020

**BigQuery**

**FEATURE:**

[ Next generation BigQuery streaming
](https://cloud.google.com/bigquery/quotas#streaming_inserts) is now [
Generally Available (GA) ](https://cloud.google.com/products/?hl=EN#product-
launch-stages) .

**Cloud Composer**

**FEATURE:**

Cloud Composer is now available in Hong Kong ( ` asia-east2 ` ).

**FEATURE:**

Cloud Composer is now available in Las Vegas ( ` us-west4 ` ).

**Cloud Monitoring**

**FEATURE:**

Monitoring Query Language (MQL) is now available in Beta. MQL is an
expressive, text-based interface to Cloud Monitoring time-series data. With
MQL, you can create charts you can't create any other way. You can access MQL
from both the Cloud Console and the Monitoring API. For more information, see
[ Introduction to Monitoring Query Language
](https://cloud.google.com/monitoring/mql/) .

**Cloud Run**

**FEATURE:**

Cloud Code IDE extensions support Cloud Run. See [ Cloud Code for VS Code
](https://cloud.google.com/code/docs/vscode/deploying-a-cloud-run-app) and [
Cloud Code for IntelliJ
](https://cloud.google.com/code/docs/intellij/deploying-a-cloud-run-app)

**Cloud TPU**

**CHANGED:**

Cloud TPU now supports TensorFlow 2.2. See the [ TensorFlow 2.2 Release Notes
](https://github.com/tensorflow/tensorflow/releases/tag/v2.2.0) for a complete
list of features included with this release. New models for Image segmentation
and Image classification have been added to the official cloud [ TPU supported
models list ](https://cloud.google.com/tpu/docs/tutorials/support-matrix) .

**Dialogflow**

**FEATURE:**

Beta launch of a one-click integration with the [ Voximplant
](https://cloud.google.com/dialogflow/docs/integrations/voximplant) telephony
partner:

##  May 07, 2020

**Anthos GKE deployed on AWS**

**BREAKING:**

To upgrade your Anthos GKE on AWS clusters, you need to [ uninstall
](https://cloud.google.com/anthos/gke/docs/aws/how-to/uninstalling) all your
management and user clusters. You also need to download the new version of the
[ ` anthos-gke `
](https://cloud.google.com/anthos/gke/docs/aws/downloads#anthos-gke_cli_tool)
cli tool.

**CHANGED:**

Anthos GKE on AWS now supports [ auto-scaling
](https://cloud.google.com/anthos/gke/docs/aws/how-to/scaling-user-cluster) .
You can enable auto-scaling by changing settings in your AWSNodePools, or
scale your clusters manually by adding new AWSNodePools.

**CHANGED:**

Built-in EBS StorageClass names have been changed to ` standard-rwo ` and `
premium-rwo ` . If you declare the [ ` singlewriter-standard ` or `
singlewriter-premium `
](https://cloud.google.com/anthos/gke/docs/aws/concepts/storage.md)
StorageClasses with your workloads, you must update your workloads when
upgrading.

**CHANGED:**

Anthos GKE on AWS now support for Application-layer secrets encryption with
AWS KMS by passing a KMS key ARN to your [ AWSCluster
](https://cloud.google.com/anthos/gke/docs/aws/reference/awscluster#speccontrolplane)
.

##  May 06, 2020

**Traffic Director**

**CHANGED:**

A new document is added to [ Traffic Director
](https://cloud.google.com/traffic-director/docs) : [ Ingress traffic for your
mesh ](https://cloud.google.com/traffic-director/docs/traffic-director-
ingress-traffic) .

##  May 05, 2020

**Dataproc**

**FEATURE:**

Clusters can now be created with non-preemptible secondary workers.

**Dialogflow**

**FEATURE:**

GA (general availability) launch of [ auto speech adaptation
](https://cloud.google.com/dialogflow/docs/speech-adaptation) .

##  May 04, 2020

**Cloud Data Loss Prevention**

**CHANGED:**

We have made quality and performance enhancements to our name detectors.
PERSON_NAME should be used in most scenarios as it will return the most
comprehensive finding. MALE_NAME and FEMALE_NAME are now synonymous with
FIRST_NAME with [ ` Likelihood `
](https://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#likelihood)
now never being greater than ` POSSIBLE ` . These changes will be rolled out
over the coming days.

**Cloud SQL for MySQL**

**DEPRECATED:**

As [ previously announced ](https://cloud.google.com/sql/docs/mysql/release-
notes#January_29_2019) , Cloud SQL First Generation was deprecated on January
29, 2019. All First Generation instances have been migrated to Second
Generation. In the documentation and in the Google Cloud Console, "MySQL
Second Generation instances" are now referred to simply as "MySQL instances."
For general information about this deprecation, see the existing [ deprecation
notice ](https://cloud.google.com/sql/docs/mysql/deprecation-notice) .

**Dialogflow**

**CHANGED:**

The shutdown of 7 integrations [ announced in January
](https://cloud.google.com/dialogflow/docs/release-notes#January_06_2020) is
now extended to June 6th, 2020.

##  May 01, 2020

**BigQuery**

**FEATURE:**

A new function, ` JSON_EXTRACT_ARRAY ` , has been added to the list of JSON
functions. This function allows you to extract the contents of a JSON document
as a string array. For more information, see the [ ` JSON_EXTRACT_ARRAY `
reference section ](https://cloud.google.com/bigquery/docs/reference/standard-
sql/json_functions#json_extract_array) .

**FEATURE:**

The ` ORDER BY ` clause now supports the ` NULLS FIRST ` and ` NULLS LAST `
clauses. These clauses allow you to specify the sort order of null and non-
null values. For more information, see the [ ` ORDER BY ` reference section
](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-
syntax#order_by_clause) .

**Cloud CDN**

**CHANGED:**

Added a new [ Features page ](https://cloud.google.com/cdn/docs/features) that
summarizes all Cloud CDN capabilities.

**Dataproc**

**FEATURE:**

Announcing the [ Beta ](https://cloud.google.com/products#product-launch-
stages) release of [ Dataproc Component Gateway
](https://cloud.google.com/dataproc/docs/concepts/accessing/dataproc-gateways)
, which provides secure access to web endpoints for Dataproc default and
optional components.

**Text-to-Speech**

**FEATURE:**

Cloud Text-to-Speech now offers 36 new voices (both Standard and WaveNet) in
the following languages. See the [ Supported Voices and Languages
](https://cloud.google.com/text-to-speech/docs/voices) page for complete
details.

  * Arabic 
  * Bengali (India) 
  * English (India) 
  * French (France) 
  * German (Germany) 
  * Gujarati (India) 
  * Hindi (India) 
  * Indonesian (Indonesia) 
  * Kannada (India) 
  * Malayalam (India) 
  * Mandarin Chinese 
  * Russian (Russia) 
  * Tamil (India) 
  * Telugu (India) 
  * Thai (Thailand) 

##  April 30, 2020

**BigQuery**

**CHANGED:**

The BigQuery Data Transfer Service is now available in the [ Taiwan (asia-
east1) region ](https://cloud.google.com/bigquery-
transfer/docs/locations#supported_regions) .

**BigQuery Data Transfer Service**

**CHANGED:**

BigQuery Data Transfer Service is now available in the [ Taiwan (asia-east1)
region ](https://cloud.google.com/bigquery-
transfer/docs/locations#supported_regions) .

**Compute Engine**

**CHANGED:**

SSD persistent disks now have increased write throughput limits on instances
with 1 to 15 vCPUs. This improvement applies to SSD persistent disks on all
machine types except C2 machine types. To learn more about the requirements to
reach these limits, see [ Block storage performance
](https://cloud.google.com/compute/docs/disks/performance#size_price_performance)
.

**Config Connector**

**CHANGED:**

Fixes for the examples for the following resources: CloudBuildTrigger,
AccessContextManager, ComputeDisk, and ComputeSubNetwork

**CHANGED:**

Reduced memory requirements for deletion defender, recorder, and webhook.
Reduced cpu requirements for recorder and webhook Increased CPU for the
manager controller from 100m to 200m.

**CHANGED:**

Ensure the webhook process does not signal it is ready until it is serving
HTTP traffic

**Data Catalog**

**FEATURE:**

Data Catalog is now generally available (GA). \- The Data Catalog v1 API,
gcloud commands, and UI are now available. For details, [ see the API
reference ](https://cloud.google.com/data-catalog/docs/reference) . Code
samples throughout the documentation have been updated to use the new API. \-
Data Catalog has been regionalized, and now hosts user metadata in [ 23
regions worldwide ](https://cloud.google.com/data-
catalog/docs/concepts/regions) . \- Billing has been enabled for Data Catalog
API calls and storage using all supported resources. For more info, see the [
pricing page ](https://cloud.google.com/data-catalog/pricing) .

**Dialogflow**

**FEATURE:**

Beta launch of a one-click integration with a new telephony partner:

  * [ Avaya ](https://cloud.google.com/dialogflow/docs/integrations/avaya)

##  April 29, 2020

**AI Platform Prediction**

**FEATURE:**

AI Platform Prediction now supports several [ regional endpoints
](https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints) for
online prediction. Regional endpoints provide additional protection against
outages in other regions by isolating your model and version resources from
other regions. The following regional endpoints are available in beta:

  * ` us-central1-ml.googleapis.com `
  * ` europe-west4-ml.googleapis.com `
  * ` asia-east1-ml.googleapis.com `

You can use these endpoints instead of the global endpoint, `
ml.googleapis.com ` , when you use AI Platform Prediction for online
prediction. [ Learn how to use regional endpoints for online prediction, and
read about their benefits and limitations. ](https://cloud.google.com/ai-
platform/prediction/docs/regional-endpoints)

**FEATURE:**

You can now deploy scikit-learn and XGBoost models for online prediction using
[ Compute Engine (N1) machine types ](https://cloud.google.com/ai-
platform/prediction/docs/machine-types-online-prediction) . Previously, you
could only deploy TensorFlow models when you used these machine types. Learn
more about [ ML framework support for Compute Engine (N1) machine types
](https://cloud.google.com/ai-platform/prediction/docs/machine-types-online-
prediction#ml_framework_support) .

You cannot use GPUs with scikit-learn or XGBoost models, and you can only use
scikit-learn and XGBoost models with Compute Engine (N1) machine types when
you deploy your models and versions to a [ regional endpoint
](https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints) .

Compute Engine (N1) machine types for online prediction remain available in
the beta launch stage.

**FEATURE:**

The ` europe-west4 ` (Netherlands) and ` asia-east1 ` (Taiwan) regions are now
available for online prediction. These regions are only available for online
prediction on their respective [ regional endpoints
](https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints) ,
and you can only use [ Compute Engine (N1) machine types
](https://cloud.google.com/ai-platform/prediction/docs/machine-types-online-
prediction) for online prediction in these regions.

When you deploy model versions in the ` europe-west4 ` region, you can
optionally use NVIDIA Tesla P4, NVIDIA Tesla T4, or NVIDIA Tesla V100 GPUs to
accelerate prediction.

When you deploy model versions in the ` asia-east1 ` region, you can
optionally use NVIDIA Tesla K80 or NVIDIA Tesla P100 GPUs to accelerate
prediction.

Learn more about [ using GPUs for online prediction
](https://cloud.google.com/ai-platform/prediction/docs/machine-types-online-
prediction#gpus) , and see [ which GPUs are available in which regions
](https://cloud.google.com/ai-platform/prediction/docs/regions) .

Learn about the [ pricing for the newly available regions and GPU resources
](https://cloud.google.com/ai-platform/prediction/pricing) .

**CHANGED:**

We recommend against using Compute Engine (N1) machine types on the AI
Platform Prediction global endpoint. Instead, only use Compute Engine (N1)
machine types when you deploy models and versions to a [ regional endpoint
](https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints) .

Model versions that use Compute Engine (N1) machine types and were previously
deployed to the ` us-central1 ` region on the global endpoint will continue to
function.

**Virtual Private Cloud**

**CHANGED:**

Google Cloud now encrypts VPC traffic within the boundaries of the data
centers in _asia-east2_ . We will roll out this feature gradually to other
regions. Google Cloud already encrypts VPC traffic _between all data centers_
as described in [ Encryption in Transit in Google Cloud
](https://cloud.google.com/security/encryption-in-transit#virtual-network) .

##  April 28, 2020

**Anthos Service Mesh**

**FEATURE:**

The Anthos Service Mesh dashboard in the Google Cloud Console is generally
available for Anthos Service Mesh installations on Google Kubernetes Engine
clusters. For more information, see the [ Observability overview
](https://cloud.google.com/service-mesh/docs/observability-overview) .

**Cloud Data Loss Prevention**

**FEATURE:**

Added additional [ infoType detector
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * JSON_WEB_TOKEN 

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

**Media Translation**

**FEATURE:**

Beta release of Media Translation API. Media Translation translates an audio
file or stream of speech into text for 12 languages.

##  April 27, 2020

**BigQuery**

**CHANGED:**

BigQuery is now available in the [ Las Vegas (us-west4) region
](https://cloud.google.com/bigquery/docs/locations#supported_regions) .

**BigQuery BI Engine**

**CHANGED:**

BigQuery BI Engine is now available in the [ Las Vegas (us-west4) region
](https://cloud.google.com/bi-engine/docs/locations#supported_regions) .

**BigQuery Data Transfer Service**

**CHANGED:**

BigQuery Data Transfer Service is now available in the [ Las Vegas (us-west4)
region ](https://cloud.google.com/bigquery-
transfer/docs/locations#supported_regions) .

**BigQuery ML**

**CHANGED:**

BigQuery ML is now available in the [ Las Vegas (us-west4) region
](https://cloud.google.com/bigquery-ml/docs/locations#supported_regions) .

**Cloud Composer**

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.10.2-airflow-1.10.2 ` , ` composer-1.10.2-airflow-1.10.3 ` and ` composer-1.10.2-airflow-1.10.6 ` . The default is ` composer-1.10.2-airflow-1.10.3 ` . Upgrade your Cloud SDK to use features in this release. 

**FIXED:**

  * Fixed an issue with the CloudSQL Proxy HealthCheck that caused the Proxy Pod to restart repeatedly. 
  * The fluentd spec for in-cluster build log exporting now correctly points to the production fluentd image from ` cloud-airflow-releaser ` . This fix is required for Composer to correctly perform in-cluster builds for VPC SC configuration. 
  * Adjusted ImageBuilder to fix PyPI package installation issues when using VPC SC. 
  * Fixed intermittent issues with ` airflow-monitoring ` during the initialization phase. 
  * Fixed an issue that caused the Airflow scheduler and worker pods to take ~10 minutes to terminate. 
  * Fixed an issue with upgrading the image version and improved error handling during Composer environment upgrades. 

**DEPRECATED:**

  * The oldest supported version of Composer is now ` composer-1.6.0-airflow-x.x.x `

**Cloud Load Balancing**

**FEATURE:**

[ Google-managed SSL certificates ](https://cloud.google.com/load-
balancing/docs/ssl-certificates/google-managed-certs) are available in
**General Availability** .

**Cloud Logging**

**CHANGED:**

The Logs Viewer (Preview) is now GA. To learn more, go to the [ Logs Viewer
(Preview) Overview page ](https://cloud.google.com/logging/docs/view/logs-
viewer-preview) .

**Dataproc**

**FEATURE:**

Dataproc on GKE version ` 1.4.27-beta ` is available with minor fixes.

##  April 25, 2020

**Dialogflow**

**CHANGED:**

In May 2020, the [ Facebook Messenger
](https://cloud.google.com/dialogflow/docs/integrations/facebook) integration
will be updated, and you may notice slight changes related to fulfillment.

To make sure that your Facebook Messenger bot keeps functioning normally,
observe the following recommendations:

  1. To get the Facebook ` sender.id ` value, use the ` originalDetectIntentRequest.payload.data.sender ` field from the Dialogflow ` WebhookRequest ` message. 
  2. To get the ` source ` field value, use the ` originalDetectIntentRequest.source ` field from the Dialogflow ` WebhookRequest ` message. 
  3. To send rich response messages from your webhook to the Facebook Messenger integration, use the ` WebhookResponse.fulfillment_mesages[].payload ` field. 
  4. In your webhook logic, don’t rely on the fields that are not documented in the official [ Facebook Messenger API ](https://developers.facebook.com/docs/messenger-platform/reference/) . 

If you have any questions, reach out to your primary [ support channel
](https://cloud.google.com/dialogflow/docs/support/getting-support#one-on-one)
.

##  April 24, 2020

**AI Platform Prediction**

**FEATURE:**

Visualization settings for AI Explanations are now available. You can
customize how feature attributions are displayed for image data.

Learn more about [ visualizing explanations ](https://cloud.google.com/ai-
platform/prediction/docs/ai-explanations/visualizing-explanations) .

**Dataproc**

**FEATURE:**

**Image 1.5**

Delta Lake version is upgraded to 0.5.0 release. Delta Lake Hive Connector
0.1.0 is also added to the 1.5 image.

**FEATURE:**

Customers can now adjust the amount of time the Dataproc startup script will
wait for Presto Coordinator service to start before deciding that their
startup has succeeded. This is set via ` dataproc:startup.component.service-
binding-timeout.presto-coordinator ` property and takes a value in seconds.
The maximum respected value is 1800 (30 minutes).

**CHANGED:**

New [ sub-minor
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions#supported_cloud_dataproc_versions) image versions: 1.2.96-debian9,
1.3.56-debian9, 1.4.27-debian9, 1.3.56-debian10, 1.4.27-debian10,
1.5.2-debian10, 1.3.56-ubuntu18, 1.4.27-ubuntu18, 1.5.2-ubuntu18

**CHANGED:**

**Image 1.5**

Cloud Storage connector upgraded to version 2.1.2 (for more information,
review the [ change notes ](https://github.com/GoogleCloudDataproc/hadoop-
connectors/releases/tag/v2.1.2) in the GitHub repository)

**FIXED:**

**Image 1.5**

Notebook bug fixes: fixed a bug in Zeppelin and Jupyter that resulted in a
failure to render images when using Component Gateway. Also fixed a Jupyter
Notebooks bug that [ caused notebook downloads to fail
](https://github.com/jupyter/notebook/issues/4869) .

**Virtual Private Cloud**

**FEATURE:**

[ Private Google Access for on-premises hosts
](https://cloud.google.com/vpc/docs/private-access-options#pga-onprem) permits
on-premises hosts to send traffic from any internal IP addresses, not just RFC
1918 addresses. This feature is now **Generally Available** .

##  April 23, 2020

**Anthos**

**FEATURE:**

[ Anthos ](https://cloud.google.com/anthos) 1.3.1 is now available.

**Updated components:**

  * [ Anthos GKE on-prem release notes ](https://cloud.google.com/anthos/gke/docs/on-prem/release-notes)

**Anthos Config Management**

**CHANGED:**

Anthos Config Management images are now included in the Google-provided system
images for [ Binary Authorization ](https://cloud.google.com/binary-
authorization) .

**FEATURE:**

Policy Agent now allows configuration of namespaces that will bypass the
admission controller. For more information, see [ Excluding Namespaces from
Policy Controller ](https://cloud.google.com/anthos-config-
management/docs/how-to/policy-controller-exclude-namespaces)

**CHANGED:**

You can now [ exempt Namespaces ](https://cloud.google.com/anthos-config-
management/docs/how-to/policy-controller-exclude-namespaces) from Policy
Controller enforcement

**FIXED:**

Anthos Config Management v1.3.1 now supports Kubernetes v1.16 and higher.
Earlier versions of Anthos Config Management relied on APIs that have been [
deprecated in Kubernetes v1.16 ](https://cloud.google.com/kubernetes-
engine/docs/deprecations/apis-1-16) .

**FIXED:**

The Anthos Config Management Syncer pod now reports when it detects that it is
fighting with another process over a resource.

**FIXED:**

Anthos Config Management no longer allows managing resources in unmanaged
Namespaces.

**ISSUE:**

If you define a CRD with an integer field that has min/max values, Anthos
Config Management will be unable to update the CRD.

**FIXED:**

Anthos Config Management no longer overwrites undeclared labels and
annotations on Namespaces.

**Anthos GKE on-prem**

**CHANGED:**

Preflight check in ` gkeadm ` for access to the Cloud Storage bucket that
holds the admin workstation OVA.

**CHANGED:**

Preflight check for internet access includes additional URL `
www.googleapis.com ` .

**CHANGED:**

Preflight check for test VM DNS availability.

**CHANGED:**

Preflight check for test VM NTP availability.

**CHANGED:**

Preflight check for test VM F5 access.

**CHANGED:**

Before downloading and creating VM templates from OVAs, GKE on-prem checks if
the VM template already exists in vCenter.

**CHANGED:**

Rename ` gkeadm ` ’s automatically created service accounts.

**CHANGED:**

OVA download displays download progress.

**CHANGED:**

` gkeadm ` prepopulates ` bundlepath ` in the seed config on the admin
workstation.

**CHANGED:**

Fix for Docker failed DNS resolution on admin workstation at startup.

**CHANGED:**

Admin workstation provisioned by ` gkeadm ` uses thin disk provisioning.

**CHANGED:**

Improved user cluster Istio ingress gateway reliability.

**CHANGED:**

Ubuntu image is upgraded to include newest packages.

**CHANGED:**

Update the vCenter credentials for your clusters using the preview command [ `
gkectl update credentials vsphere `
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/updating-cluster-
credentials) .

**FIXED:**

The ` gkeadm ` configuration file, ` admin-ws-config.yaml ` , accepts paths
that are prefixed with ` ~/ ` for the Certificate Authority (CA) certificate.

**FIXED:**

Test VMs wait until the network is ready before starting preflight checks.

**FIXED:**

Improve the error message in preflight check failure for F5 BIG-IP.

**FIXED:**

Skip VIP check in preflight check in manual load balancing mode.

**FIXED:**

Upgraded Calico to version 3.8.8 to fix several security vulnerabilities.

**FIXED:**

Upgraded F5 BIG-IP Controller Docker image to version 1.14.0 to fix a security
vulnerability.

**FIXED:**

Fixed ` gkeadm ` admin workstation ` gcloud ` proxy username and password
configuration.

**FIXED:**

Fixed the bug that was preventing ` gkectl check-config ` from automatically
using the proxy that you set in your configuration file when running the full
set of [ preflight validation checks
](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/preflight-checks)
with any GKE on-prem [ download image
](https://cloud.google.com/anthos/gke/docs/on-prem/downloads#bundle-latest) .

**FIXED:**

Fixed an admin workstation upgrade failure when the upgrade process was unable
to retrieve SSH keys, which would cause a Golang segmentation fault.

**Cloud Billing**

**FEATURE:**

For customers with [ self-serve/online
](https://cloud.google.com/billing/docs/concepts#billing_account_types) Cloud
Billing accounts, you can now find your Cloud Billing documents in the
**Documents** page of the Cloud Billing console. In the Documents page, you
can find your monthly invoices or statements, as well as tax documents, if
applicable to your account. Before this launch, the Documents page was only
available to customers viewing [ invoiced
](https://cloud.google.com/billing/docs/concepts#billing_account_types) Cloud
Billing accounts, while self-serve/online accounts were limited to finding
their Cloud Billing documents in the Transactions page. See the [
⁠documentation ](https://cloud.google.com/billing/docs/how-to/get-invoice) for
more details.

**CHANGED:**

Cost forecasts in Cloud Billing reports has been updated to calculate your
forecasted spend up to 12 months in the future. Previously, the calculation
forecasted your spend for the next 30 days. Cost forecasts make it easier to
see at a glance how your costs are trending and how much you are projected to
spend over a time range you specify. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/reports#cost-forecast) for more
information.

**Cloud Load Balancing**

**FEATURE:**

External HTTP(S) load balancers now support [ header-based routing
](https://cloud.google.com/load-balancing/docs/https/setting-up-traffic-
management#http-header-based-routing) and [ query parameter-based routing
](https://cloud.google.com/load-balancing/docs/https/setting-up-traffic-
management#query-parameter-routing) .

These features are available in **General Availability** .

##  April 22, 2020

**BigQuery ML**

**FEATURE:**

BigQuery ML now supports exporting BigQuery ML models to Cloud Storage and
using them for online prediction. This feature is in [ beta
](https://cloud.google.com/products#product-launch-stages) . For more
information, see [ Exporting models ](https://cloud.google.com/bigquery-
ml/docs/exporting-models) .

**Cloud Billing**

**FEATURE:**

Budget alerts: new budget filters are now available. In addition to project
and product filters, you can now scope your budgets and alerts for groups of
subaccounts and resource labels. Budget alerts help you stay informed of how
your spend is tracking against your budget so you can avoid billing surprises.
(Note that these filters are not available in the Budgets API in this
release.) See the [ ⁠documentation
](https://cloud.google.com/billing/docs/how-to/budgets) for more details.

**Cloud Data Fusion**

**FEATURE:**

Cloud Data Fusion version 6.1.2 is now available. This version includes
several stability and performance improvements and new features.

  * Added support for [ Field Level Lineage ](https://cloud.google.com/data-fusion/docs/tutorials/lineage) for Spark plugins and Streaming pipelines 
  * Added support for Spark 2.4 
  * Added an option to skip header in the files in delimited, CSV, TSV, and text formats 
  * Added an option for database source to replace the characters in the field names 

**FIXED:**

Reduced preview startup by 60%. Also added limit to max concurrent preview
runs (10 by default).

**FIXED:**

Fixed a bug that caused errors when Wrangler's parse-as-csv with header was
used when reading multiple small files.

**FIXED:**

Fixed a bug that caused zombie processes when using the Remote Hadoop
Provisioner.

**FIXED:**

Fixed a bug that caused DBSource plugin to fail in preview mode.

**FIXED:**

Fixed a race condition that caused a failure when running a Spark program.

##  April 21, 2020

**Cloud TPU**

**FEATURE:**

Cloud TPUs and Cloud TPU Pods now support PyTorch 1.5 via the PyTorch/XLA
integration. This integration makes it possible for PyTorch users to do
everything they can do on GPUs on Cloud TPUs, while minimizing changes to the
user experience. You can try out PyTorch on an 8-core Cloud TPU device for
free via Google Colab, and you can use PyTorch on Cloud TPUs at a much larger
scale on Google Cloud (all the way up to full Cloud TPU Pods).

See the ⁠ [ PyTorch/XLA 1.5 Release Notes
](https://github.com/pytorch/xla/releases/tag/v1.5.0) for a complete list of
features included in this release.

**Config Connector**

**CHANGED:**

Miscellaneous bug fixes and improvements

##  April 20, 2020

**App Engine flexible environment .NET**

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV)

**App Engine flexible environment Go**

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

**App Engine flexible environment Java**

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

**App Engine flexible environment Node.js**

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

**App Engine flexible environment PHP**

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

**App Engine flexible environment Ruby**

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

**App Engine flexible environment custom runtimes**

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

**App Engine standard environment Go**

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

**App Engine standard environment Java**

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

**CHANGED:**

  * Updated Java SDK to Version 1.9.80 
  * Fixed deployment of cron.yaml file with retry_parameters configured 
  * Fixed class LocalTaskQueueTestConfig to support custom paths for queue.yaml files ( [ public issue 138528920 ](https://issuetracker.google.com/138528920) ) 

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

**App Engine standard environment Node.js**

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

**App Engine standard environment PHP**

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

**App Engine standard environment Python**

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

**App Engine standard environment Ruby**

**FEATURE:**

App Engine is now available in the ` us-west4 ` region (Las Vegas, NV).

**Cloud Bigtable**

**FEATURE:**

Cloud Bigtable is now available in the [ ` us-west4 ` (Las Vegas) region
](https://cloud.google.com/bigtable/docs/locations) .

**Cloud Key Management Service**

**FEATURE:**

Cloud KMS and Cloud EKM resources are available in the ` us-west4 ` region.
Cloud HSM resources are **not** available in this region.

Cloud HSM resources are available in the ` global ` multi-regional location.

For information about which [ Cloud Locations
](https://cloud.google.com/about/locations/) are supported by Cloud KMS, Cloud
HSM, and Cloud EKM, see the [ Cloud KMS regional locations
](https://cloud.google.com/kms/docs/locations#regional) .

**Cloud Load Balancing**

**FEATURE:**

[ Internal TCP/UDP Load Balancing with failover groups
](https://cloud.google.com/load-balancing/docs/internal/failover-overview) is
available in **General Availability** .

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

**Cloud SQL for MySQL**

**FEATURE:**

Support for [ us-west4 ](https://cloud.google.com/sql/docs/mysql/locations)
region (Las Vegas).

**Cloud SQL for PostgreSQL**

**FEATURE:**

Support for [ us-west4 ](https://cloud.google.com/sql/docs/postgres/locations)
region (Las Vegas).

**Cloud SQL for SQL Server**

**FEATURE:**

Support for [ us-west4
](https://cloud.google.com/sql/docs/sqlserver/locations) region (Las Vegas).

**Cloud Spanner**

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances#available-configurations-
regional) can now be created in Las Vegas (us-west4).

**Cloud Storage**

**FEATURE:**

Las Vegas region ( ` us-west4 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

**Cloud VPN**

**FEATURE:**

Cloud VPN is now available in [ region
](https://cloud.google.com/compute/docs/regions-zones/#available) us-west4
(Las Vegas, Nevada, USA).

Pricing is available on the [ Cloud VPN pricing page
](https://cloud.google.com/vpn/pricing) .

**Compute Engine**

**FEATURE:**

  * The ` us-west4 ` Las Vegas, Nevada region is now available to all projects and users. The zones in the ` us-west4 ` region have [ N1 and E2 machine types ](https://cloud.google.com/compute/docs/machine-types) . See [ Regions and zones ](https://cloud.google.com/compute/docs/regions-zones) for more information. 

**Dataflow**

**FEATURE:**

Dataflow is now able to use workers in zones in the ` us-west4 ` region (Las
Vegas).

**Dataproc**

**CHANGED:**

Dataproc is now available in the ` us-west4 ` [ region
](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available)
(Las Vegas).

**Datastore**

**FEATURE:**

Support for [ ` us-west4 ` region (Las Vegas)
](https://cloud.google.com/datastore/docs/locations) .

**Dialogflow**

**FEATURE:**

Beta launch of one-click integrations with two telephony partners:

  * [ AudioCodes ](https://cloud.google.com/dialogflow/docs/integrations/audiocodes)
  * [ SignalWire ](https://cloud.google.com/dialogflow/docs/integrations/signalwire)

**Filestore**

**FEATURE:**

Filestore is available in the ` us-west4 ` (Las Vegas) region. See [ Regions
and zones ](https://cloud.google.com/filestore/docs/regions) .

**Firestore**

**FEATURE:**

Support for [ ` us-west4 ` region (Las Vegas)
](https://cloud.google.com/firestore/docs/locations) .

**Memorystore for Redis**

**FEATURE:**

Added new Memorystore for Redis [ region
](https://cloud.google.com/memorystore/docs/redis/regions) : Las Vegas ( ` us-
west4 ` ).

**Virtual Private Cloud**

**FEATURE:**

For auto mode VPC networks, added a new subnet ` 10.182.0.0/20 ` for the Las
Vegas ` us-west4 ` region. For more information, see [ Auto mode IP ranges
](https://cloud.google.com/vpc/docs/vpc#ip-ranges) .

**CHANGED:**

[ Packet Mirroring pricing ](https://cloud.google.com/compute/network-
pricing#packet-mirroring) will come into effect from June 20, 2020. There is
no charge for Packet Mirroring until that time.

