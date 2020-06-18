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

##  June 17, 2020

**Cloud Debugger**

**FEATURE:**

Cloud Debugger now lets you canary snapshots and logpoints on your Python
applications. To learn more, see the [ Python page for setting up Cloud
Debugger ](https://cloud.google.com/debugger/docs/setup/python) .

**Memorystore for Memcached**

**FEATURE:**

Added new Memorystore for Memcached [ regions
](https://cloud.google.com/memorystore/docs/memcached/regions) : Finland ( `
europe-north1 ` ), Hong Kong ( ` asia-east2 ` ), Jakarta ( ` asia-southeast2 `
), Las Vegas ( ` us-west4 ` ), Montréal ( ` northamerica-northeast1 ` ),
Mumbai ( ` asia-south1 ` ), Osaka ( ` asia-northeast2 ` ), Salt Lake City ( `
us-west3 ` ), São Paulo ( ` southamerica-east1 ` ), Seoul ( ` asia-northeast3
` ), and Zurich ( ` europe-west6 ` ).

##  June 16, 2020

**BigQuery**

**FEATURE:**

[ ` INFORMATION_SCHEMA ` views for jobs
](https://cloud.google.com/bigquery/docs/information-schema-jobs) are now [
generally available (GA) ](https://cloud.google.com/products/?hl=EN#product-
launch-stages) .

**BigQuery Data Transfer Service**

**FEATURE:**

The [ Top Brands report ](https://cloud.google.com/bigquery-
transfer/docs/merchant-center-top-brands-schema) for Google Merchant Center
Best Sellers exports is now in [ beta
](https://cloud.google.com/products/#product-launch-stages) .

**BigQuery ML**

**FEATURE:**

BigQuery ML now supports [ beta ](https://cloud.google.com/products#product-
launch-stages) integration with [ AI Platform ](https://cloud.google.com/ai-
platform) . The following models are supported in [ beta
](http://cloud/products#product-launch-stages) :

  * AutoML Tables models. For more information, see [ CREATE MODEL statement for AutoML Tables models ](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-automl) . 

  * Boosted Tree models using XGBoost. For more information, see [ CREATE MODEL statement for Boosted Tree models ](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-boosted-tree) . 

  * Deep Neural Network (DNN) models. For more information, see [ CREATE MODEL statement for DNN models ](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-dnn-models) . 

**Cloud Interconnect**

**CHANGED:**

The public documentation for Cloud Interconnect is now located under the [
Network Connectivity page ](https://cloud.google.com/network-
connectivity/docs/) .

**Cloud Router**

**CHANGED:**

The public documentation for Cloud Router is now located under the [ Network
Connectivity page ](https://cloud.google.com/network-connectivity/docs/) .

**Cloud Run**

**FEATURE:**

The Cloud Run user interface now allows you to copy a Cloud Run service.

**Cloud VPN**

**CHANGED:**

The public documentation for Cloud VPN is now located under the [ Network
Connectivity page ](https://cloud.google.com/network-connectivity/docs/) .

**Config Connector**

**FEATURE:**

You can use ` config-connector ` tool to export Google Cloud resources into
Config Connector: [ documentation ](https://cloud.google.com/config-
connector/docs/how-to/importing-existing-resources)

**FIXED:**

Bug fixes

**Pub/Sub**

**FEATURE:**

[ Retry policies for Pub/Sub subscriptions
](https://cloud.google.com/pubsub/docs/admin#creating_subscriptions) are now
available at the GA launch stage.

##  June 15, 2020

**AI Platform Training**

**FEATURE:**

AI Platform Training now supports [ private services access
](https://cloud.google.com/vpc/docs/private-access-options#service-networking)
in beta. You can use VPC Network Peering to create a private connection so
that training jobs can connect to your network on private IP.

Learn how to set up [ VPC Network Peering with AI Platform Training
](https://cloud.google.com/ai-platform/training/docs/vpc-peering) .

**Anthos Config Management**

**ISSUE:**

A regression in Anthos Config Management 1.3.2 results in unnecessary patches
to the API server for the ` gatekeeper-system ` namespace and spurious logging
for error ` KNV2005 ` . This "fight" results when the ` gatekeeper-system `
namespace is managed in the Git repo, and two Anthos Config Management
components (the operator and syncer) are both trying to reconcile the state of
the namespace with the API server. The only workaround at this time is to [
unmanage ](https://cloud.google.com/anthos-config-management/docs/how-
to/managing-objects#unmanaged-namespaces) the ` gatekeeper-system ` namespace.
The issue will be fixed in Anthos Config Management 1.4.1.

**Anthos Service Mesh**

**FIXED:**

**1.5.5-asm.2**

Fixes a bug in the ` istioctl ` ` HorizontalPodAutoscaling ` setting that
caused Anthos Service Mesh installations to fail.

**Cloud Data Loss Prevention**

**FEATURE:**

Added [ infoType detector ](https://cloud.google.com/dlp/docs/infotypes-
reference) :

  * VEHICLE_IDENTIFICATION_NUMBER 

**Cloud Monitoring**

**CHANGED:**

The Service Monitoring API is now Generally Available. You can use this
feature to create services, set service-level objectives (SLOs), and create
alerting policies to monitor your SLOs. See [ Service monitoring
](https://cloud.google.com/monitoring/service-monitoring/) for documentation,
and [ ` services ` ](https://cloud.google.com/monitoring/api/v3/#service-
monitoring) for reference material.

**Cloud VPN**

**FEATURE:**

Cloud VPN now supports [ an org-level policy
](https://cloud.google.com/vpn/docs/concepts/overview#vpn-org-policy) that
restricts peer IP addresses through a Cloud VPN tunnel.

##  June 12, 2020

**Cloud Build**

**CHANGED:**

Upgraded to Docker server version 19.03.8.

**Cloud Functions**

**FEATURE:**

Cloud Functions is now available in the following regions:

  * ` europe-west6 ` (Zurich) 
  * ` us-west3 ` (Salt Lake City) 

See [ Cloud Functions Locations
](https://cloud.google.com/functions/docs/locations) for details.

**Config Connector**

**FEATURE:**

  * Added ability to [ update streaming DataflowJobs ](https://cloud.google.com/dataflow/docs/guides/updating-a-pipeline) by updating its spec (e.g. ` spec.templateGcsPath ` ). Note that not all fields can be updated, and batch DataflowJobs don't support updates. 
  * Added ` IAMPolicy ` to the output of ` config-connector `

**Virtual Private Cloud**

**FEATURE:**

[ Firewall Rules Logging metadata controls
](https://cloud.google.com/vpc/docs/firewall-rules-logging#log-format) is now
available in **Beta** .

##  June 11, 2020

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M49 release**

TensorFlow Enterprise images updated to 1.15.3 and 2.1.1.

The [ tensorflow-enterprise-addons ](https://pypi.org/project/tensorflow-
enterprise-addons/) package is now available in all deep learning
environments.

XGBoost, MXNet, R, PyTorch, CNTK, and Caffe images have been updated with
library upgrades and bug fixes.

**Access Context Manager**

**FEATURE:**

General availability of the Access Context Manager Bulk API.

Use the Access Context Manager Bulk API to replace all of your organization's
access levels in one operation. For more information, see [ Making bulk
changes to access levels ](https://cloud.google.com/access-context-
manager/docs/bulk-operations) .

**Anthos Service Mesh**

**FIXED:**

**1.5.5-asm.0 and 1.4.10-asm.1**

Fixes the security issue, CVE-2020-11080, with the same fixes as [ OSS Istio
1.5.5 ](https://istio.io/news/releases/1.5.x/announcing-1.5.5/) . The security
fixes were backported to ASM 1.4.10.

**Description**

A vulnerability affecting the HTTP/2 library used by Envoy has been fixed and
publicly disclosed (c.f. Denial of service: Overly large SETTINGS frames ).

[ CVE-2020-11080 ](https://cve.mitre.org/cgi-
bin/cvename.cgi?name=CVE-2020-11080) : By sending a specially crafted packet,
an attacker could cause the CPU to spike at 100%. This could be sent to the
ingress gateway or a sidecar.

**Mitigation**

HTTP/2 support could be disabled on the Ingress Gateway as a temporary
workaround using the following configuration. HTTP/2 support at ingress can
only be disabled if you are not exposing HTTP/2 services that cannot fallback
to HTTP/1.1 through ingress. Note that gRPC services cannot fallback to
HTTP/1.1.

    
    
    apiVersion: networking.istio.io/v1alpha3
    kind: EnvoyFilter
    metadata:
      name: disable-ingress-h2
      namespace: istio-system
    spec:
      workloadSelector:
        labels:
          istio: ingressgateway
      configPatches:
      - applyTo: NETWORK_FILTER # http connection manager is a filter in Envoy
        match:
          context: GATEWAY
          listener:
            filterChain:
              filter:
                name: "envoy.http_connection_manager"
        patch:
          operation: MERGE
          value:
            typed_config:
              "@type": type.googleapis.com/envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager
              codec_type: HTTP1
    

For additional information, see [ ISTIO-SECURITY-2020-006
](https://istio.io/news/security/istio-security-2020-006) .

**App Engine standard environment Go**

**FEATURE:**

The [ Go 1.13 runtime
](https://cloud.google.com/appengine/docs/standard/go/runtime) for the App
Engine standard environment is now generally available.

**Cloud Vision**

**CHANGED:**

**OCR legacy model access extension**

Based on customer feedback, we have decided to extend support of the legacy `
TEXT_DETECTION ` and ` DOCUMENT_TEXT_DETECTION ` models. These legacy models
are accessed by specifying "builtin/legacy_20190601" in the [ ` model `
](https://cloud.google.com/vision/docs/reference/rest/v1/Feature) of a `
Feature ` object.

These models will now be accessible until **November 15, 2020 (6 months from
launch date)** to give customers more time to adapt and migrate to the new
model.

See the  May 15, 2020  release note for the original update announcement.

**Dataproc**

**FEATURE:**

Users can now configure a [ ` tempBucket `
](https://cloud.google.com/dataproc/docs/reference/rest/v1/ClusterConfig#FIELDS.temp_bucket)
in API calls. The temp bucket is a Cloud Storage bucket used to store
ephemeral cluster and jobs data, such as Spark and MapReduce history files. If
you do not specify a temp bucket, Dataproc will determine a Cloud Storage
location (US, ASIA, or EU) for your cluster's temp bucket according to the
Compute Engine zone where your cluster is deployed, and then create and manage
this project-level, per-location bucket.

**CHANGED:**

  * New [ subminor image versions ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#supported_cloud_dataproc_versions) : 1.2.99-debian9, 1.3.59-debian9, 1.4.30-debian9, 1.3.59-debian10, 1.4.30-debian10, 1.5.5-debian10, 1.3.59-ubuntu18, 1.4.30-ubuntu18, and 1.5.5-ubuntu18. 

  * New [ preview image 2.0.0-RC1-debian10, 2.0.0-RC1-ubuntu18 ](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-versions#supported_cloud_dataproc_versions) , with the following components: 

    * Anaconda 2019.10 
    * Atlas 2.0.0 
    * Druid 0.18.1 
    * Flink 1.10.1 
    * Hadoop 3.2.1 
    * HBase 2.2.4 
    * Hive 3.1.2 (with LLAP support) 
    * Hue 4.7.0 
    * JupyterLab 2.1.0 
    * Kafka 2.3.1 
    * Miniconda3 4.8.3 
    * Pig 0.18.0 
    * Presto SQL 333 
    * Oozie 5.2.0 
    * R 3.6.0 
    * Ranger 2.0.0 
    * Solr 8.1.1 
    * Spark 3.0.0 
    * Sqoop 1.5.0 
    * Zeppelin 0.9.0 

**CHANGED:**

  * Image 1.3+ 

    * Patched [ HIVE-23496 ](https://issues.apache.org/jira/browse/HIVE-23496) Adding a flag to disable materialized views cache warm up. 

**CHANGED:**

Druid's Historical's and Broker's JVM and runtime properties are now
calculated using server resources. Previously, only the Historical's and
MiddleManager's ` MaxHeapSize ` property was calculated using server
resources. This change modifies how new values for ` MaxHeapSize ` and `
MaxDirectMemorySize ` properties are calculated for Broker and Historical
processes. Also, new runtime properties ` druid.processing.numThreads ` and `
druid.processing.numMergeBuffers ` are calculated using server resources.

**CHANGED:**

If the project-level staging bucket is manually deleted, it will be recreated
when a cluster is created.

**CHANGED:**

Dataproc now uses [ Compute Engine shielded VMs
](https://cloud.google.com/security/shielded-cloud/shielded-vm) for Debian 10
and Ubuntu 18.04 clusters by default.

**CHANGED:**

Dataproc Job container logging now supports [ Dataproc Kerberized clusters
](https://cloud.google.com/dataproc/docs/concepts/configuring-
clusters/security#create_a_kerberos_cluster) .

**FIXED:**

Image 1.5:

  * Fixed a bug that prevented users from logging on to the Presto UI when using Component Gateway. 

**VPC Service Controls**

**FEATURE:**

General availability for bulk changes to service perimeters.

Using Access Context Manager's Bulk API, you can replace all of your
organization's service perimeters in one operation. For more information, see
[ Making bulk changes to service perimeters ](https://cloud.google.com/vpc-
service-controls/docs/bulk-operations) .

##  June 10, 2020

**Cloud CDN**

**FEATURE:**

HTTP(S) Load Balancing with [ Cloud CDN logging
](https://cloud.google.com/cdn/docs/logging) is available in **General
Availability** .

##  June 09, 2020

**BigQuery**

**FEATURE:**

Clustering for non-partitioned tables is now supported. For more information
about clustered tables, see [ Introduction to clustered tables
](https://cloud.google.com/bigquery/docs/clustered-tables) .

**Cloud Run**

**FEATURE:**

Export a Cloud Run service to a YAML file with ` gcloud run services describe
SERVICE --format export `

##  June 08, 2020

**AI Platform Prediction**

**FIXED:**

The [ **Total latency** chart ](https://cloud.google.com/ai-
platform/prediction/docs/monitor-prediction) on the **Version details** page
of the Google Cloud Console was reporting incorrect information. This chart
has now been fixed.

In some cases, this adjustment might cause latencies to appear higher than
they were previously. However, the latency of models has not changed.

This affects both Compute Engine (N1) machine types and legacy (MLS1) machine
types.

**App Engine flexible environment .NET**

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

**App Engine flexible environment Go**

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

**App Engine flexible environment Java**

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

**App Engine flexible environment Node.js**

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

**App Engine flexible environment PHP**

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

**App Engine flexible environment Ruby**

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

**App Engine standard environment Go**

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

**App Engine standard environment Java**

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

**App Engine standard environment Node.js**

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

**App Engine standard environment PHP**

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

**App Engine standard environment Python**

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

**App Engine standard environment Ruby**

**FEATURE:**

App Engine is now available in the ` asia-southeast2 ` region (Jakarta).

**BigQuery**

**CHANGED:**

BigQuery is now available in the [ Jakarta (asia-southeast2) region
](https://cloud.google.com/bigquery/docs/locations#supported_regions) .

**BigQuery BI Engine**

**CHANGED:**

BigQuery BI Engine is now available in the [ Jakarta (asia-southeast2) region
](https://cloud.google.com/bi-engine/docs/locations#supported_regions) .

**BigQuery Data Transfer Service**

**CHANGED:**

BigQuery Data Transfer Service is now available in the [ Jakarta (asia-
southeast2) region ](https://cloud.google.com/bigquery-
transfer/docs/locations#supported_regions) .

**BigQuery ML**

**CHANGED:**

BigQuery ML is now available in the [ Jakarta (asia-southeast2) region
](https://cloud.google.com/bigquery-ml/docs/locations#supported_regions) .

**Cloud Bigtable**

**FEATURE:**

Cloud Bigtable is now available in the [ ` asia-southeast2 ` (Jakarta) region
](https://cloud.google.com/bigtable/docs/locations) .

**Cloud Key Management Service**

**FEATURE:**

Cloud KMS and Cloud EKM resources are available in the ` asia-southeast2 `
region. Cloud HSM resources are **not** available in this region.

For information about which [ Cloud Locations
](https://cloud.google.com/about/locations/) are supported by Cloud KMS, Cloud
HSM, and Cloud EKM, see the [ Cloud KMS regional locations
](https://cloud.google.com/kms/docs/locations#regional) .

**Cloud Monitoring**

**FEATURE:**

Enhancements to the pre-configured Compute Engine **VM Instances** dashboard.
Compute Engine cross-fleet metrics and detail views specific to CPU, Disk,
Memory, and Network are now available. Use filters to narrow down the set of
VMs being inspected, and use the time selector or in-chart time selection to
change the time window. VMs with the Monitoring agent installed get detailed
memory and disk analysis out of the box.

**Cloud SQL for MySQL**

**FEATURE:**

Support for [ asia-southeast2
](https://cloud.google.com/sql/docs/mysql/locations) region (Jakarta).

**Cloud SQL for PostgreSQL**

**FEATURE:**

Support for [ asia-southeast2
](https://cloud.google.com/sql/docs/mysql/locations) region (Jakarta).

**Cloud SQL for SQL Server**

**FEATURE:**

Support for [ asia-southeast2
](https://cloud.google.com/sql/docs/mysql/locations) region (Jakarta).

**Cloud Spanner**

**FEATURE:**

A second [ multi-region instance configuration
](https://cloud.google.com/spanner/docs/instances#available-configurations-
multi-region) is now available in Europe - ` eur5 ` (London/Belgium).

**FEATURE:**

A [ multi-region instance configuration
](https://cloud.google.com/spanner/docs/instances#available-configurations-
multi-region) is now available in Asia - ` asia1 ` (Tokyo/Osaka).

**FEATURE:**

Cloud Spanner [ regional instances
](https://cloud.google.com/spanner/docs/instances#available-configurations-
regional) can now be created in Jakarta (asia-southeast2).

**Cloud Storage**

**FEATURE:**

Jakarta region ( ` asia-southeast2 ` ) launched.

  * New [ location ](https://cloud.google.com/storage/docs/locations) for storing your data. 

**Cloud VPN**

**FEATURE:**

Cloud VPN is now available in [ region
](https://cloud.google.com/compute/docs/regions-zones/#available) asia-
southeast2 (Jakarta, Indonesia).

Pricing is available on the [ Cloud VPN pricing page
](https://cloud.google.com/vpn/pricing) .

**Compute Engine**

**FEATURE:**

The ` asia-southeast2 ` Jakarta, Indonesia region is now available to all
projects and users. The zones in the ` asia-southeast2 ` region have [ E2 and
N1 machine types ](https://cloud.google.com/compute/docs/machine-types) . See
[ Regions and zones ](https://cloud.google.com/compute/docs/regions-zones) for
more information.

**FEATURE:**

Enhancements to the pre-configured Cloud Monitoring Compute Engine **VM
Instances** dashboard. Compute Engine cross-fleet metrics and detail views
specific to CPU, Disk, Memory, and Network are now available. Use filters to
narrow down the set of VMs being inspected, and use the time selector or in-
chart time selection to change the time window. VMs with the Monitoring agent
installed get detailed memory and disk analysis out of the box.

**Dataflow**

**FEATURE:**

Dataflow is now able to use workers in zones in the ` asia-southeast2 ` region
(Jakarta).

**Dataproc**

**FEATURE:**

Dataproc is now available in the ` asia-southeast2 ` [ region
](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available)
(Jakarta).

**Datastore**

**FEATURE:**

Support for the [ ` asia-southeast2 ` (Jakarta)
](https://cloud.google.com/datastore/docs/locations) .

**Filestore**

**FEATURE:**

[ **High Scale SSD** ](https://cloud.google.com/filestore/docs/high-scale)
tier released to beta. This new service tier for Filestore provides greater
performance and allows you to grow and shrink capacity between 60-320 TB.

**FEATURE:**

[ **IP-based access control**
](https://cloud.google.com/filestore/docs/creating-instances#configuring_ip-
based_access_control) released to beta. This feature allows you to control
access to file shares by the IP addresses of clients.

**CHANGED:**

Filestore service tier name change:

  * **Standard** tier is now called **Basic HDD** . 
  * **Premium** tier is now called **Basic SSD** . 
  * You can still use the old tier names and they will continue to be supported. 

This change may affect you if you use:  
* The ` gcloud beta filestore ` command line tool (beta). * The Filestore beta API (v1beta1). * The Cloud Console in combination with the Filestore API. * The Cloud Console in combination with the ` gcloud ` tool. 

For details, see [ New service tier names
](https://cloud.google.com/filestore/docs/high-scale#new_service_tier_names) .

**FEATURE:**

Filestore is available in the ` asia-southeast2 ` (Jakarta) region. See [
Regions and zones ](https://cloud.google.com/filestore/docs/regions) .

**Firestore**

**FEATURE:**

Support for the [ ` asia-southeast2 ` (Jakarta)
](https://cloud.google.com/firestore/docs/locations) .

**Memorystore for Redis**

**FEATURE:**

Added new Memorystore for Redis [ region
](https://cloud.google.com/memorystore/docs/redis/regions) : Jakarta ( ` asia-
southeast2 ` ).

**Pub/Sub**

**FEATURE:**

Pub/Sub is now available in the ` asia-southeast2 ` region (Jakarta).

**FEATURE:**

Pub/Sub [ message filtering ](https://cloud.google.com/pubsub/docs/filtering)
is now available at the [ beta launch stage
](https://cloud.google.com/products/#product-launch-stages) .

**Virtual Private Cloud**

**FEATURE:**

For auto mode VPC networks, added a new subnet ` 10.184.0.0/20 ` for the
Jakarta ` asia-southeast2 ` region. For more information, see [ Auto mode IP
ranges ](https://cloud.google.com/vpc/docs/vpc#ip-ranges) .

##  June 05, 2020

**Cloud Functions**

**DEPRECATED:**

The Node.js 8 runtime is deprecated as of 2020-06-05. To ensure that your
functions are on a supported version of Node.js, migrate them to [ Node.js 10
](https://cloud.google.com/functions/docs/concepts/nodejs-10-runtime) .

For more discussion of Cloud Functions runtime support policy, see [ Runtime
Support ](https://cloud.google.com/functions/docs/runtime-support) .

**Cloud Logging**

**CHANGED:**

Custom retention is now generally available (GA). In order to have time to
explore this feature, you won't be charged for extended retention of logs
until March 31, 2021. To learn more, see the [ Logging pricing section on the
Pricing for Google Cloud's operations suite page
](https://cloud.google.com/stackdriver/pricing#logging-costs) .

**Compute Engine**

**FEATURE:**

[ CPU overcommit on sole-tenant nodes
](https://cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-
vms) lets you overprovision sole-tenant node resources and schedule more VM
CPUs on a sole-tenant node than are normally available. This feature is in
**Beta** .

**FEATURE:**

[ New sole-tenant node types (m1-node-96-1433 and n2-node-80-640)
](https://cloud.google.com/compute/docs/nodes#node_types) are available in
**Beta** .

##  June 04, 2020

**AutoML Vision Image Classification (ICN)**

**DEPRECATED:**

**v1beta1 endpoint end-of-life**

After June 4, 2020, the v1beta1 version of AutoML API will deny increasing
numbers of API requests from AutoML Vision users. Please refer to the [
November 20, 2019 ](https://cloud.google.com/vision/automl/docs/release-
notes#November_20_2019) release notes and migrate to v1 version immediately.

If you have any questions regarding the above action items, join the [ cloud-
vision-discuss Google group ](https://groups.google.com/g/cloud-vision-
discuss) . For further assistance, please open an issue in this [ private
issue tracker
](https://issuetracker.google.com/issues/new?component=836902&template=1440861)
.

**AutoML Vision Object Detection**

**DEPRECATED:**

**v1beta1 endpoint end-of-life**

After June 4, 2020, the v1beta1 version of AutoML API will deny increasing
numbers of API requests from AutoML Vision users. Please refer to the [
November 20, 2019 ](https://cloud.google.com/vision/automl/object-
detection/docs/release-notes#November_20_2019) release notes and migrate to v1
version immediately.

If you have any questions regarding the above action items, join the [ cloud-
vision-discuss Google group ](https://groups.google.com/g/cloud-vision-
discuss) . For further assistance, please open an issue in this [ private
issue tracker
](https://issuetracker.google.com/issues/new?component=836902&template=1440861)
.

**BigQuery**

**FEATURE:**

BigQuery Table ACL is now available as a [ beta
](https://cloud.google.com/products#product-launch-stages) release. For more
information, see [ Introduction to table access controls
](https://cloud.google.com/bigquery/docs/table-access-controls-intro) .

**Cloud Vision**

**FEATURE:**

**Access Transparency GA**

Access Transparency logging is now Generally Available. If you want to enable
Access Transparency logs, see [ Enabling Access Transparency
](https://cloud.google.com/logging/docs/audit/access-transparency-
overview#enabling) .

**Dataprep by Trifacta**

**FEATURE:**

**Flow parameters:** Create flow parameters that you can reference in the
recipes of your flow.

  * **NOTE:** For this release, flow parameters can be applied into your recipes only. 
  * As needed, you can apply overrides to the parameters in your flow or to downstream flows. 
  * **NOTE:** Flow parameters do not apply to datasets or output objects, which have their own parameters. However, if you specify an override at the flow level, any parameters within the flow that use the same name receive the override value, including output object parameters and datasets with parameters. 
  * See [ Manage Parameters Dialog ](https://cloud.google.com/dataprep/docs/html/Manage-Parameters-Dialog_156863476.html) . 
  * For more information on parameters, see [ Overview of Parameterization ](https://cloud.google.com/dataprep/docs/html/Overview-of-Parameterization_118228665.html) . 

**FEATURE:**

**Introducing new Flow View:** The Flow View page has been redesigned to
improve the user experience and overall productivity.

**NOTE:** This feature is in Beta release.

  * Enhancements include: 
    * Drag and drop to reposition objects on the Flow View canvas, and zoom in and out to focus on areas of development. 
    * Perform joins and unions between objects on the Flow View canvas. 
    * Annotate the canvas with notes. 
  * You can toggle between new and classic views through the context menu in the corner of Flow View. See [ Flow View Page ](https://cloud.google.com/dataprep/docs/html/Flow-View-Page_57344806.html) . 

**FEATURE:**

**Redesigned Settings and Help menus:** See [ Home Page
](https://cloud.google.com/dataprep/docs/html/Home-Page_118228879.html) .

  * User settings are now modified through Preferences. See [ Preferences Page ](https://cloud.google.com/dataprep/docs/html/Preferences-Page_136155223.html) . 

**FEATURE:**

**Report issue:** If you are experiencing an issue with Cloud Dataprep by
TRIFACTA INC., you can gather useful information from the application to
deliver to [ Support ](https://cloud.google.com/support/) .

  * From the Help menu, select **Report issue** . 

**FEATURE:**

**Transformer page:**

  * Join steps are now created in a larger window for more workspace. See [ Join Window ](https://cloud.google.com/dataprep/docs/html/Join-Window_57344880.html) . 
  * New column selection UI simplifies choosing columns in your transformations. See [ Transform Builder ](https://cloud.google.com/dataprep/docs/html/Transform-Builder_57344873.html) . 

**FEATURE:**

**Transformer page performance:**

  * Improved performance when loading the Transformer page and when navigating between the Flow View and Transformer pages. 
  * Faster and improved method of surfacing transform suggestions based on machine learning. 

**FEATURE:**

**PDF profiles:** When visual profiling is enabled for a job, you can now
download your visual profile in PDF format. See [ Job Details Page
](https://cloud.google.com/dataprep/docs/html/Job-Details-Page_57344846.html)
.

**FEATURE:**

**New functions:**

  * New aggregation functions for Datetime values: 
    * [ MINDATE Function ](https://cloud.google.com/dataprep/docs/html/MINDATE-Function_156863338.html)
    * [ MAXDATE Function ](https://cloud.google.com/dataprep/docs/html/MAXDATE-Function_156863339.html)
    * [ MODEDATE Function ](https://cloud.google.com/dataprep/docs/html/MODEDATE-Function_156863340.html)
  * New parsing by data type functions: 
    * [ PARSEBOOL Function ](https://cloud.google.com/dataprep/docs/html/PARSEBOOL-Function_156863406.html)
    * [ PARSEFLOAT Function ](https://cloud.google.com/dataprep/docs/html/PARSEFLOAT-Function_156863407.html)
    * [ PARSEINT Function ](https://cloud.google.com/dataprep/docs/html/PARSEINT-Function_156863405.html)
    * [ PARSEDATE Function ](https://cloud.google.com/dataprep/docs/html/PARSEDATE-Function_145272352.html)
  * New functions for calculating working days between two valid dates: 
    * [ NETWORKDAYS Function ](https://cloud.google.com/dataprep/docs/html/NETWORKDAYS-Function_156863336.html)
    * [ NETWORKDAYSINTL Function ](https://cloud.google.com/dataprep/docs/html/NETWORKDAYSINTL-Function_156863337.html)
    * [ WORKDAY Function ](https://cloud.google.com/dataprep/docs/html/WORKDAY-Function_156863341.html)
    * [ WORKDAYINTL Function ](https://cloud.google.com/dataprep/docs/html/WORKDAYINTL-Function_156863342.html)
  * New time zone conversion functions: 
    * [ CONVERTFROMUTC Function ](https://cloud.google.com/dataprep/docs/html/CONVERTFROMUTC-Function_156863343.html)
    * [ CONVERTTOUTC Function ](https://cloud.google.com/dataprep/docs/html/CONVERTTOUTC-Function_156863344.html)
    * [ CONVERTTIMEZONE Function ](https://cloud.google.com/dataprep/docs/html/CONVERTTIMEZONE-Function_156863345.html)
  * New statistical functions: 
    * [ MEDIAN Function ](https://cloud.google.com/dataprep/docs/html/MEDIAN-Function_156863249.html)
    * [ PERCENTILE Function ](https://cloud.google.com/dataprep/docs/html/PERCENTILE-Function_156863254.html)
    * [ QUARTILE Function ](https://cloud.google.com/dataprep/docs/html/QUARTILE-Function_156863255.html)
    * [ CORREL Function ](https://cloud.google.com/dataprep/docs/html/CORREL-Function_156863232.html)
    * [ COVAR Function ](https://cloud.google.com/dataprep/docs/html/COVAR-Function_156863239.html)
    * [ COVARSAMP Function ](https://cloud.google.com/dataprep/docs/html/COVARSAMP-Function_156863240.html)
  * Ignore case parameter added to string functions: 
    * [ STARTSWITH Function ](https://cloud.google.com/dataprep/docs/html/STARTSWITH-Function_73335390.html)
    * [ ENDSWITH Function ](https://cloud.google.com/dataprep/docs/html/ENDSWITH-Function_73335391.html)
    * [ EXACT Function ](https://cloud.google.com/dataprep/docs/html/EXACT-Function_118228817.html)
    * [ MATCHES Function ](https://cloud.google.com/dataprep/docs/html/MATCHES-Function_57344678.html)
    * [ STRINGGREATERTHAN Function ](https://cloud.google.com/dataprep/docs/html/STRINGGREATERTHAN-Function_99745898.html)
    * [ STRINGGREATERTHANEQUAL Function ](https://cloud.google.com/dataprep/docs/html/STRINGGREATERTHANEQUAL-Function_99745899.html)
    * [ STRINGLESSTHAN Function ](https://cloud.google.com/dataprep/docs/html/STRINGLESSTHAN-Function_99745901.html)
    * [ STRINGLESSTHANEQUAL Function ](https://cloud.google.com/dataprep/docs/html/STRINGLESSTHANEQUAL-Function_99745900.html)
    * [ SUBSTITUTE Function ](https://cloud.google.com/dataprep/docs/html/SUBSTITUTE-Function_99745897.html)

**CHANGED:**

**Parameter overrides:** If you have upgraded to Release 7.1 or later, any
parameter overrides that you have specified in your flows must be re-applied.
For more information, see [ Manage Parameters Dialog
](https://cloud.google.com/dataprep/docs/html/Manage-Parameters-
Dialog_156863476.html) .

**CHANGED:**

**Language:** All MODE functions return the lowest value in a set of values if
there is a tie in the evaluation.

**CHANGED:**

**API Documentation:**

  * API reference documentation is now available directly through the application. This release includes more supported endpoints and documented options. To access, select **Help menu > API Documentation ** . 

  * **NOTE:** API reference content is no longer available with the product documentation. Please use the in-app reference documentation instead. 

  * Workflow documentation is still available with the product documentation. For more information, see [ API Reference ](https://cloud.google.com/dataprep/docs/html/API-Reference_145281441.html) . 

**DEPRECATED:**

**Send a Copy:** You can no longer send a copy of a flow to another user.

  * **New method:** Create a copy of a flow and share it with the other user. 
  * For more information, see [ Share Flow Dialog ](https://cloud.google.com/dataprep/docs/html/Share-Flow-Dialog_118228911.html) . 

**DEPRECATED:**

**Re-run jobs using Cloud Dataflow templates:** This feature is no longer
available. Cloud data flow templates can no longer be used to re-run jobs.

  * **New method:** Please use the /v4/jobGroups endpoint to run and re-run jobs. 
  * For more information, see [ API Reference ](https://cloud.google.com/dataprep/docs/html/API-Reference_145281441.html) . 

**ISSUE:**

**TD-49559:** Cannot select and apply custom data types through column Type
menu.

  * **Workaround:** You can change the type of the column as a recipe step. Use the Change column type transformation. From the New type drop-down, select ` Custom ` . Then, enter the name of the type for the Custom type value. 

**ISSUE:**

**TD-47473:** Uploaded files (CSV, XLS, PDF) that contain a space in the
filename fail to be converted.

  * **Workaround:** Remove the space in the filename and upload again. 

**VPC Service Controls**

**FEATURE:**

The VPC accessible services feature is now generally available. Use VPC
accessible services to limit the access of network endpoints and VMs in a
perimeter to only services protected by that perimeter.

For more information about the feature, see [ VPC accessible services
](https://cloud.google.com/docs/vpc-service-controls/docs/vpc-accessible-
services) .

##  June 03, 2020

**Cloud Load Balancing**

**FEATURE:**

[ HTTP(S) Load Balancing logging ](https://cloud.google.com/load-
balancing/docs/https/https-logging-monitoring#logging) is now available in
**General Availability** .

**Cloud Logging**

**FEATURE:**

In the Logs Viewer (Preview), you can now save your queries, which can then be
viewed and run from the **Saved** queries tab. For more information, see the [
Saved queries section on the Building queries page
](https://cloud.google.com/logging/docs/view/building-queries#saved-queries) .

**Cloud Run**

**FEATURE:**

The Cloud Run user interface now allows you to edit the service YAML.

**Cloud Spanner**

**CHANGED:**

Cloud Spanner SQL now supports the following statistical aggregate functions -
STDDEV, VARIANCE. For more information, see [ Statistical Aggregate Functions
](https://cloud.google.com/spanner/docs/statistical_aggregate_functions) .

**Config Connector**

**CHANGED:**

Miscellaneous bug fixes and improvements

**Memorystore for Redis**

**FEATURE:**

The [ Version Upgrade
](https://cloud.google.com/memorystore/docs/redis/upgrading-instance-version)
and [ Redis version 5.0
](https://cloud.google.com/memorystore/docs/redis/supported-versions) features
are now Generally Available on Memorystore for Redis.

**Virtual Private Cloud**

**FEATURE:**

[ Hierarchical firewall policies ](https://cloud.google.com/vpc/docs/firewall-
policies) are now available in **Beta** .

##  June 02, 2020

**BigQuery**

**FEATURE:**

You can now [ purchase BigQuery slots
](https://cloud.google.com/bigquery/docs/reservations-workload-
management#getting_started_with_reservations) using the ` bq ` command-line
tool. BigQuery Reservations allows you to purchase slots to take advantage of
BigQuery [ flat-rate pricing
](https://cloud.google.com/bigquery/pricing#flat_rate_pricing) and allocate
slots for workload management.

**FEATURE:**

A new GIS function, [ ` ST_Simplify `
](https://cloud.google.com/bigquery/docs/reference/standard-
sql/geography_functions#st_simplify) , is available. [ ` ST_Simplify `
](https://cloud.google.com/bigquery/docs/reference/standard-
sql/geography_functions#st_simplify) returns a simplified version of the input
` GEOGRAPHY ` by replacing sections with straight lines.

**CHANGED:**

Standard SQL view definition bodies can now contain references without project
qualifiers, as long as the view is created by the [ ` tables.insert `
](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables/insert) REST
API or is in the same project used to run the [ ` CREATE VIEW `
](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-
definition-language#create_view_statement) DDL query.

**CHANGED:**

Standard SQL [ user-defined function
](https://cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-
functions) definition bodies can now contain references to tables and views.

**Cloud Load Balancing**

**FEATURE:**

You can now use a [ custom filter ](https://cloud.google.com/load-
balancing/docs/negs/setting-up-zonal-
negs#custom_filtering_when_you_list_endpoints_in_a_network_endpoint_group)
when you list endpoints in a zonal network endpoint group. This feature is
available as a Beta release.

##  June 01, 2020

**Access Context Manager**

**FEATURE:**

General availability of custom access levels.

[ Custom access levels ](https://cloud.google.com/access-context-
manager/docs/custom-access-levels) provide a way to use Common Expression
Language to craft custom conditions. [ Create custom access levels
](https://cloud.google.com/access-context-manager/docs/create-custom-access-
level) using the ` gcloud ` command line tool, the Access Context Manager API,
and in the Google Cloud Console using the Advanced Mode for configuring access
levels.

**Compute Engine**

**FEATURE:**

NVIDIA® Tesla® T4 GPUs are now available in the following additional regions
and zones:

  * Changua County, Taiwan ` asia-east1-c `

For information about using T4 GPUs on Compute Engine, see [ GPUs on Compute
Engine ](https://cloud.google.com/compute/docs/gpus) .

**Dialogflow**

**CHANGED:**

The shutdown of 7 integrations [ announced in January
](https://cloud.google.com/dialogflow/docs/release-notes#January_06_2020) is
now extended to July 6th, 2020.

##  May 29, 2020

**Anthos GKE deployed on AWS**

**CHANGED:**

A new build of Anthos GKE on AWS has been released. This build removes the
need to check AWS IAM privileges when creating a management cluster. **You
don't need to update** if you have not encountered this issue.

To install this build, download the ` anthos-gke ` tool by running the
following command:

` gsutil cp gs://gke-multi-cloud-release/bin/aws-0.2.1-gke.8/anthos-gke . `

Then, recreate your [ Terraform configuration
](https://cloud.google.com/anthos/gke/docs/aws/how-to/installing-management)
and continue with your installation.

**Cloud Billing**

**FEATURE:**

[ ` Labels ` ](https://cloud.google.com/billing/docs/how-to/cost-
table#columns_in_the_cost_table) column added to the [ flat table view
](https://cloud.google.com/billing/docs/how-to/cost-table#flat_table_view) of
the Cloud Billing Cost Table report. The Cost Table report provides a tabular
view of your invoice costs. You can quickly filter your costs by available
fields, such as project, service, SKU, and labels (among other fields), and
you can download the table to CSV for offline analysis. See the [
documentation ](https://cloud.google.com/billing/docs/how-to/cost-table) for
more details.

**Cloud CDN**

**CHANGED:**

To help you get started quickly, added two new examples for setting up Cloud
CDN:

  * [ Setting up Cloud CDN with a managed instance group ](https://cloud.google.com/cdn/docs/setting-up-cdn-with-mig)
  * [ Setting up Cloud CDN with a backend bucket ](https://cloud.google.com/cdn/docs/setting-up-cdn-with-bucket)

**Cloud TPU**

**CHANGED:**

Cloud TPU now supports TensorFlow version 1.15.3. See the [ TensorFlow 1.15.3
Release Notes ](https://github.com/tensorflow/tensorflow/releases/tag/v1.15.3)
.

**Config Connector**

**CHANGED:**

Added support for ` SQLSSLCert `

**CHANGED:**

Supported acquisition of backends added to Compute Backend Services out-of-
band of Config Connector

**FIXED:**

Fixed support for [ autoscaling and manually resizing node pools with
ContainerNodePool ](https://github.com/GoogleCloudPlatform/k8s-config-
connector/issues/165)

**Dialogflow**

**CHANGED:**

The [ Dialogflow Facebook Messenger integration
](https://cloud.google.com/dialogflow/docs/integrations/facebook) has been
updated to to be compliant with newer Facebook Messenger API versions. If you
have an agent that enabled this integration prior to today, you should have
received an email from Dialogflow with upgrade instructions. If you have not
received this email, please [ contact Dialogflow support
](https://cloud.google.com/dialogflow/docs/support/getting-support) .

**Identity-Aware Proxy**

**FEATURE:**

The ability to authenticate users with [ external identities
](https://cloud.google.com/iap/docs/enable-external-identities) is now
generally available.

**Virtual Private Cloud**

**FEATURE:**

GKE annotations and advanced controls for [ VPC Flow Logs
](https://cloud.google.com/vpc/docs/using-flow-logs) is now available in
**General Availability** .

##  May 28, 2020

**Cloud Functions**

**CHANGED:**

Cloud Functions now supports [ Go 1.13
](https://cloud.google.com/functions/docs/concepts/go-runtime) at the [
General Availability release level
](https://cloud.google.com/products/#product-launch-stages) .

**Cloud Key Management Service**

**FEATURE:**

Several fields related to data integrity have been added to the Cloud KMS API,
along with guidelines for using them. To learn more about maintaining data
integrity when performing cryptographic operations, see [ Verifying end-to-end
data integrity ](https://cloud.google.com/kms/docs/data-integrity-guidelines)
.

##  May 27, 2020

**Cloud Billing**

**CHANGED:**

New data property now available for Cloud Billing budget alerts that are
configured for [ programmatic notifications
](https://cloud.google.com/billing/docs/how-to/budgets-programmatic-
notifications) . You set up a Cloud Billing budget to trigger an alert
notification based on [ threshold rules
](https://cloud.google.com/billing/docs/how-to/budgets#alert-thresholds) for
_Actual_ or _Forecasted_ spend. Programmatic notifications triggered on
**Forecasted** costs are now identified with the ` forecastThresholdExceeded `
property in the JSON object. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/budgets-programmatic-
notifications#notification_format) for more details.

**Config Connector**

**CHANGED:**

Added support for ` BigQueryJob ` resource

**Dataproc**

**FEATURE:**

Dataproc now provides beta support for [ Dataproc Hub
](https://cloud.google.com/dataproc/docs/tutorials/dataproc-hub-admins) .

**Google Cloud Armor**

**CHANGED:**

Error correction: Beta flag removed from feature Google Cloud Armor with Cloud
CDN. This feature was released with the status General Availabiliity.

##  May 26, 2020

**Cloud Composer**

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.10.4-airflow-1.10.2 ` , ` composer-1.10.4-airflow-1.10.3 ` and ` composer-1.10.4-airflow-1.10.6 ` . The default is ` composer-1.10.4-airflow-1.10.3 ` . Upgrade your Cloud SDK to use features in this release. 
  * **For Airflow 1.10.6 and later:** The Airflow config property ` [celery] pool ` is now blocked. 

**FIXED:**

  * Fixed an issue with Airflow 1.10.6 environments where task logs were not visible in the UI when DAG serialization was enabled. 

**Cloud Functions**

**FEATURE:**

Cloud Functions has added support for a new runtime, Java 11, in Beta:

  * [ The Java Runtime ](https://cloud.google.com/functions/docs/concepts/java-runtime)

**Pub/Sub**

**FEATURE:**

[ Pub/Sub Lite ](https://cloud.google.com/pubsub/docs/choosing-pubsub-or-lite)
is now available at the [ beta launch stage
](https://cloud.google.com/products/#product-launch-stages) .

**Recommender**

**FEATURE:**

You can now view, prioritize, and apply recommendations in the Google Cloud
Console using Recommendation Hub ( [ Beta
](https://cloud.google.com/products/#product-launch-stages) ).

[ Get started with Recommendation Hub
](https://cloud.google.com/recommender/docs/recommendation-hub/getting-
started) .

##  May 21, 2020

**AI Platform Training**

**FEATURE:**

You can now use TPUs with TensorFlow 2.1 when you create a training job with
runtime version 2.1. You can also [ use TPUs with TensorFlow 2.1 when you
train in a custom container ](https://cloud.google.com/ai-
platform/training/docs/using-tpus#custom-containers) .

Read the [ guide to using TPUs with AI Platform Training
](https://cloud.google.com/ai-platform/training/docs/using-tpus) , which has
been updated to show how to use TPUs with TensorFlow 2 APIs.

**Anthos**

**FEATURE:**

[ Anthos ](https://cloud.google.com/anthos) 1.3.2 is now available.

**Updated components:**

  * [ Anthos GKE on-prem release notes ](https://cloud.google.com/anthos/gke/docs/on-prem/release-notes)
  * [ Anthos Config Management release notes ](https://cloud.google.com/anthos-config-management/docs/release-notes)
  * [ Anthos GKE on AWS ](https://cloud.google.com/anthos/gke/docs/aws/) is available as a limited preview for customers with an existing relationship with Google Cloud. Contact your sales representative for access. 

**Anthos Config Management**

**CHANGED:**

This release includes several performance and memory improvements.

In order to help prevent accidental deletion, Anthos Config Management will no
longer allow a user to remove all namespaces or cluster-scoped resources in a
single commit. If you wish to delete the full set of resources under
management, it now requires two steps: remove all but one in a first commit,
allow ACM to sync those changes, then remove the final resource in a second
commit.

**CHANGED:**

[ Error documentation ](https://cloud.google.com/anthos-config-
management/docs/reference/errors) has been updated to add more information on
error codes. Errors that are no longer encountered in the product have been
removed. Most error references have been embellished with examples and steps
for remediation.

**CHANGED:**

Anthos Config Management now supports a GKE-only authentication mechanism
based on the service account of the cluster's node pool. Documentation on its
use is [ here ](https://cloud.google.com/anthos-config-management/docs/how-
to/installing#git-creds-gcenode) .

**FEATURE:**

Anthos Config Management now includes [ Config Connector
](https://cloud.google.com/config-connector) v1.8.0.

**CHANGED:**

Anthos Config Management will now attempt to detect when resources that it
manages are also managed by other controllers. Documentation on this behavior
is available in [ error ` knv2005 ` ](https://cloud.google.com/anthos-config-
management/docs/reference/errors#knv2005) which ACM will log in that case.

**CHANGED:**

Policy Controller has been upgraded to include a newer version of [ Open
Policy Agent Gatekeeper ](https://github.com/open-policy-
agent/gatekeeper/tree/480baac44179d75d418b88fbd2c80581fcf183dd) .

This version includes updates to improve the management of policy resources.
As a consequence, finalizers are no longer used to manage Constraints and
Constraint Templates.

The following metrics have been made obsolete due to these changes and have
been removed:

  * gatekeeper_watch_manager_is_running 

  * gatekeeper_watch_manager_last_restart_check_time 

  * gatekeeper_watch_manager_last_restart_time 

  * gatekeeper_watch_manager_restart_attempts 

The following metrics were removed and will be re-implemented in a later
version:

  * gatekeeper_watch_manager_intended_watch_gvk 

  * gatekeeper_watch_manager_watched_gvk 

**Anthos GKE on-prem**

**FEATURE:**

Workload Identity is now available in Alpha for GKE on-prem. Please contact
support if you are interested in a trial of Workload Identity in GKE on-prem.

**CHANGED:**

Preflight check for VM internet and Docker Registry access validation is
updated.

**CHANGED:**

Preflight check for internet validation is updated to not follow redirect. If
your organization requires outbound traffic to pass through a proxy server,
you no longer need to whitelist the following addresses in your proxy server:

  * console.cloud.google.com 
  * cloud.google.com 

**CHANGED:**

The Ubuntu image is upgraded to include the newest packages.

**FIXED:**

Upgraded the Istio image to version 1.4.7 to fix a security vulnerability.

**FIXED:**

Some ConfigMaps in the admin cluster were refactored to Secrets to allow for
more granular access control of sensitive configuration data.

**BigQuery**

**CHANGED:**

The BigQuery Storage API now supports reading small anonymous (cached) tables
without any limitations.

**Cloud Billing**

**FEATURE:**

Cloud Billing Budget API: new budget filters for groups of subaccounts and
resource labels are now available in the Budget API. See the [ documentation
](https://cloud.google.com/billing/docs/reference/budget/rest/v1beta1/billingAccounts.budgets)
for more details.

**Cloud Data Loss Prevention**

**FEATURE:**

Added additional [ infoType detectors
](https://cloud.google.com/dlp/docs/infotypes-reference) :

  * IRELAND_DRIVING_LICENSE_NUMBER 
  * IRELAND_EIRCODE 

**Cloud SQL for PostgreSQL**

**FEATURE:**

PostgreSQL version 12 is now generally available. To start using PostgreSQL
12, see [ Creating instances
](https://cloud.google.com/sql/docs/postgres/create-instance) .

**Cloud TPU**

**CHANGED:**

Cloud TPU now supports TensorFlow 2.1.1 with Keras support. See the [
TensorFlow 2.1.1 Release Notes
](https://github.com/tensorflow/tensorflow/releases/tag/v2.1.1) for a complete
list of features included in this release.

**Compute Engine**

**FEATURE:**

E2 shared-core machine types now support committed use discounts in all
regions. See the [ VM instance ](https://cloud.google.com/compute/vm-instance-
pricing#e2_sharedcore_machine_types) pricing page for more information.

**FEATURE:**

You can now SSH to your VMs using hardware-backed SSH key pairs. For more
information, see [ SSH with security keys
](https://cloud.google.com/compute/docs/tutorials/ssh-with-sk) .

**Dataproc**

**FEATURE:**

You can now set ` core:fs.defaultFS ` to a location in Cloud Storage (for
example, ` gs://bucket ` ) when creating a cluster to set Cloud Storage as the
default filesystem. This also sets ` core:fs.gs.reported.permissions ` , the
reported permission returned by the Cloud Storage connector for all files, to
777. If Cloud Storage is not set as the default filesystem, this property will
continue to return 700, the default value.

**FEATURE:**

**Image 1.4 and 1.5**

[ HADOOP-16984 ](https://issues.apache.org/jira/browse/HADOOP-16984) : Enable
persistent history server to read from done directory.

**CHANGED:**

New [ sub-minor versions
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions#supported_cloud_dataproc_versions) of Dataproc images:
1.2.98-debian9, 1.3.58-debian9, 1.4.29-debian9, 1.3.58-debian10,
1.4.29-debian10, 1.5.4-debian10, 1.3.58-ubuntu18, 1.4.29-ubuntu18,
1.5.4-ubuntu18.

**CHANGED:**

**Image 1.3, 1.4, and 1.5**

  * Restrict Jupyter, Zeppelin, and Knox to only accept connections from ` localhost ` when [ Component Gateway ](https://cloud.google.com/dataproc/docs/concepts/accessing/dataproc-gateways) is enabled. This restriction reduces the risk of remote code execution over unsecured notebook server APIs. To override this change, when you create the cluster, set the Jupyter, Zeppelin, and Knox [ cluster properties ](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/cluster-properties) , respectively, as follows: ` dataproc:jupyter.listen.all.interfaces=true ` , ` zeppelin:zeppelin.server.addr=0.0.0.0 ` , and ` knox:gateway.host=0.0.0.0 ` . 

  * Upgrade Hive to version 2.3.7. 

**CHANGED:**

**Image 1.4 and 1.5**

[ SPARK-29367 ](https://issues.apache.org/jira/browse/SPARK-29367) : Add `
ARROW_PRE_0_15_IPC_FORMAT=1 ` in yarn-env.sh to fix the Pandas UDF issue with
` pyarrow ` 0.15.

**CHANGED:**

**Image 1.5**

  * Upgrade Druid to [ version 0.17.1 ](https://github.com/apache/druid/releases/tag/druid-0.17.1) . 

  * Upgrade Cloud Storage Connector to [ version 2.1.3 ](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v2.1.3) . 

  * Upgrade Delta Lake to [ version 0.6.0 ](https://github.com/delta-io/delta/releases/tag/v0.6.0) . 

**CHANGED:**

Hide the "Quit" button from Jupyter notebook ( ` c.NotebookApp.quit_button =
False ` ) when using the [ Jupyter optional component
](https://cloud.google.com/dataproc/docs/concepts/components/jupyter) . The
Jupyter environment is shut down when the cluster is deleted.

**CHANGED:**

Set the ` hive.localize.resource.num.wait.attempts ` property to 25 to improve
reliability of Hive queries.

**FIXED:**

**Image 1.5**

Fix a race condition in which ` hbase-master ` would try to write `
/hbase/.tmp/hbase.version ` to HDFS before HDFS was initialized. This can
increase cluster creation time for clusters created with HBase.

**FIXED:**

  * Fix a race condition in which, when the ` am.primary_only ` property is provided, the "non-preemptible" node label was not added to the resource manager's node label store before node managers started registering with the resource manager. 

  * Store resource manager node labels in Cloud Storage when ` am.primary_only ` property is provided. 

**DEPRECATED:**

The ` dataproc:alpha.state.shuffle.hcfs.enabled ` [ cluster property
](https://cloud.google.com/dataproc/docs/concepts/configuring-
clusters/cluster-properties) has been deprecated. To enable Enhanced
Flexibility Mode (EFM) for Spark, set ` dataproc:efm.spark.shuffle=hcfs ` . To
enable EFM for MapReduce, set ` dataproc:efm.mapreduce.shuffle=hcfs ` .

**VPC Service Controls**

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for the following integration:

  * [ Service Directory ](https://cloud.google.com/service-directory/docs/securing-with-vpc-sc)

**Video Intelligence API**

**FEATURE:**

The following features are available in the Video Intelligence API version
v1p3beta1:

**Face detection** : Locate faces within a video, and identify attributes such
as glasses being worn. [ Learn more ](https://cloud.google.com/video-
intelligence/docs/face-detection)

**Person detection** : Locate people in a video, and identify attributes and
2D landmarks. [ Learn more ](https://cloud.google.com/video-
intelligence/docs/people-detection)

##  May 20, 2020

**Anthos Service Mesh**

**FEATURE:**

**1.5.4-asm.2**

1.5.4-asm.2 is now available.

**FIXED:**

**Security fixes**

1.5.4-asm.2 contains all the same security fixes that are in Anthos Service
Mesh 1.4.

**FEATURE:**

**Beta release of the Anthos CLI**

The Anthos CLI simplifies the installation of Anthos Service Mesh. You can use
the Anthos CLI to:

  * Create a new cluster that meets the Anthos Service Mesh cluster requirements and install Anthos Service Mesh. See [ Installing Anthos Service Mesh on a new cluster using the Anthos CLI ](https://cloud.google.com//service-mesh/docs/gke-anthos-cli-new-cluster) . 
  * Update an existing cluster with the options that Anthos Service Mesh requires and install Anthos Service Mesh. See [ Installing Anthos Service Mesh on an existing cluster using the Anthos CLI ](https://cloud.google.com//service-mesh/docs/gke-anthos-cli-existing-cluster) . 

**BREAKING:**

**Port change for automatic sidecar injection**

If you are installing Anthos Service Mesh on a private cluster, you must add a
firewall rule to open port 15017 if you want to use [ automatic sidecar
injection ](https://cloud.google.com/service-mesh/docs/proxy-injection) . In
Anthos Service Mesh 1.4, the port used for automatic sidecar injection is
9443.

If you don't add the firewall rule and automatic sidecar injection is enabled,
you get an error when you deploy workloads. For details on adding a firewall
rule, see [ Adding firewall rules for specific use cases
](https://cloud.google.com/kubernetes-engine/docs/how-to/private-
clusters#add_firewall_rules) .

**DEPRECATED:**

**The alpha authentication policy is deprecated**

See [ Updating to the beta security policies
](https://cloud.google.com/service-mesh/docs/security/update-authentication-
policies) for more information.

**BREAKING:**

**` IstioOperator ` API replaces ` IstioControlPlane ` API **

The alpha [ ` IstioControlPlane ` API
](https://archive.istio.io/v1.4/docs/reference/config/istio.operator.v1alpha12.pb/#IstioControlPlane)
has been replaced by the [ ` IstioOperator ` API
](https://istio.io/docs/reference/config/istio.operator.v1alpha1/#IstioComponentSetSpec)
. You must use the ` IstioOperator ` API in YAML files to enable optional
features when you install Anthos Service Mesh.

**CHANGED:**

**Istio CNI plugin is supported**

By default Anthos Service Mesh injects an ` initContainer ` , ` istio-init ` ,
in pods deployed in the mesh. The ` istio-init ` container sets up the pod
network traffic redirection to/from the sidecar proxy. This requires the user
or service-account deploying pods to the mesh to have sufficient Kubernetes
RBAC permissions to deploy containers with the ` NET_ADMIN ` and ` NET_RAW `
capabilities. Requiring users to have elevated Kubernetes RBAC permissions is
problematic for some organization's security compliance. The Istio Container
Network Interface (CNI) plugin is a replacement for the ` istio-init `
container that performs the same networking functionality but without
requiring users to enable elevated Kubernetes RBAC permissions.

The Istio CNI plugin performs the mesh pod traffic redirection in the
Kubernetes pod lifecycle's network setup phase, thereby removing the
requirement for the ` NET_ADMIN ` and ` NET_RAW ` capabilities for users
deploying pods into the mesh. The Istio CNI plugin replaces the functionality
provided by the ` istio-init ` container.

**CHANGED:**

**Enabling pod security policies no longer needed**

SDS security was improved by merging Node Agent with Pilot Agent as Istio
Agent and removing cross-pod UDS, which no longer requires users to deploy
Kubernetes pod security policies for UDS connections.

**BigQuery**

**FEATURE:**

Happy 10th birthday, BigQuery!

**FEATURE:**

[ Cloud SQL federated queries ](https://cloud.google.com/bigquery/docs/cloud-
sql-federated-queries) are now generally available [ (GA)
](https://cloud.google.com/terms/launch-stages) .

**FEATURE:**

[ Hourly partitioned tables ](https://cloud.google.com/bigquery/docs/creating-
column-partitions) are now in [ beta
](https://cloud.google.com/products/#product-launch-stages) .

**FEATURE:**

Dynamic SQL is now available as a [ beta
](https://cloud.google.com/products/#product-launch-stages) release in all
BigQuery regions. Dynamic SQL lets you generate and execute SQL statements
dynamically at runtime. For more information, see [ EXECUTE IMMEDIATE
](https://cloud.google.com/bigquery/docs/reference/standard-
sql/scripting#execute_immediate) .

**FEATURE:**

[ BigQuery Trial slots
](https://cloud.google.com/bigquery/pricing#flat_rate_pricing) are now
available in US and EU multi-regions. Trial slots are a limited promotion for
qualified customers.

**Cloud Load Balancing**

**FEATURE:**

For internal TCP/UDP load balancers, you can create [ multiple forwarding
rules with the same IP address ](https://cloud.google.com/load-
balancing/docs/internal/multiple-forwarding-rules-same-ip) . The forwarding
rules can have different protocols and ports. This feature is available in
**Beta** .

**Cloud Monitoring**

**FEATURE:**

Cloud Monitoring introduces an improved experience for viewing and managing
incidents. Improvements include performance optimizations for Workspaces with
large numbers of incidents, summary statics, and the ability to filter by
alerting policy name, metric type, and resource type. For more information,
see [ Incidents and events
](https://cloud.google.com/monitoring/alerts/incidents-events) .

**Cloud Run**

**FEATURE:**

The Cloud Run [ container instance metadata server
](https://cloud.google.com/run/docs/reference/container-contract#metadata-
server) now exposes the unique identifier of the container instance and the
region of the Cloud Run service

**Compute Engine**

**FEATURE:**

If your managed instance group encountered errors - for example, if a VM could
not be created - you can [ view those errors
](https://cloud.google.com/compute/docs/instance-groups/getting-info-about-
migs#listing_instance_errors) to diagnose and mitigate the cause. This is
**Generally available** .

