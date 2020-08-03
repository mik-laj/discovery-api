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

##  July 31, 2020

**BigQuery**

**CHANGED:**

Updated version of [ Magnitude Simba ODBC
](https://cloud.google.com/bigquery/providers/simba-drivers) driver includes
performance improvements and bug fixes.

**Cloud Functions**

**FEATURE:**

Cloud Functions is now available in the following regions:

  * ` asia-south1 ` (Mumbai) 
  * ` asia-southeast2 ` (Jakarta) 
  * ` asia-northeast3 ` (Seoul) 

See [ Cloud Functions Locations
](https://cloud.google.com/functions/docs/locations) for details.

**Compute Engine**

**FEATURE:**

N2D machine types are now available in ` asia-east1 ` in all three zones. For
more information, see the [ VM instance pricing
](https://cloud.google.com/compute/vm-instance-pricing#n2d_machine_types)
page.

**Dataproc**

**FEATURE:**

**Enabled[ Kerberos
](https://cloud.google.com/dataproc/docs/concepts/configuring-
clusters/security) automatic-configuration feature. ** When creating a
cluster, users can enable Kerberos by setting the `
dataproc:kerberos.beta.automatic-config.enable ` [ cluster property
](https://cloud.google.com/dataproc/docs/concepts/configuring-
clusters/cluster-properties#service_properties) to ` true ` . When using this
feature, users do not need to specify the Kerberos root principal password
with the ` --kerberos-root-principal-password ` and ` --kerberos-kms-key-uri `
flags.

**CHANGED:**

New [ sub-minor versions
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions#supported_dataproc_versions) of Dataproc images: 1.3.65-debian10,
1.3.65-ubuntu18, 1.4.36-debian10, 1.4.36-ubuntu18, 1.5.11-debian10,
1.5.11-ubuntu18, 2.0.0-RC7-debian10, and 2.0.0-RC7-ubuntu18.

**CHANGED:**

1.3+ images (includes Preview image):

  * [ HADOOP-16984 ](https://issues.apache.org/jira/browse/HADOOP-16984) : Added support to read history files only from the done directory. 

  * [ MAPREDUCE-7279 ](https://issues.apache.org/jira/browse/MAPREDUCE-7279) : Display the Resource Manager name on the HistoryServer web page. 

  * [ SPARK-32135 ](https://issues.apache.org/jira/browse/SPARK-32135) : Show the Spark driver name on the Spark history web page. 

  * [ SPARK-32097 ](https://issues.apache.org/jira/browse/SPARK-32097) : Allow reading Spark history log files via the Spark history server from multiple directories. 

**CHANGED:**

Images 1.3 - 1.5:

  * [ HIVE-20600 ](https://issues.apache.org/jira/browse/HIVE-20600) : Fixed Hive Metastore connection leak. 

**CHANGED:**

Images 1.5 - 2.0 preview:

  * Upgraded the [ Cloud Storage connector ](https://cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage) to version 2.1.4 (see the GitHub [ change notes ](https://github.com/GoogleCloudDataproc/hadoop-connectors/releases/tag/v2.1.4) ). 

**FIXED:**

Fixed an issue where optional components that depend on HDFS failed on single
node clusters.

**FIXED:**

Fixed an issue that caused workflows to be stuck in the RUNNING state when
managed clusters (created by the workflow) were deleted while the workflow was
running.

**Identity and Access Management**

**CHANGED:**

We are delaying the upcoming changes for [ deleted members that are bound to a
role ](https://cloud.google.com/iam/docs/release-notes#July_01_2020) . These
changes will take effect starting on September 14, 2020.

**Storage Transfer Service**

**FEATURE:**

Transfers from Microsoft Azure Blob Storage are now generally available.

##  July 30, 2020

**Anthos**

**FEATURE:**

[ Anthos ](https://cloud.google.com/anthos) 1.3.3 is now available.

**Updated components:**

  * [ Anthos GKE on-prem release notes ](https://cloud.google.com/anthos/gke/docs/on-prem/release-notes)

**Anthos GKE on-prem**

**FEATURE:**

Anthos GKE on-prem 1.3.3-gke.0 is now available. To upgrade, see [ Upgrading
GKE on-prem ](https://cloud.google.com/anthos/gke/docs/on-prem/how-
to/upgrading) . GKE on-prem 1.3.3-gke.0 clusters run on Kubernetes
1.15.12-gke.9.

**FIXED:**

**Fixes:**

  * Fixed [ CVE-2020-8559 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8559) described in [ Security bulletins ](https://cloud.google.com/anthos/gke/docs/on-prem/security-bulletins#gcp-2020-009) . 
  * Updated the git-sync image to fix security vulnerability [ CVE-2019-5482 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5482) . 
  * Updated the kindest/node image to fix security vulnerability [ CVE-2020-13777 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-13777) . 

**Cloud Logging**

**CHANGED:**

The Logs field explorer panel is now generally available (GA). To learn more,
see the [ Logs field explorer section on Logs Viewer (Preview) interface page
](https://cloud.google.com/logging/docs/view/logs-viewer-interface#logs-field-
panel) .

**Cloud Run**

**FEATURE:**

You can now tag Cloud Run revisions. Tagged revisions get a dedicated URL
allowing developers to reach these specific revisions without needing to
allocate traffic to it.

**Cloud Spanner**

**FEATURE:**

The Cloud Spanner emulator is now [ generally available
](https://cloud.google.com/products/#product-launch-stages) , enabling you to
develop and test applications locally. For more information, see [ Using the
Cloud Spanner Emulator ](https://cloud.google.com/spanner/docs/emulator) .

**Compute Engine**

**FEATURE:**

When creating patch jobs, you can now choose whether to deploy zones
concurrently or one at a time. You can also now specify a disruption budget
for your VMs. For more information, see [ Patch rollout options
](https://cloud.google.com/compute/docs/os-patch-management/create-patch-
job#rollout-options) .

**FEATURE:**

N2 machines are now available in Sao Paulo ` southamerica-southeast1 ` in all
three zones. For more information, see [ VM instance pricing
](https://cloud.google.com/compute/vm-instance-pricing#n2_machine_types) .

**FEATURE:**

You can access ` m2-megamem ` memory-optimized machine types in all zones that
already have ` m2-ultramem ` memory-optimized machine types. These two machine
types have also been added to ` asia-south1-b ` . You can use ` m1-ultramem `
machine types in ` asia-south1-a ` . To learn more, read [ Memory-optimized
machine type family ](https://cloud.google.com/compute/vm-instance-
pricing#memory-optimized) .

**Dialogflow**

**FEATURE:**

GA (general availability) launch of [ mega agents
](https://cloud.google.com/dialogflow/docs/agents-mega) .

**FEATURE:**

Beta launch of the [ Facebook Workplace integration
](https://cloud.google.com/dialogflow/docs/integrations/workplace) .

**Network Intelligence Center**

**DEPRECATED:**

Network Topology no longer supports [ infrastructure segments
](https://cloud.google.com/network-intelligence-center/docs/network-
topology/how-to/using-network-topology#defining-infra-segment) . This feature
is deprecated and will be completely removed after 90 days. If you have any
questions, see [ Getting support ](https://cloud.google.com/network-
intelligence-center/docs/network-topology/support/getting-support) .

##  July 28, 2020

**Compute Engine**

**CHANGED:**

Improved validation checks will be introduced on API calls to `
compute.googleapis.com ` starting on August 3, 2020 to increase reliability
and REST API compliance of the Compute Engine platform for all users. Learn
how to [ Validate API Requests
](https://cloud.google.com/compute/docs/api/how-tos/api-requests-
responses#validating_api_requests) to ensure your requests are properly
formed.

**Memorystore for Redis**

**FEATURE:**

Support for [ VPC Service Controls on Memorystore for Redis
](https://cloud.google.com/memorystore/docs/redis/using-vpc-service-controls)
is now Generally Available.

**Migrate for Anthos**

**DEPRECATED:**

The ` migctl migration cleanup ` command has been removed and is no longer
necessary.

**DEPRECATED:**

In previous releases, you used a command in the form: ` migctl source create
ce my-ce-src --project my-project --zone zone ` to create a migration for
Compute Engine. The ` --zone ` option has been removed when creating a Compute
Engine migration. Using the ` --zone ` option in this release causes an error.

**DEPRECATED:**

The ` migctl migration logs ` command has been removed. You now use the Google
Console to view logs.

**FEATURE:**

Added the new ` --json-key sa.json ` option to the ` migctl source create ce `
command to create a migration for Compute Engine, where ` sa.json ` specifies
a service account. See [ Optionally creating a service account when using
Compute Engine as a migration source ](/release-notes/config-dev-
env#optionally_creating_a_service_account_when_using_as_a_migration_source)
for more.

**FEATURE:**

To edit the migration plan, you must now use the ` migctl migration get my-
migration ` command to download the plan. After you are done editing the plan,
you have to upload it by using the ` migctl migration update my-migration `
command. See [ Customizing a migration plan ](/release-notes/customizing-a-
migration-plan) for more.

**FEATURE:**

Added support for Anthos GKE on-prem clusters running on VMware. On-prem
support lets you migrate source VM workloads in a vCenter/vSphere environment
to a GKE on-prem cluster running in the same vCenter/vSphere environment. See
[ Migration prerequisites ](/release-notes/migration-prerequisites) for the
requirements for on-prem migration.

**FEATURE:**

The Google Cloud Console provides a web-based, graphical user interface that
you can use to manage your Google Cloud Console projects and resources.
Migrate for Anthos now supports the migration of workloads by using the Google
Cloud Console.

In this release, the Migrate for Anthos on the Cloud Consoledoes not support
migrations for Windows or for on-prem, including monitoring Windows or on-prem
migrations.

**FEATURE:**

Migrate for Anthos now includes [ Custom Resource Definitions (CRDs)
](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-
resources/) that enable you to easily create and manage migrations using an
API. For example, you can use these CRDs to build your own automated tools.

**FEATURE:**

Added the ` node-selectors ` and ` tolerations ` options to the ` migctl setup
install ` installation command that lets you install Migrate for Anthos on a
specific set of nodes or node pools in a cluster. See [ Installing Migrate for
Anthos ](https://cloud.google.com/migrate/anthos/docs/installing-migrate-
components) .

**FEATURE:**

You can use Migrate for Anthos to migrate Windows VMs to workloads on GKE.
This process clones your Compute Engine VM disks and uses the clone to
generate artifacts (including a Dockerfile and a zip archive with extracted
workload files and settings) you can use to build a deployable GKE image. See
[ Adding a Windows migration source ](/release-notes/windows/migrating-win-vm-
overview) .

**ISSUE:**

**160309992:** Editing a migration plan from the GUI console might fail if it
was also edited using ` migctl ` .

**ISSUE:**

**161135630:** Attempting multiple migrations of the same remote VM (from
VMware, AWS or Azure) simultaneously, might result in a stuck migration
process.

**Workaround:** Delete the stuck migration.

**ISSUE:**

**161214397:** For Anthos on-prem, in case of a missing service-account to
upload container images to the Container Registry, the migration might get
stuck.

**Workaround:** Add the service-account. If you are using the Migrate for
Anthos CRD API, delete the GenerateArtifactsTask and recreate it. If using the
` migctl ` CLI tool, delete the migration and recreate it. You can first
download the migration YAML using ` migctl migration get ` to back up any
customizations you have made.

**ISSUE:**

**161110816:** ` migctl migration create ` with a source that doesn't exist
fails with a non-informative error message: ` request was denied ` .

**ISSUE:**

**161104564:** Creating a Linux migration with wrong ` os-type ` specification
causes the migration process to get stuck until deleted.

**ISSUE:**

**160858543, 160836394, 160844377, 154430477, 154403665, 153241390, 153239696,
152408818, 151516642, 132002453:** Unstable network in Migrate for Anthos
infrastructure, or a GKE node restart, might cause migration to get stuck.

**Workaround:** Delete the migration and re-create it. If recreating the
migration does not solve the issue, please contact [ support
](https://cloud.google.com/support-hub#migrate-for-compute-engine-formerly-
velostrata) .

**ISSUE:**

**161787358:** In some cases, upgrading from version v1.3 to v1.4 might fail
with ` Failed to convert source ` message.

**Workaround:** Re-run the upgrade command.

**ISSUE:**

**153811691, 153439420:** Migrate for Anthos support for older Java does not
handle OpenJDK 7 and 8 CPU resource calculations.

**ISSUE:**

**152974631:** Using GKE nodes with CPU and Memory configurations below the
recommended values might cause migrations to get stuck.

**FIXED:**

**GKE on-prem preview:** If a source was created with ` migctl source create `
using the wrong credentials, you could not delete the migration with ` migctl
migration delete ` . This issue has been fixed in the GA release of on-prem
support.

**DEPRECATED:**

In version 1.4, by default Migrate for Anthos installs to and performs
migrations in the ` v2k-system ` namespace. In previous release, you could
specify the namespace. The option to specify a namespace has been removed.

**ISSUE:**

**157890913, 160082702, 161125635, 159693579** : A migration might continue to
indicate that it is running, while an issue encountered prevents further
processing.

**Workaround** : Check event messages on the migration object using the
verbose ` migctl ` status command: ` migclt migration status migration_name -v
` . You might be able to correct the issue to allow the migration to continue
or the migration should be deleted and recreated if an Error event is listed
without further retries.

An example is when creating a Windows migration on a cluster with no Windows
nodes. In this case the event message will show: ` Warning FailedScheduling
10s Pod discover-xyz 0/1 nodes are available: 1 node(s) didn't match node
selector. `

**VPC Service Controls**

**FEATURE:**

General availability for the following integration:

  * [ Memorystore for Redis ](https://cloud.google.com/memorystore/docs/redis)

##  July 27, 2020

**BigQuery**

**FEATURE:**

` INFORMATION_SCHEMA ` views for [ streaming metadata
](https://cloud.google.com/bigquery/docs/information-schema-streaming) are now
in [ alpha ](https://cloud.google.com/products/?hl=EN#product-launch-stages) .
You can use these views to retrieve historical and real-time information about
streaming data into BigQuery.

**Cloud Run**

**FEATURE:**

Cloud Run is now available in ` asia-southeast1 ` (Singapore)

**Dataflow**

**FEATURE:**

Dataflow now [ supports
](https://cloud.google.com/dataflow/pricing#pricing_details) Dataflow Shuffle,
Streaming Engine, FlexRS, and the following [ regional endpoints
](https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) in GA:

  * ` northamerica-northeast1 ` (Montréal) 
  * ` asia-southeast1 ` (Singapore) 
  * ` australia-southeast1 ` (Sydney) 

**Dialogflow**

**FEATURE:**

Beta launch of [ Dialogflow Messenger
](https://cloud.google.com/dialogflow/docs/integrations/dialogflow-messenger)
. This new integration provides a customizable chat dialog for your agent that
can be embedded in your website.

**Security Command Center**

**DEPRECATED:**

Security Command Center v1beta1 API will be disabled on Jan. 31, 2021. All
users will be required to migrate to Security Command Center v1 API, which is
now in general availability.

  * Update to Google-provided v1 API [ client libraries ](https://cloud.google.com/apis/docs/client-libraries-explained) . 
  * Move your client libraries and [ HTTP/grpc calls ](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) to v1 by following instructions in the reference documentation for [ service endpoints ](https://cloud.google.com/security-command-center/docs/reference/rest#service-endpoint_2) and [ SDK configuration ](https://cloud.google.com/security-command-center/docs/how-to-programmatic-access) . 
  * If you call this service using your own libraries, follow the guidance in our [ Security Command Center API Overview ](https://cloud.google.com/security-command-center/docs/reference/rest#service:-securitycenter.googleapis.com_2) when making API requests. 
  * To use ` ListFindings ` calls in the v1 API, update your response handling to respond to an extra layer of object nesting, as shown below: 
    * v1beta1: ` response.getFindings().forEach( x -> ....) `
    * v1: ` response.getListFindingsResults().forEach(x -> { x.getFinding(); .... }) `

Additional changes to the v1 API are listed below. Learn more about [ Using
the Security Command Center API ](https://cloud.google.com/security-command-
center/docs/how-to#using-the-security-command-center-api) .

**BREAKING:**

The ` SeverityLevel ` finding source property for all Security Health
Analytics findings will be removed and replaced with a field named ` Severity
` , which retains the same values. * **Impact:** Finding notification filters,
post-processing, and alerting based on the ` SeverityLevel ` finding source
property will no longer be possible. * **Recommendation:** Replace the `
SeverityLevel ` finding source property with the ` Severity ` finding
attribute property to retain existing functionality.

**BREAKING:**

The ` nodePools ` finding source property will be removed from the `
OVER_PRIVILEGED_SCOPES ` findings and replaced with a source property named `
VulnerableNodePools ` . * **Impact:** Finding notification filters, post-
processing and alerting based on this finding source property may fail. *
**Recommendation:** Modify workflows as necessary to utilize the new `
VulnerableNodePools ` source property.

**BREAKING:**

The finding category of ` 2SV_NOT_ENFORCED ` is being renamed `
MFA_NOT_ENFORCED ` . * **Impact:** Case-sensitive finding notification
filters, post-processing, and alerting based on the previous finding category
name may fail. * **Recommendation:** Update any post-processing to use the new
category name.

**BREAKING:**

The ` ExceptionInstructions ` source property will be removed from all
Security Health Analytics findings. * **Impact:** Finding notification
filters, post-processing, and alerting based on the finding source property
may fail. * **In progress:** A new property that will indicate the current
state of findings is being developed.

**BREAKING:**

The ` ProjectId ` source property from all Security Health Analytics findings
will be removed. * **Impact:** Finding notification filters, post-processing,
and alerting based on the finding source property may fail. *
**Recommendation:** Update workflows to utilize the project id in the `
resource.project_display_name ` field of a ` ListFindingsResult ` .

**BREAKING:**

The ` AssetSettings ` finding source property from ` PUBLIC_SQL_INSTANCE ` , `
SQL_PUBLIC_IP ` , ` SSL_NOT_ENFORCED ` , ` AUTO_BACKUP_DISABLED ` , `
SQL_NO_ROOT_PASSWORD ` , ` SQL_WEAK_ROOT_PASSWORD ` finding types will be
removed, as it contains data duplicated from the asset entity. * **Impact:**
Finding notification filters, post-processing, and alerting based on the
finding source property will fail. * **Recommendation:** Replacing the `
AssetSettings ` finding source property with the ` Settings ` resource
property from the asset underlying the finding will retain existing
functionality.

**BREAKING:**

The ` Allowed ` finding source property from ` OPEN_FIREWALL ` findings will
be replaced with changed a new field named `
ExternallyAccessibleProtocolsAndPorts ` , which will contain a subset of the
values from the ` Allowed ` property. * **Impact:** Finding notification
filters, post-processing, and alerting based on the finding source property
will fail. * **Recommendation:** Modify your workflows as necessary to utilize
the new ` ExternallyAccessibleProtocolsAndPorts ` source property.

**BREAKING:**

The ` SourceRanges ` finding source property from findings in OPEN_FIREWALL
findings will be replaced with a new ` ExternalSourceRanges ` , which will
contain a subset of the values from the ` SourceRanges ` property. *
**Impact:** Finding notification filters, post-processing and alerting based
on the finding source property will fail. * **Recommendation:** Modify your
workflows as necessary to utilize the new ` ExternalSourceRanges ` source
property.

**BREAKING:**

As of Jan. 31, 2021, the ` UpdateFinding ` API will no longer support storing
string properties that are longer than 7,000 characters. * **Impact:** Calls
to ` UpdateFinding ` that seek to store string properties longer than 7,000
characters will be rejected with an invalid argument error. *
**Recommendation:** Consider storing string properties longer than 7,000
characters as JSON structs or JSON lists. Learn more about [ writing findings
](https://cloud.google.com/security-command-
center/docs/reference/rest/v1/organizations.sources.findings#Finding) .

**BREAKING:**

As of Sept. 1, 2020, the ` ListFindings ` API will no longer support searching
on finding properties that are longer than 7,000 characters. * **Impact:**
Searches on strings that are longer than 7,000 characters will not return
expected results. For example, if a partial string match filter has a match at
the 7,005th character on a property in a finding, that finding will not be
returned because that match is past the 7,000-character threshold. An
exception will not be returned. * **Recommendation:** Customers can remove
filter restrictions (e.g. x : "some-value") that are supposed to match very
long properties. The results can then be filtered locally to remove findings
whose strings do not match designated criteria. Learn more about [ filtering
findings ](https://cloud.google.com/security-command-center/docs/how-to-api-
list-findings#filtering_findings) .

**CHANGED:**

The ` OffendingIamRoles ` source property in extensions of IAM Scanner
Configurations will use structured data instead of a JSON-formatted string. *
**Impact:** Finding notification filters, post-processing, and alerting based
on the finding source property will need to be updated to take advantage of
the new data type on findings of the following categories: `
ADMIN_SERVICE_ACCOUNT ` , ` NON_ORG_IAM_MEMBER ` , ` PRIMITIVE_ROLES_USED ` ,
` OVER_PRIVILEGED_SERVICE_ACCOUNT_USER ` , ` REDIS_ROLE_USED_ON_ORG ` , `
SERVICE_ACCOUNT_ROLE_SEPARATION ` , ` KMS_ROLE_SEPARATION ` . *
**Recommendation:** Update workflows to utilize the new data type.

**CHANGED:**

The ` QualifiedLogMetricNames ` source property in specific ` Monitoring `
findings from Security Health Analytics will use a list instead of a
character-separated string value. * **Impact:** Finding notification filters,
post-processing and alerting based on the finding source property will need to
be updated to take advantage of the new data type for findings of the
following categories: ` AUDIT_CONFIG_NOT_MONITORED ` , `
BUCKET_IAM_NOT_MONITORED ` , ` CUSTOM_ROLE_NOT_MONITORED ` , `
FIREWALL_NOT_MONITORED ` , ` NETWORK_NOT_MONITORED ` , ` OWNER_NOT_MONITORED `
, ` ROUTE_NOT_MONITORED ` , ` SQL_INSTANCE_NOT_MONITORED ` . *
**Recommendation:** Update workflows to utilize the new data type.

**CHANGED:**

The ` AlertPolicyFailureReasons ` source property in specific ` Monitoring `
findings from Security Health Analytics will use a list instead of a
character-separated string value. * **Impact:** Finding notification filters,
post-processing and alerting based on the finding source property will need to
be updated to take advantage of the new data type for findings of the
following categories: ` AUDIT_CONFIG_NOT_MONITORED ` , `
BUCKET_IAM_NOT_MONITORED ` , ` CUSTOM_ROLE_NOT_MONITORED ` , `
FIREWALL_NOT_MONITORED ` , ` NETWORK_NOT_MONITORED ` , ` OWNER_NOT_MONITORED `
, ` ROUTE_NOT_MONITORED ` , ` SQL_INSTANCE_NOT_MONITORED ` . *
**Recommendation:** Update workflows to utilize the new data type.

**CHANGED:**

The ` CompatibleFeatures ` source property in ` WEAK_SSL_POLICY ` findings
will use a list instead of a character-separated string value. * **Impact:**
Finding notification filters, post-processing, and alerting based on the
finding source property will need to be updated to take advantage of the new
data type for findings. * **Recommendation:** Update workflows to utilize the
new data type.

##  July 25, 2020

**Cloud Load Balancing**

**CHANGED:**

The introductory period during which you could use Internal HTTP(S) Load
Balancing without charge has ended. Starting July 25, 2020, your usage of
Internal HTTP(S) Load Balancing will be [ billed to your project
](https://cloud.google.com/vpc/network-pricing#internal-https-lb) .

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

**App Engine standard environment Go**

**FEATURE:**

[ Serverless VPC Access support for Shared VPC
](https://cloud.google.com/appengine/docs/standard/go/connecting-vpc#shared-
vpc) is now available in Beta.

**App Engine standard environment Java**

**FEATURE:**

[ Serverless VPC Access support for Shared VPC
](https://cloud.google.com/appengine/docs/standard/java/connecting-vpc#shared-
vpc) is now available in Beta.

**FEATURE:**

[ Serverless VPC Access support for Shared VPC
](https://cloud.google.com/appengine/docs/standard/java11/connecting-
vpc#shared-vpc) is now available in Beta.

**App Engine standard environment Node.js**

**FEATURE:**

[ Serverless VPC Access support for Shared VPC
](https://cloud.google.com/appengine/docs/standard/nodejs/connecting-
vpc#shared-vpc) is now available in Beta.

**App Engine standard environment PHP**

**FEATURE:**

[ Serverless VPC Access support for Shared VPC
](https://cloud.google.com/appengine/docs/standard/php7/connecting-vpc#shared-
vpc) is now available in Beta.

**App Engine standard environment Python**

**FEATURE:**

[ Serverless VPC Access support for Shared VPC
](https://cloud.google.com/appengine/docs/standard/python/connecting-
vpc#shared-vpc) is now available in Beta.

**FEATURE:**

[ Serverless VPC Access support for Shared VPC
](https://cloud.google.com/appengine/docs/standard/python3/connecting-
vpc#shared-vpc) is now available in Beta.

**App Engine standard environment Ruby**

**FEATURE:**

[ Serverless VPC Access support for Shared VPC
](https://cloud.google.com/appengine/docs/standard/ruby/connecting-vpc#shared-
vpc) is now available in Beta.

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

**Cloud Functions**

**FEATURE:**

[ Serverless VPC Access support for Shared VPC
](https://cloud.google.com/functions/docs/networking/connecting-vpc#shared-
vpc) is now available in Beta.

**Cloud Run**

**FEATURE:**

[ Serverless VPC Access support for Shared VPC
](https://cloud.google.com/run/docs/configuring/connecting-vpc#shared-vpc) is
now available in Beta.

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

Allow removing ` sudo ` access from Deep Learning Containers.

Debian-10-based images are released. You can create [ Shielded VM instances
](https://cloud.google.com/security/shielded-cloud/shielded-vm) from these
images.

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

