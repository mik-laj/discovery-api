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

##  July 07, 2020

**Cloud Composer**

**CHANGED:**

  * [ New versions ](https://cloud.google.com/composer/docs/concepts/versioning/composer-versions) of Cloud Composer images: ` composer-1.10.6-airflow-1.10.2 ` , ` composer-1.10.6-airflow-1.10.3 ` and ` composer-1.10.6-airflow-1.10.6 ` . The default is ` composer-1.10.6-airflow-1.10.3 ` . Upgrade your Cloud SDK to use features in this release. 

  * **For Airflow 1.10.6 and later:** The Airflow config property ` [celery] pool ` is now blocked. 

**FIXED:**

  * Fixed an issue with Airflow 1.10.6 environments where task logs were not visible in the UI when DAG serialization was enabled. 

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

##  June 22, 2020

**Anthos Service Mesh**

**FIXED:**

**1.5.6-asm.0 and 1.4.10.asm.2**

Contains the same fixes as OSS Istio 1.5.6. Non-critical, minor improvements
were also backported to ASM 1.4.10. See [ Announcing Istio 1.5.6
](https://istio.io/latest/news/releases/1.5.x/announcing-1.5.6/) for more
information.

**Cloud Build**

**FEATURE:**

Cloud Build's substitution variables can now refer to other substitution
variables, manipulate them using bash-style string operations, and pull
information from a trigger event payload. To learn more, see [ Using bash-
style string operations and payload bindings in substitutions
](http://cloud.google.com/cloud-build/docs/configuring-builds/use-bash-and-
bindings-in-substitutions) .

**Cloud Key Management Service**

**FEATURE:**

Keys hosted by [ Thales
](https://thalesdocs.com/dpod/services/key_management_services/ekms/ekms_setup_guide/)
are now supported in Cloud EKM. To learn more, see [ Cloud EKM
](https://cloud.google.com/kms/docs/ekm) .

**Compute Engine**

**FEATURE:**

N2D machine types are now available in Belgium, europe-west1, in all three
zones. Read more information on the [ VM instance pricing
](https://cloud.google.com/compute/vm-instance-pricing#n2d_machine_types)
page.

**Firestore**

**FEATURE:**

The Google Cloud console now includes a [ Firestore usage dashboard
](https://cloud.google.com/firestore/docs/monitor-usage) .

**Identity and Access Management**

**DEPRECATED:**

Using the Cloud IAM API to sign JSON Web Tokens (JWTs) or binary blobs is now
deprecated.

  * If you use the Cloud IAM API or its client libraries to sign JWTs or binary blobs, you must [ migrate to the Service Account Credentials API ](https://cloud.google.com/iam/docs/migrating-to-credentials-api) before July 1, 2021. 
  * If you use the ` gcloud ` command-line tool to sign JWTs, you must [ prepare for changes to the ` gcloud ` tool ](https://cloud.google.com/iam/docs/migrating-to-credentials-api#gcloud) before July 1, 2021. 

##  June 19, 2020

**Cloud Data Loss Prevention**

**FEATURE:**

Added support for location-based processing. Learn more:

  * [ Cloud DLP locations ](https://cloud.google.com/dlp/docs/locations)
  * [ Specifying processing locations ](https://cloud.google.com/dlp/docs/specifying-location)

**Cloud Functions**

**FEATURE:**

Cloud Functions is now available in the following regions:

  * ` australia-southeast1 ` (Sydney) 
  * ` northamerica-northeast1 ` (Montreal) 

See [ Cloud Functions Locations
](https://cloud.google.com/functions/docs/locations) for details.

**Cloud Run for Anthos**

**FEATURE:**

Cloud Run for Anthos on Google Cloud version [ 0.14.0-gke.5
](https://github.com/knative/serving/releases/tag/v0.14.0) is now available
for following cluster versions (and greater):

  * 1.17.6-gke.4 

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

**Compute Engine**

**FEATURE:**

[ New sole-tenant node types (c2-node-60-240, n1-node-96-1433, and
n2d-node-224-896) ](https://cloud.google.com/compute/docs/nodes#node_types)
are available in **Beta** .

**Resource Manager**

**FEATURE:**

The Organization Policy for [ restricting peer IP addresses through a Cloud
VPN tunnel ](https://cloud.google.com/network-
connectivity/docs/vpn/concepts/overview#vpn-org-policy) has been launched into
general availability.

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

