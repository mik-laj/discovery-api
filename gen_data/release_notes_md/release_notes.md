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
**Beta** .

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

##  May 19, 2020

**Cloud Debugger**

**FEATURE:**

Cloud Debugger now lets you canary snapshots and logpoints on your Java
applications. To learn more, see the [ Java page for setting up Cloud Debugger
](https://cloud.google.com/debugger/docs/setup/java) .

**Cloud Monitoring**

**CHANGED:**

Alert notifications delivered by email now come from "alerting-
noreply@google.com" instead of "alerts@stackdriver.com".

**Compute Engine**

**FEATURE:**

Troubleshoot VMs by [ capturing screenshots
](https://cloud.google.com/compute/docs/instances/capturing-vm-screenshots) .
This is in **beta** .

**Config Connector**

**FIXED:**

Bug fixes and reliability improvements

**FIXED:**

Improving handling of scenarios when ` version ` field on ` ContainerNodePool
` is updated externally

**Filestore**

**FEATURE:**

Learn how to create [ low disk space alerts
](https://cloud.google.com/filestore/docs/monitoring-instances) for your
Filestore instances.

##  May 18, 2020

**AI Platform Deep Learning VM Image**

**FEATURE:**

TensorFlow 2.2 images have been added. The new TensorFlow 2.2 image families
are ` tf2-2-2-cpu ` and ` tf2-2-2-cu101 ` . See the [ available image families
](https://cloud.google.com/ai-platform/deep-learning-vm/docs/images) .

**Cloud Bigtable**

**CHANGED:**

The [ Cloud Bigtable Monitoring
](https://cloud.google.com/bigtable/docs/monitoring-instance) page in the
Cloud Console has been redesigned. Changes to the visual experience include
the following:

  * Views that are now split into separate tabs 
  * A new time range picker 
  * Updated styling on the graphs 

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

**Game Servers**

**CHANGED:**

Added support in the Google Cloud Console for managing game server [ configs
](https://cloud.google.com/game-servers/docs/how-to/creating-config) , [
deployments ](https://cloud.google.com/game-servers/docs/how-to/creating-
deployment) , and [ rollouts ](https://cloud.google.com/game-servers/docs/how-
to/updating-rollout) . You can now create, view, update, and delete game
server configs, deployments, and rollouts from the Cloud Console.

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

**App Engine flexible environment .NET**

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/flexible/dotnet/labeling-resources)
.

**App Engine flexible environment Go**

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/flexible/go/labeling-resources) .

**App Engine flexible environment Java**

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/flexible/java/labeling-resources) .

**App Engine flexible environment Node.js**

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/flexible/nodejs/labeling-resources)
.

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

**App Engine standard environment Go**

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/standard/go/labeling-resources) .

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/standard/go111/labeling-resources) .

**App Engine standard environment Java**

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/standard/java/labeling-resources) .

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/standard/java11/labeling-resources)
.

**App Engine standard environment Node.js**

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/standard/nodejs/labeling-resources)
.

**App Engine standard environment PHP**

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/standard/php/labeling-resources) .

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/standard/php7/labeling-resources) .

**App Engine standard environment Python**

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/standard/python/labeling-resources)
.

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/standard/python3/labeling-resources)
.

**App Engine standard environment Ruby**

**FEATURE:**

To get a fine-grained view of billing data for each resource used by your App
Engine services, you can apply labels to the services, export your billing
data to BigQuery, and run queries. For more information, see [ Labeling App
Engine resources
](https://cloud.google.com/appengine/docs/standard/ruby/labeling-resources) .

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

