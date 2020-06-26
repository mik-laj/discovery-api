#  Release notes

This page documents production updates to Config Connector. Check this page
for announcements about new or updated features, bug fixes, known issues, and
deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google
Cloud release notes ](/release-notes) page.

To get the latest product updates delivered to you, add the URL of this page
to your [ feed reader
](https://wikipedia.org/wiki/Comparison_of_feed_aggregators) , or add the feed
URL directly: ` https://cloud.google.com/feeds/configconnector-release-
notes.xml `

##  June 25, 2020

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

##  June 16, 2020

**FEATURE:**

You can use ` config-connector ` tool to export Google Cloud resources into
Config Connector: [ documentation ](https://cloud.google.com/config-
connector/docs/how-to/importing-existing-resources)

**FIXED:**

Bug fixes

##  June 12, 2020

**FEATURE:**

  * Added ability to [ update streaming DataflowJobs ](https://cloud.google.com/dataflow/docs/guides/updating-a-pipeline) by updating its spec (e.g. ` spec.templateGcsPath ` ). Note that not all fields can be updated, and batch DataflowJobs don't support updates. 
  * Added ` IAMPolicy ` to the output of ` config-connector `

##  June 03, 2020

**CHANGED:**

Miscellaneous bug fixes and improvements

##  May 29, 2020

**CHANGED:**

Added support for ` SQLSSLCert `

**CHANGED:**

Supported acquisition of backends added to Compute Backend Services out-of-
band of Config Connector

**FIXED:**

Fixed support for [ autoscaling and manually resizing node pools with
ContainerNodePool ](https://github.com/GoogleCloudPlatform/k8s-config-
connector/issues/165)

##  May 27, 2020

**CHANGED:**

Added support for ` BigQueryJob ` resource

##  May 19, 2020

**FIXED:**

Bug fixes and reliability improvements

**FIXED:**

Improving handling of scenarios when ` version ` field on ` ContainerNodePool
` is updated externally

##  May 15, 2020

**FIXED:**

fix ContainerNodePool version upgrade scenario

**CHANGED:**

increase the cpu/memory request for webhook and recorder

**CHANGED:**

Miscellaneous bug fixes and improvement

##  April 30, 2020

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

##  April 21, 2020

**CHANGED:**

Miscellaneous bug fixes and improvements

##  April 14, 2020

**CHANGED:**

Added readiness probes to Config Connector pods

##  April 10, 2020

**FEATURE:**

Add the CloudBuildTrigger resource

Add the SourceRepoRepository resource

**CHANGED:**

miscellaneous bug fixes and improvements

##  April 02, 2020

**FIXED:**

Fixed the [ ComputeInstance idempotency issue
](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/103)

##  March 25, 2020

**FEATURE:**

Add "Deletion Defender" workload -- a pod whose job is to ensure that only
resources meant to trigger a delete on the underlying API do so. If this
workload goes down for whatever reason, the controller is prevented from
performing deletions, thus protecting against accidental deletions in the case
of cascading deletions prompted by uninstalling CRDs.

**FEATURE:**

Add support for structured metadata list for ComputeInstance and
ComputeInstanceTemplate in the form of a spec.metadata field.

##  March 23, 2020

**FIXED:**

Fixed label update issue on ContainerCluster
(https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/110)

**CHANGED:**

Bumped memory request and limit for the manager pod as resource usage has gone
up and the original limit of 256 Mi was found to not be sufficient for large
customers

**CHANGED:**

Changed admission webhooks to return non-200 error codes when denying
admission

##  March 18, 2020

**CHANGED:**

miscellaneous bug fixes and improvements

##  March 10, 2020

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

##  February 26, 2020

**FEATURE:**

Added support for ` DataflowJob ` resource

##  February 21, 2020

**FEATURE:**

Added support for ` ComputeNetworkEndpointGroup ` resource

##  February 17, 2020

**FEATURE:**

Added support for ` DNSPolicy ` resource

##  February 09, 2020

**FEATURE:**

Added support for ` ComputeResourcePolicy ` resource

##  January 23, 2020

**FEATURE:**

Config Connector has reached [ General Availability (GA)
](https://cloud.google.com/products/#product-launch-stages) .

**FEATURE:**

Config Connector now supports configuring GCP resources with sensitive data in
GKE Secrets.

**FEATURE:**

Config connector now supports authenticating to multiple Google Service
Accounts using different Kubernetes Service accounts in your Config Connector
cluster using [ Namespaced mode ](https://cloud.google.com/config-
connector/docs/how-to/install-upgrade-
uninstall#choosing_your_installation_method) .

**FEATURE:**

Some Config Connector resources now support directives, which allow Config
Connector to take additional actions beyond creating or deleting resources.
For more information, see [ Resources ](https://cloud.google.com/config-
connector/docs/concepts/resources#directives)

##  January 09, 2020

**FEATURE:**

Added support for ` DNSRecordSet ` , ` Project ` and ` ServiceUsage `
resources

##  January 02, 2020

**FEATURE:**

Added external resource reference support for ` IAMPolicy ` and `
IAMPolicyMember `

**FEATURE:**

Improved initial Prometheus metrics

##  December 23, 2019

**FEATURE:**

Add support for ComputeNodeTemplate

**FEATURE:**

Add initial support for exporting prometheus metrics

**CHANGED:**

No longer run system components as root

**CHANGED:**

Add a specific ResourceReference structure to IAMPolicy and IAMPolicyMember

##  December 17, 2019

**FEATURE:**

Added the ` external ` field to support the external resource references

**FEATURE:**

Added support for ComputeTargetTCPProxy

##  December 12, 2019

**FEATURE:**

Added support for SpannerDatabase

##  November 26, 2019

**FEATURE:**

Added support for ServiceNetworkingConnection and ComputeTargetHTTPSProxy

##  November 21, 2019

**FEATURE:**

Added support for ComputeInterconnectAttachment, ComputeSSLProxy,
ComputeTargetSSLProxy, (Regional)ComputeDisk

##  November 06, 2019

**FEATURE:**

Added support for FirestoreIndex, ComputeRouterInterface, ComputeRoute,
ComputeRouterPeer

##  November 01, 2019

**FEATURE:**

New resources supported: IAMPolicyMember, BigQueryTable, ComputeVPNTunnel,
ComputeImage, ComputeSnapshot, ComputeBackendBucket, ComputeDisk,
ComputeSSLCertificate, ComputeHTTPHealthCheck, ComputeRouterNAT,
ComputeExternalVPNGateway, ComputeRouter, ComputeVPNTunnel, DNSManagedZone,
StorageNotification

**BREAKING:**

Breaking namespace changes for the following resources: \-
GlobalComputeAddress: v1alpha2->v2apha3 \- ComputeNetwork: v1alpha2->v1alpha3
\- ComputeSubnetwork: v1alpha2->v1alpha3 \- ComputeBackendService:
v1alpha2->v1alpha3 \- ComputeHealthCheck: v1alpha2->v1alpha3 \-
ComputeFirewall: v1alpha2->v1alpha3

##  October 22, 2019

**FEATURE:**

Added new resources and [ samples
](https://github.com/GoogleCloudPlatform/k8s-config-
connector/tree/master/samples) for BigQueryTable, ComputeExternalVPNGateway

##  October 15, 2019

**CHANGED:**

Bump compute api group version to v1alpha2

  * rename ComputeGlobalForwardingRule to ComputeForwardingRule 
  * add required location field to the following existing resources: ComputeAddress, ComputeBackendService, ComputeForwardingRule, ComputeHealthCheck, ComputeTargetHttpProxy, ComputeURLMap 
  * ComputeAddress CRD now supports both global and regional compute addresses 

**FEATURE:**

Add the following new resources with [ samples
](https://github.com/GoogleCloudPlatform/k8s-config-
connector/tree/master/samples) : ComputeNetworkPeering,
ComputeTargetVPNGateway, ComputeVpnGateway, IAMCustomRole,
ComputeHTTPSHealthCheck, ComputeSharedVPCHostProject, ComputeRouter

##  October 08, 2019

**CHANGED:**

New ` gcp ` category in CRDs, so you can view Config Connector resources via `
kubectl get gcp `

##  September 30, 2019

**FEATURE:**

Config Connector now supports GKE [ workload identity
](https://cloud.google.com/config-connector/docs/how-to/install-upgrade-
uninstall#choosing_your_installation_method)

**FEATURE:**

Added the ContainerNodePool resource

##  September 20, 2019

**FEATURE:**

Adding ComputeGlobalForwardingRule resource and examples

##  September 13, 2019

**FIXED:**

Fixed an issue with creating service account keys across projects.

##  September 09, 2019

**CHANGED:**

Update samples for version 0.1.2

##  September 03, 2019

**FEATURE:**

Added ComputeTargetHTTPProxy, ComputeBackendService, ComputeFirewall,
ComputeUrlMap resources

**CHANGED:**

Samples updates for newly added resources, as well bigtablecluster,
bigtableinstance, iampolicy

##  August 16, 2019

**FEATURE:**

Config Connector v0.1.1 is now available in Beta.

