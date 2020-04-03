#  Google Cloud Platform release notes

The following release notes cover the most recent changes over the last 30
days. For a comprehensive list, see the [ individual product release note
pages ](/release-notes/all) .

##  March 30, 2020

**Cloud Monitoring**

**FEATURE:**

You can now write time-series data for custom and Prometheus metrics at the
rate of 1 data point every 10 seconds. This was previously limited to 1 point
every minute.

**CHANGED:**

Data for custom and Prometheus metrics is now retained for 24 months.
Previously, the retention period was 6 weeks.

**Cloud Trace**

**FEATURE:**

You can now use [ OpenTelemetry ](https://opentelemetry.io/) with [ Go
](https://cloud.google.com/trace/docs/setup/go-ot) and [ Node.js
](https://cloud.google.com/trace/docs/setup/nodejs-ot) to instrument your
applications running on GKE and Compute Engine.

**Service Directory**

**FEATURE:**

[ Service Directory ](https://cloud.google.com/service-directory/docs/) is
available in **Beta** .

##  March 26, 2020

**Memorystore for Memcached**

**FEATURE:**

Beta release of Memorystore for Memcached.

##  March 25, 2020

**Dialogflow**

**CHANGED:**

The shutdown of 7 integrations [ announced in January
](https://cloud.google.com/dialogflow/docs/release-notes#January_06_2020) is
now extended to May 6th, 2020.

##  March 24, 2020

**Cloud Profiler**

**CHANGED:**

Integration of Stackdriver Profiler with Virtual Private Cloud Service
Controls is now Generally Available. For more information, see [ VPC Service
Controls documentation ](https://cloud.google.com/vpc-service-controls/docs/)
.

##  March 23, 2020

**Anthos**

**FEATURE:**

[ Anthos ](https://cloud.google.com/anthos) 1.3.0 is now available.

###  Release notes for updated Anthos components

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

##  March 20, 2020

**Cloud Load Balancing**

**CHANGED:**

To help you get started quickly, added two new examples for external HTTP(S)
Load Balancing:

  * [ Setting up a simple external HTTP load balancer ](https://cloud.google.com/load-balancing/docs/https/ext-http-lb-simple)
  * [ Setting up a simple external HTTPS load balancer ](https://cloud.google.com/load-balancing/docs/https/ext-https-lb-simple)

**FEATURE:**

[ Health check logging ](https://cloud.google.com/load-balancing/docs/health-
check-logging) is now available in **Beta** .

##  March 19, 2020

**Cloud Spanner**

**FEATURE:**

The open-source [ C++ client library for Cloud Spanner
](https://github.com/googleapis/google-cloud-cpp-spanner) is now available. To
get started using C++ with Cloud Spanner, [ see this tutorial
](https://cloud.google.com/spanner/docs/getting-started/cpp) .

##  March 18, 2020

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

##  March 17, 2020

**Cloud Identity and Access Management**

**CHANGED:**

[ Forwarding rule attributes ](https://cloud.google.com/iam/docs/conditions-
attribute-reference#forwarding-rule) for Cloud IAM Conditions are now [
generally available ](https://cloud.google.com/products/#product-launch-
stages) . You can use these attributes to specify the types of [ forwarding
rules ](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts)
that a member can create.

**Cloud Logging**

**CHANGED:**

Incoming log entries must have timestamps that don't exceed the [ logs
retention periods
](https://cloud.google.com/logging/quotas#logs_retention_periods) in the past,
and that don't exceed 24 hours in the future. Log entries outside those time
boundaries aren't ingested by Cloud Logging.

**Dataproc**

**FEATURE:**

Added a ` dataproc:job.history.to-gcs.enabled ` [ cluster property
](https://cloud.google.com/dataproc/docs/concepts/configuring-
clusters/cluster-properties#service_properties) that allows persisting
MapReduce and Spark history files to the Dataproc temp bucket (default: ` true
` for image versions 1.5+). bucket. This property defaults to ` true ` for
image versions 1.5 and up. Users can overwrite the locations of job history
file persistence through the following properties:

  * ` mapreduce.jobhistory.done-dir `
  * ` mapreduce.jobhistory.intermediate-done-dir ` * ` spark.eventLog.dir `
  * ` spark.history.fs.logDirectory `

**FEATURE:**

Added support for ` n2- ` , ` c2- ` , ` e2- ` , ` n2d- ` , and ` m2- ` machine
types when using [ Auto Zone Placement
](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-
zone) . Previously, users could only specify ` n1- ` or ` custom- ` machine
types when using Auto Zone Placement.

**FEATURE:**

Added a ` mapreduce.jobhistory.always-scan-user-dir ` cluster property that
enables the MapReduce job history server to read the history files
(recommended when writing history files to Cloud Storage). The default is `
true ` .

**FEATURE:**

Customers can now enable the [ Cloud Profiler
](https://cloud.google.com/dataproc/docs/guides/profiling) when submitting a
Dataproc job by setting the ` cloud.profiler.enable ` property. To use
profiling, customers must enable the Cloud Profiler API for their project and
create the cluster with ` --scopes=cloud-platform ` . The following profiling
properties can also be set when submitting a Dataproc job:

  1. ` cloud.profiler.name ` : to collect profiler data under the specified name. If not specified, it defaults to the job UUID. 

  2. ` cloud.profiler.service.version ` : to compare profiler information from different job runs. If not specified, defaults to the job UUID. 

**CHANGED:**

New [ sub-minor versions
](https://cloud.google.com/dataproc/docs/concepts/versioning/dataproc-
versions#supported_cloud_dataproc_versions) of Dataproc images:
1.2.93-debian9, 1.3.53-debian9, 1.4.24-debian9, 1.5.0-RC9-debian10,
1.3.53-ubuntu18, 1.4.24-ubuntu18, and 1.5.0-RC9-ubuntu18

**CHANGED:**

**Image 1.2, 1.3, 1.4**

Upgraded HBase to 1.3.6

**CHANGED:**

**Image 1.4, 1.5 preview**

Added ` ARROW_PRE_0_15_IPC_FORMAT=1 ` for spark-env for pyarrow upgrade from
0.13 to 0.15.

**CHANGED:**

**Image 1.5 preview**

  * Preinstalled additional Python packages and Jupyter[Lab] extensions to align Jupyter notebook environment with AI Platforms Notebooks when Jupyter optional component is enabled. 

  * Upgraded Druid version to 0.17.0 

**CHANGED:**

Normalized custom image URLs to a full URL, for example: `
https://www.googleapis.com/compute/v1/projects/foo-project/global/images/foo-
image ` . The cluster creation API will continue to accept relative names,
such as ` projects/foo-project/global/images/foo-image ` or ` foo-image ` (see
[ Dataproc API doesn't return imageUri in a consistent format
](https://issuetracker.google.com/issues/139762442) ).

**CHANGED:**

Cluster list methods now return results in lexical order.

**FIXED:**

**Image 1.3, 1.4, 1.5 preview**

Fixed YARN container log links in Component Gateway

##  March 16, 2020

**Cloud SQL for MySQL**

**FEATURE:**

Cloud SQL now supports read replicas in a different region than that of the
primary instance, providing additional protection against regional outages and
improving read performance by making replicas available closer to your
application. To get started, see [ Cross-region replicas
](https://cloud.google.com/sql/docs/mysql/replication/cross-region-replicas) .

Cloud SQL instances using [ private IP
](https://cloud.google.com/sql/docs/mysql/private-ip) are now accessible
across regions, at the regular cross-region network egress cost.

**Cloud SQL for PostgreSQL**

**FEATURE:**

Cloud SQL now supports read replicas in a different region than that of the
primary instance, providing additional protection against regional outages and
improving read performance by making replicas available closer to your
application. To get started, see [ Cross-region replicas
](https://cloud.google.com/sql/docs/postgres/replication/cross-region-
replicas) .

Cloud SQL instances using [ private IP
](https://cloud.google.com/sql/docs/postgres/private-ip) are now accessible
across regions, at the regular cross-region network egress cost.

**Cloud SQL for SQL Server**

**FEATURE:**

Cloud SQL instances using [ private IP
](https://cloud.google.com/sql/docs/sqlserver/private-ip) are now accessible
across regions, at the regular cross-region network egress cost.

**Container Registry**

**FEATURE:**

Artifact Registry, the evolution of Container Registry, is now available in
beta. It includes support for Docker as well as Maven and npm package formats.

If you currently use Container Registry, see [ Planning for the upgrade from
Container Registry ](https://cloud.google.com/artifacts/docs/upgrade) for more
information.

**Dataproc**

**FEATURE:**

Announcing the [ General Availability (GA)
](https://cloud.google.com/terms/launch-stages#launch-stages) release of
Dataproc [ minimum CPU platform
](https://cloud.google.com/dataproc/docs/concepts/compute/dataproc-min-cpu) .

**Memorystore for Redis**

**FEATURE:**

Added new Memorystore for Redis [ region
](https://cloud.google.com/memorystore/docs/redis/regions) : Salt Lake City (
` us-west3 ` ).

##  March 13, 2020

**App Engine flexible environment Java**

**FEATURE:**

App Engine is now available in the ` asia-northeast3 ` region (Seoul).

**BigQuery Data Transfer Service**

**CHANGED:**

BigQuery Data Transfer Service now supports the [ Finland region
](https://cloud.google.com/bigquery-transfer/docs/locations#locations) .

**Dialogflow**

**CHANGED:**

On March 16, 2020, the [ Inline Editor
](https://cloud.google.com/dialogflow/docs/fulfillment-inline-editor) will use
[ Cloud Functions ](https://cloud.google.com/functions/docs) instead of [
Cloud Functions for Firebase ](https://firebase.google.com/docs/functions) .

##  March 12, 2020

**Cloud Build**

**FEATURE:**

The [ Create trigger ](https://console.cloud.google.com/cloud-build/triggers)
page on the Cloud Console has been updated. To learn more about creating build
triggers, see [ Creating and managing triggers
](https://cloud.google.com/cloud-build/docs/running-builds/create-manage-
triggers) .

**Cloud Logging**

**CHANGED:**

Cloud Logging Agent for Windows version 1-11 is now available. This version
upgrades ` fluentd ` from 1.4.2 to 1.7.4. Go to [ Installing the Cloud Logging
agent ](https://cloud.google.com/logging/docs/agent/installation) for
information on installing this version of the agent.

**Data Catalog**

**FEATURE:**

[ Support for custom entries ](https://cloud.google.com/data-catalog/docs/how-
to/custom-entries) is now in beta. This feature lets you ingest metadata of
any type, so it can be tagged and searched in Data Catalog.

##  March 11, 2020

**BigQuery Data Transfer Service**

**CHANGED:**

BigQuery Data Transfer Service now supports the [ Zürich region
](https://cloud.google.com/bigquery-transfer/docs/locations#locations) .

**Datastore**

**FEATURE:**

Support for [ ` us-west3 ` (Salt Lake City) and ` asia-northeast3 ` (Seoul)
](https://cloud.google.com/datastore/docs/locations) .

**Firestore**

**FEATURE:**

Support for [ ` us-west3 ` (Salt Lake City) and ` asia-northeast3 ` (Seoul)
](https://cloud.google.com/firestore/docs/locations) .

**Secret Manager**

**FEATURE:**

[ Secret Manager ](https://cloud.google.com/secret-manager/) is generally
available.

##  March 10, 2020

**Cloud Logging**

**FEATURE:**

Logs Viewer (Preview) now contains a histogram panel. The histogram panel lets
you visualize your logs data to more easily spot patterns and troubleshoot
issues. For more information, see [ Using Logs Viewer (Preview)
](https://cloud.google.com/logging/docs/view/logs-viewer-interface) .

**Config Connector**

**FEATURE:**

ComputeHealthCheck's location field now supports supplying a region

**FIXED:**

Fixed an issue with deleting StorageBucketAccessControl when the
ServiceAccount did not exist:
https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/39

**CHANGED:**

With the exception of role-bindings, moved all system components for
namespaced mode into the cnrm-system, note: you must completely uninstall and
reinstall to upgrade namespaced mode completely for this release.

**FEATURE:**

Added a version annotation to the Config Connector manifests

**Dataproc**

**CHANGED:**

Added the following flags to ` gcloud dataproc clusters create ` and ` gcloud
dataproc workflow-templates set-managed-cluster ` commands:

  * ` --num-secondary-workers `
  * ` --num-secondary-worker-local-ssds `
  * ` --secondary-worker-boot-disk-size `
  * ` --secondary-worker-boot-disk-type `
  * ` --secondary-worker-accelerator `

**DEPRECATED:**

The following flags to ` gcloud dataproc clusters create ` and ` gcloud
dataproc workflow-templates set-managed-cluster ` commands have been
deprecated:

  * ` --num-preemptible-workers `
  * ` --num-preemptible-worker-local-ssds `
  * ` --preemptible-worker-boot-disk-size `
  * ` --preemptible-worker-boot-disk-type `
  * ` --preemptible-worker-accelerator `

See the related change, above, for the new flags to use in place of these
deprecated flags.

**Dialogflow**

**CHANGED:**

Event names are now [ limited to 150 characters
](https://cloud.google.com/dialogflow/quotas#length_limits) .

**Managed Service for Microsoft Active Directory**

**FEATURE:**

[ VPC Service Controls ](https://cloud.google.com/vpc-service-
controls/docs/overview) integration is now in [ beta
](https://cloud.google.com/products/#product-launch-stages) .

Learn more about [ configuring VPC Service Controls
](https://cloud.google.com/managed-microsoft-ad/docs/how-to-use-vpc-service-
controls) for Managed Microsoft AD to provide additional security.

**VPC Service Controls**

**FEATURE:**

[ Beta stage ](https://cloud.google.com/products/#product-launch-stages)
support for:

  * [ Managed Service for Microsoft Active Directory ](https://cloud.google.com/managed-microsoft-ad/docs)

##  March 09, 2020

**AI Platform Prediction**

**FEATURE:**

[ Runtime version 2.1 ](https://cloud.google.com/ai-
platform/prediction/docs/runtime-version-list) for AI Platform Prediction is
now available.

Runtime version 2.1 is the first runtime version to support TensorFlow 2 for
online and batch prediction. Specifically, this runtime version includes
TensorFlow 2.1.0. Review the updated [ guide to exporting TensorFlow
SavedModels for use with AI Platform Prediction ](https://cloud.google.com/ai-
platform/prediction/docs/exporting-savedmodel-for-prediction) for details
about exporting compatible models by using TensorFlow 2 APIs, like Keras.

When you use runtime version 2.1 for online prediction, you can currently only
deploy TensorFlow model versions. You cannot deploy scikit-learn, XGBoost, or
custom prediction routine artifacts for online prediction with runtime version
2.1. For the time being, continue to use runtime version 1.15 to serve
predictions from these types of models.

Runtime version 2.1 is also the first runtime version _not_ to support Python
2.7. The Python Software Foundation ended support for Python 2.7 on January 1,
2020. No AI Platform runtime versions released after January 1, 2020 support
Python 2.7.

**ISSUE:**

If you deploy a model version for online prediction that uses [ runtime
version 2.1 ](https://cloud.google.com/ai-platform/prediction/docs/runtime-
version-list) with a [ GPU ](https://cloud.google.com/ai-
platform/prediction/docs/machine-types-online-prediction#gpus) , AI Platform
Prediction uses TensorFlow 2.0.0 (instead of TensorFlow 2.1.0) to serve
predictions. This is a known issue, and the release notes will be updated when
online prediction with GPUs supports TensorFlow 2.1.0.

**AI Platform Training**

**FEATURE:**

[ Runtime version 2.1 ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list) for AI Platform Training is now
available.

Runtime version 2.1 is the first runtime version to support TensorFlow 2.
Specifically, this runtime version includes TensorFlow 2.1.0. Read the new [
Training with TensorFlow 2 guide ](https://cloud.google.com/ai-
platform/training/docs/tensorflow-2) to learn about important differences to
consider when using AI Platform Training with TensorFlow 2, compared to
TensorFlow 1.

Runtime version 2.1 is also the first runtime version _not_ to support Python
2.7. The Python Software Foundation ended support for Python 2.7 on January 1,
2020. No AI Platform runtime versions released after January 1, 2020 support
Python 2.7.

Runtime version 2.1 also updates many other dependencies; see the [ runtime
version list ](https://cloud.google.com/ai-platform/training/docs/runtime-
version-list) for more details.

**ISSUE:**

[ Runtime version 2.1 ](https://cloud.google.com/ai-
platform/training/docs/runtime-version-list) includes scikit-learn 0.22 rather
than 0.22.1. This is a known issue, and the release notes will be updated when
runtime version 2.1 includes scikit-learn 0.22.1.

**FEATURE:**

When you train with runtime version 2.1 or later, AI Platform Training uses
the ` chief ` task name to represent the master VM in the [ ` TF_CONFIG `
environment variable ](https://cloud.google.com/ai-
platform/training/docs/distributed-training-details#chief-versus-master/) .
This environment variable is important for distributed training with
TensorFlow. For runtime version 1.15 and earlier, AI Platform Training uses
the ` master ` task name instead, but this task name is not supported in
TensorFlow 2.

However, by default, AI Platform Training continues to use the ` master ` task
name in [ custom container training jobs ](https://cloud.google.com/ai-
platform/training/docs/distributed-training-containers) . If you are
performing multi-worker distributed training with TensorFlow 2 in a custom
container, set the new [ ` trainingInput.useChiefInTfConfig `
](https://cloud.google.com/ai-
platform/training/docs/reference/rest/v1/projects.jobs#traininginput) field to
` true ` when you create a custom container training job in order to use the `
chief ` task name.

[ Learn more about this change. ](https://cloud.google.com/ai-
platform/training/docs/distributed-training-details#chief-versus-master)

**Cloud Composer**

**FEATURE:**

You can now control access to the Airflow web server, either allowing access
from any IP address (default), or specifying which IP ranges have access. For
details, see [ Creating environments
](https://cloud.google.com/composer/docs/how-
to/managing/creating#creating_a_new_environment) .

##  March 06, 2020

**AI Platform Training**

**CHANGED:**

The [ built-in linear learner algorithm ](https://cloud.google.com/ai-
platform/training/docs/algorithms/linear-learner) and the [ built-in wide and
deep algorithm ](https://cloud.google.com/ai-
platform/training/docs/algorithms/wide-and-deep) now use TensorFlow 1.14 for
training. They previously used TensorFlow 1.12.

The [ single-replica version of the built-in XGBoost algorithm
](https://cloud.google.com/ai-platform/training/docs/algorithms/xgboost) now
uses XGBoost 0.81 for training. It previously used XGBoost 0.80.

**App Engine flexible environment .NET**

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

**App Engine flexible environment Go**

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

**App Engine flexible environment Java**

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

**App Engine flexible environment Node.js**

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

**App Engine flexible environment PHP**

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

**App Engine flexible environment Python**

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

**App Engine flexible environment Ruby**

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

**App Engine standard environment Go**

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

**App Engine standard environment Java**

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

**App Engine standard environment Node.js**

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

**App Engine standard environment PHP**

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

**App Engine standard environment Python**

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

**App Engine standard environment Ruby**

**FEATURE:**

App Engine is now available in the ` us-west3 region ` (Salt Lake City, Utah).

##  March 05, 2020

**AI Platform Pipelines**

**FEATURE:**

[ AI Platform Pipelines ](https://cloud.google.com/ai-
platform/pipelines/docs/) is now available in beta. AI Platform Pipelines
makes it easier to get started with MLOps by saving you the difficulty of
setting up Kubeflow Pipelines with TensorFlow Extended (TFX). [ Kubeflow
Pipelines ](https://www.kubeflow.org/docs/pipelines/overview/pipelines-
overview/) is an open source platform for running, monitoring, auditing, and
managing machine learning (ML) pipelines on Kubernetes. [ TFX
](https://www.tensorflow.org/tfx) is an open source project for building ML
pipelines that orchestrate end-to-end ML workflows.

  * [ Get started with AI Platform Pipelines ](https://cloud.google.com/ai-platform/pipelines/docs/getting-started) . 
  * Learn more about [ AI Platform Pipelines and ML pipelines ](https://cloud.google.com/ai-platform/pipelines/docs/introduction) . 
  * [ Orchestrate your ML process as a pipeline ](https://cloud.google.com/ai-platform/pipelines/docs/create-pipeline) . 

**App Engine standard environment Python**

**CHANGED:**

Updated Python SDK to version 1.9.89.

**Cloud Identity and Access Management**

**FEATURE:**

For Cloud Storage buckets, you can now use [ Credential Access Boundaries
](https://cloud.google.com/iam/docs/downscoping-short-lived-credentials) ,
currently in beta, to downscope the permissions that a short-lived credential
can use.

**Cloud Key Management Service**

**FEATURE:**

Cloud EKM resources are now available in the ` asia-northeast3 ` and ` us-
west3 ` [ locations ](https://cloud.google.com/kms/docs/locations) .

**Cloud Spanner**

**FEATURE:**

Foreign keys is now [ generally available
](https://cloud.google.com/terms/launch-stages) . For more information, see [
Foreign keys overview ](https://cloud.google.com/spanner/docs/foreign-
keys/overview) .

**Speech-to-Text**

**FEATURE:**

Cloud Speech-to-Text now supports seven new [ languages
](https://cloud.google.com/speech-to-text/docs/languages) : Burmese, Estonian,
Uzbek, Punjabi, Albanian, Macedonian, and Mongolian.

**FEATURE:**

The [ speaker diarization ](https://cloud.google.com/speech-to-
text/docs/multiple-voices) , [ automatic punctuation
](https://cloud.google.com/speech-to-text/docs/automatic-punctuation) , [
speech adaptation boost ](https://cloud.google.com/speech-to-text/docs/boost)
, and [ enhanced telephony model ](https://cloud.google.com/speech-to-
text/docs/enhanced-models) features are now available for new languages. See
the supported [ languages page ](https://cloud.google.com/speech-to-
text/docs/languages) for a complete list.

**CHANGED:**

[ Class tokens ](https://cloud.google.com/speech-to-text/docs/class-tokens)
are now available for general use. You can use class tokens with [ speech
adaptation ](https://cloud.google.com/speech-to-text/docs/speech-
adaptation#classes) to help the model recognize concepts in your recorded
audio data.

##  March 04, 2020

**Binary Authorization**

**DEPRECATED:**

Support for the Binary Authorization Beta API was discontinued on September
16, 2019. As a result, **the Binary Authorization Beta API will stop working
after March 16, 2020.** To prevent service interruption, you must take actions
outlined in the [ Binary Authorization GA Migration Guide
](https://cloud.google.com/binary-authorization/docs/ga-migration-guide) prior
to that date.

