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

##  July 24, 2020

**Anthos GKE on AWS**

**CHANGED:**

Anthos GKE on AWS is now generally available.

**CHANGED:**

Clusters support in-place upgrades, with the ability to upgrade the control
plane and node pools separately.

**CHANGED:**

Clusters can be deployed in a high availability (HA) configuration, where
control plane instances and node pools are spread across multiple availability
zones.

**CHANGED:**

Clusters have been validated to support up to 200 nodes and 6000 pods.

**CHANGED:**

Allows the number of nodes to be scaled dynamically based on traffic volume to
increase utilization and reduce cost, and improve performance

**CHANGED:**

Anthos can be deployed within existing AWS VPCs, leveraging existing security
groups to secure those clusters. Customers can ingress traffic using NLB and
ALBs. Additionally Anthos on AWS supports AWS IAM and OIDC. This makes
deploying Anthos easy, eliminates the need to provision new accounts, and
minimizes configuration of the environment.

**CHANGED:**

With Anthos Config Management enterprises can set policies on their AWS
workloads and with Anthos Service Mesh, they can monitor, manage, and secure
them.

**CHANGED:**

Kubernetes settings (flags and sysctl settings) have been updated to match
GKE.

**BREAKING:**

Upgrades from beta versions are not supported. To install Anthos GKE on AWS,
you must remove your user and management clusters, then reinstall them.

**Anthos Service Mesh**

**CHANGED:**

Anthos Service Mesh on GKE on AWS is supported.

