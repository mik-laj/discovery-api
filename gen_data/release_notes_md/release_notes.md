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

##  August 20, 2020

**Anthos**

**FEATURE:**

[ Anthos ](https://cloud.google.com/anthos) 1.4.2 is now available.

**Updated components:**

  * [ Anthos GKE on-prem release notes ](https://cloud.google.com/anthos/gke/docs/on-prem/release-notes)
  * [ Anthos Config Management release notes ](https://cloud.google.com/anthos-config-management/docs/release-notes)

**Anthos Config Management**

**FEATURE:**

Anthos Config Management now includes [ Config Connector
](https://cloud.google.com/config-connector) v1.15.1.

**FEATURE:**

Anthos Policy Controller has been updated to include a more recent build of
OPA Gatekeeper ( [ hash: 1de87b6 ](https://github.com/open-policy-
agent/gatekeeper/commit/1de87b6d3c2ed3609e69b789d722e28285873861) ).

**CHANGED:**

This release includes several logging and performance improvements.

**ISSUE:**

An issue with git submodule support is preventing syncing of configuration
stored in submodule repositories. If this affects you, please [ contact
support ](https://cloud.google.com/support-hub) so we can suggest ways to
handle your required use cases.

**Anthos GKE on-prem**

**FEATURE:**

Anthos GKE on-prem 1.4.2-gke.3 is now available. To upgrade, see [ Upgrading
GKE on-prem ](https://cloud.google.comanthos/gke/docs/on-prem/how-
to/upgrading) . GKE on-prem 1.4.2-gke.3 clusters run on Kubernetes
1.16.11-gke.11.

**FEATURE:**

GPU support (beta solution in collaboration with Nvidia)

[ In partnership with Nvidia
](https://cloud.google.com/blog/products/compute/anthos-supports-nvidia-gpus)
, users can now manually attach a GPU to a worker node VM to run GPU
workloads. This requires using the [ open source Nvidia GPU operator
](https://github.com/NVIDIA/gpu-operator) .

**Note:** Manually attached GPUs do not persist through node lifecycle events.
You must manually re-attach them. This is a beta solution and can be used for
evaluation and proof of concept.

**CHANGED:**

The Ubuntu image is upgraded to include the newest packages.

**CHANGED:**

` gkectl delete loadbalancer ` is updated to support the new version of
configuration files for admin and user clusters.

**FIXED:**

**Fixes:**

  * Resolved a few incorrect Kubelet Metrics' names collected by Prometheus. 
  * Updated restarting machines process during admin cluster upgrade to make the upgrade process more resilient to transient connection issues. 
  * Resolved a preflight check OS image validation error when using a non-default vSphere folder for cluster creation; the OS image template is expected to be in that folder. 
  * Resolved a ` gkectl upgrade loadbalancer ` issue to avoid validating the upgraded SeesawGroup. This fix lets the existing SeesawGroup config be updated without negatively affecting the upgrade process. 
  * Resolved an issue where ClientConfig CRD is deleted when the upgrade to the latest version is run multiple times. 
  * Resolved a ` gkectl update credentials vsphere ` issue where the vsphere-metrics-exporter was using the old credentials even after updating the credentials. 
  * Resolved an issue where the VIP preflight check reported a user cluster add-on load balancer IP false positive. 
  * Fixed ` gkeadm ` updating config after upgrading on Windows, specifically for the ` gkeOnPremVersion ` and ` bundlePath ` fields. 
  * Automatically mount the data disk after rebooting on admin workstations created using ` gkeadm ` 1.4.0 and later. 
  * Reverted thin disk provisioning change for boot disks in 1.4.0 and 1.4.1 on all normal (excludes test VMs) cluster nodes. 
  * Removed vCenter Server access check from user cluster nodes. 

**App Engine standard environment Java**

**CHANGED:**

Updated Java SDK to version 1.9.82.

**Cloud Spanner**

**FEATURE:**

A new [ multi-region instance configuration
](https://cloud.google.com/spanner/docs/instances#available-configurations-
multi-region) is now available in North America - ` nam11 ` (Iowa/South
Carolina).

**Cloud TPU**

**FEATURE:**

#  PyTorch/XLA 1.6 Release (GA)

##  Highlights

Cloud TPUs now support the [ PyTorch 1.6 release
](https://github.com/pytorch/pytorch/releases/tag/v1.6.0) , via PyTorch/XLA
integration. With this release we mark our general availability (GA) with the
models such as ResNet, FairSeq Transformer and RoBERTa, and HuggingFace GLUE
task models that have been rigorously tested and optimized.

In addition, with our PyTorch/XLA 1.6 release, you no longer need to run the [
env-setup.py ](https://github.com/pytorch/xla/blob/master/contrib/scripts/env-
setup.py) script on Colab/Kaggle as those are now compatible with native `
torch ` wheels. You can still continue to use that script if you would like to
run with our latest unstable releases.

##  New Features

  * XLA RNG state checkpointing/loading (https://github.com/pytorch/xla/pull/2096) 
  * Device Memory XRT API (https://github.com/pytorch/xla/pull/2295) 
  * [Kaggle/Colab] Small host VM memory environment utility (https://github.com/pytorch/xla/pull/2025) 
  * [Advanced User] XLA Builder Support (https://github.com/pytorch/xla/pull/2125) 
  * New op supported on PyTorch/XLA 
    * Hardsigmoid (https://github.com/pytorch/xla/pull/1940) 
    * true_divide (https://github.com/pytorch/xla/pull/1782) 
    * max_unpool2d (https://github.com/pytorch/xla/pull/2188) 
    * max_unpool3d (https://github.com/pytorch/xla/pull/2188) 
    * Replication_pad1d (https://github.com/pytorch/xla/pull/2188) 
    * Replication_pad2d (https://github.com/pytorch/xla/pull/2188) 
  * Dynamic shape support on XLA:CPU and XLA:GPU (experimental) 

##  Bug Fixes

  * RNG Fix (proper dropout) 
  * Manual all-reduce in backward pass (https://github.com/pytorch/xla/pull/2325) 

**Compute Engine**

**FEATURE:**

The Organization Policy for [ restricting protocol forwarding creation
](https://cloud.google.com/compute/docs/protocol-
forwarding#enforcing_protocol_forwarding_settings_across_a_project_folder_or_organization)
has launched into general availability.

**Istio on Google Kubernetes Engine**

**FIXED:**

**Istio 1.4.10-gke.5**

Fixes an issue with protocol detection connection timeouts.

##  August 19, 2020

**AI Platform Prediction**

**CHANGED:**

You can now use [ runtime version 2.1 ](https://cloud.google.com/ai-
platform/prediction/docs/runtime-version-list) to serve online predictions
using scikit-learn 0.22.1 and XGBoost 0.90.

**BigQuery**

**FEATURE:**

When using consecutive ` ON ` / ` USING ` clauses, parentheses are now
optional and can be omitted. For example, you can use either of the following
statements:

  * ` FROM A JOIN (B JOIN C ON B.x = C.y) USING (z) `
  * ` FROM A JOIN B JOIN C ON B.x = C.y USING (z) `

**Cloud Interconnect**

**FEATURE:**

Organization policy constraints for Cloud Interconnect is available in
**Beta** .

To control which VPC networks can use Cloud Interconnect, you can set an
organization policy. For more information, see [ Restricting Cloud
Interconnect usage ](https://cloud.google.com/network-
connectivity/docs/interconnect/how-to/restricting-usage) .

**Cloud Load Balancing**

**FEATURE:**

The Organization policy constraint for [ restricting Cloud Load Balancing
creation ](https://cloud.google.com/load-balancing/docs/org-policy-
constraints) is now available in **General Availability** .

**Cloud NAT**

**FEATURE:**

[ Organization policy constraints for Cloud NAT
](https://cloud.google.com/nat/docs/org-policy-constraints) is available in
**Beta** .

**Cloud TPU**

**FEATURE:**

Cloud TPU now supports Shared VPC in Beta.

Shared VPC allows an organization to connect resources from multiple projects
to a common VPC network to communicate with each other securely and
efficiently using internal IPs from that network. This release enables
connecting to Cloud TPU Nodes from Shared VPC networks.

**Config Connector**

**FEATURE:**

Add support for configuring Bigtable garbage collection policies with the `
BigtableGCPolicy ` resource

**FIXED:**

Fixes issue where ` SQLUser ` would constantly update despite there being no
changes.

**FIXED:**

Fix issue where Deletion Defender would sometimes panic during uninstallation
of Config Connector, preventing uninstallation to complete.

**FIXED:**

Performance improvements.

**Game Servers**

**FEATURE:**

**General availability release** Game Servers is generally available with
release version v1.

**FEATURE:**

[ VPC Service Controls ](https://cloud.google.com/vpc-service-
controls/docs/overview) provide additional security for Game Servers
resources.

**Resource Manager**

**FEATURE:**

The Organization Policies for [ restricting Cloud Interconnect usage
](https://cloud.google.com/network-connectivity/docs/interconnect/how-
to/restricting-usage) have launched into beta.

The Organization Policy for [ restricting protocol forwarding creation
](https://cloud.google.com/compute/docs/protocol-
forwarding#enforcing_protocol_forwarding_settings_across_a_project_folder_or_organization)
has launched into general availability.

The Organization policy for [ restricting Cloud Load Balancing creation
](https://cloud.google.com/load-balancing/docs/org-policy-constraints) has
launched into general availability.

##  August 18, 2020

**AI Platform Prediction**

**CHANGED:**

[ Compute Engine (N1) machine types for online prediction
](https://cloud.google.com/ai-platform/prediction/docs/machine-types-online-
prediction) are now generally available. They are available on all [ regional
endpoints ](https://cloud.google.com/ai-platform/prediction/docs/regional-
endpoints) .

The [ AI Platform Training and Prediction Service Level Agreement
](https://cloud.google.com/ai-platform/training-and-prediction/sla) does not
apply to [ model versions that use a Compute Engine (N1) machine type and
fewer than two prediction nodes ](https://cloud.google.com/ai-
platform/prediction/docs/machine-types-online-prediction#scaling) .

**CHANGED:**

[ GPUs for online prediction ](https://cloud.google.com/ai-
platform/prediction/docs/machine-types-online-prediction#gpus) are now
generally available. You can use GPUs to serve predictions when you create a
TensorFlow model version that uses a [ Compute Engine (N1) machine type
](https://cloud.google.com/ai-platform/prediction/docs/machine-types-online-
prediction) .

Learn [ which types of GPU are available on each regional endpoint
](https://cloud.google.com/ai-
platform/prediction/docs/regions#using_gpus_for_online_prediction) .

**CHANGED:**

The following [ regional endpoints for online prediction
](https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints) are
now generally available:

  * ` us-central1-ml.googleapis.com `
  * ` europe-west4-ml.googleapis.com `
  * ` asia-east1-ml.googleapis.com `

**DEPRECATED:**

Using [ Compute Engine (N1) machine types ](https://cloud.google.com/ai-
platform/prediction/docs/machine-types-online-prediction) on the global API
endpoint ( ` ml.googleapis.com ` ) is deprecated. This functionality was
previously available in beta in the ` us-central1 ` region.

To continue to use Compute Engine (N1) machine types in the ` us-central1 `
region, create a model on the ` us-central1-ml.googleapis.com ` [ regional
endpoint ](https://cloud.google.com/ai-platform/prediction/docs/regional-
endpoints) , and then create model versions using that model.

**BigQuery**

**FEATURE:**

You can now explicitly assign projects to use on-demand pricing with
Reservations. See [ Assign a project to None
](https://cloud.google.com/bigquery/docs/reservations-tasks#assign-project-to-
none) .

**Cloud Run**

**FEATURE:**

You can now [ allocate up to 4GiB of memory
](https://cloud.google.com/run/docs/configuring/memory-limits) to your Cloud
Run (fully managed) services.

**Compute Engine**

**FEATURE:**

N2D machine types are now available in ` us-central1-c ` . For more
information, see the [ VM instance pricing
](https://cloud.google.com/compute/vm-instance-pricing#n2d_machine_types)
page.

**FEATURE:**

N2D machine types are now available in Northern Virginia ` us-east4-a,b ` .
For more information, see the [ VM instance pricing
](https://cloud.google.com/compute/vm-instance-pricing#n2d_machine_types)
page.

##  August 17, 2020

**AI Platform Deep Learning Containers**

**FEATURE:**

TensorFlow Enterprise 2.3 environments are now available. These environments
include support for A100 GPU accelerators, CUDA 11, and TensorFloat-32 (TF32).

**AI Platform Training**

**FEATURE:**

You can now set a maximum time that you are willing to wait between the moment
when you create a training job and the moment when AI Platform Training starts
running the job. If your training job has not started running after this
duration, AI Platform Training cancels the job. Set the maximum wait time by
specifying the [ ` scheduling.maxWaitTime ` ](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs#scheduling) field.

**Artifact Registry**

**FEATURE:**

You can now use Pub/Sub to configure notifications for changes in Docker
repositories. For more information, see [ Configuring Pub/Sub notifications
](https://cloud.google.com/artifact-registry/docs/configure-notifications) .

**BigQuery ML**

**FEATURE:**

Matrix Factorization model support is now [ Generally Available
](https://cloud.google.com/products/#product-launch-stages) (GA). For more
information, see the following documentation:

  * [ ` CREATE MODEL ` statement for Matrix Factorization ](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-matrix-factorization)

  * [ ` ML.RECOMMEND ` function ](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-recommend)

  * [ Using BigQuery ML to predict movie recommendations ](https://cloud.google.com/bigquery-ml/docs/bigqueryml-mf-explicit-tutorial)

  * [ Using BigQuery ML to predict website content for visitors ](https://cloud.google.com/bigquery-ml/docs/bigqueryml-mf-implicit-tutorial)

**Cloud Build**

**FEATURE:**

The Cloud Build GitHub App now allows users to [ view triggers by name
](https://cloud.google.com/cloud-build/docs/create-github-app-
triggers#data_sharing) on [ GitHub ](https://github.com/) , including in pull
requests. Note that required status checks may need to be updated on GitHub
after enabling this feature.

**Cloud Load Balancing**

**FEATURE:**

[ Setting up Internal HTTP(S) Load Balancing in a Shared VPC _service_ project
](https://cloud.google.com/load-balancing/docs/l7-internal/l7-internal-shared-
vpc) is now available in **General Availability** .

**Cloud Logging**

**FEATURE:**

To help you explore your logs more efficiently, Cloud Logging now provides
suggested queries based on the context of your Google Cloud project. For more
information, go to [ Suggested queries
](https://cloud.google.com/logging/docs/view/building-
queries#suggested_queries) .

**Cloud Trace**

**FEATURE:**

The Cloud Trace viewer now supports search by the trace ID. For more
information, see [ Viewing Trace Details
](https://cloud.google.com/trace/docs/viewing-details) .

**Dataproc**

**FEATURE:**

Launched new [ Personal Cluster Authentication
](https://cloud.google.com/dataproc/docs/concepts/iam/personal-auth) feature,
which allows the creation of single-user clusters that can access Cloud
Storage using the user's own credentials instead of a VM service account.

##  August 14, 2020

**AI Platform Training**

**FEATURE:**

The [ TabNet ](https://arxiv.org/abs/1908.07442) built-in algorithm is now
available in Beta. You can train models on tabular data for classification and
regression problems, and also get feature attributions to help explain the
model's behavior.

Try the [ TabNet built-in algorithm introductory tutorial
](https://cloud.google.com/ai-platform/training/docs/algorithms/tab-net-start)
.

**Anthos Service Mesh**

**FIXED:**

**1.6.8-asm.0 and 1.5.9-asm.0**

Fixes the security issue, [ ISTIO-SECURITY-2020-009
](https://istio.io/latest/news/security/istio-security-2020-009) , with the
same fixes as Istio 1.6.8 and Istio 1.5.9. For more information, see the Istio
release notes:

  * [ Istio 1.6.8 release notes ](https://istio.io/latest/news/releases/1.6.x/announcing-1.6.8/)

  * [ Istio 1.5.9 release notes ](https://istio.io/latest/news/releases/1.5.x/announcing-1.5.9/)

**Cloud Functions**

**CHANGED:**

Cloud Functions now supports [ Java 11
](https://cloud.google.com/functions/docs/concepts/java-runtime) at the [
General Availability release level
](https://cloud.google.com/products/#product-launch-stages) .

**Dataproc**

**CHANGED:**

Dataproc quotas are now regional: each region now has its own quota, which can
be separately adjusted. All existing quota overrides have been migrated;
customer action is not required.

**CHANGED:**

Enabled Spark SQL parquet metadata cache (removed `
spark.sql.parquet.cacheMetadata=false ` from Spark default configuration).

**CHANGED:**

New [ sub minor versions
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions#supported_dataproc_versions) of Dataproc images: 1.3.66-debian10,
1.3.66-ubuntu18, 1.4.37-debian10, 1.4.37-ubuntu18, 1.5.12-debian10,
1.5.12-ubuntu18, 2.0.0-RC8-debian10, and 2.0.0-RC8-ubuntu18.

**CHANGED:**

Image 1.4:

  * Fixed a bug in Spark EFM HCFS shuffle where failures after partial commits are not recoverable. 
  * Upgraded Spark to [ 2.4.6 version ](http://spark.apache.org/news/spark-2-4-6.html) . 

**CHANGED:**

Image 1.5:

  * Fixed a bug in Spark EFM HCFS shuffle where failures after partial commits are not recoverable. 
  * Upgraded Spark to [ 2.4.6 version ](http://spark.apache.org/news/spark-2-4-6.html) . 
  * Upgraded Zeppelin to [ 0.9.0-preview2 version ](https://zeppelin.apache.org/docs/0.9.0-preview2/) . 
  * Included all plugins in Zeppelin installation by default. 

**CHANGED:**

Image 2.0 preview:

  * Upgraded Zeppelin to [ 0.9.0-preview2 version ](https://zeppelin.apache.org/docs/0.9.0-preview2/) . 
  * Included all plugins in Zeppelin installation by default. 
  * Upgraded HBase to [ 2.2.5 version ](https://downloads.apache.org/hbase/2.2.5/RELEASENOTES.md) . 

**Identity Platform**

**FEATURE:**

Multi-factor authentication (MFA) is now GA!

**Identity and Access Management**

**FEATURE:**

You can now use Cloud Monitoring to [ check when your service accounts and
service account keys were used ](https://cloud.google.com/iam/docs/service-
account-monitoring) . This feature is available in beta.

**FEATURE:**

You can now use an organization policy to [ extend the maximum lifetime for
OAuth 2.0 access tokens ](https://cloud.google.com/iam/docs/creating-short-
lived-service-account-credentials#sa-credentials-oauth) that you create for a
service account.

**Resource Manager**

**FEATURE:**

The Organization Policy for [ extending the maximum lifetime for OAuth 2.0
access tokens ](https://cloud.google.com/iam/docs/creating-short-lived-
service-account-credentials#sa-credentials-oauth) that you create for a
service account has been launched into general availability.

##  August 13, 2020

**BigQuery**

**CHANGED:**

The [ exports per day ](https://cloud.google.com/bigquery/quotas#export_jobs)
(Extract Bytes) default quota has been raised from 10 TB to 50 TB per day.

**Cloud Monitoring**

**FEATURE:**

The new, out-of-the-box **Infrastructure Summary** dashboard for Compute
Engine VMs provides a single-pane-of-glass view into your VM fleet and load
balancers. At a glance, you can see the top 5 VMs across a variety of key
metrics including memory, CPU, sent/received traffic, latency, disk
read/write, and more.

**Config Connector**

**FEATURE:**

The Config Connector [ GKE Add-on ](https://cloud.google.com/config-
connector/docs/how-to/install-upgrade-uninstall#installing_kcc) is launched to
GA. Users can now enable the GKE Add-on on cluster creation with the ` gcloud
` CLI or on the Cloud Console.

**FEATURE:**

Add support for ` BigtableAppProfile `

**Google Cloud Marketplace Partners**

**FEATURE:**

Google Cloud Marketplace supports filters, called Category IDs, that are
available to customers within the Google Cloud console. When you add a
Category ID, your solution shows up in the filtered view for that category
when customers search for solutions in Cloud Marketplace. You can select up to
two categories for each of your solutions.

To add or modify categories, go to the **Solutions Details** page and edit the
**Category ID** section.

**Virtual Private Cloud**

**FEATURE:**

[ GRE support ](https://cloud.google.com/vpc/docs/vpc#specifications) for VPC
networks is now available in **Beta** .

##  August 12, 2020

**Cloud Billing**

**FEATURE:**

Recommendations for Compute Engine committed use discounts are now available
in **beta** . Recommendations provide you opportunities to optimize your
compute costs by analyzing your VM spending trends and recommending committed
use discount contracts. For understanding and purchasing committed use
discount recommendations, see [ the documentation
](https://cloud.google.com/billing/docs/how-to/cud-analysis-resource-
based#understanding_commitment_recommendations) .

**Cloud Monitoring**

**FEATURE:**

Enhancements to the pre-configured Compute Engine **VM Instances** dashboard.
The inventory table now includes a **Monitoring Agent Status** column, and the
Monitoring agent can be installed by using a UI workflow from the table. The
**Explore** tab gives an overview of additional metrics being sent (including
agent metrics, custom metrics, and logs-based metrics) as well as a set of
quick links to learn more about each type of metric. You can also use the
**Recommended Alerts** button on the dashboard to configure fleet-wide alerts.

**Compute Engine**

**FEATURE:**

Compute Engine [ Committed use discount recommendations
](https://cloud.google.com/compute/docs/instances/signing-up-committed-use-
discounts#recommendations) are available in beta. Committed use
recommendations give you opportunities to optimize your compute costs by
analyzing your VM spending trends. For additional information, see [
Understanding commitment recommendations
](https://cloud.google.com/billing/docs/how-to/cud-analysis-resource-
based#understanding_commitment_recommendations) .

**CHANGED:**

[ CPU overcommit on sole-tenant nodes
](https://cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-
vms) lets you overprovision sole-tenant node resources and schedule more VM
CPUs on a sole-tenant node than are normally available. This feature is
**Generally Available** .

**FEATURE:**

Key metrics for persistent disks in the new disk-level Monitoring tab are now
**Generally Available** . Select any persistent disk attached to a single VM
from [ Disks ](https://console.cloud.google.com/compute/disks) to see mean
throughput, peak throughput, mean operations, and peak operations. You can
also open each metric in [ Monitoring
](https://console.cloud.google.com/monitoring) for querying, browsing, adding
to a dashboard, or configuring alerts.

**Migrate for Compute Engine**

**FEATURE:**

V4.11 offers integration with Secret Manager. You can store Migrate for
Compute Engine password and encryption key as objects in secret manager to
provide a higher level of security and control. See [ Configuring the
migration manager ](https://cloud.google.com/migrate/compute-
engine/docs/4.11/how-to/configure-manager/configuring-migration-manager) for
more.

**FEATURE:**

V4.11 introduces Windows upgrade with bring-your-own-license (BYOL) feature.
Migrating Windows Server 2008R2 with a customer owned license (BYOL) can
upgrade to Windows Server 2012R2 using BYOL as part of the migration process.
See [ Upgrading Windows Server VMs ](https://cloud.google.com/migrate/compute-
engine/docs/4.11/how-to/upgrading-vms/upgrading-windows-vms) for more.

**FEATURE:**

V4.11 introduces automatic deployment of Google Cloud OS Config agent to
migrating VMs. This allows you to get insights on your migrated VM patch
status and automate deployment of software patches to migrated VMs. See [
Adapting VMs to run on Google Cloud
](https://cloud.google.com/migrate/compute-engine/docs/4.11/concepts/planning-
a-migration/vm-adaptations) for more.

**FEATURE:**

Migrate Backend network connectivity requirement to Migrate Manager and Cloud
Extensions have been reduced, all traffic on this channel is performed over
port 443 (HTTPS and TLS) instead of using port 9111. See [ Network access
requirements ](https://cloud.google.com/migrate/compute-
engine/docs/4.11/concepts/planning-a-migration/network-access-requirements)
for more.

**FEATURE:**

Usability enhancements in the following flows:

  * Automatic adjustments of VDDK max open sessions when accessing vSphere V6.5 to avoid overloading VDDK max connections limit. 
  * Support for vCenter certificate update flow. 
  * Enhancement of automatic license assignment feature to offline migration flow. 

**ISSUE:**

**#160405343** : Due to a change in behavior on the activation flow for SUSE,
configuring repositories on SUSE Enterprise Linux instances post-detach now
fail.

**Workaround** : The following workaround can be used prior to detach (either
before migration or before detach).

  1. Follow the instructions described for Situation 4 at [ https://www.suse.com/support/kb/doc/?id=000019633 ](https://www.suse.com/support/kb/doc/?id=000019633) to download the required packages for Compute Engine as a tar.gz file. 

  2. **For SLES 12.x** , then run the following commands: 
    
        tar -xf late_instance_offline_update_gce_SLE12.tar.gz
    cd x86_64/
    zypper --no-refresh --no-remote --non-interactive in *.rpm```
    

  1. **For SLES 15.x** , then run the following commands: 
    
        tar -xf late_instance_offline_update_gce_SLE15.tar.gz
    cd x86_64/
    zypper --no-refresh --no-remote --non-interactive in *.rpm```
    

**ISSUE:**

**#149004085** : Ubuntu 14 from on-premise may fail to start networking post
detach.

**Workaround** : Connect via the serial console and manually add the network
interface with DHCP.

**ISSUE:**

**#145086776** : In rare cases, older versions of RHEL7 may hang during
streaming or reach a Kernel panic. This issues were resolved in later versions
of RHEL7.

**Workaround** : Run ` sudo yum update ` before migrating to update the
system.

**ISSUE:**

**#145644737** : Clones created on Azure or AWS from instances of Linux
distributions that use cloud-init may experience issues in booting after
installing the Linux prep package.

**Workaround** : Uninstall the package before cloning and reinstall when
preparing to migrate.

**ISSUE:**

**#143313211** : Customer migrating RHEL 6.8 VM may experience boot issues in
the cloud destination.

RHEL 6.x systems using kernel versions 2.6.32-xxx and using LVM may reach a
kernel panic when booting in Compute Engine during migration.

**Workaround** : The kernel should be upgraded to 2.6.32-754 or higher before
migrating.

**ISSUE:**

**#143262721** : Migration of VM from Azure fails when data disk is greater
than 4 terabytes.

At this time, Migrate for Compute Engine does not support migration of Azure
VMs with data disks bigger than 4TB.

**Workaround** : Make sure VM has data disk smaller than 4TB.

**ISSUE:**

**#131532690** : Run-in-cloud and migration operations may fail for Windows
Server 2016 workload when Symantec Endpoint Protection (SEP) is installed.
This may also happen when SEP appears to be disabled.

**Workaround** : Modify workload Network interface bindings to remove the SEP
option.

  1. Download [ Microsoft Network VSP Bind (nvspbind) ](https://gallery.technet.microsoft.com/Hyper-V-Network-VSP-Bind-cf937850)
  2. Install Microsoft_Nvspbind_package.EXE into c:\temp. 
  3. Open a command prompt as an Administrator and run the following: 

` nvspbind.exe /d * symc_teefer2 `

**ISSUE:**

**#131614405** : When the Velostrata Prep RPM is installed on SUSE Linux
Enterprise Server 11, the VM obtains a DHCP IP address in addition to an
existing static IP configuration. This issue occurs when the VM is started on-
premises in a subnet that is enabled with DHCP services.

**Note** : The issue does not occur when the subnet has no DHCP services.
There is no connectivity impact for communications with the original static IP
address.

**ISSUE:**

**#131637800** : After registering the Velostrata plug-in, running the Cloud
Extension wizard might generate an error "XXXXXXXXXX" upon "Finish".

**Workaround** : Un-register the Velostrata plug-in and restart the vSphere
Web client service, then re-register the plug-in. Contact support if the issue
persists.

**ISSUE:**

**#131548730** : In some cases, when a VM is moved to Run-in-Cloud while a 3rd
party VM-level backup solution holds a temporary snapshot, the Migrate for
Compute Engine periodic write-back operations will not complete even after the
backup solution deletes the temporary snapshot. The uncommitted writes counter
on the VM will show an increasing size and no consistency checkpoint will be
created on-premises.

**Workaround** : Select the Run On-Premises action for the VM and wait for the
task to complete, which will commit all pending writes. Then select the Run-
in-Cloud action again. Note that committing many pending writes may take a
while. Do not use the Force option as this will result in the loss of the
uncommitted writes.

**ISSUE:**

**#131605387** : vCenter reboot causes Velostrata tasks in vCenter to
disappear from UI. This is a vCenter limitation.

**Workaround** : Use the Velostrata PowerShell module to monitor Velostrata
managed VMs or Cloud Extensions tasks that are currently running.

**ISSUE:**

**#131638716** : With an ESXi host in maintenance mode, if a VM is moved to
cloud, the operation will fail and get stuck in the rollback phase.

**Workaround** : Manually cancel the Run-in-Cloud task, migrate the VM to
another ESXi host in the cluster and retry the Run-in-Cloud operation.

**ISSUE:**

**#131638455** : A Run-in-Cloud operation fails with the error - "Failed to
create virtual machine snapshot. The attempted operation cannot be performed
in the current state (Powered off)".

**Workaround** : The VMware VM snapshot file may be pointing to a non-existent
snapshot. Contact support for assistance in correcting the issue.

**ISSUE:**

**#131534862** : In rare cases, after running a Workload back on-premises -
Workload VMDK's are locked. In certain cases, this is due to network
disruptions between the Velostrata management appliance and the ESXi host on
which the workload is running.

**Note** : The issue will resolve itself after 1-2 hours.

**ISSUE:**

**#131550214** : During Detach, the operation might fail with the following
error message: "Operation was canceled".

**Workaround** : Retry the Detach operation.

**ISSUE:**

**#131650367** : When performing a detach after a cancel detach operation, the
action may fail.

**Workaround** : Retry the operation.

**ISSUE:**

**#131649978** : In the event of certain system failures, Velostrata
components disconnect from vCenter. In this case, an event may not be sent,
resulting in the alarm either not being set properly or not being cleared
properly.

**Workaround** : Clear the alarm manually in vCenter.

**ISSUE:**

**#131532549** : For workloads with a Windows machine using a retail license,
when returning from the cloud, the license is not present.

**Workaround** : Reinstall the license.

**ISSUE:**

**#131555885** : vCenter "Export OVA" operation is available when the VM in
cloud is running in cache mode, however, this operation results in a corrupted
OVA.

**Workaround** : Only create OVA after the detach.

**ISSUE:**

**#131647857** : In rare cases, when a cloud component instance is created and
system fails before it is tagged, the instance will remain untagged. This will
not allow full clean-up or repair of the CE.

**Workaround** : Manually tag the instance, and then run "Repair".

**ISSUE:**

**#131537125** : Cloud Extension high availability does not work for workloads
running Ubuntu OS with LVM configuration.

**Workaround** : Update the kernel to 3.13.0-161 or higher.

**ISSUE:**

**#131560126** : Suse12: Due to a bug in SUSE kernel older than 4.2,
configurations that include BTRFS mounts with subvolumes are not supported.

**Workaround** : Upgrade to SUSE version with Kernel >=4.2 (SP2).

**ISSUE:**

**#131533480** : When using the Create Cloud Extension wizard, using an
illegal HTTP proxy address will not generate a warning message.

**Workaround** : Delete the CE and then create the CE with a valid HTTP proxy
address.

**ISSUE:**

**#131647654** : Run on-premises operation succeeded but the status is marked
as failed with error "Failed to consolidate snapshots"

**Workaround** : Consolidate snapshots via vCenter, and clear the error
manually.

**ISSUE:**

**#131558198** : PowerShell client for cloud to cloud Runbook reports errors
when running on PowerShell 3.0

**Workaround** : Upgrade to PowerShell 4.0

**ISSUE:**

**#131533056** : When migrating RHEL 7.4 from AWS to Google Cloud, Google
Cloud agent will not be installed automatically.

**Workaround** : Manually remove the AWS agent and install Google Cloud agent

**ISSUE:**

**#131532713** : After Offline Migration of Windows 2003R2, if a NIC is
manually deleted, it may be impossible to auto-detect and automatically
reinstall it.

**Workaround** : The VM storage can be attached to a different VM, and the NIC
Registry entry could be imported manually using a similar VM as a reference.
Contact support for assistance.

**ISSUE:**

**#131532666** : Linux versions running with kernel version 2.6.32 may
experience a kernel panic on ephemeral storage access failures; these are more
likely while streaming over iSCSI.

**Workaround** : Upgrade your kernel. The issue will also reduce in likelihood
after Detach.

**ISSUE:**

**#131532846** : Certain firewalls and anti-viruses may cause Windows VMs to
fail when moved to cloud by blocking iSCSI traffic.

**Workaround** : Disable the affecting service while migrating and reinstall
after Detach.

**ISSUE:**

**#131532882** : In certain cases, initiating Run in Cloud during a Windows
update may cause the update to terminate abruptly and cause a failure to boot
in the cloud.

**Workaround** : Allow the system to finish Windows update and/or suspend
Windows updates before migrating.

**ISSUE:**

**#135664281** : When completing or canceling Azure to Google Cloud migration,
if Velostrata Management failed to start the importer, Velostrata-created
resources may be left in the original instance's resource group.

**ISSUE:**

**#133137658** : Scenario: No network connection between Migration Manager and
VSphere

Customer Impact: RunInCloud task will stay stuck due to failure in call to
getReadSessions on VSphere.

**Workaround** : Fix the network connection. If not, cancel the task and try
again.

**ISSUE:**

**#135573857** : Scenario: When moving a VM back on-prem with "force" flag,
failure to consolidate snapshot will cause the VM to remain as managed by
Velostrata. RunInCloud on the same VM may fail since it is not allowed on
managed VMs.

**Workaround** : Wait a couple of minutes and try again.

**ISSUE:**

**#137082702** : In rare cases, the Cancel detach operation succeeds but the
VM instance will fail to start.

**Workaround** : Move the instance back and move it again to the cloud.

##  August 11, 2020

**BigQuery**

**CHANGED:**

For [ flat-rate pricing
](https://cloud.google.com/bigquery/pricing#flat_rate_pricing) , the minimum
slot purchase is now 100 slots. Slots can be purchased in 100-slot increments.

**Cloud Logging**

**CHANGED:**

Users now manage logs exclusions through logs sinks. As a result, custom roles
that have the ` logging.sinks.* ` permissions can now control the volume of
logs ingested into Cloud Logging through logs sinks.

We recommend that you review any custom roles with the ` logging.sinks.* `
permissions so that you can make adjustments as needed.

**FEATURE:**

Beta release: You can now use Logs Buckets to centralize or divide your logs
based on your needs. For information about this feature, refer to the [
Managing logs buckets ](https://cloud.google.com/logging/docs/buckets) guide.

##  August 10, 2020

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M54 release**

  * Added support for the europe-west3 region 
  * Updated the Explainable AI sdk and added explainers 
  * Fixed llvm-openmp support 
  * Added support for instance auto upgrade 
  * Made Deep Learning VM images and Deep Learning Containers more consistent for TPU 
  * Updated NCCL to 2.7.6 in CU110 images 
  * Added the scikit-learn package and container 
  * Added JRE to R images 
  * Limited custom container memory utilization 

**Cloud Composer**

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.11.2-airflow-1.10.3 ` , ` composer-1.11.2-airflow-1.10.6 ` , and ` composer-1.11.2-airflow-1.10.9 ` . The default is ` composer-1.11.2-airflow-1.10.6 ` . Upgrade your Cloud SDK to use features in this release. 

**FEATURE:**

  * **Airflow 1.10.6 and 1.10.9:** You can now specify a location argument when creating a ` BigQueryCheckOperator ` to use it in a different region from the Composer environment. 

**FIXED:**

  * Fixed GKE setting incompatibilities that broke environment creation for Composer versions between 1.7.2 and 1.8.3. 
  * When DAG serialization is on, plugins and DAGs are no longer synced when the Airflow web server starts up. This fixes web server failures when plugins use custom PyPI packages. 
  * Fixed intermittent failures when triggering a DAG from the Airflow Web UI with DAG serialization turned on. 
  * Fixed update operations (installing Python dependencies and upgrading environments) for domain-scoped projects. 
  * Fixed a broken link to the Airflow documentation in Airflow 1.10.9. 

**Dialogflow**

**FEATURE:**

Beta launch of [ regionalization and data residency
](https://cloud.google.com/dialogflow/docs/how/region) .

##  August 08, 2020

**Config Connector**

**FEATURE:**

Added support for ` BigtableTable `

**FIXED:**

Fix a bug where a CRD would be marked as uninstalling on a dryrun delete

##  August 07, 2020

**Cloud Billing**

**FEATURE:**

You can now view a summary of all your spend-based committed use discounts
(CUD) and purchase new commitments in the [ commitment dashboard
](https://cloud.google.com/docs/cuds-spend-based#view_commitment_dashboard) .
The dashboard lists the **type** of commitment, **region** it's located,
current **active** commitments, **term** length, and the **start** and **end**
dates for the commitment. See [ the documentation
](https://cloud.google.com/docs/cuds-spend-based#view_commitment_dashboard)
for more details.

**FEATURE:**

**New columns added to Cost Table report: Credit ID and Credit name.**
Starting with your **July 2020** invoice month, the [ cost table report
](https://cloud.google.com/billing/docs/how-to/cost-table) now includes
columns for ` Credit ID ` and ` Credit name ` . Including credit details in
the cost table report is especially useful for understanding project-level
credits, or for analyzing the source of multiple credits of the same type,
earned during the same invoice period (such as sustained usage discounts
earned as usage increases).

When you first load the cost table report, the credit columns are hidden by
default. You can use the [ column selector to customize the columns
](https://cloud.google.com/billing/docs/how-to/cost-
table#columns_in_the_cost_table) you view in the report as well as the columns
you download to CSV. See the [ documentation
](https://cloud.google.com/billing/docs/how-to/cost-table) for more details.

**Compute Engine**

**FEATURE:**

You can now update multiple instance properties using a single request from
the command-line tool or the Compute Engine API to update multiple instance
properties. For more information, see [ Updating instance properties
](https://cloud.google.com/compute/docs/instances/update-instance-properties)
.

##  August 06, 2020

**AI Platform Deep Learning VM Image**

**FEATURE:**

**M53 release**

TensorFlow Enterprise 2.3 images, including images that support CUDA 11.0, are
now available.

**BigQuery**

**CHANGED:**

BigQuery is now available in the following regions: [ Oregon (us-west1),
Belgium (europe-west1), and Netherlands (europe-west4)
](https://cloud.google.com/bigquery/docs/locations#regional-locations) .

**BigQuery BI Engine**

**CHANGED:**

BigQuery BI Engine is now available following regions: [ Oregon (us-west1),
Belgium (europe-west1), and Netherlands (europe-west4)
](https://cloud.google.com/bi-engine/docs/locations#regional-locations) .

**BigQuery Data Transfer Service**

**CHANGED:**

BigQuery Data Transfer Service is now available following regions: [ Oregon
(us-west1), Belgium (europe-west1), and Netherlands (europe-west4)
](https://cloud.google.com/bigquery-transfer/docs/locations#regional-
locations) .

**BigQuery ML**

**CHANGED:**

BigQuery ML is now available following regions: [ Oregon (us-west1), Belgium
(europe-west1), and Netherlands (europe-west4)
](https://cloud.google.com/bigquery-ml/docs/locations#regional-locations) .

**Cloud Billing**

**FEATURE:**

If you have a **negotiated pricing contract** associated with your Cloud
Billing account, **starting with your July 2020 invoice** , the [ **Cloud
Billing report** ](https://cloud.google.com/billing/docs/how-to/reports) and
the [ **Cost Breakdown report** ](https://cloud.google.com/billing/docs/how-
to/cost-breakdown) now support displaying your costs calculated using list
prices, displaying your **negotiated savings** as a separate credit. This view
helps you see how much money you are saving on your Google Cloud costs because
of your negotiated pricing contract.

For information on how to view your list costs and negotiated savings in
reports, see the documentation:

  * [ Learn more about viewing negotiated savings in your **Cloud Billing report** ](https://cloud.google.com/billing/docs/how-to/reports#contract-pricing) . 
  * [ Learn more about viewing negotiated savings in your **Cost Breakdown report** ](https://cloud.google.com/billing/docs/how-to/cost-breakdown#negotiated-savings) . 

**Cloud Spanner**

**FEATURE:**

A new [ multi-region instance configuration
](https://cloud.google.com/spanner/docs/instances#available-configurations-
multi-region) is now available in North America - ` nam10 ` (Iowa/Salt Lake).

##  August 05, 2020

**Cloud Functions**

**FEATURE:**

Cloud Functions Java 11, Python 3.7 or 3.8, and Go 1.13 runtimes now build
container images in the user's project, providing direct access to build logs
and removing the preset build-time quota.

See [ Building Cloud Functions
](https://cloud.google.com/functions/docs/building) for details.

**Istio on Google Kubernetes Engine**

**FEATURE:**

Starting with version 1.6, the Istio on GKE add-on uses the Istio Operator for
installation and configuration. When you upgrade your cluster to
1.17.7-gke.8+, 1.17.8-gke.6+, or higher, the Istio 1.6 Operator and control
plane are installed alongside the existing 1.4.x Istio control plane. The
upgrade requires user action and follows the [ dual control plane upgrade
](https://istio.io/latest/blog/2020/multiple-control-planes/) process
(referred to as canary upgrades in the Istio documentation). With a dual
control plane upgrade, you can migrate to the 1.6 version by setting a label
on your workloads to point to the new control plane and performing a rolling
restart. To learn more, see [ Upgrading to Istio 1.6 with Operator
](https://cloud.google.com/istio/docs/istio-on-gke/upgrade-with-operator) .

**Pub/Sub**

**FEATURE:**

Pub/Sub [ message ordering ](https://cloud.google.com/pubsub/docs/ordering) is
now available at the [ beta launch stage
](https://cloud.google.com/products/#product-launch-stages) .

##  August 04, 2020

**AI Platform Training**

**FEATURE:**

Read a new guide to [ distributed PyTorch training
](https://cloud.google.com/ai-platform/training/docs/distributed-pytorch) .
You can use this guide with [ pre-built PyTorch containers
](https://cloud.google.com/ai-platform/training/docs/getting-started-
pytorch#pytorch_containers) , which are in beta.

**Anthos GKE on AWS**

**FIXED:**

Anthos GKE on AWS 1.4.1-gke.17 is released. This release fixes a memory leak
that causes clusters to become unresponsive.

To upgrade your clusters, perform the following steps:

  1. Restart your [ control plane instances ](https://cloud.google.com/anthos/gke/docs/aws/troubleshooting#rebooting_your_control_plane) . 
  2. Upgrade your [ management service ](http://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading-management) to aws-1.4.1-gke.17. 
  3. Upgrade your [ user cluster's ](http://cloud.google.com/anthos/gke/docs/aws/how-to/upgrading-user-cluster) AWSCluster and AWSNodePools to 1.16.9-gke.15. 

**CHANGED:**

Use version 1.16.9-gke.15 for creating new clusters.

**Compute Engine**

**CHANGED:**

You can attach a maximum of 24 local SSD partitions for 9 TB per instance.
This is **generally available** on instances with N1 machine types. For more
information, see [ Local SSDs
](https://cloud.google.com/compute/docs/disks#localssds) .

##  August 03, 2020

**Anthos GKE on AWS**

**ISSUE:**

Anthos GKE on AWS 1.4.1-gke.15 clusters will experience a memory leak that
results in an unresponsive cluster. A fix for this issue is in development.

If you are planning to deploy an Anthos GKE on AWS cluster, wait until the fix
is ready.

**Cloud Asset Inventory**

**DEPRECATED:**

k8s.io/Node fields deprecation

The following two fields for assets of ` k8s.io/Node ` are now deprecated in
the exported output of Cloud Storage and BigQuery.

  * ` metadata.resourceVersion `
  * ` status.conditions.lastHeartbeatTime `

**Cloud Composer**

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.11.1-airflow-1.10.3 ` , ` composer-1.11.1-airflow-1.10.6 ` , and ` composer-1.11.1-airflow-1.10.9 ` . The default is ` composer-1.11.1-airflow-1.10.6 ` . Upgrade your Cloud SDK to use features in this release. 
  * Composer now enforces ` iam.serviceAccounts.actAs ` permission checks on the service account specified during Composer environment creation. See [ Creating environments ](https://cloud.google.com/composer/docs/how-to/managing/creating#access-control) for details. 

**FEATURE:**

  * Private IP environments can now be creating using non-rfc 1918 CGN ranges (100.64.0.0/10) 
  * New PyPi packages have been added for Composer version composer-1.11.0-airflow-1.10.6. These make it possible to install apache-airflow-backport-providers-google with no additional package upgrades. 
  * The PyPi package ` google-cloud-datacatalog ` can now be installed on Composer environments running Airflow 1.10.6 and Python 3. 
  * Cloud Composer 1.11.1+: Backport providers are installed by default for Airflow 1.10.6 and 1.10.9. 
  * You can now use the ` label.worker_id ` filter in Cloud Monitoring logs to see logs sent out of a specific Airflow worker Pod. 
  * With the Composer Beta API, you can now upgrade an environment to any of the three latest Composer versions (instead of just the latest). 
  * You can now modify these previously blocked Airflow configurations: ` [scheduler] scheduler_heartbeat_sec ` , ` [scheduler] job_heartbeat_sec ` , ` [scheduler] run_duration `

**FIXED:**

  * A more informative error message was added for environment creation failures caused by issues with Cloud SQL instance creation. 
  * Improved error reporting has been added for update operations that change the web server image in cases where the error occurs before the new web server image is created. 
  * The Airflow-worker liveness check has been changed so that a task just added to a queue will not fire an alert. 
  * Reduced the amount of non-informative logs thrown by the environment in Composer 1.10.6. 
  * Improved the syncing procedure for env_var.json in Airflow 1.10.9 (it should no longer throw "missing file:" errors). 
  * Airflow-worker and airflow-scheduler will no longer throw "missing env_var.json" errors in Airflow 1.10.6. 

**Cloud Logging**

**FEATURE:**

Alpha release: You can now use Logs Buckets to centralize or divide your logs
based on your needs. For information about this feature, refer to the [
Managing logs buckets ](https://cloud.google.com/logging/docs/buckets) guide.
To participate in the alpha or to get notified when Logs Buckets goes beta,
fill out the [ sign up form
](https://docs.google.com/forms/d/e/1FAIpQLSeBVpNBivnTAAd4G3rdait9t94uG9TWc07oGwNRGcE071TeCA/viewform)
.

**Cloud Run**

**FEATURE:**

When [ setting up Continuous Deployment
](https://cloud.google.com/run/docs/continuous-deployment-with-cloud-build) in
the Cloud Run user interface, you can now select a repository that contains
Go, Node.js, Python Java or .NET Core code. It will be built using [ Google
Cloud Buildpacks ](https://github.com/GoogleCloudPlatform/buildpacks) without
needing a Dockerfile.

**Compute Engine**

**FEATURE:**

You can now access C2 machine types in the following zones: Taiwan: ` asia-
east1-a ` , Singapore: ` asia-southeast1-a ` , Sao Paulo: ` southamerica-
east1-b,c ` , and Oregon: ` us-west1-b ` . For more information, see [ VM
instance pricing ](https://cloud.google.com/compute/vm-instance-
pricing#c2_machine_types) .

**Dataproc**

**CHANGED:**

Dataproc users are required to have [ service account ActAs permission
](https://cloud.google.com/iam/docs/service-accounts-actas) to deploy Dataproc
resources, for example, to create clusters and submit jobs. See [ Managing
service account impersonation
](https://cloud.google.com/iam/docs/impersonating-service-accounts) for more
information.

**Opt-in for existing Dataproc customers:** This change does not automatically
apply to current Dataproc customers without ` ActAs ` permission. To opt in,
see [ Securing Dataproc, Dataflow, and Cloud Data Fusion
](https://cloud.google.com/iam/docs/service-accounts-actas#dataproc-dataflow-
datafusion) .

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

**Config Connector**

**FEATURE:**

Add support for ` ArtifactRegistryRepository `

**FEATURE:**

Changes ` DataflowJob ` to allow for ` spec.parameters ` and `
spec.ipConfiguration ` to be updateable

**FIXED:**

Fixes issue that was causing ` ContainerNodePool ` and ` SQLDatabase ` to
display ` UpdateFailed ` due to the referenced ` ContainerCluster ` or `
SQLDatabase ` not being ready

**FIXED:**

Fixes issue preventing the creation of BigQuery resources that read from
Google Drive files due to insufficient OAuth 2.0 scopes

**FIXED:**

Fixes issue causing ` SourceRepoRepository ` to constantly update even when
there were no changes

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

**Anthos Config Management**

**FIXED:**

Updated the git-sync image to fix security vulnerability [ CVE-2019-5482
](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5482) .

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

**Cloud Composer**

**FEATURE:**

Cloud Composer is now available in Osaka ( ` asia-northeast2 ` ).

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

**Data Catalog**

**FEATURE:**

Data Catalog is now available in Seoul ( ` asia-northeast3 ` ).

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

