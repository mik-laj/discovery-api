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

##  April 28, 2020

**Anthos Service Mesh**

**FEATURE:**

The Anthos Service Mesh dashboard in the Google Cloud Console is generally
available for Anthos Service Mesh installations on Google Kubernetes Engine
clusters. For more information, see the [ Observability overview
](https://cloud.google.com/service-mesh/docs/observability-overview) .

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
admission controller. For more information, please see [ Excluding Namespaces
from Policy Controller ](https://cloud.google.com/anthos-config-
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

**FIXED:**

This release includes several performance and memory improvements.

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

##  April 17, 2020

**BigQuery ML**

**FEATURE:**

BigQuery ML now supports Matrix Factorization models for recommendations, as a
[ beta ](https://cloud.google.com/products#product-launch-stages) release. For
more information, see [ The CREATE MODEL statement for Matrix Factorization
](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-
syntax-create-matrix-factorization) .

**Cloud CDN**

**FEATURE:**

Cloud CDN [ request logs ](https://cloud.google.com/cdn/docs/logging) now
include a ` cacheId ` field, which captures the location and cache node the
client connected to. A ` cacheId ` of ` LHR-1209ea83 ` indicates a client
connected to an edge cache near London, with ` 1209ea83 ` representing the
opaque ID of the cache instance their response was served from.

Location codes map to ⁠ [ IATA codes
](https://en.wikipedia.org/wiki/IATA_airport_code) . The ` cacheId ` field can
be found within the ` jsonPayload ` object in each log entry.

**Cloud Composer**

**BREAKING:**

Composer version 1.10.1 has been rolled back. If you created an environment
with ` composer-1.10.1-airflow-* ` , you can retrieve and delete the
environment, but not update it. We recommend that you delete the environment
and create a new environment with the latest image version. Refer to the March
20, 2020 release notes for default version.

**Cloud Spanner**

**FEATURE:**

Cloud Spanner Backup and Restore is now [ generally available
](https://cloud.google.com/products#product-launch-stages) , enabling you to
create backups of Cloud Spanner databases on demand, and restore them. For
more information, see [ Backup and Restore
](https://cloud.google.com/spanner/docs/backup) .

**FEATURE:**

Query Optimizer Versioning is now [ generally available
](https://cloud.google.com/products#product-launch-stages) , enabling you to
select which version of the optimizer to use for your database, application or
query. For more information, see [ Query optimizer
](https://cloud.google.com/spanner/docs/query-optimizer/overview) .

**Dataproc**

**FEATURE:**

Announcing the [ Beta ](https://cloud.google.com/products#product-launch-
stages) release of [ Dataproc on Google Kubernetes Engine
](https://cloud.google.com/dataproc/docs/concepts/jobs/dataproc-gke) .
Customers can now create Dataproc on GKE clusters to run Spark jobs on
Kubernetes via the Dataproc jobs API.

##  April 16, 2020

**BigQuery**

**FEATURE:**

[ BigQuery Reservations ](https://cloud.google.com/bigquery/docs/reservations-
intro) is now [ Generally Available (GA)
](https://cloud.google.com/products/?hl=EN#product-launch-stages) . BigQuery
Reservations allows you to purchase BigQuery [ slots
](https://cloud.google.com/bigquery/docs/slots) to take advantage of BigQuery
[ flat-rate pricing
](https://cloud.google.com/bigquery/pricing#flat_rate_pricing) and allocate
slots for workload management.

**CHANGED:**

Around the end of April 2020, [ ` INFORMATION_SCHEMA ` (Beta) views for
dataset metadata ](https://cloud.google.com/bigquery/docs/information-schema-
datasets) will return metadata about all datasets in a region. Currently,
these views return metadata about all datasets in the project across all
regions. This upcoming change will also provide support for querying a
specific region's metadata (for example, ` region-
us.INFORMATION_SCHEMA.SCHEMATA ` instead of ` INFORMATION_SCHEMA.SCHEMATA ` ).

You can replicate this future behavior now by filtering on the ` SCHEMATA `
view's ` LOCATION ` column (for example, ` LOCATION = 'US' ` ).

**Cloud Billing**

**FEATURE:**

Discount sharing for committed use discounts is now available in **beta** .
With discount sharing enabled, you can apply your purchased commitments across
multiple projects within a single Cloud Billing account. Discount sharing
helps you minimize the overhead of managing each of your commitments
individually and provides increased flexibility so that you can use the
compute options that best suit your needs, while also increasing cost
predictability.

  * For more information about enabling committed use discount sharing, see [ Turning on committed use discount sharing ](https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#turning_on_committed_use_discount_sharing) . 
  * For more information on the possible cost savings using committed use discount sharing, see [ Understanding discount sharing ](https://cloud.google.com/billing/docs/how-to/cud-analysis#understanding_discount_sharing) . 

**FEATURE:**

Cloud Billing console now has a Pricing report, providing a tabular view of
the prices of Google’s cloud services SKUs, including Google Cloud, Google
Maps Platform, and G Suite. You can select to view the SKUs with historical
usage on the billing account or all Google Cloud SKUs. If you have a
negotiated contract, the pricing table will include the list price, the
contract price and the effective discount. You can also download the table to
CSV for offline analysis. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/pricing-table) for more
details.

**Cloud Data Loss Prevention**

**FEATURE:**

Added support for ` PDF ` and ` WORD ` [ ` FileTypes `
](http://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#filetype)
and ` PDF ` and ` WORD_DOCUMENT ` [ ` BytesTypes `
](http://cloud.google.com/dlp/docs/reference/rpc/google.privacy.dlp.v2#bytestype)
.

**Compute Engine**

**FEATURE:**

  * Committed use discount shared billing is now available in **beta** . You can share committed use discounts among all your projects that fall under the same billing account. For more information, see [ Signing up committed use discounts ](https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) . 

**Dataprep by Trifacta**

**FIXED:**

TD-47149: Cannot edit settings when importing Google Sheets.

**Google Cloud Marketplace Partners**

**FEATURE:**

You can now create private quotes for VM solutions ( [ alpha
](https://cloud.google.com/products/?hl=EN#product-launch-stages) ).

[ Learn about creating quotes for specific customers
](https://cloud.google.com/marketplace/docs/partners/create-quotes) .

**Network Intelligence Center**

**FEATURE:**

[ Performance Dashboard ](https://cloud.google.com/network-intelligence-
center/docs/performance-dashboard/concepts/overview) is now available in
**General Availability** .

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

**Compute Engine**

**FEATURE:**

You can identify VM instances that are not being used with [ idle VM
recommendations ](https://cloud.google.com/compute/docs/instances/viewing-and-
applying-idle-vm-recommendations) . Use these recommendations to reduce unused
resources and reduce your compute bill. This feature is **Generally
available** .

**FEATURE:**

You can manage, maintain, and view patch compliance for your VM instances
using the OS patch management feature. For more information, see [ OS patch
management ](https://cloud.google.com/compute/docs/os-patch-management) . This
feature is now **Generally available** .

**FEATURE:**

The latest stable version of the OS Config agent is [ ` 20200402.01 `
](https://github.com/GoogleCloudPlatform/osconfig/releases/tag/20200402.01) .
If you were using OS patch management in Beta, you can update the agent on
your existing VMs, see [ Updating the OS Config agent
](https://cloud.google.com/compute/docs/manage-os#update-agent) .

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
now includes two default catalogs:

  * ` bigquery ` pointing to the datasets of the cluster's project 

  * ` bigquery_public_data ` pointing to the public datasets 

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

**Google Cloud Armor**

**FEATURE:**

Google Cloud Armor support for CDN origins and hybrid origins is now available
in **General Availability** .

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

**App Engine flexible environment PHP**

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

**Compute Engine**

**FEATURE:**

  * **GA:** [ Compute Engine enables Shielded VM features by default ](https://cloud.google.com/compute/docs/instances/modifying-shielded-vm) . 

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

**Compute Engine**

**FEATURE:**

  * You can identify idle persistent disk resources by using [ idle persistent disk recommendations ](https://cloud.google.com/compute/docs/disks/viewing-and-applying-idle-pd-recommendations) . Following these recommendations will help reduce unused resources and reduce your compute bill. This feature is in **Beta** . 

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

**Compute Engine**

**FEATURE:**

  * C2 machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * Ashburn, Northern Virginia, USA ` us-east4-b,c `

**FEATURE:**

  * N2 machine types are now available in the following [ regions and zones ](https://cloud.google.com/compute/docs/regions-zones#available) : 

    * The Dalles, Oregon, USA ` us-west1-b `
    * Ashburn, Northern Virginia, USA ` us-east4-a `
    * St. Ghislain, Belgium ` europe-west1-d `

**FEATURE:**

  * [ N2D machine types ](https://cloud.google.com/compute/docs/machine-types#n2d_machine_types) are now **Generally Available** . 

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

**Cloud Asset Inventory**

**FEATURE:**

BigQuery export for org policies and access policies

You can now export org policies and access policies to BigQuery tables. See [
Exporting assets to BigQuery ](https://cloud.google.com/asset-
inventory/docs/exporting-to-bigquery) for more information.

**FEATURE:**

Real-time asset monitoring for org policies and access policies

You can now subscribe to real-time notifications for changes to org policies
and access policies. See [ Monitoring asset changes
](https://cloud.google.com/asset-inventory/docs/monitoring-asset-changes) for
more information.

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