For more information, see [ Installing Anthos Service Mesh on GKE on AWS
](https://cloud.google.com/service-mesh/docs/gke-on-aws-install) .

**BigQuery**

**CHANGED:**

BigQuery Data Transfer Service is now available in the following regions: [
Montréal (northamerica-northeast1), Frankfurt (europe-west3), Mumbai (asia-
south1), and Seoul (asia-northeast3) ](https://cloud.google.com/bigquery-
transfer/docs/locations#regional-locations) .

**BigQuery Data Transfer Service**

**CHANGED:**

BigQuery Data Transfer Service is now available in the following regions: [
Montréal (northamerica-northeast1), Frankfurt (europe-west3), Mumbai (asia-
south1), and Seoul (asia-northeast3) ](https://cloud.google.com/bigquery-
transfer/docs/locations#regional-locations) .

**Cloud Composer**

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.11.0-airflow-1.10.2 ` , ` composer-1.11.0-airflow-1.10.3 ` , ` composer-1.11.0-airflow-1.10.6 ` , and ` composer-1.11.0-airflow-1.10.9 ` . The default is ` composer-1.11.0-airflow-1.10.3 ` . Upgrade your Cloud SDK to use features in this release. 

**FEATURE:**

  * Airflow 1.10.9 is now supported. 
  * Environment upgrades have been enabled for the latest two Composer versions (1.11.0 and 1.10.6). 
  * Added a retry feature to the Airflow CeleryExecutor (disabled by default). You can configure the number of times Celery will attempt to execute a task by setting the ` [celery] max_command_attempts ` property. The delay between each retry can also be adjusted with ` [celery] command_retry_wait_duration ` (default: 5 seconds). 

**FIXED:**

  * New PyPi packages have been added for Composer version ` composer-1.11.0-airflow-1.10.6 ` . These make it possible to install ` apache-airflow-backport-providers-google ` with no additional package upgrades. 
  * The PyPi package ` google-cloud-datacatalog ` can now be installed on Composer environments running Airflow 1.10.6 and Python 3. 
  * Fixed synchronization of environment variables to the web server. 
  * Improved error reporting when PyPI package installation fails. 

**DEPRECATED:**

  * Composer versions 1.6.1, 1.7.0, and 1.7.1 are now deprecated. 

**Compute Engine**

**FEATURE:**

  * NVIDIA® Tesla® T4 GPUs are now available in the following additional regions and zones: 

    * Ashburn, Northern Virginia, USA: ` us-east4-b `

For information about using T4 GPUs on Compute Engine, see [ GPUs on Compute
Engine ](https://cloud.google.com/compute/docs/gpus/) .

**FEATURE:**

N2 machines are now available in Northern Virginia ` us-east4-c ` . Read more
information on the [ VM instance pricing
](https://cloud.google.com/compute/vm-instance-pricing#n2_machine_types) page.

**Dataproc**

**FEATURE:**

Terminals started in Jupyter and JupyterLab now use login shells. The
terminals behave as if you SSH'd into the cluster as ` root ` .

**CHANGED:**

Upgraded the ` jupyter-gcs-contents-manager ` package to the latest version.
This upgrade includes a bug fix to a 404 (NOT FOUND) error message that was
issued in response to an attempt to create a file in the virtual top-level
directory instead of the expected 403 (PERMISSION DENIED) error message.

**CHANGED:**

New [ sub-minor versions
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions#supported_dataproc_versions) of Dataproc images: 1.3.64-debian10,
1.3.64-ubuntu18, 1.4.35-debian10, 1.4.35-ubuntu18, 1.5.10-debian10,
1.5.10-ubuntu18, 2.0.0-RC6-debian10, and 2.0.0-RC6-ubuntu18.

**FIXED:**

Fixed a bug in which the HDFS DataNode daemon was enabled on secondary workers
but not started (except on VM reboot if started automatically by ` systemd `
).

**FIXED:**

Fixed a bug in which ` StartLimitIntervalSec=0 ` appeared in the Service
section instead of the Unit section for ` systemd ` services, which disabled
rate limiting for retries when ` systemd ` restarted a service.

##  July 23, 2020

**Anthos**

**FEATURE:**

[ Anthos ](https://cloud.google.com/anthos) 1.4.1 is now available.

**Updated components:**

  * [ Anthos GKE on-prem release notes ](https://cloud.google.com/anthos/gke/docs/on-prem/release-notes)
  * [ Anthos Config Management release notes ](https://cloud.google.com/anthos-config-management/docs/release-notes)

**Anthos Config Management**

**FEATURE:**

[ Config Connector ](https://cloud.google.com/config-connector) has been
updated in Anthos Config Management to version 1.13.1.

**FEATURE:**

Anthos Config Management now includes Hierarchy Controller as a beta feature.
For more information on this component, see the [ Hierarchy Controller
overview ](https://cloud.google.com/anthos-config-
management/docs/concepts/hierarchy-controller) .

**CHANGED:**

Policy Controller users may now enable [ \--log-denies
](https://github.com/open-policy-agent/gatekeeper/blob/master/README.md#log-
denies) to log all denies and dryrun failures. This is useful when trying to
see what is being denied or fails dry-run and for keeping a log to debug
cluster problems without looking through the status of all constraints. This
is configured by setting ` spec.policyController.logDeniesEnabled: true ` in
the configuration file for the Operator. There is an example in the section on
[ Installing Policy Controller ](https://cloud.google.com/anthos-config-
management/docs/how-to/installing-policy-controller) .

**CHANGED:**

This release includes several logging and performance improvements.

**CHANGED:**

This release includes several fixes and improvements for the ` nomos ` command
line utility.

**CHANGED:**

The use of unsecured HTTP for GitHub repo connections or in an http_proxy is
now discouraged, and support for unsecured HTTP will be removed in a future
release. HTTPS will continue to be supported for GitHub repo and local proxy
connections.

**CHANGED:**

This release improves the handling of GitHub repositories with very large
histories.

**CHANGED:**

Prior to this release, Config Sync and ` kubectl ` controllers and processes
used the same annotation ( ` kubectl.kubernetes.io/last-applied-configuration
` ) to calculate three-way merge patches. The shared annotation sometimes
resulted in resource fights, causing unnecessary removal of each other's
fields. Config Sync now uses its own annotation, which prevents resource
clashes.

In most cases, this change will be transparent to you. However, there are two
cases where some previously unspecified behavior will change.

The first case is when you have run ` kubectl apply ` on an unmanaged resource
in a cluster, and you later add that same resource to the GitHub repo.
Previously, Config Sync would have pruned any fields that were previously
applied but not declared in the GitHub repo. Now, Config Sync writes the
declared fields to the resource and leaves undeclared fields in place. If you
want to remove those fields, do one of the following:

  * Get a local copy of the resource from GitHub and ` kubectl apply ` it. 
  * Use ` kubectl edit --save-config ` to remove the fields directly. 

The second case is when you stop managing a resource on the cluster or even
stop all of Config Sync on a cluster. In this case, if you want to prune
fields from a previously managed resource, you will see different behavior.
Previously, you could get a local copy of the resource from GitHub, remove the
unwanted fields, and ` kubectl apply ` it. Now, ` kubectl apply ` no longer
prunes the missing fields. If you want to remove those fields, do one of the
following:

  * Call ` kubectl apply set-last-applied ` with the unmodified resource from GitHub, then remove unwanted fields and ` kubectl apply ` it again without the ` set-last-applied ` flag. 
  * Use ` kubectl edit --save-config ` to remove the fields directly. 

**FIXED:**

In error messages, links to error docs are now more concise.

**Anthos GKE on-prem**

**FEATURE:**

Anthos GKE on-prem 1.4.1-gke.1 is now available. To upgrade, see [ Upgrading
GKE on-prem ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/upgrading) . GKE on-prem 1.4.1-gke.1 clusters run on Kubernetes
1.16.9-gke.14.

**FEATURE:**

**Anthos Identity Service LDAP authentication is now available in Alpha for
GKE on-prem**

Contact support if you are interested in a trial of the LDAP authentication
feature in GKE on-prem.

**FEATURE:**

**Support for F5 BIG-IP load balancer credentials update**

This preview release enables customers to manage and update the F5 BIG-IP load
balancer credentials by using the ` gkectl update credentials f5bigip `
command.

**CHANGED:**

**Functionality changes:**

  * The Ubuntu image is upgraded to include the newest packages. 
  * Preflight checks are updated to validate that the ` gkectl ` version matches the target cluster version for cluster creation and upgrade. 
  * Preflight checks are updated to validate the Window OS version used for running ` gkeadm ` . The ` gkeadm ` command-line tool is only available for Linux, Windows 10, and Windows Server 2019. 
  * ` gkeadm ` is updated to populate ` network.vCenter.networkName ` in both [ admin cluster ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/admin-cluster-configuration-file) and [ user cluster ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/user-cluster-configuration-file) configuration files. 

**FIXED:**

**Fixes:**

  * Removed the static IP used by admin workstation after upgrade from ` ~/.ssh/known_hosts ` to avoid manual workaround. 
  * Resolved a known issue that ` network.vCenter.networkName ` is not populated in the user cluster configuration file during user cluster creation. 
  * Resolved a user cluster upgrade–related issue to only wait for the machines and pods in the same namespace within the cluster to be ready to complete the cluster upgrade. 
  * Updated the default value for ` ingressHTTPNodePort ` and ` ingressHTTPSNodePort ` in the ` loadBalancer.manualLB ` section of the [ admin cluster configuration ](https://cloud.google.com/anthos/gke/docs/on-prem/how-to/admin-cluster-configuration-file) file. 
  * Fixed [ CVE-2020-8558 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8558) and [ CVE-2020-8559 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8559) described in [ Security bulletins ](https://cloud.google.com/anthos/gke/docs/on-prem/security-bulletins#gcp-2020-009) . 
  * Logging and monitoring: Resolved an issue that stackdriver-log-forwarder was not scheduled on the master node on the admin cluster. 
  * Resolved the following known issues published in the 1.4.0 release notes: 
    * If a user cluster is created without any node pool named the same as the cluster, managing the node pools using ` gkectl update cluster ` would fail. To avoid this issue, when creating a user cluster, you need to name one node pool the same as the cluster. 
    * The ` gkectl ` command might exit with panic when converting config from "/path/to/config.yaml" to v1 config files. When that occurs, you can resolve the issue by removing the unused bundled load balancer section ("loadbalancerconfig") in the config file. 
    * When using gkeadm to upgrade an admin workstation on Windows, the info file filled out from this template needs to have the line endings converted to use Unix line endings (LF) instead of Windows line endings (CRLF). You can use Notepad++ to convert the line endings. 
    * When running a preflight check for ` config.yaml ` that contains both ` admincluster ` and ` usercluster ` sections, the "data disk" check in the "user cluster vCenter" category might fail with the message: ` [FAILURE] Data Disk: Data disk is not in a folder. Use a data disk in a folder when using vSAN datastore. ` User clusters don't use data disks, and it's safe to ignore the failure. 
    * When upgrading the admin cluster, the preflight check for the user cluster OS image validation will fail. The user cluster OS image is not used in this case, and it's safe to ignore the "User Cluster OS Image Exists" failure in this case. 
    * User cluster creation and upgrade might be stuck with the error: ` Failed to update machine status: no matches for kind "Machine" in version "cluster.k8s.io/v1alpha1". ` To resolve this, you need to delete the clusterapi pod in the user cluster namespace in the admin cluster. 

**ISSUE:**

**Known issues:**

  * During reboots, the data disk is not remounted on the admin workstation when using GKE on-prem 1.4.0 or 1.4.1 because the startup script is not run after the initial creation. To resolve this, you can run ` sudo mount /dev/sdb1 /home/ubuntu ` . 

**Cloud Billing**

**FEATURE:**

**Export your Cloud Billing account SKU prices to BigQuery.** You can now
export your pricing information for Google Cloud and Google Maps Platform SKUs
to BigQuery. Exporting your pricing data allows you to audit, analyze, and/or
join your pricing data with your exported cost data. The pricing export
includes list prices, pricing tiers, and, when applicable, any promotional or
negotiated pricing. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/export-data-bigquery) for more
details.

**Dialogflow**

**DEPRECATED:**

Amazon Alexa importer and exporter are no longer supported.

**Network Intelligence Center**

**FEATURE:**

Network Topology includes two new metrics for connections between entities:
packet loss and latency. Additionally, you can now use a drop-down menu to
select which metric Network Topology overlays on traffic paths. For more
information, see [ Viewing metrics for traffic between entities
](https://cloud.google.com/network-intelligence-center/docs/network-
topology/how-to/using-network-
topology#viewing_metrics_for_traffic_between_entities) and [ Network Topology
metrics reference ](https://cloud.google.com/network-intelligence-
center/docs/network-topology/reference/metrics-reference) .

**Virtual Private Cloud**

**FEATURE:**

[ Serverless VPC Access ](https://cloud.google.com/vpc/docs/configure-
serverless-vpc-access) support for [ Shared VPC
](https://cloud.google.com/vpc/docs/shared-vpc) is now available in **Beta** .

##  July 22, 2020

**Anthos Service Mesh**

**FEATURE:**

**1.6.5-asm.7, 1.5.8-asm.7, and 1.4.10-asm.15 are now available**

This release provides these features and fixes:

  * Builds Istiod (Pilot), Citadel Agent, Pilot Agent, Galley, and Sidecar Injector with [ Go+BoringCrypto ](https://go.googlesource.com/go/+/refs/heads/dev.boringcrypto) . 
  * Builds Istio Proxy (Envoy) with the [ \--define boringssl=fips ](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/security/ssl#fips-140-2) option. 
  * Ensures the components listed above use FIPS-compliant algorithms. 

**Cloud Bigtable**

**FEATURE:**

Cloud Bigtable's fully integrated [ backups feature
](https://cloud.google.com/bigtable/docs/backups) is now generally available.
Backups let you save a copy of a table's schema and data and restore the
backup to a new table at a later time.

##  July 21, 2020

**AutoML Video Intelligence Object Tracking**

**CHANGED:**

In April 2020, a model upgrade for the AutoML Video Object Tracking feature
was released. This release is for non-downloadable models only. Models trained
after April 2020 may show improvements in the evaluation results.

**Cloud Run**

**FEATURE:**

Cloud Run resources are now available in [ Cloud Asset Inventory
](https://cloud.google.com/asset-inventory/docs/overview)

**Compute Engine**

**FEATURE:**

You can now create _balanced persistent disks_ , in addition to standard and
SSD persistent disks. Balanced persistent disks are an alternative to SSD
persistent disks that balance performance and cost. For more information, see
[ Persistent disk types
](https://cloud.google.com/compute/docs/disks/index#disk-types) .

**Config Connector**

**FIXED:**

bug fixes and performance improvements

**Istio on Google Kubernetes Engine**

**FIXED:**

**Istio 1.4.10-gke.4**

Fixes known security issues with the same fixes as [ OSS Istio 1.4.10
](https://istio.io/news/releases/1.4.x/announcing-1.4.10/)

**Recommendations AI**

**FEATURE:**

**Recommendations AI public beta**

Recommendations AI is now in public beta.

**CHANGED:**

**New pricing available**

Pricing for Recommendations AI has been updated for public beta. For new
pricing and free trial details, see [ Pricing
](https://cloud.google.com/recommendations-ai/pricing) .

**FEATURE:**

**UI redesign**

The [ Recommendations AI console
](https://console.cloud.google.com/recommendation/catalogs/default_catalog/dashboard)
has a new look. You'll see a new layout, including a redesigned dashboard and
improved [ alerts setup ](https://cloud.google.com/recommendations-
ai/docs/monitor) .

**FEATURE:**

**New support resources**

We have new support resources available:

  * File bugs and feature requests on our [ public issue tracker ](https://issuetracker.google.com/issues/new?component=911831) . 
  * Ask a question about Recommendations AI [ on Stack Overflow ](http://stackoverflow.com/questions/tagged/google-cloud-recommendations) , using the tag ` google-cloud-recommendations ` . 
  * Join the [ cloud-recommendations-users ](https://groups.google.com/forum/#!forum/cloud-recommendations-users) Google group to discuss Recommendations AI and receive announcements and updates. 

See [ Getting support ](https://cloud.google.com/recommendations-
ai/docs/getting-support) for all support resources.

**FEATURE:**

**New FAQ page**

A Frequently Asked Questions page is now available. [ See the FAQ here
](https://cloud.google.com/recommendations-ai/docs/faq) .

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

**Resource Manager**

**FEATURE:**

The Organization Policy for [ enabling detailed Cloud Audit Logs
](https://cloud.google.com/storage/docs/org-policy-constraints#audit-logging)
has launched into general availability.

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

**Resource Manager**

**FEATURE:**

The Organization Policy for [ restricting protocol forwarding creation
](https://cloud.google.com/compute/docs/protocol-
forwarding#enforcing_protocol_forwarding_settings_across_a_project_folder_or_organization)
has launched into public beta.

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

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M51 release**

` sudo ` access removed from Deep Learning Containers.

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

